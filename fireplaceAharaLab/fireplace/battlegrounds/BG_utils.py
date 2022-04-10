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

BobsFieldSize={1:3, 2:4, 3:4, 4:5, 5:5, 6:6}
TierUpCost={1:5, 2:6, 3:8, 4:11, 5:10}

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
		cards.battlegrounds.BG_hero1.BG_PoolSet_Hero1 
	# デッキを作る新しいゲームの始まり。
	for i in range(6):
		if i<5:
			rep=8
		else:
			rep=3
		for repeat in range(rep):	# BAN される raceはここで除外
			decks[i] += cards.battlegrounds.BG_minion.BG_PoolSet_Minion[i]
			decks[i] += cards.battlegrounds.BG_minion_beast.BG_PoolSet_Beast[i]
			decks[i] += cards.battlegrounds.BG_minion_demon.BG_PoolSet_Demon[i]
			decks[i] += cards.battlegrounds.BG_minion_dragon.BG_PoolSet_Dragon[i]
			decks[i] += cards.battlegrounds.BG_minion_elemental.BG_PoolSet_Elemental[i]
			decks[i] += cards.battlegrounds.BG_minion_mecha.BG_PoolSet_Mecha[i]
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
		### 組合せをランダムに決める（現状固定）
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
			frozencard=0
			repeat = len(bartender.field)
			for i in range(repeat):
				card = bartender.field[0]
				if not card.frozen:
					ReturnCard(decks, card)
				else:
					frozencard += 1
			for repeat in range(bartender.BobsTmpFieldSize-frozencard):
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
			if hero0.armor>0:# armorも加味する
				if hero0.armor >= damage0:
					hero0.armor -= damage0
				else:
					hero0.damage += (damage0 - hero0.armor)
					hero0.armor=0
			else:
				hero0.damage += damage0#
			print_hero_stats(BG_Bars[matches[i][0]].controller.hero, BG_Bars[matches[i][1]].controller.hero)
			if hero0.health<=0:
				#Hero をケルスザード'TB_KTRAF_H_1'に交代して続行する。
				#ケルスザードは酒場のムーブを行わない。
				pass
		if damage1>0:
			hero1 = BG_Bars[matches[i][1]].controller.hero
			if hero1.armor>0:# armorも加味する
				if hero1.armor >= damage1:
					hero1.armor -= damage1
				else:
					hero1.damage += (damage1 - hero1.armor)
					hero1.armor=0
			else:
				hero1.damage += damage1#
			print_hero_stats(BG_Bars[matches[i][0]].controller.hero, BG_Bars[matches[i][1]].controller.hero)
			if hero1.health<=0:
				#Hero をケルスザード'TB_KTRAF_H_1'に交代する。
				pass
		pass
		#次のターンへ
		for bar in BG_Bars:
			controller = bar.controller
			# グレードアップコストを減らす。
			controller.TierUpCost = max(0, controller.TierUpCost-1) 
			#ターン更新に伴うコインの補充。
			bar.turn += 1
			controller.used_mana = 0 
			pass

	# 無限ループ終わり
	pass

def print_hero_stats(hero0, hero1):
	print("<< %s (%s)<< health=%d"%(hero0, hero0.controller, hero0.health))
	print("<< %s (%s)<< health=%d"%(hero1, hero1.controller, hero1.health))
	pass

class MovePlay(IntEnum):
	VALID=0
	PLAY=1
	ORDER=2
	BUY=3
	SELL=4
	POWER=5
	TIERUP=6
	REROLE=7
	FREEZE=8
	TURNEND=9
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
			self.play(self.target, position=self.param0, targetpos=self.param1)
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
		elif self.move==MovePlay.POWER:# move a card from field to opponent
			self.power(self.target)
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

	def play(self, card, position=-1, targetpos=-1):
		if card!=None and len(self.controller.field)<7:
			if position<0:
				position += len(self.controller.field)
			card._summon_index = position
			if card.requires_target() and targetpos>=0 and self.controller.field[targetpos] in card.targets:
				card.target = se
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

	def power(self, target):
		controller = self.controller
		heropower = self.controller.hero.power
		if heropower.is_usable() and heropower.cost >= controller.mana:
			if heropower.requires_target() and target in heropower.targets:
				if target in self.controller.field:
					heropower.use(target=target)
			else:
				heropower.use()
		pass

	def tierup(self):
		if self.controller.Tier<=5 and self.controller.mana>=self.controller.TierUpCost:
			self.controller.Tier += 1
			self.controller.used_mana += self.controller.TierUpCost
			self.controller.TierUpCost = TierUpCost[self.controller.Tier]

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
				if card.requires_target():
					for target in card.targets:
						targetpos=controller.field.index(target)
						ret.append(Move(bar, card, MovePlay.PLAY, param0=pos, param1=targetpos))
				else:
					ret.append(Move(bar, card, MovePlay.PLAY, param0=pos))
	#ORDER=2
	for pos0 in range(len(controller.field)):
		card = controller.field[pos0]
		for pos in range(len(controller.field)):
			if pos != pos0:
				ret.append(Move(bar, card, MovePlay.ORDER, param0=pos))
	#BUY=3
	if controller.mana>=3:
		for card in bartender.field:
			ret.append(Move(bar, card, MovePlay.BUY))
	#SELL=4
	for card in controller.field:
		ret.append(Move(bar, card, MovePlay.SELL))
	#POWER=5
	if controller.hero.power.is_usable() and controller.hero.power.cost >= controller.mana:
		if controller.hero.power.requires_target() and len(controller.hero.power.targets)>0:
			for target in controller.hero.power.targets:
				ret.append(Move(bar, target, MovePlay.POWER))
		else:
			ret.append(Move(bar, None, MovePlay.POWER))
	#TIERUP=6
	if controller.Tier<=5 and controller.mana>=controller.TierUpCost:
		ret.append(Move(bar, None, MovePlay.TIERUP))
	#REROLE=7
	if controller.mana>=bar.reroleCost:
		ret.append(Move(bar, None, MovePlay.REROLE, 0))
	#FREEZE=8
	ret.append(Move(bar, None, MovePlay.FREEZE, 0))
	#TURNEND=9
	ret.append(Move(bar, None, MovePlay.TURNEND, 0))
	return ret
