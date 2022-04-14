from fireplace import cards
from fireplace.card import Card
#from fireplace.actions import *
from fireplace.player import Player
import random
from hearthstone.enums import Zone,State, CardClass
from fireplace.cards.battlegrounds import BG_hero1

class BG_Agent(object):
	""" バトルグラウンドのエージェントのクラス
	エージェントを作るときはこのクラスを継承してください。"""
	def __init__(self, myName: str, myFunction, myOption: list, myClass: CardClass, rating ,E = 0, heroChoiceStrategy=None, moveStrategy = None, choiceStrategy=None):
		self.name = myName
		self.func = myFunction
		self.option = myOption
		self.myClass = myClass
		self.rating = rating = 1500
		self.E = E 
		self.heroChoiceStrategy = heroChoiceStrategy
		self.moveStrategy = moveStrategy
		self.choiceStrategy = choiceStrategy
		self.tierupCost=5# -> player
		self.player = Player(myName, None, None)
		pass

	def __str__(self):
		return self.name

class BG_RandomAgent(BG_Agent):
	def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000 ):
		super().__init__(myName, myFunction, myOption, myClass, rating, \
			heroChoiceStrategy=self.RandomHeroChoice, \
			moveStrategy=self.RandomMoveChoice )
		pass
	def Random(self, game, option=[], gameLog=[], debugLog=False):
		player = thisgame.current_player
		loopCount=0
		while loopCount<20:
			loopCount+=1
			myCandidate = getBGCandidates(game)
			if len(myCandidate)>0:
				myChoice = random.choice(myCandidate)
				exc = executeAction(thisgame, myChoice, debugLog=debugLog)
				postAction(player)
				if exc==ExceptionPlay.GAMEOVER:
					return ExceptionPlay.GAMEOVER
				else:
					continue
			return ExceptionPlay.VALID
		pass

	def RandomHeroChoice(self, heroes):
		return random.choice(heroes)

	def RandomMoveChoice(self, bar, candidates, controller, bartender):
		return random.choice(candidates)

class BG_HumanAgent(BG_Agent):
	def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000 ):
		super().__init__(myName, myFunction, myOption, myClass, rating , \
			heroChoiceStrategy=self.HumanHeroChoice, \
			moveStrategy = self.HumanMoveChoice)
		pass
	def HumanInput(self, game, option=[], gameLog=[], debugLog=False):
		pass
	def HumanMoveChoice(self, bar, candidates, controller, bartender):
		self.printBar(bar, controller, bartender)
		count=0
		for move in candidates:
			self.printMove(count, move)
			count += 1
		while True:
			try :
				print("->",end='')
				inputNum = int(input())
				if inputNum>=0 and inputNum<len(candidates):
					return candidates[inputNum]
			except ValueError :
				pass
		pass
	def HumanHeroChoice(self, heroes):
		count=0
		for card in heroes:
			self.printHero(count, card)
			count += 1
		while True:
			try :
				print("->",end='')
				inputNum = int(input())
				if inputNum>=0 and inputNum<len(heroes):
					return heroes[inputNum]
			except ValueError :
				pass
	def printHero(self, count, cardID):
		card = cards.db[cardID]
		hpID=card.hero_power
		hp=cards.db[hpID]
		bdID=BG_hero1.BG_Hero1_Buddy[cardID]
		bd=cards.db[bdID]
		print("[%d] %s "%(count, card.name))
		print("HeroPower:%s"%(hp.description.replace('\n',' ')))
		print("Buddy:%s"%(bd.description.replace('\n',' ')))
		pass
	def printMove(self, count, move):
		print("[%d] %s"%(count, move))
		pass
	def printBar(self, bar, controller, bartender):
		print("----------------------------------------------")
		print("Tier[%d], TierUpCost[%d], ReroleCost[%d], Gold[%d/%d]"%(controller.Tier, controller.TierUpCost, bar.reroleCost, controller.mana, controller.max_mana ))
		print("----------------------------------------------")
		for card in bartender.field:
			if card.frozen:
				print("Bar   : %s (frozen)"%(card))
			else:
				print("Bar   : %s"%(card))
		print("----------------------------------------------")
		for card in controller.field:
			print("Field : %s"%(card))
		print("----------------------------------------------")
		for card in controller.hand:
			print("Hand  : %s"%(card))
		print("----------------------------------------------")
		pass

def DealCard(decks, bartender, grade):
	dk=[]
	for i in range(grade):
		dk += decks[i]
	cardID = random.choice(dk)
	card = bartender.card(cardID)
	gr = card.tech_level-1
	decks[gr].remove(cardID)
	return card

def ReturnCard(decks, card):
	gr = card.tech_level-1
	decks[gr].append(card.id)
	card.zone=Zone.GRAVEYARD
	#card.controller.field.remove(card)
	pass


