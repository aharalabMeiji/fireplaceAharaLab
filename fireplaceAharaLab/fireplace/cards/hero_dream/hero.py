from ..utils import *

class HERO_01:
	""" Garrosh Hellscream
	"""
	pass

class HERO_01bp:
	"""Armor Up! (Garrosh Hellscream)"""
	activate = GainArmor(FRIENDLY_HERO, 2)
class HERO_01bp2:#OK
	""" Tank Up!
	<b>Hero Power</b>
	Gain 4 Armor."""
	activate = GainArmor(FRIENDLY_HERO, 4)
	pass

class HERO_05:
	""" Garrosh Hellscream
	"""
	pass

class HERO_05bp:
	"""Steady Shot (Rexxar)"""
	requirements = {PlayReq.REQ_MINION_OR_ENEMY_HERO: 0, PlayReq.REQ_STEADY_SHOT: 0}
	activate = Hit(ENEMY_HERO, 2)
	pass
class HERO_05bp2:#OK
	"""Ballista Shot
	<b>Hero Power</b>
	Deal $3 damage to the enemy hero.@<b>Hero Power</b>
	Deal $3 damage."""
	requirements = {PlayReq.REQ_MINION_OR_ENEMY_HERO: 0, PlayReq.REQ_STEADY_SHOT: 0}
	activate = Hit(ENEMY_HERO, 3)
	pass
class HERO_05dbp:
	"""Steady Shot (Rexxar)"""
	requirements = { 
		PlayReq.REQ_ENEMY_TARGET: 0, 
		PlayReq.REQ_HERO_OR_MINION_TARGET: 0, #new comer
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	activate = Hit(TARGET, 2)
	pass


class HERO_06:
	""" Malfurion Stormrage
	"""
	pass
class HERO_06bp:
	"""Shapeshift"""
	activate = Buff(FRIENDLY_HERO, "HERO_06ebp"), GainArmor(FRIENDLY_HERO, 1)
HERO_06ebp = buff(atk=1)
class HERO_06bp2:#OK
	"""Dire Shapeshift
	<b>Hero Power</b>
	+2 Attack this turn.
	+2 Armor."""
	activate = Buff(FRIENDLY_HERO, "HERO_06ebp2"), GainArmor(FRIENDLY_HERO, 2)
HERO_06ebp2 = buff(atk=2)

class HERO_08:
	"""  Jaina Proudmoore
	"""
	pass
class HERO_08bp:
	"""Fireblast (Jaina Proudmoore)"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	activate = Hit(TARGET, 1)
	pass
class HERO_08bp2:#OK
	"""Fireblast Rank 2
	<b>Hero Power</b>
	Deal $2 damage."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	activate = Hit(TARGET, 2)
	pass

