from utils import *

def play_round_robin_competition(players: list, matchNumber=10):# players: Agentのリスト
	Nplayer = len(players)
	ScoreWin = [0] * Nplayer
	ScoreLose = [0] * Nplayer
	pass

	for i in range(Nplayer):
		for k in range(Nplayer-1-i):
			j=i+1+k
			agent1 = players[i]
			agent2 = players[j]
			if agent1.name==agent2.name:
				agent1.name += "1"
				agent2.name += "2"
			print("Start %s vs. %s"%(agent1.name, agent2.name))
			for repeat in range(matchNumber):
				winner = play_one_game(agent1,agent2,debugLog=False)
				print("winner is %r"%winner)
				if winner == agent1.name:
					ScoreWin[i]+=1
					ScoreLose[j]+=1
				elif winner == agent2.name:
					ScoreWin[j]+=1
					ScoreLose[i]+=1
	for i in range(Nplayer):
		print ("%s: win %d, lose %d"%(players[i].name,ScoreWin[i], ScoreLose[i]))
