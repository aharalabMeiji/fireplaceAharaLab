from ..utils import *

Sunken_Warrior=[]


Sunken_Igneous_Lavagorger=True  ###
Sunken_Clash_of_the_Colossals=True  ###
Sunken_Tidal_Revenant=True  ###
Sunken_Trenchstalker=True  ###
Sunken_Nellie_the_Great_Thresher=True  ###
Sunken_Azsharan_Trident=True  ###
Sunken_Blackscale_Brute=True  ###
Sunken_Forged_in_Flame=True  ###
Sunken_From_the_Depths=True  ###
Sunken_Guard_the_City=True  ###
Sunken_Obsidiansmith=True  ###
Sunken_Lady_Ashvane=True  ###
Sunken_The_Fires_of_Zin_Azshari=True  ###


if Sunken_Igneous_Lavagorger:# 
	Sunken_Warrior+=['TID_714']
	Sunken_Warrior+=['TID_714e']
class TID_714:# <10>[1658]
	""" Igneous Lavagorger
	[Taunt] [Battlecry:] [Dredge]. Gain_Armor equal to its Cost. """
	#
	pass
class TID_714e:# <10>[1658]
	""" Gorged
	Increased attack. """
	#
	pass




if Sunken_Clash_of_the_Colossals:# 
	Sunken_Warrior+=['TID_715']
	Sunken_Warrior+=['TID_715e']
class TID_715:# <10>[1658]
	""" Clash of the Colossals
	Add a random [Colossal] minion to both players' hands. Yours costs (2) less. """
	#

class TID_715e:# <10>[1658]
	""" Colossal Advantage
	Costs (2) less. """
	#
	pass




if Sunken_Tidal_Revenant:# 
	Sunken_Warrior+=['TID_716']
class TID_716:# <10>[1658]
	""" Tidal Revenant
	[Battlecry:] Deal 5 damage. Gain 5 Armor. """
	#
	pass




if Sunken_Trenchstalker:# 
	Sunken_Warrior+=['TSC_659']
class TSC_659:# <10>[1658]
	""" Trenchstalker
	[Battlecry:] Attack three different random enemies. """
	#
	pass




if Sunken_Nellie_the_Great_Thresher:# 
	Sunken_Warrior+=['TSC_660']
	Sunken_Warrior+=['TSC_660e']
	Sunken_Warrior+=['TSC_660e2']
	Sunken_Warrior+=['TSC_660t']
class TSC_660:# <10>[1658]
	""" Nellie, the Great Thresher
	[Colossal +1][Battlecry:] [Discover] 3 Piratesto crew Nellie's Ship! """
	#

class TSC_660e:# <10>[1658]
	""" Mercenary's Fee
	Costs (1) less. """
	#

class TSC_660e2:# <10>[1658]
	""" Pirate Crew
	Holding Nellie's Pirate Crew. """
	#

class TSC_660t:# <10>[1658]
	""" Nellie's Pirate Ship
	[[Taunt].] [Deathrattle:] AddNellie's Pirate crew to yourhand. They cost (1) less. """
	#
	pass




if Sunken_Azsharan_Trident:# 
	Sunken_Warrior+=['TSC_913']
	Sunken_Warrior+=['TSC_913t']
class TSC_913:# <10>[1658]
	""" Azsharan Trident
	[Deathrattle:] Puta 'Sunken Trident' on the_bottom of your deck. """
	#
	pass
class TSC_913t:# <10>[1658]
	""" Sunken Trident
	After your hero attacks, deal 2 damage to all enemy minions. """
	#
	pass




if Sunken_Blackscale_Brute:# 
	Sunken_Warrior+=['TSC_917']
	Sunken_Warrior+=['TSC_917t']
class TSC_917:# <10>[1658]
	""" Blackscale Brute
	[Taunt]. [Battlecry:] If youhave a weapon equipped, summon a 5/6 Naga with [Rush]. """
	#

class TSC_917t:# <10>[1658]
	""" Firescale Berserker
	[Rush] """
	#
	pass




if Sunken_Forged_in_Flame:# 
	Sunken_Warrior+=['TSC_939']
class TSC_939:# <10>[1658]
	""" Forged in Flame
	Destroy your weapon, then draw cards equal to its Attack. """
	#
	pass




if Sunken_From_the_Depths:# 
	Sunken_Warrior+=['TSC_940']
	Sunken_Warrior+=['TSC_940e2']
class TSC_940:# <10>[1658]
	""" From the Depths
	Reduce the Cost of thebottom five cards in your_deck by (3), then [Dredge]. """
	#
	pass

class TSC_940e2:# <10>[1658]
	""" Current Events
	Costs (3) less. """
	#
	pass




if Sunken_Guard_the_City:# 
	Sunken_Warrior+=['TSC_941']
	Sunken_Warrior+=['TSC_941t']
class TSC_941:# <10>[1658]
	""" Guard the City
	Gain 3 Armor.Summon a 2/3 Naga with [Taunt]. """
	#

class TSC_941t:# <10>[1658]
	""" Naga Centaur
	[Taunt] """
	#
	pass




if Sunken_Obsidiansmith:# 
	Sunken_Warrior+=['TSC_942']
	Sunken_Warrior+=['TSC_942e']
class TSC_942:# <10>[1658]
	""" Obsidiansmith
	[Battlecry:] [Dredge]. If it'sa minion or a weapon,give it +1/+1. """
	#
	pass

class TSC_942e:# <10>[1658]
	""" Flameforged
	+1/+1. """
	#
	pass




if Sunken_Lady_Ashvane:# 
	Sunken_Warrior+=['TSC_943']
	Sunken_Warrior+=['TSC_943e']
class TSC_943:# <10>[1658]
	""" Lady Ashvane
	[Battlecry:] Give all weaponsin your hand, deck, and battlefield +1/+1. """
	#

class TSC_943e:# <10>[1658]
	""" Rigid Carapace
	+1/+1. """
	#
	pass




if Sunken_The_Fires_of_Zin_Azshari:# 
	Sunken_Warrior+=['TSC_944']
	Sunken_Warrior+=['TSC_944e']
class TSC_944:# <10>[1658]
	""" The Fires of Zin-Azshari
	Replace your deck with minions that cost (5) or more. They cost (5). """
	#
	pass

class TSC_944e:# <10>[1658]
	""" The Fiery Deep
	Costs (5). """
	#
	pass

