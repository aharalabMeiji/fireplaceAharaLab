
from ..utils import *

Darkmoon_Warrior=['DMF_521','DMF_521t','DMF_522',
'DMF_523','DMF_524','DMF_524e','DMF_525',
'DMF_526','DMF_526a','DMF_526e','DMF_528',
'DMF_529','DMF_530','DMF_530e','DMF_531','DMF_531e',
'YOP_013','YOP_013e','YOP_014','YOP_014e',]


class DMF_521:#OK <10>[1466]
	""" Sword Eater
	[Taunt][Battlecry:] Equip a 3/2_Sword. """
	play = Summon(CONTROLLER, 'DMF_521t')
	pass

class DMF_521t:# <10>[1466]
	""" Jawbreaker
	 """
	#
	pass

#class DMF_522:###OK   bigWarrior
#	"""Minefield
#	Deal 5 damage randomly split among all minions."""
#	play = Hit(RANDOM_MINION, 1) * 5
#	pass

class DMF_523:#OK <10>[1466]
	""" Bumper Car
	[Rush][Deathrattle:] Add two 1/1 Riders with [Rush] to_your hand. """
	deathrattle = Give(CONTROLLER, 'DMF_523t') * 2
	pass
class DMF_523t:
	""" Darkmoon Rider """
	pass

class DMF_524:#OK <10>[1466]
	""" Ringmaster's Baton
	After your hero attacks, give a Mech, Dragon, and Pirate in your hand +1/+1. """
	events = Attack(FRIENDLY_HERO).on(
		Buff(RANDOM(FRIENDLY_HAND + MECH), 'DMF_524e'),
		Buff(RANDOM(FRIENDLY_HAND + DRAGON), 'DMF_524e'),
		Buff(RANDOM(FRIENDLY_HAND + PIRATE), 'DMF_524e'),
		)
	pass

DMF_524e=buff(1,1)# <10>[1466]
#	""" Big-Top Special
#	+1/+1. """

class DMF_525:#OK <10>[1466]
	""" Ringmaster Whatley
	[Battlecry:] Draw a Mech, Dragon, and Pirate. """
	play = (
		Give(CONTROLLER, RANDOM(FRIENDLY_DECK + MECH)),
		Give(CONTROLLER, RANDOM(FRIENDLY_DECK + DRAGON)),
		Give(CONTROLLER, RANDOM(FRIENDLY_DECK + PIRATE)),
		)
	pass

class DMF_526:#OK <10>[1466]
	""" Stage Dive
	Draw a [Rush] minion. [Corrupt:] Give it +2/+1. """
	play = Give(CONTROLLER, RANDOM(FRIENDLY_DECK + RUSH))
	pass

class DMF_526a:#OK <10>[1466]
	""" Stage Dive
	[Corrupted]Draw a [Rush] minion and give it +2/+1. """
	play = Give(CONTROLLER, RANDOM(FRIENDLY_DECK + RUSH)).then(Buff(Give.CARD,'DMF_526e'))
	pass
DMF_526e=buff(2,1)# <10>[1466]
#	""" Bweeeoooow!
#	+2/+1. """

class DMF_528_Action(TargetedAction):
	TARGET = ActionArg()#controller
	def do(self, source, target) -> int:
		controller = target
		new_cost = source.data.tags.get(GameTag.COST)
		races = [Race.BEAST, Race.DEMON, Race.DRAGON,Race.MECHANICAL,\
		   Race.MURLOC,Race.PIRATE,Race.TOTEM,Race.ELEMENTAL,Race.QUILBOAR]
		for race in races:
			for card in controller.field:
				if card.race == race:
					new_cost -=1
					log.info("%s reduces cost of %s to %d"%(card, source, new_cost))
					break
		source.cost = new_cost
	pass
class DMF_528:#OK <10>[1466]
	""" Tent Trasher
	[[Rush].] Costs (1) less for each friendly minion with a unique minion type. """
	class Hand:
		update = DMF_528_Action(CONTROLLER) 
	pass

class DMF_529:#OK <10>[1466]
	""" E.T.C., God of Metal
	After a friendly [Rush] minion attacks, deal 2 damage to the enemy hero. """
	events = Attack(FRIENDLY_MINIONS + RUSH).on(Hit(ENEMY_HERO,2))
	pass

class DMF_530:#OK <10>[1466]
	""" Feat of Strength
	Give a random [Taunt] minion in your hand +5/+5. """
	play = Buff(RANDOM(FRIENDLY_HAND + MINION + TAUNT), 'DMF_530e')
	pass
DMF_530e=buff(5,5)# <10>[1466]
#	""" So Strong!
#	+5/+5. """

class DMF_531:#OK <10>[1466]
	""" Stage Hand
	[Battlecry:] Give a random minion in your hand +1/+1. """
	play = Buff(RANDOM(FRIENDLY_HAND + MINION), 'DMF_531e') 
	pass
DMF_531e=buff(1,1)# <10>[1466]
""" Ready to Perform
+1/+1. """

class YOP_013:#OK <10>[1466]
	""" Spiked Wheel
	Has +3 Attack while your hero has Armor. """
	update = (ARMOR(FRIENDLY_HERO)>0) & BuffOnce(FRIENDLY_HERO, 'YOP_013e') | RemoveBuff(FRIENDLY_HERO, 'YOP_013e')
	pass
YOP_013e=buff(atk=3)##<12>[1466]

class YOP_014:#OK <10>[1466]
	""" Ironclad
	[Battlecry:] If your hero has Armor, gain +2/+2. """
	play = (ARMOR(FRIENDLY_HERO)>0) & Buff(SELF, 'YOP_014e')
	pass
YOP_014e=buff(2,2)

