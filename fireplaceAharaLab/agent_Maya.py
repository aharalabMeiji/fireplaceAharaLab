#MayaAgent

import os.path
import random
from bisect import bisect
from importlib import import_module
from pkgutil import iter_modules
from typing import List
import copy
from hearthstone.enums import CardClass, CardType,PlayState, Zone,State#
import time#
import sys
from fireplace.card import Card
from fireplace.exceptions import GameOver
from fireplace.utils import random_draft,CardList
from fireplace.deck import Deck
from utils import *
class agent_Maya(Agent):
	def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000 ):
		super().__init__(myName, myFunction, myOption, myClass, rating )
	def agent_MayaAI(self, game: Game, option=[self.myName], gameLog=[], debugLog=False):
		while True:
			self.currentPlayer=game.current_player
			print("--------------------simulate start!!----------------")
			#探索編
			self.candidates=getCandidates(game,_includeTurnEnd=True)
			if len(self.candidates)==1:
				print("len(self.candidates)==1")
				return ExceptionPlay.VALID
				pass
			self.takingAction=self.try_montecarlo_tree_search(game,self.candidates,_name=option[0]);
			print("--------------------simulate end!!------------------")
			print(self.takingAction)
			# iterate over our hand and play whatever is playable
			#多分executeActionで大丈夫だろ
			if self.takingAction.type ==ExceptionPlay.TURNEND:
				return ExceptionPlay.VALID
				pass
			self.exc=executeAction(game, self.takingAction)
			self.myPostAction(self.currentPlayer)
			if self.exc==ExceptionPlay.GAMEOVER:
				return ExceptionPlay.GAMEOVER
			else:
				continue
		return ExceptionPlay.VALID
		pass
	def myPostAction(self,player):
		while player.choice:
			self.choice = random.choice(player.choice.cards)
			#print("Choosing card %r" % (choice))
			self.myChoiceStr = str(self.choice)
			if 'RandomCardPicker' in str(self.choice):
				self.myCardID =  random.choice(self.choice.find_cards())
				self.myCard = Card(self.myCardID)
				self.myCard.controller = player#?
				self.myCard.draw()
				player.choice = None
			else :
				player.choice.choose(self.choice)
			pass
	def try_montecarlo_tree_search(self,_candidates=[],_trialPerTree=50,_numOfTree=10,_name="Default"):
		from fireplace.deck import Deck
		self.copyGame=copy.deepcopy(_game)
		self.myPlayer=self.copyGame.current_player
		self.enemy=self.myPlayer.opponent
		self.handNum=len(self.enemy.hand)
		self.totalScores=[]
		if len(_candidates)==0:
			return
			pass
		if len(_candidates)==1:
			return _candidates[0]
			pass
		for i in range(_numOfTree):
			#シミュレーション下準備
			#random_sampling
			self.exclude = ['CFM_672','CFM_621','CFM_095','LOE_076','BT_490']
			self.temporaryDeck=random_draft(self.enemy.hero,self.exclude)
			self.enemy.hand=CardList()
			self.enemy.deck=Deck()
			for item in self.temporaryDeck:
				self.enemy.card(item,zone=Zone.DECK)
				pass
			self.enemy.draw(count=self.handNum)
			#ゲーム木展開
			#あとでcandidatesをpopするからそのまま使うと_candidatesは空説
			self.currentCandidate=getCandidates(self.copyGame,_includeTurnEnd=True)
			self.root=Node(self.copyGame,None,None,self.currentCandidate,_name=_name)
			for tree in range(_trialPerTree):
				self.current_node = self.root;
				while len(self.current_node.untriedMoves) == 0 and len(self.current_node.childNodes) != 0:
					self.current_node = self.current_node.selectChild();
				if len(self.current_node.untriedMoves) != 0:
					self.expanding_action=self.current_node.choose_expanding_action()
					self.current_node = self.current_node.expandChild(self.expanding_action);
				self.result = current_node.simulate();
				self.current_node.backPropagate(self.result);
			self.visitScores=list(map(lambda node:myActionValue(node.move,node.visits),self.root.childNodes))
			self.totalScores=self.addActionValues(self.totalScores,self.visitScores)
			print("totalScores")
			for item in self.totalScores:
				print(item.action)
				print("-->{score}".format(score=item.score))
				pass
		self.maxScore=max(list(map(lambda actionValue:actionValue.score,self.totalScores)))
		self.retAction=0
		for item in self.totalScores:
			if item.score==self.maxScore:
				self.retAction=item.action
				pass
			pass
		print(self.retAction)
		for item in _candidates:
			if item==self.retAction:
				self.retAction=item;
				pass
			pass
		#time.sleep(5)
		return self.retAction
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
		self.retNode=self.childNodes[self.values.index(max(self.values))]
		return self.retNode
		pass
	def expandChild(self,action):
		self.expandingGame=copy.deepcopy(self.gameTree)
		self.simcand=getCandidates(self.expandingGame,_includeTurnEnd=True)
		self.myPolicy=""
		for item in self.simcand:
			if item==action:
				self.myPolicy=item
				pass
			pass
		self.exc=executeAction(self.expandingGame,self.myPolicy)
		self.myPostAction(self.expandingGame.current_player)
		try:
			if self.exc==ExceptionPlay.GAMEOVER:
				print("the game has been ended.")
				self.child=Node(self.expandingGame,action,self,[],_name=self.name)
				self.childNodes.append(self.child)
				return self.child
				pass
			elif action.type ==ExceptionPlay.TURNEND:
				self.expandingGame.end_turn()
				pass
			self.child=Node(self.expandingGame,action,self,getCandidates(self.expandingGame,_includeTurnEnd=True),_name=self.name)
			self.childNodes.append(self.child)
			return self.child
		except GameOver as over:
			print("the game has been ended.")
			self.child=Node(self.expandingGame,action,self,[],_name=self.name)
			self.childNodes.append(self.child)
			return self.child
			pass
	def choose_expanding_action(self):
		self.index=int(random.random()*len(self.untriedMoves))
		return self.untriedMoves.pop(self.index)
		pass
	def simulate(self):
		if self.gameTree.state==State.COMPLETE:
			self.winnerName=self.judgeWinner(self.gameTree)
			if self.winnerName==self.name:
				self.score=1
				pass
			elif self.winnerName=="DRAW":
				self.score=0.5
			else:
				self.score=0
			pass
		else:
			self.score=self.simulate_random_game(self.gameTree,_name=self.name)
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
	def simulate_random_turn(self,game: ".game.Game"):
		#申し訳ないがちょっとだけ賢い可能性がある
		self.player= = game.current_player
		while True:
			#getCandidate使った方が早くないか？
			# iterate over our hand and play whatever is playable
			self.simCandidates=getCandidates(game,_includeTurnEnd=True)
			self.index=int(random.random()*len(self.simCandidates))
			if simCandidates[index].type ==ExceptionPlay.TURNEND:
				game.end_turn();
				return ExceptionPlay.VALID
			self.exc=executeAction(game,self.simCandidates[self.index])
			self.myPostAction(self.player)
			if self.exc==ExceptionPlay.GAMEOVER:
				return ExceptionPlay.GAMEOVER
			else:
				continue
				pass
	def simulate_random_game(self,game)->"int":
		self.retVal=0
		self.simulating_game=copy.deepcopy(game)
		self.winner=""
		while True:
			try:
				self.gameState=self.simulate_random_turn(self.simulating_game)
			except GameOver as e:
				print("exception")
				print(self.simulating_game.current_player.name)
				print(self.simulating_game.current_player.playstate)
				self.winner=self.judgeWinner(self.simulating_game)
				break;
			if self.simulating_game.state==State.COMPLETE:
				self.winner=self.judgeWinner(self.simulating_game)
				break;
			if self.gameState==ExceptionPlay.INVALID:
				print("gameState==ExceptionPlay.INVALID")
				self.winner=self.judgeWinner(self.simulating_game)
				break;
				pass
		if self.winner==self.name:
			self.retVal+=1
		elif self.winner=="DRAW":
			self.retVal+=0.5
			pass
		return self.retVal
	def judgeWinner(self,game):
		if game.current_player.playstate == PlayState.WON:
			return game.current_player.name
		if game.current_player.playstate == PlayState.LOST:
			return game.current_player.opponent.name
		return 'DRAW'
		pass
