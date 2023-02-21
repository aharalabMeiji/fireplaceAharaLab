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
		,myClass=CardClass.PRIEST)
		#,mulliganStrategy=StandardVectorAgent.StandardMulligan) 
	Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.MAGE)
		#,mulliganStrategy=StandardVectorAgent.StandardMulligan) 
	##DEMONHUNTER,DRUID,HUNTER,MAGE,NEUTRAL,PALADIN,PRIEST,ROGUE,SHAMAN,WARLOCK,WARRIOR


	####################################################################

	#ゲームプレイ(きまったゲーム数を対戦し、勝ち数を数える)

	#FaceHunter by Aharalab
	MyDeck=[
		"VAN_CS2_162","VAN_CS2_162","VAN_EX1_032","VAN_EX1_032","VAN_EX1_050","VAN_EX1_050","VAN_CS2_226","VAN_CS2_226","VAN_DS1_184","VAN_DS1_184",
		"VAN_EX1_533","VAN_EX1_533","VAN_EX1_537","VAN_EX1_537","VAN_CS2_187","VAN_CS2_187","VAN_CS2_179","VAN_CS2_179","VAN_CS2_125","VAN_CS2_125",
		"VAN_CS2_203","VAN_CS2_203","VAN_EX1_049","VAN_EX1_049","VAN_EX1_539","VAN_EX1_539","VAN_EX1_080","VAN_EX1_080","VAN_CS2_181","VAN_CS2_181",]
	#空デッキを指定すると、ランダムデッキが構築される
	#a,b,c = play_set_of_games(Vector1, Vector2, deck1=[], deck2=[], gameNumber=20, debugLog=True)

	####################################################################
	
	#aharalab-build-deck
	filename='myfile-priest-mage-E03.csv'
	f = open(filename, 'r')
	datalist = f.readlines()
	f.close()
	MyDeck=[
		# 129 / 1000
		#'VAN_NEW1_016','VAN_NEW1_016',#VAN_NEW1_016,Captain's Parrot,Neutral,Rarity.EPIC,2,1,1,<b>Battlecry:</b> Draw a Pirate from your deck.
		#'VAN_CS2_222','VAN_CS2_222',#VAN_CS2_222,Stormwind Champion,Neutral,Rarity.FREE,7,6,6,Your other minions have +1/+1.
		#'VAN_EX1_029','VAN_EX1_029',#VAN_EX1_029,Leper Gnome,Neutral,Rarity.COMMON,1,2,1,<b>Deathrattle:</b> Deal 2 damage to the enemy_hero.
		#  357 / 1000
		"VAN_EX1_339","VAN_EX1_339",#VAN_EX1_339,Thoughtsteal,Priest,Rarity.COMMON,3,0,0,Copy 2 cards in your opponent's deck and add them to your hand.
		#"VAN_EX1_561",#VAN_EX1_561,Alexstrasza,Neutral,Rarity.LEGENDARY,9,8,8,<b>Battlecry:</b> Set a hero's remaining Health to 15.
		#"VAN_CS2_147","VAN_CS2_147",#VAN_CS2_147,Gnomish Inventor,Neutral,Rarity.FREE,4,2,4,<b>Battlecry:</b> Draw a card.
		#"VAN_EX1_015","VAN_EX1_015",#VAN_EX1_015,Novice Engineer,Neutral,Rarity.FREE,2,1,1,<b>Battlecry:</b> Draw a card.
		# 256 / 1000
		"VAN_EX1_004","VAN_EX1_004",#VAN_EX1_004,Young Priestess,Neutral,Rarity.RARE,1,2,1,At the end of your turn give another random friendly minion +1 Health.
		"VAN_EX1_506","VAN_EX1_506",#VAN_EX1_506,Murloc Tidehunter,Neutral,Rarity.FREE,2,2,1,<b>Battlecry:</b> Summon a 1/1_Murloc Scout.
		"VAN_EX1_076","VAN_EX1_076",#VAN_EX1_076,Pint-Sized Summoner,Neutral,Rarity.RARE,2,2,2,The first minion you play each turn costs (1) less.
		"VAN_EX1_029","VAN_EX1_029",#VAN_EX1_029,Leper Gnome,Neutral,Rarity.COMMON,1,2,1,<b>Deathrattle:</b> Deal 2 damage to the enemy_hero.
		"VAN_CS2_121","VAN_CS2_121",#VAN_CS2_121,Frostwolf Grunt,Neutral,Rarity.FREE,2,2,2,<b>Taunt</b>
		"VAN_CS2_155","VAN_CS2_155",#VAN_CS2_155,Archmage,Neutral,Rarity.FREE,6,4,7,<b>Spell Damage +1</b>

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
	
