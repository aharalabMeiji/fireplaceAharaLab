from agent_Genzo import getActionCandidates
from enum import IntEnum

def agent_Hunter(game,weight):
    #ハンター前提
    myCandidate = getActionCandidates(game)
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
