
from ..utils import *

Scholo_Warrior=['SCH_238','SCH_238e','SCH_317','SCH_525',]
# bigWarrior: 'SCH_237','SCH_237e','SCH_237e2','SCH_337','SCH_337t','SCH_621',
# 'SCH_526e','SCH_425e',

#'Story_01_Garrosh','Story_01_Grommash','Story_01_Malkorok',
#'Story_01_Upgrade','Story_02_Baine','Story_02_Blackhand',
#'Story_02_BlackhandHP','Story_02_Gorgrom',
#'Story_02_GorgromHP','Story_02_Intimidation',]

#class SCH_237:# <10>[1443] bigWarrior
#	""" Athletic Studies
#	[Discover] a [Rush] minion. Your next one costs (1) less. """
#	play = (
#		Discover(CONTROLLER, RandomMinion(rush=True)),
#		Buff(FRIENDLY_MINIONS + RUSH, 'SCH_237e')
#		)
#	pass
#class SCH_237e:# <10>[1443]
#	""" Athletic Studies
#	Your next [Rush] minion costs (1) less. """
#	cost = lambda self, i: max(i-1, 0)
#	events = Play(FRIENDLY_MINIONS + RUSH).on(Destroy(SELF))
#	pass
#class SCH_237e2:# <10>[1443]
#	""" Studying Athletics
#	Costs (1) less. """
#	#
#	pass

class SCH_238:#OK <10>[1443] #
	""" Reaper's Scythe
	[Spellburst]: Also damages adjacent minions this turn. """
	events = OWN_SPELL_PLAY.on(BuffOnce(FRIENDLY_HERO, 'SCH_238e'))
	pass

class SCH_238e:# <10>[1443] #_ONE_TURN_EFFECT
	""" Reaping
	Damages minions next to whomever your hero attacks. """
	events = Attack(FRIENDLY_HERO, ENEMY_MINIONS).on(Hit(ADJACENT(ENEMY_MINIONS+Attack.DEFENDER), ATK(OWNER)))
	pass

class SCH_317_Action(TargetedAction):
	TARGET = ActionArg()
	CARD = ActionArg()
	def do(self, source, target, card):
		controller = target
		new_card = Summon(controller, card.id).trigger(controller)
		if new_card[0] != []:
			new_card = new_card[0][0]
			new_card.max_health = 1
	pass
class SCH_317:#OK <10>[1443]
	""" Playmaker
	After you play a [Rush]minion, summon a copy_with 1 Health remaining. """
	events = Play(CONTROLLER, FRIENDLY_MINIONS + RUSH).on(SCH_317_Action(CONTROLLER, Play.CARD))
	pass

#class SCH_337:# <10>[1443] bigWarrior
#	""" Troublemaker
#	At the end of your turn, summon two 3/3 Ruffians that attack random enemies. """
#	events = OWN_TURN_END.on(
#		Summon(CONTROLLER, 'SCH_337t').then(RegularAttack(Summon.CARD, RANDOM(ENEMY_MINIONS)))
#		)
#	pass
#class SCH_337t:# <10>[1443]
#	""" Ruffian
#	 """
#	#
	pass

#class SCH_425e:# <10>[1443] # SCH_425:<12>[1443]
#	""" Sharpened
#	+1/+1. """
#	#
#	pass

class SCH_525:#OK <10>[1443]
	""" In Formation!
	Add 2 random [Taunt] minions to your hand. """
	play = Give(CONTROLLER, RandomMinion(taunt=True)) * 2
	pass

#class SCH_526e:# <10>[1443] # SCH_526:<5>[1443]
#	""" A Common Peasant
#	Health changed to 1. """
#	#
#	pass

#class SCH_621:# <10>[1443] -> bigWarrior
#	""" Rattlegore
#	[Deathrattle:] Resummon this with -1/-1. """
#	#
#	pass

