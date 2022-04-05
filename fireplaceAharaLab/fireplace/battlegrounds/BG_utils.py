from fireplace import cards
from fireplace.game import Game
from fireplace.card import Card
from fireplace.actions import *
from fireplace.player import Player
from enum import IntEnum
import random
from hearthstone.enums import Zone,State

from .BG_agent import *
from .BG_bar import BG_Bar
from .BG_battle import BG_Battle

decks=[[],[],[],[],[],[]]



BobsFieldSize={1:3,2:4,3:4,4:5,5:5,6:6}

def BG_main():
	#使用カードの初期化
	cards.db.BG_initialize()
	#エージェントのリスト
	Agents=[
		BG_HumanAgent("Human1",BG_HumanAgent.HumanInput ),
		BG_RandomAgent("Random1",BG_RandomAgent.Random),
		BG_RandomAgent("Random2",BG_RandomAgent.Random),
		BG_RandomAgent("Random3",BG_RandomAgent.Random)
		]
	# ヒーローセット
	Heroes = \
		cards.battlegrounds.BG_hero20.BG20_Heroes + \
		cards.battlegrounds.BG_hero21.BG21_Heroes
	# デッキを作る
	for i in range(6):
		if i<5:
			rep=8
		else:
			rep=3
		for repeat in range(rep):	# BAN される raceはここで除外
			decks[i] += cards.battlegrounds.BG_minion.BG_PoolSet_Minion[i]
			decks[i] += cards.battlegrounds.BG_minion_beast.BG_PoolSet_Beast[i]
	# ヒーローの選択
	BG_Bars=[]
	for agent in Agents:
		theHeroes = random.sample(Heroes, 2)
		Heroes.remove(theHeroes[0])
		Heroes.remove(theHeroes[1])
		theHero = agent.heroChoiceStrategy(theHeroes)
		heroCard=Card(theHero)
		thePlayer = Player(agent.name, decks[0], theHero)#とりあえずグレ１をデッキとしておく。
		# ゲームのたちあげ
		bar = BG_Bar(thePlayer)
		bar.BG_setup()
		bar.player1 = bar.current_player = bar.controller
		bar.player2 = bar.bartender
		bar.turn=1
		BG_Bars.append(bar)
		pass
	# 無限ループ始まり
	prevMatches=[[0,1],[2,3]]# 直前の組合せを保存するための変数
	while True:	
		### 組合せを決める
		matches=[[0,1],[2,3]]#
		#battlesはこのままで繰り返し使う。
		battles = [None,None]
		### ムーブのループ始まり
		for bar in BG_Bars:
			controller = bar.controller
			controller.game = bar
			bartender = bar.bartender
			for agent in Agents:
				if agent.name == controller.name:
					break
			bartender.BobsTmpFieldSize=BobsFieldSize[bar.turn]
			controller.max_mana = min(10,bar.turn+2)
			# リロール
			notfrozen=0
			for card in bartender.field:
				if not card.frozen:
					ReturnCard(decks, card)
				else:
					notfrozen += 1
			for repeat in range(max(bartender.BobsTmpFieldSize,controller.BobsTmpFieldSize)-notfrozen):
				card = DealCard(decks,controller.Tier)
				card.controller = bartender
				card.zone = Zone.PLAY
			while True:
				### （バーテンダーに）カードを配る
				##### ムーブの選択肢を作る
				candidates = GetMoveCandidates(bar, controller, bartender)
				##### それぞれのムーブを行う（エージェントを呼び出す。）
				choice = agent.moveStrategy(bar, candidates, controller, bartender)
				#### ターンエンドが選択されていれば、ループから脱出。
				if choice.move==MovePlay.TURNEND:
					break
				else:
					choice.execute()
				pass
		### ムーブのループ終わり
		### 対戦
		i=0
		battles[i] = BG_Battle([BG_Bars[matches[i][0]],BG_Bars[matches[i][1]]])
		damage0, damage1 = battles[i].battle()
		### 対戦後処理
		if damage0>0:
			hero0 = BG_Bars[matches[i][0]].controller.hero
			hero0.damage += damage0## armorも加味すること。
			if hero0.health<=0:
				#Hero をケルスザード'TB_KTRAF_H_1'に交代する。
				pass
		if damage1>0:
			hero1 = BG_Bars[matches[i][0]].controller.hero
			hero1.damage += damage1## armorも加味すること。
			if hero1.health<=0:
				#Hero をケルスザード'TB_KTRAF_H_1'に交代する。
				pass
		pass
	# 無限ループ終わり
	pass

class MovePlay(IntEnum):
	VALID=0
	PLAY=1
	ORDER=2
	BUY=3
	SELL=4
	TIERUP=5
	REROLE=6
	FREEZE=7
	TURNEND=8
	pass

class Move(object):
	def __init__(self, game, target, move, param0=0, param1=0, param2=0):
		self.game=game
		self.controller = game.controller
		self.bartender = game.bartender
		self.game = game
		self.target = target
		self.move = move
		self.param0 = param0
		self.param1 = param1
		self.param2 = param2
		pass
	def __str__(self):
		return "%s %s %d"%(self.target, self.move, self.param0)

	def execute(self):
		if self.move==MovePlay.PLAY:# move a card from hand to field
			self.play(self.target, self.param0)
			pass
		elif self.move==MovePlay.ORDER:# change the order of field cards 
			self.changeOrder(self.target, self.param0)
			pass
		elif self.move==MovePlay.BUY:# move a card from opponent field to hand
			self.buy(self.target)
			pass
		elif self.move==MovePlay.SELL:# move a card from field to opponent
			self.sell(self.target)
			pass
		elif self.move==MovePlay.TIERUP:#push a button of grade-up
			self.tierup()
			pass
		elif self.move==MovePlay.REROLE:# refresh opponent field by pool set
			self.rerole()
			pass
		elif self.move==MovePlay.FREEZE:# fix opponent field 
			self.freeze()
			pass
		else:
			pass
		pass

	def play(self, card, position=-1):
		if card!=None and len(self.controller.field)<7:
			if position<0:
				position += len(self.controller.field)
			card._summon_index = position
			card.zone=Zone.PLAY
			self.controller.add_summon_log(card)

	def changeOrder(self, card, p0):
		len = len(self.controller.field)
		field = self.controller.field
		tmp = card
		for p in range(len):
			if field[p]==card:
				break
		if p>p0:
			for offset in range(p-p0):
				q=p-offset
				field[q]=field[q-1]
			field[p0]=tmp
		elif p<p0:
			for offset in range(p0-p):
				q=p+offset
				field[q]=field[q+1]
			field[p0]=tmp
		pass

	def buy(self, card):
		if self.controller.mana>=3:
			for c in self.bartender.field:
				if c==card:
					card.controller = self.controller
					card.zone = Zone.HAND
					self.controller.used_mana += 3
					self.controller.add_buy_log(card)
					self.bartender.field.remove(c)
					return
			pass
		pass

	def sell(self, card):
		for c in self.controller.field:
			if c==card:
				card.zone=Zone.GRAVEYARD
				self.controller.used_mana -= 1
				return
		pass

	def tierup(self):
		if self.controller.Tier<=5 and self.controller.mana>=self.controller.TierUpCost:
			self.controller.Tier += 1
			self.controller.usedmana += self.controller.TierUpCost

	def rerole(self):
		if self.controller.mana>=self.game.reroleCost:
			for card in self.bartender.field:
				ReturnCard(decks,card)
			for card in range(max(self.bartender.BobsTmpFieldSize, self.controller.BobsTmpFieldSize)):
				card = DealCard(decks, self.controller.Tier)
				card.controller = self.bartender
				card.zone = Zone.PLAY

		pass

	def freeze(self):
		allfrozen=True
		for c in self.bartender.field:
			if not c.frozen:
				allfrozen=False
		if allfrozen:
			for c in self.bartender.field:
				c.frozen=False
		else:
			for c in self.bartender.field:
				c.frozen=True
		pass

	def turnend(self):
		pass

	def turnbegin(self):
		pass

def GetMoveCandidates(bar, controller, bartender):
	ret = []
	#PLAY=1
	if len(controller.field)<7:
		for card in controller.hand:
			for pos in range(len(controller.field)+1):
				ret.append(Move(bar, card, MovePlay.PLAY, pos))
	#ORDER=2
	for pos0 in range(len(controller.field)):
		card = controller.field[pos0]
		for pos in range(len(controller.field)):
			if pos != pos0:
				ret.append(Move(bar, card, MovePlay.ORDER, pos))
	#BUY=3
	if controller.mana>=3:
		for card in bartender.field:
			ret.append(Move(bar, card, MovePlay.BUY, 0))
	#SELL=4
	for card in controller.field:
		ret.append(Move(bar, card, MovePlay.SELL, 0))
	#TIERUP=5
	if controller.Tier<=5 and controller.mana>=controller.TierUpCost:
		ret.append(Move(bar, None, MovePlay.TIERUP, 0))
	#REROLE=6
	if controller.mana>=bar.reroleCost:
		ret.append(Move(bar, None, MovePlay.REROLE, 0))
	#FREEZE=7
	ret.append(Move(bar, None, MovePlay.FREEZE, 0))
	#TURNEND=8
	ret.append(Move(bar, None, MovePlay.TURNEND, 0))
	return ret
