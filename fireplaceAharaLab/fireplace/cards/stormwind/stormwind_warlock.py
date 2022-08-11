
from ..utils import *

StormWind_Warlock=[]

StormWind_Shadowblade_Slinger=True  ###
StormWind_Wicked_Shipment=True  ###
StormWind_Hullbreaker=True  ###
StormWind_Runed_Mithril_Rod=True  ###
StormWind_Bloodbound_Imp=True  ###
StormWind_Dark_Alley_Pact=True  ###
StormWind_Shady_Bartender=True  ###
StormWind_Dreaded_Mount=True  ###
StormWind_Demonic_Assault=True  ###
StormWind_Entitled_Customer=True  ###
StormWind_Touch_of_the_Nathrezim=True  ###
StormWind_The_Demon_Seed=True  ###
StormWind_Anetheron=True  ###

######################################################


if StormWind_Shadowblade_Slinger:# 
	StormWind_Warlock+=['DED_503']
class DED_503:# <9>[1578]
	""" Shadowblade Slinger
	[Battlecry:] If you've takendamage this turn, deal that_much to an enemy minion. """
	#
	pass




if StormWind_Wicked_Shipment:# 
	StormWind_Warlock+=['DED_504']
class DED_504:# <9>[1578]
	""" Wicked Shipment
	[Tradeable]Summon @ 1/1 |4(Imp, Imps).<i>(Upgrades by 2when [Traded]!)</i> """
	#
	pass




if StormWind_Hullbreaker:# 
	StormWind_Warlock+=['DED_505']
class DED_505:# <9>[1578]
	""" Hullbreaker
	[Battlecry and Deathrattle:]Draw a spell. Your hero takesdamage equal to its Cost. """
	#
	pass




if StormWind_Runed_Mithril_Rod:# 
	StormWind_Warlock+=['SW_003']
class SW_003:# <9>[1578]
	""" Runed Mithril Rod
	After you draw 4 cards,reduce the Cost of cardsin your hand by (1).Lose 1 Durability. """
	#
	pass




if StormWind_Bloodbound_Imp:# 
	StormWind_Warlock+=['SW_084']
class SW_084:# <9>[1578]
	""" Bloodbound Imp
	Whenever this attacks, deal 2 damage to your_hero. """
	#
	pass




if StormWind_Dark_Alley_Pact:# 
	StormWind_Warlock+=['SW_085']
	StormWind_Warlock+=['SW_085t']
class SW_085:# <9>[1578]
	""" Dark Alley Pact
	Summon a Fiendwith stats equal toyour hand size. """
	#
	pass

class SW_085t:# <9>[1578]
	""" Fiend
	 """
	#
	pass




if StormWind_Shady_Bartender:# 
	StormWind_Warlock+=['SW_086']
class SW_086:# <9>[1578]
	""" Shady Bartender
	[Tradeable][Battlecry:] Give your Demons +2/+2. """
	#
	pass




if StormWind_Dreaded_Mount:# 
	StormWind_Warlock+=['SW_087']
	StormWind_Warlock+=['SW_087t']
class SW_087:# <9>[1578]
	""" Dreaded Mount
	Give a minion +1/+1.When it dies, summonan endless Dreadsteed. """
	#
	pass

class SW_087t:# <9>[1578]
	""" Tamsin's Dreadsteed
	[Deathrattle:] At the endof the turn, summon Tamsin's Dreadsteed. """
	#
	pass




if StormWind_Demonic_Assault:# 
	StormWind_Warlock+=['SW_088']
class SW_088:# <9>[1578]
	""" Demonic Assault
	Deal $3 damage.Summon two 1/3Voidwalkers with [Taunt]. """
	#
	pass




if StormWind_Entitled_Customer:# 
	StormWind_Warlock+=['SW_089']
class SW_089:# <9>[1578]
	""" Entitled Customer
	[Battlecry:] Deal damage equal to your hand size to all other minions. """
	#
	pass




if StormWind_Touch_of_the_Nathrezim:# 
	StormWind_Warlock+=['SW_090']
class SW_090:# <9>[1578]
	""" Touch of the Nathrezim
	Deal $2 damage to aminion. If it dies, restore3 Health to your hero. """
	#
	pass




if StormWind_The_Demon_Seed:# 
	StormWind_Warlock+=['SW_091']
	StormWind_Warlock+=['SW_091t']
	StormWind_Warlock+=['SW_091t3']
	StormWind_Warlock+=['SW_091t4']
class SW_091:# <9>[1578]
	""" The Demon Seed
	[Questline:] Take 8damage on your turns.[Reward:] [Lifesteal]. Deal $3damage to the enemy hero. """
	#
	pass

class SW_091t:# <9>[1578]
	""" Establish the Link
	[Questline:] Take 8damage on your turns.[Reward:] [Lifesteal]. Deal $3damage to the enemy hero. """
	#
	pass

class SW_091t3:# <9>[1578]
	""" Complete the Ritual
	[Questline:] Take 8damage on your turns.[Reward:] BlightbornTamsin. """
	#
	pass

class SW_091t4:# <9>[1578]
	""" Blightborn Tamsin
	[Battlecry:] For the rest ofthe game, damage you takeon your turn damages your__opponent instead. """
	#
	pass




if StormWind_Anetheron:# 
	StormWind_Warlock+=['SW_092']
class SW_092:# <9>[1578]
	""" Anetheron
	Costs (1) if your hand is full. """
	#
	pass


