from fireplace import cards
from fireplace.game import Game
from fireplace.actions import *
from fireplace.player import Player

def BG_Agent(object):
	""" バトルグラウンドのエージェントのクラス
	エージェントを作るときはこのクラスを継承してください。"""
	def __init__(self, myName: str, myFunction, myOption: list, myClass: CardClass, rating ,E = 0, mulliganStrategy = None, choiceStrategy=None):
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

def BG_RandomAgent(BG_Agent):
	def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000 ):
		super().__init__(myName, myFunction, myOption, myClass, rating )
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

def BG_HumanAgent(BG_Agent):
	def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000 ):
		super().__init__(myName, myFunction, myOption, myClass, rating )
		pass
	def HumanInputChoice(self, game, option=[], gameLog=[], debugLog=False):
		pass

def BG_main():
	#使用カードの初期化
	cards.db.BG_initialize()
	#エージェントのリスト
	Agents=[
		BG_HumanAgent("Human1",BG_HumanAgent.HumanInput,choiceStrategy=HumanAgent.HumanInputChoice),
		BG_RandomAgent("Random1",BG_RandomAgent.Random),
		BG_RandomAgent("Random1",BG_RandomAgent.Random),
		BG_RandomAgent("Random1",BG_RandomAgent.Random)
		]
	# ヒーローセット
	Heroes = \
		cards.battlegrounds.BG_hero20.BG20_Heroes + \
		cards.battlegrounds.BG_hero21.BG21_Heroes
	# ゲームのたちあげ
	mainGame = BG_Game()
	# プールセットの決定
	decks = mainGame.decks
	# ヒーローの選択
	for agent in Agents:
		hisHeroes = random.sample(Heroes, 2)
		Heroes.remove(hisHeroes[0])
		Heroes.remove(hisHeroes[1])
		hisHero = agent.choiceHero(hisHeroes)
		agent.setHero(hisHero)
		pass
	# 無限ループ始まり
	while True:	
		### 組合せを決める
		matches=[[0,1],[2,3]]#
		### ムーブのループ始まり

		while True:
			##### ムーブの選択肢を作る
			candidates = self.candidate
			##### それぞれのムーブを行う（エージェントを呼び出す。）
			#### ターンエンドが選択されていれば、ループから脱出。
			pass
		### ムーブのループ終わり
		### 対戦
		i=0
		battles[i].agent1=Agents[matches[i][0]]
		battles[i].agent2=Agents[matches[i][1]]
		battle[i].setup()
		### 対戦後処理
		pass
	# 無限ループ終わり
	pass
	pass


class BG_Battle(Game):
	agent1=None
	agent2=None
	def __init__(self):
		super().__init__()
		pass
	def setup(self):
		"""
		エージェントのデータからバトルフィールドの設定をする。
		"""
		pass
	


class BG_Game(Game):
	# デッキを作る
	def __init__(self):
		self.tavern=1
	pass
	
	@property
	def decks(self):
		# BAN される raceはここで除外
		decks=[[],[],[],[],[],[]]
		for i in range(6):
			if i<5:
				rep=10
			else:
				rep=5
			for repeat in range(rep):
				decks[i] += cards.battlegrounds.BGminion.BG_PoolSet_Minion[i]
				decks[i] += cards.battlegrounds.BGminion.BG_PoolSet_Beast[i]
		return decks


class MovePlay(IntEnum):
	VALID=0
	PLAY=1
	ORDER=2
	BUY=3
	SELL=4
	TIERUP=5
	REROLE=6
	FREEZE=7
	pass

class Move(object):
	def __init__(self, game, target, move, param0, param1=0, param2=0):
		self.controller = target.controller
		self.bartender = self.controller.opponent
		self.game = game
		self.target = target
		self.move = move
		self.param0 = param0
		self.param1 = param1
		self.param2 = param2
		pass

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
		len = len(self.controller.field)
		if card!=None and len<7:
			if position<0:
				position += len
			Play(self.controller, card, None, position, None).trigger(self.controller)

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
		len =len(self.bartender.field)
		if self.controller.mana>=3:
			for c in self.bartender.field:
				if c==card:
					card.controller = self.controller
					card.zone = Zone.HAND
					self.controller.self.used_mana += 3
					return
			pass
		pass

	def sell(self, card):
		len = len(self.controller.field)
		for c in self.controller.field:
			if c==card:
				card.zone=Zone.GRAVEYARD
				return
		pass

	def tierup(self):
		if self.controller.Tier<=5 and self.controller.mana>=self.controller.TierUpCost:
			self.controller.Tier += 1
			self.controller.usedmana += self.controller.TierUpCost

	def rerole(self):
		import random
		draw = random.sample(commonDeck, self.controller.BobsFieldSize)
		for c in self.bartender.field:
			cost = c.cost

		for c in draw:
			c.controller = self.bartenderc.zone 
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

