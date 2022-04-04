from fireplace import cards
from fireplace.game import Game
from fireplace.card import Card
from fireplace.actions import *
from fireplace.player import Player
from enum import IntEnum
import random
from hearthstone.enums import Zone,State

decks=[[],[],[],[],[],[]]

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
		print("[%d] %s"%(count, card.name))
		pass
	def printMove(self, count, move):
		print("[%d] %s"%(count, move))
		pass
	def printBar(self, bar, controller, bartender):
		print("Tier[%d], TierUpCost[%d], ReroleCost[%d], Gold[%d]"%(controller.Tier, controller.TierUpCost, bar.reroleCost, controller.mana ))
		for card in bartender.field:
			if card.frozen:
				print("Bar   : %s (frozen)"%(card))
			else:
				print("Bar   : %s"%(card))
		for card in controller.field:
			print("Field : %s"%(card))
		for card in controller.hand:
			print("Hand  : %s"%(card))
		pass

def DealCard(decks, grade):
	dk=[]
	for i in range(grade):
		dk += decks[i]
	cardID = random.choice(dk)
	card = Card(cardID)
	gr = card.tech_level-1
	decks[gr].remove(cardID)
	return card

def ReturnCard(decks, card):
	gr = card.tech_level-1
	decks[gr].append(card.id)
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

BobsFieldSize={1:3,2:4,3:4,4:5,5:5,6:5}

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
			hero1.damage += damage0## armorも加味すること。
			if hero1.health<=0:
				#Hero をケルスザード'TB_KTRAF_H_1'に交代する。
				pass
		pass
	# 無限ループ終わり
	pass

from fireplace.deepcopy import deepcopy_game
class BG_Battle(Game):
	def __init__(self, bars):
		self.game1=deepcopy_game(bars[0], bars[0].current_player,0)
		self.game2=deepcopy_game(bars[1], bars[1].current_player,0)
		self.player1 = self.game1.current_player
		self.player2 = self.game2.current_player
		super().__init__([self.player1, self.player2])
		pass
	def battle(self):
		#エージェントのデータからバトルフィールドの設定をする。
		#for card in self.game1.current_player.field:
		#	card.controller = self.player1 #????
		#	card.zone = Zone.PLAY #????
		#for card in self.game2.current_player.field:
		#	card.controller = self.player2 #????
		#	card.zone = Zone.PLAYER #????
		#プレイヤーのopponentを設定
		self.player1.opponent=self.player2
		self.player2.opponent=self.player1
		#先攻後攻を決める（枚数の多いほうが先攻、同数ならばランダム）
		#self.first #先攻 #self.second #後攻
		if len(self.player1.field)>len(self.player2.field):
			self.first = self.player1
			self.second = self.player2
		elif len(self.player1.field)<len(self.player2.field):
			self.first = self.player2
			self.second = self.player1
		else:
			self.first = random.choice([self.player1, self.player2])
			self.second = self.first.opponent
		#playstateをPLAYINGにする。格段の意味は見いだせない
		for player in self.players:
			player.playstate = PlayState.PLAYING
		#turn_beginを実行（先攻、後攻の順）（イベントを発生させるため）
		BeginTurn(self.first).trigger(self)## trigger主はplayer?
		BeginTurn(self.second).trigger(self)
		#パラメータ設定
		self.current_player=self.first
		self.first.AttackIndex=0
		self.second.AttackIndex=0
		# フィールド表示
		self.printField()
		#ループ開始
		while True:
			#一方が全滅したかどうかの判断（もし全滅していたら終戦処理へ）
			if len(self.first.field)==0 or len(self.second.field)==0:
				break
			#攻撃者
			attacker = self.current_player.field[self.current_player]
			#被攻撃者
			taunts=[]
			for card in self.current_player.opponent.field:
				if card.taunt:
					taunts.append[card]
			if len(tanuts)>0:
				defenders = taunts
			else:
				defenders = self.current_player.opponent.field
			defender=random.choice(defenders)
			#攻撃
			RegularAttack(attacker, defender)
			#死者が出る場合にその処理(deathrattle)
			self.current_player.end_turn()
			#攻撃ターンの交代(freezeとone_turn_effectはない)
			self.current_player.AttackIndex+=1
			if self.current_player.AttackIndex>= len(self.current_player.field):
				self.current_player.AttackIndex=0
			self.current_player = self.current_player.opponent
			pass
		#引き分け
		if len(self.first.field)==0 and len(self.second.field)==0:
			return 0,0 #続行
		elif len(self.player1.field)==0:
			# 「セカンドのフィールドの残りカードのtech_levelの総和＋セカンドのTier」を求める
			damage = self.player2.Tier
			for card in self.player2.field:
				damage += card.tech_level
			# ダメージを返す
			return damage, 0
		else:#if len(self.player2.field)==0:
			# 「ファーストのフィールドの残りカードのtech_levelの総和＋ファーストのTier」を求める
			damage = self.player1.Tier
			for card in self.player1.field:
				damage += card.tech_level
			# ダメージを返す
			return 0, damage
		pass

	def printField(self):
		print("--------%s--------"%self.first.name)
		for card in self.first.field:
			print("%s:%s(%d/%d)"%(self.first.name, card, card.atk, card.health))
		print("--------%s--------"%self.second.name)
		for card in self.second.field:
			print("%s:%s(%d/%d)"%(self.second.name, card, card.atk, card.health))
		print("--------[over]--------")
	


class BG_Bar(Game):
	def __init__(self, player):
		self.bartender = Player('Bartender', player.starting_deck, 'DALA_BOSS_99h')
		self.controller = player
		#self.controller.starting_hero.game=self
		players = (self.bartender, player)
		super().__init__(players)
		self.reroleCost=1
	pass

	def BG_setup(self):
		self.log("Setting up game %r", self)
		self.state = State.RUNNING
		#self.step = Step.BEGIN_DRAW
		self.zone = Zone.PLAY
		self.players[0].opponent = self.players[1]
		self.players[1].opponent = self.players[0]
		for player in self.players:
			player.zone = Zone.PLAY
			#self.manager.new_entity(player)

		first, second = self.controller, self.bartender
		self.player1 = first
		self.player1.first_player = True
		self.player2 = second
		self.player2.first_player = False

		for player in self.players:
			player.summon(player.starting_hero)
			#player.playstate = PlayState.PLAYING

	


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

