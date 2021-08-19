import random
from collections import OrderedDict

from hearthstone.enums import (
	BlockType, CardClass, CardType, Mulligan, PlayState, Step, Zone, GameTag
)

from .dsl import LazyNum, LazyValue, Selector
from .entity import Entity
from .exceptions import InvalidAction
from .logging import log
from .utils import random_class


def _eval_card(source, card):
	"""
	Return a Card instance from \a card
	The card argument can be:
	- A Card instance (nothing is done)
	- The string ID of the card (the card is created)
	- A LazyValue (the card is dynamically created)
	- A Selector (take entity lists and returns a sub-list)
	"""
	if isinstance(card, LazyValue):
		card = card.evaluate(source)

	if isinstance(card, Action):
		card = card.trigger(source)[0]

	if isinstance(card, Selector):
		card = card.eval(source.game, source)

	if not isinstance(card, list):
		cards = [card]
	else:
		cards = card

	ret = []
	for card in cards:
		if isinstance(card, str):
			ret.append(source.controller.card(card, source))
		else:
			ret.append(card)

	return ret


class EventListener:
	ON = 1
	AFTER = 2

	def __init__(self, trigger, actions, at):
		self.trigger = trigger
		self.actions = actions
		self.at = at
		self.once = False

	def __repr__(self):
		return "<EventListener %r>" % (self.trigger)


class ActionMeta(type):
	def __new__(metacls, name, bases, namespace):
		cls = type.__new__(metacls, name, bases, dict(namespace))
		argslist = []
		for k, v in namespace.items():
			if not isinstance(v, ActionArg):
				continue
			v._setup(len(argslist), k, cls)
			argslist.append(v)
		cls.ARGS = tuple(argslist)
		return cls

	@classmethod
	def __prepare__(metacls, name, bases):
		return OrderedDict()


class ActionArg(LazyValue):
	def _setup(self, index, name, owner):
		self.index = index
		self.name = name
		self.owner = owner

	def __repr__(self):
		return "<%s.%s>" % (self.owner.__name__, self.name)

	def evaluate(self, source):
		# This is used when an event listener triggers and the callback
		# Action has arguments of the type Action.FOO
		# XXX we rely on source.event_args to be set, but it's very racey.
		# If multiple events happen on an entity at once, stuff will go wrong.
		if source.event_args == None:## add it to avoid the interruption.
			return []
		assert source.event_args
		return source.event_args[self.index]


class CardArg(ActionArg):
	# Type hint
	pass


class IntArg(ActionArg, LazyNum):
	def evaluate(self, source):
		ret = super().evaluate(source)
		return self.num(ret)


class Action(metaclass=ActionMeta):
	def __init__(self, *args, **kwargs):
		self._args = args
		self._kwargs = kwargs
		self.callback = ()
		self.times = 1
		self.event_queue = []

	def __repr__(self):
		args = ["%s=%r" % (k, v) for k, v in zip(self.ARGS, self._args)]
		return "<Action: %s(%s)>" % (self.__class__.__name__, ", ".join(args))

	def after(self, *actions):
		return EventListener(self, actions, EventListener.AFTER)

	def on(self, *actions):
		return EventListener(self, actions, EventListener.ON)

	def then(self, *args):
		"""
		Create a callback containing an action queue, called upon the
		action's trigger with the action's arguments available.
		"""
		ret = self.__class__(*self._args, **self._kwargs)
		ret.callback = args
		ret.times = self.times
		return ret

	def _broadcast(self, entity, source, at, *args):
		for event in entity.events:
			if event.at != at:
				continue
			if isinstance(event.trigger, self.__class__) and event.trigger.matches(entity, args):
				log.info("%r triggers off %r from %r", entity, self, source)
				entity.trigger_event(source, event, args)
	def broadcast(self, source, at, *args):
		for entity in source.game.entities:
			self._broadcast(entity, source, at, *args)

		for hand in source.game.hands:
			for entity in hand.entities:
				self._broadcast(entity, source, at, *args)

	def queue_broadcast(self, obj, args):
		self.event_queue.append((obj, args))

	def resolve_broadcasts(self):
		for obj, args in self.event_queue:
			obj.broadcast(*args)
		self.event_queue = []

	def get_args(self, source):
		return self._args

	def matches(self, source, args):
		for arg, match in zip(args, self._args):
			if match is None:
				# Allow matching Action(None, None, z) to Action(x, y, z)
				continue
			if arg is None:
				# We got an arg of None and a match not None. Bad.
				return False
			if callable(match):
				res = match(arg)
				if not res:
					return False
			else:
				# this stuff is stupidslow
				res = match.eval([arg], source)
				if not res or res[0] is not arg:
					return False
		return True


class GameAction(Action):
	def trigger(self, source):
		args = self.get_args(source)
		self.do(source, *args)


class Attack(GameAction):
	"""
	Make \a ATTACKER attack \a DEFENDER
	"""
	ATTACKER = ActionArg()
	DEFENDER = ActionArg()

	def get_args(self, source):
		attacker = _eval_card(source, self._args[0])[0]
		try:
			defender = _eval_card(source, self._args[1])[0]
		except IndexError as e:## annihilation in procedure
			defender = None
		return attacker, defender

	def do(self, source, attacker, defender):
		log.info("%r attacks %r", attacker, defender)
		if not defender:
			return
		attacker.attack_target = defender
		defender.defending = True
		source.game.proposed_attacker = attacker
		source.game.proposed_defender = defender
		source.game.manager.step(Step.MAIN_COMBAT, Step.MAIN_ACTION)
		source.game.refresh_auras()  # XXX Needed for Gorehowl
		self.broadcast(source, EventListener.ON, attacker, defender)

		defender = source.game.proposed_defender
		source.game.proposed_attacker = None
		source.game.proposed_defender = None
		if attacker.should_exit_combat:
			log.info("Attack has been interrupted.")
			attacker.attack_target = None
			defender.defending = False
			return

		assert attacker is not defender, "Why are you hitting yourself %r?" % (attacker)

		# Save the attacker/defender atk values in case they change during the attack
		# (eg. in case of Enrage)
		def_atk = defender.atk
		source.game.queue_actions(attacker, [Hit(defender, attacker.atk)])
		if def_atk:
			source.game.queue_actions(defender, [Hit(attacker, def_atk)])

		self.broadcast(source, EventListener.AFTER, attacker, defender)

		attacker.attack_target = None
		defender.defending = False
		attacker.num_attacks += 1


class BeginTurn(GameAction):
	"""
	Make \a player begin the turn
	"""
	PLAYER = ActionArg()

	def do(self, source, player):
		source.manager.step(source.next_step, Step.MAIN_READY)
		source.turn += 1
		source.log("%s begins turn %i", player, source.turn)
		source.current_player = player
		source.manager.step(source.next_step, Step.MAIN_START_TRIGGERS)
		source.manager.step(source.next_step, source.next_step)
		self.broadcast(source, EventListener.ON, player)
		source._begin_turn(player)
		player.times_spells_played_this_turn = 0 # aharalab #DAL_603
		player.spells_played_this_turn=[] # aharalab #DAL_558

class Concede(GameAction):
	"""
	Make \a player concede
	"""
	PLAYER = ActionArg()

	def do(self, source, player):
		player.playstate = PlayState.CONCEDED
		source.game.check_for_end_game()


class Disconnect(GameAction):
	"""
	Make \a player disconnect
	"""
	PLAYER = ActionArg()

	def do(self, source, player):
		player.playstate = PlayState.DISCONNECTED


class Deaths(GameAction):
	"""
	Process all deaths in the PLAY Zone.
	"""
	def do(self, source, *args):
		source.game.process_deaths()


class Death(GameAction):
	"""
	Move target to the GRAVEYARD Zone.
	"""
	ENTITY = ActionArg()

	def do(self, source, target):
		log.info("Processing Death for %r", target)
		self.broadcast(source, EventListener.ON, target)
		if target.deathrattles:
			source.game.queue_actions(source, [Deathrattle(target)])
		if target.reborn:# aharalab
			source.game.queue_actions(source, [Reborn(target)])
		if target.id== 'DRG_253':# aharalab for Dwarven Sharpshooter
			ChangeHeroPower(target.controller, "HERO_05bp").trigger(target)

class EndTurn(GameAction):
	"""
	End the current turn
	"""
	PLAYER = ActionArg()

	def do(self, source, player):
		if player.choice:
			raise InvalidAction(
				"%r cannot end turn with the open choice %r." % (player, player.choice)
			)
		self.broadcast(source, EventListener.ON, player)
		source.game._end_turn()


class Joust(GameAction):
	"""
	Perform a joust between \a challenger and \a defender.
	Note that this does not evaluate the results of the joust. For that,
	see dsl.evaluators.JoustEvaluator.
	"""
	CHALLENGER = ActionArg()
	DEFENDER = ActionArg()

	def get_args(self, source):
		challenger = self._args[0].eval(source.game, source)
		defender = self._args[1].eval(source.game, source)
		return challenger and challenger[0], defender and defender[0]

	def do(self, source, challenger, defender):
		log.info("Jousting %r vs %r", challenger, defender)
		source.game.joust(source, challenger, defender, self.callback)


class Choice(GameAction):
	PLAYER = ActionArg()
	CARDS = ActionArg()
	CARD = ActionArg()

	def get_args(self, source):
		player = self._args[0]
		if isinstance(player, Selector):
			player = player.eval(source.game.players, source)
			assert len(player) == 1
			player = player[0]
		cards = self._args[1]
		if isinstance(cards, Selector):
			cards = cards.eval(source.game, source)
		elif isinstance(cards, LazyValue):
			cards = cards.evaluate(source)
		elif isinstance(cards, list):
			eval_cards = []
			for card in cards:
				if isinstance(card, LazyValue):
					eval_cards.append(card.evaluate(source)[0])
				else:
					eval_cards.append(card)
			cards = eval_cards

		return player, cards

	def do(self, source, player, cards):
		if len(cards) == 0:
			return
		log.info("%r choice from %r", player, cards)
		self.next_choice = player.choice
		player.choice = self
		self.source = source
		self.player = player
		self.cards = cards
		self.min_count = 1
		self.max_count = 1

	def choose(self, card):
		if card not in self.cards:
			raise InvalidAction("%r is not a valid choice (one of %r)" % (card, self.cards))
		for action in self.callback:
			self.source.game.trigger(
				self.source, [action], [self.player, self.cards, card])
		self.player.choice = self.next_choice

class GenericChoice(Choice):
	def choose(self, card):
		super().choose(card)
		for _card in self.cards:
			if _card is card:
				if card.type == CardType.HERO_POWER:
					_card.zone = Zone.PLAY
				elif len(self.player.hand) < self.player.max_hand_size:
					_card.zone = Zone.HAND
				else:
					_card.discard()
			else:
				_card.discard()


class MulliganChoice(GameAction):
	PLAYER = ActionArg()

	def __init__(self, *args, callback):
		super().__init__(*args)
		self.callback = callback

	def do(self, source, player):
		player.mulligan_state = Mulligan.INPUT
		player.choice = self
		# NOTE: Ideally, we give The Coin when the Mulligan is over.
		# Unfortunately, that's not compatible with Blizzard's way.
		self.cards = player.hand.exclude(id="GAME_005")
		self.source = source
		self.player = player
		self.min_count = 0
		# but weirdly, the game server includes the coin in the mulligan count
		self.max_count = len(player.hand)

	def choose(self, *cards):
		self.player.max_hand_size=20#loose the limitter temporarily
		self.player.draw(len(cards))
		for card in cards:
			assert card in self.cards
			card.zone = Zone.DECK
		self.player.choice = None
		self.player.shuffle_deck()
		self.player.max_hand_size=10
		self.player.mulligan_state = Mulligan.DONE

		if self.player.opponent.mulligan_state == Mulligan.DONE:
			self.callback()


class Play(GameAction):
	"""
	Make the source player play \a card, on \a target or None.
	Choose play action from \a choose or None.
	"""
	PLAYER = ActionArg()
	CARD = CardArg()
	TARGET = ActionArg()
	INDEX = IntArg()
	CHOOSE = ActionArg()

	def _broadcast(self, entity, source, at, *args):
		# Prevent cards from triggering off their own play
		if entity is args[1]:
			return
		return super()._broadcast(entity, source, at, *args)

	def do(self, source, card, target, index, choose):
		player = source
		log.info("%s plays %r (target=%r, index=%r)", player, card, target, index)

		player.pay_cost(card, card.cost)

		card.target = target
		card._summon_index = index

		battlecry_card = choose or card
		# We check whether the battlecry will trigger, before the card.zone changes
		if battlecry_card.battlecry_requires_target() and not target:
			log.info("%r requires a target for its battlecry. Will not trigger.")
			trigger_battlecry = False
		else:
			trigger_battlecry = True

		if card is card.controller.hand[0] or card is card.controller.hand[-1]:
			trigger_outcast = True
		else:
			trigger_outcast = False

		card.zone = Zone.PLAY

		# Remember cast on friendly characters
		if target and target.controller == source:
			card.cast_on_friendly_characters = True

		# NOTE: A Play is not a summon! But it sure looks like one.
		# We need to fake a Summon broadcast.
		summon_action = Summon(player, card)

		if card.type in (CardType.MINION, CardType.WEAPON):
			self.queue_broadcast(summon_action, (player, EventListener.ON, player, card))
		self.broadcast(player, EventListener.ON, player, card, target)
		self.resolve_broadcasts()

		# "Can't Play" (aka Counter) means triggers don't happen either
		if not card.cant_play:
			if trigger_outcast and card.get_actions("outcast"):
				source.game.trigger(card, card.get_actions("outcast"), event_args=None)
			elif trigger_battlecry:
				source.game.queue_actions(card, [Battlecry(battlecry_card, card.target)])

			# If the play action transforms the card (eg. Druid of the Claw), we
			# have to broadcast the morph result as minion instead.
			played_card = card.morphed or card
			if played_card.type in (CardType.MINION, CardType.WEAPON):
				summon_action.broadcast(player, EventListener.AFTER, player, played_card)
			self.broadcast(player, EventListener.AFTER, player, played_card, target)

		player.combo = True
		player.last_card_played = card
		player.cards_played_this_turn += 1
		if card.type == CardType.MINION:
			player.minions_played_this_turn += 1

		card.target = None
		card.choose = None


class Activate(GameAction):
	PLAYER = ActionArg()
	CARD = CardArg()
	TARGET = ActionArg()

	def get_args(self, source):
		return (source, ) + super().get_args(source)

	def do(self, source, player, heropower, target=None):
		player.pay_cost(heropower, heropower.cost)
		self.broadcast(source, EventListener.ON, player, heropower, target)

		actions = heropower.get_actions("activate")
		source.game.action_start(BlockType.PLAY, heropower, 0, target)
		source.game.main_power(heropower, actions, target)
		source.game.action_end(BlockType.PLAY, heropower)

		for entity in player.live_entities:
			if not entity.ignore_scripts:
				actions = entity.get_actions("inspire")
				if actions:
					source.game.trigger(entity, actions, event_args=None)

		heropower.activations_this_turn += 1


class Overload(GameAction):
	PLAYER = ActionArg()
	AMOUNT = IntArg()

	def do(self, source, player, amount):
		if player.cant_overload:
			log.info("%r cannot overload %s", source, player)
			return
		log.info("%r overloads %s for %i", source, player, amount)
		self.broadcast(source, EventListener.ON, player, amount)
		player.overloaded += amount


class TargetedAction(Action):
	TARGET = ActionArg()

	def __init__(self, *args, **kwargs):
		self.source = kwargs.pop("source", None)
		super().__init__(*args, **kwargs)
		self.trigger_index = 0

	def __repr__(self):
		args = ["%s=%r" % (k, v) for k, v in zip(self.ARGS[1:], self._args[1:])]
		return "<TargetedAction: %s(%s)>" % (self.__class__.__name__, ", ".join(args))

	def __mul__(self, value):
		self.times = value
		return self

	def eval(self, selector, source):
		if isinstance(selector, Entity):
			return [selector]
		else:
			return selector.eval(source.game, source)

	def get_target_args(self, source, target):
		ret = []
		for k, v in zip(self.ARGS[1:], self._args[1:]):
			if isinstance(v, Selector):
				# evaluate Selector arguments
				v = v.eval(source.game, source)
			elif isinstance(v, LazyValue):
				v = v.evaluate(source)
			elif isinstance(k, CardArg):
				v = _eval_card(source, v)
			ret.append(v)
		return ret

	def get_targets(self, source, t):
		if isinstance(t, Entity):
			ret = t
		elif isinstance(t, LazyValue):
			ret = t.evaluate(source)
		else:
			ret = t.eval(source.game, source)
		if not ret:
			return []
		if not hasattr(ret, "__iter__"):
			# Bit of a hack to ensure we always get a list back
			ret = [ret]
		return ret

	def trigger(self, source):
		ret = []

		if self.source is not None:
			source = self.source.eval(source.game, source)
			assert len(source) == 1
			source = source[0]

		times = self.times
		if isinstance(times, LazyValue):
			times = times.evaluate(source)
		elif isinstance(times, Action):
			times = times.trigger(source)[0]

		for i in range(times):
			self.trigger_index = i
			args = self.get_args(source)
			targets = self.get_targets(source, args[0])
			args = args[1:]
			log.info("%r triggering %r targeting %r", source, self, targets)
			for target in targets:
				target_args = self.get_target_args(source, target)
				ret.append(self.do(source, target, *target_args))

				for action in self.callback:
					log.info("%r queues up callback %r", self, action)
					ret += source.game.queue_actions(source, [action], event_args=[target] + target_args)

		self.resolve_broadcasts()

		return ret


class Buff(TargetedAction):
	"""
	Buff character targets with Enchantment \a id
	NOTE: Any Card can buff any other Card. The controller of the
	Card that buffs the target becomes the controller of the buff.
	"""
	TARGET = ActionArg()
	BUFF = ActionArg()

	def get_target_args(self, source, target):
		buff = self._args[1]
		buff = source.controller.card(buff)
		buff.source = source
		return [buff]

	def do(self, source, target, buff):
		kwargs = self._kwargs.copy()
		for k, v in kwargs.items():
			if isinstance(v, LazyValue):
				v = v.evaluate(source)
			setattr(buff, k, v)
		return buff.apply(target)

class EatsCard(TargetedAction):
	""" add other stats to target stats
	"""
	TARGET = ActionArg()
	OTHER = ActionArg()
	def do(self, source, target, other):
		if isinstance(other,list):
			other = other[0]
		if isinstance(target,list):
			target = target[0]
		target.atk += other.atk
		target.max_health += other.max_health
		log.info("ate %r from opponent's hand"%(other))
		log.info("%r gains +%d/+%d"%(target, other.atk,other.max_health))
		other.discard()
		pass

class Bounce(TargetedAction):
	"""
	Bounce minion targets on the field back into the hand.
	"""
	def do(self, source, target):
		if len(target.controller.hand) >= target.controller.max_hand_size:
			log.info("%r is bounced to a full hand and gets destroyed", target)
			return source.game.queue_actions(source, [Destroy(target)])
		else:
			log.info("%r is bounced back to %s's hand", target, target.controller)
			target.zone = Zone.HAND


class CopyDeathrattles(TargetedAction):
	"""
	Copy the deathrattles from a card onto the target
	"""
	TARGET = ActionArg()
	DEATHRATTLES = ActionArg()

	def do(self, source, target, entities):
		for entity in entities:
			for deathrattle in entity.deathrattles:
				target.additional_deathrattles.append(deathrattle)


class Counter(TargetedAction):
	"""
	Counter a card, making it unplayable.
	"""
	def do(self, source, target):
		target.cant_play = True


class Predamage(TargetedAction):
	"""
	Predamage target by \a amount.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def do(self, source, target, amount):
		for i in range(target.incoming_damage_multiplier):
			amount *= 2
		target.predamage = amount
		if amount:
			self.broadcast(source, EventListener.ON, target, amount)
			return source.game.trigger_actions(source, [Damage(target)])[0][0]
		return 0


class PutOnTop(TargetedAction):
	"""
	Put card on deck top
	"""
	TARGET = ActionArg()
	CARD = CardArg()

	def do(self, source, target, cards):
		log.info("%r put on %s's deck top", cards, target)
		if not isinstance(cards, list):
			cards = [cards]

		for card in cards:
			if card.controller != target:
				card.zone = Zone.SETASIDE
				card.controller = target
			if len(target.deck) >= target.max_deck_size:
				log.info("Put(%r) fails because %r's deck is full", card, target)
				continue
			card.zone = Zone.DECK
			card, card.controller.deck[-1] = card.controller.deck[-1], card


class Damage(TargetedAction):
	"""
	Damage target by \a amount.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def get_target_args(self, source, target):
		return [target.predamage]

	def do(self, source, target, amount):
		amount = target._hit(target.predamage)
		target.predamage = 0
		if source.type == CardType.MINION and source.stealthed:
			# TODO this should be an event listener of sorts
			source.stealthed = False
		if amount:
			# check hasattr: some sources of damage are game or player (like fatigue)
			# weapon damage itself after hero attack, but does not trigger lifesteal
			if hasattr(source, "lifesteal") and source.lifesteal and source.type != CardType.WEAPON:
				source.heal(source.controller.hero, amount)
			self.broadcast(source, EventListener.ON, target, amount, source)
			# poisonous can not destory hero
			if hasattr(source, "poisonous") and source.poisonous and (
				target.type != CardType.HERO and source.type != CardType.WEAPON):
				target.destroy()
		return amount


class Deathrattle(TargetedAction):
	"""
	Trigger deathrattles on card targets.
	"""
	def do(self, source, target):
		for deathrattle in target.deathrattles:
			if callable(deathrattle):
				actions = deathrattle(target)
			else:
				actions = deathrattle
			source.game.queue_actions(target, actions)

			if target.controller.extra_deathrattles:
				log.info("Triggering deathrattles for %r again", target)
				source.game.queue_actions(target, actions)


class Battlecry(TargetedAction):
	"""
	Trigger Battlecry on card targets
	"""
	CARD = CardArg()
	TARGET = ActionArg()

	def get_target_args(self, source, target):
		arg = self._args[1]
		if isinstance(arg, Selector):
			arg = arg.eval(source.game, source)
			assert len(arg) == 1
			arg = arg[0]
		return [arg]

	def do(self, source, card, target):
		player = card.controller

		if card.has_combo and player.combo:
			log.info("Activating %r combo targeting %r", card, target)
			actions = card.get_actions("combo")
		else:
			log.info("Activating %r action targeting %r", card, target)
			actions = card.get_actions("play")

		source.target = target
		source.game.main_power(source, actions, target)

		if player.extra_battlecries and card.has_battlecry:
			source.game.main_power(source, actions, target)

		if card.overload:
			source.game.queue_actions(card, [Overload(player, card.overload)])


class Destroy(TargetedAction):
	"""
	Destroy character targets.
	"""
	
	def do(self, source, target):
		if not target:
			return
		if target.delayed_destruction:
			#  If the card is in PLAY, it is instead scheduled to be destroyed
			# It will be moved to the graveyard on the next Death event
			log.info("%r marks %r for imminent death", source, target)
			target.to_be_destroyed = True
		else:
			log.info("%r destroys %r", source, target)
			if target.type == CardType.ENCHANTMENT:
				target.remove()
			else:
				target.zone = Zone.GRAVEYARD


class Discard(TargetedAction):
	"""
	Discard card targets in a player's hand
	"""
	TARGET = ActionArg()
	def do(self, source, target):
		self.broadcast(source, EventListener.ON, target)
		target.discard()


class Discover(TargetedAction):
	"""
	Opens a generic choice for three random cards matching a filter.
	"""
	TARGET = ActionArg()
	CARDS = CardArg()

	def get_target_args(self, source, target):
		if target.hero.data.card_class != CardClass.NEUTRAL:
			# use hero class for Discover if not neutral (eg. Ragnaros)
			discover_class = target.hero.data.card_class
		elif source.data.card_class != CardClass.NEUTRAL:
			# use card class for neutral hero classes
			discover_class = source.data.card_class
		else:
			# use random class for neutral hero classes with neutral cards
			discover_class = random_class()

		picker = self._args[1] * 3
		picker = picker.copy_with_weighting(1, card_class=CardClass.NEUTRAL)
		picker = picker.copy_with_weighting(4, card_class=discover_class)
		return [picker.evaluate(source)]

	def do(self, source, target, cards):
		log.info("%r discovers %r for %s", source, cards, target)
		source.game.queue_actions(source, [GenericChoice(target, cards)])


class Draw(TargetedAction):
	"""
	Make player targets draw a card from their deck.
	"""
	TARGET = ActionArg()
	CARD = CardArg()

	def get_target_args(self, source, target):
		if target.deck:
			card = target.deck[-1]
		else:
			card = None
		return [card]

	def do(self, source, target, card):
		if card is None:
			target.fatigue()
			return []
		card.draw()
		self.broadcast(source, EventListener.ON, target, card, source)

		return [card]


class Fatigue(TargetedAction):
	"""
	Hit a player with a tick of fatigue
	"""
	def do(self, source, target):
		if target.cant_fatigue:
			log.info("%s can't fatigue and does not take damage", target)
			return
		target.fatigue_counter += 1
		log.info("%s takes %i fatigue damage", target, target.fatigue_counter)
		return source.game.queue_actions(source, [Hit(target.hero, target.fatigue_counter)])


class ForceDraw(TargetedAction):
	"""
	Draw card targets into their owners hand
	"""
	TARGET = ActionArg()
	def do(self, source, target):
		if not hasattr(target, "__iter__"):
			target.draw()
		else:
			for tgt in target:
				if not hasattr(tgt, "__iter__"):
					tgt.draw()

class DrawUntil(TargetedAction):
	"""
	Make target player target draw up to \a amount cards minus their hand count.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def do(self, source, target, amount):
		if target not in target.game.players:
			raise InvalidAction("%r is not a player" % target)
		difference = max(0, amount - len(target.hand))
		if difference > 0:
			return source.game.queue_actions(source, [Draw(target) * difference])


class FullHeal(TargetedAction):
	"""
	Fully heal character targets.
	"""
	def do(self, source, target):
		source.heal(target, target.max_health)


class GainArmor(TargetedAction):
	"""
	Make hero targets gain \a amount armor.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def do(self, source, target, amount):
		target.armor += amount
		self.broadcast(source, EventListener.ON, target, amount)


class GainMana(TargetedAction):
	"""
	Give player targets \a Mana crystals.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def do(self, source, target, amount):
		target.max_mana = max(target.max_mana + amount, 0)


class SpendMana(TargetedAction):
	"""
	Make player targets spend \a amount Mana.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def do(self, source, target, amount):
		target.used_mana = max(target.used_mana + amount, 0)


class Give(TargetedAction):
	"""
	Give player targets card \a id.
	"""
	TARGET = ActionArg()
	CARD = CardArg()

	def do(self, source, target, cards):
		log.info("Giving %r to %s", cards, target)
		ret = []
		if not hasattr(cards, "__iter__"):
			# Support Give on multiple cards at once (eg. Echo of Medivh)
			cards = [cards]
		for card in cards:
			if len(target.hand) >= target.max_hand_size:
				log.info("Give(%r) fails because %r's hand is full", card, target)
				continue
			## when card==[]  ## added, 13/8/2021 
			if hasattr(card, "__iter__") and len(card)==0:
				break;
			## 
			card.controller = target
			card.zone = Zone.HAND
			# if drawn_card is 'casts_when_drawn' then immediately play.  by aharalab  19.12.2020
			if hasattr(card, "casts_when_drawn"):
				card.game.queue_actions(card.controller, [Play(card, None, None, None)])
			ret.append(card)
		return ret


class Hit(TargetedAction):
	"""
	Hit character targets by \a amount.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def do(self, source, target, amount):
		amount = source.get_damage(amount, target)
		if amount:
			return source.game.queue_actions(source, [Predamage(target, amount)])[0][0]
		return 0


class Heal(TargetedAction):
	"""
	Heal character targets by \a amount.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def do(self, source, target, amount):
		if source.controller.healing_as_damage:
			return source.game.queue_actions(source, [Hit(target, amount)])

		amount <<= source.controller.healing_double
		amount = min(amount, target.damage)
		if amount:
			# Undamaged targets do not receive heals
			log.info("%r heals %r for %i", source, target, amount)
			target.damage -= amount
			self.queue_broadcast(self, (source, EventListener.ON, target, amount))


class ManaThisTurn(TargetedAction):
	"""
	Give player targets \a amount Mana this turn.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def do(self, source, target, amount):
		target.temp_mana += min(target.max_resources - target.mana, amount)


class Mill(TargetedAction):
	"""
	Mill \a count cards from the top of the player targets' deck.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def do(self, source, target, count):
		target.mill(count)


class Morph(TargetedAction):
	"""
	Morph minion target into \a minion id
	"""
	TARGET = ActionArg()
	CARD = CardArg()

	def get_target_args(self, source, target):
		card = _eval_card(source, self._args[1])
		assert len(card) == 1
		card = card[0]
		card.controller = target.controller
		return [card]

	def do(self, source, target, card):
		log.info("Morphing %r into %r", target, card)
		target_zone = target.zone
		if card.zone != target_zone:
			# Transfer the zone position
			card._summon_index = target.zone_position
			# In-place morph is OK, eg. in the case of Lord Jaraxxus
			card.zone = target_zone
		target.clear_buffs()
		target.zone = Zone.SETASIDE
		target.morphed = card
		return card


class FillMana(TargetedAction):
	"""
	Refill \a amount mana crystals from player targets.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def do(self, source, target, amount):
		target.used_mana -= amount


class Retarget(TargetedAction):
	TARGET = ActionArg()
	CARD = CardArg()

	def do(self, source, target, new_target):
		if not new_target:
			return
		assert len(new_target) == 1
		new_target = new_target[0]
		if target.type in (CardType.HERO, CardType.MINION) and target.attacking:
			log.info("Retargeting %r's attack to %r", target, new_target)
			source.game.proposed_defender.defending = False
			source.game.proposed_defender = new_target
		else:
			log.info("Retargeting %r from %r to %r", target, target.target, new_target)
			target.target = new_target

		return new_target


class Reveal(TargetedAction):
	"""
	Reveal secret targets.
	"""
	def do(self, source, target):
		log.info("Revealing secret %r", target)
		self.broadcast(source, EventListener.ON, target)
		target.zone = Zone.GRAVEYARD


class SetCurrentHealth(TargetedAction):
	"""
	Sets the current health of the character target to \a amount.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def do(self, source, target, amount):
		log.info("Setting current health on %r to %i", target, amount)
		maxhp = target.max_health
		target.damage = max(0, maxhp - amount)


class SetTag(TargetedAction):
	"""
	Sets targets' given tags.
	"""
	TARGET = ActionArg()
	TAGS = ActionArg()

	def do(self, source, target, tags):
		if isinstance(tags, dict):
			for tag, value in tags.items():
				target.tags[tag] = value
		else:
			for tag in tags:
				target.tags[tag] = True


class UnsetTag(TargetedAction):
	"""
	Unset targets' given tags.
	"""
	TARGET = ActionArg()
	TAGS = ActionArg()

	def do(self, source, target, tags):
		for tag in tags:
			target.tags[tag] = False


class Silence(TargetedAction):
	"""
	Silence minion targets.
	"""
	def do(self, source, target):
		log.info("Silencing %r", self)
		self.broadcast(source, EventListener.ON, target)

		target.clear_buffs()
		if hasattr(target, 'silenceable_attributes'):
			for attr in target.silenceable_attributes:
				if hasattr(target, attr) and getattr(target, attr):
					setattr(target, attr, False)

		# Wipe the event listeners
		target._events = []
		target.silenced = True


class Summon(TargetedAction):
	"""
	Make player targets summon \a id onto their field.
	This works for equipping weapons as well as summoning minions.
	"""
	TARGET = ActionArg()
	CARD = CardArg()

	def _broadcast(self, entity, source, at, *args):
		# Prevent cards from triggering off their own summon
		if entity is args[1]:
			return
		return super()._broadcast(entity, source, at, *args)

	def do(self, source, target, cards):
		log.info("%s summons %r", target, cards)
		if not isinstance(cards, list):
			cards = [cards]

		for card in cards:
			if not card.is_summonable():
				continue
			if card.controller != target:
				card.controller = target
			if card.zone != Zone.PLAY:
				if source.type == CardType.MINION and source.zone == Zone.PLAY:
					source_index = source.controller.field.index(source)
					card._summon_index = source_index + ((self.trigger_index + 1) % 2)
				card.zone = Zone.PLAY
			self.queue_broadcast(self, (source, EventListener.ON, target, card))
			self.broadcast(source, EventListener.AFTER, target, card)

		return cards


class Shuffle(TargetedAction):
	"""
	Shuffle card targets into player target's deck.
	"""
	TARGET = ActionArg()
	CARD = CardArg()

	def do(self, source, target, cards):
		log.info("%r shuffles into %s's deck", cards, target)
		if not isinstance(cards, list):
			cards = [cards]

		for card in cards:
			if card.controller != target:
				card.zone = Zone.SETASIDE
				card.controller = target
			if len(target.deck) >= target.max_deck_size:
				log.info("Shuffle(%r) fails because %r's deck is full", card, target)
				continue
			card.zone = Zone.DECK
			target.shuffle_deck()


class Swap(TargetedAction):
	"""
	Swap minion target with \a other.
	Behaviour is undefined when swapping more than two minions.
	"""
	TARGET = ActionArg()
	OTHER = ActionArg()

	def get_target_args(self, source, target):
		other = self.eval(self._args[1], source)
		if not other:
			return (None, )
		assert len(other) == 1
		return [other[0]]

	def do(self, source, target, other):
		if other is not None:
			orig = target.zone
			target.zone = other.zone
			other.zone = orig


class SwapHealth(TargetedAction):
	"""
	Swap health between two minions using \a buff.
	"""
	TARGET = ActionArg()
	OTHER = ActionArg()
	BUFF = ActionArg()

	def do(self, source, target, other, buff):
		other = other[0]
		buff1 = source.controller.card(buff)
		buff1.health = other.health
		buff2 = source.controller.card(buff)
		buff2.health = target.health
		buff1.apply(target)
		buff2.apply(other)


class Steal(TargetedAction):
	"""
	Make the controller take control of targets.
	The controller is the controller of the source of the action.
	"""
	TARGET = ActionArg()
	CONTROLLER = ActionArg()

	def get_target_args(self, source, target):
		if len(self._args) > 1:
			# Controller was specified
			controller = self.eval(self._args[1], source)
			assert len(controller) == 1
			controller = controller[0]
		else:
			# Default to the source's controller
			controller = source.controller
		return [controller]

	def do(self, source, target, controller):
		log.info("%s takes control of %r", controller, target)
		zone = target.zone
		target.zone = Zone.SETASIDE
		target.controller = controller
		target.turns_in_play = 0  # To ensure summoning sickness
		target.zone = zone


class UnlockOverload(TargetedAction):
	"""
	Unlock the target player's overload, both current and owed.
	"""
	def do(self, source, target):
		log.info("%s overload gets cleared", target)
		target.overloaded = 0
		target.overload_locked = 0


class SummonJadeGolem(TargetedAction):
	"""
	Summons a Jade Golem for target player according to his Jade Golem Status
	"""
	TARGET = ActionArg()
	CARD = CardArg()

	def get_target_args(self, source, target):
		jade_size = "CFM_712_t" + str(target.jade_golem).zfill(2)
		return _eval_card(source, jade_size)

	def do(self, source, target, card):
		log.info("%s summons a Jade Golem for %s", source, target)
		target.jade_golem = target.jade_golem + 1 if target.jade_golem <= 29 else 30
		if card.is_summonable():
			source.game.queue_actions(source, [Summon(target, card)])


class CastSpell(TargetedAction):
	"""
	Cast a spell target random
	"""
	CARD = CardArg()

	def do(self, source, card):
		target = None
		if card.must_choose_one:
			card = random.choice(card.choose_cards)
		if card.requires_target():
			if len(card.targets):
				target = random.choice(card.targets)
			else:
				log.info("%s cast spell %s don't have a legal target", source, card)
				return
		card.target = target
		log.info("%s cast spell %s target %s", source, card, target)
		source.game.queue_actions(source, [Battlecry(card, card.target)])
		player = source.controller
		while player.choice:
			choice = random.choice(player.choice.cards)
			print("Choosing card %r" % (choice))
			player.choice.choose(choice)
		source.game.queue_actions(source, [Deaths()])


class CastSpellTargetsEnemiesIfPossible(TargetedAction):
	"""
	Cast a spell target random targets enemies if possible
	"""
	CARD = CardArg()

	def do(self, source, card):
		target = None
		if card.must_choose_one:
			card = random.choice(card.choose_cards)
		if card.requires_target():
			targets = card.targets
			if len(targets) > 0:
				enemy_targets = list(filter(
					lambda item: item.controller != source.controller, targets))
				if len(enemy_targets) > 0:
					target = random.choice(enemy_targets)
				else:
					target = random.choice(targets)
			else:
				log.info("%s cast spell %s don't have a legal target", source, card)
				return
		card.target = target
		log.info("%s cast spell %s target %s", source, card, target)
		source.game.queue_actions(source, [Battlecry(card, card.target)])
		player = source.controller
		while player.choice:
			choice = random.choice(player.choice.cards)
			print("Choosing card %r" % (choice))
			player.choice.choose(choice)
		source.game.queue_actions(source, [Deaths()])


class Evolve(TargetedAction):
	"""
	Transform your minions into random minions that cost (\a amount) more
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def do(self, source, target, amount):
		from . import cards
		cost = target.cost + amount
		card_set = cards.filter(collectible=True, cost=cost, type=CardType.MINION)
		if card_set:
			card = random.choice(card_set)
			return source.game.queue_actions(source, [Morph(target, card)])


class ExtraAttack(TargetedAction):
	"""
	Get target an extra attack change
	"""
	TARGET = ActionArg()

	def do(self, source, target):
		log.info("%s gets an extra attack change.", target)
		target.num_attacks -= 1


class SwapState(TargetedAction):
	"""
	Swap stats between two minions using \a buff.
	"""
	TARGET = ActionArg()
	OTHER = ActionArg()
	BUFF = ActionArg()

	def do(self, source, target, other, buff):
		log.info("swap state %s and %s", target, other)
		other = other[0]
		buff1 = source.controller.card(buff)
		buff1._atk = other.atk
		buff1.data.scripts.atk = lambda self, i: self._atk
		buff1.health = other.health
		buff2 = source.controller.card(buff)
		buff2._atk = target.atk
		buff2.data.scripts.atk = lambda self, i: self._atk
		buff2.health = target.health
		buff1.apply(target)
		buff2.apply(other)


class CopyState(TargetedAction):
	"""
	Copy target state, buff on self
	"""
	TARGET = ActionArg()
	OTHER = ActionArg()
	BUFF = ActionArg()

	def do(self, source, target, buff):
		target = target
		buff = source.controller.card(buff)
		buff._atk = target.atk
		buff.data.scripts.atk = lambda self, i: self._atk
		buff.health = target.health
		buff.apply(source)


class RefreshHeroPower(TargetedAction):
	"""
	Helper to Refresh Hero Power
	"""
	HEROPOWER = ActionArg()

	def do(self, source, heropower):
		log.info("Refresh Hero Power %s.", heropower)
		heropower.activations_this_turn = 0
		return heropower


class KazakusHelper(GameAction):
	"""
	Kazakus is too difficult !!!
	"""

	def do(self, source):
		player = source.controller
		self.source = source
		self.player = player
		self.next_choice = player.choice
		player.choice = self
		self.source = source
		self.cards = [
			player.card("CFM_621t11"),
			player.card("CFM_621t12"),
			player.card("CFM_621t13")
		]
		self.min_count = 1
		self.max_count = 1
		self.choosed_cards = []
		self.cost_1_potions = [
			"CFM_621t2", "CFM_621t3", "CFM_621t4",
			"CFM_621t5", "CFM_621t6", "CFM_621t8",
			"CFM_621t9", "CFM_621t10", "CFM_621t37"]
		self.cost_5_potions = [
			"CFM_621t16", "CFM_621t17", "CFM_621t18", "CFM_621t19", "CFM_621t20",
			"CFM_621t21", "CFM_621t22", "CFM_621t23", "CFM_621t24", "CFM_621t38"]
		self.cost_10_potions = [
			"CFM_621t25", "CFM_621t26", "CFM_621t27", "CFM_621t28", "CFM_621t29",
			"CFM_621t30", "CFM_621t31", "CFM_621t32", "CFM_621t33", "CFM_621t39"]

	def do_step2(self):
		card = self.choosed_cards[0]
		if card.id == "CFM_621t11":
			cards = self.cost_1_potions
		elif card.id == "CFM_621t12":
			cards = self.cost_5_potions
		elif card.id == "CFM_621t13":
			cards = self.cost_10_potions
		else:
			raise InvalidAction("Kazakus choose a missed card %s" % card)
		cards = random.sample(cards, 3)
		self.cards = []
		for card in cards:
			self.cards.append(self.player.card(card))

	def do_step3(self):
		card = self.choosed_cards[0]
		if card.id == "CFM_621t11":
			cards = self.cost_1_potions
		elif card.id == "CFM_621t12":
			cards = self.cost_5_potions
		elif card.id == "CFM_621t13":
			cards = self.cost_10_potions
		else:
			raise InvalidAction("Kazakus choose a missed card %s" % card)
		cards.remove(self.choosed_cards[1])
		cards = random.sample(cards, 3)
		self.cards = []
		for card in cards:
			self.cards.append(self.player.card(card))

	def done(self):
		card = self.choosed_cards[0]
		new_card = None
		if card.id == "CFM_621t11":
			new_card = self.player.card("CFM_621t1")
		elif card.id == "CFM_621t12":
			new_card = self.player.card("CFM_621t14")
		elif card.id == "CFM_621t13":
			new_card = self.player.card("CFM_621t15")
		else:
			raise InvalidAction("Kazakus choose a missed card %s" % card)
		card1 = self.choosed_cards[1]
		card2 = self.choosed_cards[2]
		new_card.data.scripts.play = card1.data.scripts.play + card2.data.scripts.play
		new_card.requirements.update(card1.requirements)
		new_card.requirements.update(card2.requirements)
		self.player.give(new_card)

	def choose(self, card):
		if card not in self.cards:
			raise InvalidAction("%r is not a valid choice (one of %r)" % (card, self.cards))
		else:
			self.choosed_cards.append(card)
			if len(self.choosed_cards) == 1:
				self.do_step2()
			if len(self.choosed_cards) == 2:
				self.do_step3()
			if len(self.choosed_cards) == 3:
				self.done()
				self.player.choice = self.next_choice


class Upgrade(TargetedAction):
	"""
	Upgrade cards
	"""
	TARGET = ActionArg
	AMOUNT = IntArg()

	def do(self, source, target):
		log.info("Upgrade %s counter to %s", target, target.upgrade_counter + 1)
		target.upgrade_counter += 1
		self.broadcast(source, EventListener.AFTER, target, target.upgrade_counter)


class Awaken(TargetedAction):
	"""
	Awaken a dormant minion
	"""
	TARGET = ActionArg()

	def do(self, source, target):
		log.info("%s is awaken", target)
		target.turns_in_play = 1
		if target.get_actions("awaken"):
			source.game.trigger(target, target.get_actions("awaken"), event_args=None)




#######  aharalab  ############
#
class SidequestCounter(TargetedAction):
	"""
	
	"""
	TARGET = ActionArg()# sidequest card
	AMOUNT = IntArg() #max of call
	TARGETACTION = ActionArg()# sidequest action
	def do(self, source, target, amount, targetaction):
		log.info("Setting Counter on %r -> %i, %r", target, (target._tmp_int1_+1), targetaction)
		target._tmp_int1_ += 1
		if target._tmp_int1_== amount:
			if targetaction!=None:
				if not isinstance(targetaction,list):
					targetaction = [targetaction]
				for action in targetaction:
					if isinstance(action, TargetedAction):
						action.trigger(source)

class SidequestCounterEq(TargetedAction):
	"""
	
	"""
	TARGET = ActionArg()# sidequest card
	AMOUNT = IntArg() #max of call
	TARGETACTION = ActionArg()# sidequest action
	def do(self, source, target, amount, targetaction):
		if target._tmp_int1_== amount:
			log.info("Setting Counter on %r :%i== %i, %r", target, target._tmp_int1_, amount, targetaction)
			if targetaction!=None:
				if not isinstance(targetaction,list):
					targetaction = [targetaction]
				for action in targetaction:
					if isinstance(action, TargetedAction):
						action.trigger(source)

class SidequestCounterNeq(TargetedAction):
	"""
	
	"""
	TARGET = ActionArg()# sidequest card
	AMOUNT = IntArg() #max of call
	TARGETACTION = ActionArg()# sidequest action
	def do(self, source, target, amount, targetaction):
		if target._tmp_int1_ != amount:
			log.info("Setting Counter on %r :%i!= %i, %r", target, target._tmp_int1_, amount, targetaction)
			if targetaction!=None:
				if not isinstance(targetaction,list):
					targetaction = [targetaction]
				for action in targetaction:
					if isinstance(action, TargetedAction):
						action.trigger(source)

class SidequestCounterClear(TargetedAction):
	TARGET = ActionArg()# sidequest card
	def do(self, source, target):
		log.info("Setting Counter on %r to be 0", target)
		target._tmp_int1_ = 0

class SidequestManaCounter(TargetedAction):
	TARGET = ActionArg()# sidequest card
	CARD = ActionArg()# spell card
	AMOUNT = IntArg() #max of mana
	TARGETACTION = ActionArg()# sidequest action
	def do(self, source, target, card, amount, targetaction):
		log.info("Setting Counter on %r is added by %d->%d, %r", target, card.cost, (target._tmp_int1_+card.cost), targetaction)
		target._tmp_int1_ += card.cost
		if target._tmp_int1_>= amount:
			i=0
			if targetaction!=None:
				if not isinstance(targetaction,list):
					targetaction = [targetaction]
				for action in targetaction:
					if isinstance(action, TargetedAction):
						action.trigger(source)

class SetMaxHealth(TargetedAction):
	"""
	Sets the max health of the character target to \a amount.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		log.info("Setting max_health on %r to %i", target, amount)
		target.max_health = amount
class SetAtk(TargetedAction):
	"""
	Sets the current health of the character target to \a amount.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		log.info("Setting atk on %r to %i", target, amount)
		target.atk = amount

		
from .dsl.copy import Copy

class Reborn(TargetedAction):
	"""
	Reborn!
	"""
	TARGET = ActionArg()
	def do(self, source, target):
		log.info("Reborn on %r", target)
		controller = target.controller
		reboran_minion = Summon(controller, target).trigger(source)
		if isinstance(reboran_minion,list):
			reboran_minion = reboran_minion[0]
		if isinstance(reboran_minion,list):
			reboran_minion = reboran_minion[0]
		reboran_minion.reborn = False
		reboran_minion.max_health = 1


from .dsl.copy import Copy
class CopyCostA(Copy):
	def __init__(self, selector, amount, id=None):
		self.id = id
		self.selector = selector
		self.amount = amount
	def copy(self, source, entity):
		ret = super().copy(source, entity)
		ret.cost=self.amount
		return ret

class HitAndExcess(TargetedAction):#DRG_321 #SCH_348
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		from math import floor
		target_health=target.health
		if target_health>=amount:
			Hit(target,amount).trigger(source)
			return
		Hit(target,target_health).trigger(source)
		player = target.controller
		field = player.field
		len_field = len(field)
		fieldID=0
		for i in range(len(field)):
			if field[i].entity_id == target.entity_id:
				fieldID=i
				break
		if 0<fieldID and fieldID<len_field-1:
			l_dmg = floor((amount-target_health)/2)
			r_dmg = amount-target_health-l_dmg
			Hit(field[fieldID-1], l_dmg).trigger(source)
			Hit(field[fieldID+1], r_dmg).trigger(source)
		if 0==fieldID and fieldID<len_field-1: 
			Hit(field[fieldID+1], amount-target_health).trigger(source)
		if 0<fieldID and fieldID==len_field-1: 
			Hit(field[fieldID-1], amount-target_health).trigger(source)
		pass

class HitAndExcessToOther(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	OTHER = ActionArg()
	def do(self, source, target, amount,other):
		if isinstance(target,list):
			target = target[0]
		if isinstance(other,list):
			other = other[0]
		target_health=target.health
		if target_health>=amount:
			Hit(target,amount).trigger(source)
			return
		Hit(target,target_health).trigger(source)
		Hit(other,amount-target_health).trigger(source)
		pass

class HoldinHatch(TargetedAction):#DRG_086
	TARGET = ActionArg()#player
	CARD = ActionArg()
	def do(self, source, target, card):
		card = card[0]
		source._tmp_list1_=card
		card.zone = Zone.SETASIDE
		pass

class OpenHatch(TargetedAction):#DRG_086
	TARGET = ActionArg()#player
	def do(self, source, target):
		Summon(target, source._tmp_list1_).trigger(source)
		pass

class DestroyArmor(TargetedAction):
	"""
	Destroy targets armor.
	"""
	TARGET = ActionArg()
	def do(self, source, target):
		target.armor = 0
		self.broadcast(source, EventListener.ON, target)


class SwapController(TargetedAction):
	TARGET = ActionArg()# controller's heropower
	OTHER = ActionArg()# oponent's heropower
	def do(self, source,target,other):
		if isinstance(target,list):
			target = target[0]
		if isinstance(other,list):
			other = other[0]
		target_controller=target.controller
		other_controller=other.controller
		target_controller.hero.power = other
		other_controller.hero.power = target
		target.controller = other_controller
		other.controller = target_controller
		log.info("%s and %s swap their controllers.",target, other)

class SwapMinionAndHand(TargetedAction):
	TARGET = ActionArg()# minion
	OTHER = ActionArg()# card in hand
	def do(self, source,target,other):
		if isinstance(target,list):
			target = target[0]
		if isinstance(other,list):
			other = other[0]
		newTargetController=other.controller
		newTargetZone = other.zone
		newOtherController=target.controller
		newOtherZone = target.zone
		target.controller = newTargetController
		target.zone = newTargetZone
		other.controller = newOtherController
		other.zone = newOtherZone
		log.info("%r and %r swap their positions.",target, other)


class RegularAttack(TargetedAction):
	TARGET = ActionArg()#ATTACKER
	OTHER = ActionArg()#DEFFENDER
	def do(self, source, target, other):
		if not isinstance(other,list):
			other = [other]
		if not isinstance(target,list):
			target = [target]
		for attcard in target:
			for defcard in other:
				if attcard.can_attack(defcard):
					Hit(defcard, attcard.atk).trigger(attcard)
				if defcard.can_attack(attcard):
					Hit(attcard, defcard.atk).trigger(defcard)

class Dormant(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		target.dormant = amount

class CastSpellMe(TargetedAction):
	"""
	Cast a spell target to me
	"""
	CARD = CardArg()
	AIMEDTARGET = CardArg()
	### we might modify CastSpell itself, but no get any risk
	def do(self, source, card, aimedtarget):
		target = None
		if card.must_choose_one:
			card = random.choice(card.choose_cards)
		if card.requires_target():
			if len(card.targets):
				if aimedtarget in card.targets:
					target = aimedtarget
				else:
					target = random.choice(card.targets)
			else:
				log.info("%s cast spell %s don't have a legal target", source, card)
				return
		card.target = target
		log.info("%s cast spell %s target %s", source, card, target)
		source.game.queue_actions(source, [Battlecry(card, card.target)])
		player = source.controller
		while player.choice:
			choice = random.choice(player.choice.cards)
			print("Choosing card %r" % (choice))
			player.choice.choose(choice)
		source.game.queue_actions(source, [Deaths()])

class SetAttr(TargetedAction):
	TARGET = ActionArg()
	ATTR = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, attr, amount):
		if hasattr(target, attr):
			setattr(target, attr, amount)


class BuffOnce(TargetedAction):
	"""

	"""
	TARGET = ActionArg()
	BUFF = ActionArg()
	def do(self, source, target, buff):
		targets = target
		if not isinstance(target, list):
			targets = [targets]
		for card in targets:
			omit=False
			for hisBuff in card.buffs:
				if hisBuff == buff:
					omit=True
					break;
			if not omit:
				Buff(card, buff).trigger(source)
		pass

class PermanentBuff(TargetedAction):
	"""
	"""
	TARGET = ActionArg()
	BUFFATK = IntArg()
	BUFFHEALTH = ActionArg()
	def do(self, source, target, buffatk, buffhealth):
		if isinstance(target,list):
			target = target[0]
		target.atk += buffatk
		target.max_health += buffhealth
		return target
		pass

###SCH_714
class EducatedElekkMemory(TargetedAction):
	""" Educated Elekk (epic)"""
	#[x]Whenever a spell is played, this minion remembers it.
	#<b>Deathrattle:</b> Shuffle the spells into your deck.
	HOST = ActionArg()# spell card just played
	TARGET = ActionArg()# spell card just played
	def do(self,source,target,card):
		log.info("%s remember the card: %s",target,card)
		target._tmp_list1_.append(card)

class EducatedElekkDeathrattle(TargetedAction):
	""" Educated Elekk (epic)"""
	#[x]Whenever a spell is played, this minion remembers it.
	#<b>Deathrattle:</b> Shuffle the spells into your deck.
	def do(self,source,target):
		log.info("%s Deathrattle",target)
		for card in target._tmp_list1_:
			Shuffle(target.controller, card).trigger(source)

class TentacledMenace(TargetedAction):#DRG_084
	"""Tentacled Menace	Epic
	<b>Battlecry:</b> Each player draws a card. Swap their_Costs."""
	TARGET = ActionArg()# controller
	OTHER = ActionArg()# oponent
	def do(self, source, target, other):
		draw1 = Draw(target)
		cards1 = draw1.trigger(source)
		card1 = cards1[0][0]
		draw2 = Draw(other[0])
		cards2 = draw2.trigger(source)
		card2 = cards2[0][0]
		card1.cost, card2.cost = card2.cost, card1.cost
		log.info("Draw cards and change their costs.")

class ArgentBraggart(TargetedAction):
	"""SCH_149
	<b>Battlecry:</b> Gain Attack and Health to match the highest in the battlefield.
	"""
	TARGET = ActionArg()# SELF
	def do(self, source, target):
		controller = target.controller
		opponent = controller.opponent
		friendly_minions = controller.field
		enemy_minions = opponent.field
		atk=0
		max_health=0
		for card in friendly_minions:
			if card.atk>atk:
				atk=card.atk
			if card.max_health>max_health:
				max_health = card.max_health
		for card in enemy_minions:
			if card.atk>atk:
				atk=card.atk
			if card.max_health>max_health:
				max_health = card.max_health
		target.atk = target._atk = atk
		target.max_health = max_health
		pass

class CeremonialMaul(TargetedAction):#SCH_523:
	"""
	SCH_523
	"""
	TARGET = ActionArg()# CONTROLLER
	OTHER = ActionArg()# Play.PLAYER=Spellcard
	BUFF = ActionArg()# "SCH_523t"

	def do(self, source, target, other, buff):
		new_minion = Summon(target, buff).trigger(source)
		new_minion = new_minion[0][0]
		cost = other.cost##
		new_minion._atk = new_minion.atk = cost
		new_minion.data.scripts.atk = lambda self, i: self._atk
		new_minion.max_health = cost

class Freeze(TargetedAction):
	"""

	"""
	TARGET = ActionArg()#TARGET
	def do(self, source, target):
		log.info("%r Freezes %r", self, target)
		if not target.tags[GameTag.CANT_BE_FROZEN]:
			SetTag(target, (GameTag.FROZEN, )).trigger(source)
		else:
			log.info("Freezing is blocked!")

class SetCannotAttackHeroesTag(TargetedAction):
	"""

	"""
	TARGET = ActionArg()#TARGET
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		log.info("cannot_attack_heroes: on : %r", target)
		target.cannot_attack_heroes = (amount==1)
		pass

class ChangeHeroPower(TargetedAction):
	"""
	"""
	TARGET = ActionArg()#CONTROLLER
	CARD = CardArg()
	def do(self, source, target, card):
		exh = target.hero.power.activations_this_turn
		#summon card
		newHeroPower=Summon(target,card).trigger(source)
		if isinstance(newHeroPower,list):
			newHeroPower = newHeroPower[0]
		if isinstance(newHeroPower,list):
			newHeroPower = newHeroPower[0]
		#copy exhausted
		newHeroPower.activations_this_turn = exh
		pass

class DAL731Duel(TargetedAction):
	"""
	Duel!
	"""
	TARGET = ActionArg()
	OTHER = ActionArg()
	def do(self, source, target, other):
		if isinstance(other,list):
			other = other[0]
		if isinstance(target,list):
			target = target[0]
		Summon(other.controller,other).trigger(other.controller)
		Summon(target.controller,target).trigger(target.controller)
		log.info("Duel: %r vs. %r", target, other)
		Hit(other, target.atk).trigger(target.controller)
		Hit(target, other.atk).trigger(other.controller)

class ULD703DesertObelisk(TargetedAction):
	TARGET = ActionArg()
	def do(self,source,target):
		controller = target.controller
		id = target.id
		field = controller.field
		count=0
		for card in field:
			if card.id==id:
				count+=1
		if count >= 3:
			enemy=controller.opponent
			enemy_characters=enemy.characters
			Hit(random.choice(enemy_characters),5).trigger(source)

class DAL558ArchmageVargoth(TargetedAction):
	TARGET = ActionArg()#controller
	def do(self,source,target):
		if len(target.spells_played_this_turn)>0:
			card = random.choice(target.spells_played_this_turn)
			Summon(target,card).trigger(source)

class BT126TeronGorefiend(TargetedAction):
	"""Teron Gorefiend	Minion	Legendary
	[x]<b>Battlecry:</b> Destroy all
	other friendly minions."""
	TARGET = ActionArg()#card
	def do(self,source,target):#
		target._tmp_list1_=[]
		for n in range(len(target.controller.field)):
			card = target.controller.field[0]
			if card.id != 'BT_126':
				card.zone = Zone.SETASIDE
				target._tmp_list1_.append(card)
		pass
class BT126TeronGorefiendDeathrattle(TargetedAction):
	"""Teron Gorefiend	Minion	Legendary
	<b>Deathrattle:</b> Resummon
	them with +1/+1."""
	TARGET = ActionArg()#card
	def do(self,source,target):
		for card in target._tmp_list1_:
			card.zone = Zone.PLAY
			Buff(card, "BT_126e2").trigger(source)
		pass

class WC_028_Meeting_Stone(TargetedAction):
	""" Meeting Stone """
	TARGET = ActionArg()#the controller
	def do(self,source,target):
		new_minion =  Give(target, "EX1_044").trigger(source)
		new_minion = new_minion[0][0]
		newAtk=new_minion.atk+random.randint(1,3)
		new_minion._atk = new_minion.atk = newAtk
		new_minion.data.scripts.atk = lambda self, i: self._atk
		newHealth = new_minion.health+random.randint(1,3)
		new_minion.max_health = newHealth
		log.info("Give %s with atk=%d, health=%d"%(new_minion.data.name, newAtk, newHealth))

class WC_027_Devouring_Ectoplasm(TargetedAction):
	""" Devouring Ectoplasm """
	TARGET = ActionArg()#the controller
	def do(self,source,target):
		new_minion =  Summon(target, "EX1_044").trigger(source)
		new_minion = new_minion[0][0]
		newAtk=new_minion.atk+random.randint(1,3)
		new_minion._atk = new_minion.atk = newAtk
		new_minion.data.scripts.atk = lambda self, i: self._atk
		newHealth = new_minion.health+random.randint(1,3)
		new_minion.max_health = newHealth
		log.info("Summon %s with atk=%d, health=%d"%(new_minion.data.name, newAtk, newHealth))


class Frenzy(TargetedAction):
	""" Frenzy """
	TARGET = ActionArg()#self
	TARGETACTION = ActionArg()
	def do(self,source,target,targetaction):
		#if target.frenzy==1 and target.frenzyFlag==0:
		if target.frenzyFlag==0:
			log.info("Frenzy action of %r "%(target))
			targetaction.trigger(source)
			target.frenzyFlag=1
			pass 

class WC_035_Archdruid_Naralex(TargetedAction):
	TARGET = ActionArg()#self
	def do(self, source, target):
		dreams=["DREAM_01","DREAM_02","DREAM_03","DREAM_04","DREAM_05"]
		newCard = random.choice(dreams)
		Give(target,newCard).trigger(source)
		pass

class CountSummon(TargetedAction):
	TARGET = ActionArg()#self
	LIST = ActionArg()#Minion List
	def do(self, source, target, list) -> int:
		thisGame = target.game
		logList = thisGame.get_log()
		count = 0
		for log in logList:
			if log.card.id in list and log.type==BlockType.PLAY and log.card.controller == target.controller:
				count += 1
		return count

class HaveMana(TargetedAction):
	TARGET = ActionArg()#controller
	AMOUNT = IntArg()
	def do(self,source,target,amount):
		if target.mana>=amount:
			self.broadcast(source, EventListener.ON, target, amount)


class BAR_042_Action(TargetedAction):
	def do(self, source, target):
		_highestCostCards=[]
		for _card in target.deck:
			if _card.type==CardType.SPELL:
				if len(_highestCostCards)==0:
					_highestCostCards = [_card]
				elif _highestCostCards[0].cost < _card.cost:
					_highestCostCards = [_card]
				elif _highestCostCards[0].cost == _card.cost:
					_highestCostCards.append(_card)
		if len(_highestCostCards)>0:
			_card = random.choice(_highestCostCards)
			_cost = _card.cost
			log.info("Highest cost spell is %r (cost %d)"%(_card, _cost))
			log.info("Summon a minion of cost %d"%( _cost))
			Give(target,_card).trigger(source)
			_highestMinions = []
			for _card2 in target.deck:
				if _card2.type==CardType.MINION and _card2.cost == _cost:
					_highestMinions.append(_card2)
			if(len(_highestMinions)>0):
				_card2 = random.choice(_highestMinions)
				Summon(target,_card2).trigger(source)
			else:
				log.info("no minion of cost %d"%( _cost))
		else:
			log.info("no spell is in the deck"%())

class BAR_037_Warsong_Wrangler(Choice):
	#Give all copies of it +2/+1 <i>(wherever_they_are)</i>.
	def choose(self, card):
		super().choose(card)
		log.info("%s chooses %r"%(card.controller.data.name, card))
		for _card in self.cards:
			if _card is card:
				if card.type == CardType.HERO_POWER:
					_card.zone = Zone.PLAY
				elif len(self.player.hand) < self.player.max_hand_size:
					_card.zone = Zone.HAND
				else:
					_card.discard()
			else:
				_card.discard()
		game = card.game
		cardList = game.decks + game.hands + game.characters
		for _card in cardList:
			if _card.id == card.id:
				Buff(_card,"BAR_037e").trigger(card.controller)
		pass

class BAR_081_Southsea_Scoundrel(Choice):
	#Give all copies of it +2/+1 <i>(wherever_they_are)</i>.
	def choose(self, card):
		super().choose(card)
		log.info("%s chooses %r"%(card.controller.name, card))
		for _card in self.cards:
			if _card is card:
				if card.type == CardType.HERO_POWER:
					_card.zone = Zone.PLAY
				elif len(self.player.hand) < self.player.max_hand_size:
					_card.zone = Zone.HAND
				else:
					_card.discard()
			else:
				_card.discard()
		controller = card.controller.opponent##もともと相手のもの->これは自分
		Give(controller,card.id).trigger(controller)
		pass

class BAR_079_Kazakus_Golem_Shaper(Choice):

	def do(self,source,target, cards):
		target.choice = self
		## agent's choice 
		card = random.choice(player.choice.cards)
		## overload choose(self, card)
		log.info("%s chooses %r"%(card.controller.data.name, card))
		for _card in self.cards:
			if _card is card:
				if card.type == CardType.HERO_POWER:
					_card.zone = Zone.PLAY
				elif len(self.player.hand) < self.player.max_hand_size:
					_card.zone = Zone.HAND
				else:
					_card.discard()
			else:
				_card.discard()
		if card.ID=='BAR_079_m1':
			BAR_079_m1_Action(target,["BAR_079t4","BAR_079t5","BAR_079t6","BAR_079t7","BAR_079t8","BAR_079t9"]).trigger(source)
		if card.ID=='BAR_079_m2':
			BAR_079_m2_Action(target,["BAR_079t4","BAR_079t5","BAR_079t6","BAR_079t7","BAR_079t8","BAR_079t9"]).trigger(source)
		if card.ID=='BAR_079_m3':
			BAR_079_m3_Action(target,["BAR_079t4","BAR_079t5","BAR_079t6","BAR_079t7","BAR_079t8","BAR_079t9"]).trigger(source)

class BAR_079_m1_Action(Choice):
	def do(self,source,target, cards):
		target.choice = self
		## agent's choice 
		card = random.choice(player.choice.cards)
		## overload choose(self, card)
		for _card in self.cards:
			if _card is card:
				if card.type == CardType.HERO_POWER:
					_card.zone = Zone.PLAY
				elif len(self.player.hand) < self.player.max_hand_size:
					_card.zone = Zone.HAND
				else:
					_card.discard()
			else:
				_card.discard()
		if card.id=='BAR_079t4':
			pass

class BAR_079_m1_Action(Choice):
	pass
class BAR_079_m1_Action(Choice):
	pass
