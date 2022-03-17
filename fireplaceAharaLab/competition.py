from utils import *
from EloRatingSystem import *
import numpy as np

def play_round_robin_competition(players: list, matchNumber=10):# players: Agentのリスト
	Nplayer = len(players)
	ScoreWin = [[0 for i in range(Nplayer)] for j in range(Nplayer)]
	pass

	for i in range(Nplayer):
		for k in range(Nplayer-1-i):
			j=i+1+k
			agent1 = players[i]
			agent2 = players[j]
			PCalculation(agent1,agent2)
			if agent1.name==agent2.name:
				agent1.name += "1"
				agent2.name += "2"
			deck1,deck2= DeckSelecter()

			print("Start %s(%s) vs. %s(%s)"%(agent1.name, BigDeck.name(deck1), agent2.name, BigDeck.name(deck2)))
			for repeat in range(matchNumber):
				winner = play_one_game_competition(agent1,agent2,deck1, deck2,debugLog=False)
				print("winner is %r"%winner)
				if winner == agent1.name:
					newRate(agent1,agent2)
					ScoreWin[i][j]+=1
				elif winner == agent2.name:
					newRate(agent2,agent1)
					ScoreWin[j][i]+=1
			print("Start %s(%s) vs. %s(%s)"%(agent1.name, BigDeck.name(deck2), agent2.name, BigDeck.name(deck1)))
			for repeat in range(matchNumber):
				winner = play_one_game_competition(agent1,agent2,deck2, deck1,debugLog=False)
				print("winner is %r"%winner)
				if winner == agent1.name:
					newRate(agent1,agent2)
					ScoreWin[i][j]+=1
				elif winner == agent2.name:
					newRate(agent2,agent1)
					ScoreWin[j][i]+=1

	with open("standings.csv", mode="w") as standings:
				for x in range(Nplayer):
					NumWin=0
					NumLose=0
					standings.write(players[x].name+",")
					for y in range(Nplayer):
						standings.write(str(ScoreWin[x][y])+",")
						NumWin += ScoreWin[x][y]
						NumLose += ScoreWin[y][x]
					standings.write(str(NumWin)+",")
					standings.write(str(NumLose)+"\n")
					print ("%s: win %d, lose %d(%f)"%(players[x].name,NumWin, NumLose,players[x].rating))

def DeckSelecter():
	ran = np.random.randint(0, 3,1)
	if ran ==0:
		return BigDeck.clownDruid, BigDeck.faceHunter
	elif ran ==1:
		return BigDeck.faceHunter, BigDeck.bigWarrior
	else:
		return BigDeck.bigWarrior, BigDeck.clownDruid


#def play_one_game_competition(P1: Agent, P2: Agent, deck1=[], deck2=[], HeroHPOption=30, debugLog=True, showFieldHand=True):
def play_one_game_competition(P1: Agent, P2: Agent, deck1=[], deck2=[], debugLog=True, HEROHPOPTION=30, P1MAXMANA=1, P2MAXMANA=1, P1HAND=3, P2HAND=3, showFieldHand=True):
	""" エージェント同士で1回対戦する。
	実験的に、ヒーローの体力、初期マナ数、初期ハンド枚数をコントロールできます。
	play one game by P1 and P2 """
	from fireplace.utils import random_draft
	from fireplace.player import Player
	import random
	exclude = []# you may exclude some cards to construct a deck
	log.info("New game settings")
	if len(deck1)==0:
		deck1 = random_draft(P1.myClass,exclude)#random deck wrt its class
	if len(deck2)==0:
		deck2 = random_draft(P2.myClass,exclude)#random deck wrt its class
	player1 = Player(P1.name, deck1, P1.myClass.default_hero)
	player2 = Player(P2.name, deck2, P2.myClass.default_hero)
	player1.choiceStrategy = P1.choiceStrategy
	player2.choiceStrategy = P2.choiceStrategy
	game = Game(players=(player1, player2))
	# Configurations
	player1._start_hand_size=P1HAND## this line must be before 'start()'
	player2._start_hand_size=P2HAND## 
	player1.max_mana=int(P1MAXMANA)-1## this line must be before 'start()'
	player2.max_mana=int(P2MAXMANA)-1
	game.start()
	player1.hero.max_health = int(HEROHPOPTION)## this line must be below 'start()'
	player2.hero.max_health = int(HEROHPOPTION)## 


	#mulligan exchange
	# Any agent are allowed to give an algorithm to do mulligan exchange.
	for player in game.players:
		if player.name==P1.name:
			if P1.mulliganStrategy == None:
				mull_count = random.randint(0, len(player.choice.cards))
				cards_to_mulligan = random.sample(player.choice.cards, mull_count)
			else:
				cards_to_mulligan = P1.mulliganStrategy(P1, player.choice.cards)
		elif player.name==P2.name:
			if P2.mulliganStrategy == None:
				mull_count = random.randint(0, len(player.choice.cards))
				cards_to_mulligan = random.sample(player.choice.cards, mull_count)
			else:
				cards_to_mulligan = P2.mulliganStrategy(P2, player.choice.cards)
		player.choice.choose(*cards_to_mulligan)# includes begin_turn()
	#mulligan exchange end
	log.info("New game start")

	print (">>>>> game begins: %s vs. %s <<<<<"%(game.player1.name, game.player2.name))
	filename = P1.name+"-"+P2.name+"("+BigDeck.name(deck1)+"-"+BigDeck.name(deck2)+")"+str(time.time())+".txt"
	#game.setFilename(filename)
	with open(filename, mode="a") as gameshow:
		gameshow.write (">>>>> game begins: "+game.player1.name+"("+BigDeck.name(deck1)+")"+" vs. "+game.player2.name+"("+BigDeck.name(deck2)+")"+" <<<<<\n")
	while True:	
		#game main loop
		player = game.current_player
		if showFieldHand:
			show_field_hand(game.player1, game.player2, filename)
			if debugLog:
				print (">>>>> %s 's turn <<<<<"%(player.name))
			with open(filename, mode="a") as gameshow:
				gameshow.write (">>>>> "+player.name+" 's turn <<<<<\n")
		start_time = time.time()
		if player.name==P1.name:
			#please make each Agent.func has arguments 'self, game, option, gameLog, debugLog'
			P1.func(P1, game, option=P1.option, gameLog=game.get_log(), debugLog=debugLog)
		elif player.name==P2.name:
			#please make each Agent.func has arguments 'self, game, option, gameLog, debugLog'
			P2.func(P2, game, option=P2.option, gameLog=game.get_log(), debugLog=debugLog)
		else:
			Original_random(game)#random player by fireplace
		#turn end procedure from here
		if player.choice!=None:
			player.choice=None#somotimes it comes here
		if game.state!=State.COMPLETE:
			try:
				game.end_turn()
				if debugLog:
					print(">>>>%s>>>>turn change %d[sec]>>>>%s"%(player, time.time()-start_time, player.opponent),end='  ')
					print("%d : %d"%(player1.hero.health+player1.hero.armor,player2.hero.health+player2.hero.armor))
					with open(filename, mode="a") as gameshow:
						gameshow.write(">>>>>"+player.name+" 's turn time: "+str(time.time()-start_time)+"[sec] <<<<<\n\n")
				if game.current_player.choice!=None:
					postAction(game.current_player)
			except GameOver:#it rarely occurs
				gameover=0
		#ゲーム終了フラグが立っていたらゲーム終了処理を行う
		#if game was over 
		if game.state==State.COMPLETE:
			if debugLog:
				print(">>>>>>>>>>game end >>>>>>>>"%(),end=' ')
				print("%d : %d"%(player1.hero.health,player2.hero.health))
			if game.current_player.playstate == PlayState.WON:
				return game.current_player.name
			if game.current_player.playstate == PlayState.LOST:
				return game.current_player.opponent.name
			return 'DRAW'#Maybe impossible to come here.



def show_field_hand(Player1, Player2, filename):
	with open(filename, mode="a") as display:
		display.write("========%s 's HAND======\n"%(Player1.name))
		player = Player1
		for card in player.hand:
			display.write("%s   : "%card)
			if card.data.type == CardType.MINION:
				display.write("%2d(%2d/%2d)%s\n"%(card.cost, card.atk, card.health, card.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
			elif card.data.type == CardType.SPELL:
				display.write("%2d : %s\n"%(card.cost, card.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
			elif card.data.type == CardType.WEAPON:
				display.write("%2d(%2d/%2d) : %s\n"%(card.cost, card.atk, card.durability, card.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
		display.write("========%s 's SECRETS======\n"%(Player1.name))
		for card in player.secrets:
			display.write("%s   : "%card)
			if hasattr(card, 'sidequest'):
				display.write("(%d)"%card._tmp_int1_)
			display.write("%s\n"%(card.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
		display.write("========%s 's PLAYGROUND======\n"%(Player1.name))
		for character in player.characters:
			display.write("%s   : "%character)
			if character == player.hero:
				if player.weapon:
					display.write("(%2d/%2d/%2d+%d)(%s)"%(character.atk,player.weapon.durability,character.health,character.armor,player.weapon.data.name))
				else:
					display.write("(%2d/%2d+%d)"%(character.atk,character.health,character.armor))
			else :
				display.write("(%2d/%2d)"%(character.atk,character.health))
				if character.silenced:
					display.write("(silenced)")
				if character.windfury:
					display.write("(windfury)")
				if character.poisonous:
					display.write("(poisonous)")
				if character.frozen:
					display.write("(frozen)")
				if character.reborn:
					display.write("(reborn)")
				if character.taunt:
					display.write("(taunt)")
				if character.stealthed:
					display.write("(stealthed)")
				if character.divine_shield:
					display.write("(divine_shield)")
				if character.dormant!=0:
					display.write("(dormant:%d)"%(character.dormant))
				if character.spellpower>0:
					display.write("(spellpower:%d)"%(character.spellpower))
			display.write(" %s\n"%(character.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
		if player.hero.power.is_usable():
			display.write("%s   : "%player.hero.power)
			display.write("<%2d>"%player.hero.power.cost)
			display.write("%s\n"%player.hero.power.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']'))
		display.write("========%s 's PLAYGROUND======\n"%(Player2.name))
		player = Player2
		for character in player.characters:
			display.write("%s   : "%character)
			if character == player.hero:
				if player.weapon:
					display.write("(%2d/%2d/%2d+%d)(%s)"%(character.atk,player.weapon.durability,character.health,character.armor,player.weapon.data.name))
				else:
					display.write("(%2d/%2d+%d)"%(character.atk,character.health,character.armor))
			else :
				display.write("(%2d/%2d)"%(character.atk,character.health))
				if character.silenced:
					display.write("(silenced)")
				if character.windfury:
					display.write("(windfury)")
				if character.poisonous:
					display.write("(poisonous)")
				if character.frozen:
					display.write("(frozen)")
				if character.reborn:
					display.write("(reborn)")
				if character.taunt:
					display.write("(taunt)")
				if character.stealthed:
					display.write("(stealthed)")
				if character.divine_shield:
					display.write("(divine_shield)")
				if character.dormant!=0:
					display.write("(dormant:%d)"%(character.dormant))
				if character.spellpower>0:
					display.write("(spellpower:%d)"%(character.spellpower))
			display.write("%s\n"%(character.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
		if player.hero.power.is_usable():
			display.write("%s   : "%player.hero.power)
			display.write("<%2d>"%player.hero.power.cost)
			display.write("%s\n"%player.hero.power.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']'))
		display.write("========%s 's SECRETS======\n"%(Player2.name))
		for card in player.secrets:
			display.write("%s   : "%card)
			if hasattr(card, 'sidequest'):
				display.write("(%d)"%card._tmp_int1_)
			display.write("%s\n"%(card.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
		display.write("========%s 's HAND======\n"%(Player2.name))
		for card in player.hand:
			display.write("%s   : "%card)
			if card.data.type == CardType.MINION:
				display.write("%2d(%2d/%2d)%s\n"%(card.cost, card.atk, card.health, card.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
			elif card.data.type == CardType.SPELL:
				display.write("%2d : %s\n"%(card.cost, card.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
			elif card.data.type == CardType.WEAPON:
				display.write("%2d(%2d/%2d) : %s\n"%(card.cost, card.atk, card.durability, card.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
		pass
