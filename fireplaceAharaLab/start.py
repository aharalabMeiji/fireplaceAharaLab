#!/usr/bin/env python
import sys
from hearthstone.enums import *
from utils import *
from agent_Standard import *
from agent_Maya import *
from agent_word_strategy import *
from agent_AngryCat import *

sys.path.append("..")

#
#		main()
#
def main():
	from fireplace import cards
	cards.db.initialize()
	#人間手入力(クラスを指定しないとハンターになる)
	Human=HumanAgent("Human",HumanAgent.HumanInput,myClass=CardClass.HUNTER)
	#ランダムプレーヤー
	Random=StandardAgent("Random",StandardAgent.StandardRandom, myClass=CardClass.MAGE) 
	#ベクトルプレーヤー。意外と強い。このプレーヤーとサシで勝負して勝てるくらいが一応の目安。
	Vector=StandardVectorAgent("Vector",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.MAGE) 		

	# Maya : モンテカルロによる読み切り
	#Maya=Agent("Maya",Maya_MCTS)

	# Miyaryo
	#from agent_miyaryo import miyaryoAgent
	#miyaryo=miyaryoAgent("Miyaryo",miyaryoAgent.miyaryoAI)

	# Takasho001
	#from agent_takasho001 import takasho001Agent
	#takasho001=takasho001Agent("Takasho",takasho001Agent.takashoAI)

	# 言葉で戦略を組み立てるエージェント by Ahara
	#from agent_word_strategy import WordStrategyAgent
	#WordStrategy = WordStrategyAgent("WS", WordStrategyAgent.agent_word_strategy\
	#	,myOption=[WS.ミニョンで敵ヒーローの体力を削る, WS.呪文を使えるなら呪文, WS.ランダムにプレー]\
	#	,myClass=CardClass.PRIEST)

	#AngryCat ： シンプルに選択するアルゴリズム
	from agent_AngryCat import AngryCatAgent
	AngryCat = AngryCatAgent("AngryCat", AngryCatAgent.AngryCatAI)

	#HunterCat : faceHunter専用のエージェント
	from agent_HunterCat import HunterCatAgent
	HunterCat=HunterCatAgent("HunterCat", HunterCatAgent.HunterCatAI)

	####################################################################

	#ゲームプレイ(きまったゲーム数を対戦し、勝ち数を数える)
	#play_set_of_games(Random, Human, BigDeck.faceHunter, BigDeck.faceHunter, gameNumber=10, debugLog=True)
	#デッキを固定しての対戦（ここでは両者ともフェイスハンター）
	#play_set_of_games(Human, Random, BigDeck.faceHunter, BigDeck.faceHunter, gameNumber=10, debugLog=True)

	#デッキを固定しての総当たり戦
	from competition import play_round_robin_competition
	play_round_robin_competition([Random,Vector,AngryCat,HunterCat],matchNumber=1)

	#特定の2枚のカードのシナジーを調べる(idea by Maya)
	#from card_pair import investigate_card_pair, find_card_pair
	#investigate_card_pair()
	#シナジーのあるカードの組を漠然と探す
	#find_card_pair(1)
	#print("test_branch_yamadamaya")

	pass
if __name__ == "__main__":
	main()


