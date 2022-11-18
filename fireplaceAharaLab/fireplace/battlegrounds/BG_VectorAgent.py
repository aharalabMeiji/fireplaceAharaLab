from .BG_agent import BG_Agent, BG_NecoAgent
from .BG_enums import MovePlay
from .BG_battle import BG_Battle
from .BG_bar import BG_Bar
from ..deepcopy import deepcopy_game
from ..player import Player
from ..actions import Hit
from hearthstone.enums import Zone,State, CardClass, CardType, GameTag, Race
import random


class BG_VectorAgent(BG_Agent):
	def __init__(self, myName, myOption = [], rating =1000 ):
		super().__init__(myName, myOption, rating, \
			heroChoiceStrategy=self.VectorHeroChoice, \
			moveStrategy=self.VectorMoveChoice,
			choiceStrategy=self.VectorDiscoveryChoice)
		self. favorites=[
			['BG21_000','CFM_316','FP1_031',],## frog + baron
			]
		self.dummyAgent = BG_NecoAgent("Dummy")
		self.dummyHero = 'BG22_HERO_007'
		self.dummyPlayer = Player(self.dummyAgent.name, [], self.dummyHero)
		self.dummyBar = BG_Bar(self.dummyPlayer)
		self.dummyBar.BG_setup()
		self.dummyBar.player1 = self.dummyBar.current_player = self.dummyBar.controller
		self.dummyBar.player2 = self.dummyBar.bartender
		pass
	def getStats(self, card):
		if card.type==CardType.MINION:
			return card.atk+card.max_health
		else:
			return 10
	def defenseStep(self, health, shield, amount):
		return int(health/amount)+1+shield
	def attackStep(self, atk, windfury, poisonous, amount):
		if poisonous: 
			return 1
		else:
			return int(amount/atk/windfury)+1
	def GetStats(self, controller, new_card=None, old_card=None):
		total_steps=0
		defense05=0
		defense10=0
		defense15=0
		defense20=0
		defense40=0
		attack05=0
		attack10=0
		attack15=0
		attack20=0
		attack40=0
		poisonous=0
		self.controllerBar=deepcopy_game(controller.game, controller, 0)
		self.controller=self.controllerBar.controller
		self.vectorBattle = BG_Battle([self.controllerBar, self.dummyBar])
		while len(self.controller.field)>0:
			card = self.controller.field[0]
			atk = card.atk
			health = card.health
			if card.divine_shield:
				Hit(card, health).trigger(self.dummyPlayer)
				shield=1
			else:
				shield=0
			if card.windfury:
				windfury=2
			else:
				windfury=1
			Hit(card, health).trigger(self.dummyPlayer)
			if card.poisonous:
				if shield:
					poisonous += 2
				else:
					poisonous += 1
			total_step += 1
			defense05 += self.defenseStep(health, shield, 5)
			defense10 += self.defenseStep(health, shield, 10)
			defense15 += self.defenseStep(health, shield, 15)
			defense20 += self.defenseStep(health, shield, 20)
			defense40 += self.defenseStep(health, shield, 40)
			attack05 -= self.attackStep(atk, windfury, card.poisonous, 5)
			attack10 -= self.attackStep(atk, windfury, card.poisonous, 10)
			attack15 -= self.attackStep(atk, windfury, card.poisonous, 15)
			attack20 -= self.attackStep(atk, windfury, card.poisonous, 20)
			attack40 -= self.attackStep(atk, windfury, card.poisonous, 40)
		return [total_step, defense05, defense10, defense15, defense20, defense40, \
			attack05, attack10, attack15, attack20, attack40, poisonous]

	def VectorMoveChoice(self, bar, candidates, controller, bartender):
		if len(candidates)>0:
			choices=[]
			tier = controller.tavern_tier
			gold = controller.mana
			if (tier,gold) in [(1,4),(2,7),(3,9),(4,10),(5,10)]:
				for move in candidates:
					if move.move==MovePlay.TIERUP:
						return move
			if gold>=3:
				max_stats=self.GetStats(controller)
				max_stats_cards=[[None, None]]
				for move in candidates:
					if move.move==MovePlay.BUY:
						new_card = move.target
						if len(controller.field)<7:
							old_card=None
							stats=self.GetStats(controller, new_card, old_card)
						else:
							for old_card in controller.field:
								stats=self.GetStats(controller, new_card, old_card)
				if len(choices)>0:
					return random.choice(choices)
			if len(controller.field)<7 and len(controller.hand)>0:
				max_stats=0
				choices=[]
				for move in candidates:
					if move.move==MovePlay.PLAY:
						card = move.target
						if choices==[]:
							choices=[move]
							max_stats=self.getStats(move.target)
						elif self.getStats(card)>max_stats:
							choices=[move]
							max_stats=self.getStats(move.target)
						elif self.getStats(card)==max_stats:
							choices.append(move)
				if len(choices)>0:
					return random.choice(choices)
			if len(controller.field)==7 and len(controller.hand)>0:
				max_stats=999
				min_minion=None
				for card in controller.field:
					if max_stats>self.getStats(card):
						min_minion=card
						max_stats=self.getStats(card)
				for move in candidates:
					if move.move==MovePlay.BUY:
						card = move.target
						if self.getStats(card)>max_stats:
							choices=[move]
							max_stats=self.getStats(move.target)
						elif self.getStats(card)==max_stats:
							choices.append(move)
				if len(choices)>0:
					for choice in candidates:
						if choice.target==card and choice.move==MovePlay.SELL:
							return choice
			for choice in candidates:
				if choice.move==MovePlay.TURNEND:
					return choice
		return None

	def VectorHeroChoice(self, heroes):
		favorites=[
			'BG23_HERO_304',## #80#Lady Vashj
			'TB_BaconShop_HERO_18',#47#Patches the Pirate
			]
		for hero in favorites:
			if hero in heroes:
				return hero
		return random.choice(heroes)
	def VectorDiscoveryChoice(self, controller, choices):
		return random.choice(choices)




