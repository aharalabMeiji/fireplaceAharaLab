#### takashoのAI #####
import random
from utils import *
import numpy as np
import copy
from fireplace.exceptions import GameOver
from hearthstone.enums import CardClass, CardType#
from utils import Candidate, ExceptionPlay, getCandidates, executeAction
from fireplace.game import Game
from enum import IntEnum

from agent_Standard import postAction, StandardRandom





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
