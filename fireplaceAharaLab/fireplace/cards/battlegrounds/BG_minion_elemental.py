
from ..utils import *

BG_Minion_Elemental =[
	'BGS_116','TB_BaconUps_167',#Refreshing Anomaly(1)
	'BGS_115','BGS_115t','TB_BaconUps_156',#Sellemental(1)
	'BGS_127','TB_Baconups_202',#Molten Rock(2)
	'BGS_120','TB_BaconUps_160',#Party Elemental(2)
	'BGS_119','TB_BaconUps_159',#Crackling Cyclone(3)
	'BG21_021','BG21_021e','BG21_021_G',#Smogger(3)
	'BGS_122','TB_BaconUps_161',#Stasis Elemental(3)
	'BG21_020','BG21_020e','BG21_020pe','BG21_020_G',#Dazzling Lightspawn(4)
	'BG21_040','BG21_040_G',#Recycling Wraith(4)
	'BGS_126','TB_BaconUps_166',#Wildfire Elemental(4)
	'BGS_123','TB_BaconUps_162',#Tavern Tempest(5)
	'BGS_121','TB_BaconUps_165',#Gentle Djinni(6)
	'BGS_100','TB_BaconUps_200',#Lil' Rag (6)
]

BG_PoolSet_Elemental=[
	['BGS_116','BGS_115',],
	['BGS_127','BGS_120',],
	['BGS_119','BG21_021','BGS_122',],
	['BG21_020','BG21_040','BGS_126',],
	['BGS_123',],
	['BGS_121','BGS_100',],
	]

BG_Elemental_Gold={
	'BGS_116':'TB_BaconUps_167',#Refreshing Anomaly(1)
	'BGS_115':'TB_BaconUps_156',#Sellemental(1)
	'BGS_127':'TB_Baconups_202',#Molten Rock(2)
	'BGS_120':'TB_BaconUps_160',#Party Elemental(2)
	'BGS_119':'TB_BaconUps_159',#Crackling Cyclone(3)
	'BG21_021':'BG21_021_G',#Smogger(3)
	'BGS_122':'TB_BaconUps_161',#Stasis Elemental(3)
	'BG21_020':'BG21_020_G',#Dazzling Lightspawn(4)
	'BG21_040':'BG21_040_G',#Recycling Wraith(4)
	'BGS_126':'TB_BaconUps_166',#Wildfire Elemental(4)
	'BGS_123':'TB_BaconUps_162',#Tavern Tempest(5)
	'BGS_121':'TB_BaconUps_165',#Gentle Djinni(6)
	'BGS_100':'TB_BaconUps_200',#Lil' Rag (6)
	}

#Refreshing Anomaly(1)
class BGS_116:# <12>[1453]
	""" Refreshing Anomaly
	[Battlecry:] Your next[Refresh] costs (0). """
	#
	pass
class TB_BaconUps_167:# <12>[1453]
	""" Refreshing Anomaly
	[Battlecry:] Your next two [Refreshes] cost (0). """
	#
	pass

#Sellemental(1)
class BGS_115:# <12>[1453]
	""" Sellemental
	When you sell this,add a 2/2 Elementalto your hand. """
	#
	pass
class BGS_115t:# <12>[1453]
	""" Water Droplet
	 """
	#
	pass
class TB_BaconUps_156:# <12>[1453]
	""" Sellemental
	When you sell this,add two 2/2 Elementalsto your hand. """
	#
	pass

#Molten Rock(2)
class BGS_127:# <12>[1453]
	""" Molten Rock
	[Taunt]. After you play an Elemental, gain +1 Health. """
	#
	pass
class TB_Baconups_202:# <12>[1453]
	""" Molten Rock
	[Taunt]. After you play an Elemental, gain +2 Health. """
	#
	pass

#Party Elemental(2)
class BGS_120:# <12>[1453]
	""" Party Elemental
	After you play an Elemental, give another random friendly Elemental +1/+1. """
	#
	pass
class TB_BaconUps_160:# <12>[1453]
	""" Party Elemental
	After you play an Elemental, give another random friendly Elemental +1/+1 twice. """
	#
	pass

#Crackling Cyclone(3)
class BGS_119:# <12>[1453]
	""" Crackling Cyclone
	[Divine Shield][Windfury] """
	#
	pass
class TB_BaconUps_159:# <12>[1453]
	""" Crackling Cyclone
	[Divine Shield][Mega-Windfury] """
	#
	pass

#Smogger(3)
class BG21_021:# <12>[1453]
	""" Smogger
	[Battlecry:] Give a friendly Elemental stats equal to your Tavern Tier. """
	#
	pass
class BG21_021e:# <12>[1453]
	""" Smogged
	Increased stats. """
	#
	pass

class BG21_021_G:# <12>[1453]
	""" Smogger
	[Battlecry:] Give a friendlyElemental stats equal to_your Tavern Tier twice. """
	#
	pass

#Stasis Elemental(3)
class BGS_122:# <12>[1453]
	""" Stasis Elemental
	[Battlecry:] Add another random Elemental to Bob's Tavern and [Freeze] it. """
	#
	pass
class TB_BaconUps_161:# <12>[1453]
	""" Stasis Elemental
	[Battlecry:] Add two other random Elementals to Bob's Tavern and [Freeze] them. """
	#
	pass

#Dazzling Lightspawn(4)
class BG21_020:# <12>[1453]
	""" Dazzling Lightspawn
	[Avenge (2):] Elementals inBob's Tavern have +1/+1__for the rest of the game. """
	#
	pass
class BG21_020e:# <12>[1453]
	""" Dazzled
	Increased stats. """
	#
	pass

class BG21_020pe:# <12>[1453]
	""" Dazzling Lightspawn Player Enchant
	Increased stats. """
	#
	pass
class BG21_020_G:# <12>[1453]
	""" Dazzling Lightspawn
	[Avenge (2):] Elementals inBob's Tavern have +2/+2__for the rest of the game. """
	#
	pass

#Recycling Wraith(4)
class BG21_040:# <12>[1453]
	""" Recycling Wraith
	After you play anElemental, your next[Refresh] costs (1) less. """
	#
	pass

class BG21_040_G:# <12>[1453]
	""" Recycling Wraith
	After you play anElemental, your next two[Refreshes] cost (1) less. """
	#
	pass

#Wildfire Elemental(4)
class BGS_126:# <12>[1453]
	""" Wildfire Elemental
	After this attacks and killsa minion, deal excess damage to a random adjacent minion. """
	#
	pass
class TB_BaconUps_166:# <12>[1453]
	""" Wildfire Elemental
	After this attacks and killsa minion, deal excess damage to both adjacent minions. """
	#
	pass

#Tavern Tempest(5)
class BGS_123:# <12>[1453]
	""" Tavern Tempest
	[Battlecry:] Add another random Elemental to your hand. """
	#
	pass
class TB_BaconUps_162:# <12>[1453]
	""" Tavern Tempest
	[Battlecry:] Add two other random Elementals to your hand. """
	#
	pass

#Gentle Djinni(6)
class BGS_121:# <12>[1453]
	""" Gentle Djinni
	[Taunt]. [Deathrattle:] Summon another random Elemental and add a copy of it to your hand. """
	#
	pass
class TB_BaconUps_165:# <12>[1453]
	""" Gentle Djinni
	[Taunt]. [Deathrattle:] Summon two other random Elementals and add copies of them to your hand. """
	#
	pass

#Lil' Rag (6)
class BGS_100:# <12>[1453]
	""" Lil' Rag
	After you play an Elemental,give a friendly minion statsequal to the Elemental'sTavern Tier. """
	#
	pass
class TB_BaconUps_200:# <12>[1453]
	""" Lil' Rag
	After you play an Elemental,give a friendly minion statsequal to the Elemental'sTavern Tier twice. """
	#
	pass













