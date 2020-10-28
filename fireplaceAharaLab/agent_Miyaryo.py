import random
import numpy as np
import copy
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


exclude = ['CFM_672', 'CFM_621', 'CFM_095', 'LOE_076', 'BT_490']


class MiyaryoAgent(Agent):

    def __init__(self, myName: str, myFunction, myOption=[], myClass: CardClass = CardClass.HUNTER, rating=1000):
        super().__init__(myName, myFunction, myOption, myClass, rating)

    def MiyaryoAI(self, game, option=[], gameLog=[], debugLog=False):
        print("turn %d" % game.turn)
        player = game.current_player

        while True:
            tmpGame = copy.deepcopy(game)
            myCandidate = getCandidates(
                tmpGame, _smartCombat=False, _includeTurnEnd=True)  # 実行できることがらをリストで取得

            sScore = self.getBoardScore(tmpGame)

            if len(myCandidate) <= 1:  # 何もしないを選択した時
                myChoice = random.choice(myCandidate)  # ランダムに一つ選ぶ
                if myChoice.type == ExceptionPlay.TURNEND:
                    return
                return ExceptionPlay.INVALID
            else:
                eScore = self.primitiveMonte(tmpGame, myCandidate)
                mychoice = np.argmax(eScore)
                if myCandidate[mychoice].type == ExceptionPlay.TURNEND:
                    print("あえてターンエンド")
                    return
                executeAction(game, myCandidate[mychoice])
                postAction(player)
        return ExceptionPlay.VALID

    def primitiveMonte(self, _game: Game, _candidates: list):
        retScore = []
        player = _game.current_player
        for i in range(len(_candidates)):
            canScore = []
            for j in range(5):
                tmpGame = copy.deepcopy(_game)
                executeAction(tmpGame, _candidates[i],debugLog=False)
                postAction(player)
                while True:
                    tmpCandidates = getCandidates(
                        tmpGame, _smartCombat=False, _includeTurnEnd=True)
                    index = int(random.random()*len(tmpCandidates))
                    if tmpCandidates[index].type == ExceptionPlay.TURNEND:
                        break
                    else:
                        executeAction(tmpGame, tmpCandidates[index],debugLog=False)
                        postAction(player)
                canScore.append(self.getBoardScore(tmpGame))
            retScore.append(sum(canScore)/len(canScore))
        return retScore

    def getBoardScore(self, _game: Game):
        me = _game.current_player
        he = _game.current_player.opponent
        vLength = 34  # ベクトルの長さ
        v = [0] * vLength
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
                if getattr(char, 'spell_damage', 0): # int
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
                if getattr(char, 'spell_damage', 0): # int
                    v[28] += char.spell_damage
                # if char.spellburst:
                if getattr(char, 'windfury', 0):     # 追加攻撃回数(int)
                    v[29] += char.windfury*char.atk
        v[30] = me.hero.atk
        v[31] = he.hero.atk
        v[32] = len(me.hand)
        v[33] = len(he.hand)
        w = [1]*vLength
        for i in range(vLength):
            if i in [1, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 31, 33]:
                w[i] *= -1
        w[7] *= -1
        w[21] *= -1
        w[8] *= 0
        w[22] *= 0
        w[32] *= 0.5
        w[33] *= 0.5
        score = 0
        for i in range(vLength):
            score += v[i]*w[i]
        return score


def Miya_UCT(game: ".game.Game", option=[], debugLog=True):
    while True:
        player = game.current_player
        print("%s TurnStart" % player)
        copyTree = copy.deepcopy(game)
        player = copyTree.current_player
        # 探索編
        candidates = getCandidates(
            copyTree, _smartCombat=False, _includeTurnEnd=True)
        if len(candidates) == 1:
            print("len(candidates)==1  TurnEnd")
            return ExceptionPlay.VALID
            pass
        print("--------------------simulate start!!----------------")
        takingAction = tryUCT(copyTree, candidates, _trialPerTree=10)
        print("--------------------simulate end!!------------------")
        print(takingAction)
        # iterate over our hand and play whatever is playable

        if takingAction.type == ExceptionPlay.TURNEND:
            return ExceptionPlay.VALID
            pass
        exc = executeAction(game, takingAction)
        postAction(player)
        if exc == ExceptionPlay.GAMEOVER:
            return ExceptionPlay.GAMEOVER
        else:
            continue
    print("%s TurnEnd" % player)
    return ExceptionPlay.VALID
    pass


def tryUCT(_game, _candidates=[], _trialPerTree=10, _numOfTree=2):

    totalScores = []
    if len(_candidates) == 0:
        print("noCans")
        return
        pass
    if len(_candidates) == 1:
        return _candidates[0]
        pass
    for i in range(_numOfTree):
        # シミュレーション下準備
        # random_sampling
        copyGame = copy.deepcopy(_game)
        myPlayer = copyGame.current_player
        enemy = myPlayer.opponent
        handNum = len(enemy.hand)
        d = random_draft(enemy.hero, exclude)
        enemy.hand = CardList()
        enemy.deck = Deck()
        for item in d:
            enemy.card(item, zone=Zone.DECK)
            pass
        enemy.draw(count=handNum)
        # ゲーム木展開
        root = Node(copyGame, None, None, _candidates)
        for k in range(_trialPerTree):
            current_node = root
            while len(current_node.untriedMoves) == 0 and len(current_node.childNodes) != 0:
                current_node = current_node.selectChild()
            if len(current_node.untriedMoves) != 0:
                expanding_action = current_node.choose_expanding_action()
                current_node = current_node.expandChild(expanding_action)
            result = current_node.simulate()
            current_node.backPropagate(result)
        # print("childNodes")
        # print(root.childNodes)
        visitScores = list(map(lambda node: myActionValue(
            node.move, node.visits), root.childNodes))
        # print(visitScores)
        # print(totalScores)
        totalScores = addActionValues(totalScores, visitScores)
        print("totalScores")
        for item in totalScores:
            print(item.action)
            print("-->{score}".format(score=item.score))
            pass
    maxScore = max(
        list(map(lambda actionValue: actionValue.score, totalScores)))
    retAction = 0
    for item in totalScores:
        if item.score == maxScore:
            retAction = item.action
            pass
        pass
    print(retAction)
    return retAction
    pass


def addActionValues(original, additional):
    if len(original) == 0:
        return copy.deepcopy(additional)
        pass
    retList = copy.deepcopy(original)
    for item in retList:
        for add in additional:
            if item.action == add.action:
                item.score += add.score
                pass
            pass
        pass
    return retList
    pass


class Node(object):
    """docstring for Node"""

    def __init__(self, gameTree, move, parent, actions):
        super(Node, self).__init__()
        self.gameTree = gameTree
        self.move = move
        self.parent = parent
        self.childNodes = []
        self.wins = 0
        self.visits = 0
        self.untriedMoves = copy.deepcopy(actions)
        self.score = 0

    def selectChild(self):
        import math
        self.totalVisit = self.visits
        self.values = list(map(lambda node: node.wins/node.visits +
                               math.sqrt(math.log(self.totalVisit)/node.visits), self.childNodes))
        retNode = self.childNodes[self.values.index(max(self.values))]
        return retNode
        pass

    def expandChild(self, action):  # maya氏改訂版
        # print("expandChild-----------------------------")
        # print(action)
        self.expandingGame = copy.deepcopy(self.gameTree)
        exc = executeAction(self.expandingGame, action)
        postAction(self.expandingGame.current_player)
        if exc == ExceptionPlay.GAMEOVER:
            print("the game has been ended.")
            child = Node(self.expandingGame, action, self, [])
            self.childNodes.append(child)
            return child
            pass
        elif action.type == ExceptionPlay.TURNEND:
            self.expandingGame.end_turn()
            pass
        child = Node(self.expandingGame, action, self, getCandidates(
            self.expandingGame, _smartCombat=False, _includeTurnEnd=True))
        self.childNodes.append(child)
        return child

    def choose_expanding_action(self):
        index = int(random.random()*len(self.untriedMoves))
        return self.untriedMoves.pop(index)
        pass

    def simulate(self):
        return simulate_random_game(self.gameTree)
        pass

    def backPropagate(self, result=None):
        self.addVal = self.score
        if result is not None:
            self.addVal = result
            pass
        self.wins += self.addVal
        self.visits += 1
        if self.parent is None:
            pass
        else:
            self.parent.backPropagate(self.addVal)
        pass

    def setScore(self, _score):
        self.score = _score
        pass


def simulate_random_turn(game: ".game.Game"):
    player = game.current_player
    while True:
        simCandidates = getCandidates(
            game, _smartCombat=False, _includeTurnEnd=True)
        index = int(random.random()*len(simCandidates))
        if simCandidates[index].type is ExceptionPlay.TURNEND:
            try:
                game.end_turn()
                return ExceptionPlay.VALID
                pass
            except GameOver as over:
                return ExceptionPlay.INVALID
        exc = executeAction(game, simCandidates[index], debugLog=False)
        postAction(player)
        if exc == ExceptionPlay.GAMEOVER:
            return ExceptionPlay.GAMEOVER
        else:
            continue
            pass


def simulate_random_game(game, trial=1) -> "int":
    retVal = 0
    for i in range(trial):
        simulating_game = copy.deepcopy(game)
        winner = ""
        while True:
            gameState = simulate_random_turn(simulating_game)
            if simulating_game.state == State.COMPLETE:
                winner = judgeWinner(simulating_game)
                break
            if gameState == ExceptionPlay.INVALID:
                print("gameState==ExceptionPlay.INVALID")
                winner = judgeWinner(simulating_game)
                break
                pass
        if winner == "Miya":
            retVal += 1
        elif winner == "DRAW":
            retVal += 0.5
            pass
    return retVal
    pass


def judgeWinner(game):
    if game.current_player.playstate == PlayState.WON:
        return game.current_player.name
    if game.current_player.playstate == PlayState.LOST:
        return game.current_player.opponent.name
    return 'DRAW'
    pass
