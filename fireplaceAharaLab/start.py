#!/usr/bin/env python
from base64 import b16decode
from binascii import a2b_base64
from re import A
import sys
from hearthstone.enums import *
from utils import *
from agent_Standard import *
from fireplace import cards
from fireplace.debug_utilities import printClasses, printClasses_BG24, parse, parseDeck, printPool
from fireplace.config import Config

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

	######### entries (samples) ############

	#deckCatHunter ## this is a sample
	deckCatHunter={
		"deck":[
		"VAN_CS2_162", "VAN_CS2_162", "VAN_EX1_032", "VAN_EX1_032", "VAN_EX1_050", "VAN_EX1_050", "VAN_CS2_226", "VAN_CS2_226", "VAN_DS1_184", "VAN_DS1_184",
		"VAN_EX1_533", "VAN_EX1_533", "VAN_EX1_537", "VAN_EX1_537", "VAN_CS2_187", "VAN_CS2_187", "VAN_CS2_179", "VAN_CS2_179", "VAN_CS2_125", "VAN_CS2_125",
		"VAN_CS2_203", "VAN_CS2_203", "VAN_EX1_049", "VAN_EX1_049", "VAN_EX1_539", "VAN_EX1_539", "VAN_EX1_080", "VAN_EX1_080", "VAN_CS2_181", "VAN_CS2_181",],
		"class":CardClass.HUNTER}
	#frozenMidrangeMage ## this is a sample
	frozenMidrangeMage = {
		"deck":parseDeck("AAEDAf0ECJiiBMSqBNGjBLehBNuhBLWhBM2jBN+VBAvolQTilQS7ogSyoQTDowTVoQTQoQTZlgSTogS5oQSwlgQA"),
		"class":CardClass.MAGE}

	competition_round=0

	########## qualifying ##############

	if competition_round==0:
		theDeck=deckCatHunter
		Vector1=StandardVectorAgent("Vector1",StandardVectorAgent.StandardStep1\
			,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
			,myClass=theDeck["class"])

		myclasses = [CardClass.DRUID,CardClass.HUNTER,CardClass.MAGE,CardClass.PALADIN,CardClass.PRIEST,CardClass.ROGUE,CardClass.SHAMAN,CardClass.WARLOCK,CardClass.WARRIOR]
		win=0
		lose=0
		for myclass in myclasses:
			Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
				,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
				,myClass=myclass)	
			a,b,c = play_set_of_games(Vector1, Vector2, deck1=theDeck["deck"], deck2=[], gameNumber=10, debugLog=True)		
			win+=a
			lose+=b
		print("#### result ####")
		print("win : %d, lose : %d"%(win,lose))
		print("################")
		input()
		pass


	########## final #############

	if competition_round==1:
		theDeck1=deckCatHunter
		theDeck2=frozenMidrangeMage

		Vector1=StandardVectorAgent("Vector1",StandardVectorAgent.StandardStep1\
			,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
			,myClass=theDeck1["class"])
		Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
			,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
			,myClass=theDeck2["class"])	
		#空デッキを指定すると、ランダムデッキが構築される
		a,b,c = play_set_of_games(Vector1, Vector2, deck1=theDeck1["deck"], deck2=theDeck2["deck"], gameNumber=10, debugLog=True)
		print("#### result ####")
		print("Player1 wins : %d, player2 wins : %d"%(a,b))
		print("################")
		input()
	


	####################################################################

### deckCat ###

def deckCatMain():
	sourceClass=CardClass.HUNTER
	Vector1=StandardVectorAgent("Vector1",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=sourceClass)
	targetClasses=[CardClass.DRUID,CardClass.HUNTER,CardClass.MAGE,CardClass.PALADIN,CardClass.PRIEST,CardClass.ROGUE,CardClass.SHAMAN,CardClass.WARLOCK,CardClass.WARRIOR]
	lenTarget=len(targetClasses)
	cardsfilename="myDeck-%s-all.csv"%sourceClass
	deckfilename="myDeck-%s-all.csv"%sourceClass
	poolfilename="classic_pool_en.csv"
	matchN=100
	MyDeck=[

	]
	mydict ={}
	mydict['XXXX']=0
	df = open(deckfilename, 'w')
	df.write("\t\tmyDeck-%s-all\n\n"%sourceClass)
	df.close()
	pf = open(poolfilename, 'r')
	readlines = pf.read()
	for line in readlines:
		pass
	win_count=0
	for myCardClass in targetClasses:
		Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
			,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
			,myClass=myCardClass)
		for repeat in range(matchN):
			winner , mydict_thisplay = play_one_game(Vector1, Vector2, deck1=MyDeck, deck2=[], debugLog=True)
			if winner=='Vector1':
				win_count += 1
				for key in mydict_thisplay:
					if key in mydict.keys():
						mydict[key] = mydict[key]+1
					else:
						mydict[key] = 1

				f = open(cardsfilename, 'w')
				for key,value in mydict.items():
					f.write(key+','+str(value)+"\n")
				f.close()
			else:
				for key in mydict_thisplay:
					if key in mydict.keys():
						mydict[key] = mydict[key]-1
					else:
						mydict[key] = -1

				f = open(cardsfilename, 'w')
				for key,value in mydict.items():
					f.write(key+','+str(value)+"\n")
				f.close()
	df = open(deckfilename, 'w')
	df.write("\t\tWins: %d / %d = %f\n\n"%(win_count, matchN*lenTarget, 1.0*win_count/(matchN*lenTarget)))
	df.close()
	
	pass

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
	
