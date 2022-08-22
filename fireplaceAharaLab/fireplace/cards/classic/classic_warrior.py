from ..utils import *

Classic_Warrior=[]

Classic_Charge=True
Classic_Rampage=True
Classic_Heroic_Strike=True
Classic_Fiery_War_Axe=True
Classic_Execute=True
Classic_Arcanite_Reaper=True
Classic_Cleave=True
Classic_Warsong_Commander=True
Classic_Slam=True
Classic_Battle_Rage=True
Classic_Arathi_Weaponsmith=True
Classic_Whirlwind=True
Classic_Armorsmith=True
Classic_Brawl=True
Classic_Mortal_Strike=True
Classic_Upgrade=True
Classic_Shield_Slam=True
Classic_Gorehowl=True
Classic_Grommash_Hellscream=True
Classic_Cruel_Taskmaster=True
Classic_Frothing_Berserker=True
Classic_Shield_Block=True
Classic_Inner_Rage=True
Classic_Armor_Up=False # HP
Classic_Korkron_Elite=True
Classic_Commanding_Shout=True



if Classic_Charge:# 
	Classic_Warrior+=['VAN_CS2_103']
	Classic_Warrior+=['VAN_CS2_103e2']
class VAN_CS2_103:# <10>[1646]
	""" Charge
	Give a friendly minion +2 Attack and [Charge]. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "CS2_103e2")
	pass
VAN_CS2_103e2 = buff(atk=2, charge=True)

if Classic_Rampage:# 
	Classic_Warrior+=['VAN_CS2_104','CS2_104e']
class VAN_CS2_104:# <10>[1646]
	""" Rampage
	Give a damaged minion +3/+3. """
	requirements = {
		PlayReq.REQ_DAMAGED_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "CS2_104e")
	pass
CS2_104e = buff(+3, +3)

if Classic_Heroic_Strike:# 
	Classic_Warrior+=['VAN_CS2_105','CS2_105e']
class VAN_CS2_105:# <10>[1646]
	""" Heroic Strike
	Give your hero +4_Attack this turn. """
	play = Buff(FRIENDLY_HERO, "CS2_105e")
	pass
CS2_105e = buff(atk=4)

if Classic_Fiery_War_Axe:# 
	Classic_Warrior+=['VAN_CS2_106']
class VAN_CS2_106:# <10>[1646]
	""" Fiery War Axe
	 """
	#
	pass

if Classic_Execute:# 
	Classic_Warrior+=['VAN_CS2_108']
class VAN_CS2_108:# <10>[1646]
	""" Execute
	Destroy a damaged enemy minion. """
	requirements = {
		PlayReq.REQ_DAMAGED_TARGET: 0,
		PlayReq.REQ_ENEMY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Destroy(TARGET)
	pass

if Classic_Arcanite_Reaper:# 
	Classic_Warrior+=['VAN_CS2_112']
class VAN_CS2_112:# <10>[1646]
	""" Arcanite Reaper
	 """
	#
	pass

if Classic_Cleave:# 
	Classic_Warrior+=['VAN_CS2_114']
class VAN_CS2_114:# <10>[1646]
	""" Cleave
	Deal $2 damage totwo random enemyminions. """
	requirements = {PlayReq.REQ_MINIMUM_ENEMY_MINIONS: 1}
	play = Hit(RANDOM_ENEMY_MINION * 2, 2)
	pass

if Classic_Warsong_Commander:# 
	Classic_Warrior+=['VAN_EX1_084','EX1_084e']
class VAN_EX1_084:# <10>[1646]
	""" Warsong Commander
	Whenever you summon a minion with 3 or less Attack, give it [Charge]. """
	update = Refresh(FRIENDLY_MINIONS + CHARGE, buff="EX1_084e")
	pass
EX1_084e = buff(atk=1)

if Classic_Slam:# 
	Classic_Warrior+=['VAN_EX1_391']
class VAN_EX1_391:# <10>[1646]
	""" Slam
	Deal $2 damage to a minion. If it survives, draw a card. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 2), Dead(TARGET) | Draw(CONTROLLER)
	pass

if Classic_Battle_Rage:# 
	Classic_Warrior+=['VAN_EX1_392']
class VAN_EX1_392:# <10>[1646]
	""" Battle Rage
	Draw a card for each damaged friendly character. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0}
	play = Draw(CONTROLLER) * Count(FRIENDLY_CHARACTERS + DAMAGED)
	pass

if Classic_Arathi_Weaponsmith:# 
	Classic_Warrior+=['VAN_EX1_398','EX1_398t']
class VAN_EX1_398:# <10>[1646]
	""" Arathi Weaponsmith
	[Battlecry:] Equip a 2/2_weapon. """
	play = Summon(CONTROLLER, "EX1_398t")
	pass
class EX1_398t:
	pass

if Classic_Whirlwind:# 
	Classic_Warrior+=['VAN_EX1_400']
class VAN_EX1_400:# <10>[1646]
	""" Whirlwind
	Deal $1 damage to ALL_minions. """
	play = Hit(ALL_MINIONS, 1)
	pass

if Classic_Armorsmith:# 
	Classic_Warrior+=['VAN_EX1_402']
class VAN_EX1_402:# <10>[1646]
	""" Armorsmith
	Whenever a friendly minion_takes damage, gain 1 Armor. """
	events = Damage(FRIENDLY_MINIONS).on(GainArmor(FRIENDLY_HERO, 1))
	pass

if Classic_Brawl:# 
	Classic_Warrior+=['VAN_EX1_407']
class VAN_EX1_407:# <10>[1646]
	""" Brawl
	Destroy all minions except one. <i>(chosen randomly)</i> """
	requirements = {PlayReq.REQ_MINIMUM_TOTAL_MINIONS: 2}
	play = (
		Find(ALL_MINIONS + ALWAYS_WINS_BRAWLS) &
		Destroy(ALL_MINIONS - RANDOM(ALL_MINIONS + ALWAYS_WINS_BRAWLS)) |
		Destroy(ALL_MINIONS - RANDOM_MINION)
	)
	pass

if Classic_Mortal_Strike:# 
	Classic_Warrior+=['VAN_EX1_408']
class VAN_EX1_408:# <10>[1646]
	""" Mortal Strike
	Deal $4 damage. If you have 12 or less Health, deal $6 instead. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	powered_up = CURRENT_HEALTH(FRIENDLY_HERO) <= 12
	play = powered_up & Hit(TARGET, 6) | Hit(TARGET, 4)
	pass

if Classic_Upgrade:# 
	Classic_Warrior+=['VAN_EX1_409','EX1_409e']
class VAN_EX1_409:# <10>[1646]
	""" Upgrade!
	If you have a weapon, give it +1/+1. Otherwise equip a 1/3 weapon. """
	play = (
		Find(FRIENDLY_WEAPON) &
		Buff(FRIENDLY_WEAPON, "EX1_409e") |
		Summon(CONTROLLER, "EX1_409t")
	)
	pass
EX1_409e = buff(+1, +1)

if Classic_Shield_Slam:# 
	Classic_Warrior+=['VAN_EX1_410']
class VAN_EX1_410:# <10>[1646]
	""" Shield Slam
	Deal 1 damage to a minion for each Armor you have. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, ARMOR(FRIENDLY_HERO))
	pass

if Classic_Gorehowl:# 
	Classic_Warrior+=['VAN_EX1_411']
class VAN_EX1_411:# <10>[1646]
	""" Gorehowl
	Attacking a minion costs 1 Attack instead of 1 Durability. """
	#
	pass

if Classic_Grommash_Hellscream:# 
	Classic_Warrior+=['VAN_EX1_414','EX1_414e']
class VAN_EX1_414:# <10>[1646]
	""" Grommash Hellscream
	[Charge][Enrage:] +6 Attack """
	enrage = Refresh(SELF, buff="EX1_414e")
	pass
EX1_414e = buff(atk=6)

if Classic_Cruel_Taskmaster:# 
	Classic_Warrior+=['VAN_EX1_603','EX1_603e']
class VAN_EX1_603:# <10>[1646]
	""" Cruel Taskmaster
	[Battlecry:] Deal 1 damage to a minion and give it +2_Attack. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_NONSELF_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Buff(TARGET, "EX1_603e"), Hit(TARGET, 1)
	pass
EX1_603e = buff(atk=2)

if Classic_Frothing_Berserker:# 
	Classic_Warrior+=['VAN_EX1_604','EX1_604o']
class VAN_EX1_604:# <10>[1646]
	""" Frothing Berserker
	Whenever a minion takes damage, gain +1 Attack. """
	events = Damage(ALL_MINIONS).on(Buff(SELF, "EX1_604o"))
	pass
EX1_604o = buff(atk=1)

if Classic_Shield_Block:# 
	Classic_Warrior+=['VAN_EX1_606']
class VAN_EX1_606:# <10>[1646]
	""" Shield Block
	Gain 5 Armor.Draw a card. """
	play = GainArmor(FRIENDLY_HERO, 5), Draw(CONTROLLER)
	pass

if Classic_Inner_Rage:# 
	Classic_Warrior+=['VAN_EX1_607','EX1_607e']
class VAN_EX1_607:# <10>[1646]
	""" Inner Rage
	Deal $1 damage to a minion and give it +2_Attack. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "EX1_607e"), Hit(TARGET, 1)
	pass
EX1_607e = buff(atk=2)

if Classic_Armor_Up:# 
	Classic_Warrior+=['VAN_HERO_01bp']
	Classic_Warrior+=['VAN_HERO_01bp2']
class VAN_HERO_01bp:# <10>[1646]
	""" Armor Up!
	[Hero Power]Gain 2 Armor. """
	#
	pass
class VAN_HERO_01bp2:# <10>[1646]
	""" Tank Up!
	[Hero Power]Gain 4 Armor. """
	#
	pass

if Classic_Korkron_Elite:# 
	Classic_Warrior+=['VAN_NEW1_011']
class VAN_NEW1_011:# <10>[1646]
	""" Kor'kron Elite
	[Charge] """
	#
	pass

if Classic_Commanding_Shout:# 
	Classic_Warrior+=['VAN_NEW1_036','NEW1_036e','NEW1_036e2']
class VAN_NEW1_036:# <10>[1646]
	""" Commanding Shout
	Your minions can't be reduced below 1 Health this turn. Draw a card. """
	play = Buff(FRIENDLY_MINIONS, "NEW1_036e"), Buff(CONTROLLER, "NEW1_036e2")
	pass
NEW1_036e = buff(health_minimum=1)
class NEW1_036e2:
	events = Summon(CONTROLLER, MINION).on(Buff(Summon.CARD, "NEW1_036e"))


