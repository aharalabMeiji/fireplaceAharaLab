from ..utils import *

CORE_WARRIOR=['CORE_CS2_106','CORE_CS2_108','CORE_EX1_084','EX1_084e',
	'CORE_EX1_391','CORE_EX1_400','CORE_EX1_402',
	'CORE_EX1_411','EX1_411e','EX1_411e2',
	'CORE_EX1_414','EX1_414e','CORE_EX1_603','EX1_603e',
	'CORE_EX1_604','EX1_604o','CORE_GVG_053',
	'CS3_008','CS3_008e','CS3_009','CS3_030',]
#['CORE_EX1_407','CORE_EX1_410',]#bigWarrior


class CORE_CS2_106:#OK  <10>[1637]
	""" Fiery War Axe
	 """
	#
	pass

class CORE_CS2_108:#OK <10>[1637]
	""" Execute
	Destroy a damaged enemy minion. """
	requirements = {
		PlayReq.REQ_DAMAGED_TARGET: 0,
		PlayReq.REQ_ENEMY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Destroy(TARGET)
	pass

class CORE_EX1_084:#OK <10>[1637]
	""" Warsong Commander
	After you summon another minion, give it [Rush]. """
	events = Summon(FRIENDLY - SELF).on(Buff(Summon.CARD,"EX1_084e"))
	pass
EX1_084e = buff(rush=True)

class CORE_EX1_391:#OK <10>[1637]
	""" Slam
	Deal $2 damage to a minion. If it survives, draw a card. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 2), Dead(TARGET) | Draw(CONTROLLER)
	pass

class CORE_EX1_400:#OK <10>[1637]
	""" Whirlwind
	Deal $1 damage to ALL_minions. """
	play = Hit(ALL_MINIONS, 1)
	pass

class CORE_EX1_402:#OK <10>[1637]
	""" Armorsmith
	Whenever a friendly minion_takes damage, gain 1 Armor. """
	events = Damage(FRIENDLY_MINIONS).on(GainArmor(FRIENDLY_HERO, 1))
	pass

#class CORE_EX1_407:# <10>[1637]# -> cards.bigWarrior.bigWarrior
#	""" Brawl
#	Destroy all minions except one. <i>(chosen randomly)</i> """
#    requirements = {PlayReq.REQ_MINIMUM_TOTAL_MINIONS: 2}
#    play = (
#        Find(ALL_MINIONS + ALWAYS_WINS_BRAWLS) &
#        Destroy(ALL_MINIONS - RANDOM(ALL_MINIONS + ALWAYS_WINS_BRAWLS)) |
#        Destroy(ALL_MINIONS - RANDOM_MINION)#たぶんこれだけでよい、と思う。
#    )
#	pass

#class CORE_EX1_410:# <10>[1637] -> cards.bigWarrior.bigWarrior
#	""" Shield Slam
#	Deal 1 damage to a minion for each Armor you have. """
#	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0,  PlayReq.REQ_MINION_TARGET: 0}
#	play = Hit(TARGET, 2)#ARMOR(FRIENDLY_HERO))
#	pass

class CORE_EX1_411:#OK <10>[1637] ## この武器は滅びる？のだろうか？
	""" Gorehowl
	Attacking a minion costs 1 Attack instead of 1 Durability. """
	update = Attacking(FRIENDLY_HERO, MINION) & Refresh(SELF, buff="EX1_411e")
	events = Attack(FRIENDLY_HERO, MINION).after(Buff(SELF, "EX1_411e2"))
	pass
EX1_411e = buff(immune=True)
EX1_411e2 = buff(atk=-1)

class CORE_EX1_414:#OK <10>[1637]
	""" Grommash Hellscream
	[Charge]Has +6 Attack while damaged. """
	enrage = Refresh(SELF, buff="EX1_414e")
	pass
EX1_414e = buff(atk=6)

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

class CORE_EX1_604:#OK <10>[1637]
	""" Frothing Berserker
	Whenever a minion takes damage, gain +1 Attack. """
	events = Damage(ALL_MINIONS).on(Buff(SELF, "EX1_604o"))
	pass
EX1_604o = buff(atk=1)

class CORE_GVG_053:#OK <10>[1637]
	""" Shieldmaiden
	[Battlecry:] Gain 5 Armor. """
	play = GainArmor(FRIENDLY_HERO, 5)
	pass

class CS3_008:#OK <10>[1637]
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

class CS3_009:#OK <10>[1637]
	""" War Cache
	Add a random Warrior minion, spell, and weapon to your hand. """
	play = (
		Give(CONTROLLER, RandomMinion(card_class=CardClass.WARRIOR)),
		Give(CONTROLLER, RandomSpell(card_class=CardClass.WARRIOR)),
		Give(CONTROLLER, RandomWeapon(card_class=CardClass.WARRIOR)),
		)
	pass

class CS3_030:# <10>[1637]
	""" Warsong Outrider
	[Rush] """
	#
	pass