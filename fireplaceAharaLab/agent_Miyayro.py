from __future__ import print_function
from sys import getsizeof, stderr
import random
import numpy as np
import copy
import time
import cProfile
import gc
import sys
from fireplace.exceptions import GameOver
from hearthstone.enums import CardType, BlockType
from utils import *
from hearthstone.enums import CardClass, CardType, PlayState, Zone, State
from fireplace.actions import Action
from fireplace.card import Card
from fireplace.game import Game
from fireplace.utils import random_draft, CardList
from enum import IntEnum
from fireplace.deck import Deck
from itertools import chain
from collections import deque
try:
    from reprlib import repr
except ImportError:
    pass


def total_size(o, handlers={}, verbose=False):
    # with open('file.txt', 'a') as stderr:
    # print("始まり", file=stderr)
    """ Returns the approximate memory footprint an object and all of its contents.
    Automatically finds the contents of the following builtin containers and
    their subclasses:  tuple, list, deque, dict, set and frozenset.
    To search other containers, add handlers to iterate over their contents:
        handlers = {SomeContainerClass: iter,
                    OtherContainerClass: OtherContainerClass.get_elements}
    """
    def dict_handler(d): return chain.from_iterable(d.items())
    all_handlers = {tuple: iter,
                    list: iter,
                    deque: iter,
                    dict: dict_handler,
                    set: iter,
                    frozenset: iter,
                    }
    all_handlers.update(handlers)     # user handlers take precedence
    seen = set()                      # track which object id's have already been seen
    default_size = getsizeof(0)       # estimate sizeof object without __sizeof__

    def sizeof(o):
        if id(o) in seen:       # do not double count the same object
            return 0
        seen.add(id(o))
        s = getsizeof(o, default_size)

        if verbose:
            with open('file.txt', 'a') as stderr:
                print(s, type(o), repr(o))  # , file=stderr)

        for typ, handler in all_handlers.items():
            if isinstance(o, typ):
                s += sum(map(sizeof, handler(o)))
                break
            else:
                if not hasattr(o.__class__, '__slots__'):
                    if hasattr(o, '__dict__'):
                        # no __slots__ *usually* means a __dict__, but some special builtin classes (such as `type(None)`) have neither
                        s += sizeof(o.__dict__)
                        # else, `o` has no attributes at all, so sys.getsizeof() actually returned the correct value
                else:
                    s += sum(sizeof(getattr(o, x))
                             for x in o.__class__.__slots__ if hasattr(o, x))
        return s

    return sizeof(o)


exclude = ['CFM_672', 'CFM_621', 'CFM_095', 'LOE_076', 'BT_490']


class MiyaryoAgent(Agent):

    vLength = 38  # ベクトルの長さ
    w = np.array([1, -1, 1, 1, 1, 1, 1, -1, 0, 1, 1, 1, 1, 1, 1, 1, -1, -1, -
                  1, -1, -1, 1, 0, -1, -1, -1, -1, -1, -1, -1, 2, -2, 4, -8, 1, -1, 0.5, -0.5])
    lethal = False
    DebugLog = True
    start = None

    def __init__(self, myName: str, myFunction, myOption=[], myClass: CardClass = CardClass.HUNTER, rating=1000):
        super().__init__(myName, myFunction, myOption, myClass, rating)

    def MiyaryoAI(self, game, option=[], gameLog=[], debugLog=False):
        self.start = time.time()
        self.DebugLog = debugLog
        player = game.current_player
        if self.DebugLog:
            print("turn %d" % game.turn)
            print(f"秘策数{len(player.secrets)}")
            print(f"相手秘策数{len(player.opponent.secrets)}")
        self.lethal = False
        while True:
            # print(total_size(game.get_log()))
            # print(f"ログの長さ{len(game.get_log())}")
            copystart = time.time()
            tmpGame = copy.deepcopy(game)
            # print(f"elapsed_time:{time.time()-copystart}")
            # print(total_size(tmpGame,verbose = True))
            myCandidate = getCandidates(
                game, _smartCombat=False, _includeTurnEnd=True)  # 実行できることがらをリストで取得

            if len(myCandidate) <= 1:  # 何もしないを選択した時
                myChoice = random.choice(myCandidate)  # ランダムに一つ選ぶ
                if myChoice.type == ExceptionPlay.TURNEND:
                    return
                return ExceptionPlay.INVALID
            else:
                # print(f"モンテ前{total_size(game.get_log())}")
                finalScores = self.primitiveMonte(tmpGame, myCandidate)
                # finalScores = np.random.randint(10, size=len(myCandidate))
                # print(f"モンテ後{total_size(game.get_log())}")
                if isinstance(finalScores, str):
                    self.StandardRandom(game,debugLog=self.DebugLog)
                    return ExceptionPlay.VALID
                elif isinstance(finalScores, int):
                    mychoice = finalScores
                    self.lethal = True
                else:
                    if len(player.opponent.secrets):
                        finalScores = finalScores[:len(finalScores)-1]
                    mychoice = np.argmax(finalScores)
                if myCandidate[mychoice].type == ExceptionPlay.TURNEND:
                    print("あえてターンエンド")
                    return ExceptionPlay.VALID
                act = myCandidate[mychoice]
                # print(f"アクションサイズ{total_size(myCandidate[mychoice])}")
                executeAction(game, act, debugLog=debugLog)
                postAction(player)
                if self.lethal == True:
                    return ExceptionPlay.VALID
        return ExceptionPlay.VALID

    def primitiveMonte(self, montegame: Game, _candidates: list):
        retScore = np.empty(0)
        player = montegame.current_player
        beforeScore = self.getBoardScore(montegame)
        for i in range(len(_candidates)):
            if time.time()-self.start > 28:
                print("時間切れ")
                return "over"
            canScore = np.empty((0, self.vLength))
            for j in range(5):
                if _candidates[i].type == ExceptionPlay.TURNEND:
                    canScore = np.append(canScore, [beforeScore], axis=0)
                    continue
                start = time.time()
                tmGame = copy.deepcopy(montegame)
                # print(f"elapsed_time:{time.time()-start}")
                executeAction(tmGame, _candidates[i], debugLog=False)
                postAction(player)
                if tmGame.current_player.opponent.hero.health <= 0:
                    return i
                while True:
                    tmpCandidates = getCandidates(
                        tmGame, _smartCombat=False, _includeTurnEnd=True)
                    index = int(random.random()*len(tmpCandidates))
                    if tmpCandidates[index].type == ExceptionPlay.TURNEND:
                        break
                    else:
                        executeAction(
                            tmGame, tmpCandidates[index], debugLog=False)
                        postAction(player)
                canScore = np.append(
                    canScore, [self.getBoardScore(tmGame)], axis=0)
            calcedScore = self.calcScore(
                beforeScore, np.mean(canScore, axis=0), self.lethal)
            if self.DebugLog:
                print(f"_{i}_{_candidates[i]}", end='')
                print(f'--> {calcedScore:.3f}')
            retScore = np.append(retScore, calcedScore)
        return retScore
        pass

    def calcScore(self, _before, _after, _lethal):
        tmpW = np.copy(self.w)
        # if self.DebugLog:
        #     print(f"before{_before}")
        #     print(f"after{_after}")
        # print(f"w{tmpW}")
        retScore = np.sum((_after - _before) * tmpW)
        return retScore
        pass

    def getBoardScore(self, _game: Game):
        me = _game.current_player
        he = _game.current_player.opponent
        v = np.zeros(self.vLength)
        v[0] = me.hero.health
        v[1] = he.hero.health
        for char in me.characters:
            if char.type == CardType.MINION:
                v[2] += char.atk
                v[3] += char.health
                if getattr(char, 'taunt', 0):
                    v[4] += char.health
                # if char.battlecry:
                if getattr(char, 'deathrattles', 0):
                    v[5] += 1
                # if char.discover:
                if getattr(char, 'divine_shield', 0):
                    v[6] += 1
                # if char.dormant:
                # if char.echo:
                if getattr(char, 'forgetful', 0):
                    v[7] += 1
                if getattr(char, 'immune', 0):
                    v[8] += 1
                if getattr(char, 'has_inspire', 0):
                    v[9] += 1
                if getattr(char, 'lifesteal', 0):
                    v[10] += 1
                # if char.magnetic:
                # if char.outcast:
                if getattr(char, 'overkill', 0):
                    v[11] += 1
                # if char.overload:
                if getattr(char, 'poisonous', 0):
                    v[12] += 1
                if getattr(char, 'reborn', 0):
                    v[13] += 1
                # if char.rush:
                if getattr(char, 'spell_damage', 0):  # int
                    v[14] += char.spell_damage
                # if char.spellburst:
                if getattr(char, 'windfury', 0):     # 追加攻撃回数(int)
                    v[15] += char.windfury
        for char in he.characters:
            if char.type == CardType.MINION:
                v[16] += char.atk
                v[17] += char.health
                if getattr(char, 'taunt', 0):
                    v[18] += char.health
                # if char.battlecry:
                if getattr(char, 'deathrattles', 0):
                    v[19] += 1
                # if char.discover:
                if getattr(char, 'divine_shield', 0):
                    v[20] += 1
                # if char.dormant:
                # if char.echo:
                if getattr(char, 'forgetful', 0):
                    v[21] += 1
                if getattr(char, 'immune', 0):
                    v[22] += 1
                if getattr(char, 'has_inspire', 0):
                    v[23] += 1
                if getattr(char, 'lifesteal', 0):
                    v[24] += 1
                # if char.magnetic:
                # if char.outcast:
                if getattr(char, 'overkill', 0):
                    v[25] += 1
                # if char.overload:
                if getattr(char, 'poisonous', 0):
                    v[26] += 1
                if getattr(char, 'reborn', 0):
                    v[27] += 1
                # if char.rush:
                if getattr(char, 'spell_damage', 0):  # int
                    v[28] += char.spell_damage
                # if char.spellburst:
                if getattr(char, 'windfury', 0):     # 追加攻撃回数(int)
                    v[29] += char.windfury*char.atk
        for char in me.characters:
            if char.type == CardType.MINION:
                des = char.data.description
                if '[x]' in des and not ':' in des:
                    v[30] += char.health
        for char in he.characters:
            if char.type == CardType.MINION:
                des = char.data.description
                if '[x]' in des and not ':' in des:
                    v[31] += char.health
        v[32] = len(me.secrets)
        v[33] = len(he.secrets)
        v[34] = me.hero.atk
        v[35] = he.hero.atk
        v[36] = len(me.hand)
        v[37] = len(he.hand)
        return v
        pass

    def checkLethal(self, _game):
        totalAttack = 0
        totalTauntHealth = 0
        me = _game.current_player
        he = _game.current_player.opponent
        for char in me.characters:
            if char.can_attack():
                totalAttack += char.atk
        for char in he.characters:
            if char.taunt:
                totalTauntHealth += char.health
        if totalAttack - he.hero.health - totalTauntHealth >= 0:
            return True
        else:
            return False
        pass

    def StandardRandom(self, thisgame: ".game.Game", option=[], gameLog=[], debugLog=False):
        player = thisgame.current_player
        loopCount = 0
        while loopCount < 20:
            loopCount += 1
            myCandidate = getCandidates(thisgame)
            if len(myCandidate) > 0:
                myChoice = random.choice(myCandidate)
                exc = executeAction(thisgame, myChoice, debugLog=debugLog)
                postAction(player)
                if exc == ExceptionPlay.GAMEOVER:
                    return ExceptionPlay.GAMEOVER
                else:
                    continue
            return ExceptionPlay.VALID