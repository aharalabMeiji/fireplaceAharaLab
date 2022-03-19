import random
import copy
import pickle
from fireplace import card, cards
from fireplace.exceptions import GameOver
from hearthstone.enums import CardType, BlockType, CardClass#
from utils import *
from fireplace.actions import Action
from fireplace.card import Card
from fireplace.game import Game
from enum import IntEnum
import numpy as np


BATCH_SIZE = 128
GAMMA = 0.999
EPS_START = 0.9
EPS_END = 0.05
EPS_DECAY = 200
TARGET_UPDATE = 10

class QueenAgent(Agent):
	game =None
	player =None
	qtable = np.zeros((6*6*11*11*2*2,20+1+1))
	qq = np.array([[1,2,3],[2,3,4]])
	state = None
	eps_threshold = 0.5

	vLength = 39  # �x�N�g���̒���
	w = np.array([1, -1, 1, 1, 1, 1, 1, -1, 0, 1, 1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, 0, -1, -1, -1, -1, -1, -1, -1, 2, -2, 4, -8, 1, -1, 0.5, -0.5,3])

	def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000, mulliganStrategy=None ):
		super().__init__(myName, myFunction, myOption, myClass, rating )
		#with open('qtable', 'rb', encoding='shift_jis') as qtable:
		#	self.qtable = pickle.load(qtable)
		pass

	def QAI(self, thisgame, option=[], gameLog=[], debugLog=False):
		
		self.game = thisgame
		self.player = thisgame.current_player
		loopCount=0
		while loopCount<20:
			loopCount+=1
			myCandidate = getCandidates(thisgame)
			simpCan = self.classify_action(myCandidate)
			#for x in simpCan:
			#	print(simpCan)
			self.state = self.observe_state(self.game)
			action = self.chooseAction(simpCan)
			maxscore=0
			index=0
			actionIndex = 21
			if simpCan[action]=="power":
				actionIndex=21
				for x in myCandidate:
					if x.type==BlockType.POWER:
						tmpgame = fireplace_deepcopy(self.game)
						before=self.getBoardScore(tmpgame)
						exc = executeAction(tmpgame, x, debugLog=False)
						postAction(self.player)
						after = self.getBoardScore(tmpgame)
						maxscore = self.calcScore(before, after)
						index = x
				pass
			elif simpCan[action]=="attack":
				actionIndex=20
				for x in myCandidate:
					if x.type==BlockType.ATTACK:
						tmpgame = fireplace_deepcopy(self.game)
						before=self.getBoardScore(tmpgame)
						exc = executeAction(tmpgame, x, debugLog=False)
						postAction(self.player)
						after = self.getBoardScore(tmpgame)
						if maxscore < self.calcScore(before, after):
							maxscore = self.calcScore(before, after)
							index = x
			else:
				for i in range(len(self.clownDruidCard)):
					if simpCan[action]==self.clownDruidCard[i]:
						actionIndex=i
					else:
						actionIndex=20
				for x in myCandidate:
					if x.type == BlockType.PLAY:
						tmpgame = fireplace_deepcopy(self.game)
						before=self.getBoardScore(tmpgame)
						exc = executeAction(tmpgame, x, debugLog=False)
						postAction(self.player)
						after = self.getBoardScore(tmpgame)
						if maxscore < self.calcScore(before, after):
							maxscore = self.calcScore(before, after)
							index = x
			copygame = fireplace_deepcopy(self.game)
			exc = executeAction(thisgame, myCandidate[index], debugLog=False)
			value = self.calcValue(myCandidate[index].card,copygame)

			tableslice = qtable[state[0]*17424/6+state[1]*2904/6+state[2]*484/11+state[3]*44/11+state[4]*4/2+state[5]]
			tableslice[actionIndex] = (tableslice[actionIndex] + value)/2.0



			#if len(myCandidate)>0:
			#	myChoice = random.choice(myCandidate)
			#	exc = executeAction(thisgame, myChoice, debugLog=debugLog)
			#	postAction(self.player)
			#	if exc==ExceptionPlay.GAMEOVER:
			#		return ExceptionPlay.GAMEOVER
			#	else:
			#		continue
			return ExceptionPlay.VALID

	def classify_action(self, candidates):
		atkflag=False
		simpleCandidates =[]
		for  i in candidates:
			if i.type==BlockType.ATTACK:
				if not atkflag:
					simpleCandidates.append("attack")
					atkflag = True
				pass
			elif i.type==BlockType.PLAY:
				simpleCandidates.append(i.card.id)
				pass
			elif i.type==BlockType.POWER:
				simpleCandidates.append("power")
				pass
			else:
				pass
		return simpleCandidates
	def observe_state(self, game):

		me=game.current_player
		he=game.current_player.opponent
		a=min((me.hero.health+me.hero.armor-1)/5,5)
		b=min((he.hero.health+he.hero.armor-1)/5,5)
		c=game.turn/2
		d=me.mana
		if len(me.characters)>1:
			e=1
		else:
			e=0
		if len(he.characters)>1:
			f=1
		else:
			f=0
		s=[a,b,c,d,e,f]
		return s
	def chooseAction(self,simplecan):
		s=self.state
		doko = int(s[0]*(17424/6)+s[1]*(2904/6)+s[2]*(484/11)+s[3]*(44/11)+s[4]*(4/2)+s[5])
		print(doko)
		tabe = self.qq[0]
		tableslice = self.qtable[doko]
		rannum = random.randint(0,len(simplecan))
		maxvalue=0
		maxindex=0
		canvalue =[0]*len(simplecan)
		for i in range(len(simplecan)):
			if simplecan[i]=="power":
				canvalue[i]=tableslice[21]
			elif simplecan[i]=="attack":
				canvalue[i]=tableslice[20]
			else:
				for x in range(19):
					if canvalue[i] == self.clownDruidCard[x]:
						canvalue[i] = tableslice[x]
					else:
						canvalue[i] = tableslice[19]
		for i in range(len(simplecan)):
			if canvalue[rannum%len(simplecan)]>maxvalue:
				maxvalue=canvalue[rannum%len(simplecan)]
				maxindex=rannum%len(simplecan)
			rannum +=1
		if self.eps_threshold <random.random():
			return maxindex
		else:
			return random.randint(0,len(simplecan))
		pass

	def SimpleMulligan(self, choiceCards):
		# make cost 1~4 cards left
		print("%s mulligan turn"%(self.name))
		cards_to_mulligan = []
		for num in range(len(choiceCards)):
			if choiceCards[num].cost > 5:
				cards_to_mulligan.append(choiceCards[num])
		return cards_to_mulligan

	def getBoardScore(self, _game: Game):
		me = _game.current_player
		he = _game.current_player.opponent
		v = np.zeros(self.vLength)
		v[0] = me.hero.health
		v[1] = he.hero.health
		for char in me.characters:
			if char.type == CardType.MINION:
				v[2] += char.atk
				v[3] += char.health
				if getattr(char, 'taunt', 0):
					v[4] += char.health
				# if char.battlecry:
				if getattr(char, 'deathrattles', 0):
					v[5] += 1
				# if char.discover:
				if getattr(char, 'divine_shield', 0):
					v[6] += 1
				# if char.dormant:
				# if char.echo:
				if getattr(char, 'forgetful', 0):
					v[7] += 1
				if getattr(char, 'immune', 0):
					v[8] += 1
				if getattr(char, 'has_inspire', 0):
					v[9] += 1
				if getattr(char, 'lifesteal', 0):
					v[10] += 1
				# if char.magnetic:
				# if char.outcast:
				if getattr(char, 'overkill', 0):
					v[11] += 1
				# if char.overload:
				if getattr(char, 'poisonous', 0):
					v[12] += 1
				if getattr(char, 'reborn', 0):
					v[13] += 1
				# if char.rush:
				if getattr(char, 'spell_damage', 0):  # int
					v[14] += char.spell_damage
				# if char.spellburst:
				if getattr(char, 'windfury', 0):     # �ǉ��U����(int)
					v[15] += char.windfury
		for char in he.characters:
			if char.type == CardType.MINION:
				v[16] += char.atk
				v[17] += char.health
				if getattr(char, 'taunt', 0):
					v[18] += char.health
				# if char.battlecry:
				if getattr(char, 'deathrattles', 0):
					v[19] += 1
				# if char.discover:
				if getattr(char, 'divine_shield', 0):
					v[20] += 1
				# if char.dormant:
				# if char.echo:
				if getattr(char, 'forgetful', 0):
					v[21] += 1
				if getattr(char, 'immune', 0):
					v[22] += 1
				if getattr(char, 'has_inspire', 0):
					v[23] += 1
				if getattr(char, 'lifesteal', 0):
					v[24] += 1
				# if char.magnetic:
				# if char.outcast:
				if getattr(char, 'overkill', 0):
					v[25] += 1
				# if char.overload:
				if getattr(char, 'poisonous', 0):
					v[26] += 1
				if getattr(char, 'reborn', 0):
					v[27] += 1
				# if char.rush:
				if getattr(char, 'spell_damage', 0):  # int
					v[28] += char.spell_damage
				# if char.spellburst:
				if getattr(char, 'windfury', 0):     # �ǉ��U����(int)
					v[29] += char.windfury*char.atk
		for char in me.characters:
			if char.type == CardType.MINION:
				des = char.data.description
				if '[x]' in des and not ':' in des:
					v[30] += char.health
		for char in he.characters:
			if char.type == CardType.MINION:
				des = char.data.description
				if '[x]' in des and not ':' in des:
					v[31] += char.health
		v[32] = len(me.secrets)
		v[33] = len(he.secrets)
		v[34] = me.hero.atk
		v[35] = he.hero.atk
		v[36] = len(me.hand)
		v[37] = len(he.hand)
		v[38] = me._max_mana
		return v
		pass

		def calcScore(self, _before, _after):
			tmpW = np.copy(self.w)
			 #if self.DebugLog:
				# print(f"before{_before}")
				# print(f"after{_after}")
			 #print(f"w{tmpW}")
			if _before is int:
				retScore = _after - _before
				return retScore
			else:
				retScore = np.sum((_after - _before) * tmpW)
			return retScore
			pass

	def calcValue(self, action,copygame):
		card = action.card
		if action.type == BlockType.PLAY:
			if card.id == "GAME__005":
				return 1
			elif card.id == "CORE_EX1_169":
				return 1
			elif card.id == "SCH_427":
				return 2
			elif card.id == "SCH_311":
				return card.atk+(len(self.player.characters)-1)
			elif card.id == "SCH_333":
				return 1
			elif card.id == "DMF_075":
				return len(self.player.hand)-len(copygame.current_player.hand)
			elif card.id == "CORE_CS2_013":
				a=10-(self.game.turn/2)
				return max(a,0)
			elif card.id == "BT_130":
				return max(10-(self.game.turn/2),0)+1
			elif card.id == "BAR_535":
				return card.atk+card.health
			elif card.id == "SCH_605":
				return card.atk*2
			elif card.id == "SCH_616":
				return card.atk+2
			elif card.id == "DMF_078":
				return card.atk+card.health
			elif card.id == "DMF_078t":
				return card.atk+card.health
			elif card.id == "SCH_610":
				return (len(self.player.characters)-len(copygame.current_player.characters))*7
			elif card.id == "BAR_042":
				if  (len(self.player.characters)-len(copygame.current_player.characters))>1:
					return card.atk +6
				else:
					return card.atk
			elif card.id == "DMF_163":
				return (len(self.player.characters)-len(copygame.current_player.characters))*4
			elif card.id == "DMF_163t":
				return (len(self.player.characters)-len(copygame.current_player.characters))*4
			elif card.id == "SCH_609":
				return 10
			elif card.id == "DMF_188":
				return len(self.player.hand)-len(copygame.current_player.hand)*3
			else:
				return calcScore(self.getBoardScore(copygame), self.getBoardScore(self.game))
		else:
			return calcScore(self.getBoardScore(copygame), self.getBoardScore(self.game))



	clownDruidCard = [
		'GAME_005',#�R�C��
		'CORE_EX1_169',#Innervate(���C) (0)
		'SCH_427',#Lightning Bloom(�d������) (0)
		'SCH_311',#Animated Broomstick(���Ԃق���) (1/1/1)
		'SCH_333',#Nature Studies(���R�w�̗\�K) (1)
		'DMF_075',#Guess the Weight(�d������) (2)
		'CORE_CS2_013',#Wild Growth(�쐶�̔ɖ�) (3)
		'BT_130',#Overgrowth(�ߏ�ɐB) (4)
		'BAR_535',#Thickhide Kodo(����̃R�h�[) (4/3/5)
		'SCH_605',#Lake Thresher(�΂̃X���b�V���[) (5/4/6)
		'SCH_616',#Twilight Runner(�g���C���C�g�����i�[) (5/5/4)
		'DMF_078',#Strongman(���͒j) (7/6/6)
		'DMF_078t',
		'SCH_610',#Guardian Animals(���b) (8)
		'BAR_042',#Primordial Protector(�n���̎���) (8/6/6)
		'DMF_163',#Carnival Clown(�J�[�j�o���̃s�G��) (9/4/4)
		'DMF_163t',
		'SCH_609',#Survival of the Fittest(�K�Ґ���) (10)
		'DMF_188']#Y'Shaarj, the Defiler(�w���̖��胄�V�����[�W��) (10/10/10)
	bigWarriorCard = [
		'GAME_005',#�R�C��
		'SW_023',#Provoke(���藧��) (0)spell, tradeable
		'SCH_237',#Athletic Studies(�̈�w�̗\�K) (1)spell
		'CORE_EX1_410',#Shield Slam(�V�[���h�X����) (1)spell
		'BT_124',#Corsair Cache(�C���̉B������) (2)spell
		'DMF_522',#Minefield(�n����) (2) spell
		'BT_117',#Bladestorm(���n��) (3)spell
		'SW_094',#Heavy Plate(�d���Z) (3) spell, tradeable
		'BT_781',#Bulwark of Azzinoth(�A�Y�B�m�X�̖h��) (3/1/4)weapon
		'BAR_845',#Rancor(�⍦) (4) spell
		'BAR_844',#Outrider's Axe(�擱�҂̕�) (4/3/3)weapon
		'YOP_005',#Barricade(�o���P�[�h) (4) spell 
		'CORE_EX1_407',#Brawl(����) (5) spell
		'SW_021',#Cowardly Grunt(�D�����̕���) (6/6/2) 
		'SCH_533',#Commencement(�w�ʎ��^��) (7)
		'SW_024',#Lothar (���[�T�[) (7/7/7)
		'SCH_337',#Troublemaker(�s�Ǌw��) (8/6/8)
		'SW_068',#Mo'arg Forgefiend(���A�[�O�̒b��S) (8/8/8)
		'SCH_621',]#Rattlegore(���g���S�A) (9/9/9)
	faceHunterCard = [
		'GAME_005',#�R�C��
		'SCH_617',#Adorable Infestation(�J���C�C�N����) (1)
		'SCH_600',#Demon Companion(�����̑��_) (1)
		'SCH_231',#Intrepid Initiate(�}�����k��) (1/1/2)
		'CORE_DS1_184',#Tracking(�ǐՏp) (1)
		'SCH_279',#Trueaim Crescent(�g�D���[�G�C���E�N���Z���g) (1/1/4) weapon
		'SCH_133',#Wolpertinger(���H���p�[�e�B���K�[) (1/1/1)
		'BAR_801',#Wound Prey(�l���̏�) (1)
		'SCH_713',#Cult Neophyte(���c�̐V�����) (2/3/2)
		'BT_211',#Imprisoned Felmaw(���󂳂ꂵ�t�F�����[) (2/5/4)
		'CORE_BRM_013',#Quick Shot(���˂̈��) (2)
		'SW_321',#Aimed Shot(�_������) (3)
		'BAR_721',#Mankrik(�}���N���b�N) (3/3/4)
		'BAR_032',#Piercing Shot(�ђʒe) (4)
		'DMF_088',#Rinling's Rifle(���������O�̃��C�t��) (4/2/2) weapon
		'BAR_037',#Warsong Wrangler(�E�H�[�\���O�̏b�����) (4/3/4)
		'BAR_551',#Barak Kodobane(�o���N�E�R�h�[�x�C��) (5/3/5)
		'DMF_087',]#Trampling Rhino(���ݒׂ��T�C) (5/5/5)



class Qlearning:
	def __init__(self, num_states, num_actions):
		self.num_states = num_states
		self.num_actions = num_actions
		self.q_table = np.random.uniform(low=0, high=0, size=(NUM_DIGITIZE**self.num_states, self.num_actions))

	

	pass