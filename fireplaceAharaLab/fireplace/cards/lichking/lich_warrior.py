from ..utils import *

Lich_Warrior=[]

Lich_Sunfire_Smithing=True
Lich_Last_Stand=True
Lich_Silverfury_Stalwart=True
Lich_Light_of_the_Phoenix=True
Lich_Thoribelore=True
Lich_Blazing_Power=True
Lich_Disruptive_Spellbreaker=True
Lich_Asvedon_the_Grandshield=True
Lich_Sunfury_Champion=True
Lich_Embers_of_Strength=True


if Lich_Sunfire_Smithing:# 
	Lich_Warrior+=['RLK_600']
class RLK_600_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_600:# <10>[1776]
	""" Sunfire Smithing (spell:4)
	Equip a 4/2 Sword. Give a random minion in your hand +4/+2. """
	#
	pass

	Lich_Warrior+=['RLK_600e']
class RLK_600e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_600e:# <10>[1776]
	""" Overheated (0)
	+4/+2. """
	#
	pass

	Lich_Warrior+=['RLK_600t']
class RLK_600t_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_600t:# <10>[1776]
	""" Flamberge (4)
	 """
	#
	pass

if Lich_Last_Stand:# 
	Lich_Warrior+=['RLK_601']
class RLK_601_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_601:# <10>[1776]
	""" Last Stand (spell:4)
	Draw a <b>Taunt</b> minion. Double its stats. """
	#
	pass

	Lich_Warrior+=['RLK_601e']
class RLK_601e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_601e:# <10>[1776]
	""" Stalwart Stand (0)
	Stats Doubled. """
	#
	pass

if Lich_Silverfury_Stalwart:# 
	Lich_Warrior+=['RLK_602']
class RLK_602_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_602:# <10>[1776]
	""" Silverfury Stalwart (minion:6/4/8)
	<b><b>Taunt</b>, Rush</b> Can't be targeted by spells or Hero Powers. """
	#
	pass

if Lich_Light_of_the_Phoenix:# 
	Lich_Warrior+=['RLK_603']
class RLK_603_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_603:# <10>[1776]
	""" Light of the Phoenix (spell:4)
	Draw 2 cards. Costs (1) less for each damaged friendly character. """
	#
	pass

if Lich_Thoribelore:# 
	Lich_Warrior+=['RLK_604']
class RLK_604_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_604:# <10>[1776]
	""" Thori'belore (minion:4/4/4)
	<b>Rush</b>. <b>Deathrattle:</b> Go <b>Dormant</b>. Cast a Fire spell to revive Thori'belore! <i>(Revives 2 times.)</i> """
	#
	pass

	Lich_Warrior+=['RLK_604a']
class RLK_604a_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_604a:# <10>[1776]
	""" Thori'belore (minion:4/4/4)
	<b>Rush</b>. <b>Deathrattle:</b> Go <b>Dormant</b>. Cast a Fire spell to revive Thori'belore! <i>(Revives once.)</i> """
	#
	pass

	Lich_Warrior+=['RLK_604b']
class RLK_604b_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_604b:# <10>[1776]
	""" Thori'belore (minion:4/4/4)
	<b>Rush</b> """
	#
	pass

	Lich_Warrior+=['RLK_604t']
class RLK_604t_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_604t:# <10>[1776]
	""" Phoenix Egg (minion:21/0/1)
	<b>Dormant</b> Cast a Fire spell to revive Thori'belore! """
	#
	pass

	Lich_Warrior+=['RLK_604t2']
class RLK_604t2_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_604t2:# <10>[1776]
	""" Phoenix Egg (minion:21/0/1)
	<b>Dormant</b> Cast a Fire spell to revive Thori'belore! """
	#
	pass

if Lich_Blazing_Power:# 
	Lich_Warrior+=['RLK_605']
class RLK_605_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_605:# <10>[1776]
	""" Blazing Power (spell:2)
	Give a minion +1/+1. Repeat for each damaged friendly character. """
	#
	pass

	Lich_Warrior+=['RLK_605e']
class RLK_605e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_605e:# <10>[1776]
	""" On Fire! (0)
	+1/+1. """
	#
	pass

if Lich_Disruptive_Spellbreaker:# 
	Lich_Warrior+=['RLK_607']
class RLK_607_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_607:# <10>[1776]
	""" Disruptive Spellbreaker (minion:5/4/5)
	At the end of your turn, your opponent discards a spell. """
	#
	pass

	Lich_Warrior+=['RLK_607e']
class RLK_607e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_607e:# <10>[1776]
	""" Broken Spell (0)
	Storing {0}. """
	#
	pass

if Lich_Asvedon_the_Grandshield:# 
	Lich_Warrior+=['RLK_608']
class RLK_608_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_608:# <10>[1776]
	""" Asvedon, the Grandshield (minion:3/3/3)
	<b>Battlecry:</b> Cast a copy of the last spell your opponent played. """
	#
	pass

if Lich_Sunfury_Champion:# 
	Lich_Warrior+=['RLK_609']
class RLK_609_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_609:# <10>[1776]
	""" Sunfury Champion (minion:1/1/3)
	After you cast a Fire spell, deal 1 damage to all minions. """
	#
	pass

if Lich_Embers_of_Strength:# 
	Lich_Warrior+=['RLK_960']
class RLK_960_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_960:# <10>[1776]
	""" Embers of Strength (spell:2)
	Summon two 1/2 Guards with <b>Taunt</b>. <b>Manathirst (6):</b> Give them +1/+2. """
	#
	pass

	Lich_Warrior+=['RLK_960e']
class RLK_960e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_960e:# <10>[1776]
	""" Empowered Embers (0)
	+1/+2. """
	#
	pass

	Lich_Warrior+=['RLK_960t']
class RLK_960t_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_960t:# <10>[1776]
	""" Emberbound Guard (minion:1/1/2)
	<b>Taunt</b> """
	#
	pass

