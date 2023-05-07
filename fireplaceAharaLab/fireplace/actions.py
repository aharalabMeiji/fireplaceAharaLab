import random
from collections import OrderedDict

from hearthstone.enums import (
	BlockType, CardClass, CardSet, CardType, Mulligan, PlayState, Step, Zone, GameTag, Race
)

from .dsl import LazyNum, LazyValue, Selector
from .entity import Entity
from .exceptions import InvalidAction
from .logging import log
from .utils import random_class
from .config import Config
from .dsl.random_picker import RandomEntourage, RandomID

def _eval_card(source, card):
	"""
	Return a Card instance from a card
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
		card = card.eval(source.game.allcards, source) # 

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
				if Config.LOGINFO:
					Config.log("actions.broadcast","%s triggers off %s from %s"%(entity, self, source))
				entity.trigger_event(source, event, args)
			elif isinstance(self, event.trigger.__class__) and event.trigger.matches(entity, args):#or its inverse
				if Config.LOGINFO:
					Config.log("actions.broadcast","%s triggers off %s from %s"%(entity, self, source))
				entity.trigger_event(source, event, args)
	def broadcast(self, source, at, *args):
		broadcast_entities = source.game.broadcast_entities
		for entity in broadcast_entities:
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
			if isinstance(match, int):
				return match==arg
			if isinstance(match, list) and isinstance(match[0], int):
				return arg in match
			if callable(match):
				res = match(arg)
				if not res:
					return False
			else:
				# this stuff is stupidslow
				res = match.eval([arg], source)
				if not res or (res[0] != arg and res!=arg):
					return False
		return True


class GameAction(Action):
	def trigger(self, source):
		args = self.get_args(source)
		self.do(source, *args)


class Attack(GameAction):
	"""
	Make a ATTACKER attack a DEFENDER
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
		if Config.LOGINFO:
			Config.log("Attack.do","%s attacks %s"%(attacker, defender))
		if attacker == None or defender == None: ## rarely happens
			return
		attacker.attack_target = defender
		defender.defending = True
		source.game.proposed_attacker = attacker
		source.game.proposed_defender = defender
		source.game.manager.step(Step.MAIN_COMBAT, Step.MAIN_ACTION)
		source.game.refresh_auras()  # 
		attacker.stop_attack=False
		self.broadcast(source, EventListener.ON, attacker, defender)
		if attacker.stop_attack:# in the broadcast, it may happen
			return

		defender = source.game.proposed_defender
		if defender == None: ## rarely happens
			return
		source.game.proposed_attacker = None
		source.game.proposed_defender = None
		if attacker.should_exit_combat:
			if Config.LOGINFO:
				Config.log("Attack.do","Attack has been interrupted."%())
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

class BeginBar(GameAction):
	PLAYER = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, player, amount):
		player.game.refresh_auras()## refresh aura_buff
		if source.game.turn==amount or amount==0:	
			self.broadcast(source, EventListener.ON, player)
		#### discover a darkmoon tickets see tag{2044}(darkmoon_ticket_tier) after 23.6
		if player.game.parent.darkmoon_ticket_by_4 and source.game.turn%4 == 0:
			k=min(int(source.game.turn/4),3)
			source.entourage = random.sample(player.game.parent.BG_darkmoon_tickets[k], 3)
			Discover(player, RandomEntourage()).trigger(source)

		pass

class BeginTurn(GameAction):
	"""
	Make a player begin the turn
	"""
	PLAYER = ActionArg()

	def do(self, source, player):
		source.manager.step(source.next_step, Step.MAIN_READY)
		source.turn += 1
		if Config.LOGINFO:
			Config.log("BeginTurn.do","%s begins turn %i"%(player, source.turn))
		source.current_player = player
		source.manager.step(source.next_step, Step.MAIN_START_TRIGGERS)
		source.manager.step(source.next_step, source.next_step)
		self.broadcast(source, EventListener.ON, player)
		source._begin_turn(player)
		player.times_spells_played_this_turn = 0 # DAL_603
		player.spells_played_this_turn=[] # DAL_558
		player.died_this_turn=[] # CORE_EX1_190

class BeginBattle(GameAction):
	"""
	Make a player begin the battle ( battlegrounds )
	"""
	PLAYER = ActionArg()
	def do(self, source, player):
		source.manager.step(source.next_step, Step.MAIN_READY)
		if Config.LOGINFO:
			Config.log("BeginBattle.do","%s begins a battle"%(player))
		source.manager.step(source.next_step, Step.MAIN_START_TRIGGERS)
		source.manager.step(source.next_step, source.next_step)
		self.broadcast(source, EventListener.ON, player)
		source.no_drawing_at_turn_begin=True
		source._begin_turn(player)



class Concede(GameAction):
	"""
	Make a player concede
	"""
	PLAYER = ActionArg()

	def do(self, source, player):
		player.playstate = PlayState.CONCEDED
		source.game.check_for_end_game()


class Disconnect(GameAction):
	"""
	Make a player disconnect
	"""
	PLAYER = ActionArg()

	def do(self, source, player):
		player.playstate = PlayState.DISCONNECTED


class Deaths(GameAction):
	"""
	Process all deaths in the PLAY Zone.
	"""
	def do(self, source, *args):
		#source.game.refresh_auras()  # 
		source.game.process_deaths()


class Death(GameAction):
	"""
	Move target to the GRAVEYARD Zone.
	ENTITY = ActionArg()
	"""
	ENTITY = ActionArg()
	def do(self, source, entity):
		if entity.death_processed:## One entity is killed only once.
			return
		entity.death_processed=True
		if Config.LOGINFO:
			Config.log("Death.do","Processing Death for %r"% ( entity))
		source.game.refresh_auras()
		if not entity in entity.controller.death_log:
			entity.controller.add_death_log(entity)
		if getattr(source.game, 'this_is_battle',False):## battle of battlegrounds
			if hasattr(entity, 'deepcopy_original'):
				if hasattr(entity.deepcopy_original,'killed_in_former_battle'):
					entity.deepcopy_original.killed_in_former_battle=True
		if entity.type == CardType.MINION:
			self.broadcast(source, EventListener.ON, entity)
			self.broadcast(source, EventListener.AFTER, entity)
		if entity.id == 'SW_323'and entity._Asphyxia_=='alive': #The king rat
			source.game.queue_actions(source, [Asphyxia(entity)])
		if hasattr(entity, "deathrattles") and hasattr(entity, "deathrattle_valid") and entity.deathrattles and entity.deathrattle_valid:
			source.game.queue_actions(source, [Deathrattle(entity)])
		if entity.reborn:# 
			source.game.queue_actions(source, [Reborn(entity)])
		if entity.id== 'DRG_253':#  Dwarven Sharpshooter
			ChangeHeroPower(entity.controller, "HERO_05bp").trigger(entity)
		if entity.id!='RLK_506t' and entity.id!='RLK_061t':# Risen Groom, Risen Footmen
			AddCorpse(entity.controller, 1).trigger(entity)
		if entity.controller.gorefiend_cardID!=None:
			if len(entity.controller.field)<entity.controller.game.MAX_MINIONS_ON_FIELD:### 7
				newcard = entity.controller.card(entity.controller.gorefiend_cardID)
				newcard.zone=Zone.PLAY


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
		if getattr(player.game,'turn_end_effects_twice',False)==True:
			self.broadcast(source, EventListener.ON, player)
		source.game.refresh_auras()  # XXX 
		source.game._end_turn()


class Joust(GameAction):
	"""
	Perform a joust between a challenger and a defender.
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
		if Config.LOGINFO:
			Config.log("Jouse.do","Jousting %r vs %r"%(challenger, defender))
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
			cards = cards.eval(source.game.targetable_allcards + source.game.graveyard, source) # game? entities + decks?
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
		if len(self._args)>=3:
			option = self._args[2]
		else: 
			option=None
		return player, cards, option

	def do(self, source, player, cards, option=None):
		if len(cards) == 0:
			if Config.LOGINFO:
				Config.log("Choice.do","No choice for this condition."%())
			return
		if Config.LOGINFO:
			Config.log("Choice.do","%r choice from %r"%(player, cards))
		self.next_choice = player.choice
		player.choice = self
		player.choiceText = source.choiceText
		self.source = source
		self.player = player
		self.cards = cards
		self.option = option
		self.min_count = 1
		self.max_count = 1
		self.broadcast(self.player, EventListener.ON, self.player, self.cards, None)

	def choose(self, card):
		if card not in self.cards:
			raise InvalidAction("%r is not a valid choice (one of %r)" % (card, self.cards))
		self.broadcast(self.player, EventListener.AFTER, self.player, self.cards, card)
		for action in self.callback:
			self.source.game.trigger(
				self.source, [action], [self.player, self.cards, card])
		self.player.choice = self.next_choice

class GenericChoice(Choice):
	def choose(self, card):
		private_casts_when_chosen = ['YOP_024t']
		self.next_choice=None
		super().choose(card)
		if not hasattr(card, 'controller') or not hasattr(card, 'type'):
			return
		if Config.LOGINFO:
			Config.log("GenericChoice.choose","%s chooses %r"%(card.controller.name, card))
		for _card in self.cards:
			if _card is card:
				if card.type == CardType.HERO_POWER:
					script_data_num=self.player.hero.power.script_data_num_1
					new_card = self.player.card(_card.id)# make a new copy
					new_card.zone = Zone.PLAY
					new_card.script_data_num_1 = script_data_num
					new_card.data.tags[GameTag.TAG_SCRIPT_DATA_NUM_1] = script_data_num
				elif len(self.player.hand) < self.player.max_hand_size:
					new_card = self.player.card(_card.id)# make a new copy
					new_card.zone = Zone.HAND
					if new_card.id in private_casts_when_chosen:
						Play(new_card,None,None,None).trigger(card.controller)
		# we may return the new card. 


class GenericChoiceOnDeck(Choice):
	## choose from Deck 
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		if Config.LOGINFO:
			Config.log("GenericChoiceOnDeck.choose","%s chooses %r"%(card.controller.name, card))
		for _card in self.cards:# cards are from Deck
			if _card is card:
				if len(self.player.hand) < self.player.max_hand_size:
					_card.zone = Zone.HAND
				else:
					_card.discard()
			else:
				_card.discard()





class GenericChoicePlay(GenericChoice):## 
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		controller = self.player
		for new_card in controller.hand:
			if new_card.id == card.id:
				Summon(controller, new_card).trigger(self.source)
				break
		pass

class GenericChoiceChangeHeropower(GenericChoice):## 
	def choose(self, card):
		self.next_choice=None
		self.player.choice = None
		super().choose(card)
		controller = self.player
		if card.type != CardType.HERO_POWER:
			return
		ChangeHeroPower(controller, card).trigger(controller)
		pass


class GenericChoiceBattlecry(GenericChoice):## 
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		controller = self.player
		for new_card in controller.hand:
			if new_card.id == card.id:
				Battlecry(new_card, new_card.target).trigger(new_card)
				#new_card.zone=Zone.PLAY# 必要？
				break
		pass

class GenericChoiceSecret(Choice):## 
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		card.zone=Zone.SECRET
		pass



class GenericChoicePlayOnDeck(Choice):## callbackで対応可能
	def choose(self, card):
		self.next_choice=None
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
	Make the source player play a card, on a target or None.
	Choose play action from a choose or None.
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
		#if card.cant_play:
		#	if Config.LOGINFO:
		#		Config.log("Play.do)%r can't be played "%(card))
		#	return

		player = source
		player.spell_and_damage=False
		if Config.LOGINFO:
			Config.log("Play.do","%s plays %r (target=%r, index=%r)"%(player, card, target, index))

		player.pay_cost(card, card.cost)
		player.add_play_log(card, card2=choose)

		card.target = target
		card._summon_index = index

		battlecry_card = choose or card
		# We check whether the battlecry will trigger, before the card.zone changes
		if battlecry_card.battlecry_requires_target() and not target:
			if Config.LOGINFO:
				Config.log("Play.do","%r requires a target for its battlecry. Will not trigger." % card)
			trigger_battlecry = False
		else:
			trigger_battlecry = True

		if card is card.controller.hand[0] or card is card.controller.hand[-1]:
			trigger_outcast = True
		else:
			trigger_outcast = False

		card.zone = Zone.PLAY###  battlecry_card or card?
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

		# "Can't Play" (aka Counter) means triggers don't happen either-> resign
		if not card.cant_play:
			#corrupt:
			Corrupt(player, card).trigger(player)
			#spellpower_by_spell
			if card.type==CardType.SPELL and getattr(card, 'spellpower_by_spell',0)>0:
				player.spellpower_by_spell+=getattr(card, 'spellpower_by_spell',0)
			#outcast
			if trigger_outcast and card.get_actions("outcast"):
				player.add_outcast_play_log(card)
				source.game.trigger(card, card.get_actions("outcast"), event_args=None)
			elif trigger_battlecry:
				source.game.queue_actions(card, [Battlecry(battlecry_card, card.target)])
				if hasattr(player,'spell_cast_twice') and player.spell_cast_twice:
					if Config.LOGINFO:
						Config.log("Play.do","spell %r is casted twice." % card)
					source.game.queue_actions(card, [Battlecry(battlecry_card, card.target)])
				elif hasattr(battlecry_card,'spell_cast_twice') and battlecry_card.spell_cast_twice:
					if Config.LOGINFO:
						Config.log("Play.do","spell %r is casted twice." % card)
					source.game.queue_actions(card, [Battlecry(battlecry_card, card.target)])

			source.game.refresh_auras()
			# If the play action transforms the card (eg. Druid of the Claw), we
			# have to broadcast the morph result as minion instead.
			played_card = card.morphed or card
			if played_card.type in (CardType.MINION, CardType.WEAPON):
				summon_action.broadcast(player, EventListener.AFTER, player, played_card)
			self.broadcast(player, EventListener.AFTER, player, played_card, target)
		elif card.zone!=Zone.GRAVEYARD: ## if card.cant_play
			card.zone=Zone.GRAVEYARD
			

		player.combo = True
		player.last_card_played = card
		player.cards_played_this_turn += 1
		if card.type == CardType.MINION:
			player.minions_played_this_turn += 1

		card.target = None
		card.choose = None

class BG_Play(GameAction):
	"""
	Make the source player play a card, on a target or None.
	Choose play action from a choose or None.
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
		if Config.LOGINFO:
			Config.log("BG_Play.do","%s plays %r (target=%r, index=%r)"%(player, card, target, index))
		player.add_play_log(card)

		card.target = target
		card._summon_index = index
		battlecry_card = choose or card
		# We check whether the battlecry will trigger, before the card.zone changes
		if battlecry_card.battlecry_requires_target() and not target:
			if Config.LOGINFO:
				Config.log("BG_Play.do","%r requires a target for its battlecry. Will not trigger." % card)
			trigger_battlecry = False
		else:
			trigger_battlecry = True
		card.zone = Zone.PLAY
		if card.type == CardType.MINION:
			player.add_summon_log(card)
		# Remember cast on friendly characters
		if target and target.controller == source:
			card.cast_on_friendly_characters = True
		summon_action = Summon(player, card)
		if card.type in (CardType.MINION, CardType.WEAPON):
			self.queue_broadcast(summon_action, (player, EventListener.ON, player, card))
		self.broadcast(player, EventListener.ON, player, card, target)
		for value in player.game.parent.BG_Gold.values():
			if card.id==value:
				triple_bonus = Give(player, 'TB_BaconShop_Triples_01').trigger(source)
				triple_bonus = triple_bonus[0]
				if triple_bonus==[]:
					break
				triple_bonus = triple_bonus[0]
				triple_bonus.tags[GameTag.TAG_SCRIPT_DATA_NUM_1] = min(player.tavern_tier+1, 6)
				break
			pass
		self.resolve_broadcasts()
		#Corrupt(player, card).trigger(player)
		# "Can't Play" (aka Counter) means triggers don't happen either
		if not card.cant_play:
			if trigger_battlecry:
				source.game.queue_actions(card, [Battlecry(battlecry_card, card.target)])
			played_card = card.morphed or card
			if played_card.type in (CardType.MINION, CardType.WEAPON):
				summon_action.broadcast(player, EventListener.AFTER, player, played_card)
			self.broadcast(player, EventListener.AFTER, player, played_card, target)
		player.combo = True
		player.last_card_played = card
		#player.cards_played_this_turn += 1
		#if card.type == CardType.MINION:
		#	player.minions_played_this_turn += 1
		card.target = None
		card.choose = None


class Activate(GameAction):
	PLAYER = ActionArg()
	CARD = CardArg()
	TARGET = ActionArg()

	def get_args(self, source):
		return (source, ) + super().get_args(source)

	def do(self, source, player, heropower, target=None):

		if target!=None and getattr(target, 'cant_be_targeted_by_hero_powers'):
			return

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
			if Config.LOGINFO:
				Config.log("Overload.do","%r cannot overload %s", source, player)
			return
		if Config.LOGINFO:
			Config.log("Overload.do","%r overloads %s for %i"%(source, player, amount))
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
		return "<Action: %s(%s)>" % (self.__class__.__name__, ", ".join(args))

	def __mul__(self, value):
		self.times = value
		return self

	def eval(self, selector, source):
		if isinstance(selector, Entity):
			return [selector]
		else:
			return selector.eval(source.game.targetable_allcards+source.game.graveyard, source) # 

	def get_target_args(self, source, target):
		ret = []
		for k, v in zip(self.ARGS[1:], self._args[1:]):
			if isinstance(v, Selector):
				# evaluate Selector arguments
				v = v.eval(source.game.targetable_allcards+source.game.graveyard, source)# 
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
			ret = t.eval(source.game.targetable_allcards+source.game.graveyard, source) ##
		if not ret:
			return []
		if not hasattr(ret, "__iter__"):
			# Bit of a hack to ensure we always get a list back
			ret = [ret]
		return ret

	def trigger(self, source):
		ret = []

		if self.source is not None:
			source = self.source.eval(source.game.targetable_allcards, source) ## 
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
			if Config.LOGINFO:
				Config.log("TargetedAction.trigger","%s triggering %r targeting %r"%(source, self, targets))
			for target in targets:
				target_args = self.get_target_args(source, target)
				from .player import Player
				from .card import PlayableCard
				from .game import Game
				if isinstance(source, Player):
					source.add_targetedaction_log({'class':self,'source':source,'target':target,'target_args':target_args, 'turn':source.controller.game.turn})## log for action
				elif isinstance(source, PlayableCard):
					source.controller.add_targetedaction_log({'class':self,'source':source,'target':target,'target_args':target_args, 'turn':source.controller.game.turn})## log for action
				elif isinstance(source, Game):
					target.controller.add_targetedaction_log({'class':self,'source':source,'target':target,'target_args':target_args, 'turn':source.turn})## log for action
				ret.append(self.do(source, target, *target_args))

				for action in self.callback:
					if Config.LOGINFO:
						Config.log("TargetedAction.trigger","%r queues up callback %r"%(self, action))
					ret += source.game.queue_actions(source, [action], event_args=[target] + target_args)

		self.resolve_broadcasts()

		return ret


class Buff(TargetedAction):
	"""
	Buff character targets with Enchantment an id
	NOTE: Any Card can buff any other Card. The controller of the
	Card that buffs the target becomes the controller of the buff.
	TARGET = ActionArg()
	BUFF = ActionArg()
	"""
	TARGET = ActionArg()
	BUFF = ActionArg()

	def get_target_args(self, source, target):
		buff = self._args[1]
		buff = source.controller.card(buff)
		buff.source = source
		self.buff=buff
		return [buff]

	def do(self, source, target, buff):
		kwargs = self._kwargs.copy()
		if target==None or target==[]:
			return
		for k, v in kwargs.items():
			if isinstance(v, LazyValue):
				v = v.evaluate(source)
			setattr(buff, k, v)
		if source.controller==target.controller and target.type==CardType.HERO:##FRIENDLY_HERO
			source.controller.lost_in_the_park = buff.atk##  SW_428 Lost in the park
		self.broadcast(source, EventListener.ON, target, buff)
		ret = buff.apply(target)
		if Config.LOGINFO:
			Config.log("Buff.do","Buff %s to %s"%(buff, target))
		self.broadcast(source, EventListener.AFTER, target, buff)
		return ret

class BuffPermanently(Buff):
	def do(self, source, target, buff):
		ret = super().do(source, target, buff)
		#buff.apply(target)
		if Config.LOGINFO:
			Config.log("BuffPermanently.do","Buff also to the deepcopy original"%())
		if target.deepcopy_original:
			buff.apply(target.deepcopy_original)
		return ret

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

class RemoveAllBuff(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		buffList = target.buffs
		for bf in reversed(buffList):
			target.buffs.remove(bf)
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
		if Config.LOGINFO:
			Config.log("EatsCard.do","ate %r from opponent's hand"%(other))
			Config.log("EatsCard.do","%r gains +%d/+%d"%(target, other.atk,other.max_health))
		other.discard()
		pass

class Bounce(TargetedAction):
	"""
	Bounce minion targets on the field back into the hand.
	"""
	TARGET=ActionArg()
	def do(self, source, target):
		if len(target.controller.hand) >= target.controller.max_hand_size:
			if Config.LOGINFO:
				Config.log("Bounce.do","%r is bounced to a full hand and gets destroyed"%(target))
			return source.game.queue_actions(source, [Destroy(target)])
		else:
			if Config.LOGINFO:
				Config.log("Bounce.do","%r is bounced back to %s's hand"%(target, target.controller))
			target.zone = Zone.HAND
			self.broadcast(source, EventListener.ON, target)


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
	Predamage target by an amount.
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
			amount = source.game.trigger_actions(source, [Damage(target)])
			if isinstance(amount, list):
				amount=amount[0]
			if isinstance(amount, list):
				amount=amount[0]
			return amount
		return 0


class PutOnTop(TargetedAction):
	"""
	Put card on deck top
	"""
	TARGET = ActionArg()
	CARD = CardArg()

	def do(self, source, target, cards):
		if Config.LOGINFO:
			Config.log("PutOnTop.do","%r put on %s's deck top"%(cards, target))
		if not isinstance(cards, list):
			cards = [cards]

		for card in cards:
			if card.controller != target:
				card.zone = Zone.SETASIDE
				card.controller = target
			if len(target.deck) >= target.max_deck_size:
				if Config.LOGINFO:
					Config.log("PutOnTop.do","Put (%r) fails because %r's deck is full"%(card, target))
				continue
			card.zone = Zone.DECK
			card, card.controller.deck[-1] = card.controller.deck[-1], card
		return cards


class Damage(TargetedAction):
	"""
	Damage target by an amount.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def get_target_args(self, source, target):
		return [target.predamage]

	def do(self, source, target, amount):
		# in method '_hit', we manage divine_shield and damage amount.
 
		if hasattr(target, 'divine_shield') and target.divine_shield:
			target.game.trigger_actions(source, [LoseDivineShield(target)])
			cards=[card for card in target.buffs if getattr(card, 'divine_shield', 0)==1]
			for card in cards:
				#card.data.tags[GameTag.DIVINE_SHIELD]=False
				card.divine_shield=False
			target.divine_shield = False
			if Config.LOGINFO:
				Config.log("Damage.do","%r's divine shield prevents %i damage."%( target, amount))
			return 0
		if 'SW_091t5' in [buff.id for buff in target.controller.buffs]:
			controller = target.controller
			if controller==controller.game.current_player:
				if Config.LOGINFO:
					Config.log("Damage.do","%r has a buff Blightborn and it prevents %i damage."%( target, amount))
				Hit(controller.opponent.hero, amount).trigger(controller)
			return 0
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
			if hasattr(source, "lifesteal") and source.lifesteal and source.type == CardType.ENCHANTMENT:
				source.owner.heal(source.controller.hero, amount)
			elif hasattr(source, "lifesteal") and source.lifesteal and source.type != CardType.WEAPON:
				source.heal(source.controller.hero, amount)
			self.broadcast(source, EventListener.ON, target, amount, source)
			# poisonous can not destory hero
			if hasattr(source, "poisonous") and source.poisonous and (
				target.type != CardType.HERO and source.type != CardType.WEAPON):
				if Config.LOGINFO:
					Config.log("Damage.do","%r destroys %r by poison"%(source, target))
				#target.destroy()
				Destroy(target).trigger(source)
			Deaths().trigger(source.controller)###ここに追加してみた
		return amount


class Deathrattle(TargetedAction):
	"""
	Trigger deathrattles on card targets.
	TARGET = ActionArg()
	"""
	TARGET = ActionArg()
	def do(self, source, target):
		target.deathrattle_valid=False
		for deathrattle in target.deathrattles:
			if callable(deathrattle):
				actions = deathrattle(target)
			else:
				actions = deathrattle
			self.broadcast(source, EventListener.ON, target)
			source.game.queue_actions(target, actions)

			if target.controller.extra_deathrattles:
				if Config.LOGINFO:
					Config.log("Deathrattle.do","Triggering deathrattles for %r again"%target)
				source.game.queue_actions(target, actions)
			if getattr(source, 'extra_deathrattles_minion', False)==True:## RLK_912
				if Config.LOGINFO:
					Config.log("Deathrattle.do","Triggering deathrattles for %r again"%target)
				source.game.queue_actions(target, actions)
			if target.controller.extra_extra_deathrattles: ## TB_BaconUps_055
				if Config.LOGINFO:
					Config.log("Deathrattle.do","Triggering deathrattles for %r again and again"% target)
				source.game.queue_actions(target, actions)
				source.game.queue_actions(target, actions)

class Battlecry(TargetedAction):
	"""
	Trigger Battlecry on card targets
	CARD = CardArg()
	TARGET = ActionArg()
	"""
	CARD = CardArg()
	TARGET = ActionArg()

	def get_target_args(self, source, target):
		arg = self._args[1]
		if isinstance(arg, Selector):
			arg = arg.eval(source.game.targetable_allcards, source) ##
			assert len(arg) == 1
			arg = arg[0]
		return [arg]

	def do(self, source, card, target):
		player = card.controller

		if source.type==CardType.SPELL and target!=None and getattr(target, 'cant_be_targeted_by_spells'):
			return

		if card.has_combo and player.combo:
			if Config.LOGINFO:
				Config.log("Battlecry.do","Activating %r combo targeting %r"%(card, target))
			actions = card.get_actions("combo")
		else:
			if Config.LOGINFO:
				Config.log("Battlecry.do","Activating %r action targeting %r"%(card, target))
			actions = card.get_actions("play")

		source.target = target
		source.game.main_power(source, actions, target)
		if card.has_battlecry:
			if hasattr(actions,'__iter__'):
				for action in actions:
					player.add_battlecry_log({'card':card, 'action':action, 'target':target, 'requirements':card.requirements})
			else:
				player.add_battlecry_log(actions)

		if player.extra_battlecries and card.has_battlecry:
			source.game.main_power(source, actions, target)
		elif player.extra_extra_battlecries and card.has_battlecry: ## golden Brann :TB_BaconUps_045
			source.game.main_power(source, actions, target)
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
		#if target.delayed_destruction:
		if target.zone == Zone.PLAY:
			#  If the card is in PLAY, it is instead scheduled to be destroyed
			# It will be moved to the graveyard on the next Death event
			if Config.LOGINFO:
				Config.log("Destroy.do","%r marks %r for imminent death"%(source, target))
			if target.type == CardType.ENCHANTMENT:
				target.remove()
			else:
				self.broadcast(source, EventListener.ON, target)
				target.to_be_destroyed = True
				source.game.process_deaths()
		else:
			if Config.LOGINFO:
				Config.log("Destroy.do","%r destroys %r"%(source, target))
			if target.type == CardType.ENCHANTMENT:
				target.remove()
			else:
				self.broadcast(source, EventListener.ON, target)				
				target.zone = Zone.GRAVEYARD

class DestroyOriginal(TargetedAction):
	"""
	Destroy character targets. (in battlegrounds)
	"""
	TARGET = ActionArg()
	def do(self, source, target):
		if not target:
			return
		if not target.deepcopy_original:
			return
		if Config.LOGINFO:
			Config.log("Destroy.do","%r destroys %r"%(source, target.deepcopy_original))
		if target.deepcopy_original.type == CardType.ENCHANTMENT:
			target.remove()
			target.deepcopy_original.remove()
		else:
			target.zone = Zone.GRAVEYARD
			target.deepcopy_original.zone = Zone.GRAVEYARD



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
		elif source.data and source.data.card_class != CardClass.NEUTRAL:
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
		if Config.LOGINFO:
			Config.log("Discover.do","%r discovers %r for %s"%(source, cards, target))
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
		self.broadcast(source, EventListener.ON, target, card, source)
		card.draw()
		card.controller.add_give_log(card)
		self.broadcast(source, EventListener.AFTER, target, card, source)

		return [card]


class Fatigue(TargetedAction):
	"""
	Hit a player with a tick of fatigue
	"""
	def do(self, source, target):
		if target.cant_fatigue:
			if Config.LOGINFO:
				Config.log("Fatigue.do","%s can't fatigue and does not take damage", target)
			return
		target.fatigue_counter += 1
		if Config.LOGINFO:
			Config.log("Fatigue.do","%s takes %i fatigue damage"%(target, target.fatigue_counter))
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
	Make target player target draw up to an amount cards minus their hand count.
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
	Make hero targets gain an amount armor.
	TARGET = ActionArg(): hero
	AMOUNT = IntArg()
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
	Give player targets a Mana crystals.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def do(self, source, target, amount):
		target.max_mana = max(target.max_mana + amount, 0)


class SpendMana(TargetedAction):
	"""
	Make player targets spend an amount Mana.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def do(self, source, target, amount):
		target.used_mana = max(target.used_mana + amount, 0)
		self.broadcast(source, EventListener.AFTER, target, amount)



class Give(TargetedAction):
	"""
	Give player targets card an id.
	TARGET = ActionArg()
	CARD = CardArg()	
	"""
	TARGET = ActionArg()
	CARD = CardArg()

	def do(self, source, target, cards):
		if Config.LOGINFO:
			Config.log("Give.do","Giving %r to %s"%(cards, target))
		ret = []
		if not hasattr(cards, "__iter__"):
			# Support Give on multiple cards at once (eg. Echo of Medivh)
			cards = [cards]
		if len(cards)>0:
			self.broadcast(source, EventListener.ON, target, cards[0])
		for card in cards:
			assert hasattr(target, 'hand'), "target must have attr -hand-"
			if len(target.hand) >= target.max_hand_size:
				if Config.LOGINFO:
					Config.log("Give.do","Give(%r) fails because %r's hand is full"%(card, target))
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
			card.controller.add_give_log(card)
			card.controller.game.mixing_concoction(card.controller) # 25.0 RLK_570

			# if card is 'casts_when_drawn' then immediately play.  
			card.game.casts_when_drawn(card, card.controller)
			WhenDrawn(card.controller, card).trigger(source)
			ret.append(card)
			## in battlegrounds, we need check if a triple happens
		if len(cards)>0:
			self.broadcast(source, EventListener.AFTER, target, cards[0])
		return ret

class WhenDrawn(TargetedAction):
	TARGET = ActionArg()
	CARD = CardArg()
	def do(self, source, target, card):
		self.broadcast(source, EventListener.ON, target, card)
		self.broadcast(source, EventListener.AFTER, target, card)

class GiveInBattle(TargetedAction):
	TARGET = ActionArg()
	CARD = ActionArg()
	def do(self, source, target, card):
		controller=target.deepcopy_original
		Give(controller, card).trigger(source)


class Hit(TargetedAction):
	"""
	Hit character targets by an amount.
	"""
	TARGET = ActionArg()
	AMOUNT = ActionArg()

	def do(self, source, target, amount):
		if target.type==CardType.LOCATION:
			return
		if source.type==CardType.SPELL and getattr(target, 'cant_be_targeted_by_spells'):
			return
		if source.type==CardType.HERO_POWER and getattr(target, 'cant_be_targeted_by_hero_powers'):
			return
		if Config.LOGINFO:
			Config.log("Hit.do","%s hits %s by %d"%(source, target, amount))
		amount = source.get_damage(amount, target)
		# if target is hero and target.controller has buff 'AV_146e'(Take half damage, rounded up)
		if target.type==CardType.HERO and target.controller.take_half_damage:
			if amount%2==0:
				amount = amount/2
			else:
				amount = (amount+1)/2
		if target.type==CardType.HERO and target.take_only_one_damage:
			if amount>0:
				amount=1
		#if source.type==CardType.SPELL and source.poisonous:
		#	killed_by_poisonous_spell=True
		if amount:
			#if isinstance(source,PlayableCard):
			#self.broadcast(source, EventListener.ON, target, amount)
			target.attacker=source ## 
			if hasattr(source, 'honorable_kill') and source.honorable_kill:
				if target.type==CardType.WEAPON and target==source:## when decreasing his durability
					pass
				elif target.type==CardType.WEAPON:## when decreasing other's durability
					pass
				else:
					target_health = target.health
					if target_health == amount:
						if Config.LOGINFO:
							Config.log("Hit.do","%s hits %s and gets honorable kill"%(source, target))
						target.honorably_killed = True
						event_args=[target]
						if source.type==CardType.HERO and source.controller.weapon!=None :
							actions = source.controller.weapon.get_actions("honorable_kill")
							source.game.trigger(source.controller.weapon, actions,event_args=event_args)
						else:
							actions = source.get_actions("honorable_kill")
							source.game.trigger(source, actions,event_args=event_args)
						for buff in source.buffs:
							if hasattr(buff, 'honorable_kill'):
								actions = buff.get_actions('honorable_kill')
								source.game.trigger(source, actions, event_args=event_args)
			ret = source.game.queue_actions(source, [Predamage(target, amount)])
			#self.broadcast(source, EventListener.AFTER, target, amount)
			return ret[0][0]
		return 0

class ActivateHit(Hit):
	"""
	HeroPower hits character targets by an amount.
	"""
	TARGET = ActionArg()
	AMOUNT = ActionArg()

	def do(self, source, target, amount):
		self.broadcast(source, EventListener.ON, target, amount)
		ret = super().do(source, target, amount)
		self.broadcast(source, EventListener.AFTER, target, amount)
		return ret


class Honorable_kill(TargetedAction):
	TARGET=ActionArg()
	AMOUNT=IntArg()
	TARGETEDACTION=ActionArg()
	def do(self, source, target, amount, targetedaction):
		if target.health==amount:
			self.broadcast(source, EventListener.ON, target, amount, targetedaction)
			for action in targetedaction:
				action.trigger(source)

class SplitHit(TargetedAction):
	"""
	Hit character targets by  an amount.
	TARGET = ActionArg()#CONTROLLER
	TARGETS = ActionArg()
	AMOUNT = ActionArg()
	"""
	TARGET = ActionArg()#CONTROLLER
	TARGETS = ActionArg()
	AMOUNT = ActionArg()

	def do(self, source, target, targets, amount):
		if Config.LOGINFO:
			Config.log("SplitHit.do","%s hits %s splitly by %d"%(source, targets, amount))
		if not isinstance(targets, list):
			targets = [targets]
		if targets==[]:
			return
		ret = []
		amount = source.controller.get_spell_damage(amount)## adding spellpower.
		if amount:
			for repeat in range(amount):
				target = random.choice(targets)
				if source.get_damage(1, target)>0:
					target.attacker=source ## 
					if hasattr(source, 'honorable_kill') and source.honorable_kill:
						if target.type==CardType.WEAPON and target==source:## when decreasing durability
							pass
						else:
							target_health = target.health
							if target_health == 1:
								if Config.LOGINFO:
									Config.log("Hit.do","%s hits %s and gets honorable kill"%(source, target))
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
					ret.append(Predamage(target, 1))
			return source.game.queue_actions(source, ret)[0][0]
		return 0

class Heal(TargetedAction):
	"""
	Heal character targets by a amount.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def do(self, source, target, amount):
		if target.type!=CardType.MINION and target.type!=CardType.HERO:
			return
		if source.controller.healing_as_damage:
			return source.game.queue_actions(source, [Hit(target, amount)])

		amount <<= source.controller.healing_double
		amount = min(amount, target.damage)
		if amount:
			# Undamaged targets do not receive heals
			if Config.LOGINFO:
				Config.log("Heal.do","%r heals %r for %i"%(source, target, amount))
			target.damage -= amount
			self.queue_broadcast(self, (source, EventListener.ON, target, amount))


class ManaThisTurn(TargetedAction):
	"""
	Give player targets a amount Mana this turn.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def do(self, source, target, amount):
		if target.type != CardType.PLAYER:
			return
		target.temp_mana += min(target.max_resources - target.mana, amount)

class Manathirst(GameAction):
	"""
	"""
	def do(self, source, amount, action1, action2, target=None):
		mana = source.controller.mana
		manathirst=amount-source.cost
		#manathirst=getattr(source, 'manathirst', 0)
		#assert isinstance(action1, list) amd isinstance(action2, list), ""
		if mana==manathirst:
			if action1!=[]:
				for action in action1:
					if isinstance(action, TargetedAction) or isinstance(action, GameAction) or isinstance(action, Choice):
						action.trigger(source)
		else:
			if action2!=[]:
				for action in action2:
					if isinstance(action, TargetedAction) or isinstance(action, GameAction) or isinstance(action, Choice):
						action.trigger(source)
		pass

class ManaThisTurnOnly(TargetedAction):
	"""
	Give player targets a amount Mana this turn.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def do(self, source, target, amount):
		if target.type != CardType.PLAYER:
			return
		target.used_mana -= amount ### battlegrounds version


class Mill(TargetedAction):
	"""
	Mill a count cards from the top of the player targets' deck.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def do(self, source, target, count):
		target.mill(count)


class Morph(TargetedAction):
	"""
	Morph minion target into a minion id
	TARGET = ActionArg()
	CARD = CardArg()
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
			if Config.LOGINFO:
				Config.log("Morph.do","Morphing %r into %r"%(target, card))
			target_zone = target.zone
			if card.zone != target_zone:
				# Transfer the zone position
				card._summon_index = target.zone_position
				# In-place morph is OK, eg. in the case of Lord Jaraxxus
				card.zone = target_zone
			target.clear_buffs()
			target.zone = Zone.SETASIDE
			if target in target.controller.field:
				target.controller.field.remove(target)
			target.morphed = card
			self.broadcast(source, EventListener.ON, target, card)
			self.broadcast(source, EventListener.AFTER, target, card)
			return card


class SW_078_Morph(TargetedAction):
	"""
	Morph minion target into a minion id
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
			if Config.LOGINFO:
				Config.log("SW_078_Morph.do","Morphing %r into %r"%(target, card))
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
			if Config.LOGINFO:
				Config.log("DMF_108_Morph.do","Morphing %r into %r", target, card)
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
	Refill a amount mana crystals from player targets.
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
			if Config.LOGINFO:
				Config.log("Retarget.do","Retargeting %r's attack to %r"%(target, new_target))
			source.game.proposed_defender.defending = False
			source.game.proposed_defender = new_target
		else:
			if Config.LOGINFO:
				Config.log("Retarget.do","Retargeting %r from %r to %r"%(target, target.target, new_target))
			target.target = new_target

		return new_target


class Reveal(TargetedAction):
	"""
	Reveal secret targets.
	"""
	TARGET = ActionArg()
	def do(self, source, target):
		if Config.LOGINFO:
			Config.log("Reveal.do","Revealing secret %r"%target)
		target.controller.add_reveal_log(target)
		self.broadcast(source, EventListener.ON, target)
		target.zone = Zone.GRAVEYARD
		self.broadcast(source, EventListener.AFTER, target)


class SetCurrentHealth(TargetedAction):
	"""
	Sets the current health of the character target to a amount.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def do(self, source, target, amount):
		if Config.LOGINFO:
			Config.log("SetCurrentHealth.do","Setting current health on %r to %i"%(target, amount))
		maxhp = target.max_health
		target.damage = max(0, maxhp - amount)

class SetMaxMana(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self,source, target, amount):
		if Config.LOGINFO:
			Config.log("SetMaxMana.do","Setting max_mana on %r to %i"%(target, amount))
		target._max_mana = amount
		pass


class SetTag(TargetedAction):
	"""
	Sets targets' given tags.
	"""
	TARGET = ActionArg()
	TAGS = ActionArg()

	def do(self, source, target, tags):
		if Config.LOGINFO:
			Config.log("SetTag.do","Setting current tag on %r to %s"%(target, tags))
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
			if Config.LOGINFO:
				Config.log("UnsetTag.do","%s unset tag %s"%(target, tag))
			target.tags[tag] = False


class Silence(TargetedAction):
	"""
	Silence minion targets.
	"""
	TARGET = ActionArg()
	def do(self, source, target):
		if Config.LOGINFO:
			Config.log("Silence.do","Silencing %r"%target)
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
	Make player targets summon a id onto their field.
	This works for equipping weapons as well as summoning minions.
	TARGET = ActionArg()#CONTROLLER
	CARD = CardArg()
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
			if Config.LOGINFO:
				Config.log("Summon.do","<><><><><><><><><><><><>")
				Config.log("Summon.do","%s is not a player, he/she cannot summon anything"% target)
				Config.log("Summon.do","<><><><><><><><><><><><>")
			return
		if Config.LOGINFO:
			Config.log("Summon.do","%s summons %r"%(target, cards))

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
			### Eternal_Knight ### new 25.2.2
			if card.id=='BG25_008':
				if card.controller.eternal_knight_powered_up>0: ### Eternal_Knight
					Buff(card, 'BG25_008pe',
						atk=card.controller.eternal_knight_powered_up,
						max_health=card.controller.eternal_knight_powered_up
						).trigger(card.controller)		
			elif card.id=='BG25_008_G':
				if card.controller.eternal_knight_powered_up>0: ### Eternal_Knight(gold)
					Buff(card, 'BG25_008pe',
						atk=card.controller.eternal_knight_powered_up*2,
						max_health=card.controller.eternal_knight_powered_up*2
						).trigger(card.controller)		

		return cards


class Shuffle(TargetedAction):
	"""
	Shuffle card targets into player target's deck.
	"""
	TARGET = ActionArg()
	CARD = CardArg()

	def do(self, source, target, cards):
		if Config.LOGINFO:
			Config.log("Shuffle.do","%r shuffles into %s's deck"%(cards, target))
		if not isinstance(cards, list):
			cards = [cards]
		if cards[0]==None:
			return
		for card in cards:
			if card.controller != target:
				card.zone = Zone.SETASIDE
				card.controller = target
			if len(target.deck) >= target.max_deck_size:
				if Config.LOGINFO:
					Config.log("Shuffle.do","Shuffle(%r) fails because %r's deck is full"%(card, target))
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
		if Config.LOGINFO:
			Config.log("ShuffleBuff.do","%r shuffles into %s's deck"%( cards, target))
		if not isinstance(cards, list):
			cards = [cards]
		for card in cards:
			Buff(card,buff).trigger(source)
			if card.controller != target:
				card.zone = Zone.SETASIDE
				card.controller = target
			if len(target.deck) >= target.max_deck_size:
				if Config.LOGINFO:
					Config.log("ShuffleBuff.do","Shuffle(%r) fails because %r's deck is full", card, target)
				continue
			card.zone = Zone.DECK
			target.shuffle_deck()

class ShuffleBottom(TargetedAction):
	"""
	Shuffle card targets into player target's deck into its bottom.
	TARGET = ActionArg()#controller
	CARD = CardArg()
	"""
	TARGET = ActionArg()#controller
	CARD = CardArg()

	def do(self, source, target, cards):
		if Config.LOGINFO:
			Config.log("ShuffleBottom.do","%r shuffles into %s's deck's bottom"%(cards, target))
		if not isinstance(cards, list):
			cards = [cards]
		if cards[0]==None or cards[0]==[]:
			return
		for card in cards:
			if card.controller != target:
				card.zone = Zone.SETASIDE
				card.controller = target
			if len(target.deck) >= target.max_deck_size:
				if Config.LOGINFO:
					Config.log("ShuffleBottom.do","Shuffle(%r) fails because %r's deck is full"%(card, target))
				continue
			card.zone = Zone.DECK
			target.shiftdown_deck()## make the top card to botom
		return cards

class ShuffleTop(TargetedAction):
	"""
	Shuffle card targets into player target's deck into its top.
	TARGET = ActionArg()#controller
	CARD = CardArg()
	"""
	TARGET = ActionArg()#controller
	CARD = CardArg()

	def do(self, source, target, cards):
		if Config.LOGINFO:
			Config.log("ShuffleTop.do","%r shuffles into %s's deck's top"%(cards, target))
		if not isinstance(cards, list):
			cards = [cards]
		if cards[0]==None or cards[0]==[]:
			return
		for card in cards:
			if card.controller != target:
				card.zone = Zone.SETASIDE
				card.controller = target
			if len(target.deck) >= target.max_deck_size:
				if Config.LOGINFO:
					Config.log("ShuffleTop.do","Shuffle(%r) fails because %r's deck is full"%(card, target))
				continue
			card.zone = Zone.DECK
		return cards


class Swap(TargetedAction):
	"""
	Swap minion target with another.
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
	Swap health between two minions using a buff.
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
		if Config.LOGINFO:
			Config.log("Steal.do","%s takes control of %r"%(controller, target))
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
		if Config.LOGINFO:
			Config.log("UnlockOverload.do","%s overload gets cleared"%(target))
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
		if Config.LOGINFO:
			Config.log("SummonJadeGolem.do","%s summons a Jade Golem for %s"%(source, target))
		target.jade_golem = target.jade_golem + 1 if target.jade_golem <= 29 else 30
		if card.is_summonable():
			source.game.queue_actions(source, [Summon(target, card)])

class PlayBattlecry(TargetedAction):
	"""
	Play a battlecry target random
	CARD = CardArg()	"""
	CARD = CardArg()
	def do(self, source, card):
		target = None
		if card.type!=CardType.MINION:
			return
		if card.has_battlecry!=True:
			return
		if card.requires_target():
			if len(card.targets):
				target = random.choice(card.targets)
			else:
				if Config.LOGINFO:
					Config.log("PlayBattlecry.do","%s play battlecry %s don't have a legal target"%(source, card))
				return
		if Config.LOGINFO:
			Config.log("PlayBattlecry.do","%s play battlecry of %s for a legal target"%(source, card))
		Battlecry(card, target).trigger(source)
		pass

class CastSpell(TargetedAction):
	"""
	Cast a spell target random
	CARD = CardArg()
	"""
	CARD = CardArg()

	def do(self, source, card):
		target = None
		if card.must_choose_one and len(card.choose_cards):
			card = random.choice(card.choose_cards)
		if card.requires_target():
			if len(card.targets):
				target = random.choice(card.targets)
			else:
				if Config.LOGINFO:
					Config.log("CastSpell.do","%s cast spell %s don't have a legal target"%(source, card))
				return
		card.target = target
		if Config.LOGINFO:
			Config.log("CastSpell.do","%s cast spell %s target %s"%(source, card, target))
		source.game.queue_actions(source, [Battlecry(card, card.target)])
		player = source.controller
		player.add_play_log(card)
		#while player.choice:
		#	choice = random.choice(player.choice.cards)
		#	print("Choosing card %r" % (choice))
		#	player.choice.choose(choice)
		source.game.queue_actions(source, [Deaths()])

class CastSecret(TargetedAction):
	"""
	Cast a secret
	"""
	CARDS = CardArg()
	def do(self, source, cards):
		if Config.LOGINFO:
			Config.log("CastSecret.do","%s cast secret %s "%(source, cards))
		if not isinstance(cards,list):
			cards = [cards]
		for card in cards:
			if getattr(card, "this_is_secret", False):
				card.zone=Zone.SECRET
		source.controller.add_play_log(card)


class Evolve(TargetedAction):
	"""
	Transform your minions into random minions that cost ( an amount) more
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()

	def do(self, source, target, amount):
		from . import cards
		cost = target.cost + amount
		card_set = cards.filter(collectible=True, cost=cost, type=CardType.MINION)
		if card_set and len(card_set):
			card = random.choice(card_set)
			return source.game.queue_actions(source, [Morph(target, card)])


class ExtraAttack(TargetedAction):
	"""
	Get target an extra attack change
	"""
	TARGET = ActionArg()

	def do(self, source, target):
		if Config.LOGINFO:
			Config.log("ExtraAttack.do","%s gets an extra attack change."%(target))
		target.num_attacks -= 1


class SwapState(TargetedAction):
	"""
	Swap stats between two minions using a buff.
	"""
	TARGET = ActionArg()
	OTHER = ActionArg()
	BUFF = ActionArg()

	def do(self, source, target, other, buff):
		if Config.LOGINFO:
			Config.log("SwapState.do","swap state %s and %s", target, other)
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
		if Config.LOGINFO:
			Config.log("RefreshHeroPower.do","Refresh Hero Power %s.", heropower)
		heropower.activations_this_turn = 0
		return heropower

class RefreshMana(TargetedAction):
	"""
	Helper to Refresh MANA
	TARGET = ActionArg()#controller
	AMOUNT = IntArg()
	"""
	TARGET = ActionArg()#controller
	AMOUNT = IntArg()
	def do(self, source, target,amount):
		if Config.LOGINFO:
			Config.log("RefreshMana.do","Refresh Mana by %s."%(amount))
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
		if Config.LOGINFO:
			Config.log("Upgrade.do","Upgrade %s counter to %s", target, target.upgrade_counter + 1)
		target.upgrade_counter += 1
		self.broadcast(source, EventListener.AFTER, target, target.upgrade_counter)


class Awaken(TargetedAction):
	"""
	Awaken a dormant minion
	"""
	TARGET = ActionArg()

	def do(self, source, target):
		if Config.LOGINFO:
			Config.log("Awaken.do","%s is awaken"% target)
		target.turns_in_play = 1
		self.broadcast(source, EventListener.ON, target)
		if target.get_actions("awaken"):
			source.game.trigger(target, target.get_actions("awaken"), event_args=None)




#######  sidequest  ############
#
class SidequestCounter(TargetedAction):
	"""
	target, amount, targetaction
	"""
	TARGET = ActionArg()# sidequest card
	AMOUNT = IntArg() #max of call
	TARGETACTION = ActionArg()# sidequest action
	def do(self, source, target, amount, targetaction):
		if Config.LOGINFO:
			Config.log("SidequestCounter.do","Setting Counter on %r -> %i, %r"%(target, (source.sidequest_counter+1), targetaction))
		target.sidequest_counter += 1
		target.script_data_num_1 = amount - target.sidequest_counter
		if target.sidequest_counter== amount:
			target.sidequest_counter = 0
			target.script_data_num_1 = amount
			if targetaction!=None:
				if not isinstance(targetaction,list):
					targetaction = [targetaction]
				for action in targetaction:
					if isinstance(action, TargetedAction): 
						action.trigger(source)
					if isinstance(action, GameAction): 
						action.trigger(source)
					if isinstance(action, Choice): 
						action.trigger(source)

class QuestCounter(TargetedAction):
	"""
	target, targetaction 
	"""
	TARGET = ActionArg()# sidequest card
	STEP=IntArg()
	def do(self, source, target, step=1):
		if getattr(target.controller.game,'this_is_battle', False):
			target = target.deepcopy_original
		amount = target.quest_progress_total
		targetaction = target.sidequest_list0
		if Config.LOGINFO:
			Config.log("SidequestCounter.do","Setting Counter on %r -> %i, %r"%(target, (source.sidequest_counter+step), targetaction))
		target.sidequest_counter += step
		target.script_data_num_1 = amount - target.sidequest_counter
		target.script_data_text_0 = str(target.script_data_num_1)
		if target.sidequest_counter== amount:
			target.sidequest_counter = 0
			target.script_data_num_1 = amount
			if targetaction!=None:
				for action in targetaction:
					if getattr(action,'type', 0)==40:
						CastSecret(action).trigger(source)
					target.destroy()
					#if isinstance(action, TargetedAction): 
					#	action.trigger(source)
					#if isinstance(action, Choice): 
					#	action.trigger(source)


class SidequestCounterText0(TargetedAction):
	"""
	"""
	TARGET = ActionArg()# sidequest card
	AMOUNT = IntArg() #max of call
	TARGETACTION = ActionArg()# sidequest action
	def do(self, source, target, amount, targetaction):
		if Config.LOGINFO:
			Config.log("SidequestCounter.do","Setting Counter on %r -> %i, %r"%(target, (source.sidequest_counter+1), targetaction))
		target.sidequest_counter += 1
		target.script_data_num_1 = amount - target.sidequest_counter
		target.script_data_text_0 = str(target.script_data_num_1)
		if target.sidequest_counter== amount:
			target.sidequest_counter = 0
			target.script_data_num_1 = amount
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
		if target.sidequest_counter== amount:
			if Config.LOGINFO:
				Config.log("SidequestCounterEq","Setting Counter on %r :%i== %i, %r", target, target.sidequest_counter, amount, targetaction)
			target.sidequest_counter = 0
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
		if target.sidequest_counter != amount:
			if Config.LOGINFO:
				Config.log("SidequestCounterNeq.do","Setting Counter on %r :%i!= %i, %r", target, target.sidequest_counter, amount, targetaction)
			target.sidequest_counter = 0
			if targetaction!=None:
				if not isinstance(targetaction,list):
					targetaction = [targetaction]
				for action in targetaction:
					if isinstance(action, TargetedAction):
						action.trigger(source)

class SidequestCounterClear(TargetedAction):
	TARGET = ActionArg()# sidequest card
	def do(self, source, target):
		if Config.LOGINFO:
			Config.log("SidequestCounterClear.do","Setting Counter on %r to be 0", target)
		target.sidequest_counter = 0

class SidequestManaCounter(TargetedAction):
	"""
	TARGET = ActionArg()# sidequest card
	CARD = ActionArg()# spell card
	AMOUNT = IntArg() #max of mana
	TARGETACTION = ActionArg()# sidequest action
	"""
	TARGET = ActionArg()# sidequest card
	CARD = ActionArg()# spell card
	AMOUNT = IntArg() #max of mana
	TARGETACTION = ActionArg()# sidequest action
	def do(self, source, target, card, amount, targetaction):
		if Config.LOGINFO:
			Config.log("SidequestManaCounter.do","Setting Counter on %r is added by %d->%d, %r"%(target, card.cost, (target.sidequest_counter+card.cost), targetaction))
		target.sidequest_counter += card.cost
		if target.sidequest_counter>= amount:
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
		if Config.LOGINFO:
			Config.log("SidequestLostInTheParkCounter.do","Setting Counter on %r rolls by %d->%d, %r"%( target, target.controller.lost_in_the_park, (target.sidequest_counter+target.controller.lost_in_the_park), targetaction))
		target.sidequest_counter += target.controller.lost_in_the_park
		target.controller.lost_in_the_park = 0 # to avoid a double count
		if target.sidequest_counter>= amount:
			if targetaction!=None:
				if not isinstance(targetaction,list):
					targetaction = [targetaction]
				for action in targetaction:
					if isinstance(action, TargetedAction):
						action.trigger(source)


###################### end of sidequest

class SetMaxHealth(TargetedAction):
	"""
	Sets the max health of the character target to  an amount.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		if Config.LOGINFO:
			Config.log("SetMaxHealth.do","Setting max_health on %r to %i", target, amount)
		target.max_health = amount

class SetAtk(TargetedAction):
	"""
	Sets the current health of the character target to a amount.
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		if Config.LOGINFO:
			Config.log("SetAtk.do","Setting atk on %r to %i", target, amount)
		target.atk = amount
class SetCost(TargetedAction):
	"""
	Sets the cost of the character target to an amount.
	TARGET = ActionArg()
	AMOUNT = IntArg()
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		if Config.LOGINFO:
			Config.log("SetCost","Setting cost on %r to %i"%(target, amount))
		target.cost = amount


class Reborn(TargetedAction):
	"""
	Reborn!
	TARGET = ActionArg()
	"""
	TARGET = ActionArg()
	def do(self, source, target):
		if Config.LOGINFO:
			Config.log("Reborn.do","Reborn on %r"%(target))
		controller = target.controller
		self.broadcast(controller, EventListener.ON, target)
		reborn_minion = Summon(controller, target.id).trigger(source)
		if isinstance(reborn_minion,list):
			reborn_minion = reborn_minion[0]
		if isinstance(reborn_minion,list):
			reborn_minion = reborn_minion[0]
		reborn_minion.reborn = False
		if reborn_minion.id in ['BG24_005','BG24_005_G']:##Sinrunner Branchy ## new 25.2.2
			for buff in target.buffs:
				buff.apply(reborn_minion)
			pass
		else:
			reborn_minion.max_health = 1
		self.broadcast(controller, EventListener.AFTER, target)
	pass

class Trade(TargetedAction):
	""" Trade
	TARGET = ActionArg() ## CONTROLLER
	CARD = ActionArg()
	"""
	TARGET = ActionArg() ## CONTROLLER
	CARD = ActionArg()
	# to do is in game.grade_card()
	def do(self, source, target, card):
		self.broadcast(source, EventListener.ON, target, card)
		pass

class Asphyxia(TargetedAction):
	TARGET = ActionArg()# the card
	def do(self, source, target):
		_score_limit = 5
		if target._Asphyxia_ == 'alive' and target.dead:
			if Config.LOGINFO:
				Config.log("Asphyxia.do","The King Rat turns death.")
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
			target.sidequest_counter += 1
			if Config.LOGINFO:
				Config.log("Asphyxia.do","The King Rat is under asphyxia. Counter is %i."%(target.sidequest_counter))
			if target.sidequest_counter == _score_limit:
				target.sidequest_counter = 0
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
		source.sidequest_list1=card
		card.zone = Zone.SETASIDE
		pass

class OpenHatch(TargetedAction):#DRG_086
	TARGET = ActionArg()#player
	def do(self, source, target):
		Summon(target, source.sidequest_list1).trigger(source)
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
		if Config.LOGINFO:
			Config.log("SwapController.do","%s and %s swap their controllers.",target, other)

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
		if Config.LOGINFO:
			Config.log("SwapMinionAndHand.do","%r and %r swap their positions."%(target, other))


class RegularAttack(TargetedAction):
	""" attack without paying the cost.
	TARGET = ActionArg()#ATTACKER
	OTHER = ActionArg()#DEFENDER
	"""
	TARGET = ActionArg()#ATTACKER
	OTHER = ActionArg()#DEFENDER
	def do(self, source, target, other):
		if other==[]:
			return
		if not isinstance(other,list):
			other = [other]
		if not isinstance(target,list):
			target = [target]
		Attack(target, other).broadcast(source, EventListener.ON, target[0], other[0])
		self.broadcast(source, EventListener.ON, target[0], other[0])
		for attcard in target:
			for defcard in other:
				if Config.LOGINFO:
					Config.log("RegularAttack.do","%s attacks '%s'"%(attcard, defcard ))
				if attcard.can_regular_attack():
					Hit(defcard, attcard.atk).trigger(attcard)
				if defcard.atk>0:
					Hit(attcard, defcard.atk).trigger(defcard)
				Attack(target, other).broadcast(source, EventListener.AFTER, attcard, defcard)
				self.broadcast(source, EventListener.AFTER, attcard, defcard)

class BG_Attack(TargetedAction):
	TARGET = ActionArg()#ATTACKER
	OTHER = ActionArg()#DEFFENDER
	def do(self, source, target, other):
		if not isinstance(other,list):
			other = [other]
		if not isinstance(target,list):
			target = [target]
		for attcard in target:
			for defcard in other:
				Attack(attcard, defcard).broadcast(source, EventListener.ON, attcard, defcard)
				self.broadcast(source, EventListener.ON, attcard, defcard)
		for attcard in target:
			for defcard in other:
				if attcard.zone == Zone.PLAY and defcard.zone == Zone.PLAY:# if they're alive
					if attcard.atk>0:
						print("%s(%s) -> %s(%s) : "%(attcard, attcard.controller, defcard, defcard.controller))
						Hit(defcard, attcard.atk).trigger(attcard)
					if defcard.atk>0:
						Hit(attcard, defcard.atk).trigger(defcard)
		for attcard in target:
			for defcard in other:
				Attack(attcard, defcard).broadcast(source, EventListener.AFTER, attcard, defcard)
				self.broadcast(source, EventListener.AFTER, attcard, defcard)

class Dormant(TargetedAction):
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()
	"""
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		target.dormant = amount

class SetAttr(TargetedAction):
	TARGET = ActionArg()
	ATTR = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, attr, amount):
		if hasattr(target, attr):
			if Config.LOGINFO:
				Config.log("SetAttr.do","%s set attr '%s' into %d"%(target, attr, amount ))
			setattr(target, attr, amount)

class SetDivineShield(TargetedAction):
	"""
	TARGET = ActionArg()
	AMOUNT = ActionArg()"""
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount=True):
		if Config.LOGINFO:
			Config.log("SetDivineShield.do"," Let '%s' have a divine shiled"%(target))
		setattr(target, 'divine_shield', amount)

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

class DredgeChoice(Choice):
	def choose(self, card):
		super().choose(card)
		if Config.LOGINFO:
			Config.log("DredgeChoice.choose","%s chooses %r"%(card.controller.name, card))
		controller = card.controller
		for c in controller.deck[:3]:
			if card.id==c.id:
				controller.deck.remove(c)
				controller.deck.append(c)
				break
		pass

class Dredge(TargetedAction):
	"""
	TARGET=ActionArg()#CONTROLLER
	"""
	TARGET=ActionArg()
	def do(self, source, target):
		bottom3ID=[card.id for card in target.deck[:3]]
		DredgeChoice(target, RandomID(*bottom3ID)*3).trigger(source)
	pass



###SCH_714
class EducatedElekkMemory(TargetedAction):
	""" Educated Elekk (epic)"""
	#[x]Whenever a spell is played, this minion remembers it.
	#[Deathrattle:] Shuffle the spells into your deck.
	HOST = ActionArg()# spell card just played
	TARGET = ActionArg()# spell card just played
	def do(self,source,target,card):
		if Config.LOGINFO:
			Config.log("EducatedElekkMemory","%s remember the card: %s",target,card)
		target.sidequest_list1.append(card)

class EducatedElekkDeathrattle(TargetedAction):
	""" Educated Elekk (epic)"""
	#[x]Whenever a spell is played, this minion remembers it.
	#[Deathrattle:] Shuffle the spells into your deck.
	def do(self,source,target):
		if Config.LOGINFO:
			Config.log("EducatedElekkDeathrattle.do","%s Deathrattle",target)
		for card in target.sidequest_list1:
			Shuffle(target.controller, card).trigger(source)

class TentacledMenace(TargetedAction):#DRG_084
	"""Tentacled Menace	Epic
	[Battlecry:] Each player draws a card. Swap their_Costs."""
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
				if Config.LOGINFO:
					Config.log("TentacledMenace.do","Draw cards and change their costs."%())

class ArgentBraggart(TargetedAction):
	"""SCH_149
	[Battlecry:] Gain Attack and Health to match the highest in the battlefield.
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

#class InheritGuardiansLegacy(TargetedAction):
#	"""   """
#	def do(self, source, target):
#		if Config.LOGINFO:
#			Config.log("InheritGuardiansLegacy.do","Gardian's Legacy was inherited by %r"%(target))
#		target.guardians_legacy=True
#		pass

class Freeze(TargetedAction):
	"""
	TARGET = ActionArg()#TARGET
	"""
	TARGET = ActionArg()#TARGET
	def do(self, source, target):
		if Config.LOGINFO:
			Config.log("Freeze.do","%r Freezes %r"%(self, target))
		if not target.tags[GameTag.CANT_BE_FROZEN]:
			##SetTag(target, (GameTag.FROZEN, )).trigger(source)
			target.frozen = True
			self.broadcast(source, EventListener.ON, target)
		else:
			if Config.LOGINFO:
				Config.log("Freeze.do","Freezing is blocked!")

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
#		if Config.LOGINFO:print("cannot_attack_heroes: on : %r", target)
#		target.cannot_attack_heroes = (amount==1)
#		pass

class ChangeHeroPower(TargetedAction):
	"""
	TARGET = ActionArg()#CONTROLLER
	CARD = CardArg()
	"""
	TARGET = ActionArg()#CONTROLLER
	CARD = CardArg()
	def do(self, source, target, card):
		oldHeroPower=target.hero.power
		if oldHeroPower==None:
			exh=0
			script_data_num_1=0
		else:
			exh = oldHeroPower.activations_this_turn
			script_data_num_1 = oldHeroPower.script_data_num_1
		#summon card
		newHeroPower=Summon(target,card).trigger(source)
		if newHeroPower[0]==[]:
			return
		newHeroPower = newHeroPower[0][0]
		#copy exhausted
		newHeroPower.activations_this_turn = exh
		newHeroPower.script_data_num_1 = script_data_num_1
		newHeroPower.data.tags[GameTag.TAG_SCRIPT_DATA_NUM_1] = script_data_num_1
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
		if Config.LOGINFO:
			Config.log("DAL731Duel.do","Duel: %r vs. %r", target, other)
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
			if len(enemy_characters):
				Hit(random.choice(enemy_characters),5).trigger(source)

class DAL558ArchmageVargoth(TargetedAction):
	TARGET = ActionArg()#controller
	def do(self,source,target):
		if len(target.spells_played_this_turn)>0:
			card = random.choice(target.spells_played_this_turn)
			Summon(target,card).trigger(source)

class BT126TeronGorefiend(TargetedAction):
	"""Teron Gorefiend	Minion	Legendary
	[x][Battlecry:] Destroy all
	other friendly minions."""
	TARGET = ActionArg()#card
	def do(self,source,target):#
		target.sidequest_list1=[]
		for n in range(len(target.controller.field)):
			card = target.controller.field[0]
			if card.id != 'BT_126':
				card.zone = Zone.SETASIDE
				target.sidequest_list1.append(card)
		pass
class BT126TeronGorefiendDeathrattle(TargetedAction):
	"""Teron Gorefiend	Minion	Legendary
	[Deathrattle:] Resummon
	them with +1/+1."""
	TARGET = ActionArg()#card
	def do(self,source,target):
		for card in target.sidequest_list1:
			card.zone = Zone.PLAY
			Buff(card, "BT_126e2").trigger(source)
		pass

class SummonAdventurerWithBonus(TargetedAction):
	""" Devouring Ectoplasm 
	TARGET = ActionArg()#the controller
	"""
	TARGET = ActionArg()#the controller
	def do(self,source,target,amount=1):
		cards = random.sample(['WC_034', 'WC_034t', 'WC_034t2', 'WC_034t3', 'WC_034t4', 'WC_034t5', 'WC_034t6', 'WC_034t7', 'WC_034t8'],amount)
		for card in cards:
			newcard=Summon(target, card).trigger(source)
			if isinstance(newcard, list) and len(newcard):
				newcard=newcard[0]
			if isinstance(newcard, list) and len(newcard):
				newcard=newcard[0]
			if getattr(newcard, 'this_is_minion', None)==None:
				return
			newAtk=random.randint(1,3)
			newHealth=random.randint(1,3)
			Buff(newcard, "WC_034e", atk=newAtk, max_health=newHealth)
			if Config.LOGINFO:
				Config.log("SummonAdventurerWithBonus.do","Summon %s with atk=%d, health=%d"%(newcard.data.name, newAtk, newHealth))

class Frenzy(TargetedAction):
	""" Frenzy """
	TARGET = ActionArg()#self
	TARGETACTION = ActionArg()
	def do(self,source,target,targetaction):
		# 'frenzy' is silencable
		if target.frenzy==1 and target.frenzyFlag==0:
		#if target.frenzyFlag==0:
			if Config.LOGINFO:
				Config.log("Frenzy.do","Frenzy action of %r "%(target))
			if not isinstance(targetaction, list):
				targetaction = [targetaction]
			for action in targetaction:
				action.trigger(source)
			target.frenzyFlag=1
			pass 

class Infuse(TargetedAction):### new 24.2
	TARGET=ActionArg()
	INFUSED=ActionArg()
	def do(self, source, target, infused, infuse_in_deck=0):
		controller=target
		if infuse_in_deck==1 and controller.infuse_in_deck==False:
			return None
		source.script_data_num_1 -= 1
		if Config.LOGINFO:
			Config.log("Infuse.do","Infusing %d -> %d for %r"%(source.script_data_num_1+1, source.script_data_num_1, infused))
		if source.script_data_num_1<= 0:
			self.broadcast(source, EventListener.ON, target, infused)
			target = controller.card(infused)
			if target.type == CardType.MINION:
				target.zone = Zone.HAND
				for buff in source.buffs:
					buff.apply(target)
				target.morphed = source
				source.discard()
			self.broadcast(source, EventListener.AFTER, target, infused)
			return target
		return None


#class HonorableKill(TargetedAction):
#	""" Honorable Kill """
#	TARGET = ActionArg() # predamaged minion
#	AMOUNT = IntArg()
#	TARGETEDACTION = ActionArg()
#	def do(self, source, target, amount, targetaction):
#		# 'honorable_kill' is silenceable
#		if source.honorable_kill==1:
#			if taget.health == amount:
#				if Config.LOGINFO:print("Honorable Kill works on %s"%(source))
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
			if Config.LOGINFO:
				Config.log("Moribund.do","%r is moribund."%target)
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
	"""
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	"""
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount=1):
		if hasattr(target,'script_data_num_1'):
			if isinstance(target.script_data_num_1, int)==False:
				target.script_data_num_1=0
			target.script_data_num_1 += amount
		pass

############### player.script_const_1 関連 ########################

def ScriptConst1(card):
    if hasattr(card.controller,'script_const_1'):
        return card.controller.script_const_1
    else:
        return 0
    pass

class HitScriptConst1(TargetedAction):
    CARD=ActionArg()#card
    TARGET=ActionArg()#target
    def do(self,source,card,target):
        amount = ScriptDataNum1(card)
        if not isinstance(target,list):
            target = [target]
        for _card in target:
            Hit(_card,amount).trigger(source)

class SetScriptConst1(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		if hasattr(target,'script_const_1'):
			target.script_const_1 = amount
		pass

class AddScriptConst1(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		if hasattr(target,'script_const_1'):
			target.script_const_1 += amount
		pass

###############################################################


## Battlegrounds actions

class ApplyBanana(TargetedAction):
	TARGET=ActionArg()
	GEM=ActionArg()
	def do(self, source, target, gem):
		if Config.LOGINFO:
			Config.log("ApplyBanana.do","%s feed a banana to %s"%(source, target))		
		if gem=='BGS_Treasures_000e':## big banana
			self.broadcast(source, EventListener.ON, target, gem)
			Buff(target,'BGS_Treasures_000e').trigger(source)
			self.broadcast(source, EventListener.AFTER, target, gem)
			target.gem_applied_thisturn=True
		elif gem=='DMF_065e':## banana
			self.broadcast(source, EventListener.ON, target, gem)
			Buff(target,'DMF_065e').trigger(source)
			self.broadcast(source, EventListener.AFTER, target, gem)
			target.gem_applied_thisturn=True

class ApplyGem(TargetedAction):
	TARGET=ActionArg()
	GEM=ActionArg()
	def do(self, source, target, gem):
		if gem=='BG20_GEM':
			Buff(target,'BG20_GEMe').trigger(source)
			self.broadcast(source, EventListener.ON, target, gem)
			self.broadcast(source, EventListener.AFTER, target, gem)
			target.gem_applied_thisturn=True

class Avenge(TargetedAction):
	TARGET=ActionArg()
	AMOUNT=IntArg()
	TARGETACTION=ActionArg()
	def do(self, source, target, amount, targetaction):
		if Config.LOGINFO:
			Config.log("Avenge.do","Avenge Counter on %r -> %i, %r"%(source, (source.sidequest_counter+1), targetaction))
		source.sidequest_counter += 1
		if source.sidequest_counter== amount:
			source.sidequest_counter = 0
			if targetaction!=None:
				if not isinstance(targetaction,list):
					targetaction = [targetaction]
				for action in targetaction:
					if isinstance(action, Action):
						action.trigger(source)

class BeginBattleTurn(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		controller.game.refresh_auras()## refresh aura_buff
		self.broadcast(source, EventListener.ON, target)
		self.broadcast(source, EventListener.AFTER, target)

class BeginGame(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		controller.game.refresh_auras()## refresh aura_buff
		self.broadcast(source, EventListener.ON, target)
		self.broadcast(source, EventListener.AFTER, target)

class RLK_214_Begingame_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		for cd in reversed(controller.deck):
			if cd.id=='RLK_214':
				cd.zone==Zone.SETASIDE
				cd.zone==Zone.GRAVEYARD
		card = controller.card("RLK_214t")
		minions=[cd for cd in controller.deck if cd.type==CardType.MINION]
		if len(minions)>3:
			minions=random.sample(minions, 3)
		card.sidequest_list0=[cd.id for cd in minions]
		card.zone=Zone.DECK
		for cd in reversed(minions):
			cd.zone==Zone.SETASIDE
			cd.zone==Zone.GRAVEYARD
		pass

class Buy(TargetedAction): ## battlegrounds
	""" Buy a minion 
	TARGET = ActionArg()# controller
	CARD = ActionArg()
	"""
	TARGET = ActionArg()
	CARD = ActionArg()
	def do(self, source, target, card):
		controller = target
		minionprice = controller.game.minionCost


		if controller.hero.power.id=='TB_BaconShop_HP_054':## Millhouse flag
			minionprice = 2 ##maybe no need
			controller.game.minionCost = 2
		bartender = controller.opponent
		if card.id in 'BG25_520_G' and controller.hero.health>minionprice:
			for c in bartender.field:
				if c==card:
					#bartender.field.remove(c)
					buffs=[]
					for buff in card.buffs:
						buffs.append(buff)
					card.zone=Zone.SETASIDE
					card.controller = controller
					card.zone = Zone.HAND
					for buff in buffs:
						buff.apply(card)
					card.frozen=False
					controller.add_buy_log(card)
					controller.game.refresh_auras()## refresh aura_buff
					self.broadcast(source, EventListener.ON, controller, card)
					self.broadcast(source, EventListener.AFTER, controller, card)
					gold_card_id = controller.game.BG_find_triple()## トリプルを判定
					if gold_card_id:
						controller.game.BG_deal_gold(gold_card_id)
					return
			pass
		if controller.mana>=minionprice:
			for c in bartender.field:
				if c==card:
					#bartender.field.remove(c)
					buffs=[]
					for buff in card.buffs:
						buffs.append(buff)
					card.zone=Zone.SETASIDE
					card.controller = controller
					card.zone = Zone.HAND
					for buff in buffs:
						buff.apply(card)
					card.frozen=False
					controller.used_mana += minionprice
					controller.total_used_mana_this_turn += minionprice
					controller.spentmoney_in_this_turn += minionprice
					controller.add_buy_log(card)
					controller.game.refresh_auras()## refresh aura_buff
					self.broadcast(source, EventListener.ON, controller, card)
					self.broadcast(source, EventListener.AFTER, controller, card)
					gold_card_id = controller.game.BG_find_triple()## トリプルを判定
					if gold_card_id:
						controller.game.BG_deal_gold(gold_card_id)
					return
			pass
		pass

class Destroy_spellcraft(TargetedAction):
	TARGET = ActionArg()
	def do(self,source,target):
		if not target.permanent_buff:
			if target.type==CardType.ENCHANTMENT:
				target.remove()
			else:
				Destroy(target).trigger(source.controller)
		pass
	pass



class DiscoverTwice(Choice):
	def choose(self, card):
		self.source.sidequest_counter += 1
		if self.source.sidequest_counter>=2:
			self.next_choice=None
		else:
			self.next_choice=self
		super().choose(card)
		card.zone = Zone.HAND
		cards = self._args[1]
		if isinstance(cards, LazyValue):
			self.cards = cards.evaluate(self.source)


class EatsMinion(TargetedAction):
	TARGET = ActionArg()
	CARD = ActionArg()
	AMOUNT = IntArg()
	BUFF = ActionArg()
	def do(self, source, target, card, amount, buff):
		if target==[] or card==[]:
			return
		if isinstance(target,list):
			target = target[0]
		if isinstance(card,list):
			card = card[0]
		Buff(target,  buff, atk=card.atk * amount, max_health = card.max_health * amount).trigger(target)
		Destroy(card).trigger(target)
	pass


class EndBattle(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		self.broadcast(source, EventListener.ON, target)
		self.broadcast(source, EventListener.AFTER, target)

class GetFreeRerole(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		controller.game.free_rerole += 1
		controller.game.reroleCost=0
		pass
	pass

class HitAdjacentMinions(TargetedAction):#Cave Hydra, Foe Reaper 4000,
	TARGET=ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		for card in target.adjacent_minions:
			Hit(card, amount).trigger(source)

class LoseDivineShield(GameAction):#聖盾を失ったとき
	TARGET=ActionArg()
	def do(self, source, target):
		self.broadcast(source, EventListener.ON, target)
		self.broadcast(source, EventListener.AFTER, target)

class Magnetic(TargetedAction):#超電磁
	TARGET = ActionArg()
	BUFF = ActionArg()
	def do(self, source, target, buffs):
		if not target in target.controller.field:
			return
		index = target.controller.field.index(target)
		if index==len(target.controller.field)-1:
			return
		other = target.controller.field[index+1]
		if other.race == Race.MECHANICAL:
			if not isinstance(buffs,list):
				buffs = [buffs]
			for buff in buffs:
				Buff(other, buff).trigger(target.controller)
			target.deathrattle_valid=False### deathrattle を止めたい
			Destroy(target).trigger(target.controller)
		if 'BG25_807t' in target.id:## 'BG25_807t','BG25_807t_G','BG25_807t2','BG25_807t2_G','BG25_807t3','BG25_807t3_G'
			if other.race == Race.DEMON:
				if not isinstance(buffs,list):
					buffs = [buffs]
				for buff in buffs:
					Buff(other, buff).trigger(target.controller)
				target.deathrattle_valid=False### deathrattle を止めたい
				Destroy(target).trigger(target.controller)
		pass

class MakeCardUnplayable(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		target.cant_play = True
	pass

class GradeupByMana(GameAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		self.broadcast(source, EventListener.ON, target, amount)
		self.broadcast(source, EventListener.AFTER, target, amount)
	pass


class MorphGold(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		if isinstance(target, list):
			target = target[0]
		id = target.id
		gold_id = target.controller.game.parent.BG_Gold[id]
		if not gold_id:
			return
		buffs = []
		buffs += target.buffs
		myzone=target.zone
		target.zone=Zone.GRAVEYARD
		newcard = target.controller.card(gold_id)
		for buff in buffs:## inheriting all buffs
			buff.apply(newcard)
		if Config.LOGINFO:
			print("Gold card!!!"," by %s"%(target.controller))

		newcard.zone = myzone # 必要か？PLAY?
		return newcard

class ReduceTierUpCost(TargetedAction):
	TARGET=ActionArg()
	AMOUNT=IntArg()
	def do(self, source, target, amount):
		if hasattr(target,'tavern_tierup_cost'):
			target.tavern_tierup_cost = max(target.tavern_tierup_cost-amount, 0)
		pass

class Rerole(TargetedAction): ## battlegrounds
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		game = controller.game
		bartender = game.bartender
		if controller.mana>=game.reroleCost:
			self.broadcast(source, EventListener.ON, target)
			controller.used_mana += game.reroleCost
			controller.total_used_mana_this_turn += game.reroleCost
			controller.spentmoney_in_this_turn += game.reroleCost
			for i in range(len(bartender.field)):
				card=bartender.field[0]
				game.parent.ReturnCard(card)
			if controller.hero.power.id=='TB_BaconShop_HP_065t2':### アランナフラグ
				bartender.len_bobs_field=7
			for repeat in range(bartender.len_bobs_field):
				card = game.parent.DealCard(bartender, controller.tavern_tier)
				if controller.hero.power.id=='TB_BaconShop_HP_101':### サイラスフラグ
					if random.choice([0,1]):
						card.darkmoon_ticket = True
			if game.free_rerole>1:
				game.free_rerole -= 1
				game.reroleCost=0
			else:
				game.free_rerole = 0
				game.reroleCost=1
				if controller.hero.power.id=='TB_BaconShop_HP_054':## Millhouse flag
					game.reroleCost=2
			self.broadcast(source, EventListener.AFTER, target)
		pass

class Sell(TargetedAction):
	""" Sell a minion (battlegrounds)
	TARGET = ActionArg()#controller
	CARD = CardArg()#card
	"""
	TARGET = ActionArg()
	CARD = CardArg()
	def do(self, source, target, card):
		controller = target
		if isinstance(card,list):
			card = card[0]
		for c in controller.field:
			if c==card:
				self.broadcast(source, EventListener.ON, target, card)
				self.broadcast(source, EventListener.AFTER, target, card)
				card.zone=Zone.GRAVEYARD
				controller.game.refresh_auras()## refresh aura_buff
				if card.data.tags.get(1587):
					controller.used_mana -= card.gambler_sell_price
				else:
					controller.used_mana -= 1
				controller.sells_in_this_turn+=1
				return
		pass

class Spellcraft(TargetedAction):
	CONTROLLER = ActionArg()
	SPELLCARD = ActionArg()
	def do(self, source, controller, spellcard):
		if controller!=source.controller:
			controller=source.controller## why! no way.
		self.broadcast(source, EventListener.ON, controller, spellcard)
		Give(controller, spellcard).trigger(source)
		self.broadcast(source, EventListener.AFTER, controller, spellcard)
		pass

class SpellcraftSpell(TargetedAction):
	TARGET = ActionArg()
	SPELLCARD = ActionArg()
	def do(self, source, target, spellcard):
		controller=source.controller
		if target!=None and target.this_is_minion:
			self.broadcast(source, EventListener.ON, controller, spellcard, target)
			Buff(target, spellcard).trigger(controller)
			self.broadcast(source, EventListener.AFTER, controller, spellcard, target)
		pass

class StealGem(TargetedAction):
	TARGET = ActionArg()
	CARDS = ActionArg()
	def do(self, source, target, cards):
		if not isinstance(cards, list):
			cards = [cards]
		gem_count=0
		for card in cards:
			repeat = len(card.buffs)
			for i in range(repeat):
				c = card.buffs[repeat-1-i]
				if c.id=='BG20_GEMe':
					card.buffs.remove(c)
					gem_count += 1
		for i in range(gem_count):
			ApplyGem(target, 'BG20_GEM').trigger(source)

class SummonOnce(Summon):
	"""
	Make player targets summon an id onto their field.
	This works for equipping weapons as well as summoning minions.
	"""
	TARGET = ActionArg()
	CARD = CardArg()

	def do(self, source, target, cards):
		if target.type != CardType.PLAYER:
			if Config.LOGINFO:
				Config.log("SummonOnce.do","<><><><><><><><><><><><>")
				Config.log("SummonOnce.do","%s is not a player, he/she cannot summon anything", target)
				Config.log("SummonOnce.do","<><><><><><><><><><><><>")
			return
		if Config.LOGINFO:
			Config.log("SummonOnce.do","%s summons %r"%(target, cards))

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
			## no broadcasting
		return cards

class UpgradeTier(TargetedAction):
	TARGET=ActionArg()#controller
	def do(self, source, target):
		tavern_tierup_cost={1:5, 2:7, 3:8, 4:9, 5:10, 6:10} ## new 23.2.2
		##tavern_tierup_cost={1:5, 2:7, 3:8, 4:11, 5:10, 6:10}
		controller = target
		bar = target.game
		if controller.tavern_tier<=5 and controller.mana >= controller.tavern_tierup_cost:
			controller.tavern_tier += 1
			controller.used_mana += controller.tavern_tierup_cost
			controller.total_used_mana_this_turn += controller.tavern_tierup_cost
			controller.spentmoney_in_this_turn += controller.tavern_tierup_cost
			controller.tavern_tierup_cost = tavern_tierup_cost[controller.tavern_tier]
			controller.game.refresh_auras()## refresh aura_buff
			if controller.hero.power.id=='TB_BaconShop_HP_054': #Millhouse flag
				controller.tavern_tierup_cost += 1
			self.broadcast(source, EventListener.ON, controller)
			self.broadcast(source, EventListener.AFTER, controller)
	pass

class TieGame(TargetedAction):
	TARGET=ActionArg()#controller
	def do(self, source, target):
		self.broadcast(source, EventListener.ON, target)
		self.broadcast(source, EventListener.AFTER, target)		
		pass

class WinGame(TargetedAction):
	TARGET=ActionArg()#controller
	def do(self, source, target):
		self.broadcast(source, EventListener.ON, target)
		self.broadcast(source, EventListener.AFTER, target)		
		pass

class LoseGame(TargetedAction):
	TARGET=ActionArg()#controller
	def do(self, source, target):
		self.broadcast(source, EventListener.ON, target)
		self.broadcast(source, EventListener.AFTER, target)		
		pass

class AddCorpse(TargetedAction):## new 25.0
	PLAYER = ActionArg()
	AMOUNT = IntArg()# this may be a negative number
	def do(self, source, player, amount):
		if hasattr(player, 'corpse'):
			if Config.LOGINFO:
				Config.log("AddCorpse.do","Add %s corpse by %d"%(player, amount))
			player.corpse = max(0, player.corpse+amount)
		pass

class SpendCorpse(TargetedAction):## new 25.0
	PLAYER = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, player, amount):
		if hasattr(player, 'corpse'):
			if player.corpse>=amount:
				self.broadcast(source, EventListener.ON, player, amount)
				if Config.LOGINFO:
					Config.log("AddCorpse.do","%s spends %d his/her corpses"%(player, amount))
				player.corpse -= amount
				self.broadcast(source, EventListener.AFTER, player, amount)		
		pass

