class Config:# ()is the default value

	HEARTHSTONE=1# ランク戦をするならこちら（バトグラより優先）
	BATTLEGROUNDS=0# バトグラをするならこちら
	CARDTEST=0# カードの動作テストをするならこちら
	CARDCLASS=1# カードクラス（core & hunter など）のカードの抽出するモード

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

	LOGINFO=1# log.info相当のログ表示
	LOGINFO_INDENT=">"
	LOGINFO_LOG=[]
	DEEPCOPY_LOGINFO=0
	PRINT_HITLOG=0 # Hitイベントを表示する

	#battlegrounds option
	PATCH_VERSION = 2360
	PATCH23_1 = 2310## 22年4月以前のレギュレーション（バディーあり）
	PATCH23_2_2 = 2322 ## 22年5月以降のレギュレーション（バディーなし）
	PATCH23_6 = 2360 ## 22年6月28日のレギュレーション

	PLAYER1_HUMAN=1 ##人間プレーヤーあり
	CARD_PRESET1=''
	CARD_PRESET2=''
	RANDOM_RACE=1 #プレーする種族をランダムに選ぶ（default:1）
	#['beast','demon','dragon','elemental','mecha','murloc','naga','pirate','quilboar']から選ぶ
	RACE_CHOICE=['pirate','quilboar','dragon']#RANDOM_RACE=0のときに有効
	HERO_1='' #人間プレーヤーはヒーローを指定できる
	HERO_2='' #人間プレーヤーはヒーローを指定できる

	ALL_PLAYERS_LOGINFO = 1 ## すべてのプレーヤーのバーにおけるムーブをテキスト表示する 

	
