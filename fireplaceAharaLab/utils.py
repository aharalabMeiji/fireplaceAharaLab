from hearthstone.enums import CardClass,BlockType, CardType ,PlayState, State
from enum import IntEnum
from fireplace.game import Game
from fireplace.card import Card
from fireplace.exceptions import GameOver
from fireplace.actions import *
from fireplace.utils import ActionType
import copy
import random
import time
from fireplace.config import Config

class Agent(object):
	""" エージェントのクラス
	エージェントを作るときはこのクラスを継承してください。"""
	def __init__(self, myName: str, myFunction, myOption: list, myClass: CardClass, rating ,E = 0, mulliganStrategy = None, choiceStrategy=None):
		self.name = myName
		self.func = myFunction
		self.option = myOption
		self.myClass = myClass
		self.rating = rating = 1500
		self.E = E 
		self.mulliganStrategy = mulliganStrategy
		self.choiceStrategy = choiceStrategy
		pass

	def __str__(self):
		return self.name

def begingame_events(player):
	deckCardId=[card.id for card in player.controller.deck]
	if 'REV_018' in deckCardId:
		player.hero.max_health=40
	elif 'RLK_214' in deckCardId:
		RLK_214_Begingame_Action().trigger(player)
	pass


def play_one_game(P1: Agent, P2: Agent, deck1=[], deck2=[], debugLog=True, HEROHPOPTION=30, P1MAXMANA=1, P2MAXMANA=1, P1HAND=3, P2HAND=3):
	""" エージェント同士で1回対戦する。
	実験的に、ヒーローの体力、初期マナ数、初期ハンド枚数をコントロールできます。
	play one game by P1 and P2 """
	from fireplace.utils import random_draft
	from fireplace.player import Player
	import random
	exclude = []# you may exclude some cards to construct a deck
	if Config.LOGINFO:
		print("New game settings")
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
	##
	begingame_events(player1)
	begingame_events(player2)
	##
	if Config.LOGINFO:
		print("New game start")
	for player in game.players:
		BeginGame(player).trigger(player)
		if debugLog:
			print("player = %s : hands"%(player))
			for card in player.hand:
				print("--- %r"%(card))
	print("=-=-=-=-=-=-=-=-")
	while True:	
		#game main loop
		player = game.current_player
		start_time = time.time()
		if player.name==P1.name:
			#please make each Agent.func has arguments 'self, game, option, gameLog, debugLog'
			P1.func(P1, game, option=P1.option, gameLog=game.get_log(), debugLog=debugLog)
		elif player.name==P2.name:
			#please make each Agent.func has arguments 'self, game, option, gameLog, debugLog'
			P2.func(P2, game, option=P2.option, gameLog=game.get_log(), debugLog=debugLog)
		#else:
		#	Original_random(game)#random player by fireplace
		#turn end procedure from here
		if player.choice!=None:
			player.choice=None#somotimes it comes here
		if game.state!=State.COMPLETE:
			try:
				if game.current_player.choice!=None:
					postAction(game.current_player)
				if debugLog:
					print(">>>>%s>>>>turn change %d[sec]>>>>%s"%(player, time.time()-start_time, player.opponent),end='  ')
					print("%d : %d"%(player1.hero.health+player1.hero.armor,player2.hero.health+player2.hero.armor))
				game.end_turn()
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

def play_set_of_games(P1: Agent, P2: Agent, deck1=[], deck2=[], gameNumber=15, debugLog=True, HEROHPOPTION=30, P1MAXMANA=1, P2MAXMANA=1, P1HAND=3, P2HAND=3):
	""" 決まった回数の試合を行い、勝敗数を表示する 
	"""
	if debugLog:
		print(" %r (%s) vs.  %r (%s)"%(P1.name, P1.myClass, P2.name, P2.myClass))
	Count1 = 0
	Count2 = 0
	for i in range(gameNumber):
		winner = play_one_game(P1,P2,deck1, deck2, debugLog=debugLog, HEROHPOPTION=HEROHPOPTION, P1MAXMANA=P1MAXMANA, P2MAXMANA=P2MAXMANA, P1HAND=P1HAND, P2HAND=P2HAND)
		if debugLog:
			print("winner is %r"%winner)
		if winner == P1.name:
			Count1+=1
		elif winner == P2.name:
			Count2+=1
	print(" %r (%s) wins: %d"%(P1.name, P1.myClass, Count1))
	print(" %r (%s) wins: %d"%(P2.name, P2.myClass, Count2))
	print(" Draw: %d"%(gameNumber-Count1-Count2))
	return Count1, Count2, (gameNumber-Count1-Count2)

class Candidate(object):
	""" アクションの候補手のクラス 
	"""
	def __init__(self, card, card2=None, type=BlockType.PLAY, target=None, turn=None):
		#super(myAction, self).__init__()
		self.turn=turn
		self.card = card
		self.card2 = card2
		self.type = type
		self.target = target
		self.score = 0
		self.notes = ''
		pass

	def __str__(self):
		if self.type==BlockType.ATTACK:
			atk1=self.card.atk
			health1=self.card.health
			if self.card.type==CardType.HERO:
				health1 += self.card.armor
			atk2=self.target.atk
			health2=self.target.health
			if self.target.type==CardType.HERO:
				health2 += self.target.armor
			return "{card}({atk1}/{health1}) -> attacks -> {target}({atk2}/{health2})".format(
				card=self.card, atk1=atk1, health1=health1, 
				target=self.target, atk2=atk2, health2=health2)
		elif self.type==ActionType.LOCATION:
			health1=self.card.health
			if self.card.type==CardType.HERO:
				health1 += self.card.armor
			atk2=self.target.atk
			health2=self.target.health
			if self.target.type==CardType.HERO:
				health2 += self.target.armor
			return "{card}(**/{health1}) -> attacks -> {target}({atk2}/{health2})".format(
				card=self.card, health1=health1, 
				target=self.target, atk2=atk2, health2=health2)
		elif self.type==ExceptionPlay.TURNEND:
			return "Turn end."
		elif self.type==BlockType.POWER:
			if self.target:
				atk2=self.target.atk
				health2=self.target.health
				if self.target.type==CardType.HERO:
					health2 += self.target.armor
				return "{card} -> heropower -> {target}({atk2}/{health2})".format(
					card=self.card, 
					target=self.target,atk2=atk2,health2=health2)
			else:
				return "{card} -> heropower".format(card=self.card)
		elif self.type==BlockType.PLAY:
			if self.target==None or self.type==ActionType.LOCATION:
				return "{card}({id}):{cost} -> plays".format(card=self.card, cost = self.card.cost,id=self.card.id)
			else :
				atk2=self.target.atk
				health2=self.target.health
				if self.target.type==CardType.HERO:
					health2 += self.target.armor
				return "{card}({id}):{cost} -> plays -> {target}({atk2}/{health2})".format(
					card=self.card, cost = self.card.cost,
					target=self.target, atk2=atk2, health2=health2,id=self.card.id)
		elif self.type==ActionType.TRADE:
			return "{card} -> trade".format(card=self.card)
		elif self.type==ActionType.LOCATION:
			if self.target==None:
				return "{card}({id}): location".format(card=self.card,id=self.card.id)
			else:
				return "{card}({id}): location -> {target}({atk2}/{health2})".format(
					card=self.card,id=self.card.id,
					target=self.target, atk2=atk2, health2=health2)
		return "{card}->{type}(target={target})".format(card=self.card,type=str(self.type),target=self.target)
		pass

	def __eq__(self,obj):
		return str(self)==str(obj)
		pass
	def clearScore(self):
		self.score = 0

class GameWithLog(Game):
	""" game with logs  """
	def __init__(self, players):
		super().__init__(players=players)
#
#  getCandidates
#
def getCandidates(mygame,_includeTurnEnd=False):
	""" アクションの候補をすべてリスト化して返す 
	_includeTurnEnd=False 「何もしない」というアクションを候補に入れない
	"""
	player = mygame.current_player
	myCandidate = []
	for card in player.hand:
		if card.is_playable():
			if card.must_choose_one:
				for card2 in card.choose_cards:
					if card2.is_playable():
						if card2.requires_target():
							for target in card.targets:
								if target.zone==Zone.PLAY: 
									myCandidate.append(Candidate(card, card2=card2, type=BlockType.PLAY, target=target,		turn=mygame.turn))
						else:
							myCandidate.append(Candidate(card, card2=card2, type=BlockType.PLAY, target=None, turn=mygame.turn))
			else:# card2=None
				if card.requires_target():
					for target in card.targets:
						if target.zone==Zone.PLAY:
							myCandidate.append(Candidate(card, type=BlockType.PLAY, target=target, turn=mygame.turn))
				else:
					myCandidate.append(Candidate(card, type=BlockType.PLAY, target=None, turn=mygame.turn))
	for character in player.characters:
		if character.type==CardType.LOCATION:
			if character.is_playable():
				if len(character.location_targets)>0:
					for target in character.location_targets:
						myCandidate.append(Candidate(card, type=ActionType.LOCATION, target=target, turn=mygame.turn))
				else:
					myCandidate.append(Candidate(card, type=ActionType.LOCATION, target=None, turn=mygame.turn))	
		elif character.can_attack():
			for target in character.targets:
				if target.zone==Zone.PLAY and character.can_attack(target) and character != target:
					#myH=character.health
					#hisA=target.atk
					#if (myH > hisA) or (not _smartCombat):
					myCandidate.append(Candidate(character, type=BlockType.ATTACK, target=target, turn=mygame.turn))
	if player.hero.power and player.hero.power.is_usable():
		if len(player.hero.power.targets)>0:
			for target in player.hero.power.targets:
				if target.zone==Zone.PLAY:
					myCandidate.append(Candidate(player.hero.power, type=BlockType.POWER, target=target, turn=mygame.turn))
		else:
			myCandidate.append(Candidate(player.hero.power, type=BlockType.POWER, target=None, turn=mygame.turn))
	for character in player.hand:
		_yes, _option = character.can_trade()
		if _yes:
			myCandidate.append(Candidate(character, type=ActionType.TRADE, target=None, turn=mygame.turn))
			pass
	if _includeTurnEnd:
		#この選択肢は「何もしない」選択肢ですが、
		#ターンを終了することはできないので、
		#エージェントの方でターンを終了してあげてください
		myCandidate.append(Candidate(None,type=ExceptionPlay.TURNEND, turn=mygame.turn))
		pass
	return myCandidate

def identifyPlayer(name1, name2):
	if len(name1) > len(name2):
		return (name1[:len(name2)]==name2)
	elif len(name1) < len(name2):
		return (name2[:len(name1)]==name1)
	if len(name1) == len(name2):
		return (name1==name2)

def identifyPlayCard(card1, card2):
	if card1==None or card2==None:
		return False
	cond1 = card1.is_playable() and card2.is_playable()
	cond2 = card1.id==card2.id
	cond3 = identifyPlayer(card1.controller.name, card2.controller.name)
	cond4 = card1.zone == card2.zone 
	#cond4 = card1.atk == card2.atk and card1.health == card2.health
	if cond1 and cond2 and cond3 and cond4:
		return True
	return False
def easyIdentifyPlayCard(card1, card2):
	if card1==None or card2==None:
		return False
	cond2 = card1.id==card2.id
	cond3 = identifyPlayer(card1.controller.name, card2.controller.name)
	if cond2 and cond3:
		return True
	return False
def identifyAttackCard(card1, card2):
	if card1==None or card2==None:
		return False
	cond11 = card1.can_attack()
	cond12 = card2.can_attack()
	cond2 = card1.id==card2.id
	cond3 = identifyPlayer(card1.controller.name, card2.controller.name)
	cond4 = card1.zone == card2.zone 
	#cond4 = card1.atk == card2.atk and card1.health == card2.health
	if cond12 and cond2 and cond3 and cond4:
		return True
	return False
def identifyTargetCard(card1, card2):
	if card1==None or card2==None:
		return False
	cond2 = card1.id==card2.id
	cond3 = identifyPlayer(card1.controller.name, card2.controller.name)
	#cond4 = card1.zone == card2.zone 
	if cond2 and cond3:
		return True
	return False
#
#  executeAction
#
def executeAction(mygame, action: Candidate, debugLog=True):
	""" Candidate型のアクションを実行する """
	mygame.add_log(action)
	if mygame.ended:
		return ExceptionPlay.GAMEOVER
	if action.type ==ExceptionPlay.TURNEND:
		return ExceptionPlay.TURNEND
		pass
	player=mygame.current_player
	thisEntities= mygame.entities + mygame.hands
	if debugLog:
		print(">%s>>%s"%(player,str(action)))
	theCard=theTarget=theCard2=None
	#print(id(action.card.game))
	#print(id(mygame))
	if action.card.game==mygame:
		theCard=action.card
	if action.card2!=None and action.card2.game==mygame:
		theCard2=action.card2
	if action.target!=None and action.card.game==mygame:
		theTarget=action.target
	if theCard!=None and ((action.target==None and theTarget==None) or (action.target!=None and theTarget!=None)):
		pass
	else:
		if action.card.zone==Zone.HAND and action.type==BlockType.PLAY:
			for card in player.hand:
				if identifyPlayCard(card, action.card):
					theCard = card
					if theCard.must_choose_one:
						for card2 in card.choose_cards:
							if easyIdentifyPlayCard(card2, action.card2):
								theCard2 = card2
								if theCard2.requires_target():
									for target in theCard2.targets:
										if identifyTargetCard(target, action.target):
											theTarget=target
								else:
									pass
					else:# card2=None
						if theCard.requires_target():
							for target in theCard.targets:
								if identifyTargetCard(target, action.target):
									theTarget=target
						else:
							pass
				else:
					_yes, _option = card.can_trade()
					if _yes and card.id==action.card.id:
						theCard = card
		if action.card.zone==Zone.PLAY and action.type==BlockType.ATTACK:
			for card in player.characters:
				if identifyAttackCard(card, action.card):
					theCard = card
					for target in card.targets:
						if identifyTargetCard(target, action.target): 
							##character.can_attack(target)
							theTarget = target
		if player.hero.power.id==action.card.id and action.type==BlockType.POWER:
			if player.hero.power.is_usable():
				theCard = player.hero.power
				for target in theCard.targets:
					if identifyTargetCard(target, action.target):
						theTarget = target
	if theCard==None:## to debug
		noCard=True
		if action.card.zone==Zone.HAND and action.type==BlockType.PLAY:
			for card in player.hand:
				if card.id==action.card.id:
					noCard=False
					if identifyPlayer(card.controller.name, action.card.controller.name):
						if card.is_playable():
							#print ("OK")
							theCard = card
							pass
						else:
							#print ("This card %s is unplayable"%(card))
							x=card.is_playable()
							return#

		if action.card.zone==Zone.PLAY and action.type==BlockType.ATTACK:
			for card in player.characters:
				if card.id==action.card.id:
					noCard=False
					if identifyPlayer(card.controller.name, action.card.controller.name):
						if card.can_attack():
							#print ("OK")
							theCard = card
							pass
						else:
							#print ("This card %s is unplayable"%(character))
							return#
		if player.hero.power.id==action.card.id and action.type==BlockType.POWER:
			if not player.hero.power.is_usable():
				if player.mana<player.hero.power.cost:
					pass
				else:
					player.hero.power.is_usable()
			pass
		if noCard:
			#print("no card %s is contained in the hand"%(action.card))
			return
		pass
	if action.type==BlockType.PLAY:
		if action.card.id != theCard.id:
			#print("%s != %s"%(action.card.id, theCard.id))
			#print("%s"%(action.card.game==mygame))
			return ExceptionPlay.INVALID
		if (theTarget != None and theTarget not in theCard.targets):
			#print ("theCard : %s"%(theCard))
			#for card in theCard.targets:
			#	print ("theCard.targets : %s"%(card))
			#print ("theCard2 : %s"%(theCard2))
			#print ("theTarget : %s"%(theTarget))
			return ExceptionPlay.INVALID
		if theCard.requires_target() and theTarget == None:
			#if action.target!=None:
			#	print ("action.target : %s(%s)"%(action.target, action.target.id))
			#	for card in theCard.targets:
			#		print ("theCard.targets : %s(%s)"%(card, card.id))
			#		print ("->identifyTarget : %s"%(identifyTargetCard(card, action.target)))
			#game1 = action.card.controller.game
			#game2 = theCard.controller.game
			#can1 = getCandidates(game1)
			#can2 = getCandidates(game2)
			#print("%d, %d"%(len(can1),len(can2)))
			return ExceptionPlay.INVALID
		if not theCard.is_playable():
			#result = theCard.is_playable()
			return ExceptionPlay.INVALID
		try:
			theCard.play(target=theTarget,choose=theCard2)
			if mygame.ended:
				return ExceptionPlay.GAMEOVER
			else:
				return ExceptionPlay.VALID
		except GameOver:
			return ExceptionPlay.GAMEOVER
	if action.type==BlockType.ATTACK:
		if not theCard.can_attack(theTarget):
			theCard.can_attack(theTarget)
			return ExceptionPlay.INVALID
		if theTarget==None:
			return ExceptionPlay.VALID
		try:
			theCard.attack(theTarget)
			if mygame.ended:
				return ExceptionPlay.GAMEOVER
			else:
				return ExceptionPlay.VALID
		except GameOver:
			return ExceptionPlay.GAMEOVER
	if action.type==BlockType.POWER:
		if not theCard.is_usable():
			return ExceptionPlay.INVALID
		try:
			if theCard.requires_target():
				if theTarget==None:
					return ExceptionPlay.INVALID
				else:
					theCard.use(target=theTarget)
			else:
				theCard.use()
			return ExceptionPlay.VALID
		except GameOver:
			return ExceptionPlay.GAMEOVER
	if action.type==ActionType.TRADE:
		_yes, _option = theCard.can_trade()
		if not _yes:
			return ExceptionPlay.INVALID
		try:
			theCard.trade(_option)#
			return ExceptionPlay.VALID
		except GameOver:#まあこれはないと思うけど。
			return ExceptionPlay.GAMEOVER
	if action.type==ActionType.LOCATION:
		if not theCard.is_playable():
			return ExceptionPlay.INVALID
		try:
			theCard.location(target=theTarget)#
			return ExceptionPlay.VALID
		except GameOver:
			return ExceptionPlay.GAMEOVER
	return ExceptionPlay.INVALID

class ExceptionPlay(IntEnum):
	""" ゲームの例外処理に使うフラグ """
	VALID=0
	GAMEOVER=1
	INVALID=2
	TURNEND=4

class BigDeck:
	#Available
	faceHunter = ['SCH_617','SCH_617','SCH_600','SCH_600','SCH_231','SCH_231',
		'CORE_DS1_184','CORE_DS1_184','SCH_279','SCH_133','SCH_133','BAR_801',
		'BAR_801','SCH_713','SCH_713','BT_211','BT_211','CORE_BRM_013',
		'CORE_BRM_013','SW_321','SW_321','BAR_721','BAR_032','BAR_032',
		'DMF_088','BAR_037','BAR_037','BAR_551','DMF_087','DMF_087',]
	bigWarrior = ['SW_023','SCH_237','SCH_237','CORE_EX1_410','CORE_EX1_410','BT_124',
		'DMF_522','DMF_522','BT_117','BT_117','SW_094','SW_094',
		'BT_781','BAR_845','BAR_845','BAR_844','YOP_005','YOP_005',
		'CORE_EX1_407','CORE_EX1_407','SW_021','SW_021','SCH_533','SCH_533',
		'SW_024','SCH_337','SCH_337','SW_068','SW_068','SCH_621',
		]
	clownDruid = ['CORE_EX1_169','CORE_EX1_169','SCH_427','SCH_427','SCH_311','SCH_311',
		'SCH_333','SCH_333','DMF_075','DMF_075','CORE_CS2_013','CORE_CS2_013',
		'BT_130','BT_130','BAR_535','SCH_605','SCH_605','SCH_616',
		'SCH_616','DMF_078','DMF_078','SCH_610','SCH_610','BAR_042',
		'BAR_042','DMF_163','DMF_163','SCH_609','SCH_609','AV_205'#'DMF_188'
		]


def postAction(player):
	while True:
		if player.choice == None:
			return None
		else:
			if player.choiceStrategy==None:
				if len(player.choice.cards)==0:
					choice = None
				else:
					choice = random.choice(player.choice.cards)
			else:
				choice = player.choiceStrategy(player,player.choice.cards)
			if Config.LOGINFO:
				print("%r Chooses a card %r" % (player, choice))
			#myChoiceStr = str(choice)
			if 'RandomCardPicker' in str(choice):
				myCardID =  random.choice(choice.find_cards())
				Give(player, myCardID).trigger(player)
				player.choice = None
			else :
				if choice == None:
					player.choice=None##return
					return None
				else:
					player.choice.choose(choice)
					##return choice

def random_draft_from_implemented_cards(card_class: CardClass, exclude=[]):
	"""
	カードクラスに従って「効果が実装されているカード」でランダムデッキを作る
	"""
	from fireplace import cards
	from fireplace.deck import Deck
	import random
	import os.path
	from pkgutil import iter_modules
	from importlib import import_module

	deck = []
	collection = []
	# hero = card_class.default_hero

	cards_module = os.path.join(os.path.dirname(__file__), "fireplace\\cards")
	CARD_SETS = [cs for _, cs, ispkg in iter_modules([cards_module]) if ispkg]
	for card in cards.db.keys():
		if card in exclude:
			continue
		cls = cards.db[card]
		if not cls.collectible:
			continue
		if cls.type == CardType.HERO:
			# Heroes are collectible...
			continue
		if cls.card_class and cls.card_class not in [card_class, CardClass.NEUTRAL]:
			# Play with more possibilities
			continue
		for cardset in CARD_SETS:
			module = import_module("fireplace.cards.%s" % (cardset))
			if hasattr(module, card):
				collection.append(cls)

	while len(deck) < Deck.MAX_CARDS:
		card = random.choice(collection)
		if deck.count(card.id) < card.max_count_in_deck:
			deck.append(card.id)

	return deck

def getTurnLog(gameLog, turnN):
	""" gameLogから特定のターンの情報を引き出す """
	if len(gameLog)<=0:
		return []
	ret = []
	for i in range(len(gameLog)):
		if gameLog[i].turn == turnN:
			ret.append(gameLog[i])
	return ret

from fireplace.deepcopy import deepcopy_game
def debug_deepcopy(game,player):
	return deepcopy_game(game,player,0)

def fireplace_deepcopy(game):
	return deepcopy_game(game, game.current_player,0)


