from ..utils import *

class BT_724:
	"""Ethereal Augmerchant	Minion	Common
	&lt;b&gt;Battlecry:&lt;/b&gt; Deal 1 damage to a minion and give it &lt;b&gt;Spell Damage +1&lt;/b&gt;."""
	requirements = { PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0} 
	play = Hit(TARGET, 1)
	update = Refresh(TARGET, {GameTag.SPELLPOWER: +1})
class BT_722:
	"""Guardian Augmerchant	Minion	Common
	&lt;b&gt;Battlecry:&lt;/b&gt; Deal 1 damage to a minion and give it &lt;b&gt;Divine Shield&lt;/b&gt;."""
	requirements = { PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0} 
	play = Hit(TARGET, 1), 	SetTag(TARGET, GameTag.DIVINE_SHIELD)
class BT_731:
	"""Infectious Sporeling	Minion	Rare
	After this damages a minion, turn it into an Infectious_Sporeling."""
	events = Attack(SELF).after(Morph(TARGET,"BT_731"))
class BT_723:
	"""Rocket Augmerchant	Minion	Common
	&lt;b&gt;Battlecry:&lt;/b&gt; Deal 1 damage to a minion and give it &lt;b&gt;Rush&lt;/b&gt;."""
	requirements = { PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0} 
	play = Hit(TARGET, 1), 	SetTag(TARGET, GameTag.RUSH)
class BT_727:
	"""Soulbound Ashtongue	Minion	Common
	Whenever this minion takes damage, also deal that amount to your hero."""
	events = Attack(ALL_CHARACTERS,SELF).on(Hit(FRIENDLY_HERO,Attack.ATTACKER.ATK))
class BT_715:
	"""Bonechewer Brawler	Minion	Common
	[x]&lt;b&gt;Taunt&lt;/b&gt;
	Whenever this minion takes
	_damage, gain +2 Attack."""
	events = Attack(ALL_CHARACTERS,SELF).on(Buff(SELF,"BT_715e"))
BT_715e = buff(2,0)
class BT_156:
	"""Imprisoned Vilefiend	Minion	Common
	&lt;b&gt;Dormant&lt;/b&gt; for 2 turns.
	&lt;b&gt;Rush&lt;/b&gt;"""
	dormant = 2
class BT_733:
	"""Mo'arg Artificer	Minion	Epic
	All minions take double damage from spells."""
	update = Refresh(FRIENDLY_MINIONS, {GameTag.SPELLPOWER_DOUBLE: 1})
class BT_008:
	"""Rustsworn Initiate	Minion	Common
	&lt;b&gt;Deathrattle:&lt;/b&gt; Summon a 1/1 Impcaster with
	&lt;b&gt;Spell Damage +1&lt;/b&gt;."""
	deathrattle = Summon(CONTROLLER,"BT_008t")
class BT_008t:
	pass
class BT_:
	"""Blistering Rot	Minion	Rare
	"""
class BT_:
	"""Frozen Shadoweaver	Minion	Common
	"""
class BT_:
	"""Overconfident Orc	Minion	Common
	"""
class BT_:
	"""Teron Gorefiend	Minion	Legendary
	"""
class BT_:
	"""Terrorguard Escapee	Minion	Common
	"""
class BT_:
	"""Burrowing Scorpid	Minion	Common
	"""
class BT_:
	"""Disguised Wanderer	Minion	Common
	"""
class BT_:
	"""Felfin Navigator	Minion	Common
	"""
class BT_:
	"""Magtheridon	Minion	Legendary
	"""
class BT_:
	"""Maiev Shadowsong	Minion	Legendary
	"""
class BT_:
	"""Replicat-o-tron	Minion	Epic
	"""
class BT_:
	"""Rustsworn Cultist	Minion	Common
	"""
class BT_:
	"""Al'ar	Minion	Legendary
	"""
class BT_:
	"""Ruststeed Raider	Minion	Common
	"""
class BT_:
	"""Waste Warden	Minion	Epic
	"""
class BT_:
	"""Dragonmaw Sky Stalker	Minion	Common
	"""
class BT_:
	"""Scavenging Shivarra	Minion	Common
	"""
class BT_:
	"""Bonechewer Vanguard	Minion	Common
	"""
class BT_:
	"""Kael'thas Sunstrider	Minion	Legendary
	"""
class BT_:
	"""Supreme Abyssal	Minion	Common
	"""
class BT_:
	"""Scrapyard Colossus	Minion	Rare
	"""
