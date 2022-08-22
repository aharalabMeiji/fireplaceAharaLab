from ..utils import *

Classic_Rogue=[]

Classic_Backstab=True
Classic_Cold_Blood=True
Classic_Deadly_Poison=True
Classic_Sinister_Strike=True
Classic_Assassinate=True
Classic_Sprint=True
Classic_Assassins_Blade=True
Classic_Wicked_Knife=True
Classic_Blade_Flurry=True
Classic_Eviscerate=True
Classic_Betrayal=True
Classic_Conceal=True
Classic_Fan_of_Knives=True
Classic_Defias_Ringleader=True
Classic_Perditions_Blade=True
Classic_SI7_Agent=True
Classic_Headcrack=True
Classic_Shadowstep=True
Classic_Preparation=True
Classic_Shiv=True
Classic_Patient_Assassin=True
Classic_Sap=True
Classic_Edwin_VanCleef=True
Classic_Dagger_Mastery=False# HP
Classic_Vanish=True
Classic_Kidnapper=True
Classic_Master_of_Disguise=True


if Classic_Backstab:# 
	Classic_Rogue+=['VAN_CS2_072']
class VAN_CS2_072:# <7>[1646]
	""" Backstab
	Deal $2 damage to an undamaged minion. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0,
		PlayReq.REQ_UNDAMAGED_TARGET: 0}
	play = Hit(TARGET, 2)
	pass

if Classic_Cold_Blood:# 
	Classic_Rogue+=['VAN_CS2_073','CS2_073e','CS2_073e2']
class VAN_CS2_073:# <7>[1646]
	""" Cold Blood
	Give a minion +2 Attack. [Combo:] +4 Attack instead. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "CS2_073e")
	combo = Buff(TARGET, "CS2_073e2")
	pass
CS2_073e = buff(atk=2)
CS2_073e2 = buff(atk=4)

if Classic_Deadly_Poison:# 
	Classic_Rogue+=['VAN_CS2_074','CS2_074e']
class VAN_CS2_074:# <7>[1646]
	""" Deadly Poison
	Give your weapon +2_Attack. """
	requirements = {PlayReq.REQ_WEAPON_EQUIPPED: 0}
	play = Buff(FRIENDLY_WEAPON, "CS2_074e")
	pass
CS2_074e = buff(atk=2)

if Classic_Sinister_Strike:# 
	Classic_Rogue+=['VAN_CS2_075']
class VAN_CS2_075:# <7>[1646]
	""" Sinister Strike
	Deal $3 damage to the_enemy hero. """
	play = Hit(ENEMY_HERO, 3)
	pass

if Classic_Assassinate:# 
	Classic_Rogue+=['VAN_CS2_076']
class VAN_CS2_076:# <7>[1646]
	""" Assassinate
	Destroy an enemy minion. """
	requirements = {
		PlayReq.REQ_ENEMY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Destroy(TARGET)
	pass

if Classic_Sprint:# 
	Classic_Rogue+=['VAN_CS2_077']
class VAN_CS2_077:# <7>[1646]
	""" Sprint
	Draw 4 cards. """
	play = Draw(CONTROLLER) * 4
	pass

if Classic_Assassins_Blade:# 
	Classic_Rogue+=['VAN_CS2_080']
class VAN_CS2_080:# <7>[1646]
	""" Assassin's Blade
	 """
	#
	pass

if Classic_Wicked_Knife:# 
	Classic_Rogue+=['VAN_CS2_082']
class VAN_CS2_082:# <7>[1646]
	""" Wicked Knife
	 """
	#
	pass

if Classic_Blade_Flurry:# 
	Classic_Rogue+=['VAN_CS2_233']
class VAN_CS2_233:# <7>[1646]
	""" Blade Flurry
	Destroy your weapon and deal its damage to all enemies. """
	requirements = {PlayReq.REQ_WEAPON_EQUIPPED: 0}
	play = Hit(ENEMY_MINIONS, ATK(FRIENDLY_WEAPON)), Destroy(FRIENDLY_WEAPON)
	pass

if Classic_Eviscerate:# 
	Classic_Rogue+=['VAN_EX1_124']
class VAN_EX1_124:# <7>[1646]
	""" Eviscerate
	Deal $2 damage. [Combo:] Deal $4 damage instead. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 2)
	combo = Hit(TARGET, 4)
	pass

if Classic_Betrayal:# 
	Classic_Rogue+=['VAN_EX1_126']
class VAN_EX1_126:# <7>[1646]
	""" Betrayal
	Force an enemy minion to deal its damage to the minions next to it. """
	requirements = {
		PlayReq.REQ_ENEMY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(SELF_ADJACENT, ATK(SELF), source=TARGET)
	pass

if Classic_Conceal:# 
	Classic_Rogue+=['VAN_EX1_128','EX1_128e']
class VAN_EX1_128:# <7>[1646]
	""" Conceal
	Give your minions [Stealth] until your next_turn. """
	play = (
		Buff(FRIENDLY_MINIONS - STEALTH, "EX1_128e"),
		Stealth(FRIENDLY_MINIONS),
	)
	pass
class EX1_128e:
	events = OWN_TURN_BEGIN.on(Unstealth(OWNER), Destroy(SELF))

if Classic_Fan_of_Knives:# 
	Classic_Rogue+=['VAN_EX1_129']
class VAN_EX1_129:# <7>[1646]
	""" Fan of Knives
	Deal $1 damage to all enemy minions. Draw_a card. """
	play = Hit(ENEMY_MINIONS, 1), Draw(CONTROLLER)
	pass

if Classic_Defias_Ringleader:# 
	Classic_Rogue+=['VAN_EX1_131','EX1_131t']
class VAN_EX1_131:# <7>[1646]
	""" Defias Ringleader
	[Combo:] Summon a 2/1 Defias Bandit. """
	combo = Summon(CONTROLLER, "EX1_131t")
	pass
class EX1_131t:
	pass

if Classic_Perditions_Blade:# 
	Classic_Rogue+=['VAN_EX1_133']
class VAN_EX1_133:# <7>[1646]
	""" Perdition's Blade
	[Battlecry:] Deal 1 damage. [Combo:] Deal 2 instead. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Hit(TARGET, 1)
	combo = Hit(TARGET, 2)
	pass

if Classic_SI7_Agent:# 
	Classic_Rogue+=['VAN_EX1_134']
class VAN_EX1_134:# <7>[1646]
	""" SI:7 Agent
	[Combo:] Deal 2 damage. """
	requirements = {PlayReq.REQ_TARGET_FOR_COMBO: 0}
	combo = Hit(TARGET, 2)
	pass

if Classic_Headcrack:# 
	Classic_Rogue+=['VAN_EX1_137']
class VAN_EX1_137:# <7>[1646]
	""" Headcrack
	Deal $2 damage to the enemy hero. [Combo:] Return this to your hand next turn. """
	play = Hit(ENEMY_HERO, 2)
	combo = (play, TURN_END.on(Give(CONTROLLER, "EX1_137")))
	pass

if Classic_Shadowstep:# 
	Classic_Rogue+=['VAN_EX1_144']
class VAN_EX1_144:# <7>[1646]
	""" Shadowstep
	Return a friendly minion to your hand. It_costs (2) less. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Bounce(TARGET), Buff(TARGET, "EX1_144e")
	pass
@custom_card
class EX1_144e:
	tags = {
		GameTag.CARDNAME: "Shadowstep Buff",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.COST: -2,
	}
	events = REMOVED_IN_PLAY

if Classic_Preparation:# 
	Classic_Rogue+=['VAN_EX1_145']
	Classic_Rogue+=['VAN_EX1_145o']
class VAN_EX1_145:# <7>[1646]
	""" Preparation
	The next spell you cast this turn costs (3) less. """
	play = Buff(CONTROLLER, "EX1_145o")
	pass
class VAN_EX1_145o:# <7>[1646]
	""" Preparation
	The next spell you cast this turn costs (3) less. """
	update = Refresh(FRIENDLY_HAND + SPELL, {GameTag.COST: -2})
	events = OWN_SPELL_PLAY.on(Destroy(SELF))
	pass

if Classic_Shiv:# 
	Classic_Rogue+=['VAN_EX1_278']
class VAN_EX1_278:# <7>[1646]
	""" Shiv
	Deal $1 damage.Draw a card. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 1), Draw(CONTROLLER)
	pass

if Classic_Patient_Assassin:# 
	Classic_Rogue+=['VAN_EX1_522']
class VAN_EX1_522:# <7>[1646]
	""" Patient Assassin
	[Stealth]. Destroy any minion damaged by this minion. """
	#[Stealth] [Poisonous] # old card
	events = Attack(SELF, ENEMY_MINIONS).on(Destroy(Attack.DEFENDER))
	pass

if Classic_Sap:# 
	Classic_Rogue+=['VAN_EX1_581']
class VAN_EX1_581:# <7>[1646]
	""" Sap
	Return an enemy minion to your opponent's hand. """
	requirements = {
		PlayReq.REQ_ENEMY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Bounce(TARGET)
	pass

if Classic_Edwin_VanCleef:# 
	Classic_Rogue+=['VAN_EX1_613','EX1_613e']
class VAN_EX1_613:# <7>[1646]
	""" Edwin VanCleef
	[Combo:] Gain +2/+2 for each card played earlier this turn. """
	combo = Buff(SELF, "EX1_613e") * Attr(CONTROLLER, GameTag.NUM_CARDS_PLAYED_THIS_TURN)
	pass
EX1_613e = buff(+2, +2)

if Classic_Dagger_Mastery:# 
	Classic_Rogue+=['VAN_HERO_03bp']
	Classic_Rogue+=['VAN_HERO_03bp2']
class VAN_HERO_03bp:# <7>[1646]
	""" Dagger Mastery
	[Hero Power]Equip a 1/2 Dagger. """
	#
	pass
class VAN_HERO_03bp2:# <7>[1646]
	""" Poisoned Daggers
	[Hero Power]Equip a 2/2 Weapon. """
	#
	pass

if Classic_Vanish:# 
	Classic_Rogue+=['VAN_NEW1_004']
class VAN_NEW1_004:# <7>[1646]
	""" Vanish
	Return all minions to their owner's hand. """
	play = Bounce(ALL_MINIONS)
	pass

if Classic_Kidnapper:# 
	Classic_Rogue+=['VAN_NEW1_005']
class VAN_NEW1_005:# <7>[1646]
	""" Kidnapper
	[Combo:] Return a minion to_its owner's hand. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_FOR_COMBO: 0}
	combo = Bounce(TARGET)
	pass

if Classic_Master_of_Disguise:# 
	Classic_Rogue+=['VAN_NEW1_014','NEW1_014e']
class VAN_NEW1_014:# <7>[1646]
	""" Master of Disguise
	[Battlecry:] Give a friendly minion [Stealth]. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_NONSELF_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Buff(TARGET - STEALTH, "NEW1_014e")
	pass
class NEW1_014e:
	"""Disguised"""
	tags = {GameTag.STEALTH: True}
	events = OWN_TURN_BEGIN.on(Unstealth(OWNER), Destroy(SELF))

