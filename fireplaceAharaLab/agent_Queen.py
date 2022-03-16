import random
import copy
from fireplace.exceptions import GameOver
from hearthstone.enums import CardType, BlockType, CardClass#
from utils import ExceptionPlay, Candidate, executeAction, getCandidates, postAction,Agent
from fireplace.actions import Action
from fireplace.card import Card
from fireplace.game import Game
from enum import IntEnum
import numpy as np


class QueenAgent(Agent):
	def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000 ):
		super().__init__(myName, myFunction, myOption, myClass, rating )
		pass

	def QAI(self, thisgame, option=[], gameLog=[], debugLog=False):
		player = thisgame.current_player
		loopCount=0
		while loopCount<20:
			loopCount+=1
			myCandidate = getCandidates(thisgame)
			if len(myCandidate)>0:
				myChoice = random.choice(myCandidate)
				exc = executeAction(thisgame, myChoice, debugLog=debugLog)
				postAction(player)
				if exc==ExceptionPlay.GAMEOVER:
					return ExceptionPlay.GAMEOVER
				else:
					continue
			return ExceptionPlay.VALID

class Qlearning:
    def __init__(self, num_states, num_actions):
        self.num_states = num_states
        self.num_actions = num_actions
        self.q_table = np.random.uniform(low=0, high=0, size=(NUM_DIGITIZE**self.num_states, self.num_actions))

    def classify_action():


    pass

def 