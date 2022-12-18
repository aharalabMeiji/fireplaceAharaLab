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
Lich_Conjured_Arrow=True
Lich_Windrunners_Bow=True
Lich_Arcane_Quiver=True
Lich_Silvermoon_Farstrider=True
Lich_Sylvanas_Windrunner=True
Lich_Quick_Fire=True
Lich_Sylvanas_Windrunner=True


if Lich_Conjured_Arrow:# 
	Lich_Hunter+=['RLK_804']
class RLK_804_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_804:# <3>[1776]
	""" Conjured Arrow (spell:2)
	Deal $2 damage to a minion. <b>Manathirst (6):</b> Draw that many cards. """
	#
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
class RLK_819_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_819:# <3>[1776]
	""" Eversong Portal (spell:4)
	Summon $1 4/4 |4(Lynx, Lynxes) with <b>Rush</b> <i>(improved by <b>Spell Damage</b>)</i>. """
	#
	pass

	Lich_Hunter+=['RLK_819t']
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
class RLK_827_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_827:# <3>[1776]
	""" Keeneye Spotter (minion:3/3/4)
	Whenever your hero attacks a minion, set its Health to 1. """
	#
	pass

	Lich_Hunter+=['RLK_827e']
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
class RLK_828_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_828:# <3>[1776]
	""" Hope of Quel'Thalas (6)
	After your hero attacks, give your minions +1/+1 <i>(wherever they are).</i> """
	#
	pass

	Lich_Hunter+=['RLK_828e']
class RLK_828e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_828e:# <3>[1776]
	""" Light of the Sunwell (0)
	+1/+1 """
	#
	pass

if Lich_Conjured_Arrow:# 
	Lich_Hunter+=['RLK_Prologue_804']
class RLK_Prologue_804_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_Prologue_804:# <3>[1776]
	""" Conjured Arrow (spell:4)
	Deal $2 damage to a minion and draw 2 cards. """
	#
	pass

if Lich_Windrunners_Bow:# 
	Lich_Hunter+=['RLK_Prologue_Bow_003w']
class RLK_Prologue_Bow_003w_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_Prologue_Bow_003w:# <3>[1776]
	""" Windrunner's Bow (5)
	After your hero attacks, summon two Silvermoon Sentinels. """
	#
	pass

if Lich_Arcane_Quiver:# 
	Lich_Hunter+=['RLK_Prologue_RLK_817']
class RLK_Prologue_RLK_817_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_Prologue_RLK_817:# <3>[1776]
	""" Arcane Quiver (spell:2)
	<b>Discover</b> a spell from your deck. If it's Arcane, give it <b>Spell Damage +1</b>. """
	#
	pass

if Lich_Silvermoon_Farstrider:# 
	Lich_Hunter+=['RLK_Prologue_RLK_826']
class RLK_Prologue_RLK_826_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_Prologue_RLK_826:# <3>[1776]
	""" Silvermoon Farstrider (minion:2/2/3)
	<b>Battlecry:</b> Give all Arcane spells in your hand <b>Spell Damage +1</b>. """
	#
	pass

if Lich_Sylvanas_Windrunner:# 
	Lich_Hunter+=['RLK_Prologue_Sylvanas_003hb']
class RLK_Prologue_Sylvanas_003hb_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_Prologue_Sylvanas_003hb:# <3>[1776]
	""" Sylvanas Windrunner (0)
	 """
	#
	pass

if Lich_Quick_Fire:# 
	Lich_Hunter+=['RLK_Prologue_Sylvanas_003p']
class RLK_Prologue_Sylvanas_003p_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_Prologue_Sylvanas_003p:# <3>[1776]
	""" Quick Fire (1)
	<b>Hero Power</b> Deal $1 damage to two random enemy minions. """
	#
	pass

if Lich_Sylvanas_Windrunner:# 
	Lich_Hunter+=['RLK_Prologue_SylvanasB_003hb2']
class RLK_Prologue_SylvanasB_003hb2_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_Prologue_SylvanasB_003hb2:# <3>[1776]
	""" Sylvanas Windrunner (0)
	 """
	#
	pass

