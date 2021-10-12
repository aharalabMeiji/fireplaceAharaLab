from enum import IntEnum
from fireplace import cards
from hearthstone.enums import Zone,State,CardType
from .game import Game
from .card import Hero,HeroPower,Minion,Spell,Weapon,Enchantment
from .player import Player

class DeepCopyOption(IntEnum):
	FREE=0# full deepcopy
	GAMEPLAY=1# stealth the enemy's data

def DeepCopyGame(game, player, option):
	player1 = DeepCopyPlayer(game.player1, 0)##  
	player2 = DeepCopyPlayer(game.player2, 0)
	new_game = Game(players=(game.player1, game.player2))
	new_game.manager.start_game()
	player1.game = player2.game = new_game
	CopyPlayerAttr(game.player1, player1)
	CopyPlayerAttr(game.player2, player2)
	CopyGameAttr(game, new_game)
	if player.name == game.player1.name:
		new_game.current_player = new_game.player1
		new_game.manager.turn(new_game.player1)
	else:
		new_game.current_player = new_game.player2
		new_game.manager.turn(new_game.player2)
	pass

def CreateVacantCard(card):
	if card.type==CardType.MINION:
		return Minion(cards.db[card.id])
	if card.type==CardType.SPELL:
		return Spell(cards.db[card.id])
	if card.type==CardType.WEAPON:
		return Weapon(cards.db[card.id])
	if card.type==CardType.ENCHANTMENT:
		return Enchantment(cards.db[card.id])

def DeepCopyPlayer(player, option):
	new_hero = Hero(cards.db[player.hero.id])# vacant hero
	new_deck = []
	for card in player.deck:
		new_deck.append(CreateVacantCard(card))
	new_player = Player(player.name, new_deck, new_hero)
	return new_player

def CopyPlayerAttr(oldX, newY):
	newY.starting_hero.controller=newY
	newY.starting_hero.zone = Zone.PLAY
	if not newY.hero.power:
		card=HeroPower(cards.db[oldX.hero.power.id])
		card.controller = newY
		card.zone = Zone.PLAY
	attrs=['activations_this_turn','additional_activations','aura','cant_be_frozen',\
		'cant_play','cast_on_friendly_characters','cost','heropower_damage',\
		'lifesteal','morphed','old_power','overload','play_counter',\
		'requirements','reborn','target','windfury',
		]
	for attr in attrs:
		value = getattr(oldX.hero.power,attr)
		setattr(newY.hero.power,attr, value)
	for buff in oldX.hero.power.buffs:
		newY.hero.power.buffs.append(Enchantment(cards.db[buff.id]))
	#events
	#play_targets
	#targets
	for card in newY.starting_deck:
		card.controller=newY
		card.zone = Zone.DECK
	for card in oldX.hand:
		new_card = CreateVacantCard(card)
		new_card.controller=newY
		for buff in card.buffs:
			new_card.buffs.append(Enchantment(cards.db[buff.id]))
		new_card.zone = Zone.HAND
	for card in oldX.field:
		new_char = Minion(cards.db[card.id])
		new_char.controller = newY
		for buff in card.buffs:
			new_char.buffs.append(Enchantment(cards.db[buff.id]))
		new_char.damage = card.damage	
		new_char.zone = Zone.PLAY
	for card in oldX.secrets:
		new_card = CreateVacantCard(card)
		new_card.controller=newY
		new_card.zone = Zone.SECRET
	for card in oldX.graveyard:
		new_card = CreateVacantCard(card)
		new_card.controller = newY
		new_card.zone=Zone.GRAVEYARD
	pass

def CopyGameAttr(oldX,newY):
	newY.state = State.RUNNING
	newY.step = oldX.step#Step.MAIN_ACTION
	#newY.zone = Zone.PLAY
	newY.players[0].opponent = newY.players[1]
	newY.players[1].opponent = newY.players[0]
	for player in newY.players:
		player.zone = Zone.PLAY
		newY.manager.new_entity(player)#################
	newY.players[0].first_player = oldX.players[0].first_player
	newY.players[1].first_player = oldX.players[1].first_player
	if newY.players[0].first_player:
		newY.player1 = newY.players[0]
		newY.player2 = newY.players[1]
	else:
		newY.player1 = newY.players[1]
		newY.player2 = newY.players[0]
	pass