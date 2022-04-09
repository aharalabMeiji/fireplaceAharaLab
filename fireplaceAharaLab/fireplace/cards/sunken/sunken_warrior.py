
from ..utils import *

#CardSet.THE_SUNKEN_CITY_CardClass.WARRIOR=['TSC_659','TSC_660','TSC_660e','TSC_660e2','TSC_660t','TSC_913','TSC_913t','TSC_917','TSC_917t','TSC_939','TSC_940','TSC_940e2','TSC_941','TSC_941t','TSC_942','TSC_942e','TSC_943','TSC_943e','TSC_944','TSC_944e',]
class TSC_659:# <10>[1658]
	""" Trenchstalker
	[Battlecry:] Attack three different random enemies. """
	def play(self):
		controller = self.controller
		opponent = controller.opponent
		op_characters = opponent.character#=[opponent.hero]+opponent.field
		targets = random.sample(op_characters, 3)
		if len(targets)>0:
			for target in targets:
				RegularAttack(self, target).trigger(controller)
		pass
	pass

class TSC_660_Choice(Choice):
	def choose(self, card):
		self.source._sidequest_counter_ += 1
		if self.source._sidequest_counter_>=3:
			self.next_choice=None
		else:
			self.next_choice=self
		super().choose(card)
		card.zone = Zone.SETASIDE
		Buff(card, 'TSC_660e').trigger(self.controller)
		self.source.sidequest_list0.append(card)
		cards = self._args[1]
		if isinstance(cards, LazyValue):
			self.cards = cards.evaluate(self.source)

class TSC_660:# <10>[1658]
	""" Nellie, the Great Thresher
	[Colossal +1][Battlecry:] [Discover] 3 Pirates to crew Nellie's Ship! """
	play = TSC_660_Choice(CONTROLLER, RandomMinion(race=Race.PIRATE)*3)
	pass

TSC_660e=buff(cost=SET(1))# <10>[1658]
""" Mercenary's Fee
Costs (1). """

class TSC_660e2:# <10>[1658]
	""" Pirate Crew
	Holding Nellie's Pirate Crew. """
	#
	pass

class TSC_660t_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		for card in source.owner.sidequest_list0:
			card.zone = Zone.HAND
		pass
class TSC_660t:# <10>[1658]
	""" Nellie's Pirate Ship
	[[Taunt].] [Deathrattle:] Add Nellie's Pirate crew to your hand. They cost (1). """
	deathrattle = TSC_660t_Action(CONTROLLER)
	pass

class TSC_913:# <10>[1658]
	""" Azsharan Trident
	[Deathrattle:] Put a 'Sunken Trident' on the_bottom of your deck. """
	deathrattle = PutOnBottom(CONTROLLER, 'TSC_913t')
	pass

class TSC_913t:# <10>[1658]
	""" Sunken Trident
	After your hero attacks, deal 2 damage to all enemy minions. """
	events = Attack(FRIENDLY_HERO).after(Hit(ENEMY_MINIONS, 2))
	pass

class TSC_917:# <10>[1658]
	""" Blackscale Brute
	[Taunt]. [Battlecry:] If youhave a weapon equipped, summon a 5/6 Naga with [Rush]. """
	play = Find(FRIENDLY_WEAPON) & Summon(CONTROLLER,'TSC_917t')
	pass

class TSC_917t:# <10>[1658]
	""" Firescale Berserker
	[Rush] """
	pass

class TSC_939:# <10>[1658]
	""" Forged in Flame
	Destroy your weapon, then draw cards equal to its Attack. """
	play = Draw(CONTROLLER) * ATK(FRIENDLY_WEAPON), Destroy(FRIENDLY_WEAPON)
	pass

class TSC_940:# <10>[1658]
	""" From the Depths (3)
	Reduce the Cost of the bottom five cards in your_deck by (3), then [Dredge]. """
	def play(self):
		controller = self.controller
		for i in range(5):
			Buff(controller.deck[i],'TSC_940e2').trigger(SELF)
		Dredge(CONTROLLER).trigger(SELF)
	pass

TSC_940e2=buff(cost=-3)# <10>[1658]
""" Current Events
Costs (3) less. """

class TSC_941:# <10>[1658]
	""" Guard the City (2)
	Gain 3 Armor.Summon a 2/3 Naga with [Taunt]. """
	play = GainArmor(FRIENDLY_HERO,3), Summon(CONTROLLER,'TSC_941t')
	pass

class TSC_941t:# <10>[1658]
	""" Naga Centaur
	[Taunt] """
	pass

class TSC_942_Action(Dredge):
	def choose(self, card):
		super().choose(card)
		if card.type == CardType.MINION or card.type == CardType.WEAPON:
			Buff(card,'TSC_942e').trigger(self.source)
		pass
class TSC_942:# <10>[1658]
	""" Obsidiansmith (2/3/2)
	[Battlecry:] [Dredge]. If it's a minion or a weapon,give it +1/+1. """
	play = TSC_942_Action(CONTROLLER)
	pass

TSC_942e=buff(1,1)# <10>[1658]
""" Flameforged
+1/+1. """

class TSC_943:# <10>[1658]
	""" Lady Ashvane (5/5/5)
	[Battlecry:] Give all weaponsin your hand, deck, and battlefield +1/+1. """
	play = Buff(FRIENDLY_HAND + WEAPON,'TSC_943e'), Buff(FRIENDLY_DECK + WEAPON,'TSC_943e'), Buff(FRIENDLY_WEAPON,'TSC_943e'),
	pass
TSC_943e=buff(1,1)# <10>[1658]
""" Rigid Carapace
+1/+1. """

class TSC_944:# <10>[1658]
	""" The Fires of Zin-Azshari (2)
	Replace your deck with minions that cost (5) or more. They cost (5). """
	def play(self):
		controller = self.controller
		num = controller.deck
		collection = []
		for card in cards.db.keys():
			cls = cards.db[card]
			if not cls.collectible:
				continue
			if cls.type == CardType.HERO:				# Heroes are collectible...
				continue
			if cls.card_class and cls.card_class not in [card_class, CardClass.NEUTRAL]:
				continue
			collection.append(cls)
		deck = random.sample(collection, num)
		for card in controller.deck:
			card.zone = Zone.GRAVEYARD
		for card in deck:
			card.zone = Zone.DECK
			Buff(card, 'TSC_944e').trigger(self.source)
	pass
TSC_944e=buff(cost=SET(5))# <10>[1658]
""" The Fiery Deep
Costs (5). """

