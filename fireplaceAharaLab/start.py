#!/usr/bin/env python
from league_match import set_up_one_game_with_human,setup_play_game,set_up_one_game_hunter_vs_human
import sys
from card_pair import investigate_card_pair, find_card_pair

sys.path.append("..")

#
#		main()
#
def main():
	from fireplace import cards
	cards.db.initialize()
	#setup_play_game(loopNumber=1)#リーグ戦
	#set_up_one_game_with_human()#人vsCOM
	#set_up_one_game_hunter_vs_human()#人vsHunter
	investigate_card_pair()
	#find_card_pair(1)


	pass
if __name__ == "__main__":
	main()
