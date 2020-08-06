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
from fireplace.exceptions import GameOver
import csv

def Maya_MCTS(game: ".game.Game"):
	while True:
		copyTree=copy.deepcopy(game)
		print("--------------------simulate start!!----------------")
		action=try_montecarlo_tree_search(copyTree,2000);
		print("--------------------simulate end!!------------------")
		print(action.card)
		print(action.type)
		print(action.target)
		# iterate over our hand and play whatever is playable
		if action.type=="play":
			for item in player.hand:
				if item==action.card:
					if item.requires_target():
						for target in item.targets:
							item.play(target)
							break
							pass
						pass
					else:
						item.play()
						break
					pass
				pass
			pass
		elif action.type=="attack":
			for character in player.characters:
				if character==action.card and character.can_attack():
					for target in character.targets:
						if target==action.target and character.can_attack(target):
							character.attack(target)
							break;
							pass
						pass
					pass
					break
				pass
			pass
		else:
			break
			pass
	pass


def simulate_random_turn(game: ".game.Game"):
	player = game.current_player
	# gameのディープコピーを生成
	# 全ての選択肢に対して探索をすることから始める
	while True:
		# iterate over our hand and play whatever is playable
		for card in player.hand:
			if card.is_playable() and random.random() < 0.5:
				target = None
				if card.must_choose_one:
					card = random.choice(card.choose_cards)
				if card.requires_target():
					target = random.choice(card.targets)
				print("Playing %r on %r" % (card, target))
				card.play(target=target)
				if player.choice:
					choice = random.choice(player.choice.cards)
					print("Choosing card %r" % (choice))
					player.choice.choose(choice)
				continue
		# Randomly attack with whatever can attack
		for character in player.characters:
			if character.can_attack():
				character.attack(random.choice(character.targets))

		break

	game.end_turn()
	return game
def simulate_random_game(game,trial=1)->"int":
	retVal=0
	for i in range(trial):
		hoge=copy.deepcopy(game)
		try:
			while True:
				hoge=simulate_random_turn(hoge)
				pass
		except GameOver:
			if hoge.current_player.name=="Player1" and hoge.current_player.playstate==PlayState.WON:
				retVal+=1
				pass
			pass
	return retVal
	pass
def execute_action(game,action):
	g=copy.deepcopy(game)
	turnplayer=g.current_player
	c=None
	target=None
	if action.type=="play":
		for item in turnplayer.hand:
			if item==action.card:
				c=item
				if action.target is not None:
					for t in card.targets:
						if t==action.target:
							target=t
						pass
					pass
				pass
			pass
		pass
		c.play(target=target)
	elif action.type=="attack":
		for item in turnplayer.characters:
			if item==action.card and item.can_attack():
				c=item
				for t in item.targets:
					if t==action.target:
						target=t
					pass
				pass
			pass
		pass
		if c.can_attack(target):
			c.attack(target)
			pass
	else:
		g.end_turn()
	return g
def get_valid_actions(game):
	copyGame=copy.deepcopy(game)
	myPlayer=copyGame.current_player
	actions=[]
	for card in myPlayer.hand:
		if card.is_playable():
			target=None
			if card.requires_target():
				for t in card.targets:
					actions.append(Action(card,"play",t))
					pass
				pass
			else:
				actions.append(Action(card,"play",target))
			pass
		pass
	for character in myPlayer.characters:
		if character.can_attack():
			for t in character.targets :
				actions.append(Action(character,"attack",t))
				pass
			pass
		pass
	pass
	actions.append(Action(None,"do_nothing",None))
	return actions
def try_primitive_montecarlo_simulation(game,max_trial):
	copyGame=copy.deepcopy(game)
	myPlayer=copyGame.current_player
	actions=get_valid_actions(copyGame)
	nextBoards=list(map(lambda a:execute_action(copyGame,a),actions))
	scores=list(map(lambda b:simulate_random_game(b,max_trial),nextBoards))
	print(scores)
	return actions[scores.index(max(scores))]
def try_montecarlo_tree_search(game,max_trial,_numOfTree=10):
	from fireplace.deck import Deck

	copyGame=copy.deepcopy(game)
	myPlayer=copyGame.current_player
	enemy=myPlayer.opponent
	handNum=len(enemy.hand)
	actions=get_valid_actions(copyGame)
	totalScores=[]
	if len(actions)==1:
		return actions[0]
		pass
	for i in range(_numOfTree):
		#random_sampling
		d=random_draft(CardClass.HUNTER)
		enemy.hand=CardList()
		enemy.deck=Deck()
		for item in d:
			enemy.card(item,zone=Zone.DECK)
			pass
		enemy.draw(count=handNum)
		root=Node(copyGame,None,None,actions)
		for k in range(int(max_trial/_numOfTree)):
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
				print("expanding...")
				expandingAction=currentNode.choose_expanding_action()
				try:
					currentNode=currentNode.expandChild(expandingAction)
				except GameOver as inst:
					mes,winner=inst.args
					newChild=Node(None,expandingAction,currentNode,[])
					if winner=="Player1":
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
			print("random simulation start!")
			result=currentNode.simulate()
			currentNode.backPropagate(result)
			pass
		visitScores=list(map(lambda node:ActionValue(node.move,node.visits),root.childNodes))
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
def develop_deck_addopting_specific_cards(_cards,_collection):
	"""
	Return a deck of 30 random cards for the \a card_class
	"""
	from fireplace import cards
	from fireplace.deck import Deck

	retDeck = []
	collection = []
	# hero = card_class.default_hero
	for item in _cards:
		retDeck.append(item.id)
		pass
	while len(retDeck) < Deck.MAX_CARDS:
		card = random.choice(_collection)
		if retDeck.count(card.id) < card.max_count_in_deck:
			retDeck.append(card.id)

	return retDeck
	pass
class Action(object):
	"""docstring for Action"""
	def __init__(self, _card,_type,_target=None):
		super(Action, self).__init__()
		self.card=_card
		self.type=_type
		self.target=_target

	def __str__(self):
		return "{card}->{type}(target={target})".format(card=self.card,type=self.type,target=self.target)
		pass

	def __eq__(self,obj):
		return str(self)==str(obj)
		pass
class ActionValue(object):
	"""docstring for ActionValue"""
	def __init__(self, _action,_score):
		super(ActionValue, self).__init__()
		self.action = _action
		self.score=_score
		
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
	def expandChild(self,action):
		self.expandedTree=execute_action(self.gameTree,action)
		child=Node(self.expandedTree,action,self,get_valid_actions(self.expandedTree))
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
