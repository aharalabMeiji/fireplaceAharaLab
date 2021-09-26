from enum import IntEnum
from fireplace import cards
from hearthstone.enums import Zone,State,CardType
from .game import Game

class DeepCopyOption(IntEnum):
	FREE=0# full deepcopy
	GAMEPLAY=1# stealth the enemy's data

def DeepCopyGame(game, player, option):
	player1 = DeepCopyPlayer(game.player1, 0)## includeing deck, hero, 
	player2 = DeepCopyPlayer(game.player2, 0)
	new_game = Game(players=(game.player1, game.player2))
	if player.name == game.player1.name:
		new_game.current_player = new_game.players[0]
	else:
		new_game.current_player = new_game.players[1]
	#setup
	new_game.state = State.RUNNING
	new_game.step = game.step#Step.MAIN_ACTION
	#new_game.zone = Zone.PLAY
	new_game.players[0].opponent = new_game.players[1]
	new_game.players[1].opponent = new_game.players[0]
	for player in new_game.players:
		new_game.zone = Zone.PLAY
		new_game.manager.new_entity(player)#################

	if game.player1==game.player[0]:
		new_game.player1 = new_game.player[0]
		new_game.player1.first_player = True
		new_game.player2 = new_game.player[1]
		new_game.player2.first_player = False
	else:
		new_game.player1 = new_game.player[1]
		new_game.player1.first_player = True
		new_game.player2 = new_game.player[0]
		new_game.player2.first_player = False
	for player in self.players:
	#	player.prepare_for_game()
		#self.summon(self.starting_hero)
		player.hero = DeepCopyHero(game.hero, 0)
		hero.zone = Zone.PLAY
		#for id in self.starting_deck:
		#	self.card(id, zone=Zone.DECK)
		#self.shuffle_deck()
		#self.cthun = self.card("OG_280")
		#self.playstate = PlayState.PLAYING
		#self.setup_piece_of_cthun()

		# Draw initial hand (but not any more than what we have in the deck)
		#hand_size = min(len(self.deck), self.start_hand_size)
		#starting_hand = random.sample(self.deck, hand_size)
		# It's faster to move cards directly to the hand instead of drawing
		#for card in starting_hand:
		#	card.zone = Zone.HAND
	#self.manager.start_game()
	pass


def DeepCopyWeapon(weapon,option):
	if weapon:
		card=Weapon(cards.db[weapon.id])
		card.damage=0
		return card
	pass

def DeepCopyHeroPower(power,option):
	if power:
		card=HeroPower(cards.db[power.id])
		card.health=power.health
		card.health=power.health
		card.activations_this_turn = 0
		card.old_power = None
		return card
	pass

from .card import *
import random

def CreateVacantCard(card):
	if card.type==CardType.MINION:
		return Minion(cards.db[cardID])
	if card.type==CardType.SPELL:
		return Spell(cards.db[cardID])
	if card.type==CardType.WEAPON:
		return Weapon(cards.db[cardID])
	if card.type==CardType.ENCHANTMENT:
		return Enchantment(cards.db[cardID])

def DeepCopyDeck(cardList):
	deck = []
	for card in cardList:
		deck.append(CreateVacantCard(card))
	return random.shuffle(deck)

def DeepCopyPlayer(player, option):
	new_hero = Hero(cards.db[player.hero.id])# vacant hero
	new_deck = DeepCopyDeck(player.deck)
	new_player = Player(player.name, new_deck, new_hero)
	return new_player