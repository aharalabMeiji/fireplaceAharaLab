
from ..utils import *

Stormwind_Warrior=[
'SW_027',
'SW_028','SW_028t','SW_028t2','SW_028t5','SW_028t6',
'SW_029','SW_030','SW_093','SW_093e','SW_097','SW_097t','skele21']
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

class SW_027:##OK <10>[1578]
	""" Shiver Their Timbers!
	Deal $2 damage to a minion. If you control a Pirate, deal $5 instead. """
	requirements = { PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0}
	play = Find(FRIENDLY_MINIONS + PIRATE) & Hit(TARGET, 5) | Hit(TARGET, 2)
	#
	pass

class SW_028:##OK <10>[1578]
	""" Raid the Docks
	[Questline:] Play 3 Pirates.[Reward:] Draw a weapon. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Play(CONTROLLER, PIRATE).on(
		SidequestCounter(SELF,  3, [
			Give(CONTROLLER, RANDOM(FRIENDLY_DECK + WEAPON)),
			Summon(CONTROLLER, 'SW_028t'),
			Destroy(SELF)
			])
		)
	pass

class SW_028t:##OK <10>[1578]
	""" Create a Distraction
	[Questline:] Play 3 Pirates.[Reward:] Deal $2 damage to a random enemy twice.	"""
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Play(CONTROLLER, PIRATE).on(
		SidequestCounter(SELF,  3, [## 3 = self.quest_progrss_total
			Hit(RANDOM(ENEMY_CHARACTERS), 2),
			Hit(RANDOM(ENEMY_CHARACTERS), 2),
			Summon(CONTROLLER, 'SW_028t2'),
			Destroy(SELF)
			])
		)
	pass

class SW_028t2:##OK <10>[1578]
	""" Secure the Supplies
	[Questline:] Play 2 Pirates.[Reward:] Cap'n Rokara. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Play(CONTROLLER, PIRATE).on(
		SidequestCounter(SELF,  2, [
			Give(CONTROLLER, 'SW_028t5'),
			Destroy(SELF)
			])
		)
	pass

class SW_028t5:##OK <10>[1578]
	""" Cap'n Rokara
	[Battlecry:] Summon The Juggernaut! """
	play = Summon(CONTROLLER, 'SW_028t6')
	pass

class SW_028t6:##OK <10>[1578]
	""" The Juggernaut
	[Start of Your Turn:]Summon a Pirate, equip aWarrior weapon, and fire two cannons that deal 2 damage! """
	events = OWN_TURN_BEGIN.on(
		Summon(CONTROLLER, RandomMinion(race = Race.PIRATE)),
		Summon(CONTROLLER, RandomWeapon(card_class = CardClass.WARRIOR)),
		Hit(RANDOM(ENEMY_CHARACTERS), 2) * 2
		)
	pass

class SW_029:##OK <10>[1578]
	""" Harbor Scamp
	[Battlecry:] Draw a Pirate. """
	play = Give(CONTROLLER, RandomMinion(race = Race.PIRATE))
	pass

class SW_030:##OK <10>[1578]
	""" Cargo Guard
	At the end of your turn, gain 3 Armor. """
	events = OWN_TURN_END.on(
		GainArmor(FRIENDLY_HERO, 3)
		)
	pass

class SW_093:##OK <10>[1578]
	""" Stormwind Freebooter
	[Battlecry:] Give your hero +2 Attack this turn. """
	play = Buff(FRIENDLY_HERO, 'SW_093e')
	pass
SW_093e = buff(atk=2 )# ONE_TURN_EFFECT

#class SW_094:###OK
#	"""Heavy Plate
#	Tradeable: Gain 8 Armor."""
#	play = GainArmor(FRIENDLY_HERO, 8)
#	pass

class SW_097:# <10>[1578]
	""" Remote-Controlled Golem
	After this takes damage,shuffle two Golem Parts intoyour deck. When drawn,__summon a 2/1 Mech. """
	events = Damage(SELF).on( Shuffle( CONTROLLER, 'SW_097t') * 2)
	pass

class SW_097t:# <10>[1578]
	""" Golem Parts
	[Casts When Drawn]Summon a 2/1 Damaged Golem. """
	play = Summon(CONTROLLER, 'skele21')
	pass
class skele21:
	""" Damaged Golem """
	pass
