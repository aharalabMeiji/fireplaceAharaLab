#StandardStep2

import random
import numpy as np
import copy
from fireplace.exceptions import GameOver
from hearthstone.enums import CardClass#
from utils import Candidate, ExceptionPlay, getCandidates, executeAction
from fireplace.game import Game
from enum import IntEnum

from agent_Standard import postAction


def getHisWorth(thisGame: Game):
	Vec = []
	His = thisGame.current_player.opponent
	Vec.append(His.hero.health)
	hisCharA = 0
	hisCharH = 0
	hisTauntCharH = 0
	for char in His.characters:
		hisCharA += char.atk
		hisCharH += char.health
		#GameTag.TAUNT
		if char.taunt:
			hisTauntCharH += char.health
	Vec.append(hisCharA)
	Vec.append(hisCharH)
	Vec.append(hisTauntCharH)
	My=thisGame.current_player
	myCharA = hisCharA
	myCharH = hisCharH
	myTauntCharH = hisTauntCharH
	for char in My.characters:
		myCharA -= char.atk
		myCharH -= char.health
		#GameTag.TAUNT
		if char.taunt:
			myTauntCharH -= char.health
	Vec.append(myCharA)
	Vec.append(myCharH)
	Vec.append(myTauntCharH)
	return Vec

def getDiffHisWorth(thisGame: Game, myChoice: Candidate):
	oldVec = getHisWorth(thisGame)
	newGame = copy.deepcopy(thisGame)
	executeAction(newGame,myChoice, debugLog=False)
	newVec = getHisWorth(newGame)
	answer=[]
	for i in range (len(oldVec)):
		answer.append(newVec[i]-oldVec[i])
	return answer

def getNegativity(Vec):
	hisMin=10
	hisNegative=0
	hisBigNegative=0
	for i in range(len(Vec)):
		if Vec[i]<0:
			hisNegative += 1
		if Vec[i]<-2:
			hisBigNegative += 1
		if Vec[i]<hisMin:
			hisMin = Vec[i]
	return hisMin, hisNegative, hisBigNegative

def AngryCatAI(thisGame: Game, option=[], debugLog=True):
	while True:
		myCandidates = getCandidates(thisGame)
		if len(myCandidates)==0:
			return
		else:
			myChoice1=myChoice2=myChoice3=[]
			M1=M2=M3=0
			for myChoice in myCandidates:
				hisMin, myPositive, myBigPositive = getNegativity(getDiffHisWorth(thisGame, myChoice)) 
				myMax = -hisMin
				if M1<myMax:
					M1=myMax
					myChoice1=[myChoice]
				elif M1>0 and M1==myMax:
					myChoice1.append(myChoice)
				if M2<myPositive:
					M2=myPositive
					myChoice2=[myChoice]
				elif M2>0 and M2==myPositive:
					myChoice2.append(myChoice)
				if M3<myBigPositive:
					M3=myBigPositive
					myChoice3=[myChoice]
				elif M3>0 and M3==myBigPositive:
					myChoice3.append(myChoice)
			myChoices = myChoice1+myChoice2+myChoice3
			if len(myChoices)==0:
				return
			else:
				myChoice = random.choice(myChoices)
				executeAction(thisGame, myChoice, debugLog=True)
				postAction(thisGame.current_player)

