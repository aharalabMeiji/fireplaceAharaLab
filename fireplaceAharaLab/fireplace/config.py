# made by AharaLab

from enum import IntEnum

class Config(IntEnum):# ()内はデフォルト値
    HEROHPOPTION=10 #ヒーロー体力(30)
    FSFIXED=1 # 先攻と後攻を固定(0) YES:>0 NO:0
    P1MAXMANA=10 # 先攻マナ(1)
    P2MAXMANA=1 # 後攻マナ(1)
    P1HAND=3 # 先攻ハンド枚数(3)
    P2HAND=2 # 後攻ハンド枚数(4) ※コインを含む
    COIN=1 # 後攻にコインを与えるか(1) YES:>0 NO:0

    pass

