from ..utils import *

Alterac_Priest=[]

Alterac_Xyrella_the_Devout=True
Alterac_Deliverance=True
Alterac_Shadow_Word_Devour=True
Alterac_Undying_Disciple=True
Alterac_Luminous_Geode=True
Alterac_Spirit_Guide=True
Alterac_Bless=True
Alterac_Gift_of_the_Naaru=True
Alterac_Najak_Hexxen=True
Alterac_Stormpike_Aid_Station=True
Alterac_Horn_of_Wrathion=True
Alterac_Lightmaw_Netherdrake=True
Alterac_Mida_Pure_Light=True


if Alterac_Xyrella_the_Devout:# 
	Alterac_Priest+=['AV_207']
	Alterac_Priest+=['AV_207p']
	Alterac_Priest+=['AV_207p2']
class AV_207:# <6>[1626]
	""" Xyrella, the Devout
	[Battlecry:] Trigger the [Deathrattle] of every friendly minion that died this game. """
	#
	pass

class AV_207p:# <6>[1626]
	""" Holy Touch
	[Hero Power] Restore #5 Health. Flip each turn. """
	#
	pass

class AV_207p2:# <6>[1626]
	""" Void Spike
	[Hero Power] Deal $5 damage. Flip each turn. """
	#
	pass

if Alterac_Deliverance:# 
	Alterac_Priest+=['AV_315']
	Alterac_Priest+=['AV_315e2']
class AV_315:# <6>[1626]
	""" Deliverance
	Deal $3 damage to a minion. [Honorable Kill:] Summon a new 3/3 copy of it. """
	#
	pass

class AV_315e2:# <6>[1626]
	""" Salvation
	Attack and Health set to 3. """
	#
	pass

if Alterac_Shadow_Word_Devour:# 
	Alterac_Priest+=['AV_324']
	Alterac_Priest+=['AV_324e2']
	Alterac_Priest+=['AV_324e2b']
	Alterac_Priest+=['AV_324e3']
	Alterac_Priest+=['AV_324eb']
class AV_324:# <6>[1626]
	""" Shadow Word: Devour
	Choose a minion. It steals 1 Health from _ALL other minions. """
	#
	pass

class AV_324e2:# <6>[1626]
	""" Superior
	Increased Health. """
	#
	pass

class AV_324e2b:# <6>[1626]
	""" Superior
	Increased Health. """
	#
	pass

class AV_324e3:# <6>[1626]
	""" Inferior
	Reduced Health. """
	#
	pass

class AV_324eb:# <6>[1626]
	""" Inferior
	Reduced Health. """
	#
	pass

if Alterac_Undying_Disciple:# 
	Alterac_Priest+=['AV_325']
class AV_325:# <6>[1626]
	""" Undying Disciple
	[Taunt] [Deathrattle:] Deal damage equal to this minion's Attack to all enemy minions. """
	#
	pass

if Alterac_Luminous_Geode:# 
	Alterac_Priest+=['AV_326']
	Alterac_Priest+=['AV_326e']
class AV_326:# <6>[1626]
	""" Luminous Geode
	After a friendly minion is healed, give it +2 Attack. """
	#
	pass

class AV_326e:# <6>[1626]
	""" Illuminated
	+2 Attack. """
	#
	pass

if Alterac_Spirit_Guide:# 
	Alterac_Priest+=['AV_328']
class AV_328:# <6>[1626]
	""" Spirit Guide
	[Taunt] [Deathrattle:] Draw a Holy spell and a Shadow spell. """
	#
	pass

if Alterac_Bless:# 
	Alterac_Priest+=['AV_329']
	Alterac_Priest+=['AV_329e']
	Alterac_Priest+=['AV_329e2']
class AV_329:# <6>[1626]
	""" Bless
	Give a minion +2 Health, then set its Attack to be equal to its Health. """
	#
	pass

class AV_329e:# <6>[1626]
	""" Blessed
	+2 Health and this minion's Attack is equal to its Health. """
	#
	pass

class AV_329e2:# <6>[1626]
	""" Blessed
	+2 Health. """
	#
	pass

if Alterac_Gift_of_the_Naaru:# 
	Alterac_Priest+=['AV_330']
class AV_330:# <6>[1626]
	""" Gift of the Naaru
	Restore #3 Health to all characters. If any are still damaged, draw a card. """
	#
	pass

if Alterac_Najak_Hexxen:# 
	Alterac_Priest+=['AV_331']
	Alterac_Priest+=['AV_331e']
	Alterac_Priest+=['AV_331e2']
class AV_331:# <6>[1626]
	""" Najak Hexxen
	[Battlecry:] Take control of an enemy minion. [Deathrattle:] Give the minion back. """
	#
	pass

class AV_331e:# <6>[1626]
	""" Dark Concoction
	Give this back when Najak is destroyed. """
	#
	pass

class AV_331e2:# <6>[1626]
	""" Dark Concoction
	Took control of {0}. """
	#
	pass

if Alterac_Stormpike_Aid_Station:# 
	Alterac_Priest+=['AV_664']
	Alterac_Priest+=['AV_664e2']
class AV_664:# <6>[1626]
	""" Stormpike Aid Station
	At the end of your turn, give your minions +2 Health. Lasts 3 turns. """
	#
	pass

class AV_664e2:# <6>[1626]
	""" Restored
	+2 Health. """
	#
	pass

if Alterac_Horn_of_Wrathion:# 
	Alterac_Priest+=['ONY_017']
class ONY_017:# <6>[1626]
	""" Horn of Wrathion
	Draw a minion. If it's a Dragon, summon two 2/1 Whelps with [Rush]. """
	#
	pass

if Alterac_Lightmaw_Netherdrake:# 
	Alterac_Priest+=['ONY_026']
class ONY_026:# <6>[1626]
	""" Lightmaw Netherdrake
	[Battlecry:] If you're holding a Holy and a Shadow spell, deal 3 damage to all other minions. """
	#
	pass

if Alterac_Mida_Pure_Light:# 
	Alterac_Priest+=['ONY_028']
	Alterac_Priest+=['ONY_028t']
class ONY_028:# <6>[1626]
	""" Mi'da, Pure Light
	[Divine Shield], [Lifesteal] [Deathrattle:] Shuffle a Fragment into your deck that resummons Mi'da when drawn. """
	#
	pass

class ONY_028t:# <6>[1626]
	""" Fragment of Mi'da
	[Casts When Drawn] Summon Mi'da, Pure Light. """
	#
	pass


