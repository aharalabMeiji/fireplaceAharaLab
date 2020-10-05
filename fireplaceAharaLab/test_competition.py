from hearthstone.enums import CardClass,BlockType, CardType ,PlayState, State
from enum import IntEnum
from fireplace.game import Game
from fireplace.exceptions import GameOver
import copy
from utils import *



# play_facehunterGames()にしよう！
def play_MechaHunterGames(P1: Agent, P2: Agent, gameNumber=15, debugLog=True): # 属性チェック
	if P1.myClass != CardClass.HUNTER or P2.myClass != CardClass.HUNTER:
		print("In MechaHunterGames, Player is expected to be of HUNTER.")
	if debugLog:
		print(" %r (%s) vs.  %r (%s)"%(P1.name, P1.myClass, P2.name, P2.myClass)) #　対戦者の表示
	Count1 = 0
	Count2 = 0
	
	for i in range(gameNumber): # gameNumber:繰り返し対戦数
		winner = play_one_game(P1,P2,deck1=BigDeck.MechaHunter, deck2=BigDeck.MechaHunter,debugLog=debugLog) # 対戦 deck1とdeck2をfaceHunterに
		print("winner is %r"%winner)
		if winner == P1.name:
			Count1+=1
		elif winner == P2.name:
			Count2+=1
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
		return "{card}->{type}(target={target})".format(card=self.card,type=str(self.type),target=self.target)
		pass

	def __eq__(self,obj):
		return str(self)==str(obj)
		pass
	def clearScore(self):
		self.score = 0


#
##  getActionCandidates : utils version
##
def getCandidates(mygame,_smartCombat=True,_includeTurnEnd=False):
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
								myCandidate.append(Candidate(card, card2=card2, type=BlockType.PLAY, target=target))
						else:
							myCandidate.append(Candidate(card, card2=card2, type=BlockType.PLAY, target=None))
			else:# card2=None
				if card.requires_target():
					for target in card.targets:
						myCandidate.append(Candidate(card, type=BlockType.PLAY, target=target))
				else:
					myCandidate.append(Candidate(card, type=BlockType.PLAY, target=None))
	for character in player.characters:
		if character.can_attack():
			for target in character.targets:
				if character.can_attack(target):
					myH=character.health
					hisA=target.atk
					if (myH > hisA) or (not _smartCombat):
						myCandidate.append(Candidate(character, type=BlockType.ATTACK, target=target))
	if _includeTurnEnd:
		#この選択肢は「何もしない」選択肢ですが、
		#ターンを終了することはできないので、
		#エージェントの方でターンを終了してあげてください
		myCandidate.append(Candidate(None,type=ExceptionPlay.TURNEND))
		pass
	return myCandidate
#
#  executeAction
#
def executeAction(mygame,action: Candidate, debugLog=True):
	"""　"""
	if action.type ==ExceptionPlay.TURNEND:
		return ExceptionPlay.TURNEND
		pass
	player=mygame.current_player
	thisEntities= mygame.entities + mygame.hands
	if debugLog:
		print("%s %s"%(player,str(action)))
	theCard=theTarget=None
	#print(id(action.card.game))
	#print(id(mygame))
	if action.card.game==mygame:
		theCard=action.card
	if action.card2!=None and action.card2.game==mygame:
		theCard2=None
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
	if action.type==BlockType.PLAY:
		if (theTarget != None and theTarget not in theCard.targets):
			return ExceptionPlay.INVALID
		if not theCard.is_playable():
			return ExceptionPlay.INVALID
		try:
			theCard.play(target=theTarget)
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
	return ExceptionPlay.INVALID

class ExceptionPlay(IntEnum):
	""" """
	VALID=0
	GAMEOVER=1
	INVALID=2
	TURNEND=3

def weight_deepcopy_and_perturb(weight):
	import random
	wgt=[]
	for i in range(len(weight)):
		wgt.append(weight[i])
	plus = random.randint(0,len(weight)-1)
	wgt[plus] += 3
	minus = random.randint(0,len(weight)-1)
	wgt[minus] -= 3
	if wgt[minus]<1 :
		wgt[minus]=1
	return wgt

class BigDeck:
	testHunter = ['EX1_611','BT_203','EX1_536','EX1_539','NEW1_031',\
		'SCH_617','SCH_312','SCH_231','SCH_600','DRG_252',\
		'ULD_152','SCH_142','DRG_256','DAL_604','BOT_251',\
		'BOT_251','BOT_700','EX1_556','EX1_556','BOT_532',\
		'BOT_532','BOT_312','BOT_312','BOT_563','BOT_563',\
		'BOT_548','EX1_116','BOT_107','BOT_107','BOT_034']
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


