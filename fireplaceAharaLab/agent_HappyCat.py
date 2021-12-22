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
		'SW_023',#Provoke(0)spell, tradeable
		'SCH_237','SCH_237',#Athletic Studies(1)spell
		'CORE_EX1_410','CORE_EX1_410',#Shield Slam(1)spell
		'BT_124',#Corsair Cache (2)spell
		'DMF_522','DMF_522',#Minefield(2) spell
		'BT_117','BT_117',#Bladestorm(3)spell
		'SW_094','SW_094',#Heavy Plate(3) spell, tradeable
		'BT_781',#Bulwark of Azzinoth(3/1/4)weapon
		'BAR_845','BAR_845',#Rancor(4) spell
		'BAR_844',#Outrider's Axe(4/3/3)weapon
		'YOP_005','YOP_005',#Barricade(4) spell 
		'CORE_EX1_407','CORE_EX1_407',#Brawl(5) spell
		'SW_021','SW_021',#Cowardly Grunt(6/6/2) 
		'SCH_533','SCH_533',#Commencement(7)
		'SW_024',#Lothar (7/7/7)
		'SCH_337','SCH_337',#Troublemaker(8/6/8)
		#'SCH_337t', #Ruffian(3/3/3)
		'SW_068','SW_068',#Mo'arg Forgefiend(8/8/8)
		'SCH_621',]#Rattlegore(9/9/9)
	def WarriorDruidChoice(myCandidate):
		pass
	def WarriorHunterChoice(myCandidate):
		pass
