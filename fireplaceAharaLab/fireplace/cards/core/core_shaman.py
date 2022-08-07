from ..utils import *


Core_Shaman=[]
##23.6
Menacing_Nimbus=True
Windfury=True
Fire_Elemental=True
Rockbiter_Weapon=True
Bloodlust=True
Far_Sight=True
Lightning_Bolt=True
Hex=True
Feral_Spirit=True
Lightning_Storm=True
Flametongue_Totem=True
Doomhammer=True
Mana_Tide_Totem=True
Maelstrom_Portal=True
AlAkir_the_Windlord=True
Kragwa,_the_Frog=True
Tidal_Surge=True
Novice_Zapper=True


class CORE_AT_047:# <8>[1637]## 22.6
	""" Draenei Totemcarver
	[Battlecry:] Gain +1/+1 for each friendly Totem. """
	play = Buff(SELF, "AT_047e") * Count(FRIENDLY_MINIONS + TOTEM)
	pass
AT_047e = buff(+1, +1)


class CORE_AT_075:# <5>[1637]## 22.6
	""" Warhorse Trainer
	Your Silver Hand Recruits have +1 Attack. """
	update = Refresh(FRIENDLY + ID("CS2_101t"), buff="AT_075e")	
	pass
AT_075e = buff(atk=1)


if Menacing_Nimbus:# ##23.6
	Core_Shaman+=['CORE_BOT_533']
class CORE_BOT_533:# <8>[1637]##23.6
	""" Menacing Nimbus
	[Battlecry:] Add a random Elemental to your hand. """
	play = Give(CONTROLLER, RandomCard(race=Race.ELEMENTAL))
	pass


class CORE_CS2_039:# <8>[1637]## 22.6
	""" Windfury
	Give a minion [Windfury]. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = GiveWindfury(TARGET - WINDFURY)
	pass

if Windfury:# 
	Core_Shaman+=['CORE_CS2_039e']
class CORE_CS2_039e:# <8>[1637]##23.6
	""" Windfury
	[Windfury]. """
	#
	pass

if Fire_Elemental:# 
	Core_Shaman+=['CORE_CS2_042']
class CORE_CS2_042:# <8>[1637]##23.6
	""" Fire Elemental
	[Battlecry:] Deal 4 damage. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Hit(TARGET, 4)	
	pass

if Rockbiter_Weapon:# 
	Core_Shaman+=['CORE_CS2_045']
class CORE_CS2_045:# <8>[1637]##23.6
	""" Rockbiter Weapon
	Give a friendly character +3 Attack this turn. """
	requirements = {PlayReq.REQ_FRIENDLY_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "CS2_045e")
	pass
CS2_045e = buff(atk=3)## ONE_TURN_EFFECT

if Bloodlust:# 
	Core_Shaman+=['CORE_CS2_046']
class CORE_CS2_046:# <8>[1637]##23.6
	""" Bloodlust
	Give your minions +3_Attack this turn. """
	#
	pass

if Far_Sight:# 
	Core_Shaman+=['CORE_CS2_053']
class CORE_CS2_053:# <8>[1637]##23.6
	""" Far Sight
	Draw a card. That card costs (3) less. """
	#
	pass

if Lightning_Bolt:# 
	Core_Shaman+=['CORE_EX1_238']
class CORE_EX1_238:# <8>[1637]##23.6
	""" Lightning Bolt
	Deal $3 damage. [Overload:] (1) """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 3)	
	pass

if Hex:# 
	Core_Shaman+=['CORE_EX1_246']
class CORE_EX1_246:# <8>[1637]##23.6
	""" Hex
	Transform a minion into a 0/1 Frog with [Taunt]. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Morph(TARGET, "hexfrog")
	pass
#EX1_246e#Morphed buff?
class hexfrog:
	""" Frog
	[Taunt] """

if Feral_Spirit:# 
	Core_Shaman+=['CORE_EX1_248']
class CORE_EX1_248:# <8>[1637]##23.6
	""" Feral Spirit
	Summon two 2/3 Spirit Wolves with [Taunt]. [Overload:] (1) """
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	play = Summon(CONTROLLER, "EX1_tk11") * 2
	pass
class EX1_tk11:
	""" Spirit Wolf
	<b>Taunt</b> """
	pass

class CORE_EX1_250:# <8>[1637]## 22.6
	""" Earth Elemental
	[Taunt][[Overload]:] (2) """
	#
	pass

if Lightning_Storm:# 
	Core_Shaman+=['CORE_EX1_259']
class CORE_EX1_259:# <8>[1637]##23.6
	""" Lightning Storm
	Deal $3 damage to all_enemy minions. [Overload:] (2) """
	#
	pass

class CORE_EX1_258:# <8>[1637]## 22.6
	""" Unbound Elemental
	After you play a card_with [Overload], gain_+1/+1. """
	events = Play(CONTROLLER, OVERLOAD).on(Buff(SELF, "EX1_258e"))
	pass
EX1_258e = buff(+1, +1)

class CORE_EX1_259:# <8>[1637]## 22.6
	""" Lightning Storm
	Deal $3 damage to all_enemy minions. [Overload:] (2) """
	play = Hit(ENEMY_MINIONS, 3)
	pass


if Flametongue_Totem:# 
	Core_Shaman+=['CORE_EX1_565']
class CORE_EX1_565:# <8>[1637]##23.6
	""" Flametongue Totem
	Adjacent minions have +2_Attack. """
	#
	pass

if Doomhammer:# 
	Core_Shaman+=['CORE_EX1_567']
class CORE_EX1_567:# <8>[1637]##23.6
	""" Doomhammer
	[Windfury, Overload:] (2) """
	#
	pass

if Mana_Tide_Totem:# 
	Core_Shaman+=['CORE_EX1_575']
class CORE_EX1_575:# <8>[1637]##23.6
	""" Mana Tide Totem
	At the end of your turn, draw a card. """
	events = OWN_TURN_END.on(Draw(CONTROLLER))
	pass

if Maelstrom_Portal:# 
	Core_Shaman+=['CORE_KAR_073']
class CORE_KAR_073:# <8>[1637]##23.6
	""" Maelstrom Portal
	Deal_$1_damage to_all_enemy_minions. Summon_a_random1-Cost minion. """
	#
	pass




if AlAkir_the_Windlord:# 
	Core_Shaman+=['CORE_NEW1_010']
class CORE_NEW1_010:# <8>[1637]##23.6
	""" Al'Akir the Windlord
	[Charge, Divine Shield, Taunt, Windfury] """
	#
	pass

if Kragwa,_the_Frog:# 
	Core_Shaman+=['CORE_TRL_345']
class CORE_TRL_345:# <8>[1637]##23.6
	""" Krag'wa, the Frog
	[Battlecry:] Return all spells you played last turn to_your hand. """
	#
	pass

if Tidal_Surge:# 
	Core_Shaman+=['CORE_UNG_817']
class CORE_UNG_817:# <8>[1637]##23.6
	""" Tidal Surge
	[Lifesteal]Deal $4 damage to a_minion. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 4)
	pass

if Novice_Zapper:# 
	Core_Shaman+=['CS3_007']
class CS3_007:# <8>[1637]##23.6
	""" Novice Zapper
	[Spell Damage +1] [Overload:] (1) """
	#
	pass

class CS3_016:# <5>[1637]## 22.6
	""" Reckoning
	[Secret:] After an enemy minion deals 3 or more damage, destroy it. """
	secret = Attack(ENEMY_MINIONS, FRIENDLY_CHARACTERS).after(
		Reveal(SELF),
		Destroy(Attack.ATTACKER)
		)
	pass

