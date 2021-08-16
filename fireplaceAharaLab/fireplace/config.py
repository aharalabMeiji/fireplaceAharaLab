# made by AharaLab

from enum import IntEnum

class Config(IntEnum):# ()内はデフォルト値
    FSFIXED=0 # 先攻と後攻を固定(0) YES:>0 NO:0
    COIN=1 # 後攻にコインを与えるか(1) YES:>0 NO:0
    EX_CARD=1 # 後攻にカードを与えるか(1) YES:>0 NO:0
    # 以下はplay_set_of_games()のオプションへ移動
    #HEROHPOPTION=30 #ヒーロー体力(30)
    #P1MAXMANA=1 # 先攻マナ(1) 1~10
    #P2MAXMANA=1 # 後攻マナ(1) 1~10
    #P1HAND=3 # 先攻ハンド枚数(3) 1~9 
    #P2HAND=4 # 後攻ハンド枚数(4) 1~9 ※コインは含まない


