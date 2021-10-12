from ..utils import *

# 未実装
# 'BT_113e',
# 'BT_187e','BT_187e2','BT_196e',
# 'BT_302e','BT_309e','BT_711e',

class BT_724:#OK
	"""Ethereal Augmerchant	Minion	Common
	<b>Battlecry:</b> Deal 1 damage to a minion and give it <b>Spell Damage +1</b>."""
	requirements = { PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0} 
	play = Hit(TARGET, 1), SetTag(TARGET, (GameTag.SPELLPOWER,))
class BT_724e:
	pass
class BT_722:#OK
	"""Guardian Augmerchant	Minion	Common
	<b>Battlecry:</b> Deal 1 damage to a minion and give it <b>Divine Shield</b>."""
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
	<b>Battlecry:</b> Deal 1 damage to a minion and give it <b>Rush</b>."""
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
	[x]<b>Taunt</b>
	Whenever this minion takes
	_damage, gain +2 Attack."""
	events = Attack(ALL_CHARACTERS,SELF).on(Buff(SELF,"BT_715e"))
BT_715e = buff(2,0)## -> BT_730
class BT_156:#OK
	"""Imprisoned Vilefiend	Minion	Common
	<b>Dormant</b> for 2 turns.
	<b>Rush</b>"""
	dormant = 2
class BT_733:#OK
	"""Mo'arg Artificer	Minion	Epic
	All minions take double damage from spells."""
	update = Refresh(FRIENDLY_MINIONS, {GameTag.SPELLPOWER_DOUBLE: 1})
class BT_008:#OK
	"""Rustsworn Initiate	Minion	Common
	<b>Deathrattle:</b> Summon a 1/1 Impcaster with
	<b>Spell Damage +1</b>."""
	deathrattle = Summon(CONTROLLER,"BT_008t")
class BT_008t:
	pass
class BT_721:#OK
	"""Blistering Rot	Minion	Rare
	[x]At the end of your turn,
	summon a Rot with stats
	equal to this minion's."""
	play = OWN_TURN_END.on(Summon(CONTROLLER, "BT_721t"))
class BT_721t:
	""" Living Rot """
	pass
class BT_714:#OK
	"""Frozen Shadoweaver	Minion	Common
	<b>Battlecry:</b> <b>Freeze</b> an_enemy."""
	requirements = {PlayReq.REQ_ENEMY_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	#play = SetTag(TARGET,(GameTag.FROZEN, ))
	play = Freeze(TARGET)
class DestroyBuff(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	def do(self, source, target, buff):
		for card in source.buffs:
			if card.id==buff:
				source.buffs.remove(card)
				card.zone=Zone.GRAVEYARD
		pass
class BT_730:###とりあえず
	"""Overconfident Orc	Minion	Common
	<b>Taunt</b>
	While at full Health,
	this has +2 Attack."""
	play = Buff(SELF,'BT_715e')
	events = Damage(SELF).on(DestroyBuff(SELF,'BT_715e'))
class BT_126:#OK
	"""Teron Gorefiend	Minion	Legendary
	[x]<b>Battlecry:</b> Destroy all
	other friendly minions.
	<b>Deathrattle:</b> Resummon
	them with +1/+1."""
	play = BT126TeronGorefiend(SELF)
	deathrattle = BT126TeronGorefiendDeathrattle(SELF)
	#deathrattle = Buff(Summon(CONTROLLER, Copy(Destroy.TARGET)),"BT_126e2")
BT_126e = buff(0,0)
#"""Shadowy Construct"""
BT_126e2 = buff(1,1)
class BT_159:#OK
	"""Terrorguard Escapee	Minion	Common
	<b>Battlecry:</b> Summon three 1/1 Huntresses for your_opponent."""
	play = Summon(OPPONENT, "BT_159t") * 3
class BT_159t:
	""" Huntress """
	pass
class BT_717:#OK
	"""Burrowing Scorpid	Minion	Common
	[x]<b>Battlecry:</b> Deal 2 damage.
	If that kills the target,
	gain <b>Stealth</b>."""
	requirements = {PlayReq.REQ_ENEMY_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 2).then( Death(TARGET).on(SetTag(SELF,(GameTag.STEALTH,))))
class BT_728:#OK
	"""Disguised Wanderer	Minion	Common
	><b>Deathrattle:</b> Summon a 9/1 Inquisitor."""
	deathrattle = Summon(CONTROLLER, "BT_728t")
class BT_728t:
	""" Rustsworn Inquisitor """
	pass
class BT_010:#OK
	"""Felfin Navigator	Minion	Common
	<b>Battlecry:</b> Give your other Murlocs +1/+1."""
	play = Buff(FRIENDLY_MINIONS + MURLOC - SELF, "BT_010e")
BT_010e = buff(1,1)
class BT_850:#OK
	"""Magtheridon	Minion	Legendary
	[x]<b>Dormant</b>. <b>Battlecry:</b> Summon
	three 1/3 enemy Warders.
	When they die, destroy all
	minions and awaken."""
	dormant = -1 #infinite dormant
	play = Summon(OPPONENT, "BT_850t") * 3
	events = Death(ENEMY+ID("BT_850t")).on(SidequestCounter(SELF,3,[Destroy(ALL_MINIONS - SELF), SetAttr(SELF, 'dormant',0), Awaken(SELF) ]))
class BT_850e:
	pass
class BT_850t:
	""" Hellfire Warder """
	pass
class BT_737:#OK
	"""Maiev Shadowsong	Minion	Legendary
	<b>Battlecry:</b> Choose a minion.
	It goes <b>Dormant</b> for 2 turns."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0, PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_ENEMY_TARGET:0}
	play = Dormant(TARGET, 2)
BT_737e = buff(dormant=2)#un-used
class BT_190:#OK
	"""Replicat-o-tron	Minion	Epic
	At the end of your turn, transform a neighbor into a copy of this."""
	play = OWN_TURN_END.on(Morph(SELF_ADJACENT,Copy(SELF)))
class BT_160:#OK
	"""Rustsworn Cultist	Minion	Common
	[x]<b>Battlecry:</b> Give your
	other minions &quot;<b>Deathrattle:</b>
	Summon a 1/1 Demon.&quot;"""
	play = Buff( FRIENDLY_MINIONS - SELF, "BT_160e")
class BT_160e:
   deathrattle = Summon(CONTROLLER, "BT_160t")
   tags = {GameTag.DEATHRATTLE: True}
class BT_160t:

	"""Rusted Devil"""
class BT_735:#OK
	"""Al'ar	Minion	Legendary
	<b>Deathrattle</b>: Summon a
	0/3 Ashes of Al'ar that resurrects this minion on your next turn."""
	deathrattle = Summon(CONTROLLER, "BT_735t")
class BT_735t:
	"""Ashes of Al'ar
	At the start of your turn, transform this into Al'ar."""
	events = OWN_TURN_BEGIN.on(Morph(SELF, "BT_735"))
	pass
class BT_720:#OK
	"""Ruststeed Raider	Minion	Common
	<b>Taunt</b>, <b>Rush</b>
	<b>Battlecry:</b> Gain +4 Attack this turn."""
	play = Buff(SELF, "BT_720e")
BT_720e = buff(4,0)#with one_turn_effect
class BT_729:#OK
	"""Waste Warden	Minion	Epic
	[x]<b>Battlecry:</b> Deal 3 damage to
	a minion and all others of
	the same minion type."""
	requirements = {
		PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0, PlayReq.REQ_TARGET_TO_PLAY:0,
		}
	def play(self):
		for card in self.controller.opponent.field:
			if card.race == self.target.race:
				Hit(card, 3).trigger(self)
		pass
class BT_726:#OK
	"""Dragonmaw Sky Stalker	Minion	Common
	<b>Deathrattle:</b> Summon a 3/4 Dragonrider."""
	deathrattle = Summon(CONTROLLER, "BT_726t")
class BT_726t:
	pass
class BT_732:#OK
	"""Scavenging Shivarra	Minion	Common
	<b>Battlecry:</b> Deal 6 damage randomly split among all_other minions."""
	play = Hit(RANDOM(ALL_MINIONS - SELF), 1) * 6
class BT_716:#OK
	"""Bonechewer Vanguard	Minion	Common
	[x]<b>Taunt</b>
	Whenever this minion takes
	damage, gain +2 Attack."""
	events = Attack(IN_PLAY,SELF).after(Buff(SELF, "BT_716e"))
BT_716e = buff(2,0)
class BT_255:## strictly saying, it is not correct#################################
	"""Kael'thas Sunstrider	Minion	Legendary
	Every third spell you cast each turn costs (1)."""
	events = [
		OWN_TURN_BEGIN.on(SidequestCounterClear(SELF)),
		OWN_SPELL_PLAY.on(SidequestCounter(SELF, 2, [Buff(FRIENDLY_HAND + SPELL, "BT_255e")])),
		]
class BT_255e:
   cost = SET(1)
class BT_734:#OK
	"""Supreme Abyssal	Minion	Common
	Can't attack heroes."""
	tags = {GameTag.CANNOT_ATTACK_HEROES: True}
class BT_155:#OK
	"""Scrapyard Colossus	Minion	Rare
	[x]<b>Taunt</b>
	<b>Deathrattle:</b> Summon a 
	7/7 Felcracked Colossus
	with <b>Taunt</b>."""
	deathrattle = Summon(CONTROLLER, "BT_155t")
class BT_155t:
	""" Felcracked Colossus """
	pass
