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
		,myClass=CardClass.HUNTER)
		#,mulliganStrategy=StandardVectorAgent.StandardMulligan) 
	Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.WARRIOR)
		#,mulliganStrategy=StandardVectorAgent.StandardMulligan) 
	##DEMONHUNTER,DRUID,HUNTER,MAGE,NEUTRAL,PALADIN,PRIEST,ROGUE,SHAMAN,WARLOCK,WARRIOR


	####################################################################

	#ゲームプレイ(きまったゲーム数を対戦し、勝ち数を数える)

	#MyDeck: DRUID
	#MyDeck=['VAN_CS1_042','VAN_CS1_042','VAN_CS1_069','VAN_CS1_069','VAN_CS2_117','VAN_CS2_117','VAN_CS2_118','VAN_CS2_118','VAN_CS2_119','VAN_CS2_119','VAN_CS2_120','VAN_CS2_120','VAN_CS2_121','VAN_CS2_121','VAN_CS2_122','VAN_CS2_122','VAN_CS2_124','VAN_CS2_124','VAN_CS2_125','VAN_CS2_125','VAN_CS2_127','VAN_CS2_127','VAN_CS2_131','VAN_CS2_131','VAN_CS2_141','VAN_CS2_142','VAN_CS2_146','VAN_CS2_147','VAN_CS2_150','VAN_CS2_151']
	#空デッキを指定すると、ランダムデッキが構築される
	#a,b,c = play_set_of_games(Vector1, Vector2, deck1=[], deck2=[], gameNumber=20, debugLog=True)

	####################################################################
	
	#aharalab-build-deck
	filename='myfile-hunter-warrior-F03.csv'
	f = open(filename, 'r')
	datalist = f.readlines()
	f.close()
	MyDeck=[
		### 200/500

		"VAN_CS2_162","VAN_CS2_162",#VAN_CS2_162#,Lord of the Arena,Neutral,Rarity.FREE,6,6,5,<b>Taunt</b>
		"VAN_EX1_032","VAN_EX1_032",#VAN_EX1_032#,Sunwalker,Neutral,Rarity.RARE,6,4,5,<b>Taunt</b><b>Divine Shield</b>
		"VAN_EX1_050","VAN_EX1_050",#VAN_EX1_050#,Coldlight Oracle,Neutral,Rarity.RARE,3,2,2,<b>Battlecry:</b> Each player draws 2 cards.
		"VAN_CS2_226","VAN_CS2_226",#VAN_CS2_226#,Frostwolf Warlord,Neutral,Rarity.FREE,5,4,4,<b>Battlecry:</b> Gain +1/+1 for each other friendly minion on the battlefield.
		"VAN_DS1_184","VAN_DS1_184",#VAN_DS1_184#,Tracking,Hunter,Rarity.FREE,1,0,0,Look at the top 3 cards of your deck. Draw one and discard the others.
		
		### 720/1000
		
		"VAN_EX1_533","VAN_EX1_533",#VAN_EX1_533,Misdirection,Hunter,Rarity.RARE,2,0,0,<b>Secret:</b> When an enemy attacks your hero instead it attacks another random character.
		"VAN_EX1_537","VAN_EX1_537",#VAN_EX1_537,Explosive Shot,Hunter,Rarity.RARE,5,0,0,Deal $5 damage to a minion and $2 damage to adjacent ones.
		"VAN_CS2_187","VAN_CS2_187",#VAN_CS2_187,Booty Bay Bodyguard,Neutral,Rarity.FREE,5,5,4,<b>Taunt</b>
		"VAN_CS2_179","VAN_CS2_179",#VAN_CS2_179,Sen'jin Shieldmasta,Neutral,Rarity.FREE,4,3,5,<b>Taunt</b>
		"VAN_CS2_125","VAN_CS2_125",#VAN_CS2_125,Ironfur Grizzly,Neutral,Rarity.FREE,3,3,3,<b>Taunt</b>

		### 963/1000

		"VAN_CS2_203","VAN_CS2_203",#VAN_CS2_203,Ironbeak Owl,Neutral,Rarity.COMMON,2,2,1,<b>Battlecry:</b> <b>Silence</b> a_minion.
		"VAN_EX1_049","VAN_EX1_049",#VAN_EX1_049,Youthful Brewmaster,Neutral,Rarity.COMMON,2,3,2,<b>Battlecry:</b> Return a friendly minion from the battlefield to your hand.
		"VAN_EX1_539","VAN_EX1_539",#VAN_EX1_539,Kill Command,Hunter,Rarity.FREE,3,0,0,Deal $3 damage. If you control a Beast deal$5 damage instead.
		"VAN_EX1_080","VAN_EX1_080",#VAN_EX1_080,Secretkeeper,Neutral,Rarity.RARE,1,1,2,Whenever a <b>Secret</b> is played gain +1/+1.
		"VAN_CS2_181","VAN_CS2_181",#VAN_CS2_181,Injured Blademaster,Neutral,Rarity.RARE,3,4,7,<b>Battlecry:</b> Deal 4 damage to HIMSELF.

		### 908/1000

		]

	mydict ={}
	for line in datalist:
		terms = line.split(',')
		mydict[terms[0]]=int(terms[1])

	win_count=0
	total=1000
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
	print("Vector1 wins: %d / %d"%(win_count, total))


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
	
