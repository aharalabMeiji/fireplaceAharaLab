from agent_Genzo import getActionCandidates
from enum import IntEnum
import random
import numpy as np
import copy
from fireplace.exceptions import GameOver, InvalidAction
from fireplace.card import CardType
from fireplace.logging import log
from hearthstone.enums import CardClass, CardType,PlayState, Zone,State, GameTag#
from typing import List
from utils import myAction, myActionValue
from fireplace.actions import Action
from fireplace.card import Card
from fireplace.game import Game

def agent_Hunter(game: Game,weight):
    #ハンター前提
    myCandidates =  getEstimatedActionCandidates(game)    
    pass

def getEstimatedActionCandidates(game: Game):
    myCandidate = getActionCandidates(game)
    myEstimation = []
    for myChoice in myCandidate:
        if myChoice.type=="play":
            #特記事項別にscoreを追加する。
            description = myChoice.card.description
            if "体力" in description and "回復" in description:
                #if some minion or the hero loses his health
                #then it has optional score
                pass
            if "挑発" in description:
                #if big minion is on the field
                #then this choice is positive
                pass

class HunterLocalStrategy(IntEnum):
    悪魔の相棒=1
    エースハンタークリーン=2
    血の伝令=3
    森林オオカミ=4
    追跡術=5
    魔力の一矢=6
    野獣の怒り=7
    ホタルチョウ=8
    連射=9
    封印されし玄室=10
    ドワーフの狙撃手=11
    三匹がキル=12
    露払い=13
    ジゴイノシシ=14
    カワイイ侵入者=15
    ヴォルパーティンガー=16
    圧倒=17
    歴死学の予習=18
    狩人の狙い=19
    ヘビの罠=20
    ミスディレクション=21
    凍結の罠=22
    照明弾=23
    爆発の罠=24
    狙撃=25
    腐肉食いのハイエナ=26
    感圧板=27
    フェーズストーカー=27
    蝕竜の息吹=28
    真新しいニオイ=29
    クズ拾いの工夫=30
    封印されしフェルモー=31
    群れの戦術=32
    殺しの命令=33
    獣の相棒=34
    イーグルホーンボウ=35
    必殺の一矢=36
