from ..utils import *


Core_Hunter=[]
Quick_Shot=True##23.6
Marked_Shot=True##23.6
Tracking=True##23.6
Arcane_Shot=True##23.6
Savannah_Highmane=True##23.6
King_Krush=True##23.6
Snake_Trap=True##23.6
Explosive_Trap=True##23.6
Freezing_Trap=True##23.6
Deadly_Shot=True##23.6
Houndmaster_Shaw=True##23.6
Dire_Frenzy=True##23.6
Cloaked_Huntress=True##23.6
Candleshot=True##23.6
Animal_Companion=True##23.6
Springpaw=True##23.6
Selective_Breeder=True##23.6


class CORE_AT_061:# 3 1637 ##22.6
	""" Lock and Load
	Each time you cast a spell this turn, add a random Hunter card to your hand. """
	play = Buff(CONTROLLER, "AT_061e")
	pass
class AT_061e:# 3 15 
	events = OWN_SPELL_PLAY.on(
		Give(CONTROLLER, RandomCollectible(card_class=CardClass.HUNTER))
	)


if Quick_Shot:# 
	Core_Hunter+=['CORE_BRM_013']
class CORE_BRM_013:# 3 1637
	""" Quick Shot
	Deal $3 damage.If your hand is empty, draw a card. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	powered_up = Count(FRIENDLY_HAND - SELF) == 0
	play = Hit(TARGET, 3), EMPTY_HAND & Draw(CONTROLLER)
	pass

if Marked_Shot:# 
	Core_Hunter+=['CORE_DAL_371']
class CORE_DAL_371:# <3>[1637]
	""" Marked Shot
	Deal $4 damage to_a_minion. [Discover]_a_spell. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0, PlayReq.REQ_MINION_TARGET:0,}
	play = Hit(TARGET, 4), Discover(CONTROLLER, RandomSpell())
	pass

if Tracking:# 
	Core_Hunter+=['CORE_DS1_184']
class CORE_DS1_184:# 3 1637 #
	""" Tracking
	[Discover] a card from your deck. """
	play = GenericChoiceOnDeck(CONTROLLER, FRIENDLY_DECK[:3])
	pass

if Arcane_Shot:# 
	Core_Hunter+=['CORE_DS1_185']
class CORE_DS1_185:# 3 1637
	""" Arcane Shot
	Deal $2 damage. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 2)
	pass

class CORE_EX1_531:# 3 1637 ## 22.6
	""" Scavenging Hyena
	Whenever a friendly Beast dies, gain +2/+1. """
	events = Death(FRIENDLY + BEAST).on(Buff(SELF, "EX1_531e"))
	pass
EX1_531e = buff(+2, +1)# 3 3


if Savannah_Highmane:# 
	Core_Hunter+=['CORE_EX1_534','EX1_534t']
class CORE_EX1_534:# 3 1637
	""" Savannah Highmane
	[Deathrattle:] Summon two 2/2 Hyenas. """
	deathrattle = Summon(CONTROLLER, "EX1_534t") * 2
	pass
class EX1_534t:# 3 3
	""" 2/2 Hyenas  """
	pass


if King_Krush:# 
	Core_Hunter+=['CORE_EX1_543']
class CORE_EX1_543:# 3 1637
	""" King Krush
	[Charge] """
	#
	pass


if Snake_Trap:# 
	Core_Hunter+=['CORE_EX1_554','EX1_554t']
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


if Explosive_Trap:# 
	Core_Hunter+=['CORE_EX1_610']
class CORE_EX1_610:# 3 1637
	""" Explosive Trap
	[Secret:] When your hero is attacked, deal $2 damage to all enemies. """
	secret = Attack(ENEMY_CHARACTERS, FRIENDLY_HERO).on(
		Reveal(SELF), Hit(ENEMY_CHARACTERS, 2))
	pass

if Freezing_Trap:# 
	Core_Hunter+=['CORE_EX1_611','EX1_611e']
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

if Deadly_Shot:# 
	Core_Hunter+=['CORE_EX1_617']
class CORE_EX1_617:# 3 1637
	""" Deadly Shot
	Destroy a random enemy minion. """
	requirements = {PlayReq.REQ_MINIMUM_ENEMY_MINIONS: 1}
	play = Destroy(RANDOM_ENEMY_MINION)
	pass

class CORE_FP1_011:# 3 1637 ## 22.6
	""" Webspinner
	[Deathrattle:] Add a random Beast card to your hand. """
	deathrattle = Give(CONTROLLER, RandomBeast())
	pass

if Houndmaster_Shaw:# 
	Core_Hunter+=['CORE_GIL_650']
class CORE_GIL_650:# <3>[1637]##########################23.6 new
	""" Houndmaster Shaw
	Your other minions have[Rush]. """
	update = Refresh(FRIENDLY_MINIONS - SELF, {GameTag.RUSH: True})
	pass

if Dire_Frenzy:# 
	Core_Hunter+=['CORE_GIL_828','GIL_828e']
class CORE_GIL_828:# <3>[1637]
	""" Dire Frenzy
	Give a Beast +3/+3. Shuffle 3 copies into your deck with +3/+3. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0,
		PlayReq.REQ_TARGET_WITH_RACE: 20,}
	play = Buff(TARGET,'GIL_828e'),Shuffle(CONTROLLER,ExactCopy(TARGET)),Shuffle(CONTROLLER,ExactCopy(TARGET)),Shuffle(CONTROLLER,ExactCopy(TARGET))
	pass
GIL_828e=buff(atk=3,health=3)# 12 1125

class CORE_ICC_419:# 3 1637 ## 22.6
	""" Bearshark
	Can't be targeted by spells or Hero Powers. """
	#
	pass

if Cloaked_Huntress:# 
	Core_Hunter+=['CORE_KAR_006']
class CORE_KAR_006:# <3>[1637] ##########23.6 new
	""" Cloaked Huntress
	Your [Secrets] cost (0). """
	update = Refresh(FRIENDLY_HAND + SECRET, {GameTag.COST: SET(0)})
	pass

if Candleshot:# 
	Core_Hunter+=['CORE_LOOT_222']
class CORE_LOOT_222:# <3>[1637] ######## 23.6 new
	""" Candleshot
	Your hero is [Immune] while attacking. """
	update = Refresh(FRIENDLY_HERO, {GameTag.IMMUNE_WHILE_ATTACKING:True})
	pass

if Animal_Companion:# 
	Core_Hunter+=['CORE_NEW1_031','NEW1_032','NEW1_033','NEW1_033o','NEW1_034']
class CORE_NEW1_031:# <3>[1637] ######## 23.6 new
	""" Animal Companion
	Summon a random Beast Companion. """
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

class CORE_TRL_111:# 3 1637 ## 22.6
	""" Headhunter's Hatchet
	[Battlecry:] If you control a Beast, gain+1 Durability. """
	powered_up = Find(FRIENDLY_MINIONS + BEAST)
	play = powered_up & (Buff(SELF, 'TRL_111e1'))
	pass
TRL_111e1=buff(health=1)# 12 1129

if Springpaw:# 
	Core_Hunter+=['CORE_TRL_348','TRL_348t']
class CORE_TRL_348:# <3>[1637] #### 22.6
	""" Springpaw
	[Rush][Battlecry:] Add a 1/1 Lynx with [Rush] to your hand. """
	play = Give(CONTROLLER, 'TRL_348t')
	pass
class TRL_348t:
	pass

if Selective_Breeder:# 
	Core_Hunter+=['CS3_015']
class CS3_015:# <3>[1637]
	""" Selective Breeder
	[Battlecry:] [Discover] a copy of a Beast in your deck. """
	play = GenericChoice(CONTROLLER, RANDOM(FRIENDLY_DECK+BEAST)*3)
	pass

###############################

