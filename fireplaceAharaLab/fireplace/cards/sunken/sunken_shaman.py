from ..utils import *

Sunken_Shaman=[]

Sunken_Tidelost_Burrower=True  ###
Sunken_Clownfish=True  ###
Sunken_Command_of_Neptulon=True  ###
Sunken_Wrathspine_Enchanter=True  ###
Sunken_Schooling=True  ###
Sunken_Piranha_Poacher=True  ###
Sunken_Radiance_of_Azshara=True  ###
Sunken_Scalding_Geyser=True  ###
Sunken_Glugg_the_Gulper=True  ###
Sunken_Coral_Keeper=True  ###
Sunken_Azsharan_Scroll=True  ###
Sunken_Anchored_Totem=True  ###
Sunken_Bioluminescence=True  ###

if Sunken_Tidelost_Burrower:# 
	Sunken_Shaman+=['TID_003']
	Sunken_Shaman+=['TID_003e2']
class TID_003:# <8>[1658]
	""" Tidelost Burrower
	[Battlecry:] [Dredge].If it's a Murloc, summon a 2/2 copy of it. """
	#
	pass

class TID_003e2:# <8>[1658]
	""" Revealed
	2/2. """
	#
	pass

if Sunken_Clownfish:# 
	Sunken_Shaman+=['TID_004']
	Sunken_Shaman+=['TID_004e']
	Sunken_Shaman+=['TID_004e2']
class TID_004:# <8>[1658]
	""" Clownfish
	[Battlecry:] Your next two Murlocs cost (2) less. """
	#
	pass

class TID_004e:# <8>[1658]
	""" Clownfish Car
	Your next two Murlocs cost (2) less. """
	#
	pass

class TID_004e2:# <8>[1658]
	""" Clownin' Around
	Costs (2) less. """
	#
	pass

if Sunken_Command_of_Neptulon:# 
	Sunken_Shaman+=['TID_005']
	Sunken_Shaman+=['TID_005t']
class TID_005:# <8>[1658]
	""" Command of Neptulon
	Summon two 5/4 Elementals with [Rush].[Overload:] (1) """
	#
	pass

class TID_005t:# <8>[1658]
	""" Water Revenant
	[Rush] """
	#
	pass

if Sunken_Wrathspine_Enchanter:# 
	Sunken_Shaman+=['TSC_630']
class TSC_630:# <8>[1658]
	""" Wrathspine Enchanter
	[Battlecry:] Cast a copy of a Fire, Frost, and Nature spell in your hand <i>(targets chosen randomly).</i> """
	#
	pass

if Sunken_Schooling:# 
	Sunken_Shaman+=['TSC_631']
class TSC_631:# <8>[1658]
	""" Schooling
	Add three 1/1 PiranhaSwarmers to your hand. """
	#
	pass

if Sunken_Piranha_Poacher:# 
	Sunken_Shaman+=['TSC_633']
class TSC_633:# <8>[1658]
	""" Piranha Poacher
	At the end of your turn,add a 1/1 Piranha Swarmer to your hand. """
	#
	pass

if Sunken_Radiance_of_Azshara:# 
	Sunken_Shaman+=['TSC_635']
	Sunken_Shaman+=['TSC_635e']
class TSC_635:# <8>[1658]
	""" Radiance of Azshara
	[Fire Spell Damage +2]Your Nature spells cost (1)less. After you cast a Frostspell, gain 3 Armor. """
	#
	pass

class TSC_635e:# <8>[1658]
	""" Kaldorei Strength
	Costs (1) less. """
	#
	pass

if Sunken_Scalding_Geyser:# 
	Sunken_Shaman+=['TSC_637']
class TSC_637:# <8>[1658]
	""" Scalding Geyser
	Deal $2 damage.[Dredge]. """
	#
	pass

if Sunken_Glugg_the_Gulper:# 
	Sunken_Shaman+=['TSC_639']
	Sunken_Shaman+=['TSC_639e']
	Sunken_Shaman+=['TSC_639e2']
	Sunken_Shaman+=['TSC_639t']
	Sunken_Shaman+=['TSC_639t2']
	Sunken_Shaman+=['TSC_639t3']
class TSC_639:# <8>[1658]
	""" Glugg the Gulper
	[Colossal +3] After a friendly minion dies,gain its original stats. """
	#
	pass

class TSC_639e:# <8>[1658]
	""" Gulped
	Increased stats. """
	#
	pass

class TSC_639e2:# <8>[1658]
	""" Gulped
	Increased stats. """
	#
	pass

class TSC_639t:# <8>[1658]
	""" Glugg's Tail
	[Taunt] """
	#
	pass

class TSC_639t2:# <8>[1658]
	""" Glugg's Tail
	[Taunt] """
	#
	pass

class TSC_639t3:# <8>[1658]
	""" Glugg's Tail
	[Taunt] """
	#
	pass

if Sunken_Coral_Keeper:# 
	Sunken_Shaman+=['TSC_648']
	Sunken_Shaman+=['TSC_648t']
class TSC_648:# <8>[1658]
	""" Coral Keeper
	[Battlecry:] Summon a3/3 Elemental for eachspell school you'vecast this game. """
	#
	pass

class TSC_648t:# <8>[1658]
	""" Coral Elemental
	 """
	#
	pass

if Sunken_Azsharan_Scroll:# 
	Sunken_Shaman+=['TSC_772']
	Sunken_Shaman+=['TSC_772t']
class TSC_772:# <8>[1658]
	""" Azsharan Scroll
	[Discover] a Fire, Frost or Nature spell. Put a 'Sunken Scroll' on the bottom of your deck. """
	#
	pass

class TSC_772t:# <8>[1658]
	""" Sunken Scroll
	Add a Fire, Frost, and Nature spell from your class to your hand. """
	#
	pass

if Sunken_Anchored_Totem:# 
	Sunken_Shaman+=['TSC_922']
	Sunken_Shaman+=['TSC_922e']
class TSC_922:# <8>[1658]
	""" Anchored Totem
	After you summon a 1-Cost minion, give it +2/+1. """
	#
	pass

class TSC_922e:# <8>[1658]
	""" Sink or Swim
	+2/+1 """
	#
	pass

if Sunken_Bioluminescence:# 
	Sunken_Shaman+=['TSC_923']
	Sunken_Shaman+=['TSC_923e']
class TSC_923:# <8>[1658]
	""" Bioluminescence
	Give your minions[Spell Damage +1]. """
	#
	pass

class TSC_923e:# <8>[1658]
	""" Bioluminescent
	[Spell Damage +1]. """
	#
	pass

