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

class HERO_02:
	pass
class HERO_02bp:
	"""Totemic Call"""
	requirements = {
		PlayReq.REQ_ENTIRE_ENTOURAGE_NOT_IN_PLAY: 0,
		PlayReq.REQ_NUM_MINION_SLOTS: 1}
	entourage = ["CS2_050", "CS2_051", "CS2_052", "NEW1_009"]
	def activate(self):
		totems = [t for t in self.entourage if not self.controller.field.contains(t)]
		if len(totems)>0:
			yield Summon(CONTROLLER, random.choice(totems))##
	pass
class CS2_050: 
	""" Searing Totem
	"""
	pass
class CS2_051: 
	""" Stoneclaw Totem
	&lt;b&gt;Taunt&lt;/b&gt; """
	pass
class CS2_052: 
	""" Wrath of Air Totem
	&lt;b&gt;Spell Damage +1&lt;/b&gt; """ 
	pass
class NEW1_009:
	""" Healing Totem
	At the end of your turn, restore #1 Health to all friendly minions. """
	events = OWN_TURN_END.on(Heal(FRIENDLY_MINIONS, 1))
	pass
class HERO_02bp2:################################# pass, need to modify 
	""" Totemic Slam
	<b>Hero Power</b>
	Summon a Totem of your choice."""
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	choose = ("CS2_050", "CS2_051", "CS2_052", "NEW1_009")

class HERO_03:
	""" Valeera Sanguinar
	"""
	pass
class HERO_03bp:
	"""Dagger Mastery"""
	activate = Find(FRIENDLY_WEAPON + ID("AT_034")) | Summon(CONTROLLER, "CS2_082")
	pass
class HERO_03bp2:#OK
	""" Poisoned Daggers
	<b>Hero Power</b>
	Equip a 2/2 Weapon."""
	activate = Summon(CONTROLLER, "AT_132_ROGUEt")
	pass
class AT_034:
	"""Poisoned Blade"""
	inspire = Buff(SELF, "AT_034e")
	pass
AT_034e = buff(atk=1)
class CS2_082:
	""" Wicked Knife
	(weapon) """
	pass
class AT_132_ROGUEt:
	""" Poisoned Dagger
	(weapon) """
	pass

class HERO_04:
	""" Uther Lightbringer
	"""
class HERO_04bp:
	"""Reinforce (Uther Lightbringer)"""
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	activate = Summon(CONTROLLER, "CS2_101t")
class CS2_101t:
	""" Silver Hand Recruit (1/1/1)
	"""
class HERO_04bp2:#OK
	""" The Silver Hand
	<b>Hero Power</b>
	Summon two 1/1 Recruits."""
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	activate = Summon(CONTROLLER, "CS2_101t") * 2

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
	activate = Buff(FRIENDLY_HERO, "CS2_017o"), GainArmor(FRIENDLY_HERO, 1)
#HERO_06ebp = buff(atk=1)
CS2_017o = buff(atk=1)
class HERO_06bp2:#OK
	"""Dire Shapeshift
	<b>Hero Power</b>
	+2 Attack this turn.
	+2 Armor."""
	activate = Buff(FRIENDLY_HERO, "AT_132_DRUIDe"), GainArmor(FRIENDLY_HERO, 2)
#HERO_06ebp2 = buff(atk=2)
AT_132_DRUIDe = buff(atk=2)

class HERO_07:
	""" Gul'dan
	"""
	pass
class HERO_07bp:
	"""Life Tap"""
	activate = Hit(FRIENDLY_HERO, 2), Draw(CONTROLLER)
class HERO_07bp2:#OK
	"""Soul Tap
	<b>Hero Power</b>	Draw a card."""
	activate = Draw(CONTROLLER)

class HERO_08:
	"""  Jaina Proudmoore
	"""
	pass
class HERO_08bp:
	"""Fireblast (Jaina Proudmoore)"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0, PlayReq.REQ_ENEMY_TARGET: 0, PlayReq.REQ_HERO_OR_MINION_TARGET:0}
	activate = Hit(TARGET, 1)
	pass
class HERO_08bp2:#OK
	"""Fireblast Rank 2
	<b>Hero Power</b>
	Deal $2 damage."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0, PlayReq.REQ_ENEMY_TARGET: 0, PlayReq.REQ_HERO_OR_MINION_TARGET:0}
	activate = Hit(TARGET, 2)
	pass

class HERO_09:#
	""" Anduin Wrynn  """
	pass

class HERO_09bp:#
	"""Lesser Heal (Anduin Wrynn)"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	activate = Heal(TARGET, 2)
class HERO_09bp2:#OK
	"""Heal
	<b>Hero Power</b>
	Restore #4 Health."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	activate = Heal(TARGET, 4)
