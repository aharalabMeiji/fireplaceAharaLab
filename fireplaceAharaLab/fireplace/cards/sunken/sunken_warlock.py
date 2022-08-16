from ..utils import *

Sunken_Warlock=[]

Sunken_Herald_of_Shadows=True  ###
Sunken_Immolate=True  ###
Sunken_Commander_Ulthok=True  ###
Sunken_Azsharan_Scavenger=True  ###
Sunken_Voidgill=True  ###
Sunken_Bloodscent_Vilefin=True  ###
Sunken_Abyssal_Wave=True  ###
Sunken_Rock_Bottom=True  ###
Sunken_Sirakess_Cultist=True  ###
Sunken_Dragged_Below=True  ###
Sunken_Chum_Bucket=True  ###
Sunken_Zaqul=True  ###
Sunken_Gigafin=True  ###


if Sunken_Herald_of_Shadows:# 
	Sunken_Warlock+=['TID_717']
	Sunken_Warlock+=['TID_717e']
	Sunken_Warlock+=['TID_717e2']
	Sunken_Warlock+=['TID_717e2b']
	Sunken_Warlock+=['TID_717eb']
class TID_717:# <9>[1658]
	""" Herald of Shadows
	[Battlecry:] If you've cast a Shadow spell while holding this, steal 2 Health from a minion. """
	#
	pass
class TID_717e:# <9>[1658]
	""" Siphoned
	Reduced Health. """
	#
	pass
class TID_717e2:# <9>[1658]
	""" Shadow Siphon
	Increased Health. """
	#
	pass
class TID_717e2b:# <9>[1658]
	""" Siphoned
	Increased Health. """
	#
	pass
class TID_717eb:# <9>[1658]
	""" Siphoned
	Reduced Health. """
	#
	pass




if Sunken_Immolate:# 
	Sunken_Warlock+=['TID_718']
	Sunken_Warlock+=['TID_718e']
	Sunken_Warlock+=['TID_718e2']
class TID_718:# <9>[1658]
	""" Immolate
	Light every card in the opponent's hand on fire. In 3 turns, any stillin hand are destroyed! """
	#
	pass

class TID_718e:# <9>[1658]
	""" Engulfed in Flame
	In 3 turns, destroy the opponent's cards that are on fire. """
	#
	pass

class TID_718e2:# <9>[1658]
	""" Engulfed in Flame
	This card is on fire! """
	#
	pass

if Sunken_Commander_Ulthok:# 
	Sunken_Warlock+=['TID_719']
	Sunken_Warlock+=['TID_719e']
class TID_719:# <9>[1658]
	""" Commander Ulthok
	[Battlecry:] Your opponent's cards cost Health instead of Mana next turn. """
	#
	pass

class TID_719e:# <9>[1658]
	""" Blood Squeeze
	Your cards cost Health instead of Mana this turn. """
	#
	pass

if Sunken_Azsharan_Scavenger:# 
	Sunken_Warlock+=['TSC_039']
	Sunken_Warlock+=['TSC_039t']
	Sunken_Warlock+=['TSC_039te']
class TSC_039:# <9>[1658]
	""" Azsharan Scavenger
	[Battlecry:] Put a 'Sunken Scavenger' on the bottom of your deck. """
	#
	pass

class TSC_039t:# <9>[1658]
	""" Sunken Scavenger
	[Battlecry:] Give your other Murlocs +1/+1 <i>(wherever they are)</i>. """
	#
	pass

class TSC_039te:# <9>[1658]
	""" Mllgggrrrr
	+1/+1. """
	#
	pass

if Sunken_Voidgill:# 
	Sunken_Warlock+=['TSC_614']
	Sunken_Warlock+=['TSC_614e']
class TSC_614:# <9>[1658]
	""" Voidgill
	[Deathrattle:] Give all Murlocs in your hand +1/+1. """
	#
	pass

class TSC_614e:# <9>[1658]
	""" Void Powered
	+1/+1. """
	#
	pass

if Sunken_Bloodscent_Vilefin:# 
	Sunken_Warlock+=['TSC_753']
	Sunken_Warlock+=['TSC_753e']
class TSC_753:# <9>[1658]
	""" Bloodscent Vilefin
	[Battlecry:] [Dredge]. If it's aMurloc, change its Cost to_Health instead of Mana. """
	#
	pass

class TSC_753e:# <9>[1658]
	""" Fresh Scent
	Costs Health instead of Mana. """
	#
	pass

if Sunken_Abyssal_Wave:# 
	Sunken_Warlock+=['TSC_924']
class TSC_924:# <9>[1658]
	""" Abyssal Wave
	Deal $4 damage toall minions. Give youropponent an AbyssalCurse. """
	#
	pass

if Sunken_Rock_Bottom:# 
	Sunken_Warlock+=['TSC_925']
	Sunken_Warlock+=['TSC_925t']
class TSC_925:# <9>[1658]
	""" Rock Bottom
	Summon a 1/1Murloc, then [Dredge].If it's also a Murloc,summon one more. """
	#
	pass

class TSC_925t:# <9>[1658]
	""" Coldlight Lurker
	 """
	#
	pass

if Sunken_Sirakess_Cultist:# 
	Sunken_Warlock+=['TSC_955']
	Sunken_Warlock+=['TSC_955t']
class TSC_955:# <9>[1658]
	""" Sira'kess Cultist
	[Battlecry:] Giveyour opponent anAbyssal Curse. """
	#
	pass

class TSC_955t:# <9>[1658]
	""" Abyssal Curse
	At the start of your turn,take {0} damage. Each Curseis worse than the last.<i>({1} |4(turn,turns) remaining).</i> """
	#
	pass

if Sunken_Dragged_Below:# 
	Sunken_Warlock+=['TSC_956']
class TSC_956:# <9>[1658]
	""" Dragged Below
	Deal $4 damageto a minion.Give your opponentan Abyssal Curse. """
	#
	pass

if Sunken_Chum_Bucket:# 
	Sunken_Warlock+=['TSC_957']
	Sunken_Warlock+=['TSC_957e']
class TSC_957:# <9>[1658]
	""" Chum Bucket
	Give all Murlocs in yourhand +1/+1. Repeat foreach Murloc you control. """
	#
	pass

class TSC_957e:# <9>[1658]
	""" Empty Bucket
	+1/+1. """
	#
	pass

if Sunken_Zaqul:# 
	Sunken_Warlock+=['TSC_959']
	Sunken_Warlock+=['TSC_959e']
	Sunken_Warlock+=['TSC_959e2']
class TSC_959:# <9>[1658]
	""" Za'qul
	Your Abyssal Curses heal youfor the damage they deal.[Battlecry:] Give your opponentan Abyssal Curse. """
	#
	pass

class TSC_959e:# <9>[1658]
	""" Cursed
	Your Abyssal Curses heal youfor the damage they deal. """
	#
	pass

class TSC_959e2:# <9>[1658]
	""" Cursed
	Your Curses cost (2) more this game. """
	#
	pass

if Sunken_Gigafin:# 
	Sunken_Warlock+=['TSC_962']
	Sunken_Warlock+=['TSC_962e']
	Sunken_Warlock+=['TSC_962e2']
	Sunken_Warlock+=['TSC_962t']
class TSC_962:# <9>[1658]
	""" Gigafin
	[Colossal +1]. [Battlecry:]Devour all enemy minions.[Deathrattle:] Spit themback out. """
	#
	pass

class TSC_962e:# <9>[1658]
	""" Swallowed Whole
	Storing a Minion. """
	#
	pass

class TSC_962e2:# <9>[1658]
	""" Bloated
	Gigafin has eaten all enemy minions! """
	#
	pass
class TSC_962t:# <9>[1658]
	""" Gigafin's Maw
	[Taunt][Deathrattle:] Permanently destroy all minions inside Gigafin. """
	#
	pass

