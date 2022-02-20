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

class HappyCat:
	dict={}
	def add_dict(id1, id2, phase):
		pass

class HappyCatAgent(Agent):
	game = None
	player = None
	option=[]
	HumanInput = True
	# Human input: if true, shows various candidate and allows us to input by hand.
	def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000 , mulliganStrategy=None):
		super().__init__(myName, myFunction, myOption, myClass, rating, mulliganStrategy=mulliganStrategy )
	def HappyCatAI(self, game, option=[], gameLog=[], debugLog=False):
		self.player = game.current_player
		self.game = game
		self.option = option
		for loop in range(20):# loop max
			myCandidate = getCandidates(game, _includeTurnEnd=True)#including 'turnend'
			myChoice = self.MainChoice(myCandidate)
			if myChoice.type == ExceptionPlay.TURNEND:#何もしないを選択したとき
				return
			else:
				executeAction(game, myChoice, debugLog=debugLog)#選択したものを実行
				postAction(player)#後処理
		pass

	def RandomChoice(self, candidate):
		return random.choice(candidate)
	def RandomPlayToTuenEnd(game):
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
			score = self.getStageScore(tmpGame, self.option)
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
				score = self.getStageScore(tmpGame, self.option)
		return score
	def VectorChoice(self, candidate):
		first = [-1,None]
		#second = [-1,None]
		#third = [-1,None]
		for branch in candidate:
			score = self.VectorScore(branch)
			if first[0]<score:
				first[0]=score
				first[1]=branch
			pass
		pass

	def MainChoice(self, game, candidate):
		if self.HumanInput:
			self.ShowDataForHuman(game)
			self.ShowAnalysis(game)
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
				player.weapon.data.name\
				), end=" ")
		else:
			print("(%2d/%2d+%d)"%(\
				character.atk,\
				character.health,\
				character.armor), end=" ")
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
				continue
			print('[%d]'%myCount, end=' ')
			myCard = myChoice.card
			print("%s"%myCard, end='  ')
			if myChoice.card2!=None:
				print("(%s)"%myChoice.card2, end=' ')
			if myCard.data.type==CardType.SPELL:#show spell in hand
				print('<%2d> %s'%(\
					myCard.cost, \
					adjust_text_by_spellpower(myChoice.card2.data.description, player, myCard)), end=' ')
			elif myCard.data.type==CardType.MINION:
				print('<%2d>(%2d/%2d)'%(myCard.cost, myCard.atk, myCard.health), end=' ')
			elif myCard.data.type==CardType.WEAPON:
				print('<%2d> %s'%(myCard.cost, adjust_text_by_spellpower(myCard.data.description, player, myCard)), end=' ')
			if myChoice.type == ActionType.PLAY:
				print(' PLAYS', end=' ')
			if myChoice.type == ActionType.TRADE:
				print(' TRADES', end=' ')
			if myChoice.type == ActionType.ATTACK:
				print(' ATTACKS', end=' ')
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

	def ShowAnalysis(self,game):
		##analysis by vector
		vectorChoices=self.VectorKernel(game)
		print("Vector agent candidates:")
		for choice in vectorChoices:
			print("  %s"%(choice))
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
	def heroes(self,my,his):
		myHeroH = my.hero.health
		hisHeroH = his.hero.health
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
			if minion.devine_shield:
				myShieldCharA += minion.atk
			if minion.reborn:
				myRebornCharA += minion.atk
		return [myCharH,myCharA,myTauntCharH,myTauntCharA,myShieldCharA,myRebornCharA]
	def hisField(self, his):
		hisCharH = 0
		hisCharA = 0
		hisTauntCharH = 0
		hisTauntCharA = 0
		for minion in his.field:
			hisCharH += minion.health
			hisCharA += minion.atk
			if chminionar.taunt:
				hisTauntCharH += minion.health
				hisTauntCharA += chminionar.atk
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
		return [MinionCH,MinionCN,PlayableMinionCH,PlayableMinionCN,SpellCN,PlayableSpellCN]
	def getStatusVector(self, game):
		my = game.current_player
		his = game.current_player.opponent
		return self.gameStatus(my)+self.heroes(my,his)+self.myField(my)+self.hisField(his)+self.myHand(my)

	def getActionVector(self, candidate):
		#druid
		card=[]
		another=True
		for cardID in self.clownDruidCard:
			if cardID==candidate.card.id:
				card.append(1)
				another=False
			else:
				card.append(0)
		if another:
			card.append(1)
		else:
			card.append(0)
		target=[]
		if target==None:
			target=[1,0,0]
		elif target.type==CardType.HERO:
			target=[0,1,0]
		else:
			target=[0,0,1]
		return card+target
