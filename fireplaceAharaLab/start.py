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
		,myClass=CardClass.DRUID)
		#,mulliganStrategy=StandardVectorAgent.StandardMulligan) 
	Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.DRUID)
		#,mulliganStrategy=StandardVectorAgent.StandardMulligan) 
	##DEMONHUNTER,DRUID,HUNTER,MAGE,NEUTRAL,PALADIN,PRIEST,ROGUE,SHAMAN,WARLOCK,WARRIOR


	####################################################################

	#ゲームプレイ(きまったゲーム数を対戦し、勝ち数を数える)

	#MyDeck: DRUID
	#MyDeck=['VAN_CS1_042','VAN_CS1_042','VAN_CS1_069','VAN_CS1_069','VAN_CS2_117','VAN_CS2_117','VAN_CS2_118','VAN_CS2_118','VAN_CS2_119','VAN_CS2_119','VAN_CS2_120','VAN_CS2_120','VAN_CS2_121','VAN_CS2_121','VAN_CS2_122','VAN_CS2_122','VAN_CS2_124','VAN_CS2_124','VAN_CS2_125','VAN_CS2_125','VAN_CS2_127','VAN_CS2_127','VAN_CS2_131','VAN_CS2_131','VAN_CS2_141','VAN_CS2_142','VAN_CS2_146','VAN_CS2_147','VAN_CS2_150','VAN_CS2_151']
	#空デッキを指定すると、ランダムデッキが構築される
	a,b,c = play_set_of_games(Vector1, Vector2, deck1=[], deck2=[], gameNumber=10, debugLog=True)
	


	####################################################################


from card_test.simulate_game import card_test

def battleground_main():
	from fireplace.battlegrounds.BG_utils import  BG_main
	for repeat in range(5):
		BG=BG_main()
		BG.BG_main()



if __name__ == "__main__":
	if Config.HEARTHSTONE==1 or Config.HEARTHSTONE==2:
		main()
	elif Config.HEARTHSTONE==3:
		battleground_main()
	elif Config.HEARTHSTONE==4:
		card_test()
	elif Config.HEARTHSTONE==5:
		printPool()
		#printClasses()
	elif Config.HEARTHSTONE==10:
		parse()
		#parseDeck("AAECAZICAA+t7AOz7APs9QP09gOsgASwgASHnwThpASIsgSuwASozgSB1ASe1ATW3gTd7QQA")
	
