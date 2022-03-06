from ..utils import *

#Alterac_Warrior=['AV_108','AV_109','AV_109e','AV_119','AV_119e','AV_145','AV_145e','AV_202','AV_202p','AV_202t2','AV_321','AV_322','AV_323','AV_323t','AV_565','AV_660',]

class AV_108:
	"""Shield Shatter (10) frost
	Deal 5 damage to all minions. Costs (1) less for each Armor you have. """
	cost_mod = -ARMOR(FRIENDLY_HERO)
	play = Hit(ALL_MINIONS, 5)
	pass

class AV_109:#
	""" Frozen Buckler (2) frost
	Gain 10 Armor. At the start of your next turn, lose 5 Armor. """
	play = GainArmor(FRIENDLY_HERO,10), Buff(CONTROLLER, 'AV_109e')
	pass
class AV_109e:
	events = OWN_TURN_BEGIN.on(GainArmor(FRIENDLY_HERO, -5), Destroy(SELF))

class AV_119:
	""" To the Front! (2) 
	Your minions cost (2) less this turn (but not less than 1). """
	play = Buff(FRIENDLY_HAND, 'AV_119e')
	pass
class AV_119e:
	cost = lambda self, i: max(1,i-2)
	events = OWN_TURN_END.on(Destroy(SELF))

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

class AV_321:
	""" Glory Chaser (3/4/3)
	After you play a Taunt minion, draw a card. """
	events = Play(CONTROLLER, FRIENDLY + TAUNT).on(Draw(CONTROLLER))
	pass

class AV_322:
	""" Snowed In (3) frost
	Destroy a damaged minion. Freeze all other minions. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_DAMAGED_TARGET:0 }
	play = (
		Destroy(TARGET),
		Freeze(ALL_MINIONS - SELF),
		)
	pass

class AV_323:
	""" Scrapsmith (3/2/4)
	Taunt Battlecry: Add two 2/4 Grunts with Taunt to your hand. """
	play = Give(CONTROLLER, 'AV_323t') * 2
	pass
class AV_323t:
	"""   """
	pass

class AV_565:
	""" Axe Berserker (4/3/5)
	Rush. Honorable Kill: Draw a weapon. """
	honorable_kill = Give(CONTROLLER, RANDOM(FRIENDLY_DECK + WEAPON))
	pass

class AV_660:
	""" Iceblood Garrison (2)
	At the end of your turn, deal 1 damage to all minions. Lasts 3 turns. """
	tags = {GameTag.SIDEQUEST:True, }
	events=[
		OWN_TURN_END.on(Hit(ALL_MINIONS, 1)),
		OWN_TURN_BEGIN.on(SidequestCounter(SELF, 3, [Destroy(SELF)])),
		]
	pass


class ONY_023:# <10>[1626]
	""" Hit It Very Hard
	Gain +10 Attack and "Can't attack heroes" this turn. """
	play = Buff(FRIENDLY_HERO, 'ONY_023e')
	pass

ONY_023e=buff(10,0,cannot_attack_heroes = True)
#class ONY_023e:# <10>[1626]
""" HIT IT HARD
+10 Attack this turn. """
#TAG_ONE_TURN_EFFECT
## see SCH_138e2
#pass

class ONY_024:# <10>[1626]
	""" Onyxian Drake
	[Taunt] [Battlecry:] Deal damage equal to your Armor to an enemy minion. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0}
	play = Hit(TARGET, ARMOR(FRIENDLY_HERO))
	pass

class ONY_025:# <10>[1626]
	""" Shoulder Check
	[Tradeable]Give a minion +2/+1 and [Rush]. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0}
	play = Buff(TARGET, 'ONY_025e')
	pass
ONY_025e=buff(2,1,rush=True)#<12>[1626]