#!/usr/bin/env python
from league_match import set_up_one_game_with_human,setup_play_game
import sys
from card_pair import investigate_card_pair, find_card_pair

sys.path.append("..")

#
#		main()
#
def main():
	from fireplace import cards
	cards.db.initialize()
	#setup_play_game(loopNumber=1,player1isNew=1)#リーグ戦
	#leagueMatch.set_up_one_game_with_human()#人vsCOM
	#investigate_card_pair()
	find_card_pair(1)

if __name__ == "__main__":
	main()
