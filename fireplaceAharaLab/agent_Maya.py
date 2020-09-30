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
from utils import ExceptionPlay, myAction, myActionValue,getCandidates,executeAction

from card_pair import get_all_cards,get_all_vanillas

def Maya_MCTS(game: ".game.Game",_name="Default"):
	while True:
		player=game.current_player
		print("--------------------simulate start!!----------------")
		#探索編
		candidates=getCandidates(game,_includeTurnEnd=True)
		if len(candidates)==1:
			print("len(candidates)==1")
			return ExceptionPlay.VALID
			pass
		takingAction=try_montecarlo_tree_search(game,candidates);
		print("--------------------simulate end!!------------------")
		print(takingAction)
		# iterate over our hand and play whatever is playable
		#多分executeActionで大丈夫だろ
		if takingAction.type ==ExceptionPlay.TURNEND:
			return ExceptionPlay.VALID
			pass
		exc=executeAction(game, takingAction,debugLog=False)
		postAction(player)
		if exc==ExceptionPlay.GAMEOVER:
			return ExceptionPlay.GAMEOVER
		else:
			continue
	return ExceptionPlay.VALID
	pass
def postAction(player):
	while player.choice:
		choice = random.choice(player.choice.cards)
		#print("Choosing card %r" % (choice))
		myChoiceStr = str(choice)
		if 'RandomCardPicker' in str(choice):
			myCardID =  random.choice(choice.find_cards())
			myCard = Card(myCardID)
			myCard.controller = player#?
			myCard.draw()
			player.choice = None
		else :
			player.choice.choose(choice)
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
def simulate_random_game(game,trial=1,_name="Default")->"int":
	retVal=0
	for i in range(trial):
		simulating_game=copy.deepcopy(game)
		winner=""
		while True:
			try:
				gameState=simulate_random_turn(simulating_game)
			except GameOver as e:
				print("exception")
				print(simulating_game.current_player.name)
				print(simulating_game.current_player.playstate)
				winner=judgeWinner(simulating_game)
				break;
			if simulating_game.state==State.COMPLETE:
				winner=judgeWinner(simulating_game)
				break;
			if gameState==ExceptionPlay.INVALID:
				print("gameState==ExceptionPlay.INVALID")
				winner=judgeWinner(simulating_game)
				break;
				pass
		if winner==_name:
			retVal+=1
		elif winner=="DRAW":
			retVal+=0.5
			pass
	return retVal
	pass
def try_montecarlo_tree_search(_game,_candidates=[],_trialPerTree=50,_numOfTree=10,_name="Default"):
	from fireplace.deck import Deck
	copyGame=copy.deepcopy(_game)
	myPlayer=copyGame.current_player
	enemy=myPlayer.opponent
	handNum=len(enemy.hand)
	totalScores=[]
	if len(_candidates)==0:
		return
		pass
	if len(_candidates)==1:
		return _candidates[0]
		pass
	for i in range(_numOfTree):
		#シミュレーション下準備
		#random_sampling
		exclude = ['CFM_672','CFM_621','CFM_095','LOE_076','BT_490']
		allCards=get_all_cards(enemy.hero)
		vanillas=get_all_vanillas(allCards)
		random.shuffle(vanillas)
		d=vanillas[0:10]
		enemy.hand=CardList()
		enemy.deck=Deck()
		for item in d:
			enemy.card(item.id,zone=Zone.DECK)
			pass
		enemy.draw(count=handNum)
		#ゲーム木展開
		#あとでcandidatesをpopするからそのまま使うと_candidatesは空説
		cand=getCandidates(copyGame,_includeTurnEnd=True)
		root=Node(copyGame,None,None,cand,_name=_name)
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
	for item in _candidates:
		if item==retAction:
			retAction=item;
			pass
		pass
	time.sleep(5)
	return retAction
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
class Node(object):
	"""docstring for Node"""
	def __init__(self, gameTree,move,parent,_candidates,_name=None):
		super(Node, self).__init__()
		self.gameTree=gameTree
		self.move=move
		self.parent=parent
		self.childNodes=[]
		self.wins=0
		self.visits=0
		self.untriedMoves=_candidates
		self.score=0
		self.name=_name
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
		exc=executeAction(self.expandingGame,myPolicy)
		postAction(self.expandingGame.current_player)
		if exc==ExceptionPlay.GAMEOVER:
			print("the game has been ended.")
			child=Node(self.expandingGame,action,self,[],_name=self.name)
			self.childNodes.append(child)
			return child
			pass
		elif action.type ==ExceptionPlay.TURNEND:
			self.expandingGame.end_turn()
			pass
		child=Node(self.expandingGame,action,self,getCandidates(self.expandingGame,_includeTurnEnd=True),_name=self.name)
		self.childNodes.append(child)
		return child
	def choose_expanding_action(self):
		index=int(random.random()*len(self.untriedMoves))
		return self.untriedMoves.pop(index)		
		pass
	def simulate(self):
		if self.gameTree.state==State.COMPLETE:
			self.winnerName=judgeWinner(self.gameTree)
			if self.winnerName==self.name:
				self.score=1
				pass
			elif self.winnerName=="DRAW":
				self.score=0.5
			else:
				self.score=0
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
		self.wins+=self.addVal
		self.visits+=1;
		if self.parent is None:
			pass
		else:
			self.parent.backPropagate(self.addVal)
		pass
