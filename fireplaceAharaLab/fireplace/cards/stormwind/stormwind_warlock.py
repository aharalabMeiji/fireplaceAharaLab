
from ..utils import *

StormWind_Warlock=[]

StormWind_Shadowblade_Slinger=True  ###
StormWind_Wicked_Shipment=True  ###
StormWind_Hullbreaker=True  ###
StormWind_Runed_Mithril_Rod=True  ###
StormWind_Bloodbound_Imp=True  ###
StormWind_Dark_Alley_Pact=True  ###
StormWind_Shady_Bartender=True  ###
StormWind_Dreaded_Mount=True  ###
StormWind_Demonic_Assault=True  ###
StormWind_Entitled_Customer=True  ###
StormWind_Touch_of_the_Nathrezim=True  ###
StormWind_The_Demon_Seed=True  ###
StormWind_Anetheron=True  ###

######################################################


if StormWind_Shadowblade_Slinger:# 
	StormWind_Warlock+=['DED_503']
class DED_503:# <9>[1578]
	""" Shadowblade Slinger
	[Battlecry:] If you've taken damage this turn, deal that_much to an enemy minion. """
	def play(self):
		if self.controller.damage_amount_of_this_turn>0:
			Hit(RANDOM(ENEMY_MINIONS), self.controller.damage_amount_of_this_turn).trigger(self)
	pass




if StormWind_Wicked_Shipment:#  ### OK
	StormWind_Warlock+=['DED_504','EX1_598']
class DED_504_AddSidequestCounter(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount=1):
		if hasattr(target,'_sidequest_counter_'):
			target._sidequest_counter_ += amount
		pass
class DED_504:# <9>[1578]
	""" Wicked Shipment
	[Tradeable]Summon @ 1/1 |4(Imp, Imps)(EX1_598).<i>(Upgrades by 2when [Traded]!)</i> """
	#<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="2"/>
	def play(self):
		for i in range(self._sidequest_counter_+1):
			Summon(self.controller, 'EX1_598').trigger(self)
	class Hand:
		events = Trade(CONTROLLER).on(DED_504_AddSidequestCounter(SELF, 2))
	pass
class EX1_598:
	pass



if StormWind_Hullbreaker:# 
	StormWind_Warlock+=['DED_505']
class DED_505:# <9>[1578]
	""" Hullbreaker
	[Battlecry and Deathrattle:]Draw a spell. Your hero takes damage equal to its Cost. """
	play = Give(CONTROLLER, RANDOM(FRIENDLY_DECK + SPELL)).after(Hit(FRIENDLY_HERO, COST(Give.CARD)))
	pass




if StormWind_Runed_Mithril_Rod:# 
	StormWind_Warlock+=['SW_003','SW_003e']
class SW_003:# <9>[1578]
	""" Runed Mithril Rod
	After you draw 4 cards,reduce the Cost of cards in your hand by (1).Lose 1 Durability. """
	play = Draw(CONTROLLER) * 4, Buff(FRIENDLY_HAND, 'SW_003e'), Hit(FRIENDLY_WEAPON, 1)
	pass
class SW_003e:
	cost = lambda self, i: max(i-1,0)



if StormWind_Bloodbound_Imp:# 
	StormWind_Warlock+=['SW_084']
class SW_084:# <9>[1578]
	""" Bloodbound Imp
	Whenever this attacks, deal 2 damage to your_hero. """
	events = Attack(SELF).on(Hit(FRIENDLY_HERO, 2))
	pass




if StormWind_Dark_Alley_Pact:# 
	StormWind_Warlock+=['SW_085']
	StormWind_Warlock+=['SW_085t']
class SW_085:# <9>[1578]
	""" Dark Alley Pact
	Summon a Fiend with stats equal to your hand size. """
	def play(self):
		newcard = Summon(CONTROLLER, 'SW_085t').trigger(self)
		newcard = newcard[0][0]
		amount=len(self.controller.hand)
		newcard.atk=amount
		newcard.max_health=amount
	pass
class SW_085t:# <9>[1578]
	""" Fiend 	 """
	pass





if StormWind_Shady_Bartender:# 
	StormWind_Warlock+=['SW_086','SW_086e']
class SW_086:# <9>[1578]
	""" Shady Bartender
	[Tradeable][Battlecry:] Give your Demons +2/+2. """
	play = Buff(FRIENDLY_MINIONS + DEMON, 'SW_086e')
	pass
SW_086e=buff(2,2)



if StormWind_Dreaded_Mount:# 
	StormWind_Warlock+=['SW_087','SW_087e','SW_087e2']
	StormWind_Warlock+=['SW_087t']
class SW_087:# <9>[1578]
	""" Dreaded Mount
	Give a minion +1/+1.When it dies, summon an endless Dreadsteed. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }	#
	play = Buff(TARGET, 'SW_087e'), 
	pass

class SW_087t:# <9>[1578]
	""" Tamsin's Dreadsteed
	[Deathrattle:] At the end of the turn, summon Tamsin's Dreadsteed. """
	deathrattle = Buff(CONTROLLER, 'SW_087e2')
	pass
class SW_087e:
	tags = {
		GameTag.ATK:1,
		GameTag.HEALTH:1,
		GameTag.DEATHRATTLE:1	
		}
	deathrattle = Summon(CONTROLLER, SW_087t)
class SW_087e2:
	events = OWN_TURN_END.on(Summon(CONTROLLER, SW_087t))
	pass



if StormWind_Demonic_Assault:# 
	StormWind_Warlock+=['SW_088']
class SW_088:# <9>[1578]
	""" Demonic Assault
	Deal $3 damage.Summon two 1/3 Voidwalkers(CORE_CS2_065) with [Taunt]. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = Hit(TARGET, 3), Summon(CONTROLLER, 'CORE_CS2_065') * 2
	pass




if StormWind_Entitled_Customer:# 
	StormWind_Warlock+=['SW_089']
class SW_089:# <9>[1578]
	""" Entitled Customer
	[Battlecry:] Deal damage equal to your hand size to all other minions. """
	play = Hit(ALL_MINIONS - SELF, Count(FRIENDLY_HAND))
	pass




if StormWind_Touch_of_the_Nathrezim:# 
	StormWind_Warlock+=['SW_090']
class SW_090_Action(TargetedAction):
	TARGET=ActionArg()#CONTROLLER
	CARD=ActionArg()
	AMOUNT=IntArg()
	def do(self, source, target, card, amount):
		if card.health<=amount or card.to_be_destroyed:
			Heal(target.hero, 3).trigger(source)
		pass
class SW_090:# <9>[1578]
	""" Touch of the Nathrezim
	Deal $2 damage to a minion. If it dies, restore 3 Health to your hero. """
	play = Hit(TARGET, 2).after(SW_090_Action(CONTROLLER, Hit.TARGET, Hit.AMOUNT))
	pass



if StormWind_The_Demon_Seed:# 
	StormWind_Warlock+=['SW_091']
	StormWind_Warlock+=['SW_091t']
	StormWind_Warlock+=['SW_091t3']
	StormWind_Warlock+=['SW_091t4','SW_091t5']
class SidequestDamageCounter(TargetedAction):
	"""
	TARGET = ActionArg()# sidequest card
	CARD = ActionArg()# damage amount
	AMOUNT = IntArg() #max of mana
	TARGETACTION = ActionArg()# sidequest action
	"""
	TARGET = ActionArg()# sidequest card
	DAMAGE = IntArg()# damage
	AMOUNT = IntArg() # max
	ACTIONS = ActionArg()# sidequest action
	def do(self, source, target, damage, amount, actions):
		if source.controller==source.controller.game.current_player:
			if Config.LOGINFO:
				print("(SidequestDamageCounter.do)Setting Counter on %r is added by %d->%d, %d", target,	target._sidequest_counter_, (target._sidequest_counter_+damage), actions)
			target._sidequest_counter_ += damage
			if target._sidequest_counter_>= amount:
				#target._sidequest_counter_ -= amount
				if actions!=None:
					for action in actions:
						action.trigger(source)
				Destroy(source).trigger(source)
class SW_091:# <9>[1578]
	""" The Demon Seed
	[Questline:] Take 8 damage on your turns.[Reward:] [Lifesteal]. Deal $3damage to the enemy hero. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Damage(FRIENDLY_CHARACTERS).on(
		SidequestDamageCounter(SELF, Damage.AMOUNT, 8, [
			SetAttr(SELF, 'lifesteal', 1),
			Hit(ENEMY_HERO, 3),
			Summon(CONTROLLER, 'SW_091t')
			]))
	pass

class SW_091t:# <9>[1578]
	""" Establish the Link
	[Questline:] Take 8damage on your turns.[Reward:] [Lifesteal]. Deal $3damage to the enemy hero. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Damage(FRIENDLY_CHARACTERS).on(
		SidequestDamageCounter(SELF, Damage.AMOUNT, 8, [
			SetAttr(SELF, 'lifesteal', 1),
			Hit(ENEMY_HERO, 3),
			Summon(CONTROLLER, 'SW_091t3')
			]))
	pass

class SW_091t3:# <9>[1578]
	""" Complete the Ritual
	[Questline:] Take 8damage on your turns.[Reward:] BlightbornTamsin. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Damage(FRIENDLY_CHARACTERS).on(
		SidequestDamageCounter(SELF, Damage.AMOUNT, 8, [Give(CONTROLLER, 'SW_091t4') ]))
	pass

class SW_091t4:# <9>[1578]
	""" Blightborn Tamsin
	[Battlecry:] For the rest of the game, damage you take on your turn damages your__opponent instead. """
	play = Buff(CONTROLLER,'SW_091t5')
	pass
class SW_091t5:
	""" Blightborn (enchantment)
	For the rest of the game, damage you take on your turn instead damages your opponent."""

if StormWind_Anetheron:# 
	StormWind_Warlock+=['SW_092']
class SW_092:# <9>[1578]
	""" Anetheron
	Costs (1) if your hand is full. """
	powered_up = Count(FRIENDLY_HAND)==10
	update = powered_up & Refresh(SELF, {GameTag.COST:SET(1)})
	pass


