import random
from itertools import chain

from hearthstone.enums import CardType, PlayState, Race, Zone

from .actions import Concede, Draw, Fatigue, Give, Hit, Steal, Summon
from .aura import TargetableByAuras
from .card import Card
from .deck import Deck
from .entity import Entity, slot_property
from .managers import PlayerManager
from .utils import CardList
from .config import Config #

class PlayLog:
	card=None
	turn=0
	amount=0
	def __init__(self, _card, _turn, _cost, _amount=0, card2=None):
		self.card = _card
		self.card2 = card2
		self.turn = _turn
		self.cost = _cost
		self.amount = _amount
		pass
	pass

class Player(Entity, TargetableByAuras):
	Manager = PlayerManager
	all_targets_random = slot_property("all_targets_random")
	cant_overload = slot_property("cant_overload")
	choose_both = slot_property("choose_both")
	extra_battlecries = slot_property("extra_battlecries")
	extra_extra_battlecries = slot_property("extra_extra_battlecries")
	extra_deathrattles = slot_property("extra_deathrattles")
	extra_extra_deathrattles = slot_property("extra_extra_deathrattles") ## TB_BaconUps_055
	healing_double = slot_property("healing_double", sum)
	hero_power_double = slot_property("hero_power_double", sum)
	healing_as_damage = slot_property("healing_as_damage")
	shadowform = slot_property("shadowform")
	spellpower_double = slot_property("spellpower_double", sum)
	spellpower_adjustment = slot_property("spellpower", sum)
	murlocs_cost_health = slot_property("murlocs_cost_health")
	type = CardType.PLAYER

	def __init__(self, name, deck, hero):
		self.starting_deck = deck
		self.starting_hero = hero
		self.data = None
		self.name = name
		self.hero = None
		super().__init__()
		self.deck = Deck()
		self.hand = CardList()
		self.discarded = CardList()
		self.field = CardList()
		self.graveyard = CardList()
		self.secrets = CardList()
		self.quests = CardList()
		self.rewards = CardList()
		self.choice = None
		self.choiceText = 'Choose one.'
		self.max_hand_size = 10
		self.max_resources = 20
		self.max_deck_size = 60
		self.cant_draw = False
		self.cant_fatigue = False
		self.entourage = []
		self.fatigue_counter = 0
		self.last_card_played = None
		self.cards_played_this_turn = 0
		self.cards_drawn_this_turn = 0
		self.minions_played_this_turn =0
		self.overloaded = 0
		self.overload_locked = 0
		self._max_mana = 0
		self._start_hand_size = 3
		self.playstate = PlayState.INVALID
		self.temp_mana = 0
		self.timeout = 75
		self.times_hero_power_used_this_game = 0
		self.used_mana = 0
		self.total_used_mana_this_turn = 0
		self.minions_killed_this_turn = 0
		self.weapon = None
		self.zone = Zone.INVALID
		self.jade_golem = 1
		self.take_half_damage=False
		self.times_spell_played_this_game = 0
		self.times_secret_played_this_game = 0
		self.times_spell_to_friendly_minion_this_game = 0 #
		self.times_card_to_play_out_of_deck = 0 #
		self.times_spells_played_this_turn = 0 #
		self.spells_played_this_turn=[] #
		self.died_this_turn=[] #
		#self.cthun = None
		self.piece_of_cthun = [0,0,0,0]
		self._death_log=[]
		self._play_log=[]
		self._outcast_play_log=[]
		self._damage_log=[]
		self._activate_log=[]
		self._summon_log=[]
		self._reveal_log=[]
		self._targetedaction_log=[]
		self._battlecry_log=[]
		self._give_log=[]
		self._buy_log=[] # battlegraounds
		self.spell_and_damage=False
		#self.guardians_legacy = False#CS3_001
		self.spellpower_option=0 # SW_450t4
		self.choiceStrategy = None
		self.lost_in_the_park=0
		self.carry_cards=[] # YOP_024
		self.abyssal_curse=1## TSC_955t
		self.infuse_in_deck=False ## new 24.4
		self.cant_reveal_secret=False ## new 24.4
		self.relic_improvision=1 ## new 24.2
		self.draw_extra_card=False ## new 24.4
		self.corpse=0 ## new 25.0

		self.tavern_tier=1# battlegrounds
		self.tavern_tierup_cost=5 # battlegrounds
		self.extra_tavern_tierup_reduce_cost=0 # battlegrounds
		self.len_bobs_field=3 # battlegrounds
		self.extra_len_bobs_field=0 # battleground
		self.attacker_index=0 # battlegrounds
		self.first_dead_minion=None # battlegrounds
		self.second_dead_minion=None # battlegrounds
		self.once_per_turn=0 # battlegrounds
		self.deepcopy_original=None # battlegrounds
		self.nomi_powered_up = 0## battlegrounds, Nomi
		self.lightspawn_powered_up = 0## battlegrounds, lightspoan
		self.eternal_knight_powered_up = 0## battlegrounds,Eternal_Knight
		self.nerubian_deathswarmer_powered_up = 0## battlegrounds,Nerubian_Deathswarmer
		self.felemental_powered_up = 0## battlegrounds, Felemental, new 25.2.2
		self.stormpike_powered_up = 0## battlegrounds, Vanndar Stormpike, new 25.6
		self.spentmoney_in_this_turn=0 ## battlegrounds, #Captain Flat Tusk
		self.buddy_gauge=0## battlegrounds, # buddy
		self.got_buddy=0## battlegrounds, # buddy
		self.buddy_id=''## battlegrounds, # buddy
		self.buddy_taver_tier=''## battlegrounds, # buddy
		self.parent_agent=None## # battlegrounds
		self.sells_in_this_turn=0 # battlegrounds
		self.prev_field=[] # battlegrounds
		self.script_const_1=0 ## general use
		self.gifts=[] # battlegrounds
		self.spellpower_by_spell=0
		self.gorefiend_cardID=None ## battlegrounds ## BG25_HERO_103
		self.im_a_player=True # battlegrounds

	def __str__(self):
		return self.name

	def __repr__(self):
		return "%s(name=%r, hero=%r)" % (self.__class__.__name__, self.name, self.hero)

	@property
	def current_player(self):
		return self.game.current_player is self

	@property
	def controller(self):
		return self

	@property
	def mana(self):
		mana = max(0, self.max_mana - self.used_mana - self.overload_locked) + self.temp_mana
		return mana

	@property
	def max_mana(self):
		return self._max_mana

	@max_mana.setter
	def max_mana(self, amount):
		self._max_mana = min(self.max_resources, max(0, amount))
		if Config.LOGINFO:
			Config.log("Player.max_mana","%s is now at %i mana crystals"%(self, self._max_mana))

	@property
	def heropower_damage(self):
		return sum(minion.heropower_damage for minion in self.field)

	@property
	def spellpower(self):
		aura_power = self.controller.spellpower_adjustment + self.controller.spellpower_by_spell
		minion_power = 0
		for minion in self.field:
			if hasattr(minion,'spellpower'):
				if hasattr(minion,'dormant') and minion.dormant>0:
					continue
				minion_power += minion.spellpower
		return aura_power + minion_power + self.spellpower_option

	@property
	def spellpower_fire(self):# There is a referenced tag in SW_112, but this is the only card for this tag.
		minion_power = 0
		for minion in self.field:
			if hasattr(minion,'spellpower_fire'):
				if hasattr(minion,'dormant') and minion.dormant>0:
					continue
				minion_power += minion.spellpower_fire
		return minion_power
	@property
	def spellpower_nature(self):# 
		minion_power = 0
		for minion in self.field:
			if hasattr(minion,'spellpower_nature'):
				if hasattr(minion,'dormant') and minion.dormant>0:
					continue
				minion_power += minion.spellpower_nature
		return minion_power
	@property
	def start_hand_size(self):
		# old version
		if Config.EX_CARD and not self.first_player:
			# Give the second player an extra card
			return self._start_hand_size + 1
		else:
			return self._start_hand_size

	@property
	def characters(self):
		return CardList(chain([self.hero] if self.hero else [], self.field))

	@property
	def entities(self):
		for entity in self.field:
			yield from entity.entities
		yield from self.secrets
		yield from self.quests
		yield from self.rewards
		yield from self.buffs
		if self.hero:
			yield from self.hero.entities
		yield self

	@property
	def targetable_entities(self):
		yield from self.field
		yield from self.secrets
		yield from self.quests
		yield from self.rewards
		if self.hero:
			yield from self.hero.targetable_entities
		yield self

	@property
	def broadcast_entities(self):
		for entity in self.field:
			yield from entity.entities
		yield from self.secrets
		yield from self.quests
		for entity in self.rewards:
			yield from entity.entities
		yield from self.buffs
		for entity in self.hand:
			yield from entity.buffs
		if self.hero:
			yield from self.hero.entities
		yield self

	def hand_broadcast_entities(self):
		for entity in self.field:
			yield from entity.entities
		yield from self.secrets
		yield from self.quests
		for entity in self.rewards:
			yield from entity.entities
		yield from self.buffs
		if self.hero:
			yield from self.hero.entities
		yield self

	@property
	def live_entities(self):
		yield from self.field
		if self.hero:
			yield self.hero
		if self.weapon:
			yield self.weapon

	@property
	def actionable_entities(self):
		yield from self.characters
		yield from self.hand
		if self.hero.power:
			yield self.hero.power

	@property
	def minion_slots(self):
		return max(0, self.game.MAX_MINIONS_ON_FIELD - len(self.field))

	def card(self, id, source=None, parent=None, zone=Zone.SETASIDE):
		card = Card(id)
		card.controller = self
		card.zone = zone
		card.play_counter = self.game.play_counter
		self.game.play_counter += 1
		if source is not None:
			card.creator = source
		if parent is not None:
			card.parent_card = parent
		#if id == "OG_280" and self.controller.cthun is not None:
		#	cthun = self.controller.cthun
		#	for k in cthun.silenceable_attributes:
		#		v = getattr(cthun, k)
		#		setattr(card, k, v)
		#	card.silenced = cthun.silenced
		#	card.damage = cthun.damage
		#	for buff in cthun.buffs:
		#s		cthun.buff(card, buff.id)
		self.game.manager.new_entity(card)
		return card

	def setup_piece_of_cthun(self):#DMF_254
		player = self
		for card in player.deck:
			if card.id=='DMF_254':
				card.destroy()
				self.card('DMF_254t3',zone=Zone.DECK)
				self.card('DMF_254t4',zone=Zone.DECK)
				self.card('DMF_254t5',zone=Zone.DECK)
				self.card('DMF_254t7',zone=Zone.DECK)
				self.shuffle_deck()
		pass

	def contains_questline(self, deck):
		for card in deck:
			if hasattr(card, 'questline') and card.questline:
				return card
		return None
		

	def prepare_for_game(self):
		self.summon(self.starting_hero)
		for id in self.starting_deck:
			self.card(id, zone=Zone.DECK)
		self.shuffle_deck()
		#self.cthun = self.card("OG_280")
		self.playstate = PlayState.PLAYING
		self.setup_piece_of_cthun()

		# Draw initial hand (but not any more than what we have in the deck)
		hand_size = min(len(self.deck), self.start_hand_size)
		questline_card = self.contains_questline(self.deck)
		# questline card must be included in the initial hand.
		if questline_card != None:
			starting_hand = [questline_card]+random.sample(self.deck, hand_size-1)
		else:
			starting_hand = random.sample(self.deck, hand_size)

		# It's faster to move cards directly to the hand instead of drawing
		for card in starting_hand:
			card.zone = Zone.HAND

	def get_spell_damage(self, amount: int) -> int:
		"""
		Returns the amount of damage \a amount will do, taking
		SPELLPOWER and SPELLPOWER_DOUBLE into account.
		"""
		amount += self.spellpower
		amount <<= self.controller.spellpower_double
		return amount

	def get_spell_damage_fire(self, amount: int) -> int:
		"""
		Returns the amount of damage for only fire card \a amount will do, taking
		SPELLPOWER and SPELLPOWER_DOUBLE into account.
		"""
		amount += (self.spellpower+self.spellpower_fire)
		amount <<= self.controller.spellpower_double
		return amount

	def get_spell_damage_nature(self, amount: int) -> int:
		"""
		Returns the amount of damage for only nature card \a amount will do, taking
		SPELLPOWER and SPELLPOWER_DOUBLE into account.
		"""
		amount += (self.spellpower+self.spellpower_nature)
		amount <<= self.controller.spellpower_double
		return amount


	def discard_hand(self):
		if Config.LOGINFO:
			Config.log("Player.discard_hand","%r discards their entire hand!", self)
		# iterate the list in reverse so we don't skip over cards in the process
		# yes it's stupid.
		for card in self.hand[::-1]:
			card.discard()

	def can_pay_cost(self, card):
		"""
		Returns whether the player can pay the resource cost of a card.
		"""
		if card.card_costs_health:# and card.type == CardType.SPELL: <---diversion for WC_023e
			return self.hero.health > card.cost
		if card.card_costs_armor:# RLK_659 new 25.0
			return self.hero.armor > card.cost
		if self.murlocs_cost_health:
			if card.type == CardType.MINION and card.race == Race.MURLOC:
				return self.hero.health > card.cost
		return self.mana >= card.cost

	def pay_cost(self, source, amount: int) -> int:
		"""
		Make player pay \a amount mana.
		Returns how much mana is spent, after temporary mana adjustments.
		"""

		#strictly, if buff = OG_121e then the source must be a SPELL, if buff = WC_023e, no condition here.
		## OG_121 is very old card and more, not a classic card nor a core card.
		if source.card_costs_health:# and source.type == CardType.SPELL: <--- diversion for WC_023e
			if Config.LOGINFO:
				Config.log("Player.pay_cost","%s costs %i health"%(self, amount))
			self.game.queue_actions(self, [Hit(self.hero, amount)])
			return amount
		if source.card_costs_armor:# new 25.0  RLK_659
			if Config.LOGINFO:
				Config.log("Player.pay_cost","%s costs %i armor"%(self, amount))
			self.game.queue_actions(self, [Hit(self.hero, amount)])
			return amount
		if self.murlocs_cost_health:
			if source.type == CardType.MINION and source.race == Race.MURLOC:
				if Config.LOGINFO:
					Config.log("Player.pay_cost","%s murlocs cost %i health"%(self, amount))
				self.game.queue_actions(self, [Hit(self.hero, amount)])
				return amount
		if self.temp_mana:
			# Coin, Innervate etc
			used_temp = min(self.temp_mana, amount)
			amount -= used_temp
			self.temp_mana -= used_temp
		if Config.LOGINFO:
			Config.log("Player.pay_cost","%s pays %i mana to %i"%( self, amount, (self.used_mana + amount))) #
		self.used_mana += amount
		return amount

	def shuffle_deck(self):
		if Config.LOGINFO:
			Config.log("shuffle_deck","%r shuffles his deck"% self)
		random.shuffle(self.deck)

	def shiftdown_deck(self):
		if Config.LOGINFO:
			Config.log("shiftdown_deck","%r makes the top card to bottom of his deck"% self)
		topcard = self.deck[-1]
		self.deck.remove(topcard)
		self.deck.insert(0, topcard)
		pass

	def draw(self, count=1):
		if self.cant_draw:
			if Config.LOGINFO:
				Config.log("Player.draw","%s tries to draw %i cards, but can't draw"%(self, count))
			return None

		ret = self.game.cheat_action(self, [Draw(self) * count])[0]
		if count == 1:
			if not ret[0]:  # fatigue
				return None
			return ret[0][0]
		return ret

	def mill(self, count=1):
		if count == 1:
			if not self.deck:
				return
			else:
				card = self.deck[-1]
			if Config.LOGINFO:
				Config.log("Player.mill","%s mills %r"%(self, card))
			card.discard()
			return card
		else:
			ret = []
			while count:
				ret.append(self.mill())
				count -= 1
			return ret

	def give(self, id):
		cards = self.game.cheat_action(self, [Give(self, id)])[0]
		if cards[0] != []:
			return cards[0][0]
		else:
			return None

	def concede(self):
		ret = self.game.cheat_action(self, [Concede(self)])
		return ret

	def fatigue(self):
		return self.game.cheat_action(self, [Fatigue(self)])[0]

	def steal(self, card):
		return self.game.cheat_action(self, [Steal(card)])

	def summon(self, card):
		"""
		Puts \a card in the PLAY zone
		"""
		if isinstance(card, str):
			card = self.card(card, zone=Zone.PLAY)
		self.game.cheat_action(self, [Summon(self, card)])
		return card

	## death_log
	def add_death_log(self, card):
		self._death_log.append([card,card.game.turn])
		self.died_this_turn.append(card)
	@property
	def death_log(self):
		_ret = []
		for _log in self._death_log:
			_ret.append(_log[0])
		return _ret
	@property
	def death_this_turn(self):
		_ret = []
		for _log in self._death_log:
			if _log[1] == self.game.turn:
				_ret.append(_log[0])
		return _ret
	@property
	def death_last_opponent_turn(self):
		_ret = []
		for _log in self._death_log:
			if _log[1] == self.game.turn-1:
				_ret.append(_log[0])
		return _ret
	@property
	def death_last_turn(self):
		_ret = []
		for _log in self._death_log:
			if _log[1] == self.game.turn-2:
				_ret.append(_log[0])
		return _ret
	@property
	def death_after_last_turn(self):
		_ret = []
		for _log in self._death_log:
			if _log[1] == self.game.turn-1 or _log[1] == self.game.turn:
				_ret.append(_log[0])
		return _ret


	##play_log
	def add_play_log(self, card, card2=None):
		self._play_log.append(PlayLog(card, card.game.turn, card.cost, card2=card2))
	@property
	def play_log(self):
		_ret = []
		for _log in self._play_log:
			_ret.append(_log.card)
		return _ret
	@property
	def play_last_turn(self):
		_ret = []
		for _log in self._play_log:
			if _log.turn == self.game.turn - 2:
				_ret.append(_log.card)
		return _ret
	@property
	def play_this_turn(self):
		_ret = []
		for _log in self._play_log:
			if _log.turn == self.game.turn:
				_ret.append(_log.card)
		return _ret
	@property
	def total_spell_cost(self):
		amount=0
		for _log in self._play_log:
			if _log.card.type==CardType.SPELL:
				amount += _log.cost
		return amount
	@property
	def last_choose_one(self):
		for playlog in reversed(self._play_log):
			card = playlog.card
			card2 = playlog.card2
			if getattr(card,'has_choose_one', 0) and card2!=None:
				return [card, card2]
		return []



	##outcast_play_log
	def add_outcast_play_log(self, card, card2=None):
		self._outcast_play_log.append(PlayLog(card, card.game.turn, card.cost, card2=card2))
	@property
	def outcast_play_log(self):
		_ret = []
		for _log in self._outcast_play_log:
			_ret.append(_log.card)
		return _ret


	##activate_log
	def add_activate_log(self, card, amount):
		self._activate_log.append(PlayLog(card,card.game.turn, card.cost, amount))
	@property
	def activate_log(self):
		_ret = []
		for _log in self._activate_log:
			_ret.append(_log.card)
		return _ret

	##damage_log
	def add_damage_log(self, card, amount):
		self._damage_log.append(PlayLog(card, card.game.turn, card.cost, amount))
	@property
	def damage_log(self):
		_ret = []
		for _log in self._damage_log:
			_ret.append(_log.card)
		return _ret
	@property
	def damage_log_of_this_turn(self):
		_ret = []
		for _log in self._damage_log:
			if _log.turn == self.game.turn:
				_ret.append(_log.card)
		return _ret
	@property
	def damage_amount_of_this_turn(self):
		_ret = 0
		for _log in self._damage_log:
			if _log.turn == self.game.turn:
				_ret += _log.amount
		return _ret

	##sammon_log
	def add_summon_log(self, card):
		self._summon_log.append(PlayLog(card, card.game.turn, card.cost ))
	@property
	def summon_log(self):
		_ret = []
		for _log in self._summon_log:
			_ret.append(_log.card)
		return _ret

	##reveal_log
	def add_reveal_log(self, card):
		self._reveal_log.append(PlayLog(card, card.game.turn, card.cost))
	@property
	def reveal_log(self):
		_ret = []
		for _log in self._reveal_log:
			_ret.append(_log.card)
		return _ret

	##targetedaction_log
	def add_targetedaction_log(self, action):
		self._targetedaction_log.append(action)
	@property
	def targetedaction_log(self):
		return self._targetedaction_log

	## battlecry_log
	def add_battlecry_log(self, battlecry):
		self._battlecry_log.append(battlecry)
	@property
	def battlecry_log(self):
		return self._battlecry_log

	## Draw and Give
	def add_give_log(self, card):
		self._give_log.append({'card':card, 'turn':card.game.turn})
	@property
	def give_log(self):
		return [log['card'] for log in self._give_log]

	### battlegraounds
	def add_buy_log(self, card):
		self._buy_log.append(PlayLog(card, card.game.turn, 0))
	@property
	def buy_log(self):
		ret = []
		for _log in self._buy_log:
			ret.append(_log.card)
		return ret
	def buy_this_turn_log(self):
		ret = []
		turn =self.game.turn
		for _log in self._buy_log:
			if _log.turn == turn:
				ret.append(_log.card)
		return ret
