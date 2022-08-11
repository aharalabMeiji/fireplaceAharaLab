
from ..utils import *

Stormwind_DemonHunter=[]


Stormwind_Need_for_Greed=True###
Stormwind_Crows_Nest_Lookout=True###
Stormwind_Proving_Grounds=True###
Stormwind_Irebound_Brute=True###
Stormwind_Final_Showdown=True###
Stormwind_Fel_Barrage=True###
Stormwind_Sigil_of_Alacrity=True###
Stormwind_Persistent_Peddler=True###
Stormwind_Felgorger=True###
Stormwind_Jace_Darkweaver=True###
Stormwind_Metamorfin=True###
Stormwind_Chaos_Leech=True###
Stormwind_Lions_Frenzy=True###



if Stormwind_Need_for_Greed:# 
	Stormwind_DemonHunter+=['DED_506']
class DED_506:# <14>[1578]
	""" Need for Greed
	[Tradeable]Draw 3 cards. If drawn this turn, this costs (3). """
	#
	pass

if Stormwind_Crows_Nest_Lookout:# 
	Stormwind_DemonHunter+=['DED_507']
class DED_507:# <14>[1578]
	""" Crow's Nest Lookout
	[Battlecry:] Deal 2 damageto the left and right-mostenemy minions. """
	#
	pass

if Stormwind_Proving_Grounds:# 
	Stormwind_DemonHunter+=['DED_508']
class DED_508:# <14>[1578]
	""" Proving Grounds
	Summon two minions from your deck.They fight! """
	#
	pass



if Stormwind_Irebound_Brute:# 
	Stormwind_DemonHunter+=['SW_037','SW_037e']
class SW_037:# <14>[1578]
	""" Irebound Brute
	[Taunt]Costs (1) less for eachcard drawn this turn. """
	#
	pass
class SW_037e:# <14>[1578]
	""" Prepped to Strike
	Costs (1) less. """
	#
	pass




if Stormwind_Final_Showdown:# 
	Stormwind_DemonHunter+=['SW_039']
	Stormwind_DemonHunter+=['SW_039t']
	Stormwind_DemonHunter+=['SW_039t2e']
	Stormwind_DemonHunter+=['SW_039t3']
	Stormwind_DemonHunter+=['SW_039t3_t']
class SW_039:# <14>[1578]
	""" Final Showdown
	[Questline:] Draw 4 cards in one turn. [Reward:] Reduce the Cost of the cards drawn by (1). """
	#
	pass
class SW_039t:# <14>[1578]
	""" Gain Momentum
	[Questline:] Draw 5 cards in one turn. [Reward:] Reduce the Cost of the cards drawn by (1). """
	#
	pass

class SW_039t2e:# <14>[1578]
	""" Faster Moves
	Costs (2) less. """
	#
	pass

class SW_039t3:# <14>[1578]
	""" Close the Portal
	[Questline:] Draw 5 cards in one turn.[Reward:] Demonslayer Kurtrus. """
	#
	pass

class SW_039t3_t:# <14>[1578]
	""" Demonslayer Kurtrus
	[Battlecry:] For the rest of the game, cards you draw cost (2) less. """
	#
	pass





if Stormwind_Fel_Barrage:# 
	Stormwind_DemonHunter+=['SW_040']
class SW_040:# <14>[1578]
	""" Fel Barrage
	Deal $2 damage tothe lowest Healthenemy, twice. """
	#
	pass




if Stormwind_Sigil_of_Alacrity:# 
	Stormwind_DemonHunter+=['SW_041']
class SW_041:# <14>[1578]
	""" Sigil of Alacrity
	At the start of your nextturn, draw a card and_reduce its Cost by (1). """
	#
	pass

class SW_041e2:# <14>[1578]
	""" Light as a Feather
	Costs (1) less. """
	#
	pass




if Stormwind_Persistent_Peddler:# 
	Stormwind_DemonHunter+=['SW_042']
class SW_042:# <14>[1578]
	""" Persistent Peddler
	[Tradeable][Deathrattle:] Summon a Persistent Peddler from your deck. """
	#
	pass




if Stormwind_Felgorger:# 
	Stormwind_DemonHunter+=['SW_043']
class SW_043:# <14>[1578]
	""" Felgorger
	[Battlecry:] Draw a Fel spell. Reduce its Cost by (2). """
	#
	pass




if Stormwind_Jace_Darkweaver:# 
	Stormwind_DemonHunter+=['SW_044']
class SW_044:# <14>[1578]
	""" Jace Darkweaver
	[Battlecry:] Cast all Fel spells you've played this game <i>(targets enemies if possible)</i>. """
	#
	pass




if Stormwind_Metamorfin:# 
	Stormwind_DemonHunter+=['SW_451']
	Stormwind_DemonHunter+=['SW_451e']
class SW_451:# <14>[1578]
	""" Metamorfin
	[Taunt][Battlecry:] If you've cast a Fel spell this turn, gain +2/+2. """
	#
	pass

class SW_451e:# <14>[1578]
	""" Mighty Morphing
	+2/+2. """
	#
	pass




if Stormwind_Chaos_Leech:# 
	Stormwind_DemonHunter+=['SW_452']
class SW_452:# <14>[1578]
	""" Chaos Leech
	[Lifesteal]. Deal $3 damage to a minion.[Outcast:] Deal $5 instead. """
	#
	pass




if Stormwind_Lions_Frenzy:# 
	Stormwind_DemonHunter+=['SW_454']
class SW_454:# <14>[1578]
	""" Lion's Frenzy
	Has Attack equal to the number of cards you've drawn this turn. """
	#
	pass



##############################################################################