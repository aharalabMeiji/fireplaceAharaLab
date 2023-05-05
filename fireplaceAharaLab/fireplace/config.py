class Config:# ()is the default value

	HEARTHSTONE=3
	#1: Hearthstone standard battle
	#256: standard 25.6
	#2: Hearthstone classic cards
	#3: Hearthstone battleground

	#4: Checking a specific card for debugging
	#5: List up cards data (to build a new cards file.)
	#6: Vector Agent(fix), random deck, standard battles simulation
	#7: Vector Agent(fix), random deck, classic battles simulation

	#8: bigDeck games (with classic pool)

	#10: Decoding from a 'deckcode' to list of cards.

	#11: first competition
	#12: second competition
	#13: third competition ( 2023/3/19 )


	#1 standard battle options
	FSFIXED=0 # fixing first and second YES:>0 NO:0(0) # 
	COIN=1 # giving a coin to the second  YES:>0 NO:0(1) #
	EX_CARD=1 # giving an extra ard to the second  YES:>0 NO:0(1) #
	# options of play_set_of_games()
	#HEROHPOPTION=30 #ヒーロー体力(30)
	#P1MAXMANA=1 # 先攻マナ(1) 1~10
	#P2MAXMANA=1 # 後攻マナ(1) 1~10
	#P1HAND=3 # 先攻ハンド枚数(3) 1~9 
	#P2HAND=3 # 後攻ハンド枚数(3) 1~9 # the coin is not included

	#LOGINFO
	LOGINFO=1 # as log.info
	LOGINFO_INDENT=0
	def log(function, message):
		if Config.LOGINFO_INDENT>0:
			for repeat in range(Config.LOGINFO_INDENT):
				print("====>", end="")
		print("( %s )"%(function), end="")
		print(" %s"%(message))
	DEEPCOPY_LOGINFO=0

	#debugLog
	GAMELOG=1 # as debugLog option

	#3 battlegrounds options
	BUDDY_SYSTEM = 0### buddy system (- 23.1) -April 2022
	NEW_BUDDY_SYSTEM = 1 ### buddy system 25.6 -
	DARKMOON_TICKET_FOR_ALL=0 ## darkmoon tickets for all player anytime
	DARKMOON_TICKET_FOR_ALL_BY_HALF=0 ## darkmoon tickets for all player sometimes
	QUEST_REWARD=0 ## quest and reward system（24.2 - ）(banned 25.2.2-)
	QUEST_PRESET=''
	REWARD_PRESET_FIRST=0 ## preset a reward at the beginning (for debugging)
	REWARD_PRESET=''

	PLAYER1_HUMAN=0 ## battleground with human player
	CARD_PRESET1=''
	CARD_PRESET2=''
	RANDOM_RACE=1 #random sampling from races（default:1）
	#sample from ['beast','demon','dragon','elemental','mecha','murloc','naga','pirate','quilboar','undead']
	RACE_CHOICE=['naga','dragon']# valid when RANDOM_RACE=0
	HERO_1='' #第1プレーヤーはヒーローを指定できる
	HERO_2='' #人間プレーヤーはヒーローを指定できる

	ALL_PLAYERS_LOGINFO = 1 ## すべてのプレーヤーのバーにおけるムーブをテキスト表示する 


	#4: Checking a specific card for debugging
	CARD_TEST_SET='RETURN_OF_THE_LICH_KING'
	## VANILLA,THE_BARRENS,STORMWIND,ALTERAC_VALLEY,THE_SUNKEN_CITY,REVENDRETH, CORE, 
	## RETURN_OF_THE_LICH_KING, PATH_OF_ARTHAS
	CARD_TEST_CLASS='WARLOCK'
	## DEATHKNIGHT,DEMONHUNTER,DRUID,HUNTER,MAGE,NEUTRAL,PALADIN,PRIEST,ROGUE,SHAMAN,WARLOCK,WARRIOR,
	## 

	#6 #7 options (fixing agents, random deck)
	PLAYERA_CLASS='ROGUE'
	PLAYERB_CLASS='SHAMAN'
	SIMULATION_NUMBER=50
	## DEATHKNIGHT,DEMONHUNTER,DRUID,HUNTER,MAGE,PALADIN,PRIEST,ROGUE,SHAMAN,WARLOCK,WARRIOR,

	#8 options (specific agents, specific deck, classic battle pool)
	PLAYERA_DECK="bigWarrior"
	PLAYERB_DECK="clownDruid"
	## faceHunter, bigWarrior, clownDruid
	PLAYERA_AGENT="Vector"
	PLAYERB_AGENT="Vector"
	#Vector
	SIMULATION_BIGDECK_NUMBER=100 # number of matches of simulation





