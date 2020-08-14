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

class StatusWeight(object):
	"""
	Status Weight for my agent
	"""
	def __init__(self, w: list):#正の数からなる長さ＊＊＊のlist
		self.myHeroH = w[0]#自ヒーローのHP
		self.hisHeroH = -w[1]#相手ヒーローのHP
		self.myCharA = w[2]#自分のフィールドにあるミニョンの攻撃力の総和
		self.myCharH = w[3]#自分のフィールドにあるミニョンのHPの総和
		self.myTauntCharH = w[4]#自分のフィールドにある挑発ミニョンのHPの総和
		self.hisCharA = -w[5]#相手のフィールドにあるミニョンの攻撃力の総和
		self.hisCharH = -w[6]#相手のフィールドにあるミニョンのHPの総和
		self.hisTauntCharH = -w[7]#相手のフィールドにある挑発ミニョンのHPの総和
		self.MinionCH = w[8]#手持ちのミニョンのカードのHPの総和
		self.SpellCN = w[9]#手持ちの呪文のカードの枚数


	def __str__(self):
		myText =  ''+str(self.myHeroH)+','
		myText += str(-self.hisHeroH)+','
		myText += str(self.myCharA)+','
		myText += str(self.myCharH)+','
		myText += str(self.myTauntCharH)+','
		myText += str(-self.hisCharA)+','
		myText += str(-self.hisCharH)+','
		myText += str(-self.hisTauntCharH)+','
		myText += str(-self.MinionCH)+','
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

#class StanderdStrategy(IntEnum):
#	
#	standard strategy
#	
#	INVALID = 0
#	ATTACKxMINION = 1
#	ATTACKxSPELL = 2
#	HEALxMINION = 3
#	HEALxHERO = 4
#	BLOCKxHERO = 5
#	STRENGTHENxMINION = 6
#	pass
