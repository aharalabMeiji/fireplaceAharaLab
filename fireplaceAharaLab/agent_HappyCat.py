import random
import copy
from fireplace.exceptions import GameOver, InvalidAction
from fireplace.logging import log
from hearthstone.enums import  CardType, BlockType, Race#
from typing import List
from utils import *
from fireplace.card import Card
from fireplace.game import Game

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
		'CORE_EX1_169','CORE_EX1_169',
		'SCH_427','SCH_427',
		'SCH_311','SCH_311',
		'SCH_333','SCH_333',
		'DMF_075','DMF_075',
		'CORE_CS2_013','CORE_CS2_013',
		'BT_130','BT_130',
		'BAR_535',
		'SCH_605','SCH_605',
		'SCH_616','SCH_616',
		'DMF_078','DMF_078',
		'SCH_610','SCH_610',
		'BAR_042','BAR_042',
		'DMF_163','DMF_163',
		'SCH_609','SCH_609',
		'DMF_188']
	def DruidHunterChoice(myCandidate):
		pass
	def DruidWarriorChoice(myCandidate):
		pass

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
		pass
	def HunterWarriorChoice(myCandidate):
		pass

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
		pass
	def WarriorHunterChoice(myCandidate):
		pass


	def getVector(game):
		ret=[]
		my = game.current_player
		his = game.current_player.opponent
		turn=game.turn
		myMMana=my.max_mana
		myMana=my.mana
		gameStatus=[turn,myMMana,myMana]
		myHeroH = my.hero.health
		hisHeroH = his.hero.health
		myHeroA = my.hero.atk
		hisHeroA = his.hero.atk
		heroV=[myHeroH,myHeroA,hisHeroH,hisHeroA]
		myCharH = 0
		myCharA = 0
		myTauntCharH = 0
		myTauntCharA = 0
		for minion in my.field:
			myCharH += minion.health
			myCharA += minion.atk
			if minion.taunt:
				myTauntCharH += minion.health
				myTauntCharA += minion.atk
		myField=[myCharH,myCharA,myTauntCharH,myTauntCharA]
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
		hisField=[hisCharH,hisCharA,hisTauntCharH,hisTauntCharA]
