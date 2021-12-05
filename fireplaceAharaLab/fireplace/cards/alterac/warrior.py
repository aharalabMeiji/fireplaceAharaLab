from ..utils import *

#Alterac_Warrior=['AV_108','AV_109','AV_119','AV_119e','AV_145','AV_145e','AV_202','AV_202p','AV_202t2','AV_321','AV_322','AV_323','AV_323t','AV_565','AV_660',]

class AV_108:
	"""Shield Shatter (10) frost
	Deal 5 damage to all minions. Costs (1) less for each Armor you have. """
	cost_mod = -ARMOR(FRIENDLY_HERO)
	play = Hit(ALL_MINIONS, 5)
	pass

class AV_109:#
	""" Frozen Buckler (2) frost
	Gain 10 Armor. At the start of your next turn, lose 5 Armor. """
	play = GainArmor(FRIENDLY_HERO,10)
	events = OWN_TURN_BEGIN.on(SidequestCounter(SELF,1,[GainArmor(ERIENDLY_HERO, -5)]))
	pass

class AV_119:
	""" To the Front! (2) 
	Your minions cost (2) less this turn (but not less than 1). """
	play = Buff(FRIENDLY_HAND, 'AV_119e')
	pass
class AV_119e:
	cost = lambda self, i: max(1,i-2)
	events = OWN_TURN_END.on(Destroy())

class AV_145_Action(TargetedAction):
	TARGET = ActionArg()
	def do (self,source, target):
		controller = target.controller
		if controller.hero.total_armor>=15:
			BuffOnce(source, 'ALT_WAR_8e').trigger(controller)
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
		Summon(CONTROLLER, 'AV_202t2'),
		#ChangeHero(SELF)
		)
	pass
class AV_202p:
	"""  Grand Slam """
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
	play = (
		Destroy(ALL_MINIONS + DAMAGED),
		Freeze(ALL_MINIONS),
		)
	pass

class AV_323:
	""" Scrapsmith (3/2/4)
	Taunt Battlecry: Add two 2/4 Grunts with Taunt to your hand. """
	play = Give(CONTROLLER, 'AV_323t')
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

