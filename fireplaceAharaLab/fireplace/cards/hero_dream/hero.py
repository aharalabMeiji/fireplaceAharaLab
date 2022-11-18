from ..utils import *

Heroes=[
	'HERO_01',
	'HERO_01bp','HERO_01bp2',#Armor Up!
]
class HERO_01:
	""" Garrosh Hellscream
	"""
	pass

class HERO_01bp:
	"""Armor Up! (Garrosh Hellscream)"""
	activate = GainArmor(FRIENDLY_HERO, 2)
class HERO_01bp2:#OK
	""" Tank Up!
	[Hero Power]
	Gain 4 Armor."""
	activate = GainArmor(FRIENDLY_HERO, 4)
	pass

Heroes+=[
	'HERO_02',
	'HERO_02bp','HERO_02bp2',#Totemic Call
	"CS2_050", "CS2_051", "CS2_052", "NEW1_009",
	]
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
	[Taunt] """
	pass
class CS2_052: 
	""" Wrath of Air Totem
	[Spell Damage +1] """ 
	pass
class NEW1_009:
	""" Healing Totem
	At the end of your turn, restore #1 Health to all friendly minions. """
	events = OWN_TURN_END.on(Heal(FRIENDLY_MINIONS, 1))
	pass
class HERO_02bp2:################################# pass, need to modify 
	""" Totemic Slam
	[Hero Power]
	Summon a Totem of your choice."""
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	choose = ("CS2_050", "CS2_051", "CS2_052", "NEW1_009")

Heroes+=[	'HERO_03',
	'HERO_03bp','HERO_03bp2',#Dagger Mastery
	'AT_034','AT_034e','CS2_082','AT_132_ROGUEt',
]
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
	[Hero Power]
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
Heroes+=[	'HERO_04',
	'HERO_04bp','HERO_04bp2','CS2_101t',#steady shot
]
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
	[Hero Power]
	Summon two 1/1 Recruits."""
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	activate = Summon(CONTROLLER, "CS2_101t") * 2

Heroes+=[	'HERO_05',
	'HERO_05bp','HERO_05bp2','HERO_05dbp',#Reinforce 
]
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
	[Hero Power]
	Deal $3 damage to the enemy hero.@[Hero Power]
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

Heroes+=[	'HERO_06',	
	'HERO_06bp','CS2_017o','HERO_06bp2','AT_132_DRUIDe',#Shapeshift
]
class HERO_06:
	""" Malfurion Stormrage
	"""
	pass
class HERO_06bp:
	"""Shapeshift"""
	activate = Buff(FRIENDLY_HERO, "HERO_06bpe"), GainArmor(FRIENDLY_HERO, 1)
@custom_card
class HERO_06bpe:
	tags = {
		GameTag.CARDNAME: "Dire Shapeshift",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.ATK: 1,
		GameTag.TAG_ONE_TURN_EFFECT: 1,}
class HERO_06bp2:#OK
	"""Dire Shapeshift
	[Hero Power]
	+2 Attack this turn.
	+2 Armor."""
	activate = Buff(FRIENDLY_HERO, "HERO_06bp2e"), GainArmor(FRIENDLY_HERO, 2)
@custom_card
class HERO_06bp2e:
	tags = {
		GameTag.CARDNAME: "Dire Shapeshift",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.ATK: 2,
		GameTag.TAG_ONE_TURN_EFFECT: 1,}


Heroes+=[	'HERO_07',
	'HERO_07bp','HERO_07bp2',#Life Tap
]
class HERO_07:
	""" Gul'dan
	"""
	pass
class HERO_07bp:
	"""Life Tap"""
	activate = Hit(FRIENDLY_HERO, 2), Draw(CONTROLLER)
class HERO_07bp2:#OK
	"""Soul Tap
	[Hero Power]	Draw a card."""
	activate = Draw(CONTROLLER)

Heroes+=[	'HERO_08',
	'HERO_08bp','HERO_08bp2',# Fireblast(<4>[1635])
]
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
	[Hero Power]
	Deal $2 damage."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0, PlayReq.REQ_ENEMY_TARGET: 0, PlayReq.REQ_HERO_OR_MINION_TARGET:0}
	activate = Hit(TARGET, 2)
	pass

Heroes+=[	'HERO_09',
	'HERO_09bp','HERO_09bp2',# Lesser Heal
	]
class HERO_09:#
	""" Anduin Wrynn  """
	pass

class HERO_09bp:#
	"""Lesser Heal (Anduin Wrynn)"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	activate = Heal(TARGET, 2)
class HERO_09bp2:#OK
	"""Heal
	[Hero Power]
	Restore #4 Health."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	activate = Heal(TARGET, 4)

	
Heroes+=['HERO_10',
	'HERO_10bp','HERO_10bpe','HERO_10bp2','HERO_10pe2',##Demon Claws
	]
class HERO_10:#
	""" Illidan Stormrage  """
	pass
class HERO_10bp:#
	"""Demon Claws
	[x][Hero Power]+1 Attack this turn."""
	activate = Buff(FRIENDLY_HERO, 'HERO_10bpe')
HERO_10bpe=buff(1,0)
#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>
class HERO_10bp2:#OK
	"""Demon's Bite
	[Hero Power] +2 Attack this turn."""
	activate = Buff(FRIENDLY_HERO, 'HERO_10pe2')
HERO_10pe2=buff(2,0)

