#MayaAgent

import os.path
import random
from bisect import bisect
from importlib import import_module
from pkgutil import iter_modules
from typing import List
from xml.etree import ElementTree
import copy
from hearthstone.enums import CardClass, CardType,PlayState, Zone,State#
import time#
import sys
from fireplace.card import Card
from fireplace.exceptions import GameOver
from fireplace.utils import random_draft,CardList
from fireplace.deck import Deck
import csv
from utils import ExceptionPlay, getCandidates, executeAction, postAction, Agent

class MayaAgent(Agent):
	def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000 ):
		super().__init__(myName, myFunction, myOption, myClass, rating )
		pass

	def Maya_MCTS(self, thisgame: ".game.Game", option=[], gameLog=[], debugLog=False):
		player = thisgame.current_player
		print("--------------------simulate start!!----------------")
		while True:
			#探索編
			candidates=getCandidates(thisgame,_includeTurnEnd=True)
			if len(candidates)==0:#ここは1になっていたが、0だと思われる。
				print("len(candidates)==0")
				return ExceptionPlay.VALID
				pass
			takingAction=try_montecarlo_tree_search(thisgame, candidates);
			print("--------------------simulate end!!------------------")
			# print(takingAction)
			# iterate over our hand and play whatever is playable
			#多分executeActionで大丈夫だろ
			if takingAction.type == ExceptionPlay.TURNEND:
				return ExceptionPlay.VALID
				pass
			exc=executeAction(thisgame, takingAction)
			postAction(player)
			if exc==ExceptionPlay.GAMEOVER:
				return ExceptionPlay.GAMEOVER
			else:
				continue
		return ExceptionPlay.VALID
		pass

def try_montecarlo_tree_search(_game, _candidates=[], _trialPerTree=50, _numOfTree=10):
	from fireplace.deck import Deck
	copyGame=copy.deepcopy(_game)#フルコピーをとる。
	myPlayer=copyGame.current_player#呼び出した「自分」
	enemy=myPlayer.opponent#呼び出した「相手」
	handNum=len(enemy.hand)#相手のハンドの枚数
	totalScores=[]
	if len(_candidates)==0:#事前にはじいているので、これは起こらない。
		return
		pass
	if len(_candidates)==1:#そもそもアクション候補が1つなら、そのアクションを行う。
		return _candidates[0]
		pass
	for i in range(_numOfTree):
		#シミュレーション下準備（この下準備は運営側で提供すべき。具体的にはdeepcopyのときに組み込むべき。）
		#random_sampling
		exclude = [	'SCH_199','SCH_259','YOD_009','DRG_050','DRG_242','DRG_099','ULD_178','DAL_800']# Aug. 2021
		d=random_draft(enemy.hero.card_class,exclude)#カードクラスに従ったランダムなデッキ。第1引数はクラス名に変更。
		enemy.hand=CardList()#敵のハンドをクリア
		enemy.deck=Deck()#敵のデッキをクリア
		for item in d:#敵のデッキを更新
			enemy.card(item,zone=Zone.DECK)
			pass
		enemy.draw(count=handNum)#敵のハンドを更新
		#ゲーム木展開
		#あとでcandidatesをpopするからそのまま使うと_candidatesは空説
		cand=getCandidates(copyGame,_includeTurnEnd=True)
		root=Node(copyGame,None,None,cand)#ファイル内クラス
		for k in range(_trialPerTree):
			current_node = root;
			while len(current_node.untriedMoves) == 0 and len(current_node.childNodes) != 0:
				current_node = current_node.selectChild();
			if len(current_node.untriedMoves) != 0:
				expanding_action=current_node.choose_expanding_action()
				current_node = current_node.expandChild(expanding_action);
			result = current_node.simulate();
			current_node.backPropagate(result);
		visitScores=list(map(lambda node:myActionValue(node.move,node.visits),root.childNodes))
		totalScores=addActionValues(totalScores,visitScores)
		print("totalScores")
		for item in totalScores:
			print("{action} -->{score}".format(action=item.action, score=item.score))
			pass
	maxScore=max(list(map(lambda actionValue:actionValue.score,totalScores)))
	retAction=0
	for item in totalScores:
		if item.score==maxScore:
			retAction=item.action
			pass
		pass
	print(retAction)
	for item in _candidates:
		if item==retAction:
			retAction=item;
			pass
		pass
	#time.sleep(5)
	return retAction
	pass

class Node(object):#ファイル内クラス。（ファイル内クラスは許される。）
	"""docstring for Node"""
	def __init__(self, gameTree, move, parent, _candidates):
		super(Node, self).__init__()
		self.gameTree=gameTree
		self.move=move
		self.parent=parent
		self.childNodes=[]
		self.wins=0
		self.visits=0
		self.untriedMoves=_candidates
		self.score=0
	def selectChild(self):
		import math#
		self.totalVisit=self.visits
		self.values=list(map(lambda node:node.wins/node.visits+math.sqrt(2*math.log(self.totalVisit)/node.visits),self.childNodes))
		retNode=self.childNodes[self.values.index(max(self.values))]
		return retNode
		pass
	def expandChild(self,action):
		self.expandingGame=copy.deepcopy(self.gameTree)
		simcand=getCandidates(self.expandingGame,_includeTurnEnd=True)
		myPolicy=""
		for item in simcand:
			if item==action:
				myPolicy=item
				pass
			pass
		exc=executeAction(self.expandingGame,myPolicy,debugLog=False)
		postAction(self.expandingGame.current_player)
		if exc==ExceptionPlay.GAMEOVER:
			print("the game has been ended.")
			child=Node(self.expandingGame,action,self,[])
			self.childNodes.append(child)
			return child
			pass
		elif action.type ==ExceptionPlay.TURNEND:
			self.expandingGame.end_turn()
			pass
		child=Node(self.expandingGame,action,self,getCandidates(self.expandingGame,_includeTurnEnd=True))
		self.childNodes.append(child)
		return child
	def choose_expanding_action(self):
		index=int(random.random()*len(self.untriedMoves))
		return self.untriedMoves.pop(index)		
		pass
	def simulate(self):
		if self.gameTree.state==State.COMPLETE:
			self.score=judgeWinner(self.gameTree)
			pass
		else:
			self.score=simulate_random_game(self.gameTree)
		return self.score
		pass
	def backPropagate(self,result=None):
		self.addVal=self.score
		if result is not None:
			self.addVal=result
			pass
		if self.addVal=="Maya":
			self.wins+=1
		elif self.addVal=="DRAW":
			self.wins+=0.5
		self.visits+=1;
		if self.parent is None:
			pass
		else:
			self.parent.backPropagate(self.addVal)
		pass

class myActionValue(object):#旧マヤ版ActionValue
	"""docstring for myActionValue"""
	def __init__(self, _action,_score):
		super(myActionValue, self).__init__()
		self.action = _action
		self.score=_score

class Evaluation(object):
	"""docstring for Evaluation"""
	def __init__(self, deck,score):
		super(Evaluation, self).__init__()
		self.deck = deck
		self.score=score
	def getScore(self):
		return self.score
		pass		
		

def addActionValues(original,additional):
	if len(original)==0:
		return copy.deepcopy(additional)
		pass
	retList=copy.deepcopy(original)
	for item in retList:
		for add in additional:
			if item.action==add.action:
				item.score+=add.score
				pass
			pass
		pass
	return retList
	pass
def simulate_random_turn(game: ".game.Game"):
	#申し訳ないがちょっとだけ賢い可能性がある
	player = game.current_player
	while True:
		#getCandidate使った方が早くないか？
		# iterate over our hand and play whatever is playable
		simCandidates=getCandidates(game,_includeTurnEnd=True)
		index=int(random.random()*len(simCandidates))
		if simCandidates[index].type ==ExceptionPlay.TURNEND:
			game.end_turn();
			return ExceptionPlay.VALID
		exc=executeAction(game,simCandidates[index],debugLog=False)
		postAction(player)
		if exc==ExceptionPlay.GAMEOVER:
			return ExceptionPlay.GAMEOVER
		else:
			continue
			pass
def simulate_random_game(game,trial=1)->"int":
	retVal=0
	for i in range(trial):
		simulating_game=copy.deepcopy(game)
		winner=""
		while True:
			try:
				gameState=simulate_random_turn(simulating_game)
			except GameOver as e:
				if simulating_game.current_player.playstate== PlayState.WON:
					pass
					#print("GameOver: %s won."%(simulating_game.current_player.name))
				elif simulating_game.current_player.playstate== PlayState.LOST:
					pass
					#print("GameOver: %s lost."%(simulating_game.current_player.name))
				else:
					print("%s is %s)"%(simulating_game.current_player.name,simulating_game.current_player.playstate ))
				winner=judgeWinner(simulating_game)
				break;
			if simulating_game.state==State.COMPLETE:
				winner=judgeWinner(simulating_game)
				#print("GameComplete: %s won."%(winner))
				break;
			if gameState==ExceptionPlay.INVALID:
				winner=judgeWinner(simulating_game)
				print("Invalid gameend: %s won."%(winner))
				break;
				pass
		if winner=="Maya":
			retVal+=1
		elif winner=="DRAW":
			retVal+=0.5
			pass
	return retVal
	pass
def get_cardList(card_class:CardClass,exclude=[]):
	from fireplace import cards

	collection = []
	#-->card list
	# hero = card_class.default_hero

	for card in cards.db.keys():
		if card in exclude:
			continue
		cls = cards.db[card]
		if not cls.collectible:
			continue
		if cls.type == CardType.HERO:
			# Heroes are collectible...
			continue
		if cls.card_class and cls.card_class not in [card_class, CardClass.NEUTRAL]:
			# Play with more possibilities
			continue
		collection.append(cls)
	pass
	return collection
def judgeWinner(game):
	if game.current_player.playstate == PlayState.WON:
		return game.current_player.name
	if game.current_player.playstate == PlayState.LOST:
		return game.current_player.opponent.name
	return 'DRAW'
	pass
