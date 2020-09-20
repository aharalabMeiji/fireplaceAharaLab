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

def Maya_MCTS(game: ".game.Game"):
	while True:
		copyTree=copy.deepcopy(game)
		player=copyTree.current_player
		print("--------------------simulate start!!----------------")
		#探索編
		candidates=getCandidates(copyTree)
		print("getCandidates")
		if len(candidates)==0:
			print("len(candidates)==0")
			return ExceptionPlay.VALID
			pass
		takingAction=try_montecarlo_tree_search(copyTree,candidates,_trialPerTree=1000);
		print("--------------------simulate end!!------------------")
		print(takingAction)
		# iterate over our hand and play whatever is playable
		#多分executeActionで大丈夫だろ
		exc=executeAction(game, takingAction)
		postAction(player)
		if exc==ExceptionPlay.GAMEOVER:
			return ExceptionPlay.GAMEOVER
		else:
			continue
	return ExceptionPlay.VALID
	pass
def postAction(player):
	if player.choice:
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
		simCandidates=getCandidates(game)
		index=int(random.random()*(len(simCandidates)+1))
		if index==len(simCandidates):
			pass
		else:
			exc=executeAction(game,simCandidates[index])
			postAction(player)
			if exc==ExceptionPlay.GAMEOVER:
				return ExceptionPlay.GAMEOVER
			else:
				continue
				pass
		game.end_turn();
		return ExceptionPlay.VALID
def simulate_random_game(game,trial=1)->"int":
	retVal=0
	for i in range(trial):
		simulating_game=copy.deepcopy(game)
		winner=""
		while True:
			gameState=simulate_random_turn(simulating_game)
			if simulating_game.state==State.COMPLETE:
				if simulating_game.current_player.playstate == PlayState.WON:
					winner=simulating_game.current_player.name
					break;
					pass
				if simulating_game.current_player.playstate == PlayState.LOST:
					winner=simulating_game.opponent.name
					break;
					pass
				winner="DRAW"
				break;
		if winner=="Maya":
			retVal+=1
		elif winner=="DRAW":
			retVal+=0.5
			pass
	return retVal
	pass
def try_montecarlo_tree_search(_game,_candidates=[],_trialPerTree=10,_numOfTree=10):
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
		d=random_draft(enemy.hero)
		enemy.hand=CardList()
		enemy.deck=Deck()
		for item in d:
			enemy.card(item,zone=Zone.DECK)
			pass
		enemy.draw(count=handNum)
		#ゲーム木展開
		root=Node(copyGame,None,None,_candidates)
		print(_candidates)
		for k in range(_trialPerTree):
			currentNode=root
			print("----------")
			print("dig tree...")
			while len(currentNode.untriedMoves)==0 and len(currentNode.childNodes)!=0:
				currentNode=currentNode.selectChild()
				print(currentNode.move)
				print("->")
				pass
			print("digged!!")
			print("expand child...")
			if len(currentNode.untriedMoves)!=0:
				#まだ探索してない枝がある
				print("expanding...")
				expandingAction=currentNode.choose_expanding_action()
				try:
					currentNode=currentNode.expandChild(expandingAction)
				except GameOver:
					#今gameoverに勝者の情報は入っていないので注意して
					newChild=Node(None,expandingAction,currentNode,[])
					if winner=="Maya":
						newChild.setScore(1)
						pass
					else:
						newChild.setScore(0)
					currentNode.childNodes.append(newChild)
					newChild.backPropagate()
					continue
				print("done")
				pass
			else:
				currentNode.backPropagate()
				continue
				pass
			print("is it ended?")
			result=simulate_random_game(currentNode.gameTree)
			currentNode.backPropagate(result)
			pass
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
	#time.sleep(5)
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
class Node(object):
	"""docstring for Node"""
	def __init__(self, gameTree,move,parent,_candidates):
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
		self.originalGame=copy.deepcopy(self.gameTree)
		executeAction(self.gameTree,action)
		postAction(self.gameTree.current_player)
		child=Node(self.gameTree,action,self,getCandidates(self.gameTree))
		self.childNodes.append(child)
		self.gameTree=self.originalGame
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