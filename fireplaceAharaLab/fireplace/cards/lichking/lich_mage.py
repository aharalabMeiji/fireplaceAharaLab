from ..utils import *

Lich_Mage=[]

Lich_Vexallus=True
Lich_Arcsplitter=True
Lich_Magisters_Apprentice=True
Lich_Arcane_Defenders=True
Lich_Energy_Shaper=True
Lich_Vast_Wisdom=True
Lich_Prismatic_Elemental=True
Lich_Arcane_Wyrm=True
Lich_Grand_Magister_Rommath=True
Lich_Arcane_Bolt=True


if Lich_Vexallus:# 
	Lich_Mage+=['RLK_541']
class RLK_541_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_541:# <4>[1776]
	""" Vexallus (minion:5/3/5)
	Your Arcane spells cast twice. """
	#
	pass

if Lich_Arcsplitter:# 
	Lich_Mage+=['RLK_542']
class RLK_542_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_542:# <4>[1776]
	""" Arcsplitter (minion:3/3/2)
	<b>Deathrattle:</b> Add 2 Arcane Bolts to your hand. """
	#
	pass

if Lich_Magisters_Apprentice:# 
	Lich_Mage+=['RLK_543']
class RLK_543_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_543:# <4>[1776]
	""" Magister's Apprentice (minion:2/3/2)
	Your Arcane spells cost (1) less. """
	#
	pass

if Lich_Arcane_Defenders:# 
	Lich_Mage+=['RLK_544']
class RLK_544_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_544:# <4>[1776]
	""" Arcane Defenders (spell:8)
	Summon two 5/6 Golems with <b>Taunt</b> and "Can't be targeted by spells or Hero Powers." """
	#
	pass

	Lich_Mage+=['RLK_544t']
class RLK_544t_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_544t:# <4>[1776]
	""" Golem Guardian (minion:5/5/6)
	<b>Taunt</b> Can't be targeted by spells or Hero Powers. """
	#
	pass

if Lich_Energy_Shaper:# 
	Lich_Mage+=['RLK_545']
class RLK_545_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_545:# <4>[1776]
	""" Energy Shaper (minion:4/3/5)
	<b>Battlecry:</b> Transform all spells in your hand into ones that cost (2) more. <i>(They keep their original Cost.)</i> """
	#
	pass

if Lich_Vast_Wisdom:# 
	Lich_Mage+=['RLK_546']
class RLK_546_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_546:# <4>[1776]
	""" Vast Wisdom (spell:3)
	<b>Discover</b> two spells that cost (3) or less. Swap their Costs. """
	#
	pass

	Lich_Mage+=['RLK_546e']
class RLK_546e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_546e:# <4>[1776]
	""" Infinite Wisdom (0)
	This card's cost is swapped. """
	#
	pass

if Lich_Prismatic_Elemental:# 
	Lich_Mage+=['RLK_547']
class RLK_547_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_547:# <4>[1776]
	""" Prismatic Elemental (minion:2/1/3)
	<b>Battlecry:</b> <b>Discover</b> a spell from any class. It costs (1) less. """
	#
	pass

	Lich_Mage+=['RLK_547e']
class RLK_547e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_547e:# <4>[1776]
	""" Strange Energy (0)
	Costs (1) less. """
	#
	pass

if Lich_Arcane_Wyrm:# 
	Lich_Mage+=['RLK_548']
class RLK_548_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_548:# <4>[1776]
	""" Arcane Wyrm (minion:1/1/2)
	<b>Battlecry:</b> Add an Arcane Bolt to your hand. """
	#
	pass

if Lich_Grand_Magister_Rommath:# 
	Lich_Mage+=['RLK_803']
class RLK_803_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_803:# <4>[1776]
	""" Grand Magister Rommath (minion:9/5/7)
	<b>Battlecry:</b> Recast each spell you've cast this game that didn't start in your deck. """
	#
	pass

	Lich_Mage+=['RLK_803e']
class RLK_803e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_803e:# <4>[1776]
	""" Mana Sated (0)
	Your Arcane spells cast twice. """
	#
	pass

if Lich_Arcane_Bolt:# 
	Lich_Mage+=['RLK_843']
class RLK_843_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_843:# <4>[1776]
	""" Arcane Bolt (spell:1)
	Deal $2 damage. <b>Manathirst (8):</b> Deal $3 damage instead. """
	#
	pass

