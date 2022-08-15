from ..utils import *

Sunken_Warrior=[]


Sunken_Igneous_Lavagorger=True  ###
Sunken_Clash_of_the_Colossals=True  ###
Sunken_Tidal_Revenant=True  ###
Sunken_Trenchstalker=True  ###
Sunken_Nellie_the_Great_Thresher=True  ###
Sunken_Azsharan_Trident=True  ###
Sunken_Blackscale_Brute=True  ###
Sunken_Forged_in_Flame=True  ###
Sunken_From_the_Depths=True  ###
Sunken_Guard_the_City=True  ###
Sunken_Obsidiansmith=True  ###
Sunken_Lady_Ashvane=True  ###
Sunken_The_Fires_of_Zin_Azshari=True  ###


if Sunken_Igneous_Lavagorger:# 
	Sunken_Warrior+=['TID_714']
	#Sunken_Warrior+=['TID_714e']
class TID_714_DredgeChoice(Choice):
	def choose(self, card):
		super().choose(card)
		if Config.LOGINFO:
			print("(DredgeChoice.choose)%s chooses %r"%(card.controller.name, card))
		controller = card.controller
		for c in controller.deck[:3]:
			if card.id==c.id:
				controller.deck.remove(c)
				controller.deck.append(c)
				GainArmor(controller.hero, c.cost).trigger(controller)
				break
		pass
class TID_714_Dredge(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		bottom3ID=[card.id for card in target.deck[:3]]
		TID_714_DredgeChoice(target, RandomID(*bottom3ID)*3).trigger(source)
	pass
class TID_714:# <10>[1658]
	""" Igneous Lavagorger
	[Taunt] [Battlecry:] [Dredge]. Gain_Armor equal to its Cost. """
	play = TID_714_Dredge(CONTROLLER)
	pass
#class TID_714e:# <10>[1658]
#	""" Gorged	Increased attack. """
#	pass




if Sunken_Clash_of_the_Colossals:# 
	Sunken_Warrior+=['TID_715']
	Sunken_Warrior+=['TID_715e']
class TID_715:# <10>[1658]
	""" Clash of the Colossals
	Add a random [Colossal] minion to both players' hands. Yours costs (2) less. """
	play = Give(CONTROLLER, RandomMinion(colossal=True)).then(Buff(Give.CARD, 'TID_715e')),Give(OPPONENT, RandomMinion(colossal=True))
class TID_715e:# <10>[1658]
	""" Colossal Advantage
	Costs (2) less. """
	cost=lambda self, i: max(i-2,0)
	pass




if Sunken_Tidal_Revenant:# 
	Sunken_Warrior+=['TID_716']
class TID_716:# <10>[1658]
	""" Tidal Revenant
	[Battlecry:] Deal 5 damage. Gain 5 Armor. """
	#
	pass




if Sunken_Trenchstalker:# 
	Sunken_Warrior+=['TSC_659']
class TSC_659:# <10>[1658]
	""" Trenchstalker
	[Battlecry:] Attack three different random enemies. """
	#
	pass




if Sunken_Nellie_the_Great_Thresher:# 
	Sunken_Warrior+=['TSC_660']
	Sunken_Warrior+=['TSC_660e']
	Sunken_Warrior+=['TSC_660e2']
	Sunken_Warrior+=['TSC_660t']
class TSC_660_Choice(Choice):
	def choose(self, card):
		self.source._sidequest_counter_ += 1
		if self.source._sidequest_counter_>=3:
			self.next_choice=None
		else:
			self.next_choice=self
		super().choose(card)
		Buff(card, 'TSC_660e').trigger(self.source)
		self.source.sidequest_list0.append(card)
		cards = self._args[1]
		if isinstance(cards, LazyValue):
			self.cards = cards.evaluate(self.source)

class TSC_660:# <10>[1658]
	""" Nellie, the Great Thresher
	[Colossal +1][Battlecry:] [Discover] 3 Pirates to crew Nellie's Ship! """
	play = (
		Summon(CONTROLLER, 'TSC_660t'),
		TSC_660_Choice(CONTROLLER, RandomPirate()*3, ),
		)
TSC_660e=buff(cost=-1)
class TSC_660e2:# <10>[1658]
	pass

class TSC_660t:# <10>[1658]
	""" Nellie's Pirate Ship
	[[Taunt].] [Deathrattle:] AddNellie's Pirate crew to your hand. They cost (1) less. """
	#
	pass




if Sunken_Azsharan_Trident:# 
	Sunken_Warrior+=['TSC_913']
	Sunken_Warrior+=['TSC_913t']
class TSC_913:# <10>[1658]
	""" Azsharan Trident
	[Deathrattle:] Puta 'Sunken Trident' on the_bottom of your deck. """
	#
	pass
class TSC_913t:# <10>[1658]
	""" Sunken Trident
	After your hero attacks, deal 2 damage to all enemy minions. """
	#
	pass




if Sunken_Blackscale_Brute:# 
	Sunken_Warrior+=['TSC_917']
	Sunken_Warrior+=['TSC_917t']
class TSC_917:# <10>[1658]
	""" Blackscale Brute
	[Taunt]. [Battlecry:] If youhave a weapon equipped, summon a 5/6 Naga with [Rush]. """
	#

class TSC_917t:# <10>[1658]
	""" Firescale Berserker
	[Rush] """
	#
	pass




if Sunken_Forged_in_Flame:# 
	Sunken_Warrior+=['TSC_939']
class TSC_939:# <10>[1658]
	""" Forged in Flame
	Destroy your weapon, then draw cards equal to its Attack. """
	#
	pass




if Sunken_From_the_Depths:# 
	Sunken_Warrior+=['TSC_940']
	Sunken_Warrior+=['TSC_940e2']
class TSC_940_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = target
		for card in controller.deck[:5]:
			Buff(card, 'TSC_940e2').trigger(controller)
class TSC_940:# <10>[1658]
	""" From the Depths
	Reduce the Cost of thebottom five cards in your_deck by (3), then [Dredge]. """
	play = TSC_940_Action(CONTROLLER), Dredge(CONTROLLER)
	pass
TSC_940e2=buff(cost=-3)




if Sunken_Guard_the_City:# 
	Sunken_Warrior+=['TSC_941']
	Sunken_Warrior+=['TSC_941t']
class TSC_941:# <10>[1658]
	""" Guard the City
	Gain 3 Armor.Summon a 2/3 Naga with [Taunt]. """
	#

class TSC_941t:# <10>[1658]
	""" Naga Centaur
	[Taunt] """
	#
	pass




if Sunken_Obsidiansmith:# 
	Sunken_Warrior+=['TSC_942']
	Sunken_Warrior+=['TSC_942e']
class TSC_942_DredgeChoice(Choice):
	def choose(self, card):
		super().choose(card)
		if Config.LOGINFO:
			print("(DredgeChoice.choose)%s chooses %r"%(card.controller.name, card))
		controller = card.controller
		for c in controller.deck[:3]:
			if card.id==c.id:
				controller.deck.remove(c)
				controller.deck.append(c)
				if c.type==CardType.MINION or c.type==CardType.WEAPON:
					Buff(c, 'TSC_942e').trigger(controller)
				break
		pass

class TSC_942_Dredge(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		bottom3ID=[card.id for card in target.deck[:3]]
		TSC_942_DredgeChoice(target, RandomID(*bottom3ID)*3).trigger(source)
	pass
class TSC_942:# <10>[1658]
	""" Obsidiansmith
	[Battlecry:] [Dredge]. If it's a minion or a weapon, give it +1/+1. """
	play = TSC_942_Dredge(CONTROLLER)
	pass
TSC_942e=buff(1,1)




if Sunken_Lady_Ashvane:# 
	Sunken_Warrior+=['TSC_943']
	Sunken_Warrior+=['TSC_943e']
class TSC_943:# <10>[1658]
	""" Lady Ashvane
	[Battlecry:] Give all weaponsin your hand, deck, and battlefield +1/+1. """
	#

class TSC_943e:# <10>[1658]
	""" Rigid Carapace
	+1/+1. """
	#
	pass




if Sunken_The_Fires_of_Zin_Azshari:# 
	Sunken_Warrior+=['TSC_944']
	Sunken_Warrior+=['TSC_944e']
class TSC_944:# <10>[1658]
	""" The Fires of Zin-Azshari
	Replace your deck with minions that cost (5) or more. They cost (5). """
	#
	pass

class TSC_944e:# <10>[1658]
	""" The Fiery Deep
	Costs (5). """
	#
	pass

