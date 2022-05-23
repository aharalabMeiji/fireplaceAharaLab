#from enum import IntEnum

class Config:# ()is the default value

	HEARTHSTONE=0# ランク戦をするならこちら（バトグラより優先）
	BATTLEGROUNDS=1# バトグラをするならこちら
	CARDTEST=0# カードの動作テストをするならこちら

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

	LOGINFO=0# log.info相当のログ表示
	DEEPCOPY_LOGINFO=0

	#battlegrounds option
	PATCH23_2_2 = 1 ## 22年5月以降のレギュレーション（バディーなし）

	HUMAN_PLAY=1 ##人間プレーヤーあり
	CARD_PRESET=1 # 人間プレーヤーに最初からカードを与える
	CARD_PRESET1=''
	CARD_PRESET2=''
	RANDOM_RACE=1 #プレーする種族をランダムに選ぶ（default:1）
	#['beast','demon','dragon','elemental','mecha','murloc','naga','pirate','quilboar']から選ぶ
	RACE_CHOICE=['pirate','quilboar','elemental']
	HERO_1=18 #人間プレーヤーはヒーローを指定できる(0~78)
	HERO_2=41 #人間プレーヤーはヒーローを指定できる(0~78)

	#00#A. F. Kay, #HP#BUDDY
	#01#Al'Akir#HP#BUDDY
	#02#Alexstrasza #HP#BUDDY
	#03#Ambassador Faelin #HP#BUDDY
	#04#Aranna Starseeker #HP#BUDDY
	#05#Arch-Villain Rafaam  #HP#BUDDY
	#06#Bru'kan
	#07#C'Thun
	#08#Captain Eudora
	#09#Captain Hooktusk
	#10#Cariel Roame  #HP#BUDDY
	#11#Chenvaala
	#12#Cookie the Cook
	#13#Dancin' Deryl  #HP#BUDDY
	#14#Death Speaker Blackthorn
	#15#Deathwing    #HP#BUDDY
	#16#Dinotamer Brann
	#17#Drek'Thar ### HP
	#18#Edwin VanCleef ### HP
	#19#Elise Starseeker
	#20#Forest Warden Omu
	#21#Fungalmancer Flurgl
	#22#Galakrond
	#23#Galewing
	#24#George the Fallen
	#25#Greybough
	#26#Guff Runetotem
	#27#Illidan Stormrage
	#28#Infinite Toki
	#29#Jandice Barov
	#30#Kael'thas Sunstrider
	#31#King Mukla
	#32#Kurtrus Ashfallen
	#33#Lich Baz'hial
	#34#Lord Barov
	#35#Lord Jaraxxus ### HP
	#36#Maiev Shadowsong ### HP
	#37#Malygos ### HP
	#38#Master Nguyen
	#39#Millhouse Manastorm ### HP
	#40#Millificent Manastorm ### HP
	#41#Mr. Bigglesworth
	#42#Mutanus the Devourer
	#43#N'Zoth
	#44#Nozdormu
	#45#Onyxia
	#46#Overlord Saurfang
	#47#Patches the Pirate
	#48#Patchwerk
	#49#Pyramad
	#50#Queen Wagtoggle
	#51#Ragnaros the Firelord
	#52#Rakanishu  ### HP
	#53#Reno Jackson  ### HP
	#54#Rokara  ### HP
	#55#Scabbs Cutterbutter  ### HP
	#56#Shudderwock
	#57#Silas Darkmoon ### HP
	#58#Sindragosa ### HP
	#59#Sir Finley Mrrgglton ### HP
	#60#Skycap'n Kragg ### HP
	#61#Sneed ### HP
	#62#Tamsin Roame ### HP
	#63#Tavish Stormpike ### HP
	#64#Tess Greymane ### HP
	#65#The Curator ### HP
	#66#The Great Akazamzarak ### HP
	#67#The Lich King ###HP
	#68#The Rat King ### HP
	#69#Tickatus #HP
	#70#Trade Prince Gallywix ## HP
	#71#Vanndar Stormpike ## HP 
	#72#Varden Dawngrasp ## HP 
	#73#Vol'jin  ### HP 
	#74#Xyrella  ### HP 
	#75#Y'Shaarj  ### HP
	#76#Yogg-Saron, Hope's End  ### HP
	#77#Ysera  ### HP
	#78#Zephrys, the Great  ### HP