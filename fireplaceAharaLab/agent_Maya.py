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
from fireplace.utils import random_draft,CardList
from fireplace.deck import Deck
import csv
from utils import myAction, myActionValue, Node,getCandidates,executeAction

def Maya_MCTS(game: ".game.Game"):
	while True:
		copyTree=copy.deepcopy(game)
		player=copyTree.current_player
		print("--------------------simulate start!!----------------")
		action=try_montecarlo_tree_search(copyTree,100);
		print("--------------------simulate end!!------------------")
		print(action)
		# iterate over our hand and play whatever is playable
		exc=executeAction(game, action)
		if exc==ExceptionPlay.GAMEOVER:
			return ExceptionPlay.GAMEOVER
		else:
			continue
	return ExceptionPlay.VALID
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
		simulating_game=copy.deepcopy(game)
		try:
			while True:
				simulating_game=simulate_random_turn(simulating_game)
				pass
		except GameOver:
			if simulating_game.current_player.name=="Maya" and simulating_game.current_player.playstate==PlayState.WON:
				retVal+=1
				pass
			pass
	return retVal
	pass
def try_montecarlo_tree_search(game,max_trial,_numOfTree=10):
	from fireplace.deck import Deck

	copyGame=copy.deepcopy(game)
	myPlayer=copyGame.current_player
	enemy=myPlayer.opponent
	handNum=len(enemy.hand)
	candidates=getCandidates(copyGame)
	totalScores=[]
	if len(candidates)==1:
		return candidates[0]
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
		root=Node(copyGame,None,None,candidates)
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
			print("random simulation start!")
			result=currentNode.simulate()
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
