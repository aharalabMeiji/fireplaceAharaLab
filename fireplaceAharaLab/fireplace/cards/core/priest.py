from ..utils import *

Core_Priest=[
	"CORE_AT_055","CORE_CS1_112","CORE_CS1_130",
	]
class CORE_AT_055:# <6>[1637]
	""" Flash Heal
	Restore #5 Health. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Heal(TARGET, 5)	
	pass

class CORE_CS1_112:# <6>[1637]
	""" Holy Nova
	Deal $2 damage to all enemy minions. Restore #2 Health to all friendly characters. """
	play = Hit(ENEMY_MINIONS, 2), Heal(FRIENDLY_CHARACTERS, 2)
	pass

class CORE_CS1_130:# <6>[1637]
	""" Holy Smite
	Deal $3 damageto a minion. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 3)
	pass

class CORE_EX1_193:# <6>[1637]## no EX1_193 card ################
	""" Psychic Conjurer
	[Battlecry:] Copy a card in your opponent’s deck and add it to your hand. """
	#
	pass

class CORE_EX1_194:# <6>[1637]## no EX1_194 card ################
	""" Power Infusion
	Give a minion +2/+6. """
	#
	pass

class CORE_EX1_195:# <6>[1637]## no EX1_195 card ################
	""" Kul Tiran Chaplain
	[Battlecry:] Give a friendly minion +2 Health. """
	#
	pass

class CORE_EX1_197:# <6>[1637]## no EX1_197 card ################
	""" Shadow Word: Ruin
	Destroy all minions with 5 or more Attack. """
	#
	pass

class CORE_EX1_198:# <6>[1637]## no EX1_198 card ################
	""" Natalie Seline
	[Battlecry:] Destroy a minion and gain its Health. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_ENEMY_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = (
		Buff(SELF, 'EX1_198e', max_health=CURRENT_HEALTH(TARGET)),
		Destroy(TARGET)
		)
	pass


class CORE_EX1_335:# <6>[1637]
	""" Lightspawn
	This minion's Attack is always equal to its Health. """
	update = Refresh(SELF, {GameTag.ATK: lambda self, i: self.health}, priority=100)
	pass

class CORE_EX1_622:# <6>[1637]
	""" Shadow Word: Death
	Destroy a minion with 5_or more Attack. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_MIN_ATTACK: 5,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Destroy(TARGET)
	pass

class CORE_EX1_623:# <6>[1637]
	""" Temple Enforcer
	[Battlecry:] Give a friendly minion +3 Health. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Buff(TARGET, "EX1_623e")
	pass
EX1_623e = buff(health=3)

class CORE_EX1_625:# <6>[1637]
	""" Shadowform
	Your Hero Power becomes 'Deal 2 damage.' """
	play = Switch(FRIENDLY_HERO_POWER, {
		"EX1_625t": Summon(CONTROLLER, "EX1_625t2"),
		"EX1_625t2": (),
		None: Summon(CONTROLLER, "EX1_625t"),
	})
class EX1_625t:
	"""Mind Spike"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	activate = Hit(TARGET, 2)
	update = Refresh(CONTROLLER, {GameTag.SHADOWFORM: True})
class EX1_625t2:
	"""Mind Shatter"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	activate = Hit(TARGET, 3)
	update = Refresh(CONTROLLER, {GameTag.SHADOWFORM: True})

class CS3_013:# <6>[1637]
	""" Shadowed Spirit
	[Deathrattle:] Deal 3 damage to the enemy hero. """
	deathrattle = Hit(ENEMY_HERO, 3)
	pass

class CS3_014:# <6>[1637]
	""" Crimson Clergy
	After a friendly character is healed, gain +1 Attack. """
	#
	pass

class CS3_014e:# <6>[1637]
	""" Holy Affinity
	+1 Attack. """
	#
	pass

class CS3_027:# <6>[1637]
	""" Focused Will
	[Silence] a minion, then give it +3 Health. """
	#
	pass

class CS3_027e:# <6>[1637]
	""" Focused Will
	+3 Health. """
	#
	pass
