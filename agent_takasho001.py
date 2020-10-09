#### takashoのAI #####
import random
import numpy as np
import copy
from fireplace.exceptions import GameOver
from hearthstone.enums import CardClass, CardType#
from utils import Candidate, ExceptionPlay, getCandidates, executeAction
from fireplace.game import Game
from enum import IntEnum

from agent_Standard import postAction, StandardRandom

def takasho001AI(thisGame: Game,debugLog=True):
	# とりあえず