
from ..utils import *

#Alterac_Paladin=['AV_146','AV_146e','AV_146e2','AV_206','AV_206p','AV_206pe','AV_213','AV_338','AV_338e','AV_338e2','AV_339','AV_340','AV_341','AV_342','AV_342t','AV_343','AV_343e','AV_344','AV_344e','AV_345',]
#Alterac_Paladin += ['ONY_020','ONY_020e','ONY_022','ONY_027','ONY_027e',]

class AV_146:# <5>[1626] (7/2/5)
	""" The Immovable Object
	This doesn't lose Durability. Your hero takes half damage, rounded up. """
	play = Buff(SELF, 'AV_146e2'), Buff(FRIENDLY_HERO,'AV_146e')
	pass

class AV_146e:# <5>[1626]
	""" Tough
	Take half damage, rounded up. """
	#
	pass

class AV_146e2:# <5>[1626]
	""" Resilient Weapon
	No durability loss. """
	#
	pass

class AV_206:# <5>[1626]
	""" Lightforged Cariel (7/*/5) hero
	[Battlecry:] Deal 2 damage to all enemies.Equip a 2/5 Immovable Object. """
	play = Hit(ENEMY_CHARACTERS, 2), Summon(CONTROLLER, 'AV_146')
	pass

class AV_206p:# <5>[1626]
	""" Blessing of Queens (2) heropower
	[Hero Power]Give a random minion in your hand +4/+4. """
	activate = Buff(RANDOM(FRIENDLY_HAND + MINION), 'AV_206pe')
	pass
AV_206pe=buff(4,4)# <5>[1626]
""" Blessing of Queens
+4/+4. """

class AV_213:# <5>[1626]
	""" Vitality Surge
	Draw a minion.Restore Health to your hero equal to its Cost. """
	#
	pass

class AV_338:# <5>[1626]
	""" Hold the Bridge
	Give a minion +2/+1and [Divine Shield].It gains [Lifesteal] untilend of turn. """
	#
	pass

class AV_338e:# <5>[1626]
	""" High Morale
	+2/+1. """
	#
	pass

class AV_338e2:# <5>[1626]
	""" High Morale
	[Lifesteal] this turn. """
	#
	pass

class AV_339:# <5>[1626]
	""" Templar Captain
	[Rush]. After this attacksa minion, summon a 5/5Defender with [Taunt]. """
	#
	pass

class AV_340:# <5>[1626]
	""" Brasswing
	At the end of your turn, deal2 damage to all enemies.[Honorable Kill:] Restore 4Health to your hero. """
	#
	pass

class AV_341:# <5>[1626]
	""" Cavalry Horn
	[Deathrattle:] Summon the lowest Cost minion in your hand. """
	#
	pass

class AV_342:# <5>[1626]
	""" Protect the Innocent
	Summon a 5/5 Defender with [Taunt]. If your hero was healed this turn, summon another. """
	#
	pass

class AV_342t:# <5>[1626]
	""" Stormpike Defender
	[Taunt] """
	#
	pass

class AV_343:# <5>[1626]
	""" Stonehearth Vindicator
	[Battlecry:] Draw a spellthat costs (3) or less.It costs (0) this turn. """
	#
	pass

class AV_343e:# <5>[1626]
	""" Stone Fortitude
	Costs (3) less this turn. """
	#
	pass

class AV_344:# <5>[1626]
	""" Dun Baldar Bridge
	After you summon aminion, give it +2/+2.Lasts 3 turns. """
	#
	pass

class AV_344e:# <5>[1626]
	""" Coldtooth Supplies
	+2/+2. """
	#
	pass

class AV_345:# <5>[1626]
	""" Saidan the Scarlet
	[Rush.] Whenever this minion gains Attack or Health, double that amount <i>(wherever this is)</i>. """
	#
	pass


class ONY_020:# <5>[1626]
	""" Stormwind Avenger
	After you cast a spell on this minion, it gains +2 Attack. """
	#
	pass

class ONY_020e:# <5>[1626]
	""" En Garde!
	+2 Attack. """
	#
	pass

class ONY_022:# <5>[1626]
	""" Battle Vicar
	[Battlecry:] [Discover] aHoly spell. """
	#
	pass

class ONY_027:# <5>[1626]
	""" Ring of Courage
	[Tradeable]Give a minion +1/+1. Repeat for each enemy minion. """
	#
	pass

class ONY_027e:# <5>[1626]
	""" Heroic
	+1/+1. """
	#
	pass
