from ..utils import *


class SCH_133:
##Wolpertinger OK 
	""" Wolpertinger 
	<b>Battlecry:</b> Summon a copy of this."""
	play = Summon(CONTROLLER, ExactCopy(SELF))

class SCH_239:#OK
	##Krolusk Barkstripper SCH_239
	#<b>Spellburst:</b> Destroy a random enemy minion.
	play = OWN_SPELL_PLAY.on(Destroy(RANDOM_ENEMY_MINION))
	pass

class SCH_244:#OK
	##Teacher's Pet  SCH_244
	#[x]<b>Taunt</b> <b>Deathrattle:</b> Summon a random 3-Cost Beast.
	deathrattle = Summon(CONTROLLER, RandomBeast(cost=3))
	pass

class SCH_279:#OK
	## Trueaim Crescent SCH_279 
	##After your Hero attacks a minion, your minions attack it too.
	events = Attack(FRIENDLY_HERO,ENEMY_MINIONS).after(#OK for this line
		RegularAttack(FRIENDLY_MINIONS, Attack.DEFENDER)##  need check RegularAttack its validity
	)
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
	update = Refresh(IN_HAND + FRIENDLY + MINION + DEATHRATTLE, {GameTag.COST: -1})#OK
	events = Play(CONTROLLER, DEATHRATTLE).on(Destroy(SELF))#OK
	pass

SCH_300e2 = buff(cost=-1)
	#Studying Carrion 
	#Costs (1) less.

class SCH_340:#OK
	##Bloated Python SCH_340
	#<b>Deathrattle:</b> Summon a 4/4 Hapless Handler.
	deathrattle = Summon(CONTROLLER, "SCH_340t")
	pass
class SCH_340t:
	#Hapless Handler
	pass
	
class SCH_538:
	##Ace Hunter Kreen SCH_538
	#Your other characters are <b>Immune</b> while attacking.
	update = Refresh(FRIENDLY_MINIONS-SELF,buff='SCH_538e')#OK
	pass
SCH_538e=buff(immune_while_attacking=True)#

class SCH_539:#OK
	##Professor Slate  SCH_539
	#Your spells are <b>Poisonous</b>.
	update = SetTag(FRIENDLY_HAND + SPELL,(GameTag.POISONOUS, ))# is it OK???????
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
	# [x]<b>Choose One -</b> Give Beasts in your deck +1/+1; or Transform into a copy of a friendly Beast.
	choose = ("SCH_607a", "SCH_607b")#OK
	play =ChooseBoth(SELF) & Morph(SELF, RANDOM((FRIENDLY + BEAST) - FRIENDLY_HERO));#OK
	pass

class SCH_607a:
	"""Transfiguration
	Transform into a copy of a friendly Beast."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE:Race.BEAST}
	play = Morph(SELF, ExactCopy(TARGET))#OK
	#update = Refresh(FRIENDLY_DECK+BEAST,buff="SCH_607e")#
	pass

class SCH_607b:
	"""Rile the Herd
	Give Beasts in your deck +1/+1. """
	play = Buff(FRIENDLY_DECK + BEAST,"SCH_607e") 
	pass

SCH_607e = buff(1,1);


class SCH_610:#OK
	"""Guardian Animals SCH_610
	Summon two Beasts that cost (5) or less from your deck. Give_them <b>Rush</b>."""
	play = Summon(CONTROLLER, RANDOM(FRIENDLY_DECK + BEAST + (COST <= 5))).then(
		SetTag(Summon.CARD, (GameTag.RUSH,))
	)*2
class SCH_617:
	"""Adorable Infestation 
	Give a minion +1/+1. Summon a 1/1 Cub. Add a Cub to your hand."""
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "SCH_617e"), Summon(CONTROLLER, "SCH_617t"),Give(CONTROLLER, "SCH_617t")

SCH_617e = buff(1, 1)

class SCH_617t:
	pass

class SCH_618:
	"""Blood Herald
	Whenever a friendly minion dies while this is in your hand, gain +1/+1."""
	class Hand:
		events = Death(FRIENDLY + MINION).on(Buff(SELF, "SCH_618e"))#OK
	pass

SCH_618e = buff(1, 1)

