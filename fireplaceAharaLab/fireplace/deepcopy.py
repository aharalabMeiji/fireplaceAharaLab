from enum import IntEnum
from fireplace import cards
from hearthstone.enums import Zone,State,CardType
from .card import Hero,HeroPower,Minion,Spell,Weapon,Enchantment,Sidequest
from .player import Player
from .game import Game
import copy
import random

class DeepCopyOption(IntEnum):
	FREE=0# full deepcopy
	GAMEPLAY=1# stealth the enemy's data
	pass

def debug_card(oldCard, newCard):
	print("--------debug--",newCard)
	attrList = oldCard.__dict__.keys()
	for attr in attrList:
		print("[%s]"%(attr),end="")
		if hasattr(newCard, attr):
			if getattr(newCard, attr) != getattr(oldCard, attr):
				print ("%s: %s != %s"%(attr,getattr(newCard, attr), getattr(oldCard, attr)))
		else:
			print ("no attribute : %s = %s"%(attr, getattr(oldCard, attr)))
	print("--------debug--%s-----------"%(oldCard.controller))
	pass

def deepcopy_game(game, player, option):
	#print("================deepcopy starts================")
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
	if oldGame.current_player==oldPlayer1:
		newGame.current_player = newPlayer1
	else:
		newGame.current_player = newPlayer2
	#debug_card(oldPlayer1.hero, newPlayer1.hero)
	#debug_card(oldPlayer2, newPlayer2)
	copy_gameattr(game, newGame)
	#debug_card(oldGame, newGame)
	#for i in range(len(newPlayer1.hand)):
	#	newCard = newPlayer1.hand[i]
	#	oldCard = oldPlayer1.hand[i]
	#	debug_card(oldCard, newCard)
	if option==1:
		itsme = newGame.current_player
		itshim = itsme.opponent
		random.shuffle(itsme.deck)
		for card in itshim.hand:
			if random.choice([True, False]):
				alt_card = random.choice(itshim.deck)
				card.zone=Zone.DECK
				alt_card.zone=Zone.HAND
			pass
		pass
		random.shuffle(itshim.deck)
		random.shuffle(itshim.hand)
	#print("================deepcopy ends================")
	return newGame

def create_vacant_card(card):
	if card.type==CardType.MINION:
		return Minion(cards.db[card.id])
	if card.type==CardType.SPELL:
		if hasattr(card.data,'sidequest') and card.data.sidequest or hasattr(card.data,'questline') and card.data.questline:
			return Sidequest(cards.db[card.id])
		else:
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

def copy_cardattr(oldCard, newCard):
	attrList = oldCard.__dict__.keys()
	excludeList=[
		'manager','target','choose_cards','data','tags','uuid','_events','buffs','id','controller','parent_card','aura','entity_id','_zone','game',
		]
	for attr in attrList:
		if not attr in excludeList:
			src = getattr(oldCard, attr)
			if not isinstance(src,list):
				setattr(newCard, attr, src)
			else:
				setattr(newCard, attr, copy.deepcopy(src))
			pass
		pass

	pass

def copy_playerattr(oldPlayer, newPlayer):
	new_hero = newPlayer.starting_hero
	new_hero.controller=newPlayer
	excludeHeroAttrs = [
		'attack_targets', 'attackable', 'attacking','card_class', 'classes','type','entity_id',
		'controller', 'data', 'entities', 'game', 'health','id','power','race','target','rarity','manager',
		'play_counter','tags','uuid','requirements',
		]
	for attr in oldPlayer.hero.__dict__.keys():
		if not attr in excludeHeroAttrs:
			value = getattr(oldPlayer.hero, attr)
			if not isinstance(value,list):
				setattr(new_hero, attr, value)
			else:
				setattr(new_hero, attr, copy.deepcopy(value))
			pass
		pass
	new_hero.zone = Zone.PLAY
	new_hero.game.manager.new_entity(new_hero)
	src = getattr(oldPlayer.hero, 'turns_in_play')
	setattr(new_hero, 'turns_in_play', src)
	src = getattr(oldPlayer.hero, 'play_counter')
	setattr(new_hero, 'play_counter', src)
	if not newPlayer.hero.power:
		card=HeroPower(cards.db[oldPlayer.hero.power.id])
		card.controller = newPlayer
		card.zone = Zone.PLAY
		card.game.manager.new_entity(card)
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
				'first_player','mulligan_state','turn_start',
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
				if src == []:
					setattr(newPlayer, attr, [])
				elif not isinstance(src[0], list):
					new_src = []
					for elm in src:
						new_src.append(elm)
					setattr(newPlayer, attr, new_src)
				else:
					new_src = []
					for elm in src:
						new_src_sub = []
						for elm_sub in elm:
							new_src_sub.append(elm_sub)
						new_src.append(new_src_sub)
					setattr(newPlayer, attr, new_src)
					#setattr(newPlayer, attr, copy.deepcopy(src))
				pass
			pass
		pass
	for card in oldPlayer.deck:
		new_card = create_vacant_card(card)
		new_card.controller=newPlayer
		copy_cardattr(card,new_card)
		new_card.zone = Zone.DECK
		new_card.game.manager.new_entity(new_card)
	for card in oldPlayer.hand:
		new_card = create_vacant_card(card)
		new_card.controller=newPlayer
		copy_cardattr(card,new_card)
		for buff in card.buffs:
			new_buff = Enchantment(cards.db[buff.id])
			new_buff.source = buff.source
			new_buff.controller = newPlayer
			new_buff.owner = card
			new_buff.apply(new_card)
			new_card.buffs.append(new_buff)
		new_card.zone = Zone.HAND
		new_card.game.manager.new_entity(new_card)
	for card in oldPlayer.field:
		new_card = Minion(cards.db[card.id])
		new_card.controller = newPlayer
		copy_cardattr(card, new_card)
		for buff in card.buffs:
			new_buff = Enchantment(cards.db[buff.id])
			new_buff.source = buff.source
			new_buff.controller = newPlayer
			new_buff.owner = card
			new_buff.apply(new_card)
			new_card.buffs.append(new_buff)
		new_card._summon_index = len(newPlayer.field)
		new_card.zone = Zone.PLAY
		new_card.game.manager.new_entity(new_card)
	for card in oldPlayer.secrets:
		new_card = create_vacant_card(card)
		new_card.controller=newPlayer
		new_card.zone = Zone.SECRET
		copy_cardattr(card,new_card)
		new_card.game.manager.new_entity(new_card)
	for card in oldPlayer.graveyard:
		new_card = create_vacant_card(card)
		if new_card != None:
			new_card.controller = newPlayer
			new_card.zone=Zone.GRAVEYARD
			copy_cardattr(card,new_card)
			new_card.game.manager.new_entity(new_card)
	for card in oldPlayer.game.setaside:
		if card.controller == oldPlayer:
			new_card = create_vacant_card(card)
			new_card.controller = newPlayer
			new_card.zone = Zone.SETASIDE
			copy_cardattr(card, new_card)
			new_card.game.manager.new_entity(new_card)
		pass
	pass

def copy_gameattr(oldGame,newGame):
	gameAttrs =['next_step','turn','tick','zone','state','step',
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