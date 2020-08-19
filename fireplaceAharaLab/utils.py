from hearthstone.enums import BlockType,CardType 
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


class Candidate(object):
	"""　"""
	def __init__(self, _card, _card2=None, _type=BlockType.PLAY, _target=None, _score=0, _strategy=StandardStrategy.FREE):
		#super(myAction, self).__init__()
		self.card=_card
		self.card2=_card2
		self.type=_type
		self.target=_target
		self.score=_score
		self.strategy = _strategy
		self.notes=''
		pass

	def __str__(self):
		return "{card}->{type}(target={target})".format(card=self.card,type=self.type,target=self.target)
		pass

	def __eq__(self,obj):
		return str(self)==str(obj)
		pass
	def clearScore(self):
		self.score = 0
	def setStrategy(self):
		"""
			FREE = 0
			HITATTACKxMINION = 1
			HITATTACKxHERO = 1
			SPELLATTACKxMINION = 2
			SPELLATTACKxHERO = 2
			HEALxMINION = 3
			HEALxHERO = 4
			DEFNEDxHERO = 5
			STRENGTHENxMINION = 6
			IMPROVExSTATUS = 7
		"""
		if minionAttackMinion():
			strategy=StandardStrategy.HITATTACKxMINION
		if minionAttackHero():
			strategy=StandardStrategy.HITATTACKxHERO
		if spellAttackMinion():
			strategy=StandardStrategy.SPELLATTACKxMINION
		if spellAttackHero():
			strategy=StandardStrategy.SPELLATTACKxHERO
		if healMinion():
			strategy=StandardStrategy.HEALxMINION
		#if defendHero():#HUNTERにはない。
		strategy=StandardStrategy.FREE
		pass
	def minionAttackMinion(self):
		if self.target!=None:
			if self.card.type == CardType.MINION and \
			   self.target.type == CardType.MINION and \
			   self.type==BlockType.ATTACK:
				return True
		return False
	def minionAttackHero(self):
		if self.target!=None:
			if self.card.type == CardType.MINION and \
			   self.target.type == CardType.HERO and \
			   self.type==BlockType.ATTACK:
				return True
		return False
	def spellAttackMinion(self):
		if self.target!=None:
			if self.card.type == CardType.SPELL and \
			   self.target.type == CardType.MINION and \
			   self.type==BlockType.PLAY:
				return True
		return False
	def spellAttackHero(self):
		if self.target!=None:
			if self.card.type == CardType.SPELL and \
			   self.target.type == CardType.HERO and \
			   self.type==BlockType.PLAY:
				return True
		return False
	def healMinion():
		if self.target!=None and \
		self.target.type == CardType.MINION and\
		self.target.controller == self.card.controller and\
		self.type==BlockType.PLAY:# + healing condition
			return True
		return False

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


