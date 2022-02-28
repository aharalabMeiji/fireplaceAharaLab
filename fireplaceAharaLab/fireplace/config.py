# made by AharaLab

from enum import IntEnum

class Config(IntEnum):# ()is the default value
    FSFIXED=0 # fixing first and second (先攻と後攻を固定) YES:>0 NO:0(0) 
    COIN=1 # giving a coin to the second (後攻にコインを与えるか) YES:>0 NO:0(1)
    EX_CARD=1 # giving an extra ard to the second (後攻にカードを与えるか) YES:>0 NO:0(1)
    # 以下はplay_set_of_games()のオプションへ移動
    #HEROHPOPTION=30 #ヒーロー体力(30)
    #P1MAXMANA=1 # 先攻マナ(1) 1~10
    #P2MAXMANA=1 # 後攻マナ(1) 1~10
    #P1HAND=3 # 先攻ハンド枚数(3) 1~9 
    #P2HAND=3 # 後攻ハンド枚数(3) 1~9 ※コインは含まない


