
from ..utils import *
from fireplace.battlegrounds.BG_actions import *

BG_Minion=[
	
	'BGS_004','BGS_004e','TB_BaconUps_079','TB_BaconUps_079e',#Wrath Weaver	1
	'BGS_106','TB_BaconUps_255',#Acolyte of C'Thun	2
	'BGS_082','BGS_082e','TB_BaconUps_144','TB_BaconUps_144e',#Menagerie Mug	2
	'BG20_203','BG20_203_G',#Prophet of the Boar	2
	'OG_221','TB_BaconUps_014',#Selfless Hero	2
	'OG_256','OG_256e','TB_BaconUps_025','TB_BaconUps_025e',#Spawn of N'Zoth	2
	'FP1_024','TB_BaconUps_118',#Unstable Ghoul	2
	'BG21_013','BG21_013e','BG21_013_G',#Whelp Smuggler	2
	'BGS_110','BGS_110e','TB_BaconUps_302','TB_BaconUps_302e',#Arm of the Empire	3
	'BG21_002','BG21_002e','BG21_002_G','BG21_002_Ge',#Bird Buddy	3
	'BG21_030','BG21_030e','BG21_030_G','BG21_030_Ge',#Budding Greenthumb	3
	'DS1_070','DS1_070o','TB_BaconUps_068','TB_BaconUps_068e',#Houndmaster	3
	'DAL_575','TB_BaconUps_034',#Khadgar	3
	'BGS_002','TB_BaconUps_075',#Soul Juggler	3
	'BGS_111','BGS_111e','TB_BaconUps_301','TB_BaconUps_301e',#Champion of Y'Shaarj	4
	'CORE_EX1_093','EX1_093e','TB_BaconUps_009','TB_BaconUps_009e',#Defender of Argus	4
	'BG21_007','BG21_007_G',#Impatient Doomsayer	4
	'BGS_105','BGS_105e','TB_BaconUps_207',#Majordomo Executus	4
	'BGS_083','BGS_083e','TB_BaconUps_145','TB_BaconUps_145e',#Menagerie Jug	4
	'ICC_807',  'ICC_807e',  'TB_BaconUps_072', 'TB_BaconUps_072e',#Strongshell Scavenger	4
	'BG21_038','BG21_038_G',#Witchwing Nestmatron	4
	'CORE_FP1_031','TB_BaconUps_055',#Baron Rivendare	5
	'LOE_077','LOE_077e','TB_BaconUps_045','TB_BaconUps_045e',#Brann Bronzebeard	5
	'BGS_131','TB_BaconUps_251',#Deadly Spore	5
	'BGS_012','TB_BaconUps_087',#Kangor's Apprentice	5
	'BGS_009','BGS_009e','TB_BaconUps_082','TB_BaconUps_082e',#Lightfang Enforcer	5
	'BG21_036','BG21_036e','BG21_036_G','BG21_036_Ge',#Master of Realities	5
	'BGS_202','BGS_202e','TB_BaconUps_258','TB_BaconUps_258e',#Mythrax the Unraveler	5
	'BGS_104','BGS_104e1','BGS_104pe','TB_BaconUps_201',#Nomi, Kitchen Nightmare	5
	'BGS_069','TB_BaconUps_121',#Amalgadon	6
	'BGS_040','TB_BaconUps_154',#Nadina the Red	6
	'BG21_011','BG21_011e','BG21_011e2','BG21_011_G','BG21_011_Ge',#Seafood Slinger	6
	'BGS_022','TB_BaconUps_091',	#Zapp Slywick	6
	]

BG_PoolSet_Minion=[
	['BGS_004',],
	['BGS_106','BGS_082','BG20_203','OG_221','OG_256','FP1_024','BG21_013',],
	['BGS_110','BG21_002','BG21_030','DS1_070','DAL_575','BGS_002',],
	['BGS_111','CORE_EX1_093','BG21_007','BGS_105','BGS_083','ICC_807','BG21_038',],
	['CORE_FP1_031','LOE_077','BGS_131','BGS_012','BGS_009','BG21_036','BGS_202','BGS_104',],
	['BGS_069','BGS_040','BG21_011','BGS_022',],
	]

BG_Minon_Gold={
	#Wrath Weaver	1	1	3	-	-
	'BGS_004':'TB_BaconUps_079',
	#Acolyte of C'Thun	2	2	3	-	Reborn
	'BGS_106':'TB_BaconUps_255',
	#Menagerie Mug	2	2	2	-	Battlecry
	'BGS_082':'TB_BaconUps_144',
	#Prophet of the Boar	2	3	3	-	Blood Gem
	'BG20_203':'BG20_203_G',
	#Selfless Hero	2	2	1	-	Deathrattle
	'OG_221':'TB_BaconUps_014',
	#Spawn of N'Zoth	2	2	2	-	Deathrattle
	'OG_256':'TB_BaconUps_025',
	#Unstable Ghoul	2	1	3	-	Deathrattle
	'FP1_024':'TB_BaconUps_118',
	#Whelp Smuggler	2	2	5	-	-
	'BG21_013':'BG21_013_G',
	#Arm of the Empire	3	4	4	-	Taunt
	'BGS_110':'TB_BaconUps_302',
	#Bird Buddy	3	2	4	-	Avenge (X)
	'BG21_002':'BG21_002_G',
	#Budding Greenthumb	3	1	4	-	Avenge (X)
	'BG21_030':'BG21_030_G',
	#Houndmaster	3	4	3	-	Battlecry
	'DS1_070':'TB_BaconUps_068',
	#Khadgar	3	2	2	-	-
	'DAL_575':'TB_BaconUps_034',
	#Soul Juggler	3	3	5	-	-
	'BGS_002':'TB_BaconUps_075',
	#Champion of Y'Shaarj	4	4	4	-	Taunt
	'BGS_111':'TB_BaconUps_301',
	#Defender of Argus	4	3	3	-	Battlecry
	'CORE_EX1_093':'TB_BaconUps_009',
	#Impatient Doomsayer	4	2	6	-	Avenge (X)
	'BG21_007':'BG21_007_G',
	#Majordomo Executus	4	6	3	-	-
	'BGS_105':'TB_BaconUps_207',
	#Menagerie Jug	4	3	3	-	Battlecry
	'BGS_083':'TB_BaconUps_145',
	#Strongshell Scavenger	4	2	3	-	Battlecry
	'ICC_807': 'TB_BaconUps_072',
	#Witchwing Nestmatron	4	3	5	-	Avenge (X)
	'BG21_038':'BG21_038_G',
	#Baron Rivendare	5	1	7	-	Deathrattle
	'CORE_FP1_031':'TB_BaconUps_055',
	#Brann Bronzebeard	5	2	4	-	Battlecry
	'LOE_077':'TB_BaconUps_045',
	#Deadly Spore	5	1	1	-	Poisonous
	'BGS_131':'TB_BaconUps_251',
	#Kangor's Apprentice	5	3	6	-	Deathrattle
	'BGS_012':'TB_BaconUps_087',
	#Lightfang Enforcer	5	2	2	-	-
	'BGS_009':'TB_BaconUps_082',
	#Master of Realities	5	6	6	-	Taunt
	'BG21_036':'BG21_036_G',
	#Mythrax the Unraveler	5	4	4	-	-
	'BGS_202':'TB_BaconUps_258',
	#Nomi, Kitchen Nightmare	5	4	4	-	-
	'BGS_104':'TB_BaconUps_201',
	#Amalgadon	6	6	6	*	Adapt
	'BGS_069':'TB_BaconUps_121',
	#Friend of a Friend	6	5	6	-	Battlecry
	'BG22_404':'BG22_404_G',#BAN
	#Nadina the Red	6	7	4	-	Deathrattle
	'BGS_040':'TB_BaconUps_154',
	#Seafood Slinger	6	5	5	-	Battlecry
	'BG21_011':'BG21_011_G',
	#Zapp Slywick	6	7	10	-	Windfury
	'BGS_022':'TB_BaconUps_091',	
	}

#Wrath Weaver	1	1	3	-	- BGS_004 TB_BaconUps_079 おりや
class BGS_004:# <12>[1453]
	""" Wrath Weaver
	After you play a Demon, deal 1 damage to your hero and gain +2/+2. """
	events = BG_Play(CONTROLLER, FRIENDLY + DEMON).after(Hit(FRIENDLY_HERO,1),Buff(SELF,'BGS_004e'))
	pass
BGS_004e=buff(2,2)# <12>[1453]
""" Wrath Woven
Increased stats. """
class TB_BaconUps_079:# <12>[1453]
	""" Wrath Weaver
	After you play a Demon, deal 1 damage to your hero and gain +4/+4. """
	events = Play(CONTROLLER, FRIENDLY_HAND + DEMON).after(Hit(FRIENDLY_HERO,1),Buff(SELF,'TB_BaconUps_079e'))
	pass
class TB_BaconUps_079e:# <12>[1453]
	""" Wrath Woven
	Increased stats. """
	#
	pass


#Acolyte of C'Thun	2	2	3	-	Reborn BGS_106 TB_BaconUps_255 クトゥーンのじさい
class BGS_106:# <12>[1453]
	""" Acolyte of C'Thun
	[Taunt][Reborn] """
	pass
class TB_BaconUps_255:# <12>[1453]
	""" Acolyte of C'Thun
	[Taunt][Reborn] """
	pass

#Menagerie Mug	2	2	2	-	Battlecry  BGS_082 TB_BaconUps_144
class BGS_082_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		controller = target
		field = controller.field
		flag = [0] * len(field)
		ret = []
		while True:
			if sum(flag)==len(field):
				break
			c =random.choice(field)
			addOK=True
			for d in ret:
				if c.race == d.race:
					flag[field.index(c)]=1
					addOK=False
					continue
			if addOK:
				ret.append(c)
				flag[field.index(c)]=1
			pass
		if len(ret)<=3:
			sample = ret
		else:
			sample = random.sample(ret,3)
		for c in sample:
			Buff(c,buff).trigger(source)

class BGS_082:# <12>[1453]
	""" Menagerie Mug
	[Battlecry:] Give 3 random friendly minions of different minion types +1/+1. """
	play = BGS_082_Action(CONTROLLER,'BGS_082e')
	pass
BGS_082e=buff(1,1)# <12>[1453]
""" Sip of Tea
+1/+1. """
class TB_BaconUps_144:# <12>[1453]
	""" Menagerie Mug
	[Battlecry:] Give 3 randomfriendly minions of differentminion types +2/+2. """
	play = BGS_082_Action(CONTROLLER,'TB_BaconUps_144e')
	pass
TB_BaconUps_144e=buff(2,2)# <12>[1453]
""" Sip of Tea
+2/+2. """



#Prophet of the Boar	2	3	3	-	Blood Gem BG20_203 BG20_203_G
class BG20_203_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		controller = target
		if controller.ActivateThisTurn==False:
			for repeat in range(amount):
				Give(controller, 'BG20_GEM')
				#.trigger(source)
			controller.ActivateThisTurn=True
class BG20_203:# <12>[1453]
	""" Prophet of the Boar
	[Once per Turn:] After you play a Quilboar, gain a [Blood Gem]. """
	events = [
		Play(CONTROLLER, QUILBOAR).after(BG20_203_Action(CONTROLLER, 1)),
		OWN_TURN_BEGIN.on(SetAttr(CONTROLLER, 'ActivateThisTurn', False))
		]
	pass
class BG20_203_G:# <12>[1453]
	""" Prophet of the Boar
	[Once per Turn:] After you play a Quilboar, gain 2 [Blood Gems]. """
	events = [
		Play(CONTROLLER, QUILBOAR).after(BG20_203_Action(CONTROLLER, 2)),
		OWN_TURN_BEGIN.on(SetAttr(CONTROLLER, 'ActivateThisTurn', False))
		]
	pass


#Selfless Hero	2	2	1	-	Deathrattle OG_221 TB_BaconUps_014　けんしん
## 動作確認済み
class OG_221:
	"""Selfless Hero:
	&lt;b&gt;Deathrattle:&lt;/b&gt; Give a random friendly minion &lt;b&gt;Divine Shield&lt;/b&gt;."""
	deathrattle = GiveDivineShield(RANDOM_FRIENDLY_MINION)
class TB_BaconUps_014:# <5>[1453]
	""" Selfless Hero
	[Deathrattle:] Give 2_random friendly minions [Divine Shield]. """
	deathrattle = GiveDivineShield(RANDOM_FRIENDLY_MINION) * 2
	pass



#Spawn of N'Zoth	2	2	2	-	Deathrattle　 OG_256 TB_BaconUps_025 んぞす
## 動作確認済み
class OG_256:
	""" Spawn of N'Zoth
	[Deathrattle:] Give your minions +1/+1. """
	deathrattle = Buff(FRIENDLY_MINIONS, 'OG_256e')#
	pass
OG_256e=buff(1,1)
class TB_BaconUps_025:# <12>[1453]
	""" Spawn of N'Zoth
	[Deathrattle:] Give your minions +2/+2. """
	deathrattle = Buff(FRIENDLY_MINIONS, 'TB_BaconUps_025e')#
	pass
TB_BaconUps_025e = buff(2,2)



#Unstable Ghoul	2	1	3	-	Deathrattle FP1_024  TB_BaconUps_118 ぐうる
class FP1_024:# <12>[1453]
	""" Unstable Ghoul
	&lt;b&gt;Taunt&lt;/b&gt;. &lt;b&gt;Deathrattle:&lt;/b&gt; Deal 1 damage to all minions. """
	deathrattle = Hit(ALL_MINIONS, 1)
	pass
class TB_BaconUps_118:# <12>[1453]
	""" Unstable Ghoul
	[Taunt][Deathrattle:] Deal 1 damage to all minions twice. """
	deathrattle = Hit(ALL_MINIONS, 1) * 2
	pass



#Whelp Smuggler	2	2	5	-	- BG21_013  BG21_013_G 密輸人
class BG21_013:# <12>[1453]
	""" Whelp Smuggler
	After a friendly Dragon gains Attack, give it +1_Health. """
	events = Buff(FRIENDLY + DRAGON).on(Buff(Buff.TARGET,'BG21_013e'))
	pass
BG21_013e=buff(0,1)
class BG21_013_G:# <12>[1453]
	""" Whelp Smuggler
	After a friendly Dragon gains Attack, give it +2_Health. """
	events = Buff(FRIENDLY + DRAGON).on(Buff(Buff.TARGET,'BG21_013e') * 2)
	pass


#Arm of the Empire	3	4	4	-	Taunt BGS_110  TB_BaconUps_302 
class BGS_110:# <12>[1453]
	""" Arm of the Empire
	Whenever a friendly [Taunt]minion is attacked,give it +2 Attackpermanently. """
	events = Attack(ENEMY_MINIONS, FRIENDLY_MINIONS+TAUNT).on(BuffPermanently(Attack.DEFENDER,'BGS_110e'))
	pass
BGS_110e=buff(2,0)# <12>[1453]
""" Armed!
+2 Attack """
class TB_BaconUps_302:# <12>[1453]
	""" Arm of the Empire
	Whenever a friendly [Taunt]minion is attacked,give it +4 Attackpermanently. """
	events = Attack(ENEMY_MINIONS, FRIENDLY_MINIONS+TAUNT).on(BuffPermanently(Attack.DEFENDER,'BGS_110e'))
	pass
TB_BaconUps_302e=buff(4,0)# <12>[1453]
""" Double Armed!
+4 Attack """


#Bird Buddy	3	2	4	-	Avenge (X)  BG21_002  BG21_002_G  愛鳥家
class BG21_002:# <12>[1453]
	""" Bird Buddy
	[Avenge (1):] Give your Beasts +1/+1. """
	events = Death(FRIENDLY).on(Avenge(SELF, 1, \
		[Buff(FRIENDLY_MINIONS + BEAST, 'BG21_002e')]\
		))
	pass
BG21_002e=buff(1,1)
""" Well Fed
+1/+1. """
class BG21_002_G:# <12>[1453]
	""" Bird Buddy
	[Avenge (1):] Give your Beasts +2/+2. """
	events = Death(FRIENDLY).on(Avenge(SELF, 1, \
		[Buff(FRIENDLY_MINIONS + BEAST, 'BG21_002_Ge')]\
		))
	pass
BG21_002_Ge=buff(2,2)# <12>[1453]
""" Well Fed
+2/+2. """



#Budding Greenthumb	3	1	4	-	Avenge (X)  BG21_030  BG21_030_G 栽培家
class BG21_030:# <12>[1453]
	""" Budding Greenthumb
	[Avenge (3):] Give adjacent minions +2/+1 permanently. """
	events = Death(FRIENDLY).on(Avenge(SELF, 3, [BuffPermanently(SELF_ADJACENT, 'BG21_030e')]))
	pass
BG21_030e=buff(2,1)
class BG21_030_G:# <12>[1453]
	""" Budding Greenthumb
	[Avenge (3):] Giveadjacent minions+4/+2 permanently. """
	events = Death(FRIENDLY).on(Avenge(SELF, 3, [BuffPermanently(SELF_ADJACENT, 'BG21_030_Ge')]))
	pass
BG21_030_Ge=buff(4,2)



#Houndmaster	3	4	3	-	Battlecry  DS1_070  TB_BaconUps_068 TB_BaconUps_068e 猟犬使い
class DS1_070:# <3>[1453]
	""" Houndmaster
	&lt;b&gt;Battlecry:&lt;/b&gt; Give a friendly Beast +2/+2 and &lt;b&gt;Taunt&lt;/b&gt;."""
	requirements = {
		PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0,PlayReq.REQ_MINION_TARGET:0, 
		}
	play = Buff(TARGET, 'DS1_070o')
	pass
DS1_070o=buff(2,2,taunt=True)
class TB_BaconUps_068:# <3>[1453]
	""" Houndmaster
	[Battlecry:] Give a friendly Beast +4/+4 and [Taunt]. """
	requirements = {
		PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0,PlayReq.REQ_MINION_TARGET:0, 
		}
	play = Buff(TARGET, 'TB_BaconUps_068e')
	pass
TB_BaconUps_068e=buff(2,2,taunt=True)# <3>[1453]
""" Master's Presence
+4/+4 and [Taunt]. """


#Khadgar	3	2	2	-	-  DAL_575 TB_BaconUps_034 カドガー 
class DAL_575:
	""" Khadgar
	Your cards that summon minions summon twice_as_many. """
	##############  infinite loop?
	events = Summon(FRIENDLY_MINIONS).after(SummonOnce(CONTROLLER, ExactCopy(Summon.CARD)))
	pass
class TB_BaconUps_034:# <4>[1453]
	""" Khadgar
	Your cards that summon minions summon three times as many. """
	events = Summon(FRIENDLY_MINIONS).after(SummonOnce(CONTROLLER, ExactCopy(Summon.CARD))*2)
	pass


#Soul Juggler	3	3	5	-	-  BGS_002  TB_BaconUps_075 ソールジャグラー
class BGS_002:# <9>[1453]
	""" Soul Juggler
	After a friendly Demon dies, deal 3 damage to a random enemy minion. """
	events = Death(FRIENDLY + DEMON).on(Hit(RANDOM(ENEMY_MINIONS), 3))
	pass
class TB_BaconUps_075:# <9>[1453]
	""" Soul Juggler
	After a friendly Demon dies, deal 3 damage to a random enemy minion twice. """
	events = Death(FRIENDLY + DEMON).on(Hit(RANDOM(ENEMY_MINIONS), 3) * 2)
	pass


#Champion of Y'Shaarj	4	4	4	-	Taunt  BGS_111 BGS_111e   TB_BaconUps_301 TB_BaconUps_301e
class BGS_111:# <12>[1453]  ヤシャラージュ
	""" Champion of Y'Shaarj
	Whenever a friendly [Taunt] minion is attacked, gain +1/+1 permanently. """
	events = Attack(ENEMY_MINIONS, FRIENDLY + TAUNT).on(BuffPermanently(SELF, 'BGS_111e'))
	pass
BGS_111e=buff(1,1)# <12>[1453]
""" Y'Shaarj!!!
+1/+1. """
class TB_BaconUps_301:# <12>[1453]
	""" Champion of Y'Shaarj
	Whenever a friendly [Taunt] minion is attacked, gain +2/+2 permanently. """
	events = Attack(ENEMY_MINIONS, FRIENDLY + TAUNT).on(BuffPermanently(SELF, 'TB_BaconUps_301e'))
	pass
TB_BaconUps_301e=buff(2,2)# <12>[1453]
""" Y'Shaarj!!!!!!
+2/+2. """



#Defender of Argus	4	3	3	-	Battlecry CORE_EX1_093  TB_BaconUps_009 
class CORE_EX1_093:# <12>[1453]   アルガス
	""" Defender of Argus
	[Battlecry:] Give adjacent minions +1/+1 and [Taunt]. """
	play = Buff(SELF_ADJACENT, 'EX1_093e')
	pass
EX1_093e=buff(1,1,taunt=True)
""" Hand of Argus
+2/+2 and [Taunt]. """
class TB_BaconUps_009:# <12>[1453]
	""" Defender of Argus
	[Battlecry:] Give adjacent minions +2/+2 and [Taunt]. """
	play = Buff(SELF_ADJACENT, 'TB_BaconUps_009e')
	pass
TB_BaconUps_009e=buff(2,2,taunt=True)# <12>[1453]
""" Hand of Argus
+2/+2 and [Taunt]. """


#Impatient Doomsayer	4	2	6	-	Avenge (X) BG21_007 BG21_007_G
class BG21_007:# <12>[1453]
	""" Impatient Doomsayer 終魔通予言者
	[Avenge (4):] Add a random Demon to your hand. """
	events = Death(FRIENDLY).on(Avenge(SELF, 4, [Give(CONTROLLER, RandomDemon())]))
	pass
class BG21_007_G:# <12>[1453]
	""" Impatient Doomsayer
	[Avenge (4):] Add 2 random Demons to your hand. """
	events = Death(FRIENDLY).on(Avenge(SELF, 4, [Give(CONTROLLER, RandomDemon()), Give(CONTROLLER, RandomDemon())]))
	pass


#Majordomo Executus	4	6	3	-	-  BGS_105  BGS_105e  TB_BaconUps_207
class BGS_105_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		if len(controller.field)>0:
			left_card = controller.field[0]
			count=1
			for card in controller.play_this_turn:
				if card.race==Race.ELEMENTAL:
					count += 1
			BGS_105e.atk=lambda self,i:i+1
			BGS_105e.max_health=lambda self,i:i+1
			for repeat in range(count):
				Buff(left_card, 'BGS_105e').trigger(source)
		pass
	pass
class BGS_105:# <12>[1453]
	""" Majordomo Executus エグゼクタス
	At the end of your turn, giveyour left-most minion +1/+1.Repeat for each Elementalyou played this turn. """
	events = OWN_TURN_END.on(BGS_105_Action(CONTROLLER))
	pass
class BGS_105e:# <12>[1453]
	""" Aegis of the Firelord
	Increased stats. """
	pass
class TB_BaconUps_207_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		if len(controller.field)>0:
			left_card = controller.field[0]
			count=1
			for card in controller.play_this_turn:
				if card.race==Race.ELEMENTAL:
					count += 1
			BGS_105e.atk=lambda self,i:i+2
			BGS_105e.max_health=lambda self,i:i+2
			for repeat in range(count):
				Buff(left_card, 'BGS_105e').trigger(source)
		pass
	pass
class TB_BaconUps_207:# <12>[1453]
	""" Majordomo Executus
	At the end of your turn, giveyour left-most minion +2/+2.Repeat for each Elementalyou played this turn. """
	#
	pass


#Menagerie Jug	4	3	3	-	Battlecry  BGS_083 BGS_083e  TB_BaconUps_145 TB_BaconUps_145e
class BGS_083:# <12>[1453] ミナジェリ
	""" Menagerie Jug
	[Battlecry:] Give 3 random friendly minions of different minion types +2/+2. """
	play = BGS_082_Action(CONTROLLER,'BGS_083e')
	pass
BGS_083e=buff(2,2)# <12>[1453]
""" Gulp of Tea
+2/+2. """
class TB_BaconUps_145:# <12>[1453]
	""" Menagerie Jug
	[Battlecry:] Give 3 randomfriendly minions of differentminion types +4/+4. """
	play = BGS_082_Action(CONTROLLER,'TB_BaconUps_145e')
	pass
TB_BaconUps_145e=buff(4,4)# <12>[1453]
""" Gulp of Tea
+4/+4. """



#Strongshell Scavenger	4	2	3	-	Battlecry  ICC_807  ICC_807e  TB_BaconUps_072 TB_BaconUps_072e
class ICC_807:# <2>[1453]
	""" Strongshell Scavenger  クズ拾い
	&lt;b&gt;Battlecry:&lt;/b&gt; Give your &lt;b&gt;Taunt&lt;/b&gt; minions +2/+2. """
	play = Buff(FRIENDLY + TAUNT, 'ICC_807e')
	pass
ICC_807e=buff(2,2)# <12>[1453]
""" Strongshell
+2/+2. """
class TB_BaconUps_072:# <2>[1453]
	""" Strongshell Scavenger
	[Battlecry:] Give your [Taunt] minions +4/+4. """
	play = Buff(FRIENDLY + TAUNT, 'TB_BaconUps_072e')
	pass
TB_BaconUps_072e=buff(4,4)# <12>[1453]
""" Strongshell
+4/+4. """


#Witchwing Nestmatron	4	3	5	-	Avenge (X)  BG21_038 BG21_038_G
class BG21_038:# <12>[1453] 巣母
	""" Witchwing Nestmatron
	[Avenge (3):] Add a random [Battlecry] minion to your_hand. """
	events = Death(FRIENDLY).on(Avenge(SELF, 3, [Give(CONTROLLER, RandomMinion(has_battlecry=True))]))
	pass
class BG21_038_G:# <12>[1453]
	""" Witchwing Nestmatron
	[Avenge (3):] Add 2 random [Battlecry] minions to your_hand. """
	events = Death(FRIENDLY).on(Avenge(SELF, 3, [Give(CONTROLLER, RandomMinion(has_battlecry=True)), Give(CONTROLLER, RandomMinion(has_battlecry=True))]))
	pass


#Baron Rivendare	5	1	7	-	Deathrattle  CORE_FP1_031 TB_BaconUps_055 ばろん
class CORE_FP1_031:
	"""Baron Rivendare
	Your minions trigger their &lt;b&gt;Deathrattles&lt;/b&gt; twice."""
	update = Refresh(CONTROLLER, {GameTag.EXTRA_DEATHRATTLES: True})
	pass
class TB_BaconUps_055:# <12>[1453]
	""" Baron Rivendare
	Your minions trigger their [Deathrattles] three times. """
	update = Refresh(CONTROLLER, {GameTag.EXTRA_DEATHRATTLES_ADDITIONAL: True})
	pass

#Brann Bronzebeard	5	2	4	-	Battlecry  LOE_077 LOE_077e  TB_BaconUps_045  TB_BaconUps_045e
class LOE_077:#    ぶらん
	""" Brann Bronzebeard
	Your &lt;b&gt;Battlecries&lt;/b&gt; trigger twice. """
	update = Refresh(CONTROLLER, {GameTag.EXTRA_BATTLECRIES_BASE: True})
	pass
class LOE_077e:# 
	""" Bronzebeard Battlecry
	Your &lt;b&gt;Battlecries&lt;/b&gt; trigger twice. """
	pass
class TB_BaconUps_045:# <12>[1453]
	""" Brann Bronzebeard
	Your [Battlecries] trigger three times. """
	update = Refresh(CONTROLLER, {GameTag.EXTRA_BATTLECRIES_ADDITIONAL: True})
	pass
class TB_BaconUps_045e:# <12>[1453]
	""" Bronzebeard Battlecry
	Your [Battlecries] trigger three times. """
	pass



#Deadly Spore	5	1	1	-	Poisonous BGS_131  TB_BaconUps_251
class BGS_131:# <12>[1453]
	""" Deadly Spore  横死の胞子
	[Poisonous] """
	pass
class TB_BaconUps_251:# <12>[1453]
	""" Deadly Spore
	[Poisonous] """
	pass



#Kangor's Apprentice	5	3	6	-	Deathrattle    BGS_012  TB_BaconUps_087
class BGS_012_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		controller = target
		cards = []
		for card in controller.death_log:
			if card.race == Race.MECHA:
				cards.append(card)
		for repeat in range(amount):
			if repeat<len(cards):
				Summon(controller, cards[repeat].id).trigger(source)
class BGS_012:# <12>[1453]   ケンゴー
	""" Kangor's Apprentice
	[Deathrattle]: Summon the first 2 friendly Mechs that died this combat. """
	deathrattle = BGS_012_Action(CONTROLLER, 2)
	pass
class TB_BaconUps_087:# <12>[1453]
	""" Kangor's Apprentice
	[Deathrattle]: Summon the first 4 friendly Mechs that died this combat. """
	deathrattle = BGS_012_Action(CONTROLLER, 4)
	#
	pass


#Lightfang Enforcer	5	2	2	-	-    BGS_009 BGS_009e  TB_BaconUps_082 TB_BaconUps_082e
class BGS_009_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		controller = target
		races=[]
		for card in controller.field:
			if card.race==Race.INVALID:
				pass
			elif card.race==Race.ALL:
				races.append(card.race)
			elif not card.race in races:
				races.append(card.race)
		buffsize = len(races)*amount
		BGS_009e.atk = lambda self,i:(i+buffsize)
		BGS_009e.max_health = lambda self,i:(i+buffsize)
		Buff(SELF, 'BGS_009e').trigger(source)
class BGS_009:# <12>[1453]  光牙
	""" Lightfang Enforcer
	At the end of your turn, give a friendly minion of each minion type +2/+2. """
	events = OWN_TURN_END.on(BGS_009_Action(CONTROLLER, 2))
	pass
class BGS_009e:# <7>[1453]
	""" Blessed
	Increased stats. """
class TB_BaconUps_082:# <12>[1453]
	""" Lightfang Enforcer
	At the end of your turn,give a friendly minionof each minion type+4/+4. """
	events = OWN_TURN_END.on(BGS_009_Action(CONTROLLER, 4))
	pass
class TB_BaconUps_082e:# <7>[1453]
	""" Blessed
	Increased stats. """



#Master of Realities	5	6	6	-	Taunt  BG21_036 BG21_036e BG21_036_G BG21_036_Ge
class BG21_036:# <12>[1453] 多重現実の支配者
	""" Master of Realities
	[[Taunt].] After a friendly Elemental gains stats, gain +1/+1. """
	events = Buff(FRIENDLY + ELEMENTAL).on(Buff(SELF,'BG21_036e'))
	pass
BG21_036e=buff(1,1)
class BG21_036_G:# <12>[1453]
	""" Master of Realities
	[[Taunt].] After a friendly Elemental gains stats, gain +2/+2. """
	events = Buff(FRIENDLY + ELEMENTAL).on(Buff(SELF,'BG21_036_Ge'))
	pass
BG21_036_Ge=buff(2,2)# <12>[1453]
""" The Elemental Plane
+2/+2. """



#Mythrax the Unraveler	5	4	4	-	-  BGS_202 BGS_202e TB_BaconUps_258 TB_BaconUps_258e
class BGS_202_Action(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	def do(self, source, target, buff):
		controller = target
		races=[]
		for card in controller.field:
			if card.race==Race.INVALID:
				pass
			elif card.race==Race.ALL:
				races.append(card.race)
			elif not card.race in races:
				races.append(card.race)
		buffsize = len(races)*amount
		for repeat in range(buffsize):
			Buff(source, buff).trigger(source)
class BGS_202:# <12>[1453] ミスラクス
	""" Mythrax the Unraveler
	At the end of your turn,gain +2/+2 for each__minion type you control. """
	events = OWN_TURN_END.on(BGS_202_Action(CONTROLLER, 'BGS_202e'))
	pass
BGS_202e=buff(2,2)# <12>[1453]
""" Void Echoes
+2/+2. """
class TB_BaconUps_258:# <12>[1453]
	""" Mythrax the Unraveler
	At the end of your turn,gain +4/+4 for each__minion type you control. """
	events = OWN_TURN_END.on(BGS_202_Action(CONTROLLER, 'TB_BaconUps_258e'))
	pass
TB_BaconUps_258e=buff(4,4)# <12>[1453]
""" Void Echoes
+4/+4. """





#Nomi, Kitchen Nightmare	5	4	4	-	-  BGS_104 BGS_104e1 BGS_104pe TB_BaconUps_201
class BGS_104_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		controller = target
		controller.nomi_powered_up += amount
		buffsize=controller.nomi_powered_up
		BGS_104pe.atk = lambda self,i:(i+buffsize)
		BGS_104pe.max_health= lambda self,i:(i+buffsize)
class BGS_104:# <12>[1453]  ノミ（🐼）
	""" Nomi, Kitchen Nightmare
	After you play an Elemental,Elementals in Bob's Tavern have +1/+1 for the restof the game. """
	events = Play(CONTROLLER, FRIENDLY_MINIONS + ELEMENTAL).on(BGS_104_Action(CONTROLLER, 1))
	pass
class BGS_104e1:# <12>[1453]
	""" Tavern Feast
	Increased stats. """
	pass
class BGS_104pe:# <12>[1453]
	""" Nomi Player Enchant
	Increased stats. """
	pass
class TB_BaconUps_201:# <12>[1453]
	""" Nomi, Kitchen Nightmare
	After you play an Elemental,Elementals in Bob's Tavernhave +2/+2 for the restof the game. """
	events = Play(CONTROLLER, FRIENDLY_MINIONS + ELEMENTAL).on(BGS_104_Action(CONTROLLER, 2))
	pass


#Amalgadon	6	6	6	*	Adapt  BGS_069 TB_BaconUps_121 
class BGS_069_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		controller = target
		races=[]
		for card in controller.field:
			if card.race==Race.INVALID:
				pass
			elif card.race==Race.ALL:
				races.append(card.race)
			elif not card.race in races:
				races.append(card.race)
		buffsize = len(races)*amount
		for repeat in range(buffsize):
			# adapting something
			num = random.choice([1,2,3,4,5,6])
			if num==1:
				source.atk += 3
			elif num==2:
				source.divine_shield = True
			elif num==3:
				source.taunt = True
			elif num==4:
				source.poinsonous = True
			elif num==5:
				source.windfury = True
			elif num==6:
				source.max_health += 3
		pass
class BGS_069:##  アマルガドン　(アルマゲドンではない）
	""" Amalgadon
	&lt;b&gt;Battlecry:&lt;/b&gt; For each different minion type you have among other minions, &lt;b&gt;Adapt&lt;/b&gt; randomly."""
	play = BGS_069_Action(CONTROLLER, 1)	
	pass
class TB_BaconUps_121:
	""" Amalgadon
	&lt;b&gt;Battlecry:&lt;/b&gt; For each different minion type you have among other minions, &lt;b&gt;Adapt&lt;/b&gt; randomly twice."""
	play = BGS_069_Action(CONTROLLER, 2)
	pass



#Friend of a Friend	(BAN)	6	5	6	-	Battlecry   BG22_404 BG22_404_G 
class BG22_404:# <12>[1453]　友達の友達　ばん！
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
class BGS_040:# <12>[1453]　　ナディナ
	""" Nadina the Red
	[Deathrattle:] Give your Dragons [Divine Shield]. """
	deathrattle = GiveDivineShield(FRIENDLY_MINIONS + DRAGON)
	pass
class TB_BaconUps_154:# <12>[1453]
	""" Nadina the Red
	[Deathrattle:] Give your Dragons [Divine Shield]. """
	deathrattle = GiveDivineShield(FRIENDLY_MINIONS + DRAGON)
	pass


#Seafood Slinger	6	5	5	-	Battlecry BG21_011 BG21_011e BG21_011e2 BG21_011_G BG21_011_Ge
class BG21_011:# <12>[1453]　板前
	""" Seafood Slinger
	[Battlecry:] Make a Murloc Golden. """
	requirements={
		PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.MURLOC }
	#play = GiveGoldCard(CONTROLLER, TARGET)
	pass
BG21_011e=buff(3,3)# <12>[1453] ??????????????
class BG21_011e2:# <12>[1453]  ??????????????
	""" Battlecry Self-Trigger [DNT]
	 """
	#
	pass
class BG21_011_G:# <12>[1453]
	""" Seafood Slinger
	[Battlecry:] Make a Murloc Golden. """
	requirements={
		PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.MURLOC }
	#play = GiveGoldCard(CONTROLLER, TARGET)
	pass
BG21_011_Ge=buff(6,6)# <12>[1453]  ????????????



#Zapp Slywick	6	7	10	-	Windfury  BGS_022 TB_BaconUps_091
class BGS_022:# <12>[1453]　ざっぷ
	""" Zapp Slywick
	[Windfury]This minion always attacks the enemy minion with the lowest Attack. """
	#<ReferencedTag enumID="189" name="WINDFURY" type="Int" value="1"/> ### REF-TAGだ！
	pass
class TB_BaconUps_091:# <12>[1453]
	""" Zapp Slywick
	[Mega-Windfury]This minion always attacksthe enemy minion withthe lowest Attack. """
	#<Tag enumID="189" name="WINDFURY" type="Int" value="3"/>　###これはオケ
	pass
