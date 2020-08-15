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


def set_up_one_game_with_human():#人vsCOM
	GenzosX=[]
	class1 = CardClass.HUNTER#3
	class2 = CardClass.PALADIN#5
	filename = "test_data"+str(int(class1))+str(int(class2))+".csv"
	test_data = open(filename, "r")
	for line in test_data:
		div = line.split(',')
		if div[0]!="name" and class1*10+class2 == int(div[1]):
			name=div[0]
			rating=int(div[2])
			weight=[int(div[3]),int(div[4]),int(div[5]),int(div[6]),int(div[7]),int(div[8]),int(div[9]),int(div[10]),int(div[11]),int(div[12]),int(div[13]),int(div[14]),int(div[15]),int(div[16]),int(div[17]),int(div[18]),int(div[19]),int(div[20]),int(div[21]),int(div[22])]
			thisAgent = Genzo(GenzoWeight(weight), name, class1, class2,rating)
			GenzosX.append(thisAgent)
	test_data.close()
	P1 = random.choice(GenzosX)
	P2=Genzo(GenzoWeight([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]),"Human", class2, class1,1000)
	winner = my_play_one_game(P1,P2)
	print("winner is %r"%winner)
	print(" %r (%r) wins: %r"%(P1.name, P1.myClass, Count1))
	print(" %r (%r) wins: %r"%(P2.name, P2.myClass, Count2))

def setup_play_game(createMorph=0, createNew=0, player1isNew=0, player2isNew=0, loopNumber=100):#リーグ戦
	GenzosX=[]
	GenzosY=[]
	class1 = CardClass.HUNTER#3
	#class2 = CardClass.MAGE#4
	class2 = CardClass.PALADIN#5
	filename12 = "test_data"+str(int(class1))+str(int(class2))+".csv"
	filename21 = "test_data"+str(int(class2))+str(int(class1))+".csv"
	test_data = open(filename12, "r")
	for line in test_data:
		div = line.split(',')
		if div[0]!="name" and class1*10+class2 == int(div[1]):
			name=div[0]+'X'
			rating=int(div[2])
			weight=[int(div[3]),int(div[4]),int(div[5]),int(div[6]),int(div[7]),\
				int(div[8]),int(div[9]),int(div[10]),int(div[11]),int(div[12]),\
				int(div[13]),int(div[14]),int(div[15]),int(div[16]),int(div[17]),\
				int(div[18]),int(div[19]),int(div[20]),int(div[21]),int(div[22])]
			thisAgent = Genzo(GenzoWeight(weight), name, class1, class2,rating)
			GenzosX.append(thisAgent)
	test_data.close()
	test_data = open(filename21, "r")
	for line in test_data:
		div = line.split(',')
		if div[0]!="name" and class2*10+class1 == int(div[1]):
			name=div[0]+'Y'
			rating=int(div[2])
			weight=[int(div[3]),int(div[4]),int(div[5]),int(div[6]),int(div[7]),\
				int(div[8]),int(div[9]),int(div[10]),int(div[11]),int(div[12]),\
				int(div[13]),int(div[14]),int(div[15]),int(div[16]),int(div[17]),\
				int(div[18]),int(div[19]),int(div[20]),int(div[21]),int(div[22])]
			thisAgent = Genzo(GenzoWeight(weight), name, class2, class1, rating)
			GenzosY.append(thisAgent)
	test_data.close()
	newName="JumboImp"#毎回、何か自分で工夫する
	#,,VoodooDoll,,Lucentbark,Nozari,CatrinaMuerte,,
	#TakNozwhisker,,WalkingFountain,
	#終わったもの：DarkPeddler,Mrrgglton,MadameLazul
	if createNew==1:
		newWeight = createNewWeight(0)#0:new agent
	if createMorph==1:
		newWeight = createNewWeight(1,GenzosX)#0:1:morphed agent
	if createNew==1 or createMorph==1:
		newAgent=Genzo(newWeight, newName+'X', class1, class2, 1000)
		GenzosX.append(newAgent)
		mewAgent=Genzo(newWeight, newName+'Y', class2, class1, 1000)
		GenzosY.append(mewAgent)

	#Human=Genzo(GenzoWeight(1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0),"Human", CardClass.SHAMAN, CardClass.HUNTER,1000)
	for k in range(loopNumber):
		Count1=0
		Count2=0
		CountDraw=0
		if player1isNew==0:
			P1=random.choice(GenzosX)#full random
		else:
			P1=GenzosX[-1]#last one
		if player2isNew==0:
			P2=random.choice(GenzosY)#full random
		else :
			P2=GenzosY[-1]#last one
		print(" %r (%s) vs.  %r (%s)"%(P1.name, P1.myClass, P2.name, P2.myClass))
		for i in range(19):
			winner = my_play_one_game(P1,P2)
			print("winner is %r"%winner)
			if winner == P1.name:
				Count1+=1
			elif winner == P2.name:
				Count2+=1
			else:
				CountDraw+=1
		#print(" %r (%r) wins: %r"%(P1.name, P1.myClass, Count1))
		#print(" %r (%r) wins: %r"%(P2.name, P2.myClass, Count2))
		#print(" Draw: %d"%CountDraw)

		import math
		# rating
		diff=math.exp(float(P1.rating-P2.rating)*0.01)# レーティングが100違うとe倍の実力差
		e12=diff/(1.0+diff)
		e21=1.0/(1.0+diff)
		K=2.0
		newRating1 = P1.rating+round((e21*Count1-e12*Count2)*K)
		newRating2 = P2.rating+round((e12*Count2-e21*Count1)*K)
		if newRating1<1:
			newRating1=1;
		if newRating2<1:
			newRating2=1;
		print(" %r (%r) wins: %d, rating: %d->%d"%(P1.name, P1.myClass, Count1, P1.rating, newRating1))
		print(" %r (%r) wins: %d, rating: %d->%d"%(P2.name, P2.myClass, Count2, P2.rating, newRating2))
		P1.rating=newRating1
		P2.rating=newRating2
		#class1=class2のときはratingをそろえる作業が入る。
		with open(filename12, mode='w') as f:
			f.write("name,class,rating\n")
			for P in GenzosX:
				text = (P.name[:-1])+','+str(int(class1))+str(int(class2))+','+str(P.rating)+','
				text += str(P.weight)+'\n'
				f.write(text)
		with open(filename21, mode='w') as f:
			f.write("name,class,rating\n")
			for P in GenzosY:
				text = (P.name[:-1])+','+str(int(class2))+str(int(class1))+','+str(P.rating)+','
				text += str(P.weight)+'\n'
				f.write(text)
#
#  createNewWeight()
#
def createNewWeight(option,GenzosX=None):
	if option==0:
		weight=[]
		for i in range(20):
			weight.append(random.randint(1,9))
		return GenzoWeight(weight)
	else:
		#既存のものの変形
		originalAgent = random.choice(GenzosX)
		newWeight = originalAgent.weight.deepcopyAndPerturb()
		return newWeight

#
#	my_setup_game()
#
def my_setup_game(P1,P2) -> ".game.Game":
	exclude = ['CFM_672','CFM_621','CFM_095','LOE_076','BT_490']
	#LOE_076:Sir Finley Mrrgglton
	#'BT_490'魔力喰い、ターゲットの扱いにエラーがあるので除外。
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
		if game.state!=State.COMPLETE:
			try:
				game.end_turn()
			except GameOver:#まれにおこる
				gameover=0
		if game.state==State.COMPLETE:
			if game.current_player.playstate == PlayState.WON:
				return game.current_player.name
			if game.current_player.playstate == PlayState.LOST:
				return game.current_player.opponent.name
			return 'DRAW'






