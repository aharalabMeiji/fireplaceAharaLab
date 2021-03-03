#!/usr/bin/env python
import sys
from hearthstone.enums import *
from utils import *
from agent_Standard import *
from agent_Maya import *
from agent_word_strategy import *
from agent_AngryCat import *
from agent_faceHunter_Mirror_Maya import *
import random
import csv
sys.path.append("..")
import math
import datetime
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
	Maya=agent_Maya("Maya",agent_Maya.agent_MayaAI)
	faceHunter_Maya=faceHunter_Mirror_Maya("faceHunter_Mirror_Maya",faceHunter_Mirror_Maya.faceHunter_Mirror_MayaAI\
		,myOption=[1,1,1,1,1,1,1,1,1,1,1,1])
	faceHunter_Maya2=faceHunter_Mirror_Maya("faceHunter_Mirroring",faceHunter_Mirror_Maya.faceHunter_Mirror_MayaAI\
		,myOption=[1,-1,1,-1,1,-1,1,-1,1,-1,1,-1])
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
	#from agent_AngryCat import AngryCatAgent
	#AngryCat = AngryCatAgent("AngryCat", AngryCatAgent.AngryCatAI)

	#HunterCat : faceHunter専用のエージェント
	#from agent_HunterCat import HunterCatAgent
	#HunterCat=HunterCatAgent("HunterCat", HunterCatAgent.HunterCatAI)

	####################################################################

	#ゲームプレイ(きまったゲーム数を対戦し、勝ち数を数える)
	option_pool=[[0, -0.33, -0.43,0,0, 0.68,-0.48,0,0,0, 0.1,0] for k in range(2)]
	while True:
		first,second=tournament(option_pool)
		print(datetime.datetime.now())
		option_pool=[]
		option_pool.append(first)
		option_pool.append(second)
		option_pool.extend(get_mutate_vector(2))
		option_pool.extend(get_evolute_vector(first,get_num=2))
		option_pool.extend(get_evolute_vector(second,get_num=2))
		print(first)
		print(second)
		with open('./data/result.csv',"a") as f:
			writer=csv.writer(f,lineterminator="\n")
			writer.writerows([first,second])
			print("----------------------finished===================")
		pass
	#デッキを固定しての対戦（ここでは両者ともフェイスハンター）
	#play_set_of_games(Human, Random, BigDeck.faceHunter, BigDeck.faceHunter, gameNumber=10, debugLog=True)

	#デッキを固定しての総当たり戦
	#from competition import play_round_robin_competition
	#play_round_robin_competition([Random,Vector,AngryCat,HunterCat],matchNumber=1)

	#特定の2枚のカードのシナジーを調べる(idea by Maya)
	#from card_pair import investigate_card_pair, find_card_pair
	#investigate_card_pair()
	#シナジーのあるカードの組を漠然と探す
	#find_card_pair(1)
	#print("test_branch_yamadamaya")

	pass
def normalize(_option:list=[]):
	size=sum(list(map(lambda i: i*i,_option)))
	return list(map(lambda i:i/math.sqrt(size),_option))
	pass
def get_evolute_vector(_option:list=[],get_num=6):
	threashold=0.1
	retVectors=[]
	for i in range(get_num):
		retVectors.append(normalize(list(map(lambda item:item+random.random()*threashold,_option))))
		pass
	return retVectors
	pass
def get_mutate_vector(get_num=2):
	return [[random.random()*2-1 for i in range(12) ] for k in range(get_num)]
	pass
def tournament(_option_pool:list=[],sample_num=2):
	temp_pool=_option_pool
	if len(temp_pool)%sample_num==1:
		temp_pool.append([random.random()*2-1])
		pass
	random.shuffle(temp_pool)
	if len(temp_pool)<=sample_num:
		return temp_pool[0],temp_pool[1]
		pass
	else:
		winner_pool=[]
		for i in range(int(len(temp_pool)/2)):
			marionette_Maya=faceHunter_Mirror_Maya("marionette",faceHunter_Mirror_Maya.faceHunter_Mirror_MayaAI,myOption=temp_pool[2*i])
			reTale=faceHunter_Mirror_Maya("reTale",faceHunter_Mirror_Maya.faceHunter_Mirror_MayaAI,myOption=temp_pool[2*i+1])
			winner_pool.append(mirror_match(marionette_Maya, reTale,BigDeck.faceHunter,BigDeck.faceHunter,gameNumber=31, debugLog=True))
		return tournament(winner_pool)
	pass
def mirror_match(P1: Agent, P2: Agent, deck1=[], deck2=[], gameNumber=15, debugLog=True):
	""" 決まった回数の試合を行い、勝敗数を表示する 
	"""
	if debugLog:
		print(" %r (%s) vs.  %r (%s)"%(P1.name, P1.myClass, P2.name, P2.myClass))
	Count1 = 0
	Count2 = 0
	for i in range(gameNumber):
		winner = play_one_game(P1,P2,deck1, deck2, debugLog=debugLog)
		if debugLog:
			print("winner is %r"%winner)
		if winner == P1.name:
			Count1+=1
		elif winner == P2.name:
			Count2+=1
	print(" %r (%s) wins: %d"%(P1.name, P1.myClass, Count1))
	print(" %r (%s) wins: %d"%(P2.name, P2.myClass, Count2))
	print(" Draw: %d"%(gameNumber-Count1-Count2))
	if Count2>Count1:
		return P2.option
		pass
	return P1.option
if __name__ == "__main__":
	main()


