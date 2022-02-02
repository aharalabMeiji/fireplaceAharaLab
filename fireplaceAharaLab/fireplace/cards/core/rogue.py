from ..utils import *

#Core_Rogue=["CORE_CS2_072","CORE_CS2_073","CS2_073e","CS2_073e2","CORE_CS2_074","CS2_074e","CORE_CS2_075","CORE_CS2_076","CORE_CS2_077","CORE_CS2_080","CORE_EX1_134","CORE_EX1_144","CORE_EX1_145","EX1_145e","EX1_145o","CORE_EX1_522","CORE_ICC_809","ICC_809e","CORE_KAR_069","CORE_LOE_012","CORE_OG_070","OG_070e","CS3_005"]

class CORE_CS2_072:# <7>[1637]
	""" Backstab
	Deal $2 damage to an undamaged minion. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0,
		PlayReq.REQ_UNDAMAGED_TARGET: 0}
	play = Hit(TARGET, 2)	
	pass

class CORE_CS2_073:# <7>[1637]
	""" Cold Blood
	Give a minion +2 Attack. [Combo:] +4 Attack instead. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "CS2_073e")
	combo = Buff(TARGET, "CS2_073e2")
	pass
CS2_073e = buff(atk=2)
CS2_073e2 = buff(atk=4)

class CORE_CS2_074:# <7>[1637]
	""" Deadly Poison
	Give your weapon +2_Attack. """
	requirements = {PlayReq.REQ_WEAPON_EQUIPPED: 0}
	play = Buff(FRIENDLY_WEAPON, "CS2_074e")
	pass
CS2_074e = buff(atk=2)

class CORE_CS2_075:# <7>[1637]
	""" Sinister Strike
	Deal $3 damage to the_enemy hero. """
	play = Hit(ENEMY_HERO, 3)
	pass

class CORE_CS2_076:# <7>[1637]
	""" Assassinate
	Destroy an enemy minion. """
	requirements = {
		PlayReq.REQ_ENEMY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Destroy(TARGET)	
	pass

class CORE_CS2_077:# <7>[1637]
	""" Sprint
	Draw 4 cards. """
	play = Draw(CONTROLLER) * 4	
	pass

class CORE_CS2_080:# <7>[1637]
	""" Assassin's Blade
	 """
	#vanilla
	pass

class CORE_EX1_134:# <7>[1637]
	""" SI:7 Agent
	[Combo:] Deal 2 damage. """
	requirements = {PlayReq.REQ_TARGET_FOR_COMBO: 0, PlayReq.REQ_MINION_TARGET:0}
	combo = Hit(TARGET, 2)	
	pass

class CORE_EX1_144:# <7>[1637]
	""" Shadowstep
	Return a friendly minion to your hand. It_costs (2) less. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Bounce(TARGET), Buff(TARGET, "EX1_144e")

@custom_card
class EX1_144e:
	tags = {
		GameTag.CARDNAME: "Shadowstep Buff",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.COST: -2,
	}
	events = REMOVED_IN_PLAY

class CORE_EX1_145:# <7>[1637]##
	""" Preparation
	The next spell you cast this turn costs (2) less. """
	play = Buff(FRIENDLY_HAND + SPELL, 'EX1_145e')
	pass
class EX1_145e:
	cost = lambda self, i : max(i-2,0)
	events =[
		OWN_SPELL_PLAY.on(Destroy(SELF)),
		OWN_TURN_END.on(Destroy(SELF))
		]
	pass
EX1_145o=buff(cost=-2)#ONE_TURN_EFFECT

class CORE_EX1_522:# <7>[1637]#
	""" Patient Assassin
	[Stealth] [Poisonous] """
	#
	pass

class CORE_ICC_809:# <7>[1637]##
	""" Plague Scientist
	[Combo:] Give a friendly minion [Poisonous]. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_FOR_COMBO: 0}
	combo = Buff(TARGET, 'ICC_809e')
	pass
ICC_809e=buff(poisonous=True)

class CORE_KAR_069:# <7>[1637]
	""" Swashburglar
	[Battlecry:] Add a random card from another class to_your hand. """
	play = Give(CONTROLLER, RandomCollectible(card_class=ENEMY_CLASS))
	pass

class CORE_LOE_012:# <7>[1637]
	""" Tomb Pillager
	[Deathrattle:] Add a Coin to your hand. """
	deathrattle = Give(CONTROLLER, "GAME_005")
	pass

class CORE_OG_070:# <7>[1637]
	""" Bladed Cultist
	[Combo:] Gain +1/+1. """
	combo = Buff(SELF, "OG_070e")
OG_070e = buff(+1, +1)

class CS3_005Action(TargetedAction):
	""" Vanessa VanCleef
	[Combo:] Add a copy of the last card your opponent played to your hand. """
	TARGET=ActionArg()
	def do(self,source,target):
		controller = target
		opponent = controller.opponent
		opponent_play = opponent.play_log
		if len(opponent_play)>0:
			last_card_id=opponent_play[-1].id
			Give(controller,last_card_id).trigger(source)
		pass
class CS3_005:# <7>[1637]#
	""" Vanessa VanCleef
	[Combo:] Add a copy of the last card your opponent played to your hand. """
	combo = CS3_005Action(CONTROLLER)
	pass

