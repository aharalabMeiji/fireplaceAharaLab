from ..utils import *

class BT_724:#OK
	"""Ethereal Augmerchant	Minion	Common
	&lt;b&gt;Battlecry:&lt;/b&gt; Deal 1 damage to a minion and give it &lt;b&gt;Spell Damage +1&lt;/b&gt;."""
	requirements = { PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0} 
	play = Hit(TARGET, 1), SetTag(TARGET, (GameTag.SPELLPOWER,))
class BT_722:#OK
	"""Guardian Augmerchant	Minion	Common
	&lt;b&gt;Battlecry:&lt;/b&gt; Deal 1 damage to a minion and give it &lt;b&gt;Divine Shield&lt;/b&gt;."""
	requirements = { PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0} 
	play = Hit(TARGET, 1), 	SetTag(TARGET, (GameTag.DIVINE_SHIELD,))
class BT_731:#OK
	"""Infectious Sporeling	Minion	Rare
	After this damages a minion, turn it into an Infectious_Sporeling."""
	events = Attack(SELF).after(Morph(ATTACK_TARGET,"BT_731"))
class BT_723:#OK
	"""Rocket Augmerchant	Minion	Common
	&lt;b&gt;Battlecry:&lt;/b&gt; Deal 1 damage to a minion and give it &lt;b&gt;Rush&lt;/b&gt;."""
	requirements = { PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0} 
	play = Hit(TARGET, 1), 	SetTag(TARGET, (GameTag.RUSH,))
class BT_727:#OK
	"""Soulbound Ashtongue	Minion	Common
	Whenever this minion takes damage, also deal that amount to your hero."""
	events = Attack(ALL_CHARACTERS,SELF).on(Hit(FRIENDLY_HERO, Attr(Attack.ATTACKER, GameTag.ATK)))
class BT_715:#OK
	"""Bonechewer Brawler	Minion	Common
	[x]&lt;b&gt;Taunt&lt;/b&gt;
	Whenever this minion takes
	_damage, gain +2 Attack."""
	events = Attack(ALL_CHARACTERS,SELF).on(Buff(SELF,"BT_715e"))
BT_715e = buff(2,0)
class BT_156:#OK
	"""Imprisoned Vilefiend	Minion	Common
	&lt;b&gt;Dormant&lt;/b&gt; for 2 turns.
	&lt;b&gt;Rush&lt;/b&gt;"""
	dormant = 2
class BT_733:#OK
	"""Mo'arg Artificer	Minion	Epic
	All minions take double damage from spells."""
	update = Refresh(FRIENDLY_MINIONS, {GameTag.SPELLPOWER_DOUBLE: 1})
class BT_008:#OK
	"""Rustsworn Initiate	Minion	Common
	&lt;b&gt;Deathrattle:&lt;/b&gt; Summon a 1/1 Impcaster with
	&lt;b&gt;Spell Damage +1&lt;/b&gt;."""
	deathrattle = Summon(CONTROLLER,"BT_008t")
class BT_008t:
	pass
class BT_721:
	"""Blistering Rot	Minion	Rare
	[x]At the end of your turn,
	summon a Rot with stats
	equal to this minion's."""
	play = OWN_TURN_END.on(Summon(CONTROLLER, "BT_721t"))
class BT_721t:
	""" Living Rot """
	pass
class BT_714:
	"""Frozen Shadoweaver	Minion	Common
	&lt;b&gt;Battlecry:&lt;/b&gt; &lt;b&gt;Freeze&lt;/b&gt; an_enemy."""
	requirements = {PlayReq.REQ_ENEMY_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Freeze(TARGET)
class BT_730:
	"""Overconfident Orc	Minion	Common
	&lt;b&gt;Taunt&lt;/b&gt;
	While at full Health,
	this has +2 Attack."""
	events = -Damage(SELF).on()
class BT_126:####################################################
	"""Teron Gorefiend	Minion	Legendary
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; Destroy all
	other friendly minions.
	&lt;b&gt;Deathrattle:&lt;/b&gt; Resummon
	them with +1/+1."""
	play = Destroy(FRIENDLY_MINIONS - SELF)
	deathrattle = Summon(CONTROLLER, Destroy.TARGET).then(Buff(Summon.CARD, "BT_126e2"))
BT_126e = buff(0,0)
"""Shadowy Construct"""
BT_126e2 = buff(1,1)
class BT_159:
	"""Terrorguard Escapee	Minion	Common
	&lt;b&gt;Battlecry:&lt;/b&gt; Summon three 1/1 Huntresses for your_opponent."""
	play = Summon(OPPONENT, "BT_159t") * 3
class BT_159t:
	""" Huntress """
	pass
class BT_717:
	"""Burrowing Scorpid	Minion	Common
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; Deal 2 damage.
	If that kills the target,
	gain &lt;b&gt;Stealth&lt;/b&gt;."""
	requirements = {PlayReq.REQ_ENEMY_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 2)
	events = Death(Hit.TARGET).on(SetTag(SELF,GameTag.STEALTH))
class BT_728:
	"""Disguised Wanderer	Minion	Common
	>&lt;b&gt;Deathrattle:&lt;/b&gt; Summon a 9/1 Inquisitor."""
	deathrattel = Summon(CONTROLLER, "BT_728t")
class BT_728t:
	""" Rustsworn Inquisitor """
	pass
class BT_010:
	"""Felfin Navigator	Minion	Common
	&lt;b&gt;Battlecry:&lt;/b&gt; Give your other Murlocs +1/+1."""
	play = Buff(FRIENDLY_MINIONS + MURLOC - SELF, "BT_010e")
BT_010e = buff(1,1)
class BT_850:
	"""Magtheridon	Minion	Legendary
	[x]&lt;b&gt;Dormant&lt;/b&gt;. &lt;b&gt;Battlecry:&lt;/b&gt; Summon
	three 1/3 enemy Warders.
	When they die, destroy all
	minions and awaken."""

#BT_850e
class BT_850t:
	""" Hellfire Warder """
	pass
class BT_737:
	"""Maiev Shadowsong	Minion	Legendary
	&lt;b&gt;Battlecry:&lt;/b&gt; Choose a minion.
	It goes &lt;b&gt;Dormant&lt;/b&gt; for 2 turns."""
class BT_190:
	"""Replicat-o-tron	Minion	Epic
	At the end of your turn, transform a neighbor into a copy of this."""
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
