
from ..utils import *

Barrens_Shaman=[]

Barrens_South_Coast_Chieftain=True  ###
Barrens_Nofin_Can_Stop_Us=True  ###
Barrens_Tinyfins_Caravan=True  ###
Barrens_Chain_Lightning_Rank_1=True  ###
Barrens_Arid_Stormer=True  ###
Barrens_Brukan=True  ###
Barrens_Earth_Revenant=True  ###
Barrens_Spawnpool_Forager=True  ###
Barrens_Lilypad_Lurker=True  ###
Barrens_Firemancer_Flurgl=True  ###
Barrens_Primal_Dungeoneer=True  ###
Barrens_Perpetual_Flame=True  ###
Barrens_Wailing_Vapor=True  ###


#########################################

if Barrens_South_Coast_Chieftain:# 
	Barrens_Shaman+=['BAR_040']
class BAR_040:# <8>[1525]
	""" South Coast Chieftain
	[Battlecry:] If you control another Murloc, deal 2_damage. """
	#
	pass




if Barrens_Nofin_Can_Stop_Us:# 
	Barrens_Shaman+=['BAR_041']
class BAR_041:# <8>[1525]
	""" Nofin Can Stop Us
	Give your minions+1/+1. Give yourMurlocs an extra +1/+1. """
	#
	pass




if Barrens_Tinyfins_Caravan:# 
	Barrens_Shaman+=['BAR_043']
class BAR_043:# <8>[1525]
	""" Tinyfin's Caravan
	At the start of your turn, draw a Murloc. """
	#
	pass




if Barrens_Chain_Lightning_Rank_1:# 
	Barrens_Shaman+=['BAR_044']
	Barrens_Shaman+=['BAR_044t']
	Barrens_Shaman+=['BAR_044t2']
class BAR_044:# <8>[1525]
	""" Chain Lightning Rank 1
	Deal $2 damage to a minion and a random adjacent one. <i>Upgrades when you have 5 Mana.</i> """
	#
	pass
class BAR_044t:# <8>[1525]
	""" Chain Lightning Rank 2
	Deal $3 damage to a minion and a random adjacent one. <i>Upgrades when you have 10 Mana.</i> """
	#
	pass
class BAR_044t2:# <8>[1525]
	""" Chain Lightning Rank 3
	Deal $4 damage to a minion and a random adjacent one. """
	#
	pass




if Barrens_Arid_Stormer:# 
	Barrens_Shaman+=['BAR_045']
class BAR_045:# <8>[1525]
	""" Arid Stormer
	[Battlecry:] If you played an Elemental last turn, gain [Rush] and [Windfury]. """
	#
	pass




if Barrens_Brukan:# 
	Barrens_Shaman+=['BAR_048']
class BAR_048:# <8>[1525]
	""" Bru'kan
	[Nature Spell Damage +3] """
	#
	pass




if Barrens_Earth_Revenant:# 
	Barrens_Shaman+=['BAR_750']
class BAR_750:# <8>[1525]
	""" Earth Revenant
	[Taunt] [Battlecry:] Deal 1 damageto all enemy minions. """
	#
	pass




if Barrens_Spawnpool_Forager:# 
	Barrens_Shaman+=['BAR_751']
	Barrens_Shaman+=['BAR_751t']
class BAR_751:# <8>[1525]
	""" Spawnpool Forager
	[Deathrattle:] Summon a 1/1 Tinyfin. """
	#
	pass
class BAR_751t:# <8>[1525]
	""" Diremuck Tinyfin
	 """
	#
	pass




if Barrens_Lilypad_Lurker:# 
	Barrens_Shaman+=['BAR_848']
class BAR_848:# <8>[1525]
	""" Lilypad Lurker
	[Battlecry:] If you played anElemental last turn, transforman enemy minion into a0/1 Frog with [Taunt]. """
	#
	pass




if Barrens_Firemancer_Flurgl:# 
	Barrens_Shaman+=['BAR_860']
class BAR_860:# <8>[1525]
	""" Firemancer Flurgl
	After you play a Murloc,deal 1 damage toall enemies. """
	#
	pass




if Barrens_Primal_Dungeoneer:# 
	Barrens_Shaman+=['WC_005']
class WC_005:# <8>[1525]
	""" Primal Dungeoneer
	[Battlecry:] Draw a spell.If it's a Nature spell, alsodraw an Elemental. """
	#
	pass




if Barrens_Perpetual_Flame:# 
	Barrens_Shaman+=['WC_020']
class WC_020:# <8>[1525]
	""" Perpetual Flame
	Deal $3 damage to a random enemy minion. If it dies, recast this. [Overload:] 1 """
	#
	pass




if Barrens_Wailing_Vapor:# 
	Barrens_Shaman+=['WC_042']
	Barrens_Shaman+=['WC_042e']
class WC_042:# <8>[1525]
	""" Wailing Vapor
	After you play an Elemental,gain +1 Attack. """
	#
	pass
class WC_042e:# <8>[1525]
	""" Rising Gas
	+1 Attack. """
	#
	pass


