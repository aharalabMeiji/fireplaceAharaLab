from ..utils import *

##### paladin@uldum,,,10,,,,,

class ULD_145:#OK
	"""Brazen Zealot,,1,2,1,Minion,Rare,-,-
	Whenever you summon a minion, gain +1 Attack."""
	events = Summon(CONTROLLER, MINION).on(Buff(SELF, "ULD_145e"))
ULD_145e = buff(1,0)

class ULD_431:#OK
	"""Making Mummies,,1,-,-,Spell,Legendary,-,Quest
	[x][Quest:] Play 5 [Reborn]
	minions.
	[Reward:] Emperor Wraps."""
	tags={GameTag.SIDEQUEST:True}
	events = Play(CONTROLLER, MINION + EnumSelector(GameTag.REBORN)).on(SidequestCounter(SELF, 5, Summon(CONTROLLER, "ULD_431p")))
class ULD_431e:
	atk = SET(2)
	max_health = SET(2)
	pass
class ULD_431p:
	""" Emperor Wraps
	[x][Hero Power]
	Summon a 2/2 copy
	of a friendly minion."""
	activate = Summon(CONTROLLER, Copy(RANDOM(FRIENDLY_MINIONS))).then(Buff(Summon.CARD, "ULD_431e"))

class ULD_217:#OK
	"""Micro Mummy,,2,1,2,Minion,Epic,Mech,Reborn
	[x][Reborn]
	At the end of your turn, give
	another random friendly
	minion +1 Attack."""
	events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_MINIONS - SELF), "ULD_217e"))
ULD_217e = buff(1,0)

class ULD_439:#OK
	"""Sandwasp Queen,,2,3,1,Minion,Common,Beast,Battlecry
	[Battlecry:] Add two 2/1 Sandwasps to your hand."""
	play = Give(CONTROLLER, "ULD_439t") * 2
class ULD_439t:
	pass

class ULD_500:#OK
	"""Sir Finley of the Sands,,2,2,3,Minion,Legendary,Murloc,Battlecry
	[x][Battlecry:] If your deck has
	no duplicates, [Discover] an
	upgraded Hero Power."""
	## HERO_04bp,HERO_04fbp : hero.power:[Hero Power]Summon a 1/1 Silver Hand Recruit.
	## HERO_04bp2,HERO_04fbp2:[Hero Power]Summon two 1/1 Recruits.
	entourage = ['HERO_01bp2',  'HERO_03bp2', 'HERO_04bp2','HERO_05bp2','HERO_06bp2', 'HERO_07bp2', 'HERO_08bp2', 'HERO_09bp2']
	#'HERO_02bp2',
	powered_up = -FindDuplicates(FRIENDLY_DECK)
	play = powered_up & Choice(CONTROLLER, RandomEntourage()*3).then(Summon(CONTROLLER, Choice.CARD))
#class HERO_01bp2:#OK
#	""" Tank Up!
#	[Hero Power]
#	Gain 4 Armor."""
#	activate = GainArmor(FRIENDLY_HERO, 4)
#class HERO_02bp2:################################# pass 
#	""" Totemic Slam
#	[Hero Power]
#	Summon a Totem of your choice."""
#	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
#	choose = ("AT_132_SHAMANa", "AT_132_SHAMANb", "AT_132_SHAMANc", "AT_132_SHAMANd")
#class HERO_03bp2:#OK
#	""" Poisoned Daggers
#	[Hero Power]
#	Equip a 2/2 Weapon."""
#	activate = Summon(CONTROLLER, "AT_132_ROGUEt")
#class HERO_04bp2:#OK
#	""" The Silver Hand
#	[Hero Power]
#	Summon two 1/1 Recruits."""
#	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
#	activate = Summon(CONTROLLER, "CS2_101t") * 2
#class HERO_05bp2:#OK
#	"""Ballista Shot
#	[Hero Power]
#	Deal $3 damage to the enemy hero.@[Hero Power]
#	Deal $3 damage."""
#	requirements = {PlayReq.REQ_MINION_OR_ENEMY_HERO: 0, PlayReq.REQ_STEADY_SHOT: 0}
#	activate = Hit(ENEMY_HERO, 3)
#class HERO_06bp2:#OK
#	"""Dire Shapeshift
#	[Hero Power]
#	+2 Attack this turn.
#	+2 Armor."""
#	activate = Buff(FRIENDLY_HERO, "AT_132_DRUIDe"), GainArmor(FRIENDLY_HERO, 2)
#AT_132_DRUIDe = buff(atk=2)
#class HERO_07bp2:#OK
#	"""Soul Tap
#	[Hero Power]
#	Draw a card."""
#	activate = Draw(CONTROLLER)
#class HERO_08bp2:#OK
#	"""Fireblast Rank 2
#	[Hero Power]
#	Deal $2 damage."""
#	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
#	activate = Hit(TARGET, 2)
#class HERO_09bp2:#OK
#	"""Heal
#	[Hero Power]
#	Restore #4 Health."""
#	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
#	activate = Heal(TARGET, 4)



class ULD_728:#OK
	"""Subdue,,2,-,-,Spell,Common,-,-
	Set a minion's Attack and Health to 1."""
	requirements = {PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_TO_PLAY:0}
	play = Buff(TARGET,"ULD_728e")
class ULD_728e:
	atk=SET(1)
	max_health=SET(1)

class ULD_438:#OK
	"""Salhet's Pride,,3,3,1,Minion,Rare,Beast,Deathrattle
	[Deathrattle:] Draw two
	1-Health minions from your_deck."""
	deathrattle = ForceDraw(RANDOM(FRIENDLY_DECK + MINION + (COST == 1))) * 2

class ULD_207:#OK
	"""Ancestral Guardian,,4,4,2,Minion,Common,-,Lifesteal
	[Lifesteal]
	[Reborn]"""

class ULD_143:#OK
	"""Pharaoh's Blessing,,6,-,-,Spell,Rare,-,Divine Shield
	Give a minion +4/+4, [Divine Shield], and [Taunt]."""
	requirements = {PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_TO_PLAY:0}
	play = Buff(TARGET,"ULD_143e"), SetTag(TARGET, (GameTag.DIVINE_SHIELD, GameTag.TAUNT))
ULD_143e = buff(4,4)

class ULD_716:#OK
	"""Tip the Scales,,8,-,-,Spell,Epic,-,-
	Summon 7 Murlocs from your deck."""
	play = Summon(CONTROLLER, RANDOM(FRIENDLY_DECK + MURLOC)) * 7