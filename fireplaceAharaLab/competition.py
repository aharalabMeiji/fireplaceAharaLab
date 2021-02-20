from utils import *

def play_round_robin_competition(players: list, matchNumber=10):# players: Agentのリスト
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
				if agent1.name==agent2.name:
					agent1.name += "1"
					agent2.name += "2"
				winner = play_one_game_competition(agent1,agent2,BigDeck.faceHunter, BigDeck.faceHunter,debugLog=True)
				print("winner is %r"%winner)
				if winner == agent1.name:
					ScoreWin[i]+=1
					ScoreLose[j]+=1
				elif winner == agent2.name:
					ScoreWin[j]+=1
					ScoreLose[i]+=1
	for i in range(Nplayer):
		print ("%s: win %d, lose %d"%(players[i].name,ScoreWin[i], ScoreLose[i]))

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
	while True:	
		#エージェントの処理ここから
		player = game.current_player
		if showFieldHand:
			show_field_hand(game.player1, game.player2)
			print (">>>>> %s 's turn <<<<<"%(player.name))
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

def show_field_hand(Player1, Player2):
	print("========%s 's HAND======"%(Player1.name))
	player = Player1
	for card in player.hand:
		print("%s"%card, end='   : ')
		if card.data.type == CardType.MINION:
			print("%2d(%2d/%2d)%s"%(card.cost, card.atk, card.health, card.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
		elif card.data.type == CardType.SPELL:
			print("%2d : %s"%(card.cost, card.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
		elif card.data.type == CardType.WEAPON:
			print("%2d(%2d/%2d) : %s"%(card.cost, card.atk, card.durability, card.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
	print("========%s 's SECRETS======"%(Player1.name))
	for card in player.secrets:
		print("%s"%card, end='   : ')
		if hasattr(card, 'sidequest'):
			print("(%d)"%card._tmp_int1_, end="")
		print("%s"%(card.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
	print("========%s 's PLAYGROUND======"%(Player1.name))
	for character in player.characters:
		print("%s"%character, end='   : ')
		if character == player.hero:
			if player.weapon:
				print("(%2d/%2d/%2d+%d)(%s)"%(character.atk,player.weapon.durability,character.health,character.armor,player.weapon.data.name), end=" ")
			else:
				print("(%2d/%2d+%d)"%(character.atk,character.health,character.armor), end=" ")
		else :
			print("(%2d/%2d)"%(character.atk,character.health), end=" ")
			if character.silenced:
				print("(silenced)", end=" ")
			if character.windfury:
				print("(windfury)", end=" ")
			if character.poisonous:
				print("(poisonous)", end=" ")
			if character.frozen:
				print("(frozen)", end=" ")
			if character.reborn:
				print("(reborn)", end=" ")
			if character.taunt:
				print("(taunt)", end=" ")
			if character.stealthed:
				print("(stealthed)", end=" ")
			if character.divine_shield:
				print("(divine_shield)", end=" ")
			if character.dormant!=0:
				print("(dormant:%d)"%(character.dormant), end=" ")
			if character.spellpower>0:
				print("(spellpower:%d)"%(character.spellpower), end=" ")
		print("%s"%(character.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
	if player.hero.power.is_usable():
		print("%s"%player.hero.power, end='   : ')
		print("<%2d>"%player.hero.power.cost, end=' ')
		print("%s"%player.hero.power.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']'))
	print("========%s 's PLAYGROUND======"%(Player2.name))
	player = Player2
	for character in player.characters:
		print("%s"%character, end='   : ')
		if character == player.hero:
			if player.weapon:
				print("(%2d/%2d/%2d+%d)(%s)"%(character.atk,player.weapon.durability,character.health,character.armor,player.weapon.data.name), end=" ")
			else:
				print("(%2d/%2d+%d)"%(character.atk,character.health,character.armor), end=" ")
		else :
			print("(%2d/%2d)"%(character.atk,character.health), end=" ")
			if character.silenced:
				print("(silenced)", end=" ")
			if character.windfury:
				print("(windfury)", end=" ")
			if character.poisonous:
				print("(poisonous)", end=" ")
			if character.frozen:
				print("(frozen)", end=" ")
			if character.reborn:
				print("(reborn)", end=" ")
			if character.taunt:
				print("(taunt)", end=" ")
			if character.stealthed:
				print("(stealthed)", end=" ")
			if character.divine_shield:
				print("(divine_shield)", end=" ")
			if character.dormant!=0:
				print("(dormant:%d)"%(character.dormant), end=" ")
			if character.spellpower>0:
				print("(spellpower:%d)"%(character.spellpower), end=" ")
		print("%s"%(character.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
	if player.hero.power.is_usable():
		print("%s"%player.hero.power, end='   : ')
		print("<%2d>"%player.hero.power.cost, end=' ')
		print("%s"%player.hero.power.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']'))
	print("========%s 's SECRETS======"%(Player2.name))
	for card in player.secrets:
		print("%s"%card, end='   : ')
		if hasattr(card, 'sidequest'):
			print("(%d)"%card._tmp_int1_, end="")
		print("%s"%(card.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
	print("========%s 's HAND======"%(Player2.name))
	for card in player.hand:
		print("%s"%card, end='   : ')
		if card.data.type == CardType.MINION:
			print("%2d(%2d/%2d)%s"%(card.cost, card.atk, card.health, card.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
		elif card.data.type == CardType.SPELL:
			print("%2d : %s"%(card.cost, card.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
		elif card.data.type == CardType.WEAPON:
			print("%2d(%2d/%2d) : %s"%(card.cost, card.atk, card.durability, card.data.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
	pass