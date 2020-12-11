from ..utils import *

####### hunter in shadows #######

class DAL_373:
	"""Rapid Fire	Spell	Common
	&lt;b&gt;Twinspell&lt;/b&gt;
	Deal $1 damage."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0,
			PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Hit(TARGET, 1),Give(CONTROLLER,"DAL_373ts")
class DAL_373ts:
	"""Rapid Fire	Spell	Common"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0,
			PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Hit(TARGET, 1)

class DAL_587:
	"""Shimmerfly	Minion	Rare
	&lt;b&gt;Deathrattle:&lt;/b&gt; Add a random Hunter spell to your hand."""
	deathrattle = Give(CONTROLLER, RANDOM(SPELL + EnumSelector(CardClass.HUNTER)))

class DAL_377:
	"""Nine Lives	Spell	Epic	
	&lt;b&gt;Discover&lt;/b&gt; a friendly &lt;b&gt;Deathrattle&lt;/b&gt; minion that died this game. Also trigger its &lt;b&gt;Deathrattle&lt;/b&gt;."""
	play = Discover(CONTROLLER, KILLED + FRIENDLY + DEATHRATTLE). after(Deathrattle(Discover.CARDS))

class DAL_604:
	"""Ursatron	Minion	Common
	&lt;b&gt;Deathrattle:&lt;/b&gt; Draw a Mech from your deck."""
	deathrattle = Draw(CONTROLLER, FRIENDLY_DECK + MECH)## Draw?

class DAL_372:
	"""Arcane Fletcher	Minion	Epic
	[x]Whenever you play a
	1-Cost minion, draw a
	spell from your deck."""
	events = Play(CONTROLLER, FRIENDLY_MINIONS + (COST == 1)).on(Draw(CONTROLLER, FRIENDLY_DECK + SPELL))

class DAL_371:
	"""Marked Shot	Spell	Common
	Deal $4 damage to_a_minion. &lt;b&gt;Discover&lt;/b&gt;_a_spell."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Hit(TARGET, 4), Discover(CONTROLLER, SPELL)

class DAL_589:
	"""Hunting Party	Spell	Rare
	Copy all Beasts in your_hand."""
	play = Give(CONTROLLER, Copy(FRIENDLY_HAND+BEAST))

class DAL_376:
	"""Oblivitron	Minion	Legendary
	[x]&lt;b&gt;Deathrattle:&lt;/b&gt; Summon a
	Mech from your hand and
	trigger its &lt;b&gt;Deathrattle&lt;/b&gt;."""
	deathrattle = Summon(CONTROLLER, RANDOM(FRIENDLY_HAND + MECH)), Deathrattle(Summon.CARD)

class DAL_378:
	"""Unleash the Beast	Spell	Rare
	&lt;b&gt;Twinspell&lt;/b&gt;
	Summon a 5/5 Wyvern with &lt;b&gt;Rush&lt;/b&gt;."""
	play = Summon(CONTROLLER, "DAL_378t1").on(Give(CONTROLLER, "DAL_378ts"))
class DAL_378t1:
	""" Wyvern""" 
	pass
class DAL_378ts:
	play = Summon(CONTROLLER, "DAL_378t1")

class DAL_379:
	"""Vereesa Windrunner	Minion	Legendary
	&lt;b&gt;Battlecry:&lt;/b&gt; Equip Thori'dal, the Stars' Fury."""
	play = Summon(CONTROLLER, "DAL_379t")
#DAL_379e
class DAL_379t:
	""" Thori'dal, the Stars' Fury """ 