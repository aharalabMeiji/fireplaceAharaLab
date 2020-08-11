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
from enum import IntEnum
from agent_Genzo import GenzoRandom
from agent_Genzo import GenzoStep1
from agent_Genzo import Original_random
from agent_Genzo import HumanInput
from fireplace.utils import random_draft
from Genzo import Genzo,GenzoWeight 

sys.path.append("..")

def setup_play_game():
	GenzosX=[]
	GenzosY=[]
	class1 = CardClass.HUNTER#3
	class2 = CardClass.MAGE#4
	filename12 = "test_data"+str(int(class1))+str(int(class2))+".txt"
	filename21 = "test_data"+str(int(class2))+str(int(class1))+".txt"
	test_data = open(filename12, "r")
	for line in test_data:
		div = line.split(',')
		if class1*10+class2 == int(div[1]):
			name=div[0]
			rating=int(div[2])
			weight=GenzoWeight(int(div[3]),int(div[4]),int(div[5]),int(div[6]),int(div[7]),int(div[8]),int(div[9]),int(div[10]),int(div[11]),int(div[12]))
			thisAgent = Genzo(weight, name,class1, class2,rating)
			GenzosX.append(thisAgent)
	test_data.close()
	test_data = open(filename21, "r")
	for line in test_data:
		div = line.split(',')
		if class2*10+class1 == int(div[1]):
			name=div[0]
			rating=int(div[2])
			weight=GenzoWeight(int(div[3]),int(div[4]),int(div[5]),int(div[6]),int(div[7]),int(div[8]),int(div[9]),int(div[10]),int(div[11]),int(div[12]))
			thisAgent = Genzo(weight, name, class2, class1, rating)
			GenzosY.append(thisAgent)
	test_data.close()
	newName="CatrinaMuerte"#毎回、何か自分で工夫する
	#,Tak Nozwhisker,Togwaggle,Walking Fountain,Fel Lord Betrug,Jumbo Imp,Boom Reaver,Elysiana
	newWeight=createNewWeight()#新作
	#newWeight=NearExsiting()#既存のものの変形
	newAgent=Genzo(newWeight,newName,class1,class2,100)
	GenzosX.append(newAgent)
	newAgent=Genzo(newWeight,newName,class2,class1,100)
	GenzosY.append(newAgent)

	Human=Genzo(GenzoWeight(1,2,3,4,5,6,7,8,9,1),"Human", CardClass.SHAMAN, CardClass.HUNTER,100)
	for k in range(20):
		Count1=0
		Count2=0
		CountDraw=0
		P1=random.choice(GenzosX)
		P2=random.choice(GenzosY)
		for i in range(10):
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

		import math
		# rating
		diff=math.exp((P1.rating-P2.rating)*0.02)# レーティングが50違うとe倍の実力差
		e12=diff/(1+diff)
		e21=1/1+diff
		K=2
		newRating1 = P1.rating+round((Count1*e21-Count2*e12)*K)
		newRating2 = P2.rating+round((Count2*e12-Count1*e21)*K)
		if newRating1<1:
			newRating1=1;
		if newRating2<1:
			newRating2=1;
		P1.rating=newRating1
		P2.rating=newRating2
		#class1=class2のときはratingをそろえる作業が入る。
		with open(filename12, mode='w') as f:
			for P in GenzosX:
				text = P.name+','+str(int(class1))+str(int(class2))+','+str(P.rating)+','
				text += str(P.weight)+'\n'
				f.write(text)
		with open(filename21, mode='w') as f:
			for P in GenzosY:
				text = P.name+','+str(int(class2))+str(int(class1))+','+str(P.rating)+','
				text += str(P.weight)+'\n'
				f.write(text)
#
#  createNewWeight()
#
def createNewWeight():
	return GenzoWeight(random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9),random.randint(1,9))
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
		#print("Can mulligan %r" % (player.choice.cards))
		mull_count = random.randint(0, len(player.choice.cards))
		cards_to_mulligan = random.sample(player.choice.cards, mull_count)
		player.choice.choose(*cards_to_mulligan)
	turnNumber=0
	print("Turn ",end='--')
	while True:	
		turnNumber+=1
		print("%d"%turnNumber,end=':')
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
			GenzoStep1(game,P1.weight)
		elif player.name==P2.name:
			GenzoStep1(game,P2.weight)
		else:
			Original_random(game)
		if player.choice!=None:#不要なはずだが、ねんのため
			player.choice=None
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
