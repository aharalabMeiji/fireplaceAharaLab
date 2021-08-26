#!/usr/bin/env python
import sys
from hearthstone.enums import *
from utils import *
from agent_Standard import *
#from agent_Maya import *
from agent_word_strategy import *
from agent_AngryCat import *

sys.path.append("..")

from fireplace import cards

def printClasses():
	print('')
	print('from ..utils import *')
	print('')
	_cardList = []
	for _id in cards.db.keys():
		_card = cards.db[_id]
		if _card.card_set== CardSet.CORE:
			if _card.card_class == CardClass.HUNTER: 
				_cardList.append(_card.id)
				print('class %s:# %d %d'%(_card.id, _card.card_class, _card.card_set))
				print('    """ %s'%(_card.name))
				print('    %s """'%(_card.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
				print('    #'%())
				print('    pass'%())
				print(''%())


#
#		main()
#
def main():
	cards.db.initialize()
	#printClasses()
	#人間手入力(クラスを指定しないとハンターになる)
	Human=HumanAgent("Human1",HumanAgent.HumanInput,myClass=CardClass.HUNTER)
	  # ,mulliganStrategy=HumanAgent.HumanInputMulligan)
	Human2=HumanAgent("Human2",HumanAgent.HumanInput,myClass=CardClass.HUNTER)
	#ランダムプレーヤー
	Random=StandardAgent("Random",StandardAgent.StandardRandom, myClass=CardClass.HUNTER) 
	#ベクトルプレーヤー。意外と強い。このプレーヤーとサシで勝負して勝てるくらいが一応の目安。
	Vector1=StandardVectorAgent("Vector1",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.HUNTER)
		#,mulliganStrategy=StandardVectorAgent.StandardMulligan) 	
	Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.PALADIN)
		#,mulliganStrategy=StandardVectorAgent.StandardMulligan) 	

	# Maya : モンテカルロによる読み切り
	#from agent_Maya import MayaAgent
	#Maya=MayaAgent("Maya",MayaAgent.Maya_MCTS,myClass=CardClass.MAGE)

	# Miyaryo
	# winner of the 1st competition of the fixed deck
	#from agent_Miyaryo import MiyaryoAgent
	#Miyaryo=MiyaryoAgent("Miyaryo",MiyaryoAgent.MiyaryoAI)

	# Takasho001
	#from agent_takasho001 import takasho001Agent
	#takasho001=takasho001Agent("Takasho",takasho001Agent.takashoAI)

	# 言葉で戦略を組み立てるエージェント by Ahara
	#from agent_word_strategy import WordStrategyAgent
	#WordStrategy = WordStrategyAgent("WS", WordStrategyAgent.agent_word_strategy\
	#	,myOption=[WS.ミニョンで敵ヒーローの体力を削る, WS.呪文を使えるなら呪文, WS.ランダムにプレー]\
	#	,myClass=CardClass.PRIEST)

	#HunterCat : faceHunter専用のエージェント
	#from agent_HunterCat import HunterCatAgent
	#HunterCat=HunterCatAgent("HunterCat", HunterCatAgent.HunterCatAI)

	####################################################################

	#ゲームプレイ(きまったゲーム数を対戦し、勝ち数を数える)
	#play_set_of_games(Human, Vector, deck1=[], deck2=[], gameNumber=1, debugLog=True)
	play_set_of_games(Vector1, Vector2, deck1=[], deck2=[], gameNumber=10, debugLog=True)
	#play_set_of_games(Human, Human2, deck1=[], deck2=[], gameNumber=1, debugLog=True, P1MAXMANA=10, P2MAXMANA=10)

	#デッキを固定しての総当たり戦
	#デッキ種類は関数内で設定
	#レーティングを表示する。
	#from competition import play_round_robin_competition
	#play_round_robin_competition([Random,Vector,AngryCat,HunterCat],matchNumber=1)

	#特定の2枚のカードのシナジーを調べる(idea by Maya)
	#from card_pair import investigate_card_pair, find_card_pair
	#investigate_card_pair()
	#シナジーのあるカードの組を漠然と探す
	#find_card_pair(1)
	#print("test_branch_yamadamaya")

	pass
if __name__ == "__main__":
	main()


