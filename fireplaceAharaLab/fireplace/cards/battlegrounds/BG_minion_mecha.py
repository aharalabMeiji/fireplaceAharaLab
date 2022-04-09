from ..utils import *

BG_Minion_Mecha =[
	'ULD_217', 'ULD_217e','TB_BaconUps_250',	#Micro Mummy(1)
	'BG21_022','BG21_022_G',	#Pupbot(1)
	'EX1_556', 'skele21','TB_BaconUps_006','TB_BaconUps_006t',	#Harvest Golem(2)
	'BOT_606', 'TB_BaconUps_028',	#Kaboom Bot(2)
	'GVG_048','TB_BaconUps_066',	#Metaltooth Leaper(2)
	'BGS_071', 'TB_BaconUps_123',	#Deflect-o-Bot(3)
	'BOT_312', 'BOT_312e','TB_BaconUps_032','TB_BaconUps_032t',	#Replicating Menace(3)
	'GVG_055', 'TB_BaconUps_069',	#Screwjank Clunker(3)
	'BOT_911', 'TB_BaconUps_099',	#Annoy-o-Module(4)
	'BG21_024', 'BG21_024_G',	#Grease Bot(4)
	'BOT_537', 'BOT_537t','TB_BaconUps_039', 'TB_BaconUps_039t',	#Mechano-Eg'g(4)
	'BG21_023', 'BG21_023_G',	#Mechano-Tank(4)
	'BG20_401', 'BG20_401_G',	#Holy Mecherel(5)
	'GVG_113', 'TB_BaconUps_153',	#Foe Reaper 4000(6)
	'BG21_025',	'BG21_025_G',	#Omega Buster(6)
	]
BG_PoolSet_Mecha=[
	['ULD_217', 'BG21_022',],
	['EX1_556', 'BOT_606', 'GVG_048', ],
	['BGS_071', 'BOT_312', 'GVG_055', ],
	['BOT_911', 'BG21_024', 'BOT_537', 'BG21_023', ],
	['BG20_401', ],
	['GVG_113', 'BG21_025', ],
	]
BG_Mecha_Gold={
	'ULD_217':'TB_BaconUps_250',	#Micro Mummy(1)
	'BG21_022':'BG21_022_G',	#Pupbot(1)
	'EX1_556':'TB_BaconUps_006',	#Harvest Golem(2)
	'BOT_606':'TB_BaconUps_028',	#Kaboom Bot(2)
	'GVG_048':'TB_BaconUps_066',	#Metaltooth Leaper(2)
	'BGS_071':'TB_BaconUps_123',	#Deflect-o-Bot(3)
	'BOT_312':'TB_BaconUps_032',	#Replicating Menace(3)
	'GVG_055':'TB_BaconUps_069',	#Screwjank Clunker(3)
	'BOT_911':'TB_BaconUps_099',	#Annoy-o-Module(4)
	'BG21_024':'BG21_024_G',	#Grease Bot(4)
	'BOT_537':'TB_BaconUps_039',	#Mechano-Eg'g(4)
	'BG21_023':'BG21_023_G',	#Mechano-Tank(4)
	'BG20_401':'BG20_401_G',	#Holy Mecherel(5)
	'GVG_113':'TB_BaconUps_153',	#Foe Reaper 4000(6)
	'BG21_025':'BG21_025_G',	#Omega Buster(6)
	}

#Micro Mummy(1)
class ULD_217:
	"""
	&lt;b&gt;Reborn&lt;/b&gt;At the end of your turn, giveanother random friendlyminion +1 Attack."""
	pass
ULD_217e=buff(1,0)
class TB_BaconUps_250:# <5>[1453]
	""" Micro Mummy
	[Reborn]At the end of your turn, giveanother random friendlyminion +2 Attack. """
	#
	pass

#Pupbot(1)
class BG21_022:# <12>[1453]
	""" Pupbot
	[Divine Shield] """
	#
	pass

class BG21_022_G:# <12>[1453]
	""" Pupbot
	[Divine Shield] """
	#
	pass

#Harvest Golem(2)
class EX1_556:
	"""
	&lt;b&gt;Deathrattle:&lt;/b&gt; Summon a 2/1 Damaged Golem."""
	pass
class skele21:
	"""
	"""
class TB_BaconUps_006:# <12>[1453]
	""" Harvest Golem
	[Deathrattle:] Summon a 4/2 Damaged Golem. """
	#
	pass

class TB_BaconUps_006t:# <12>[1453]
	""" Damaged Golem
	 """
	#
	pass

#Kaboom Bot(2)
class BOT_606:
	"""
	&lt;b&gt;Deathrattle:&lt;/b&gt; Deal 4_damage to a random enemy minion. """
	pass
class TB_BaconUps_028:# <12>[1453]
	""" Kaboom Bot
	[Deathrattle:] Deal 4_damage to a random enemy minion twice. """
	#
	pass

#Metaltooth Leaper(2)
class GVG_048:
	"""
	&lt;b&gt;Battlecry:&lt;/b&gt; Give your other Mechs +2 Attack."""
class TB_BaconUps_066:# <3>[1453]
	""" Metaltooth Leaper
	[Battlecry:] Give your other Mechs +4 Attack. """
	#
	pass

#Deflect-o-Bot(3)
class BGS_071:# <12>[1453]
	""" Deflect-o-Bot
	[Divine Shield]Whenever you summon a Mechduring combat, gain +2 Attackand [Divine Shield]. """
	#
	pass
class TB_BaconUps_123:# <12>[1453]
	""" Deflect-o-Bot
	[Divine Shield]Whenever you summon a Mechduring combat, gain +4 Attackand [Divine Shield]. """
	#
	pass

#Replicating Menace(3)
class BOT_312:
	"""Replicating Menace
	&lt;b&gt;Magnetic&lt;/b&gt;&lt;b&gt;Deathrattle:&lt;/b&gt; Summon three 1/1 Microbots."""
class BOT_312e:
	"""Replicating Menace
	"""
	pass
class TB_BaconUps_032:# <12>[1453]
	""" Replicating Menace
	[Magnetic][Deathrattle:] Summon three 2/2 Microbots. """
	#
	pass

class TB_BaconUps_032t:# <12>[1453]
	""" Microbot
	 """
	#
	pass

#Screwjank Clunker(3)
class GVG_055:
	""" Screwjank Clunker
	&lt;b&gt;Battlecry:&lt;/b&gt; Give a friendly Mech +2/+2 """
	pass
class TB_BaconUps_069:# <10>[1453]
	""" Screwjank Clunker
	[Battlecry:] Give a friendly Mech +4/+4. """
	#
	pass

#Annoy-o-Module(4)
class BOT_911:
	"""
	&lt;b&gt;Magnetic&lt;/b&gt;&lt;b&gt;Divine Shield&lt;/b&gt;&lt;b&gt;Taunt&lt;/b&gt;"""
	pass
class TB_BaconUps_099:# <5>[1453]
	""" Annoy-o-Module
	[Magnetic][Divine Shield][Taunt] """
	#
	pass

#Grease Bot(4)
class BG21_024:# <12>[1453]
	""" Grease Bot
	After a friendly minion loses [Divine Shield], give it +1/+1_permanently. """
	#
	pass

class BG21_024_G:# <12>[1453]
	""" Grease Bot
	After a friendly minion loses [Divine Shield], give it +2/+2_permanently. """
	#
	pass

#Mechano-Egg(4)
class BOT_537:
	"""
	&lt;b&gt;Deathrattle:&lt;/b&gt; Summon an 8/8 Robosaur."""
	pass
class BOT_537t:
	"""
	"""
	pass
class TB_BaconUps_039:# <5>[1453]
	""" Mechano-Egg
	[Deathrattle:] Summon a 16/16 Robosaur. """
	#
	pass
class TB_BaconUps_039t:
	""" Robosaur
	"""
#Mechano-Tank(4)
class BG21_023:# <12>[1453]
	""" Mechano-Tank
	[Avenge (2):] Deal 5 damage to the highest Health enemy minion. """
	#
	pass

class BG21_023_G:# <12>[1453]
	""" Mechano-Tank
	[Avenge (2):] Deal 5 damageto the highest Healthenemy minion twice. """
	#
	pass

#Holy Mecherel(5)
class BG20_401:# <12>[1453]
	""" Holy Mecherel
	After another friendly minion loses [Divine Shield], gain [Divine Shield]. """
	#
	pass

class BG20_401_G:# <12>[1453]
	""" Holy Mecherel
	After another friendly minion loses [Divine Shield], gain [Divine Shield]. """
	#
	pass

#Foe Reaper 4000(6)
class GVG_113:
	""" Foe Reaper 4000
	Also damages the minions next to whomever it attacks. """
	pass
class TB_BaconUps_153:# <12>[1453]
	""" Foe Reaper 4000
	Also damages the minions next to whomever it attacks. """
	#
	pass

#Omega Buster(6)
class BG21_025:# <12>[1453]
	""" Omega Buster
	[Deathrattle:] Summon five 1/1 Microbots. For each that doesn't fit, give your Mechs +1/+1. """
	#
	pass

class BG21_025_G:# <12>[1453]
	""" Omega Buster
	[Deathrattle:] Summon five 2/2 Microbots. For each that doesn't fit, give your Mechs +2/+2. """
	#
	pass




