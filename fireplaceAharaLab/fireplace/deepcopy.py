from enum import IntEnum
from fireplace import cards
from hearthstone.enums import GameTag, Zone,State,CardType,Step
from .card import Hero,HeroPower,Minion,Spell,Weapon,Enchantment,Sidequest,Secret,Location,QuestReward
from .player import Player, PlayLog
from .game import Game
from .aura import AuraBuff
import copy
import random
from .logging import log
from .exceptions import InvalidAction
from .config import Config

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
	""" deepcopy a game state. 
	"""
	if Config.DEEPCOPY_LOGINFO:
		print("================deepcopy starts================")
	oldGame = game
	oldPlayer1 = game.player1
	oldPlayer2 = game.player2
	## create new players
	try:
		newPlayer1 = deep_copy_player(oldPlayer1, 0)##
		newPlayer2 = deep_copy_player(oldPlayer2, 0)
	except RuntimeError as e:
		print (e)
	## create a new game
	newGame = Game(players=(newPlayer1, newPlayer2))
	newGame.manager.start_game()
	newPlayer1.game = newPlayer2.game = newGame
	newPlayer1.opponent = newPlayer2
	newPlayer2.opponent = newPlayer1
	if oldGame.current_player==oldPlayer1:
		newGame.current_player = newPlayer1
	else:
		newGame.current_player = newPlayer2
	## player's attributes
	copy_playerattr(oldPlayer1, newPlayer1)
	copy_playerattr(oldPlayer2, newPlayer2)
	## game's attributes
	copy_gameattr(game, newGame)
	## option
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
	if Config.DEEPCOPY_LOGINFO:
		print("================deepcopy ends================")
	return newGame

def deep_copy_player(player, option):
	"""
	create a new player with his deck and his hero
	"""
	new_hero = Hero(cards.db[player.hero.id])# vacant hero
	new_starting_deck = []
	for cardID in player.starting_deck:
		new_starting_deck.append(cardID)
	new_player = Player(player.name+'x', new_starting_deck, new_hero)
	return new_player

def create_vacant_card(card):
	if card.type==CardType.MINION:
		return Minion(cards.db[card.id])
	if card.type==CardType.SPELL:
		if hasattr(card.data,'sidequest') and card.data.sidequest:
			return Sidequest(cards.db[card.id])
		elif hasattr(card.data,'questline') and card.data.questline:
			return Sidequest(cards.db[card.id])
		elif hasattr(card.data,'quest') and card.data.quest:
			return Sidequest(cards.db[card.id])
		elif hasattr(card.data,'secret') and card.data.secret:
			return Secret(cards.db[card.id])
		else:
			return Spell(cards.db[card.id])
	if card.type==CardType.WEAPON:
		return Weapon(cards.db[card.id])
	if card.type==CardType.ENCHANTMENT:
		return Enchantment(cards.db[card.id])
	if card.type==CardType.HERO:
		return Hero(cards.db[card.id])
	if card.type==CardType.HERO_POWER:
		return HeroPower(cards.db[card.id])
	if card.type==CardType.LOCATION: ##QuestReward
		return Location(cards.db[card.id])
	if card.type==40: ##QuestReward
		return QuestReward(cards.db[card.id])
	raise InvalidAction("This card is not supported in deepcopy: %s" % card)

def deepcopy_aurabuff(oldCard):
	ret=[]
	for card in oldCard:
		if isinstance(card,AuraBuff):
			buff=AuraBuff(card.source, card.entity)
		else:
			#print ("Consider how to avoid this trouble!!")
			buff=copy.deepcopy(card)
		buff.tick = card.source.controller.game.tick
		ret.append(buff)
	return ret

def deepcopy_slots(oldCard, newCard):
	for card in oldCard.slots:
		if isinstance(card,AuraBuff):
			buff=AuraBuff(card.source, card.entity)
		else:
			#print ("Consider how to avoid this trouble!!")
			buff=copy.deepcopy(card)
		buff.tick = card.source.controller.game.tick
		newCard.slots.append(buff)
	return ret


def deepcopy_enchantment(oldCards, oldCard, newCard):
	"""
	@oldCards: for example, buffs of oldCard
	"""
	ret=[]
	for card in oldCards:
		Ncard = Enchantment(cards.db[card.id])
		Ncard.source = newCard
		Ncard.controller = newCard.controller
		Ncard.owner = newCard
		newCard.game.manager.new_entity(Ncard)## insert entity_id
		ret.append(Ncard)
	return ret

def deepcopy_minion(oldCards, oldCard, newCard):
	"""
	oldCards: for example, choose_cards of oldCard
	"""
	ret=[]
	for card in oldCards:
		Ncard = Minion(cards.db[card.id])
		Ncard.controller = newCard.controller
		newCard.game.manager.new_entity(Ncard)
		ret.append(Ncard)
	return ret

def deepcopy_spell(oldCards, oldCard, newCard):
	"""
	oldCards: for example, choose-one cards of oldCard
	"""
	ret=[]
	for card in oldCards:
		is_sidequest=(hasattr(card.data,'sidequest') and card.data.sidequest)
		is_questline=(hasattr(card.data,'questline') and card.data.questline)
		if is_sidequest or is_questline:
			Ncard = Sidequest(cards.db[card.id])
		else:
			Ncard = Spell(cards.db[card.id])
		Ncard.controller = newCard.controller
		newCard.game.manager.new_entity(Ncard)
		ret.append(Ncard)
	return ret

def deepcopy_reward(oldCards, oldCard, newCard):
	"""
	oldCards: 
	"""
	ret=[]
	for card in oldCards:
		is_reward=(card.type==CardType.BATTLEGROUND_QUEST_REWARD)
		assert is_reward, ""
		Ncard = QuestReward(cards.db[card.id])
		Ncard.controller = newCard.controller
		newCard.game.manager.new_entity(Ncard)
		ret.append(Ncard)
	return ret


def deepcopy_log(oldLog):
	ret=[]
	for log in oldLog:
		ret.append(PlayLog(log.card, log.turn, log.amount))
	return ret

def deepcopy_HeroPower(oldHeroPower):
	## hero power
	ret=[]
	if oldHeroPower:
		newPlayer = oldHeroPower.controller
		card=HeroPower(cards.db[oldHeroPower.id])#
		card.controller = newPlayer
		## or Summon(newPlayer, card).trigger(newPlayer)
		card.game.manager.new_entity(card)
		# heropower's attr
		heropowerAttrs=['activations_this_turn','additional_activations','aura','cant_be_frozen',\
			'cant_play','cast_on_friendly_characters','cost','heropower_damage',\
			'lifesteal','morphed','old_power','overload','play_counter',\
			'requirements','reborn','sidequest_counter','script_data_num_1',\
			'sidequest_list0','target','windfury',
			]
		for attr in heropowerAttrs:
			value = getattr(oldHeroPower,attr)
			setattr(newPlayer.hero.power,attr, value)
		for buff in oldHeroPower.buffs:
			newPlayer.hero.power.buffs.append(Enchantment(cards.db[buff.id]))
			ret.append(card)
	return ret


def copy_cardattr(oldCard, newCard):
	""" copy attributes from and to existing cards
	"""
	attrList = oldCard.__dict__.keys()
	excludeList=[		
		'manager','target','data','tags','uuid','_events','buffs','id','controller','parent_card','aura','entity_id','_zone','game',
		]
	for attr in attrList:
		if not attr in excludeList:
			src = getattr(oldCard, attr)
			if not isinstance(src,list):
				setattr(newCard, attr, src)
			else:
				if src==[]:
					setattr(newCard, attr, [])
				else:
					newSrc=[]
					for card in src:
						if isinstance(card, AuraBuff):
							newSrc += deepcopy_aurabuff([card])
						elif isinstance(card, Enchantment):## 
							newSrc += deepcopy_enchantment([card], oldCard, newCard)
						elif isinstance(card, Minion):##choose one card
							newSrc += deepcopy_minion([card], oldCard, newCard)
						elif isinstance(card, Secret):##choose one card
							newSrc += deepcopy_spell([card], oldCard, newCard)
						elif isinstance(card, Sidequest):##choose one card
							newSrc += deepcopy_spell([card], oldCard, newCard)
						elif isinstance(card, Spell):##choose one card
							newSrc += deepcopy_spell([card], oldCard, newCard)
						elif isinstance(card, QuestReward):##
							newSrc += deepcopy_reward([card], oldCard, newCard)
						elif isinstance(card, PlayLog):
							newSrc += deepcopy_log([card])
						elif isinstance(card, HeroPower):
							newSrc += deepcopy_HeroPower(card)
						elif isinstance(card, str):##discover,entourage
							newSrc += [card]
						else:
							newSrc += [copy.deepcopy(card)]
					setattr(newCard, attr, newSrc)
			pass
		pass

	pass



def copy_playerattr(oldPlayer, newPlayer):
	## hero
	new_hero = newPlayer.starting_hero
	new_hero.controller=newPlayer
	## hero's attr
	excludeHeroAttrs = [
		'attack_targets', 'attackable', 'attacking','card_class', 'classes','type','entity_id',
		'controller', 'data', 'entities', 'game', 'health','id','power','race','target','rarity','manager',
		'play_counter','tags','uuid','requirements','slots'
		]
	for attr in oldPlayer.hero.__dict__.keys():
		if not attr in excludeHeroAttrs:
			value = getattr(oldPlayer.hero, attr)
			if not isinstance(value,list):
				setattr(new_hero, attr, value)
			elif value==[]:
				setattr(new_hero, attr, [])
			elif isinstance(value[0], Enchantment):## 
				setattr(new_hero, attr, deepcopy_enchantment(value, oldPlayer.hero, new_hero))
			elif isinstance(value[0], AuraBuff):## 
				setattr(new_hero, attr, deepcopy_aurabuff(value))
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
	## hero power
	if oldPlayer.hero.power:
		card=HeroPower(cards.db[oldPlayer.hero.power.id])#
		card.controller = newPlayer
		card.zone = Zone.PLAY
		card.deepcopy_original = oldPlayer.hero.power
		## or Summon(newPlayer, card).trigger(newPlayer)
		card.game.manager.new_entity(card)
		# heropower's attr
		heropowerAttrs=['activations_this_turn','additional_activations','aura','cant_be_frozen',\
			'cant_play','cast_on_friendly_characters','cost','heropower_damage',\
			'lifesteal','morphed','old_power','overload','play_counter',\
			'requirements','reborn','sidequest_counter','script_data_num_1',\
			'sidequest_list0','target','windfury',
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
	playerAttrs = ['cards_drawn_this_turn','_max_mana','max_mana','playstate','zone',
				'first_player','mulligan_state','turn_start',
				'minions_played_this_turn','combo','cards_played_this_turn',
				'spell_and_damage','spellpower_option',
				'choiceStrategy','lost_in_the_park','zone',
				'piece_of_cthun','_death_log','_play_log','_damage_log',
				'_activate_log','_summon_log','_reveal_log','carry_cards',
				'last_card_played','used_mana','total_used_mana_this_turn','overload_locked','temp_mana',
				'times_spell_played_this_game',
				'times_spells_played_this_turn','spells_played_this_turn',
				'times_hero_power_used_this_game','times_card_to_play_out_of_deck','tavern_tier',]
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
	# deck-cards attr.
	for card in oldPlayer.deck:
		new_card = create_vacant_card(card)
		new_card.controller=newPlayer
		copy_cardattr(card,new_card)
		new_card.deepcopy_original = card
		new_card.zone = Zone.DECK
		new_card.game.manager.new_entity(new_card)
	#hand-cards attr.
	for card in oldPlayer.hand:
		new_card = create_vacant_card(card)
		new_card.controller=newPlayer
		copy_cardattr(card,new_card)
		new_card.deepcopy_original = card
		new_card.zone = Zone.HAND
		new_card.game.manager.new_entity(new_card)
	#field-cards attr.
	for card in oldPlayer.field:
		new_card = Minion(cards.db[card.id])
		new_card.controller = newPlayer
		copy_cardattr(card, new_card)
		new_card.deepcopy_original = card
		#if len(card.game.active_aura_buffs)>0:
		#	new_card.game.refresh_auras()
		for buff in card.buffs:
			if buff not in card.game.active_aura_buffs:
				new_buff = Enchantment(cards.db[buff.id])
				new_buff.source = buff.source## it is an original card, but no otherway
				new_buff.controller = newPlayer
				new_buff.owner = new_card
				new_buff.entity = new_card
				new_buff.tags[GameTag.ATK]=buff.atk## modified buff
				new_buff.tags[GameTag.HEALTH]=buff.max_health## modified buff
				new_buff.apply(new_card)
			else:
				new_buff = Enchantment(cards.db[buff.id])
				new_buff.source = buff.source## it is an original card, but no otherway
				new_buff.controller = newPlayer
				new_buff.owner = new_card
				new_buff.entity = new_card
				new_buff.tags[GameTag.ATK]=buff.atk## modified buff
				new_buff.tags[GameTag.HEALTH]=buff.max_health## modified buff
				new_buff.apply(new_card)
				new_buff.tick = buff.tick+new_card.game.tick-card.game.tick
				new_card.game.active_aura_buffs.append(new_buff)
		new_card._summon_index = len(newPlayer.field)
		new_card.zone = Zone.PLAY
		new_card.game.manager.new_entity(new_card)
	#new_card.game.refresh_auras()
	## secret-cards attr.
	for card in oldPlayer.secrets:
		new_card = create_vacant_card(card)
		new_card.controller=newPlayer
		new_card.zone = Zone.SECRET
		copy_cardattr(card,new_card)
		new_card.deepcopy_original = card
		new_card.game.manager.new_entity(new_card)
	## quest-cards attr.
	for card in oldPlayer.quests:
		new_card = create_vacant_card(card)
		new_card.controller=newPlayer
		new_card.zone = Zone.SECRET
		copy_cardattr(card,new_card)
		new_card.deepcopy_original = card
		new_card.game.manager.new_entity(new_card)
	## reward-cards attr.
	for card in oldPlayer.rewards:
		new_card = create_vacant_card(card)
		new_card.controller=newPlayer
		new_card.zone = Zone.SECRET
		copy_cardattr(card,new_card)
		new_card.deepcopy_original = card
		new_card.game.manager.new_entity(new_card)
	## graveyard-cards attr.
	for card in oldPlayer.graveyard:
		new_card = create_vacant_card(card)
		if new_card != None:
			new_card.controller = newPlayer
			new_card.zone=Zone.GRAVEYARD
			new_card.deepcopy_original = card
			copy_cardattr(card,new_card)
			new_card.game.manager.new_entity(new_card)
	## setaside-cards attr.
	for card in oldPlayer.game.setaside:
		if card.controller == oldPlayer:
			new_card = create_vacant_card(card)
			new_card.controller = newPlayer
			new_card.zone = Zone.SETASIDE
			new_card.deepcopy_original = card
			copy_cardattr(card, new_card)
			new_card.game.manager.new_entity(new_card)
		pass
	pass

def copy_gameattr(oldGame,newGame):
	""" copy game's attr.
	"""
	gameAttrs =['next_step','turn','tick','zone','state','step',
			'proposed_attacker','proposed_defender',
		]
	## copying 'active_aura_buffs' will be done at appendin buffs
	for attr in gameAttrs:
		if hasattr(oldGame,attr):
			src = getattr(oldGame, attr)
			if not isinstance(src,list):
				setattr(newGame, attr, src)
			elif src==[]:
				setattr(newGame, attr, [])
			elif attr=='_myLog_':
				ret=[]
				for element in src:
					ret.append(copy.copy(element))
				setattr(newGame, attr, ret)
			else:
				ret=[]
				for element in src:
					if isinstance(element, AuraBuff):
						ret.append(deepcopy_aurabuff([element]))
					else:
						ret.append(copy.deepcopy(element))
				setattr(newGame, attr, ret)
			pass
		pass
	for player in newGame.players:
		newGame.manager.new_entity(player)####
	if newGame.players[0].first_player:
		newGame.player1 = newGame.players[0]
		newGame.player2 = newGame.players[1]
	else:
		newGame.player1 = newGame.players[1]
		newGame.player2 = newGame.players[0]
	pass