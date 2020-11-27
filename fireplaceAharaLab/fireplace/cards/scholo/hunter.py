from ..utils import *


class SCH_133:
##Wolpertinger <-done  SCH_133
	""" Wolpertinger 
	雄叫び: このミニオンの   コピーを1体召喚する。"""
	play = Summon(CONTROLLER, ExactCopy(SELF))

class SCH_239:
	##Krolusk Barkstripper SCH_239
	#魔法活性:	ランダムな敵のミニオン1体を破壊する。
	play = OWN_SPELL_PLAY.on(Destroy(RANDOM_ENEMY_MINION))#OK
	pass

class SCH_244:
	##Teacher's Pet  SCH_244
	#挑発、断末魔:	#ランダムなコスト3の	#___獣1体を召喚する。
	deathrattle = Summon(CONTROLLER, RandomBeast(cost=3))#OK
	pass

class SCH_279:
	## Trueaim Crescent SCH_279 
	##自分のヒーローが	##ミニオンを攻撃した後	##味方のミニオン全てが	##_____同じ標的を攻撃する。
	events = Attack(FRIENDLY_HERO,ENEMY_MINIONS).after(#この行OK
		ExtraAttack(FRIENDLY_MINIONS)
		#Hit(Attack.DEFENDER,1)#この行、実現できていない。
	)#検証待ち
	pass

class SCH_300:#OK
	##Carrion Studies SCH_300
	#Discover a Deathrattle minion. Your next one costs (1) less.
	play = DISCOVER(RandomMinion(deathrattle=True)).then(
	   Buff(CONTROLLER, "SCH_300e")
	   )
	pass
class SCH_300e:
	#Carrion Studies
	#Your next [Deathrattle] minion costs (1) less.
	update = Refresh(DEATHRATTLE, buff="SCH_300e2")#OK
	events = Play(CONTROLLER, DEATHRATTLE).on(Destroy(SELF))#OK
	pass

SCH_300e2 = buff(cost=-1)
	#Studying Carrion 
	#Costs (1) less.

class SCH_340:
	##Bloated Python SCH_340
	#断末魔:#4/4の	#「つかえてたヘビ使い」	#を1体召喚する。
	deathrattle = Summon(CONTROLLER, "SCH_340t")#OK
	pass
class SCH_340t:
	#Hapless Handler
	pass
	
class SCH_538:
	##Ace Hunter Kreen SCH_538
	#自身を除く味方の	#キャラクターは	#攻撃する際に 無敵 を得る。
	update = Refresh(FRIENDLY_MINIONS-SELF,{GameTag.IMMUNE: True})#OK
	pass

class SCH_539:
	##Professor Slate  SCH_539
	#自分の呪文は	# 猛毒 を持つ。(これを持つカードからダメージを受けたミニオンは、残り体力に関わらず破壊される。)
	update = Refresh(IN_PLAY + SPELL, {GameTag.POISONOUS: True})#検証不能、バグはない。
	pass

class SCH_600:
	## Demon Companion SCH_600
	""" 悪魔の相棒 	 ランダムな悪魔の相棒を1体召喚する。 """
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	entourage = ["SCH_600t1", "SCH_600t2", "SCH_600t3"]
	play = Summon(CONTROLLER, RandomEntourage())
	#def play(self):
	#	friend_demon = random.choice(["SCH_600t1", "SCH_600t2", "SCH_600t3"])
	#	yield Summon(CONTROLLER, friend_demon)

class SCH_600t1:
	""" フハァー """
	pass
class SCH_600t2:
	""" シーミャ """
	pass
class SCH_600t3:
	""" オレック
	[x]自身を除く味方のミニオンは攻撃力+1を得る。 """
	update = Refresh(FRIENDLY_MINIONS - SELF, buff="SCH_600t3e")

SCH_600t3e = buff(1,0)

class SCH_604:
	##Overwhelm SCH_604
	#ミニオン1体に#$2ダメージを与える。#自分の陣地の獣1体につき#さらに1ダメージを与える。
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET,2), Hit(TARGET,1) * Count(FRIENDLY_MINIONS + BEAST)#OK
	pass

class SCH_607:
##Shan'do Wildclaw SCH_607
# 選択:  自分のデッキの獣#全てに+1/+1を付与する。
#または、味方の獣1体の#コピーに変身する。
	requirements = { PlayReq.REQ_TARGET_TO_PLAY: 0 }
	choose = ("SCH_607a", "SCH_607b")#確認できず。
	play =ChooseBoth(CONTROLLER) & Morph(SELF, RANDOM(FRIENDLY+BEAST));#OK
	pass

class SCH_607a:
	#Transfiguration
	play = Buff(FRIENDLY_DECK+BEAST,"SCH_607e")#OK
	#update = Refresh(FRIENDLY_DECK+BEAST,buff="SCH_607e")#
	pass

class SCH_607b:
	#Rile the Herd
	#play = Buff(FRIENDLY_MINIONS,buff="SCH_607e")
	play = Morph(SELF, RANDOM(FRIENDLY+BEAST))#OK
	pass

SCH_607e = buff(1,1);


class SCH_610:
	##Guardian Animals SCH_610
	#自分のデッキから	#コスト（5）以下の獣を	#2体召喚する。それらに	# 急襲 を付与する。
	play = Summon(FRIENDLY_MINIONS + BEAST).on(Buff(Summon.TARGET, buff(rush=True))), Summon(FRIENDLY_MINIONS + BEAST).on(Buff(Summon.TARGET, buff(rush=True)))#検証待ち
	pass#確認できず。

class SCH_617:
	##Adorable Infestation <-done SCH_617
	"""  カワイイ侵入者 
	ミニオン1体に +1/+1を付与する。 1/1の仔を1体召喚する。 仔1体を自分の 手札に追加する。"""
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "SCH_617e"), Summon(CONTROLLER, "SCH_617t"),Give(CONTROLLER, "SCH_617t")

SCH_617e = buff(1, 1)

class SCH_617t:
	pass

class SCH_618:
	##Blood Herald SCH_618
	#このカードが手札に#ある間、味方のミニオン#が死ぬ度に+1/+1を#獲得する。
	class Hand:
		events = Death(FRIENDLY + MINION).on(Buff(SELF, "SCH_618e"))#OK
	pass

SCH_618e = buff(1, 1)

