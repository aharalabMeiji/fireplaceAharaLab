from ..utils import *

Lich_Hunter=[]

Lich_Conjured_Arrow=True
Lich_Arcane_Quiver=True
Lich_Ricochet_Shot=True
Lich_Eversong_Portal=True
Lich_Halduron_Brightwing=True
Lich_Scourge_Tamer=True
Lich_Shockspitter=True
Lich_Silvermoon_Farstrider=True
Lich_Keeneye_Spotter=True
Lich_Hope_of_QuelThalas=True


if Lich_Conjured_Arrow:# 
	Lich_Hunter+=['RLK_804']
class RLK_804_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_804:# <3>[1776]
	""" Conjured Arrow (spell:2)
	Deal $2 damage to a minion. <b>Manathirst (6):</b> Draw that many cards. """
	requirements = REQUIRE_ENEMY_MINION_TARGET
	play = Manathirst(6, [Hit(TARGET, 2)], [Draw(CONTROLLER), Draw(CONTROLLER)])
	pass

if Lich_Arcane_Quiver:# 
	Lich_Hunter+=['RLK_817']
class RLK_817_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_817:# <3>[1776]
	""" Arcane Quiver (spell:2)
	<b>Discover</b> a spell from your deck. If it's Arcane, give it <b>Spell Damage +1</b>. """
	#
	pass

if Lich_Ricochet_Shot:# 
	Lich_Hunter+=['RLK_818']
class RLK_818_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_818:# <3>[1776]
	""" Ricochet Shot (spell:1)
	Deal $1 damage to three random enemies. """
	#
	pass

if Lich_Eversong_Portal:# 
	Lich_Hunter+=['RLK_819']
	Lich_Hunter+=['RLK_819t']
class RLK_819_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_819:# <3>[1776]
	""" Eversong Portal (spell:4)
	Summon $1 4/4 |4(Lynx, Lynxes) with <b>Rush</b> <i>(improved by <b>Spell Damage</b>)</i>. """
	#
	pass

class RLK_819t_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_819t:# <3>[1776]
	""" Eversong Lynx (minion:4/4/4)
	<b>Rush</b> """
	#
	pass

if Lich_Halduron_Brightwing:# 
	Lich_Hunter+=['RLK_820']
class RLK_820_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_820:# <3>[1776]
	""" Halduron Brightwing (minion:3/3/4)
	<b>Battlecry:</b> Give all Arcane spells in your deck <b>Spell Damage +1</b>. """
	#
	pass

if Lich_Scourge_Tamer:# 
	Lich_Hunter+=['RLK_821']
class RLK_821_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_821:# <3>[1776]
	""" Scourge Tamer (minion:2/2/2)
	<b>Battlecry:</b> Craft a custom Zombeast. """
	#
	pass

if Lich_Shockspitter:# 
	Lich_Hunter+=['RLK_825']
class RLK_825_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_825:# <3>[1776]
	""" Shockspitter (minion:2/2/2)
	<b>Battlecry:</b> Deal @ damage. <i>(Improved by your hero attacks this game!)</i> """
	#
	pass

if Lich_Silvermoon_Farstrider:# 
	Lich_Hunter+=['RLK_826']
class RLK_826_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_826:# <3>[1776]
	""" Silvermoon Farstrider (minion:2/2/3)
	<b>Battlecry:</b> Give all Arcane spells in your hand <b>Spell Damage +1</b>. """
	#
	pass

if Lich_Keeneye_Spotter:# 
	Lich_Hunter+=['RLK_827']
	Lich_Hunter+=['RLK_827e']
class RLK_827_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_827:# <3>[1776]
	""" Keeneye Spotter (minion:3/3/4)
	Whenever your hero attacks a minion, set its Health to 1. """
	#
	pass

class RLK_827e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_827e:# <3>[1776]
	""" Hunter's Mark (0)
	This minion has 1 Health. """
	#
	pass

if Lich_Hope_of_QuelThalas:# 
	Lich_Hunter+=['RLK_828']
	Lich_Hunter+=['RLK_828e']
class RLK_828_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_828:# <3>[1776]
	""" Hope of Quel'Thalas (6)
	After your hero attacks, give your minions +1/+1 <i>(wherever they are).</i> """
	#
	pass

class RLK_828e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_828e:# <3>[1776]
	""" Light of the Sunwell (0)
	+1/+1 """
	#
	pass

