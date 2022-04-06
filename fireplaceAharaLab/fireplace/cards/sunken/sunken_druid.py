
from ..utils import *

sunken_druid=['TSC_026','TSC_026t','TSC_650','TSC_650a','TSC_650d','TSC_650t','TSC_650t4','TSC_651','TSC_651e','TSC_652','TSC_653','TSC_654','TSC_656','TSC_656t','TSC_657','TSC_657e','TSC_658','TSC_927','TSC_927e','TSC_927t',]

class TSC_026:# <2>[1658]###############################
	""" Colaque
	[Colossal +1] [Immune] while you control Colaque's Shell. """
	play = Summon(CONTROLLER, 'TSC_026t')
	pass

class TSC_026t:# <2>[1658]
	""" Colaque's Shell
	[Taunt][Deathrattle:] Gain 8 Armor. """
	#
	pass

class TSC_650:# <2>[1658]
	""" Flipper Friends
	[Choose One] - Summon a 6/6 Orca with [Taunt]; or six 1/1 Otters with [Rush]. """
	choose = ('TSC_650a','TSC_650b')
	play = ChooseBoth(SELF) & (
		Summon(CONTROLLER, 'TSC_650t'), Summon(CONTROLLER, 'TSC_650t4')
	)
	pass

class TSC_650a:# <2>[1658]
	""" Order the Orca
	Summon a 6/6 Orca with [Taunt]. """
	play = Summon(CONTROLLER, 'TSC_650t')
	pass

class TSC_650d:# <2>[1658]
	""" Romp of Otters
	Summon six 1/1 Otters with [Rush]. """
	play = Summon(CONTROLLER, 'TSC_650t4')
	pass

class TSC_650t:# <2>[1658]
	""" Orca
	[Taunt] """
	#
	pass

class TSC_650t4:# <2>[1658]
	""" Otter
	[Rush] """
	#
	pass

class TSC_651:# <2>[1658]
	""" Seaweed Strike
	Deal $4 damage to a minion.If you played a Naga while holding this, also give yourhero +4 Attack this turn. """
	requirements={
		PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0,
		}
	play = Hit(TARGET, 4)
	class Hand:
		events = Play(CONTROLLER, FRIENDLY+NAGA).on(Buff(FRIENDLY_HERO,'TSC_651e'))
	pass

class TSC_651e:# <2>[1658]
	""" Explosive
	+4 Attack this turn. """
	#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>
	atk = lambda self, i: i+4
	pass

class TSC_652:# <2>[1658]
	""" Green-Thumb Gardener
	[Battlecry:] Refresh empty Mana Crystals equal to the Cost of the most expensive spell in your hand. """
	def play(self):
		controller = self.controller
		maxCost=-1
		for card in controller.hand:
			if card.type == CardType.SPELL:
				if card.cost>maxCost:
					maxCost = card.cost
		if maxCost>0:
			RefreshMana(controller, maxCost).trigger(source)
	pass

class TSC_653_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target, card):
		controller = target
		if card.controller != target:
			card.zone = Zone.SETASIDE
			card.controller = target
		card.atk += 2
		card.max_health += 2
		card.zone = Zone.DECK
		index = controller.deck.index(card)
		tmp = card## rolling
		for i in range(index):
			controller.deck[index-i]=controller.deck[index-1-i]
		controller.deck[0]=tmp
		pass

class TSC_653:# <2>[1658]
	""" Bottomfeeder
	[Deathrattle:] Add a Bottom feeder to the bottom of your deck with permanent +2/+2. """
	deathrattle = TSC_653_Action(CONTROLLER,'TSC_653')
	pass

class TSC_654_Action(Dredge):
	TARGET = ActionArg()
	def choose (self, card):
		super().choose(card)
		controller = target
		if controller.mana>= card.cost:
			Draw(controller, card).trigger(controller)

class TSC_654:# <2>[1658]
	""" Aquatic Form (cost=0)
	[Dredge]. If you have the Mana to play the card this turn, draw it. """
	play = TSC_654_Action(CONTROLLER)
	pass

class TSC_656_Action(TargetedAction):# <2>[1658]
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		card = Summon(controller, 'TSC_656t').trigger(controller)
		handsize = len(controller.hand)
		card = card[0][0]
		card.atk=handsize
		card.max_health=handsize
		pass
	pass

class TSC_656:# <2>[1658]
	""" Miracle Growth
	Draw 3 cards.Summon a Plant with [Taunt] and stats equal to your hand size. """
	play = Draw(CONTROLLER) * 3, TSC_656_Action(CONTROLLER)
	pass

class TSC_656t:# <2>[1658]
	""" Kelp Creeper
	[Taunt] """
	pass

class TSC_657:# <2>[1658]
	""" Dozing Kelpkeeper
	[Rush]. Starts [Dormant].After you've cast 5 Mana worth of spells, awaken. """
	dormant = -1
	events = OWN_SPELL_PLAY.on(SidequestManaCounter(SELF, Play.CARD, 5, [Awake(SELF)]))
	pass

class TSC_657e:# <2>[1658]
	""" Aquatic Slumber
	[Dormant]. Awaken after you cast @ Mana worth of spells. """
	pass

class TSC_658:# <2>[1658]
	""" Hedra the Heretic
	[Battlecry:] For each spellyou've cast while holdingthis, summon a minionof that spell's Cost. """
	class Hand:
		events = OWN_SPELL_PLAY.on(Summon(CONTROLLER, RandomMinion(cost=COST(Play.CARD))))
	pass

class TSC_927:# <2>[1658]
	""" Azsharan Gardens
	Give all minions in your hand +1/+1. Put a 'Sunken Gardens' on the bottom of your deck. """
	play = Buff(FRIENDLY_HAND, 'TSC_927e'), PutOnBottom(CONTROLLER, 'TSC_927t')
	pass

TSC_927e=buff(1,1)# <2>[1658]
""" Watered
+1/+1. """

class TSC_927t:# <2>[1658]
	""" Sunken Gardens
	Give +1/+1 to all minions in your hand, deck, and battlefield. """
	play = Buff(FRIENDLY_HAND, 'TSC_927e'), Buff(FRIENDLY_DECK, 'TSC_927e'), Buff(FRIENDLY_MINIONS, 'TSC_927e')
	pass

