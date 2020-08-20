#!/usr/bin/env python
import sys

sys.path.append("..")

#
#		main()
#
def main():
	from fireplace import cards
	cards.db.initialize()
	from utils import Agent,play_set_of_games
	from hearthstone.enums import CardClass
	Human=Agent("Human",None,myClass=CardClass.MAGE)
	StandardRandom=Agent("Standard",None) # Classを指定しないとHUNTER
	
	## Maya=Agent("Maya",None)

	# StandardStep1 のように、オプション付きのオリジナルエージェントも呼び出すことができる。
	#from agent_Standard import StandardStep1,StandardWeight
	#StandardPlayer=Agent("GhostCat", StandardStep1,\
	#   myOption=StandardWeight([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]),\
	#   myClass=CardClass.WARRIOR)# StandardStep1(game, option, debugLog) が　呼び出すべき関数名

	#from agent_word_strategy import WS, agent_word_strategy
	#WSplayer = Agent("WS", agent_word_strategy,\
	#	myOption=[WS.ミニョンで敵ヒーローの体力を削る, WS.呪文を使えるなら呪文, WS.ランダムにプレー],\
	#	myClass=CardClass.PRIEST)

	#ゲームプレイ
	play_set_of_games(Human, StandardRandom, gameNumber=1, debugLog=True) 
	
	##StandardStep1のリーグ戦
	#from league_match import play_league
	#play_league(matchNumber=1)

	#from card_pair import investigate_card_pair, find_card_pair
	#investigate_card_pair()
	#find_card_pair(1)


	pass
if __name__ == "__main__":
	main()
