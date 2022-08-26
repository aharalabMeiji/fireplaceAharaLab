
from ..utils import *

StormWind_DemonHunter=[]


StormWind_Need_for_Greed=True###
StormWind_Crows_Nest_Lookout=True###
StormWind_Proving_Grounds=True###
StormWind_Irebound_Brute=True###
StormWind_Final_Showdown=True###
StormWind_Fel_Barrage=True###
StormWind_Sigil_of_Alacrity=True###
StormWind_Persistent_Peddler=True###
StormWind_Felgorger=True###
StormWind_Jace_Darkweaver=True###
StormWind_Metamorfin=True###
StormWind_Chaos_Leech=True###
StormWind_Lions_Frenzy=True###



if StormWind_Need_for_Greed:# 
	StormWind_DemonHunter+=['DED_506']
class DED_506:# <14>[1578] spell(5)
	""" Need for Greed
	[Tradeable]Draw 3 cards. If drawn this turn, this costs (3). """
	cost = lambda self, i : 3
	play = Draw(CONTROLLER) * 3
	events = OWN_TURN_END.on(SetCost(CONTROLLER, 5))
	pass

if StormWind_Crows_Nest_Lookout:# 
	StormWind_DemonHunter+=['DED_507']
class DED_507:# <14>[1578]
	""" Crow's Nest Lookout
	[Battlecry:] Deal 2 damage to the left and right-most enemy minions. """
	def play(self):
		leftmost = self.controller.opponent.field[0]
		rightmost = self.controller.opponent.field[-1]
		if leftmost!=rightmost:
			Hit(leftmost, 2).trigger(self)
		Hit(rightmost, 2).trigger(self)
	pass

if StormWind_Proving_Grounds:# 
	StormWind_DemonHunter+=['DED_508']
class DED_508:# <14>[1578]
	""" Proving Grounds
	Summon two minions from your deck.They fight! """
	def play(self):
		minions = [card for card in self.controller.deck if card.type==CardType.MINION]
		cards=random.sample(minions, 2)
		for card in cards:
			card.zone=Zone.PLAY
			card.rush=True
	pass



if StormWind_Irebound_Brute:# 
	StormWind_DemonHunter+=['SW_037','SW_037e']
class SW_037_Action1(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		while True:
			thisbuffs=[buff for buff in source.buffs if buff.id=='SW_037e']
			if thisbuffs!=[]:
				source.thisbuffs[-1].remove()
			else:
				break
class SW_037:# <14>[1578]
	""" Irebound Brute
	[Taunt]Costs (1) less for each card drawn this turn. """
	events =[
		OWN_TURN_BEGIN.on(SW_037_Action1(CONTROLLER)),
		Draw(CONTROLLER).on(Buff(SELF, 'SW_037e'))
		]
	pass
class SW_037e:# <14>[1578]
	""" Prepped to Strike Costs (1) less. """
	cost = lambda self, i: max(i-1,0)
	pass




if StormWind_Final_Showdown:# 
	StormWind_DemonHunter+=['SW_039']
	StormWind_DemonHunter+=['SW_039t']
	StormWind_DemonHunter+=['SW_039t2e']
	StormWind_DemonHunter+=['SW_039t3']
	StormWind_DemonHunter+=['SW_039t3_t','SW_039t3_te']
class SW_039_Action1(TargetedAction):
	TARGET=ActionArg()
	AMOUNT=IntArg()
	def do(self, source, target,amount):
		controller=target
		if controller.cards_drawn_this_turn==amount:
			for action in controller._targetedaction_log:
				if isinstance(action['class'],Draw) and action['turn']==controller.game.turn:
					card = action['target_args'][0]
					Buff(card, 'SW_039t2e').trigger(source)
class SW_039:# <14>[1578]
	""" Final Showdown
	[Questline:] Draw 4 cards in one turn. [Reward:] Reduce the Cost of the cards drawn by (1). """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Draw(CONTROLLER).on(SW_039_Action1(CONTROLLER,4 ), Summon(CONTROLLER,'SW_039t'),Destroy(SELF))
	#
	pass
class SW_039t:# <14>[1578]
	""" Gain Momentum
	[Questline:] Draw 5 cards in one turn. [Reward:] Reduce the Cost of the cards drawn by (1). """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Draw(CONTROLLER).on(SW_039_Action1(CONTROLLER, 5), Summon(CONTROLLER,'SW_039t3'),Destroy(SELF))
	pass

class SW_039t2e:# <14>[1578]
	""" Faster Moves Costs (1) less. """
	cost = lambda self, i: max(i-1,0)
	pass
class SW_039_Action2(TargetedAction):
	TARGET=ActionArg()
	AMOUNT=IntArg()
	def do(self, source, target,amount):
		controller=target
		if controller.cards_drawn_this_turn==amount:
			Give(CONTROLLER, 'SW_039t3_t').trigger(source)
class SW_039t3:# <14>[1578]
	""" Close the Portal
	[Questline:] Draw 5 cards in one turn.[Reward:] Demonslayer Kurtrus. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Draw(CONTROLLER).on(SW_039_Action2(CONTROLLER, 5),Destroy(SELF))
	pass
class SW_039t3_t:# <14>[1578]
	""" Demonslayer Kurtrus
	[Battlecry:] For the rest of the game, cards you draw cost (2) less. """
	#
	pass
class SW_039t3_te:
	cost = lambda self, i: max(i-2,0)
	pass





if StormWind_Fel_Barrage:# 
	StormWind_DemonHunter+=['SW_040']
class SW_040:# <14>[1578]
	""" Fel Barrage
	Deal $2 damage to the lowest Health enemy, twice. """
	def play(self):
		for repeat in range(2):
			lowest=[]
			for card in self.controller.opponent.field:
				if lowest==[] or lowest[0].health > card.health:
					lowest=[card]
				elif lowest[0].health == card.health:
					lowest.append(card)
			if lowest!=[]:
				Hit(random.choice(lowest), 2).trigger(self)
	pass




if StormWind_Sigil_of_Alacrity:# 
	StormWind_DemonHunter+=['SW_041']
class SW_041:# <14>[1578]
	""" Sigil of Alacrity
	At the start of your next turn, draw a card and_reduce its Cost by (1). """
	events = OWN_TURN_BEGIN.on(Draw(CONTROLLER).after(Buff(Draw.CARD,'SW_041e2')))
	pass

class SW_041e2:# <14>[1578]
	""" Light as a Feather 	Costs (1) less. """
	cost = lambda self, i: max(i-1,0)	
	pass




if StormWind_Persistent_Peddler:# 
	StormWind_DemonHunter+=['SW_042']
class SW_042:# <14>[1578]
	""" Persistent Peddler
	[Tradeable][Deathrattle:] Summon a Persistent Peddler(SW_042) from your deck. """
	deathrattle = Summon(CONTROLLER, RANDOM(FRIENDLY_DECK + ID('SW_042')))
	pass




if StormWind_Felgorger:# 
	StormWind_DemonHunter+=['SW_043']
class SW_043:# <14>[1578]
	""" Felgorger
	[Battlecry:] Draw a Fel spell. Reduce its Cost by (2). """
	play = Give(CONTROLLER, RANDOM(FRIENDLY_DECK + FEL)).on(Buff(Give.CARD,'SW_043e'))
	pass
class SW_043e:
	cost=lambda self, i: max(i-2,0)



if StormWind_Jace_Darkweaver:# 
	StormWind_DemonHunter+=['SW_044']
class SW_044:# <14>[1578]
	""" Jace Darkweaver
	[Battlecry:] Cast all Fel spells you've played this game <i>(targets enemies if possible)</i>. """
	def play(self):
		actions=[action for action in self.controller._targetedaction_log if isinstance(action['class'], Play) and action['source'].type==CardType.SPELL and action['source'].spell_school==SpellSchool.FEL ]
		for action in actions:
			newcard = self.controller.card(action['source'].id)
			if newcard.targets!=[]:
				newcard.target=random.choice(newcard.targets)
				Battlecry(newcard, newcard.target).trigger(self)
			else:
				newcard.target=None
				Battlecry(newcard, None).trigger(self)

	pass




if StormWind_Metamorfin:# 
	StormWind_DemonHunter+=['SW_451']
	StormWind_DemonHunter+=['SW_451e']
class SW_451:# <14>[1578]
	""" Metamorfin
	[Taunt][Battlecry:] If you've cast a Fel spell this turn, gain +2/+2. """
	def play(self):
		actions=[action for action in self.controller._targetedaction_log if isinstance(action['class'], Play) and action['source'].type==CardType.SPELL and action['source'].spell_school==SpellSchool.FEL and action['turn']==self.controller.game.turn]
		if len(actions)>0:
			Buff(self, 'SW_451e').trigger(self)
	pass
SW_451e=buff(2,2)




if StormWind_Chaos_Leech:# 
	StormWind_DemonHunter+=['SW_452']
class SW_452:# <14>[1578]
	""" Chaos Leech
	[Lifesteal]. Deal $3 damage to a minion.[Outcast:] Deal $5 instead. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = Hit(TARGET, 3)
	outcast = Hit(TARGET, 5)
	
	pass




if StormWind_Lions_Frenzy:# 
	StormWind_DemonHunter+=['SW_454']
class SW_454_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		actions=[action for action in self.controller._targetedaction_log if isinstance(action['class'], Draw) and action['turn']==self.controller.game.turn]
		source.atk = len(actions)
class SW_454:# <14>[1578] weapon (3/0/2)
	""" Lion's Frenzy
	Has Attack equal to the number of cards you've drawn this turn. """
	events = [
		Draw(CONTROLLER).on(SW_454_Action(CONTROLLER)),
		OWN_TURN_BEGIN.on(SW_454_Action(CONTROLLER))
	]
	pass


##############################################################################
