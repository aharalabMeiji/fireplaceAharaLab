from ..utils import *

BG_Minion_Quilboar=[
	'BG20_100','BG20_100_G',#Razorfen Geomancer	1
	'BG20_301','BG20_301_G',#Sun-Bacon Relaxer	1
	'BG20_101','BG20_101_G',#Roadboar	2
	'BG20_102','BG20_102e','BG20_102_G','BG20_102_Ge',#Tough Tusk	2
	'BG20_201','BG20_201_G',#Bannerboar	3
	'BG20_103','BG20_103_G',#Bristleback Brute	3
	'BG21_037','BG21_037_G',#Gemsplitter	3
	'BG20_105','BG20_105_G',#Thorncaller	3
	'BG20_104','BG20_104_G',#Bonker	4
	'BG20_207','BG20_207e','BG20_207_G','BG20_207_Ge',#Dynamic Duo	4
	'BG20_106','BG20_106e','BG20_106_G',#Groundshaker	4
	'BG20_202','BG20_202_G',#Necrolyte	4
	'BG20_302','BG20_302e','BG20_302_G','BG20_302_Ge',#Aggem Thorncurse	5
	'BG20_206','BG20_206_G',#Captain Flat Tusk	6
	'BG20_303','BG20_303_G',#Charlga	6
	]

BG_PoolSet_Quilboar=[
	['BG20_100','BG20_301',],
	['BG20_101','BG20_102',],
	['BG20_201','BG20_103','BG21_037','BG20_105',],
	['BG20_104','BG20_207','BG20_106','BG20_202',],
	['BG20_302',],
	['BG20_206','BG20_303',],
	]

BG_Quilboar_Gold={
	'BG20_100':'BG20_100_G',#Razorfen Geomancer	1
	'BG20_301':'BG20_301_G',#Sun-Bacon Relaxer	1
	'BG20_101':'BG20_101_G',#Roadboar	2
	'BG20_102':'BG20_102_G',#Tough Tusk	2
	'BG20_201':'BG20_201_G',#Bannerboar	3
	'BG20_103':'BG20_103_G',#Bristleback Brute	3
	'BG21_037':'BG21_037_G',#Gemsplitter	3
	'BG20_105':'BG20_105_G',#Thorncaller	3
	'BG20_104':'BG20_104_G',#Bonker	4
	'BG20_207':'BG20_207_G',#Dynamic Duo	4
	'BG20_106':'BG20_106_G',#Groundshaker	4
	'BG20_202':'BG20_202_G',#Necrolyte	4
	'BG20_302':'BG20_302_G',#Aggem Thorncurse	5
	'BG20_206':'BG20_206_G',#Captain Flat Tusk	6
	'BG20_303':'BG20_303_G',#Charlga	6	
	}

#Razorfen Geomancer	1
class BG20_100:# <12>[1453]
	""" Razorfen Geomancer
	[Battlecry:] Gain a[Blood Gem]. """
	#
	pass
class BG20_100_G:# <12>[1453]
	""" Razorfen Geomancer
	[Battlecry:] Gain 2[Blood Gems]. """
	#
	pass

#Sun-Bacon Relaxer	1
class BG20_301:# <12>[1453]
	""" Sun-Bacon Relaxer
	When you sell this, gain 2_[Blood Gems]. """
	#
	pass

class BG20_301_G:# <12>[1453]
	""" Sun-Bacon Relaxer
	When you sell this, gain 4_[Blood Gems]. """
	#
	pass

#Roadboar	2
class BG20_101:# <12>[1453]
	""" Roadboar
	[Frenzy:] Gain a [Blood Gem]. """
	#
	pass

class BG20_101_G:# <12>[1453]
	""" Roadboar
	[Frenzy:] Gain 2 [Blood Gems]. """
	#
	pass

#Tough Tusk	2
class BG20_102:# <12>[1453]
	""" Tough Tusk
	After a [Blood Gem] is played on this, gain [Divine Shield] for the next combat. """
	#
	pass
class BG20_102e:# <12>[1453]
	""" Toughened
	[Divine Shield] next combat. """
	#
	pass
class BG20_102_G:# <12>[1453]
	""" Tough Tusk
	After a [Blood Gem] is played on this, gain[Divine Shield]. """
	#
	pass
class BG20_102_Ge:# <12>[1453]
	""" Real Tough
	[Divine Shield]. """
	#
	pass

#Bannerboar	3
class BG20_201:# <12>[1453]
	""" Bannerboar
	At the end of your turn, play a [Blood Gem] on adjacent Quilboar. """
	#
	pass

class BG20_201_G:# <12>[1453]
	""" Bannerboar
	At the end of your turn, play 2 [Blood Gems] on adjacent Quilboar. """
	#
	pass

#Bristleback Brute	3
class BG20_103:# <12>[1453]
	""" Bristleback Brute
	The first [Blood Gem] played on this each turn gives an extra +3/+3. """
	#
	pass

class BG20_103_G:# <12>[1453]
	""" Bristleback Brute
	The first [Blood Gem] played on this each turn gives an extra +6/+6. """
	#
	pass

#Gemsplitter	3
class BG21_037:# <12>[1453]
	""" Gemsplitter
	After a friendly minion loses [Divine Shield], gain a_[Blood Gem]. """
	#
	pass

class BG21_037_G:# <12>[1453]
	""" Gemsplitter
	After a friendly minion loses [Divine Shield], gain 2_[Blood Gems]. """
	#
	pass

#Thorncaller	3
class BG20_105:# <12>[1453]
	""" Thorncaller
	[Battlecry and Deathrattle:] Gain a [Blood Gem]. """
	#
	pass

class BG20_105_G:# <12>[1453]
	""" Thorncaller
	[Battlecry and Deathrattle:] Gain 2 [Blood Gems]. """
	#
	pass

#Bonker	4
class BG20_104:# <12>[1453]
	""" Bonker
	[Windfury]After this attacks, gain a [Blood Gem]. """
	#
	pass

class BG20_104_G:# <12>[1453]
	""" Bonker
	[Mega-Windfury]After this attacks, gain a [Blood Gem]. """
	#
	pass

#Dynamic Duo	4
class BG20_207:# <12>[1453]
	""" Dynamic Duo
	[[Taunt].] After a [Blood Gem]is played on anotherQuilboar, gain +1/+1. """
	#
	pass
class BG20_207e:# <12>[1453]
	""" Boar's Favor
	+1/+1. """
	#
	pass
class BG20_207_G:# <12>[1453]
	""" Dynamic Duo
	[[Taunt].] After a [Blood Gem]is played on anotherQuilboar, gain +2/+2. """
	#
	pass
class BG20_207_Ge:# <12>[1453]
	""" Boar's Favor
	+2/+2. """
	#
	pass

#Groundshaker	4
class BG20_106:# <12>[1453]
	""" Groundshaker
	After a [Blood Gem] is played on this, give your other minions +2 Attack for next combat only. """
	#
	pass
class BG20_106e:# <12>[1453]
	""" Groundshook
	+@ Attack. """
	#
	pass

class BG20_106_G:# <12>[1453]
	""" Groundshaker
	After a [Blood Gem] is played on this, give your other minions +4 Attack for next combat only. """
	#
	pass

#Necrolyte	4
class BG20_202:# <12>[1453]
	""" Necrolyte
	[Battlecry:] Play 2 [BloodGems] on a friendly minion.It steals all [Blood Gems]from its neighbors. """
	#
	pass

class BG20_202_G:# <12>[1453]
	""" Necrolyte
	[Battlecry:] Play 4 [BloodGems] on a friendly minion.It steals all [Blood Gems]from its neighbors. """
	#
	pass

#Aggem Thorncurse	5
class BG20_302:# <12>[1453]
	""" Aggem Thorncurse
	After a [Blood Gem] is played on this, give a friendly minion of each minion type +1/+1. """
	#
	pass
class BG20_302e:# <12>[1453]
	""" Thorncursed
	+1/+1 """
	#
	pass
class BG20_302_G:# <12>[1453]
	""" Aggem Thorncurse
	After a [Blood Gem] is played on this, give a friendly minion of each minion type +2/+2. """
	#
	pass
class BG20_302_Ge:# <12>[1453]
	""" Thorncursed
	+2/+2 """
	#
	pass


#Captain Flat Tusk	6
class BG20_206:# <12>[1453]
	""" Captain Flat Tusk
	After you spend 4 Gold, gain a [Blood Gem].<i>(@ Gold left!)</i> """
	#
	pass
class BG20_206_G:# <12>[1453]
	""" Captain Flat Tusk
	After you spend 4 Gold,gain 2 [Blood Gems].<i>(@ Gold left!)</i> """
	#
	pass

#Charlga	6
class BG20_303:# <12>[1453]
	""" Charlga
	At the end of your turn, play a [Blood Gem] on all friendly minions. """
	#
	pass

class BG20_303_G:# <12>[1453]
	""" Charlga
	At the end of your turn, play 2 [Blood Gems] on all friendly minions. """
	#
	pass

