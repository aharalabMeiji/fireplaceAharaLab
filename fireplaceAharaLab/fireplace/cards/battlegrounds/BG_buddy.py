from ..utils import *

BattleGrounds_Buddy=[\
	'BG20_HERO_100_Buddy','BG20_HERO_100_Buddy_e','BG20_HERO_100_Buddy_G','BG20_HERO_100_Buddy_Ge',
					'BG20_HERO_101_Buddy','BG20_HERO_101_Buddy_G','BG20_HERO_102_Buddy','BG20_HERO_102_Buddy_G','BG20_HERO_103_Buddy','BG20_HERO_103_Buddy_G','BG20_HERO_201_Buddy','BG20_HERO_201_Buddy_G','BG20_HERO_202_Buddy','BG20_HERO_202_Buddy_G','BG20_HERO_242_Buddy','BG20_HERO_242_Buddy_G','BG20_HERO_280_Buddy','BG20_HERO_280_Buddy_G','BG20_HERO_282_Buddy','BG20_HERO_282_Buddy_G','BG20_HERO_283_Buddy','BG20_HERO_283_Buddy_G','BG20_HERO_301_Buddy','BG20_HERO_301_Buddy_G','BG20_HERO_666p_t0',\
	'BG21_HERO_000_Buddy','BG21_HERO_000_Buddy_G','BG21_HERO_010_Buddy','BG21_HERO_010_Buddy_G','BG21_HERO_020_Buddy','BG21_HERO_020_Buddy_G','BG21_HERO_030_Buddy','BG21_HERO_030_Buddy_G','BG22_001','BG22_001_G','BG22_001t2','BG22_001t2_G','BG22_202','BG22_202_G','BG22_401','BG22_401_G','BG22_404','BG22_404_G','BG22_HERO_000_Buddy','BG22_HERO_000_Buddy_G','BG22_HERO_001_Buddy','BG22_HERO_001_Buddy_G','BG22_HERO_001p_t1et','BG22_HERO_002_Buddy','BG22_HERO_002_Buddy_G','BG22_HERO_003_Buddy','BG22_HERO_003_Buddy_G','BG22_HERO_004_Buddy','BG22_HERO_004_Buddy_G','BG22_HERO_201_Buddy','BG22_HERO_201_Buddy_G','BG22_HERO_305_Buddy','BG22_HERO_305_Buddy_G','BG22_HERO_305t',
	]

class BG20_HERO_100_Buddy:# <12>[1453]
	""" Icesnarl the Mighty
	After a friendly minionkills an enemy, gain+1 Health permanently. """
	events = Attack(FRIENDLY_MINIONS, ENEMY_CHARACTERS).on(Buff(SELF, 'BG20_HERO_100_Buddy_e'))
	pass
BG20_HERO_100_Buddy_e=buff(0,1)# <12>[1453]
class BG20_HERO_100_Buddy_G:# <12>[1453]
	""" Icesnarl the Mighty
	After a friendly minionkills an enemy, gain+2 Health permanently. """
	events = Attack(FRIENDLY_MINIONS, ENEMY_CHARACTERS).on(Buff(SELF, 'BG20_HERO_100_Buddy_Ge'))
	pass
BG20_HERO_100_Buddy_Ge=buff(0,2)# <12>[1453]

class BG20_HERO_101_Buddy:# <12>[1453]
	""" Baby Elekk
	After you play a minion with Attack equal to its Health, gain +2/+2. """
	#
	pass

class BG20_HERO_101_Buddy_G:# <12>[1453]
	""" Baby Elekk
	After you play a minion with Attack equal to its Health, gain +4/+4. """
	#
	pass

class BG20_HERO_102_Buddy:# <12>[1453]
	""" Dranosh Saurfang
	'For the Horde!' also grants Health. """
	#
	pass

class BG20_HERO_102_Buddy_G:# <12>[1453]
	""" Dranosh Saurfang
	'For the Horde!' also grants Health twice. """
	#
	pass

class BG20_HERO_103_Buddy:# <12>[1453]
	""" Death's Head Sage
	After you gain a [Blood Gem], gain an extra one. """
	#
	pass

class BG20_HERO_103_Buddy_G:# <12>[1453]
	""" Death's Head Sage
	After you gain a [Blood Gem], gain two extra. """
	#
	pass

class BG20_HERO_201_Buddy:# <12>[1453]
	""" Master Gadrin
	At the end of your turn,the minion to the leftof this copies thisminion's Attack. """
	#
	pass

class BG20_HERO_201_Buddy_G:# <12>[1453]
	""" Master Gadrin
	At the end of your turn,adjacent minions copythis minion's Attack. """
	#
	pass

class BG20_HERO_202_Buddy:# <12>[1453]
	""" Lei Flamepaw
	'Power of the Storm' offers3 options instead of 2. """
	#
	pass

class BG20_HERO_202_Buddy_G:# <12>[1453]
	""" Lei Flamepaw
	'Power of the Storm' offers4 options instead of 2. """
	#
	pass

class BG20_HERO_242_Buddy:# <12>[1453]
	""" Baby Kodo
	[Battlecry: Refresh] Bob's Tavern with a minion of each Tavern Tier. """
	#
	pass

class BG20_HERO_242_Buddy_G:# <12>[1453]
	""" Baby Kodo
	[Battlecry: Refresh] Bob's Tavern with a minion of each Tavern Tier. """
	#
	pass

class BG20_HERO_280_Buddy:# <12>[1453]
	""" Living Nightmare
	After you buy a minion,minions in Bob's Tavernhave +1/+1 this turn. """
	#
	pass

class BG20_HERO_280_Buddy_G:# <12>[1453]
	""" Living Nightmare
	After you buy a minion,minions in Bob's Tavernhave +2/+2 this turn. """
	#
	pass

class BG20_HERO_282_Buddy:# <12>[1453]
	""" Monstrosity
	After a friendly minion dies, gain its Attack. """
	#
	pass

class BG20_HERO_282_Buddy_G:# <12>[1453]
	""" Monstrosity
	After a friendly minion dies, gain its Attack twice. """
	#
	pass

class BG20_HERO_283_Buddy:# <12>[1453]
	""" Flight Trainer
	At the end of your turn, progress your flightpath by_1 turn. """
	#
	pass

class BG20_HERO_283_Buddy_G:# <12>[1453]
	""" Flight Trainer
	At the end of your turn, progress your flightpath by_2 turns. """
	#
	pass

class BG20_HERO_301_Buddy:# <12>[1453]
	""" Nightmare Ectoplasm
	When you 'Devour' this, spit its stats onto 2 extra_minions. """
	#
	pass

class BG20_HERO_301_Buddy_G:# <12>[1453]
	""" Nightmare Ectoplasm
	When you 'Devour' this, spit its stats onto 4 extra_minions. """
	#
	pass

class BG20_HERO_666p_t0:# <10>[1453]
	""" Diablo, Lord of Terror
	[Deathrattle:] Give youropponent loot!<i>(If this survives, Diablogets 2 loot instead.)</i> """
	#
	pass

class BG21_HERO_000_Buddy:# <12>[1453]
	""" Captain Fairmount
	At the end of your turn, give five random friendly minions +1/+1. """
	#
	pass

class BG21_HERO_000_Buddy_G:# <12>[1453]
	""" Captain Fairmount
	At the end of your turn, give five random friendly minions +2/+2. """
	#
	pass

class BG21_HERO_010_Buddy:# <12>[1453]
	""" Warden Thelwater
	At the start of your turn,add your next opponent's Buddy to your hand. """
	#
	pass

class BG21_HERO_010_Buddy_G:# <12>[1453]
	""" Warden Thelwater
	At the start of your turn, add 2 of your next opponent's Buddy to your hand. """
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

class BG21_HERO_030_Buddy:# <12>[1453]
	""" Piloted Whirl-O-Tron
	[Battlecry:] Copy a friendly minion's [Deathrattles]. """
	#
	pass

class BG21_HERO_030_Buddy_G:# <12>[1453]
	""" Piloted Whirl-O-Tron
	[Battlecry:] Copy a friendly minion's [Deathrattles] twice. """
	#
	pass


class BG22_HERO_000_Buddy:# <12>[1453]
	""" Crabby
	After your Hero Power fires,give adjacent minions stats__equal to the damage dealt._ """
	#
	pass

class BG22_HERO_000_Buddy_G:# <12>[1453]
	""" Crabby
	After your Hero Power fires, give adjacent minions stats equal to twice the damage dealt. """
	#
	pass

class BG22_HERO_001_Buddy:# <12>[1453]
	""" Spirit Raptor
	After you call upon a newElement, this remembers it.[Deathrattle:] Call uponthose Elements. """
	#
	pass

class BG22_HERO_001_Buddy_G:# <12>[1453]
	""" Spirit Raptor
	After you call upon a newElement, this remembers it.[Deathrattle:] Call upon thoseElements twice. """
	#
	pass

class BG22_HERO_001p_t1et:# <12>[1453]
	""" Stone Elemental
	 """
	#
	pass

class BG22_HERO_002_Buddy:# <12>[1453]
	""" Frostwolf Lieutenant
	[Avenge (2):] Give your minions +1 Attack permanently. """
	#
	pass

class BG22_HERO_002_Buddy_G:# <12>[1453]
	""" Frostwolf Lieutenant
	[Avenge (2):] Give your minions +2 Attack permanently. """
	#
	pass

class BG22_HERO_003_Buddy:# <12>[1453]
	""" Stormpike Lieutenant
	[Avenge (2):] Give your minions +1 Health permanently. """
	#
	pass

class BG22_HERO_003_Buddy_G:# <12>[1453]
	""" Stormpike Lieutenant
	[Avenge (2):] Give your minions +2 Health permanently. """
	#
	pass

class BG22_HERO_004_Buddy:# <12>[1453]
	""" Varden's Aquarrior
	'Twice as Nice' also gives the copy stats equal to your Tavern Tier. """
	#
	pass

class BG22_HERO_004_Buddy_G:# <12>[1453]
	""" Varden's Aquarrior
	'Twice as Nice' also givesthe copy stats equal toyour Tavern Tier twice. """
	#
	pass

class BG22_HERO_201_Buddy:# <12>[1453]
	""" Submersible Chef
	[Battlecry:] Add a random Tier 1, 3, and 5 minion to your hand. """
	#
	pass

class BG22_HERO_201_Buddy_G:# <12>[1453]
	""" Submersible Chef
	[Battlecry:] Add a random Tier 1, 3, and 5 minion to your hand twice. """
	#
	pass

class BG22_HERO_305_Buddy:# <12>[1453]
	""" Many Whelps
	Whenever you summon a Whelp, gain +2/+2 permanently. """
	#
	pass

class BG22_HERO_305_Buddy_G:# <12>[1453]
	""" Many Whelps
	Whenever you summon a Whelp, gain +4/+4 permanently. """
	#
	pass

class BG22_HERO_305t:# <12>[1453]
	""" Onyxian Whelp
	 """
	#
	pass


