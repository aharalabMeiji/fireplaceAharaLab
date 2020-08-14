from hearthstone.enums import CardClass,CardType,PlayState, Zone,State
from fireplace.utils import random_draft
import random
from agent_Genzo import GenzoRandom,GenzoStep1
from fireplace.game import Game
from fireplace.player import Player
import copy
from fireplace.exceptions import GameOver
from Genzo import Genzo,GenzoWeight 

def start_card_pair_investigation( onlyresult=0):
	card_class = CardClass.HUNTER
	allCards=get_all_cards(card_class)
	vanillas = get_all_vanillas(allCards)
	nonVanillas = get_all_non_vanillas(allCards)

	count1=0
	count2=0

	#hearthstone_data/CardDefs.XML の 246910行の 30 -> 10にする必要がある。（ヒーローの初期HP変更)
	#ヒーローパワーを消す、というのもよいかも。
	#良いカードペアを漠然と探す旅に出る？
	nonvanilla1 = 'EX1_045'#random.choice(nonVanillas).id#自分で指定してもよい
	nonvanilla2 = 'EX1_332'#random.choice(nonVanillas).id#
	#古代の番人：EX1_045:攻撃できない。
	#沈黙:EX1_332:ミニオン1体を&lt;b&gt;沈黙&lt;/b&gt;させる

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
		turnNumber=0
		print("Turn ",end=':')
		while True:
			turnNumber+=1
			print(turnNumber,end=":")
			#if turnNumber==8:
				#print("(%d : %d)"%(game.player1.hero.health,game.player2.hero.health),end=" ")
			#GenzoRandom(game)#ここはもう少し賢くする
			GenzoStep1(game,GenzoWeight([5,5,1,1,1,0,0,0,0,-10,0,0,0,0,0,0,0,0,0,0]))#ここはもう少し賢くする
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
		if winner=="Player1":
			count1 += 1
		elif winner=="Player2":
			count2 += 1
	print("%d : %d"%(count1, count2))

def find_card_pair( onlyresult=0):
	card_class = CardClass.HUNTER
	allCards=get_all_cards(card_class)
	vanillas = get_all_vanillas(allCards)
	nonVanillas = get_all_non_vanillas(allCards)

	count1=0
	count2=0

	#hearthstone_data/CardDefs.XML の 246910行の 30 -> 10にする必要がある。（ヒーローの初期HP変更)
	#ヒーローパワーを消す、というのもよいかも。
	#良いカードペアを漠然と探す旅に出る？
	nonvanilla1 = 'EX1_045'#random.choice(nonVanillas).id#自分で指定してもよい
	nonvanilla2 = 'EX1_332'#random.choice(nonVanillas).id#
	#古代の番人：EX1_045:攻撃できない。
	#沈黙:EX1_332:ミニオン1体を&lt;b&gt;沈黙&lt;/b&gt;させる

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
		turnNumber=0
		print("Turn ",end=':')
		while True:
			turnNumber+=1
			print(turnNumber,end=":")
			#if turnNumber==8:
				#print("(%d : %d)"%(game.player1.hero.health,game.player2.hero.health),end=" ")
			#GenzoRandom(game)#ここはもう少し賢くする
			GenzoStep1(game,GenzoWeight([5,5,1,1,1,0,0,0,0,-10,0,0,0,0,0,0,0,0,0,0]))#ここはもう少し賢くする
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
		if winner=="Player1":
			count1 += 1
		elif winner=="Player2":
			count2 += 1
	print("%d : %d"%(count1, count2))

def get_all_cards(card_class: CardClass):
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
		if cls.cost<=1:
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
