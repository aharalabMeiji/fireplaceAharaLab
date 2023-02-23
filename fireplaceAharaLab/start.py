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
	filename='myfile-hunter-all_E03.csv'
	f = open(filename, 'r')
	datalist = f.readlines()
	f.close()
	MyDeck=[
		#593 / 1080
		"VAN_EX1_610","VAN_EX1_610",#VAN_EX1_610,Explosive Trap,Hunter,Rarity.COMMON,2,0,0,<b>Secret:</b> When your hero is attacked deal $2 damage to all enemies.
		"VAN_EX1_032","VAN_EX1_032",#VAN_EX1_032,Sunwalker,Neutral,Rarity.RARE,6,4,5,<b>Taunt</b><b>Divine Shield</b>
		"VAN_NEW1_019","VAN_NEW1_019",#VAN_NEW1_019,Knife Juggler,Neutral,Rarity.RARE,2,3,2,[x]After you summon aminion deal 1 damageto a random enemy.
		"VAN_DS1_178","VAN_DS1_178",#VAN_DS1_178,Tundra Rhino,Hunter,Rarity.FREE,5,2,5,Your Beasts have <b>Charge</b>.
		"VAN_CS2_226","VAN_CS2_226",#VAN_CS2_226,Frostwolf Warlord,Neutral,Rarity.FREE,5,4,4,<b>Battlecry:</b> Gain +1/+1 for each other friendly minion on the battlefield.
		# 804 / 1080
		"VAN_NEW1_029",#VAN_NEW1_029,Millhouse Manastorm,Neutral,Rarity.LEGENDARY,2,4,4,<b>Battlecry:</b> Enemy spells cost (0) next turn.
		"VAN_CS2_187","VAN_CS2_187",#VAN_CS2_187,Booty Bay Bodyguard,Neutral,Rarity.FREE,5,5,4,<b>Taunt</b>
		"VAN_DS1_175","VAN_DS1_175",#VAN_DS1_175,Timber Wolf,Hunter,Rarity.FREE,1,1,1,Your other Beasts have +1_Attack.
		"VAN_CS1_042","VAN_CS1_042",#VAN_CS1_042,Goldshire Footman,Neutral,Rarity.FREE,1,1,2,<b>Taunt</b>
		"VAN_CS2_189","VAN_CS2_189",#VAN_CS2_189,Elven Archer,Neutral,Rarity.FREE,1,1,1,<b>Battlecry:</b> Deal 1 damage.
		# 893 / 1080
		"VAN_CS2_147","VAN_CS2_147",#VAN_CS2_147,Gnomish Inventor,Neutral,Rarity.FREE,4,2,4,<b>Battlecry:</b> Draw a card.
		"VAN_EX1_539","VAN_EX1_539",#VAN_EX1_539,Kill Command,Hunter,Rarity.FREE,3,0,0,Deal $3 damage. If you control a Beast deal$5 damage instead.
		"VAN_EX1_029","VAN_EX1_029",#VAN_EX1_029,Leper Gnome,Neutral,Rarity.COMMON,1,2,1,<b>Deathrattle:</b> Deal 2 damage to the enemy_hero.
		"VAN_EX1_506","VAN_EX1_506",#VAN_EX1_506,Murloc Tidehunter,Neutral,Rarity.FREE,2,2,1,<b>Battlecry:</b> Summon a 1/1_Murloc Scout.
		"VAN_DS1_184","VAN_DS1_184",#VAN_DS1_184,Tracking,Hunter,Rarity.FREE,1,0,0,Look at the top 3 cards of your deck. Draw one and discard the others.
		"VAN_EX1_021",#VAN_EX1_021,Thrallmar Farseer,Neutral,Rarity.COMMON,3,2,3,<b>Windfury</b>
		## 946 / 1080
		]

	mydict ={}
	for line in datalist:
		terms = line.split(',')
		mydict[terms[0]]=int(terms[1])

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
	print("Vector1 wins: %d / %d"%(win_count, total*9))


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
	
