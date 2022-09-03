from ..utils import *


Core_Warrior=[]

Bash=True ##23.6
Fiery_War_Axe=True##23.6
Execute=True##23.6
Slam=True##23.6
Whirlwind=True##23.6
Armorsmith=True##23.6
Brawl=True##23.6
Shield_Slam=True##23.6
Gorehowl=True##23.6
Grommash_Hellscream=True##23.6
Cruel_Taskmaster=True##23.6
Frothing_Berserker=True##23.6
Shield_Block=True##23.6
Darius_Crowley=True##23.6
Shieldmaiden=True##23.6
Bloodhoof_Brave=True##23.6
Bloodsail_Deckhand=True##23.6


###################

if Bash:# 23.6  
	Core_Warrior+=['CORE_AT_064']
class CORE_AT_064:# <10>[1637] ## maybe OK ##
	""" Bash
	Deal $3 damage.Gain 3 Armor. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 3), GainArmor(FRIENDLY_HERO, 3)

if Fiery_War_Axe:# 
	Core_Warrior+=['CORE_CS2_106']
class CORE_CS2_106:# <10>[1637]
	""" Fiery War Axe
	 """
	pass

if Execute:# 
	Core_Warrior+=['CORE_CS2_108']
class CORE_CS2_108:# <10>[1637]  ## maybe OK ##
	""" Execute
	Destroy a damaged enemy minion. """
	requirements = {PlayReq.REQ_DAMAGED_TARGET: 0,PlayReq.REQ_ENEMY_TARGET: 0,PlayReq.REQ_MINION_TARGET: 0,PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Destroy(TARGET)
	pass

class CORE_EX1_084:#OK <10>[1637] ## 22.6
	""" Warsong Commander
	After you summon another minion, give it [Rush]. """
	events = Summon(CONTROLLER, FRIENDLY_MINIONS).on(Buff(Summon.CARD,"EX1_084e"))
	pass
EX1_084e = buff(rush=True)

if Slam:# 
	Core_Warrior+=['CORE_EX1_391']
class CORE_EX1_391:# <10>[1637]
	""" Slam
	Deal $2 damage to a minion. If it survives, draw a card. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 2), Dead(TARGET) | Draw(CONTROLLER)
	pass

if Whirlwind:# 
	Core_Warrior+=['CORE_EX1_400']
class CORE_EX1_400:# <10>[1637]
	""" Whirlwind
	Deal $1 damage to ALL_minions. """
	play = Hit(ALL_MINIONS, 1)
	pass

if Armorsmith:# 
	Core_Warrior+=['CORE_EX1_402']
class CORE_EX1_402:# <10>[1637]
	""" Armorsmith
	Whenever a friendly minion_takes damage, gain 1 Armor. """
	events = Damage(FRIENDLY_MINIONS).on(GainArmor(FRIENDLY_HERO, 1))
	pass

if Brawl:# 
	Core_Warrior+=['CORE_EX1_407']
class CORE_EX1_407:# <10>[1637] ## bigWarrior
	""" Brawl
	Destroy all minions except one. <i>(chosen randomly)</i> """
	requirements = {PlayReq.REQ_MINIMUM_TOTAL_MINIONS: 2}
	play = Destroy(ALL_MINIONS - RANDOM_MINION)#
	pass

if Shield_Slam:# 
	Core_Warrior+=['CORE_EX1_410']
class CORE_EX1_410:# <10>[1637]
	""" Shield Slam
	Deal 1 damage to a minion for each Armor you have. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0,  PlayReq.REQ_MINION_TARGET: 0}
	play = Hit(TARGET, ARMOR(FRIENDLY_HERO))
	pass

if Gorehowl:# 
	Core_Warrior+=['CORE_EX1_411','EX1_411e','EX1_411e2']
class CORE_EX1_411_Action1(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		#target = this weapon
		target.max_durability += 1
		pass
class CORE_EX1_411_Action2(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		#target = this weapon
		target.atk -= 1
		if target.atk==0:
			Destroy(target).trigger(source)
		pass
class CORE_EX1_411:# <10>[1637] ##########正しく動作しない。
	""" Gorehowl
	Attacking a minion costs 1 Attack instead of 1 Durability. """
	events = [Attack(FRIENDLY_HERO).on(CORE_EX1_411_Action1(SELF)), Attack(FRIENDLY_HERO).after(CORE_EX1_411_Action2(SELF))]
	pass
class EX1_411e:
	pass
EX1_411e2 = buff(atk=-1)

if Grommash_Hellscream:# 
	Core_Warrior+=['CORE_EX1_414','EX1_414e']
class CORE_EX1_414:# <10>[1637]
	""" Grommash Hellscream
	[Charge]Has +6 Attack while damaged. """
	enrage = Refresh(SELF, buff="EX1_414e")
	pass
EX1_414e = buff(atk=6)

if Cruel_Taskmaster:# 
	Core_Warrior+=['CORE_EX1_603','EX1_603e']
class CORE_EX1_603:# <10>[1637]
	""" Cruel Taskmaster
	[Battlecry:] Deal 1 damage to a minion and give it +2_Attack. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_NONSELF_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Buff(TARGET, "EX1_603e"), Hit(TARGET, 1)
	pass
EX1_603e = buff(atk=2)

if Frothing_Berserker:# 
	Core_Warrior+=['CORE_EX1_604','EX1_604o']
class CORE_EX1_604:# <10>[1637]
	""" Frothing Berserker
	Whenever a minion takes damage, gain +1 Attack. """
	events = Damage(ALL_MINIONS).on(Buff(SELF, "EX1_604o"))
	pass
EX1_604o = buff(atk=1)

if Shield_Block:# ##23.6
	Core_Warrior+=['CORE_EX1_606']
class CORE_EX1_606:# <10>[1637]
	""" Shield Block
	Gain 5 Armor.Draw a card. """
	play = GainArmor(FRIENDLY_HERO, 5), Draw(CONTROLLER)
	pass

if Darius_Crowley:# ##23.6
	Core_Warrior+=['CORE_GIL_547']
class CORE_GIL_547_Action(TargetedAction):
	ATTACKER=ActionArg()
	DEFENDER=ActionArg()
	def do(self, source, attacker, defender):
		if attacker.atk>=defender.health:
			Buff(SELF,'CORE_GIL_547e').trigger(source)
class CORE_GIL_547:# <10>[1637]
	""" Darius Crowley
	[Rush]After this attacks and kills a minion, gain +2/+2. """
	events = Attack(SELF, ENEMY_MINIONS).on(CORE_GIL_547_Action(Attack.ATTACKER, Attack.DEFENDER))
	pass
@custom_card
class CORE_GIL_547e:
	tags = {
		GameTag.CARDNAME: "Darius Crowley",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.ATK:2,
		GameTag.HEALTH:2,
	}

if Shieldmaiden:# 
	Core_Warrior+=['CORE_GVG_053']
class CORE_GVG_053:# <10>[1637]
	""" Shieldmaiden
	[Battlecry:] Gain 5 Armor. """
	play = GainArmor(FRIENDLY_HERO, 5)
	pass

if Bloodhoof_Brave:# ##23.6
	Core_Warrior+=['CORE_OG_218','OG_218e']
class CORE_OG_218:# <10>[1637]
	""" Bloodhoof Brave
	[Taunt]Has +3 Attack while damaged. """
	enrage = Refresh(SELF, buff="OG_218e")
OG_218e = buff(atk=3)

if Bloodsail_Deckhand:# 
	Core_Warrior+=['CS3_008']
	Core_Warrior+=['CS3_008e']
class CS3_008:# <10>[1637]
	""" Bloodsail Deckhand
	[Battlecry:] The next weapon you play costs(1) less. """
	play = Buff(FRIENDLY_HAND + WEAPON,'CS3_008e')
	pass
class CS3_008e:# <10>[1637]## updateが弱いかも
	""" To Arrrms!
	Your next weapon costs (1) less. """
	cost = lambda self, i: max(i-1,0)
	events = Play(CONTROLLER, WEAPON).on(Destroy(SELF))
	pass


class CS3_009:#OK <10>[1637] ##22.6
	""" War Cache
	Add a random Warrior minion, spell, and weapon to your hand. """
	play = (
		Give(CONTROLLER, RandomMinion(card_class=CardClass.WARRIOR)),
		Give(CONTROLLER, RandomSpell(card_class=CardClass.WARRIOR)),
		Give(CONTROLLER, RandomWeapon(card_class=CardClass.WARRIOR)),
		)
	pass

class CS3_030:# <10>[1637] ##22.6
	""" Warsong Outrider
	[Rush] """
	pass

