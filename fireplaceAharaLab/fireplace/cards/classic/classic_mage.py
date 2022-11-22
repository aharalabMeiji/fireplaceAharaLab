
from ..utils import *

Classic_Mage=[]
Classic_Frostbolt=True
Classic_Pyroblast=True
Classic_Polymorph=True
Classic_Arcane_Intellect=True
Classic_Frostbolt=True
Classic_Arcane_Explosion=True
Classic_Frost_Nova=True
Classic_Mirror_Image=True
Classic_Blizzard=True
Classic_Fireball=True
Classic_Ice_Lance=True
Classic_Flamestrike=True
Classic_Water_Elemental=True
Classic_Mirror_Image=True
Classic_Ethereal_Arcanist=True
Classic_Cone_of_Cold=True
Classic_Arcane_Missiles=True
Classic_Pyroblast=True
Classic_Counterspell=True
Classic_Ice_Barrier=True
Classic_Mirror_Entity=True
Classic_Ice_Block=True
Classic_Archmage_Antonidas=True
Classic_Vaporize=True
Classic_Sorcerers_Apprentice=True
Classic_Kirin_Tor_Mage=True
Classic_Fireblast=True
Classic_Fireblast_Rank_2=True
Classic_Mana_Wyrm=True
Classic_Spellbender=True
Classic_Spellbender=True


if Classic_Polymorph:# 
	Classic_Mage+=['VAN_CS2_022','CS2_tk1']
class VAN_CS2_022:# <4>[1646]
	""" Polymorph
	Transform a minioninto a 1/1 Sheep. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Morph(TARGET, "CS2_tk1")
	pass
class CS2_tk1:
	pass

if Classic_Arcane_Intellect:# 
	Classic_Mage+=['VAN_CS2_023']
class VAN_CS2_023:# <4>[1646]
	""" Arcane Intellect
	Draw 2 cards. """
	play = Draw(CONTROLLER) * 2
	pass

if Classic_Frostbolt:# 
	Classic_Mage+=['VAN_CS2_024']
class VAN_CS2_024:# <4>[1646]
	""" Frostbolt
	Deal $3 damage to a_character and [Freeze] it. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 3), Freeze(TARGET)
	pass

if Classic_Arcane_Explosion:# 
	Classic_Mage+=['VAN_CS2_025']
class VAN_CS2_025:# <4>[1646]
	""" Arcane Explosion
	Deal $1 damage to all enemy minions. """
	play = Hit(ENEMY_MINIONS, 1)
	pass

if Classic_Frost_Nova:# 
	Classic_Mage+=['VAN_CS2_026']
class VAN_CS2_026:# <4>[1646]
	""" Frost Nova
	[Freeze] all enemy minions. """
	play = Freeze(ENEMY_MINIONS)
	pass

if Classic_Mirror_Image:# 
	Classic_Mage+=['VAN_CS2_027']
class VAN_CS2_027:# <4>[1646]
	""" Mirror Image
	Summon two 0/2 minions with [Taunt]. """
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	play = Summon(CONTROLLER, "VAN_CS2_mirror") * 2
	pass

if Classic_Blizzard:# 
	Classic_Mage+=['VAN_CS2_028']
class VAN_CS2_028:# <4>[1646]
	""" Blizzard
	Deal $2 damage to all enemy minions and [Freeze] them. """
	play = Hit(ENEMY_MINIONS, 2), Freeze(ENEMY_MINIONS)
	pass

if Classic_Fireball:# 
	Classic_Mage+=['VAN_CS2_029']
class VAN_CS2_029:# <4>[1646]
	""" Fireball
	Deal $6 damage. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 6)
	pass

if Classic_Ice_Lance:# 
	Classic_Mage+=['VAN_CS2_031']
class VAN_CS2_031:# <4>[1646]
	""" Ice Lance
	[Freeze] a character. If it was already [Frozen], deal $4 damage instead. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Find(TARGET + FROZEN) & Hit(TARGET, 4) | Freeze(TARGET)
	pass

if Classic_Flamestrike:# 
	Classic_Mage+=['VAN_CS2_032']
class VAN_CS2_032:# <4>[1646]
	""" Flamestrike
	Deal $4 damage to all enemy minions. """
	play = Hit(ENEMY_MINIONS, 4)
	pass

if Classic_Water_Elemental:# 
	Classic_Mage+=['VAN_CS2_033']
class VAN_CS2_033:# <4>[1646]
	""" Water Elemental
	[Freeze] any character damaged by this minion. """
	events = Damage(CHARACTER, None, SELF).on(Freeze(Damage.TARGET))
	pass

if Classic_Mirror_Image:# 
	Classic_Mage+=['VAN_CS2_mirror']
class VAN_CS2_mirror:# <4>[1646]
	""" Mirror Image
	[Taunt] """
	#
	pass

if Classic_Ethereal_Arcanist:# 
	Classic_Mage+=['VAN_EX1_274','EX1_274e']
class VAN_EX1_274:# <4>[1646]
	""" Ethereal Arcanist
	If you control a [Secret] at_the end of your turn, gain +2/+2. """
	events = OWN_TURN_END.on(Find(FRIENDLY_SECRETS) & Buff(SELF, "EX1_274e"))
	pass
EX1_274e = buff(+2, +2)

if Classic_Cone_of_Cold:# 
	Classic_Mage+=['VAN_EX1_275']
class VAN_EX1_275:# <4>[1646]
	""" Cone of Cold
	[Freeze] a minion and the minions next to it, and deal $1 damage to them. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET | TARGET_ADJACENT, 1), Freeze(TARGET | TARGET_ADJACENT)
	pass

if Classic_Arcane_Missiles:# 
	Classic_Mage+=['VAN_EX1_277']
class VAN_EX1_277:# <4>[1646]
	""" Arcane Missiles
	Deal $3 damage randomly split among all enemy characters. """
	def play(self):
		count = self.controller.get_spell_damage(3)
		yield Hit(RANDOM_ENEMY_CHARACTER, 1) * count
	pass

if Classic_Pyroblast:# 
	Classic_Mage+=['VAN_EX1_279']
class VAN_EX1_279:# <4>[1646]
	""" Pyroblast
	Deal $10 damage. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 10)
	pass

if Classic_Counterspell:# 
	Classic_Mage+=['VAN_EX1_287']
class VAN_EX1_287:# <4>[1646]
	""" Counterspell
	[Secret:] When your opponent casts a spell, [Counter] it. """
	secret = Play(OPPONENT, SPELL).on(
		Reveal(SELF), Counter(Play.CARD)
	)
	pass

if Classic_Ice_Barrier:# 
	Classic_Mage+=['VAN_EX1_289']
class VAN_EX1_289:# <4>[1646]
	""" Ice Barrier
	[Secret:] As soon as yourhero is attacked, gain8 Armor. """
	secret = Attack(CHARACTER, FRIENDLY_HERO).on(
		Reveal(SELF), GainArmor(FRIENDLY_HERO, 8)
	)
	pass

if Classic_Mirror_Entity:# 
	Classic_Mage+=['VAN_EX1_294']
class VAN_EX1_294:# <4>[1646]
	""" Mirror Entity
	[Secret:] Whenyour opponent plays aminion, summon a copy of it. """
	secret = [
		Play(OPPONENT, MINION).after(
			Reveal(SELF), Summon(CONTROLLER, ExactCopy(Play.CARD))
		),
		#Play(OPPONENT, ID("EX1_323h")).after(
		#	Reveal(SELF), Summon(CONTROLLER, "EX1_323")
		#)  # :-)
	]
	pass

if Classic_Ice_Block:# 
	Classic_Mage+=['VAN_EX1_295','EX1_295o']
class VAN_EX1_295:# <4>[1646]
	""" Ice Block
	[Secret:] When your hero takes fatal damage, prevent it and become [Immune] this turn. """
	secret = Predamage(FRIENDLY_HERO).on(
		Lethal(FRIENDLY_HERO, Predamage.AMOUNT) & (
			Reveal(SELF),
			Buff(FRIENDLY_HERO, "EX1_295o"),
			Predamage(FRIENDLY_HERO, 0)
		)
	)
	pass
EX1_295o = buff(immune=True)

if Classic_Archmage_Antonidas:# 
	Classic_Mage+=['VAN_EX1_559']
class VAN_EX1_559:# <4>[1646]
	""" Archmage Antonidas
	Whenever you cast a spell, add a 'Fireball' spell to_your hand. """
	events = OWN_SPELL_PLAY.on(Give(CONTROLLER, "VAN_CS2_029"))
	pass

if Classic_Vaporize:# 
	Classic_Mage+=['VAN_EX1_594']
class VAN_EX1_594:# <4>[1646]
	""" Vaporize
	[Secret:] When a minion attacks your hero, destroy it. """
	secret = Attack(MINION, FRIENDLY_HERO).on(
		Reveal(SELF), Destroy(Attack.ATTACKER)
	)
	pass

if Classic_Sorcerers_Apprentice:# 
	Classic_Mage+=['VAN_EX1_608']
class VAN_EX1_608:# <4>[1646]
	""" Sorcerer's Apprentice
	Your spells cost (1) less. """
	update = Refresh(FRIENDLY_HAND + SPELL, {GameTag.COST: -1})
	pass

if Classic_Kirin_Tor_Mage:# 
	Classic_Mage+=['VAN_EX1_612','EX1_612o']
class VAN_EX1_612:# <4>[1646]
	""" Kirin Tor Mage
	[Battlecry:] The next [Secret]you play this turn costs (0). """
	play = Buff(CONTROLLER, "EX1_612o")
	pass
class EX1_612o:
	update = Refresh(FRIENDLY_HAND + SECRET, {GameTag.COST: SET(0)})
	events = Play(CONTROLLER, SECRET).on(Destroy(SELF))

if Classic_Mana_Wyrm:# 
	Classic_Mage+=['VAN_NEW1_012','NEW1_012o']
class VAN_NEW1_012:# <4>[1646]
	""" Mana Wyrm
	Whenever you cast a spell, gain +1 Attack. """
	events = OWN_SPELL_PLAY.on(Buff(SELF, "NEW1_012o"))
	pass
NEW1_012o = buff(atk=1)

if Classic_Spellbender:# 
	Classic_Mage+=['VAN_tt_010']
class VAN_tt_010:# <4>[1646]
	""" Spellbender
	[Secret:] When an enemy casts a spell on a minion, summon a 1/3 as the new target. """
	secret = Play(OPPONENT, SPELL, MINION).on(FULL_BOARD | (
		Reveal(SELF), Retarget(Play.CARD, Summon(CONTROLLER, "tt_010a"))
	))
	pass

if Classic_Spellbender:# 
	Classic_Mage+=['VAN_tt_010a']
class VAN_tt_010a:# <4>[1646]
	""" Spellbender
	 """
	#
	pass

