import random
import numpy as np
import copy
from fireplace.exceptions import GameOver, InvalidAction
from fireplace.card import CardType
from fireplace.logging import log
from hearthstone.enums import CardClass, CardType,PlayState, Zone,State, GameTag#
from typing import List
from utils import myAction, myActionValue
from fireplace.actions import Action
from fireplace.card import Card
from fireplace.game import Game
from enum import IntEnum

def GenzoRandom(thisgame: ".game.Game"):
	player = thisgame.current_player
	loopCount=0
	while loopCount<20:
		loopCount+=1
		myCandidate = []
		for card in player.hand:
			if card.is_playable():
				target = None
				if card.must_choose_one:
					card = random.choice(card.choose_cards)#ここに相当する部分の戦略なし
				if card.requires_target():
					for target in card.targets:
						myCandidate.append([card, target])
				else:
					myCandidate.append([card,None])
		if len(myCandidate) > 0:
			myChoice = random.choice(myCandidate)
			if executePlay(myChoice[0], myChoice[1])==ExceptionPlay.GAMEOVER:
				return ExceptionPlay.GAMEOVER
			if player.choice:
				choice = random.choice(player.choice.cards)
				#print("Choosing card %r" % (choice))
				myChoiceStr = str(choice)
				if 'RandomCardPicker' in str(choice):
					myCardID =  random.choice(choice.find_cards())
					myCard = Card(myCardID)
					myCard.controller = player#?
					myCard.draw()
					#player.hand.append(myCard)#?
					#myCard.zone = Zone.HAND#?
					player.choice = None
				else :
					player.choice.choose(choice)
				continue
		else:
			myCandidate = []# Randomly attack with whatever can attack
			for character in player.characters:
				if character.can_attack():
					for target in character.targets:
						if character.can_attack(target):
							myH=character.health
							hisA=target.atk
							if myH > hisA:
								myCandidate.append([character,target])
			if len(myCandidate)>0:
				myChoice = random.choice(myCandidate)
				if executeAttack(myChoice[0], myChoice[1])==ExceptionPlay.GAMEOVER:
					return ExceptionPlay.GAMEOVER
			else:
				return ExceptionPlay.VALID
def getStageScore(game,weight):
	me = game.current_player
	he = game.current_player.opponent
	myHero = me.hero
	hisHero = he.hero
	myHeroH = myHero.health
	hisHeroH = hisHero.health
	myCharH = 0
	myCharN = 0
	myTauntCharH = 0
	for char in me.characters:
		myCharH += char.health
		myCharN += 1
		#GameTag.TAUNT
		if char.taunt:
			myTauntCharH += char.health
	hisCharH = 0
	hisCharN = 0
	hisTauntCharH = 0
	for char in he.characters:
		hisCharH += char.health
		hisCharN += 1
		#GameTag.TAUNT
		if char.taunt:
			hisTauntCharH += char.health
	myMinionCardH = 0
	mySpellCardN = 0
	for card in me.hand:
		if card.type == CardType.MINION:
			myMinionCardH += card.health
		if card.type == CardType.SPELL:
			mySpellCardN += 1
	score = 0
	score += weight.mHH * myHeroH
	score += weight.hHH * hisHeroH
	score += weight.mCN * myCharN
	score += weight.mCH * myCharH
	score += weight.mTCH * myTauntCharH
	score += weight.hCN * hisCharN
	score += weight.hCH * hisCharH
	score += weight.hTCH * hisTauntCharH
	score += weight.mMCH * myMinionCardH
	score += weight.mSCN * mySpellCardN
	return score
def executePlay(card,target=None):
	if not card.is_playable():
		return ExceptionPlay.INVALID
	if target != None and target != card.targets:
		return ExceptionPlay.INVALID
	try:
		card.play(target=target)
	except GameOver:
		return ExceptionPlay.GAMEOVER
	return ExceptionPlay.VALID
def executeAttack(card,target):
	if not card.can_attack(target):
		return ExceptionPlay.INVALID
	try:
		card.attack(target)
	except GameOver:
		return ExceptionPlay.GAMEOVER
	return ExceptionPlay.VALID
class ExceptionPlay(IntEnum):
	VALID=0
	GAMEOVER=1
	INVALID=2
#
##  getActionCandidates
##
def getActionCandidates(mygame):
	player = mygame.current_player
	myCandidate = []
	for card in player.hand:
		if card.is_playable():
			target = None
			if card.must_choose_one:
				card = random.choice(card.choose_cards)#ここでカードが入れ替わるときの対応をしていない
			if card.requires_target():
				for target in card.targets:
					if card.is_playable():
						myCandidate.append(myAction(card, 'play', target))
			else:
				if card.is_playable():
					myCandidate.append(myAction(card, 'play', None))
	for character in player.characters:
		if character.can_attack():
			for target in character.targets:
				if character.can_attack(target):
					myH=character.health
					hisA=target.atk
					if myH > hisA:
						myCandidate.append(myAction(character, 'attack', target))
	return myCandidate
#
#  executeAction
#
def executeAction(game,action):
	player=game.current_player
	theCard=None
	theTarget=None
	if action.type=="play":
		for card in player.hand:
			if card==action.card:
				theCard=card
				if action.target != None:
					for target in theCard.targets:
						if target==action.target:
							theTarget=target
							return executePlay(theCard,theTarget)
				else:
					return executePlay(theCard)
	elif action.type=="attack":
		for character in player.characters:
			if character==action.card:
				theCard=character
				for target in theCard.targets:
					if target==action.target:	
						theTarget=target
						return executeAttack(theCard,theTarget)
	return ExceptionPlay.INVALID

def GenzoStep1(game: ".game.Game", myW):
	myWeight=myW
	myCandidate = getActionCandidates(game)
	myChoices = []
	maxScore=0
	maxChoice = None
	#print(">>>>>>>>>>>>>>>>>>>")
	for myChoice in myCandidate:
		tmpGame = copy.deepcopy(game)
		if executeAction(tmpGame, myChoice)==ExceptionPlay.GAMEOVER:
			score=100000
		else:
			if GenzoRandom(tmpGame)==ExceptionPlay.GAMEOVER:#ここをもっと賢くしてもよい
				score=100000
			else:
				score = getStageScore(tmpGame,myWeight)
		#print("-------------------")
		#print("%s %s %s %d"%(myChoice.card,myChoice.type,myChoice.target,score))
		#print("-------------------")
		if score > maxScore:
			maxScore = score
			myChoices = [myChoice]
		elif score == maxScore:
			myChoices.append(myChoice)
	#print("<<<<<<<<<<<<<<<<<<<")
	if len(myChoices)>0:
		ret = executeAction(game, random.choice(myChoices))
		if ret==ExceptionPlay.GAMEOVER:
			return ExceptionPlay.GAMEOVER
		if ret==ExceptionPlay.INVALID:
			return ExceptionPlay.INVALID
		player = game.current_player
		if player.choice:# ここは戦略に入っていない。
			choice = random.choice(player.choice.cards)
			print("Choosing card %r" % (choice))
			myChoiceStr = str(choice)
			if 'RandomCardPicker' in str(choice):
				myCardID =  random.choice(choice.find_cards())
				myCard = Card(myCardID)
				myCard.controller = player#?
				myCard.draw()
				player.choice = None
			else :
				player.choice.choose(choice)
		return GenzoRandom(game)
	else:
		return ExceptionPlay.VALID
#
#   Original random
#
def Original_random(game: ".game.Game"):
	player = game.current_player
	while True:
		for card in player.hand:
			if card.is_playable() and random.random() < 0.5:
				target = None
				if card.must_choose_one:
					card = random.choice(card.choose_cards)
				if card.requires_target():
					target = random.choice(card.targets)
				print("Playing %r on %r" % (card, target))
				executePlay(card,target)
				if player.choice:
					choice = random.choice(player.choice.cards)
					print("Choosing card %r" % (choice))
					myChoiceStr = str(choice)
					if 'RandomCardPicker' in str(choice):
						myCardID =  random.choice(choice.find_cards())
						myCard = Card(myCardID)
						myCard.controller = player#?
						myCard.draw()
						player.choice = None
					else :
						player.choice.choose(choice)
					continue
		# Randomly attack with whatever can attack
		for character in player.characters:
			if character.can_attack():
				target = random.choice(character.targets)
				executeAttack(character, target)
		break
def HumanInput(game):
	player = game.current_player
	while True:
		myCandidate = []
		print("HAND:")
		for card in player.hand:
			print(card, end=' : ')
			if card.data.type == CardType.MINION:
				print("%d(%d/%d)%s"%(card.data.cost, card.data.atk, card.data.health, card.data.description.replace('\n','')))
			elif card.data.type == CardType.SPELL:
				print("%d : %s"%(card.data.cost, card.data.description.replace('\n','')))
			if card.is_playable():
				target = None
				if card.must_choose_one:
					card = random.choice(card.choose_cards)
				if card.requires_target():
					for target in card.targets:
						myCandidate.append([card,"plays", target])
				else:
					myCandidate.append([card,"plays",None])
		print("OPPONENT'S PLAY:")
		for character in player.opponent.characters:
			print(character, end=':')
			print("(%d/%d)"%(character.atk,character.health))
		print("PLAY:")
		for character in player.characters:
			print(character, end=':')
			print("(%d/%d)"%(character.atk,character.health))
			if character.can_attack():
				for target in character.targets:
					if character.can_attack(target):
						myH=character.health
						hisA=target.atk
						#if myH > hisA:
						myCandidate.append([character,"attacks",target])
		print("Your turn:%d/%d mana"%(player.mana,player.max_mana))
		print("[0] ターンを終了する")
		myCount = 1
		for myChoice in myCandidate:
			print('[%d]'%myCount, end=' ')
			myCard = myChoice[0]
			print(myCard, end=' ')
			if myCard.data.type==CardType.MINION:
				print('%d(%d/%d)'%(myCard.cost, myCard.atk,myCard.health), end=' ')
			elif myCard.data.type==CardType.SPELL:
				print('%r'%(myCard.data.description.replace('\n','')), end=' ')
			myCard = myChoice[2]
			print('%s'%myChoice[1], end=' ')
			if myCard != None:
				print(myCard, end=' ')
				if myCard.data.type==CardType.MINION:
					print('(%d/%d)'%(myCard.atk,myCard.health), end=' ')
			myCount += 1
			print('')
		str = input()
		inputNum = int(str)
		if len(myCandidate)==0 or inputNum == 0:
			break;
		if inputNum>0 and inputNum<=len(myCandidate):
			myChoice = myCandidate[inputNum-1]
			if myChoice[1]=="plays":
				executePlay(myChoice[0], myChoice[2])
			elif myChoice[1]=="attacks":
				executeAttack(myChoice[0], myChoice[2])
			if player.choice:
				choice = random.choice(player.choice.cards)
				print("Choosing card %r" % (choice))
				myChoiceStr = str(choice)
				if 'RandomCardPicker' in str(choice):
					myCardID =  random.choice(choice.find_cards())
					myCard = Card(myCardID)
					myCard.controller = player#?
					myCard.draw()
					player.choice = None
				else :
					player.choice.choose(choice)
				continue

