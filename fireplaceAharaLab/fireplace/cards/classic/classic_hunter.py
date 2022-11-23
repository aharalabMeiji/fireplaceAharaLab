
from ..utils import *

Classic_Hunter=[]
Classic_Hunters_Mark=True
Classic_Starving_Buzzard=True
Classic_Houndmaster=True
Classic_Timber_Wolf=True
Classic_Tundra_Rhino=True
Classic_Multi_Shot=True
Classic_Tracking=True
Classic_Arcane_Shot=True
Classic_Gladiators_Longbow=True
Classic_Scavenging_Hyena=True
Classic_Misdirection=True
Classic_Savannah_Highmane=True
Classic_Eaglehorn_Bow=True
Classic_Explosive_Shot=True
Classic_Unleash_the_Hounds=True
Classic_Kill_Command=True
Classic_King_Krush=True
Classic_Flare=True
Classic_Bestial_Wrath=True
Classic_Snake_Trap=True
Classic_Snake=True
Classic_Snipe=True
Classic_Explosive_Trap=True
Classic_Freezing_Trap=True
Classic_Deadly_Shot=True
Classic_Steady_Shot=True
Classic_Ballista_Shot=True
Classic_Animal_Companion=True
Classic_Misha=True
Classic_Leokk=True
Classic_Huffer=True

if Classic_Hunters_Mark:# 
	Classic_Hunter+=['VAN_CS2_084','CS2_084e']
class VAN_CS2_084:# <3>[1646]
	""" Hunter's Mark
	Change a minion's Health to 1. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "CS2_084e")
	pass
class CS2_084e:
	max_health = SET(1)

if Classic_Starving_Buzzard:# 
	Classic_Hunter+=['VAN_CS2_237']
class VAN_CS2_237:# <3>[1646]
	""" Starving Buzzard
	Whenever you summon a Beast, draw a card. """
	events = Summon(CONTROLLER, BEAST).on(Draw(CONTROLLER))
	pass

if Classic_Houndmaster:# 
	Classic_Hunter+=['VAN_DS1_070','DS1_070o']
class VAN_DS1_070:# <3>[1646]
	""" Houndmaster
	[Battlecry:] Give a friendly Beast +2/+2 and [Taunt]. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0,
		PlayReq.REQ_TARGET_WITH_RACE: 20}
	powered_up = Find(FRIENDLY_MINIONS + BEAST)
	play = Buff(TARGET, "DS1_070o")
	pass
DS1_070o = buff(+2, +2, taunt=True)

if Classic_Timber_Wolf:# 
	Classic_Hunter+=['VAN_DS1_175','DS1_175o']
class VAN_DS1_175:# <3>[1646]
	""" Timber Wolf
	Your other Beasts have +1_Attack. """
	update = Refresh(FRIENDLY_MINIONS + BEAST - SELF, buff="DS1_175o")
	pass
DS1_175o = buff(atk=1)

if Classic_Tundra_Rhino:# 
	Classic_Hunter+=['VAN_DS1_178','DS1_178e']
class VAN_DS1_178:# <3>[1646]
	""" Tundra Rhino
	Your Beasts have [Charge]. """
	update = Refresh(FRIENDLY_MINIONS + BEAST, buff="DS1_178e")
	pass
DS1_178e = buff(charge=True)

if Classic_Multi_Shot:# 
	Classic_Hunter+=['VAN_DS1_183']
class VAN_DS1_183:# <3>[1646]
	""" Multi-Shot
	Deal $3 damage to two random enemy minions. """
	requirements = {PlayReq.REQ_MINIMUM_ENEMY_MINIONS: 1}
	play = Hit(RANDOM_ENEMY_MINION * 2, 3)
	pass

if Classic_Tracking:# 
	Classic_Hunter+=['VAN_DS1_184']
class VAN_DS1_184:# <3>[1646]
	""" Tracking
	Look at the top 3 cards of your deck. Draw one and discard the others. """
	play = GenericChoice(CONTROLLER, FRIENDLY_DECK[:3])
	pass

if Classic_Arcane_Shot:# 
	Classic_Hunter+=['VAN_DS1_185']
class VAN_DS1_185:# <3>[1646]
	""" Arcane Shot
	Deal $2 damage. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 2)
	pass

if Classic_Gladiators_Longbow:# 
	Classic_Hunter+=['VAN_DS1_188']
class VAN_DS1_188:# <3>[1646]
	""" Gladiator's Longbow
	Your hero is [Immune] while attacking. """
	update = Refresh(FRIENDLY_HERO, {GameTag.IMMUNE_WHILE_ATTACKING: True})
	pass

if Classic_Scavenging_Hyena:# 
	Classic_Hunter+=['VAN_EX1_531','EX1_531e']
class VAN_EX1_531:# <3>[1646]
	""" Scavenging Hyena
	Whenever a friendly Beast dies, gain +2/+1. """
	events = Death(FRIENDLY + BEAST).on(Buff(SELF, "EX1_531e"))
	pass
EX1_531e = buff(+2, +1)

if Classic_Misdirection:# 
	Classic_Hunter+=['VAN_EX1_533']
class VAN_EX1_533:# <3>[1646]
	""" Misdirection
	[Secret:] When an enemy attacks your hero, instead it attacks another random character. """
	secret = Attack(ALL_CHARACTERS, FRIENDLY_HERO).on(
		Reveal(SELF),
		Retarget(Attack.ATTACKER, RANDOM(ALL_CHARACTERS - FRIENDLY_HERO - Attack.ATTACKER))
	)
	pass

if Classic_Savannah_Highmane:# 
	Classic_Hunter+=['VAN_EX1_534','EX1_534t']
class VAN_EX1_534:# <3>[1646]
	""" Savannah Highmane
	[Deathrattle:] Summon two 2/2 Hyenas. """
	deathrattle = Summon(CONTROLLER, "EX1_534t") * 2
	pass
class EX1_534t:
	""" 2/2 Hyena """
	pass

if Classic_Eaglehorn_Bow:# 
	Classic_Hunter+=['VAN_EX1_536','EX1_536e']
class VAN_EX1_536:# <3>[1646]
	""" Eaglehorn Bow
	Whenever a [Secret] is revealed, gain +1 Durability. """
	events = Reveal(FRIENDLY_SECRETS).on(Buff(SELF, "EX1_536e"))
	pass
EX1_536e = buff(health=1)

if Classic_Explosive_Shot:# 
	Classic_Hunter+=['VAN_EX1_537']
class VAN_EX1_537:# <3>[1646]
	""" Explosive Shot
	Deal $5 damage to a minion and $2 damage to adjacent ones. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 5), Hit(TARGET_ADJACENT, 2)
	pass

if Classic_Unleash_the_Hounds:# 
	Classic_Hunter+=['VAN_EX1_538','EX1_538t']
class VAN_EX1_538:# <3>[1646]
	""" Unleash the Hounds
	For each enemy minion, summon a 1/1 Hound with [Charge]. """
	requirements = {PlayReq.REQ_MINIMUM_ENEMY_MINIONS: 1, PlayReq.REQ_NUM_MINION_SLOTS: 1}
	play = Summon(CONTROLLER, "EX1_538t") * Count(ENEMY_MINIONS)
	pass
class EX1_538t:
	""" 1/1 Hound with [Charge]"""
	pass

if Classic_Kill_Command:# 
	Classic_Hunter+=['VAN_EX1_539']
class VAN_EX1_539:# <3>[1646]
	""" Kill Command
	Deal $3 damage. If you control a Beast, deal$5 damage instead. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	powered_up = Find(FRIENDLY_MINIONS + BEAST)
	play = powered_up & Hit(TARGET, 5) | Hit(TARGET, 3)
	pass

if Classic_King_Krush:# 
	Classic_Hunter+=['VAN_EX1_543']
class VAN_EX1_543:# <3>[1646]
	""" King Krush
	[Charge] """
	#
	pass

if Classic_Flare:# 
	Classic_Hunter+=['VAN_EX1_544']
class VAN_EX1_544:# <3>[1646]
	""" Flare
	All minions lose [Stealth]. Destroy all enemy [Secrets]. Draw a card. """
	play = (
		Unstealth(ALL_MINIONS),
		Destroy(ENEMY_SECRETS),
		Draw(CONTROLLER),
	)
	pass

if Classic_Bestial_Wrath:# 
	Classic_Hunter+=['VAN_EX1_549','EX1_549o']
class VAN_EX1_549:# <3>[1646]
	""" Bestial Wrath
	Give a Beast +2 Attack and [Immune] this turn. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0,
		PlayReq.REQ_TARGET_WITH_RACE: 20}
	play = Buff(TARGET, "EX1_549o")
	pass
EX1_549o = buff(atk=2, immune=True)

if Classic_Snake_Trap:# 
	Classic_Hunter+=['VAN_EX1_554']
class VAN_EX1_554:# <3>[1646]
	""" Snake Trap
	[Secret:] When one of your minions is attacked, summon three 1/1 Snakes. """
	secret = Attack(ALL_MINIONS, FRIENDLY_MINIONS).on(FULL_BOARD | (
		Reveal(SELF), Summon(CONTROLLER, "VAN_EX1_554t") * 3
	))
	pass

if Classic_Snake:# 
	Classic_Hunter+=['VAN_EX1_554t']
class VAN_EX1_554t:# <3>[1646]
	""" Snake
	 """
	#
	pass

if Classic_Snipe:# 
	Classic_Hunter+=['VAN_EX1_609']
class VAN_EX1_609:# <3>[1646]
	""" Snipe
	[Secret:] After your opponent plays a minion, deal $4 damage to it. """
	secret = Play(OPPONENT, MINION).after(
		Reveal(SELF), Hit(Play.CARD, 4)
	)
	pass

if Classic_Explosive_Trap:# 
	Classic_Hunter+=['VAN_EX1_610']
class VAN_EX1_610:# <3>[1646]
	""" Explosive Trap
	[Secret:] When your hero is attacked, deal $2 damage to all enemies. """
	secret = Attack(ENEMY_CHARACTERS, FRIENDLY_HERO).on(
		Reveal(SELF), Hit(ENEMY_CHARACTERS, 2)
	)
	pass

if Classic_Freezing_Trap:# 
	Classic_Hunter+=['VAN_EX1_611','EX1_611e']
class VAN_EX1_611:# <3>[1646]
	""" Freezing Trap
	[Secret:] When an enemy minion attacks, return it to its owner's hand. It costs (2) more. """
	secret = Attack(ENEMY_MINIONS).on(
		Reveal(SELF),
		Bounce(Attack.ATTACKER),
		Buff(Attack.ATTACKER, "EX1_611e")
	)
	pass
class EX1_611e:
	events = REMOVED_IN_PLAY
	tags = {GameTag.COST: +2}

if Classic_Deadly_Shot:# 
	Classic_Hunter+=['VAN_EX1_617']
class VAN_EX1_617:# <3>[1646]
	""" Deadly Shot
	Destroy a random enemy minion. """
	requirements = {PlayReq.REQ_MINIMUM_ENEMY_MINIONS: 1}
	play = Destroy(RANDOM_ENEMY_MINION)
	pass

if Classic_Steady_Shot:# 
	Classic_Hunter+=['VAN_HERO_05bp']
class VAN_HERO_05bp:# <3>[1646]
	""" Steady Shot
	[Hero Power]Deal $2 damage to the enemy hero.@[Hero Power]Deal $2 damage. """
	requirements = {PlayReq.REQ_MINION_OR_ENEMY_HERO: 0, PlayReq.REQ_STEADY_SHOT: 0}
	activate = Hit(ENEMY_HERO, 2)
	pass

if Classic_Ballista_Shot:# 
	Classic_Hunter+=['VAN_HERO_05bp2']
class VAN_HERO_05bp2:# <3>[1646]
	""" Ballista Shot
	[Hero Power]Deal $3 damage to the enemy hero.@[Hero Power]Deal $3 damage. """
	#
	pass

if Classic_Animal_Companion:# 
	Classic_Hunter+=['VAN_NEW1_031']
class VAN_NEW1_031_Action(GameAction):
	def do(self, source):
		cards=["VAN_NEW1_032", "VAN_NEW1_033", "VAN_NEW1_034"]
		Summon(source.controller, random.choice(cards)).trigger(source)
class VAN_NEW1_031:# <3>[1646]
	""" Animal Companion
	Summon a random Beast Companion. """
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	entourage = ["VAN_NEW1_032", "VAN_NEW1_033", "VAN_NEW1_034"]
	play = VAN_NEW1_031_Action()
	pass

if Classic_Misha:# 
	Classic_Hunter+=['VAN_NEW1_032']
class VAN_NEW1_032:# <3>[1646]
	""" Misha
	[Taunt] """
	#
	pass

if Classic_Leokk:# 
	Classic_Hunter+=['VAN_NEW1_033','NEW1_033o']
class VAN_NEW1_033:# <3>[1646]
	""" Leokk
	Your other minions have +1 Attack. """
	update = Refresh(FRIENDLY_MINIONS - SELF, buff="NEW1_033o")
	pass
NEW1_033o = buff(atk=1)

if Classic_Huffer:# 
	Classic_Hunter+=['VAN_NEW1_034']
class VAN_NEW1_034:# <3>[1646]
	""" Huffer
	[Charge] """
	#
	pass


