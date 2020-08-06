import random
from typing import List
import copy
from fireplace.exceptions import GameOver

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
		for card in player.hand:
			if card.is_playable():
				target = None
				if card.must_choose_one:
					card = random.choice(card.choose_cards)
				if card.requires_target():
					for target in card.targets:
						myCandidate.append([card,"play", target])
				else:
					myCandidate.append([card,"play",None])
		for character in player.characters:
			if character.can_attack():
				for target in character.targets:
					if character.can_attack(target):
						myH=character.health
						hisA=target.atk
						if myH > hisA:
							myCandidate.append([character,"attack",target])
		print("Your turn:")
		print("[0] : pass")
		myCount = 1
		for myChoice in myCandidate:
			print("[%d] : %r %r %r" % (myCount,myChoice[0],myChoice[1],myChoice[2]))
			myCount += 1
		str = input()
		inputNum = int(str)
		if len(myCandidate)==0 or inputNum == 0:
			break;
		if inputNum>0 and inputNum<=len(myCandidate):
			myChoice = myCandidate[inputNum-1]
			if myChoice[1]=="play":
				myChoice[0].play(target=myChoice[2])
			elif myChoice[1]=="attack":
				myChoice[0].attack(myChoice[2])
			if player.choice:
				choice = random.choice(player.choice.cards)
				print("Choosing card %r" % (choice))
				try:
					player.choice.choose(choice)
				except AttributeError:
					continue
				continue

