
from ..utils import *

Scholo_Warrior=['SCH_237','SCH_237e','SCH_237e2',
'SCH_238','SCH_238e','SCH_317','SCH_337','SCH_337t',
'SCH_425e','SCH_525','SCH_526e','SCH_621',]
#'Story_01_Garrosh','Story_01_Grommash','Story_01_Malkorok',
#'Story_01_Upgrade','Story_02_Baine','Story_02_Blackhand',
#'Story_02_BlackhandHP','Story_02_Gorgrom',
#'Story_02_GorgromHP','Story_02_Intimidation',]

class SCH_237:# <10>[1443]
	""" Athletic Studies
	[Discover] a [Rush] minion. Your next one costs (1) less. """
	play = (
		Discover(CONTROLLER, RandomMinion(rush=True)),
		Buff(FRIENDLY_MINIONS + RUSH, 'SCH_237e')
		)
	pass
class SCH_237e:# <10>[1443]
	""" Athletic Studies
	Your next [Rush] minion costs (1) less. """
	cost = lambda self, i: max(i-1, 0)
	events = Play(FRIENDLY_MINIONS + RUSH).on(Destroy(SELF))
	pass
class SCH_237e2:# <10>[1443]
	""" Studying Athletics
	Costs (1) less. """
	#
	pass

class SCH_238:# <10>[1443] #
	""" Reaper's Scythe
	[Spellburst]: Also damages adjacent minions this turn. """
	play = OWN_SPELL_PLAY.on(Buff(SELF, 'SCH_238e'))
	pass

class SCH_238e:# <10>[1443] #_ONE_TURN_EFFECT
	""" Reaping
	Damages minions next to whomever your hero attacks. """
	events = Attack(OWNER, ENEMY_MINIONS).on(Hit(ADJUSCENT(Attack.DEFENDER), ATK(OWNER)))
	pass

class SCH_317:# <10>[1443]
	""" Playmaker
	After you play a [Rush]minion, summon a copy_with 1 Health remaining. """
	#
	pass

class SCH_337:# <10>[1443]
	""" Troublemaker
	At the end of your turn, summon two 3/3 Ruffians that attack random enemies. """
	#
	pass

class SCH_337t:# <10>[1443]
	""" Ruffian
	 """
	#
	pass

class SCH_425e:# <10>[1443]
	""" Sharpened
	+1/+1. """
	#
	pass

class SCH_525:# <10>[1443]
	""" In Formation!
	Add 2 random [Taunt] minions to your hand. """
	#
	pass

class SCH_526e:# <10>[1443]
	""" A Common Peasant
	Health changed to 1. """
	#
	pass

class SCH_621:# <10>[1443]
	""" Rattlegore
	[Deathrattle:] Resummon this with -1/-1. """
	#
	pass

