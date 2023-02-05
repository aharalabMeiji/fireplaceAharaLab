from pickle import NONE
import random

from hearthstone.enums import CardClass, CardType, GameTag, PlayReq, Race, Rarity
from hearthstone.utils import CARDRACE_TAG_MAP

from ..actions import *
from ..aura import Refresh
from ..dsl import *
from ..events import *


# For buffs which are removed when the card is moved to play (eg. cost buffs)
# This needs to be Summon, because of Summon from the hand
REMOVED_IN_PLAY = Summon(PLAYER, OWNER).after(Destroy(SELF))

ENEMY_CLASS = Attr(ENEMY_HERO, GameTag.CLASS)
FRIENDLY_CLASS = Attr(FRIENDLY_HERO, GameTag.CLASS)


#Freeze = lambda target: SetTag(target, (GameTag.FROZEN, )) ##
Stealth = lambda target: SetTag(target, (GameTag.STEALTH, ))
Unstealth = lambda target: UnsetTag(target, (GameTag.STEALTH, ))
Taunt = lambda target: SetTag(target, (GameTag.TAUNT, ))
GiveCharge = lambda target: SetTag(target, (GameTag.CHARGE, ))
GiveDivineShield = lambda target: SetTag(target, (GameTag.DIVINE_SHIELD, ))
GiveWindfury = lambda target: SetTag(target, (GameTag.WINDFURY, ))


CLEAVE = Hit(TARGET_ADJACENT, ATK(SELF))
COINFLIP = RandomNumber(0, 1) == 1
EMPTY_BOARD = Count(FRIENDLY_MINIONS) == 0
EMPTY_HAND = Count(FRIENDLY_HAND) == 0
FULL_BOARD = Count(FRIENDLY_MINIONS) == 7
FULL_HAND = Count(FRIENDLY_HAND) == 10
HOLDING_DRAGON = Find(FRIENDLY_HAND + DRAGON - SELF)

DISCOVER = lambda *args: Discover(CONTROLLER, *args)

BASIC_HERO_POWERS = [
	"HERO_01bp", "HERO_02bp", "HERO_03bp",
	"HERO_04bp", "HERO_05bp", "HERO_06bp",
	"HERO_07bp", "HERO_08bp", "HERO_09bp",
	#"HERO_10bp",
]

CARDCLASSES=[
	CardClass.DEATHKNIGHT,
	CardClass.DEMONHUNTER,
	CardClass.DRUID,
	CardClass.HUNTER,
	CardClass.MAGE,
	CardClass.PALADIN,
	CardClass.PRIEST,
	CardClass.ROGUE,
	CardClass.SHAMAN,
	CardClass.WARLOCK,
	CardClass.WARRIOR,
   ]
CLASSES_EXCEPT_ROGUE=[
	CardClass.DEATHKNIGHT,
	CardClass.DEMONHUNTER,
	CardClass.DRUID,
	CardClass.HUNTER,
	CardClass.MAGE,
	CardClass.PALADIN,
	CardClass.PRIEST,
	CardClass.SHAMAN,
	CardClass.WARLOCK,
	CardClass.WARRIOR,
   ]
CLASSES_EXCEPT_PALADIN=[
	CardClass.DEMONHUNTER,
	CardClass.DRUID,
	CardClass.HUNTER,
	CardClass.MAGE,
	CardClass.PRIEST,
	CardClass.ROGUE,
	CardClass.SHAMAN,
	CardClass.WARLOCK,
	CardClass.WARRIOR,
   ]
RACES=[
	Race.INVALID,
	Race.MURLOC,
	Race.DEMON,
	Race.MECHANICAL,
	Race.ELEMENTAL,
	Race.BEAST,
	Race.PIRATE,
	Race.DRAGON,
	Race.ALL,
	Race.QUILBOAR,
	Race.NAGA,
	Race.UNDEAD
]

OTHERCLASSES = lambda myclass: CARDCLASSES.remove(myclass)

def race_identity(target, param):
	""" def race_identity(target, param): """
	if target.type==CardType.MINION:
		if target.race==param:
			return True
		if target.data.tags.get(CARDRACE_TAG_MAP[param]):
			return True
	return False

POTIONS = [
	"CFM_021",  # Freezing Potion
	"CFM_065",  # Volcanic Potion
	"CFM_620",  # Potion of Polymorph
	"CFM_603",  # Potion of Madness
	"CFM_604",  # Greater Healing Potion
	"CFM_661",  # Pint-Size Potion
	"CFM_662",  # Dragonfire Potion
	"CFM_094",  # Felfire Potion
	"CFM_608",  # Blastcrystal Potion
	"CFM_611",  # Bloodfury Potion
]

LIBRAMS = IDS([
	"BT_011",  # Libram of Justice
	"BT_024",  # Libram of Hope
	"BT_025",  # Libram of Wisdom
])

RandomBasicTotem = lambda *args: RandomID("CS2_050", "CS2_051", "CS2_052", "NEW1_009")
RandomBasicHeroPower = lambda *args: RandomID(*BASIC_HERO_POWERS)
RandomPotion = lambda *args: RandomID(*POTIONS)

# 50% chance to attack the wrong enemy.
FORGETFUL = Attack(SELF).on(
	COINFLIP & Retarget(SELF, RANDOM(ALL_CHARACTERS - Attack.DEFENDER - CONTROLLED_BY(SELF)))
)

AT_MAX_MANA = lambda s: MANA(s) == 10
CHECK_CTHUN = ATK(HIGHEST_ATK(CTHUN)) >= 10


class JoustHelper(Evaluator):
	"""
	A helper evaluator class for jousts to allow JOUST & ... syntax.
	"""
	def __init__(self, challenger, defender):
		self.challenger = challenger
		self.defender = defender
		super().__init__()

	def trigger(self, source):
		action = Joust(self.challenger, self.defender).then(
			JoustEvaluator(Joust.CHALLENGER, Joust.DEFENDER) & self._if | self._else
		)

		return action.trigger(source)


JOUST = JoustHelper(
	RANDOM(FRIENDLY_DECK + MINION),
	RANDOM(ENEMY_DECK + MINION)
)
RECRUIT = lambda selector: Summon(CONTROLLER, RANDOM(FRIENDLY_DECK + selector))


def SET(amt):
	return lambda self, i: amt


# Buff helper
def buff(atk=0, health=0, **kwargs):
	buff_tags = {}
	if atk:
		buff_tags[GameTag.ATK] = atk
	if health:
		buff_tags[GameTag.HEALTH] = health

	for tag in GameTag:
		if tag.name.lower() in kwargs.copy():
			buff_tags[tag] = kwargs.pop(tag.name.lower())

	if "immune" in kwargs:
		value = kwargs.pop("immune")
		buff_tags[GameTag.CANT_BE_DAMAGED] = value
		buff_tags[GameTag.CANT_BE_TARGETED_BY_OPPONENTS] = value

	if kwargs:
		raise NotImplementedError(kwargs)

	class Buff:
		tags = buff_tags

	return Buff


def AttackHealthSwapBuff():
	def apply(self, target):
		self._xatk = target.health
		self._xhealth = target.atk
		target.damage = 0

	cls = buff()
	cls.atk = lambda self, i: self._xatk
	cls.max_health = lambda self, i: self._xhealth
	cls.apply = apply

	return cls


def GainEmptyMana(selector, amount):
	"""
	Helper to gain an empty mana crystal (gains mana, then spends it)
	"""
	return GainMana(selector, amount), SpendMana(selector, amount)


def custom_card(cls):
	from . import CardDB, db
	id = cls.__name__
	if GameTag.CARDNAME not in cls.tags:
		raise ValueError("No name provided for custom card %r" % (cls))
	db[id] = CardDB.merge(id, None, cls)
	# Give the card its fake name
	db[id].strings = {
		GameTag.CARDNAME: {"enUS": cls.tags[GameTag.CARDNAME]},
		GameTag.CARDTEXT_INHAND: {"enUS": ""}
	}
	return cls

def choiceAction(player):
	while True:
		if player.choice == None:
			return
		else:
			if player.choiceStrategy==None:
				if len(player.choice.cards)==0:
					choice = None
				else:
					choice = random.choice(player.choice.cards)
			else:
				choice = player.choiceStrategy(player,player.choice.cards)
			if Config.LOGINFO:
				Config.log("BG_utils.choiceAction","%r Chooses a card %r from %r" % (player, choice, player.choice.cards))
			#myChoiceStr = str(choice)
			if 'RandomCardPicker' in str(choice):
				myCardID =  random.choice(choice.find_cards())
				Give(player,myCardID).trigger(player)
				player.choice = None
			else :
				if choice == None:
					player.choice=None##return
				else:
					player.choice.choose(choice)


def exactCopy(card, source):
	ret = source.controller.card(card.id, source)
	ret.zone=Zone.SETASIDE
	for k in card.silenceable_attributes:
		v = getattr(card, k)
		setattr(ret, k, v)
	ret.silenced = card.silenced
	ret.damage = card.damage
	for buff in card.buffs:
		# Recreate the buff stack
		card.buff(ret, buff.id)
	ret.script_data_text_0=card.script_data_text_0
	return ret

def get00(card):
	if isinstance(card, list) or isinstance(card, tuple):
		if len(card)>0:
			card=card[0]
		else:
			card=None
	if isinstance(card, list) or isinstance(card, tuple):
		if len(card)>0:
			card=card[0]
		else:
			card=None
	return card


REQUIRE_ENEMY_MINION_TARGET={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }

REQUIRE_FRIEND_MINION_TARGET={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }


#sample 

class t_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=target
		pass

class c_Action(GameAction):
	PLAYER=ActionArg()
	def do(self, source, player):
		pass

class c_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		card.zone=Zone.HAND
		pass




	def play(self):
		controller=self.controller
		source=self
		target=self.target
		actions=[action for action in self.controller._targetedaction_log if isinstance(action['class'], Battlecry)]
		cards=[card for card in self.controller.play_log if card.type==CardType.SPELL]
@custom_card
class original_e:
	tags = {
		GameTag.CARDNAME: "ZZZZ",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
	}

