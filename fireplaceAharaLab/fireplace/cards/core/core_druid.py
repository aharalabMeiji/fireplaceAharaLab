from ..utils import *


Core_Druid=[]

Living_Roots=True#23.6
Landscaping=False#22.6
Mark_of_the_Wild=True#22.6#23.6
Wild_Growth=True#22.6#23.6
Wrath=True#23.6
Soul_of_the_Forest=True#22.6#23.6
Power_of_the_Wild=True#22.6#23.6
Nourish=True#22.6#23.6
Druid_of_the_Claw=True#22.6#23.6
Innervate=True#22.6#23.6
Ancient_of_War=False#22.6
Force_of_Nature=True#22.6#23.6
Cenarius=True#22.6#23.6
Menagerie_Warden=False#22.6
Enchanted_Raven=False#22.6
Mounted_Raptor=True#23.6
Ancient_of_Lore=True#23.6
Fandral_Staghelm=True#23.6
Feral_Rage=True#22.6#23.6
Pounce=True#22.6#23.6
Earthen_Scales=True#23.6
Nordrassil_Druid=True#22.6#23.6


if Living_Roots:# 
	Core_Druid+=['CORE_AT_037','AT_037a','AT_037b','AT_037t']
class CORE_AT_037:# <2>[1637]##########################
	""" Living Roots
	[Choose One -] Deal $2 damage; or Summon two 1/1 Saplings. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	choose = ("AT_037a", "AT_037b")
	play = ChooseBoth(CONTROLLER) & (Hit(TARGET, 2), Summon(CONTROLLER, "AT_037t") * 2)
class AT_037a:
	play = Hit(TARGET, 2)
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
class AT_037b:
	play = Summon(CONTROLLER, "AT_037t") * 2

if Landscaping:#22.6
	Core_Druid+=['CORE_BOT_420',]
class CORE_BOT_420:###OK <2>[1637]
	""" Landscaping
	Summon two 2/2 Treants. """
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 2}
	play = Summon(CONTROLLER,'EX1_158t') * 2
	pass

if Mark_of_the_Wild:# #22.6#23.6
	Core_Druid+=['CORE_CS2_009','CS2_009e',]
class CORE_CS2_009:# <2>[1637]
	""" Mark of the Wild
	Give a minion [Taunt] and +2/+3.<i>(+2 Attack/+3 Health)</i> """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "CS2_009e")
	pass
CS2_009e=buff(atk=2,health=3,taunt=True)

if Wild_Growth:# #22.6#23.6
	Core_Druid+=['CORE_CS2_013','CS2_013t',]
class CORE_CS2_013:# <2>[1637]
	""" Wild Growth
	Gain an empty Mana Crystal. """
	play = GainEmptyMana(CONTROLLER, 1)
	pass
class CS2_013t:##???
	play = Draw(CONTROLLER)

if Wrath:# #23.6
	Core_Druid+=['CORE_EX1_154','EX1_154a','EX1_154b']
class CORE_EX1_154:# <2>[1637]##################
	""" Wrath
	[Choose One -]Deal $3 damage to a minion; or $1 damageand draw a card. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	choose = ("EX1_154a", "EX1_154b")
	play = ChooseBoth(CONTROLLER) & (Hit(TARGET, 3), Hit(TARGET, 1), Draw(CONTROLLER))
class EX1_154a:
	"""Wrath (3 Damage)"""
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 3)
class EX1_154b:
	"""Wrath (1 Damage)"""
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 1), Draw(CONTROLLER)



if Soul_of_the_Forest:# #22.6#23.6
	Core_Druid+=['CORE_EX1_158','EX1_158e','EX1_158t',]
class CORE_EX1_158:# <2>[1637]
	""" Soul of the Forest
	Give your minions "[Deathrattle:] Summon a 2/2 Treant." """
	play = Buff(FRIENDLY_MINIONS, "EX1_158e")
	pass
class EX1_158e:
	deathrattle = Summon(CONTROLLER, "EX1_158t")
	tags = {GameTag.DEATHRATTLE: True}
	pass
class EX1_158t:
	pass

if Power_of_the_Wild:##22.6#23.6 
	Core_Druid+=['CORE_EX1_160','EX1_160a','EX1_160b','EX1_160be','EX1_160t',]
class CORE_EX1_160:# <2>[1637]
	""" Power of the Wild
	[Choose One -] Give your minions +1/+1; or Summon a 3/2 Panther. """
	choose = ("EX1_160b", "EX1_160a")
	play = ChooseBoth(CONTROLLER) & (
		Buff(FRIENDLY_MINIONS, "EX1_160be"), Summon(CONTROLLER, "EX1_160t")
	)
class EX1_160a:
	play = Summon(CONTROLLER, "EX1_160t")
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
class EX1_160b:
	play = Buff(FRIENDLY_MINIONS, "EX1_160be")
EX1_160be = buff(+1, +1)
class EX1_160t:
	""" Panther
	""" 
	pass

if Nourish:##22.6#23.6 
	Core_Druid+=['CORE_EX1_164','EX1_164a','EX1_164b',]
class CORE_EX1_164:# <2>[1637]Spell
	""" Nourish
	[Choose One -] Gain 2_Mana Crystals; or Draw 3 cards. """
	choose = ("EX1_164a", "EX1_164b")
	play = ChooseBoth(CONTROLLER) & (GainMana(CONTROLLER, 2), Draw(CONTROLLER), Draw(CONTROLLER), Draw(CONTROLLER))
class EX1_164a:##spell
	play = GainMana(CONTROLLER, 2)
class EX1_164b:##spell
	play = Draw(CONTROLLER) * 3

if Druid_of_the_Claw:# #22.6#23.6
	Core_Druid+=['CORE_EX1_165','EX1_165a','EX1_165b','EX1_165t1','EX1_165t2','OG_044a']
class CORE_EX1_165:# <2>[1637]Minion
	""" Druid of the Claw
	[Choose One -] Transform into a 5/4 with [Rush];or a 5/6 with [Taunt]. """
	choose = ("EX1_165a", "EX1_165b")
	play = ChooseBoth(CONTROLLER) & (Morph(SELF, "OG_044a"))
class EX1_165a:##minion
	play = Morph(SELF, "EX1_165t1")
class EX1_165b:##minion
	play = Morph(SELF, "EX1_165t2")
class EX1_165t1:##minion rush
	pass
class EX1_165t2:##minion taunt
	pass
class OG_044a:## minion rush and taunt
	pass

if Innervate:##22.6#23.6 
	Core_Druid+=['CORE_EX1_169',]
class CORE_EX1_169:# <2>[1637]
	""" Innervate
	Gain 1 Mana Crystal this turn only. """
	play = ManaThisTurn(CONTROLLER, 1)
	pass

if Ancient_of_War:##22.6 
	Core_Druid+=['CORE_EX1_178','EX1_178a','EX1_178ae','EX1_178b','EX1_178be',]
class CORE_EX1_178:#OK <2>[1637]
	""" Ancient of War
	[Choose One -]+5 Attack; or +5 Health and [Taunt]. """
	choose = ("EX1_178b", "EX1_178a")
	play = ChooseBoth(SELF) & (Buff(SELF, "EX1_178ae"), Buff(SELF, "EX1_178be"))
class EX1_178a:
	""" Rooted
	+5 Health and &lt;b&gt;Taunt&lt;/b&gt;."""
	play = Buff(SELF, "EX1_178ae")
EX1_178ae = buff(health=5, taunt=True)
class EX1_178b:
	play = Buff(SELF, "EX1_178be")
EX1_178be = buff(atk=5)

if Force_of_Nature:##22.6#23.6 
	Core_Druid+=['CORE_EX1_571','EX1_158t',]
class CORE_EX1_571:# <2>[1637]
	""" Force of Nature
	Summon three 2/2 Treants. """
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 3}
	play = Summon(CONTROLLER, "EX1_158t") * 3
	pass
class EX1_tk9:
	pass

if Cenarius:##22.6#23.6 
	Core_Druid+=['CORE_EX1_573','EX1_573a','EX1_573ae','EX1_573b','EX1_573t',]
class CORE_EX1_573:# <2>[1637]
	""" Cenarius
	[Choose One -] Give your other minions +2/+2; or Summon two 2/2 Treants with [Taunt]. """
	choose = ("EX1_573a", "EX1_573b")
	play = ChooseBoth(CONTROLLER) & (
		Buff(FRIENDLY_MINIONS - SELF, "EX1_573ae"),
		Summon(CONTROLLER, "EX1_573t") * 2
	)
class EX1_573a:
	play = Buff(FRIENDLY_MINIONS - SELF, "EX1_573ae")
EX1_573ae = buff(+2, +2)
class EX1_573b:
	play = Summon(CONTROLLER, "EX1_573t") * 2
class EX1_573t:
	pass

if Menagerie_Warden:#22.6
	Core_Druid+=['CORE_KAR_065',]
class CORE_KAR_065:#OK <2>[1637]
	""" Menagerie Warden
	[Battlecry:] Choose a friendly Beast. Summon a_copy of it. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0,
		PlayReq.REQ_TARGET_WITH_RACE: 20}
	powered_up = Find(FRIENDLY_MINIONS + BEAST)
	play = Summon(CONTROLLER, ExactCopy(TARGET))
	pass

if Enchanted_Raven:#22.6
	Core_Druid+=['CORE_KAR_300',]
class CORE_KAR_300:# <2>[1637]
	""" Enchanted Raven
	 """
	#
	pass

if Mounted_Raptor:# #23.6
	Core_Druid+=['CORE_LOE_050']
class CORE_LOE_050:# <2>[1637]############################
	""" Mounted Raptor
	[Deathrattle:] Summon a random 1-Cost minion. """
	deathrattle = Summon(CONTROLLER, RandomMinion(cost=1))
	pass

if Ancient_of_Lore:##23.6 
	Core_Druid+=['CORE_NEW1_008','NEW1_008a','NEW1_008b']
class CORE_NEW1_008:# <2>[1637##############################
	""" Ancient of Lore
	[Choose One -] Draw 2 cards; or Restore #5 Health. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	choose = ("NEW1_008a", "NEW1_008b")
	play = ChooseBoth(CONTROLLER) & (Draw(CONTROLLER), Draw(CONTROLLER), Heal(TARGET, 5))
class NEW1_008a:
	play = Draw(CONTROLLER)*2
class NEW1_008b:
	play = Heal(TARGET, 5)
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}

if Fandral_Staghelm:##23.6 
	Core_Druid+=['CORE_OG_044']#,'OG_044a','OG_044b','OG_044c','OG_044e'
class CORE_OG_044:# <2>[1637]############################
	""" Fandral Staghelm
	Your [Choose One] cards and powers have both effects combined. """
	update = Refresh(CONTROLLER, {GameTag.CHOOSE_BOTH: True,})
	pass
## we may use OG_044e as a buff card.

if Feral_Rage:# #22.6#23.6
	Core_Druid+=['CORE_OG_047','OG_047a','OG_047b','OG_047e',]
class CORE_OG_047:# <2>[1637]
	""" Feral Rage
	[Choose One -] Give your hero +4 Attack this turn; or Gain 8 Armor. """
	choose = ("OG_047a", "OG_047b")
	play = ChooseBoth(CONTROLLER) & (
		Buff(FRIENDLY_HERO, "OG_047e"),
		GainArmor(FRIENDLY_HERO, 8)
	)
class OG_047a:
	play = Buff(FRIENDLY_HERO, "OG_047e")
OG_047e = buff(atk=4)
class OG_047b:
	play = GainArmor(FRIENDLY_HERO, 8)

if Pounce:# #22.6#23.6
	Core_Druid+=['CORE_TRL_243','TRL_243e',]
class CORE_TRL_243:# <2>[1637]
	""" Pounce
	Give your hero +2_Attack this turn. """
	play=Buff(FRIENDLY_HERO,'TRL_243e')
	pass
TRL_243e=buff(atk=2)# ONE_TURN_EFFECT


if Earthen_Scales:##23.6 
	Core_Druid+=['CORE_UNG_108','UNG_108e']
class CORE_UNG_108:# <2>[1637]#########################
	""" Earthen Scales
	Give a friendly minion +1/+1, then gain Armor equal to its Attack. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET,'UNG_108e'), GainArmor(FRIENDLY_HERO, ATK(TARGET))
	pass
UNG_108e=buff(1,1)

if Nordrassil_Druid:#22.6#23.6
	Core_Druid+=['CS3_012','CS3_012e', ]
class CS3_012:#OK <2>[1637]
	""" Nordrassil Druid
	[Battlecry:] The next spell you cast this turn costs_(3)_less. """
	play = Buff(FRIENDLY_HAND + SPELL,'CS3_012e')
	pass
class CS3_012e:# <2>[1637]
	""" Nature's Rite
	Your next spell this turn costs (3) less. """
	cost = lambda self, i: max(i-3,0)
	events =[
	   OWN_SPELL_PLAY.on(Destroy(SELF)),
	   OWN_TURN_END.on(Destroy(SELF)),
	   ]
	pass





















