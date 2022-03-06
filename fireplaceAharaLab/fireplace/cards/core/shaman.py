from ..utils import *

#Core_Shaman=[
#	'CORE_AT_047','AT_047e','CORE_BOT_533','CORE_CS2_039','CORE_CS2_042','CORE_CS2_045','CS2_045e','CORE_EX1_238','CORE_EX1_246','hexfrog','CORE_EX1_248','EX1_tk11','CORE_EX1_250','CORE_EX1_258','EX1_258e','CORE_EX1_259','CORE_EX1_567','CORE_EX1_575','CORE_NEW1_010','CORE_UNG_817','CS3_007','',]

class CORE_AT_047:# <8>[1637]
	""" Draenei Totemcarver
	[Battlecry:] Gain +1/+1 for each friendly Totem. """
	play = Buff(SELF, "AT_047e") * Count(FRIENDLY_MINIONS + TOTEM)
	pass
AT_047e = buff(+1, +1)

class CORE_BOT_533:# <8>[1637]
	""" Menacing Nimbus
	[Battlecry:] Add a random Elemental to your hand. """
	play = Give(CONTROLLER, RandomCard(race=Race.ELEMENTAL))
	pass

class CORE_CS2_039:# <8>[1637]
	""" Windfury
	Give a minion [Windfury]. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = GiveWindfury(TARGET - WINDFURY)
	pass

class CORE_CS2_042:# <8>[1637]
	""" Fire Elemental
	[Battlecry:] Deal 4 damage. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Hit(TARGET, 4)	
	pass

class CORE_CS2_045:# <8>[1637]
	""" Rockbiter Weapon
	Give a friendly character +3 Attack this turn. """
	requirements = {PlayReq.REQ_FRIENDLY_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "CS2_045e")
	pass
CS2_045e = buff(atk=3)## ONE_TURN_EFFECT

class CORE_EX1_238:# <8>[1637]
	""" Lightning Bolt
	Deal $3 damage. [Overload:] (1) """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 3)	
	pass

class CORE_EX1_246:# <8>[1637]
	""" Hex
	Transform a minion into a 0/1 Frog with [Taunt]. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Morph(TARGET, "hexfrog")
	pass
#EX1_246e#Morphed buff?
class hexfrog:
	""" Frog
	[Taunt] """

class CORE_EX1_248:# <8>[1637]
	""" Feral Spirit
	Summon two 2/3 Spirit Wolves with [Taunt]. [Overload:] (1) """
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	play = Summon(CONTROLLER, "EX1_tk11") * 2
	pass
class EX1_tk11:
	""" Spirit Wolf
	&lt;b&gt;Taunt&lt;/b&gt; """
	pass

class CORE_EX1_250:# <8>[1637]
	""" Earth Elemental
	[Taunt][[Overload]:] (2) """
	#
	pass

class CORE_EX1_258:# <8>[1637]
	""" Unbound Elemental
	After you play a card_with [Overload], gain_+1/+1. """
	events = Play(CONTROLLER, OVERLOAD).on(Buff(SELF, "EX1_258e"))
	pass
EX1_258e = buff(+1, +1)

class CORE_EX1_259:# <8>[1637]
	""" Lightning Storm
	Deal $3 damage to all_enemy minions. [Overload:] (2) """
	play = Hit(ENEMY_MINIONS, 3)
	pass

class CORE_EX1_567:# <8>[1637]
	""" Doomhammer
	[Windfury, Overload:] (2) """
	#
	pass

class CORE_EX1_575:# <8>[1637]
	""" Mana Tide Totem
	At the end of your turn, draw a card. """
	events = OWN_TURN_END.on(Draw(CONTROLLER))
	pass

class CORE_NEW1_010:# <8>[1637]
	""" Al'Akir the Windlord
	[Charge, Divine Shield, Taunt, Windfury] """
	#
	pass

class CORE_UNG_817:# <8>[1637]
	""" Tidal Surge
	[Lifesteal]Deal $4 damage to a_minion. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 4)
	pass

class CS3_007:# <8>[1637]
	""" Novice Zapper
	[Spell Damage +1] [Overload:] (1) """
	#
	pass

############# core paladin  #######

class CS3_016:# <5>[1637]
	""" Reckoning
	[Secret:] After an enemy minion deals 3 or more damage, destroy it. """
	secret = Attack(ENEMY_MINIONS, FRIENDLY_CHARACTERS).after(
		Reveal(SELF),
		Destroy(Attack.ATTACKER)
		)
	pass

class CORE_AT_075:# <5>[1637]
	""" Warhorse Trainer
	Your Silver Hand Recruits have +1 Attack. """
	update = Refresh(FRIENDLY + ID("CS2_101t"), buff="AT_075e")	
	pass
AT_075e = buff(atk=1)
