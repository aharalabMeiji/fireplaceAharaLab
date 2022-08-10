from ..utils import *
##嶋田君の仕事！！


#####################################

Core_Paladin=[]
Core_Warhorse_Trainer=True
Core_Blessing_of_Kings=True
Core_Consecration=True
Core_Truesilver_Champion=True
Core_Amber_Watcher=True
Core_Bronze_Explorer=True
Core_Noble_Sacrifice=True
Core_Argent_Protector=True
Core_Aldor_Peacekeeper=True
Core_Tirion_Fordring=True
Core_Equality=True
Core_Avenge=True
Core_Righteous_Protector=True
Core_Ragnaros_Lightlord=True
Core_Stand_Against_Darkness=True
Core_Flash_of_Light=True
Core_Reckoning=True



if Core_Warhorse_Trainer:# 
	Core_Paladin+=['CORE_AT_075']
class CORE_AT_075:# <5>[1637]#23.6 ## visually OK
	""" Warhorse Trainer
	Your Silver Hand Recruits have +1 Attack. """
	update = Refresh(FRIENDLY_MINIONS+ID('CS2_101t'),{GameTag.ATK: +1})
	pass
#class CS2_101t:
""" Silver Hand Recruit (1/1/1)"""


class CORE_CS2_088:# <5>[1637]##.22.6  ## visually OK
	""" Guardian of Kings
	[Taunt][Battlecry:] Restore #6 Health to your hero. """
	play = Heal(FRIENDLY_HERO, 6)
	pass

class CORE_CS2_089:# <5>[1637]##.22.6 ## visually OK
	""" Holy Light
	Restore #8 Health to your hero. """
	play = Heal(FRIENDLY_HERO, 8)
	pass


if Core_Blessing_of_Kings:# 
	Core_Paladin+=['CORE_CS2_092','CS2_092e']
class CORE_CS2_092:# <5>[1637]#23.6 ## visually OK
	""" Blessing of Kings
	Give a minion +4/+4. <i>(+4 Attack/+4 Health)</i> """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0,PlayReq.REQ_MINION_TARGET:0}
	play = Buff(TARGET, 'CS2_092e')
	pass
CS2_092e = buff(+4, +4)

if Core_Consecration:# 
	Core_Paladin+=['CORE_CS2_093']
class CORE_CS2_093:# <5>[1637]#23.6 ## visually OK
	""" Consecration
	Deal $2 damage to all enemies. """
	play = Hit(ENEMY_CHARACTERS, 2)
	pass

if Core_Truesilver_Champion:# 
	Core_Paladin+=['CORE_CS2_097']
class CORE_CS2_097:# <5>[1637]#23.6 ## visually OK
	""" Truesilver Champion
	Whenever your hero attacks, restore #2_Health to it. """
	events = Attack(FRIENDLY_HERO).on(Heal(FRIENDLY_HERO, 2))
	pass

if Core_Amber_Watcher:# 
	Core_Paladin+=['CORE_DRG_226']
class CORE_DRG_226:# <5>[1637]#23.6 ## visually OK
	""" Amber Watcher
	[Battlecry:] Restore #8_Health. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_HERO_OR_MINION_TARGET:0}
	play = Heal(TARGET, 8)
	pass

if Core_Bronze_Explorer:# 
	Core_Paladin+=['CORE_DRG_229']
class CORE_DRG_229:# <5>[1637]#23.6 ## visually OK
	""" Bronze Explorer
	[Lifesteal][Battlecry:] [Discover] a Dragon. """
	play = Discover(CONTROLLER, RandomDragon())	
	pass

if Core_Noble_Sacrifice:# 
	Core_Paladin+=['CORE_EX1_130','EX1_130a']
class CORE_EX1_130:# <5>[1637]#23.6 ## visually OK
	""" Noble Sacrifice
	[Secret:] When an enemy attacks, summon a 2/1 Defender as the new target. """
	secret = Attack(ENEMY_MINIONS).on(
		FULL_BOARD | (
			Reveal(SELF), 
			Retarget(Attack.ATTACKER, Summon(CONTROLLER, "EX1_130a"))
	))
	pass
class EX1_130a:
	pass

if Core_Argent_Protector:# 
	Core_Paladin+=['CORE_EX1_362']
class CORE_EX1_362:# <5>[1637]#23.6 ## visually OK
	""" Argent Protector
	[Battlecry:] Give a friendly minion [Divine Shield]. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_NONSELF_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = GiveDivineShield(TARGET)
	pass

if Core_Aldor_Peacekeeper:# 
	Core_Paladin+=['CORE_EX1_382']
class CORE_EX1_382:# <5>[1637]#23.6 ## visually OK
	""" Aldor Peacekeeper
	[Battlecry:] Change an_enemy minion's Attack to 1. """
	requirements = {
		PlayReq.REQ_ENEMY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Buff(TARGET, "EX1_382e")
class EX1_382e:
	atk = SET(1)

if Core_Tirion_Fordring:# 
	Core_Paladin+=['CORE_EX1_383','EX1_383t']
class CORE_EX1_383:# <5>[1637]#23.6 ## visually OK
	""" Tirion Fordring
	[[Divine Shield],] [Taunt] [Deathrattle:] Equip a 5/3_Ashbringer. """
	deathrattle = Summon(CONTROLLER, "EX1_383t")
	pass
class EX1_383t:
	pass

if Core_Equality:# 
	Core_Paladin+=['CORE_EX1_619']
class CORE_EX1_619:# <5>[1637]#23.6 ## visually OK
	""" Equality
	Change the Health of ALL minions to 1. """
	play = Buff(ALL_MINIONS, "EX1_619e")
class EX1_619e:
	max_health = SET(1)

if Core_Avenge:# 
	Core_Paladin+=['CORE_FP1_020']
class CORE_FP1_020:# <5>[1637]#23.6 ## visually OK
	""" Avenge
	[Secret:] When one of your minions dies, give a random friendly minion +3/+2. """
	secret = Death(FRIENDLY + MINION).on(EMPTY_BOARD | (
		Reveal(SELF), Buff(RANDOM_FRIENDLY_MINION, "FP1_020e")
	))
FP1_020e = buff(+3, +2)

if Core_Righteous_Protector:# 
	Core_Paladin+=['CORE_ICC_038']
class CORE_ICC_038:# <5>[1637]#23.6 ## visually OK
	""" Righteous Protector
	[Taunt][Divine Shield] """
	pass

if Core_Ragnaros_Lightlord:# 
	Core_Paladin+=['CORE_OG_229']
class CORE_OG_229:# <5>[1637]#23.6 ## visually OK
	""" Ragnaros, Lightlord
	At the end of your turn, restore #8 Health to a damaged friendly character. """
	events = OWN_TURN_END.on(Heal(RANDOM(FRIENDLY + DAMAGED_CHARACTERS), 8))
	pass

if Core_Stand_Against_Darkness:# 
	Core_Paladin+=['CORE_OG_273']
class CORE_OG_273:# <5>[1637]#23.6 ## visually OK
	""" Stand Against Darkness
	Summon five 1/1 Silver Hand Recruits. """
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	play = Summon(CONTROLLER, "CS2_101t") * 5

if Core_Flash_of_Light:# 
	Core_Paladin+=['CORE_TRL_307']
class CORE_TRL_307:# <5>[1637]#23.6 ## visually OK
	""" Flash of Light
	Restore #4 Health. Draw a card. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Heal(TARGET, 4), Draw(CONTROLLER)
	pass

if Core_Reckoning:# 
	Core_Paladin+=['CS3_016']
class CS3_016_Action(TargetedAction):
	ATTACKER = ActionArg()
	DEFENDER = IntArg()
	def do(self, source, attacker):
		if attacker.atk>=3:
			Destroy(attacker).trigger(source)
class CS3_016:# <5>[1637]#23.6  ########### need to check #################
	""" Reckoning
	[Secret:] After an enemy minion deals 3 or more damage, destroy it. """
	secret = Attack(ENEMY_MINIONS).on(CS3_016_Action(Attack.ATTACKER))
	pass

class CS3_029:# <5>[1637]##.22.6
	""" Pursuit of Justice
	Give +1 Attack to Silver Hand Recruits you summon this game. """
	#
	pass
class CS3_029e:# <5>[1637]#23.6
	""" Pursuit of Justice
	Your Silver Hand Recruits have +1 Attack. """
class CS3_029e2:# <5>[1637]#23.6
	""" Pursuit of Justice
	+1 Attack. """


