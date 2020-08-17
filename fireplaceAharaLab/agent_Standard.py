import random
import numpy as np
import copy
from fireplace.exceptions import GameOver, InvalidAction
from fireplace.card import CardType
from fireplace.logging import log
from hearthstone.enums import CardClass, CardType,PlayState, Zone,State, GameTag#
from typing import List
from utils import myAction, myActionValue, ExceptionPlay, StandardStrategy
from fireplace.actions import Action
from fireplace.card import Card
from fireplace.game import Game
from enum import IntEnum

def StandardRandom(thisgame: ".game.Game"):
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
	myCharA = 0
	myCharH = 0
	myTauntCharH = 0
	for char in me.characters:
		myCharA += char.atk
		myCharH += char.health
		#GameTag.TAUNT
		if char.taunt:
			myTauntCharH += char.health
	hisCharA = 0
	hisCharH = 0
	hisTauntCharH = 0
	for char in he.characters:
		hisCharA += char.atk
		hisCharH += char.health
		#GameTag.TAUNT
		if char.taunt:
			hisTauntCharH += char.health
	MinionCH = 0#手持ちのミニョンカードのHPの総和
	SpellCN = 0#手持ちのスペルカードの枚数
	BattleCryCN = 0#雄叫びカードの枚数
	ChargeCN = 0#突撃カードの枚数
	WinduryCN = 0#疾風カードの枚数
	TauntCN = 0#挑発カードの枚数
	DamageCN = 0#ダメージカードの枚数
	GainCN = 0#獲得#回復カードの枚数
	SummonCN = 0#召喚カードの枚数
	LifeStealCN = 0#生命奪取カードの枚数
	GiveCN = 0#付与カードの枚数
	VanillaCN = 0#バニラカードの枚数
	for card in me.hand:
		des = card.data.description
		if card.type == CardType.MINION:
			MinionCH += card.health
		if card.type == CardType.SPELL:
			SpellCN += 1
		if '雄叫び' in des:
			BattleCryCN += 1
		if '突撃' in des:
			ChargeCN += 1
		if '疾風' in des:
			WinduryCN += 1
		if '挑発' in des:
			TauntCN += 1
		if 'ダメージ' in des:
			DamageCN += 1
		if '獲得' in des:
			GainCN+=1
		if '召喚' in des:
			SummonCN+=1
		if '生命奪取' in des:
			LifeStealCN+=1
		if '付与' in des:
			GiveCN+=1
		if len(des)<3:
			VanillaCN+=1
	score = 0
	score += weight.myHeroH * myHeroH
	score += weight.hisHeroH * hisHeroH
	score += weight.myCharA * myCharA
	score += weight.myCharH * myCharH
	score += weight.myTauntCharH * myTauntCharH
	score += weight.hisCharA * hisCharA
	score += weight.hisCharH * hisCharH
	score += weight.hisTauntCharH * hisTauntCharH
	score += weight.MinionCH * MinionCH
	score += weight.SpellCN * SpellCN
	score += weight.BattleCryCN*BattleCryCN
	score += weight.ChargeCN*ChargeCN
	score += weight.WinduryCN*WinduryCN
	score += weight.TauntCN*TauntCN
	score += weight.DamageCN*DamageCN
	score += weight.GainCN*GainCN
	score += weight.SummonCN*SummonCN
	score += weight.LifeStealCN*LifeStealCN
	score += weight.GiveCN*GiveCN
	score += weight.VanillaCN*VanillaCN
	#score += weight.
	return score
def executePlay(card,target=None):
	if not card.is_playable():
		return ExceptionPlay.INVALID
	if target != None and target not in card.targets:
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
#
##  getActionCandidates Standard version
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

def StandardStep1(game: ".game.Game", myW):
	myWeight=myW
	myCandidate = getActionCandidates(game)
	myChoices = []
	maxScore=-100000
	maxChoice = None
	#print(">>>>>>>>>>>>>>>>>>>")
	for myChoice in myCandidate:
		tmpGame = copy.deepcopy(game)
		if executeAction(tmpGame, myChoice)==ExceptionPlay.GAMEOVER:
			score=100000
		else:
			if StandardRandom(tmpGame)==ExceptionPlay.GAMEOVER:#ここをもっと賢くしてもよい
				score=100000
			else:
				score = getStageScore(tmpGame,myWeight)
		#print("-------------------")
		#print("%s %s %s %d"%(myChoice.card,myChoice.type,myChoice.target,score))
		#print("-------------------")
		if score > maxScore:
			maxScore = score
			myChoices = [myChoice]
			if score==100000:
				break
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
		return StandardRandom(game)
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

class Standard(object):
	"""
	Situation Vector with evolutionary calculation 
	"""
	def __init__(self, _weight, _name, _myClass, _hisClass, _rating):
		super(Standard, self).__init__()
		self.weight=_weight
		self.name=_name
		self.myClass=_myClass
		self.hisClass=_hisClass
		self.rating=_rating

	def __str__(self):
		return "%s(%s)<%s>"%(self.name,self.myClass,str(self.weight))

	def __eq__(self,obj):
		return str(self)==str(obj)

class StandardWeight(object):
	"""
	Weight for Standard agent
	"""
	def __init__(self, w):
		self.myHeroH = w[0]#自ヒーローのHPを増やす
		self.hisHeroH = w[1]#相手ヒーローのHPを減らす
		self.myCharA = w[2]#自分のフィールドにあるミニョンの攻撃力の総和を増やす
		self.myCharH = w[3]#自分のフィールドにあるミニョンのHPの総和を増やす
		self.myTauntCharH = w[4]#自分のフィールドにある挑発ミニョンのHPの総和を増やす
		self.hisCharA = w[5]#相手のフィールドにあるミニョンの攻撃力の総和を減らす
		self.hisCharH = w[6]#相手のフィールドにあるミニョンのHPの総和を減らす
		self.hisTauntCharH = w[7]#相手のフィールドにある挑発ミニョンのHPの総和を減らす
		self.MinionCH = w[8]#手持ちのミニョンのカードを使う
		self.SpellCN = w[9]#手持ちの呪文のカードを使う
		self.BattleCryCN = w[10]#雄叫びカードを使う
		self.ChargeCN = w[11]#突撃カードを使う
		self.WinduryCN = w[12]#疾風カードを使う
		self.TauntCN = w[13]#挑発カードを使う
		self.DamageCN = w[14]#ダメージカードを使う
		self.GainCN = w[15]#獲得#回復カードを使う
		self.SummonCN = w[16]#召喚カードを使う
		self.LifeStealCN = w[17]#生命奪取カードを使う
		self.GiveCN = w[18]#付与カードを使う
		self.VanillaCN = w[19]#バニラカードを使う

	def __str__(self):
		myText = str(self.myHeroH)+','
		myText += str(self.hisHeroH)+','
		myText += str(self.myCharA)+','
		myText += str(self.myCharH)+','
		myText += str(self.myTauntCharH)+','
		myText += str(self.hisCharA)+','
		myText += str(self.hisCharH)+','
		myText += str(self.hisTauntCharH)+','
		myText += str(self.MinionCH)+','
		myText += str(self.SpellCN)+','
		myText += str(self.BattleCryCN)+','
		myText += str(self.ChargeCN)+','
		myText += str(self.WinduryCN)+','
		myText += str(self.TauntCN)+','
		myText += str(self.DamageCN)+','
		myText += str(self.GainCN)+','
		myText += str(self.SummonCN)+','
		myText += str(self.LifeStealCN)+','
		myText += str(self.GiveCN)+','
		myText += str(self.VanillaCN)
		return myText

	def __eq__(self,obj):
		return self.name==obj.name 

	def deepcopy(self):
		import random
		wgt = [self.myHeroH,self.hisHeroH,self.myCharA,self.myCharH,\
		self.myTauntCharH,self.hisCharA,self.hisCharH,self.hisTauntCharH,\
		self.MinionCH,self.SpellCN,\
		self.BattleCryCN,self.ChargeCN,self.WinduryCN,self.TauntCN,\
		self.DamageCN,self.GainCN,self.SummonCN,self.LifeStealCN,\
		self.GiveCN,self.VanillaCN]
		return StandardWeight(wgt)

	def deepcopyAndPerturb(self):
		import random
		wgt = [self.myHeroH,self.hisHeroH,self.myCharA,self.myCharH,\
		self.myTauntCharH,self.hisCharA,self.hisCharH,self.hisTauntCharH,\
		self.MinionCH,self.SpellCN,\
		self.BattleCryCN,self.ChargeCN,self.WinduryCN,self.TauntCN,\
		self.DamageCN,self.GainCN,self.SummonCN,self.LifeStealCN,\
		self.GiveCN,self.VanillaCN]
		plus = random.randint(0,19)
		wgt[plus] += 3
		minus = random.randint(0,19)
		wgt[minus] -= 3
		if wgt[minus]<1 :
			wgt[minus]=1
		return StandardWeight(wgt)

