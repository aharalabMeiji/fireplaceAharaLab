#!/usr/bin/env python
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
		,myClass=CardClass.WARRIOR)
		#,mulliganStrategy=StandardVectorAgent.StandardMulligan) 
	Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.PRIEST)
		#,mulliganStrategy=StandardVectorAgent.StandardMulligan) 
	##DEMONHUNTER,DRUID,HUNTER,MAGE,NEUTRAL,PALADIN,PRIEST,ROGUE,SHAMAN,WARLOCK,WARRIOR


	####################################################################

	#ゲームプレイ(きまったゲーム数を対戦し、勝ち数を数える)

	#FaceHunter by Aharalab
	MyDeck=[
		"VAN_CS2_162","VAN_CS2_162", "VAN_EX1_032","VAN_EX1_032", "VAN_EX1_050","VAN_EX1_050", "VAN_CS2_226","VAN_CS2_226", "VAN_DS1_184","VAN_DS1_184",
		"VAN_EX1_533","VAN_EX1_533", "VAN_EX1_537","VAN_EX1_537", "VAN_CS2_187","VAN_CS2_187", "VAN_CS2_179","VAN_CS2_179", "VAN_CS2_125","VAN_CS2_125",
		"VAN_CS2_203","VAN_CS2_203", "VAN_EX1_049","VAN_EX1_049", "VAN_EX1_539","VAN_EX1_539", "VAN_EX1_080","VAN_EX1_080", "VAN_CS2_181","VAN_CS2_181",]
	#空デッキを指定すると、ランダムデッキが構築される
	#a,b,c = play_set_of_games(Vector1, Vector2, deck1=[], deck2=[], gameNumber=20, debugLog=True)

	####################################################################
	
	#aharalab-build-deck
	filename='myfile-****-****_E00.csv'
	MyDeck=[

		]
	#f = open(filename, 'r')
	#datalist = f.readlines()
	#f.close()
	mydict ={}
	mydict['XXXX']=0
	#for line in datalist:
	#	terms = line.split(',')
	#	mydict[terms[0]]=int(terms[1])

	win_count=0
	total=120
	for myCardClass in [CardClass.DRUID, CardClass.HUNTER, CardClass.MAGE, CardClass.PALADIN, CardClass.PRIEST, CardClass.ROGUE, CardClass.SHAMAN, CardClass.WARLOCK, CardClass.WARRIOR]:
		Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
			,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
			,myClass=myCardClass)
		for repeat in range(total):
			winner , mydict_thisplay = play_one_game(Vector1, Vector2, deck1=MyDeck, deck2=[], debugLog=True)
			if winner=='Vector1':
				win_count += 1
				for key in mydict_thisplay:
					if key in mydict.keys():
						mydict[key] = mydict[key]+1
					else:
						mydict[key] = 1

				f = open(filename, 'w')
				for key,value in mydict.items():
					f.write(key+','+str(value)+"\n")
				f.close()
			else:
				for key in mydict_thisplay:
					if key in mydict.keys():
						mydict[key] = mydict[key]-1
					else:
						mydict[key] = -1

				f = open(filename, 'w')
				for key,value in mydict.items():
					f.write(key+','+str(value)+"\n")
				f.close()

	pass
	print("Vector1 wins: %d / %d = %f"%(win_count, total*9, 1.0*win_count/(total*9)))


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
	
