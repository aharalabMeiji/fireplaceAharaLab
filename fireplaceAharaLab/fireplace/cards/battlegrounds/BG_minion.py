
from ..utils import *

BG_Minion=[
	#Wrath Weaver	1	1	3	-	-
	'BGS_004','BGS_004e','TB_BaconUps_079','TB_BaconUps_079e',
	#Acolyte of C'Thun	2	2	3	-	Reborn
	'BGS_106','TB_BaconUps_255',
	#Menagerie Mug	2	2	2	-	Battlecry
	'BGS_082','BGS_082e','TB_BaconUps_144','TB_BaconUps_144e',
	#Prophet of the Boar	2	3	3	-	Blood Gem
	'BG20_203','BG20_203_G',
	#Selfless Hero	2	2	1	-	Deathrattle
	'OG_221','TB_BaconUps_014',
	#Spawn of N'Zoth	2	2	2	-	Deathrattle
	'OG_256','OG_256e','TB_BaconUps_025',
	#Unstable Ghoul	2	1	3	-	Deathrattle
	'FP1_024','TB_BaconUps_118',
	#Whelp Smuggler	2	2	5	-	-
	'BG21_013','BG21_013_G',
	#Arm of the Empire	3	4	4	-	Taunt
	'BGS_110','BGS_110e','TB_BaconUps_302','TB_BaconUps_302e',
	#Bird Buddy	3	2	4	-	Avenge (X)
	'BG21_002','BG21_002e','BG21_002_G','BG21_002_Ge',
	#Budding Greenthumb	3	1	4	-	Avenge (X)
	'BG21_030','BG21_030_G',
	#Houndmaster	3	4	3	-	Battlecry
	'DS1_070','DS1_070o','TB_BaconUps_068','TB_BaconUps_068e',
	#Khadgar	3	2	2	-	-
	'DAL_575','TB_BaconUps_034'
	#Soul Juggler	3	3	5	-	-
	'BGS_002','TB_BaconUps_075',
	#Champion of Y'Shaarj	4	4	4	-	Taunt
	'BGS_111','BGS_111e','TB_BaconUps_301','TB_BaconUps_301e',
	#Defender of Argus	4	3	3	-	Battlecry
	'CORE_EX1_093','EX1_093e','TB_BaconUps_009','TB_BaconUps_009e',
	#Impatient Doomsayer	4	2	6	-	Avenge (X)
	'BG21_007','BG21_007_G',
	#Majordomo Executus	4	6	3	-	-
	'BGS_105','BGS_105e','TB_BaconUps_207',
	#Menagerie Jug	4	3	3	-	Battlecry
	'BGS_083','BGS_083e','TB_BaconUps_145','TB_BaconUps_145e',
	#Strongshell Scavenger	4	2	3	-	Battlecry
	'ICC_807',  'ICC_807e',  'TB_BaconUps_072', 'TB_BaconUps_072e',
	#Witchwing Nestmatron	4	3	5	-	Avenge (X)
	'BG21_038','BG21_038_G',
	#Baron Rivendare	5	1	7	-	Deathrattle
	'CORE_FP1_031','TB_BaconUps_055',
	#Brann Bronzebeard	5	2	4	-	Battlecry
	'LOE_077','LOE_077e','TB_BaconUps_045','TB_BaconUps_045e',
	#Deadly Spore	5	1	1	-	Poisonous
	'BGS_131','TB_BaconUps_251',
	#Kangor's Apprentice	5	3	6	-	Deathrattle
	'BGS_012','TB_BaconUps_087',
	#Lightfang Enforcer	5	2	2	-	-
	'BGS_009','BGS_009e','TB_BaconUps_082','TB_BaconUps_082e',
	#Master of Realities	5	6	6	-	Taunt
	'BG21_036','BG21_036e','BG21_036_G','BG21_036_Ge',
	#Mythrax the Unraveler	5	4	4	-	-
	'BGS_202','BGS_202e','TB_BaconUps_258','TB_BaconUps_258e',
	#Nomi, Kitchen Nightmare	5	4	4	-	-
	'BGS_104','BGS_104e1','BGS_104pe','TB_BaconUps_201',
	#Amalgadon	6	6	6	*	Adapt
	'BGS_069','TB_BaconUps_121',
	#Friend of a Friend	6	5	6	-	Battlecry
	#'BG22_404','BG22_404_G',#BAN
	#Nadina the Red	6	7	4	-	Deathrattle
	'BGS_040','TB_BaconUps_154',
	#Seafood Slinger	6	5	5	-	Battlecry
	'BG21_011','BG21_011e','BG21_011e2','BG21_011_G','BG21_011_Ge'
	#Zapp Slywick	6	7	10	-	Windfury
	'BGS_022','TB_BaconUps_091',	
	]

BG_PoolSet_Minion=[
	['BGS_004',],
	['BGS_106','BGS_082','BG20_203','OG_221','OG_256','FP1_024','BG21_013',],
	['BGS_110','BG21_002','BG21_030','DS1_070','DAL_575','BGS_002',],
	['BGS_111','CORE_EX1_093','BG21_007','BGS_105','BGS_083','ICC_807','BG21_038',],
	['CORE_FP1_031','LOE_077','BGS_131','BGS_012','BGS_009','BG21_036','BGS_202','BGS_104',],
	['BGS_069','BGS_040','BG21_011','BGS_022',],
	]

#Wrath Weaver	1	1	3	-	- BGS_004 TB_BaconUps_079 おりや
class BGS_004:# <12>[1453]
	""" Wrath Weaver
	After you play a Demon, deal 1 damage to your hero and gain +2/+2. """
	#
	pass
class BGS_004e:# <12>[1453]
	""" Wrath Woven
	Increased stats. """
	#
	pass
class TB_BaconUps_079:# <12>[1453]
	""" Wrath Weaver
	After you play a Demon, deal 1 damage to your hero and gain +4/+4. """
	#
	pass

class TB_BaconUps_079e:# <12>[1453]
	""" Wrath Woven
	Increased stats. """
	#
	pass


#Acolyte of C'Thun	2	2	3	-	Reborn BGS_106 TB_BaconUps_255 クトゥーン
class BGS_106:# <12>[1453]
	""" Acolyte of C'Thun
	[Taunt][Reborn] """
	#
	pass
class TB_BaconUps_255:# <12>[1453]
	""" Acolyte of C'Thun
	[Taunt][Reborn] """
	#
	pass

#Menagerie Mug	2	2	2	-	Battlecry  BGS_082 TB_BaconUps_144
class BGS_082:# <12>[1453]
	""" Menagerie Mug
	[Battlecry:] Give 3 randomfriendly minions of differentminion types +1/+1. """
	#
	pass
class BGS_082e:# <12>[1453]
	""" Sip of Tea
	+1/+1. """
	#
	pass
class TB_BaconUps_144:# <12>[1453]
	""" Menagerie Mug
	[Battlecry:] Give 3 randomfriendly minions of differentminion types +2/+2. """
	#
	pass
class TB_BaconUps_144e:# <12>[1453]
	""" Sip of Tea
	+2/+2. """
	#
	pass


#Prophet of the Boar	2	3	3	-	Blood Gem BG20_203 BG20_203_G
class BG20_203:# <12>[1453]
	""" Prophet of the Boar
	[Once per Turn:] After you play a Quilboar, gain a [Blood Gem]. """
	#
	pass

class BG20_203_G:# <12>[1453]
	""" Prophet of the Boar
	[Once per Turn:] After you play a Quilboar, gain 2 [Blood Gems]. """
	#
	pass

#Selfless Hero	2	2	1	-	Deathrattle OG_221 TB_BaconUps_014
class OG_221:
	"""Selfless Hero:
	&lt;b&gt;Deathrattle:&lt;/b&gt; Give a random friendly minion &lt;b&gt;Divine Shield&lt;/b&gt;."""
class TB_BaconUps_014:# <5>[1453]
	""" Selfless Hero
	[Deathrattle:] Give 2_random friendly minions [Divine Shield]. """
	#
	pass

#Spawn of N'Zoth	2	2	2	-	Deathrattle　 OG_256 TB_BaconUps_025 んぞす
class OG_256:
	""" Spawn of N'Zoth
	[Deathrattle:] Give your minions +1/+1. """
	#
	pass
OG_256e=buff(1,1)
class TB_BaconUps_025:# <12>[1453]
	""" Spawn of N'Zoth
	[Deathrattle:] Give your minions +2/+2. """
	#
	pass

#Unstable Ghoul	2	1	3	-	Deathrattle FP1_024  TB_BaconUps_118 ぐうる
class FP1_024:# <12>[1453]
	""" Unstable Ghoul
	&lt;b&gt;Taunt&lt;/b&gt;. &lt;b&gt;Deathrattle:&lt;/b&gt; Deal 1 damage to all minions. """
	#
	pass
class TB_BaconUps_118:# <12>[1453]
	""" Unstable Ghoul
	[Taunt][Deathrattle:] Deal 1 damage to all minions twice. """
	#
	pass

#Whelp Smuggler	2	2	5	-	- BG21_013  BG21_013_G 密輸人
class BG21_013:# <12>[1453]
	""" Whelp Smuggler
	After a friendly Dragon gains Attack, give it +1_Health. """
	#
	pass
class BG21_013_G:# <12>[1453]
	""" Whelp Smuggler
	After a friendly Dragon gains Attack, give it +2_Health. """
	#
	pass


#Arm of the Empire	3	4	4	-	Taunt BGS_110  TB_BaconUps_302 
class BGS_110:# <12>[1453]
	""" Arm of the Empire
	Whenever a friendly [Taunt]minion is attacked,give it +2 Attackpermanently. """
	#
	pass
class BGS_110e:# <12>[1453]
	""" Armed!
	+2 Attack """
	#
	pass
class TB_BaconUps_302:# <12>[1453]
	""" Arm of the Empire
	Whenever a friendly [Taunt]minion is attacked,give it +4 Attackpermanently. """
	#
	pass
class TB_BaconUps_302e:# <12>[1453]
	""" Double Armed!
	+4 Attack """
	#
	pass

#Bird Buddy	3	2	4	-	Avenge (X)  BG21_002  BG21_002_G  愛鳥家
class BG21_002:# <12>[1453]
	""" Bird Buddy愛鳥家
	[Avenge (1):] Give your Beasts +1/+1. """
	#
	pass
class BG21_002_G:# <12>[1453]
	""" Bird Buddy
	[Avenge (1):] Give your Beasts +2/+2. """
	#
	pass
class BG21_002_Ge:# <12>[1453]
	""" Well Fed
	+2/+2. """
	#
	pass
class BG21_002e:# <12>[1453]
	""" Well Fed
	+1/+1. """
	#
	pass


#Budding Greenthumb	3	1	4	-	Avenge (X)  BG21_030  BG21_030_G
class BG21_030:# <12>[1453]
	""" Budding Greenthumb
	[Avenge (3):] Giveadjacent minions+2/+1 permanently. """
	#
	pass
class BG21_030_G:# <12>[1453]
	""" Budding Greenthumb
	[Avenge (3):] Giveadjacent minions+4/+2 permanently. """
	#
	pass

#Houndmaster	3	4	3	-	Battlecry  DS1_070  TB_BaconUps_068 TB_BaconUps_068e
class DS1_070:# <3>[1453]
	""" Houndmaster
	&lt;b&gt;Battlecry:&lt;/b&gt; Give a friendly Beast +2/+2 and &lt;b&gt;Taunt&lt;/b&gt;."""
	#
	pass
DS1_070o=buff(2,2,taunt=True)
class TB_BaconUps_068:# <3>[1453]
	""" Houndmaster
	[Battlecry:] Give a friendly Beast +4/+4 and [Taunt]. """
	#
	pass
class TB_BaconUps_068e:# <3>[1453]
	""" Master's Presence
	+4/+4 and [Taunt]. """
	#
	pass


#Khadgar	3	2	2	-	-  DAL_575 TB_BaconUps_034 カドガー
class DAL_575:
	""" Khadgar
	Your cards that summon minions summon twice_as_many. """
	#
	pass
class TB_BaconUps_034:# <4>[1453]
	""" Khadgar
	Your cards that summon minions summon three times as many. """
	#
	pass


#Soul Juggler	3	3	5	-	-  BGS_002  TB_BaconUps_075
class BGS_002:# <9>[1453]
	""" Soul Juggler
	After a friendly Demon dies, deal 3 damage to a random enemy minion. """
	#
	pass
class TB_BaconUps_075:# <9>[1453]
	""" Soul Juggler
	After a friendly Demon dies, deal 3 damage to a random enemy minion twice. """
	#
	pass


#Champion of Y'Shaarj	4	4	4	-	Taunt  BGS_111 BGS_111e   TB_BaconUps_301 TB_BaconUps_301e
class BGS_111:# <12>[1453]
	""" Champion of Y'Shaarj
	Whenever a friendly [Taunt] minion is attacked, gain +1/+1 permanently. """
	#
	pass
class BGS_111e:# <12>[1453]
	""" Y'Shaarj!!!
	+1/+1. """
	#
	pass
class TB_BaconUps_301:# <12>[1453]
	""" Champion of Y'Shaarj
	Whenever a friendly [Taunt] minion is attacked, gain +2/+2 permanently. """
	#
	pass

class TB_BaconUps_301e:# <12>[1453]
	""" Y'Shaarj!!!!!!
	+2/+2. """
	#
	pass

#Defender of Argus	4	3	3	-	Battlecry CORE_EX1_093  TB_BaconUps_009 TB_BaconUps_009
class CORE_EX1_093:# <12>[1453]
	""" Defender of Argus
	[Battlecry:] Give adjacent minions +1/+1 and [Taunt]. """
	#
	pass
EX1_093e=buff(1,1,taunt=True)
""" Hand of Argus
+2/+2 and [Taunt]. """
class TB_BaconUps_009:# <12>[1453]
	""" Defender of Argus
	[Battlecry:] Give adjacent minions +2/+2 and [Taunt]. """
	#
	pass
class TB_BaconUps_009e:# <12>[1453]
	""" Hand of Argus
	+2/+2 and [Taunt]. """
	#
	pass

#Impatient Doomsayer	4	2	6	-	Avenge (X) BG21_007 BG21_007_G
class BG21_007:# <12>[1453]
	""" Impatient Doomsayer
	[Avenge (4):] Add a random Demon to your hand. """
	#
	pass
class BG21_007_G:# <12>[1453]
	""" Impatient Doomsayer
	[Avenge (4):] Add 2 random Demons to your hand. """
	#
	pass


#Majordomo Executus	4	6	3	-	-  BGS_105  BGS_105e  TB_BaconUps_207
class BGS_105:# <12>[1453]
	""" Majordomo Executus
	At the end of your turn, giveyour left-most minion +1/+1.Repeat for each Elementalyou played this turn. """
	#
	pass
class BGS_105e:# <12>[1453]
	""" Aegis of the Firelord
	Increased stats. """
	#
	pass
class TB_BaconUps_207:# <12>[1453]
	""" Majordomo Executus
	At the end of your turn, giveyour left-most minion +2/+2.Repeat for each Elementalyou played this turn. """
	#
	pass


#Menagerie Jug	4	3	3	-	Battlecry  BGS_083 BGS_083e  TB_BaconUps_145 TB_BaconUps_145e
class BGS_083:# <12>[1453]
	""" Menagerie Jug
	[Battlecry:] Give 3 randomfriendly minions of different minion types +2/+2. """
	#
	pass
class BGS_083e:# <12>[1453]
	""" Gulp of Tea
	+2/+2. """
	#
	pass
class TB_BaconUps_145:# <12>[1453]
	""" Menagerie Jug
	[Battlecry:] Give 3 randomfriendly minions of differentminion types +4/+4. """
	#
	pass

class TB_BaconUps_145e:# <12>[1453]
	""" Gulp of Tea
	+4/+4. """
	#
	pass


#Strongshell Scavenger	4	2	3	-	Battlecry  ICC_807  ICC_807e  TB_BaconUps_072 TB_BaconUps_072e
class ICC_807:# <2>[1453]
	""" Strongshell Scavenger
	&lt;b&gt;Battlecry:&lt;/b&gt; Give your &lt;b&gt;Taunt&lt;/b&gt; minions +2/+2. """
	#
	pass

class ICC_807e:# <12>[1453]
	""" Strongshell
	+2/+2. """
	#
	pass
class TB_BaconUps_072:# <2>[1453]
	""" Strongshell Scavenger
	[Battlecry:] Give your [Taunt] minions +4/+4. """
	#
	pass
class TB_BaconUps_072e:# <12>[1453]
	""" Strongshell
	+4/+4. """
	#
	pass

#Witchwing Nestmatron	4	3	5	-	Avenge (X)  BG21_038 BG21_038_G
class BG21_038:# <12>[1453]
	""" Witchwing Nestmatron
	[Avenge (3):] Add a random [Battlecry] minion to your_hand. """
	#
	pass
class BG21_038_G:# <12>[1453]
	""" Witchwing Nestmatron
	[Avenge (3):] Add 2 random [Battlecry] minions to your_hand. """
	#
	pass

#Baron Rivendare	5	1	7	-	Deathrattle  CORE_FP1_031 TB_BaconUps_055 ばろん
class CORE_FP1_031:
	"""Baron Rivendare
	Your minions trigger their &lt;b&gt;Deathrattles&lt;/b&gt; twice."""
	pass
class TB_BaconUps_055:# <12>[1453]
	""" Baron Rivendare
	Your minions trigger their [Deathrattles] three times. """
	#
	pass

#Brann Bronzebeard	5	2	4	-	Battlecry  LOE_077 LOE_077e  TB_BaconUps_045  TB_BaconUps_045e
class LOE_077:# 
	""" Brann Bronzebeard
	Your &lt;b&gt;Battlecries&lt;/b&gt; trigger twice. """
	#
	pass
class LOE_077e:# 
	""" Bronzebeard Battlecry
	Your &lt;b&gt;Battlecries&lt;/b&gt; trigger twice. """
	#
	pass
class TB_BaconUps_045:# <12>[1453]
	""" Brann Bronzebeard
	Your [Battlecries] trigger three times. """
	#
	pass

class TB_BaconUps_045e:# <12>[1453]
	""" Bronzebeard Battlecry
	Your [Battlecries] trigger three times. """
	#
	pass

#Deadly Spore	5	1	1	-	Poisonous BGS_131  TB_BaconUps_251
class BGS_131:# <12>[1453]
	""" Deadly Spore
	[Poisonous] """
	#
	pass
class TB_BaconUps_251:# <12>[1453]
	""" Deadly Spore
	[Poisonous] """
	#
	pass


#Kangor's Apprentice	5	3	6	-	Deathrattle    BGS_012  TB_BaconUps_087
class BGS_012:# <12>[1453]
	""" Kangor's Apprentice
	[Deathrattle]: Summon the first 2 friendly Mechs that died this combat. """
	#
	pass
class TB_BaconUps_087:# <12>[1453]
	""" Kangor's Apprentice
	[Deathrattle]: Summon the first 4 friendly Mechs that died this combat. """
	#
	pass


#Lightfang Enforcer	5	2	2	-	-    BGS_009 BGS_009e  TB_BaconUps_082 TB_BaconUps_082e
class BGS_009:# <12>[1453]
	""" Lightfang Enforcer
	At the end of your turn,give a friendly minionof each minion type+2/+2. """
	#
	pass
class BGS_009e:# <7>[1453]
	""" Blessed
	Increased stats. """
	#
	pass
class TB_BaconUps_082:# <12>[1453]
	""" Lightfang Enforcer
	At the end of your turn,give a friendly minionof each minion type+4/+4. """
	#
	pass

class TB_BaconUps_082e:# <7>[1453]
	""" Blessed
	Increased stats. """
	#
	pass


#Master of Realities	5	6	6	-	Taunt  BG21_036 BG21_036e BG21_036_G BG21_036_Ge
class BG21_036:# <12>[1453]
	""" Master of Realities
	[[Taunt].] After a friendly Elemental gains stats, gain +1/+1. """
	#
	pass
class BG21_036_G:# <12>[1453]
	""" Master of Realities
	[[Taunt].] After a friendly Elemental gains stats, gain +2/+2. """
	#
	pass
class BG21_036_Ge:# <12>[1453]
	""" The Elemental Plane
	+2/+2. """
	#
	pass
class BG21_036e:# <12>[1453]
	""" The Elemental Plane
	+1/+1. """
	#
	pass

#Mythrax the Unraveler	5	4	4	-	-  BGS_202 BGS_202e TB_BaconUps_258 TB_BaconUps_258e
class BGS_202:# <12>[1453]
	""" Mythrax the Unraveler
	At the end of your turn,gain +2/+2 for each__minion type you control. """
	#
	pass
class BGS_202e:# <12>[1453]
	""" Void Echoes
	+2/+2. """
	#
	pass
class TB_BaconUps_258:# <12>[1453]
	""" Mythrax the Unraveler
	At the end of your turn,gain +4/+4 for each__minion type you control. """
	#
	pass
class TB_BaconUps_258e:# <12>[1453]
	""" Void Echoes
	+4/+4. """
	#
	pass
#Nomi, Kitchen Nightmare	5	4	4	-	-  BGS_104 BGS_104e1 BGS_104pe TB_BaconUps_201
class BGS_104:# <12>[1453]
	""" Nomi, Kitchen Nightmare
	After you play an Elemental,Elementals in Bob's Tavernhave +1/+1 for the restof the game. """
	#
	pass
class BGS_104e1:# <12>[1453]
	""" Tavern Feast
	Increased stats. """
	#
	pass
class BGS_104pe:# <12>[1453]
	""" Nomi Player Enchant
	Increased stats. """
	#
	pass
class TB_BaconUps_201:# <12>[1453]
	""" Nomi, Kitchen Nightmare
	After you play an Elemental,Elementals in Bob's Tavernhave +2/+2 for the restof the game. """
	#
	pass

#Amalgadon	6	6	6	*	Adapt  BGS_069 TB_BaconUps_121 
class BGS_069:
	""" Amalgadon
	&lt;b&gt;Battlecry:&lt;/b&gt; For each different minion type you have among other minions, &lt;b&gt;Adapt&lt;/b&gt; randomly."""
	#
	pass
class TB_BaconUps_121:
	""" Amalgadon
	&lt;b&gt;Battlecry:&lt;/b&gt; For each different minion type you have among other minions, &lt;b&gt;Adapt&lt;/b&gt; randomly twice."""
	#
	pass

#Friend of a Friend	(BAN)	6	5	6	-	Battlecry   BG22_404 BG22_404_G 
class BG22_404:# <12>[1453]
	""" Friend of a Friend(BAN)
	[Battlecry: Discover] a Buddy. """
	#
	pass
class BG22_404_G:# <12>[1453]
	""" Friend of a Friend(BAN)
	[Battlecry: Discover]two Buddies. """
	#
	pass

#Nadina the Red	6	7	4	-	Deathrattle  BGS_040 TB_BaconUps_154
class BGS_040:# <12>[1453]
	""" Nadina the Red
	[Deathrattle:] Give your Dragons [Divine Shield]. """
	#
	pass
class TB_BaconUps_154:# <12>[1453]
	""" Nadina the Red
	[Deathrattle:] Give your Dragons [Divine Shield]. """
	#
	pass

#Seafood Slinger	6	5	5	-	Battlecry BG21_011 BG21_011e BG21_011e2 BG21_011_G BG21_011_Ge
class BG21_011:# <12>[1453]
	""" Seafood Slinger
	[Battlecry:] Make a Murloc Golden. """
	#
	pass
class BG21_011e:# <12>[1453]
	""" Slung
	+3/+3. """
	#
	pass
class BG21_011e2:# <12>[1453]
	""" Battlecry Self-Trigger [DNT]
	 """
	#
	pass
class BG21_011_G:# <12>[1453]
	""" Seafood Slinger
	[Battlecry:] Make a Murloc Golden. """
	#
	pass
class BG21_011_Ge:# <12>[1453]
	""" Slung
	+6/+6. """
	#
	pass

#Zapp Slywick	6	7	10	-	Windfury  BGS_022 TB_BaconUps_091
class BGS_022:# <12>[1453]
	""" Zapp Slywick
	[Windfury]This minion always attacksthe enemy minion withthe lowest Attack. """
	#
	pass
class TB_BaconUps_091:# <12>[1453]
	""" Zapp Slywick
	[Mega-Windfury]This minion always attacksthe enemy minion withthe lowest Attack. """
	#
	pass

#############################################


##
## miscellinous enchantments or banned items
##

class BG20_304:# <12>[1453]
	""" Archdruid Hamuul  (BAN??)
	[Battlecry:] [Refresh] Bob's Tavern with minions of your most common type. """
	#
	pass
class BG20_304_G:# <12>[1453]
	""" Archdruid Hamuul  (BAN??)
	[Battlecry:] [Refresh] Bob's Tavern with minions of your most common type. """
	#
	pass



class BG21_013e:# <12>[1453]
	""" Job Whelp Done
	Increased Health. """
	#
	pass





class BG21_018:# <12>[1453]
	""" Defiant Shipwright (BAN??)
	After you upgrade yourTavern Tier, add a randomPirate to Bob's Tavern. """
	#
	pass
class BG21_018_G:# <12>[1453]
	""" Defiant Shipwright
	After you upgrade yourTavern Tier, add two random Pirates to Bob's Tavern. """
	#
	pass


class BG21_024_Ge:# <12>[1453]
	""" Greased Up
	+2/+2. """
	#
	pass

class BG21_024e:# <12>[1453]
	""" Greased Up
	+1/+1. """
	#
	pass

class BG21_025e:# <12>[1453]
	""" Omega Busted
	+1/+1. """
	#
	pass

class BG21_025e2:# <12>[1453]
	""" Omega Busted
	+2/+2. """
	#
	pass

class BG21_027_Ge:# <12>[1453]
	""" Evolved
	Tripled Attack. """
	#
	pass

class BG21_027e:# <12>[1453]
	""" Evolved
	Doubled Attack. """
	#
	pass



class BG21_030_Ge:# <12>[1453]
	""" Budding
	+4/+2. """
	#
	pass

class BG21_030e:# <12>[1453]
	""" Budding
	+2/+1. """
	#
	pass





class BG21_039_Ge:# <12>[1453]
	""" Grasp of Kathra'natir
	Kathra'natir is granting +4 Attack. """
	#
	pass

class BG21_039e:# <12>[1453]
	""" Grasp of Kathra'natir
	Kathra'natir is granting +2 Attack. """
	#
	pass

class BG21_040e:# <12>[1453]
	""" Refresh Costs 1 less
	 """
	#
	pass

class BG22_401_Ge:# <12>[1453]
	""" Swamped
	+2 Attack. """
	#
	pass

class BG22_401e:# <12>[1453]
	""" Swamped
	+1 Attack. """
	#
	pass


class BG22_BuddyMeter:# <12>[1453]
	""" Buddy Meter
	 """
	#
	pass

class BG22_BuddyPlayerEnch:# <12>[1453]
	""" Buddy Player Enchantment [DNT]
	 """
	#
	pass

class BGS_001e:# <12>[1453]
	""" Impish
	+2/+2. """
	#
	pass




class BGS_010e:# <12>[1453]
	""" Monstrous
	Health increased. """
	#
	pass


class BGS_017:# <12>[1453]
	""" Pack Leader
	Whenever you summon a Beast, give it +2 Attack. """
	#
	pass

class BGS_017e:# <12>[1453]
	""" Feral Calling
	+2 Attack. """
	#
	pass

class BGS_018e:# <12>[1453]
	""" Soul of the Beast
	+5/+5. """
	#
	pass

class BGS_021e:# <12>[1453]
	""" Rampage
	+5/+5. """
	#
	pass



class BGS_028pe:# <7>[1453]
	""" PogoCounterEnchantment
	Counts the number of Pogo-Hoppers played. """
	#
	pass

class BGS_029:# <12>[1453]
	""" Shifter Zerus
	Each turn this is in your hand, transform it into a random minion. """
	#
	pass

class BGS_029e:# <12>[1453]
	""" Shifting
	Transforming into random minions. """
	#
	pass

class BGS_030e:# <12>[1453]
	""" Bagurgled
	Increased stats. """
	#
	pass

class BGS_033e1:# <12>[1453]
	""" Well Fed
	Increased stats. """
	#
	pass

class BGS_035:# <12>[1453]
	""" Waxrider Togwaggle
	Whenever a friendly Dragon kills an enemy, gain +2/+2. """
	#
	pass

class BGS_035e:# <12>[1453]
	""" Dragon Wax
	Increased stats. """
	#
	pass

class BGS_036e:# <12>[1453]
	""" Dragonlust
	Increased stats. """
	#
	pass

class BGS_037e:# <12>[1453]
	""" Time Dilation
	+2/+1. """
	#
	pass

class BGS_038e:# <12>[1453]
	""" Twilight Embrace
	+2/+2. """
	#
	pass



class BGS_041e:# <12>[1453]
	""" Arcane Aspect
	+1/+1. """
	#
	pass

class BGS_044e:# <9>[1453]
	""" Protect Mama!
	[Taunt] """
	#
	pass

class BGS_045e:# <12>[1453]
	""" Cold Breath
	Multiplying Attack. """
	#
	pass

class BGS_046t:# <12>[1453]
	""" Treasure Chest
	[Deathrattle:] Summon a random Golden minion. """
	#
	pass

class BGS_047e:# <12>[1453]
	""" Yaharr!!
	+2/+1. """
	#
	pass

class BGS_048e:# <12>[1453]
	""" Pirate Tattoos
	Increased stats. """
	#
	pass

class BGS_053e:# <12>[1453]
	""" Pirate Life!
	+3 Attack. """
	#
	pass

class BGS_056e:# <12>[1453]
	""" Snarled
	+2/+2. """
	#
	pass

class BGS_059e:# <12>[1453]
	""" Devoured Soul
	Increased stats. """
	#
	pass

class BGS_066e:# <12>[1453]
	""" Gold Grubbing
	Increased stats. """
	#
	pass

class BGS_067e:# <12>[1453]
	""" Divinity
	Increased stats. """
	#
	pass

class BGS_071e:# <12>[1453]
	""" Deflect-o-Shield
	Increased stats. """
	#
	pass

class BGS_075e:# <3>[1453]
	""" Rabid
	+1/+2. """
	#
	pass

class BGS_077:# <12>[1453]
	""" Arcane Cannon (BAN?)
	Can't attack.After an adjacent minionattacks, deal 2 damageto an enemy minion. """
	#
	pass

class BGS_079:# <12>[1453]
	""" The Tide Razor (??)
	[Deathrattle]: Summon 3 random Pirates. """
	#
	pass

class BGS_080e:# <12>[1453]
	""" Broken Seas
	+2/+2. """
	#
	pass

class BGS_081e:# <12>[1453]
	""" Loot!
	+1/+1. """
	#
	pass




class BGS_100e:# <12>[1453]
	""" Lil' Hand of Rag
	Increased stats. """
	#
	pass






class BGS_112:# <12>[1453]
	""" Qiraji Harbinger
	After a friendly minion with [Taunt] dies, give its neighbors +2/+2. """
	#
	pass

class BGS_112e:# <12>[1453]
	""" Harbinger's Illusion
	+2/+2. """
	#
	pass

class BGS_113:# <12>[1453]
	""" Faceless Taverngoer
	[Battlecry:] Choose a minionin Bob's Tavern. Transforminto a plain copy of it. """
	#
	pass

class BGS_116e:# <12>[1453]
	""" Refresh Costs 0
	 """
	#
	pass

class BGS_120e:# <12>[1453]
	""" Party Time
	+1/+1. """
	#
	pass

class BGS_124e:# <12>[1453]
	""" Garrdian
	+1 Health. """
	#
	pass

class BGS_127e:# <12>[1453]
	""" Lava Shield
	+1 Health. """
	#
	pass

class BGS_128e:# <12>[1453]
	""" Elemental Energy
	+1/+1. """
	#
	pass


class BGS_200:# <12>[1453]
	""" Warden of Old
	[Deathrattle:] Add a Gold Coin to your hand. """
	#
	pass

class BGS_201:# <12>[1453]
	""" Tormented Ritualist
	[Taunt]Whenever this is attacked,give adjacent minions+1/+1. """
	#
	pass

class BGS_201e:# <12>[1453]
	""" Ritual Sacrifice
	+1/+1. """
	#
	pass



class BGS_204e:# <12>[1453]
	""" Bigger!!!
	+1/+1. """
	#
	pass

class BGS_205:# <12>[1453]
	""" Elistra the Immortal (BAN)
	[Divine Shield]. [Reborn].Whenever a friendly [Taunt]minion is attacked, this__gets attacked instead. """
	#
	pass
class TB_BaconUps_306:# <12>[1453]
	""" Elistra the Immortal (BAN)
	[Divine Shield]. [Reborn].Whenever a friendly [Taunt]minion is attacked, this__gets attacked instead. """
	#
	pass


########################################################################################
##
## TB_BaconUps series 
##
########################################################################################



class TB_BaconUps_011e:# <12>[1453]
	""" Blarghghl
	Increased Attack. """
	#
	pass


class TB_BaconUps_025:# <12>[1453]
	""" Spawn of N'Zoth
	[Deathrattle:] Give your minions +2/+2. """
	#
	pass

class TB_BaconUps_025e:# <12>[1453]
	""" Slimed
	+2/+2. """
	#
	pass

class TB_BaconUps_031:# <6>[1453]
	""" Tortollan Shellraiser
	[Taunt][Deathrattle:] Give a random_friendly minion +2/+2. """
	#
	pass

class TB_BaconUps_031e:# <6>[1453]
	""" Shellshield
	+2/+2. """
	#
	pass

class TB_BaconUps_032e:# <12>[1453]
	""" Replicating Menace
	[Deathrattle:] Summon three 2/2 Microbots. """
	#
	pass

class TB_BaconUps_033:# <10>[1453]
	""" Festeroot Hulk
	After a friendly minion attacks, gain +2 Attack. """
	#
	pass

class TB_BaconUps_033e:# <12>[1453]
	""" Grown
	Increased Attack. """
	#
	pass


class TB_BaconUps_037:# <12>[1453]
	""" Crowd Favorite
	Whenever you play a card with [Battlecry], gain +2/+2. """
	#
	pass

class TB_BaconUps_037e:# <12>[1453]
	""" Huge Ego
	Increased stats. """
	#
	pass

class TB_BaconUps_038:# <12>[1453]
	""" Phalanx Commander
	Your [Taunt] minionshave +4 Attack. """
	#
	pass

class TB_BaconUps_038e:# <12>[1453]
	""" Commanded
	Phalanx Commander is granting this +4 Attack. """
	#
	pass

class TB_BaconUps_043e:# <3>[1453]
	""" Well Fed
	Increased Attack and Health. """
	#
	pass

class TB_BaconUps_044e:# <7>[1453]
	""" Ironed Out
	Increased stats. """
	#
	pass



class TB_BaconUps_046e:# <12>[1453]
	""" Junked Up
	Increased stats. """
	#
	pass

class TB_BaconUps_047:# <5>[1453]
	""" Bolvar, Fireblood
	[Divine Shield]After a friendly minion loses_[Divine Shield], gain +4 Attack. """
	#
	pass

class TB_BaconUps_047e:# <5>[1453]
	""" Fading Light
	Increased Attack. """
	#
	pass

class TB_BaconUps_053e:# <9>[1453]
	""" Siegebreaking
	Siegebreaker is granting this minion +2 Attack. """
	#
	pass

class TB_BaconUps_055:# <12>[1453]
	""" Baron Rivendare
	Your minions trigger their [Deathrattles] three times. """
	#
	pass

class TB_Baconups_055e:# <12>[1453]
	""" Rivendare Deathrattle
	Your minions trigger their [Deathrattles] three times. """
	#
	pass

class TB_BaconUps_058:# <12>[1453]
	""" The Boogeymonster
	Whenever this attacks and kills a minion, gain +4/+4. """
	#
	pass

class TB_BaconUps_058e:# <12>[1453]
	""" Tasty!
	Increased stats. """
	#
	pass

class TB_BaconUps_060e:# <9>[1453]
	""" Grasp of Mal'Ganis
	Mal'Ganis is granting +4/+4. """
	#
	pass

class TB_BaconUps_061e:# <12>[1453]
	""" Trained
	+2/+2 """
	#
	pass

class TB_BaconUps_062e:# <12>[1453]
	""" Impish
	+4/+4. """
	#
	pass

class TB_BaconUps_063e:# <12>[1453]
	""" Well Fed
	+2/+2. """
	#
	pass

class TB_BaconUps_064e:# <12>[1453]
	""" Mrghlglhal
	+4 Health. """
	#
	pass

class TB_BaconUps_066e:# <3>[1453]
	""" Metal Teeth
	+4 Attack. """
	#
	pass


class TB_BaconUps_069e:# <10>[1453]
	""" Screwy Jank
	+4/+4. """
	#
	pass

class TB_BaconUps_070:# <9>[1453]
	""" Crystalweaver
	[Battlecry:] Give your Demons +2/+2. """
	#
	pass

class TB_BaconUps_070e:# <12>[1453]
	""" Serrated Shadows
	+2/+2. """
	#
	pass

class TB_BaconUps_072:# <2>[1453]
	""" Strongshell Scavenger
	[Battlecry:] Give your [Taunt] minions +4/+4. """
	#
	pass

class TB_BaconUps_072e:# <12>[1453]
	""" Strongshell
	+4/+4. """
	#
	pass

class TB_BaconUps_073:# <12>[1453]
	""" Menagerie Magician
	[Battlecry:] Give a random friendly Beast, Dragon, and Murloc +4/+4. """
	#
	pass

class TB_BaconUps_073e:# <12>[1453]
	""" A Simple Trick
	+4/+4. """
	#
	pass

class TB_BaconUps_074:# <2>[1453]
	""" Virmen Sensei
	[Battlecry:] Give a friendly Beast +4/+4. """
	#
	pass

class TB_BaconUps_074e:# <12>[1453]
	""" Get Big
	+4/+4. """
	#
	pass


class TB_BaconUps_077e:# <7>[1453]
	""" Kinetic Energy
	Increased stats. """
	#
	pass




class TB_BaconUps_085e:# <12>[1453]
	""" Soul of the Beast
	+10/+10. """
	#
	pass

class TB_BaconUps_086:# <12>[1453]
	""" Pack Leader
	Whenever you summon a Beast, give it +4 Attack. """
	#
	pass

class TB_BaconUps_086e:# <12>[1453]
	""" Feral Calling
	+4 Attack. """
	#
	pass


class TB_BaconUps_088e:# <12>[1453]
	""" Strength of the Pack
	+2 Attack from {0}. """
	#
	pass

class TB_BaconUps_090e:# <12>[1453]
	""" Rampage
	+10/+10. """
	#
	pass



class TB_BaconUps_094e:# <12>[1453]
	""" Pistons
	Increased Attack. """
	#
	pass

class TB_BaconUps_095:# <12>[1453]
	""" Shifter Zerus
	Each turn this is in your hand, transform it into a random minion. """
	#
	pass

class TB_BaconUps_095e:# <12>[1453]
	""" Shifting
	Transforming into random minions. """
	#
	pass

class TB_BaconUps_099e:# <5>[1453]
	""" Annoy-o-Module
	[Taunt], [Divine Shield]. """
	#
	pass

class TB_BaconUps_100e:# <12>[1453]
	""" Bagurgled
	Increased stats. """
	#
	pass

class TB_BaconUps_101e:# <9>[1453]
	""" Brow Furrow
	Increased stats. """
	#
	pass

class TB_BaconUps_104e:# <12>[1453]
	""" Well Fed
	Increased stats. """
	#
	pass

class TB_BaconUps_105:# <12>[1453]
	""" Waxrider Togwaggle
	Whenever a friendly Dragon kills an enemy, gain +4/+4. """
	#
	pass

class TB_BaconUps_105e:# <12>[1453]
	""" Dragon Wax
	Increased stats. """
	#
	pass

class TB_BaconUps_106e:# <12>[1453]
	""" Dragonlust
	Increased stats. """
	#
	pass

class TB_BaconUps_107e:# <12>[1453]
	""" Time Dilation
	+4/+2. """
	#
	pass

class TB_BaconUps_108e:# <12>[1453]
	""" Twilight Embrace
	+4/+4. """
	#
	pass

class TB_BaconUps_109e:# <12>[1453]
	""" Arcane Aspect
	+2/+2. """
	#
	pass

class TB_BaconUps_115e:# <12>[1453]
	""" Cold Breath
	Multiplying Attack. """
	#
	pass

class TB_BaconUps_117e:# <12>[1453]
	""" Divinity
	Increased stats. """
	#
	pass

class TB_BaconUps_118:# <12>[1453]
	""" Unstable Ghoul
	[Taunt][Deathrattle:] Deal 1 damage to all minions twice. """
	#
	pass

class TB_BaconUps_120e:# <12>[1453]
	""" Dragonscales
	Attack increased. """
	#
	pass

class TB_BaconUps_123e:# <12>[1453]
	""" Deflect-o-Shield
	Increased stats. """
	#
	pass

class TB_BaconUps_124e:# <12>[1453]
	""" Felfin Fueled
	+2/+2. """
	#
	pass

class TB_BaconUps_125e:# <3>[1453]
	""" Rabid
	+2/+4. """
	#
	pass

class TB_BaconUps_128:# <12>[1453]
	""" Arcane Cannon (BAN?)
	Can't attack.After an adjacent minionattacks, deal 2 damage to___an enemy minion twice. """
	#
	pass

class TB_BaconUps_130e:# <12>[1453]
	""" Gold Grubbing
	Increased stats. """
	#
	pass

class TB_BaconUps_132t:# <12>[1453]
	""" Treasure Chest
	[Deathrattle:] Summon 2 random Golden minions. """
	#
	pass

class TB_BaconUps_134e:# <12>[1453]
	""" Yaharr!!
	+4/+2. """
	#
	pass

class TB_BaconUps_136e:# <12>[1453]
	""" Yarrr!
	Southsea Captain is granting +2/+2. """
	#
	pass

class TB_BaconUps_137:# <12>[1453]
	""" The Tide Razor (BAN)
	[Deathrattle]: Summon 6 random Pirates. """
	#
	pass

class TB_BaconUps_138e:# <12>[1453]
	""" Pirate Life!
	+6 Attack. """
	#
	pass

class TB_BaconUps_139e:# <12>[1453]
	""" Snarled
	+4/+4. """
	#
	pass

class TB_BaconUps_140e:# <12>[1453]
	""" Pirate Tattoos
	Increased stats. """
	#
	pass

class TB_BaconUps_142e:# <12>[1453]
	""" Broken Seas
	+4/+4. """
	#
	pass

class TB_BaconUps_143e:# <12>[1453]
	""" Loot!
	+2/+2. """
	#
	pass

class TB_BaconUps_147:# <5>[1453]
	""" Righteous Protector (BAN?)
	[Taunt][Divine Shield] """
	#
	pass

class TB_BaconUps_163e:# <12>[1453]
	""" Garrdian
	+2 Health. """
	#
	pass



class TB_Baconups_202e:# <12>[1453]
	""" Lava Shield
	+2 Health. """
	#
	pass

class TB_Baconups_203e:# <12>[1453]
	""" Elemental Energy
	+2/+2. """
	#
	pass


class TB_BaconUps_250e:# <12>[1453]
	""" Microwrapped
	Attack increased. """
	#
	pass

class TB_BaconUps_256:# <12>[1453]
	""" Warden of Old (BAN?)
	[Deathrattle:] Add 2 Gold Coins to your hand. """
	#
	pass

class TB_BaconUps_257:# <12>[1453]
	""" Tormented Ritualist (BAN?)
	[Taunt]Whenever this is attacked,give adjacent minions+2/+2. """
	#
	pass

class TB_BaconUps_257e:# <12>[1453]
	""" Ritual Sacrifice (BAN?)
	+2/+2. """
	#
	pass

class TB_BaconUps_303:# <12>[1453]
	""" Qiraji Harbinger
	After a friendly minion with [Taunt] dies, give its neighbors +4/+4. """
	#
	pass

class TB_BaconUps_303e:# <12>[1453]
	""" Harbinger's Illusion
	+4/+4. """
	#
	pass

class TB_BaconUps_304e:# <12>[1453]
	""" Bigger!!!
	+2/+2. """
	#
	pass

class TB_BaconUps_305:# <12>[1453]
	""" Faceless Taverngoer(BAN?)
	[Battlecry:] Choose a minionin Bob's Tavern. Transforminto a Golden copy of it. """
	#
	pass

class TB_BaconUps_308:# <5>[1453]
	""" Argent Braggart(BAN?)
	[Battlecry:] Gain Attack andHealth to match double thehighest in the battlefield. """
	#
	pass

class TB_BaconUps_320:# <12>[1453]
	""" Barrens Blacksmith (BAN?)
	[Frenzy:] Give your other minions +4/+4. """
	#
	pass
class TB_BaconUps_320e:# <12>[1453]
	""" Superforged(BAN?)
	+4/+4. """
	#
	pass


