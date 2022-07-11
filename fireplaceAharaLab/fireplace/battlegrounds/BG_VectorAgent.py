from .BG_agent import BG_Agent
from .BG_enums import MovePlay
from .BG_battle import BG_Battle
from fireplace.deepcopy import deepcopy_game
from hearthstone.enums import Zone,State, CardClass, CardType, GameTag, Race
import random


class BG_VectorAgent(BG_Agent):
	def __init__(self, myName, myOption = [], rating =1000 ):
		super().__init__(myName, myOption, rating, \
			heroChoiceStrategy=self.VectorHeroChoice, \
			moveStrategy=self.VectorMoveChoice,
			choiceStrategy=self.VectorDiscoveryChoice)
		self. favorites=[
			['BG21_000','CFM_316','FP1_031',],## Š^‘lƒoƒƒ“
			]
		pass
	def getStats(self, card):
		if card.type==CardType.MINION:
			return card.atk+card.max_health
		else:
			return 10

	def GetStats(self, controller, new_card=None, old_card=None):
		self.dummy = Player('dummy', None, None)
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
		self.bar1=controller.game
		self.game1=deepcopy_game(self.bar1, controller, 0)
		self.player1 = self.game1.player1
		self.player1.deepcopy_original = self.bar1.controller
		self.player2 = self.game2.player1
		self.player2.deepcopy_original = None
		self.this_is_battle=True
		battlefield = BG_Battle(controller, dummy)
		while:
			pass
		pass
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




