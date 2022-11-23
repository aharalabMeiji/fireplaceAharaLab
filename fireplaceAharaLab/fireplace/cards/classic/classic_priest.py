from ..utils import *

Classic_Priest=[]

Classic_Holy_Nova=True
Classic_Mind_Control=True
Classic_Inner_Fire=True
Classic_Holy_Smite=True
Classic_Mind_Vision=True
Classic_Power_Word_Shield=True
Classic_Shadow_Word_Pain=True
Classic_Northshire_Cleric=True
Classic_Divine_Spirit=True
Classic_Mind_Blast=True
Classic_Cabal_Shadow_Priest=True
Classic_Silence=True
Classic_Shadow_Madness=True
Classic_Lightspawn=True
Classic_Thoughtsteal=True
Classic_Lightwell=True
Classic_Mindgames=True
Classic_Prophet_Velen=True
Classic_Auchenai_Soulpriest=True
Classic_Circle_of_Healing=True
Classic_Shadow_Word_Death=True
Classic_Temple_Enforcer=True
Classic_Holy_Fire=True
Classic_Shadowform=True
Classic_Mass_Dispel=True
Classic_Mind_Controlling=True
Classic_Lesser_Heal=False # heropower
Classic_Lesser_Fortitude=False # heropower


if Classic_Holy_Nova:# 
	Classic_Priest+=['VAN_CS1_112']
class VAN_CS1_112:# <6>[1646]
	""" Holy Nova
	Deal $2 damage to all enemies. Restore #2 Health to all friendly characters. """
	play = Hit(ENEMY_MINIONS, 2), Heal(FRIENDLY_CHARACTERS, 2)
	pass

if Classic_Mind_Control:# 
	Classic_Priest+=['VAN_CS1_113']
class VAN_CS1_113:# <6>[1646]
	""" Mind Control
	Take control of an enemy minion. """
	requirements = {
		PlayReq.REQ_ENEMY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_NUM_MINION_SLOTS: 1,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Steal(TARGET)
	pass

if Classic_Inner_Fire:# 
	Classic_Priest+=['VAN_CS1_129','CS1_129e']
class VAN_CS1_129:# <6>[1646]
	""" Inner Fire
	Change a minion's Attack to be equal to its Health. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "CS1_129e")
	pass
class CS1_129e:
	atk = lambda self, i: self._xatk
	def apply(self, target):
		self._xatk = target.health

if Classic_Holy_Smite:# 
	Classic_Priest+=['VAN_CS1_130']
class VAN_CS1_130:# <6>[1646]
	""" Holy Smite
	Deal $2 damage. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 2)
	pass

if Classic_Mind_Vision:# 
	Classic_Priest+=['VAN_CS2_003']
class VAN_CS2_003:# <6>[1646]
	""" Mind Vision
	Put a copy of a random card in your opponent's hand into your hand. """
	play = Give(CONTROLLER, Copy(RANDOM(ENEMY_HAND)))
	pass

if Classic_Power_Word_Shield:# 
	Classic_Priest+=['VAN_CS2_004','CS2_004e']
class VAN_CS2_004:# <6>[1646]
	""" Power Word: Shield
	Give a minion +2_Health.Draw a card. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "CS2_004e"), Draw(CONTROLLER)
	pass
CS2_004e = buff(health=2)

if Classic_Shadow_Word_Pain:# 
	Classic_Priest+=['VAN_CS2_234']
class VAN_CS2_234:# <6>[1646]
	""" Shadow Word: Pain
	Destroy a minion with 3_or less Attack. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_MAX_ATTACK: 3,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Destroy(TARGET)
	pass

if Classic_Northshire_Cleric:# 
	Classic_Priest+=['VAN_CS2_235']
class VAN_CS2_235:# <6>[1646]
	""" Northshire Cleric
	Whenever a minion is healed, draw a card. """
	events = Heal(ALL_MINIONS).on(Draw(CONTROLLER))
	pass

if Classic_Divine_Spirit:# 
	Classic_Priest+=['VAN_CS2_236','CS2_236e']
class VAN_CS2_236:# <6>[1646]
	""" Divine Spirit
	Double a minion's Health. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "CS2_236e", max_health=CURRENT_HEALTH(TARGET))
	pass
class CS2_236e:
	pass

if Classic_Mind_Blast:# 
	Classic_Priest+=['VAN_DS1_233']
class VAN_DS1_233:# <6>[1646]
	""" Mind Blast
	Deal $5 damage to the enemy hero. """
	play = Hit(ENEMY_HERO, 5)
	pass

if Classic_Cabal_Shadow_Priest:# 
	Classic_Priest+=['VAN_EX1_091']
class VAN_EX1_091:# <6>[1646]
	""" Cabal Shadow Priest
	[Battlecry:] Take control of an enemy minion that has 2 or less Attack. """
	requirements = {
		PlayReq.REQ_ENEMY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0,
		PlayReq.REQ_TARGET_MAX_ATTACK: 2}
	play = Steal(TARGET)
	pass

if Classic_Silence:# 
	Classic_Priest+=['VAN_EX1_332']
class VAN_EX1_332:# <6>[1646]
	""" Silence
	[Silence] a minion. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Silence(TARGET)
	pass

if Classic_Shadow_Madness:# 
	Classic_Priest+=['VAN_EX1_334','EX1_334e']
class VAN_EX1_334:# <6>[1646]
	""" Shadow Madness
	Gain control of an enemy minion with 3 or less Attack until end of turn. """
	requirements = {
		PlayReq.REQ_ENEMY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_NUM_MINION_SLOTS: 1,
		PlayReq.REQ_TARGET_MAX_ATTACK: 3,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Steal(TARGET), Buff(TARGET, "EX1_334e")
	pass
class EX1_334e:
	events = [
		TURN_END.on(Destroy(SELF), Steal(OWNER, OPPONENT)),
		Silence(OWNER).on(Steal(OWNER, OPPONENT))
	]
	tags = {GameTag.CHARGE: True}


if Classic_Lightspawn:# 
	Classic_Priest+=['VAN_EX1_335']
class VAN_EX1_335:# <6>[1646]
	""" Lightspawn
	This minion's Attack is always equal to its Health. """
	update = Refresh(SELF, {GameTag.ATK: lambda self, i: self.health}, priority=100)
	pass

if Classic_Thoughtsteal:# 
	Classic_Priest+=['VAN_EX1_339']
class VAN_EX1_339:# <6>[1646]
	""" Thoughtsteal
	Copy 2 cards in your opponent's deck and add them to your hand. """
	play = Give(CONTROLLER, Copy(RANDOM(ENEMY_DECK) * 2))
	pass

if Classic_Lightwell:# 
	Classic_Priest+=['VAN_EX1_341']
class VAN_EX1_341:# <6>[1646]
	""" Lightwell
	At the start of your turn, restore #3 Health to a damaged friendly character. """
	events = OWN_TURN_BEGIN.on(Heal(RANDOM(FRIENDLY + DAMAGED_CHARACTERS), 3))
	pass

if Classic_Mindgames:# 
	Classic_Priest+=['VAN_EX1_345']
	Classic_Priest+=['VAN_EX1_345t']
class VAN_EX1_345:# <6>[1646]
	""" Mindgames
	Put a copy ofa random minion fromyour opponent's deck into the battlefield. """
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	play = (
		Find(ENEMY_DECK + MINION) &
		Summon(CONTROLLER, Copy(RANDOM(ENEMY_DECK + MINION))) |
		Summon(CONTROLLER, "EX1_345t")
	)
	pass
class VAN_EX1_345t:# <6>[1646]
	""" Shadow of Nothing
	Mindgames whiffed! Your opponent had no minions! """
	#
	pass

if Classic_Prophet_Velen:# 
	Classic_Priest+=['VAN_EX1_350']
class VAN_EX1_350:# <6>[1646]
	""" Prophet Velen
	Double the damage and healing of your spells and Hero Power. """
	update = Refresh(CONTROLLER, {
		GameTag.HEALING_DOUBLE: 1,
		GameTag.SPELLPOWER_DOUBLE: 1,
		GameTag.HERO_POWER_DOUBLE: 1,
	})
	pass

if Classic_Auchenai_Soulpriest:# 
	Classic_Priest+=['VAN_EX1_591']
class VAN_EX1_591:# <6>[1646]
	""" Auchenai Soulpriest
	Your cards and powers that restore Health now deal damage instead. """
	update = Refresh(CONTROLLER, {
		GameTag.EMBRACE_THE_SHADOW: True,
	})
	pass

if Classic_Circle_of_Healing:# 
	Classic_Priest+=['VAN_EX1_621']
class VAN_EX1_621:# <6>[1646]
	""" Circle of Healing
	Restore #4 Health to ALL_minions. """
	play = Heal(ALL_MINIONS, 4)
	pass

if Classic_Shadow_Word_Death:# 
	Classic_Priest+=['VAN_EX1_622']
class VAN_EX1_622:# <6>[1646]
	""" Shadow Word: Death
	Destroy a minion with 5_or more Attack. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_MIN_ATTACK: 5,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Destroy(TARGET)
	pass

if Classic_Temple_Enforcer:# 
	Classic_Priest+=['VAN_EX1_623','EX1_623e']
class VAN_EX1_623:# <6>[1646]
	""" Temple Enforcer
	[Battlecry:] Give a friendly minion +3 Health. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Buff(TARGET, "EX1_623e")
	pass
EX1_623e = buff(health=3)

if Classic_Holy_Fire:# 
	Classic_Priest+=['VAN_EX1_624']
class VAN_EX1_624:# <6>[1646]
	""" Holy Fire
	Deal $5 damage. Restore #5 Health to your hero. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 5), Heal(FRIENDLY_HERO, 5)
	pass

if Classic_Shadowform:# 
	Classic_Priest+=['VAN_EX1_625','EX1_625t','EX1_625t2']
class VAN_EX1_625:# <6>[1646]
	""" Shadowform
	Your Hero Power becomes 'Deal 2 damage.' If already in Shadowform: 3 damage. """
	play = Switch(FRIENDLY_HERO_POWER, {
		"EX1_625t": Summon(CONTROLLER, "EX1_625t2"),
		"EX1_625t2": (),
		None: Summon(CONTROLLER, "EX1_625t"),
	})
	pass
class EX1_625t:
	"""Mind Spike"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	activate = Hit(TARGET, 2)
	update = Refresh(CONTROLLER, {GameTag.SHADOWFORM: True})
class EX1_625t2:
	"""Mind Shatter"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	activate = Hit(TARGET, 3)
	update = Refresh(CONTROLLER, {GameTag.SHADOWFORM: True})


if Classic_Mass_Dispel:# 
	Classic_Priest+=['VAN_EX1_626']
class VAN_EX1_626:# <6>[1646]
	""" Mass Dispel
	[Silence] all enemy minions. Draw a card. """
	play = Silence(ENEMY_MINIONS), Draw(CONTROLLER)
	pass

if Classic_Mind_Controlling:# 
	Classic_Priest+=['VAN_EX1_tk31']
class VAN_EX1_tk31:# <6>[1646]
	""" Mind Controlling
	 """
	#
	pass

if Classic_Lesser_Heal:# 
	Classic_Priest+=['VAN_HERO_09bp']
	Classic_Priest+=['VAN_HERO_09bp2']
class VAN_HERO_09bp:# <6>[1646]
	""" Lesser Heal
	[Hero Power]Restore #2 Health. """
	#
	pass

class VAN_HERO_09bp2:# <6>[1646]
	""" Heal
	[Hero Power]Restore #4 Health. """
	#
	pass

if Classic_Lesser_Fortitude:# 
	Classic_Priest+=['VAN_HERO_09e1']
class VAN_HERO_09e1:# <6>[1646]
	""" Lesser Fortitude
	+1 Health. """
	#
	pass

