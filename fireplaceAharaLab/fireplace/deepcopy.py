from enum import IntEnum
from fireplace import cards
from hearthstone.enums import Zone,State,CardType
from .card import Hero,HeroPower,Minion,Spell,Weapon,Enchantment
from .player import Player
from .game import Game
import copy

class DeepCopyOption(IntEnum):
	FREE=0# full deepcopy
	GAMEPLAY=1# stealth the enemy's data

def deepcopy_game(game, player, option):
	oldGame = game
	oldPlayer1 = game.player1
	oldPlayer2 = game.player2
	newPlayer1 = deep_copy_player(oldPlayer1, 0)##
	newPlayer2 = deep_copy_player(oldPlayer2, 0)
	newGame = Game(players=(newPlayer1, newPlayer2))
	newGame.manager.start_game()
	newPlayer1.game = newPlayer2.game = newGame
	newPlayer1.opponent = newPlayer2
	newPlayer2.opponent = newPlayer1
	copy_playerattr(oldPlayer1, newPlayer1)
	copy_playerattr(oldPlayer2, newPlayer2)
	print("--------debug--player1-----------")
	attrList = oldPlayer1.__dict__.keys()
	for attr in attrList:
		if hasattr(newPlayer1, attr):
			if getattr(newPlayer1, attr) != getattr(oldPlayer1, attr):
				print ("%s: %s != %s"%(attr,getattr(newPlayer1, attr), getattr(oldPlayer1, attr)))
		else:
			print ("no attribute : %s"%(attr))
	print("--------debug--player1-----------")
	print("--------debug--player2-----------")
	attrList = oldPlayer2.__dict__.keys()
	for attr in attrList:
		if hasattr(newPlayer2, attr):
			if getattr(newPlayer2, attr) != getattr(oldPlayer2, attr):
				print ("%s: %s != %s"%(attr,getattr(newPlayer2, attr), getattr(oldPlayer2, attr)))
		else:
			print ("no attribute : %s"%(attr))
	print("--------debug--player1-----------")
	copy_gameattr(game, newGame)
	#if player.name == newPlayer1.name:
	#	newGame.current_player = newPlayer1
	#	newGame.manager.turn(newPlayer1)
	#else:
	#	newGame.current_player = newPlayer2
	#	newGame.manager.turn(newPlayer2)
	print("--------debug--game-----------")
	attrList = oldGame.__dict__.keys()
	for attr in attrList:
		if hasattr(newGame, attr):
			if getattr(newGame, attr) != getattr(oldGame, attr):
				print ("%s: %s != %s"%(attr,getattr(newGame, attr), getattr(oldGame, attr)))
		else:
			print ("no attribute : %s"%(attr))
	print("--------debug--game-----------")
	pass

def create_vacant_card(card):
	if card.type==CardType.MINION:
		return Minion(cards.db[card.id])
	if card.type==CardType.SPELL:
		return Spell(cards.db[card.id])
	if card.type==CardType.WEAPON:
		return Weapon(cards.db[card.id])
	if card.type==CardType.ENCHANTMENT:
		return Enchantment(cards.db[card.id])

def deep_copy_player(player, option):
	new_hero = Hero(cards.db[player.hero.id])# vacant hero
	new_starting_deck = []
	for cardID in player.starting_deck:
		new_starting_deck.append(cardID)
	new_player = Player(player.name+'x', new_starting_deck, new_hero)
	return new_player

def copy_playerattr(oldPlayer, newPlayer):
	newPlayer.starting_hero.controller=newPlayer
	newPlayer.starting_hero.zone = Zone.PLAY
	if not newPlayer.hero.power:
		card=HeroPower(cards.db[oldPlayer.hero.power.id])
		card.controller = newPlayer
		card.zone = Zone.PLAY
	# heropower's attr
	heropowerAttrs=['activations_this_turn','additional_activations','aura','cant_be_frozen',\
		'cant_play','cast_on_friendly_characters','cost','heropower_damage',\
		'lifesteal','morphed','old_power','overload','play_counter',\
		'requirements','reborn','target','windfury',
		]
	for attr in heropowerAttrs:
		value = getattr(oldPlayer.hero.power,attr)
		setattr(newPlayer.hero.power,attr, value)
	for buff in oldPlayer.hero.power.buffs:
		newPlayer.hero.power.buffs.append(Enchantment(cards.db[buff.id]))
	#events
	#play_targets
	#targets
	# player's attr 
	playerAttrs = ['cards_drawn_this_turn','_max_mana','playstate','zone',
				'entity_id','first_player','mulligan_state','turn_start',
				'minions_played_this_turn','combo','cards_played_this_turn',
				'spell_and_damage','guardians_legacy','spellpower_option',
				'choiceStrategy','lost_in_the_park','zone',
				'piece_of_cthun','_death_log','_play_log','_damage_log',
				'_activate_log','_summon_log','_reveal_log','carry_cards',
				'last_card_played','used_mana','times_spell_played_this_game',
				'times_spells_played_this_turn','spells_played_this_turn',
				'times_hero_power_used_this_game','times_card_to_play_out_of_deck',]
	for attr in playerAttrs:
		if hasattr(oldPlayer,attr):
			src = getattr(oldPlayer, attr)
			if not isinstance(src,list):
				setattr(newPlayer, attr, src)
			else:
				setattr(newPlayer, attr, copy.deepcopy(src))
			pass
		pass
	for deckcard in oldPlayer.deck:
		card = create_vacant_card(deckcard)
		card.controller=newPlayer
		card.zone = Zone.DECK
	for card in oldPlayer.hand:
		new_card = create_vacant_card(card)
		new_card.controller=newPlayer
		for buff in card.buffs:
			new_card.buffs.append(Enchantment(cards.db[buff.id]))
		new_card.zone = Zone.HAND
	for card in oldPlayer.field:
		new_char = Minion(cards.db[card.id])
		new_char.controller = newPlayer
		for buff in card.buffs:
			new_char.buffs.append(Enchantment(cards.db[buff.id]))
		new_char.damage = card.damage	
		new_char.zone = Zone.PLAY
	for card in oldPlayer.secrets:
		new_card = create_vacant_card(card)
		new_card.controller=newPlayer
		new_card.zone = Zone.SECRET
	for card in oldPlayer.graveyard:
		new_card = create_vacant_card(card)
		new_card.controller = newPlayer
		new_card.zone=Zone.GRAVEYARD
	pass

def copy_gameattr(oldGame,newGame):
	gameAttrs =['next_step','turn','current_player','tick','zone','state','step',
			 'setaside','_myLog_','active_aura_buffs','proposed_attacker','proposed_defender',
		]
	for attr in gameAttrs:
		if hasattr(oldGame,attr):
			src = getattr(oldGame, attr)
			if not isinstance(src,list):
				setattr(newGame, attr, src)
			else:
				setattr(newGame, attr, copy.deepcopy(src))
			pass
		pass
	for player in newGame.players:
		newGame.manager.new_entity(player)#################
	if newGame.players[0].first_player:
		newGame.player1 = newGame.players[0]
		newGame.player2 = newGame.players[1]
	else:
		newGame.player1 = newGame.players[1]
		newGame.player2 = newGame.players[0]
	pass