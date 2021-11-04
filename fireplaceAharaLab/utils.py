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

def play_one_game(P1: Agent, P2: Agent, deck1=[], deck2=[], debugLog=True, HEROHPOPTION=30, P1MAXMANA=1, P2MAXMANA=1, P1HAND=3, P2HAND=3):
	""" エージェント同士で1回対戦する。
	実験的に、ヒーローの体力、初期マナ数、初期ハンド枚数をコントロールできます。
	play one game by P1 and P2 """
	from fireplace.utils import random_draft
	from fireplace.player import Player
	import random
	exclude = []# you may exclude some cards to construct a deck
	log.info("New game settings")
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

	PresetHands(player1, player2)# if you want to controll the player's hand, write here
	log.info("New game start")

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
		else:
			Original_random(game)#random player by fireplace
		#turn end procedure from here
		if player.choice!=None:
			player.choice=None#somotimes it comes here
		if game.state!=State.COMPLETE:
			try:
				game.end_turn()
				if debugLog:
					print(">>>>>>>>>>turn change %d[sec]"%(time.time()-start_time),end='  ')
					print("%d : %d"%(player1.hero.health,player2.hero.health))
				if game.current_player.choice!=None:
					postAction(game.current_player)
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
	"""　アクションの候補手のクラス　
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
			return "{card}({atk1}/{health1}) -> attacks -> {target}({atk2}/{health2})".format(card=self.card, atk1=self.card.atk, health1=self.card.health, target=self.target,atk2=self.target.atk,health2=self.target.health)
		elif self.type==ExceptionPlay.TURNEND:
			return "Turn end."
		elif self.type==BlockType.POWER:
			if self.target:
				return "{card} -> heropower -> {target}({atk2}/{health2})".format(card=self.card, target=self.target,atk2=self.target.atk,health2=self.target.health)
			else:
				return "{card} -> heropower".format(card=self.card)
		elif self.type==BlockType.PLAY:
			if self.target==None:
				return "{card}:{cost} -> plays".format(card=self.card, cost = self.card.cost)
			else :
				return "{card}:{cost} -> plays -> {target}({atk2}/{health2})".format(card=self.card, cost = self.card.cost, target=self.target,atk2=self.target.atk,health2=self.target.health)
		elif self.type==ActionType.TRADE:
			return "{card} -> trade".format(card=self.card)
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
def getCandidates(mygame,_smartCombat=True,_includeTurnEnd=False):
	"""　アクションの候補をすべてリスト化して返す　
	_smartCombat=True,　スマートコンバットなもののみをリストアップする
	_includeTurnEnd=False　「何もしない」というアクションを候補に入れない
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
								myCandidate.append(Candidate(card, card2=card2, type=BlockType.PLAY, target=target, turn=mygame.turn))
						else:
							myCandidate.append(Candidate(card, card2=card2, type=BlockType.PLAY, target=None, turn=mygame.turn))
			else:# card2=None
				if card.requires_target():
					for target in card.targets:
						myCandidate.append(Candidate(card, type=BlockType.PLAY, target=target, turn=mygame.turn))
				else:
					myCandidate.append(Candidate(card, type=BlockType.PLAY, target=None, turn=mygame.turn))
	for character in player.characters:
		if character.can_attack():
			for target in character.targets:
				if character.can_attack(target) and character != target:
					myH=character.health
					hisA=target.atk
					if (myH > hisA) or (not _smartCombat):
						myCandidate.append(Candidate(character, type=BlockType.ATTACK, target=target, turn=mygame.turn))
	if player.hero.power.is_usable():
		if len(player.hero.power.targets)>0:
			for target in player.hero.power.targets:
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

#
#  executeAction
#
def executeAction(mygame, action: Candidate, debugLog=True):
	"""　Candidate型のアクションを実行する　"""
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
		for card in player.hand:
			if card.is_playable() and card.id==action.card.id and identifyPlayer(card.controller.name, action.card.controller.name):
				theCard = card
				if theCard.must_choose_one:
					for card2 in card.choose_cards:
						if card2.is_playable() and card2.id==action.card2.id and identifyPlayer(card2.controller.name, action.card2.controller.name):
							theCard2 = card2
							if theCard2.requires_target():
								for target in theCard2.targets:
									if target==action.target and identifyPlayer(target.controller.name, action.target.controller.name):
										theTarget=target
							else:
								pass
				else:# card2=None
					if theCard.requires_target():
						for target in theCard.targets:
							if target==action.target and identifyPlayer(target.controller.name, action.target.controller.name):
								theTarget=target
					else:
						pass
			else:
				_yes, _option = card.can_trade()
				if _yes and card.id==action.card.id:
					theCard = card
		for character in player.characters:
			if character.can_attack() and character==action.card and identifyPlayer(character.controller.name, action.card.controller.name):
				theCard = character
				for target in character.targets:
					if character.can_attack(target) and target==action.target and identifyPlayer(target.controller.name, action.target.controller.name):
						theTarget = target
		if player.hero.power==action.card:
			if player.hero.power.is_usable():
				theCard = player.hero.power
				for target in theCard.targets:
					if target==action.target and identifyPlayer(target.controller.name, action.target.controller.name):
						theTarget = target
	if theCard==None:## to debug
		noCard=True
		for card in player.hand:
			if card.id==action.card.id:
				noCard=False
				if identifyPlayer(card.controller.name, action.card.controller.name):
					if card.is_playable():
						print ("OK")

		for character in player.characters:
			if character.id==action.card.id:
				noCard=False
				if identifyPlayer(character.controller.name, action.card.controller.name):
					if character.can_attack():
						print ("OK")
		if noCard:
			print("no card %s is contained in the hand"%(action.card))
			return
		pass
	if action.type==BlockType.PLAY:
		if action.card.id != theCard.id:
			print("%s != %s"%(action.card.id, theCard.id))
			print("%s"%(action.card.game==mygame))
			return ExceptionPlay.INVALID
		if (theTarget != None and theTarget not in theCard.targets):
			return ExceptionPlay.INVALID
		if not theCard.is_playable():
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
	return ExceptionPlay.INVALID

class ExceptionPlay(IntEnum):
	""" ゲームの例外処理に使うフラグ　"""
	VALID=0
	GAMEOVER=1
	INVALID=2
	TURNEND=4

class BigDeck:
	#Available
	faceHunter_old = ['SCH_617','SCH_617','SCH_312','SCH_312','DRG_253','DRG_253','SCH_133','SCH_133',\
		'SCH_231','SCH_231','SCH_600','SCH_600','BT_213','BT_213','DRG_252','DRG_252',\
		'CORE_EX1_611','ULD_152','CORE_EX1_610','BT_203','SCH_142','SCH_142','EX1_536','EX1_536',\
		'EX1_539','EX1_539','NEW1_031','NEW1_031','DRG_256','SCH_428']
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
		'BAR_042','DMF_163','DMF_163','SCH_609','SCH_609','DMF_188'
		]


def postAction(player):
	while True:
		if player.choice == None:
			return
		else:
			if player.choiceStrategy==None:
				choice = random.choice(player.choice.cards)
			else:
				choice = player.choiceStrategy(player,player.choice.cards)
			log.info("%r Chooses a card %r" % (player, choice))
			#myChoiceStr = str(choice)
			if 'RandomCardPicker' in str(choice):
				myCardID =  random.choice(choice.find_cards())
				Give(player1,myCardID).trigger(player1)
				player.choice = None
			else :
				player.choice.choose(choice)

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

def ExchangeCard(cards,player):
	Discard(player.hand[0]).trigger(player)
	for _card in cards:
		if _card=='arcane':
			_card=random.choice(['CORE_DS1_185','CORE_BOT_453','YOP_019'])
		if _card=='attackspell':
			_card=random.choice(['SCH_348','SCH_604','BAR_801','BAR_032'])
		if _card=='beast':
			_card=random.choice(['SCH_133','SCH_714'])
		if _card=='corrupt':
			_card=random.choice(['DMF_124','DMF_082','DMF_073'])
		if _card=='deathrattle':
			_card=random.choice(['SW_070','CORE_FP1_007','CORE_EX1_012'])
		if _card=='dragon':
			_card='SCH_232'
		if _card=='elemental':
			_card=random.choice(['SCH_143','SCH_245'])
		if _card=='fire':
			_card=random.choice(['CORE_CS2_029','SW_462','SW_108','BAR_546','SW_110'])
		if _card=='frost':
			_card=random.choice(['SCH_509','BAR_305','CORE_GIL_801'])
		if _card=='mech':
			_card=random.choice(['CORE_GVG_085','CORE_GVG_076','CORE_GVG_044'])
		if _card=='murloc':
			_card=random.choice(['BAR_063','BAR_062','WC_030'])
		if _card=='nature':
			_card='SCH_333'
		if _card=='pirate':
			_card=random.choice(['CS3_022','CORE_NEW1_018','BAR_081'])
		if _card=='rush':
			_card=random.choice(['YOP_031'])
		if _card=='secret':
			_card=random.choice(['DMF_123','CORE_EX1_554','CORE_EX1_611'])
		if _card=='spell':
			_card=random.choice(['BAR_305','BAR_541','BAR_546','WC_041','BAR_542'])
		if _card=='spellpower':
			_card=random.choice(['SW_061'])
		if _card=='weapon':
			_card=random.choice(['WC_037','DMF_088'])
		Give(player,_card).trigger(player)

def PresetHands(player1, player2): 
	## add a specific card into the deck
	#PutOnTop(player1,'').trigger(player1)#specific card into deck
	
	#forcedraw some specific cards to debug, 特定のカードを引かせたい場合。
	#ExchangeCard([''],player1)
	#ExchangeCard(['weapon'],player2)
	pass

def PresetPlay(player, cardID):
	for card in player.hand:
		if card.id == cardID and card.is_playable():
			card.play(target=None)

