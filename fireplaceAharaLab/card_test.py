from hearthstone.enums import CardClass,BlockType, CardType ,PlayState, State
from fireplace.game import Game
from fireplace.card import Card
from fireplace.actions import *
import random
from agent_Standard import *


class DummyAgent(Agent):
	def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000 ):
		super().__init__(myName, myFunction, myOption, myClass, rating )
		pass

	def DummyAI(self, thisgame: ".game.Game", option=[], gameLog=[], debugLog=False):
		player = thisgame.current_player
		loopCount=0
		##########
		#new_game = deepcopy_game(thisgame, player, 0)
		#candidate1 = getCandidates(thisgame)
		#candidate2 = getCandidates(new_game)
		#compaireCandidates(candidate1, candidate2)
		##########
		while loopCount<20:
			##########
			#debug_board(new_game,thisgame)#
			##########
			loopCount+=1
			myCandidate = getCandidates(thisgame)
			if len(myCandidate)>0:
				myChoice = random.choice(myCandidate)
				##########
				#executeAction(new_game, myChoice, debugLog=debugLog)
				#postAction(new_game.current_player)
				##########
				exc = executeAction(thisgame, myChoice, debugLog=debugLog)
				postAction(player)
				if exc==ExceptionPlay.GAMEOVER:
					##########
					#debug_board(new_game,thisgame)#
					##########
					return ExceptionPlay.GAMEOVER
				else:
					continue
			return ExceptionPlay.VALID


def PresetGame():
	Dummy1=DummyAgent("Dummy1",DummyAgent.DummyAI,myClass=CardClass.DRUID)
	Dummy2=DummyAgent("Dummy2",DummyAgent.DummyAI,myClass=CardClass.WARRIOR)


def ExchangeCard(cards,player):
	Discard(player.hand[0]).trigger(player)
	for _card in cards:
		if _card=='arcane':
			_card=random.choice(['CORE_DS1_185','CORE_BOT_453','CORE_CS2_023','CORE_EX1_287','CORE_EX1_294','BT_002','BT_003','BT_006','BT_021','SCH_235','SCH_270','SCH_352','SCH_353','YOP_019','DMF_057','BAR_541','BAR_539','DED_517','DED_002',])
		if _card=='attackspell':
			_card=random.choice(['SCH_348','SCH_604','BAR_801','BAR_032'])
		if _card=='beast':
			_card=random.choice(['CORE_EX1_531','CORE_EX1_534','CORE_EX1_543','CORE_FP1_011','CORE_ICC_419','NEW1_032','NEW1_033','NEW1_034','CORE_CS2_120','CORE_CS2_203','CORE_EX1_014','CORE_EX1_017','CORE_EX1_028','CORE_EX1_162','CORE_LOOT_125','CS3_037','CORE_KAR_300','BT_717','BT_163t','BT_201','BT_202','BT_210','BT_210t','BT_212','BT_133','SCH_283','SCH_605','SCH_714','SCH_133','SCH_239','SCH_244','SCH_340','SCH_617t','SCH_616','DMF_070','DMF_080','DMF_080t','YOP_035','DMF_083','DMF_083t','DMF_086e','DMF_087','DMF_060','BAR_024','BAR_060t','BAR_065','BAR_743','BAR_745','BAR_030','BAR_031','BAR_034t3','BAR_034t4','BAR_034t5','BAR_035t','BAR_533t','BAR_535','BAR_538','BAR_538t','WC_036','WC_036t1','WC_026','SW_072','SW_075','SW_306','SW_323','SW_455t','SW_458t','SW_463','SW_463t','SW_428t4','SW_429t','SW_431','SW_432t','SW_436','SW_439','SW_439t2','DED_008','DED_515','DED_001a','DED_001at','DED_001b','DED_001bt','DED_001c','DRG_252',])
		if _card=='corrupt':
			_card=random.choice(['DMF_124','DMF_082','DMF_073'])
		if _card=='deathrattle':
			_card=random.choice(['SW_070','CORE_FP1_007','CORE_EX1_012'])
		if _card=='dragon':
			_card=random.choice('CORE_EX1_189','CORE_LOOT_137','CS3_031','CS3_032','CS3_033','CS3_034','CS3_035','CS3_036','EX1_116t','CORE_AT_008','BT_726','SCH_162t','SCH_230','SCH_232','SCH_711','YOP_034','YOP_025','YOP_025t','DMF_528','DREAM_03',)
		if _card=='elemental':
			_card=random.choice(['CORE_AT_092','CORE_EX1_187','CORE_EX1_249','CORE_KAR_036','CORE_UNG_813','CORE_CS2_033','BT_155','BT_155t','BT_735','SCH_143','SCH_245','DMF_044','DMF_062','DMF_190','YOP_021','DMF_100','DMF_100t','DMF_101','DMF_059','BAR_042','BAR_854','BAR_545','SW_111',])
		if _card=='fire':
			_card=random.choice(['CORE_EX1_610','CORE_CS2_029','CORE_CS2_032','SCH_348','DMF_104','BAR_546','SW_107','SW_108','SW_108t','SW_110','SW_462','CORE_EX1_610',])
		if _card=='frost':
			_card=random.choice(['CORE_EX1_611','CORE_EX1_275','CORE_EX1_289','CORE_GIL_801','BT_072','SCH_509','BAR_305','BAR_305t','BAR_305t2','BAR_812','WC_041',])
		if _card=='mech':
			_card=random.choice(['CORE_GVG_085','CORE_GVG_076','CORE_GVG_044'])
		if _card=='murloc':
			_card=random.choice(['BAR_063','BAR_062','WC_030'])
		if _card=='nature':
			_card=random.choice(['CORE_BOT_420','CORE_CS2_009','CORE_CS2_013','CORE_EX1_158','CORE_EX1_164','EX1_164a','EX1_164b','CORE_EX1_169','CORE_EX1_571','BT_128','BT_129','BT_130','BT_132','SCH_333','SCH_427','SCH_612','YOP_015','DMF_058','DMF_732','YOP_026','BAR_533','BAR_536','BAR_549','SW_422','SW_437','DREAM_02','DREAM_04','CORE_EX1_169',])
		if _card=='pirate':
			_card=random.choice(['CS3_022','CORE_NEW1_018','BAR_081'])
		if _card=='rush':
			_card=random.choice(['YOP_031'])
		if _card=='secret':
			_card=random.choice(['DMF_123','CORE_EX1_554','CORE_EX1_611'])
		if _card=='spell':
			_card=random.choice(['BAR_305','BAR_541','BAR_546','WC_041','BAR_542'])
		if _card=='spellpower':
			_card=random.choice(['CORE_CS2_142','CORE_EX1_012','CORE_GVG_109','CS3_001','BT_008t','BT_028','SCH_245','SCH_310','YOP_021','SW_061','CS2_052',])
		if _card=='weapon':
			_card=random.choice(['WC_037','DMF_088'])
		Give(player,_card).trigger(player)

def PresetHands(player1, player2): 
	## add a specific card into the deck
	#PutOnTop(player1,'').trigger(player1)#specific card into deck
	
	#forcedraw some specific cards to debug, 特定のカードを引かせたい場合。
	#ExchangeCard([''],player1)
	#ExchangeCard(['beast'],player2)
	pass

def PresetPlay(player, cardID):
	for card in player.hand:
		if card.id == cardID and card.is_playable():
			card.play(target=None)
