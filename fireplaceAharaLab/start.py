#!/usr/bin/env python
import sys
from hearthstone.enums import *
from utils import *
from agent_Standard import *
from agent_SatZooLock import deckSatZoo,SatZooAgent
from fireplace import cards
from fireplace.debug_utilities import printClasses, printClasses_BG24, parse, parseDeck, printPool
from fireplace.config import Config
from competition_deckbuilder import CompetitionDeckbuilding

sys.path.append("..")

#
#		main()
#
def main():
	if Config.HEARTHSTONE==1:
		cards.db.initialize()
	else:
		cards.db.classic_initialize()
	#manual input(if you don't specify a class, it will be a hunter)
	Human1=HumanAgent("Human1",HumanAgent.HumanInput,myClass=CardClass.DRUID,
		choiceStrategy=HumanAgent.HumanInputChoice)
		# ,mulliganStrategy=HumanAgent.HumanInputMulligan)
	Human2=HumanAgent("Human2",HumanAgent.HumanInput,myClass=CardClass.WARRIOR)
	# random agent
	Random1=StandardAgent("Random1",StandardAgent.StandardRandom, myClass=CardClass.DEMONHUNTER) 
	Random2=StandardAgent("Random2",StandardAgent.StandardRandom, myClass=CardClass.DRUID) 

	#ベクトルプレーヤー。意外と強い。このプレーヤーとサシで勝負して勝てるくらいが一応の目安。
	Vector1=StandardVectorAgent("Vector1",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.PALADIN)
		#,mulliganStrategy=StandardVectorAgent.StandardMulligan) 
	Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.PRIEST)
		#,mulliganStrategy=StandardVectorAgent.StandardMulligan) 
	##DEMONHUNTER,DRUID,HUNTER,MAGE,NEUTRAL,PALADIN,PRIEST,ROGUE,SHAMAN,WARLOCK,WARRIOR.UNDEAD


	####  decks

	# 佐藤直之先生（佐世保高専）によるデッキ、エージェント# 予選 : 862/900=0.957
	#agent_SatZooLock.deckSatZoo: ## a deck by Naoyuki Sato, Nastional Institute of Technology, Sasebo College
	#agent_SatZooLock.SatZooAgent: ## an agent for deckSatZoo by Naoyuki Sato
	#・デッキの特徴は、
	#ウォーロックをヒーローとしたアグロ型デッキです。（俗称でいうところの「ズーロック」デッキです。）
	#よくあるズーロックデッキから、
	#本プラットフォームでは強さを発揮しにくいカード（ミニオンの「召喚位置」で効果性が大きく変わるタイプのカード）を抜いて、使い方が簡単な「高パワー・高体力のミニオン」を厚めに採用しました。
	#・エージェントの特徴ですが、
	#Vectorをベースとして、この自作デッキに特化した重みによる評価関数および、細かなヒューリスティックを２～３種類ほど組み込みました。
	
	## 嶋田慶太さん（明治大学B3）のデッキ：
	## ミッドレンジドルイド# 予選 : 648 / 900 = 0.72
	shimadaMidrangeDruid={
		"name":"shimadaMidrangeDruid",
		"deck":parseDeck("AAEDAZICBI+jBNGjBJiiBIqiBA3dlgTpoQTblQTwoQS9owTzoQTKowSTogTTlQTclQS8owTEowS+oQQA"),
		"class":CardClass.DRUID}

	## ・コントロールウォリアー# 予選 : 757/900 = 0.84
	shimadaControllWarrior={
		"name":"shimadaControllWarrior",
		"deck":parseDeck("AAEDAQcG0aMEraEEiqIEmKIE2aIEtqEEDK+WBPGgBL6hBNahBP+WBL6iBMOiBJiWBLCXBLmiBJqWBMSjBAA="),
		"class":CardClass.WARRIOR}
	##デッキの作り方（全体）
	##・１枚でアドバンテージを取りやすいカードを採用（闘技場モードでピック率の高いカードを採用）
	##・ミッドレンジデッキ（序盤から盤面を強くする手段を持ち、盤面を制圧してそのまま押しきる）
	##・盤面にいるだけで強いカード、ケアされなければ莫大なアドバンテージを得られるカードを基本的に採用。

	
	## 阿原一志（明治大学）のデッキ
	# deckCat第1世代の出力のうちのベストデッキ
	deckcatDruid1 ={# : 予選：851 / 900 = 0.945556
		"name":"deckcatDruid1",
		"deck":[
		"VAN_EX1_097","VAN_EX1_097",#(0)VAN_EX1_097,Abomination,Neutral,Rarity.RARE,5,4,4,<b>Taunt</b>. <b>Deathrattle:</b> Deal 2damage to ALL characters.
		"VAN_CS2_121","VAN_CS2_121",#(0)VAN_CS2_121,Frostwolf Grunt,Neutral,Rarity.FREE,2,2,2,<b>Taunt</b>
		"VAN_NEW1_029",#(0)VAN_NEW1_029,Millhouse Manastorm,Neutral,Rarity.LEGENDARY,2,4,4,<b>Battlecry:</b> Enemy spells cost (0) next turn.
		"VAN_EX1_506","VAN_EX1_506",#(1)VAN_EX1_506,Murloc Tidehunter,Neutral,Rarity.FREE,2,2,1,<b>Battlecry:</b> Summon a 1/1_Murloc Scout.
		"VAN_EX1_032","VAN_EX1_032",#(1)VAN_EX1_032,Sunwalker,Neutral,Rarity.RARE,6,4,5,<b>Taunt</b><b>Divine Shield</b>
		"VAN_CS2_125","VAN_CS2_125",#(1)VAN_CS2_125,Ironfur Grizzly,Neutral,Rarity.FREE,3,3,3,<b>Taunt</b>
		"VAN_NEW1_023","VAN_NEW1_023",#(1)VAN_NEW1_023,Faerie Dragon,Neutral,Rarity.COMMON,2,3,2,Can't be targeted by spells or Hero Powers.
		"VAN_CS2_231","VAN_CS2_231",#(1)VAN_CS2_231,Wisp,Neutral,Rarity.COMMON,0,1,1,
		"VAN_EX1_509","VAN_EX1_509",#(2)VAN_EX1_509,Murloc Tidecaller,Neutral,Rarity.RARE,1,1,2,Whenever a Murloc is summoned gain +1 Attack.
		"VAN_NEW1_020","VAN_NEW1_020",#(2)VAN_NEW1_020,Wild Pyromancer,Neutral,Rarity.RARE,2,3,2,After you cast a spell deal 1 damage to ALL minions.
		"VAN_CS1_069","VAN_CS1_069",#(2)VAN_CS1_069,Fen Creeper,Neutral,Rarity.COMMON,5,3,6,<b>Taunt</b>
		"VAN_CS2_146","VAN_CS2_146",#(2)VAN_CS2_146,Southsea Deckhand,Neutral,Rarity.COMMON,1,2,1,Has <b>Charge</b> while you have a weapon equipped.
		"VAN_NEW1_022","VAN_NEW1_022",#(2)VAN_NEW1_022,Dread Corsair,Neutral,Rarity.COMMON,4,3,3,<b>Taunt</b>Costs (1) less per Attack of_your weapon.
		"VAN_EX1_062",#(3)VAN_EX1_062,Old Murk-Eye,Neutral,Rarity.LEGENDARY,4,2,4,<b>Charge</b>. Has +1 Attack for each other Murloc on the battlefield.
		"VAN_EX1_005","VAN_EX1_005",#(3)VAN_EX1_005,Big Game Hunter,Neutral,Rarity.EPIC,3,4,2,<b>Battlecry:</b> Destroy a minion with 7 or more Attack.
		"VAN_EX1_593","VAN_EX1_593",#(3)VAN_EX1_593,Nightblade,Neutral,Rarity.FREE,5,4,4,<b>Battlecry: </b>Deal 3 damage to the enemy hero.
		],
		"class":CardClass.DRUID}
	# deckCat第1世代の出力のうちのセカンドデッキ
	deckcatHunter1 ={# : 予選：##  Wins: 826 / 900 = 0.917778
		"name":"deckcatHunter1",
		"deck":[
		"VAN_EX1_058","VAN_EX1_058",#(0)VAN_EX1_058,Sunfury Protector,Neutral,Rarity.RARE,2,2,3,<b>Battlecry:</b> Give adjacent minions <b>Taunt</b>.
		"VAN_EX1_507","VAN_EX1_507",#(0)VAN_EX1_507,Murloc Warleader,Neutral,Rarity.EPIC,3,3,3,ALL other murlocs have +2/+1.
		"VAN_EX1_611","VAN_EX1_611",#(0)VAN_EX1_611,Freezing Trap,Hunter,Rarity.COMMON,2,0,0,<b>Secret:</b> When an enemy minion attacks return it to its owner's hand. It costs (2) more.
		"VAN_EX1_019","VAN_EX1_019",#(0)VAN_EX1_019,Shattered Sun Cleric,Neutral,Rarity.FREE,3,3,2,<b>Battlecry:</b> Give a friendly minion +1/+1.
		"VAN_EX1_076","VAN_EX1_076",#(0)VAN_EX1_076,Pint-Sized Summoner,Neutral,Rarity.RARE,2,2,2,The first minion you play each turn costs (1) less.
		"VAN_CS2_125","VAN_CS2_125",#(1)VAN_CS2_125,Ironfur Grizzly,Neutral,Rarity.FREE,3,3,3,<b>Taunt</b>
		## "VAN_EX1_062",#(1)VAN_EX1_062,Old Murk-Eye,Neutral,Rarity.LEGENDARY,4,2,4,<b>Charge</b>. Has +1 Attack for each other Murloc on the battlefield.
		"VAN_NEW1_020","VAN_NEW1_020",#(1)VAN_NEW1_020,Wild Pyromancer,Neutral,Rarity.RARE,2,3,2,After you cast a spell deal 1 damage to ALL minions.
		"VAN_EX1_533","VAN_EX1_533",#(1)VAN_EX1_533,Misdirection,Hunter,Rarity.RARE,2,0,0,<b>Secret:</b> When an enemy attacks your hero instead it attacks another random character.
		"VAN_CS2_141","VAN_CS2_141",#(1)VAN_CS2_141,Ironforge Rifleman,Neutral,Rarity.FREE,3,2,2,<b>Battlecry:</b> Deal 1 damage.
		"VAN_EX1_093","VAN_EX1_093",#(2)VAN_EX1_093,Defender of Argus,Neutral,Rarity.RARE,4,2,3,<b>Battlecry:</b> Give adjacent minions +1/+1 and <b>Taunt</b>.
		"VAN_CS2_173","VAN_CS2_173",#(2)VAN_CS2_173,Bluegill Warrior,Neutral,Rarity.FREE,2,2,1,<b>Charge</b>
		"VAN_NEW1_023","VAN_NEW1_023",#(2)VAN_NEW1_023,Faerie Dragon,Neutral,Rarity.COMMON,2,3,2,Can't be targeted by spells or Hero Powers.
		"VAN_CS2_121","VAN_CS2_121",#(2)VAN_CS2_121,Frostwolf Grunt,Neutral,Rarity.FREE,2,2,2,<b>Taunt</b>
		"VAN_CS2_189","VAN_CS2_189",#(2)VAN_CS2_189,Elven Archer,Neutral,Rarity.FREE,1,1,1,<b>Battlecry:</b> Deal 1 damage.
		"VAN_EX1_586","VAN_EX1_586",#(3)VAN_EX1_586,Sea Giant,Neutral,Rarity.EPIC,10,8,8,Costs (1) less for each other minion on the battlefield.
		],"class":CardClass.SHAMAN}
	#
	deckcatDruid2={## 予選 : 
		## Wins: 808 / 900 = 0.898
		## deckcat第2世代のベストドルイド
		"name":"deckcatDruid2",
		"deck":[
		"VAN_EX1_178","VAN_EX1_178",#(2)VAN_EX1_178,Ancient of War,Druid,Rarity.EPIC,7,5,5,<b>Choose One -</b>+5 Attack; or +5 Health and <b>Taunt</b>.
		"VAN_CS2_232","VAN_CS2_232",#(2)VAN_CS2_232,Ironbark Protector,Druid,Rarity.FREE,8,8,8,<b>Taunt</b>
		"VAN_CS2_147","VAN_CS2_147",#(2)VAN_CS2_147,Gnomish Inventor,Neutral,Rarity.FREE,4,2,4,<b>Battlecry:</b> Draw a card.
		"VAN_EX1_573",#(3)VAN_EX1_573,Cenarius,Druid,Rarity.LEGENDARY,9,5,8,<b>Choose One -</b> Give your other minions +2/+2; or Summon two 2/2 Treants with <b>Taunt</b>.
		"VAN_EX1_165","VAN_EX1_165",#(3)VAN_EX1_165,Druid of the Claw,Druid,Rarity.COMMON,5,4,4,<b>Choose One -</b> <b>Charge</b>; or +2 Health and <b>Taunt</b>.
		"VAN_EX1_097","VAN_EX1_097",#(3)VAN_EX1_097,Abomination,Neutral,Rarity.RARE,5,4,4,<b>Taunt</b>. <b>Deathrattle:</b> Deal 2damage to ALL characters.
		"VAN_EX1_164","VAN_EX1_164",#(4)VAN_EX1_164,Nourish,Druid,Rarity.RARE,5,0,0,<b>Choose One -</b> Gain 2_Mana Crystals; or Draw 3 cards.
		"VAN_EX1_050","VAN_EX1_050",#(4)VAN_EX1_050,Coldlight Oracle,Neutral,Rarity.RARE,3,2,2,<b>Battlecry:</b> Each player draws 2 cards.
		"VAN_CS2_012","VAN_CS2_012",#(4)VAN_CS2_012,Swipe,Druid,Rarity.FREE,4,0,0,Deal $4 damage to an enemy and $1 damage to all other enemies.
		"VAN_CS2_005","VAN_CS2_005",#(4)VAN_CS2_005,Claw,Druid,Rarity.FREE,1,0,0,Give your hero +2_Attack this turn. Gain 2 Armor.
		"VAN_CS2_162","VAN_CS2_162",#(5)VAN_CS2_162,Lord of the Arena,Neutral,Rarity.FREE,6,6,5,<b>Taunt</b>
		"VAN_CS2_187","VAN_CS2_187",#(5)VAN_CS2_187,Booty Bay Bodyguard,Neutral,Rarity.FREE,5,5,4,<b>Taunt</b>
		"VAN_CS2_117","VAN_CS2_117",#(5)VAN_CS2_117,Earthen Ring Farseer,Neutral,Rarity.COMMON,3,3,3,<b>Battlecry:</b> Restore #3_Health.
		"VAN_CS2_118","VAN_CS2_118",#(5)VAN_CS2_118,Magma Rager,Neutral,Rarity.FREE,3,5,1,
		"VAN_EX1_062",#(6)VAN_EX1_062,Old Murk-Eye,Neutral,Rarity.LEGENDARY,4,2,4,<b>Charge</b>. Has +1 Attack for each other Murloc on the battlefield.
		"VAN_EX1_096","VAN_EX1_096",#(6)VAN_EX1_096,Loot Hoarder,Neutral,Rarity.COMMON,2,2,1,<b>Deathrattle:</b> Draw a card.
		],"class":CardClass.SHAMAN
		}

	####################################################################

	#competition #3 stage
	COMPETITION3_QUALIFY=1
	COMPETITION3_FINAL=2

	competition_round=3


	########## qualifying ##############



	if competition_round==COMPETITION3_QUALIFY:
		#theDeck=deckSatZoo
		#Vector1=SatZooAgent("SatZoo:deckSatZoo", SatZooAgent.StandardStep1\
		#					, myOption = []\
		#					, myClass = deckSatZoo["class"]
		#					, mulliganStrategy = SatZooAgent.SatZooMulligan)
		theDeck=shimadaControllWarrior
		Vector1=StandardVectorAgent("Vector:"+theDeck["name"],\
			StandardVectorAgent.StandardStep1,\
			myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8],\
			myClass=theDeck["class"])
		myclasses = [CardClass.DRUID,CardClass.HUNTER,CardClass.MAGE,CardClass.PALADIN,CardClass.PRIEST,CardClass.ROGUE,CardClass.SHAMAN,CardClass.WARLOCK,CardClass.WARRIOR]
		win=0
		lose=0
		for myclass in myclasses:
			Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
				,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
				,myClass=myclass
			,mulliganStrategy=StandardVectorAgent.StandardMulligan)
	
			a,b,c = play_set_of_games(Vector1, Vector2, deck1=theDeck["deck"], deck2=[], gameNumber=100, debugLog=True)		
			win+=a
			lose+=b
		print("#### result ####")
		print("win : %d, lose : %d"%(win,lose))
		print("################")
		input()
		pass


	########## final #############


	#classicDruid ## this is a tier1 deck in HSReplay.net
	classicTier1Druid = {"name":"classicTier1Druid",#win : 699/1000
		"deck":parseDeck("AAEDAZICArehBNuhBA7ZlQTblQTclQSvlgSwlgTdlgT6oATpoQTwoQTxoQTzoQSTogS9owTFqgQA"),
		"class":CardClass.DRUID}

	if competition_round==COMPETITION3_FINAL:
		competitors=[
			deckSatZoo,
			#shimadaMidrangeDruid,
			shimadaControllWarrior,
			#deckcatDruid1,
			#deckcatHunter1,
			#deckcatDruid2,
		]
		Ncompetitors=len(competitors)
		results=[[0 for repeat0 in range(Ncompetitors)] for repeat1 in range(Ncompetitors)]
		for i in range(Ncompetitors):
			for j in range(Ncompetitors):
				theDeck1=competitors[i]
				theDeck2=competitors[j]
				if i<j:
					if theDeck1["name"]=="deckSatZoo":
						Agent1 = SatZooAgent("SatZoo:deckSatZoo", SatZooAgent.StandardStep1\
							, myOption = []\
							, myClass = deckSatZoo["class"]
							, mulliganStrategy = SatZooAgent.SatZooMulligan)
					else:
						Agent1=StandardVectorAgent("Vector:"+theDeck1["name"],\
							StandardVectorAgent.StandardStep1\
						,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
						,myClass=theDeck1["class"])
					if theDeck2["name"]=="deckSatZoo":
						Agent2 = SatZooAgent("SatZoo:deckSatZoo", SatZooAgent.StandardStep1\
							, myOption = []\
							, myClass = deckSatZoo["class"]
							, mulliganStrategy = SatZooAgent.SatZooMulligan)
					else:
						Agent2=StandardVectorAgent("Vector:"+theDeck2["name"],\
							StandardVectorAgent.StandardStep1\
						,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
						,myClass=theDeck2["class"],mulliganStrategy=StandardVectorAgent.StandardMulligan)	
					#空デッキを指定すると、ランダムデッキが構築される
					a,b,c = play_set_of_games(Agent1, Agent2, deck1=theDeck1["deck"], deck2=theDeck2["deck"], gameNumber=100, debugLog=True)
					results[i][j]=a
					results[j][i]=b
					rf= open("final_round_results.txt", 'a')
					rf.write("################\n")
					rf.write("Player1 (%s) wins : %d, player2 (%s) wins : %d\n"%(theDeck1["name"],a,theDeck2["name"],b))
					rf.close()
		rf= open("final_round_results.csv", 'w')
		rf.write("winner,")
		for j in range(Ncompetitors):
			theDeck2=competitors[j]
			rf.write("%s,"%(theDeck2["name"]))
		rf.write("\n")
		for i in range(Ncompetitors):
			theDeck1=competitors[i]
			rf.write("%s,"%(theDeck1["name"]))
			for j in range(Ncompetitors):
				theDeck2=competitors[j]
				rf.write("%d,"%(results[i][j]))
			rf.write("\n")
		rf.close()
	######### goto deckCat #############
	
	if competition_round==3:
		CompetitionDeckbuilding.deckCatMain(
			repeat=0,sourceClassName='MAGE',matchN=100,pickupSize=4
		)

	####################################################################

### #3

from card_test.simulate_game import card_test

def battleground_main():
	from fireplace.battlegrounds.BG_utils import  BG_main
	for repeat in range(5):
		BG=BG_main()
		BG.BG_main()


### #6

def simulation_main():
	cards.db.initialize()
	playerA_class=getattr(CardClass, Config.PLAYERA_CLASS)
	playerB_class=getattr(CardClass, Config.PLAYERB_CLASS)
	Vector1=StandardVectorAgent("Vector1",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=playerA_class)
	Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=playerB_class)
	a,b,c = play_set_of_games(Vector1, Vector2, deck1=[], deck2=[], gameNumber=Config.SIMULATION_NUMBER, debugLog=True)

### #7

def simulation_classic_main():
	cards.db.classic_initialize()
	playerA_class=getattr(CardClass, Config.PLAYERA_CLASS)
	playerB_class=getattr(CardClass, Config.PLAYERB_CLASS)
	Vector1=StandardVectorAgent("Vector1",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=playerA_class)
	Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=playerB_class)
	a,b,c = play_set_of_games(Vector1, Vector2, deck1=[], deck2=[], gameNumber=Config.SIMULATION_NUMBER, debugLog=True)

### #8

def simulation_bigDeck_classic_main():
	cclass={'faceHunter':CardClass.HUNTER, 'bigWarrior':CardClass.WARRIOR, 'clownDruid':CardClass.DRUID }
	cards.db.classic_initialize()
	playerA_class=cclass[Config.PLAYERA_DECK]
	playerB_class=cclass[Config.PLAYERB_DECK]
	Vector1=StandardVectorAgent("Vector1",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=playerA_class)
	Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=playerB_class)
	playerA_deck=getattr(BigDeck,Config.PLAYERA_DECK, [])
	playerB_deck=getattr(BigDeck,Config.PLAYERB_DECK, [])
	a,b,c = play_set_of_games(Vector1, Vector2, deck1=playerA_deck, deck2=playerB_deck, gameNumber=Config.SIMULATION_BIGDECK_NUMBER, debugLog=True)

if __name__ == "__main__":
	if Config.HEARTHSTONE==1 or Config.HEARTHSTONE==2:
		main()
	elif Config.HEARTHSTONE==3:
		battleground_main()
	elif Config.HEARTHSTONE==4:
		card_test()
	elif Config.HEARTHSTONE==5:
		#printPool()
		printClasses()
	elif Config.HEARTHSTONE==6:
		simulation_main()
	elif Config.HEARTHSTONE==7:
		simulation_classic_main()
	elif Config.HEARTHSTONE==8:
		simulation_bigDeck_classic_main()
	elif Config.HEARTHSTONE==10:
		parse()
		#parseDeck("AAECAZICAA+t7AOz7APs9QP09gOsgASwgASHnwThpASIsgSuwASozgSB1ASe1ATW3gTd7QQA")
	
