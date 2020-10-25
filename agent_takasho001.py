#### takashoのAI #####
import random
from utils import *
import numpy as np
import copy
from fireplace.exceptions import GameOver
from hearthstone.enums import CardClass, CardType, BlockType#
from utils import Candidate, ExceptionPlay, getCandidates, executeAction
from fireplace.game import Game
from enum import IntEnum

from agent_Standard import postAction, StandardRandom


<<<<<<< HEAD



class agent_takasho(Agent):    
     def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000 ):
          super().__init__(myName, myFunction, myOption, myClass, rating )
     def agent_takasho001(game: Game, option=[], gameLog=[], debugLog=False):
          while True:
			  myCandidates = getCandidates(Game)
               for choice in myCandidates:
				   if choice.type==BlockType.ATTACK and choice.target==player.opponent.hero:
					   executeAction(choice)
					   postAction(player)
					   break
					else:
						return
=======
# とりあえず殴れるときに殴る形
def takasho001AI(thisGame: Game,option = [],debugLog=True):

	player=thisGame.current_player
	min = 30
	while True:
		myCandidates = getCandidates(thisGame,_includeTurnEnd=False)
		if len(myCandidates) == 0:
			return
		for choice in myCandidates:
			tmpGame = copy.deepcopy(thisGame)
			#if choice.type==BlockType.PLAY and choice.card.type==CardType.MINION:
			executeAction(tmpGame,choice,debugLog=False)
			postAction(player)
			choice.score = tmpGame.current_player.opponent.hero.health
		
		
		myChoice = None
		for choice in myCandidates:
			if min >= choice.score:
				min = choice.score
				myChoice = choice
				print(min)
		executeAction(thisGame,myChoice,debugLog=True)
		postAction(player)
		if thisGame.current_player.opponent.hero.health ==0:
			print("かち！")
			return
		#if choice.type ==ExceptionPlay.TURNEND:#何もしないを選択したとき
		#	return

>>>>>>> 183098521aabb8043ad4dfba77b19b13119a636e
