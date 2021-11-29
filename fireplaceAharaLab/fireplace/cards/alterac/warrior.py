from ..utils import *

class ALT_WAR_1:
	""" Axe Berserker (4/3/5)
	Rush. Honorable Kill: Draw a weapon. """
	honorable_kill = Give(CONTROLLER, RANDOM(FRIENDLY_DECK + WEAPON))
	pass

class ALT_WAR_2:
	""" Glory Chaser (3/4/3)
	After you play a Taunt minion, draw a card. """
	events = Play(CONTROLLER, FRIENDLY + TAUNT).on(Draw(CONTROLLER))
	pass

class ALT_WAR_3:
	""" Iceblood Garrison (2)
	At the end of your turn, deal 1 damage to all minions. Lasts 3 turns. """
	tags = {GameTag.SIDEQUEST:True, }
	events=[
		OWN_TURN_END.on(Hit(ALL_MINIONS, 1)),
		OWN_TURN_BEGIN.on(SidequestCounter(SELF, 3, [Destroy(SELF)])),
		]
	pass

class ALT_WAR_4:
	"""Shield Shatter (10) frost
	Deal 5 damage to all minions. Costs (1) less for each Armor you have. """
	cost_mod = -ARMOR(FRIENDLY_HERO)
	play = Hit(ALL_MINIONS, 5)
	pass

class ALT_WAR_5:
	""" To the Front! (2) 
	Your minions cost (2) less this turn (but not less than 1). """
	play = Buff(FRIENDLY_HAND, 'ALT_WAR_5e')
	pass
class ALT_WAR_5e:
	cost = lambda self, i: max(1,i-2)
	events = OWN_TURN_END.on(Destroy())

class ALT_WAR_6:
	""" Scrapsmith (3/2/4)
	Taunt Battlecry: Add two 2/4 Grunts with Taunt to your hand. """
	play = Give(CONTROLLER, 'ALT_WAR_6t')
	pass
class ALT_WAR_6t:
	"""   """
	pass

class ALT_WAR_7:
	""" Rokara, the Valorous (7/*/5) hero
	Battlecry: Equip a 5/2 Unstoppable Force. """
	play = (
		Summon(CONTROLLER, 'ALT_WAR_7t'),
		#ChangeHero(SELF)
		)
	pass
class ALT_WAR_7t:
	"""   """
	pass

class ALT_WAR_8_Action(TargetedAction):
	TARGET = ActionArg()
	def do (self,source, target):
		controller = target.controller
		if controller.hero.total_armor>=15:
			BuffOnce(source, 'ALT_WAR_8e').trigger(controller)
class ALT_WAR_8:##events?
	""" Captain Galvangar (6/6/6)
	Battlecry: If you have gained 15 or more Armor this game, gain +3/+3 and Charge. (#1 left!) (Ready!) """
	play = ALT_WAR_8_Action(SELF)
	pass
ALT_WAR_8e=buff(atk=3, health=3, charge=True)

class ALT_WAR_9:#
	""" rozen Buckler (2) frost
	Gain 10 Armor. At the start of your next turn, lose 5 Armor. """
	play = GainArmor(FRIENDLY_HERO,10)
	events = OWN_TURN_BEGIN.on(SidequestCounter(SELF,1,[GainArmor(ERIENDLY_HERO, -5)]))
	pass

class ALT_WAR_10:
	""" Snowed In (3) frost
	Destroy a damaged minion. Freeze all other minions. """
	play = (
		Destroy(ALL_MINIONS + DAMAGED),
		Freeze(ALL_MINIONS),
		)
	pass

