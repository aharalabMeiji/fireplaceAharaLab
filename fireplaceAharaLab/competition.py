from utils import *
from EloRatingSystem import *

def play_round_robin_competition(players: list, matchNumber = 30):# players: Agentのリスト
	Nplayer = len(players)
	ScoreWin = [0] * Nplayer
	ScoreLose = [0] * Nplayer
	pass
	for repeat in range(matchNumber):
		for i in range(Nplayer):
			for k in range(Nplayer-1-i):
				j=i+1+k
				agent1 = players[i]
				agent2 = players[j]
				PCalculation(agent1,agent2)
				if agent1.name==agent2.name:
					agent1.name += "1"
					agent2.name += "2"
				#print("Start %s vs. %s"%(agent1.name, agent2.name))
				winner = play_one_game(agent1,agent2,BigDeck.faceHunter, BigDeck.faceHunter,debugLog=False)
				#print("winner is %r"%winner)
				if winner == agent1.name:
					newRate(agent1,agent2)
					ScoreWin[i]+=1
					ScoreLose[j]+=1
				elif winner == agent2.name:
					newRate(agent2,agent1)
					ScoreWin[j]+=1
					ScoreLose[i]+=1
	with open("ハンド差実験1vsn枚.csv", mode="a") as standings:
			for i in range(Nplayer):
				#print ("%s: win %d, lose %d(%f)"%(players[i].name,ScoreWin[i], ScoreLose[i],players[i].rating))
				standings.write("%s: win, %d, lose, %d,(%f)\n"%(players[i].name,ScoreWin[i], ScoreLose[i],players[i].rating))
				#standings.write(str(NumLose)+"\n")

	