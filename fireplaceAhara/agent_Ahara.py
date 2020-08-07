import random
import numpy as np
import copy
from fireplace.exceptions import GameOver, InvalidAction
from fireplace.card import CardType
from fireplace.logging import log
from hearthstone.enums import CardClass, CardType,PlayState, Zone,State, GameTag#
from typing import List
from utils import Action, ActionValue

def AharaRandom(game: ".game.Game"):
	player = game.current_player
	while True:
		myCandidate = []
		for card in player.hand:
			if card.is_playable():
				target = None
				if card.must_choose_one:
					card = random.choice(card.choose_cards)
				if card.requires_target():
					for target in card.targets:
						myCandidate.append([card, target])
				else:
					myCandidate.append([card,None])
		if len(myCandidate) > 0:
			myChoice = random.choice(myCandidate)
			myChoice[0].play(target=myChoice[1])
			if player.choice:
				choice = random.choice(player.choice.cards)
				print("Choosing card %r" % (choice))
				try:
					player.choice.choose(choice)
				except AttributeError:
					continue
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
				try:
					myChoice[0].attack(myChoice[1])
				except InvalidAction:
					print("(Ahara)%s cannot attack %s"%(myChoice[0],myChoice[1]))
					continue
				continue
			else:
				return game
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
		if '挑発' in char.data.description:
			myTauntCharH += char.health
	hisCharH = 0
	hisCharN = 0
	hisTauntCharH = 0
	for char in he.characters:
		hisCharH += char.health
		hisCharN += 1
		#GameTag.TAUNT
		if '挑発' in char.data.description:
			hisTauntCharH += char.health
	myMinionCardH = 0
	mySpellCardN = 0
	for card in me.hand:
		if card.type == CardType.MINION:
			myMinionCardH += card.health
		if card.type == CardType.SPELL:
			mySpellCardN += 1
	myVector=[myHeroH, hisHeroH, myCharN, myCharH, myTauntCharH, hisCharN, hisCharH, hisTauntCharH, myMinionCardH, mySpellCardN]
	return np.dot(weight,myVector)
def getActionCandidates(game):
	player = game.current_player
	myCandidate = []
	for card in player.hand:
		if card.is_playable():
			target = None
			if card.must_choose_one:
				card = random.choice(card.choose_cards)
			if card.requires_target():
				for target in card.targets:
					myCandidate.append(Action(card, 'play', target))
			else:
				myCandidate.append(Action(card, 'play', None))
	for character in player.characters:
		if character.can_attack():
			for target in character.targets:
				if character.can_attack(target):
					myH=character.health
					hisA=target.atk
					if myH > hisA:
						myCandidate.append(Action(character, 'attack', target))
	return myCandidate
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
		theCard.play(target=theTarget)
	elif action.type=="attack":
		for character in player.characters:
			if character.can_attack():
				if character==action.card:
					theCard=character
					for target in theCard.targets:
						if target==action.target:	
							theTarget=target
		if theCard.can_attack(theTarget):
			theCard.attack(theTarget)
	return game

def AharaStep1(game: ".game.Game"):
	myWeight=[1,-1,1,1,1,-1,-1,-1,1,1]
	myCandidate = getActionCandidates(game)
	myChoices = []
	maxScore=0
	maxChoice = None
	print(">>>>>>>>>>>>>>>>>>>")
	for myChoice in myCandidate:
		tmpGame = copy.deepcopy(game)
		tmpGame = executeAction(tmpGame, myChoice)
		tmpGame = AharaRandom(tmpGame)#たぶん代入は不要、ここをもっと賢くしてもよい
		score = getStageScore(tmpGame,myWeight)
		print("-------------------")
		print("%s %s %s %d"%(myChoice.card,myChoice.type,myChoice.target,score))
		print("-------------------")
		if score > maxScore:
			maxScore = score
			myChoices = [myChoice]
		elif score == maxScore:
			myChoices.append(myChoice)
	print("<<<<<<<<<<<<<<<<<<<")
	if len(myChoices)>0:
		game = executeAction(game, random.choice(myChoices))
	return AharaRandom(game)
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
				card.play(target=target)
				if player.choice:
					choice = random.choice(player.choice.cards)
					print("Choosing card %r" % (choice))
					try:
						player.choice.choose(choice)
					except AttributeError:
						print("player cannot choose card %r" % (choice))
						continue
					continue
		# Randomly attack with whatever can attack
		for character in player.characters:
			if character.can_attack():
				target = random.choice(character.targets)
				try:
					character.attack(target)
				except AttributeError:
					print("(Player1)Attribute error when %s cannot attack %s"%(character,target))
					continue
				except InvalidAction:
					print("(Player1)%s cannot attack %s"%(character,target))
					continue
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
				myChoice[0].play(target=myChoice[2])
			elif myChoice[1]=="attacks":
				myChoice[0].attack(myChoice[2])
			if player.choice:
				choice = random.choice(player.choice.cards)
				print("Choosing card %r" % (choice))
				try:
					player.choice.choose(choice)
				except AttributeError:
					continue
				continue

