
from ..utils import *

#CardSet.THE_SUNKEN_CITY_CardClass.DEMONHUNTER=['TSC_006','TSC_006e','TSC_006e2','TSC_057','TSC_057t','TSC_058','TSC_058e','TSC_217','TSC_217e','TSC_218','TSC_219','TSC_219e','TSC_219t','TSC_219t2','TSC_219t3','TSC_219t4','TSC_608','TSC_609','TSC_610','TSC_915',]
class TSC_006:# <14>[1658]
	""" Multi-Strike
	Give your hero +2 Attack this turn. They may attack an additional enemy minion. """
	#
	pass

class TSC_006e:# <14>[1658]
	""" Soulbound
	+2 Attack this turn. """
	#
	pass

class TSC_006e2:# <14>[1658]
	""" Multi-Strike enchant
	Attack +2. """
	#
	pass

class TSC_057:# <14>[1658]
	""" Azsharan Defector
	[Rush]. [Deathrattle:] Put a'Sunken Defector' on the_bottom of your deck. """
	#
	pass

class TSC_057t:# <14>[1658]
	""" Sunken Defector
	[Charge]. After this attacks, deal 5 damage to a random enemy minion. """
	#
	pass

class TSC_058:# <14>[1658]
	""" Predation
	Deal $3 damage.Costs (0) if you played a Naga while holding this. """
	#
	pass

class TSC_058e:# <14>[1658]
	""" Looting
	Costs (0). """
	#
	pass

class TSC_217:# <14>[1658]
	""" Wayward Sage
	[Outcast:] Reduce the Costof the left and right-most_cards in your hand by (1). """
	#
	pass

class TSC_217e:# <14>[1658]
	""" Found the Wrong Way
	Costs (1) less. """
	#
	pass

class TSC_218:# <14>[1658]
	""" Lady S'theno
	[Immune] while attacking.After you cast a spell, attack the lowest Health enemy. """

	pass

class TSC_219:# <14>[1658]
	""" Xhilag of the Abyss
	[Colossal +4]At the start of your turn,increase the damage of Xhilag's Stalks by 1. """
	play=(
		Summon(CONTROLLER,'TSC_219t'),
		Summon(CONTROLLER,'TSC_219t2'),
		Summon(CONTROLLER,'TSC_219t3'),
		Summon(CONTROLLER,'TSC_219t4')
	)
	events = OWN_TURN_BEGIN.on(
		AddScriptDataNum1(FRIENDLY_MINIONS+ID('TSC_219t'), 1),
		AddScriptDataNum1(FRIENDLY_MINIONS+ID('TSC_219t2'), 1),
		AddScriptDataNum1(FRIENDLY_MINIONS+ID('TSC_219t3'), 1),
		AddScriptDataNum1(FRIENDLY_MINIONS+ID('TSC_219t4'), 1)
		)
	pass
class TSC_219e:# <14>[1658]
	pass

class TSC_219t:# <14>[1658]
	""" Xhilag's Stalk
	At the end of your turn, deal @ damage to a random enemy. """
	events = OWN_TURN_END.on(HitScriptDataNum1(SELF, RANDOM(ENEMY_MINIONS)))
	pass

class TSC_219t2:# <14>[1658]
	""" Xhilag's Stalk
	At the end of your turn, deal @ damage to a random enemy. """
	events = OWN_TURN_END.on(HitScriptDataNum1(SELF, RANDOM(ENEMY_MINIONS)))
	pass

class TSC_219t3:# <14>[1658]
	""" Xhilag's Stalk
	At the end of your turn, deal @ damage to a random enemy. """
	events = OWN_TURN_END.on(HitScriptDataNum1(SELF, RANDOM(ENEMY_MINIONS)))
	pass

class TSC_219t4:# <14>[1658]
	""" Xhilag's Stalk
	At the end of your turn, deal @ damage to a random enemy. """
	events = OWN_TURN_END.on(HitScriptDataNum1(SELF, RANDOM(ENEMY_MINIONS)))
	pass

class TSC_608:# <14>[1658]
	""" Abyssal Depths
	Draw your two lowest Cost minions. """
	#
	pass

class TSC_609:# <14>[1658]
	""" Coilskar Commander
	[Taunt]. [Battlecry:] If you'vecast three spells whileholding this, summon two__copies of this.@ <i>({0} left!)</i>@ <i>(Ready!)</i> """
	#
	pass

class TSC_610:# <14>[1658]
	""" Glaiveshark
	[Battlecry:] If your heroattacked this turn, deal 2damage to all enemies. """
	#
	pass

class TSC_915:# <14>[1658]
	""" Bone Glaive
	[Battlecry:] [Dredge]. """
	#
	pass


