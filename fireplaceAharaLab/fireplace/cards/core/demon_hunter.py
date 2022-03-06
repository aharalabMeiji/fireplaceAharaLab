from ..utils import *

Core_DemonHunter=[
	"CORE_BT_035","CORE_BT_036","BT_036t","CORE_BT_235","CORE_BT_323","CORE_BT_351","BT_351e","CORE_BT_416","BT_416e","CORE_BT_423","CORE_BT_427","CORE_BT_430","CORE_BT_480","CORE_BT_491","CORE_BT_801","CORE_BT_921","CS3_017","CS3_017e","CS3_019","CS3_020",
	]
class CORE_BT_035:# <14>[1637]
	""" Chaos Strike
	Give your hero +2_Attack this turn. Draw a card. """
	play = Buff(FRIENDLY_HERO, "BT_035e"), Draw(CONTROLLER)
	pass
BT_035e = buff(atk=2)#ONE_TURN_EFFECT

class CORE_BT_036:# <14>[1637]
	""" Coordinated Strike
	Summon three 1/1_Illidari with [Rush]. """
	play = Summon(CONTROLLER, "BT_036t") * 3
	pass
class BT_036t:
	pass

class CORE_BT_235:# <14>[1637]
	""" Chaos Nova
	Deal $4 damage to all_minions. """
	play = Hit(ALL_MINIONS,4)
	pass

class CORE_BT_323:# <14>[1637]
	""" Sightless Watcher
	[Battlecry:] Look at 3 cards in your deck. Choose one to put on top. """
	play = Choice(CONTROLLER, RANDOM(FRIENDLY_DECK) * 3).then(
		PutOnTop(CONTROLLER, Choice.CARD))
	pass

class CORE_BT_351:# <14>[1637]
	""" Battlefiend
	After your hero attacks, gain +1 Attack. """
	events = Attack(FRIENDLY_HERO).after(Buff(SELF, "BT_351e"))
	pass
BT_351e = buff(atk=1)

class CORE_BT_416:# <14>[1637]
	""" Raging Felscreamer
	[Battlecry:] The next Demon you play costs (2) less. """
	play = Buff(CONTROLLER, "BT_416e")
	pass
class BT_416e:
	update = Refresh(FRIENDLY_HAND + DEMON, {GameTag.COST: -2})
	events = Play(CONTROLLER, DEMON).on(Destroy(SELF))

class CORE_BT_423:# <14>[1637]
	""" Ashtongue Battlelord
	[Taunt][Lifesteal] """
	#
	pass

class CORE_BT_427:# <14>[1637]
	""" Feast of Souls
	Draw a card for each friendly minion that died this turn. """
	play = Draw(CONTROLLER) * Count(FRIENDLY + MINION + KILLED_THIS_TURN)
	pass

class CORE_BT_430:# <14>[1637]
	""" Warglaives of Azzinoth
	After attacking a minion, your hero may attack again. """
	events = Attack(FRIENDLY_HERO, ALL_MINIONS).after(
		ExtraAttack(FRIENDLY_HERO))
	pass

class CORE_BT_480:# <14>[1637]
	""" Crimson Sigil Runner
	[Outcast:] Draw a card. """
	outcast = Draw(CONTROLLER)
	pass

class CORE_BT_491:# <14>[1637]
	""" Spectral Sight
	Draw a card.[Outcast:] Draw another. """
	play = Draw(CONTROLLER)
	outcast = Draw(CONTROLLER) * 2
	pass

class CORE_BT_801:# <14>[1637]
	""" Eye Beam
	[Lifesteal]. Deal $3 damage to a minion.[Outcast:] This costs (1). """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 3)
	update = Refresh(OUTERMOST_HAND + SELF, {GameTag.COST: SET(1)})
	pass

class CORE_BT_921:# <14>[1637]
	""" Aldrachi Warblades
	[Lifesteal] """
	#
	pass

class CS3_017:# <14>[1637]
	""" Gan'arg Glaivesmith
	[Outcast:] Give your hero +3_Attack this turn. """
	outcast=Buff(FRIENDLY_HERO,'CS3_017e')
	pass
CS3_017e=buff(atk=3)# ONE_TURN_EFFECT# <14>[1637]
""" Felfist
+3 Attack this turn. """

class CS3_019:# <14>[1637]
	""" Kor'vas Bloodthorn
	[Charge], [Lifesteal]After you play a card with [Outcast], return this to your hand. """
	events = Play(CONTROLLER, FRIENDLY_HAND + OUTCAST).after(Bounce(SELF))
	pass

class CS3_020:# <14>[1637]
	""" Illidari Inquisitor
	[Rush]. After your hero attacks an enemy, this attacks it too. """
	events = Attack(FRIENDLY_HERO, ENEMY_CHARACTERS).after(
		ExtraAttack(SELF))
	pass

