#from enum import IntEnum

class Config:# ()is the default value

    HEARTHSTONE=0# ランク戦をするならこちら
    BATTLEGROUNDS=1# バトグラをするならこちら
    CARDTEST=0

    #ランク戦のオプション
    FSFIXED=0 # fixing first and second (先攻と後攻を固定) YES:>0 NO:0(0) 
    COIN=1 # giving a coin to the second (後攻にコインを与えるか) YES:>0 NO:0(1)
    EX_CARD=1 # giving an extra ard to the second (後攻にカードを与えるか) YES:>0 NO:0(1)
    # 以下はplay_set_of_games()のオプションへ移動
    #HEROHPOPTION=30 #ヒーロー体力(30)
    #P1MAXMANA=1 # 先攻マナ(1) 1~10
    #P2MAXMANA=1 # 後攻マナ(1) 1~10
    #P1HAND=3 # 先攻ハンド枚数(3) 1~9 
    #P2HAND=3 # 後攻ハンド枚数(3) 1~9 ※コインは含まない

    LOGINFO=1 # log.info相当のログ表示
    DEEPCOPY_LOGINFO=0

    #battlegrounds option
    CARD_PRESET=1 # 人間プレーヤーに最初からカードを与える
    CARD_PRESET1='BGS_055'
    CARD_PRESET2='NEW1_027'
    BAN_RACE=1 #BANする種族をランダムに選ぶ（default:1）
    HERO_1=10 #人間プレーヤーはヒーローを指定できる(0~78)
    HERO_2=28 #人間プレーヤーはヒーローを指定できる(0~78)
