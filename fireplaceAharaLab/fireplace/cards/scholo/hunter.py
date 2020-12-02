from ..utils import *


class SCH_133:
##Wolpertinger <-done 
	""" Wolpertinger 
	&lt;b&gt;Battlecry:&lt;/b&gt; Summon a copy of this."""
	play = Summon(CONTROLLER, ExactCopy(SELF))

class SCH_239:#OK
	##Krolusk Barkstripper SCH_239
	#&lt;b&gt;Spellburst:&lt;/b&gt; Destroy a random enemy minion.
	play = OWN_SPELL_PLAY.on(Destroy(RANDOM_ENEMY_MINION))
	pass

class SCH_244:#OK
	##Teacher's Pet  SCH_244
	#[x]&lt;b&gt;Taunt&lt;/b&gt; &lt;b&gt;Deathrattle:&lt;/b&gt; Summon a random 3-Cost Beast.
	deathrattle = Summon(CONTROLLER, RandomBeast(cost=3))
	pass

class SCH_279:####################incomplete
	## Trueaim Crescent SCH_279 
	##After your Hero attacks a minion, your minions attack it too.
	events = Attack(FRIENDLY_HERO,ENEMY_MINIONS).after(#OK for this line
		Hit(Attack.DEFENDER,1) * Count(FRIENDLY_MINIONS)
		#Retarget(FRIENDLY_MINIONS, Attack.DEFENDER)
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
	update = Refresh(DEATHRATTLE, {GameTag.COST: -1})#OK
	events = Play(CONTROLLER, DEATHRATTLE).on(Destroy(SELF))#OK
	pass

SCH_300e2 = buff(cost=-1)
	#Studying Carrion 
	#Costs (1) less.

class SCH_340:#OK
	##Bloated Python SCH_340
	#&lt;b&gt;Deathrattle:&lt;/b&gt; Summon a 4/4 Hapless Handler.
	deathrattle = Summon(CONTROLLER, "SCH_340t")
	pass
class SCH_340t:
	#Hapless Handler
	pass
	
class SCH_538:
	##Ace Hunter Kreen SCH_538
	#Your other characters are &lt;b&gt;Immune&lt;/b&gt; while attacking.
	update = Refresh(FRIENDLY_MINIONS-SELF,{GameTag.IMMUNE: True})#OK
	pass

class SCH_539:
	##Professor Slate  SCH_539
	#Your spells are &lt;b&gt;Poisonous&lt;/b&gt;.
	update = Refresh(IN_PLAY + SPELL, {GameTag.POISONOUS: True})# is it OK???????
	pass

class SCH_600:#OK
	## Demon Companion SCH_600
	""" Summon a random Demon Companion. """
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	entourage = ["SCH_600t1", "SCH_600t2", "SCH_600t3"]
	play = Summon(CONTROLLER, RandomEntourage())

class SCH_600t1:
	""" Reffuh """
	pass
class SCH_600t2:
	""" Shima """
	pass
class SCH_600t3:
	""" Kolek
	[x]Your other minions have +1 Attack. """
	update = Refresh(FRIENDLY_MINIONS - SELF, buff="SCH_600t3e")

SCH_600t3e = buff(1,0)

class SCH_604:#OK
	##Overwhelm SCH_604
	#Deal $2 damage to a minion. Deal one more damage for each Beast you control.
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET,2), Hit(TARGET,1) * Count(FRIENDLY_MINIONS + BEAST)
	pass

class SCH_607:#OK
	##Shan'do Wildclaw SCH_607
	# [x]&lt;b&gt;Choose One -&lt;/b&gt; Give Beasts in your deck +1/+1; or Transform into a copy of a friendly Beast.
	requirements = { PlayReq.REQ_TARGET_TO_PLAY: 0 }
	choose = ("SCH_607a", "SCH_607b")#OK
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
	#Summon two Beasts that cost (5) or less from your deck. Give_them &lt;b&gt;Rush&lt;/b&gt;.
	play = Summon(RANDOM(FRIENDLY_DECK + BEAST)).on(Buff(Summon.TARGET, buff(rush=True))), Summon(RANDOM(FRIENDLY_DECK + BEAST)).on(Buff(Summon.TARGET, buff(rush=True)))#検証待ち
	pass#does not work

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

