from ..utils import *

BG_Minion_Naga=['BG23_000','BG23_000_G',#Mini-Myrmidon(1)
				'BG23_001','BG23_001_G',#Snail Cavalry(2)
				'BG23_002','BG23_002_G',#Shell Collector(1)
				'BG23_003','BG23_003_G',#Critter Wrangler(5)
				'BG23_004','BG23_004_G',#Deep-Sea Angler (2)
				'BG23_005','BG23_005_G',#Stormscale Siren (3)
				'BG23_006','BG23_006_G',#Eelbound Archer (4)
				'BG23_007','BG23_007_G',#Waverider (4)
				'BG23_008','BG23_008_G',#Glowscale (5)
				'BG23_009','BG23_009_G',#Lava Lurker (2)
				'BG23_010','BG23_010_G',#Eventide Brute (4)
				'BG23_011','BG23_011_G',#Shoal Commander (3)
				'BG23_012','BG23_012_G',#Corrupted Myrmidon (5)
				'BG23_013','BG23_013_G',#Tidemistress Athissa (6)
				'BG23_014','BG23_014_G',#Pashmar the Vengeful (3)
				'BGS_200','TB_BaconUps_256',#Warden of Old (3)
				]


BG_PoolSet_Naga=[
	['BG23_000','BG23_002',],#1
	['BG23_001','BG23_004','BG23_009',],#2
	['BG23_005','BG23_011','BG23_014','BGS_200',],#3
	['BG23_006','BG23_007','BG23_010',],#4
	['BG23_003','BG23_008','BG23_012',],#5
	['BG23_013',],#6
]

BG_Naga_Gold={
	'BG23_000':'BG23_000_G',#
	'BG23_001':'BG23_001_G',#
	'BG23_002':'BG23_002_G',#
	'BG23_003':'BG23_003_G',#
	'BG23_004':'BG23_004_G',#
	'BG23_005':'BG23_005_G',#
	'BG23_006':'BG23_006_G',#
	'BG23_007':'BG23_007_G',#
	'BG23_008':'BG23_008_G',#
	'BG23_009':'BG23_009_G',#
	'BG23_010':'BG23_010_G',#
	'BG23_011':'BG23_011_G',#
	'BG23_012':'BG23_012_G',#
	'BG23_013':'BG23_013_G',#
	'BG23_014':'BG23_014_G',#
	'BGS_200':'TB_BaconUps_256',
}


class BG23_000:# <12>[1453]
	""" Mini-Myrmidon(1)
	[Spellcraft:] Give a minion +2 Attack until next turn. """
	#
	pass
BG23_000e=buff(2,0)
class BG23_000t:
	""" """
class BG23_000_G:# <12>[1453]
	""" Mini-Myrmidon
	[Spellcraft:] Give a minion +4 Attack until next turn. """
	#
	pass
BG23_000_Ge=buff(0,0)
class BG23_000_Gt:
	""" """


class BG23_001:# <12>[1453]
	""" Snail Cavalry(2)
	[Once per Turn:]After you cast a spell,gain +2_Health. """
	#
	pass
BG23_001e=buff(0,2)
class BG23_001_G:# <12>[1453]
	""" Snail Cavalry
	[Once per Turn:]After you cast a spell,gain +4_Health. """
	#
	pass
BG23_001_Ge=buff(0,4)




class BG23_002:# <12>[1453]
	""" Shell Collector(1)
	[Battlecry:] Add a Gold Coin to your hand. """
	#
	pass

class BG23_002_G:# <12>[1453]
	""" Shell Collector
	[Battlecry:] Add 2 Gold Coinsto your hand. """
	#
	pass




class BG23_003:# <12>[1453]
	""" Critter Wrangler(5)
	After you cast a [Spellcraft] spell on a minion,give it +2/+2. """
	#
	pass
BG23_003e=buff(2,2)
class BG23_003_G:# <12>[1453]
	""" Critter Wrangler
	After you cast a [Spellcraft] spell on a minion,give it +4/+4. """
	#
	pass
BG23_003_Ge=buff(4,4)



class BG23_004:# <12>[1453]
	""" Deep-Sea Angler (2)
	[Spellcraft:] Give a minion+3 Health and [Taunt]until next turn. """
	#
	pass
class BG23_004e:
	pass
class BG23_004t:
	pass
class BG23_004_G:# <12>[1453]
	""" Deep-Sea Angler
	[Spellcraft:] Give a minion+6 Health and [Taunt]until next turn. """
	#
	pass
class BG23_004_Ge:
	pass
class BG23_004_Gt:
	pass




class BG23_005:# <12>[1453]
	""" Stormscale Siren (3)
	At the end of your turn,your [Spellcraft] minionscast their spellson themselves. """
	#
	pass

class BG23_005_G:# <12>[1453]
	""" Stormscale Siren
	At the end of your turn,your [Spellcraft] minionscast their spells_on themselves twice. """
	#
	pass




class BG23_006:# <12>[1453]
	""" Eelbound Archer (4)
	[Spellcraft:] Give a minion +8_Attack until next turn. """
	#
	pass
class BG23_006e:
	pass
class BG23_006t:
	pass
class BG23_006_G:# <12>[1453]
	""" Eelbound Archer
	[Spellcraft:] Give a minion+16_Attack until next turn. """
	#
	pass
class BG23_006_Ge:
	pass
class BG23_006_Gt:
	pass




class BG23_007:# <12>[1453]
	""" Waverider (4)
	[Spellcraft:] Give a minion+1/+1 and [Windfury]until next turn. """
	#
	pass
class BG23_007e:
	pass
class BG23_007t:
	pass
class BG23_007_G:# <12>[1453]
	""" Waverider
	[Spellcraft:] Give a minion+2/+2 and [Windfury]until next turn. """
	#
	pass
class BG23_007_Ge:
	pass
class BG23_007_Gt:
	pass





class BG23_008:# <12>[1453]
	""" Glowscale (5)
	[Taunt][Spellcraft:] Give a minion [Divine Shield] until next turn. """
	#
	pass
class BG23_008e:
	pass
class BG23_008t:
	pass
class BG23_008_G:# <12>[1453]
	""" Glowscale
	[Taunt][Spellcraft:] Give a minion [Divine Shield] until next turn. """
	#
	pass
class BG23_008_Ge:
	pass
class BG23_008_Gt:
	pass




class BG23_009:# <12>[1453]
	""" Lava Lurker (2)
	The first [Spellcraft] spellcast on this each turnis permanent. """
	#
	pass
class BG23_009_G:# <12>[1453]
	""" Lava Lurker
	The first 2 [Spellcraft] spellscast on this each turnare permanent. """
	#
	pass




class BG23_010:# <12>[1453]
	""" Eventide Brute (4)
	After you cast a spell,gain +1/+1. """
	#
	pass
class BG23_010e:
	pass
class BG23_010_G:# <12>[1453]
	""" Eventide Brute
	After you cast a spell,gain +2/+2. """
	#
	pass
class BG23_010_Ge:
	pass
	



class BG23_011:# <12>[1453]
	""" Shoal Commander (3)
	[Spellcraft:] Give a minion+1/+1 for each friendlyNaga until next turn. """
	#
	pass
class BG23_011e:
	pass
class BG23_011t:
	pass
class BG23_011_G:# <12>[1453]
	""" Shoal Commander
	[Spellcraft:] Give a minion+2/+2 for each friendlyNaga until next turn. """
	#
	pass
class BG23_011_Ge:
	pass
class BG23_011_Gt:
	pass




class BG23_012:# <12>[1453]
	""" Corrupted Myrmidon (5)
	[Start of Combat:] Double this minion's stats. """
	#
	pass
class BG23_012e:
	pass
class BG23_012_G:# <12>[1453]
	""" Corrupted Myrmidon
	[Start of Combat:] Triplethis minion's stats. """
	#
	pass
class BG23_012_Ge:
	pass





class BG23_013:# <12>[1453]
	""" Tidemistress Athissa (6)
	After you cast a spell, give four friendly Naga +1/+1. """
	#
	pass
class BG23_013e:
	pass
class BG23_013_G:# <12>[1453]
	""" Tidemistress Athissa
	After you cast a spell, givefour friendly Naga +2/+2. """
	#
	pass
class BG23_013_Ge:
	pass




class BG23_014:# <12>[1453]
	""" Pashmar the Vengeful (3)
	[Avenge (3):] Get a[Spellcraft] spellof your Tier or lower. """
	#
	pass
class BG23_014_G:# <12>[1453]
	""" Pashmar the Vengeful
	[Avenge (3):] Get 2[Spellcraft] spellsof your Tier or lower. """
	#
	pass





class BGS_200:# <12>[1453]
	""" Warden of Old (3)
	[Deathrattle:] Add a Gold Coin to your hand. """
	#
	pass
class TB_BaconUps_256:# <12>[1453]
	""" Warden of Old
	[Deathrattle:] Add 2 Gold Coins to your hand. """
	#
	pass
