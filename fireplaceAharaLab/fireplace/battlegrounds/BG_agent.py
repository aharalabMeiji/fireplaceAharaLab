from fireplace import cards
from fireplace.card import Card
from fireplace.player import Player
from fireplace.cards.battlegrounds import BG_hero1
import random
from hearthstone.enums import Zone,State, CardClass, CardType
from .BG_enums import MovePlay

class BG_Agent(object):
	""" バトルグラウンドのエージェントのクラス
	エージェントを作るときはこのクラスを継承してください。"""
	def __init__(self, myName: str, myOption: list, rating ,E = 0, heroChoiceStrategy=None, moveStrategy = None, choiceStrategy=None):
		self.name = myName
		self.option = myOption
		self.rating = rating = 1000
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
	def __init__(self, myName: str, myOption = [], rating =1000 ):
		super().__init__(myName, myOption, rating, \
			heroChoiceStrategy=self.RandomHeroChoice, \
			moveStrategy=self.RandomMoveChoice )
		pass
	
	def RandomHeroChoice(self, heroes):
		return random.choice(heroes)

	def RandomMoveChoice(self, bar, candidates, controller, bartender):
		return random.choice(candidates)

class BG_NecoAgent(BG_Agent):
	def __init__(self, myName, myOption = [], rating =1000 ):
		super().__init__(myName, myOption, rating, \
			heroChoiceStrategy=self.NecoHeroChoice, \
			moveStrategy=self.NecoMoveChoice,
			choiceStrategy=self.NecoDiscoveryChoice)
		pass
	def NecoMoveChoice(self, bar, candidates, controller, bartender):
		myCandidate = candidates
		if len(myCandidate)>0:
			choices=[]
			for move in myCandidate:
				if move.move==MovePlay.BUY:
					choices.append(move)
			if len(choices)>0:
				myChoice = random.choice(choices)
			else:
				choices=[]
				for move in myCandidate:
					if move.move==MovePlay.PLAY:
						choices.append(move)
				if len(choices)>0:
					myChoice = random.choice(choices)
				else:
					myChoice = random.choice(myCandidate)
			return myChoice
		return None

	def NecoHeroChoice(self, heroes):
		return random.choice(heroes)
	def NecoDiscoveryChoice(self, choices):
		return random.choice(choices)


class BG_HumanAgent(BG_Agent):
	def __init__(self, myName, myOption = [], rating =1000 ):
		super().__init__(myName, myOption, rating, \
			heroChoiceStrategy=self.HumanHeroChoice, \
			moveStrategy = self.HumanMoveChoice,
			choiceStrategy = self.HumanDiscoveryChoice	   )
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
		print("グレード[%d], グレードアップコスト[%d], リロールコスト[%d], ゴールド[%d/%d] ターン[%d]"%(controller.Tier, controller.TierUpCost, bar.reroleCost, controller.mana, controller.max_mana, bar.turn))
		buddy = controller.buddy_gauge
		if buddy>100:
			buddy = (buddy-100)*0.5
		print("%s(%d + %d), buddy : %d"%(controller.hero, controller.hero.health, controller.hero.armor, buddy))
		print("----------------------------------------------")
		for card in bartender.field:
			print("Bar   :%s" %(self.card_stats(card)))
		print("----------------------------------------------")
		for card in controller.field:
			print("Field : %s"%(self.card_stats(card)))
		print("----------------------------------------------")
		for card in controller.hand:
			print("Hand  : %s"%(self.card_stats(card)))
		print("----------------------------------------------")
		pass
	def HumanDiscoveryChoice(self, choices):
		return random.choice(choices)
		pass
	pass

	def card_stats(self, card):
		ret = ' %s'%(card)
		if card.type != CardType.MINION:
			return ret
		ret += '(%d/%d)'%(card.atk,card.health)
		if card.cant_play:
			ret += "(can't play)"
		if card.frozen:
			ret += "(frozen)"
		if card.taunt:
			ret += "(taunt)"
		if card.divine_shield:
			ret += "(divine_shield)"
		if card.windfury:
			ret += "(windfury)"
		if card.reborn:
			ret += "(reborn)"
		ret += card.data.description.replace('\n','_')
		return ret

