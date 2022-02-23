import random
import copy
from fireplace.exceptions import GameOver, InvalidAction
from fireplace.logging import log
from hearthstone.enums import  CardType, BlockType, Race#
from typing import List
from utils import *
from fireplace.card import Card
from fireplace.game import Game
from itertools import chain
from agent_Standard import StandardVectorAgent, adjust_text_by_spellpower

import tensorflow as tf
from tensorflow import keras
import numpy as np

class HappyCat:
	dict={}
	def add_dict(id1, id2, phase):
		pass

class HappyCatAgent(Agent):
	game = None
	player = None
	braches=[]
	HumanInput = True
	MLmodel1 = keras.Sequential()
	# Human input: if true, shows various candidate and allows us to input by hand.
	def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000 , mulliganStrategy=None):
		super().__init__(myName, myFunction, myOption, myClass, rating, mulliganStrategy=mulliganStrategy )
		self.Vector=StandardVectorAgent("Vector",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.DRUID)
		self.MLmodel2 = tf.keras.models.load_model('fireplaceAharaLab/happyCatData/DWW_model_turn2')
		self.MLmodel3 = keras.models.load_model('fireplaceAharaLab/happyCatData/DWW_model_turn3')
		self.MLmodel4 = keras.models.load_model('fireplaceAharaLab/happyCatData/DWW_model_turn4')
		self.MLmodel5 = keras.models.load_model('fireplaceAharaLab/happyCatData/DWW_model_turn5')
		self.MLmodel6 = keras.models.load_model('fireplaceAharaLab/happyCatData/DWW_model_turn6')
		self.MLmodel7 = keras.models.load_model('fireplaceAharaLab/happyCatData/DWW_model_turn7')
		self.MLmodel8 = keras.models.load_model('fireplaceAharaLab/happyCatData/DWW_model_turn8')
		self.MLmodel9 = keras.models.load_model('fireplaceAharaLab/happyCatData/DWW_model_turn9')
		self.MLmodel10 = keras.models.load_model('fireplaceAharaLab/happyCatData/DWW_model_turn10')
	def HappyCatAI(self, game, option=[], gameLog=[], debugLog=False):
		self.player = game.current_player
		self.game = game
		self.option = self.Vector.option
		for loop in range(20):# loop max
			myCandidate = getCandidates(game, _includeTurnEnd=True)#including 'turnend'
			myChoice = self.MainChoice(game, myCandidate)
			if myChoice.type == ExceptionPlay.TURNEND:#何もしないを選択したとき
				return
			else:
				executeAction(self.game, myChoice, debugLog=debugLog)#選択したものを実行
				postAction(self.player)#後処理
		pass

	def RandomChoice(self, candidate):
		return random.choice(candidate)
	def RandomPlayToTurnEnd(self, game):
		for loop in range(20):
			branches = getCandidates(game)
			branch = self.RandomChoice(branches)
			if branch.type==ExceptionPlay.TURNEND:
				return ExceptionPlay.VALID
			else:
				result = executeAction(game,branch,debugLog=False)
				if result==ExceptionPlay.INVALID:
					return ExceptionPlay.INVALID
				elif result==ExceptionPlay.GAMEOVER:
					return ExceptionPlay.GAMEOVER
				pass
			pass
		pass

	def VectorScore(self, branch):
		score = 0
		if branch.type==ExceptionPlay.TURNEND:
			score = self.Vector.getStageScore(self.game, self.option)
			return score
		#statusVector=self.getStatusVector(self.game)
		tmpGame = fireplace_deepcopy(self.game)
		#tmpGame = copy.deepcopy(self.game)
		result = executeAction(tmpGame, branch, debugLog=False)
		if result==ExceptionPlay.INVALID:
			stop=True
		elif result==ExceptionPlay.GAMEOVER:
			score=100000
		else:
			result = self.RandomPlayToTurnEnd(tmpGame)#ここをもっと賢くしてもよい
			if result == ExceptionPlay.GAMEOVER:
				score = 100000
			else:
				score = self.Vector.getStageScore(tmpGame, self.option)
		return score

	def VectorChoice(self, candidate):
		""" three choices by the vector agent
		"""
		first = [-100000,None]
		second = [-100000,None]
		third = [-100000,None]
		for branch in candidate:
			score = self.VectorScore(branch)
			if first[0]<score:
				third[0]=second[0]
				third[1]=second[1]
				second[0]=first[0]
				second[1]=first[1]
				first[0]=score
				first[1]=branch
			elif second[0]<score:
				third[0]=second[0]
				third[1]=second[1]
				second[0]=score
				second[1]=branch
			elif third[0]<score:
				third[0]=score
				third[1]=branch
			pass
		return first,second,third

	def MainChoice(self, game, candidate):
		if self.HumanInput:
			self.ShowDataForHuman(game)
			self.ShowAnalysis(game, candidate)
			return self.InputByHand(game, candidate)
		if len(myCandidate)>0:
			if myClass==CardClass.HUNTER:
				if hisClass==CardClass.WARRIOR:
					myChoice=HunterWarriorChoice(myCandidate)
				else:
					myChoice=HunterDruidChoice(myCandidate)
			elif myClass==CardClass.WARRIOR:
				if hisClass==CardClass.DRUID:
					myChoice=WarriorDruidChoice(myCandidate)
				else:
					myChoice=WarriorHunterChoice(myCandidate)
			elif myClass==CardClass.DRUID:
				if hisClass==CardClass.HUNTER:
					myChoice=DruidHunterChoice(myCandidate)
				else:
					myChoice=DruidWarriorChoice(myCandidate)
			else:
				myChoice = random.choice(myCandidate)#ランダムに一つ選ぶ
		return myChoice

	def ShowHero(self, character):
		player = character.controller
		print("%s"%character, end='   : ')
		if player.weapon:
			print("(%2d/%2d/%2d+%d)(%s)"%(\
				character.atk,\
				player.weapon.durability,\
				character.health,\
				character.armor,\
				player.weapon.data.name))
		else:
			print("(%2d/%2d+%d)"%(\
				character.atk,\
				character.health,\
				character.armor))
		pass
	def ShowCharacter(self, character):
		player = character.controller
		if character == player.hero:
			self.ShowHero(character)
			return
		print("%s"%character, end='   : ')
		print("(%2d/%2d)"%(character.atk,character.health), end=" ")
		if character._Asphyxia_ == 'asphyxia':
			print("(Now Asphyxia %d)"%(character._sidequest_counter_), end=' ')
		if character.charge:
			print("(charge)", end=" ")
		if character.divine_shield:
			print("(divine_shield)", end=" ")
		if character.dormant>0:
			print("(dormant:%d)"%(character.dormant), end=" ")
		elif character.dormant<0:
			if character._sidequest_counter_>0:
				print("(dormant:%d)"%(character._sidequest_counter_), end=" ")
			else:
				print("(dormant)", end=" ")
		if character.frozen:
			print("(frozen)", end=" ")
		if character.immune:
			print("(immune)", end=" ")
		if character.poisonous:
			print("(poisonous)", end=" ")
		if character.reborn:
			print("(reborn)", end=" ")
		if character.rush:
			print("(rush)", end=" ")
		if character.silenced:
			print("(silenced)", end=" ")
		if character.spellpower>0:
			print("(spellpower:%d)"%(character.spellpower), end=" ")
		if character.stealthed:
			print("(stealthed)", end=" ")
		if character.taunt:
			print("(taunt)", end=" ")
		if character.windfury:
			print("(windfury)", end=" ")
		print("%s"%(adjust_text_by_spellpower(character.data.description, player, character)))

	def ShowDataForHuman(self, game):
		player = game.current_player
		myCandidate = []
		print("========OPPONENT'S PLAYGROUND======")
		for character in player.opponent.characters:
			self.ShowCharacter(character)
		print("========OPPONENT'S SECRETS======")
		for card in player.opponent.secrets:
			if hasattr(card, 'sidequest') or hasattr(card, 'questline'):
				print("%s"%card, end='   : ')
				print("(sidequest %d)"%card._sidequest_counter_, end="")
			else:
				print("****   : ")
		print("========MY PLAYGROUND======")
		for character in player.characters:
			self.ShowCharacter(character)
		print("========MY SECRETS======")
		for card in player.secrets:
			print("%s"%card, end='   : ')
			if hasattr(card, 'sidequest') or hasattr(card, 'questline'):
				print("(sidequest %d)"%card._sidequest_counter_, end="")
			print("%s"%(adjust_text(card.data.description)))
		print("========My HAND======")
		for card in player.hand:
			print("%s"%card, end='   : ')
			if card.data.type == CardType.MINION:
				print("%2d(%2d/%2d)%s"%(card.cost, card.atk, card.health, \
					adjust_text_by_spellpower(card.data.description, player, card)))
			elif card.data.type == CardType.SPELL:
				print("%2d : %s"%(card.cost, \
					adjust_text_by_spellpower(card.data.description, player, card)))
			elif card.data.type == CardType.WEAPON:
				print("%2d(%2d/%2d) : %s"%(card.cost, card.atk, card.durability, \
					adjust_text_by_spellpower(card.data.description, player, card)))
			##
		print("========Your turn : %d/%d mana==(spell damage %d (fire %d))==="%(\
			player.mana,player.max_mana,player.spellpower,player.spellpower_fire))
		myCandidate = getCandidates(game, _includeTurnEnd=True)
		myCount = 0
		for myChoice in myCandidate:
			if myChoice.type == ExceptionPlay.TURNEND:
				print("[%d] ターンを終了する"%(myCount))
				myCount+=1
				continue
			print('[%d]'%myCount, end=' ')
			myCard = myChoice.card
			if myChoice.card2!=None:
				myCard=myChoice.card2
			print("%s(%s)"%(myCard, myCard.id), end='  ')
			if myCard.data.type==CardType.SPELL:#show spell in hand
				print('<%2d> %s'%(\
					myCard.cost, \
					adjust_text_by_spellpower(myCard.data.description, player, myCard)), end=' ')
			elif myCard.data.type==CardType.MINION:
				print('<%2d>(%2d/%2d)'%(myCard.cost, myCard.atk, myCard.health), end=' ')
			elif myCard.data.type==CardType.WEAPON:
				print('<%2d> %s'%(myCard.cost, adjust_text_by_spellpower(myCard.data.description, player, myCard)), end=' ')
			if myChoice.type == ActionType.PLAY:
				print(' PLAYS', end=' ')
			if myChoice.type == ActionType.TRADE:
				print(' TRADES <>', end=' ')
			if myChoice.type == ActionType.ATTACK:
				print(' ATTACKS => ', end=' ')
			if myChoice.type == ActionType.POWER:
				print('<%2d> POWER'%(myCard.cost), end=' ')
			targetCard = myChoice.target
			if targetCard!=None:
				print("%s(%s)"%(targetCard, targetCard.controller.name), end=' ')
				if targetCard.data.type==CardType.MINION:
					print('(%2d/%2d)'%(targetCard.atk,targetCard.health), end=' ')
			myCount += 1
			print('')
			pass
		pass

	def getBest3(self, prob):
		n1=n2=n3=-1
		v1=v2=v3=0.0
		leng=len(prob)
		for n in range(leng):
			v=prob[n]
			if v1<=v:
				n3,v3,n2,v2,n1,v1=n2,v2,n1,v1,n,v
			elif v2<=v:
				n3,v3,n2,v2=n2,v2,n,v
			elif v3<=v:
				n3,v3=n,v
				pass
			pass
		return [n1,n2,n3],[v1,v2,v3]

	def ShowAnalysis(self, game, candidate):
		##analysis by vector
		v1,v2,v3=self.VectorChoice(candidate)
		print("Vector agent candidates:")
		print("%s(%d)"%(v1[1],v1[0]))
		print("%s(%d)"%(v2[1],v2[0]))
		print("%s(%d)"%(v3[1],v3[0]))
		svec = self.getStatusVector(game)
		#print(game.turn)
		##analysis by DW_W_ML
		pred=[]
		another=['MINION','HERO','HEROPOWER','OTHERS','TURNEND']
		if self.player.max_mana == 2:
			pred = self.MLmodel2.predict([svec])
		elif self.player.max_mana == 3:
			pred = self.MLmodel3.predict([svec])
		elif self.player.max_mana == 4:
			pred = self.MLmodel4.predict([svec])
		elif self.player.max_mana == 5:
			pred = self.MLmodel5.predict([svec])
		elif self.player.max_mana == 6:
			pred = self.MLmodel6.predict([svec])
		elif self.player.max_mana == 7:
			pred = self.MLmodel7.predict([svec])
		elif self.player.max_mana == 8:
			pred = self.MLmodel8.predict([svec])
		elif self.player.max_mana == 9:
			pred = self.MLmodel9.predict([svec])
		elif self.player.max_mana >= 10:
			pred = self.MLmodel10.predict([svec])
		if len(pred)>0:
			pred = self.getBest3(pred[0])
			leng = len(self.clownDruidCard)
			for i in range(3):
				if pred[0][i]<leng:
					print("MLwin: %s:%f"%(self.clownDruidCard[pred[0][i]],pred[1][i]))
				else:
					print("MLwin: %s:%f"%(another[pred[0][i]-leng],pred[1][i]))
			print(self.getBest3(pred[0]))
		##analysis by DW_L_ML
		pass
	def InputByHand(self, game, myCandidate):
		while True:
			str = input()
			try:
				inputNum = int(str)
				break;
			except ValueError:
				inputNum = -1
		if len(myCandidate)==0 or inputNum == -1:
			return Candidate(None, type=ExceptionPlay.TURNEND, turn=game.turn)
		if inputNum>=0 and inputNum<len(myCandidate):
			return myCandidate[inputNum]
			if myChoice.type != ExceptionPlay.TURNEND:
				executeAction(game, myChoice)
				postAction(game.current_player)
		pass

	hunterMulligan=[]
	warriorMulligan=[]
	druidMulligan=[]

	def HappyCatMulligan(self, choiceCards):
		if myClass==CardClass.HUNTER:
			pass
		elif myClass==CardClass.WARRIOR:
			pass
		elif myClass==CardClass.DRUID:
			pass
		return []
		pass

	def HappyCatChoice(self, choices):
		if myClass==CardClass.HUNTER:
			pass
		elif myClass==CardClass.WARRIOR:
			pass
		elif myClass==CardClass.DRUID:
			pass
		return random.choice(choices)

	clownDruidCard = [
		'GAME_005',#コイン
		'CORE_EX1_169',#Innervate(練気) (0)
		'SCH_427',#Lightning Bloom(電光刹花) (0)
		'SCH_311',#Animated Broomstick(空飛ぶほうき) (1/1/1)
		'SCH_333',#Nature Studies(自然学の予習) (1)
		'DMF_075',#Guess the Weight(重さ当て) (2)
		'CORE_CS2_013',#Wild Growth(野生の繁茂) (3)
		'BT_130',#Overgrowth(過剰繁殖) (4)
		'BAR_535',#Thickhide Kodo(厚皮のコドー) (4/3/5)
		'SCH_605',#Lake Thresher(湖のスレッシャー) (5/4/6)
		'SCH_616',#Twilight Runner(トワイライトランナー) (5/5/4)
		'DMF_078',#Strongman(怪力男) (7/6/6)
		'SCH_610',#Guardian Animals(守護獣) (8)
		'BAR_042',#Primordial Protector(始原の守護者) (8/6/6)
		'DMF_163',#Carnival Clown(カーニバルのピエロ) (9/4/4)
		'SCH_609',#Survival of the Fittest(適者生存) (10)
		'DMF_188']#Y'Shaarj, the Defiler(背徳の魔手ヤシャラージュ) (10/10/10)
	bigWarriorCard = [
		'GAME_005',#コイン
		'SW_023',#Provoke(煽り立て) (0)spell, tradeable
		'SCH_237',#Athletic Studies(体育学の予習) (1)spell
		'CORE_EX1_410',#Shield Slam(シールドスラム) (1)spell
		'BT_124',#Corsair Cache(海賊の隠し武器) (2)spell
		'DMF_522',#Minefield(地雷原) (2) spell
		'BT_117',#Bladestorm(魔刃嵐) (3)spell
		'SW_094',#Heavy Plate(重装鎧) (3) spell, tradeable
		'BT_781',#Bulwark of Azzinoth(アズィノスの防塁) (3/1/4)weapon
		'BAR_845',#Rancor(遺恨) (4) spell
		'BAR_844',#Outrider's Axe(先導者の斧) (4/3/3)weapon
		'YOP_005',#Barricade(バリケード) (4) spell 
		'CORE_EX1_407',#Brawl(乱闘) (5) spell
		'SW_021',#Cowardly Grunt(腑抜けの兵卒) (6/6/2) 
		'SCH_533',#Commencement(学位授与式) (7)
		'SW_024',#Lothar (ローサー) (7/7/7)
		'SCH_337',#Troublemaker(不良学生) (8/6/8)
		'SW_068',#Mo'arg Forgefiend(モアーグの鍛冶鬼) (8/8/8)
		'SCH_621',]#Rattlegore(ラトルゴア) (9/9/9)
	faceHunterCard = [
		'GAME_005',#コイン
		'SCH_617',#Adorable Infestation(カワイイ侵入者) (1)
		'SCH_600',#Demon Companion(悪魔の相棒) (1)
		'SCH_231',#Intrepid Initiate(図太い徒弟) (1/1/2)
		'CORE_DS1_184',#Tracking(追跡術) (1)
		'SCH_279',#Trueaim Crescent(トゥルーエイム・クレセント) (1/1/4) weapon
		'SCH_133',#Wolpertinger(ヴォルパーティンガー) (1/1/1)
		'BAR_801',#Wound Prey(獲物の傷) (1)
		'SCH_713',#Cult Neophyte(教団の新入会員) (2/3/2)
		'BT_211',#Imprisoned Felmaw(封印されしフェルモー) (2/5/4)
		'CORE_BRM_013',#Quick Shot(速射の一矢) (2)
		'SW_321',#Aimed Shot(狙い撃ち) (3)
		'BAR_721',#Mankrik(マンクリック) (3/3/4)
		'BAR_032',#Piercing Shot(貫通弾) (4)
		'DMF_088',#Rinling's Rifle(リンリングのライフル) (4/2/2) weapon
		'BAR_037',#Warsong Wrangler(ウォーソングの獣飼育者) (4/3/4)
		'BAR_551',#Barak Kodobane(バラク・コドーベイン) (5/3/5)
		'DMF_087',]#Trampling Rhino(踏み潰すサイ) (5/5/5)
	def DruidHunterChoice(myCandidate):
		return random.choice(myCandidate)
	def DruidWarriorChoice(myCandidate):
		return random.choice(myCandidate)

	def HunterDruidChoice(myCandidate):
		return random.choice(myCandidate)
	def HunterWarriorChoice(myCandidate):
		return random.choice(myCandidate)

	def WarriorDruidChoice(myCandidate):
		return random.choice(myCandidate)
	def WarriorHunterChoice(myCandidate):
		return random.choice(myCandidate)
	def gameStatus(self,my):
		Manas=[
			[1,0,0,0,0,0,0,0,0,0,0,],
			[1,1,0,0,0,0,0,0,0,0,0,],
			[1,1,1,0,0,0,0,0,0,0,0,],
			[0,1,1,1,0,0,0,0,0,0,0,],
			[0,0,1,1,1,0,0,0,0,0,0,],
			[0,0,0,1,1,1,0,0,0,0,0,],
			[0,0,0,0,1,1,1,0,0,0,0,],
			[0,0,0,0,0,1,1,1,0,0,0,],
			[0,0,0,0,0,0,1,1,1,0,0,],
			[0,0,0,0,0,0,0,1,1,1,0,],
			[0,0,0,0,0,0,0,0,1,1,1,],
			[0,0,0,0,0,0,0,0,0,1,1,],
			]
		if my.max_mana<=10:
			myMMana=Manas[my.max_mana]
		else:
			myMMana=Manas[11]
		if my.mana<=10:
			myMana=Manas[my.mana]
		else:
			myMana=Manas[11]
		return myMMana+myMana
	#def vectorize(self,value,level,step):
	#	w=[]
	#	for i in range(level+1):
	#		w.append(0)
	#	t=int(value/step)
	#	if t>level:
	#		t=level
	#	w[t]=1
	#	return w
	def heroes(self,my,his):
		#myHeroH = self.vectorize(my.hero.health+my.hero.armor,5,6)
		#hisHeroH = self.vectorize(his.hero.health+his.hero.armor,5,6)
		#myHeroA = self.vectorize(my.hero.atk+1,3,2)
		#hisHeroA = self.vectorize(his.hero.atk+1,3,2)
		#return myHeroH+myHeroA+hisHeroH+hisHeroA
		myHeroH = my.hero.health+my.hero.armor
		hisHeroH = his.hero.health+his.hero.armor
		myHeroA = my.hero.atk
		hisHeroA = his.hero.atk
		return [myHeroH,myHeroA,hisHeroH,hisHeroA]
	def myField(self, my):
		myCharH = 0
		myCharA = 0
		myTauntCharH = 0
		myTauntCharA = 0
		myShieldCharA = 0
		myRebornCharA = 0
		for minion in my.field:
			myCharH += minion.health
			myCharA += minion.atk
			if minion.taunt:
				myTauntCharH += minion.health
				myTauntCharA += minion.atk
			if minion.divine_shield:
				myShieldCharA += minion.atk
			if minion.reborn:
				myRebornCharA += minion.atk
		#myCharH = self.vectorize(myCharH+2,5,3)
		#myCharA = self.vectorize(myCharA+2,5,3)
		#myTauntCharH = self.vectorize(myTauntCharH+2,4,3)
		#myTauntCharA = self.vectorize(myTauntCharA+1,4,2)
		#myShieldCharA = self.vectorize(myShieldCharA+1,4,2)
		#myRebornCharA = self.vectorize(myRebornCharA+1,4,2)
		#return myCharH+myCharA+myTauntCharH+myTauntCharA+myShieldCharA+myRebornCharA
		return [myCharH,myCharA,myTauntCharH,myTauntCharA,myShieldCharA,myRebornCharA]
	def hisField(self, his):
		hisCharH = 0
		hisCharA = 0
		hisTauntCharH = 0
		hisTauntCharA = 0
		for minion in his.field:
			hisCharH += minion.health
			hisCharA += minion.atk
			if minion.taunt:
				hisTauntCharH += minion.health
				hisTauntCharA += minion.atk
		#hisCharH = self.vectorize(hisCharH+2,5,3)
		#hisCharA = self.vectorize(hisCharA+2,5,3)
		#hisTauntCharH = self.vectorize(hisTauntCharH+2,4,3)
		#hisTauntCharA = self.vectorize(hisTauntCharA+1,4,2)
		#return hisCharH+hisCharA+hisTauntCharH+hisTauntCharA
		return [hisCharH,hisCharA,hisTauntCharH,hisTauntCharA]
	def myHand(self,my):
		MinionCH = 0#手持ちのミニョンカードのHPの総和
		PlayableMinionCH = 0#手持ちのミニョンカードのHPの総和
		MinionCN = 0#手持ちのミニョンカードの枚数
		PlayableMinionCN = 0#手持ちのミニョンカードの枚数
		SpellCN = 0#手持ちのスペルカードの枚数
		PlayableSpellCN = 0#手持ちのスペルカードの枚数
		for card in my.hand:
			if card.type == CardType.MINION:
				MinionCH += card.health
				MinionCN += 1
				if card.is_playable():
					PlayableMinionCH += card.health
					PlayableMinionCN += 1
			if card.type == CardType.SPELL:
				SpellCN += 1
				if card.is_playable():
					PlayableSpellCN += 1
		#MinionCH=self.vectorize(MinionCH+2,5,3)
		#PlayableMinionCH=self.vectorize(PlayableMinionCH+2,5,3)
		#MinionCN=self.vectorize(MinionCN,5,1)
		#PlayableMinionCN=self.vectorize(PlayableMinionCN,5,1)
		#SpellCN=self.vectorize(SpellCN,5,1)
		#PlayableSpellCN=self.vectorize(PlayableSpellCN,5,1)
		#return MinionCH+MinionCN+PlayableMinionCH+PlayableMinionCN+SpellCN+PlayableSpellCN
		return [MinionCH,MinionCN,PlayableMinionCH,PlayableMinionCN,SpellCN,PlayableSpellCN]
	def myHandCard(self, my, myClass):
		if myClass==CardClass.DRUID:
			cardList=self.clownDruidCard
		elif myClass==CardClass.WARRIOR:
			cardList=self.bigWarriorCard
		else:#CardClass.HUNTER
			cardList=self.faceHunterCard
		lenCardList=len(cardList)
		handCardList=[0]*(lenCardList+3)
		for card in my.hand:
			another=True
			for i in range(lenCardList):
				if card.id==cardList[i]:
					handCardList[i] = 1
					another=False
					break
			if another:
				if card.type==CardType.MINION:
					handCardList[lenCardList] = 1
				elif card.type==CardType.SPELL:
					handCardList[lenCardList+1] = 1
				else:
					handCardList[lenCardList+2] = 1
		return handCardList
	def myFieldCard(self, my, myClass):
		if myClass==CardClass.DRUID:
			cardList=self.clownDruidCard
		elif myClass==CardClass.WARRIOR:
			cardList=self.bigWarriorCard
		else:#CardClass.HUNTER
			cardList=self.faceHunterCard
		lenCardList=len(cardList)
		fieldCardList=[0]*(lenCardList+3)
		for card in my.field:
			another=True
			for i in range(lenCardList):
				if not card.asleep and card.id==cardList[i]:
					fieldCardList[i] = 1
					another=False
					break
			if another and not card.asleep:
				if card.type==CardType.MINION:
					fieldCardList[lenCardList] = 1
				elif card.type==CardType.SPELL:
					fieldCardList[lenCardList+1] = 1
				else:
					fieldCardList[lenCardList+2] = 1
		return fieldCardList
	def getStatusVector(self, game):
		my = game.current_player
		his = game.current_player.opponent
		ret = self.gameStatus(my)\
			+self.heroes(my,his)\
			+self.myField(my)\
			+self.hisField(his)\
			+self.myHand(my)\
			+self.myHandCard(my, my.hero.card_class)\
			+self.myFieldCard(my, my.hero.card_class)
		return ret

	def getActionVector(self, candidate, myClass):
		card=-1
		target=-1
		another=True
		if myClass==CardClass.DRUID:
			cardList=self.clownDruidCard
		elif myClass==CardClass.WARRIOR:
			cardList=self.bigWarriorCard
		else:#CardClass.HUNTER
			cardList=self.faceHunterCard
		for i in range(len(cardList)):
			cardID=cardList[i]
			if candidate.card!=None and candidate.card!=None and cardID==candidate.card.id:
				card=i
				another=False
				break
		if another:
			if candidate.type ==ExceptionPlay.TURNEND:
				card = len(cardList)+4
			elif candidate.card.type==CardType.MINION:
				card = len(cardList)
			elif candidate.card.type==CardType.HERO:
				card = len(cardList)+1
			elif candidate.type==CardType.HERO_POWER:
				card = len(cardList)+2
			else: 
				card = len(cardList)+3
		if candidate.target==None:
			target=0
		elif candidate.target.type==CardType.HERO:
			target=1
		else:
			target=2
		return card,target
