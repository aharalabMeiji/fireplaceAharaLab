
from ..utils import *

Classic_Druid=[]

Classic_Claw=True  ###
Classic_Healing_Touch=True  ###
Classic_Moonfire=True  ###
Classic_Mark_of_the_Wild=True  ###
Classic_Savage_Roar=True  ###
Classic_Swipe=True  ###
Classic_Wild_Growth=True  ###
Classic_Ironbark_Protector=True  ###
Classic_Wrath=True  ###
Classic_Mark_of_Nature=True  ###
Classic_Soul_of_the_Forest=True  ###
Classic_Power_of_the_Wild=True  ###
Classic_Naturalize=True  ###
Classic_Nourish=True  ###
Classic_Druid_of_the_Claw=True  ###
Classic_Keeper_of_the_Grove=True  ###
Classic_Innervate=True  ###
Classic_Starfire=True  ###
Classic_Ancient_of_War=True  ###
Classic_Bite=True  ###
Classic_Force_of_Nature=True  ###
Classic_Cenarius=True  ###
Classic_Savagery=True  ###
Classic_Treant=True  ###
Classic_Shapeshift=True  ###
Classic_Dire_Shapeshift=True  ###
Classic_Starfall=True  ###
Classic_Ancient_of_Lore=True  ###

if Classic_Claw:# 
	Classic_Druid+=['VAN_CS2_005','CS2_005o']
class VAN_CS2_005:# <2>[1646]
	""" Claw
	Give your hero +2_Attack this turn. Gain 2 Armor. """
	play = Buff(FRIENDLY_HERO, "CS2_005o"), GainArmor(FRIENDLY_HERO, 2)
	pass
CS2_005o = buff(atk=2)

if Classic_Healing_Touch:# 
	Classic_Druid+=['VAN_CS2_007']
class VAN_CS2_007:# <2>[1646]
	""" Healing Touch
	Restore #8 Health. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Heal(TARGET, 8)
	pass

if Classic_Moonfire:# 
	Classic_Druid+=['VAN_CS2_008']
class VAN_CS2_008:# <2>[1646]
	""" Moonfire
	Deal $1 damage. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 1)
	pass

if Classic_Mark_of_the_Wild:# 
	Classic_Druid+=['VAN_CS2_009']
	Classic_Druid+=['VAN_CS2_009e']
class VAN_CS2_009:# <2>[1646]
	""" Mark of the Wild
	Give a minion [Taunt] and +2/+2.<i>(+2 Attack/+2 Health)</i> """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "CS2_009e")
	pass
VAN_CS2_009e = buff(+2, +2, taunt=True)

if Classic_Savage_Roar:# 
	Classic_Druid+=['VAN_CS2_011','CS2_011o']
class VAN_CS2_011:# <2>[1646]
	""" Savage Roar
	Give your characters +2_Attack this turn. """
	play = Buff(FRIENDLY_CHARACTERS, "CS2_011o")
	pass
CS2_011o = buff(atk=2)

if Classic_Swipe:# 
	Classic_Druid+=['VAN_CS2_012']
class VAN_CS2_012:# <2>[1646]
	""" Swipe
	Deal $4 damage to an enemy and $1 damage to all other enemies. """
	requirements = {PlayReq.REQ_ENEMY_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 4), Hit(ENEMY_CHARACTERS - TARGET, 1)
	pass

if Classic_Wild_Growth:# 
	Classic_Druid+=['VAN_CS2_013']
class VAN_CS2_013:# <2>[1646]
	""" Wild Growth
	Gain an empty Mana Crystal. """
	play = (
		AT_MAX_MANA(CONTROLLER) &
		Give(CONTROLLER, "CS2_013t") |
		GainEmptyMana(CONTROLLER, 1)
	)
	pass
class CS2_013t:
	play = Draw(CONTROLLER)

if Classic_Ironbark_Protector:# 
	Classic_Druid+=['VAN_CS2_232']
class VAN_CS2_232:# <2>[1646]
	""" Ironbark Protector
	[Taunt] """
	#
	pass

if Classic_Wrath:# 
	Classic_Druid+=['VAN_EX1_154']
	Classic_Druid+=['VAN_EX1_154a']
	Classic_Druid+=['VAN_EX1_154b']
class VAN_EX1_154:# <2>[1646]
	""" Wrath
	[Choose One -]Deal $3 damage to a minion; or $1 damageand draw a card. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	choose = ("VAN_EX1_154a", "VAN_EX1_154b")
	play = ChooseBoth(CONTROLLER) & (Hit(TARGET, 3), Hit(TARGET, 1), Draw(CONTROLLER))
	pass

class VAN_EX1_154a:# <2>[1646]
	""" Solar Wrath
	Deal $3 damage to a minion. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 3)
	pass

class VAN_EX1_154b:# <2>[1646]
	""" Nature's Wrath
	Deal $1 damage to a minion. Draw a card. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 1), Draw(CONTROLLER)
	pass

if Classic_Mark_of_Nature:# 
	Classic_Druid+=['VAN_EX1_155']
	Classic_Druid+=['VAN_EX1_155a','EX1_155ae']
	Classic_Druid+=['VAN_EX1_155b','EX1_155be']
class VAN_EX1_155:# <2>[1646]
	""" Mark of Nature
	[Choose One -] Give a minion +4 Attack; or +4 Health and [Taunt]. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	choose = ("VAN_EX1_155a", "VAN_EX1_155b")
	play = ChooseBoth(CONTROLLER) & (
		Buff(TARGET, "EX1_155ae"), Buff(TARGET, "EX1_155be")
	)
	pass

class VAN_EX1_155a:# <2>[1646]
	""" Tiger's Fury
	+4 Attack. """
	play = Buff(TARGET, "EX1_155ae")
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	pass
EX1_155ae = buff(atk=4)

class VAN_EX1_155b:# <2>[1646]
	""" Thick Hide
	+4 Health and [Taunt]. """
	play = Buff(TARGET, "EX1_155be")
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	pass
EX1_155be = buff(health=4, taunt=True)

if Classic_Soul_of_the_Forest:# 
	Classic_Druid+=['VAN_EX1_158']
	Classic_Druid+=['VAN_EX1_158e']
class VAN_EX1_158:# <2>[1646]
	""" Soul of the Forest
	Give your minions "[Deathrattle:] Summon a 2/2 Treant." """
	play = Buff(FRIENDLY_MINIONS, "VAN_EX1_158e")
	pass

class VAN_EX1_158e:# <2>[1646]
	""" Soul of the Forest
	[Deathrattle:] Summon a 2/2 Treant. """
	deathrattle = Summon(CONTROLLER, "EX1_158t")
	tags = {GameTag.DEATHRATTLE: True}
	pass
class EX1_158t:
	"""   """

if Classic_Power_of_the_Wild:# 
	Classic_Druid+=['VAN_EX1_160']
	Classic_Druid+=['VAN_EX1_160a',"EX1_160t"]
	Classic_Druid+=['VAN_EX1_160b','EX1_160be']
class VAN_EX1_160:# <2>[1646]
	""" Power of the Wild
	[Choose One -] Give your minions +1/+1; or Summon a 3/2 Panther. """
	choose = ("VAN_EX1_160a", "VAN_EX1_160b")
	play = ChooseBoth(CONTROLLER) & (
		Buff(FRIENDLY_MINIONS, "EX1_160be"), Summon(CONTROLLER, "EX1_160t")
	)
	pass

class VAN_EX1_160a:# <2>[1646]
	""" Summon a Panther
	Summon a 3/2 Panther. """
	play = Summon(CONTROLLER, "EX1_160t")
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	pass
class EX1_160t:
	""" Panther
	""" 
	pass

class VAN_EX1_160b:# <2>[1646]
	""" Leader of the Pack
	Give your minions +1/+1. """
	play = Buff(FRIENDLY_MINIONS, "EX1_160be")
	pass
EX1_160be = buff(+1, +1)

if Classic_Naturalize:# 
	Classic_Druid+=['VAN_EX1_161']
class VAN_EX1_161:# <2>[1646]
	""" Naturalize
	Destroy a minion.Your opponent draws 2_cards. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Destroy(TARGET), Draw(OPPONENT) * 2
	pass

if Classic_Nourish:# 
	Classic_Druid+=['VAN_EX1_164']
	Classic_Druid+=['VAN_EX1_164a']
	Classic_Druid+=['VAN_EX1_164b']
class VAN_EX1_164:# <2>[1646]
	""" Nourish
	[Choose One -] Gain 2_Mana Crystals; or Draw 3 cards. """
	choose = ("VAN_EX1_164a", "VAN_EX1_164b")
	play = ChooseBoth(CONTROLLER) & (GainMana(CONTROLLER, 2), Draw(CONTROLLER) * 3)
	pass

class VAN_EX1_164a:# <2>[1646]
	""" Rampant Growth
	Gain 2 Mana Crystals. """
	play = GainMana(CONTROLLER, 2)
	pass

class VAN_EX1_164b:# <2>[1646]
	""" Enrich
	Draw 3 cards. """
	play = Draw(CONTROLLER) * 3
	pass

if Classic_Druid_of_the_Claw:# 
	Classic_Druid+=['VAN_EX1_165','OG_044a']
	Classic_Druid+=['VAN_EX1_165a']
	Classic_Druid+=['VAN_EX1_165b']
	Classic_Druid+=['VAN_EX1_165t1']
	Classic_Druid+=['VAN_EX1_165t2']
class VAN_EX1_165:# <2>[1646]
	""" Druid of the Claw
	[Choose One -] [Charge]; or +2 Health and [Taunt]. """
	choose = ("VAN_EX1_165a", "VAN_EX1_165b")
	play = ChooseBoth(CONTROLLER) & Morph(SELF, "OG_044a")
	pass
#OG_044a
class VAN_EX1_165a:# <2>[1646]
	""" Cat Form
	[Charge] """
	play = Morph(SELF, "VAN_EX1_165t1")
	pass

class VAN_EX1_165b:# <2>[1646]
	""" Bear Form
	+2 Health and [Taunt] """
	play = Morph(SELF, "VAN_EX1_165t2")
	pass

class VAN_EX1_165t1:# <2>[1646]
	""" Druid of the Claw
	[Charge] """
	#
	pass

class VAN_EX1_165t2:# <2>[1646]
	""" Druid of the Claw
	[Taunt] """
	#
	pass

if Classic_Keeper_of_the_Grove:# 
	Classic_Druid+=['VAN_EX1_166']
	Classic_Druid+=['VAN_EX1_166a']
	Classic_Druid+=['VAN_EX1_166b']
class VAN_EX1_166:# <2>[1646]
	""" Keeper of the Grove
	[Choose One -] Deal_2_damage; or [Silence] a minion. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	choose = ("VAN_EX1_166a", "VAN_EX1_166b")
	play = ChooseBoth(CONTROLLER) & (Hit(TARGET, 2), Silence(TARGET))

	pass

class VAN_EX1_166a:# <2>[1646]
	""" Moonfire
	Deal 2 damage. """
	play = Hit(TARGET, 2)
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	pass

class VAN_EX1_166b:# <2>[1646]
	""" Dispel
	[Silence] a minion. """
	play = Silence(TARGET)
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	pass

if Classic_Innervate:# 
	Classic_Druid+=['VAN_EX1_169']
class VAN_EX1_169:# <2>[1646]
	""" Innervate
	Gain 2 Mana Crystals this turn only. """
	play = ManaThisTurn(CONTROLLER, 1)
	pass

if Classic_Starfire:# 
	Classic_Druid+=['VAN_EX1_173']
class VAN_EX1_173:# <2>[1646]
	""" Starfire
	Deal $5 damage.Draw a card. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 5), Draw(CONTROLLER)
	pass

if Classic_Ancient_of_War:# 
	Classic_Druid+=['VAN_EX1_178']
	Classic_Druid+=['VAN_EX1_178a','EX1_178ae']
	Classic_Druid+=['VAN_EX1_178b','EX1_178be']
class VAN_EX1_178:# <2>[1646]
	""" Ancient of War
	[Choose One -]+5 Attack; or +5 Health and [Taunt]. """
	choose = ("VAN_EX1_178b", "VAN_EX1_178a")
	play = ChooseBoth(CONTROLLER) & (Buff(SELF, "EX1_178ae"), Buff(SELF, "EX1_178be"))
	pass

class VAN_EX1_178a:# <2>[1646]
	""" Rooted
	+5 Health and [Taunt]. """
	play = Buff(SELF, "EX1_178ae")
	pass
EX1_178ae = buff(health=5, taunt=True)

class VAN_EX1_178b:# <2>[1646]
	""" Uproot
	+5 Attack. """
	play = Buff(SELF, "EX1_178be")
	pass
EX1_178be = buff(atk=5)

if Classic_Bite:# 
	Classic_Druid+=['VAN_EX1_570','EX1_570e']
class VAN_EX1_570:# <2>[1646]
	""" Bite
	Give your hero +4_Attack this turn. Gain 4 Armor. """
	play = Buff(FRIENDLY_HERO, "EX1_570e"), GainArmor(FRIENDLY_HERO, 4)
	pass
EX1_570e = buff(atk=4)

if Classic_Force_of_Nature:# 
	Classic_Druid+=['VAN_EX1_571']
class VAN_EX1_571:# <2>[1646]
	""" Force of Nature
	Summon three 2/2 Treants with[Charge] that die at the end of the turn. """
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	play = Summon(CONTROLLER, "VAN_EX1_tk9") * 3
	pass

if Classic_Cenarius:# 
	Classic_Druid+=['VAN_EX1_573']
	Classic_Druid+=['VAN_EX1_573a','EX1_573ae']
	Classic_Druid+=['VAN_EX1_573b']
class VAN_EX1_573:# <2>[1646]
	""" Cenarius
	[Choose One -] Give your other minions +2/+2; or Summon two 2/2 Treants with [Taunt]. """
	choose = ("VAN_EX1_573a", "VAN_EX1_573b")
	play = ChooseBoth(CONTROLLER) & (
		Buff(FRIENDLY_MINIONS - SELF, "EX1_573ae"),
		Summon(CONTROLLER, "EX1_573t") * 2
	)
	pass

class VAN_EX1_573a:# <2>[1646]
	""" Demigod's Favor
	Give your other minions +2/+2. """
	play = Buff(FRIENDLY_MINIONS - SELF, "EX1_573ae")
	pass
EX1_573ae = buff(+2, +2)

class VAN_EX1_573b:# <2>[1646]
	""" Shan'do's Lesson
	Summon two 2/2 Treants with [Taunt]. """
	play = Summon(CONTROLLER, "EX1_573t") * 2
	pass

if Classic_Savagery:# 
	Classic_Druid+=['VAN_EX1_578']
class VAN_EX1_578:# <2>[1646]
	""" Savagery
	Deal damage equal to your hero's Attack to a minion. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, ATK(FRIENDLY_HERO))
	pass

if Classic_Treant:# 
	Classic_Druid+=['VAN_EX1_tk9']
class VAN_EX1_tk9:# <2>[1646]
	""" Treant
	 """
	#
	pass

if Classic_Treant:# 
	Classic_Druid+=['VAN_EX1_tk9b']
class VAN_EX1_tk9b:# <2>[1646]
	""" Treant
	[Charge]. At the end of the turn, destroy this minion. """
	events = OWN_TURN_END.on(Destroy(SELF))
	pass

if Classic_Shapeshift:# 
	Classic_Druid+=['HERO_06','VAN_HERO_06bp']
class HERO_06:
	""" Malfurion Stormrage
	"""
	pass
class VAN_HERO_06bp:# <2>[1646]
	""" Shapeshift
	[Hero Power]+1 Attack this turn.+1 Armor. """
	activate = Buff(FRIENDLY_HERO, "HERO_06bpe"), GainArmor(FRIENDLY_HERO, 1)
@custom_card
class HERO_06bpe:
	tags = {
		GameTag.CARDNAME: "Shapeshift",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.ATK: 1,
		GameTag.TAG_ONE_TURN_EFFECT: 1,}

if Classic_Dire_Shapeshift:# 
	Classic_Druid+=['VAN_HERO_06bp2']
class VAN_HERO_06bp2:# <2>[1646]
	""" Dire Shapeshift
	[Hero Power]+2 Attack this turn.+2 Armor. """
	activate = Buff(FRIENDLY_HERO, "HERO_06bp2e"), GainArmor(FRIENDLY_HERO, 2)
@custom_card
class HERO_06bp2e:
	tags = {
		GameTag.CARDNAME: "Dire Shapeshift",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.ATK: 2,
		GameTag.TAG_ONE_TURN_EFFECT: 1,}


if Classic_Starfall:# 
	Classic_Druid+=['VAN_NEW1_007']
	Classic_Druid+=['VAN_NEW1_007a']
	Classic_Druid+=['VAN_NEW1_007b']
class VAN_NEW1_007:# <2>[1646]
	""" Starfall
	[Choose One -]Deal $5 damage to a minion; or $2 damage to all enemy minions. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	choose = ("VAN_NEW1_007a", "VAN_NEW1_007b")
	play = ChooseBoth(CONTROLLER) & (Hit(TARGET, 5), Hit(ENEMY_MINIONS, 2))
	pass

class VAN_NEW1_007a:# <2>[1646]
	""" Stellar Drift
	Deal $2 damage to all enemy minions. """
	play = Hit(ENEMY_MINIONS, 2)
	pass

class VAN_NEW1_007b:# <2>[1646]
	""" Starlord
	Deal $5 damage to a minion. """
	play = Hit(TARGET, 5)
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	pass

if Classic_Ancient_of_Lore:# 
	Classic_Druid+=['VAN_NEW1_008']
	Classic_Druid+=['VAN_NEW1_008a']
	Classic_Druid+=['VAN_NEW1_008b']
class VAN_NEW1_008:# <2>[1646]
	""" Ancient of Lore
	[Choose One -] Draw 2 cards; or Restore #5 Health. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	choose = ("VAN_NEW1_008a", "VAN_NEW1_008b")
	play = ChooseBoth(CONTROLLER) & (Draw(CONTROLLER), Heal(TARGET, 5))
	pass

class VAN_NEW1_008a:# <2>[1646]
	""" Ancient Teachings
	Draw 2 cards. """
	play = Draw(CONTROLLER)
	pass

class VAN_NEW1_008b:# <2>[1646]
	""" Ancient Secrets
	Restore 5 Health. """
	play = Heal(TARGET, 5)
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	pass


