
from ..utils import *

Stormwind_Warrior=[
'SW_027',
'SW_028','SW_028t','SW_028t2','SW_028t5','SW_028t6',
'SW_029','SW_030','SW_093','SW_097','SW_097t',]
#'SW_021','SW_023','SW_024','SW_094',

#class SW_021:###OK bigWarrior
#	"""Cowardly Grunt
#	Deathrattle: Summon a minion from your deck."""
#	# CardDefsにdeathrattleタグがついていない
#	play = SetTag(SELF, (GameTag.DEATHRATTLE, ))
#	deathrattle = Summon(CONTROLLER, RANDOM(FRIENDLY_DECK+MINION))
#	pass

#class SW_023:###OK bigWarrior
#	"""Provoke
#	Tradeable: Choose a friendly minion. Enemy minions attack it."""
#	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_MINIMUM_ENEMY_MINIONS: 1,
#					PlayReq.REQ_TARGET_TO_PLAY: 0, PlayReq.REQ_FRIENDLY_TARGET: 0}
#	def play(self):
#		for target in self.targets:
#			for minion in self.controller.opponent.field:
#				Attack(minion,target).trigger(self.controller)
#	pass

#class SW_024_Action(TargetedAction):
#	TARGET = ActionArg()# 
#	def do(self, source, target):
#		controller = source.controller
#		enemy = controller.opponent
#		if len(enemy.field)==0:
#			return
#		deffender = random.choice(enemy.field)
#		Attack(source, deffender).trigger(controller)
#		if deffender.health <= 0:
#			Buff(source, 'SW_024e').trigger(controller)
#		pass

#class SW_024:###OK  bigWarrior
#	"""Lothar
#	At the end of your turn, attack a random enemy minion. If it dies, gain +3/+3."""
#	events = OWN_TURN_END.on(SW_024_Action(SELF))
#	#Attackは使い方が難しい。BAR_844のように、事象発生の条件として使われるほうがふつうなので。
#	#events = OWN_TURN_END.on(Attack(SELF, RANDOM_ENEMY_MINION).then(
#	#	Dead(Attack.DEFENDER) & Buff(SELF, "SW_024e")))
#	pass
#SW_024e = buff(atk=3, health=3)

class SW_027:# <10>[1578]
	""" Shiver Their Timbers!
	Deal $2 damage to a minion. If you control a Pirate, deal $5 instead. """
	#
	pass

class SW_028:# <10>[1578]
	""" Raid the Docks
	[Questline:] Play 3 Pirates.[Reward:] Draw a weapon. """
	#
	pass

class SW_028t:# <10>[1578]
	""" Create a Distraction
	[Questline:] Play 2 Pirates.[Reward:] Deal $2 damageto a random enemy twice. """
	#
	pass

class SW_028t2:# <10>[1578]
	""" Secure the Supplies
	[Questline:] Play 2 Pirates.[Reward:] Cap'n Rokara. """
	#
	pass

class SW_028t5:# <10>[1578]
	""" Cap'n Rokara
	[Battlecry:] Summon The Juggernaut! """
	#
	pass

class SW_028t6:# <10>[1578]
	""" The Juggernaut
	[Start of Your Turn:]Summon a Pirate, equip aWarrior weapon, and fire two cannons that deal 2 damage! """
	#
	pass

class SW_029:# <10>[1578]
	""" Harbor Scamp
	[Battlecry:] Draw a Pirate. """
	#
	pass

class SW_030:# <10>[1578]
	""" Cargo Guard
	At the end of your turn, gain 3 Armor. """
	#
	pass

class SW_093:# <10>[1578]
	""" Stormwind Freebooter
	[Battlecry:] Give your hero +2 Attack this turn. """
	#
	pass

#class SW_094:###OK
#	"""Heavy Plate
#	Tradeable: Gain 8 Armor."""
#	play = GainArmor(FRIENDLY_HERO, 8)
#	pass

class SW_097:# <10>[1578]
	""" Remote-Controlled Golem
	After this takes damage,shuffle two Golem Parts intoyour deck. When drawn,__summon a 2/1 Mech. """
	#
	pass

class SW_097t:# <10>[1578]
	""" Golem Parts
	[Casts When Drawn]Summon a 2/1 Damaged Golem. """
	#
	pass

