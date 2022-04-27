from ..utils import *
from fireplace.battlegrounds.BG_actions import *

BG_Minion_Demon =[
	'BG21_029','EX1_598','BG21_029_G','TB_BaconUps_030t',#Icky Imp(1)
	'BG21_006','BG21_006e','BG21_006_G',#Impulsive Trickster(1)
	'BGS_001','TB_BaconUps_062',#Nathrezim Overseer(2)
	'BGS_014','TB_BaconUps_113',#Imprisoner(2)
	'BG21_039','BG21_039_G',#Kathra'natir(3)
	'BGS_059','BGS_059e','TB_BaconUps_119',#Soul Devourer(3)
	'BGS_204','BGS_204e','TB_BaconUps_304','TB_BaconUps_304e',#Bigfernal(4)
	'DMF_533','DMF_533t','TB_BaconUps_309','TB_BaconUps_309t',#Ring Matron(4)
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

####################　インプ
class BG21_029:# <12>[1453]
	""" Icky Imp (1)
	[Deathrattle:] Summon two 1/1 Imps. """
	deathrattle = Summon(CONTROLLER, 'EX1_598') * 2
	pass
class EX1_598:#
	""" imp (1/1)
	"""
	pass
class BG21_029_G:# <12>[1453]
	""" Icky Imp
	[Deathrattle:] Summon two 2/2 Imps. """
	deathrattle = Summon(CONTROLLER, 'TB_BaconUps_030t') * 2
	pass
class TB_BaconUps_030t:#
	""" Imp (2/2)
	"""

#################### トリックスター
class BG21_006_Action(TargetedAction):
	TARGET = ActionArg()
	CONTRO = ActionArg()
	def do(self, source, target, contro):
		# controller : trickstar card
		# target = friendly minion
		if isinstance(contro, list):
			contro = contro[0]
		controller = contro
		buff_health = source.max_health
		if target!=None and target!=[]:
			Buff(target, 'BG21_006e').trigger(controller)
			buff = target.buffs[-1]
			buff.max_health = buff_health
		pass
class BG21_006:# <12>[1453]
	""" Impulsive Trickster(1)
	[Deathrattle:] Give this minion's maximum Health__to another friendly minion._ """
	deathrattle = BG21_006_Action(RANDOM(FRIENDLY_MINIONS),CONTROLLER)
	pass
class BG21_006e:# <12>[1453]
	""" Impulsive
	Increased Health. """
	pass
class BG21_006_G:# <12>[1453]
	""" Impulsive Trickster
	[Deathrattle:] Give thisminion's maximum Healthto another friendly minion twice. """
	deathrattle = BG21_006_Action(RANDOM(FRIENDLY_MINIONS)) * 2
	pass



####################ナスレズィム
class BGS_001:# <12>[1453] 
	""" Nathrezim Overseer (2)
	[Battlecry:] Give a friendly Demon +2/+2. """
	requirements = {
		PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_TARGET_WITH_RACE:Race.DEMON, PlayReq.REQ_FRIENDLY_TARGET:0, 
		}
	play = Buff(TARGET, 'BGS_001')
	pass
BGS_001e=buff(2,2)
class TB_BaconUps_062:# <12>[1453]
	""" Nathrezim Overseer
	[Battlecry:] Give a friendly Demon +4/+4. """
	requirements = {
		PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_TARGET_WITH_RACE:Race.DEMON, PlayReq.REQ_FRIENDLY_TARGET:0, 
		}
	play = Buff(TARGET, 'BGS_001')
	pass
TB_BaconUps_062e=buff(4,4)



####################  禁固番
class BGS_014:# <12>[1453]
	""" Imprisoner (2)
	[Taunt][Deathrattle:] Summon a 1/1 Imp. """
	deathrattle = Summon(CONTROLLER, 'EX1_598')
	pass
class TB_BaconUps_113:# <12>[1453]
	""" Imprisoner
	[Taunt][Deathrattle:] Summon a 2/2 Imp. """
	deathrattle = Summon(CONTROLLER, 'TB_BaconUps_030t')
	pass



#################### カスラナティール（カステラ）
class BG21_039:# <12>[1453]
	""" Kathra'natir (3)
	Your other Demons have +2 Attack.Your Hero is [Immune]. """
	update = Refresh(FRIENDLY + DEMON, buff='BG21_039e'),Refresh(FRIENDLY_HERO, {GameTag.IMMUNE:True})
	pass
BG21_039e=buff(2,0)
class BG21_039_G:# <12>[1453]
	""" Kathra'natir
	Your other Demonshave +4 Attack.Your Hero is [Immune]. """
	update = Refresh(FRIENDLY + DEMON, buff='BG21_039_Ge'),Refresh(FRIENDLY_HERO, {GameTag.IMMUNE:True})
	pass
BG21_039_Ge=buff(4,0)



####################   魂喰らい魔
class BGS_059_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		controller = source.controller
		Buff(source, 'BGS_059e').trigger(source)
		buff = source.buffs[-1]
		buff.atk = target.atk * amount
		buff.max_health = target.max_health * amount
		Destroy(target).trigger(source)
		ManaThisTurn(controller, 3 * amount).trigger(source)
class BGS_059:# <12>[1453] ## 動いている感じはある
	""" Soul Devourer (3)
	[Battlecry:] Choose a friendly Demon. Remove it to gain its stats and 3 Gold. """
	requirements={
		PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_TARGET_WITH_RACE:Race.DEMON, PlayReq.REQ_FRIENDLY_TARGET:0, 
		}
	play = BGS_059_Action(TARGET,  1)
	pass
class BGS_059e:
	pass
class TB_BaconUps_119:# <12>[1453]
	""" Soul Devourer
	[Battlecry:] Choose afriendly Demon. Removeit to gain double its statsand 6 Gold. """
	requirements={
		PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_TARGET_WITH_RACE:Race.DEMON, PlayReq.REQ_FRIENDLY_TARGET:0, 
		}
	play = BGS_059_Action(TARGET, 2)
	pass



###################　焦熱の圧鬼（あっき）
class BGS_204:# <12>[1453]
	""" Bigfernal (4)
	After you summon a Demon, gain +1/+1 permanently. """
	events = Summon(FRIENDLY + DEMON).after(BuffPermanently(SELF, 'BGS_204e' ))
	pass
BGS_204e=buff(1,1)
class TB_BaconUps_304:# <12>[1453]
	""" Bigfernal
	After you summon a Demon, gain +2/+2 permanently. """
	events = Summon(FRIENDLY + DEMON).after(BuffPermanently(SELF, 'TB_BaconUps_304e' ))
	pass
TB_BaconUps_304e=buff(2,2)


###################　　火の輪くぐらせ嬢
class DMF_533:# <9>[1453]
	""" Ring Matron (4)
	[Taunt][Deathrattle:] Summon　two 3/2 Imps. """
	deathrattle = Summon(CONTROLLER, 'DMF_533t')*2
	pass
class DMF_533t:
	pass
class TB_BaconUps_309:# <9>[1453]
	""" Ring Matron
	[Taunt][Deathrattle:] Summontwo 6/4 Imps. """
	deathrattle = Summon(CONTROLLER, 'TB_BaconUps_309t')*2
	pass
class TB_BaconUps_309t:# <9>[1453]
	""" Fiery Imp
	 """
	pass



####################　　　ウルズール
class BG21_004:# <12>[1453]
	""" Insatiable Ur'zul (5)
	[[Taunt].] After you play a Demon, consume a minion in Bob's Tavern to gain its stats. """
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




####################　　　アニヒラン
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



#################### ヴォイドロード
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

####################　　　フェルバット
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



