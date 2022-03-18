import random
import copy
import pickle
from fireplace.exceptions import GameOver
from hearthstone.enums import CardType, BlockType, CardClass#
from utils import ExceptionPlay, Candidate, executeAction, getCandidates, postAction,Agent
from fireplace.actions import Action
from fireplace.card import Card
from fireplace.game import Game
from enum import IntEnum
import numpy as np


class QueenAgent(Agent):

	qtable = np.ones(6*6*11*11*2*2,20+1+1)

	def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000 ):
		super().__init__(myName, myFunction, myOption, myClass, rating )
		pass

	def QAI(self, thisgame, option=[], gameLog=[], debugLog=False):
		player = thisgame.current_player
		loopCount=0
		while loopCount<20:
			loopCount+=1
			myCandidate = getCandidates(thisgame)
			simpCan = self.classify_action(myCandidate)
			for x in simpCan:
				print(simpCan)

			if len(myCandidate)>0:
				myChoice = random.choice(myCandidate)
				exc = executeAction(thisgame, myChoice, debugLog=debugLog)
				postAction(player)
				if exc==ExceptionPlay.GAMEOVER:
					return ExceptionPlay.GAMEOVER
				else:
					continue
			return ExceptionPlay.VALID

	def classify_action(self, candidates):
		atkflag=False
		simpleCandidates =[]
		for  i in candidates:
			if i.type==BlockType.ATTACK:
				if not atkflag:
					simpleCandidates.append("attack")
					atkflag = True
				pass
			elif i.type==BlockType.PLAY:
				simpleCandidates.append(i.card.id)
				pass
			elif i.type==BlockType.POWER:
				simpleCandidates.append("power")
				pass
			else:
				pass
		return simpleCandidates
	def observe_state(self, game):

		me=game.current_player
		he=game.current_player.opponent
		a=min((me.hero.health+me.hero.armor-1)/5,5)
		b=min((he.hero.health+he.hero.armor-1)/5,5)
		c=game.turn/2
		d=me.mana
		if len(me.characters)>1:
			e=1
		if len(he.characters)>1:
			f=1
		s=[a,b,c,d,e,f]
		return s

class Qlearning:
	def __init__(self, num_states, num_actions):
		self.num_states = num_states
		self.num_actions = num_actions
		self.q_table = np.random.uniform(low=0, high=0, size=(NUM_DIGITIZE**self.num_states, self.num_actions))

	

	pass