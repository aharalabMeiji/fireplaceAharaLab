from ..utils import *

Classic_Warlock=[]

Classic_Shadow_Bolt=True
Classic_Blood_Imp=True
Classic_Drain_Life=True
Classic_Hellfire=True
Classic_Corruption=True
Classic_Dread_Infernal=True
Classic_Voidwalker=True
Classic_Felguard=True
Classic_Mortal_Coil=True
Classic_Shadowflame=True
Classic_Void_Terror=True
Classic_Felstalker=True
Classic_Soulfire=True
Classic_Siphon_Soul=True
Classic_Doomguard=True
Classic_Twisting_Nether=True
Classic_Pit_Lord=True
Classic_Summoning_Portal=True
Classic_Power_Overwhelming=True
Classic_Sense_Demons=True
Classic_Flame_Imp=True
Classic_Bane_of_Doom=True
Classic_Lord_Jaraxxus=True
Classic_Demonfire=True
Classic_INFERNO=True
Classic_Infernal=True
Classic_Life_Tap=False ## HP
Classic_Sacrificial_Pact=True


if Classic_Shadow_Bolt:# 
	Classic_Warlock+=['VAN_CS2_057']
class VAN_CS2_057:# <9>[1646]
	""" Shadow Bolt
	Deal $4 damageto a minion. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 4)
	pass

if Classic_Blood_Imp:# 
	Classic_Warlock+=['VAN_CS2_059','CS2_059o']
class VAN_CS2_059:# <9>[1646]
	""" Blood Imp
	  [Stealth]. At the end of your  turn, give another random friendly minion +1 Health. """
	events = OWN_TURN_END.on(Buff(RANDOM_OTHER_FRIENDLY_MINION, "CS2_059o"))
	pass
CS2_059o = buff(health=1)


if Classic_Drain_Life:# 
	Classic_Warlock+=['VAN_CS2_061']
class VAN_CS2_061:# <9>[1646]
	""" Drain Life
	Deal $2 damage. Restore #2 Health to your hero. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 2), Heal(FRIENDLY_HERO, 2)
	pass

if Classic_Hellfire:# 
	Classic_Warlock+=['VAN_CS2_062']
class VAN_CS2_062:# <9>[1646]
	""" Hellfire
	Deal $3 damage to ALL_characters. """
	play = Hit(ALL_CHARACTERS, 3)
	pass

if Classic_Corruption:# 
	Classic_Warlock+=['VAN_CS2_063','CS2_063e']
class VAN_CS2_063:# <9>[1646]
	""" Corruption
	Choose an enemy minion. At the start of your turn, destroy it. """
	requirements = {
		PlayReq.REQ_ENEMY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "CS2_063e")
	pass
class CS2_063e:
	events = OWN_TURN_BEGIN.on(Destroy(OWNER))

if Classic_Dread_Infernal:# 
	Classic_Warlock+=['VAN_CS2_064']
class VAN_CS2_064:# <9>[1646]
	""" Dread Infernal
	[Battlecry:] Deal 1 damage to ALL other characters. """
	play = Hit(ALL_CHARACTERS - SELF, 1)
	pass

if Classic_Voidwalker:# 
	Classic_Warlock+=['VAN_CS2_065']
class VAN_CS2_065:# <9>[1646]
	""" Voidwalker
	[Taunt] """
	#
	pass

if Classic_Felguard:# 
	Classic_Warlock+=['VAN_EX1_301']
class VAN_EX1_301:# <9>[1646]
	""" Felguard
	[Taunt][Battlecry:] Destroy one of your Mana Crystals. """
	play = GainEmptyMana(CONTROLLER, -1)
	pass

if Classic_Mortal_Coil:# 
	Classic_Warlock+=['VAN_EX1_302']
class VAN_EX1_302:# <9>[1646]
	""" Mortal Coil
	Deal $1 damage to a minion. If that kills it, draw a card. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 1), Dead(TARGET) & Draw(CONTROLLER)
	pass

if Classic_Shadowflame:# 
	Classic_Warlock+=['VAN_EX1_303']
class VAN_EX1_303:# <9>[1646]
	""" Shadowflame
	Destroy a friendly minion and deal its Attack damage to all enemy minions. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(ENEMY_MINIONS, ATK(TARGET)), Destroy(TARGET)
	pass

if Classic_Void_Terror:# 
	Classic_Warlock+=['VAN_EX1_304', "EX1_304e"]
class VAN_EX1_304:# <9>[1646]
	""" Void Terror
	[Battlecry:] Destroy bothadjacent minions and gain their Attack and Health. """
	play = (
		Buff(SELF, "EX1_304e", atk=ATK(SELF_ADJACENT), max_health=CURRENT_HEALTH(SELF_ADJACENT)),
		Destroy(SELF_ADJACENT)
	)
	pass
class EX1_304e:
	pass

if Classic_Felstalker:# 
	Classic_Warlock+=['VAN_EX1_306']
class VAN_EX1_306:# <9>[1646]
	""" Felstalker
	[Battlecry:] Discard a random card. """
	play = Discard(RANDOM(FRIENDLY_HAND))
	pass

if Classic_Soulfire:# 
	Classic_Warlock+=['VAN_EX1_308']
class VAN_EX1_308:# <9>[1646]
	""" Soulfire
	Deal $4 damage.Discard a random card. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 4), Discard(RANDOM(FRIENDLY_HAND))
	pass

if Classic_Siphon_Soul:# 
	Classic_Warlock+=['VAN_EX1_309']
class VAN_EX1_309:# <9>[1646]
	""" Siphon Soul
	Destroy a minion. Restore #3 Health to_your hero. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Destroy(TARGET), Heal(FRIENDLY_HERO, 3)
	pass

if Classic_Doomguard:# 
	Classic_Warlock+=['VAN_EX1_310']
class VAN_EX1_310:# <9>[1646]
	""" Doomguard
	[Charge]. [Battlecry:] Discard two random cards. """
	play = Discard(RANDOM(FRIENDLY_HAND) * 2)
	pass

if Classic_Twisting_Nether:# 
	Classic_Warlock+=['VAN_EX1_312']
class VAN_EX1_312:# <9>[1646]
	""" Twisting Nether
	Destroy all minions. """
	play = Destroy(ALL_MINIONS)
	pass

if Classic_Pit_Lord:# 
	Classic_Warlock+=['VAN_EX1_313']
class VAN_EX1_313:# <9>[1646]
	""" Pit Lord
	[Battlecry:] Deal 5 damage to your hero. """
	play = Hit(FRIENDLY_HERO, 5)
	pass

if Classic_Summoning_Portal:# 
	Classic_Warlock+=['VAN_EX1_315']
class VAN_EX1_315:# <9>[1646]
	""" Summoning Portal
	Your minions cost (2) less, but not less than (1). """
	update = Refresh(FRIENDLY_HAND + MINION, {
		GameTag.COST: lambda self, i: min(i, max(1, i - 2))
	})
	pass

if Classic_Power_Overwhelming:# 
	Classic_Warlock+=['VAN_EX1_316','EX1_316e']
class VAN_EX1_316:# <9>[1646]
	""" Power Overwhelming
	Give a friendly minion +4/+4 until end of turn. Then, it dies. Horribly. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "EX1_316e")
	pass
class EX1_316e:
	events = TURN_END.on(Destroy(OWNER))
	tags = {
		GameTag.ATK: +4,
		GameTag.HEALTH: +4,
	}

if Classic_Sense_Demons:# 
	Classic_Warlock+=['VAN_EX1_317','EX1_317t']
class VAN_EX1_317:# <9>[1646]
	""" Sense Demons
	Draw 2 Demonsfrom your deck. """
	play = (
		Find(FRIENDLY_DECK + DEMON) &
		ForceDraw(RANDOM(FRIENDLY_DECK + DEMON)) |
		Give(CONTROLLER, "EX1_317t"),
	) * 2
	pass
class EX1_317t:
	pass

if Classic_Flame_Imp:# 
	Classic_Warlock+=['VAN_EX1_319']
class VAN_EX1_319:# <9>[1646]
	""" Flame Imp
	[Battlecry:] Deal 3 damage to your hero. """
	play = Hit(FRIENDLY_HERO, 3)
	pass

if Classic_Bane_of_Doom:# 
	Classic_Warlock+=['VAN_EX1_320']
class VAN_EX1_320:# <9>[1646]
	""" Bane of Doom
	Deal $2 damage to_a character. If that kills it, summon a random Demon. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 2), Dead(TARGET) & Summon(CONTROLLER, RandomMinion(race=Race.DEMON))
	pass

if Classic_Lord_Jaraxxus:# 
	Classic_Warlock+=['VAN_EX1_323']
class VAN_EX1_323:# <9>[1646]
	""" Lord Jaraxxus
	[Battlecry:] Destroy your hero and replace it with Lord Jaraxxus. """
	play = (
		Summon(CONTROLLER, "EX1_323h").then(Morph(SELF, Summon.CARD)),
		Summon(CONTROLLER, "EX1_323w")
	)
	pass

if Classic_Demonfire:# 
	Classic_Warlock+=['VAN_EX1_596','EX1_596e']
class VAN_EX1_596:# <9>[1646]
	""" Demonfire
	Deal $2 damage to a minion. If it's a friendly Demon, give it +2/+2 instead. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Find(TARGET + FRIENDLY + DEMON) & Buff(TARGET, "EX1_596e") | Hit(TARGET, 2)
	pass
EX1_596e = buff(+2, +2)


if Classic_INFERNO:# 
	Classic_Warlock+=['VAN_EX1_tk33']
class VAN_EX1_tk33:# <9>[1646]
	""" INFERNO!
	[Hero Power]Summon a 6/6 Infernal. """
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	activate = Summon(CONTROLLER, "EX1_tk34")
	pass

if Classic_Infernal:# 
	Classic_Warlock+=['VAN_EX1_tk34']
class VAN_EX1_tk34:# <9>[1646]
	""" Infernal
	 """
	#
	pass

if Classic_Life_Tap:# 
	Classic_Warlock+=['VAN_HERO_07bp']
	Classic_Warlock+=['VAN_HERO_07bp2']
class VAN_HERO_07bp:# <9>[1646]
	""" Life Tap
	[Hero Power]Draw a card and take $2_damage. """
	#
	pass
class VAN_HERO_07bp2:# <9>[1646]
	""" Soul Tap
	[Hero Power]Draw a card. """
	#
	pass

if Classic_Sacrificial_Pact:# 
	Classic_Warlock+=['VAN_NEW1_003']
class VAN_NEW1_003:# <9>[1646]
	""" Sacrificial Pact
	Destroy a Demon. Restore #5 Health to your hero. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0,
		PlayReq.REQ_TARGET_WITH_RACE: 15}
	play = Destroy(TARGET), Heal(FRIENDLY_HERO, 5)
	pass

