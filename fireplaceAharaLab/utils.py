from hearthstone.enums import CardClass,BlockType, CardType ,PlayState, State
from enum import IntEnum
from fireplace.game import Game
from fireplace.card import Card
from fireplace.exceptions import GameOver
from fireplace.actions import *
import copy
import random
#<<<<<<< HEAD
#=======
import time
from fireplace.config import Config
#>>>>>>> c947fa55d1dd14097e8109e5362956b2830eca7f

class myAction(object):#旧マヤ版Action  ActionValueとあわせて、Candidateと言う形で下に再構成した。
	"""docstring for myAction"""
	def __init__(self, _card,_type,_target=None):
		super(myAction, self).__init__()
		self.card=_card
		self.type=_type
		self.target=_target

	def __str__(self):
		return "{card}->{type}(target={target})".format(card=self.card,type=self.type,target=self.target)
		pass

	def __eq__(self,obj):
		return str(self)==str(obj)
		pass
class myActionValue(object):#旧マヤ版ActionValue
	"""docstring for myActionValue"""
	def __init__(self, _action,_score):
		super(myActionValue, self).__init__()
		self.action = _action
		self.score=_score
		
class Node(object):
	"""docstring for Node"""
	def __init__(self, gameTree,move,parent,actions):
		super(Node, self).__init__()
		self.gameTree=gameTree
		self.move=move
		self.parent=parent
		self.childNodes=[]
		self.wins=0
		self.visits=0
		self.untriedMoves=copy.deepcopy(actions)
		self.score=0
	def selectChild(self):
		import math#
		self.totalVisit=self.visits
		self.values=list(map(lambda node:node.wins/node.visits+math.sqrt(math.log(self.totalVisit)/node.visits),self.childNodes))
		retNode=self.childNodes[self.values.index(max(self.values))]
		return retNode
		pass
	def expandChild(self,action):
		self.expandedTree=executeAction(self.gameTree,action)
		child=Node(self.expandedTree,action,self,getCandidates(self.expandedTree))
		self.childNodes.append(child)
		return child
	def choose_expanding_action(self):
		index=int(random.random()*len(self.untriedMoves))
		return self.untriedMoves.pop(index)		
		pass
	def simulate(self):
		return simulate_random_game(self.gameTree)
		pass
	def backPropagate(self,result=None):
		self.addVal=self.score
		if result is not None:
			self.addVal=result
			pass
		self.wins+=self.addVal
		self.visits+=1;
		if self.parent is None:
			pass
		else:
			self.parent.backPropagate(self.addVal)
		pass
	def setScore(self,_score):
		self.score=_score
		pass

	
class Evaluation(object):
	"""docstring for Evaluation"""
	def __init__(self, deck,score):
		super(Evaluation, self).__init__()
		self.deck = deck
		self.score=score
	def getScore(self):
		return self.score
		pass		


class Agent(object):
	""" """
	def __init__(self, myName: str, myFunction, myOption: list, myClass: CardClass, rating ,E = 0):
		self.name = myName
		self.func = myFunction
		self.option = myOption
		self.myClass = myClass
		self.rating = rating = 1500
		self.E = E 
		pass

	def __str__(self):
		return self.name

def play_one_game(P1: Agent, P2: Agent, deck1=[], deck2=[], debugLog=True):
	""" 1回ゲームを行う。 """
	from fireplace.utils import random_draft
	from fireplace.player import Player
	import random
	#バグが確認されているものを当面除外する
	exclude = ['CFM_672','CFM_621','CFM_095','LOE_076','BT_490']
	# 'LOE_076' : Sir Finley Mrrgglton
	# 'BT_490' : 魔力喰い、ターゲットの扱いにエラーがあるので除外。
	deck1 = deck2 = BigDeck.faceHunter
	if len(deck1)==0:
		deck1 = random_draft(P1.myClass,exclude)#カードクラスに従ったランダムなデッキ
	if len(deck2)==0:
		deck2 = random_draft(P2.myClass,exclude)#カードクラスに従ったランダムなデッキ
	player1 = Player(P1.name, deck1, P1.myClass.default_hero)
	player2 = Player(P2.name, deck2, P2.myClass.default_hero)

	game = GameWithLog(players=(player1, player2))
	game.start()

	for player in game.players:
		#mulliganの試合前処理（デッキは撹拌される）
		mull_count = random.randint(0, len(player.choice.cards))
		cards_to_mulligan = random.sample(player.choice.cards, mull_count)
		player.choice.choose(*cards_to_mulligan)
#<<<<<<< HEAD
#	if HeroHPOption != 30:
#		game.player1.hero.max_health = HeroHPOption
#		game.player2.hero.max_health = HeroHPOption
#	PresetHands(player1, player2)
#=======
	if Config.HEROHPOPTION != 30:
		game.player1.hero.max_health = int(Config.HEROHPOPTION)
		game.player2.hero.max_health = int(Config.HEROHPOPTION)
	game.player1.max_mana=int(Config.P1MAXMANA)
	game.player2.max_mana=int(Config.P2MAXMANA)-1
	if (len(game.player1.hand)-1) != Config.P1HAND:
		if (len(game.player1.hand)-1) > Config.P1HAND:
			rt_cards = random.sample(game.player1.hand, (len(game.player1.hand)-1)-Config.P1HAND)
			for card in rt_cards:
				card.zone = Zone.DECK
		else:
			game.player1.draw(Config.P1HAND-(len(game.player1.hand)-1))
	if len(game.player2.hand) != Config.P2HAND:
		if len(game.player2.hand) > Config.P2HAND:
			rt_cards = random.sample(game.player2.hand[:len(game.player2.hand)-1], len(game.player2.hand)-Config.P2HAND)
			for card in rt_cards:
				card.zone = Zone.DECK
		else:
			game.player2.draw(Config.P2HAND-len(game.player2.hand))
	PresetHands(player1, player2)

#>>>>>>> c947fa55d1dd14097e8109e5362956b2830eca7f
	while True:	
		#エージェントの処理ここから
		player = game.current_player
		if player.name==P1.name:
			#Agent.funcには引数 self, game, option, gameLog, debugLogを作ってください
			P1.func(P1, game, option=P1.option, gameLog=game.get_log(), debugLog=debugLog)
		elif player.name==P2.name:
			#Agent.funcには引数 self, game, option, gameLog, debugLogを作ってください
			P2.func(P2, game, option=P2.option, gameLog=game.get_log(), debugLog=debugLog)
		else:
			Original_random(game)#公式のランダム
		#ターンエンドの処理ここから
		if player.choice!=None:
			player.choice=None#論理的にはおこらないが、agentのミスによりときどきおこる
		if game.state!=State.COMPLETE:
			try:
				game.end_turn()
			except GameOver:#まれにおこる
				gameover=0
		#ゲーム終了フラグが立っていたらゲーム終了処理を行う
		if game.state==State.COMPLETE:
			if game.current_player.playstate == PlayState.WON:
				return game.current_player.name
			if game.current_player.playstate == PlayState.LOST:
				return game.current_player.opponent.name
			return 'DRAW'#まず起こらないが、ねんのため。

def play_set_of_games(P1: Agent, P2: Agent, deck1=[], deck2=[], gameNumber=15, debugLog=True):
	""" 決まった回数の試合を行い、勝敗数を表示する """
	if debugLog:
		print(" %r (%s) vs.  %r (%s)"%(P1.name, P1.myClass, P2.name, P2.myClass))
	Count1 = 0
	Count2 = 0
	for i in range(gameNumber):
		winner = play_one_game(P1,P2,deck1, deck2, debugLog=debugLog)
		if debugLog:
			print("winner is %r"%winner)
		if winner == P1.name:
			Count1+=1
		elif winner == P2.name:
			Count2+=1
	print(" %r (%s) wins: %d"%(P1.name, P1.myClass, Count1))
	print(" %r (%s) wins: %d"%(P2.name, P2.myClass, Count2))
	print(" Draw: %d"%(gameNumber-Count1-Count2))

class Candidate(object):
	"""　アクションの候補手のクラス　"""
	def __init__(self, card, card2=None, type=BlockType.PLAY, target=None, turn=None):
		#super(myAction, self).__init__()
		self.turn=turn
		self.card = card
		self.card2 = card2
		self.type = type
		self.target = target
		self.score = 0
		self.minionHealth = 0
		self.notes = ''
		pass

	def __str__(self):
		return "{card}->{type}(target={target})".format(card=self.card,type=str(self.type),target=self.target)
		pass

	def __eq__(self,obj):
		return str(self)==str(obj)
		pass
	def clearScore(self):
		self.score = 0


class GameWithLog(Game):
	""" ゲーム進行のログを管理する  """
	def __init__(self, players):
		super().__init__(players=players)
		self.__myLog__=[]
	def add_log(self, choice: Candidate):
		self.__myLog__.append(choice)
	def get_log(self):
		return self.__myLog__
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
				if character.can_attack(target):
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
	if _includeTurnEnd:
		#この選択肢は「何もしない」選択肢ですが、
		#ターンを終了することはできないので、
		#エージェントの方でターンを終了してあげてください
		myCandidate.append(Candidate(None,type=ExceptionPlay.TURNEND, turn=mygame.turn))
		pass
	return myCandidate
#
#  executeAction
#
def executeAction(mygame, action: Candidate, debugLog=True):
	"""　Candidate型のアクションを実行する　"""
	mygame.add_log(action)
	if action.type ==ExceptionPlay.TURNEND:
		return ExceptionPlay.TURNEND
		pass
	player=mygame.current_player
	thisEntities= mygame.entities + mygame.hands
	if debugLog:
		print("%s %s"%(player,str(action)))
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
			if card.is_playable() and card==action.card and card.controller.name==action.card.controller.name:
				theCard = card
				if theCard.must_choose_one:
					for card2 in card.choose_cards:
						if card2.is_playable() and card2==action.card2:
							theCard2 = card2
							if theCard2.requires_target():
								for target in theCard2.targets:
									if target==action.target and target.controller.name==action.target.controller.name:
										theTarget=target
							else:
								pass
				else:# card2=None
					if theCard.requires_target():
						for target in theCard.targets:
							if target==action.target and target.controller.name == action.target.controller.name:
								theTarget=target
					else:
						pass
		for character in player.characters:
			if character.can_attack() and character==action.card and character.controller.name==action.card.controller.name:
				theCard = character
				for target in character.targets:
					if character.can_attack(target) and target==action.target and target.controller.name==action.target.controller.name:
						theTarget = target
		if player.hero.power==action.card:
			if player.hero.power.is_usable():
				theCard = player.hero.power
				for target in theCard.targets:
					if target==action.target and target.controller.name==action.target.controller.name:
						theTarget = target
	if action.type==BlockType.PLAY:
		if (theTarget != None and theTarget not in theCard.targets):
			return ExceptionPlay.INVALID
		if not theCard.is_playable():
			return ExceptionPlay.INVALID
		try:
			theCard.play(target=theTarget,choose=theCard2)
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
	return ExceptionPlay.INVALID

class ExceptionPlay(IntEnum):
	""" ゲームの例外処理に使うフラグ　"""
	VALID=0
	GAMEOVER=1
	INVALID=2
	TURNEND=4

class BigDeck:
	MechaHunter = ['BOT_445','BOT_445','BOT_035','BOT_035','BOT_038',\
		'BOT_038','BOT_309','BOT_309','BOT_907','BOT_907',\
		'BOT_033','BOT_033','DAL_604','DAL_604','BOT_251',\
		'BOT_251','BOT_700','EX1_556','EX1_556','BOT_532',\
		'BOT_532','BOT_312','BOT_312','BOT_563','BOT_563',\
		'BOT_548','EX1_116','BOT_107','BOT_107','BOT_034']
	faceHunter = [\
		'SCH_617','SCH_617','SCH_312','SCH_312','DRG_253','DRG_253','SCH_133','SCH_133',\
		'SCH_231','SCH_231','SCH_600','SCH_600','BT_213','BT_213','DRG_252','DRG_252',\
		'EX1_611','ULD_152','EX1_610','BT_203','SCH_142','SCH_142','EX1_536','EX1_536',\
		'EX1_539','EX1_539','NEW1_031','NEW1_031','DRG_256','SCH_428']

def postAction(player):
	if player.choice:
		choice = random.choice(player.choice.cards)
		#print("Choosing card %r" % (choice))
		myChoiceStr = str(choice)
		if 'RandomCardPicker' in str(choice):
			myCardID =  random.choice(choice.find_cards())
			myCard = Card(myCardID)
			myCard.controller = player#?
			myCard.draw()
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

def PresetHands(player1, player2): 
	#forcedraw some specific cards to debug, 特定のカードを引かせたい場合。
	n = 0
	m = 0
	if player1.name == "Vector1" :
		n = 1
	elif player1.name == "Vector2":
		n = 2
	elif player1.name == "Vector3":
		n = 3
	elif player1.name == "Vector4": 
		n = 4
	elif player1.name == "Vector5":
		n = 5
	elif player1.name == "Vector6":
		n = 6
	elif player1.name == "Vector7": 
		n = 7
	elif player1.name == "Vector8":
		n = 8
	elif player1.name == "Vector9":
		n = 9
	elif player1.game == "Vector10":
		n = 10
	
	if player2.name == "Vector1" :
		m = 1
	elif player2.name == "Vector2":
		m = 2
	elif player2.name == "Vector3":
		m = 3
	elif player2.name == "Vector4": 
		m = 4
	elif player2.name == "Vector5":
		m = 5
	elif player2.name == "Vector6":
		m = 6
	elif player2.name == "Vector7": 
		m = 7
	elif player2.name == "Vector8":
		m = 8
	elif player2.name == "Vector9":
		m = 9
	elif player2.game == "Vector10":
		m = 10
	#print(n)
	#print(m)
	for num in range(n):
		Draw(player1).trigger(player1) # n枚引かせる
	for num in range(m):
		Draw(player2).trigger(player2) # n枚引かせる
#Give(player1,'ULD_178').trigger(player1)#target
#=======
#	Discard(player1.hand[-1]).trigger(player1)
#	Give(player1,'SCH_270').trigger(player1)#target
	#Give(player1,'DAL_604').trigger(player1)#subtarget-
	#Give(player1,'SCH_133').trigger(player1)#subtarget-beast
	#Give(player1,'DAL_587').trigger(player1)#subtarget-deathrattle
	#Give(player1,'SCH_232').trigger(player1)#subtarget-DRAGON
	#Give(player1,'DRG_107').trigger(player1)#subtarget-elemental
	#Give(player1,'DRG_057').trigger(player1)#subtarget-MECH
	#Give(player1,'CS2_168').trigger(player1)#subtarget-murloc
	#Give(player1,'BT_720').trigger(player1)#subtarget-rush
	#Give(player1,'EX1_609').trigger(player1)#subtarget-secret
	#Give(player1,'DRG_255').trigger(player1)#subtarget-sidequest
	#Give(player1,'SCH_310').trigger(player1)#subtarget-spellpower
	#Give(player1,'BT_715').trigger(player1)#subtarget-taunt
	#Give(player1,'SCH_301').trigger(player1)#subtarget-weapon

	#Give(player2,'DAL_090').trigger(player2)#enemy
	#Give(player2,'ULD_152').trigger(player2)#enemy

	#start of the specific numbers of manas, 特定のマナ数から始めたいとき
	player1.max_mana=1
	player2.max_mana=1

	#force play by player2
	#PresetPlay(player2, 'DAL_090')# play
	#PresetPlay(player2, 'ULD_152')# play

	#force-pass of player2,
	#if player2==player2.game.current_player:
	#	player2.game.end_turn()

	#force turn end of player1
	#player1.game.end_turn()
	pass

def PresetPlay(player, cardID):
	for card in player.hand:
		if card.id == cardID and card.is_playable():
			card.play(target=None)