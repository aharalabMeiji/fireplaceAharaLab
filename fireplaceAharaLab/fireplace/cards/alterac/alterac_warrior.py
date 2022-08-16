from ..utils import *

Alterac_Warrior=[]

Alterac_Shield_Shatter=True  ###
Alterac_Frozen_Buckler=True  ###
Alterac_To_the_Front=True  ###
Alterac_Captain_Galvangar=True  ###
Alterac_Rokara_the_Valorous=True  ###
Alterac_Glory_Chaser=True  ###
Alterac_Snowed_In=True  ###
Alterac_Scrapsmith=True  ###
Alterac_Axe_Berserker=True  ###
Alterac_Iceblood_Garrison=True  ###
Alterac_Hit_It_Very_Hard=True  ###
Alterac_Onyxian_Drake=True  ###
Alterac_Shoulder_Check=True  ###



if Alterac_Shield_Shatter:# 
	Alterac_Warrior+=['AV_108']
class AV_108:
	"""Shield Shatter (10) frost
	Deal 5 damage to all minions. Costs (1) less for each Armor you have. """
	cost_mod = -ARMOR(FRIENDLY_HERO)
	play = Hit(ALL_MINIONS, 5)
	pass




if Alterac_Frozen_Buckler:# 
	Alterac_Warrior+=['AV_109']
	Alterac_Warrior+=['AV_109e']
class AV_109:#
	""" Frozen Buckler (2) frost
	Gain 10 Armor. At the start of your next turn, lose 5 Armor. """
	play = GainArmor(FRIENDLY_HERO,10), Buff(CONTROLLER, 'AV_109e')
	pass
class AV_109e:
	events = OWN_TURN_BEGIN.on(GainArmor(FRIENDLY_HERO, -5), Destroy(SELF))




if Alterac_To_the_Front:# 
	Alterac_Warrior+=['AV_119']
	Alterac_Warrior+=['AV_119e']
class AV_119:
	""" To the Front! (2) 
	Your minions cost (2) less this turn (but not less than 1). """
	play = Buff(FRIENDLY_HAND, 'AV_119e')
	pass
class AV_119e:
	tags = {GameTag.COST:-2,}
	#cost = lambda self, i: max(1,i-2)
	events = OWN_TURN_END.on(Destroy(SELF))




if Alterac_Captain_Galvangar:# 
	Alterac_Warrior+=['AV_145']
	Alterac_Warrior+=['AV_145e']
class AV_145_Action(TargetedAction):
	TARGET = ActionArg()
	def do (self,source, target):
		controller = target.controller
		if controller.hero.armor>=15:
			BuffOnce(source, 'AV_145e').trigger(controller)
class AV_145:##events?
	""" Captain Galvangar (6/6/6)
	Battlecry: If you have gained 15 or more Armor this game, gain +3/+3 and Charge. (#1 left!) (Ready!) """
	play = AV_145_Action(SELF)
	pass
AV_145e=buff(atk=3, health=3, charge=True)




if Alterac_Rokara_the_Valorous:# 
	Alterac_Warrior+=['AV_202']
	Alterac_Warrior+=['AV_202p']
	Alterac_Warrior+=['AV_202t2']
class AV_202:
	""" Rokara, the Valorous (7/*/5) hero
	Battlecry: Equip a 5/2 Unstoppable Force. """
	play = (
		Summon(CONTROLLER, 'AV_202p'),
		Summon(CONTROLLER, 'AV_202t2'),
		)
	pass
class AV_202p:
	"""  Grand Slam (Hero power)"""
	pass
class AV_202t2: 
	""" The Unstoppable Force  """
	pass




if Alterac_Glory_Chaser:# 
	Alterac_Warrior+=['AV_321']
class AV_321:
	""" Glory Chaser (3/4/3)
	After you play a Taunt minion, draw a card. """
	events = Play(CONTROLLER, FRIENDLY + TAUNT).on(Draw(CONTROLLER))
	pass




if Alterac_Snowed_In:# 
	Alterac_Warrior+=['AV_322']
class AV_322:
	""" Snowed In (3) frost
	Destroy a damaged minion. Freeze all other minions. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_DAMAGED_TARGET:0 }
	play = (
		Destroy(TARGET),
		Freeze(ALL_MINIONS - SELF),
		)
	pass




if Alterac_Scrapsmith:# 
	Alterac_Warrior+=['AV_323']
	Alterac_Warrior+=['AV_323t']
class AV_323:
	""" Scrapsmith (3/2/4)
	Taunt Battlecry: Add two 2/4 Grunts with Taunt to your hand. """
	play = Give(CONTROLLER, 'AV_323t') * 2
	pass
class AV_323t:
	"""   """
	pass




if Alterac_Axe_Berserker:# 
	Alterac_Warrior+=['AV_565']
class AV_565:
	""" Axe Berserker (4/3/5)
	Rush. Honorable Kill: Draw a weapon. """
	honorable_kill = Give(CONTROLLER, RANDOM(FRIENDLY_DECK + WEAPON))
	pass




if Alterac_Iceblood_Garrison:# 
	Alterac_Warrior+=['AV_660']
class AV_660:
	""" Iceblood Garrison (2)
	At the end of your turn, deal 1 damage to all minions. Lasts 3 turns. """
	tags = {GameTag.SIDEQUEST:True, }
	events=[
		OWN_TURN_END.on(Hit(ALL_MINIONS, 1)),
		OWN_TURN_BEGIN.on(SidequestCounter(SELF, 3, [Destroy(SELF)])),
		]
	pass




if Alterac_Hit_It_Very_Hard:# 
	Alterac_Warrior+=['ONY_023']
	Alterac_Warrior+=['ONY_023e']
class ONY_023:# <10>[1626]
	""" Hit It Very Hard
	Gain +10 Attack and "Can't attack heroes" this turn. """
	play = Buff(FRIENDLY_HERO, 'ONY_023e')
	pass
ONY_023e=buff(10,0,cannot_attack_heroes = True)
""" HIT IT HARD +10 Attack this turn. """
#TAG_ONE_TURN_EFFECT
## see SCH_138e2




if Alterac_Onyxian_Drake:# 
	Alterac_Warrior+=['ONY_024']
class ONY_024:# <10>[1626]
	""" Onyxian Drake
	[Taunt] [Battlecry:] Deal damage equal to your Armor to an enemy minion. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0}
	play = Hit(TARGET, ARMOR(FRIENDLY_HERO))
	pass




if Alterac_Shoulder_Check:# 
	Alterac_Warrior+=['ONY_025']
	Alterac_Warrior+=['ONY_025e']
class ONY_025:# <10>[1626]
	""" Shoulder Check
	[Tradeable]Give a minion +2/+1 and [Rush]. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0}
	play = Buff(TARGET, 'ONY_025e')
	pass
ONY_025e=buff(2,1,rush=True)#<12>[1626]

####################################################
