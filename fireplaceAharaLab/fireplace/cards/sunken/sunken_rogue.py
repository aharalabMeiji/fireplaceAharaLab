from ..utils import *

Sunken_Rogue=[]

Sunken_Shattershambler=True  ###
Sunken_Inkveil_Ambusher=True  ###
Sunken_Jackpot=True  ###
Sunken_Cutlass_Courier=True  ###
Sunken_Swordfish=True  ###
Sunken_Azsharan_Vessel=True  ###
Sunken_Gone_Fishin=True  ###
Sunken_Blood_in_the_Water=True  ###
Sunken_Bootstrap_Sunkeneer=True  ###
Sunken_Pirate_Admiral_Hooktusk=True  ###
Sunken_Swiftscale_Trickster=True  ###
Sunken_Crabatoa=True  ###
Sunken_Filletfighter=True  ###


if Sunken_Shattershambler:# 
	Sunken_Rogue+=['TID_078','TID_078e','TID_078e2',]
class TID_078:# <7>[1658]
	""" Shattershambler
	[Battlecry:] Your next [Deathrattle] minion costs (1) less, but immediately dies when played. """
	play = Buff(FRIENDLY_HAND + DEATHRATTLE, 'TID_078e'),Buff(FRIENDLY_HAND + DEATHRATTLE, 'TID_078e2')
	pass
class TID_078e:
	events = [
		Play(CONTROLLER, OWNER).Destroy(OWNER),
		Play(CONTROLLER, MINION+DEATHRATTLE).Destroy(SELF)
	]
	pass
class TID_078e2:
	cost = lambda self, i:max(i-1,0)
	events = Play(CONTROLLER, MINION+DEATHRATTLE).Destroy(SELF)
	pass



if Sunken_Inkveil_Ambusher:# 
	Sunken_Rogue+=['TID_080']
	Sunken_Rogue+=['TID_080e2']
class TID_080:# <7>[1658]
	""" Inkveil Ambusher
	[Stealth]Has +3 Attack and [Immune] while attacking. """
	#
	pass

class TID_080e2:# <7>[1658]
	""" Inked
	[Immune] and +3 Attack while attacking. """
	#
	pass




if Sunken_Jackpot:# 
	Sunken_Rogue+=['TID_931']
class TID_931:# <7>[1658]
	""" Jackpot!
	Add two randomspells from other classesthat cost (5) or moreto your hand. """
	#
	pass




if Sunken_Cutlass_Courier:# 
	Sunken_Rogue+=['TSC_085']
class TSC_085:# <7>[1658]
	""" Cutlass Courier
	After your hero attacks, draw a Pirate. """
	#
	pass




if Sunken_Swordfish:# 
	Sunken_Rogue+=['TSC_086']

	Sunken_Rogue+=['TSC_086e']
class TSC_086:# <7>[1658]
	""" Swordfish
	[Battlecry:] [Dredge].If it's a Pirate, give this weapon and the Pirate +2 Attack. """
	#
	pass

class TSC_086e:# <7>[1658]
	""" Sharp Point
	+2 Attack. """
	#
	pass

if Sunken_Azsharan_Vessel:# 
	Sunken_Rogue+=['TSC_912']

	Sunken_Rogue+=['TSC_912t']

	Sunken_Rogue+=['TSC_912t2']

	Sunken_Rogue+=['TSC_912t3']
class TSC_912:# <7>[1658]
	""" Azsharan Vessel
	Summon two 3/3 Pirates with [Stealth]. Put a 'Sunken Vessel' on the bottom of your deck. """
	#
	pass

class TSC_912t:# <7>[1658]
	""" Sunken Vessel
	[Casts When Drawn]Summon two 3/3 Pirates with [Stealth]. """
	#
	pass

class TSC_912t2:# <7>[1658]
	""" Sunken Pirate
	[Stealth] """
	#
	pass

class TSC_912t3:# <7>[1658]
	""" Azsharan Pirate
	[Stealth] """
	#
	pass




if Sunken_Gone_Fishin:# 
	Sunken_Rogue+=['TSC_916']
class TSC_916:# <7>[1658]
	""" Gone Fishin'
	[Dredge].[Combo:] Draw a card. """
	#
	pass




if Sunken_Blood_in_the_Water:# 
	Sunken_Rogue+=['TSC_932']

	Sunken_Rogue+=['TSC_932t']
class TSC_932:# <7>[1658]
	""" Blood in the Water
	Deal $3 damage to an enemy. Summon a 5/5 Shark with [Rush]. """
	#
	pass

class TSC_932t:# <7>[1658]
	""" Tiger Shark
	[Rush] """
	#
	pass




if Sunken_Bootstrap_Sunkeneer:# 
	Sunken_Rogue+=['TSC_933']
class TSC_933:# <7>[1658]
	""" Bootstrap Sunkeneer
	[Combo:] Put an enemyminion on the bottom of_your opponent's deck. """
	#
	pass




if Sunken_Pirate_Admiral_Hooktusk:# 
	Sunken_Rogue+=['TSC_934']

	Sunken_Rogue+=['TSC_934t']
	Sunken_Rogue+=['TSC_934t2']
	Sunken_Rogue+=['TSC_934t3']
class TSC_934:# <7>[1658]
	""" Pirate Admiral Hooktusk
	[Battlecry:] If you've summoned 8 other Pirates this game, plunder the enemy!@ <i>({0} left!)</i>@ <i>(Ready!)</i> """
	#
	pass

class TSC_934t:# <7>[1658]
	""" Take their Supplies!
	Take 5 cards from your opponent's deck. """
	#
	pass


class TSC_934t2:# <7>[1658]
	""" Take their Gold!
	Take 2 cards from your opponent's hand. """
	#
	pass


class TSC_934t3:# <7>[1658]
	""" Take their Ship!
	Take control of your opponent's highest Attack minion. """
	#
	pass





if Sunken_Swiftscale_Trickster:# 
	Sunken_Rogue+=['TSC_936']

	Sunken_Rogue+=['TSC_936e']
class TSC_936:# <7>[1658]
	""" Swiftscale Trickster
	[Battlecry:] Your next spell this turn costs (0). """
	#
	pass

class TSC_936e:# <7>[1658]
	""" Fooled the Audience
	Your next spell this turn costs (0). """
	#
	pass




if Sunken_Crabatoa:# 
	Sunken_Rogue+=['TSC_937']

	Sunken_Rogue+=['TSC_937e']

	Sunken_Rogue+=['TSC_937t']

	Sunken_Rogue+=['TSC_937t2']
	Sunken_Rogue+=['TSC_937t3']

class TSC_937:# <7>[1658]
	""" Crabatoa
	[Colossal +2]Your Crabatoa Claws have +2 Attack. """
	#
	pass

class TSC_937e:# <7>[1658]
	""" Crusty Treasure
	+2 Attack. """
	#
	pass

class TSC_937t:# <7>[1658]
	""" Crabatoa's Claw
	[Rush][Deathrattle:]  Equip a 2/1 Claw. """
	#
	pass

class TSC_937t2:# <7>[1658]
	""" Crabatoa Claw
	 """
	#
	pass

class TSC_937t3:# <7>[1658]
	""" Crabatoa's Claw
	[Rush][Deathrattle:]  Equip a 2/1 Claw. """
	#
	pass




if Sunken_Filletfighter:# 
	Sunken_Rogue+=['TSC_963']
class TSC_963:# <7>[1658]
	""" Filletfighter
	[Battlecry:] Deal 1 damage. """
	#
	pass



