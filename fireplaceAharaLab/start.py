#!/usr/bin/env python
import sys

sys.path.append("..")

#
#		main()
#
def main():
	from fireplace import cards
	cards.db.initialize()
	from utils import Agent,play_set_of_games,play_MechaHunterGames,play_one_game,BigDeck
	from hearthstone.enums import CardClass
	Human=Agent("Human",None,myClass=CardClass.MAGE)
	StandardRandom=Agent("Maya",None) # Classを指定しないとHUNTER
	
	# モンテカルロによる読み切り
	## Maya=Agent("Maya",None)

	# Standardなベクトル評価のエージェント34次元の重みベクトルをオプションとして入力する
	#from agent_Standard import StandardStep1
	#import random
	#opt = []
	#for i in range(34):
	#	opt.append(random.randint(1,10))
	#GhostCatPlayer=Agent("GhostCat", StandardStep1,myOption=opt,myClass=CardClass.WARRIOR)
	#あそび
	#PIPlayer=Agent("Pi", StandardStep1,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8],myClass=CardClass.PRIEST)

	# 言葉で戦略を組み立てるエージェント by Ahara
	#from agent_word_strategy import WS, agent_word_strategy
	#WSplayer = Agent("WS", agent_word_strategy,\
	#	myOption=[WS.ミニョンで敵ヒーローの体力を削る, WS.呪文を使えるなら呪文, WS.ランダムにプレー],\
	#	myClass=CardClass.PRIEST)

	#AngryCat by Ahara 無駄な行為を選択肢から排除するアルゴリズム
	#from agent_AngryCat import AngryCatAI
	#AngryCatPlayer = Agent("AngryCat", AngryCatAI)

	#ゲームプレイ
	play_set_of_games(Human, StandardRandom, gameNumber=1, debugLog=True) 
	#ハンター縛りのデッキ（メカハンター）による対戦
	#play_MechaHunterGames(StandardPlayer, AngryCatPlayer, gameNumber=1, debugLog=True)

	#総当たり戦
	#from competition import play_round_robin_competition
	#play_round_robin_competition([StandardRandom,PIPlayer,AngryCatPlayer],matchNumber=5)

	#特定の2枚のカードのシナジーを調べる(idea by Maya)
	#from card_pair import investigate_card_pair, find_card_pair
	#investigate_card_pair()
	#シナジーのあるカードの組を漠然と探す
	#find_card_pair(1)
	#print("test_branch_yamadamaya")

	pass
if __name__ == "__main__":
	main()
