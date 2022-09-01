from ..utils import *

Alterac_Rogue=[]

Alterac_Coldtooth_Yeti=True
Alterac_Shadowcrafter_Scabbs=True
Alterac_Wildpaw_Gnoll=True
Alterac_Snowfall_Graveyard=True
Alterac_The_Lobotomizer=True
Alterac_Cerathine_Fleetrunner=True
Alterac_Contraband_Stash=True
Alterac_Forsaken_Lieutenant=True
Alterac_Reconnaissance=True
Alterac_Double_Agent=True
Alterac_SI7_Smuggler=True
Alterac_Smokescreen=True
Alterac_Tooth_of_Nefarian=True


if Alterac_Coldtooth_Yeti:# 
	Alterac_Rogue+=['AV_201']
	Alterac_Rogue+=['AV_201e']
class AV_201:# <7>[1626]
	""" Coldtooth Yeti
	[Combo:] Gain +3 Attack. """
	combo = Buff(SELF, 'AV_201e')
	pass
AV_201e=buff(3,0)

if Alterac_Shadowcrafter_Scabbs:# 
	Alterac_Rogue+=['AV_203']
	Alterac_Rogue+=['AV_203p']
	Alterac_Rogue+=['AV_203pe']
	Alterac_Rogue+=['AV_203po']
	Alterac_Rogue+=['AV_203t']
class AV_203:# <7>[1626]
	""" Shadowcrafter Scabbs (Hero)
	[Battlecry:] Return all minions to their owner's  hands. Summon two 4/2 Shadows(AV_203t) with [Stealth]. """
	def play(self):
		for card in self.controller.field:
			Bounce(card).trigger(self)
		for card in self.controller.opponent.field:
			Bounce(card).trigger(self)
		Summon(self.controller, 'AV_203t').trigger(self)
		Summon(self.controller, 'AV_203t').trigger(self)
	pass
class AV_203p:# <7>[1626]
	""" Sleight of Hand
	[Hero Power] The next card you play this turn costs (2) less. """
	activate = Buff(FRIENDLY_HAND, 'AV_203pe')
	pass
class AV_203pe:# <7>[1626]
	""" Sleight of Hand
	The next card you play this turn costs (2) less. """
	cost = lambda self, i: max(i-2,0)
	events =[
		Play(CONTROLLER).after(Destroy(SELF)),
		OWN_TURN_END.on(Destroy(SELF))
		]
	pass
class AV_203po:# <7>[1626]
	""" Sleight of Hand
	The next card you play this turn costs (2) less. """
	#
	pass
class AV_203t:# <7>[1626]
	""" Shadow
	[Stealth] """
	#
	pass

if Alterac_Wildpaw_Gnoll:# 
	Alterac_Rogue+=['AV_298']
class AV_298_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = target
		source.cost_mod = -len( [card for card in controller.give_log if card.card_class in CARDCLASSES.remove(CardClass.ROGUE)])
		pass
class AV_298:# <7>[1626]
	""" Wildpaw Gnoll
	[Rush] Costs (1) less for each card you've added to your hand _from another class. """
	class Hand:
		events = [
			Give(CONTROLLER).on(AV_298_Action(CONTROLLER)),
			Draw(CONTROLLER).on(AV_298_Action(CONTROLLER))
			]
	pass

if Alterac_Snowfall_Graveyard:# 
	Alterac_Rogue+=['AV_400']
	Alterac_Rogue+=['AV_400e']
class AV_400:# <7>[1626]
	""" Snowfall Graveyard
	Your [Deathrattles] trigger twice. Lasts 3 turns. """
	#see barron(FP1_031)
	play = Buff(CONTROLLER, 'AV_400e')
	pass
class AV_400e:# <7>[1626]
	""" Bunkered Up
	Deathrattles trigger twice. """
	update = Refresh(CONTROLLER, {GameTag.EXTRA_DEATHRATTLES: True})	
	events = OWN_TURN_END.on(SidequestCounter(SELF, 3, [Destroy(SELF)]))
	pass

if Alterac_The_Lobotomizer:# 
	Alterac_Rogue+=['AV_402']
class AV_402_Give(TargetedAction):
	TARGET=ActionArg()
	CARDS=CardArg()
	def do(self, source, target, cards):
		card = cards[0]
		Give(target, card.id).trigger(source)
		pass
class AV_402:# <7>[1626]
	""" The Lobotomizer
	[Honorable Kill:] Get a copy of the top card of your opponent's deck. """
	honorable_kill = AV_402_Give(CONTROLLER, FRIENDLY_DECK)
	pass

if Alterac_Cerathine_Fleetrunner:# 
	Alterac_Rogue+=['AV_403']
	Alterac_Rogue+=['AV_403e2']
class AV_403:# <7>[1626]
	""" Cera'thine Fleetrunner
	[Battlecry:] Replace your minions in hand and deck  with ones from other classes. They cost (2) less. """
	def play(self):
		for repeat in range(self.controller.hand):
			self.controller.hand[0].discard()
			newcard=Give(self.controller, RandomCollectible(card_class=CLASSES_EXCEPT_ROGUE)).trigger(self)
			Buff(newcard[0][0],'AV_403e2').trigger(self)
		for repeat in range(self.controller.deck):
			self.controller.hand[0].discard()
			newcard=ShuffleTop(self.controller, RandomCollectible(card_class=CLASSES_EXCEPT_ROGUE)).trigger(self)
			Buff(newcard[0],'AV_403e2').trigger(self)
	pass
class AV_403e2:# <7>[1626]
	""" Quickfooted
	Costs (2) less. """
	cost = lambda self, i: max(i-2,0)
	pass

if Alterac_Contraband_Stash:# 
	Alterac_Rogue+=['AV_405']
class AV_405:# <7>[1626]
	""" Contraband Stash
	Replay 5 cards from other classes you've played this game. """
	#Replay = give to hand. (and play? to whom?)
	def play(self):
		cards=[card for card in self.controller.play_log if card.card_class in CLASSES_EXCEPT_ROGUE]
		if len(cards)>5:
			cards = cards.random.sample(cards, 5)
		for card in cards:
			Give(self.controller, card.id).trigger(self)
	pass

if Alterac_Forsaken_Lieutenant:# 
	Alterac_Rogue+=['AV_601']
	Alterac_Rogue+=['AV_601e']
class AV_601:# <7>[1626]
	""" Forsaken Lieutenant
	[[Stealth].] After you play a [Deathrattle] minion, become a 2/2 copy of it with [Rush]. """
	events = Play(CONTROLLER, MINION+DEATHRATTLE).after(Morph(SELF, Play.CARD).after(Buff(Morph.CARD,'AV_601e')))
	pass
class AV_601e:
	atk = lambda self,i:2
	max_health=lambda self,i:2
	tags={GameTag.RUSH:True, }

if Alterac_Reconnaissance:# 
	Alterac_Rogue+=['AV_710']
	Alterac_Rogue+=['AV_710e']
class AV_710_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		card.zone=Zone.HAND
		Buff(card, 'AV_710e').trigger(card.controller)
class AV_710:# <7>[1626]
	""" Reconnaissance
	[Discover] a [Deathrattle] minion from another class. It costs (2) less. """
	play = AV_710_Choice(CONTROLLER, RandomDeathrattle(card_class=CLASSES_EXCEPT_ROGUE))
	pass
class AV_710e:# <7>[1626]
	""" Contracted	Costs (2) less. """
	cost = lambda self, i: max(i-2,0)
	pass

if Alterac_Double_Agent:# 
	Alterac_Rogue+=['AV_711']
class AV_711:# <7>[1626]
	""" Double Agent
	[Battlecry:] If you're holding a card from another class, _summon a copy of this. """
	def play(self):
		cards = [card for card in self.controller.hand if card.card_class in CLASSES_EXCEPT_ROGUE] 
		if len(cards)>0:
			card = random.choice(cards)
			Summon(self.controller, card.id).trigger(self)
	pass

if Alterac_SI7_Smuggler:# 
	Alterac_Rogue+=['ONY_030']
class ONY_030:# <7>[1626]
	""" SI:7 Smuggler
	[Battlecry:] Summon a random @-Cost minion. <i>(Upgraded for each other SI:7 card you _have played this game.)</i> """
	def play(self):
		cards = [card for card in self.controller.play_log if card.SI7_minion==True]
		amount =len(cards)+1
		Summon(self.controller, RandomMinion(cost=amount)).trigger(self)
	pass

if Alterac_Smokescreen:# 
	Alterac_Rogue+=['ONY_031']
class ONY_031:# <7>[1626]
	""" Smokescreen
	Draw 5 cards. Trigger any [Deathrattles] drawn. """
	def play(self):
		for repeat in range(5):
			newcard=Draw(CONTROLLER).trigger(self)
			newcard=newcard[0][0]
			if newcard.deathrattles!=[]:
				if isinstance(newcard.deathrattles[0], tuple):
					for action in newcard.deathrattles[0]:
						action.trigger(self)
				else: 
					for action in newcard.deathrattles:
						action.trigger(self)
	pass

if Alterac_Tooth_of_Nefarian:# 
	Alterac_Rogue+=['ONY_032']
class ONY_032:# <7>[1626]
	""" Tooth of Nefarian
	Deal $3 damage. [Honorable Kill:] [Discover] a spell from another class. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = Hit(TARGET, 3)#
	honorable_kill = Discover(CONTROLLER, RandomSpell(card_class=CLASSES_EXCEPT_ROGUE))
	pass


