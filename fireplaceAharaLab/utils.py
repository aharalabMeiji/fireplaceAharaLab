from hearthstone.enums import BlockType, CardType ,PlayState, State
from enum import IntEnum
from fireplace.game import Game

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
		self.expandedTree=execute_action(self.gameTree,action)
		child=Node(self.expandedTree,action,self,get_valid_actions(self.expandedTree))
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
	from hearthstone.enums import CardClass
	def __init__(self, myName: str, myFunction, myOption: list=[], myClass: CardClass =CardClass.HUNTER, rating = 1000 ):
		self.name = myName
		self.func = myFunction
		self.option = myOption
		self.myClass = myClass
		self.rating = rating
		pass

	def __str__(self):
		return self.myName

def play_one_game(P1: Agent, P2: Agent, deck1=[], deck2=[], HeroHPOption=30, debugLog=True):
	from fireplace.utils import random_draft
	from fireplace.player import Player
	import random
	#バグが確認されているものを当面除外する
	exclude = ['CFM_672','CFM_621','CFM_095','LOE_076','BT_490']
	# 'LOE_076' : Sir Finley Mrrgglton
	# 'BT_490' : 魔力喰い、ターゲットの扱いにエラーがあるので除外。
	if len(deck1)==0:
		deck1 = random_draft(P1.myClass,exclude)#ランダムなデッキ
	if len(deck2)==0:
		deck2 = random_draft(P2.myClass,exclude)#ランダムなデッキ
	player1 = Player(P1.name, deck1, P1.myClass.default_hero)
	player2 = Player(P2.name, deck2, P2.myClass.default_hero)

	game = Game(players=(player1, player2))
	game.start()

	for player in game.players:
		#print("Can mulligan %r" % (player.choice.cards))
		mull_count = random.randint(0, len(player.choice.cards))
		cards_to_mulligan = random.sample(player.choice.cards, mull_count)
		player.choice.choose(*cards_to_mulligan)
	if HeroHPOption != 30:
		game.player1.hero.max_health = HeroHPOption
		game.player2.hero.max_health = HeroHPOption
	while True:	
		from agent_Standard import StandardRandom, HumanInput, Original_random 
		from agent_Maya import Maya_MCTS
		player = game.current_player
		#print("%r starts their turn."%player.name);
		if player.name=="Maya":
			Maya_MCTS(game)#マヤ氏の作品
		elif player.name=="Standard":
			StandardRandom(game, debugLog=debugLog)#公式のランダムより、もう少しキチンとしたランダムプレーエージェント
		elif player.name=="Human":
			HumanInput(game)#人がプレーするときはこれ
		elif player.name==P1.name:
			P1.func(game, option=P1.option, debugLog=debugLog)#P1.funcには引数option, debugLogを作ってください
		elif player.name==P2.name:
			P2.func(game, option=P2.option, debugLog=debugLog)#P2.funcには引数option, debugLogを作ってください
		else:
			Original_random(game)#公式のランダム
		if player.choice!=None:
			player.choice=None#論理的にはおこらないが、ときどきおこる
		if game.state!=State.COMPLETE:
			try:
				game.end_turn()
			except GameOver:#まれにおこる
				gameover=0
		if game.state==State.COMPLETE:#ゲーム終了フラグが立っていたら
			if game.current_player.playstate == PlayState.WON:
				return game.current_player.name
			if game.current_player.playstate == PlayState.LOST:
				return game.current_player.opponent.name
			return 'DRAW'

def play_set_of_games(P1: Agent, P2: Agent, gameNumber=15, debugLog=True):
	if debugLog:
		print(" %r (%s) vs.  %r (%s)"%(P1.name, P1.myClass, P2.name, P2.myClass))
	Count1 = 0
	Count2 = 0
	for i in range(gameNumber):
		winner = play_one_game(P1,P2,debugLog=debugLog)
		if debugLog:
			print("winner is %r"%winner)
		if winner == P1.name:
			Count1+=1
		elif winner == P2.name:
			Count2+=1
		if debugLog:
			print(" %r (%s) wins: %d"%(P1.name, P1.myClass, Count1))
			print(" %r (%s) wins: %d"%(P2.name, P2.myClass, Count2))
			print(" Draw: %d"%(gameNumber-Count1-Count2))


class Candidate(object):
	"""　"""
	def __init__(self, card, card2=None, type=BlockType.PLAY, target=None, score=0):
		#super(myAction, self).__init__()
		self.card = card
		self.card2 = card2
		self.type = type
		self.target = target
		self.score = score
		self.notes = ''
		pass

	def __str__(self):
		return "{card}->{type}(target={target})".format(card=self.card,type=self.type,target=self.target)
		pass

	def __eq__(self,obj):
		return str(self)==str(obj)
		pass
	def clearScore(self):
		self.score = 0


#
##  getActionCandidates : utils version
##
def getCandidates(mygame):
	"""　"""
	player = mygame.current_player
	myCandidate = []
	for card in player.hand:
		if card.is_playable():
			if card.must_choose_one:
				for card2 in card.choose_cards:
					if card2.is_playable():
						if card2.requires_target():
							for target in card.targets:
								myCandidate.append(Candidate(card, _card2=card2, _type=BlockType.PLAY, _target=target))
						else:
							myCandidate.append(Candidate(card, _card2=card2, _type=BlockType.PLAY, _target=None))
			else:# card2=None
				if card.requires_target():
					for target in card.targets:
						myCandidate.append(Candidate(card, _type=BlockType.PLAY, _target=target))
				else:
					myCandidate.append(Candidate(card, _type=BlockType.PLAY, _target=None))
	for character in player.characters:
		if character.can_attack():
			for target in character.targets:
				if character.can_attack(target):
					myH=character.health
					hisA=target.atk
					if myH > hisA:
						myCandidate.append(Candidate(character, _type=BlockType.ATTACK, _target=target))
	return myCandidate
#
#  executeAction
#
def executeAction(mygame,action: Candidate):
	"""　"""
	player=mygame.current_player
	thisEntities= mygame.entities + mygame.hands
	print("%s %s"%(player,str(action)))
	theCard=None
	theCard2=None
	theTarget=None

	for entity in thisEntities:
		if entity ==action.card:
			theCard=entity
		if entity == action.card2:
			theCard2=entity
		if entity == action.target:
			theTarget=entity

	if action.type==BlockType.PLAY:
		if not theCard.is_playable():
			return ExceptionPlay.INVALID
		if theTarget != None and theTarget not in theCard.targets:
			return ExceptionPlay.INVALID
		try:
			theCard.play(target=theTarget)
			return ExceptionPlay.VALID
		except GameOver:
			return ExceptionPlay.GAMEOVER
	if action.type==BlockType.ATTACK:
		if not theCard.can_attack(theTarget):
			return ExceptionPlay.INVALID
		try:
			theCard.attack(theTarget)
			return ExceptionPlay.VALID
		except GameOver:
			return ExceptionPlay.GAMEOVER
	return ExceptionPlay.INVALID

class ExceptionPlay(IntEnum):
	""" """
	VALID=0
	GAMEOVER=1
	INVALID=2


