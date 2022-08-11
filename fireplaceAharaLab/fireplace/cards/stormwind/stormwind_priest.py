
from ..utils import *

StormWind_Priest=[]

StormWind_Amulet_of_Undying=True  ###
StormWind_Defias_Leper=True  ###
StormWind_Copycat=True  ###
StormWind_Shadowcloth_Needle=True  ###
StormWind_Seek_Guidance=True  ###
StormWind_Call_of_the_Grave=True  ###
StormWind_Shard_of_the_Naaru=True  ###
StormWind_Void_Shard=True  ###
StormWind_Elekk_Mount=True  ###
StormWind_Twilight_Deceptor=True  ###
StormWind_Psyfiend=True  ###
StormWind_Voidtouched_Attendant=True  ###
StormWind_Darkbishop_Benedictus=True  ###


##################################


if StormWind_Amulet_of_Undying:# 
	StormWind_Priest+=['DED_512']
class DED_512:# <6>[1578]
	""" Amulet of Undying
	[Tradeable]Resurrect @ friendly[Deathrattle] |4(minion, minions).<i>(Upgrades when [Traded]!)</i> """
	#
	pass




if StormWind_Defias_Leper:# 
	StormWind_Priest+=['DED_513']
class DED_513:# <6>[1578]
	""" Defias Leper
	[Battlecry:] If you're holdinga Shadow spell, deal2 damage. """
	#
	pass




if StormWind_Copycat:# 
	StormWind_Priest+=['DED_514']
class DED_514:# <6>[1578]
	""" Copycat
	[Battlecry:] Add a copy of the next card your opponent plays to your hand. """
	#
	pass




if StormWind_Shadowcloth_Needle:# 
	StormWind_Priest+=['SW_012']
class SW_012:# <6>[1578]
	""" Shadowcloth Needle
	After you cast a Shadowspell, deal 1 damageto all enemies.Lose 1 Durability. """
	#
	pass




if StormWind_Seek_Guidance:# 
	StormWind_Priest+=['SW_433']
	StormWind_Priest+=['SW_433t']
	StormWind_Priest+=['SW_433t2']
	StormWind_Priest+=['SW_433t3']
	StormWind_Priest+=['SW_433t3a']
class SW_433:# <6>[1578]
	""" Seek Guidance
	[Questline:] Play a 2, 3,and 4-Cost card.[Reward:] [Discover] a cardfrom your deck. """
	#
	pass
class SW_433t:# <6>[1578]
	""" Discover the Void Shard
	[Questline:] Play a 5and 6-Cost card.[Reward:] [Discover] a cardfrom your deck. """
	#
	pass
class SW_433t2:# <6>[1578]
	""" Illuminate the Void
	[Questline:] Play a 7and 8-Cost card.[Reward:] Xyrella,the Sanctified. """
	#
	pass
class SW_433t3:# <6>[1578]
	""" Xyrella, the Sanctified
	[Taunt][Battlecry:] Shuffle thePurified Shard intoyour deck. """
	#
	pass
class SW_433t3a:# <6>[1578]
	""" Purified Shard
	Destroy the enemy hero. """
	#
	pass




if StormWind_Call_of_the_Grave:# 
	StormWind_Priest+=['SW_440']
class SW_440:# <6>[1578]
	""" Call of the Grave
	[Discover] a [Deathrattle]minion. If you haveenough Mana to play it,trigger its [Deathrattle]. """
	#
	pass




if StormWind_Shard_of_the_Naaru:# 
	StormWind_Priest+=['SW_441']
class SW_441:# <6>[1578]
	""" Shard of the Naaru
	[Tradeable][Silence] all enemy minions. """
	#
	pass




if StormWind_Void_Shard:# 
	StormWind_Priest+=['SW_442']
class SW_442:# <6>[1578]
	""" Void Shard
	[Lifesteal]Deal $4 damage. """
	#
	pass




if StormWind_Elekk_Mount:# 
	StormWind_Priest+=['SW_443']
	StormWind_Priest+=['SW_443e']
	StormWind_Priest+=['SW_443t']
class SW_443:# <6>[1578]
	""" Elekk Mount
	Give a minion +4/+7 and [Taunt]. When it dies, summon an Elekk. """
	#
	pass
class SW_443e:# <6>[1578]
	""" On an Elekk
	+4/+7 and [Taunt]. [Deathrattle:] Summon an Elekk. """
	#
	pass
class SW_443t:# <6>[1578]
	""" Xyrella's Elekk
	[Taunt] """
	#
	pass




if StormWind_Twilight_Deceptor:# 
	StormWind_Priest+=['SW_444']
class SW_444:# <6>[1578]
	""" Twilight Deceptor
	[Battlecry:] If any hero took damage this turn, draw a Shadow spell. """
	#
	pass




if StormWind_Psyfiend:# 
	StormWind_Priest+=['SW_445']
class SW_445:# <6>[1578]
	""" Psyfiend
	After you cast a Shadow spell, deal 2 damage to each hero. """
	#
	pass




if StormWind_Voidtouched_Attendant:# 
	StormWind_Priest+=['SW_446']
	StormWind_Priest+=['SW_446e']
class SW_446:# <6>[1578]
	""" Voidtouched Attendant
	Both heroes take one extra damage from all sources. """
	#
	pass
class SW_446e:# <6>[1578]
	""" Voidtouched
	Both heroes take one extra damage from all sources. """
	#
	pass




if StormWind_Darkbishop_Benedictus:# 
	StormWind_Priest+=['SW_448']
class SW_448:# <6>[1578]
	""" Darkbishop Benedictus
	[Start of Game:] If the spells in your deck are all Shadow, enter Shadowform. """
	#
	pass

#####################################
