from ..utils import *

Alterac_Paladin=[]

Alterac_The_Immovable_Object=True
Alterac_Lightforged_Cariel=True
Alterac_Vitality_Surge=True
Alterac_Hold_the_Bridge=True
Alterac_Templar_Captain=True
Alterac_Brasswing=True
Alterac_Cavalry_Horn=True
Alterac_Protect_the_Innocent=True
Alterac_Stonehearth_Vindicator=True
Alterac_Dun_Baldar_Bridge=True
Alterac_Saidan_the_Scarlet=True
Alterac_Stormwind_Avenger=True
Alterac_Battle_Vicar=True
Alterac_Ring_of_Courage=True
Alterac_Cariel=True


if Alterac_The_Immovable_Object:# 
	Alterac_Paladin+=['AV_146']
	Alterac_Paladin+=['AV_146e']
	Alterac_Paladin+=['AV_146e2']
class AV_146:# <5>[1626]
	""" The Immovable Object  (7/2/5)
	This doesn't loseDurability. Your hero takes half damage,rounded up. """
	play = Buff(SELF, 'AV_146e2'), Buff(CONTROLLER,'AV_146e')
	pass

class AV_146e:# <5>[1626]##############################
	""" Tough
	Take half damage, rounded up. """
	def apply(self, target):
		target.take_half_damage=True
	pass

class AV_146e2:# <5>[1626]
	""" Resilient Weapon
	No durability loss. """
	def apply(self, target):
		target.no_durability_loss=True
	pass

if Alterac_Lightforged_Cariel:# 
	Alterac_Paladin+=['AV_206']
	Alterac_Paladin+=['AV_206p']
	Alterac_Paladin+=['AV_206pe']
class AV_206:# <5>[1626]
	""" Lightforged Cariel
	[Battlecry:] Deal 2damage to all enemies.Equip a 2/5Immovable Object. """
	play = Hit(ENEMY_CHARACTERS, 2), Summon(CONTROLLER, 'AV_146')
	pass

class AV_206p:# <5>[1626]
	""" Blessing of Queens
	[Hero Power]Give a random minion in your hand +4/+4. """
	activate = Buff(RANDOM(FRIENDLY_HAND + MINION), 'AV_206pe')
	pass
AV_206pe=buff(4,4)# <5>[1626]

if Alterac_Vitality_Surge:# 
	Alterac_Paladin+=['AV_213']
class AV_213:# <5>[1626]
	""" Vitality Surge
	Draw a minion.Restore Health to your hero equal to its Cost. """
	#
	pass

if Alterac_Hold_the_Bridge:# 
	Alterac_Paladin+=['AV_338']
	Alterac_Paladin+=['AV_338e']
	Alterac_Paladin+=['AV_338e2']
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

if Alterac_Templar_Captain:# 
	Alterac_Paladin+=['AV_339']
class AV_339:# <5>[1626]
	""" Templar Captain
	[Rush]. After this attacksa minion, summon a 5/5Defender with [Taunt]. """
	#
	pass

if Alterac_Brasswing:# 
	Alterac_Paladin+=['AV_340']
class AV_340:# <5>[1626]
	""" Brasswing
	At the end of your turn, deal2 damage to all enemies.[Honorable Kill:] Restore 4Health to your hero. """
	#
	pass

if Alterac_Cavalry_Horn:# 
	Alterac_Paladin+=['AV_341']
class AV_341:# <5>[1626]
	""" Cavalry Horn
	[Deathrattle:] Summon the lowest Cost minion in your hand. """
	#
	pass

if Alterac_Protect_the_Innocent:# 
	Alterac_Paladin+=['AV_342']
	Alterac_Paladin+=['AV_342t']
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

if Alterac_Stonehearth_Vindicator:# 
	Alterac_Paladin+=['AV_343']
	Alterac_Paladin+=['AV_343e']
class AV_343:# <5>[1626]
	""" Stonehearth Vindicator
	[Battlecry:] Draw a spellthat costs (3) or less.It costs (0) this turn. """
	#
	pass

class AV_343e:# <5>[1626]
	""" Stone Fortitude
	Costs (0)  this turn. """
	#
	pass

if Alterac_Dun_Baldar_Bridge:# 
	Alterac_Paladin+=['AV_344']
	Alterac_Paladin+=['AV_344e']
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

if Alterac_Saidan_the_Scarlet:# 
	Alterac_Paladin+=['AV_345']
class AV_345:# <5>[1626]
	""" Saidan the Scarlet
	[Rush.] Whenever this minion gains Attack or Health, double that amount <i>(wherever this is)</i>. """
	#
	pass


if Alterac_Stormwind_Avenger:# 
	Alterac_Paladin+=['ONY_020']
	Alterac_Paladin+=['ONY_020e']
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

if Alterac_Battle_Vicar:# 
	Alterac_Paladin+=['ONY_022']
class ONY_022:# <5>[1626]
	""" Battle Vicar
	[Battlecry:] [Discover] aHoly spell. """
	#
	pass

if Alterac_Ring_of_Courage:# 
	Alterac_Paladin+=['ONY_027']
	Alterac_Paladin+=['ONY_027e']
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

if Alterac_Cariel:# 
	Alterac_Paladin+=['TB_01_BOM_Mercs_Cariel_001p']
class TB_01_BOM_Mercs_Cariel_001p:# <5>[1626]
	""" Cariel
	[Hero Power]Summon a friendly minion that died this game with 1 Health. """
	#
	pass

#######################

