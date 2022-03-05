from ..utils import *


class CORE_BOT_420:###OK <2>[1637]
	""" Landscaping
	Summon two 2/2 Treants. """
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	play = Summon(CONTROLLER,'EX1_158t') * 2
	pass

class CORE_CS2_009:###OK <2>[1637]
	""" Mark of the Wild
	Give a minion [Taunt] and +2/+3.<i>(+2 Attack/+3 Health)</i> """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "CS2_009e")
	pass
CS2_009e=buff(atk=2,health=3,taunt=True)

class CORE_CS2_013:# <2>[1637] ##OK
	""" Wild Growth
	Gain an empty Mana Crystal. """
	play = GainEmptyMana(CONTROLLER, 1)
	pass
class CS2_013t:
	play = Draw(CONTROLLER)

class CORE_EX1_158:###OK <2>[1637]
	""" Soul of the Forest
	Give your minions "[Deathrattle:] Summon a 2/2 Treant." """
	play = Buff(FRIENDLY_MINIONS, "EX1_158e")
	pass
class EX1_158e:
	deathrattle = Summon(CONTROLLER, "EX1_158t")
	tags = {GameTag.DEATHRATTLE: True}
	pass
class EX1_158t:
	pass

class CORE_EX1_160:#OK <2>[1637]
	""" Power of the Wild
	[Choose One -] Give your minions +1/+1; or Summon a 3/2 Panther. """
	choose = ("EX1_160a", "EX1_160b")
	play = ChooseBoth(SELF) & (
		Buff(FRIENDLY_MINIONS, "EX1_160be"), Summon(CONTROLLER, "EX1_160t")
	)
class EX1_160a:
	play = Summon(CONTROLLER, "EX1_160t")
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
class EX1_160b:
	play = Buff(FRIENDLY_MINIONS, "EX1_160be")
EX1_160be = buff(+1, +1)
class EX1_160t:
	""" Panther
	""" 
	pass

class CORE_EX1_164:# OK <2>[1637]
	""" Nourish
	[Choose One -] Gain 2_Mana Crystals; or Draw 3 cards. """
	choose = ("EX1_164a", "EX1_164b")
	play = ChooseBoth(SELF) & (GainMana(CONTROLLER, 2), Draw(CONTROLLER) * 3)
class EX1_164a:
	play = GainMana(CONTROLLER, 2)
class EX1_164b:
	play = Draw(CONTROLLER) * 3

class CORE_EX1_165:#OK <2>[1637]
	""" Druid of the Claw
	[Choose One -] Transforminto a 5/4 with [Rush];or a 5/6 with [Taunt]. """
	choose = ("EX1_165a", "EX1_165b")
	play = ChooseBoth(SELF) & Morph(SELF, "OG_044a")
class EX1_165a:
	play = Morph(SELF, "EX1_165t1")
class EX1_165b:
	play = Morph(SELF, "EX1_165t2")
class EX1_165t1:
	pass
class EX1_165t2:
	pass
class OG_044a:
	pass

class CORE_EX1_169:# <2>[1637] # clownDruid
	""" Innervate
	Gain 1 Mana Crystal this turn only. """
	play = ManaThisTurn(CONTROLLER, 1)
	pass

class CORE_EX1_178:#OK <2>[1637]
	""" Ancient of War
	[Choose One -]+5 Attack; or +5 Health and [Taunt]. """
	choose = ("EX1_178b", "EX1_178a")
	play = ChooseBoth(SELF) & (Buff(SELF, "EX1_178ae"), Buff(SELF, "EX1_178be"))
class EX1_178a:
	""" Rooted
	+5 Health and &lt;b&gt;Taunt&lt;/b&gt;."""
	play = Buff(SELF, "EX1_178ae")
EX1_178ae = buff(health=5, taunt=True)
class EX1_178b:
	play = Buff(SELF, "EX1_178be")
EX1_178be = buff(atk=5)

class CORE_EX1_571:#OK <2>[1637]
	""" Force of Nature
	Summon three 2/2 Treants. """
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	play = Summon(CONTROLLER, "EX1_tk9") * 3
	pass
class EX1_tk9:
	pass

class CORE_EX1_573:#OK <2>[1637]
	""" Cenarius
	[Choose One -] Give your other minions +2/+2; or Summon two 2/2 Treants with [Taunt]. """
	choose = ("EX1_573a", "EX1_573b")
	play = ChooseBoth(SELF) & (
		Buff(FRIENDLY_MINIONS - SELF, "EX1_573ae"),
		Summon(CONTROLLER, "EX1_573t") * 2
	)
class EX1_573a:
	play = Buff(FRIENDLY_MINIONS - SELF, "EX1_573ae")
EX1_573ae = buff(+2, +2)
class EX1_573b:
	play = Summon(CONTROLLER, "EX1_573t") * 2
class EX1_573t:
	pass

class CORE_KAR_065:#OK <2>[1637]
	""" Menagerie Warden
	[Battlecry:] Choose a friendly Beast. Summon a_copy of it. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0,
		PlayReq.REQ_TARGET_WITH_RACE: 20}
	powered_up = Find(FRIENDLY_MINIONS + BEAST)
	play = Summon(CONTROLLER, ExactCopy(TARGET))
	pass

class CORE_KAR_300:# <2>[1637]
	""" Enchanted Raven
	 """
	#
	pass

class CORE_OG_047:#OK <2>[1637]
	""" Feral Rage
	[Choose One -] Give your hero +4 Attack this turn; or Gain 8 Armor. """
	choose = ("OG_047a", "OG_047b")
	play = ChooseBoth(SELF) & (
		Buff(FRIENDLY_HERO, "OG_047e"),
		GainArmor(FRIENDLY_HERO, 8)
	)
class OG_047a:
	play = Buff(FRIENDLY_HERO, "OG_047e")
OG_047e = buff(atk=4)
class OG_047b:
	play = GainArmor(FRIENDLY_HERO, 8)

class CORE_TRL_243:#OK <2>[1637]
	""" Pounce
	Give your hero +2_Attack this turn. """
	play=Buff(FRIENDLY_HERO,'TRL_243e')
	pass
TRL_243e=buff(atk=2)# ONE_TURN_EFFECT

class CS3_012:#OK <2>[1637]
	""" Nordrassil Druid
	[Battlecry:] The next spell you cast this turn costs_(3)_less. """
	play = Buff(FRIENDLY_HAND + SPELL,'CS3_012e')
	pass

class CS3_012e:# <2>[1637]
	""" Nature's Rite
	Your next spell this turn costs (3) less. """
	cost = lambda self, i: max(i-3,0)
	events =[
	   OWN_SPELL_PLAY.on(Destroy(SELF)),
	   OWN_TURN_END.on(Destroy(SELF)),
	   ]
	pass

