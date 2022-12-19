from ..utils import *

Lich_Rogue=[]

Lich_Rotten_Rodent=True
Lich_Scourge_Illusionist=True
Lich_Noxious_Infiltrator=True
Lich_Shadow_of_Demise=True
Lich_Concoctor=True
Lich_Potion_Belt=True
Lich_Ghoulish_Alchemist=True
Lich_Vile_Apothecary=True
Lich_Potionmaster_Putricide=True
Lich_Ghostly_Strike=True


if Lich_Rotten_Rodent:# 
	Lich_Rogue+=['RLK_216']
class RLK_216_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_216:# <7>[1776]
	""" Rotten Rodent (minion:2/2/1)
	<b>Battlecry:</b> Reduce the Cost of all <b>Deathrattle</b> cards in your deck by (1). """
	#
	pass

	Lich_Rogue+=['RLK_216e']
class RLK_216e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_216e:# <7>[1776]
	""" Rotten (0)
	Costs (1) less. """
	#
	pass

if Lich_Scourge_Illusionist:# 
	Lich_Rogue+=['RLK_217']
class RLK_217_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_217:# <7>[1776]
	""" Scourge Illusionist (minion:4/4/4)
	<b>Deathrattle:</b> Add a 4/4 copy of another <b>Deathrattle</b> minion in your deck to your hand. It costs (4) less. """
	#
	pass

	Lich_Rogue+=['RLK_217e']
class RLK_217e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_217e:# <7>[1776]
	""" Illusion (0)
	4/4. """
	#
	pass

	Lich_Rogue+=['RLK_217e2']
class RLK_217e2_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_217e2:# <7>[1776]
	""" Illusory (0)
	Costs (4) less. """
	#
	pass

if Lich_Noxious_Infiltrator:# 
	Lich_Rogue+=['RLK_529']
class RLK_529_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_529:# <7>[1776]
	""" Noxious Infiltrator (minion:4/2/5)
	<b>Poisonous</b> <b>Battlecry:</b> If a friendly Undead died after your last turn, deal 1 damage to a minion. """
	#
	pass

if Lich_Shadow_of_Demise:# 
	Lich_Rogue+=['RLK_567']
class RLK_567_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_567:# <7>[1776]
	""" Shadow of Demise (spell:0)
	Each time you cast a spell, transform this into a copy of it. """
	#
	pass

	Lich_Rogue+=['RLK_567e']
class RLK_567e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_567e:# <7>[1776]
	""" Death's Reflection (0)
	Always copy your last played card. """
	#
	pass

	Lich_Rogue+=['RLK_567e2']
class RLK_567e2_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_567e2:# <7>[1776]
	""" Shadow of Death (0)
	Transforming into recent spells. """
	#
	pass

if Lich_Concoctor:# 
	Lich_Rogue+=['RLK_568']
class RLK_568_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_568:# <7>[1776]
	""" Concoctor (minion:1/1/2)
	<b>Battlecry:</b> Add a random Concoction to your hand. """
	#
	pass

if Lich_Potion_Belt:# 
	Lich_Rogue+=['RLK_569']
class RLK_569_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_569:# <7>[1776]
	""" Potion Belt (spell:2)
	<b>Discover</b> 2 Concoctions. """
	#
	pass

if Lich_Ghoulish_Alchemist:# 
	Lich_Rogue+=['RLK_570']
class RLK_570_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570:# <7>[1776]
	""" Ghoulish Alchemist (minion:2/3/2)
	<b>Battlecry</b>: Your next Concoction costs (0). """
	#
	pass

	Lich_Rogue+=['RLK_570e']
class RLK_570e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570e:# <7>[1776]
	""" Yellow Potion (0)
	+2 Attack. """
	#
	pass

	Lich_Rogue+=['RLK_570e3']
class RLK_570e3_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570e3:# <7>[1776]
	""" Blue Spirit (0)
	Costs (3) less. """
	#
	pass

	Lich_Rogue+=['RLK_570e4']
class RLK_570e4_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570e4:# <7>[1776]
	""" Doctored (0)
	Your next Concoction costs (0). """
	#
	pass

	Lich_Rogue+=['RLK_570t']
class RLK_570t_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570t:# <7>[1776]
	""" Mixed Potion (spell:3)
	 """
	#
	pass

	Lich_Rogue+=['RLK_570t1']
class RLK_570t1_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570t1:# <7>[1776]
	""" Slimy Concoction (spell:3)
	Summon a random 3-Cost minion. <i>Add another Concoction to your hand to mix together!</i> """
	#
	pass

	Lich_Rogue+=['RLK_570t1t']
class RLK_570t1t_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570t1t:# <7>[1776]
	""" Orange Slime (minion:3/3/4)
	 """
	#
	pass

	Lich_Rogue+=['RLK_570t1t1']
class RLK_570t1t1_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570t1t1:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Summon a random 3-Cost minion. Add a card to your hand from another class. It costs (3) less. """
	#
	pass

	Lich_Rogue+=['RLK_570t1t2']
class RLK_570t1t2_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570t1t2:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Summon a random 3-Cost minion. Destroy a random enemy minion. """
	#
	pass

	Lich_Rogue+=['RLK_570t1t3']
class RLK_570t1t3_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570t1t3:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Deal $3 damage. Summon a random 3-Cost minion. """
	#
	pass

	Lich_Rogue+=['RLK_570t1t4']
class RLK_570t1t4_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570t1t4:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Summon two random 3-Cost minions. """
	#
	pass

	Lich_Rogue+=['RLK_570t2']
class RLK_570t2_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570t2:# <7>[1776]
	""" Dreadful Concoction (spell:3)
	Destroy a random enemy minion. <i>Add another Concoction to your hand to mix together!</i> """
	#
	pass

	Lich_Rogue+=['RLK_570t2e']
class RLK_570t2e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570t2e:# <7>[1776]
	""" Green Potion (0)
	<b>Poisonous</b> and <b>Reborn</b>. """
	#
	pass

	Lich_Rogue+=['RLK_570t2t1']
class RLK_570t2t1_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570t2t1:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Deal $3 damage. Destroy a random enemy minion. """
	#
	pass

	Lich_Rogue+=['RLK_570t2t2']
class RLK_570t2t2_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570t2t2:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Destroy two random enemy minions. """
	#
	pass

	Lich_Rogue+=['RLK_570t3']
class RLK_570t3_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570t3:# <7>[1776]
	""" Bubbling Concoction (spell:3)
	Deal $3 damage. <i>Add another Concoction to your hand to mix together!</i> """
	#
	pass

	Lich_Rogue+=['RLK_570t3t']
class RLK_570t3t_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570t3t:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Deal $3 damage, twice. """
	#
	pass

	Lich_Rogue+=['RLK_570t4']
class RLK_570t4_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570t4:# <7>[1776]
	""" Hazy Concoction (spell:3)
	Add a card to your hand from another class. It costs (3) less. <i>Add another Concoction to your hand to mix together!</i> """
	#
	pass

	Lich_Rogue+=['RLK_570t4t1']
class RLK_570t4t1_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570t4t1:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Add a card to your hand from another class. It costs (3) less. Destroy a random enemy minion. """
	#
	pass

	Lich_Rogue+=['RLK_570t4t2']
class RLK_570t4t2_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570t4t2:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Deal $3 damage. Add a card to your hand from another class. It costs (3) less. """
	#
	pass

	Lich_Rogue+=['RLK_570t4t3']
class RLK_570t4t3_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570t4t3:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Add two cards to your hand from another class. They cost (3) less. """
	#
	pass

	Lich_Rogue+=['RLK_570t5']
class RLK_570t5_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570t5:# <7>[1776]
	""" Gleaming Concoction (spell:3)
	Draw 2 cards. <i>Add another Concoction to your hand to mix together!</i> """
	#
	pass

	Lich_Rogue+=['RLK_570tt1']
class RLK_570tt1_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570tt1:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Draw 2 cards. Summon a random 3-Cost minion. """
	#
	pass

	Lich_Rogue+=['RLK_570tt2']
class RLK_570tt2_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570tt2:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Deal $3 damage. Draw 2 cards. """
	#
	pass

	Lich_Rogue+=['RLK_570tt3']
class RLK_570tt3_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570tt3:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Draw 2 cards. Add a card to your hand from another class. It costs (3) less. """
	#
	pass

	Lich_Rogue+=['RLK_570tt4']
class RLK_570tt4_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570tt4:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Draw 2 cards. Destroy a random enemy minion. """
	#
	pass

	Lich_Rogue+=['RLK_570tt5']
class RLK_570tt5_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570tt5:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Draw 4 cards. """
	#
	pass

if Lich_Vile_Apothecary:# 
	Lich_Rogue+=['RLK_571']
class RLK_571_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_571:# <7>[1776]
	""" Vile Apothecary (minion:3/2/4)
	At the end of your turn, add a random Concoction to your hand. """
	#
	pass

if Lich_Potionmaster_Putricide:# 
	Lich_Rogue+=['RLK_572']
class RLK_572_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_572:# <7>[1776]
	""" Potionmaster Putricide (minion:2/1/4)
	After a minion dies, add a Concoction to your hand. """
	#
	pass

if Lich_Ghostly_Strike:# 
	Lich_Rogue+=['RLK_573']
class RLK_573_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_573:# <7>[1776]
	""" Ghostly Strike (spell:1)
	Deal $1 damage. <b>Combo:</b> Draw a card. """
	#
	pass

