class Config:# ()is the default value

	HEARTHSTONE=5
	#1: Hearthstone standard battle
	#2: Hearthstone classic cards
	#3: Hearthstone battleground

	#4: Checking a specific card for debugging
	#5: List up cards data (to build a new cards file.)
	#10: Decoding from a 'deckcode' to list of cards.

	#ランク戦のオプション
	FSFIXED=0 # fixing first and second YES:>0 NO:0(0) #(先攻と後攻を固定) 
	COIN=1 # giving a coin to the second  YES:>0 NO:0(1) #(後攻にコインを与えるか)
	EX_CARD=1 # giving an extra ard to the second  YES:>0 NO:0(1) #(後攻にカードを与えるか)
	# options of play_set_of_games()
	#HEROHPOPTION=30 #ヒーロー体力(30)
	#P1MAXMANA=1 # 先攻マナ(1) 1~10
	#P2MAXMANA=1 # 後攻マナ(1) 1~10
	#P1HAND=3 # 先攻ハンド枚数(3) 1~9 
	#P2HAND=3 # 後攻ハンド枚数(3) 1~9 ※コインは含まない

	LOGINFO=1# as log.info
	LOGINFO_INDENT=0
	def log(function, message):
		if Config.LOGINFO_INDENT>0:
			for repeat in range(Config.LOGINFO_INDENT):
				print("====>", end="")
		print("( %s )"%(function), end="")
		print(" %s"%(message))
	DEEPCOPY_LOGINFO=0

	#4: Checking a specific card for debugging
	CARD_TEST_SET='CORE'
	## VANILLA,THE_BARRENS,STORMWIND,ALTERAC_VALLEY,THE_SUNKEN_CITY,REVENDRETH, CORE
	CARD_TEST_CLASS='NEUTRAL'
	## DEMONHUNTER,DRUID,HUNTER,MAGE,NEUTRAL,PALADIN,PRIEST,ROGUE,SHAMAN,WARLOCK,WARRIOR,



	BUDDY_SYSTEM = 0### buddy system (- 23.1) -April 2022
	DARKMOON_TICKET_FOR_ALL=0 ## ddarkmoon tickets for all player anytime
	DARKMOON_TICKET_FOR_ALL_BY_HALF=0 ## darkmoon tickets for all player sometimes
	QUEST_REWARD=1 ## quest and reward system（24.2 - ）
	QUEST_PRESET=''
	REWARD_PRESET_FIRST=1 ## preset a reward at the beginning (for debugging)
	REWARD_PRESET=''

	PLAYER1_HUMAN=0 ## battleground with human player
	CARD_PRESET1=''
	CARD_PRESET2=''
	RANDOM_RACE=1 #プレーする種族をランダムに選ぶ（default:1）
	#sample from ['beast','demon','dragon','elemental','mecha','murloc','naga','pirate','quilboar']
	RACE_CHOICE=['pirate','beast']# valid when RANDOM_RACE=0
	HERO_1='' #第1プレーヤーはヒーローを指定できる
	HERO_2='' #人間プレーヤーはヒーローを指定できる

	ALL_PLAYERS_LOGINFO = 1 ## すべてのプレーヤーのバーにおけるムーブをテキスト表示する 




