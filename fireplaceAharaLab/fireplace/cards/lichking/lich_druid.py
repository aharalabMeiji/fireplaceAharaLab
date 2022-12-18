from ..utils import *

Lich_Druid=[]

Lich_Lingering_Zombie=True
Lich_Crypt_Keeper=True
Lich_Unending_Swarm=True
Lich_Beetlemancy=True
Lich_Wither=True
Lich_Chitinous_Plating=True
Lich_Underking=True
Lich_Elder_Nadox=True
Lich_AnubRekhan=True
Lich_Nerubian_Flyer=True


if Lich_Lingering_Zombie:# 
	Lich_Druid+=['RLK_650']
class RLK_650_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_650:# <2>[1776]
	""" Lingering Zombie (minion:1/1/1)
	<b>Deathrattle:</b> Summon a 1/1 Disarmed Zombie with "<b>Deathrattle:</b> Summon a 1/1 Zombie." """
	#
	pass

	Lich_Druid+=['RLK_650t']
class RLK_650t_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_650t:# <2>[1776]
	""" Disarmed Zombie (minion:1/1/1)
	<b>Deathrattle:</b> Summon a 1/1 Zombie. """
	#
	pass

	Lich_Druid+=['RLK_650t2']
class RLK_650t2_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_650t2:# <2>[1776]
	""" Unarmed Zombie (minion:1/1/1)
	 """
	#
	pass

if Lich_Crypt_Keeper:# 
	Lich_Druid+=['RLK_651']
class RLK_651_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_651:# <2>[1776]
	""" Crypt Keeper (minion:8/4/6)
	<b>Taunt</b>. Costs (1) less for each Armor you have. """
	#
	pass

if Lich_Unending_Swarm:# 
	Lich_Druid+=['RLK_652']
class RLK_652_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_652:# <2>[1776]
	""" Unending Swarm (spell:6)
	Resurrect all friendly minions that cost (2) or less. """
	#
	pass

if Lich_Beetlemancy:# 
	Lich_Druid+=['RLK_654']
class RLK_654_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_654:# <2>[1776]
	""" Beetlemancy (spell:5)
	<b>Choose One</b> - Gain 12 Armor; or Summon two 3/3 Beetles with <b>Taunt</b>. """
	#
	pass

	Lich_Druid+=['RLK_654a']
class RLK_654a_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_654a:# <2>[1776]
	""" Beetle Juice (spell:5)
	Gain 12 Armor. """
	#
	pass

	Lich_Druid+=['RLK_654b']
class RLK_654b_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_654b:# <2>[1776]
	""" Bug Snacks (spell:5)
	Summon two 3/3 Beetles with <b>Taunt</b>. """
	#
	pass

	Lich_Druid+=['RLK_654t']
class RLK_654t_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_654t:# <2>[1776]
	""" Beetle (minion:3/3/3)
	<b>Taunt</b> """
	#
	pass

if Lich_Wither:# 
	Lich_Druid+=['RLK_655']
class RLK_655_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_655:# <2>[1776]
	""" Wither (spell:2)
	Choose a minion. Each friendly Undead steals 1 Attack and Health from it. """
	#
	pass

	Lich_Druid+=['RLK_655e']
class RLK_655e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_655e:# <2>[1776]
	""" Withered (0)
	Reduced stats. """
	#
	pass

	Lich_Druid+=['RLK_655e2']
class RLK_655e2_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_655e2:# <2>[1776]
	""" Life Siphon (0)
	Increased stats. """
	#
	pass

	Lich_Druid+=['RLK_655e2a']
class RLK_655e2a_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_655e2a:# <2>[1776]
	""" Life Siphon (0)
	Increased Attack. """
	#
	pass

	Lich_Druid+=['RLK_655e2b']
class RLK_655e2b_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_655e2b:# <2>[1776]
	""" Life Siphon (0)
	Increased Health. """
	#
	pass

	Lich_Druid+=['RLK_655ea']
class RLK_655ea_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_655ea:# <2>[1776]
	""" Withered (0)
	Reduced Attack. """
	#
	pass

	Lich_Druid+=['RLK_655eb']
class RLK_655eb_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_655eb:# <2>[1776]
	""" Withered (0)
	Reduced Health. """
	#
	pass

if Lich_Chitinous_Plating:# 
	Lich_Druid+=['RLK_656']
class RLK_656_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_656:# <2>[1776]
	""" Chitinous Plating (spell:2)
	Gain 4 Armor. At the start of your next turn, gain 4 more. """
	#
	pass

	Lich_Druid+=['RLK_656e']
class RLK_656e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_656e:# <2>[1776]
	""" Molting (0)
	Gain 4 Armor next turn. """
	#
	pass

if Lich_Underking:# 
	Lich_Druid+=['RLK_657']
class RLK_657_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_657:# <2>[1776]
	""" Underking (minion:7/6/6)
	<b>Rush</b> <b>Battlecry and Deathrattle:</b> Gain 6 Armor. """
	#
	pass

if Lich_Elder_Nadox:# 
	Lich_Druid+=['RLK_658']
class RLK_658_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_658:# <2>[1776]
	""" Elder Nadox (minion:5/5/4)
	<b>Battlecry:</b> Destroy a friendly Undead. Your minions gain its Attack. """
	#
	pass

	Lich_Druid+=['RLK_658e']
class RLK_658e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_658e:# <2>[1776]
	""" Might of Nadox (0)
	Increased stats. """
	#
	pass

if Lich_AnubRekhan:# 
	Lich_Druid+=['RLK_659']
class RLK_659_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_659:# <2>[1776]
	""" Anub'Rekhan (minion:8/7/7)
	<b>Battlecry:</b> Gain 8 Armor. This turn, your minions cost Armor instead of Mana. """
	#
	pass

	Lich_Druid+=['RLK_659e']
class RLK_659e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_659e:# <2>[1776]
	""" Hardened Carapace (0)
	Your minions cost Armor instead of Mana this turn. """
	#
	pass

if Lich_Nerubian_Flyer:# 
	Lich_Druid+=['RLK_956']
class RLK_956_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_956:# <2>[1776]
	""" Nerubian Flyer (minion:2/2/3)
	<b>Battlecry:</b> If a friendly Undead died after your last turn, summon a 2/2 Nerubian. """
	#
	pass

	Lich_Druid+=['RLK_956t']
class RLK_956t_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_956t:# <2>[1776]
	""" Nerubian Skitterer (minion:2/2/2)
	 """
	#
	pass

