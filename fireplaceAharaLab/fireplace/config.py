# made by AharaLab

from enum import IntEnum

class Config(IntEnum):# ()内はデフォルト値
    HEROHPOPTION=30 #ヒーロー体力(30)
    FSFIXED=0 # 先攻と後攻を固定(0) YES:>0 NO:0
    P1MAXMANA=1 # 先攻マナ(1) 1~10
    P2MAXMANA=1 # 後攻マナ(1) 1~10
    P1HAND=3 # 先攻ハンド枚数(3) 0~10
    P2HAND=4 # 後攻ハンド枚数(4) ※コインを含む 1~10
    COIN=1 # 後攻にコインを与えるか(1) YES:>0 NO:0

    pass

