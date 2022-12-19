from ..utils import *

Lich_Paladin=[]

Lich_Timewarden=True
Lich_Daring_Drake=True
Lich_Flight_of_the_Bronze=True
Lich_For_QuelThalas=True
Lich_Anachronos=True
Lich_Sanguine_Soldier=True
Lich_Seal_of_Blood=True
Lich_Feast_and_Famine=True
Lich_Blood_Matriarch_Liadrin=True
Lich_Blood_Crusader=True



if Lich_Timewarden:# 
	Lich_Paladin+=['RLK_527']
class RLK_527_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_527:# <5>[1776]
	""" Timewarden (minion:4/3/5)
	<b>Battlecry:</b> Until the end of your next turn, Dragons you summon gain <b>Taunt</b> and <b>Divine Shield</b>. """
	#
	pass

	Lich_Paladin+=['RLK_527e2']
class RLK_527e2_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_527e2:# <5>[1776]
	""" From the Future (0)
	Has <b>Divine Shield</b> and <b>Taunt</b>. """
	#
	pass

if Lich_Daring_Drake:# 
	Lich_Paladin+=['RLK_916']
class RLK_916_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_916:# <5>[1776]
	""" Daring Drake (minion:4/4/4)
	<b>Rush</b> <b>Battlecry:</b> If you're holding a Dragon, gain +1/+1. """
	#
	pass

	Lich_Paladin+=['RLK_916e']
class RLK_916e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_916e:# <5>[1776]
	""" Bravery (0)
	+1/+1 """
	#
	pass

if Lich_Flight_of_the_Bronze:# 
	Lich_Paladin+=['RLK_917']
class RLK_917_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_917:# <5>[1776]
	""" Flight of the Bronze (spell:1)
	<b>Discover</b> a Dragon. <b>Manathirst (7):</b> Summon a 5/5 Drake with <b>Taunt</b>. """
	#
	pass

	Lich_Paladin+=['RLK_917t']
class RLK_917t_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_917t:# <5>[1776]
	""" Bronze Defender (minion:5/5/5)
	<b>Taunt</b> """
	#
	pass

if Lich_For_QuelThalas:# 
	Lich_Paladin+=['RLK_918']
class RLK_918_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_918:# <5>[1776]
	""" For Quel'Thalas! (spell:2)
	Give a friendly minion +3 Attack. Give your hero +2 Attack this turn. """
	#
	pass

	Lich_Paladin+=['RLK_918e']
class RLK_918e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_918e:# <5>[1776]
	""" For Quel'Thalas! (0)
	+3 Attack """
	#
	pass

	Lich_Paladin+=['RLK_918e2']
class RLK_918e2_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_918e2:# <5>[1776]
	""" For Quel'Thalas! (2)
	+2 Attack. """
	#
	pass

if Lich_Anachronos:# 
	Lich_Paladin+=['RLK_919']
class RLK_919_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_919:# <5>[1776]
	""" Anachronos (minion:7/8/8)
	<b>Battlecry:</b> Send all other minions 2 turns into the future. """
	#
	pass

	Lich_Paladin+=['RLK_919e']
class RLK_919e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_919e:# <5>[1776]
	""" Time Travel (0)
	Sending a minion 2 turns into the future. """
	#
	pass

if Lich_Sanguine_Soldier:# 
	Lich_Paladin+=['RLK_921']
class RLK_921_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_921:# <5>[1776]
	""" Sanguine Soldier (minion:1/2/1)
	<b>Divine Shield</b>  <b>Battlecry:</b> Deal 2 damage to your hero. """
	#
	pass

if Lich_Seal_of_Blood:# 
	Lich_Paladin+=['RLK_922']
class RLK_922_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_922:# <5>[1776]
	""" Seal of Blood (spell:3)
	Give a minion +3/+3 and <b>Divine Shield</b>. Deal $3 damage to your hero. """
	#
	pass

	Lich_Paladin+=['RLK_922e']
class RLK_922e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_922e:# <5>[1776]
	""" Blood Seal (0)
	+3/+3. """
	#
	pass

if Lich_Feast_and_Famine:# 
	Lich_Paladin+=['RLK_923']
class RLK_923_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_923:# <5>[1776]
	""" Feast and Famine (spell:1)
	Give your hero +3 Attack this turn. <b>Manathirst (4):</b> And <b>Lifesteal</b>. """
	#
	pass

	Lich_Paladin+=['RLK_923e1']
class RLK_923e1_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_923e1:# <5>[1776]
	""" Feast (0)
	+3 Attack this turn. """
	#
	pass

	Lich_Paladin+=['RLK_923e3']
class RLK_923e3_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_923e3:# <5>[1776]
	""" Famine (0)
	<b>Lifesteal</b> this turn. """
	#
	pass

if Lich_Blood_Matriarch_Liadrin:# 
	Lich_Paladin+=['RLK_924']
class RLK_924_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_924:# <5>[1776]
	""" Blood Matriarch Liadrin (minion:2/3/2)
	After you summon a minion with less Attack than this, give it <b>Divine Shield</b> and <b>Rush</b>. """
	#
	pass

	Lich_Paladin+=['RLK_924e']
class RLK_924e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_924e:# <5>[1776]
	""" Annointed in Blood (0)
	Gains <b>Rush</b> and <b>Divine Shield</b>. """
	#
	pass

if Lich_Blood_Crusader:# 
	Lich_Paladin+=['RLK_927']
class RLK_927_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_927:# <5>[1776]
	""" Blood Crusader (minion:6/5/5)
	<b>Battlecry:</b> Your next Paladin minion this turn costs  Health instead of Mana. """
	#
	pass

	Lich_Paladin+=['RLK_927e']
class RLK_927e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_927e:# <5>[1776]
	""" Crusade (0)
	Costs Health instead of Mana. """
	#
	pass



