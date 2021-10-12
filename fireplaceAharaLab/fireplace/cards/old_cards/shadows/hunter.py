from ..utils import *

####### hunter in shadows #######

class DAL_373:#OK
	"""Rapid Fire	Spell	Common
	<b>Twinspell</b>
	Deal $1 damage."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0,
			PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Hit(TARGET, 1),Give(CONTROLLER,"DAL_373ts")
class DAL_373ts:
	"""Rapid Fire	Spell	Common"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0,
			PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Hit(TARGET, 1)

class DAL_587:#OK
	"""Shimmerfly	Minion	Rare
	<b>Deathrattle:</b> Add a random Hunter spell to your hand."""
	deathrattle = Give(CONTROLLER, RandomSpell(card_class=CardClass.HUNTER))

class DAL_377:#OK
	"""Nine Lives	Spell	Epic	
	<b>Discover</b> a friendly <b>Deathrattle</b> 
	minion that died this game. Also trigger its <b>Deathrattle</b>."""
	play = Choice(CONTROLLER, RANDOM(FRIENDLY+KILLED+DEATHRATTLE)*3).then(
		Give(CONTROLLER, Copy(Choice.CARD)).then(
			Deathrattle(Give.CARD)
		)
	)

class DAL_604:#OK
	"""Ursatron	Minion	Common
	<b>Deathrattle:</b> Draw a Mech from your deck."""
	deathrattle = ForceDraw(CONTROLLER, RANDOM(FRIENDLY_DECK + MECH))

class DAL_372:#OK
	"""Arcane Fletcher	Minion	Epic
	[x]Whenever you play a
	1-Cost minion, draw a
	spell from your deck."""
	events = Play(CONTROLLER, FRIENDLY_MINIONS + (COST == 1)).on(ForceDraw(CONTROLLER, FRIENDLY_DECK + SPELL))

class DAL_371:#OK
	"""Marked Shot	Spell	Common
	Deal $4 damage to_a_minion. <b>Discover</b>_a_spell."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Hit(TARGET, 4), Discover(CONTROLLER, RandomSpell())

class DAL_589:#OK
	"""Hunting Party	Spell	Rare
	Copy all Beasts in your_hand."""
	play = Give(CONTROLLER, Copy(FRIENDLY_HAND+BEAST))

class DAL_376:#OK ## MECH + DEATHRATTLE = ['DAL_376:Oblivitron','DAL_604:Ursatron']
	"""Oblivitron	Minion	Legendary
	[x]<b>Deathrattle:</b> Summon a
	Mech from your hand and
	trigger its <b>Deathrattle</b>."""
	deathrattle = Summon(CONTROLLER, RANDOM(FRIENDLY_HAND + MECH)).then(Deathrattle(Summon.CARD))

class DAL_378:#OK
	"""Unleash the Beast	Spell	Rare
	<b>Twinspell</b>
	Summon a 5/5 Wyvern with <b>Rush</b>."""
	play = Summon(CONTROLLER, "DAL_378t1"),Give(CONTROLLER, "DAL_378ts")
class DAL_378t1:
	""" Wyvern""" 
	pass
class DAL_378ts:
	play = Summon(CONTROLLER, "DAL_378t1")

class DAL_379:#OK
	"""Vereesa Windrunner	Minion	Legendary
	<b>Battlecry:</b> Equip Thori'dal, the Stars' Fury."""
	play = Summon(CONTROLLER, "DAL_379t")
#DAL_379e
class DAL_379t:
	""" Thori'dal, the Stars' Fury """ 