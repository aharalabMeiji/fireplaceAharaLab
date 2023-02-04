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
		self.next_choice=None
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
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0,PlayReq.REQ_MINION_TARGET:0,  }
	play = Hit(TARGET, 5), GainArmor(FRIENDLY_HERO, 5) 
	pass




if Sunken_Trenchstalker:# 
	Sunken_Warrior+=['TSC_659']
class TSC_659:# <10>[1658]
	""" Trenchstalker
	[Battlecry:] Attack three different random enemies. """
	def play(self):
		cards = [card for card in self.controller.opponent.characters]
		if len(cards)>3:
			cards=random.sample(cards, 3)
		for card in cards:
			RegularAttack(self, card).trigger(self)
		pass
	pass




if Sunken_Nellie_the_Great_Thresher:# 
	Sunken_Warrior+=['TSC_660']
	Sunken_Warrior+=['TSC_660e']
	Sunken_Warrior+=['TSC_660e2']
	Sunken_Warrior+=['TSC_660t']
class TSC_660_Choice(Choice):
	def choose(self, card):
		self.source.sidequest_counter += 1
		if self.source.sidequest_counter>=3:
			self.next_choice=None
		else:
			self.next_choice=self
		super().choose(card)
		Buff(card, 'TSC_660e').trigger(self.source)
		self.option.sidequest_list0.append(card)#self.option=ship!
		cards = self._args[1]
		if isinstance(cards, LazyValue):
			self.cards = cards.evaluate(self.source)

class TSC_660:# <10>[1658]
	""" Nellie, the Great Thresher
	[Colossal +1][Battlecry:] [Discover] 3 Pirates to crew Nellie's Ship! """
	def play(self):
		ship=Summon(self.controller, 'TSC_660t').trigger(self)
		if ship[0]==[]:
			return
		ship=ship[0][0]
		TSC_660_Choice(self.controller, RandomPirate()*3, ship).trigger(self)
		pass		
TSC_660e=buff(cost=-2)
class TSC_660e2:# <10>[1658]
	pass
class TSC_660t_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=target
		cards=source.sidequest_list0
		for card in cards:
			card.zone=Zone.HAND
			# controller.hand.appen(card) ## no need
class TSC_660t:# <10>[1658]
	""" Nellie's Pirate Ship
	[[Taunt].] [Deathrattle:] Add Nellie's Pirate crew to your hand. They cost (1) less. """
	### 25.2.2 -
	### [[Taunt].] [Deathrattle:] Add Nellie's Pirate crew to your hand. They cost (2) less.
	deathrattle = TSC_660t_Action(CONTROLLER)
	pass




if Sunken_Azsharan_Trident:# 
	Sunken_Warrior+=['TSC_913']
	Sunken_Warrior+=['TSC_913t']
class TSC_913:# <10>[1658]
	""" Azsharan Trident
	[Deathrattle:] Put a 'Sunken Trident' on the_bottom of your deck. """
	deathrattle = ShuffleBottom(CONTROLLER, 'TSC_913t')
	pass
class TSC_913t:# <10>[1658]
	""" Sunken Trident
	After your hero attacks, deal 2 damage to all enemy minions. """
	events = Attack(FRIENDLY_HERO).after(Hit(ENEMY_MINIONS, 2))
	pass




if Sunken_Blackscale_Brute:# 
	Sunken_Warrior+=['TSC_917']
	Sunken_Warrior+=['TSC_917t']
class TSC_917:# <10>[1658]
	""" Blackscale Brute
	[Taunt]. [Battlecry:] If you have a weapon equipped, summon a 5/6 Naga with [Rush]. """
	play = Find(FRIENDLY_WEAPON) & Summon(CONTROLLER, 'TSC_917t')
class TSC_917t:# <10>[1658]
	""" Firescale Berserker
	[Rush] """
	pass




if Sunken_Forged_in_Flame:# 
	Sunken_Warrior+=['TSC_939']
class TSC_939:# <10>[1658]
	""" Forged in Flame
	Destroy your weapon, then draw cards equal to its Attack. """
	play = Draw(CONTROLLER) * ATK(FRIENDLY_WEAPON), Destroy(FRIENDLY_WEAPON) 
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
	play = GainArmor(FRIENDLY_HERO,3), Summon(CONTROLLER, 'TSC_941t')
class TSC_941t:# <10>[1658]
	""" Naga Centaur
	[Taunt] """




if Sunken_Obsidiansmith:# 
	Sunken_Warrior+=['TSC_942']
	Sunken_Warrior+=['TSC_942e']
class TSC_942_DredgeChoice(Choice):
	def choose(self, card):
		self.next_choice=None
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
	[Battlecry:] Give all weapons in your hand, deck, and battlefield +1/+1. """
	play = Buff(FRIENDLY_WEAPON, 'TSC_943e'),Buff(FRIENDLY_HAND + WEAPON, 'TSC_943e'),Buff(FRIENDLY_DECK + WEAPON, 'TSC_943e')
TSC_943e=buff(1,1)




if Sunken_The_Fires_of_Zin_Azshari:# 
	Sunken_Warrior+=['TSC_944']
	Sunken_Warrior+=['TSC_944e']
class TSC_944:# <10>[1658]
	""" The Fires of Zin-Azshari
	Replace your deck with minions that cost (5) or more. They cost (5). """
	def play(self):
		repeat = len(self.controller.deck)
		for i in range(repeat):
			self.controller.deck.remove(self.controller.deck[0])
			card = RandomMinion(cost=[5,6,7,8,9,10]).evaluate(self)
			card=card[0]
			Buff(card,'TSC_944e').trigger(self)
			card.zone=Zone.DECK## may need
	pass
class TSC_944e:
	cost=SET(5)# <10>[1658]

