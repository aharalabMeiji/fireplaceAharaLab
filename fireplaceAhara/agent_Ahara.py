import random
from typing import List
import copy
from fireplace.exceptions import GameOver
from fireplace.card import CardType

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
				myChoice[0].attack(myChoice[1])
				continue
			else:
				break
def get_score_stage(game):
	me = game.current_player
	he = game.current_player.opponent
	myHero = me.hero
	hisHero = he.hero
	myHeroH = myHero.health
	hisHeroH = hisHero.health
	return myHeroH - hisHeroH
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
						continue
					continue
		# Randomly attack with whatever can attack
		for character in player.characters:
			if character.can_attack():
				character.attack(random.choice(character.targets))
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

