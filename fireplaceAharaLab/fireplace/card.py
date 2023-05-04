from genericpath import samefile
from pickle import NONE
import random
from itertools import chain

from hearthstone.enums import CardType, MultiClassGroup, PlayReq, PlayState, \
	Race, Rarity, Step, Zone, GameTag, SpellSchool

from . import actions, cards, enums, rules
from .aura import TargetableByAuras
from .entity import BaseEntity, Entity, boolean_property, int_property, slot_property
from .exceptions import InvalidAction
from .managers import CardManager
from .targeting import TARGETING_PREREQUISITES, is_valid_target
from .utils import CardList 
from .logging import log
from .config import Config
from .actions import LoseDivineShield, WhenDrawn

THE_COIN = "GAME_005"


def Card(id):
	data = cards.db[id]
	subclass = {
		CardType.HERO: Hero,
		CardType.MINION: Minion,
		CardType.SPELL: Spell,
		CardType.ENCHANTMENT: Enchantment,
		CardType.WEAPON: Weapon,
		CardType.HERO_POWER: HeroPower,
		CardType.LOCATION: Location,
		CardType.BATTLEGROUND_QUEST_REWARD: QuestReward,
	}[data.type]
	if subclass is Spell:
		if hasattr(data,'secret') and data.secret:
			subclass = Secret# 
		if hasattr(data,'sidequest') and data.sidequest:
			subclass = Sidequest# 
		if hasattr(data,'questline') and data.questline:
			subclass = Sidequest# 
		if hasattr(data,'quest') and data.quest:
			subclass = Sidequest# 
	return subclass(data)


class BaseCard(BaseEntity):
	Manager = CardManager
	delayed_destruction = False

	def __init__(self, data):
		self.data = data
		super().__init__()
		self.requirements = data.requirements.copy()
		self.id = data.id
		self.controller = None
		self.choose = None
		self.parent_card = None
		self.aura = False
		self.heropower_damage = 0
		self._zone = Zone.INVALID
		self.tags.update(data.tags)
		self.frenzyFlag = 0
		self.choiceText = 'Choose one.'
		self.smallbox=[]#utility

	def __str__(self):
		return self.data.name

	def __hash__(self):
		return self.id.__hash__()

	def __repr__(self):
		return "<%s %r(%s)>" % (self.__class__.__name__, self.__str__(), self.id)

	def __eq__(self, other):
		if isinstance(other, BaseCard):
			return self.id.__eq__(other.id)
		elif isinstance(other, str):
			return self.id.__eq__(other)
		return super().__eq__(other)

	@property
	def game(self):
		return self.controller.game

	@property
	def zone(self):
		return self._zone

	@property
	def classes(self):
		if hasattr(self, "multi_class_group"):
			return MultiClassGroup(self.multi_class_group).card_classes
		else:
			return [self.card_class]

	@zone.setter
	def zone(self, value):
		self._set_zone(value)

	def _set_zone(self, value):
		oldzone = self.zone
		newzone = value

		#if Config.LOGINFO:
		#	Config.log("BaseCard._set_zone","%r moves from %r to %r"%(self, oldzone, newzone))

		if oldzone==Zone.HAND:
			if newzone==Zone.HAND:
				if self in self.controller.hand:
					pass
				else:
					self.controller.hand.append(self)
			elif newzone==Zone.DECK:
				if self in self.controller.hand:
					self.controller.hand.remove(self)
				self.controller.deck.append(self)
			elif newzone==Zone.SETASIDE:
				if self in self.controller.hand:
					self.controller.hand.remove(self)
				self.game.setaside.append(self)
			elif newzone==Zone.GRAVEYARD:
				if self in self.controller.hand:
					self.controller.hand.remove(self)
				self.controller.graveyard.append(self)
		elif oldzone==Zone.DECK:
			if newzone==Zone.HAND:
				if self in self.controller.deck:
					self.controller.deck.remove(self)
				self.controller.hand.append(self)
			elif newzone==Zone.DECK:
				if self in self.controller.deck:
					pass
				else:
					self.controller.deck.append(self)
			elif newzone==Zone.SETASIDE:
				if self in self.controller.deck:
					self.controller.deck.remove(self)
				self.game.setaside.append(self)
			elif newzone==Zone.GRAVEYARD:
				if self in self.controller.deck:
					self.controller.deck.remove(self)
				self.controller.graveyard.append(self)
		elif oldzone==Zone.GRAVEYARD:
			if newzone==Zone.HAND:
				if self in self.controller.graveyard:
					self.controller.graveyard.remove(self)
				self.controller.hand.append(self)
			elif newzone==Zone.DECK:
				if self in self.controller.graveyard:
					self.controller.graveyard.remove(self)
				self.controller.deck.append(self)
			elif newzone==Zone.SETASIDE:
				if self in self.controller.graveyard:
					self.controller.graveyard.remove(self)
				self.game.setaside.append(self)
			elif newzone==Zone.GRAVEYARD:
				if not self in self.controller.graveyard:
					self.controller.graveyard.append(self)
		elif oldzone==Zone.SETASIDE:
			if newzone==Zone.HAND:
				if self in self.game.setaside:
					self.game.setaside.remove(self)
				self.controller.hand.append(self)
			elif newzone==Zone.DECK:
				if self in self.game.setaside:
					self.game.setaside.remove(self)
				self.controller.deck.append(self)
			elif newzone==Zone.SETASIDE:
				if not self in self.game.setaside:
					self.game.setaside.append(self)
			elif newzone==Zone.GRAVEYARD:
				if self in self.game.setaside:
					self.game.setaside.remove(self)
				self.controller.graveyard.append(self)
		elif oldzone==Zone.INVALID:
			if newzone==Zone.HAND:
				if not self in self.controller.hand:
					self.controller.hand.append(self)
			elif newzone==Zone.DECK:
				if not self in self.controller.deck:
					self.controller.deck.append(self)
			elif newzone==Zone.SETASIDE:
				if not self in self.game.setaside:
					self.game.setaside.append(self)
			elif newzone==Zone.GRAVEYARD:
				if not self in self.controller.graveyard:
					self.controller.graveyard.append(self)

		self._zone = newzone

		if newzone == Zone.PLAY:
			self.play_counter = self.game.play_counter
			self.game.play_counter += 1

	def buff(self, target, buff, **kwargs):
		"""
		Summon \a buff and apply it to \a target
		If keyword arguments are given, attempt to set the given
		values to the buff. Example:
		player.buff(target, health=random.randint(1, 5))
		NOTE: Any Card can buff any other Card. The controller of the
		Card that buffs the target becomes the controller of the buff.
		"""
		ret = self.controller.card(buff, self)
		ret.source = self
		ret.apply(target)
		for k, v in kwargs.items():
			setattr(ret, k, v)
		return ret

	def is_playable(self) -> bool:
		"""
		Return whether the card can be played.
		Do not confuse with is_summonable()
		"""
		return False

	def play(self, *args):
		raise NotImplementedError


class PlayableCard(BaseCard, Entity, TargetableByAuras):
	cant_be_frozen = boolean_property("cant_be_frozen")# 
	card_costs_health = boolean_property("card_costs_health") #### <---- spells_cost_health
	card_costs_armor = boolean_property("card_costs_armor") # new 25.0
	corrupt = boolean_property('corrupt')# darkmoon
	corruptedcard = boolean_property('corruptedcard')#darkmoon
	has_choose_one = boolean_property("has_choose_one")
	has_battlecry = boolean_property("has_battlecry")
	honorable_kill = boolean_property("honorable_kill")
	lifesteal = boolean_property("lifesteal")
	mark_of_evil = boolean_property("mark_of_evil")# 
	piece_of_cthun=int_property("piece_of_cthun")#
	playable_zone = Zone.HAND
	reborn = boolean_property("reborn")# 
	script_data_num_1 = int_property("script_data_num_1")
	script_data_num_2 = int_property("script_data_num_2")
	trade_cost = int_property("trade_cost")#stormwind
	tradeable = boolean_property("tradeable")#stormwind
	windfury = int_property("windfury")
	colossal = boolean_property("colossal")##sunken
	SI7_minion = boolean_property("SI7_minion") ## stormwind_rogue 
	cost_blood = int_property("cost_blood") ## new 25.0
	cost_frost = int_property("cost_frost") ## new 25.0
	cost_death = int_property("cost_death") ## new 25.0
	cost_unholy = int_property("cost_unholy") ## new 25.0
	concoction = boolean_property("concoction") ## new 25.0
	sidequest_list0 = []# Sidequest
	sidequest_list1 = []# Sidequest
	sidequest_list2 = []# Sidequest
	sidequest_list3 = []# Sidequest
	sidequest_counter = 0# Sidequest
	choice_limit = 1# Sidequest
	action_option=0 # Sidequest
	_Asphyxia_ = 'alive' # SW_323 The Rat King
	honorable_kill = True
	honorably_killed = False ##
	darkmoon_ticket=False #battlegrounds
	BG_cost=0 #battlegrounds, Recruitment Map
	double_damage=0## ##BG24_704 'take double( triple) damage'

	def __init__(self, data):
		self.attacker=None
		self.cant_play = False
		self.choose_both = False
		self._choose_cards = CardList()
		self.entourage = CardList(data.entourage)
		self.get_extra_damage = 0
		self.has_combo = False
		self.overload = 0
		self.target = None
		self.rarity = Rarity.INVALID
		self.morphed = None
		self.upgrade_counter = 0
		self.cast_on_friendly_characters = False
		self.script_data_text_0=''
		self.script_data_text_1=''
		self.script_data_text_2=''
		self.script_data_text_3=''
		self.no_durability_loss=False
		#if hasattr(self, 'trade_cost') and self.trade_cost>0:## because of CardDefs's bug
		if getattr(self, 'trade_cost',0)>0:## because of CardDefs's bug
			self.tradeable = True## because of CardDefs's bug
		super().__init__(data)

	@property
	def choose_cards(self):
		if self._choose_cards==[] and self.has_choose_one:
			for id in self.data.choose_cards:
				card = self.controller.card(id, source=self, parent=self)
				self._choose_cards.append(card)
		return self._choose_cards

	
	@property
	def events(self):
		if self.zone == Zone.HAND:
			return self.data.scripts.Hand.events
		if self.zone == Zone.DECK:## EX1_295, SW_072 occurs an error
			# in existing cards, there isn't one with Deck class.  However, rarely they come here.
			return self.data.scripts.Deck.events
		if self.no_durability_loss:#AV_146e2
			return self._events # No durability loss. 
		return self.base_events + self._events

	@property
	def cost(self):
		ret = 0
		if self.zone == Zone.HAND:
			mod = self.data.scripts.cost_mod
			if mod is not None:
				r = mod.evaluate(self)
				# evaluate() can return None if it's an Evaluator (Crush)
				if r:
					ret += r
		ret = self._getattr("cost", ret)
		return max(0, ret)

	@cost.setter
	def cost(self, value):
		self._cost = value

	@property
	def must_choose_one(self):
		"""
		Returns True if the card has active choices
		"""
		if self.controller.choose_both and self.has_choose_one:
			self.choose_cards = []
		#elif self.has_choose_one and self.choose_cards==[]: -> def choose_cards
		#	for id in self.data.choose_cards:
		#		card = self.controller.card(id, source=self, parent=self)
		#		self._choose_cards.append(card)
		return bool(self.data.choose_cards)

	@property
	def powered_up(self):
		"""
		Returns True whether the card is "powered up".
		"""
		if not self.data.scripts.powered_up:
			return False
		for script in self.data.scripts.powered_up:
			if not script.check(self):
				return False
		return True

	@property
	def entities(self):
		return chain([self], self.buffs)

	@property
	def zone_position(self):
		"""
		Returns the card's position (1-indexed) in its zone, or 0 if not available.
		"""
		if self.zone == Zone.HAND:
			return self.controller.hand.index(self) + 1
		return 0
	
	def _set_zone(self, value):
		oldzone = self.zone
		newzone=value

		#if Config.LOGINFO:
		#	Config.log("PlayableCard._set_zone","card %s: %s -> %s"%(self, oldzone, newzone))
		# Keep Buff: Deck -> Hand, Hand -> Play, Deck -> Play
		# Remove Buff: Other case
		if not (oldzone, newzone) in [
		   (Zone.DECK, Zone.HAND), (Zone.HAND, Zone.PLAY), (Zone.DECK, Zone.PLAY), (Zone.INVALID, Zone.DECK), (Zone.INVALID, Zone.HAND), (Zone.INVALID, Zone.PLAY),(Zone.SETASIDE, Zone.DECK), (Zone.SETASIDE, Zone.HAND), (Zone.SETASIDE, Zone.PLAY)]:
			self.clear_buffs()
		## if data hase choose_cards, then 'self' creates the 'choose one' subcards
		#if isinstance(self.data.choose_cards, list) and len(self.data.choose_cards): -> def choose_cards
		#	del self.choose_cards[:] ## possibly 'self' has had already subcards
		#	for id in self.data.choose_cards:
		#		card = self.controller.card(id, source=self, parent=self)
		#		self._choose_cards.append(card)
		super()._set_zone(value)


	def destroy(self):
		return self.game.cheat_action(self, [actions.Destroy(self), actions.Deaths()])

	def discard(self):
		if Config.LOGINFO:
			print("Discarding %r" % self)
		self.tags[enums.DISCARDED] = True
		self.zone = Zone.GRAVEYARD

	def draw(self):
		if len(self.controller.hand) >= self.controller.max_hand_size:
			if Config.LOGINFO:
				Config.log("BaseCard.draw","%s overdraws and loses %r!"%(self.controller, self))
			self.discard()
		else:
			if Config.LOGINFO:
				Config.log("BaseCard.draw","%s draws %r"%(self.controller, self))
			if self.zone != Zone.HAND:
				self.zone = Zone.HAND
			# if self is 'casts_when_drawn' then immediately play. 
			self.game.casts_when_drawn(self, self.controller)
			WhenDrawn(self.controller, self).trigger(self.controller)
			self.controller.cards_drawn_this_turn += 1

			if self.game.step > Step.BEGIN_MULLIGAN:
				# Proc the draw script, but only if we are past mulligan
				actions = self.get_actions("draw")
				self.game.trigger(self, actions, event_args=None)

	def heal(self, target, amount):
		return self.game.cheat_action(self, [actions.Heal(target, amount)])

	def is_playable(self):
		if self.controller.choice:
			return False

		if not self.controller.current_player:
			return False

		zone = self.parent_card.zone if self.parent_card else self.zone
		if zone != self.playable_zone:
			return False

		if not self.controller.can_pay_cost(self):
			return False

		if PlayReq.REQ_TARGET_TO_PLAY in self.requirements:
			if not self.play_targets:
				return False

		if PlayReq.REQ_NUM_MINION_SLOTS in self.requirements:
			if self.requirements[PlayReq.REQ_NUM_MINION_SLOTS] > self.controller.minion_slots:
				return False

		min_enemy_minions = self.requirements.get(PlayReq.REQ_MINIMUM_ENEMY_MINIONS, 0)
		if len(self.controller.opponent.field) < min_enemy_minions:
			return False

		min_friendly_minions = self.requirements.get(1001, 0)
		if len(self.controller.field) < min_friendly_minions:
			return False


		min_total_minions = self.requirements.get(PlayReq.REQ_MINIMUM_TOTAL_MINIONS, 0)
		if len(self.controller.game.board) < min_total_minions:
			return False

		if PlayReq.REQ_ENTIRE_ENTOURAGE_NOT_IN_PLAY in self.requirements:
			if not [id for id in self.entourage if not self.controller.field.contains(id)]:
				return False

		if PlayReq.REQ_WEAPON_EQUIPPED in self.requirements:
			if not self.controller.weapon:
				return False

		if PlayReq.REQ_FRIENDLY_MINION_DIED_THIS_GAME in self.requirements:
			if not self.controller.graveyard.filter(type=CardType.MINION):
				return False

		min_tier= self.requirements.get(PlayReq.REQ_MINIMUM_TAVERN_TIER_LEVEL_TO_PLAY, 0)
		if PlayReq.REQ_MINIMUM_TAVERN_TIER_LEVEL_TO_PLAY in self.requirements:
			if self.controller.tavern_tier < min_tier:
				return False

		return self.is_summonable()

	def play(self, target=None, index=None, choose=None):
		"""
		Queue a Play action on the card.
		"""
		if choose:
			if self.must_choose_one:
				for card in self.choose_cards:
					if card.id==choose.id:
						choose=card
						break
				#choose = card = self.choose_cards.filter(id=choose)[0]
				if Config.LOGINFO:
					Config.log("BaseCard.play","%r: choosing %r"%(self, choose))
			else:
				raise InvalidAction("%r cannot be played with choice %r" % (self, choose))
		else:
			if self.must_choose_one and len(self.choose_cards)>0:
				choose=random.choice(self.choose_cards)
				raise InvalidAction("%r requires a choice (one of %r)" % (self, self.choose_cards))
			card = self
		if not self.is_playable():
			raise InvalidAction("%r isn't playable." % (self))
		if card.requires_target():
			if not target:
				raise InvalidAction("%r requires a target to play." % (self))
			elif target not in self.play_targets:
				raise InvalidAction("%r is not a valid target for %r." % (target, self))
			if self.controller.all_targets_random and len(self.play_targets):
				new_target = random.choice(self.play_targets)
				if Config.LOGINFO:
					Config.log("BaseCard.play","Retargeting %r from %r to %r", self, target, new_target)
				target = new_target
		elif target:
			if Config.LOGINFO:
					Config.log("BaseCard.play","%r does not require a target, ignoring target %r", self, target)
			target = None
		self.game.play_card(self, target, index, choose)
		if not self.id in self.controller.starting_deck:# aharalab ## DRG_109 
			self.controller.times_card_to_play_out_of_deck += 1 
		return self

	def is_summonable(self) -> bool:
		"""
		Return whether the card can be summoned.
		Do not confuse with is_playable()
		"""
		return True

	def morph(self, into):
		"""
		Morph the card into another card
		"""
		return self.game.cheat_action(self, [actions.Morph(self, into)])

	def shuffle_into_deck(self):
		"""
		Shuffle the card into the controller's deck
		"""
		return self.game.cheat_action(self, [actions.Shuffle(self.controller, self)])

	def battlecry_requires_target(self):
		"""
		True if the play action of the card requires a target
		"""
		if self.has_combo and self.controller.combo:
			if PlayReq.REQ_TARGET_FOR_COMBO in self.requirements:
				return True

		for req in TARGETING_PREREQUISITES:
			if req in self.requirements:
				return True
		return False

	def requires_target(self):
		"""
		True if the card currently requires a target
		"""
		if self.has_combo and PlayReq.REQ_TARGET_FOR_COMBO in self.requirements:
			if self.controller.combo:
				return True
		if PlayReq.REQ_TARGET_IF_AVAILABLE in self.requirements:
			return bool(self.play_targets)
		#if PlayReq.REQ_TARGET_IF_AVAILABLE_AND_DRAGON_IN_HAND in self.requirements:
		#	if self.controller.hand.filter(race=Race.DRAGON):
		#		return bool(self.play_targets)
		req = self.requirements.get(PlayReq.REQ_TARGET_IF_AVAILABLE_AND_MINIMUM_FRIENDLY_MINIONS)
		if req is not None:
			if len(self.controller.field) >= req:
				return bool(self.play_targets)
		req = self.requirements.get(PlayReq.REQ_TARGET_IF_AVAILABLE_AND_MINIMUM_FRIENDLY_SECRETS)
		if req is not None:
			if len(self.controller.secrets) >= req:
				return bool(self.play_targets)
		req = self.requirements.get(PlayReq.REQ_TARGET_IF_AVAILABLE_AND_HERO_ATTACKED_THIS_TURN)
		if req is not None:
			if self.controller.hero.num_attacks > 0:
				return bool(self.play_targets)
		return PlayReq.REQ_TARGET_TO_PLAY in self.requirements

	@property
	def play_targets(self):
		return [card for card in self.game.characters if is_valid_target(self, card)]

	@property
	def targets(self):
		return self.play_targets

	def can_trade(self,option=0):
		if not self.trade_cost > 0:
			return (False,0)
		for _card in (self.controller.hand + self.controller.field):
			if _card.id=='SW_045':
				option=1#Discover type trading
		if option==0:
			if self.trade_cost > self.controller.mana:
				if Config.LOGINFO:
					Config.log("card.can_trade","controller of %r doesn't have enough manas." % (self))
				return (False, option)
			if len(self.controller.deck)==0:
				if Config.LOGINFO:
					Config.log("card.can_trade","No card in the deck and %r cannot be trade." % (self))
				return (False, option)
			else :
				return (True, option)
		else:# option==1
			if self.trade_cost > self.controller.mana:
				if Config.LOGINFO:
					Config.log("card.can_trade","controller of %r doesn't have enough manas." % (self))
				return (False, option)
			if len(self.controller.deck)<3:
				if Config.LOGINFO:
					Config.log("card.can_trade","No enough cards in the deck to trade %r." % (self))
				return (False, option)
			else :
				return (True, option)


	def trade(self,option=0):
		self.game.trade_card(self, option)
		pass

	def get_damage(self, amount, target):
		amount = super().get_damage(amount, target)
		if target!=None and getattr(target,'double_damage', 0)==1:
			amount += amount
		if target!=None and getattr(target,'double_damage', 0)==2:
			amount += (2*amount)
		if target!=None and hasattr(target,'get_extra_damage'):
			return amount + target.get_extra_damage
		else:
			return amount

	def SPELL_SCHOOL(self, spell_school):
		return (self.type==CardType.SPELL and self.spell_school==spell_school)
	def MINION_RACE(self, race):
		return (self.type==CardType.MINION and self.race==race)

class LiveEntity(PlayableCard, Entity):
	has_deathrattle = boolean_property("has_deathrattle")
	atk = int_property("atk")
	cant_be_damaged = boolean_property("Cant Be Damaged")
	immune_while_attacking = boolean_property("immune_while_attacking")
	incoming_damage_multiplier = int_property("incoming_damage_multiplier")
	max_health = int_property("max_health")


	def __init__(self, data):
		super().__init__(data)
		self._to_be_destroyed = False
		self.damage = 0
		self.forgetful = False
		self.predamage = 0
		self.turns_in_play = 0
		self.turn_killed = -1
		self.death_processed = False


	def _set_zone(self, value):
		oldzone=self.zone
		newzone=value
		#if Config.LOGINFO:
		#	Config.log("LiveEntity._set_zone","card %s: %s -> %s"%(self, oldzone, newzone))
		if oldzone == Zone.PLAY and newzone == Zone.GRAVEYARD:
			self.turn_killed = self.game.turn
		# See issue #283 (Malorne, Anub'arak)
		self._to_be_destroyed = False # this is a live entity.
		super()._set_zone(value)


	@property
	def immune(self):
		if self.immune_while_attacking and self.attacking:
			return True
		for bf in self.buffs:
			if hasattr(bf,'cant_be_damaged') and bf.cant_be_damaged:
				return True
		return self.cant_be_damaged

	@property
	def damaged(self):
		return bool(self.damage)

	@property
	def deathrattles(self):
		ret = []
		if not self.has_deathrattle:
			return ret
		deathrattle = self.get_actions("deathrattle")
		if deathrattle:
			ret.append(deathrattle)
		for buff in self.buffs:
			for deathrattle in buff.deathrattles:
				ret.append(deathrattle)
		return ret

	@property
	def dead(self):
		return self.zone == Zone.GRAVEYARD or self.to_be_destroyed

	@property
	def alive(self):
		return self.zone != Zone.GRAVEYARD and self.to_be_destroyed==False

	@property
	def delayed_destruction(self):
		return self.zone == Zone.PLAY

	@property
	def to_be_destroyed(self):
		return getattr(self, self.health_attribute) == 0 or self._to_be_destroyed

	@to_be_destroyed.setter
	def to_be_destroyed(self, value):
		self._to_be_destroyed = value

	@property
	def killed_this_turn(self):
		return self.turn_killed == self.game.turn

	def _hit(self, amount):
		self.damage += amount
		return amount

	def hit(self, amount):
		return self.game.cheat_action(self, [actions.Hit(self, amount)])


class Character(LiveEntity):
	health_attribute = "health"
	cant_attack = boolean_property("cant_attack")
	cant_be_targeted_by_opponents = boolean_property("cant_be_targeted_by_opponents")
	cant_be_targeted_by_abilities = boolean_property("cant_be_targeted_by_abilities")
	cant_be_targeted_by_hero_powers = boolean_property("cant_be_targeted_by_hero_powers")
	cant_be_targeted_by_spells=boolean_property("cant_be_targeted_by_spells")
	heavily_armored = boolean_property("heavily_armored")
	ignore_taunt = boolean_property("ignore_taunt")
	min_health = boolean_property("min_health")
	poisonous = boolean_property("poisonous")
	rush = boolean_property("rush")
	taunt = boolean_property("taunt")
	divine_shield = boolean_property("divine_shield")
	cannot_attack_heroes = boolean_property("cannot_attack_heroes")
	buddy_id = int_property("buddy_id") # ID of buddy # battleground
	outcast_card = boolean_property("outcast_card")#
	#gold_card = int_property("gold_card")

	def __init__(self, data):
		self.attack_target = None
		self.frozen = False
		self.num_attacks = 0
		self.race = Race.INVALID
		super().__init__(data)

	@property
	def events(self):
		ret = super().events
		if self.heavily_armored:
			ret += rules.HEAVILY_ARMORED
		return ret

	@property
	def attackable(self):
		return not self.immune

	@property
	def attacking(self):
		return self.attack_target is not None

	@property
	def attack_targets(self):
		targets = self.controller.opponent.characters
		if self.cannot_attack_heroes:
			targets = self.controller.opponent.field
		if self.rush and not self.turns_in_play:
			targets = self.controller.opponent.field

		taunts = []
		if not self.ignore_taunt:
			taunts = targets.filter(taunt=True).filter(attackable=True)

		return (taunts or targets).filter(attackable=True)

	def can_regular_attack(self):
		if self.type==CardType.MINION:
			if self.dormant:
				return False
			elif not self.zone == Zone.PLAY:
				return False
			elif self.cant_attack:
				return False
			elif self.atk==0:
				return False
			elif self.frozen:
				return False
			elif self.should_exit_combat:
				return False
		else:
			return False
		return True

	def can_attack(self, target=None):
		if self.controller.choice:
			return False
		if not self.zone == Zone.PLAY:
			return False
		if self.cant_attack:
			return False
		if not self.controller.current_player:
			return False
		if not self.atk:
			return False
		if self.exhausted:
			return False
		if self.frozen:
			return False
		if not self.attack_targets:
			return False
		if target is not None and target not in self.attack_targets:
			return False
		if self.should_exit_combat:
			return False
		return True

	def can_BG_attack(self, target=None):
		#if self.controller.choice:
		#	return False
		if not self.zone == Zone.PLAY:
			return False
		if self.cant_attack:
			return False
		#if not self.controller.current_player:
		#	return False
		if self.atk==0:
			return False
		if self.exhausted:
			return False
		if self.frozen:
			return False
		if not self.attack_targets:
			return False
		if target is not None and target not in self.attack_targets:
			return False
		return True

	@property
	def max_attacks(self):
		return self.windfury + 1

	@property
	def exhausted(self):
		if self.num_attacks >= self.max_attacks:
			return True
		return False

	@property
	def should_exit_combat(self):
		if self.attacking:
			if self.dead or self.zone != Zone.PLAY:
				return True
		return False

	def attack(self, target):
		if not self.can_attack(target):
			raise InvalidAction("%r can't attack %r." % (self, target))
		self.game.attack(self, target)

	@property
	def health(self):
		return max(0, self.max_health - self.damage)

	@property
	def targets(self):
		if self.zone == Zone.PLAY:
			return self.attack_targets
		return super().targets

	def set_current_health(self, amount):
		return self.game.cheat_action(self, [actions.SetCurrentHealth(self, amount)])


class Hero(Character):
	def __init__(self, data):
		self.armor = 0
		self.power = None
		self.tatal_armor = 0
		self.take_only_one_damage = False
		super().__init__(data)

	@property
	def entities(self):
		yield self
		if self.power:
			yield self.power
		if self.controller.weapon:
			yield self.controller.weapon
		yield from self.buffs

	@property
	def targetable_entities(self):
		yield self
		if self.power:
			yield self.power
		if self.controller.weapon:
			yield self.controller.weapon

	@property
	def windfury(self):
		ret = super().windfury
		if self.controller.weapon:
			# NOTE: As of 9786, Windfury is retained even when the weapon is exhausted.
			return self.controller.weapon.windfury or ret
		return ret

	@property
	def lifesteal(self):
		ret = super().lifesteal
		if self.controller.weapon and not self.controller.weapon.exhausted:
			return self.controller.weapon.lifesteal or ret
		return ret

	@property
	def poisonous(self):
		ret = super().poisonous
		if self.controller.weapon and not self.controller.weapon.exhausted:
			return self.controller.weapon.poisonous or ret
		return ret

	def _getattr(self, attr, i):
		ret = super()._getattr(attr, i)
		if attr == "atk":
			if self.controller.weapon and not self.controller.weapon.exhausted:
				ret += self.controller.weapon.atk
		return ret

	def _set_zone(self, value):
		oldzone=self.zone
		newzone=value
		if Config.LOGINFO:
			Config.log("Hero._set_zone","card %s: %s -> %s"%(self, oldzone, newzone))
		if newzone == Zone.PLAY:
			old_hero = self.controller.hero
			self.controller.hero = self
			# if there is an former hero copy hero's health
			if old_hero:
				self.max_health=old_hero.max_health
				self.damage = old_hero.damage 
				old_hero.zone = Zone.GRAVEYARD
			if self.data.hero_power:
				self.controller.summon(self.data.hero_power)
		elif newzone == Zone.GRAVEYARD:
			if self.power:
				self.power.zone = Zone.GRAVEYARD
			if self.controller.hero is self:
				self.controller.playstate = PlayState.LOSING
		super()._set_zone(value)

	def _hit(self, amount):
		amount = super()._hit(amount)
		if self.armor:
			reduced_damage = min(amount, self.armor)
			if Config.LOGINFO:
				Config.log("BaseCard._hit","%r loses %r armor instead of damage"%(self, reduced_damage))
			self.damage -= reduced_damage
			self.armor -= reduced_damage
		return amount


class Minion(Character):
	charge = boolean_property("charge")
	has_inspire = boolean_property("has_inspire")
	spellpower = int_property("spellpower")
	stealthed = boolean_property("stealthed")
	frenzy = boolean_property("frenzy")
	tech_level = int_property("tech_level") # battlegrounds
	spellcraft_spellcard = boolean_property("spellcraft_spellcard")
	manathirst = boolean_property("manathirst")
	imp = boolean_property("imp")
	extra_deathrattles_minion = boolean_property("extra_deathrattles_base") ## RLK_912
	
	silenceable_attributes = (
		"always_wins_brawls", "aura", "cant_attack", "cant_be_targeted_by_abilities",
		"cant_be_targeted_by_hero_powers", "cant_be_targeted_by_spells", "charge", 
		"divine_shield", "enrage",
		"forgetful", "frozen", "has_deathrattle", "has_inspire", "poisonous",
		"stealthed", "taunt", "windfury", "cannot_attack_heroes", "rush", "frenzy", "honorable_kill",
	)

	def __init__(self, data):
		self.always_wins_brawls = False
		self.enrage = False
		self.silenced = False
		self._summon_index = None
		self.dormant = data.dormant
		#self.guardians_legacy = False
		self.spellpower_fire = 0
		self.spellpower_nature = 0
		self.deathrattle_valid = True
		self.deepcopy_original = None
		self.gem_applied_thisturn=False
		self.tech_level_plus1 = 4
		self.stop_attack=False## if another minion attacks instead of self, this flag will be True
		self.killed_in_former_battle=False ## battlegrounds new 24.4
		self.copied_from_opponent = False
		self.this_is_minion = True
		self.gold_original = None
		super().__init__(data)

	@property
	def ignore_scripts(self):
		return self.silenced

	@property
	def adjacent_minions(self):
		assert self.zone is Zone.PLAY, self.zone
		ret = CardList()
		index = self.zone_position - 1
		left = self.controller.field[:index]
		right = self.controller.field[index + 1:]
		if left:
			ret.append(left[-1])
		if right:
			ret.append(right[0])
		return ret

	@property
	def attackable(self):
		if self.stealthed:
			return False
		if self.dormant:
			return False
		return super().attackable

	@property
	def asleep(self):## need to add something on ULD_180 ####
		return self.zone == Zone.PLAY and not self.turns_in_play and (
			not self.charge and not self.rush)

	@property
	def exhausted(self):
		if self.asleep:
			return True
		return super().exhausted

	@property
	def enraged(self):
		return self.enrage and self.damage

	@property
	def frenzied(self):
		return self.frenzy and self.damage and self.frenzyFlag==0

	@property
	def update_scripts(self):
		yield from super().update_scripts
		if self.enraged:
			yield from self.data.scripts.enrage

	@property
	def zone_position(self):
		if self.zone == Zone.PLAY:
			return self.controller.field.index(self) + 1
		return super().zone_position

	@property
	def BG_is_gold(self):###   battlegrounds
		for value in self.controller.game.parent.BG_Gold.values():
			if self.id==value:
				return True
		return False
	
	def _set_zone(self, value):
		oldzone=self.zone
		newzone=value
		if Config.LOGINFO:
			Config.log("Minion._set_zone","card %s: %s -> %s (%r)"%(self, oldzone, newzone, self.controller))
		if oldzone==Zone.INVALID: ## invalid ->
			if newzone==Zone.PLAY: ## invalid -> field
				if self in self.controller.field:
					pass
				else:
					if self._summon_index is not None:
						self.controller.field.insert(self._summon_index, self)
					else:
						self.controller.field.append(self)
		elif oldzone==Zone.PLAY: ## field ->
			if newzone==Zone.PLAY: ## field -> field
				if self in self.controller.field:
					pass
				else:
					if self._summon_index is not None:
						self.controller.field.insert(self._summon_index, self)
					else:
						self.controller.field.append(self)
			elif newzone == Zone.GRAVEYARD: ## field -> graveyard
				if self in self.controller.field:
					self.controller.field.remove(self)
				self.controller.minions_killed_this_turn += 1
				if not self in self.controller.graveyard:
					self.controller.graveyard.append(self)
				if self.damage>0:
					self.damage = 0
			elif newzone==Zone.SETASIDE: ## field -> setaside
				if self in self.controller.field:
					self.controller.field.remove(self)
				if not self in self.controller.game.setaside:
					self.controller.game.setaside.append(self)
			
		elif oldzone==Zone.HAND: ## hand ->
			if self in self.controller.hand:
				self.controller.hand.remove(self)
			if newzone == Zone.PLAY:## hand -> play,
				if self._summon_index is not None:
					self.controller.field.insert(self._summon_index, self)
				else:
					self.controller.field.append(self)
		elif oldzone==Zone.DECK: ## deck ->
			if self in self.controller.deck:
				self.controller.deck.remove(self)
			if newzone == Zone.PLAY:## deck -> play,
				if self._summon_index is not None:
					self.controller.field.insert(self._summon_index, self)
				else:
					self.controller.field.append(self)
		elif oldzone==Zone.SETASIDE: ## setaside ->
			if self in self.controller.game.setaside:
				self.controller.game.setaside.remove(self)
			if newzone == Zone.PLAY:## setaside -> play,
				if self._summon_index is not None:
					self.controller.field.insert(self._summon_index, self)
				else:
					self.controller.field.append(self)
		if newzone == Zone.GRAVEYARD:## killed 
			if self in self.controller.game.live_entities: ## 'self' is a zombie
				if Config.LOGINFO:
					Config.log("Minion._set_zone","%s turned into a zonbie and live in the live_entries")
				if self in self.controller.live_entities:
					player=self.controller
				elif self in self.controller.opponent.live_entities:
					player=self.controller.opponent
				if not self in player.graveyard:
					player.graveyard.append(self)
				if self in player.field:
					player.field.remove(self)
				elif self in player.hand:
					player.hand.remove(self)
				elif self in player.game.setaside:
					player.game.setaside.remove(self)
		super()._set_zone(value)


	def _hit(self, amount):
		###  Remove the routine of 'divine shield prevents damages' -> class Damage'
		amount = super()._hit(amount)

		if self.health < self.min_health:
			if Config.LOGINFO:
				Config.log("BaseCard._hit","%r has HEALTH_MINIMUM of %i"%(self, self.min_health))
			self.damage = self.max_health - self.min_health

		return amount

	def bounce(self):
		return self.game.cheat_action(self, [actions.Bounce(self)])

	def is_summonable(self):
		summonable = super().is_summonable()
		if len(self.controller.field) >= self.game.MAX_MINIONS_ON_FIELD:
			return False
		return summonable

	def silence(self):
		return self.game.cheat_action(self, [actions.Silence(self)])

	def can_attack(self, target=None):
		if self.dormant:
			return False

		return super().can_attack(target)


class Spell(PlayableCard):
	spell_school = int_property("spell_school") #
	freeze = boolean_property('freeze') #
	spellcraft_spellcard = boolean_property("spellcraft_spellcard")

	def __init__(self, data):
		self.immune_to_spellpower = False
		self.receives_double_spelldamage_bonus = False
		self.repeatable=False # TSC_952
		self.spell_cast_twice=False
		self.copied_from_opponent = False
		self.spellpower_by_spell = 0
		self.this_is_spell = True
		super().__init__(data)

	def get_damage(self, amount, target):
		amount = super().get_damage(amount, target)
		if not self.immune_to_spellpower:
			if self.spell_school==SpellSchool.FIRE:
				amount = self.controller.get_spell_damage_fire(amount)
			elif self.spell_school==SpellSchool.NATURE:
				amount = self.controller.get_spell_damage_nature(amount)
			else:
				amount = self.controller.get_spell_damage(amount)
		if self.receives_double_spelldamage_bonus:
			amount *= 2
		return amount

	def play(self, target=None, index=None, choose=None):
		self.controller.times_spell_played_this_game += 1
		self.controller.times_spells_played_this_turn += 1 #
		self.controller.spells_played_this_turn.append(self) #
		if target!=None and target.controller==self.controller: #
			self.controller.times_spell_to_friendly_minion_this_game += 1 #
		return super().play(target, index, choose)

	def _set_zone(self, value):
		oldzone=self.zone
		newzone=value
		if Config.LOGINFO:
			Config.log("Spell._set_zone","card %r: %s -> %s "%(self, oldzone, newzone))
		if newzone==Zone.PLAY:
			if oldzone==Zone.HAND and self in self.controller.hand:
				self.controller.hand.remove(self)
			if oldzone==Zone.SETASIDE and self in self.controller.game.setaside:
				self.controller.game.setaside.remove(self)
			if oldzone==Zone.DECK and self in self.controller.deck:
				self.controller.deck.remove(self)
		super()._set_zone(value)
		

class Secret(PlayableCard):
	spell_school = int_property("spell_school") #
	freeze = boolean_property('freeze') #
	spellcraft_spellcard = boolean_property("spellcraft_spellcard")

	def __init__(self, data):
		self.immune_to_spellpower = False
		self.receives_double_spelldamage_bonus = False
		self.repeatable=False # TSC_952
		self.spell_cast_twice=False
		self.copied_from_opponent = False		
		self.this_is_secret=True
		super().__init__(data)

	@property
	def events(self):
		ret = super().events
		if (self.zone == Zone.SECRET or self.zone == Zone.PLAY) and not self.exhausted:
			ret += self.data.scripts.secret
		return ret

	@property
	def exhausted(self):
		return self.zone == Zone.SECRET and self.controller.current_player

	@property
	def zone_position(self):
		if self.zone == Zone.SECRET:
			return self.controller.secrets.index(self) + 1
		return super().zone_position

	def _set_zone(self, value):
		oldzone=self.zone
		newzone=value
		if Config.LOGINFO:
			Config.log("Secret._set_zone","card %s: %s -> %s"%(self, oldzone, newzone))
		if newzone == Zone.PLAY or newzone == Zone.SECRET:
			# Move secrets to the SECRET Zone when played
			self._zone = Zone.SECRET
			if not self in self.controller.secrets:
				self.controller.secrets.append(self)
		if oldzone == Zone.SECRET:
			self.controller.secrets.remove(self)
			if newzone==Zone.GRAVEYARD:
				self.controller.graveyard.append(self)
		super()._set_zone(value)

	def is_summonable(self):
		# secrets are all unique
		if self.controller.secrets.contains(self):
			return False
		return super().is_summonable()

	def play(self, target=None, index=None, choose=None):
		self.controller.times_secret_played_this_game += 1
		return super().play(target, index, choose)


class Enchantment(BaseCard):
	atk = int_property("atk")
	cost = int_property("cost")
	has_deathrattle = boolean_property("has_deathrattle")
	incoming_damage_multiplier = int_property("incoming_damage_multiplier")
	max_health = int_property("max_health")
	spellpower = int_property("spellpower")
	buffs = []
	slots = []

	def __init__(self, data):
		self.deepcopy_original = None
		self.one_turn_effect = False
		self.permanent_buff = False ## for spellcraft in battleground 
		self.additional_deathrattles = []
		self.sidequest_counter = 0# Sidequest
		self.sidequest_list0=[]# sidequest, #REV_000e
		self.this_is_enchantment=True
		super().__init__(data)

	@property
	def events(self):
		if self.owner!=None and self.owner.zone == Zone.HAND:
			return self.data.scripts.Hand.events
		if self.owner!=None and self.owner.zone == Zone.DECK:## EX1_295, SW_072 occurs an error
			# in existing cards, there isn't one with Deck class.  However, rarely they come here.
			return self.data.scripts.Deck.events
		return self.base_events + self._events

	@property
	def deathrattles(self):
		if not self.has_deathrattle:
			return []
		ret = self.additional_deathrattles[:]
		deathrattle = self.get_actions("deathrattle")
		if deathrattle:
			ret.append(deathrattle)
		if not ret:
			#raise NotImplementedError("Missing deathrattle script for %r" % (self))
			pass
		return ret

	def _getattr(self, attr, i):
		i += getattr(self, "_" + attr, 0)
		return getattr(self.data.scripts, attr, lambda s, x: x)(self, i)

	def _set_zone(self, value):
		oldzone = self.zone
		newzone = value
		if Config.LOGINFO:
			Config.log("Enchantment._set_zone","card %s: %s -> %s"%(self, oldzone, newzone))
		if newzone == Zone.PLAY:
			if self in self.controller.field:
				self.controller.field.remove(self)
			self.owner.buffs.append(self)
		elif newzone == Zone.REMOVEDFROMGAME or newzone == Zone.GRAVEYARD:
			if oldzone == newzone:
				# Can happen if a Destroy is queued after a bounce, for example
				pass
			if self.controller!=None:
				if self in self.controller.graveyard:
					self.controller.graveyard.remove(self)
			if getattr(self, 'owner', None)!=None:
				if self in self.owner.buffs:
					self.owner.buffs.remove(self)
			if getattr(self, 'game', None)!=None:
				if self in self.game.active_aura_buffs:
					self.game.active_aura_buffs.remove(self)
		super()._set_zone(newzone)


	def apply(self, target):
		if Config.LOGINFO:
			Config.log("Enchantment.apply","Applying %r to %r"% (self, target))
		self.owner = target
		if hasattr(self.data.scripts, "apply"):
			self.data.scripts.apply(self, target)
		if hasattr(self.data.scripts, "max_health"):
			if Config.LOGINFO:
				Config.log("Enchantment.apply","%r removes all damage from %r"%(self, target))
			target.damage = 0
		self.zone = Zone.PLAY
		return self

	def remove(self):
		self.zone = Zone.REMOVEDFROMGAME


class Weapon(rules.WeaponRules, LiveEntity):
	health_attribute = "durability"

	def __init__(self, *args):
		super().__init__(*args)
		self.damage = 0
		self.deathrattle_valid = True
		self.sidequest_list0=[]

	@property
	def durability(self):
		return max(0, self.max_durability - self.damage)

	@property
	def max_durability(self):
		ret = self._max_durability
		ret += self._getattr("max_health", 0)
		return max(0, ret)

	@max_durability.setter
	def max_durability(self, value):
		self._max_durability = value

	@property
	def exhausted(self):
		return self.zone == Zone.PLAY and not self.controller.current_player

	def _set_zone(self, value):
		oldzone=self.zone
		newzone=value
		if Config.LOGINFO:
			Config.log("Weapon._set_zone","card %s: %s -> %s"%(self, oldzone, newzone))
		if newzone == Zone.PLAY:
			if self.controller.weapon:
				self.controller.graveyard.append(self.controller.weapon)
				self.controller.weapon._zone=Zone.GRAVEYARD
				self.controller.weapon=None
			if oldzone==Zone.DECK and self in self.controller.deck:
				self.controller.deck.remove(self)
			if oldzone==Zone.HAND and self in self.controller.hand:
				self.controller.hand.remove(self)
			if oldzone==Zone.SETASIDE and self in self.controller.game.setaside:
				self.controller.game.setaside.remove(self)
			self.controller.weapon = self
		elif newzone==Zone.GRAVEYARD:
			if not self in self.controller.graveyard:
				self.controller.graveyard.append(self)
				self._zone=Zone.GRAVEYARD
				self.controller.weapon = None
		super()._set_zone(value)


class HeroPower(PlayableCard):
	additional_activations = int_property("additional_activations")
	passive_power = int_property("passive_power")
	playable_zone = Zone.PLAY

	def __init__(self, data):
		super().__init__(data)
		self.activations_this_turn = 0
		self.old_power = None
		self.deepcopy_original = None
		self.this_is_heropower = True

	@property
	def exhausted(self):
		if self.additional_activations == -1:
			return False
		return self.activations_this_turn >= 1 + self.additional_activations

	def _set_zone(self, value):
		oldzone=self.zone
		newzone=value
		if Config.LOGINFO:
			Config.log("HeroPower._set_zone","card %s: %s -> %s"%(self, oldzone, newzone))
		if newzone == Zone.PLAY:
			if self.controller.hero.power:
				self.controller.graveyard.append(self.controller.hero.power)
				self.controller.hero.power._zone=Zone.GRAVEYARD
			self.controller.hero.power = self
		if oldzone == Zone.PLAY and newzone==Zone.GRAVEYARD:
			self.controller.graveyard.append(self)
			self._zone=Zone.GRAVEYARD
			self.controller.hero.power = None
		super()._set_zone(value)

	def activate(self):
		return self.game.queue_actions(self.controller, [actions.Activate(self, self.target)])

	def get_damage(self, amount, target):
		amount = super().get_damage(amount, target)
		amount += self.controller.heropower_damage
		amount <<= self.controller.hero_power_double
		return amount

	def use(self, target=None):
		if not self.is_usable():
			raise InvalidAction("%r can't be used." % (self))

		if Config.LOGINFO:
			Config.log("HeroPower.use","%s uses hero power %r on %r"%(self.controller, self, target))

		if self.requires_target():
			if not target:
				raise InvalidAction("%r requires a target." % (self))
			if self.controller.all_targets_random and len(self.play_targets):
				new_target = random.choice(self.play_targets)
				if Config.LOGINFO:
					Config.log("HeroPower.use","Retargeting %r from %r to %r"%(self, target, new_target))
				target = new_target
			self.target = target
		elif target:
			if Config.LOGINFO:
				Config.log("HeroPower.use","%r does not require a target, ignoring target %r"%(self, target))

		ret = self.activate()

		self.controller.times_hero_power_used_this_game += 1
		self.target = None

		return ret

	def is_usable(self):
		if self.exhausted:
			return False
		if self.passive_power:## if hero.power is passive, there are no need to activate
			return False
		return super().is_playable()

class Location(PlayableCard):
	to_be_destroyed=False
	turns_in_play=0
	dormant=0
	cant_be_targeted_by_opponents=True
	_summon_index=None

	@property
	def events(self):
		ret = super().events
		if self.zone == Zone.SECRET:
			ret += self.data.scripts.secret
		return ret

	@property
	def exhausted(self):
		return self.zone == Zone.SECRET and self.controller.current_player

	@property
	def zone_position(self):
		if self.zone == Zone.SECRET:
			return self.controller.secrets.index(self) + 1
		return super().zone_position

	def _set_zone(self, value):
		if Config.LOGINFO:
			Config.log("Location._set_zone","card %s: %s -> %s"%(self, self.zone, value))
		if value == Zone.PLAY:## hand -> play, or deck -> play, or setaside -> play
			if self._summon_index is not None:
				self.controller.field.insert(self._summon_index, self)
			else:
				self.controller.field.append(self)
		super()._set_zone(value)
		
	def is_summonable(self):
		return super().is_summonable()

	def play(self, target=None, index=None, choose=None):
		return super().play(target, index, choose)

	@property
	def attackable(self):
		return False
	@property
	def can_attack(self, target=None):
		return False

	def location(self, target):
		actions = self.get_actions("location")
		if self.dormant!=0:
			return
		if not isinstance(actions, list) and not isinstance(actions, tuple):
			actions = [actions]
		for action in actions:
			action.trigger(self)
		self.max_health -= 1
		if self.max_health<=0:
			self.destroy()
		else:
			self.dormant=3


class QuestReward(PlayableCard):
	sidequest_counter=0
	quest_progress_total=int_property('quest_progress_total')
	this_is_questreward=True
	this_is_secret=True
	script_data_num_1=None

	@property
	def events(self):
		ret = super().events
		if (self.zone == Zone.SECRET or self.zone == Zone.PLAY) and hasattr(self.data.scripts, 'reward'):
			ret += self.data.scripts.reward
		return ret
	@property
	def exhausted(self):
		return self.zone == Zone.SECRET and self.controller.current_player
	@property
	def zone_position(self):
		if self.zone == Zone.SECRET:
			return self.controller.secrets.index(self) + 1
		return super().zone_position
	def _set_zone(self, value):
		newzone=value
		if Config.LOGINFO:
			Config.log("QuestReward._set_zone","card %s: %s -> %s"%(self, self.zone, newzone))
		if newzone == Zone.PLAY:
			# Move secrets to the SECRET Zone when played
			self.controller.rewards.append(self)
			self._zone = Zone.SECRET
		elif newzone == Zone.SECRET:
			self.controller.rewards.append(self)
			self._zone = Zone.SECRET
		elif newzone == Zone.GRAVEYARD:
			if self in self.controller.rewards:
				self.controller.rewards.remove(self)
			if self in self.controller.secrets:
				self.controller.secrets.remove(self)
			if self in self.controller.quests:
				self.controller.quests.remove(self)
		super()._set_zone(value)

	def is_summonable(self):
		# secrets are all unique
		if self.controller.secrets.contains(self):
			return False
		return super().is_summonable()
	def play(self, target=None, index=None, choose=None):
		self.controller.times_secret_played_this_game += 1
		return super().play(target, index, choose)
	pass

class Sidequest(PlayableCard):
	spell_school = int_property("spell_school") #
	freeze = boolean_property('freeze') #
	spellcraft_spellcard = boolean_property("spellcraft_spellcard")
	quest_progress_total=int_property('quest_progress_total')

	def __init__(self, data):
		self.immune_to_spellpower = False
		self.receives_double_spelldamage_bonus = False
		self.repeatable=False # TSC_952
		self.spell_cast_twice=False
		self.copied_from_opponent = False		
		self.sidequest_counter=0
		self.this_is_secret=True
		super().__init__(data)

	@property
	def events(self):
		ret = super().events
		if self.zone == Zone.SECRET:
			ret += self.data.scripts.secret
		return ret

	@property
	def exhausted(self):
		return self.zone == Zone.SECRET and self.controller.current_player

	@property
	def zone_position(self):
		if self.zone == Zone.SECRET:
			return self.controller.secrets.index(self) + 1
		return super().zone_position

	def _set_zone(self, value):
		oldzone=self.zone
		newzone=value
		if Config.LOGINFO:
			Config.log("Sidequest._set_zone","card %s: %s -> %s"%(self, oldzone, newzone))
		if self.zone == Zone.HAND:
			self.controller.hand.remove(self)
		elif self.zone == Zone.DECK:
			self.controller.deck.remove(self)
		if newzone == Zone.PLAY:
			# Move secrets to the SECRET Zone when played
			self._zone = Zone.SECRET
			self.controller.quests.append(self)
		elif newzone == Zone.SECRET:
			self._zone = Zone.SECRET
			self.controller.quests.append(self)
		elif newzone == Zone.GRAVEYARD:
			self._zone = Zone.GRAVEYARD
			self.controller.graveyard.append(self)
			if self in self.controller.secrets:
				self.controller.secrets.remove(self)
			if self in self.controller.quests:
				self.controller.quests.remove(self)
		super()._set_zone(value)

	def is_summonable(self):
		# secrets are all unique
		if self.controller.secrets.contains(self):
			return False
		return super().is_summonable()

	def play(self, target=None, index=None, choose=None):
		self.controller.times_secret_played_this_game += 1
		return super().play(target, index, choose)
