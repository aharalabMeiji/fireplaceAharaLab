import random
import numpy as np
import copy
from fireplace.exceptions import GameOver
from hearthstone.enums import CardType, BlockType
from utils import ExceptionPlay, executeAction, getCandidates, postAction, myActionValue
from hearthstone.enums import CardClass, CardType, PlayState, Zone, State
from fireplace.actions import Action
from fireplace.card import Card
from fireplace.game import Game
from fireplace.utils import random_draft,CardList
from enum import IntEnum
from fireplace.deck import Deck

exclude = ['CFM_672','CFM_621','CFM_095','LOE_076','BT_490']


def Miya_UCT(game: ".game.Game", option=[], debugLog=True):
	while True:
		copyTree=copy.deepcopy(game)
		player=copyTree.current_player
		print("--------------------simulate start!!----------------")
		#探索編
		candidates=getCandidates(copyTree,_smartCombat=False,_includeTurnEnd=True)
		print("getCandidates")
		if len(candidates)==1:
			print("len(candidates)==1  TurnEnd")
			return ExceptionPlay.VALID
			pass
		takingAction=tryUCT(copyTree,candidates,_trialPerTree=10);
		print("--------------------simulate end!!------------------")
		print(takingAction)
		# iterate over our hand and play whatever is playable

		if takingAction.type ==ExceptionPlay.TURNEND:
			return ExceptionPlay.VALID
			pass
		exc=executeAction(game, takingAction)
		postAction(player)
		if exc==ExceptionPlay.GAMEOVER:
			return ExceptionPlay.GAMEOVER
		else:
			continue
	print("ターンエンド")
	return ExceptionPlay.VALID
	pass





def tryUCT(_game,_candidates=[],_trialPerTree=10,_numOfTree=2):

	totalScores=[]
	if len(_candidates)==0:
		print("noCans")
		return
		pass
	if len(_candidates)==1:
		return _candidates[0]
		pass
	for i in range(_numOfTree):
		#シミュレーション下準備
		#random_sampling
		copyGame=copy.deepcopy(_game)
		myPlayer=copyGame.current_player
		enemy=myPlayer.opponent
		handNum=len(enemy.hand)
		d=random_draft(enemy.hero,exclude)
		enemy.hand=CardList()
		enemy.deck=Deck()
		for item in d:
			enemy.card(item,zone=Zone.DECK)
			pass
		enemy.draw(count=handNum)
		#ゲーム木展開
		root=Node(copyGame,None,None,_candidates)
		for k in range(_trialPerTree):
			current_node = root;
			while len(current_node.untriedMoves) == 0 and len(current_node.childNodes) != 0:
				current_node = current_node.selectChild();
			if len(current_node.untriedMoves) != 0:
				expanding_action=current_node.choose_expanding_action()
				current_node = current_node.expandChild(expanding_action);
			result = current_node.simulate();
			current_node.backPropagate(result);
		#print("childNodes")
		#print(root.childNodes)
		visitScores=list(map(lambda node:myActionValue(node.move,node.visits),root.childNodes))
		print(visitScores)
		print(totalScores)
		totalScores=addActionValues(totalScores,visitScores)
		print("totalScores")
		for item in totalScores:
			print(item.action)
			print("-->{score}".format(score=item.score))
			pass
	maxScore=max(list(map(lambda actionValue:actionValue.score,totalScores)))
	retAction=0
	for item in totalScores:
		if item.score==maxScore:
			retAction=item.action
			pass
		pass
	print(retAction)
	#time.sleep(5)
	return retAction
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

class Node(object):
	"""docstring for Node"""
	def __init__(self, gameTree,move,parent,actions):
		super(Node, self).__init__()
		self.gameTree=gameTree
		self.move=move
		self.parent=parent
		self.childNodes=[]
		self.wins=0
		self.visits=0
		self.untriedMoves=copy.deepcopy(actions)
		self.score=0
	def selectChild(self):
		import math#
		self.totalVisit=self.visits
		self.values=list(map(lambda node:node.wins/node.visits+math.sqrt(math.log(self.totalVisit)/node.visits),self.childNodes))
		retNode=self.childNodes[self.values.index(max(self.values))]
		return retNode
		pass
	def expandChild(self,action):#maya氏改訂版
		print("expandChild-----------------------------")
		print(action)
		self.expandingGame=copy.deepcopy(self.gameTree)
		exc=executeAction(self.expandingGame,action)
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
		child=Node(self.expandingGame,action,self,getCandidates(self.expandingGame,_smartCombat=False,_includeTurnEnd=True))
		self.childNodes.append(child)
		return child
	def choose_expanding_action(self):
		index=int(random.random()*len(self.untriedMoves))
		return self.untriedMoves.pop(index)		
		pass
	def simulate(self):
		return simulate_random_game(self.gameTree)
		pass
	def backPropagate(self,result=None):
		self.addVal=self.score
		if result is not None:
			self.addVal=result
			pass
		self.wins+=self.addVal
		self.visits+=1;
		if self.parent is None:
			pass
		else:
			self.parent.backPropagate(self.addVal)
		pass
	def setScore(self,_score):
		self.score=_score
		pass

def simulate_random_turn(game: ".game.Game"):
	#申し訳ないがちょっとだけ賢い可能性がある
	player = game.current_player
	while True:
		#getCandidate使った方が早くないか？
		# iterate over our hand and play whatever is playable
		simCandidates=getCandidates(game,_smartCombat=False,_includeTurnEnd=True)
		index=int(random.random()*len(simCandidates))
		if simCandidates[index].type is ExceptionPlay.TURNEND:
			try:
				game.end_turn();
				return ExceptionPlay.VALID
				pass
			except GameOver as over:
				return ExceptionPlay.INVALID
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
			gameState=simulate_random_turn(simulating_game)
			if simulating_game.state==State.COMPLETE:
				winner=judgeWinner(simulating_game)
				break;
			if gameState==ExceptionPlay.INVALID:
				print("gameState==ExceptionPlay.INVALID")
				winner=judgeWinner(simulating_game)
				break;
				pass
		if winner=="Miya":
			retVal+=1
		elif winner=="DRAW":
			retVal+=0.5
			pass
	return retVal
	pass

def judgeWinner(game):
	if game.current_player.playstate == PlayState.WON:
		return game.current_player.name
	if game.current_player.playstate == PlayState.LOST:
		return game.current_player.opponent.name
	return 'DRAW'
	pass