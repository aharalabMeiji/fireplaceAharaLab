import random
import time
from calendar import timegm
from itertools import chain

from hearthstone.enums import BlockType, CardType, PlayState, State, Step, Zone

from .actions import Attack, Awaken, BeginTurn, Death, EndTurn, EventListener, \
	Play,Destroy, Give, Draw, Shuffle, PayCost, Discover, Buff
from .card import THE_COIN
from .entity import Entity
from .exceptions import GameOver
from .managers import GameManager
from .utils import CardList,ActionType
from .config import Config 
from .dsl.random_picker import *



class BaseGame(Entity):
	type = CardType.GAME
	MAX_MINIONS_ON_FIELD = 7
	Manager = GameManager

	def __init__(self, players):
		self.data = None
		self.players = players
		super().__init__()
		for player in players:
			player.game = self
		self.state = State.INVALID
		self.step = Step.BEGIN_FIRST
		self.next_step = Step.BEGIN_SHUFFLE
		self.turn = 0
		self.current_player = None
		self.tick = 0
		self.active_aura_buffs = CardList()
		self.setaside = CardList()
		self._action_stack = 0
		self._myLog_=[]
		self.event_args=None
		self.zone=Zone.INVALID
		#self._stage_choice_=random.choice([## stage choice for SCH_199, 'SCH_199t23' is excluded.
		#	'SCH_199t','SCH_199t2','SCH_199t3','SCH_199t4','SCH_199t19','SCH_199t20',
		#	'SCH_199t21','SCH_199t22','SCH_199t25','SCH_199t26'])

	def __repr__(self):
		return "%s(players=%r)" % (self.__class__.__name__, self.players)

	def __iter__(self):
		return chain(self.entities, self.hands, self.decks, self.graveyard, self.setaside)

	@property
	def game(self):
		return self

	@property
	def board(self):
		return CardList(chain(self.players[0].field, self.players[1].field))

	@property
	def decks(self):
		return CardList(chain(self.players[0].deck, self.players[1].deck))

	@property
	def discarded(self):
		return CardList(chain(self.players[0].discarded, self.players[1].discarded))

	@property
	def hands(self):
		return CardList(chain(self.players[0].hand, self.players[1].hand))

	@property
	def characters(self):
		return CardList(chain(self.players[0].characters, self.players[1].characters))

	@property
	def graveyard(self):
		return CardList(chain(self.players[0].graveyard, self.players[1].graveyard))

	@property
	def entities(self):
		return CardList(chain([self], self.players[0].entities, self.players[1].entities))

	@property
	def live_entities(self):
		return CardList(chain(self.players[0].live_entities, self.players[1].live_entities))

	@property
	def allcards(self):
		return self.entities + self.hands + self.decks

	@property
	def minions_killed_this_turn(self):
		return self.players[0].minions_killed_this_turn + self.players[1].minions_killed_this_turn

	@property
	def ended(self):
		return self.state == State.COMPLETE

	def action_start(self, type, source, index, target):
		self.manager.action_start(type, source, index, target)
		if type != BlockType.PLAY:
			self._action_stack += 1

	def action_end(self, type, source):
		self.manager.action_end(type, source)

		if self.ended:
			#raise GameOver("The game has ended.")
			return
		if type != BlockType.PLAY:
			self._action_stack -= 1
		if not self._action_stack:
			self.log("Empty stack, refreshing auras and processing deaths")
			if type ==BlockType.DEATHS:
				self.log("this case.")
				return## avoid infinte loop
			self.refresh_auras()
			self.process_deaths()

	def action_block(self, source, actions, type, index=-1, target=None, event_args=None):
		self.action_start(type, source, index, target)
		if actions:
			ret = self.queue_actions(source, actions, event_args)
		else:
			ret = []
		self.action_end(type, source)
		return ret

	def attack(self, source, target):
		type = BlockType.ATTACK
		actions = [Attack(source, target)]
		result = self.action_block(source, actions, type, target=target)
		if self.state != State.COMPLETE:
			self.manager.step(Step.MAIN_ACTION, Step.MAIN_END)
		return result

	def joust(self, source, challenger, defender, actions):
		type = BlockType.JOUST
		return self.action_block(source, actions, type, event_args=[challenger, defender])

	def main_power(self, source, actions, target):
		type = BlockType.POWER
		return self.action_block(source, actions, type, target=target)

	def play_card(self, card, target, index, choose):
		type = BlockType.PLAY
		player = card.controller
		actions = [Play(card, target, index, choose)]
		return self.action_block(player, actions, type, index, target)

	def trade_card(self,card, option):
		type = ActionType.TRADE
		trader = card.controller
		if option == 0:
			actions = [PayCost(trader, card, 1), Draw(trader), Shuffle(trader,card)]
		else: #option=1
			actions = [PayCost(trader, card, 1), Discover(trader,RandomCard()), Shuffle(trader,card)]
		## callback
		if card.id == 'DED_009' and len(card.controller.field)>0:
			actions += [Buff(random.choice(card.controller.field),'EX1_084e')]#rush
		if card.id == 'DED_527':
			actions += [Buff(card, 'DED_527e')]
		#if hasattr(card.data.scripts, 'trade'):
		#	self.log ("After trading, %s is triggered by %s"%(card.get_actions('trade'),card.controller))
		#	#actions += [card.get_actions('trade')]
		return self.action_block(trader, actions, type, None, None)

	def process_deaths(self):
		type = BlockType.DEATHS
		cards = []
		for card in self.live_entities:
			if card.to_be_destroyed:
				cards.append(card)

		actions = []
		if cards:
			self.action_start(type, self, 0, None)
			for card in cards:
				card.zone = Zone.GRAVEYARD
				actions.append(Death(card))
			self.check_for_end_game()
			self.trigger(self, actions, event_args=None)
			self.action_end(type, self)

	def trigger(self, source, actions, event_args):
		"""
		Perform actions as a result of an event listener (TRIGGER)
		"""
		type = BlockType.TRIGGER
		return self.action_block(source, actions, type, event_args=event_args)

	def cheat_action(self, source, actions):
		"""
		Perform actions as if a card had just triggered them
		"""
		return self.trigger(source, actions, event_args=None)

	def check_for_end_game(self):
		"""
		Check if one or more player is currently losing.
		End the game if they are.
		"""
		gameover = False
		for player in self.players:
			if player.playstate in (PlayState.CONCEDED, PlayState.DISCONNECTED):
				player.playstate = PlayState.LOSING
			if player.playstate == PlayState.LOSING:
				gameover = True

		if gameover:
			if self.players[0].playstate == self.players[1].playstate:
				for player in self.players:
					player.playstate = PlayState.TIED
			else:
				for player in self.players:
					if player.playstate == PlayState.LOSING:
						player.playstate = PlayState.LOST
					else:
						player.playstate = PlayState.WON
			self.state = State.COMPLETE
			self.manager.step(self.next_step, Step.FINAL_WRAPUP)
			self.manager.step(self.next_step, Step.FINAL_GAMEOVER)
			self.manager.step(self.next_step)

	def queue_actions(self, source, actions, event_args=None):
		"""
		Queue a list of \a actions for processing from \a source.
		Triggers an aura refresh afterwards.
		"""
		source.event_args = event_args
		ret = self.trigger_actions(source, actions)
		source.event_args = None
		return ret

	def trigger_actions(self, source, actions):
		"""
		Performs a list of `actions` from `source`.
		This should seldom be called directly - use `queue_actions` instead.
		"""
		ret = []
		for action in actions:
			if isinstance(action, EventListener):
				# Queuing an EventListener registers it as a one-time event
				# This allows registering events from eg. play actions
				self.log("Registering event listener %r on %r", action, self)
				action.once = True
				# FIXME: Figure out a cleaner way to get the event listener target
				if source.type == CardType.SPELL:
					listener = source.controller
				else:
					listener = source
				listener._events.append(action)
			else:
				ret.append(action.trigger(source))
		return ret

	def pick_first_player(self):
		"""
		Picks and returns first player, second player
		In the default implementation, the first player is always
		"Player 0". Use CoinRules to decide it randomly.
		"""
		return self.players[0], self.players[1]

	def refresh_auras(self):
		refresh_queue = []
		for entity in self.entities:
			for script in entity.update_scripts:
				refresh_queue.append((entity, script))

		for entity in self.hands:
			for script in entity.data.scripts.Hand.update:
				refresh_queue.append((entity, script))

		# Sort the refresh queue by refresh priority (used by eg. Lightspawn)
		refresh_queue.sort(key=lambda e: getattr(e[1], "priority", 50))
		for entity, action in refresh_queue:
			action.trigger(entity)

		buffs_to_destroy = []
		for buff in self.active_aura_buffs:
			if isinstance(buff, list):
				buff=buff[0]
			if buff.tick < self.tick:
				buffs_to_destroy.append(buff)
		for buff in buffs_to_destroy:
			buff.remove()

		self.tick += 1

	def setup(self):
		self.log("Setting up game %r", self)
		self.state = State.RUNNING
		self.step = Step.BEGIN_DRAW
		self.zone = Zone.PLAY
		self.players[0].opponent = self.players[1]
		self.players[1].opponent = self.players[0]
		for player in self.players:
			player.zone = Zone.PLAY
			self.manager.new_entity(player)

		first, second = self.pick_first_player()
		self.player1 = first
		self.player1.first_player = True
		self.player2 = second
		self.player2.first_player = False

		for player in self.players:
			player.prepare_for_game()
		self.manager.start_game()

	def start(self):
		self.setup()
		self.begin_turn(self.player1)

	def end_turn(self):
		for player in self.players:
			player.minions_killed_this_turn = 0
		return self.queue_actions(self, [EndTurn(self.current_player)])

	def _end_turn(self):
		self.log("%s ends turn %i", self.current_player, self.turn)
		self.manager.step(self.next_step, Step.MAIN_CLEANUP)
		self.current_player.temp_mana = 0
		self.end_turn_cleanup()

	def end_turn_cleanup(self):
		self.manager.step(self.next_step, Step.MAIN_NEXT)
		for character in self.current_player.characters.filter(frozen=True):
			if not character.num_attacks and not character.exhausted:
				self.log("Freeze fades from %r", character)
				character.frozen = False
		for buff in self.entities.filter(one_turn_effect=True):
			self.log("Ending One-Turn effect: %r", buff)
			buff.remove()
		self.begin_turn(self.current_player.opponent)

	def skip_turn(self):
		self.end_turn()
		self.end_turn()
		return self

	# TODO  Take an extra turn, for cards like Time Warp
	def take_an_extra_turn(self):
		return self

	def begin_turn(self, player):
		ret = self.queue_actions(self, [BeginTurn(player)])
		self.manager.turn(player)
		return ret

	def card_when_drawn(self, drawn_card, player):
		from .card import Minion
		from fireplace import cards
		# if drawn_card is 'casts_when_drawn' then immediately play.  
		if hasattr(drawn_card, "casts_when_drawn"):
			self.queue_actions(player, [Play(drawn_card, None, None, None)])
			self.queue_actions(player, [Draw(player)])
		#When you draw this, add a _copy of it to your hand
		if drawn_card.id == 'SW_306':
			new_card = Minion(cards.db[drawn_card.id])
			new_card.controller = player
			new_card.zone = Zone.HAND
		# if 'BAR_034' is in hand and mana >=5 then change 'BAR_034' to 'BAR_034t'
		# if 'BAR_034t' is in hand and mana >=10 then change 'BAR_034t' to 'BAR_034t2'
		for card in player.hand:
			if card.id == 'BAR_034' and player.mana>=5:
				self.queue_actions(player,[Destroy(card)])
				self.queue_actions(player,[Give(player, 'BAR_034t')])
			if card.id == 'BAR_034t' and player.mana>=10:
				self.queue_actions(player,[Destroy(card)])
				self.queue_actions(player,[Give(player, 'BAR_034t2')])
		for card in player.hand:
			if card.id == 'BAR_305' and player.mana>=5:
				self.queue_actions(player,[Destroy(card)])
				self.queue_actions(player,[Give(player, 'BAR_305t')])
			if card.id == 'BAR_305t' and player.mana>=10:
				self.queue_actions(player,[Destroy(card)])
				self.queue_actions(player,[Give(player, 'BAR_305t2')])
		for card in player.hand:
			if card.id == 'BAR_536' and player.mana>=5:
				self.queue_actions(player,[Destroy(card)])
				self.queue_actions(player,[Give(player, 'BAR_536t')])
			if card.id == 'BAR_536t' and player.mana>=10:
				self.queue_actions(player,[Destroy(card)])
				self.queue_actions(player,[Give(player, 'BAR_536t2')])
		for card in player.hand:##Conditioning
			if card.id == 'BAR_842' and player.mana>=5:
				self.queue_actions(player,[Destroy(card)])
				self.queue_actions(player,[Give(player, 'BAR_842t')])
			if card.id == 'BAR_842t' and player.mana>=10:
				self.queue_actions(player,[Destroy(card)])
				self.queue_actions(player,[Give(player, 'BAR_842t2')])



	def _begin_turn(self, player):
		self.manager.step(self.next_step, Step.MAIN_START)
		self.manager.step(self.next_step, Step.MAIN_ACTION)

		####################
		if player.hero in player.field:
			print ("hero is on the field!! lol")
			player.field.remove(player.hero)
			player.hero.zone = Zone.PLAY
		####################

		for p in self.players:
			p.cards_drawn_this_turn = 0

		player.turn_start = timegm(time.gmtime())
		player.cards_played_this_turn = 0
		player.minions_played_this_turn = 0
		player.minions_killed_this_turn = 0
		player.combo = False
		player.max_mana += 1
		player.used_mana = 0
		player.overload_locked = player.overloaded
		player.overloaded = 0
		for entity in self.live_entities:
			if entity.type != CardType.PLAYER:
				entity.turns_in_play += 1

		if player.hero.power:
			player.hero.power.activations_this_turn = 0

		for character in self.characters:
			character.num_attacks = 0

		for minion in player.field:
			if hasattr(minion,'dormant') and minion.dormant:
				minion.dormant -= 1
				self.log("while dormant (%d) of %r"%(minion.dormant, minion))
				if not minion.dormant:
					self.queue_actions(self, [Awaken(minion)])

		drawn_card = player.draw()

		self.manager.step(self.next_step, Step.MAIN_END)
	pass

	def add_log(self, choice):
		self._myLog_.append(choice)
		pass

	def get_log(self):
		return self._myLog_

class CoinRules:
	"""
	Randomly determines the starting player when the Game starts.
	The second player gets "The Coin" (GAME_005).
	"""
	def pick_first_player(self):
		if Config.FSFIXED == 0: #Aharalab
			winner = random.choice(self.players)
			#winner = self.players[1]
			self.log("Tossing the coin... %s wins!", winner)
			return winner, winner.opponent
		else: #Aharalab
			return self.players[0], self.players[1] #Aharalab

	def begin_turn(self, player):
		if self.turn == 0 and Config.COIN > 0:
			self.log("%s gets The Coin (%s)", self.player2, THE_COIN)
			self.player2.give(THE_COIN)
		super().begin_turn(player)


class MulliganRules:
	"""
	Performs a Mulligan phase when the Game starts.
	Only begin the game after both Mulligans have been chosen.
	"""

	def start(self):
		from .actions import MulliganChoice
		self.setup()
		self.next_step = Step.BEGIN_MULLIGAN
		self.log("Entering mulligan phase")
		self.step, self.next_step = self.next_step, Step.MAIN_READY

		for player in self.players:
			self.queue_actions(self, [MulliganChoice(player, callback=self.mulligan_done)])

	def mulligan_done(self):
		self.begin_turn(self.player1)



class Game(MulliganRules, CoinRules, BaseGame):
	pass
