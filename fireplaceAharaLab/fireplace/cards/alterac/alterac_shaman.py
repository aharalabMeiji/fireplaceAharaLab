from ..utils import *

Alterac_Shaman=[]

Alterac_Glaciate=True
Alterac_Snowball_Fight=True
Alterac_Cheaty_Snobold=True
Alterac_Snowfall_Guardian=True
Alterac_Bearon_Glashear=True
Alterac_Brukan_of_the_Elements=True
Alterac_Frostbite=True
Alterac_Sleetbreaker=True
Alterac_Windchill=True
Alterac_Wildpaw_Cavern=True
Alterac_Dont_Stand_in_the_Fire=True
Alterac_Spirit_Mount=True
Alterac_Bracing_Cold=True


if Alterac_Glaciate:# 
	Alterac_Shaman+=['AV_107']
class AV_107:# <8>[1626]
	""" Glaciate
	[Discover] an 8-Cost minion. Summon and [Freeze] it. """
	#
	pass

if Alterac_Snowball_Fight:# 
	Alterac_Shaman+=['AV_250']
class AV_250:# <8>[1626]
	""" Snowball Fight!
	Deal $1 damage to a minion and [Freeze] it. If it survives, repeat this on another minion! """
	#
	pass

if Alterac_Cheaty_Snobold:# 
	Alterac_Shaman+=['AV_251']
class AV_251:# <8>[1626]
	""" Cheaty Snobold
	After an enemy is [Frozen], deal 3 damage to it. """
	#
	pass

if Alterac_Snowfall_Guardian:# 
	Alterac_Shaman+=['AV_255']

	Alterac_Shaman+=['AV_255e']
class AV_255:# <8>[1626]
	""" Snowfall Guardian
	[Battlecry:] [Freeze] all other minions. """
	#
	pass
class AV_255e:# <8>[1626]
	""" Chilled
	Increased stats. """
	#
	pass

if Alterac_Bearon_Glashear:# 
	Alterac_Shaman+=['AV_257']

	Alterac_Shaman+=['AV_257t']
class AV_257:# <8>[1626]
	""" Bearon Gla'shear
	[Battlecry:] For each Frost spell you've cast this game, summon a 3/4 Elemental that [Freezes].@ <i>(@)</i> """
	#
	pass
class AV_257t:# <8>[1626]
	""" Frozen Stagguard
	[Freeze] any character damaged by this minion. """
	#
	pass

if Alterac_Brukan_of_the_Elements:# 
	Alterac_Shaman+=['AV_258']
	Alterac_Shaman+=['AV_258p']
	Alterac_Shaman+=['AV_258p2']
	Alterac_Shaman+=['AV_258pt']
	Alterac_Shaman+=['AV_258pt3']
	Alterac_Shaman+=['AV_258pt4']
	Alterac_Shaman+=['AV_258pt7']
	Alterac_Shaman+=['AV_258t']
	Alterac_Shaman+=['AV_258t2']
	Alterac_Shaman+=['AV_258t3']
	Alterac_Shaman+=['AV_258t4']
	Alterac_Shaman+=['AV_258t6']
class AV_258:# <8>[1626]
	""" Bru'kan of the Elements
	[Battlecry:] Call upon the power of two Elements! """
	#
	pass
class AV_258p:# <8>[1626]
	""" Elemental Mastery
	[Hero Power] Call upon a different Element every turn! """
	#
	pass
class AV_258p2:# <8>[1626]
	""" Water Invocation
	[Hero Power] Restore #6 Health to all friendly characters. Swaps each turn. """
	#
	pass

class AV_258pt:# <8>[1626]
	""" Earth Invocation
	[Hero Power] Summon two 2/3 Elementals with [Taunt]. Swaps each turn. """
	#
	pass
class AV_258pt3:# <8>[1626]
	""" Fire Invocation
	[Hero Power] Deal $6 damage to the enemy hero. Swaps each turn. """
	#
	pass

class AV_258pt4:# <8>[1626]
	""" Lightning Invocation
	[Hero Power] Deal $2 damage to all enemy minions. Swaps each turn. """
	#
	pass
class AV_258pt7:# <8>[1626]
	""" Command the Elements
	[Hero Power] Call upon a different Element every turn! """
	#
	pass
class AV_258t:# <8>[1626]
	""" Earth Invocation
	Summon two 2/3 Elementals with [Taunt]. """
	#
	pass
class AV_258t2:# <8>[1626]
	""" Water Invocation
	Restore 6 Health to all friendly characters. """
	#
	pass
class AV_258t3:# <8>[1626]
	""" Fire Invocation
	Deal 6 damage to the enemy hero. """
	#
	pass
class AV_258t4:# <8>[1626]
	""" Lightning Invocation
	Deal 2 damage to all enemy minions. """
	#
	pass
class AV_258t6:# <8>[1626]
	""" Earthen Guardian
	[Taunt] """
	#
	pass

if Alterac_Frostbite:# 
	Alterac_Shaman+=['AV_259']
class AV_259:# <8>[1626]
	""" Frostbite
	Deal $3 damage. [Honorable Kill:] Your opponent's next spell costs (2) more. """
	#
	pass

if Alterac_Sleetbreaker:# 
	Alterac_Shaman+=['AV_260']
class AV_260:# <8>[1626]
	""" Sleetbreaker
	[Battlecry:] Add a Windchill to your hand. """
	#
	pass

if Alterac_Windchill:# 
	Alterac_Shaman+=['AV_266']
class AV_266:# <8>[1626]
	""" Windchill
	[Freeze] a minion. Draw a card. """
	#
	pass

if Alterac_Wildpaw_Cavern:# 
	Alterac_Shaman+=['AV_268']
class AV_268:# <8>[1626]
	""" Wildpaw Cavern
	At the end of your turn, summon a 3/4 Elemental that [Freezes]. Lasts 3 turns. """
	#
	pass

if Alterac_Dont_Stand_in_the_Fire:# 
	Alterac_Shaman+=['ONY_011']
class ONY_011:# <8>[1626]
	""" Don't Stand in the Fire!
	Deal $10 damage randomly split among all enemy minions. [Overload:] (1) """
	#
	pass

if Alterac_Spirit_Mount:# 
	Alterac_Shaman+=['ONY_012']
	Alterac_Shaman+=['ONY_012e']
	Alterac_Shaman+=['ONY_012t']
class ONY_012:# <8>[1626]
	""" Spirit Mount
	Give a minion +1/+2 and [Spell Damage +1]. When it dies, summon a Spirit Raptor. """
	#
	pass

class ONY_012e:# <8>[1626]
	""" With Da Spirits
	+1/+2 and [Spell Damage +1]. [Deathrattle:] Summon a Spirit Raptor. """
	#
	pass

class ONY_012t:# <8>[1626]
	""" Bru'kan's Raptor
	[Spell Damage +1] """
	#
	pass

if Alterac_Bracing_Cold:# 
	Alterac_Shaman+=['ONY_013']
	Alterac_Shaman+=['ONY_013e']
class ONY_013:# <8>[1626]
	""" Bracing Cold
	Restore #5 Health to your hero. Reduce the Cost of a random spell in your hand by (2). """
	#
	pass

class ONY_013e:# <8>[1626]
	""" Shivers
	Costs (2) less. """
	#
	pass

