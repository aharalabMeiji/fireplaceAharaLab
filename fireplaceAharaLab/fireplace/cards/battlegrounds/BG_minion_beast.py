
from ..utils import *

BattleGrounds_Minion_Beast=[
	'CFM_315','TB_BaconUps_093',	'CFM_315t','TB_BaconUps_093t',
	'CORE_EX1_531','TB_BaconUps_043',
	'BG21_000','BG21_000_G',
	'BGS_075','TB_BaconUps_125',
	'BG19_010','BG19_010t','BG19_010_G','BG19_010_Gt',
	'BGS_078','TB_BaconUps_135',
	'CFM_316','TB_BaconUps_027',
	'LOOT_078','TB_BaconUps_151',
	'BG21_003','BG21_003_G',
	'CORE_EX1_534','EX1_534t','TB_BaconUps_049','TB_BaconUps_049t',
	'BG20_205','BG20_205_G',
	'BG22_001','BG22_001t2','BG22_001_G','BG22_001t2_G',
	'BGS_021','TB_BaconUps_090',
	'BG21_001','BG21_001_G',
	'BGS_008','TB_BaconUps_057',
	'BGS_018','TB_BaconUps_085',]
#

class CFM_315:# <3>[25]
	""" Alleycat <beast> (1/1)
	&lt;b&gt;Battlecry:&lt;/b&gt; Summon a 1/1_Cat."""
	play = Summon(CONTROLLER, 'CFM_315t')
	pass
class CFM_315t:# <3>[25]
	""" Tabbycat <beast>
	"""
	pass
class TB_BaconUps_093:#
	""" Alleycat <beast> (2/2)
	&lt;b&gt;Battlecry:&lt;/b&gt; Summon a 2/2_Cat."""
	play = Summon(CONTROLLER, 'TB_BaconUps_093t')
	pass
class TB_BaconUps_093t:#
	""" Tabbycat <beast> (2/2)
	"""

#class CORE_EX1_531: #<3>[1637]
#	"""Scavenging Hyena (1/2/2)
#	Whenever a friendly Beast dies, gain +2/+1."""
#	events = Death(FRIENDLY + BEAST).on(Buff(SELF, "EX1_531e"))
#	pass
#EX1_531=buff(2,1)
class TB_BaconUps_043: #<3>[1637]
	"""Scavenging Hyena (1/2/2)
	Whenever a friendly Beast dies, gain +4/+2."""
	events = Death(FRIENDLY + BEAST).on(Buff(SELF, "TB_BaconUps_043e"))
	pass
TB_BaconUps_043e=buff(4,2)

class BG21_000:# <12>[1453]
	""" Leapfrogger
	[Deathrattle:] Give a friendly Beast +1/+1 and this [Deathrattle]. """
	deathrattle = Buff(RANDOM(FRIENDLY_MINIONS + BEAST), 'BG21_000e')
	pass
class BG21_000e:
	max_health = lambda self, i : i+1
	atk = lambda self, i : i+1
	tags = {GameTag.DEATHRATTLE:True, }
	deathrattle = Buff(RANDOM(FRIENDLY_MINIONS + BEAST), 'BG21_000e')
class BG21_000_G:# <12>[1453]
	""" Leapfrogger
	[Deathrattle:] Give a friendly Beast +2/+2 and this [Deathrattle]. """
	deathrattle = Buff(RANDOM(FRIENDLY_MINIONS + BEAST), 'BG21_000e')
	pass
class BG21_000_Ge:
	max_health = lambda self, i : i+2
	atk = lambda self, i : i+2
	tags = {GameTag.DEATHRATTLE:True, }
	deathrattle = Buff(RANDOM(FRIENDLY_MINIONS + BEAST), 'BG21_000e')

class BGS_075:# <3>[1453]
	""" Rabid Saurolisk (2/3/2)
	After you play a minion with [Deathrattle], gain +1/+2. """
	events = Play(CONTROLLER, FRIENDLY_MINIONS + DEATHRATTLE).after(Buff(SELF, 'BGS_075e'))
	pass
BGS_075e=buff(1,2)
class TB_BaconUps_125:# <3>[1453]
	""" Rabid Saurolisk
	After you play a minion with [Deathrattle], gain +2/+4. """
	events = Play(CONTROLLER, FRIENDLY_MINIONS + DEATHRATTLE).after(Buff(SELF, 'TB_BaconUps_125e'))
	pass
TB_BaconUps_125e=buff(2,4)

class BG19_010:# <12>[1453]
	""" Sewer Rat (2/3/2)
	[Deathrattle:] Summon a 2/3 Turtle with [Taunt]. """
	deathrattle = Summon(CONTROLLER, 'BG19_010t')
	pass
class BG19_010t:# <12>[1453]
	""" Half-Shell
	[Taunt] """
	pass
class BG19_010_G:# <12>[1453]
	""" Sewer Rat
	[Deathrattle:] Summon a 4/6 Turtle with [Taunt]. """
	deathrattle = Summon(CONTROLLER, 'BG19_010_Gt')
	pass
class BG19_010_Gt:# <12>[1453]
	""" Half-Shell
	[Taunt] """
	pass

class BGS_078_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		deathrattles = []
		for card in target.controller.field:
			deathrattles.append(card.deathrattles)
		if len(deathrattles)>0:
			random.choice(deathrattles).trigger(source)
		pass
class BGS_078:# <12>[1453]
	""" Monstrous Macaw (3/5/3)
	After this attacks, trigger another friendly minion's [Deathrattle]. """
	events = Attack(FRIENDLY_MINIONS, ENEMY_MINIONS).after(BGS_078_Action(SELF))
	pass
class TB_BaconUps_135:
	""" Monstrous Macaw (3/10/6)
	[x]After this attacks, trigger another friendly minion's &lt;b&gt;Deathrattle&lt;/b&gt; twice. """
	events = Attack(FRIENDLY_MINIONS, ENEMY_MINIONS).after(BGS_078_Action(SELF), BGS_078_Action(SELF))
	pass

class CFM_316:
	""" Rat Pack (3/2/2)
	&lt;b&gt;Deathrattle:&lt;/b&gt; Summon a number of 1/1 Rats equal _to this minion's Attack."""
	deathrattle = Summon(CONTROLLER, 'CFM_316t') * ATK(SELF)#
	pass
class CFM_316t:
	""" Rat """
	pass
class TB_BaconUps_027:
	""" Rat Pack (3/4/4)
	&lt;b&gt;Deathrattle:&lt;/b&gt; Summon a number of 2/2 Rats equal _to this minion's Attack."""
	deathrattle = Summon(CONTROLLER, 'TB_BaconUps_027t') * ATK(SELF)#
	pass
class TB_BaconUps_027t:
	""" Rat """
	pass

class LOOT_078:
	""" Cave Hydra (4/2/4)
	Also damages the minions next to whomever this attacks."""
	
	pass
class TB_BaconUps_151:
	""" Cave Hydra (4/4/8)
	Also damages the minions next to whomever this attacks."""
	#
	pass

class BG21_003:# <12>[1453]
	""" Reanimating Rattler (4/5/3)
	[Battlecry:] Give a friendly Beast [Reborn]. """
	#
	pass
class BG21_003_G:# <12>[1453]
	""" Reanimating Rattler (4/10/6)
	[Battlecry:] Give a friendly Beast [Reborn]. """
	#
	pass

class CORE_EX1_534:
	""" Savannah Highmane (4/6/5)
	&lt;b&gt;Deathrattle:&lt;/b&gt; Summon two 2/2 Hyenas."""
	#
	pass
class EX1_534t:
	""" Hyenta
	"""
	#
	pass
class TB_BaconUps_049:
	""" Savannah Highmane (4/12/10)
	&lt;b&gt;Deathrattle:&lt;/b&gt; Summon two 4/4 Hyenas."""
	#
	pass
class TB_BaconUps_049t:
	""" Hyenta
	"""
	#
	pass

class BG20_205:# <12>[1453]
	""" Agamaggan, the Great Boar (5/6/6)
	Your [Blood Gems] give an extra +1/+1. """
	#
	pass
class BG20_205_G:# <12>[1453]
	""" Agamaggan, the Great Boar (5/12/12)
	Your [Blood Gems] give an extra +2/+2. """
	#
	pass

class BG22_001:# <12>[1453]
	""" Baby Krush (5/7/7)
	Whenever this attacks,summon a 9/9 Devilsaur toattack the target first. """
	#
	pass
class BG22_001t2:
	pass
class BG22_001_G:# <12>[1453]
	""" Baby Krush (5/14/14)
	Whenever this attacks, summon an 18/18 Devilsaur to attack the target first. """
	#
	pass
class BG22_001t2_G:
	pass

class BGS_021:# <12>[1453]
	""" Mama Bear (5/5/5)
	Whenever you summon a Beast, give it +5/+5. """
	#
	pass
class TB_BaconUps_090:# <12>[1453]
	""" Mama Bear (5/10/10)
	Whenever you summon a Beast, give it +10/+10. """
	#
	pass

class BG21_001:# <12>[1453]
	""" Palescale Crocolisk(5/4/5)
	[Avenge (2) and Deathrattle:] Give another friendly Beast +6/+6. """
	#
	pass
class BG21_001_G:# <12>[1453]
	""" Palescale Crocolisk(5/8/10)
	[Avenge (2) and Deathrattle:] Give another friendly Beast +12/+12. """
	#
	pass

class BGS_008:# <6>[1453]
	""" Ghastcoiler (6/7/7)
	[Deathrattle:] Summon2 random [Deathrattle] minions. """
	#
	pass
class TB_BaconUps_057:# <6>[1453]
	""" Ghastcoiler (6/14/14)
	[Deathrattle:] Summon 4 random [Deathrattle] minions. """
	#
	pass

class BGS_018:# <12>[1453]
	""" Goldrinn, the Great Wolf (6/4/4)
	[Deathrattle:] Give your Beasts +5/+5. """
	#
	pass
class TB_BaconUps_085:# <12>[1453]
	""" Goldrinn, the Great Wolf (6/8/8)
	[Deathrattle:] Give your Beasts +5/+5. """
	#
	pass


