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
		card = card.eval(source.game.allcards, source) # game? allcards?

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
		try:
			attacker = _eval_card(source, self._args[0])[0]
		except IndexError as e:## annihilation in procedure
			attacker = None
		try:
			defender = _eval_card(source, self._args[1])[0]
		except IndexError as e:## annihilation in procedure
			defender = None
		return attacker, defender

	def do(self, source, attacker, defender):
		log.info("%r attacks %r", attacker, defender)
		if attacker == None or defender == None: ## rarely happens
			return
		attacker.attack_target = defender
		defender.defending = True
		source.game.proposed_attacker = attacker
		source.game.proposed_defender = defender
		source.game.manager.step(Step.MAIN_COMBAT, Step.MAIN_ACTION)
		source.game.refresh_auras()  # XXX Needed for Gorehowl
		self.broadcast(source, EventListener.ON, attacker, defender)

		defender = source.game.proposed_defender
		if defender == None: ## rarely happens
			return
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

		attack_after_activate=True 
		for secret in defender.controller.secrets:
			if secret.id=='CS3_016' and attacker.atk<3:
				attack_after_activate=False
		if attack_after_activate:
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
		player.times_spells_played_this_turn = 0 # DAL_603
		player.spells_played_this_turn=[] # DAL_558
		player.died_this_turn=[] # CORE_EX1_190


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
		target.controller.add_death_log(target)
		self.broadcast(source, EventListener.ON, target)
		if target.id == 'SW_323'and target._Asphyxia_=='alive': #The king rat
			source.game.queue_actions(source, [Asphyxia(target)])
		if target.deathrattles and target.deathrattle_valid:
			source.game.queue_actions(source, [Deathrattle(target)])
		if target.reborn:# 
			source.game.queue_actions(source, [Reborn(target)])
		if target.id== 'DRG_253':#  Dwarven Sharpshooter
			ChangeHeroPower(target.controller, "HERO_05bp").trigger(target)
		if target.type == CardType.MINION:
			if target.guardians_legacy:#CS3_001由来の継承
				SetGLflag(target.controller).trigger(target.controller)##ガーディアンの継承をプレーヤーに移譲する。

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

########## Choice ##############

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
			cards = cards.eval(source.game.allcards + source.game.graveyard, source) # game? entities + decks?
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
			log.info("No choice for this condition.")
			return
		log.info("%r choice from %r", player, cards)
		self.next_choice = player.choice
		player.choice = self
		player.choiceText = source.choiceText
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
		private_casts_when_chosen = ['YOP_024t']
		super().choose(card)
		if not hasattr(card, 'controller') or not hasattr(card, 'type'):
			return
		log.info("%s chooses %r"%(card.controller.name, card))
		for _card in self.cards:
			if _card is card:
				if card.type == CardType.HERO_POWER:
					new_card = self.player.card(_card.id)# make a new copy
					new_card.zone = Zone.PLAY
				elif len(self.player.hand) < self.player.max_hand_size:
					new_card = self.player.card(_card.id)# make a new copy
					new_card.zone = Zone.HAND
					if new_card.id in private_casts_when_chosen:
						Play(new_card,None,None,None).trigger(card.controller)
		# we may return the new card. 


class GenericChoiceOnDeck(Choice):
	## choose from Deck 
	def choose(self, card):
		super().choose(card)
		log.info("%s chooses %r"%(card.controller.name, card))
		for _card in self.cards:# cards are from Deck
			if _card is card:
				if len(self.player.hand) < self.player.max_hand_size:
					_card.zone = Zone.HAND
				else:
					_card.discard()
			else:
				_card.discard()


class BAR_081_Southsea_Scoundrel(Choice):## 
	#Give all copies of it +2/+1 <i>(wherever_they_are)</i>.
	def choose(self, card):
		super().choose(card)
		log.info("%s chooses %r"%(card.controller.name, card))
		for _card in self.cards:
			if _card is card:
				if card.type == CardType.HERO_POWER:
					_card.zone = Zone.PLAY
				elif len(self.player.hand) < self.player.max_hand_size:
					Give(card.controller,card.id).trigger(card.controller)
				else:
					_card.discard()
			else:
				_card.discard()
		controller = card.controller.opponent##もともと相手のもの->これは自分
		Give(controller,card.id).trigger(controller)
		pass


class GenericChoiceBuff(GenericChoice):## SW_059  ## callbackで対応可能
	def choose(self, card):
		super().choose(card)
		Buff(card,'SW_059e').trigger(card.controller)
		pass

class GenericChoicePlay(GenericChoice):## 
	def choose(self, card):
		super().choose(card)
		controller = self.player
		for new_card in controller.hand:
			if new_card.id == card.id:
				Summon(controller, new_card).trigger(controller)
				break
		pass

class GenericChoiceBattlecry(GenericChoice):## 
	def choose(self, card):
		super().choose(card)
		controller = self.player
		for new_card in controller.hand:
			if new_card.id == card.id:
				Battlecry(new_card, new_card.target).trigger(new_card)
				#new_card.zone=Zone.PLAY# 必要？
				break
		pass


class GenericChoicePlayOnDeck(Choice):## callbackで対応可能
	def choose(self, card):
		super().choose(card)
		controller = self.player
		for _card in self.cards:## cards are from deck
			if _card is card:
				Summon(controller, _card).trigger(controller)
			else:
				_card.discard()
		pass

###################  Choice end #######################

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
		player.spell_and_damage=False
		log.info("%s plays %r (target=%r, index=%r)", player, card, target, index)

		player.pay_cost(card, card.cost)
		player.add_play_log(card)

		card.target = target
		card._summon_index = index

		battlecry_card = choose or card
		# We check whether the battlecry will trigger, before the card.zone changes
		if battlecry_card.battlecry_requires_target() and not target:
			log.info("%r requires a target for its battlecry. Will not trigger." % card)
			trigger_battlecry = False
		else:
			trigger_battlecry = True

		if card is card.controller.hand[0] or card is card.controller.hand[-1]:
			trigger_outcast = True
		else:
			trigger_outcast = False

		card.zone = Zone.PLAY
		if card.type == CardType.MINION:
			player.add_summon_log(card)

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
		#corrupt:
		Corrupt(player, card).trigger(player)

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

		if heropower.data.id == 'HERO_05bp':
			player.add_activate_log(heropower, 2)
		elif heropower.data.id == 'HERO_05bp2':
			player.add_activate_log(heropower, 3)
		elif heropower.data.id == 'HERO_08bp':
			player.add_activate_log(heropower, 1)
		elif heropower.data.id == 'HERO_08bp2':
			player.add_activate_log(heropower, 2)


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

class PayCost(GameAction):
	PLAYER = ActionArg()# controller of the targeted card
	TARGET = ActionArg()# the targeted card
	AMOUNT = IntArg()
	def do(self, sourse, player, target, amount):
		player.pay_cost(target, amount)
		pass
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
			return selector.eval(source.game.allcards, source) # game ? or game.allcards?

	def get_target_args(self, source, target):
		ret = []
		for k, v in zip(self.ARGS[1:], self._args[1:]):
			if isinstance(v, Selector):
				# evaluate Selector arguments
				v = v.eval(source.game.allcards, source)# game ? or game.allcards?
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
			ret = t.eval(source.game.allcards, source) ## game? or game.entities?
		if not ret:
			return []
		if not hasattr(ret, "__iter__"):
			# Bit of a hack to ensure we always get a list back
			ret = [ret]
		return ret

	def trigger(self, source):
		ret = []

		if self.source is not None:
			source = self.source.eval(source.game.allcards, source) ## game? or game.entities?
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
				from .player import Player
				from .card import PlayableCard
				if isinstance(source, Player):
					source.add_targetedaction_log({'class':self,'source':source,'target':target})## log for action
				elif isinstance(source, PlayableCard):
					source.controller.add_targetedaction_log({'class':self,'source':source,'target':target})## log for action
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
		if source.controller==target.controller and target.type==CardType.HERO:##FRIENDLY_HERO
			source.controller.lost_in_the_park = buff.atk##  SW_428 Lost in the park
			if buff.atk>0:# it works for atk buffs
				self.broadcast(source, EventListener.ON, target)
			pass
		return buff.apply(target)

class RemoveBuff(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	def do(self, source, target, buff):
		buffList = target.buffs
		for bf in buffList:
			if bf.id == buff:
				target.buffs.remove(bf)
				break
		pass
	pass

class EatsCard(TargetedAction):
	""" add other stats to target stats
	"""
	TARGET = ActionArg()
	OTHER = ActionArg()
	def do(self, source, target, other):
		if target==[] or other==[]:
			return
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
			target.controller.add_damage_log(target, amount)
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
			if source.type == CardType.SPELL:## for SW_322
				source.controller.spell_and_damage=True
			else:
				source.controller.spell_and_damage=False
			# check hasattr: some sources of damage are game or player (like fatigue)
			# weapon damage itself after hero attack, but does not trigger lifesteal
			if hasattr(source, "lifesteal") and source.lifesteal and source.type != CardType.WEAPON:
				source.heal(source.controller.hero, amount)
			self.broadcast(source, EventListener.ON, target, amount, source)
			# poisonous can not destory hero
			if hasattr(source, "poisonous") and source.poisonous and (
				target.type != CardType.HERO and source.type != CardType.WEAPON):
				log.info("%r destroys %r by poison"%(source, target))
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
			arg = arg.eval(source.game.allcards, source) ## game? or game.allcards? decks must be included
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

class Corrupt(TargetedAction):# darkmoon fair 
	CONTROLLER = ActionArg()
	CARD = CardArg()
	def do(self, source, controller, card):
		card=card[0]
		corruptList=[]
		for target in controller.hand:
			if target.corrupt and card.cost > target.cost:
				if target.id == 'DMF_124t':# （+1/+1 in any case）
					target.max_health += 1
					target.atk += 1
				elif target.id == 'DMF_526':
					corruptList.append({'card':target,'corruptedID':target.id+"a"})
				else:
					corruptList.append({'card':target,'corruptedID':target.id+"t"})
		for target in corruptList:
			newCard = Give(controller, target['corruptedID']).trigger(controller)
			if newCard[0]!=[]:
				newCard = newCard[0][0]
				for _buff in target['card'].buffs:
					newCard.buffs.append(_buff)
		for target in corruptList:
			Destroy(target['card']).trigger(controller)
		pass

class Destroy(TargetedAction):
	"""
	Destroy character targets.
	"""
	TARGET = ActionArg()
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
		if hasattr(target,'hero') and target.hero.data.card_class != CardClass.NEUTRAL:
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
		result = picker.evaluate(source)
		if len(result) >= 0:
			return [picker.evaluate(source)]
		else:
			return [[]]

	def do(self, source, target, cards):
		log.info("%r discovers %r for %s", source, cards, target)
		source.game.queue_actions(source, [GenericChoice(target, cards)])


class SetGLflag(TargetedAction):
    def do(self, source, target):
        target.guardians_legacy = True
        log.info("Guardian's legacy flag on (%r)"%(target))


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
		#guardian's legacy #CS3_001
		player = source.controller#
		if player.guardians_legacy and card.type == CardType.MINION:
			#引いたばかりのカードにCS3_001のdeathrattleのためのフラグを追加する。
			card.spellpower = 2
			card.guardians_legacy = True##ガーディアンの継承をカードに移譲する。
			player.guardians_legacy=False
			log.info("Guardian's legacy is inderited by %r"%(card))
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
		if amount>0 and hasattr(target, 'total_armor'):
			target.total_armor += amount
		target.armor += amount
		self.broadcast(source, EventListener.ON, target, amount)

class GainAttackHealth(TargetedAction):
	TARGET=ActionArg()
	AMOUNT1=IntArg()
	AMOUNT2=IntArg()
	def do(self, source, target, amount1, amount2):
		target.atk = max(target.atk+amount1,0)
		target.max_health = max(target.max_health+amount2, 0)
		self.broadcast(source, EventListener.ON, target, amount1, amount2)

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
			## when card==[]  ## 
			if hasattr(card, "__iter__") and len(card)==0:
				break;
			## when card==None  ## 
			if card == None:
				break;
			## 
			card.controller = target
			if card.zone != Zone.HAND or not card in target.hand:
				card.zone = Zone.HAND
			# if card is 'casts_when_drawn' then immediately play.  
			card.game.card_when_drawn(card, card.controller)
			ret.append(card)
		return ret


class Hit(TargetedAction):
	"""
	Hit character targets by \a amount.
	"""
	TARGET = ActionArg()
	AMOUNT = ActionArg()

	def do(self, source, target, amount):
		amount = source.get_damage(amount, target)
		if amount:
			#if isinstance(source,PlayableCard):
			if hasattr(source, 'honorable_kill') and source.honorable_kill:
				if target.type==CardType.WEAPON and target==source:## when decreasing durability
					pass
				else:
					target_health = target.health
					if target_health == amount:
						log.info("%s hits %s and gets honorable kill"%(source, target))
						target.honorably_killed = True
						if source.type==CardType.HERO and source.controller.weapon!=None :
							actions = source.controller.weapon.get_actions("honorable_kill")
							source.game.trigger(source.controller.weapon, actions,event_args=None)
						else:
							actions = source.get_actions("honorable_kill")
							source.game.trigger(source, actions,event_args=None)
						for buff in source.buffs:
							if hasattr(buff, 'honorable_kill'):
								actions = buff.get_actions('honorable_kill')
								source.game.trigger(source, actions, event_args=None)
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
		if target.type != CardType.PLAYER:
			return
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
		if len(card)==0: # no targeted card
			return []
		assert len(card) == 1
		card = card[0]
		if card==None:
			return []
		card.controller = target.controller
		return [card]

	def do(self, source, target, card):
		if target.type == CardType.MINION:
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

class SW_078_Morph(TargetedAction):
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
		if target.type == CardType.MINION:
			log.info("Morphing %r into %r", target, card)
			target_zone = target.zone
			if card.zone != target_zone:
				# Transfer the zone position
				card._summon_index = target.zone_position
				# In-place morph is OK, eg. in the case of Lord Jaraxxus
				card.zone = target_zone
			target.clear_buffs()
			target.zone = Zone.SETASIDE
			card.cost = target.cost
			if hasattr(target, 'atk'):
				card.atk = target.atk
			if hasattr(target, 'max_health'):
				card.max_health = target.max_health
			target.morphed = card
			return card

class DMF_108_Morph(TargetedAction):
	"""
	Morph minion target into card. with same cost
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
		if target.type == CardType.MINION:
			log.info("Morphing %r into %r", target, card)
			target_zone = target.zone
			if card.zone != target_zone:
				# Transfer the zone position
				card._summon_index = target.zone_position
				# In-place morph is OK, eg. in the case of Lord Jaraxxus
				card.zone = target_zone
			target.clear_buffs()
			target.zone = Zone.SETASIDE
			card.cost = target.cost
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
		target.controller.add_reveal_log(target)
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
		log.info("Setting current tag on %r to %s", target, tags)
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
			log.info("%s unset tag %s"%(target, tag))
			target.tags[tag] = False


class Silence(TargetedAction):
	"""
	Silence minion targets.
	"""
	def do(self, source, target):
		log.info("Silencing %r", target)
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
		if target.type != CardType.PLAYER:
			log.info("<><><><><><><><><><><><>")
			log.info("%s is not a player, he/she cannot summon anything", target)
			log.info("<><><><><><><><><><><><>")
			return
		log.info("%s summons %r", target, cards)

		if not isinstance(cards, list):
			cards = [cards]

		for card in cards:
			if not hasattr(card, 'is_summonable') or not card.is_summonable():
				continue
			target.add_summon_log(card)
			if card.controller != target:
				card.controller = target
			if card.zone != Zone.PLAY:
				if source.type == CardType.MINION and source.zone == Zone.PLAY:
					source_index = source.controller.field.index(source)
					card._summon_index = source_index + ((self.trigger_index + 1) % 2)
				card.zone = Zone.PLAY
			self.queue_broadcast(self, (source, EventListener.ON, target, card))
			self.broadcast(source, EventListener.AFTER, target, card)
			# if the spells are casted by the power of another spell, we may need this line.
			#DMF_254t_Action(card).trigger(card.controller)
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
		if cards[0]==None:
			return
		for card in cards:
			if card.controller != target:
				card.zone = Zone.SETASIDE
				card.controller = target
			if len(target.deck) >= target.max_deck_size:
				log.info("Shuffle(%r) fails because %r's deck is full", card, target)
				continue
			card.zone = Zone.DECK
			target.shuffle_deck()
		return cards

class ShuffleBuff(TargetedAction):
	"""
	Shuffle and buff card targets into player target's deck.
	"""
	TARGET = ActionArg()#player
	CARD = CardArg()
	BUFF = ActionArg()
	def do(self, source, target, cards, buff):
		log.info("%r shuffles into %s's deck", cards, target)
		if not isinstance(cards, list):
			cards = [cards]
		for card in cards:
			Buff(card,buff).trigger(source)
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
		player.add_play_log(card)
		while player.choice:
			choice = random.choice(player.choice.cards)
			print("Choosing card %r" % (choice))
			player.choice.choose(choice)
		source.game.queue_actions(source, [Deaths()])

class CastSecret(TargetedAction):
	"""
	Cast a spell target random
	"""
	CARD = CardArg()
	def do(self, source, cards):
		log.info("%s cast secret %s ", source, cards)
		if not isinstance(cards,list):
			cards = [cards]
		for card in cards:
			card.zone=Zone.SECRET


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

class RefreshMana(TargetedAction):
	"""
	Helper to Refresh MANA
	"""
	TARGET = ActionArg()#controller
	AMOUNT = IntArg()
	def do(self, source, target,amount):
		log.info("Refresh Mana by %s.", amount)
		source.controller.used_mana = max(source.controller.used_mana-amount,0)



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




#######  sidequest  ############
#
class SidequestCounter(TargetedAction):
	"""
	
	"""
	TARGET = ActionArg()# sidequest card
	AMOUNT = IntArg() #max of call
	TARGETACTION = ActionArg()# sidequest action
	def do(self, source, target, amount, targetaction):
		log.info("Setting Counter on %r -> %i, %r", target, (source._sidequest_counter_+1), targetaction)
		target._sidequest_counter_ += 1
		if target._sidequest_counter_== amount:
			target._sidequest_counter_ = 0
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
		if target._sidequest_counter_== amount:
			log.info("Setting Counter on %r :%i== %i, %r", target, target._sidequest_counter_, amount, targetaction)
			target._sidequest_counter_ = 0
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
		if target._sidequest_counter_ != amount:
			log.info("Setting Counter on %r :%i!= %i, %r", target, target._sidequest_counter_, amount, targetaction)
			target._sidequest_counter_ = 0
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
		target._sidequest_counter_ = 0

class SidequestManaCounter(TargetedAction):
	TARGET = ActionArg()# sidequest card
	CARD = ActionArg()# spell card
	AMOUNT = IntArg() #max of mana
	TARGETACTION = ActionArg()# sidequest action
	def do(self, source, target, card, amount, targetaction):
		log.info("Setting Counter on %r is added by %d->%d, %r", target, card.cost, (target._sidequest_counter_+card.cost), targetaction)
		target._sidequest_counter_ += card.cost
		if target._sidequest_counter_>= amount:
			i=0
			if targetaction!=None:
				if not isinstance(targetaction,list):
					targetaction = [targetaction]
				for action in targetaction:
					if isinstance(action, TargetedAction):
						action.trigger(source)

class SidequestLostInTheParkCounter(TargetedAction):##  SW_428 Lost in the park
	""" count ATK buffed on the hero """
	TARGET = ActionArg()# sidequest card
	AMOUNT = IntArg() #max of mana
	TARGETACTION = ActionArg()# sidequest action
	def do(self, source, target, amount, targetaction):
		log.info("Setting Counter on %r rolls by %d->%d, %r", target, target.controller.lost_in_the_park, (target._sidequest_counter_+target.controller.lost_in_the_park), targetaction)
		target._sidequest_counter_ += target.controller.lost_in_the_park
		target.controller.lost_in_the_park = 0 # to avoid a double count
		if target._sidequest_counter_>= amount:
			if targetaction!=None:
				if not isinstance(targetaction,list):
					targetaction = [targetaction]
				for action in targetaction:
					if isinstance(action, TargetedAction):
						action.trigger(source)


###################### end of sidequest

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
class SetCost(TargetedAction):
	"""
	Sets the cost of the character target to \a amount.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		log.info("Setting cost on %r to %i", target, amount)
		target.cost = amount


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


class Asphyxia(TargetedAction):
	TARGET = ActionArg()# the card
	def do(self, source, target):
		_score_limit = 5
		if target._Asphyxia_ == 'alive' and target.dead:
			log.info("The King Rat turns death.")
			ret = Summon(target.controller, "SW_323").trigger(target.controller)
			if ret[0]!=[]:
				ret = ret[0][0]
				ret._Asphyxia_= 'asphyxia'
				ret.cant_attack = True
				ret.cant_be_damaged = True
				ret.cant_be_frozen = True
				ret.cant_be_targeted_by_abilities = True
				ret.cant_be_targeted_by_hero_powers = True
				ret.cant_be_targeted_by_opponents = True
		elif target._Asphyxia_ == 'asphyxia':
			target._sidequest_counter_ += 1
			log.info("The King Rat is under asphyxia. Counter is %i."%(target._sidequest_counter_))
			if target._sidequest_counter_ == _score_limit:
				target._sidequest_counter_ = 0
				target._Asphyxia_= 'alive'
				target.cant_attack = False
				target.cant_be_damaged = False
				target.cant_be_frozen = False
				target.cant_be_targeted_by_abilities = False
				target.cant_be_targeted_by_hero_powers = False
				target.cant_be_targeted_by_opponents = False
			pass
		pass


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
		if target==[] or other==[]:
			return 
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
		source._sidequest_list1_=card
		card.zone = Zone.SETASIDE
		pass

class OpenHatch(TargetedAction):#DRG_086
	TARGET = ActionArg()#player
	def do(self, source, target):
		Summon(target, source._sidequest_list1_).trigger(source)
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
		if target==[] or other==[]:
			return
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
		if target==[] or other==[]:
			return
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
			log.info("%s set attr '%s' into %d"%(target, attr, amount ))
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
		if target==[]:
			return
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
		target._sidequest_list1_.append(card)

class EducatedElekkDeathrattle(TargetedAction):
	""" Educated Elekk (epic)"""
	#[x]Whenever a spell is played, this minion remembers it.
	#<b>Deathrattle:</b> Shuffle the spells into your deck.
	def do(self,source,target):
		log.info("%s Deathrattle",target)
		for card in target._sidequest_list1_:
			Shuffle(target.controller, card).trigger(source)

class TentacledMenace(TargetedAction):#DRG_084
	"""Tentacled Menace	Epic
	<b>Battlecry:</b> Each player draws a card. Swap their_Costs."""
	TARGET = ActionArg()# controller
	OTHER = ActionArg()# oponent
	def do(self, source, target, other):
		draw1 = Draw(target)
		cards1 = draw1.trigger(source)
		if cards1[0] != []:
			card1 = cards1[0][0]
			draw2 = Draw(other[0])
			cards2 = draw2.trigger(source)
			if cards2[0] != []:
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
		if new_minion[0] != []:
			new_minion = new_minion[0][0]
			cost = other.cost##
			new_minion._atk = new_minion.atk = cost
			new_minion.data.scripts.atk = lambda self, i: self._atk
			new_minion.max_health = cost

class InheritGuardiansLegacy(TargetedAction):
	"""   """
	def do(self, source, target):
		log.info("Gardian's Legacy was inherited by %r"%(target))
		target.guardians_legacy=True
		pass

class Freeze(TargetedAction):
	"""

	"""
	TARGET = ActionArg()#TARGET
	def do(self, source, target):
		log.info("%r Freezes %r", self, target)
		if not target.tags[GameTag.CANT_BE_FROZEN]:
			##SetTag(target, (GameTag.FROZEN, )).trigger(source)
			target.frozen = True
		else:
			log.info("Freezing is blocked!")

class FreezeOrDeath(TargetedAction):
    def do (self, source, target):
        if target.frozen:
            Destroy(target).trigger(source)
        else:
            Freeze(target).trigger(source)
        pass

class FreezeOrHit(TargetedAction):
    TARGET = ActionArg()#TARGET
    AMOUNT = IntArg()
    def do (self, source, target, amount):
        if target.frozen:
            Hit(target, amount).trigger(source)
        else:
            Freeze(target).trigger(source)
        pass

#class SetCannotAttackHeroesTag(TargetedAction):
#	"""
#
#	"""
#	TARGET = ActionArg()#TARGET
#	AMOUNT = IntArg()
#	def do(self, source, target, amount):
#		log.info("cannot_attack_heroes: on : %r", target)
#		target.cannot_attack_heroes = (amount==1)
#		pass

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
		if target==[] or other==[]:
			return
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
		target._sidequest_list1_=[]
		for n in range(len(target.controller.field)):
			card = target.controller.field[0]
			if card.id != 'BT_126':
				card.zone = Zone.SETASIDE
				target._sidequest_list1_.append(card)
		pass
class BT126TeronGorefiendDeathrattle(TargetedAction):
	"""Teron Gorefiend	Minion	Legendary
	<b>Deathrattle:</b> Resummon
	them with +1/+1."""
	TARGET = ActionArg()#card
	def do(self,source,target):
		for card in target._sidequest_list1_:
			card.zone = Zone.PLAY
			Buff(card, "BT_126e2").trigger(source)
		pass

class SummonAdventurerWithBonus(TargetedAction):
	""" Devouring Ectoplasm """
	TARGET = ActionArg()#the controller
	def do(self,source,target):
		new_minion =  random.choice(['WC_034t','WC_034t2','WC_034t3','WC_034t4','WC_034t5','WC_034t6','WC_034t7','WC_034t7',])
		new_minion =  Summon(target, new_minion).trigger(source)
		if new_minion[0] != []:
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
		# 'frenzy' is silencable
		if target.frenzy==1 and target.frenzyFlag==0:
		#if target.frenzyFlag==0:
			log.info("Frenzy action of %r "%(target))
			targetaction.trigger(source)
			target.frenzyFlag=1
			pass 

#class HonorableKill(TargetedAction):
#	""" Honorable Kill """
#	TARGET = ActionArg() # predamaged minion
#	AMOUNT = IntArg()
#	TARGETEDACTION = ActionArg()
#	def do(self, source, target, amount, targetaction):
#		# 'honorable_kill' is silenceable
#		if source.honorable_kill==1:
#			if taget.health == amount:
#				log.info("Honorable Kill works on %s"%(source))
#				targetaction.trigger(source)
#			pass
#		pass
#	pass

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

class CountDeathAction(TargetedAction):
	TARGET = ActionArg()#self
	LIST = ActionArg()#Death List
	AMOUNT = IntArg()
	ACTION = ActionArg()
	def do(self, source, target, list, amount, action) :
		_thisPlayer = target.controller
		_logList = _thisPlayer.death_log
		_count = 0
		for _card in _logList:
			if _card.id in list:
				_count += 1
		# SW_075
		if source.id=='SW_075':
			for cd in _thisPlayer.hand:
				if cd.id == 'SW_075':
					cd.script_data_num_1 = _count
			for cd in _thisPlayer.field:
				if cd.id == 'SW_075':
					cd.script_data_num_1 = _count
		if _count==amount:
			action.trigger(source)

class HaveMana(TargetedAction):
	TARGET = ActionArg()#controller
	AMOUNT = IntArg()
	def do(self,source,target,amount):
		if target.mana>=amount:
			self.broadcast(source, EventListener.ON, target, amount)

class SpellAndDamage(TargetedAction):## for SW_322
	TARGET = ActionArg()
	TARGETACTION = ActionArg()
	def do(self,source,target,targetaction):
		player = source.controller
		if player.spell_and_damage:
			player.spell_and_damage = False
			targetaction.trigger(source)
		pass

class Moribund(TargetedAction):
    """ call 'on' Predamage  
	events = Predamage(SOMEONE).on(Moribund(SOMEONE,[ACTION])
	"""
    TARGET = ActionArg()
    TARGETACTIONS = ActionArg()
    def do(self, source, target, targetactions):
        if target.health<=target.predamage: 
            log.info("%r is moribund."%target)
            for action in targetactions:
                action.trigger(source)
        pass


############### script_data_num_1 関連 ########################

def ScriptDataNum1(card):
    if hasattr(card,'script_data_num_1'):
        return card.script_data_num_1
    else:
        return 0
    pass

class HitScriptDataNum1(TargetedAction):
    CARD=ActionArg()#card
    TARGET=ActionArg()#target
    def do(self,source,card,target):
        amount = ScriptDataNum1(card)
        if not isinstance(target,list):
            target = [target]
        for _card in target:
            Hit(_card,amount).trigger(source)

class SetScriptDataNum1(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		if hasattr(target,'script_data_num_1'):
			target.script_data_num_1 = amount
		pass

class AddScriptDataNum1(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		if hasattr(target,'script_data_num_1'):
			target.script_data_num_1 += amount
		pass

###############################################################