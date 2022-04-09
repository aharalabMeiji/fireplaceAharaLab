

from ..utils import *

BG_Minion_Demon =[
	'BG21_029','EX1_598','BG21_029_G','TB_BaconUps_030t',#Icky Imp(1)
	'BG21_006','BG21_006e','BG21_006_G',#Impulsive Trickster(1)
	'BGS_001','TB_BaconUps_062',#Nathrezim Overseer(2)
	'BGS_014','TB_BaconUps_113',#Imprisoner(2)
	'BG21_039','BG21_039_G',#Kathra'natir(3)
	'BGS_059','TB_BaconUps_119',#Soul Devourer(3)
	'BGS_204','TB_BaconUps_304',#Bigfernal(4)
	'DMF_533','TB_BaconUps_309','TB_BaconUps_309t',#Ring Matron(4)
	'BG21_004','BG21_004e','BG21_004_G',#Insatiable Ur'zul(5)
	'BGS_010','TB_BaconUps_083',#Annihilan Battlemaster(5)
	'LOOT_368','TB_BaconUps_059','TB_BaconUps_059t',#Voidlord(5)
	'BG21_005','BG21_005e','BG21_005_G',#Famished Felbat(6)
	'BGS_044','TB_BaconUps_116',#Imp Mama(6)
	]

BG_PoolSet_Demon=[
	['BG21_029','BG21_006',],##1
	['BGS_001','BGS_014',],##2
	['BG21_039','BGS_059',],#3
	['BGS_204','DMF_533',],#4
	['BG21_004','BGS_010','LOOT_368'],#5
	['BG21_005','BGS_044',],#6
	]

BG_Demon_Gold={
	'BG21_029':'BG21_029_G',#Icky Imp(1)
	'BG21_006':'BG21_006_G',#Impulsive Trickster(1)
	'BGS_001':'TB_BaconUps_062',#Nathrezim Overseer(2)
	'BGS_014':'TB_BaconUps_113',#Imprisoner(2)
	'BG21_039':'BG21_039_G',#Kathra'natir(3)
	'BGS_059':'TB_BaconUps_119',#Soul Devourer(3)
	'BGS_204':'TB_BaconUps_304',#Bigfernal(4)
	'DMF_533':'TB_BaconUps_309',#Ring Matron(4)
	'BG21_004':'BG21_004_G',#Insatiable Ur'zul(5)
	'BGS_010':'TB_BaconUps_083',#Annihilan Battlemaster(5)
	'LOOT_368':'TB_BaconUps_059',#Voidlord(5)
	'BG21_005':'BG21_005_G',#Famished Felbat(6)
	'BGS_044':'TB_BaconUps_116',#Imp Mama(6)
	}

####################
class BG21_029:# <12>[1453]
	""" Icky Imp (1)
	[Deathrattle:] Summon two 1/1 Imps. """
	#
	pass
class EX1_598:#
	""" imp (1/1)
	"""
	pass
class BG21_029_G:# <12>[1453]
	""" Icky Imp
	[Deathrattle:] Summon two 2/2 Imps. """
	#
	pass
class TB_BaconUps_030t:#
	""" Imp (2/2)
	"""

####################
class BG21_006:# <12>[1453]
	""" Impulsive Trickster(1)
	[Deathrattle:] Give thisminion's maximum Health__to another friendly minion._ """
	#
	pass
class BG21_006e:# <12>[1453]
	""" Impulsive
	Increased Health. """
	#
	pass
class BG21_006_G:# <12>[1453]
	""" Impulsive Trickster
	[Deathrattle:] Give thisminion's maximum Healthto another friendly miniontwice. """
	#
	pass

####################
class BGS_001:# <12>[1453]
	""" Nathrezim Overseer (2)
	[Battlecry:] Give a friendly Demon +2/+2. """
	#
	pass
class TB_BaconUps_062:# <12>[1453]
	""" Nathrezim Overseer
	[Battlecry:] Give a friendly Demon +4/+4. """
	#
	pass

####################
class BGS_014:# <12>[1453]
	""" Imprisoner (2)
	[Taunt][Deathrattle:] Summon a 1/1 Imp. """
	#
	pass
class TB_BaconUps_113:# <12>[1453]
	""" Imprisoner
	[Taunt][Deathrattle:] Summon a 2/2 Imp. """
	#
	pass

####################
class BG21_039:# <12>[1453]
	""" Kathra'natir (3)
	Your other Demonshave +2 Attack.Your Hero is [Immune]. """
	#
	pass
class BG21_039_G:# <12>[1453]
	""" Kathra'natir
	Your other Demonshave +4 Attack.Your Hero is [Immune]. """
	#
	pass

####################
class BGS_059:# <12>[1453]
	""" Soul Devourer (3)
	[Battlecry:] Choose afriendly Demon. Removeit to gain its stats and3 Gold. """
	#
	pass
class TB_BaconUps_119:# <12>[1453]
	""" Soul Devourer
	[Battlecry:] Choose afriendly Demon. Removeit to gain double its statsand 6 Gold. """
	#
	pass

###################
class BGS_204:# <12>[1453]
	""" Bigfernal (4)
	After you summon a Demon, gain +1/+1 permanently. """
	#
	pass
class TB_BaconUps_304:# <12>[1453]
	""" Bigfernal
	After you summon a Demon, gain +2/+2 permanently. """
	#
	pass

###################
class DMF_533:# <9>[1453]
	""" Ring Matron (4)
	[Taunt][Deathrattle:] Summontwo 6/4 Imps. """
	#
	pass
class TB_BaconUps_309:# <9>[1453]
	""" Ring Matron
	[Taunt][Deathrattle:] Summontwo 6/4 Imps. """
	#
	pass
class TB_BaconUps_309t:# <9>[1453]
	""" Fiery Imp
	 """
	#
	pass


####################
class BG21_004:# <12>[1453]
	""" Insatiable Ur'zul (5)
	[[Taunt].] After you play aDemon, consume a minionin Bob's Tavern to gainits stats. """
	#
	pass
class BG21_004e:# <12>[1453]
	""" Sated
	Increased Stats """
	#
	pass
class BG21_004_G:# <12>[1453]
	""" Insatiable Ur'zul
	[[Taunt].] After you play aDemon, consume a minionin Bob's Tavern to gaindouble its stats. """
	#
	pass

####################
class BGS_010:# <12>[1453]
	""" Annihilan Battlemaster (5)
	[Battlecry:] Gain +1 Health for each Health your hero_is missing. """
	#
	pass
class TB_BaconUps_083:# <12>[1453]
	""" Annihilan Battlemaster
	[Battlecry:] Gain +2 Health for each Health your hero_is missing. """
	#
	pass

####################
class LOOT_368:# <9>[1453]
	""" Voidlord (5)
	[Taunt] [Deathrattle:] Summon three2/6 Demons with [Taunt]. """
	#
	pass
class TB_BaconUps_059:# <9>[1453]
	""" Voidlord
	[Taunt] [Deathrattle:] Summon three2/6 Demons with [Taunt]. """
	#
	pass
class TB_BaconUps_059t:# <9>[1453]
	""" Voidwalker
	[Taunt] """
	#
	pass

####################
class BG21_005:# <12>[1453]
	""" Famished Felbat (6)
	At the end of your turn, eachfriendly Demon consumes aminion in Bob's Tavern to__gain its stats. """
	#
	pass
class BG21_005e:# <12>[1453]
	""" Fed by the Felbat
	Consumed the stats of minion. """
	#
	pass
class BG21_005_G:# <12>[1453]
	""" Famished Felbat
	At the end of your turn, eachfriendly Demon consumes aminion in Bob's Tavern to__gain double its stats. """
	#
	pass

####################
class BGS_044:# <9>[1453]
	""" Imp Mama (6)
	Whenever this minion takesdamage, summon a randomDemon and give it [Taunt]. """
	#
	pass
class TB_BaconUps_116:# <9>[1453]
	""" Imp Mama
	Whenever this miniontakes damage, summon2 random Demons andgive them [Taunt]. """
	#
	pass

####################



