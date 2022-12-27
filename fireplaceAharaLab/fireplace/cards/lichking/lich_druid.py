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
	Lich_Druid+=['RLK_650t']
	Lich_Druid+=['RLK_650t2']
class RLK_650:# <2>[1776]
	""" Lingering Zombie (minion:1/1/1)
	<b>Deathrattle:</b> Summon a 1/1 Disarmed Zombie with "<b>Deathrattle:</b> Summon a 1/1 Zombie." """
	deathrattle = Summon(CONTROLLER, 'RLK_650t')
	pass
class RLK_650t:# <2>[1776]
	""" Disarmed Zombie (minion:1/1/1)
	<b>Deathrattle:</b> Summon a 1/1 Zombie. """
	deathrattle = Summon(CONTROLLER, 'RLK_650t2')
	pass
class RLK_650t2:# <2>[1776]
	""" Unarmed Zombie (minion:1/1/1)
	 """
	pass

if Lich_Crypt_Keeper:# 
	Lich_Druid+=['RLK_651']
class RLK_651:# <2>[1776]
	""" Crypt Keeper (minion:8/4/6)
	<b>Taunt</b>. Costs (1) less for each Armor you have. """
	cost_mod = - ARMOR(FRIENDLY_HERO)
	pass

if Lich_Unending_Swarm:# 
	Lich_Druid+=['RLK_652']
class RLK_652_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		cards = [card.id for card in controller.death_log if card.type==CardType.MINION and card.cost<=2]
		for cardID in cards:
			Summon(controller, cardID).trigger(source)
		pass
class RLK_652:# <2>[1776]
	""" Unending Swarm (spell:6)
	Resurrect all friendly minions that cost (2) or less. """
	play = RLK_652_Action()
	pass

if Lich_Beetlemancy:# 
	Lich_Druid+=['RLK_654']
	Lich_Druid+=['RLK_654a']
	Lich_Druid+=['RLK_654b']
	Lich_Druid+=['RLK_654t']
class RLK_654:# <2>[1776]
	""" Beetlemancy (spell:5)
	<b>Choose One</b> - Gain 12 Armor; or Summon two 3/3 Beetles with <b>Taunt</b>. """
	choose=('RLK_654a','RLK_654b')
	play = ChooseBoth(CONTROLLER) & (GainArmor(FRIENDLY_HERO, 12),Summon(CONTROLLER, 'RLK_654t'), Summon(CONTROLLER, 'RLK_654t'))
	pass
class RLK_654a:# <2>[1776]
	""" Beetle Juice (spell:5)
	Gain 12 Armor. """
	play = GainArmor(FRIENDLY_HERO, 12)
	pass
class RLK_654b:# <2>[1776]
	""" Bug Snacks (spell:5)
	Summon two 3/3 Beetles with <b>Taunt</b>. """
	play = Summon(CONTROLLER, 'RLK_654t'), Summon(CONTROLLER, 'RLK_654t')#
	pass
class RLK_654t:# <2>[1776]
	""" Beetle (minion:3/3/3)
	<b>Taunt</b> """
	pass

if Lich_Wither:# 
	Lich_Druid+=['RLK_655']
	Lich_Druid+=['RLK_655e']
	Lich_Druid+=['RLK_655e2']
class RLK_655_Action(TargetedAction):# 
	def do(self, source, target):# 
		controller=source.controller
		cards=[card for card in controller.field if card.MINION_RACE(Race.UNDEAD)]
		amount=len(cards)
		if amount:
			for card in cards:
				Buff(card, 'RLK_655e2', atk=1, max_health=1).trigger(source)
			if target.health<=amount:
				Destroy(target)
			else:
				Buff(target, 'RLK_655e', atk=-min(target.atk, amount), max_health=-amount)
		pass
class RLK_655:# <2>[1776]
	""" Wither (spell:2)
	Choose a minion. Each friendly Undead steals 1 Attack and Health from it. """
	requirements = REQUIRE_ENEMY_MINION_TARGET
	play = RLK_655_Action(TARGET)
	pass
class RLK_655e:# <2>[1776]
	""" Withered (0)
	Reduced stats. """
	#
	pass
RLK_655e2=buff(1,1)



if Lich_Chitinous_Plating:# 
	Lich_Druid+=['RLK_656']
	Lich_Druid+=['RLK_656e']
class RLK_656:# <2>[1776]
	""" Chitinous Plating (spell:2)
	Gain 4 Armor. At the start of your next turn, gain 4 more. """
	play = GainArmor(FRIENDLY_HERO, 4),Buff(CONTROLLER, 'RLK_656e')
	pass
class RLK_656e:# <2>[1776]
	""" Molting (0)
	Gain 4 Armor next turn. """
	events = OWN_TURN_BEGIN.on(GainArmor(FRIENDLY_HERO, 4), Destroy(SELF))
	pass

if Lich_Underking:# 
	Lich_Druid+=['RLK_657']
class RLK_657:# <2>[1776]
	""" Underking (minion:7/6/6)
	<b>Rush</b> <b>Battlecry and Deathrattle:</b> Gain 6 Armor. """
	play = GainArmor(FRIENDLY_HERO, 6)
	deathrattle = GainArmor(FRIENDLY_HERO, 6)
	pass

if Lich_Elder_Nadox:# 
	Lich_Druid+=['RLK_658']
	Lich_Druid+=['RLK_658e']
class RLK_658_Action(TargetedAction):# 
	def do(self, source, target):# 
		controller=source.controller
		newatk=target.atk
		newhth=target.max_health
		for card in controller.field:
			if card!=target:
				Buff(card, 'RLK_658e', atk=newatk, max_health=newhth).trigger(source)
		Destroy(target).trigger(source)
		pass
class RLK_658:# <2>[1776]
	""" Elder Nadox (minion:5/5/4)
	<b>Battlecry:</b> Destroy a friendly Undead. Your minions gain its Attack. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE:Race.UNDEAD}
	play = RLK_658_Action(TARGET)
	pass
class RLK_658e:# <2>[1776]
	""" Might of Nadox (0)
	Increased stats. """
	pass

if Lich_AnubRekhan:# 
	Lich_Druid+=['RLK_659']
	Lich_Druid+=['RLK_659e']
class RLK_659e_Action(TargetedAction):# 
	def do(self, source, target):# 
		target.card_costs_armor=False
		pass
class RLK_659:# <2>[1776]
	""" Anub'Rekhan (minion:8/7/7)
	<b>Battlecry:</b> Gain 8 Armor. This turn, your minions cost Armor instead of Mana. """
	play = GainArmor(FRIENDLY_HERO, 8), Buff(FRIENDLY_HAND - SELF, 'RLK_659e')
	pass
class RLK_659e:# <2>[1776]
	""" Hardened Carapace (0)
	Your minions cost Armor instead of Mana this turn. """
	tags = {GameTag.CARD_COSTS_ARMOR: 1}
	def apply(self, target):
		target.card_costs_armor=True
		pass
	class Hand:
		events = OWN_TURN_END.on(RLK_659e_Action(OWNER), Destroy(SELF))
	pass

if Lich_Nerubian_Flyer:# 
	Lich_Druid+=['RLK_956']
	Lich_Druid+=['RLK_956t']
class RLK_956_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		cards = [card for card in controller.death_after_last_turn if card.MINION_RACE(Race.UNDEAD)]
		if len(cards):
			Summon(controller, 'RLK_956t').trigger(source)
		pass
class RLK_956:# <2>[1776]
	""" Nerubian Flyer (minion:2/2/3)
	<b>Battlecry:</b> If a friendly Undead died after your last turn, summon a 2/2 Nerubian. """
	play = RLK_956_Action()
	pass
class RLK_956t:# <2>[1776]
	""" Nerubian Skitterer (minion:2/2/2)
	"""
	pass

