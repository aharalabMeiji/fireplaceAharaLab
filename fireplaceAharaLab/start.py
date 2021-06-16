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
	Vector1=StandardVectorAgent("Vector1",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.HUNTER) 		
	Vector2 = StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.HUNTER)
	Vector3 =StandardVectorAgent("Vector3",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.HUNTER)
	Vector4 = StandardVectorAgent("Vector4",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.HUNTER)
	Vector5=StandardVectorAgent("Vector5",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.HUNTER) 		
	Vector6 = StandardVectorAgent("Vector6",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.HUNTER)
	Vector7 =StandardVectorAgent("Vector7",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.HUNTER)
	Vector8 = StandardVectorAgent("Vector8",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.HUNTER)
	Vector9 = StandardVectorAgent("Vector9",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.HUNTER)

	Vectors = [Vector1,Vector2,Vector3,Vector4,Vector5,Vector6,Vector7,Vector8,Vector9]

	# Maya : モンテカルロによる読み切り
	#Maya=Agent("Maya",Maya_MCTS)

	# Miyaryo
	# winner of the 1st competition of the fixed deck
	from agent_Miyaryo import MiyaryoAgent
	Miyaryo=MiyaryoAgent("Miyaryo",MiyaryoAgent.MiyaryoAI)

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
	#デッキ種類は関数内で設定
	#レーティングを表示する。
	from competition import play_round_robin_competition
	Pcount = 0
	for numX in range(len(Vectors)):
		for numY in range(len(Vectors)):
			Pcount = Pcount + 1
			print(Pcount)
			if not numX == numY:
				for num in range(10):
					play_round_robin_competition([Vectors[numX],Vectors[numY]],matchNumber=10)

			
	#print("1枚VS3枚しゅうりょう！")
	#for num in range(10):
		#play_round_robin_competition([Vector1,Vector3],matchNumber=10)
	#print("1枚VS5枚しゅうりょう！")
	#for num in range(10):
		#play_round_robin_competition([Vector1,Vector4],matchNumber=10)
	#print("1枚VS7枚しゅうりょう！")

	pass
if __name__ == "__main__":
	main()


