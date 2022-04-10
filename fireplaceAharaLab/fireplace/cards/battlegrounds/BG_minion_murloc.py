from ..utils import *

BG_Minion_Murloc =[
'UNG_073','TB_BaconUps_061',#Rockpool Hunter (1)
'BG22_401','BG22_401e','BG22_401_G','BG22_401_Ge',#Swampstriker (1)
'EX1_507','EX1_507e','TB_BaconUps_008','TB_BaconUps_008e',#Murloc Warleader (2)
'BG21_008','BG21_008e','BG21_008_G','BG21_008_Ge',#Saltscale Honcho (2)
'BG22_202','BG22_202_G',#Tad (2)
'EX1_103','EX1_103e','TB_BaconUps_064','TB_BaconUps_064e',#Coldlight Seer (3)
'BT_010','BT_010e','TB_BaconUps_124','TB_BaconUps_124e',#Felfin Navigator (3)
'BG21_010','BG21_010e','BG21_010_G','BG21_010_Ge',#Swolefin (3)
'BGS_020','TB_BaconUps_089',#Primalfin Lookout (4)
'BGS_030','BGS_030e','TB_BaconUps_100','TB_BaconUps_100e',#King Bagurgle (5)
'BG21_009','BG21_009e','BG21_009_G',#SI:Sefin (5)
	]

BG_PoolSet_Murloc=[
	['UNG_073','BG22_401', ],
	['EX1_507', 'BG21_008', 'BG22_202', ],
	['EX1_103', 'BT_010', 'BG21_010', ],
	['BGS_020',],
	['BGS_030', ],
	['BG21_009',],
	]
BG_Murloc_Gold={
	'UNG_073':'TB_BaconUps_061',#Rockpool Hunter (1)
	'BG22_401':'BG22_401_G',#Swampstriker (1)
	'EX1_507':'TB_BaconUps_008',#Murloc Warleader (2)
	'BG21_008':'BG21_008_G',#Saltscale Honcho (2)
	'BG22_202':'BG22_202_G',#Tad (2)
	'EX1_103':'TB_BaconUps_064',#Coldlight Seer (3)
	'BT_010':'TB_BaconUps_124',#Felfin Navigator (3)
	'BG21_010':'BG21_010_G',#Swolefin (3)
	'BGS_020':'TB_BaconUps_089',#Primalfin Lookout (4)
	'BGS_030':'TB_BaconUps_100',#King Bagurgle (5)
	'BG21_009':'BG21_009_G',#SI:Sefin (5)	
	}


#Rockpool Hunter (1)
class UNG_073:
	"""
	"""
	pass
class TB_BaconUps_061:# <12>[1453]
	""" Rockpool Hunter
	[Battlecry:] Give a friendly Murloc +2/+2. """
	#
	pass

#Swampstriker (1)
class BG22_401:# <12>[1453]
	""" Swampstriker
	After you summon a Murloc, gain +1 Attack. """
	#
	pass
BG22_401e=buff(1,0)
class BG22_401_G:# <12>[1453]
	""" Swampstriker
	After you summon a Murloc, gain +2 Attack. """
	#
	pass
BG22_401_Ge=buff(2,0)

#Murloc Warleader (2)
class EX1_507:
	"""
	"""
	pass
EX1_507e=buff(2,0)
class TB_BaconUps_008:# <12>[1453]
	""" Murloc Warleader
	Your other Murlocs have +4 Attack. """
	#
	pass
class TB_BaconUps_008e:# <12>[1453]
	""" Mrgglaargl!
	+4 Attack from Murloc Warleader. """
	#
	pass
#Saltscale Honcho (2)
class BG21_008:# <12>[1453]
	""" Saltscale Honcho
	After you play a Murloc, give two other friendly Murlocs +1 Health. """
	#
	pass
class BG21_008e:# <12>[1453]
	""" Salty
	+1 Health. """
	#
	pass
class BG21_008_G:# <12>[1453]
	""" Saltscale Honcho
	After you play a Murloc, give two other friendly Murlocs +2 Health. """
	#
	pass
class BG21_008_Ge:# <12>[1453]
	""" Extra Salty
	+2 Health. """
	#
	pass

#Tad (2)
class BG22_202:# <12>[1453]
	""" Tad
	When you sell this,add another randomMurloc to your hand. """
	#
	pass
class BG22_202_G:# <12>[1453]
	""" Tad
	When you sell this,add 2 other randomMurlocs to your hand. """
	#
	pass

#Coldlight Seer (3)
class EX1_103:
	"""
	"""
	pass
EX1_103e=buff(0,2)
class TB_BaconUps_064:# <12>[1453]
	""" Coldlight Seer
	[Battlecry:] Give your other Murlocs +4 Health. """
	#
	pass
TB_BaconUps_064e=buff(0,4)

#Felfin Navigator (3)
class BT_010:
	"""
	"""
BT_010e=buff(1,1)
class TB_BaconUps_124:# <12>[1453]
	""" Felfin Navigator
	[Battlecry:] Give your other Murlocs +2/+2. """
	#
	pass
TB_BaconUps_124e=buff(2,2)

#Swolefin (3)
class BG21_010:# <12>[1453]
	""" Swolefin
	[Battlecry:] Gain +2/+1 foreach other friendly Murloc. """
	#
	pass
class BG21_010e:# <12>[1453]
	""" Swole
	+2/+1. """
	#
	pass
class BG21_010_G:# <12>[1453]
	""" Swolefin
	[Battlecry:] Gain +4/+2 foreach other friendly Murloc. """
	#
	pass
class BG21_010_Ge:# <12>[1453]
	""" Swoler
	+4/+2. """
	#
	pass

#Primalfin Lookout (4)
class BGS_020:# <12>[1453]
	""" Primalfin Lookout
	[Battlecry:] If you control another Murloc, [Discover] a_Murloc. """
	#
	pass
class TB_BaconUps_089:# <12>[1453]
	""" Primalfin Lookout
	[Battlecry:] If you control another Murloc, [Discover] two_Murlocs. """
	#
	pass

#King Bagurgle (5)
class BGS_030:# <12>[1453]
	""" King Bagurgle
	[Battlecry and Deathrattle:] Give your other Murlocs +2/+2. """
	#
	pass
BGS_030e=buff(2,2)
class TB_BaconUps_100:# <12>[1453]
	""" King Bagurgle
	[Battlecry and Deathrattle:] Give your other Murlocs +4/+4. """
	#
	pass
TB_BaconUps_100=buff(4,4)

#SI:Sefin (5)
class BG21_009:# <12>[1453]
	""" SI:Sefin
	[Avenge (3):] Give a friendly Murloc [Poisonous] permanently. """
	#
	pass
BG21_009e=buff(poisonous=True)# <12>[1453]
""" SI:7 Training
[Poisonous] """
class BG21_009_G:# <12>[1453]
	""" SI:Sefin
	[Avenge (3):] Give 2 friendly Murlocs [Poisonous] permanently. """
	#
	pass


