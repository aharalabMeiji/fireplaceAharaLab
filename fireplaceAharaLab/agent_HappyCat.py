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
	def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000 , mulliganStrategy=None):
		super().__init__(myName, myFunction, myOption, myClass, rating, mulliganStrategy=mulliganStrategy )
	def HappyCatAI(self, game, option=[], gameLog=[], debugLog=False):
		player = game.current_player
		while True:
			myVector = self.getStatusVector(game)
			myCandidate = getCandidates(game)#実行できることがらをリストで取得
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
				if myChoice.type ==ExceptionPlay.TURNEND:#何もしないを選択したとき
					return
				executeAction(game, myChoice, debugLog=debugLog)#選択したものを実行
				postAction(player)#後処理
			else:
				return
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

	clownDruid = [
	'CORE_EX1_169','CORE_EX1_169',#Innervate(練気) (0)
	'SCH_427','SCH_427',#Lightning Bloom(電光刹花) (0)
	'SCH_311','SCH_311',#Animated Broomstick(空飛ぶほうき) (1/1/1)
	'SCH_333','SCH_333',#Nature Studies(自然学の予習) (1)
	'DMF_075','DMF_075',#Guess the Weight(重さ当て) (2)
	'CORE_CS2_013','CORE_CS2_013',#Wild Growth(野生の繁茂) (3)
	'BT_130','BT_130',#Overgrowth(過剰繁殖) (4)
	'BAR_535',#Thickhide Kodo(厚皮のコドー) (4/3/5)
	'SCH_605','SCH_605',#Lake Thresher(湖のスレッシャー) (5/4/6)
	'SCH_616','SCH_616',#Twilight Runner(トワイライトランナー) (5/5/4)
	'DMF_078','DMF_078',#Strongman(怪力男) (7/6/6)
	'SCH_610','SCH_610',#Guardian Animals(守護獣) (8)
	'BAR_042','BAR_042',#Primordial Protector(始原の守護者) (8/6/6)
	'DMF_163','DMF_163',#Carnival Clown(カーニバルのピエロ) (9/4/4)
	'SCH_609','SCH_609',#Survival of the Fittest(適者生存) (10)
	'DMF_188']#Y'Shaarj, the Defiler(背徳の魔手ヤシャラージュ) (10/10/10)
	clownDruidCard = [
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
	def DruidHunterChoice(myCandidate):
		return random.choice(myCandidate)
	def DruidWarriorChoice(myCandidate):
		return random.choice(myCandidate)

	faceHunter = [
		'SCH_617','SCH_617',
		'SCH_600','SCH_600',
		'SCH_231','SCH_231',
		'CORE_DS1_184','CORE_DS1_184',
		'SCH_279',
		'SCH_133','SCH_133',
		'BAR_801','BAR_801',
		'SCH_713','SCH_713',
		'BT_211','BT_211',
		'CORE_BRM_013','CORE_BRM_013',
		'SW_321','SW_321',
		'BAR_721',
		'BAR_032','BAR_032',
		'DMF_088',
		'BAR_037','BAR_037',
		'BAR_551',
		'DMF_087','DMF_087',]	
	def HunterDruidChoice(myCandidate):
		return random.choice(myCandidate)
	def HunterWarriorChoice(myCandidate):
		return random.choice(myCandidate)

	bigWarrior = [
		'SW_023',#Provoke(煽り立て) (0)spell, tradeable
		'SCH_237','SCH_237',#Athletic Studies(体育学の予習) (1)spell
		'CORE_EX1_410','CORE_EX1_410',#Shield Slam(シールドスラム) (1)spell
		'BT_124',#Corsair Cache(海賊の隠し武器) (2)spell
		'DMF_522','DMF_522',#Minefield(地雷原) (2) spell
		'BT_117','BT_117',#Bladestorm(魔刃嵐) (3)spell
		'SW_094','SW_094',#Heavy Plate(重装鎧) (3) spell, tradeable
		'BT_781',#Bulwark of Azzinoth(アズィノスの防塁) (3/1/4)weapon
		'BAR_845','BAR_845',#Rancor(遺恨) (4) spell
		'BAR_844',#Outrider's Axe(先導者の斧) (4/3/3)weapon
		'YOP_005','YOP_005',#Barricade(バリケード) (4) spell 
		'CORE_EX1_407','CORE_EX1_407',#Brawl(乱闘) (5) spell
		'SW_021','SW_021',#Cowardly Grunt(腑抜けの兵卒) (6/6/2) 
		'SCH_533','SCH_533',#Commencement(学位授与式) (7)
		'SW_024',#Lothar (ローサー) (7/7/7)
		'SCH_337','SCH_337',#Troublemaker(不良学生) (8/6/8)
		'SW_068','SW_068',#Mo'arg Forgefiend(モアーグの鍛冶鬼) (8/8/8)
		'SCH_621',]#Rattlegore(ラトルゴア) (9/9/9)
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
