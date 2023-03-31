import random
import copy
from fireplace.exceptions import GameOver
from hearthstone.enums import CardType, BlockType, CardClass, SpellSchool#
from utils import ExceptionPlay, Candidate, executeAction, getCandidates, postAction,Agent, fireplace_deepcopy
from fireplace.actions import Action
from fireplace.card import Card
from fireplace.game import Game
from fireplace.utils import ActionType
from enum import IntEnum
from fireplace.logging import log

from agent_Standard import *


#-------------------------------------------------------------------#
# GAT2023 �f�b�LAI�R���e�X�g�@�o��ҁ@�������V�i�����F�����ۍ���j  #
# ����f�b�L�̋L�ځi���̃t�@�C���̖`��������j�����                #
# ����G�[�W�F���g�{�́i�f�b�L�L�ڕ�����ȍ~�j���L�ڂ����t�@�C��    #
#-------------------------------------------------------------------#


##==============================================================================================================
##�@***���p���@  How to Use***�@
#    �i�� ������A���̃R�[�h�����g�̌��������Ȃǂɗ��p������Ɍ����āj
##
## 1. ���̃t�@�C���iagent_SatZooLock.py�j���AfireplaceAharaLab�t�H���_��start.py�Ɠ����K�w�ɔz�u
##
## 2. �t�H���_ fireplaceAharaLab ����start.py�@�`���ɁA
#�@   from agent_SatZooLock import *
##    �ƒǋL
##
## 3. ����start.py���ɂāA
#
#�@�@�@�@SatZoo = SatZooAgent("SatZoo", SatZooAgent.StandardStep1\
#			, myOption = []\
#			, myClass = deckSatZoo["class"]
#   		, mulliganStrategy = SatZooAgent.SatZooMulligan)	
#
##�@�@�ƋL���ăG�[�W�F���g�C���X�^���g���쐬
##
## 4. �X�ɂ���ȍ~�̍s��
#     a,b,c = play_set_of_games( *���G�[�W�F���g*, SatZoo, deck1=*���f�b�L*, deck2=deckSatZoo["deck"], gameNumber=4, debugLog=True)
#�@�@�܂���
#     a,b,c = play_set_of_games( SatZoo, *���G�[�W�F���g*, deck1=deckSatZoo["deck"], deck2=*���f�b�L*, gameNumber=4, debugLog=True)
#�@�@���ƋL�ڂ��邱�Ƃőΐ�\
##==============================================================================================================



#
#�@����f�b�L�L�ڕ�
# �@�@�i�q�[���[�F�E�H�[���b�N
#�@�@�@ �f�b�L�^�C�v�F�A�O���D�@���ɂ����g�Y�[�E���b�N�h�f�b�L�j
#
#####################################################################################
deckSatZoo={
		"name":"deckSatZoo",
		"deck":[

		"VAN_EX1_308", "VAN_EX1_308", # ���̉�

		"VAN_CS2_188", "VAN_CS2_188", #�S�R�� * 2
	    "VAN_EX1_004", "VAN_EX1_004", #�Ⴋ�v���[�X�e�X * 2
		"VAN_EX1_029", "VAN_EX1_029", #���v���m�[�� * 2
		"VAN_EX1_008", "VAN_EX1_008", #�A�[�W�F���g�̏]�R�m * 2

		"VAN_CS2_065", "VAN_CS2_065", #���H�C�h�E�H�[�J�[ * 2
		"VAN_EX1_319", "VAN_EX1_319", #���̃C���v  * 2

		"VAN_EX1_393",  "VAN_EX1_393" , #�A�}�j�̋���m * 2
		"VAN_NEW1_019", "VAN_NEW1_019", #�i�C�t�W���O���[ * 2 
		"VAN_EX1_058",  "VAN_EX1_058" , #�T���t���[���[�̌�q * 2

		"VAN_EX1_019", "VAN_EX1_019", #�V���^�[�h�̐��E�� * 2
		"VAN_CS2_125", "VAN_CS2_125", #�S�т̃O���Y���[ * 2

		"VAN_EX1_313", "VAN_EX1_313", #�s�b�g���[�h * 2
		"VAN_EX1_046", "VAN_EX1_046", #�_�[�N�A�C�A���h���[�t * 2

		"VAN_EX1_310", "VAN_EX1_310", #�h�D�[���K�[�h * 2
		 
		],
		"class":CardClass.WARLOCK}




#
#�@�@�G�[�W�F���g�̖{�̃R�[�h�L�ڕ�
#
#
#####################################################################################
class SatZooAgent(Agent):
	
	def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000, mulliganStrategy=None):
		super().__init__(myName, myFunction, myOption, myClass, rating, mulliganStrategy=mulliganStrategy )
		self.__standard_agent__=StandardAgent("SatZoo",StandardAgent.StandardRandom, myClass=myClass)
		pass

	
	###################################################################
	##�@�y�}���K���p�֐��z
	##
	##�@�@����A�O���E�H�[���b�N�f�b�L�p�ɁC�q���[���X�e�B�b�N�œ���D
	##
	##�@  @param choiceCards - �ŏ��ɔz��ꂽ��D���Acard�^�C���X�^���X�̃��X�g�Ɋi�[
	##�@�@@return �Ԃ�l�Ȃ�
	###################################################################
	def SatZooMulligan(self, choiceCards):

		mulliganDebug = False #True�ɂ���Ɠr���o�߂�\������
		if mulliganDebug: print("%s mulligan turn has began."%(self.name))
		cards_to_mulligan = []
		
		#
		# 1. �e��t���O�̃Z�b�g
		#########################
		go_first = True

		exist_flameImp = False
		exist_soulFire = False
		exist_2drop = False
		exist_1drop = False
		exist_repla = False
		exist_ugent = False
		exist_knife = False
		exist_amani = False
		exist_voidw = False

		num_flameImp = 0
		num_soulFire = 0
		num_2drop = 0
		num_1drop = 0
		num_repla = 0
		num_ugent  = 0
		num_knife = 0
		num_amani = 0
		num_voidw = 0

		if len(choiceCards) == 4:
			go_first  = False

		for card in choiceCards:
			
			if card.id == 'VAN_EX1_319': #���̃C���v
				exist_flameImp = True
				num_flameImp += 1
				exist_1drop = True
				num_1drop += 1
			if card.id == 'VAN_CS2_065': #���H�C�h�E�H�[�J
				exist_voidw = True
				num_voidw += 1
				exist_1drop = True
				num_1drop += 1
			if card.id == 'VAN_EX1_308': #�\�E���t�@�C���\
				exist_soulFire = True
				num_soulFire += 1
			if card.id == 'VAN_EX1_029': #���v���m�[��
				exist_repla = True
				num_repla += 1
				exist_1drop = True
				num_1drop += 1
			if card.id == 'VAN_EX1_008': #�A�[�W�F���g
				exist_ugent = True
				num_ugent += 1
				exist_1drop = True
				num_1drop += 1
			if card.id == 'VAN_NEW1_019': #�i�C�t�W���O���[
				exist_knife = True
				num_knife += 1
				exist_2drop = True
				num_2drop += 1
			if card.id == 'VAN_EX1_393': #�A�}�j
				exist_amani = True
				num_amani += 1
				exist_2drop = True
				num_2drop += 1
			if card.id == 'VAN_EX1_306': #�t�F���X�g�[�J�[
				exist_2drop = True
				num_2drop += 1
			if card.id == 'VAN_CS2_188' or card.id == 'VAN_EX1_004' : #�S�R���܂��̓v���[�X�e�X
				exist_1drop = True
				num_1drop += 1
		
		#
		# 2-a. ��莞�̃}���K�������@�i1-2-3�̃}�i�J�[�u�𐮂���j
		###########################################################
		if go_first:
			if exist_flameImp:
				if exist_2drop:
					#
					# case [A]
					# Best case malligun. remain a flame imp and a 2 drop minion. And remain 3drop dude, if any.
					############
					ind_remain1dro = -1
					ind_remain2dro = -1
					for ind, card in enumerate(choiceCards):
						if card.id == 'VAN_EX1_319':
							ind_remain1dro = ind
							break
					for ind, card in enumerate(choiceCards):
						if card.cost == 2:
							ind_remain2dro = ind
							break
					for ind, card in enumerate(choiceCards):
						if ind == ind_remain1dro or ind == ind_remain2dro:
							continue
						if card.cost == 3 or card.cost == 0:
							continue
						cards_to_mulligan.append(card)
					if mulliganDebug: print("mullingan list [case A]", cards_to_mulligan)
					return cards_to_mulligan
					
				else: #in case exist flame imp and no 2 drop
					#
					# case [B]
					# Good case malligun. remain a flame imp only
					##########
					ind_remain1dro = -1
					for ind, card in enumerate(choiceCards):
						if card.id == 'VAN_EX1_319':
							ind_remain1dro = ind
							break
					for ind, card in enumerate(choiceCards):
						if ind == ind_remain1dro:
							continue
						cards_to_mulligan.append(card)
					if mulliganDebug: print("mullingan list [case B]", cards_to_mulligan)
					return cards_to_mulligan				
			else: # in case no flame imp 
				if exist_repla:
					#
					# case [C]
					# remain a repla and a 2drop minion if any
					##########
					ind_remain1dro = -1
					ind_remain2dro = -1
					for ind, card in enumerate(choiceCards):
						if card.id == 'VAN_EX1_029':
							ind_remain1dro = ind
							break
					for ind, card in enumerate(choiceCards):
						if card.cost == 2:
							ind_remain2dro = ind
							break
					for ind, card in enumerate(choiceCards):
						if ind == ind_remain1dro or ind == ind_remain2dro:
							continue
						cards_to_mulligan.append(card)
					if mulliganDebug: print("mullingan list [case C]", cards_to_mulligan)
					return cards_to_mulligan				
				elif exist_ugent:
					#
					# case [D]
					# remain an urgent knight and a 2drop minion if any
					##########
					ind_remain1dro = -1
					ind_remain2dro = -1
					for ind, card in enumerate(choiceCards):
						if card.id == 'VAN_EX1_008':
							ind_remain1dro = ind
							break
					for ind, card in enumerate(choiceCards):
						if card.cost == 2:
							ind_remain2dro = ind
							break
					for ind, card in enumerate(choiceCards):
						if ind == ind_remain1dro or ind == ind_remain2dro:
							continue
						cards_to_mulligan.append(card)
					if mulliganDebug: print("mullingan list [case D]", cards_to_mulligan)
					return cards_to_mulligan
				elif exist_voidw:
					#
					# case [d-e]
					# remain a void walker and a 2drop minion if any
					#########
					ind_remain1dro = -1
					ind_remain2dro = -1
					for ind, card in enumerate(choiceCards):
						if card.id == 'VAN_CS2_065':
							ind_remain1dro = ind
							break
					for ind, card in enumerate(choiceCards):
						if card.cost == 2:
							ind_remain2dro = ind
							break
					for ind, card in enumerate(choiceCards):
						if ind == ind_remain1dro or ind == ind_remain2dro:
							continue
						cards_to_mulligan.append(card)
					if mulliganDebug: print("mullingan list [case d-e]", cards_to_mulligan)
					return cards_to_mulligan
				elif exist_1drop:
					#
					# case [E]
					# remain an powerless a 1^drop minion
					########
					ind_remain1dro = -1
					for ind, card in enumerate(choiceCards):
						if card.cost == 1:
							ind_remain1dro = ind
							break
					for ind, card in enumerate(choiceCards):
						if ind == ind_remain1dro:
							continue
						cards_to_mulligan.append(card)
					if mulliganDebug: print("mullingan list [case E]", cards_to_mulligan)
					return cards_to_mulligan				
				else: #in case only buff-up 1drops 
					#
					# case [F]
					# (no 1 drop in starting hand.) mulligan all
					########
					for card in choiceCards:
						cards_to_mulligan.append(card)
					if mulliganDebug: print("mullingan list [case F]", cards_to_mulligan)
					return cards_to_mulligan				

		
		#
		#  2-b. ��莞�̃}���K�������@�i2-2-3�̃}�i�J�[�u�𐮂���j
		####################################################
		else: # in case player go second.
			if num_2drop >= 2:
				#
				# case [a]
				# remain two 2-drop minions, and a 3-drop if any. 
				#####
				ind_remain2droA = -1
				ind_remain2droB = -1
				for ind, card in enumerate(choiceCards):
					if card.cost == 2:
						if ind_remain2droA == -1:
							ind_remain2droA = ind
						else:
							ind_remain2droB = ind
							break
				for ind, card in enumerate(choiceCards):
					if ind == ind_remain2droA or ind == ind_remain2droB:
						continue
					if card.cost == 3 or card.cost == 0:
						continue
					cards_to_mulligan.append(card)
				if mulliganDebug: print("mullingan list [case a]", cards_to_mulligan)
				return cards_to_mulligan
			elif num_2drop == 1:
				if num_1drop >= 2:
					#
					# case [b]
					# remain a 2-drop minion, and two (or more) 1-drop. 
					########
					ind_remain1droA = -1
					ind_remain1droB = -1
					for ind, card in enumerate(choiceCards):
						if card.cost == 1:
							if ind_remain1droA == -1:
								ind_remain1droA = ind
							else:
								ind_remain1droB = ind
								break
					for ind, card in enumerate(choiceCards):
						if ind == ind_remain1droA or ind == ind_remain1droB:
							continue
						if card.cost == 2:
							continue
						if card.cost == 0:
							continue
						cards_to_mulligan.append(card)
					if mulliganDebug: print("mullingan list [case b]", cards_to_mulligan)
					return cards_to_mulligan
				elif num_1drop == 1:
					#
					# case [c]
					# remain a 2-drop minion, and a 1-drop. 
					########
					for ind, card in enumerate(choiceCards):
						if card.cost == 2 or card.cost == 1:
							continue
						cards_to_mulligan.append(card)
					if mulliganDebug: print("mullingan list [case c]", cards_to_mulligan)
					return cards_to_mulligan
				else:
					#
					# case [d]
					# remain a 2-drop minion only. 
					########
					for ind, card in enumerate(choiceCards):
						if card.cost == 2:
							continue
						cards_to_mulligan.append(card)
					if mulliganDebug: print("mullingan list [case d]", cards_to_mulligan)
					return cards_to_mulligan
			else: # no 2 drop minion in hand
				#
				# case [e]
				# remain 1-drop minions only. 
				########
				for ind, card in enumerate(choiceCards):
					if card.cost == 1:
						continue
					cards_to_mulligan.append(card)
				if mulliganDebug: print("mullingan list [case e]", cards_to_mulligan)
				return cards_to_mulligan

		


	###################################################################
	##�@�y���萶���p�֐��z
	##
	##�@�@����A�O���E�H�[���b�N�f�b�L�p�ɁC������𐶐�����֐��D
	##�@�@���萶����̋ǖʂɁA�����ʂ̐��`�a�ɂ���ԕ]�����قǂ����A�P��MAX�T���ɂĒ��������D
	##
	##�@  @param game   - ���萶�����s���ׂ��ǖʏ�񂪂܂���Game�^�C���X�^���X
	##�@  @param option - ���I�{�G�[�W�F���g�ł͎g��Ȃ��I���@���p���ɔC�ӂŗ^����p�����[�^�w��p�̃��X�g�D
	##�@  @param gameLog    - �Q�[���̃��O���l�ߍ��ނ��߂̃��X�g�������ɓn���Ă��ǂ�
	##�@  @param debugLog   - �Q�[���̃��O�\���p
	##
	##�@�@@return  ExceptionPlay�^�̒萔�D���튮����VALID�A�ُ�I����INVALD�A�����ɂ�錈���Ȃ�GAMEOVER�D
	###################################################################
	def StandardStep1(self, game, option=None, gameLog=[], debugLog=True):	
		
		#print("SatZoo Thinking Start...")
		debugChoice = False ###  Display parameters and scores
		
		myWeight=option #��ł��������O�̂���
		loopCount=0

		#
		# 0. ���̃��[�v�ɂ��A��̃J�[�h����i�~�j�I���v���C�A�����v���C�A�U���A�q�[���[�p���[�j�����{�D
		#    �������^�[��������ő�20�񕪎��{�ł���
		# �@�@(�r���ł��J�[�h���삪�s����΁A���[�v�𔲂��o���āA�������Q�[���V�X�e�����ɕԂ�)
		#########################
		while loopCount<20:
			loopCount+=1
			if debugChoice:
				print(">>>>>>>>>>>>>>>>>>>")

			myCandidate = getCandidates(game)#�u�������Ȃ��v�I�����͓���Ă��Ȃ�
			myChoices = [Candidate(None,type=ExceptionPlay.TURNEND, turn=game.turn)]#�������Ȃ��I��
			maxScore = self.getStageScore(game,myWeight,debugChoice)#�������Ȃ��Ƃ��̃X�R�A

			if debugChoice:
				print("   %s %d"%(myChoices[0],maxScore))
			maxChoice = None



			#
			# 1.  Judge "Should use Coin now??"
			# 
			#########################
			hasCoin = False
			for myChoice in myCandidate:
				if myChoice.card.id == "GAME_005":
					hasCoin = True

			shouldUseCoin = False
			if hasCoin:
				remainMana = game.current_player.mana
				for card in game.current_player.hand:
					if card.id == "GAME_005":
						continue
					if card.cost == remainMana + 1:
						shouldUseCoin = True
						break

			if shouldUseCoin:
				for myChoice in myCandidate:
					if myChoice.card.id == "GAME_005":
						executeAction(game, myChoice, debugLog=debugLog)
						player = game.current_player
						postAction(player)
						break
				continue
			


			## Check if can play minion this turn. (for SPECIAL PROCEDURE 1 below.
			can_playMinion = False
			for myChoice in myCandidate:
				if myChoice.type == BlockType.PLAY and myChoice.card.type == CardType.MINION:
					can_play_Minion = True
					

			#
			#	2.  Execute legal moves
			#      ->  Evaluate next state 
			#      -->  Max Search
			#######################################
			for myChoice in myCandidate:
				tmpGame = fireplace_deepcopy(game)
				#tmpGame = copy.deepcopy(game)
				#if debugChoice:
				#	print("Estimate the score for [%s]"%(myChoice))
				result = executeAction(tmpGame, myChoice, debugLog=False)
				postAction(tmpGame.current_player)


				#
				# SPECIAL PROCEDURE 1. 
				# for playing Soul-Fire effectively
				#########################################
				soulFire_to_hero = False
				soulFire_inefficiency = False
				if myChoice.card.id == "VAN_EX1_308":
					#if can_play_Minion:
					#	continue        #Do not play soul-fire if you can play minion this turn.
					if myChoice.target.type == CardType.HERO:
						soulFire_to_hero = True
					elif myChoice.target.type == CardType.MINION:
						if myChoice.target.health + myChoice.target.atk  < 5:
							soulFire_inefficiency = True
						elif myChoice.target.divine_shield:
							soulFire_inefficiency = True
					

				if result==ExceptionPlay.INVALID:
					stop=True
				if result==ExceptionPlay.GAMEOVER:
					score=100000


				else:					
					score = self.getStageScore(tmpGame,myWeight,debugChoice)

				if soulFire_to_hero:
					score -= 10000 # Because, very bad move in general.
				if soulFire_inefficiency:
					score -= 10000 # Because, bad move in general.


				if debugChoice:
					print("   %s %d"%(myChoice,score))
				if score > maxScore:
					maxScore = score
					myChoices = [myChoice]
					if score==100000:
						break
				elif score == maxScore:
					myChoices.append(myChoice)
			if debugChoice:
				print("<<<<<<<<<<<<<<<<<<<")

			if len(myChoices)>0:
				myChoice = random.choice(myChoices)
				if myChoice.type==ExceptionPlay.TURNEND:
					if debugLog:
						print(">%s -> turnend."%(self.name))
					return ExceptionPlay.VALID

				ret = executeAction(game, myChoice,debugLog=debugLog)
				
				if ret==ExceptionPlay.GAMEOVER:
					return ExceptionPlay.GAMEOVER
				if ret==ExceptionPlay.INVALID:
					return ExceptionPlay.INVALID
				player = game.current_player
				postAction(player)
				continue

			else:
				return ExceptionPlay.VALID




	###################################################################
	#�@�y�ǖʕ]���p�̊֐��z
	#
	#�@�@�I�O������A���̊֐����Q�Ƃ���K�v�͈�؂Ȃ��I
	#	 �G�[�W�F���g�����萶�����s���ۂɁA���̃G�[�W�F���g���K�X�Ăяo�����s���D
	#	 �����ʂ̐��`�a����邾���̃V���v���Ȃ���
	#
	###################################################################
	def getStageScore(self,game, weight, debugChoice=False):
		cardPerPoint=0.3
		w_length=34
		w=[]
		w_names = ["myHP", "hisHP", "myMAtk", "myMHP", "myTaMAtk", "myTaMHP", 
			 "hisMAtk", "hisMHP", "hisTaMAtk", "hisTaMHP", 
			 "handMHP", "canPlayMHP", "handMNum", "canPlayMNum", "handSplNum", "canPlaySplNum",
			 "mydivShiNum", "myTaNum", "hisSecret", "his_Taun_&_DivSh"]
		my_weight = [1, -10, 5, 5, 0, 0,
				-5, -5, 0, -100, # Zoo lock must kill all taunt minion on opponent side. 
				0, 0, 3, 0, 3, 0, 
				10, 10, -50, -400]
		

		for i in range(len(w_names)):
			w.append(0)
		me = game.current_player
		he = game.current_player.opponent
		myHero = me.hero
		hisHero = he.hero

		#w[0]=myHeroH
		#w[1]=hisHeroH
		w[0] = myHero.health+myHero.armor
		w[1] = hisHero.health+hisHero.armor

		#w[2]=myCharA = 0
		#w[3]=myCharH = 0
		#w[4]=myTauntCharA = 0
		#w[5]=myTauntCharH = 0
		#w[16]	#���w�̐��Ȃ鏂�~�j�I���̖���
		#w[17]	#���w�̒����~�j�I���̖���
		for char in me.characters:
			if char.type == CardType.MINION:
				w[2] += char.atk
				if char.taunt:
					w[4] += char.atk
				w[3] += char.health
				if char.taunt:
					w[5] += char.health
					w[17] += 1 
				if char.divine_shield:
					w[16] += 1

		#w[18]	#�G�̔��̐�
		if len(he.secrets) > 0:
			w[18] += 1



		#w[6]=hisCharA = 0
		#w[7]=hisCharH = 0
		#w[8]=hisTauntCharA = 0
		#w[9]=hisTauntCharH = 0
		#w[19]	#  �G�w�́u���������Ȃ鏂�v�~�j�I���̖����D
		#�@�@�@�@  ����ɏd�݂Â����Ȃ��ƁA�w�T���E�H�[�J�[�x���̃J�[�h���i�v�ɏ����ł��Ȃ��Ȃ�
		for char in he.characters:
			if char.type == CardType.MINION:
				w[6] += char.atk
				if char.taunt:
					w[8] += char.atk
				w[7] += char.health
				if char.taunt:
					w[9] += char.health  
				if char.taunt and char.divine_shield:
					w[19] += 1


		#w[10]=MinionCH = 0#�莝���̃~�j�����J�[�h��HP�̑��a
		#w[11]=PlayableMinionCH = 0#�莝���̃~�j�����J�[�h��HP�̑��a
		#w[12]=MinionCN = 0#�莝���̃~�j�����J�[�h�̖���
		#w[13]=PlayableMinionCN = 0#�莝���̃~�j�����J�[�h�̖���
		#w[14]=SpellCN = 0#�莝���̃X�y���J�[�h�̖���
		#w[15]=PlayableSpellCN = 0#�莝���̃X�y���J�[�h�̖���
		for card in me.hand:
			if card.type == CardType.MINION:
				w[10] += card.health
				w[12] += 1
				if card.is_playable():
					w[11] += card.health
					w[13] += 1
			if card.type == CardType.SPELL:
				w[14] += 1
				if card.is_playable():
					w[15] += 1
		
		
		#�d�݂Â����ĉ��Z��
		score = 0.0
		for i in range(len(my_weight)):
			if debugChoice:
				if w[i]!=0 and my_weight[i] != 0:
					print("%s:%d *%d"%(w_names[i],w[i],my_weight[i]),end=", ")
				pass			
			score += w[i] * my_weight[i]
		if debugChoice:
			print("")
		return score
