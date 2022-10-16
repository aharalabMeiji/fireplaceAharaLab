
from ..utils import *

StormWind_Shaman=[]

StormWind_Brilliant_Macaw=True  ###
StormWind_Suckerhook=True  ###
StormWind_Cookie_the_Cook=True  ###
StormWind_Auctionhouse_Gavel=True  ###
StormWind_Spirit_Alpha=True  ###
StormWind_Command_the_Elements=True  ###
StormWind_Granite_Forgeborn=True  ###
StormWind_Canal_Slogger=True  ###
StormWind_Tiny_Toys=True  ###
StormWind_Charged_Call=True  ###
StormWind_Investment_Opportunity=True  ###
StormWind_Overdraft=True  ###
StormWind_Bolner_Hammerbeak=True  ###

###################################################


if StormWind_Brilliant_Macaw:# 
	StormWind_Shaman+=['DED_509']
class DED_509:# <8>[1578]
	""" Brilliant Macaw
	[Battlecry:] Repeat the last [Battlecry] you played. """
	def play(self):
		actions=[action for action in self.controller._targetedaction_log if isinstance(action['class'], Battlecry) and action['source'].id!='DED_509']
		if len(actions)>0:
			card = actions[-1]["source"]
			if hasattr(card.data.scripts, 'play'):
				action = getattr(card.data.scripts, 'play')
				print(type(action))
				if isinstance(action, list) or isinstance(action, tuple):
					self.controller.game.queue_actions(self, action)
				else:
					action()
			elif hasattr(card, 'play'):
				card.play()
	pass




if StormWind_Suckerhook:# 
	StormWind_Shaman+=['DED_511']
class DED_511_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		cost = target.weapon.cost
		newweapon=RandomWeapon(cost=cost+1).evaluate(self)
		Destroy(target.weapon).trigger(self)
		Summon(target, newweapon).trigger(self)
		pass
class DED_511:# <8>[1578]
	""" Suckerhook
	At the end of your turn,transform your weapon into one that costs (1) more. """
	OWN_TURN_END.on(DED_511_Action(CONTROLLER))
	pass




if StormWind_Cookie_the_Cook:# 
	StormWind_Shaman+=['DED_522']
	StormWind_Shaman+=['DED_522t']
class DED_522:# <8>[1578]
	""" Cookie the Cook
	[Lifesteal][Deathrattle:] Equip a 2/3__Stirring Rod with [Lifesteal]._ """
	deathrattle = Summon(CONTROLLER, 'DED_522t') 
	pass
class DED_522t:# <8>[1578]
	""" Cookie's Stirring Rod
	[Lifesteal] """
	#
	pass




if StormWind_Auctionhouse_Gavel:# 
	StormWind_Shaman+=['SW_025']
	StormWind_Shaman+=['SW_025e']
class SW_025:# <8>[1578]
	""" Auctionhouse Gavel
	After your hero attacks,reduce the Cost of a[Battlecry] minion inyour hand by (1). """
	events = Attack(FRIENDLY_HERO).after(Buff(FRIENDLY_HAND + BATTLECRY, 'SW_025e'))
	pass
class SW_025e:# <8>[1578]
	""" Sold! 	Costs (1) less. """
	cost = lambda self,i: max(i-1, 0)
	pass




if StormWind_Spirit_Alpha:# 
	StormWind_Shaman+=['SW_026','EX1_tk11']
class SW_026:# <8>[1578]
	""" Spirit Alpha
	After you play a card with[Overload], summon a 2/3 Spirit Wolf(EX1_tk11) with [Taunt]. """
	events = Play(CONTROLLER, OVERLOADED).after(Summon(CONTROLLER, 'EX1_tk11'))
	pass
class EX1_tk11:
	pass



if StormWind_Command_the_Elements:# 
	StormWind_Shaman+=['SW_031']
	StormWind_Shaman+=['SW_031t']
	StormWind_Shaman+=['SW_031t2']
	StormWind_Shaman+=['SW_031t7']
	StormWind_Shaman+=['SW_031t7e']
	StormWind_Shaman+=['SW_031t8']
class SW_031:# <8>[1578]
	""" Command the Elements
	[Questline:] Play 3 cards with [Overload].[Reward:] Unlock your[Overloaded] Mana Crystals. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Play(CONTROLLER, FRIENDLY + OVERLOAD).on(SidequestCounter(SELF, 3, [SetAttr(CONTROLLER, 'overloaded', 0)]))	#
	pass

class SW_031t:# <8>[1578]
	""" Stir the Stones
	[Questline:] Play 3 cards with [Overload].[Reward:] Summon a 3/3 Elemental(SW_031t8) with [Taunt]. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Play(CONTROLLER, FRIENDLY + OVERLOAD).on(SidequestCounter(SELF, 3, [Summon(CONTROLLER, 'SW_031t8') ]))	#
	#
	pass

class SW_031t2:# <8>[1578]
	""" Tame the Flames
	[Questline:] Play 3 cards with [Overload].[Reward:] Stormcaller Bru'kan(SW_031t7). """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Play(CONTROLLER, FRIENDLY + OVERLOAD).on(SidequestCounter(SELF, 3, [Give(CONTROLLER, 'SW_031t7') ]))	#
	#
	pass
class SW_031t7:# <8>[1578]
	""" Stormcaller Bru'kan
	[Battlecry:] For the rest of the game, your spells cast twice. """
	play = SetAttr(CONTROLLER, 'spell_cast_twice', True)
	pass
class SW_031t7e:# <8>[1578]
	""" Stormcaller 	Spells cast twice. """
	pass
class SW_031t8:# <8>[1578]
	""" Living Earth
	[Taunt] """
	pass




if StormWind_Granite_Forgeborn:# 
	StormWind_Shaman+=['SW_032']
	StormWind_Shaman+=['SW_032e']
class SW_032:# <8>[1578]
	""" Granite Forgeborn
	[Battlecry:] Reduce the cost of Elementals in your hand and deck by (1). """
	play = Buff(FRIENDLY_HAND + ELEMENTAL, 'SW_032e'), Buff(FRIENDLY_DECK + ELEMENTAL, 'SW_032e')
	pass

class SW_032e:# <8>[1578]
	""" Forged
	Costs (1) less. """
	cost = lambda self , i: max(i-1,0)
	pass




if StormWind_Canal_Slogger:# 
	StormWind_Shaman+=['SW_033']
class SW_033:# <8>[1578]
	""" Canal Slogger
	[Rush], [Lifesteal][Overload:] (1) """
	#
	pass




if StormWind_Tiny_Toys:# 
	StormWind_Shaman+=['SW_034']
class SW_034:# <8>[1578]
	""" Tiny Toys
	Summon four random 5-Cost minions.Make them 2/2. """
	def play(self):
		for repeat in range(4):
			card = RandomMinion(cost=5).evaluate(self)
			if isinstance(card, list):
				card=card[0]
			if isinstance(card, list):
				card=card[0]
			Buff(card, 'SW_034e').trigger(self)
			Summon(self.controller, card).trigger(self)
	pass
SW_034e=buff(2,2)



if StormWind_Charged_Call:# 
	StormWind_Shaman+=['SW_035']
class SW_035:# <8>[1578]
	""" Charged Call
	[Discover] a @-Cost minion and summon it. <i>(Upgraded for each [Overload] card you played this game!)</i> """
	def play(self):
		cards=[card for card in self.controller.play_log if card.overload==True]
		amount = len(cards)+1
		GenericChoicePlay(self.controller, RandomMinion(cost = amount))
	pass




if StormWind_Investment_Opportunity:# 
	StormWind_Shaman+=['SW_095']
class SW_095:# <8>[1578]
	""" Investment Opportunity
	Draw an [Overload] card. """
	play = Give(CONTROLLER, FRIENDLY_DECK + OVERLOAD)
	pass




if StormWind_Overdraft:# 
	StormWind_Shaman+=['SW_114']
class SW_114:# <8>[1578]
	""" Overdraft
	[Tradeable]Unlock your [Overloaded] Mana Crystals to deal that much damage. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = Hit(TARGET, OVERLOADED(CONTROLLER)),	SetAttr(CONTROLLER, 'overloaded', 0)
	pass




if StormWind_Bolner_Hammerbeak:# 
	StormWind_Shaman+=['SW_115']
class SW_115_Action(TargetedAction):
	TARGET=ActionArg()#CONTROLLER
	def do(self, source, target):
		actions=[action for action in source.controller._targetedaction_log if isinstance(action['class'], Battlecry) and action['turn']==target.game.turn]
		if len(actions)>0:
			card = actions[0]['source']
			if hasattr(card.data.scripts, 'play'):
				action = card.get_actions('play')
				if isinstance(action, tuple) or isinstance(action, list):
					action = action[0]
				action.trigger(source)
			elif hasattr(card, 'play'):
				card.play()
		pass
class SW_115:# <8>[1578]
	""" Bolner Hammerbeak
	After you play a [Battlecry]minion, repeat the first__[Battlecry] played this turn._ """
	events = Play(CONTROLLER, BATTLECRY).after(SW_115_Action(CONTROLLER))
	pass



