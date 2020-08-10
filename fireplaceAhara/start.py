#!/usr/bin/env python
import sys

from fireplace import cards
from fireplace.exceptions import GameOver
from hearthstone.enums import CardClass, CardType,PlayState, Zone,State#
import copy
import csv
import random
from fireplace.game import Game
from fireplace.player import Player
from agent_Genzo import GenzoRandom
from agent_Genzo import GenzoStep1
from agent_Genzo import Original_random
from agent_Genzo import HumanInput
from fireplace.utils import random_draft
from Genzo import Genzo,GenzoWeight 

sys.path.append("..")

def setup_play_game():
	#Genzos=[]
	Original=Genzo(GenzoWeight(1,1,1,1,1,1,1,1,1,1),"Original", CardClass.SHAMAN, CardClass.HUNTER)
	Rhokdelar=Genzo(GenzoWeight(1,2,5,2,6,3,2,5,4,5),"Rhokdelar", CardClass.HUNTER, CardClass.HUNTER)
	Human=Genzo(GenzoWeight(1,2,3,4,5,6,7,8,9,1),"Human", CardClass.SHAMAN, CardClass.HUNTER)
	#Genzos.append(Original)
	#Genzos.append(Rhokdelar)
	for k in range(1):
		Count1=0
		Count2=0
		CountDraw=0
		P1=Original
		P2=Rhokdelar
		for i in range(25):
			winner = my_play_one_game(P1,P2)
			print("winner is %r"%winner)
			if winner == P1.name:
				Count1+=1
			elif winner == P2.name:
				Count2+=1
			else:
				CountDraw+=1
		print(" %r (%r) wins: %r"%(P1.name, P1.myClass, Count1))
		print(" %r (%r) wins: %r"%(P2.name, P2.myClass, Count2))
		print(" Draw: %d"%CountDraw)
#
#	my_setup_game()
#
def my_setup_game(P1,P2) -> ".game.Game":
	exclude = ['CFM_672','CFM_621','CFM_095','LOE_076']
	#LOE_076:Sir Finley Mrrgglton
	deck1 = random_draft(P1.myClass,exclude)
	deck2 = random_draft(P2.myClass,exclude)
	player1 = Player(P1.name, deck1, P1.myClass.default_hero)
	player2 = Player(P2.name, deck2, P2.myClass.default_hero)

	game = Game(players=(player1, player2))
	game.start()

	return game
#
#	my_play_one_game()
#
def my_play_one_game(P1,P2) -> ".game.Game":
	game = my_setup_game(P1,P2)
	for player in game.players:
		print("Can mulligan %r" % (player.choice.cards))
		mull_count = random.randint(0, len(player.choice.cards))
		cards_to_mulligan = random.sample(player.choice.cards, mull_count)
		player.choice.choose(*cards_to_mulligan)
	while True:		
		player = game.current_player
		#print("%r starts their turn."%player.name);
		if player.name=="Player1" or player.name=="Player2":
			Original_random(game)
		elif player.name=="Maya":
			Maya_MCTS(game)#マヤ氏の作品
		elif player.name=="Genzo":
			GenzoRandom(game)
		elif player.name=="Human":
			HumanInput(game)
		elif player.name==P1.name:
			game = GenzoStep1(game,P1.weight)
		elif player.name==P2.name:
			game = GenzoStep1(game,P2.weight)
		else:
			Original_random(game)
		
		if game.state==State.COMPLETE:
			if game.current_player.playstate == PlayState.WON:
				return game.current_player.name
			if game.current_player.playstate == PlayState.LOST:
				return game.current_player.opponent.name
			if game.current_player.opponent.playstate == PlayState.LOST:## no need
				return game.current_player.name
			if game.current_player.opponent.playstate == PlayState.WON:## no need
				return game.current_player.opponent.name
			return 'DRAW'
		else:
			game.end_turn()
#
#		main()
#
def main():
	cards.db.initialize()
	if len(sys.argv) > 1:
		numgames = sys.argv[1]
		if not numgames.isdigit():
			sys.stderr.write("Usage: %s [NUMGAMES]\n" % (sys.argv[0]))
			exit(1)
		for i in range(int(numgames)):
			setup_play_game()
	else:
		setup_play_game()

class Evaluation(object):
	"""docstring for Evaluation"""
	def __init__(self, deck,score):
		super(Evaluation, self).__init__()
		self.deck = deck
		self.score=score
	def getScore(self):
		return self.score
		pass		

if __name__ == "__main__":
	main()
