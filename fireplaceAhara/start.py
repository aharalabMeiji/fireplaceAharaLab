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
from agent_Ahara import AharaRandom
from agent_Ahara import AharaStep1
from agent_Ahara import Original_random
from agent_Ahara import HumanInput
from fireplace.utils import random_draft


sys.path.append("..")

def setup_play_game():
	for k in range(1):
		Count1=0
		Count2=0
		for i in range(10):
			print(random.randint(1,6), end=',') 
		name1="Kazakus"
		name2="Rhokdelar"
		class1 = CardClass.HUNTER
		class2 = CardClass.HUNTER
		for i in range(25):
			winner = my_play_one_game(name1,name2,class1, class2)
			print("winner is %r"%winner)
			if winner == name1:
				Count1+=1
			elif winner == name2:
				Count2+=1
		print(" %r wins: %r"%(name1,Count1))
		print(" %r wins: %r"%(name2,Count2))
#
#	my_play_one_game()
#
def my_play_one_game(name1,name2,class1, class2) -> ".game.Game":
	game = my_setup_game(name1,name2,class1, class2)
	for player in game.players:
		print("Can mulligan %r" % (player.choice.cards))
		mull_count = random.randint(0, len(player.choice.cards))
		cards_to_mulligan = random.sample(player.choice.cards, mull_count)
		player.choice.choose(*cards_to_mulligan)
	try:
		while True:		
			my_play_turn(game)
	except GameOver as inst:
		if game.current_player.playstate == PlayState.WON:
			return game.current_player.name
		if game.current_player.playstate == PlayState.LOST:
			return game.current_player.opponent.name
	return game.current_player.name
#
#	my_setup_game()
#
def my_setup_game(name1,name2,class1,class2) -> ".game.Game":
	exclude = ['CFM_672','CFM_621']
	deck1 = random_draft(class1,exclude)
	deck2 = random_draft(class2,exclude)
	player1 = Player(name1, deck1, class1.default_hero)
	player2 = Player(name2, deck2, class2.default_hero)

	game = Game(players=(player1, player2))
	game.start()

	return game
def my_play_turn(game: ".game.Game") -> ".game.Game":
	player = game.current_player
	#print("%r starts their turn."%player.name);
	if player.name=="Player1" or player.name=="Player2":
		# ここにAIのコードを記入
		Original_random(game)
	elif player.name=="Maya":
		# ここにAIのコードを記入
		Maya_MCTS(game)#マヤ氏の作品
	elif player.name=="Ahara":
		# ここにAIのコードを記入
		AharaRandom(game)
	elif player.name=="Ahara1":
		# ここにAIのコードを記入
		AharaStep1(game,[1,-1,1,1,1,-1,-1,-1,1,1])
	elif player.name=="Kazakus":
		# ここにAIのコードを記入
		AharaStep1(game,[1,-2,5,2,6,-3,-2,-5,4,5])
	elif player.name=="Rhokdelar":
		# ここにAIのコードを記入
		AharaStep1(game,[5,-4,5,2,3,-6,-2,-5,2,1])
	elif player.name=="Human":
		# ここにAIのコードを記入
		HumanInput(game)
	else:
		Original_random(game)
	game.end_turn()
	return game
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
