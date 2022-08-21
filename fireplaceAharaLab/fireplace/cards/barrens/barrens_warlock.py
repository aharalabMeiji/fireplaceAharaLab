
from ..utils import *

Barrens_Warlock=[]

Barrens_Grimoire_of_Sacrifice=True  ###
Barrens_Soul_Rend=True  ###
Barrens_Apothecarys_Caravan=True  ###
Barrens_Altar_of_Fire=True  ###
Barrens_Imp_Swarm_Rank_1=True  ###
Barrens_Kabal_Outfitter=True  ###
Barrens_Blood_Shard_Bristleback=True  ###
Barrens_Barrens_Scavenger=True  ###
Barrens_Tamsin_Roame=True  ###
Barrens_Neeru_Fireblade=True  ###
Barrens_Unstable_Shadow_Blast=True  ###
Barrens_Final_Gasp=True  ###
Barrens_Stealer_of_Souls=True  ###


if Barrens_Grimoire_of_Sacrifice:# 
	Barrens_Warlock+=['BAR_910']
class BAR_910:# <9>[1525]
	""" Grimoire of Sacrifice
	Destroy a friendly minion. Deal $2 damage to all enemy minions. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	play = Destroy(TARGET), Hit(ENEMY_MINIONS, 2)
	pass




if Barrens_Soul_Rend:# 
	Barrens_Warlock+=['BAR_911']
class BAR_911:# <9>[1525]
	""" Soul Rend
	Deal $5 damage to allminions. Destroy a card inyour deck for each killed. """
	def play(self): 
		cardnum=0
		for card in self.controller.field+self.controller.opponent.field:
			amount = 5
			amount = self.get_damage(amount, card)	
			if amount>=card.health:
				cardnum+=1
		Hit(ALL_MINIONS, 5).trigger(self)
		for i in range(cardnum):
			card = random.choice(self.controller.deck)
			self.controller.deck.remove(card)
	pass




if Barrens_Apothecarys_Caravan:# 
	Barrens_Warlock+=['BAR_912']
class BAR_912_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		cards = [card for card in controller.deck if card.cost==1 and card.type==CardType.MINION]
		if len(cards)>0:
			card = random.choice(cards)
			Summon(controller, card).trigger(source)

class BAR_912:# <9>[1525]
	""" Apothecary's Caravan
	At the start of your turn,summon a 1-Cost minion from your deck. """
	events = OWN_TURN_BEGIN.on(BAR_912_Action(CONTROLLER))
	pass




if Barrens_Altar_of_Fire:# 
	Barrens_Warlock+=['BAR_913']
class BAR_913:# <9>[1525]
	""" Altar of Fire
	Destroy the top 3 cards of each deck. """
	def play(self):
		for i in range(3):
			Destroy(self.controller.deck[-1]).trigger(self)
			Destroy(self.controller.opponent.deck[-1]).trigger(self)
	pass




if Barrens_Imp_Swarm_Rank_1:# 
	Barrens_Warlock+=['BAR_914']
	Barrens_Warlock+=['BAR_914t']
	Barrens_Warlock+=['BAR_914t2']
	Barrens_Warlock+=['BAR_914t3']
class BAR_914:# <9>[1525]
	""" Imp Swarm Rank 1
	Summon a 3/2 Imp. <i>Upgrades when you have 5 Mana.</i> """
	class Hand:
		events = GradeupByMana(CONTROLLER, 5).on(Destroy(SELF),Give(CONTROLLER, 'BAR_914t'))	
	play = Summon(CONTROLLER, 'BAR_914t3')#
	pass
class BAR_914t:# <9>[1525]
	""" Imp Swarm Rank 2
	Summon two 3/2 Imps. <i>Upgrades when you have 10 Mana.</i> """
	class Hand:
		events = GradeupByMana(CONTROLLER, 10).on(Destroy(SELF),Give(CONTROLLER, 'BAR_914t2'))	
	play = Summon(CONTROLLER, 'BAR_914t3')*2#
	pass
class BAR_914t2:# <9>[1525]
	""" Imp Swarm Rank 3
	Summon three 3/2 Imps. """
	play = Summon(CONTROLLER, 'BAR_914t3')*3#
	pass
class BAR_914t3:# <9>[1525]
	""" Imp Familiar
	 """
	#
	pass




if Barrens_Kabal_Outfitter:# 
	Barrens_Warlock+=['BAR_915']
	Barrens_Warlock+=['BAR_915e']
class BAR_915:# <9>[1525]
	""" Kabal Outfitter
	[Battlecry and Deathrattle:]Give another random_friendly minion +1/+1. """
	play = Buff(FRIENDLY_MINIONS - SELF, 'BAR_915e')
	deathrattle = Buff(FRIENDLY_MINIONS - SELF, 'BAR_915e')
	pass
class BAR_915e:# <9>[1525]
	""" Outfitted 	+1/+1. """
	tags = {GameTag.ATK:1, GameTag.HEALTH:1, }
	pass




if Barrens_Blood_Shard_Bristleback:# 
	Barrens_Warlock+=['BAR_916']
class BAR_916:# <9>[1525]
	""" Blood Shard Bristleback
	[Lifesteal]. [Battlecry:] If yourdeck contains 10 or fewercards, deal 6 damageto a minion. """
	#
	pass




if Barrens_Barrens_Scavenger:# 
	Barrens_Warlock+=['BAR_917']
class BAR_917:# <9>[1525]
	""" Barrens Scavenger
	[Taunt]Costs 1 while your deckhas 10 or fewer cards. """
	#
	pass




if Barrens_Tamsin_Roame:# 
	Barrens_Warlock+=['BAR_918']
	Barrens_Warlock+=['BAR_918e']
class BAR_918:# <9>[1525]
	""" Tamsin Roame
	Whenever you cast a Shadowspell that costs 1 or more,add a copy to your handthat costs 0. """
	#
	pass
class BAR_918e:# <9>[1525]
	""" Gathered Shadows
	Costs 1. """
	#
	pass




if Barrens_Neeru_Fireblade:# 
	Barrens_Warlock+=['BAR_919']
	Barrens_Warlock+=['BAR_919t']
class BAR_919:# <9>[1525]
	""" Neeru Fireblade
	[Battlecry:] If your deck is empty, open a portal that fills your board with 3/2 Imps each turn. """
	#
	pass
class BAR_919t:# <9>[1525]
	""" Burning Blade Portal
	At the end of your turn,fill your board with 3/2 Imps. """
	#
	pass




if Barrens_Unstable_Shadow_Blast:# 
	Barrens_Warlock+=['WC_021']
class WC_021:# <9>[1525]
	""" Unstable Shadow Blast
	Deal $6 damage to aminion. Excess damage hits your hero. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	def play(self):
		target = self.target
		amount = 6
		amount = self.get_damage(amount, target)
		excess = amount - target.health
		Hit(self.target, 6).trigger(self)
		if excess>0:
			Hit(self.controller.hero, excess).trigger(self)
	#
	pass




if Barrens_Final_Gasp:# 
	Barrens_Warlock+=['WC_022']
class WC_022:# <9>[1525]
	""" Final Gasp
	Deal $1 damage to aminion. If it dies, summon a 2/2 Adventurer with a random bonus effect. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0 }	
	def plat(self):
		target = self.target
		amount=1
		amount = self.get_damage(amount, target)
		Hit(target, 1).trigger(self)
		if amount>1:
			SummonAdventurerWithBonus(CONTROLLER).trigger(self)
	pass




if Barrens_Stealer_of_Souls:# #### need check 
	Barrens_Warlock+=['WC_023','WC_023e']
class WC_023:# <9>[1525]
	""" Stealer of Souls
	After you draw a card, change its Cost to Health instead of Mana. """
	events = Draw(CONTROLLER).on(Buff(Draw.CARD, 'WC_023e'))
	pass
class WC_023e:
	"""
	Costs Health instead of Mana."""
	def apply(self,target):
		target.cards_cost_health=True
		pass
	tags = {9000: 1}#9000=GameTag.CARDS_COST_HEALTH
