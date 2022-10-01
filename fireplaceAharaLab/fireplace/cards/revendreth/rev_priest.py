from ..utils import *

Rev_Priest=[]

Rev_Clear_Conscience=True
Rev_Incriminating_Psychic=True
Rev_Theft_Accusation=True
Rev_Suspicious_Usher=True
Rev_The_Harvester_of_Envy=True
Rev_Mysterious_Visitor=True
Rev_Partner_in_Crime=True
Rev_Boon_of_the_Ascended=True
Rev_The_Light_It_Burns=True
Rev_Pelagos=True
Rev_Clean_the_Scene=True
Rev_Identity_Theft=True
Rev_Cathedral_of_Atonement=True
Rev_Pelagos=True
Rev_Cathedral_of_Atonement=True


if Rev_Clear_Conscience:# 
	Rev_Priest+=['MAW_021']
class MAW_021:# <6>[1691]
	""" Clear Conscience
	Give a friendly minion +2/+3 and "Only you can target this with spells and Hero Powers." """
	#
	pass

	Rev_Priest+=['MAW_021e']
class MAW_021e:# <6>[1691]
	""" Cleared Conscience
	+2/+3 and "Can't be targeted by spells or Hero Powers". """
	#
	pass

	Rev_Priest+=['MAW_021e2']
class MAW_021e2:# <6>[1691]
	""" In the Clear
	Can't be targeted by spells or Hero Powers. """
	#
	pass

if Rev_Incriminating_Psychic:# 
	Rev_Priest+=['MAW_022']
class MAW_022:# <6>[1691]
	""" Incriminating Psychic
	<b>Taunt</b>  <b>Deathrattle:</b> Copy a  random card from your opponent's hand. """
	#
	pass

if Rev_Theft_Accusation:# 
	Rev_Priest+=['MAW_023']
class MAW_023:# <6>[1691]
	""" Theft Accusation
	Choose a minion. Destroy it after you play a card copied from the opponent. """
	#
	pass

	Rev_Priest+=['MAW_023e']
class MAW_023e:# <6>[1691]
	""" Theft Trial
	When you play a card copied from your opponent, destroy the accused. """
	#
	pass

	Rev_Priest+=['MAW_023e2']
class MAW_023e2:# <6>[1691]
	""" Accused of Theft
	When the accuser plays a card copied from their enemy, this minion dies. """
	#
	pass

if Rev_Suspicious_Usher:# 
	Rev_Priest+=['REV_002']
class REV_002:# <6>[1691]
	""" Suspicious Usher
	<b>Battlecry:</b> <b>Discover</b> a <b>Legendary</b> minion. If your opponent guesses your __choice, they get a copy. """
	#
	pass

if Rev_The_Harvester_of_Envy:# 
	Rev_Priest+=['REV_011']
class REV_011:# <6>[1691]
	""" The Harvester of Envy
	After you play a card copied from the opponent, steal the original. """
	#
	pass

	Rev_Priest+=['REV_011e']
class REV_011e:# <6>[1691]
	""" Copied From Opponent
	 """
	#
	pass

if Rev_Mysterious_Visitor:# 
	Rev_Priest+=['REV_246']
class REV_246:# <6>[1691]
	""" Mysterious Visitor
	<b>Battlecry:</b> Reduce the Cost of cards copied from your opponent by (2). """
	#
	pass

	Rev_Priest+=['REV_246e2']
class REV_246e2:# <6>[1691]
	""" Mind Read
	Costs (2) less. """
	#
	pass

if Rev_Partner_in_Crime:# 
	Rev_Priest+=['REV_247']
class REV_247:# <6>[1691]
	""" Partner in Crime
	<b>Battlecry:</b> Summon a  copy of this minion at  the end of your turn. """
	#
	pass

	Rev_Priest+=['REV_247e']
class REV_247e:# <6>[1691]
	""" Alibi
	At the end of your turn, summon a copy of this. """
	#
	pass

if Rev_Boon_of_the_Ascended:# 
	Rev_Priest+=['REV_248']
class REV_248:# <6>[1691]
	""" Boon of the Ascended
	Give a minion +2 Health. Summon a Kyrian with its stats and <b>Taunt</b>. """
	#
	pass

	Rev_Priest+=['REV_248e']
class REV_248e:# <6>[1691]
	""" Boon of the Ascended
	+2 Health. """
	#
	pass

	Rev_Priest+=['REV_248t']
class REV_248t:# <6>[1691]
	""" Ascended Kyrian
	<b>Taunt</b> """
	#
	pass

if Rev_The_Light_It_Burns:# 
	Rev_Priest+=['REV_249']
class REV_249:# <6>[1691]
	""" The Light! It Burns!
	Deal damage to a minion  equal to its Attack. """
	#
	pass

if Rev_Pelagos:# 
	Rev_Priest+=['REV_250']
class REV_250:# <6>[1691]
	""" Pelagos
	After you cast a spell  on a friendly minion, set  its Attack and Health to  the higher of the two. """
	#
	pass

	Rev_Priest+=['REV_250e1']
class REV_250e1:# <6>[1691]
	""" Pelagos' Blessing
	Stats set to the higher value. """
	#
	pass

	Rev_Priest+=['REV_250e2']
class REV_250e2:# <6>[1691]
	""" Pelagos' Blessing
	Stats set to the higher value. """
	#
	pass

if Rev_Clean_the_Scene:# 
	Rev_Priest+=['REV_252']
class REV_252:# <6>[1691]
	""" Clean the Scene
	Destroy all minions with 3 or less Attack. <b>Infuse (@):</b> 6 or less. """
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_252t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_252t', 1))
	#
	pass

	Rev_Priest+=['REV_252t']
class REV_252t:# <6>[1691]
	""" Clean the Scene
	<b>Infused</b> Destroy all minions with  6 or less Attack. """
	#
	pass

if Rev_Identity_Theft:# 
	Rev_Priest+=['REV_253']
class REV_253:# <6>[1691]
	""" Identity Theft
	<b>Discover</b> a copy of a card from your opponent's hand and deck. """
	#
	pass

if Rev_Cathedral_of_Atonement:# 
	Rev_Priest+=['REV_290']
class REV_290:# <6>[1691]
	""" Cathedral of Atonement
	Give a minion +2/+1 and draw a card. """
	#
	pass

	Rev_Priest+=['REV_290e']
class REV_290e:# <6>[1691]
	""" Atoned
	+2/+1. """
	#
	pass

if Rev_Pelagos:# 
	Rev_Priest+=['REV_781']
class REV_781:# <6>[1691]
	""" Pelagos
	{0} {1} {2} {3} """
	#
	pass

if Rev_Cathedral_of_Atonement:# 
	Rev_Priest+=['REV_791']
class REV_791:# <6>[1691]
	""" Cathedral of Atonement
	{0} {1} """
	#
	pass

