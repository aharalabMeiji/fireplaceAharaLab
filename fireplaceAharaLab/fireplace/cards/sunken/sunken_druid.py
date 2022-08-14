from ..utils import *

Sunken_Druid=[]

Sunken_Spirit_of_the_Tides=True  ###
Sunken_Moonbeam=True  ###
Sunken_Herald_of_Nature=True  ###
Sunken_Colaque=True  ###
Sunken_Flipper_Friends=True  ###
Sunken_Seaweed_Strike=True  ###
Sunken_Green_Thumb_Gardener=True  ###
Sunken_Bottomfeeder=True  ###
Sunken_Aquatic_Form=True  ###
Sunken_Miracle_Growth=True  ###
Sunken_Dozing_Kelpkeeper=True  ###
Sunken_Hedra_the_Heretic=True  ###
Sunken_Azsharan_Gardens=True  ###




if Sunken_Spirit_of_the_Tides:# 
	Sunken_Druid+=['TID_000']
	Sunken_Druid+=['TID_000e']
class TID_000:# <2>[1658]
	""" Spirit of the Tides
	If you have any unspentMana at the end of_your turn, gain +1/+2. """
	#
	pass
class TID_000e:# <2>[1658]
	""" Endless Sea
	+1/+2. """
	#
	pass




if Sunken_Moonbeam:# 
	Sunken_Druid+=['TID_001']
class TID_001:# <2>[1658]
	""" Moonbeam
	Deal $1 damage to an enemy, twice. """
	#
	pass




if Sunken_Herald_of_Nature:# 
	Sunken_Druid+=['TID_002']
	Sunken_Druid+=['TID_002e']
class TID_002:# <2>[1658]
	""" Herald of Nature
	[Battlecry:] If you've cast a Nature spell while holding this, give your other minions +1/+2. """
	#
	pass
class TID_002e:# <2>[1658]
	""" Nature's Bounty
	+1/+2. """
	#
	pass




if Sunken_Colaque:# 
	Sunken_Druid+=['TSC_026']
	Sunken_Druid+=['TSC_026t']
class TSC_026:# <2>[1658]
	""" Colaque
	[Colossal +1] [Immune] while you controlColaque's Shell. """
	#
	pass

class TSC_026t:# <2>[1658]
	""" Colaque's Shell
	[Taunt][Deathrattle:] Gain 8 Armor. """
	#
	pass




if Sunken_Flipper_Friends:# 
	Sunken_Druid+=['TSC_650']
	Sunken_Druid+=['TSC_650a']
	Sunken_Druid+=['TSC_650d']
	Sunken_Druid+=['TSC_650t']
	Sunken_Druid+=['TSC_650t4']
class TSC_650:# <2>[1658]
	""" Flipper Friends
	[Choose One] - Summon a6/6 Orca with [Taunt]; orsix 1/1 Otters with [Rush]. """
class TSC_650a:# <2>[1658]
	""" Order the Orca
	Summon a 6/6 Orca with [Taunt]. """
	#

class TSC_650d:# <2>[1658]
	""" Romp of Otters
	Summon six 1/1 Otters with [Rush]. """
	#

class TSC_650t:# <2>[1658]
	""" Orca
	[Taunt] """
	#

class TSC_650t4:# <2>[1658]
	""" Otter
	[Rush] """
	#
	pass




if Sunken_Seaweed_Strike:# 
	Sunken_Druid+=['TSC_651']
	Sunken_Druid+=['TSC_651e']
class TSC_651:# <2>[1658]
	""" Seaweed Strike
	Deal $4 damage to a minion.If you played a Naga whileholding this, also give yourhero +4 Attack this turn. """
	#

class TSC_651e:# <2>[1658]
	""" Explosive
	+4 Attack this turn. """
	#
	pass




if Sunken_Green_Thumb_Gardener:# 
	Sunken_Druid+=['TSC_652']
class TSC_652:# <2>[1658]
	""" Green-Thumb Gardener
	[Battlecry:] Refresh emptyMana Crystals equal to theCost of the most expensivespell in your hand. """
	#
	pass




if Sunken_Bottomfeeder:# 
	Sunken_Druid+=['TSC_653']
class TSC_653:# <2>[1658]
	""" Bottomfeeder
	[Deathrattle:] Add a Bottomfeeder to the bottom of your deck with permanent +2/+2. """
	#
	pass




if Sunken_Aquatic_Form:# 
	Sunken_Druid+=['TSC_654']
class TSC_654:# <2>[1658]
	""" Aquatic Form
	[Dredge]. If you have the Mana to play the card this turn, draw it. """
	#
	pass




if Sunken_Miracle_Growth:# 
	Sunken_Druid+=['TSC_656']
	Sunken_Druid+=['TSC_656t']
class TSC_656:# <2>[1658]
	""" Miracle Growth
	Draw 3 cards.Summon a Plant with[Taunt] and stats equalto your hand size. """
	#

class TSC_656t:# <2>[1658]
	""" Kelp Creeper
	[Taunt] """
	#
	pass




if Sunken_Dozing_Kelpkeeper:# 
	Sunken_Druid+=['TSC_657']
	Sunken_Druid+=['TSC_657e']
class TSC_657:# <2>[1658]
	""" Dozing Kelpkeeper
	[Rush]. Starts [Dormant].After you've cast 5 Mana_worth of spells, awaken. """
	#

class TSC_657e:# <2>[1658]
	""" Aquatic Slumber
	[Dormant]. Awaken after you cast @ Mana worth of spells. """
	#
	pass




if Sunken_Hedra_the_Heretic:# 
	Sunken_Druid+=['TSC_658']
class TSC_658:# <2>[1658]
	""" Hedra the Heretic
	[Battlecry:] For each spellyou've cast while holdingthis, summon a minionof that spell's Cost. """
	#
	pass




if Sunken_Azsharan_Gardens:# 
	Sunken_Druid+=['TSC_927']
	Sunken_Druid+=['TSC_927e']
	Sunken_Druid+=['TSC_927t']
class TSC_927:# <2>[1658]
	""" Azsharan Gardens
	Give all minions in your hand +1/+1. Put a 'Sunken Gardens' on the bottom of your deck. """
	#

class TSC_927e:# <2>[1658]
	""" Watered
	+1/+1. """
	#

class TSC_927t:# <2>[1658]
	""" Sunken Gardens
	Give +1/+1 to all minions in your hand, deck, and battlefield. """
	#
	pass

