from ..utils import *

################################

Core_Rogue=[]
Core_Buccaneer=True
Core_Backstab=True
Core_Cold_Blood=True
Core_Deadly_Poison=True
Core_Sinister_Strike=True
Core_Assassinate=True
Core_Sprint=True
Core_Assassins_Blade=True
Core_Hench_Clan_Burglar=True ##check
Core_SI7_Agent=True
Core_Shadowstep=True
Core_Preparation=True
Core_Tess_Greymane=False#### difficult
Core_Plague_Scientist=True  ##check
Core_Swashburglar=True ##check
Core_Tomb_Pillager=True
Core_Vanessa_VanCleef=True

###############################

if Core_Buccaneer:# 
	Core_Rogue+=['CORE_AT_029','AT_029e']
class CORE_AT_029:# <7>[1637] ## 23.6 #visually OK
	""" Buccaneer
	Whenever you equip a weapon, give it +1 Attack. """
	events = Summon(FRIENDLY_WEAPON).on(Buff(Summon.TARGET, "AT_029e"))
AT_029e = buff(atk=1)

if Core_Backstab:# 
	Core_Rogue+=['CORE_CS2_072']
class CORE_CS2_072:# <7>[1637] ## 23.6 #visually OK
	""" Backstab
	Deal $2 damage to an undamaged minion. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0,
		PlayReq.REQ_UNDAMAGED_TARGET: 0}
	play = Hit(TARGET, 2)	
	pass

if Core_Cold_Blood:# 
	Core_Rogue+=['CORE_CS2_073','CS2_073e','CS2_073e2']
class CORE_CS2_073:# <7>[1637] ## 23.6 #visually OK
	""" Cold Blood
	Give a minion +2 Attack. [Combo:] +4 Attack instead. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "CS2_073e")
	combo = Buff(TARGET, "CS2_073e2")
	pass
CS2_073e = buff(atk=2)
CS2_073e2 = buff(atk=4)


if Core_Deadly_Poison:# 
	Core_Rogue+=['CORE_CS2_074','CS2_074e']
class CORE_CS2_074:# <7>[1637] ## 23.6 #visually OK
	""" Deadly Poison
	Give your weapon +2_Attack. """
	requirements = {PlayReq.REQ_WEAPON_EQUIPPED: 0}
	play = Buff(FRIENDLY_WEAPON, "CS2_074e")
	pass
CS2_074e = buff(atk=2)


if Core_Sinister_Strike:# 
	Core_Rogue+=['CORE_CS2_075']
class CORE_CS2_075:# <7>[1637] ## 23.6 #visually OK
	""" Sinister Strike
	Deal $3 damage to the_enemy hero. """
	play = Hit(ENEMY_HERO, 3)
	pass

if Core_Assassinate:# 
	Core_Rogue+=['CORE_CS2_076']
class CORE_CS2_076:# <7>[1637] ## 23.6 #visually OK
	""" Assassinate
	Destroy an enemy minion. """
	requirements = {
		PlayReq.REQ_ENEMY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Destroy(TARGET)	
	pass

if Core_Sprint:# 
	Core_Rogue+=['CORE_CS2_077']
class CORE_CS2_077:# <7>[1637] ## 23.6 #visually OK
	""" Sprint
	Draw 4 cards. """
	play = Draw(CONTROLLER) * 4	
	pass

if Core_Assassins_Blade:# 
	Core_Rogue+=['CORE_CS2_080']
class CORE_CS2_080:# <7>[1637] ## 23.6 #visually OK
	""" Assassin's Blade
	 """
	#vanilla
	pass

if Core_Hench_Clan_Burglar:# 
	Core_Rogue+=['CORE_DAL_416']
class CORE_DAL_416_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = target
		cc = controller.hero.card_class
		ccs=[2,3,4,5,6,7,8,9,10,14]
		ccs.remove(cc)
		cc = random.choice(ccs)
		Discover(controller , RandomSpell(card_class=cc)).trigger(source)
class CORE_DAL_416:# <7>[1637] ## 23.6 #################################### need check ######
	""" Hench-Clan Burglar
	[Battlecry:] [Discover] a spell from another class. """
	play = CORE_DAL_416_Action(CONTROLLER)
	#play = Discover(CONTROLLER, RAndomSpell(card_class = RANDOM_NON_FRIENDLY_CLASS))
	pass

if Core_SI7_Agent:# 
	Core_Rogue+=['CORE_EX1_134']
class CORE_EX1_134:# <7>[1637] ## 23.6 #visually OK
	""" SI:7 Agent
	[Combo:] Deal 2 damage. """
	requirements = {PlayReq.REQ_TARGET_FOR_COMBO: 0, PlayReq.REQ_MINION_TARGET:0}
	combo = Hit(TARGET, 2)	
	pass

if Core_Shadowstep:# 
	Core_Rogue+=['CORE_EX1_144']
class CORE_EX1_144:# <7>[1637] ## 23.6 #visually OK
	""" Shadowstep
	Return a friendly minion to your hand. It_costs (2) less. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Bounce(TARGET), Buff(TARGET, "EX1_144e")
@custom_card
class EX1_144e:
	tags = {
		GameTag.CARDNAME: "Shadowstep Buff",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.COST: -2,
	}
	events = REMOVED_IN_PLAY

if Core_Preparation:# 
	Core_Rogue+=['CORE_EX1_145','EX1_145e','EX1_145o']
class CORE_EX1_145:# <7>[1637] ## 23.6 #visually OK
	""" Preparation
	The next spell you cast this turn costs (2) less. """
	play = Buff(FRIENDLY_HAND + SPELL, 'EX1_145e')
	pass
class EX1_145e:
	cost = lambda self, i : max(i-2,0)
	events =[
		OWN_SPELL_PLAY.on(Destroy(SELF)),
		OWN_TURN_END.on(Destroy(SELF))
		]
	pass
EX1_145o=buff(cost=-2)#ONE_TURN_EFFECT


if Core_Tess_Greymane:# 
	Core_Rogue+=['CORE_GIL_598']
class CORE_GIL_598:# <7>[1637] ## 23.6 ####################### difficult
	""" Tess Greymane
	[Battlecry:] Replay every card from another class you've played this game <i>(targets chosen randomly)</i>. """
	#
	pass

if Core_Plague_Scientist:# 
	Core_Rogue+=['CORE_ICC_809','ICC_809e']
class CORE_ICC_809:# <7>[1637] ## 23.6 #visually OK, need check 
	""" Plague Scientist
	[Combo:] Give a friendly minion [Poisonous]. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_FOR_COMBO: 0}
	combo = Buff(TARGET, 'ICC_809e')
	pass
ICC_809e=buff(poisonous=True)


if Core_Swashburglar:# 
	Core_Rogue+=['CORE_KAR_069']
class CORE_KAR_069:# <7>[1637] ## 23.6 #################### not correct
	""" Swashburglar
	[Battlecry:] Add a random card from another class to_your hand. """
	play = Give(CONTROLLER, RandomCollectible(card_class=ENEMY_CLASS))
	#play = Give(CONTROLLER, RandomCollectible(card_class=RANDOM_NON_FRIENDLY_CLASS))
	pass

if Core_Tomb_Pillager:# 
	Core_Rogue+=['CORE_LOE_012']
class CORE_LOE_012:# <7>[1637] ## 23.6 #visually OK
	""" Tomb Pillager
	[Deathrattle:] Add a Coin to your hand. """
	deathrattle = Give(CONTROLLER, "GAME_005")
	pass

class CORE_OG_070:# <7>[1637] ##22.6
	""" Bladed Cultist
	[Combo:] Gain +1/+1. """
	combo = Buff(SELF, "OG_070e")
OG_070e = buff(+1, +1)

if Core_Vanessa_VanCleef:# 
	Core_Rogue+=['CS3_005']
class CS3_005Action(TargetedAction):
	""" Vanessa VanCleef
	[Combo:] Add a copy of the last card your opponent played to your hand. """
	TARGET=ActionArg()
	def do(self,source,target):
		controller = target
		opponent = controller.opponent
		opponent_play = opponent.play_log
		if len(opponent_play)>0:
			last_card_id=opponent_play[-1].id
			Give(controller,last_card_id).trigger(source)
		pass
class CS3_005:# <7>[1637] ## 23.6 #visually OK
	""" Vanessa VanCleef
	[Combo:] Add a copy of the last card your opponent played to your hand. """
	combo = CS3_005Action(CONTROLLER)
	pass

