from ..utils import *

class CORE_AT_003:# <4>[1637]
	""" Fallen Hero
	Your Hero Power deals 1_extra damage. """
	# HEROPOWER_DAMAGE=1
	pass

class CORE_AT_008:# <4>[1637]
	""" Coldarra Drake
	You can use your Hero Power any number of times. """
	update = Refresh(FRIENDLY_HERO_POWER, {GameTag.HEROPOWER_ADDITIONAL_ACTIVATIONS: SET(-1)})
	pass

class CORE_BOT_453:# <4>[1637]
	""" Shooting Star
	Deal $1 damage to a minion and the minions next to it. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET,1),Hit(TARGET_ADJACENT,1)
	pass

class CORE_CS2_023:# <4>[1637]
	""" Arcane Intellect
	Draw 2 cards. """
	play = Draw(CONTROLLER) * 2
	pass

class CORE_CS2_029:# <4>[1637]
	""" Fireball
	Deal $6 damage. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0, PlayReq.REQ_ENEMY_TARGET: 0, PlayReq.REQ_HERO_OR_MINION_TARGET: 0}
	play = Hit(TARGET, 6)
	pass

class CORE_CS2_032:# <4>[1637]
	""" Flamestrike
	Deal $5 damage to all enemy minions. """
	play = Hit(ENEMY_MINIONS, 5)
	pass

class CORE_CS2_033:# <4>[1637]
	""" Water Elemental
	[Freeze] any character damaged by this minion. """
	events = Damage(CHARACTER, None, SELF).on(Freeze(Damage.TARGET))
	pass

class CORE_EX1_275:# <4>[1637]
	""" Cone of Cold
	[Freeze] a minion and the minions next to it, and deal $1 damage to them. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET | TARGET_ADJACENT, 1), Freeze(TARGET | TARGET_ADJACENT)
	pass

class CORE_EX1_287:# <4>[1637]
	""" Counterspell
	[Secret:] When your opponent casts a spell, [Counter] it. """
	secret = Play(OPPONENT, SPELL).on(Reveal(SELF), Counter(Play.CARD))
	pass

class CORE_EX1_289:# <4>[1637]
	""" Ice Barrier
	[Secret:] When yourhero is attacked,gain 8 Armor. """
	secret = Attack(CHARACTER, FRIENDLY_HERO).on( Reveal(SELF), GainArmor(FRIENDLY_HERO, 8) )
	pass

class CORE_EX1_294:# <4>[1637]
	""" Mirror Entity
	[Secret:] After your opponent plays a minion, summon a copy of it. """
	secret = [
		Play(OPPONENT, MINION).after(Reveal(SELF), Summon(CONTROLLER, ExactCopy(Play.CARD))	),
		#Play(OPPONENT, ID("EX1_323h")).after(Reveal(SELF), Summon(CONTROLLER, "EX1_323"))  # :-)
		]
	pass


class CORE_GIL_801:# <4>[1637]##OK
	""" Snap Freeze
	[Freeze] a minion.If it's already [Frozen], destroy it. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = FreezeOrDeath(TARGET);
	pass

class CORE_KAR_009:# <4>[1637]
	""" Babbling Book
	[Battlecry:] Add a random Mage spell to your hand. """
	play = Give(CONTROLLER, RandomSpell())
	pass

class CORE_LOE_003:# <4>[1637]
	""" Ethereal Conjurer
	[Battlecry: Discover] a spell. """
	play = DISCOVER(RandomSpell())
	pass

class CORE_UNG_020:# <4>[1637]##OK
	""" Arcanologist
	[Battlecry:] Draw a [Secret]. """
	play = Give(CONTROLLER,RANDOM(FRIENDLY_DECK + SECRET))
	pass

class CS3_001:# <4>[1637] ##OK
	""" Aegwynn, the Guardian
	[Spell Damage +2][Deathrattle:] The next minion_you draw inherits these powers. """
	play = SetGLflag(CONTROLLER)
	#deathrattle = SetGLflag(CONTROLLER)
	pass

class CS3_001e:# <4>[1637]
	""" Guardian's Legacy
	[Spell Damage +2] and "[Deathrattle:] Pass on the Guardian's Legacy." """
	# added codes in Death()
	#play = SetTag(OWNER, (GameTag.SPELLPOWER,)) 
	#deathrattle = SetGLflag(CONTROLLER)
	pass

class CS3_001e2:# <4>[1637]
	""" Guardian's Legacy (player)
	The next minion you draw inherits the Guardian's Legacy. """
	#
	pass

class NEW1_012: #<4>[3]
	"""Mana Wyrm"""
	events = OWN_SPELL_PLAY.on(Buff(SELF, "NEW1_012o"))
	pass
NEW1_012o = buff(atk=1)
