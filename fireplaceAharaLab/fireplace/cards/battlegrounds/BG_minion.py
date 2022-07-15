from ..utils import *

BG_Wrath_Weaver=True
BG_Acolyte_of_C_Thun=False##banned
BG_Menagerie_Mug=False##banned 23.6
BG_Prophet_of_the_Boar=True
BG_Selfless_Hero=True
BG_Spawn_of_N_Zoth=True
BG_Unstable_Ghoul=False
BG_Whelp_Smuggler=True
BG_Arm_of_the_Empire=True
BG_Bird_Buddy=True
BG_Budding_Greenthumb=False

BG_Minion=[
	
	'DS1_070','DS1_070o','TB_BaconUps_068','TB_BaconUps_068e',#Houndmaster	3
	'DAL_575','TB_BaconUps_034',#Khadgar	3
	'BGS_002','TB_BaconUps_075',#Soul Juggler	3
	##'BGS_111','BGS_111e','TB_BaconUps_301','TB_BaconUps_301e',#Champion of Y'Shaarj	4 ##banned 23.6
	#'EX1_093','EX1_093e','TB_BaconUps_009','TB_BaconUps_009e',#Defender of Argus	4 ##banned 23.6
	'BG21_007','BG21_007_G',#Impatient Doomsayer	4
	'BGS_105','BGS_105e','TB_BaconUps_207',#Majordomo Executus	4
	'BGS_083','BGS_083e','TB_BaconUps_145','TB_BaconUps_145e',#Menagerie Jug	4
	'ICC_807',  'ICC_807e',  'TB_BaconUps_072', 'TB_BaconUps_072e',#Strongshell Scavenger	4
	'BG21_038','BG21_038_G',#Witchwing Nestmatron	4
	'FP1_031','TB_BaconUps_055',#Baron Rivendare	5
	'LOE_077','LOE_077e','TB_BaconUps_045','TB_BaconUps_045e',#Brann Bronzebeard	5
	##'BGS_131','TB_BaconUps_251',#Deadly Spore	5 ##banned 23.6
	'BGS_012','TB_BaconUps_087',#Kangor's Apprentice	5
	'BGS_009','BGS_009e','TB_BaconUps_082','TB_BaconUps_082e',#Lightfang Enforcer	5
	'BG21_036','BG21_036e','BG21_036_G','BG21_036_Ge',#Master of Realities	5
	'BGS_202','BGS_202e','TB_BaconUps_258','TB_BaconUps_258e',#Mythrax the Unraveler	5
	'BGS_104','BGS_104e1','BGS_104pe','TB_BaconUps_201',#Nomi, Kitchen Nightmare	5
	##'BGS_069','TB_BaconUps_121',#Amalgadon	6 ##banned 22.3
	'BGS_040','TB_BaconUps_154',#Nadina the Red	6
	##'BG21_011','BG21_011e','BG21_011e2','BG21_011_G','BG21_011_Ge',#Seafood Slinger	6 ##banned 
	'BGS_022','TB_BaconUps_091',	#Zapp Slywick	6	
	### NEW CARDS ####
	'BG23_015','BG23_015t','BG23_015_G','BG23_015_Gt', #Orgozoa, the Tender 6  NEW 23.2
	'BG23_016','BG23_016_G', # Reef Explorer 4 NEW 23.2
	'BG23_018','BG23_018t','BG23_018_G', # Darkgaze Elder 6 NEW 23.2
	'BG23_318','BG23_318_G', # Leeroy the Reckless 5 NEW 23.2
	'BG23_Spellcraft_e',
	'GIL_681','BG_GIL_681_G', # Nightmare Amalgam 3 RENEW  23.2

	'BG23_352','BG23_352e','BG23_352_G','BG23_352_Ge',## Tavern Tipper (1) >= 23.6　#OK#
	'BG_CFM_063','BG_CFM_063e','BG_CFM_063_G',## Kooky Chemist (2) >= 23.6
	'BG_AT_069','BG_AT_069_G',## Sparring Partner (2) >= 23.6
	'BG23_350','BG23_350e','BG23_350_G','BG23_350_Ge',##  Yrel (2) >=23.6
	'BGS_029','BGS_029e','TB_BaconUps_095', ## Shifter Zerus (3) >=23.6
	'BG_DAL_775','BG_DAL_775_G', ## Tunnel Blaster (4) >= 23.6
	'BG23_190','BG23_190e','BG23_190_G','BG23_190_Ge', ## Uther the Lightbringer (6) >= 23.6
]

BG_PoolSet_Minion=[
	['BGS_004','BG23_352',],
	['BG20_203','OG_221','OG_256','BG21_013','BG_CFM_063','BG_AT_069','BG23_350',], #2 
	#banned 'BGS_106','BGS_082','FP1_024',
	['BGS_110','BG21_002','DS1_070','DAL_575','BGS_002','GIL_681','BGS_029',], #3 
	#banned 'BG21_030',
	['BG21_007','BGS_105','BGS_083','ICC_807','BG21_038','BG23_016','BG_DAL_775',], #4
	#banned 'BGS_111','EX1_093',
	['FP1_031','LOE_077','BGS_012','BGS_009','BG21_036','BGS_202','BGS_104','BG23_318',], #5 
	#banned 'BGS_131',
	['BGS_040','BGS_022','BG23_015','BG23_018','BG23_190',], #6 
	#banned 'BGS_069', 'BG21_011',
]


BG_Minon_Gold={
	

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
	'EX1_093':'TB_BaconUps_009',
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
	'FP1_031':'TB_BaconUps_055',
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
	'BG23_015':'BG23_015_G', #Orgozoa, the Tender 6  NEW
	'BG23_016':'BG23_016_G', # Reef Explorer 4 NEW
	'BG23_018':'BG23_018_G', # Darkgaze Elder 6 NEW
	'BG23_318':'BG23_318_G', # Leeroy the Reckless 5 NEW
	'GIL_681':'BG_GIL_681_G', # Nightmare Amalgam 3 RENEW
	'BG23_352':'BG23_352_G',## Tavern Tipper (1) >= 23.6
	'BG_CFM_063':'BG_CFM_063_G',## Kooky Chemist (2) >= 23.6
	'BG_AT_069':'BG_AT_069_G',## Sparring Partner (2) >= 23.6
	'BG23_350':'BG23_350_G',##  Yrel (2) >=23.6
	'BGS_029':'TB_BaconUps_095', ## Shifter Zerus (3) >=23.6
	'BG_DAL_775':'BG_DAL_775_G', ## Tunnel Blaster (4) >= 23.6
	'BG23_190':'BG23_190_G', ## Uther the Lightbringer (6) >= 	
	}


if BG_Wrath_Weaver:#Wrath Weaver	1	1	3	-	-
	BG_Minion += ['BGS_004','BGS_004e','TB_BaconUps_079','TB_BaconUps_079e',]#Wrath Weaver	1
	BG_PoolSet_Minion[1].append('BGS_004')
	BG_Minon_Gold['BGS_004']='TB_BaconUps_079'
	pass

#Wrath Weaver	1	1	3	 ### maybe ###
class BGS_004:# <12>[1453] おりや
	""" Wrath Weaver
	After you play a Demon, deal 1 damage to your hero and gain +2/+2. """
	events = BG_Play(CONTROLLER, FRIENDLY + DEMON).after(Hit(FRIENDLY_HERO,1),Buff(SELF,'BGS_004e'))
	pass
BGS_004e=buff(2,2)# <12>[1453]
""" Wrath Woven, Increased stats. """
class TB_BaconUps_079:# <12>[1453]
	""" Wrath Weaver
	After you play a Demon, deal 1 damage to your hero and gain +4/+4. """
	events = BG_Play(CONTROLLER, FRIENDLY + DEMON).after(Hit(FRIENDLY_HERO,1),Buff(SELF,'TB_BaconUps_079e'))
	pass
TB_BaconUps_079e=buff(4,4)# <12>[1453]
""" Wrath Woven,	Increased stats. """



if BG_Acolyte_of_C_Thun:#Acolyte of C'Thun	2	2	3
	BG_Minion += ['BGS_106','TB_BaconUps_255',]#	1
	BG_PoolSet_Minion[2].append('BGS_106')
	BG_Minon_Gold['BGS_106']='TB_BaconUps_255'
	pass
#,#Acolyte of C'Thun	2 ##banned 23.6
class BGS_106:# <12>[1453] クトゥーンのじさい
	""" Acolyte of C'Thun
	[Taunt][Reborn] """
	pass
class TB_BaconUps_255:# <12>[1453]
	""" Acolyte of C'Thun
	[Taunt][Reborn] """
	pass



if BG_Menagerie_Mug:#Menagerie Mug	2	2	2
	BG_Minion += ['BGS_082','BGS_082e','TB_BaconUps_144','TB_BaconUps_144e',]#	1
	BG_PoolSet_Minion[2].append('BGS_082')
	BG_Minon_Gold['BGS_082']='TB_BaconUps_144'
	pass
#Menagerie Mug	2	2	2	-		 ### OK ###
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
				flag[field.index(c)]=1
				if c.race != Race.INVALID:
					ret.append(c)
			pass
		if len(ret)<=3:
			sample = ret
		else:
			sample = random.sample(ret,3)
		for c in sample:
			Buff(c,buff).trigger(source)

class BGS_082:# <12>[1453]
	""" Menagerie Mug マナジェリ
	[Battlecry:] Give 3 random friendly minions of different minion types +1/+1. """
	play = BGS_082_Action(CONTROLLER,'BGS_082e')
	pass
BGS_082e=buff(1,1)# <12>[1453]
""" Sip of Tea, +1/+1. """
class TB_BaconUps_144:# <12>[1453]
	""" Menagerie Mug
	[Battlecry:] Give 3 randomfriendly minions of differentminion types +2/+2. """
	play = BGS_082_Action(CONTROLLER,'TB_BaconUps_144e')
	pass
TB_BaconUps_144e=buff(2,2)# <12>[1453]
""" Sip of Tea, +2/+2. """



if BG_Prophet_of_the_Boar:#Prophet of the Boar	2	3	3
	BG_Minion += ['BG20_203','BG20_203_G',]#	1
	BG_PoolSet_Minion[2].append('BG20_203')
	BG_Minon_Gold['BG20_203']='BG20_203_G'
	pass
#Prophet of the Boar	2	3	3	-		 ### OK ###
class BG20_203_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		controller = target
		if controller.once_per_turn==0:
			for repeat in range(amount):
				Give(controller, 'BG20_GEM').trigger(source)
			controller.once_per_turn=1
class BG20_203:# <12>[1453]
	""" Prophet of the Boar
	[Once per Turn:] After you play a Quilboar, gain a [Blood Gem]. """
	events = [
		BG_Play(CONTROLLER, QUILBOAR).after(BG20_203_Action(CONTROLLER, 1)),
		BeginBar(CONTROLLER).on(SetAttr(CONTROLLER, 'once_per_turn', 0))
		]
	pass
class BG20_203_G:# <12>[1453]
	""" Prophet of the Boar
	[Once per Turn:] After you play a Quilboar, gain 2 [Blood Gems]. """
	events = [
		BG_Play(CONTROLLER, QUILBOAR).after(BG20_203_Action(CONTROLLER, 2)),
		BeginBar.on(SetAttr(CONTROLLER, 'once_per_turn', 0))
		]
	pass



if BG_Selfless_Hero:#Selfless Hero	2	2	1
	BG_Minion += ['OG_221','TB_BaconUps_014',]#	
	BG_PoolSet_Minion[2].append('OG_221')
	BG_Minon_Gold['OG_221']='TB_BaconUps_014'
	pass
#Selfless Hero	2	2	1	-	### OK ###
### 基本的にはこれでよいと思うが、 RANDOM(FRIENDLY_MINIONS - DIVINE_SHIELD)
###のほうが筋だと思う。
class OG_221:
	"""Selfless Hero:  けんしん
	<b>Deathrattle:</b> Give a random friendly minion <b>Divine Shield</b>."""
	deathrattle = GiveDivineShield(RANDOM_FRIENDLY_MINION)
class TB_BaconUps_014:# <5>[1453]
	""" Selfless Hero
	[Deathrattle:] Give 2_random friendly minions [Divine Shield]. """
	deathrattle = GiveDivineShield(RANDOM_FRIENDLY_MINION) * 2
	pass




if BG_Spawn_of_N_Zoth:#Spawn of N'Zoth	2	2	2	-　### OK ###
	BG_Minion += ['OG_256','OG_256e','TB_BaconUps_025','TB_BaconUps_025e',]#	
	BG_PoolSet_Minion[2].append('OG_256')
	BG_Minon_Gold['OG_256']='TB_BaconUps_025'
	pass
class OG_256:#　んぞす
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



if BG_Unstable_Ghoul:#Unstable Ghoul	2	1	3	-### OK ### ##banned 23.6
	BG_Minion += ['FP1_024','TB_BaconUps_118',]#	
	BG_PoolSet_Minion[2].append('FP1_024')
	BG_Minon_Gold['FP1_024']='TB_BaconUps_118'
	pass
class FP1_024:# <12>[1453] ぐうる
	""" Unstable Ghoul
	<b>Taunt</b>. <b>Deathrattle:</b> Deal 1 damage to all minions. """
	deathrattle = Hit(ALL_MINIONS, 1),Deaths()
	pass
class TB_BaconUps_118:# <12>[1453]
	""" Unstable Ghoul
	[Taunt][Deathrattle:] Deal 1 damage to all minions twice. """
	deathrattle = Hit(ALL_MINIONS, 1), Hit(ALL_MINIONS, 1), Deaths()
	pass



if BG_Whelp_Smuggler:#Whelp Smuggler	2	2	5	- ### OK ###
	BG_Minion += ['BG21_013','BG21_013e','BG21_013_G',]#	
	BG_PoolSet_Minion[2].append('BG21_013')
	BG_Minon_Gold['BG21_013']='BG21_013_G'
	pass
class BG21_013_Action(TargetedAction):## 密輸人
	TARGET = ActionArg()
	BUFF = ActionArg()
	TARGETBUFF = ActionArg()
	def do(self, source, target, buff, targetbuff):
		if buff.atk>0:
			Buff(target, targetbuff).trigger(target.controller)
			pass
class BG21_013:# <12>[1453]
	""" Whelp Smuggler
	After a friendly Dragon gains Attack, give it +1_Health. """
	events = Buff(FRIENDLY + DRAGON).on(BG21_013_Action(Buff.TARGET, Buff.BUFF, 'BG21_013e'))
	pass
BG21_013e=buff(0,1)
class BG21_013_G:# <12>[1453]
	""" Whelp Smuggler
	After a friendly Dragon gains Attack, give it +2_Health. """
	events = Buff(FRIENDLY + DRAGON).on(BG21_013_Action(Buff.TARGET, Buff.BUFF,'BG21_013e') * 2)
	pass




if BG_Arm_of_the_Empire:#Arm of the Empire	3	4	4	-		 ### maybe ###
	BG_Minion += ['BGS_110','BGS_110e','TB_BaconUps_302','TB_BaconUps_302e',]#	
	BG_PoolSet_Minion[3].append('BGS_110')
	BG_Minon_Gold['BGS_110']='TB_BaconUps_302'
	pass
class BGS_110:# <12>[1453] 帝国の腕
	""" Arm of the Empire
	Whenever a friendly [Taunt]minion is attacked,give it +2 Attack　permanently. """
	events = BG_Attack(ENEMY, FRIENDLY + TAUNT).on(BuffPermanently(BG_Attack.OTHER,'BGS_110e'))
	pass
BGS_110e=buff(2,0)# <12>[1453]
""" Armed!, +2 Attack """
class TB_BaconUps_302:# <12>[1453]
	""" Arm of the Empire
	Whenever a friendly [Taunt]minion is attacked,give it +4 Attackpermanently. """
	events = BG_Attack(ENEMY, FRIENDLY + TAUNT).on(BuffPermanently(BG_Attack.OTHER,'TB_BaconUps_302e'))
	pass
TB_BaconUps_302e=buff(4,0)# <12>[1453]
""" Double Armed!, +4 Attack """



if BG_Bird_Buddy:#Bird Buddy	3	2	4	-		 ### maybe ###
	BG_Minion += ['BG21_002','BG21_002e','BG21_002_G','BG21_002_Ge',]#	
	BG_PoolSet_Minion[3].append('BG21_002')
	BG_Minon_Gold['BG21_002']='BG21_002_G'
	pass
class BG21_002:# <12>[1453]  愛鳥家
	""" Bird Buddy
	[Avenge (1):] Give your Beasts +1/+1. """
	events = Death(FRIENDLY).on(Avenge(SELF, 1, \
		[Buff(FRIENDLY_MINIONS + BEAST, 'BG21_002e')]\
		))
	pass
BG21_002e=buff(1,1)
""" Well Fed, +1/+1. """
class BG21_002_G:# <12>[1453]
	""" Bird Buddy
	[Avenge (1):] Give your Beasts +2/+2. """
	events = Death(FRIENDLY).on(Avenge(SELF, 1, \
		[Buff(FRIENDLY_MINIONS + BEAST, 'BG21_002_Ge')]\
		))
	pass
BG21_002_Ge=buff(2,2)# <12>[1453]
""" Well Fed,  +2/+2. """



if BG_Budding_Greenthumb:#Budding Greenthumb	3	1	4	-	 	 ### maybe ###
	BG_Minion += ['BG21_030','BG21_030e','BG21_030_G','BG21_030_Ge',]#	
	BG_PoolSet_Minion[3].append('BG21_030')
	BG_Minon_Gold['BG21_030']='BG21_030_G'
	pass
class BG21_030:# <12>[1453]  栽培家
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



#Houndmaster	3	4	3	-		 ### maybe ###
class DS1_070:# <3>[1453] 猟犬使い
	""" Houndmaster
	<b>Battlecry:</b> Give a friendly Beast +2/+2 and <b>Taunt</b>."""
	requirements = {
		PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0,PlayReq.REQ_MINION_TARGET:0, 
		PlayReq.REQ_TARGET_WITH_RACE:Race.BEAST }
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
TB_BaconUps_068e=buff(4,4,taunt=True)# <3>[1453]
""" Master's Presence, +4/+4 and [Taunt]. """


#Khadgar	3	2	2	-	  	 ### maybe ###
class DAL_575:#カドガー
	""" Khadgar
	Your cards that summon minions summon twice_as_many. """
	##############  infinite loop?
	events = Summon(CONTROLLER, FRIENDLY_MINIONS).after(SummonOnce(CONTROLLER, ExactCopy(Summon.CARD)))
	pass
class TB_BaconUps_034:# <4>[1453]
	""" Khadgar
	Your cards that summon minions summon three times as many. """
	events = Summon(CONTROLLER, FRIENDLY_MINIONS).after(SummonOnce(CONTROLLER, ExactCopy(Summon.CARD))*2)
	pass


#Soul Juggler	3	3	5	-	 	 ### maybe ###
class BGS_002:# <9>[1453] ソールジャグラー
	""" Soul Juggler
	After a friendly Demon dies, deal 3 damage to a random enemy minion. """
	events = Death(FRIENDLY + DEMON).on(Hit(RANDOM(ENEMY_MINIONS), 3))
	pass
class TB_BaconUps_075:# <9>[1453]
	""" Soul Juggler
	After a friendly Demon dies, deal 3 damage to a random enemy minion twice. """
	events = Death(FRIENDLY + DEMON).on(Hit(RANDOM(ENEMY_MINIONS), 3) * 2)
	pass



#Champion of Y'Shaarj	4	4	4		 ### maybe ###
#class BGS_111:# <12>[1453]  ヤシャラージュ
#	""" Champion of Y'Shaarj
#	Whenever a friendly [Taunt] minion is attacked, gain +1/+1 permanently. """
#	events = BG_Attack(ENEMY, FRIENDLY + TAUNT).on(BuffPermanently(SELF, 'BGS_111e'))
#	pass
#BGS_111e=buff(1,1)# <12>[1453]
#""" Y'Shaarj!!!,  +1/+1. """
#class TB_BaconUps_301:# <12>[1453]
#	""" Champion of Y'Shaarj
#	Whenever a friendly [Taunt] minion is attacked, gain +2/+2 permanently. """
#	events = BG_Attack(ENEMY, FRIENDLY + TAUNT).on(BuffPermanently(SELF, 'TB_BaconUps_301e'))
#	pass
#TB_BaconUps_301e=buff(2,2)# <12>[1453]
""" Y'Shaarj!!!!!!,  +2/+2. """



#Defender of Argus	4	3	3	 	 ### OK ###
class EX1_093:# <12>[1453]   アルガス
	""" Defender of Argus
	[Battlecry:] Give adjacent minions +1/+1 and [Taunt]. """
	play = Buff(SELF_ADJACENT, 'EX1_093e')
	pass
EX1_093e=buff(1,1,taunt=True)
""" Hand of Argus, +2/+2 and [Taunt]. """
class TB_BaconUps_009:# <12>[1453]
	""" Defender of Argus
	[Battlecry:] Give adjacent minions +2/+2 and [Taunt]. """
	play = Buff(SELF_ADJACENT, 'TB_BaconUps_009e')
	pass
TB_BaconUps_009e=buff(2,2,taunt=True)# <12>[1453]
""" Hand of Argus,  +2/+2 and [Taunt]. """


#Impatient Doomsayer	4	2	6		 ### maybe ###
class BG21_007:# <12>[1453]  終魔通予言者
	""" Impatient Doomsayer
	[Avenge (4):] Add a random Demon to your hand. """
	events = Death(FRIENDLY).on(Avenge(SELF, 4, [Give(CONTROLLER, RandomBGDemon())]))
	pass
class BG21_007_G:# <12>[1453]
	""" Impatient Doomsayer
	[Avenge (4):] Add 2 random Demons to your hand. """
	events = Death(FRIENDLY).on(Avenge(SELF, 4, [Give(CONTROLLER, RandomBGDemon()), Give(CONTROLLER, RandomBGDemon())]))
	pass


#Majordomo Executus	4	6	3		 ### OK ###
class BGS_105_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		if len(controller.field)>0:
			left_card = controller.field[0]
			count=1
			for card in controller.play_this_turn:
				if card.type==CardType.MINION and card.race==Race.ELEMENTAL:
					count += 1
			Buff(left_card, 'BGS_105e', atk=count, max_health=count).trigger(source)
		pass
	pass
class BGS_105:# <12>[1453]
	""" Majordomo Executus エグゼクタス
	At the end of your turn, give your left-most minion +1/+1. Repeat for each Elementalyou played this turn. """
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
				if  card.type==CardType.MINION and card.race==Race.ELEMENTAL:
					count += 1
			Buff(left_card, 'BGS_105e', atk=count*2, max_health=count*2).trigger(source)
		pass
	pass
class TB_BaconUps_207:# <12>[1453]
	""" Majordomo Executus
	At the end of your turn, giveyour left-most minion +2/+2.Repeat for each Elementalyou played this turn. """
	events = OWN_TURN_END.on(TB_BaconUps_207_Action(CONTROLLER))



#Menagerie Jug	4	3	3	-		 ### maybe ###
class BGS_083:# <12>[1453] ミナジェリ
	""" Menagerie Jug
	[Battlecry:] Give 3 random friendly minions of different minion types +2/+2. """
	play = BGS_082_Action(CONTROLLER,'BGS_083e')
	pass
BGS_083e=buff(2,2)# <12>[1453]
""" Gulp of Tea,  +2/+2. """
class TB_BaconUps_145:# <12>[1453]
	""" Menagerie Jug
	[Battlecry:] Give 3 randomfriendly minions of differentminion types +4/+4. """
	play = BGS_082_Action(CONTROLLER,'TB_BaconUps_145e')
	pass
TB_BaconUps_145e=buff(4,4)# <12>[1453]
""" Gulp of Tea,  +4/+4. """



#Strongshell Scavenger	4	2	3		 ### OK ###
class ICC_807:# <2>[1453]  クズ拾い
	""" Strongshell Scavenger
	<b>Battlecry:</b> Give your <b>Taunt</b> minions +2/+2. """
	play = Buff(FRIENDLY + TAUNT, 'ICC_807e')
	pass
ICC_807e=buff(2,2)# <12>[1453]
""" Strongshell,  +2/+2. """
class TB_BaconUps_072:# <2>[1453]
	""" Strongshell Scavenger
	[Battlecry:] Give your [Taunt] minions +4/+4. """
	play = Buff(FRIENDLY + TAUNT, 'TB_BaconUps_072e')
	pass
TB_BaconUps_072e=buff(4,4)# <12>[1453]
""" Strongshell,  +4/+4. """


#Witchwing Nestmatron	4	3	5		 ### maybe ###
class BG21_038:# <12>[1453] 巣母
	""" Witchwing Nestmatron
	[Avenge (3):] Add a random [Battlecry] minion to your_hand. """
	events = Death(FRIENDLY).on(Avenge(SELF, 3, [Give(CONTROLLER, RandomBGMinion(has_battlecry=True))]))
	pass
class BG21_038_G:# <12>[1453]
	""" Witchwing Nestmatron
	[Avenge (3):] Add 2 random [Battlecry] minions to your_hand. """
	events = Death(FRIENDLY).on(Avenge(SELF, 3, [Give(CONTROLLER, RandomBGMinion(has_battlecry=True)), Give(CONTROLLER, RandomMinion(has_battlecry=True))]))
	pass


#Baron Rivendare	5	1	7		 ### maybe ###
class FP1_031:# ばろん
	"""Baron Rivendare
	Your minions trigger their <b>Deathrattles</b> twice."""
	update = Refresh(CONTROLLER, {GameTag.EXTRA_DEATHRATTLES: True})
	pass
class TB_BaconUps_055:# <12>[1453]
	""" Baron Rivendare
	Your minions trigger their [Deathrattles] three times. """
	update = Refresh(CONTROLLER, {GameTag.EXTRA_DEATHRATTLES_ADDITIONAL: True})
	pass


#Brann Bronzebeard	5	2	4		 ### maybe ###
class LOE_077:#    ぶらん
	""" Brann Bronzebeard
	Your <b>Battlecries</b> trigger twice. """
	update = Refresh(CONTROLLER, {GameTag.EXTRA_BATTLECRIES_BASE: True})
	pass
class LOE_077e:# 
	""" Bronzebeard Battlecry
	Your <b>Battlecries</b> trigger twice. """
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



##Deadly Spore	5	1	1		 ### OK ###
#class BGS_131:# <12>[1453]  横死の胞子
#	""" Deadly Spore
#	[Poisonous] """
#	pass
#class TB_BaconUps_251:# <12>[1453]
#	""" Deadly Spore
#	[Poisonous] """
#	pass



#Kangor's Apprentice	5	3	6		 ### maybe ###
class BGS_012_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		controller = target
		cards = []
		for card in controller.death_log:
			if card.race == Race.MECHANICAL:
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


#Lightfang Enforcer	5	2	2		 ### need check ###
class BGS_009_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		races=[]
		cards=[]
		for card in controller.field:
			if card.race==Race.INVALID:
				pass
			elif card.race==Race.ALL:
				races.append(card.race)
				cards.append(card)
			elif not card.race in races:
				races.append(card.race)
				cards.append(card)
		for card in cards:
			Buff(source, 'BGS_009e').trigger(source)
class BGS_009:# <12>[1453]  光牙
	""" Lightfang Enforcer
	At the end of your turn, give a friendly minion of each minion type +2/+2. """
	events = OWN_TURN_END.on(BGS_009_Action(CONTROLLER))
	pass
BGS_009e=buff(2,2)# <7>[1453]
""" Blessed,	Increased stats. """
class TB_BaconUps_082:# <12>[1453]
	""" Lightfang Enforcer
	At the end of your turn,give a friendly minionof each minion type+4/+4. """
	events = OWN_TURN_END.on(BGS_009_Action(CONTROLLER, 4))
	pass
class TB_BaconUps_082e:# <7>[1453]
	""" Blessed
	Increased stats. """



#Master of Realities	5	6	6	-		 ### maybe ###
class BG21_036_Action(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	TARGETBUFF = ActionArg()
	def do(self, source, target, buff, targetbuff):
		if buff.atk>0 or buff.health>0:
			Buff(target, targetbuff).trigger(target.controller)
class BG21_036:# <12>[1453] 多重現実の支配者
	""" Master of Realities
	[[Taunt].] After a friendly Elemental gains stats, gain +1/+1. """
	events = Buff(FRIENDLY + ELEMENTAL).on(BG21_036_Action(SELF, Buff.BUFF, 'BG21_036e'))
	pass
BG21_036e=buff(1,1)
class BG21_036_G:# <12>[1453]
	""" Master of Realities
	[[Taunt].] After a friendly Elemental gains stats, gain +2/+2. """
	events = Buff(FRIENDLY + ELEMENTAL).on(BG21_036_Action(SELF, Buff.BUFF, 'BG21_036_Ge'))
	pass
BG21_036_Ge=buff(2,2)# <12>[1453]
""" The Elemental Plane, +2/+2. """



#Mythrax the Unraveler	5	4	4		 ### maybe ###
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
		buffsize = len(races)
		for repeat in range(buffsize):
			Buff(source, buff).trigger(source)
class BGS_202:# <12>[1453] ミスラクス
	""" Mythrax the Unraveler
	At the end of your turn,gain +2/+2 for each__minion type you control. """
	events = OWN_TURN_END.on(BGS_202_Action(CONTROLLER, 'BGS_202e'))
	pass
BGS_202e=buff(2,2)# <12>[1453]
""" Void Echoes, +2/+2. """
class TB_BaconUps_258:# <12>[1453]
	""" Mythrax the Unraveler
	At the end of your turn,gain +4/+4 for each__minion type you control. """
	events = OWN_TURN_END.on(BGS_202_Action(CONTROLLER, 'TB_BaconUps_258e'))
	pass
TB_BaconUps_258e=buff(4,4)# <12>[1453]
""" Void Echoes, +4/+4. """




#Nomi, Kitchen Nightmare	5	4	4	### OK ###
class BGS_104_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		controller = target
		controller.nomi_powered_up += amount
class BGS_104:# <12>[1453]  ノミ（🐼）
	""" Nomi, Kitchen Nightmare
	After you play an Elemental,Elementals in Bob's Tavern have +1/+1 for the restof the game. """
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(BGS_104_Action(CONTROLLER, 1))
	pass
class BGS_104e1:# <12>[1453]
	""" Tavern Feast
	Increased stats. """
BGS_104pe=buff(1,1)# <12>[1453]
""" Nomi Player Enchant
Increased stats. """
class TB_BaconUps_201:# <12>[1453]
	""" Nomi, Kitchen Nightmare
	After you play an Elemental,Elementals in Bob's Tavernhave +2/+2 for the restof the game. """
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(BGS_104_Action(CONTROLLER, 2))
	pass


#Amalgadon	6	6	6	*	 	 ### need check ###  banned
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
			buff = random.choice(['UNG_999t2e','UNG_999t3e','UNG_999t4e','UNG_999t6e','UNG_999t7e','UNG_999t8e','UNG_999t13e','UNG_999t14e'])
			Buff(source, buff).trigger(source)
		pass
class BGS_069:##  アマルガドン　(アルマゲドンではない）
	""" Amalgadon
	<b>Battlecry:</b> For each different minion type you have among other minions, <b>Adapt</b> randomly."""
	play = BGS_069_Action(CONTROLLER, 1)	
	pass
class TB_BaconUps_121:
	""" Amalgadon
	<b>Battlecry:</b> For each different minion type you have among other minions, <b>Adapt</b> randomly twice."""
	play = BGS_069_Action(CONTROLLER, 2)
	pass

UNG_999t14e=buff(1,1)## 火山の力 ## +1/+1
UNG_999t13e=buff(poisonous=True)## 猛毒の唾 ## 猛毒
#class UNG_999t10e:## 霧隠れ ## 次の自分のターンまで隠れ身状態。
class UNG_999t8e:## 電気の盾 # 聖なる盾
	def apply(self,target):
		target.divine_shield=True
		pass
UNG_999t7e=buff(windfury=True)## 電光石火 # 疾風
UNG_999t6e=buff(taunt=True)## 巨体 # 挑発
#class UNG_999t5e:## 液状膜 ## 呪文とヒーローパワーの標的にならない。
UNG_999t4e=buff(0,3)## 岩状の甲殻 ## 体力+3
UNG_999t3e=buff(3,0)## 炎熱の爪 ##攻撃力+3
class UNG_999t2e:## 動き回る胞子 ##;断末魔:</b>1/1の植物を2体召喚する。
	tags={GameTag.DEATHRATTLE:True}
	deathrattle=Summon(CONTROLLER, 'UNG_999t2t1')*2
class UNG_999t2t1:## 植物
	""" """




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



#Nadina the Red	6	7	4		 ### maybe OK ###
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


#Seafood Slinger	6	5	5		 ### maybe ###
#class BG21_011:# <12>[1453]　板前
#	""" Seafood Slinger
#	[Battlecry:] Make a Murloc Golden. """
#	requirements={
#		PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.MURLOC }
#	play = MorphGold(TARGET)
#	pass
#BG21_011e=buff(3,3)# <12>[1453] ??????????????
#class BG21_011e2:# <12>[1453]  ??????????????
#	""" Battlecry Self-Trigger [DNT] """
#class BG21_011_G:# <12>[1453]
#	""" Seafood Slinger
#	[Battlecry:] Make a Murloc Golden. """
#	requirements={
#		PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.MURLOC }
#	play = MorphGold(TARGET)
#	pass
#BG21_011_Ge=buff(6,6)# <12>[1453]  ????????????



#Zapp Slywick	6	7	10	 	 ### maybe ###
class BGS_022:# <12>[1453]　ざっぷ
	""" Zapp Slywick
	[Windfury]This minion always attacks the enemy minion with the lowest Attack. """
	#<ReferencedTag enumID="189" name="WINDFURY" type="Int" value="1"/> ### REF-TAGだ！
	tags = {GameTag.WINDFURY:1}
	#本体実装はBG_Battle.pyの80行あたり
	pass
class TB_BaconUps_091:# <12>[1453]
	""" Zapp Slywick
	[Mega-Windfury]This minion always attacksthe enemy minion withthe lowest Attack. """
	#<Tag enumID="189" name="WINDFURY" type="Int" value="3"/>　###これはオケ
	pass


### Orgozoa, the Tender(6) ### OK ###
class BG23_015:# <12>[1453]
	""" Orgozoa, the Tender(6)
	&lt;b&gt;Spellcraft: Discover&lt;/b&gt; a Naga."""
	play = Spellcraft(CONTROLLER,'BG23_015t')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG23_015t'))
	tags={2359:'BG23_015t'}
class BG23_015t:
	play = Discover(CONTROLLER, RandomBGNaga(tech_level_less=TIER(CONTROLLER)))
	tags = {GameTag.TECH_LEVEL:5}
	class Hand:
		events = EndTurn(CONTROLLER).on(Destroy(SELF))
pass
class BG23_015_G:# <12>[1453]
	"""
	&lt;b&gt;Spellcraft: Discover&lt;/b&gt; 2 Naga.</enUS>"""
	play = Spellcraft(CONTROLLER,'BG23_015_Gt')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG23_015_Gt'))
	tags={2359:'BG23_015_Gt'}
	pass
class BG23_015_Gt:
	play = DiscoverTwice(CONTROLLER, RandomBGNaga(tech_level_less=TIER(CONTROLLER))*3)
	class Hand:
		events = EndTurn(CONTROLLER).on(Destroy(SELF))
	pass


### Reef Explorer(4) ### regular card OK, gold card NOT YET ###
### WARNING  : we must exclude all of banned cards
class BG23_016_Choice(Choice):
	def get_args(self, source):
		player, cards = super().get_args(source)
		controller = source.controller
		for fcard in controller.field:
			exclude_race = fcard.race
			for card in reversed(cards):
				if card.race==exclude_race:
					cards.remove(card)
			pass
		if len(cards)>0:
			if len(cards)>3:
				cards = random.sample(cards,3)
		return player, cards
	def choose(self, card):
		super().choose(card)
		if Config.LOGINFO:
			print("(BG23_016_Choice.choose)%s chooses %r"%(card.controller.name, card))
		card.zone=Zone.HAND
class BG23_016:# <12>[1453]
	""" Reef Explorer(4)
	&lt;b&gt;Battlecry: Discover&lt;/b&gt; a minion from a minion type you don't control."""
	play = BG23_016_Choice(CONTROLLER, RandomBGMinion(tech_level_less=TIER(CONTROLLER))*12)
	pass
class BG23_016_G_Choice(DiscoverTwice):
	def get_args(self, source):
		player, cards = super().get_args(source)
		controller = source.controller
		for fcard in controller.field:
			exclude_race = fcard.race
			for card in reversed(cards):
				if card.race==exclude_race:
					cards.remove(card)
			pass
		if len(cards)>0:
			if len(cards)>3:
				cards = random.sample(cards,3)
		return player, cards
class BG23_016_G:# <12>[1453]
	"""
	&lt;b&gt;Battlecry: Discover&lt;/b&gt; 2 minions from minion types you don't control."""
	play = BG23_016_G_Choice(CONTROLLER, RandomBGMinion(tech_level_less=TIER(CONTROLLER))*12)
	pass


## Darkgaze Elder (6) (quilboar)  ### maybe OK ###
class BG23_018_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		controller = target
		source.script_data_num_1 = 5-controller.spentmoney_in_this_turn
		if controller.spentmoney_in_this_turn>=5:
			quilboars=[]
			for card in controller.field:
				if card.race==Race.QUILBOAR:
					quilboars.append(card)
			if len(quilboars)>4:
				quilboars=random.select(quilboars,4)
			for card in quilboars:
				for repeat in range(amount):
					ApplyGem(card,'BG20_GEM').trigger(source)
			controller.spentmoney_in_this_turn -= 5
			source.script_data_num_1 = 5-controller.spentmoney_in_this_turn
class BG23_018:# <12>[1453]
	""" Darkgaze Elder (6)
	After you spend 5 Gold, play a &lt;b&gt;Blood Gem&lt;/b&gt; on four friendly Quilboar. &lt;i&gt;(@ Gold left!)&lt;/i&gt;"""
	events = [
		Buy(CONTROLLER).on(BG23_018_Action(CONTROLLER, 1)),
		Rerole(CONTROLLER).on(BG23_018_Action(CONTROLLER, 1)),
		UpgradeTier(CONTROLLER).on(BG23_018_Action(CONTROLLER, 1)),
		]
	pass
class BG23_018_G:# <12>[1453]
	"""
	After you spend 4 Gold, play a &lt;b&gt;Blood Gem&lt;/b&gt; on four friendly Quilboar twice. &lt;i&gt;(@ Gold left!)&lt;/i&gt;"""
	events = [
		Buy(CONTROLLER).on(BG23_018_Action(CONTROLLER, 2)),
		Rerole(CONTROLLER).on(BG23_018_Action(CONTROLLER, 2)),
		UpgradeTier(CONTROLLER).on(BG23_018_Action(CONTROLLER, 2)),
		]
	pass
class BG23_018t:# <12>[1453]
	pass


## Leeroy the Reckless (5)  ### maybe ###
class BG23_318_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		killer = target.attacker
		if hasattr(killer,'charge'):# instead of isinstance(killer, Minion)
			Destroy(killer).trigger(source.controller)
		pass
class BG23_318:# <12>[1453]
	""" Leeroy the Reckless (5)
	&lt;b&gt;Deathrattle:&lt;/b&gt; Destroy the minion that killed this."""
	deathrattle = BG23_318_Action(SELF)
	pass
class BG23_318_G:# <12>[1453]
	"""
	&lt;b&gt;Deathrattle:&lt;/b&gt; Destroy the minion that killed this."""
	deathrattle = BG23_318_Action(SELF)
	pass


class BG23_Spellcraft_e:
	""" Spellcraft In-Hand Ench [DNT]
	"""
	pass

class GIL_681:
	""" Nightmare Amalgam (3)
	&lt;i&gt;This has all minion types.&lt;/i&gt;"""
	pass
class BG_GIL_681_G:
	""" Nightmare Amalgam (3)
	&lt;i&gt;This has all minion types.&lt;/i&gt;"""
	pass


####Tavern Tipper (1) ### OK ###
class BG23_352_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		controller = source.controller
		if controller.mana>0:
			Buff(target, buff).trigger(source)
			pass
class BG23_352:
	"""Tavern Tipper (1) >= 23.6
	If you have any unspent Gold at the end of your turn, gain +1/+2."""
	events = OWN_TURN_END.on(BG23_352_Action(SELF,'BG23_352e'))
	pass
BG23_352e=buff(1,2)
class BG23_352_G:
	"""
	If you have any unspent Gold at the end of __your turn, gain +2/+4."""
	events = OWN_TURN_END.on(BG23_352_Action(SELF,'BG23_352_Ge'))
	pass
BG23_352_Ge=buff(2,4)


## Kooky Chemist (2) ### OK ###
class BG_CFM_063:
	""" Kooky Chemist (2) >= 23.6
	Battlecry: Swap the Attack and Health of a minion."""
	requirements = {PlayReq.REQ_MINION_TARGET: 0,
				 PlayReq.REQ_FRIENDLY_TARGET: 0,
				 PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Buff(TARGET, "BG_CFM_063e")
	pass
BG_CFM_063e = AttackHealthSwapBuff()
class BG_CFM_063_G:
	"""
	[Battlecry:] Swap the Attack and Health of a minion."""
	requirements = {PlayReq.REQ_MINION_TARGET: 0,
				 PlayReq.REQ_FRIENDLY_TARGET: 0,
				 PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Buff(TARGET, "BG_CFM_063e")
	pass



#### Sparring Partner (2) ### OK ####
class BG_AT_069:
	"""Sparring Partner (2) >= 23.6
	Taunt Battlecry: Give a minion Taunt."""
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_FRIENDLY_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Taunt(TARGET)
class BG_AT_069_G:
	"""
	&lt;b&gt;Taunt&lt;/b&gt; &lt;b&gt;Battlecry:&lt;/b&gt; Give a minion &lt;b&gt;Taunt&lt;/b&gt;."""
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_FRIENDLY_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Taunt(TARGET)



## Yrel (2) ### need check ###
class BG23_350_Action(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	def do(self, source, target, buff):
		## in BG battle
		controller = target
		races = []
		for card in controller.field:
			if hasattr(card, 'race') and card.race != Race.INVALID and not card.race in races:
				races.append(card.race)
		if len(races)>0:
			for race in races:
				targets=[]
				if race != Race.ALL:
					for card in controller.field:
						if hasattr(card, 'race') and card.race == race:
							targets.append(card)
					if len(targets)>0:
						Buff(random.choice(targets),buff).trigger(source)
				else:
					for card in controller.field:
						if hasattr(card, 'race') and card.race == race:
							Buff(card,buff).trigger(source)
class BG23_350:
	"""Yrel (2) >=23.6
	After this attacks, give a friendly minion of each minion type +1/+2."""
	events = BG_Attack(SELF).on(BG23_350_Action(CONTROLLER, 'BG23_350e'))
BG23_350e=buff(1,2)
class BG23_350_G:
	"""Yrel (2) >=23.6
	After this attacks, give a friendly minion of each minion type +2/+4."""
	events = BG_Attack(SELF).on(BG23_350_Action(CONTROLLER, 'BG23_350_Ge'))
BG23_350_Ge=buff(2,4)


## Shifter Zerus (3) ### hard ###
class BGS_029:
	"""Shifter Zerus (3) >=23.6
	Each turn this is in your hand, transform it into a random minion."""
class BGS_029e:
	pass
class TB_BaconUps_095:
	"""
	Each turn this is in your
hand, transform it into a
__random Golden minion."""



## Tunnel Blaster (4) ### OK ###
class BG_DAL_775: 
	"""Tunnel Blaster (4) >= 23.6
	Taunt Deathrattle: Deal 3 damage to all minions."""
	deathrattle = Hit(ALL_MINIONS, 3)
class BG_DAL_775_G:
	"""
	&lt;b&gt;Taunt&lt;/b&gt; &lt;b&gt;Deathrattle:&lt;/b&gt; Deal 3 damage to all minions twice."""
	deathrattle = Hit(ALL_MINIONS, 3) * 2


## Uther the Lightbringer (6) ### OK ###
class BG23_190_Action(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, buff, amount):
		if target:
			atk_buff = amount - target.atk
			hlt_buff = amount - target.health
			Buff(target, buff, atk=atk_buff, max_health=hlt_buff).trigger(source)
			pass
class BG23_190:
	"""Uther the Lightbringer (6) >= 23.6
	Battlecry: Set a minion's Attack and Health to 15."""
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_FRIENDLY_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}	
	play = BG23_190_Action(TARGET, 'BG23_190e', 15)
class BG23_190e:
	pass
class BG23_190_G:
	"""
	&lt;b&gt;Battlecry:&lt;/b&gt; Set a minion's Attack and Health to 30."""
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_FRIENDLY_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}	
	play = BG23_190_Action(TARGET, 'BG23_190Ge', 30)
class BG23_190_Ge:
	pass

