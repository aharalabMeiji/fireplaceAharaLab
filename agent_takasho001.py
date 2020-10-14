#### takashoのAI #####
import random
import numpy as np
import copy
from fireplace.exceptions import GameOver
from hearthstone.enums import CardClass, CardType, BlockType#
from utils import Candidate, ExceptionPlay, getCandidates, executeAction
from fireplace.game import Game
from enum import IntEnum

from agent_Standard import postAction, StandardRandom


# とりあえず殴れるときに殴る形
def takasho001AI(thisGame: Game,option = [],debugLog=True):
	count = 0
	player=thisGame.current_player
	while True:
		myCandidates = getCandidates(thisGame)
		for choice in myCandidates:
			if choice.type==BlockType.PLAY and choice.card.type==CardType.MINION:
				executeAction(thisGame,choice)
				postAction(player)
				break
		count +=1
		if count >10:
			return