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
from agent_Standard import StandardRandom
from agent_Standard import StandardStep1
from agent_Hunter import agent_Hunter_random
from fireplace.utils import random_draft
from utils import myAction, myActionValue, ExceptionPlay
from utils import Agent,play_set_of_games,play_one_game

def play_league(createMorph=0, createNew=0, player1isNew=0, player2isNew=0, matchNumber=100):#リーグ戦
	StandardsX=[]
	StandardsY=[]
	class1 = CardClass.HUNTER#3
	class2 = CardClass.PALADIN#5
	filename12 = "test_data"+str(int(class1))+str(int(class2))+".csv"
	filename21 = "test_data"+str(int(class2))+str(int(class1))+".csv"
	test_data = open(filename12, "r")
	for line in test_data:
		div = line.split(',')
		if div[0]!="name" and class1*10+class2 == int(div[1]):
			name=div[0]+'X'
			rating=int(div[2])
			weight=[]
			for i in range(34):
				weight.append(int(div[3+i]))
			thisAgent = Agent(name, StandardStep1,myOption=weight,myClass=class1, rating=rating)
			StandardsX.append(thisAgent)
	test_data.close()
	test_data = open(filename21, "r")
	for line in test_data:
		div = line.split(',')
		if div[0]!="name" and class2*10+class1 == int(div[1]):
			name=div[0]+'Y'
			rating=int(div[2])
			weight=[]
			for i in range(34):
				weight.append(int(div[3+i]))
			thisAgent = Agent(name, StandardStep1,myOption=weight,myClass=class2, rating=rating)
			StandardsY.append(thisAgent)
	test_data.close()
	newName="VoodooDoll"#毎回、何か自分で工夫する
	# Lucentbark,Nozari,CatrinaMuerte,,
	#TakNozwhisker,,WalkingFountain,
	#終わったもの：DarkPeddler,Mrrgglton,MadameLazul,JamboImp
	if createNew==1:
		newWeight = createNewWeight(0)#0:new agent
	if createMorph==1:
		newWeight = createNewWeight(1,StandardsX)#0:1:morphed agent
	if createNew==1 or createMorph==1:
		newAgent=Agent(newName+'X', StandardStep1, myOption=newWeight, myClass=class1, rating=1000)
		StandardsX.append(newAgent)
		newAgent=Agent(newName+'Y', StandardStep1, myOption=newWeight, myClass=class2, rating=1000)
		StandardsY.append(newAgent)

	for k in range(matchNumber):
		Count1=0
		Count2=0
		CountDraw=0
		if player1isNew==0:
			P1=random.choice(StandardsX)#full random
		else:
			P1=StandardsX[-1]#last one
		if player2isNew==0:
			P2=random.choice(StandardsY)#full random
		else :
			P2=StandardsY[-1]#last one
		print(" %r (%s) vs.  %r (%s)"%(P1.name, P1.myClass, P2.name, P2.myClass))
		for i in range(19):
			winner = play_one_game(P1,P2,debugLog=False)
			print("winner is %r"%winner)
			if winner == P1.name:
				Count1+=1
			elif winner == P2.name:
				Count2+=1
			else:
				CountDraw+=1
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
			for P in StandardsX:
				text = (P.name[:-1])+','+str(int(class1))+str(int(class2))+','+str(P.rating)+','
				for i in range(34):
					text += str(P.option[i])+','
				text += "\n"
				f.write(text)
		with open(filename21, mode='w') as f:
			f.write("name,class,rating\n")
			for P in StandardsY:
				text = (P.name[:-1])+','+str(int(class2))+str(int(class1))+','+str(P.rating)+','
				for i in range(34):
					text += str(P.option[i])+','
				text += "\n"
				f.write(text)
#
#  createNewWeight()
#
def createNewWeight(option,StandardsX=None):
	if option==0:
		weight=[]
		for i in range(34):
			weight.append(random.randint(1,9))
		return weight
	else:
		#既存のものの変形
		originalAgent = random.choice(StandardsX)
		newWeight = weight_deepcopy_and_perturb(originalAgent.weight)
		return newWeight

