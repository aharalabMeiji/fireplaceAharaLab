from ..utils import *

BattleGrounds_Hero20=[
	'BG21_HERO_000','BG21_HERO_000e','BG21_HERO_000p','BG21_HERO_000pe','BG21_HERO_000p2','BG21_HERO_000p3','BG21_HERO_000_Buddy','BG21_HERO_000_Buddy_e','BG21_HERO_000_Buddy_G','BG21_HERO_000_Buddy_G_e',#Cariel Roame
	'BG21_HERO_010','BG21_HERO_010p','BG21_HERO_010_Buddy','BG21_HERO_010_Buddy_G',#Scabbs Cutterbutter
	]

BG21_Heroes=[
	'BG21_HERO_000','BG21_HERO_010',
	]

#### 000 ####
class BG21_HERO_000:# <5>[1453]
	""" Cariel Roame
	"""
	pass
class BG21_HERO_000e:
	"""Cariel Watcher
	"""
	pass
class BG21_HERO_000p:
	""" Conviction (Rank 1)
	Give a random friendly minion +1/+1. &lt;i&gt;(Upgrades at Tavern Tier 3.)&lt;/i&gt;"""
	play = Buff(RANDOM_FRIENDLY_MINION,'BG21_HERO_000pe')
	pass
BG21_HERO_000pe=buff(1,1)
class BG21_HERO_000p2:
	"""Conviction (Rank 2)
	Give three random friendly minions +1/+1. &lt;i&gt;(Upgrades at Tavern Tier 5.)&lt;/i&gt;"""
	play = Buff(RANDOM_FRIENDLY_MINION,'BG21_HERO_000pe') * 3
	pass
class BG21_HERO_000p3:
	"""Conviction (Rank 3)
	Give five random _friendly minions +1/+1."""
	play = Buff(RANDOM_FRIENDLY_MINION,'BG21_HERO_000pe') * 5
class BG21_HERO_000_Buddy:# <12>[1453]
	""" Captain Fairmount
	At the end of your turn, give five random friendly minions +1/+1. """
	events = OWN_TURN_END.on(Buff(RANDOM_FRIENDLY_MINION,'BG21_HERO_000_Buddy_e') * 5)
	pass
BG21_HERO_000_Buddy_e=buff(1,1)
class BG21_HERO_000_Buddy_G:# <12>[1453]
	""" Captain Fairmount
	At the end of your turn, give five random friendly minions +2/+2. """
	events = OWN_TURN_END.on(Buff(RANDOM_FRIENDLY_MINION,'BG21_HERO_000_Buddy_G_e') * 5)
	pass
BG21_HERO_000_Buddy_G_e=buff(2,2)

#### 010 ####
class BG21_HERO_010:# <7>[1453]
	""" Scabbs Cutterbutter
	 """
	pass
class BG21_HERO_010p:# <7>[1453]
	""" I Spy
	[Discover] a plain copy of a minion from your next opponent's warband. """
	#play = GenericChoice(CONTROLLER, RANDOM(NEXT_OPPONENT) * 3)
	pass
class BG21_HERO_010_Buddy:# <12>[1453]
	""" Warden Thelwater
	At the start of your turn, add your next opponent's Buddy to your hand. """
	#events = OWN_TURN_BEGIN.on(Give(CONTROLLER, ID(NEXT_OPPONENT_BUDDY)))
	pass
class BG21_HERO_010_Buddy_G:# <12>[1453]
	""" Warden Thelwater
	At the start of your turn, add 2 of your next opponent's Buddy to your hand. """
	#events = OWN_TURN_BEGIN.on(Give(CONTROLLER, ID(NEXT_OPPONENT_BUDDY))*2)
	pass

class BG21_HERO_020:# <12>[1453]
	""" Cookie the Cook
	 """
	pass
class BG21_HERO_020p:# <12>[1453]
	""" Stir the Pot
	Throw a minion in your pot. When you've gathered 3,[Discover] from their minion types. <i>(@ left!)</i> """
	#
	pass
class BG21_HERO_020_Buddy:# <12>[1453]
	""" Sous Chef
	You can use your Hero Power an extra time each_turn. """
	#
	pass
class BG21_HERO_020_Buddy_G:# <12>[1453]
	""" Sous Chef
	You can use your Hero Power 2 extra times each_turn. """
	#
	pass



class BG21_HERO_030:# <10>[1453]
	""" Sneed
	 """
	#
	pass
class BG21_HERO_030p:# <12>[1453]
	""" Sneed's Replicator
	Give a friendly minion:"[Deathrattle]: Summon a random minion of the same Tavern Tier." """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0,}
	play = Buff(TARGET,'BG21_HERO_030pe')
	pass
class BG21_HERO_030pe:# <12>[1453]
	""" Replicate
	[Deathrattle]: Summon a random minion of the same Tavern Tier. """
	pass
class BG21_HERO_030_Buddy:# <12>[1453]
	""" Piloted Whirl-O-Tron
	[Battlecry:] Copy a friendly minion's [Deathrattles]. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0,}
	play = Buff(SELF, 'BG21_HERO_030_Buddy_e') 
	pass
class BG21_HERO_030_Buddy_e:# <12>[1453]
	""" Whirling
	Copied [Deathrattles] from {0}. """
	tags={GameTag.DEATHRATTLE:True}
	deathrattle = Deathrattle(TARGET)
	pass
class BG21_HERO_030_Buddy_G:# <12>[1453]
	""" Piloted Whirl-O-Tron
	[Battlecry:] Copy a friendly minion's [Deathrattles] twice. """
	play = Buff(SELF, 'BG21_HERO_030_Buddy_e') * 2
	pass







