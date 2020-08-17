from hearthstone.enums import BlockType,CardType 
from enum import IntEnum
from fireplace.game import Game

class myAction(object):
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
class myActionValue(object):
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

class StandardStrategy(IntEnum):
	"""	standard strategy """
	FREE = 0
	HITATTACKxMINION = 1
	SPELLATTACKxMINION = 2
	HEALxMINION = 3
	HEALxHERO = 4
	DEFNEDxHERO = 5
	STRENGTHENxMINION = 6
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
	#card = player.hero.power#HUNTER: 不抜の一矢
	#if card.is_playable():
	#	myCandidate.append(Candidate(card, _type=BlockType.PLAY))
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

class StrategyWeight(object):
	"""
	Status Weight for my agent
	"""
	def __init__(self, w: list=[0,0,0,0,0,0,0,0,0,0]):#正の数からなる長さ＊＊＊のlist
		self.myHeroH = w[0]#自ヒーローのHPの増え具合
		self.hisHeroH = w[1]#相手ヒーローのHPの減り具合
		self.myCharA = w[2]#自分のフィールドにあるミニョンの攻撃力の総和を増やす
		self.myCharH = w[3]#自分のフィールドにあるミニョンのHPの総和を増やす
		self.myTauntCharH = w[4]#自分のフィールドにある挑発ミニョンのHPの総和を増やす
		self.hisCharA = w[5]#相手のフィールドにあるミニョンの攻撃力の総和を減らす
		self.hisCharH = w[6]#相手のフィールドにあるミニョンのHPの総和を減らす
		self.hisTauntCharH = w[7]#相手のフィールドにある挑発ミニョンのHPを減らす
		self.MinionCH = w[8]#手持ちのミニョンを優先する
		self.SpellCN = w[9]#手持ちの呪文を優先する.


	def __str__(self):
		myText =  ''+str(self.myHeroH)+','
		myText += str(self.hisHeroH)+','
		myText += str(self.myCharA)+','
		myText += str(self.myCharH)+','
		myText += str(self.myTauntCharH)+','
		myText += str(self.hisCharA)+','
		myText += str(self.hisCharH)+','
		myText += str(self.hisTauntCharH)+','
		myText += str(self.MinionCH)+','
		myText += str(self.SpellCN)
		return myText

	def __eq__(self,obj):
		return self.myHeroH==obj.myHeroH and self.hisHeroH==obj.hisHeroH and \
			self.myCharA==obj.myCharA and self.myCharH==obj.myCharH and self.myTauntCharH==obj.myTauntCharH and \
			self.hisCharA==obj.hisCharA and self.hisCharH==obj.hisCharH and self.hisTauntCharH==obj.hisTauntCharH and \
			self.MinionCH==obj.MinionCH and self.SpellCN==obj.SpellCN 

	def deepcopy(self):
		import random
		wgt = [self.myHeroH,-self.hisHeroH,self.myCharA,self.myCharH,\
		self.myTauntCharH,-self.hisCharA,-self.hisCharH,-self.hisTauntCharH,\
		self.MinionCH,self.SpellCN]
		return StatusWeight(wgt)

	def deepcopyAndPerturb(self):
		import random
		wgt = [self.myHeroH,-self.hisHeroH,self.myCharA,self.myCharH,\
		self.myTauntCharH,-self.hisCharA,-self.hisCharH,-self.hisTauntCharH,\
		self.MinionCH,self.SpellCN]
		plus = random.randint(0,9)
		wgt[plus] += 1
		minus = random.randint(0,9)
		wgt[minus] -= 1
		if wgt[minus]<1 :
			wgt[minus]=1
		plus = random.randint(0,9)
		wgt[plus] += 1
		minus = random.randint(0,9)
		wgt[minus] -= 1
		if wgt[minus]<1 :
			wgt[minus]=1
		plus = random.randint(0,9)
		wgt[plus] += 1
		minus = random.randint(0,9)
		wgt[minus] -= 1
		if wgt[minus]<1 :
			wgt[minus]=1
		return StatusWeight(wgt)

	def get_status(self, game: Game):
		my = game.current_player
		his = game.current_player.opponent
		self.myHeroH = my.hero.health
		self.hisHeroH = his.hero.health
		self.myCharA = 0
		self.myCharH = 0
		self.myTauntCharH = 0
		for char in my.characters:
			self.myCharA += char.atk
			self.myCharH += char.health
			if char.taunt:
				self.myTauntCharH += char.health
		self.hisCharA = 0
		self.hisCharH = 0
		self.hisTauntCharH = 0
		for char in his.characters:
			self.hisCharA += char.atk
			self.hisCharH += char.health
			if char.taunt:
				self.hisTauntCharH += char.health
		self.MinionCH = 0#手持ちのミニョンカードのHPの総和
		self.SpellCN = 0#手持ちのスペルカードの枚数
		for card in my.hand:
			if card.type == CardType.MINION:
				self.MinionCH += card.health
			if card.type == CardType.SPELL:
				self.SpellCN += 1

