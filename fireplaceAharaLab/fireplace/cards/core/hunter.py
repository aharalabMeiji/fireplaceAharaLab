from ..utils import *

class CORE_AT_061:# 3 1637
	""" Lock and Load
	Each time you cast a spell this turn, add a random Hunter card to your hand. """
	play = Buff(CONTROLLER, "AT_061e")
	pass

class AT_061e:# 3 15 
	events = OWN_SPELL_PLAY.on(
		Give(CONTROLLER, RandomCollectible(card_class=CardClass.HUNTER))
	)

class CORE_BRM_013:# 3 1637
	""" Quick Shot
	Deal $3 damage.If your hand is empty, draw a card. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	powered_up = Count(FRIENDLY_HAND - SELF) == 0
	play = Hit(TARGET, 3), EMPTY_HAND & Draw(CONTROLLER)
	pass

class CORE_DS1_184:# 3 1637 ###############################
	""" Tracking
	[Discover] a card from your deck. """
	play = GenericChoiceOnDeck(CONTROLLER, FRIENDLY_DECK[:3])
	pass

class CORE_DS1_185:# 3 1637
	""" Arcane Shot
	Deal $2 damage. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 2)
	pass

class CORE_EX1_531:# 3 1637
	""" Scavenging Hyena
	Whenever a friendly Beast dies, gain +2/+1. """
	events = Death(FRIENDLY + BEAST).on(Buff(SELF, "EX1_531e"))
	pass
EX1_531e = buff(+2, +1)# 3 3

class CORE_EX1_534:# 3 1637
	""" Savannah Highmane
	[Deathrattle:] Summon two 2/2 Hyenas. """
	deathrattle = Summon(CONTROLLER, "EX1_534t") * 2
	pass
class EX1_534t:# 3 3
	""" 2/2 Hyenas  """
	pass

class CORE_EX1_543:# 3 1637
	""" King Krush
	[Charge] """
	#
	pass

class CORE_EX1_554:# 3 1637
	""" Snake Trap
	[Secret:] When one of your minions is attacked, summon three 1/1 Snakes. """
	secret = Attack(ALL_MINIONS, FRIENDLY_MINIONS).on(FULL_BOARD | (
		Reveal(SELF), Summon(CONTROLLER, "EX1_554t") * 3
	))
	pass

class EX1_554t:# 3 3
	""" 1/1 snake  """
	pass

class CORE_EX1_610:# 3 1637
	""" Explosive Trap
	[Secret:] When your hero is attacked, deal $2 damage to all enemies. """
	secret = Attack(ENEMY_CHARACTERS, FRIENDLY_HERO).on(
		Reveal(SELF), Hit(ENEMY_CHARACTERS, 2))
	pass

class CORE_EX1_611:# 3 1637
	""" Freezing Trap
	[Secret:] When an enemy minion attacks, return it to its owner's hand. It costs (2) more. """
	secret = Attack(ENEMY_MINIONS).on(
		Reveal(SELF),
		Bounce(Attack.ATTACKER),
		Buff(Attack.ATTACKER, "EX1_611e")
	)
	pass
class EX1_611e:# 3 3
	events = REMOVED_IN_PLAY
	tags = {GameTag.COST: +2}

class CORE_EX1_617:# 3 1637
	""" Deadly Shot
	Destroy a random enemy minion. """
	requirements = {PlayReq.REQ_MINIMUM_ENEMY_MINIONS: 1}
	play = Destroy(RANDOM_ENEMY_MINION)
	pass

class CORE_FP1_011:# 3 1637
	""" Webspinner
	[Deathrattle:] Add a random Beast card to your hand. """
	deathrattle = Give(CONTROLLER, RandomBeast())
	pass

class CORE_GIL_828:# 3 1637
	""" Dire Frenzy
	Give a Beast +3/+3. Shuffle 3 copies into your deck with +3/+3. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0,
		PlayReq.REQ_TARGET_WITH_RACE: 20}
	play = Buff(TARGET,'GIL_828e'),ShuffleBuff(CONTROLLER,Copy(TARGET),'GIL_828e')
	pass
GIL_828e=buff(atk=3,health=3)# 12 1125

class CORE_ICC_419:# 3 1637
	""" Bearshark
	Can't be targeted by spells or Hero Powers. """
	#
	pass

class CORE_TRL_111:# 3 1637
	""" Headhunter's Hatchet
	[Battlecry:] If youcontrol a Beast, gain+1 Durability. """
	#
	pass
TRL_111e1=buff(health=1)# 12 1129

class CS3_015:# 3 1637 ############################
	""" Selective Breeder
	[Battlecry:] [Discover] a copy of a Beast in your deck. """
	play = GenericChoice(CONTROLLER, RANDOM(FRIENDLY_DECK+BEAST)*3)
	pass

class NEW1_031:
	"""Animal Companion"""
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	entourage = ["NEW1_032", "NEW1_033", "NEW1_034"]
	play = Summon(CONTROLLER, RandomEntourage())
	pass

class NEW1_032:
	""" Misha
	"""
	pass
	
class NEW1_033:
	"""Leokk"""
	update = Refresh(FRIENDLY_MINIONS - SELF, buff="NEW1_033o")
	pass
NEW1_033o = buff(atk=1)

class NEW1_034:
	""" Huffer
	"""
	pass
	

