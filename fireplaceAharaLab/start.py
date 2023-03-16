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


	####################################################################

	#competition #3 stage
	COMPETITION3_QUALIFY=1
	COMPETITION3_FINAL=2

	competition_round=3

	########## qualifying ##############

	if competition_round==COMPETITION3_QUALIFY:
		theDeck=deckSatZoo
		Vector1=SatZooAgent("SatZoo:deckSatZoo", SatZooAgent.StandardStep1\
							, myOption = []\
							, myClass = deckSatZoo["class"]
							, mulliganStrategy = SatZooAgent.SatZooMulligan)

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

	# 佐世保高専、佐藤直之先生によるデッキ、エージェント# win : 862/900=0.957
	#agent_SatZooLock.deckSatZoo: ## a deck by Naoyuki Sato, Nastional Institute of Technology, Sasebo College
	#agent_SatZooLock.SatZooAgent: ## an agent for deckSatZoo by Naoyuki Sato

	#classicDruid ## this is a tier1 deck in HSReplay.net
	classicTier1Druid = {"name":"classicTier1Druid",#win : 699/1000
		"deck":parseDeck("AAEDAZICArehBNuhBA7ZlQTblQTclQSvlgSwlgTdlgT6oATpoQTwoQTxoQTzoQSTogS9owTFqgQA"),
		"class":CardClass.DRUID}

	if competition_round==COMPETITION3_FINAL:
		competitors=[
			deckSatZoo,
			classicTier1Druid
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
						Agent1=StandardVectorAgent("Vector:"+theDeck1["name"],StandardVectorAgent.StandardStep1\
						,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
						,myClass=theDeck1["class"])
					if theDeck2["name"]=="deckSatZoo":
						Agent2 = SatZooAgent("SatZoo:deckSatZoo", SatZooAgent.StandardStep1\
							, myOption = []\
							, myClass = deckSatZoo["class"]
							, mulliganStrategy = SatZooAgent.SatZooMulligan)
					else:
						Agent2=StandardVectorAgent("Vector:"+theDeck1["name"],StandardVectorAgent.StandardStep1\
						,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
						,myClass=theDeck2["class"])	
					#空デッキを指定すると、ランダムデッキが構築される
					a,b,c = play_set_of_games(Agent1, Agent2, deck1=theDeck1["deck"], deck2=theDeck2["deck"], gameNumber=10, debugLog=True)
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
		CompetitionDeckbuilding.deckCatMain(1)
		CompetitionDeckbuilding.deckCatMain(2)
		CompetitionDeckbuilding.deckCatMain(3)
		CompetitionDeckbuilding.deckCatMain(4)
		CompetitionDeckbuilding.deckCatMain(5)

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
	
