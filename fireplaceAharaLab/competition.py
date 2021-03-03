from utils import *

def play_round_robin_competition(players: list, matchNumber=10):# players: Agentのリスト
	Nplayer = len(players)
	ScoreWin = [[0 for i in range(Nplayer)] for j in range(Nplayer)]

	for repeat in range(matchNumber):
		for i in range(Nplayer):
			for k in range(Nplayer-1-i):
				j=i+1+k
				agent1 = players[i]
				agent2 = players[j]
				if agent1.name==agent2.name:
					agent1.name += "1"
					agent2.name += "2"
				winner = play_one_game_competition(agent1,agent2,BigDeck.faceHunter, BigDeck.faceHunter,debugLog=True)
				print("winner is %r"%winner)
				if winner == agent1.name:
					ScoreWin[i][j]+=1
				elif winner == agent2.name:
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


def play_one_game_competition(P1: Agent, P2: Agent, deck1=[], deck2=[], HeroHPOption=30, debugLog=True, showFieldHand=True):
	""" 1回ゲームを行う。 """
	from fireplace.utils import random_draft
	from fireplace.player import Player
	import random
	#バグが確認されているものを当面除外する
	exclude = [
		'SCH_199',## neutral-scholo, this card morphs w.r.t. the background when playing
		'SCH_259',## neutral-scholo, while this weapon is played, each turn begin allows me to compare the drawn card and other cards.
		'YOD_009',## this is a hero in galakrond
		'DRG_050','DRG_242','DRG_099',## neutral-dragon/45 These are invoking cards for galakrond
		'ULD_178',## neutral-uldum, this card allows us to add 2 of 4 enchantments when we use.
		]
	if len(deck1)==0:
		deck1 = random_draft(P1.myClass,exclude)#カードクラスに従ったランダムなデッキ
	if len(deck2)==0:
		deck2 = random_draft(P2.myClass,exclude)#カードクラスに従ったランダムなデッキ
	player1 = Player(P1.name, deck1, P1.myClass.default_hero)
	player2 = Player(P2.name, deck2, P2.myClass.default_hero)

	game = GameWithLog(players=(player1, player2))
	game.start()

	for player in game.players:
		#mulligan shuffling
		mull_count = random.randint(0, len(player.choice.cards))
		cards_to_mulligan = random.sample(player.choice.cards, mull_count)
		player.choice.choose(*cards_to_mulligan)
	if HeroHPOption != 30:
		game.player1.hero.max_health = HeroHPOption
		game.player2.hero.max_health = HeroHPOption
	print (">>>>> game begins: %s vs. %s <<<<<"%(game.player1.name, game.player2.name))
	filename = P1.name+"-"+P2.name+str(time.time())+".txt"
	game.setFilename(filename)
	with open(filename, mode="a") as gameshow:
		gameshow.write (">>>>> game begins: "+game.player1.name+" vs. "+game.player2.name+" <<<<<\n")
	while True:	
		#エージェントの処理ここから
		player = game.current_player
		if showFieldHand:
			show_field_hand(game.player1, game.player2, filename)
			print (">>>>> %s 's turn <<<<<"%(player.name))
			with open(filename, mode="a") as gameshow:
				gameshow.write (">>>>> "+player.name+" 's turn <<<<<\n")
		start_time = time.time()
		if player.name==P1.name:
			#Agent.funcには引数 self, game, option, gameLog, debugLogを作ってください
			#please make each Agent.func has attributes 'self, game, option, gameLog, debugLog'
			P1.func(P1, game, option=P1.option, gameLog=game.get_log(), debugLog=debugLog)
		elif player.name==P2.name:
			#Agent.funcには引数 self, game, option, gameLog, debugLogを作ってください
			#please make each Agent.func has attributes 'self, game, option, gameLog, debugLog'
			P2.func(P2, game, option=P2.option, gameLog=game.get_log(), debugLog=debugLog)
		else:
			Original_random(game)#random player by fireplace
		#ターンエンドの処理ここから
		#turn end procedure from here
		if player.choice!=None:
			player.choice=None#somotimes it comes here
		if game.state!=State.COMPLETE:
			try:
				game.end_turn()
				if debugLog:
					print(">>>>>%s 's turn time: %d[sec] <<<<<"%(player.name, time.time()-start_time))
					with open(filename, mode="a") as gameshow:
						gameshow.write(">>>>>"+player.name+" 's turn time: "+str(time.time()-start_time)+"[sec] <<<<<\n\n")
			except GameOver:#まれにおこる
				gameover=0
		#ゲーム終了フラグが立っていたらゲーム終了処理を行う
		#if game was over 
		if game.state==State.COMPLETE:
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