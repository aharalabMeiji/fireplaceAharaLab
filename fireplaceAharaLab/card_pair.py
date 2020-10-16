from hearthstone.enums import CardClass,CardType,PlayState, Zone,State
from fireplace.utils import random_draft
import random
from agent_Standard import StandardRandom,StandardStep1
from fireplace.game import Game
from fireplace.player import Player
import copy
from fireplace.exceptions import GameOver
from utils import Agent

def investigate_card_pair( onlyresult=0):
	card_class = CardClass.HUNTER
	allCards=get_all_cards(card_class)
	vanillas = get_all_vanillas(allCards)
	nonVanillas = get_all_non_vanillas(allCards)

	count1=0
	count2=0

	#ヒーローパワーを消す、というのもよいかも。
	#良いカードペアを漠然と探す旅に出る？
	nonvanilla1 = 'EX1_045'#random.choice(nonVanillas).id#自分で指定してもよい
	nonvanilla2 = 'EX1_332'#random.choice(nonVanillas).id#
	#古代の番人：EX1_045:攻撃できない。
	#沈黙:EX1_332:ミニオン1体を沈黙させる

	print(" specific cards : %r%r"%(nonvanilla1, nonvanilla2))
	for repeat in range(50):
		print("    GAME %d"%repeat,end="  -> ")
		#set decks and players
		deck1=[]
		position=random.randint(1,7)
		for i in range(position):
			deck1.append((random.choice(vanillas)).id)
		deck1.append(nonvanilla1)
		deck1.append(nonvanilla2)
		for i in range(8-position):#デッキは10枚
			deck1.append(random.choice(vanillas).id)
		player1 = Player("AAAA", deck1, card_class.default_hero)
		deck2 = copy.deepcopy(deck1)
		random.shuffle(deck2)
		player2 = Player("BBBB", deck2, card_class.default_hero)
		#set a game
		game = Game(players=(player1, player2))
		game.start()

		for player in game.players:
			#print("Can mulligan %r" % (player.choice.cards))
			mull_count = random.randint(0, len(player.choice.cards))
			cards_to_mulligan = random.sample(player.choice.cards, mull_count)
			player.choice.choose(*cards_to_mulligan)
		game.player1.hero.max_health=10# ヒーローのHPは10
		game.player2.hero.max_health=10

		turnNumber=0
		print("Turn ",end=':')
		while True:
			turnNumber+=1
			print(turnNumber,end=":")
			weight=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
			weight[0]=weight[1]=5
			weight[26]=10
			weight[2]=weight[3]=weight[6]=weight[7]=5
			weight[10]=weight[11]=weight[12]=weight[13]=5
			StandardStep1(game, debugLog=False)
			#StandardRandom(game,debugLog=True)
			#ここはもう少し賢い人にやってほしい
			if game.state!=State.COMPLETE:
				try:
					game.end_turn()
				except GameOver:#まれにおこる
					pass
			else:
				if game.current_player.playstate == PlayState.WON:
					winner = game.current_player.name
					break
				elif game.current_player.playstate == PlayState.LOST:
					winner = game.current_player.opponent.name
					break
				else:
					winner = "DRAW"
					break
		print("%s won."%winner)
		if winner=="AAAA":
			count1 += 1
		elif winner=="BBBB":
			count2 += 1
	print("%d : %d"%(count1, count2))

def find_card_pair(onlyresult=1):
	card_class = CardClass.MAGE#カードクラスを設定することは必須
	allCards=get_all_cards(card_class,costMax=2)
	vanillas = get_all_vanillas(allCards)
	nonVanillas = get_all_non_vanillas(allCards)
	spells = get_all_spells(allCards)

	#良いカードペアを漠然と探す旅に出る2枚は呪文カードしばり
	for matchNumber in range(10):
		count1=0
		count2=0

		#ヒーローパワーを消す、というのもよいかも。
		nonvanillaName1 = random.choice(nonVanillas)
		nonvanilla1=nonvanillaName1.id
		nonvanillaName2 = random.choice(spells)#この呪文によって、まえのカードが活かされるかどうか
		nonvanilla2=nonvanillaName2.id

		print(" specific cards : %r%r"%(nonvanillaName1, nonvanillaName2))
		for repeat in range(25):
			if onlyresult==0:
				print("    GAME %d"%repeat,end="  -> ")
			#set decks and players
			deck1=[]
			position=random.randint(1,7)
			for i in range(position):
				deck1.append((random.choice(vanillas)).id)
			deck1.append(nonvanilla1)
			deck1.append(nonvanilla2)
			for i in range(8-position):#デッキは10枚
				deck1.append(random.choice(vanillas).id)
			player1 = Player("Player1", deck1, card_class.default_hero)
			deck2 = copy.deepcopy(deck1)
			random.shuffle(deck2)
			player2 = Player("Player2", deck2, card_class.default_hero)
			#set a game
			game = Game(players=(player1, player2))
			game.start()
				
			for player in game.players:
				#print("Can mulligan %r" % (player.choice.cards))
				mull_count = random.randint(0, len(player.choice.cards))
				cards_to_mulligan = random.sample(player.choice.cards, mull_count)
				player.choice.choose(*cards_to_mulligan)
			game.player1.hero.max_health=10
			game.player2.hero.max_health=10
			turnNumber=0
			if onlyresult==0:
				print("Turn ",end=':')
			while True:
				turnNumber+=1
				if onlyresult==0:
					print(turnNumber,end=":")
				#StandardRandom(game)#ここはもう少し賢くする
				weight=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
				weight[0]=weight[1]=5
				weight[26]=10
				weight[2]=weight[3]=weight[6]=weight[7]=5
				weight[10]=weight[11]=weight[12]=weight[13]=5
				StandardStep1(game, debugLog=False)
				if game.state!=State.COMPLETE:
					try:
						game.end_turn()
					except GameOver:#まれにおこる
						pass
				if game.state==State.COMPLETE:
					if game.current_player.playstate == PlayState.WON:
						winner = game.current_player.name
						break
					elif game.current_player.playstate == PlayState.LOST:
						winner = game.current_player.opponent.name
						break
					else:
						winner = "DRAW"
					break
			if onlyresult==0:
				print("%s won."%winner)
			if winner=="Player1":
				if onlyresult==1:
					print("O",end=".")
				count1 += 1
			elif winner=="Player2":
				if onlyresult==1:
					print("X",end=".")
				count2 += 1
		print("(%d : %d)"%(count1, count2),end=" ")#25戦で10点差があれば有意な差あり
		if count1-count2>=10:
			print("Significant")
		else:
			print("")
	pass
def get_all_cards(card_class: CardClass,costMax=2):
	from fireplace import cards
	collection = []
	for card in cards.db.keys():
		cls = cards.db[card]
		if not cls.collectible:
			continue
		if cls.type == CardType.HERO:			# Heroes are collectible...
			continue
		if cls.card_class and cls.card_class not in [card_class, CardClass.NEUTRAL]:# Play with more possibilities
			continue
		if cls.cost<=costMax:
			collection.append(cls)
	return collection

def get_all_vanillas(allCards):
    vanillas=[]
    for card in allCards:
        if len(card.description)<3:# vanilla condition
            vanillas.append(card)
    return vanillas
def get_all_non_vanillas(allCards):
    vanillas=[]
    for card in allCards:
        if len(card.description)>=3:# non-vanilla condition
            vanillas.append(card)
    return vanillas
def get_all_spells(allCards):
	spells=[]
	for card in allCards:
		if card.type == CardType.SPELL:# non-vanilla condition
			spells.append(card)
	return spells
