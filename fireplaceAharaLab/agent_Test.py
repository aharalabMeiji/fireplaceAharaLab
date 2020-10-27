import random
from utils import *
import numpy as np
import copy
from fireplace.exceptions import GameOver
from hearthstone.enums import CardType, BlockType, CardClass
from fireplace.actions import Action
from fireplace.card import Card
from fireplace.game import Game
from enum import IntEnum


class TestAgent(Agent):
    def __init__(self, myName: str, myFunction, myOption=[], myClass: CardClass = CardClass.HUNTER, rating=1000):
        super().__init__(myName, myFunction, myOption, myClass, rating)

    def TestAI(game: Game, option=[], gameLog=[], debugLog=False):
        player = game.current_player
        while True:
            tmp = Card("GVG_111t").data
            print(dir(tmp))
            myCandidate = getCandidates(game)  # 実行できることがらをリストで取得
            for char in player.characters:
                print(char.id)
            if len(myCandidate) > 0:
                myChoice = random.choice(myCandidate)  # ランダムに一つ選ぶ
                if myChoice.type == ExceptionPlay.TURNEND:  # 何もしないを選択したとき
                    return
                executeAction(game, myChoice, debugLog=debugLog)  # 選択したものを実行
                postAction(player)  # 後処理
            else:
                return


# fpath = 'test.txt'
#             with open(fpath, mode='w') as f:
#                 for d in tmp:
#                     f.write(d)
