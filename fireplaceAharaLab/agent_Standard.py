import random
import copy
from fireplace.exceptions import GameOver
from hearthstone.enums import CardType, BlockType, CardClass, SpellSchool#
from utils import ExceptionPlay, Candidate, executeAction,getCandidates,postAction,Agent,fireplace_deepcopy,QTable
from fireplace.actions import Action
from fireplace.card import Card
from fireplace.game import Game
from fireplace.utils import ActionType
from enum import IntEnum


class StandardAgent(Agent):
	def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000 ):
		super().__init__(myName, myFunction, myOption, myClass, rating )
		pass

	def StandardRandom(self, thisgame: ".game.Game", option=[], gameLog=[], debugLog=False):
		player = thisgame.current_player
		loopCount=0
		while loopCount<20:
			loopCount+=1
			myCandidate = getCandidates(thisgame)
			if len(myCandidate)>0:
				myChoice = random.choice(myCandidate)
				exc = executeAction(thisgame, myChoice, debugLog=debugLog)
				postAction(player)
				if exc==ExceptionPlay.GAMEOVER:
					return ExceptionPlay.GAMEOVER
				elif myChoice.type==ExceptionPlay.TURNEND:
					return ExceptionPlay.VALID
				else:
					continue
			return ExceptionPlay.VALID

import time
class StandardVectorAgent(Agent):
	def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000, mulliganStrategy=None):
		super().__init__(myName, myFunction, myOption, myClass, rating, mulliganStrategy=mulliganStrategy )
		self.__standard_agent__=StandardAgent("Standard",StandardAgent.StandardRandom, myClass=myClass)
		self.QList=[]
		pass
	def StandardStep1(self, game, option=None, gameLog=[], debugLog=True):	
		loopCount=0
		while loopCount<20:	
			loopCount+=1
			player=game.current_player
			cardList=[player.hero.id, player.hero.power.id]+list(set(player.starting_deck))
			debug=False
			if option==None:
				print ("StandardStep1 needs an option")
				return ExceptionPlay.INVALID
			myWeight=option
			statusVector=self.getStatusVector(game)
			myCandidate = getCandidates(game)
			myChoices = []
			maxScore=-100000
			maxChoice = None
			if debug:
				print(">>>>>>>>>>>>>>>>>>>")
			for myChoice in myCandidate:
				tmpGame = fireplace_deepcopy(game)
				#tmpGame = copy.deepcopy(game)
				result = executeAction(tmpGame, myChoice, debugLog=False)
				if result==ExceptionPlay.INVALID:
					stop=True
				if result==ExceptionPlay.GAMEOVER:
					score=100000
				elif myChoice.type==ExceptionPlay.TURNEND:
					score = self.getStageScore(tmpGame,myWeight)
				else:
					if self.__standard_agent__.StandardRandom(tmpGame,debugLog=False)==ExceptionPlay.GAMEOVER:#ここをもっと賢くしてもよい
						score=100000
					else:
						score = self.getStageScore(tmpGame,myWeight)
				if debug:
					print("%s %s %s %f"%(myChoice.card,myChoice.type,myChoice.target,score))
				if score > maxScore:
					maxScore = score
					myChoices = [myChoice]
					if score==100000:
						break
				elif score == maxScore:
					myChoices.append(myChoice)
			if debug:
				print("<<<<<<<<<<<<<<<<<<<")
			if len(myChoices)>0:
				myChoice = random.choice(myChoices)
				actionCard, actionTarget=self.getActionVector(myChoice,self.myClass)
				self.QList.append(QTable(statusVector,actionCard,actionTarget))
				ret = executeAction(game, myChoice,debugLog=debugLog)
				if ret==ExceptionPlay.GAMEOVER:
					return ExceptionPlay.GAMEOVER
				if ret==ExceptionPlay.INVALID:
					return ExceptionPlay.INVALID
				player = game.current_player
				postAction(player)
				#print("(%s,%s)"%(statusVector,actionVector))
				if myChoice.type==ExceptionPlay.TURNEND:
					return ExceptionPlay.VALID
				else:
					continue
			else:
				return ExceptionPlay.VALID
	def getStageScore(self,game, weight):
		cardPerPoint=0.3
		w_length=34
		w=[]
		for i in range(w_length):
			w.append(0)
		me = game.current_player
		he = game.current_player.opponent
		myHero = me.hero
		hisHero = he.hero
		#w[0]=myHeroH
		w[0] = myHero.health+myHero.armor
		#w[1]=hisHeroH
		w[1] = hisHero.health+hisHero.armor
		#w[2]=myCharA = 0
		#w[3]=myCharH = 0
		#w[4]=myTauntCharA = 0
		#w[5]=myTauntCharH = 0
		for char in me.characters:
			w[2] += char.atk
			if char.taunt:
				w[4] += char.atk
			if char.type == CardType.MINION:
				w[3] += char.health
				if char.taunt:
					w[5] += char.health
		#w[6]=hisCharA = 0
		#w[7]=hisCharH = 0
		#w[8]=hisTauntCharA = 0
		#w[9]=hisTauntCharH = 0
		for char in he.characters:
			w[6] += char.atk
			if char.taunt:
				w[8] += char.atk
			if char.type == CardType.MINION:
				w[7] += char.health
				if char.taunt:
					w[9] += char.health
		#w[10]=MinionCH = 0#手持ちのミニョンカードのHPの総和
		#w[11]=PlayableMinionCH = 0#手持ちのミニョンカードのHPの総和
		#w[12]=MinionCN = 0#手持ちのミニョンカードの枚数
		#w[13]=PlayableMinionCN = 0#手持ちのミニョンカードの枚数
		#w[14]=SpellCN = 0#手持ちのスペルカードの枚数
		#w[15]=PlayableSpellCN = 0#手持ちのスペルカードの枚数
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
		#w[16]=BattleCryCN = 0	#雄叫びカードの枚数
		#w[17]=ChargeCN = 0	#突撃カードの枚数
		#w[18]=WinduryCN = 0	#疾風カードの枚数
		#w[19]=TauntCN = 0	#挑発カードの枚数
		#w[20]=DamageCN = 0	#ダメージカードの枚数
		#w[21]=GainCN = 0	#獲得#回復カードの枚数
		#w[22]=SummonCN = 0	#召喚カードの枚数
		#w[23]=LifeStealCN = 0	#生命奪取カードの枚数
		#w[24]=GiveCN = 0	 #付与カードの枚数
		#w[25]=DeathrattleCN = 0 #断末魔カードの枚数
		#w[26]=SilenceCN = 0	#沈黙カードの枚数
		#w[27]=SecretCN = 0	# 秘策カードの枚数
		#w[28]=DiscoverCN = 0	#発見カードの枚数
		#w[29]=DivineShieldCN = 0	#聖なる盾カードの枚数
		#w[30]=StealthCN = 0	#隠れ身カードの枚数
		#w[31]=AttackVanillaCN=0	#攻撃力の強いバニラカードを使う
		#w[32]=HealthVanillaCN=0	#体力の大きいバニラカードを使う
		#w[33]=SmallVanillaCN=0	#体力の小さいバニラカードを使う
		for card in me.hand:
			des = card.data.description
			if '雄叫び' in des:
				w[16] += 1
			if '突撃' in des:
				w[17] += 1
			if '疾風' in des:
				w[18] += 1
			if '挑発' in des:
				w[19] += 1
			if 'ダメージ' in des:
				w[20] += 1
			if '獲得' in des or '回復' in des:
				w[21] +=1
			if '召喚' in des:
				w[22] +=1
			if '生命奪取' in des:
				w[23] +=1
			if '付与' in des:
				w[24] +=1
			if '断末魔' in des:
				w[25] +=1 #断末魔カードを使う
			if '沈黙' in des:
				w[26] +=1	#沈黙カードを使う
			if '秘策' in des:
				w[27] +=1	# 秘策カードを使う
			if '発見' in des:
				w[28] +=1	#発見カードを使う
			if '聖なる盾' in des:
				w[29] +=1	#聖なる盾カードを使う
			if '隠れ身' in des:
				w[30] +=1	#隠れ身カードを使う
			if card.type == CardType.MINION and len(des)<3: #バニラ
				if card.atk>2:
					w[31] += 1	#攻撃力の強いバニラカードを使う
				if card.health>2:
					w[32] += 1	#体力の大きいバニラカードを使う
				if card.health<4:
					w[33] += 1	#体力の小さいバニラカードを使う
		score = 0.0
		for i in range(w_length):
			const=-1
			if i in [0,2,3,4,5]:
				const=1
			if i <12:
				const *= cardPerPoint
			wgt=0
			if len(weight)>i:
				wgt = weight[i]
			score += w[i]*wgt*const
		return score
	def StandardMulligan(self, choiceCards):
		# make cost 1 cards left
		print("%s mulligan turn"%(self.name))
		cards_to_mulligan = []
		for num in range(len(choiceCards)):
			if choiceCards[num].cost > 1:
				cards_to_mulligan.append(choiceCards[num])
		return cards_to_mulligan
	def StandardChoice(self, choiceCards):
		return random.choice(choiceCards)
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
	def vectorize(self,value,level,step):
		w=[]
		for i in range(level+1):
			w.append(0)
		t=int(value/step)
		if t>level:
			t=level
		w[t]=1
		return w
	def heroes(self,my,his):
		myHeroH = self.vectorize(my.hero.health+my.hero.armor,5,6)
		hisHeroH = self.vectorize(his.hero.health+his.hero.armor,5,6)
		myHeroA = self.vectorize(my.hero.atk+1,3,2)
		hisHeroA = self.vectorize(his.hero.atk+1,3,2)
		return myHeroH+myHeroA+hisHeroH+hisHeroA
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
		myCharH = self.vectorize(myCharH+2,5,3)
		myCharA = self.vectorize(myCharA+2,5,3)
		myTauntCharH = self.vectorize(myTauntCharH+2,4,3)
		myTauntCharA = self.vectorize(myTauntCharA+1,4,2)
		myShieldCharA = self.vectorize(myShieldCharA+1,4,2)
		myRebornCharA = self.vectorize(myRebornCharA+1,4,2)
		return myCharH+myCharA+myTauntCharH+myTauntCharA+myShieldCharA+myRebornCharA
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
		hisCharH = self.vectorize(hisCharH+2,5,3)
		hisCharA = self.vectorize(hisCharA+2,5,3)
		hisTauntCharH = self.vectorize(hisTauntCharH+2,4,3)
		hisTauntCharA = self.vectorize(hisTauntCharA+1,4,2)
		return hisCharH+hisCharA+hisTauntCharH+hisTauntCharA
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
		MinionCH=self.vectorize(MinionCH+2,5,3)
		PlayableMinionCH=self.vectorize(PlayableMinionCH+2,5,3)
		MinionCN=self.vectorize(MinionCN,5,1)
		PlayableMinionCN=self.vectorize(PlayableMinionCN,5,1)
		SpellCN=self.vectorize(SpellCN,5,1)
		PlayableSpellCN=self.vectorize(PlayableSpellCN,5,1)
		return MinionCH+MinionCN+PlayableMinionCH+PlayableMinionCN+SpellCN+PlayableSpellCN
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
	def getStatusVector(self, game):
		my = game.current_player
		his = game.current_player.opponent
		return self.gameStatus(my)+self.heroes(my,his)+self.myField(my)+self.hisField(his)+self.myHand(my)+self.myHandCard(my,my.hero.card_class)

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

#
#   Original random
#
def Original_random(game: ".game.Game"):
	player = game.current_player
	while True:
		for card in player.hand:
			if card.is_playable() and random.random() < 0.5:
				target = None
				if card.must_choose_one:
					card = random.choice(card.choose_cards)
				if card.requires_target():
					target = random.choice(card.targets)
				print("Playing %r on %r" % (card, target))
				executePlay(card,target)
				if player.choice:
					choice = random.choice(player.choice.cards)
					print("Choosing card %r" % (choice))
					myChoiceStr = str(choice)
					if 'RandomCardPicker' in str(choice):
						myCardID =  random.choice(choice.find_cards())
						myCard = Card(myCardID)
						myCard.controller = player#?
						myCard.draw()
						player.choice = None
					else :
						player.choice.choose(choice)
					continue
		# Randomly attack with whatever can attack
		for character in player.characters:
			if character.can_attack():
				target = random.choice(character.targets)
				executeAttack(character, target)
		break

def adjust_text(text):
	return text.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')

def adjust_text_by_spellpower(text, player, card):
	_catch_number=-1
	_new_text=adjust_text(text)
	_len=len(_new_text)
	for _i in range(_len):
		x = _new_text[_i]
		if x=='@' and hasattr(card,'script_data_num_1'):
			_new_text = _new_text[:_i] + str(card.script_data_num_1) + _new_text[_i+1:]
			pass
		if x=='@' and card.piece_of_cthun:
			_new_text = _new_text[:_i] + str(sum(player.piece_of_cthun)) + _new_text[_i+1:]
			pass
	for _i in range(_len):
		if _i<_len-3 and _new_text[_i:_i+3]=='{0}' :
			_new_text = _new_text[:_i+1] + card.script_data_text_0 + _new_text[_i+2:]
	for _i in range(_len):
		if _i<_len-3 and _new_text[_i:_i+3]=='{1}' :
			_new_text = _new_text[:_i] + _new_text[_i+3:]
	for _i in range(_len):
		if _new_text[_i]=='$':
			if _i+1<_len and _new_text[_i+1] in ['0','1','2','3','4','5','6','7','8','9']:
				_catch_number = int(_new_text[_i+1])
				_latter_text = _new_text[_i+2:]
				if _i+2<_len and _new_text[_i+2] in ['0','1','2','3','4','5','6','7','8','9']:
					_catch_number *= 10
					_catch_number += int(_new_text[_i+2])
					_latter_text = _new_text[_i+3:]
				if hasattr(card,'spell_school') and card.spell_school == SpellSchool.FIRE:
					_catch_number += player.spellpower_fire
				else :
					_catch_number += player.spellpower
				for _repeat in range(player.spellpower_double):
					_catch_number *= 2
				_new_text = _new_text[:_i] + "*" +str(_catch_number) +"*" + _latter_text
	return _new_text

class HumanAgent(Agent):
	def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000 , mulliganStrategy = None, choiceStrategy = None):
		super().__init__(myName, myFunction, myOption, myClass, rating, mulliganStrategy=mulliganStrategy, choiceStrategy = choiceStrategy )
		self.vectorAgent=StandardVectorAgent("Vector1",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=myClass)
		pass
	def HumanInput(self, game, option=None, gameLog=[], debugLog=True):
		player = game.current_player
		###############
		#from fireplace.deepcopy import deepcopy_game
		#new_game = debug_deepcopy(game, player)
		#######
		while True:
			###################
			#debug_board(new_game,game)#
			###################
			myCandidate = []
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
				if card.is_playable():
					if card.must_choose_one:
						for card2 in card.choose_cards:
							if card2.is_playable():
								if card2.requires_target():
									for target in card2.targets:
										myCandidate.append(Candidate(card, card2=card2, type=ActionType.PLAY, target=target, turn=game.turn))
								else:
									myCandidate.append(Candidate(card, card2=card2, type=ActionType.PLAY, target=None, turn=game.turn))
					else:# card2=None
						if card.requires_target():
							for target in card.targets:
								myCandidate.append(Candidate(card, type=ActionType.PLAY, target=target, turn=game.turn))
						else:
							myCandidate.append(Candidate(card, type=ActionType.PLAY, target=None, turn=game.turn))
				_yes,_option = card.can_trade()
				if _yes:
					myCandidate.append(Candidate(card, type=ActionType.TRADE, target=None, turn=game.turn))
			print("========OPPONENT'S PLAYGROUND======")
			for character in player.opponent.characters:
				print("%s"%character, end='   : ')
				if character == player.opponent.hero:
					if player.opponent.weapon:
						print("(%2d/%2d/%2d+%d)(%s)"%(character.atk,player.opponent.weapon.durability,character.health,character.armor,player.opponent.weapon.data.name), end=" ")
					else:
						print("(%2d/%2d+%d)"%(character.atk,character.health,character.armor), end=" ")
				else :
					print("(%2d/%2d)"%(character.atk,character.health), end=" ")
					if character._Asphyxia_ == 'asphyxia':
						print("(Now Asphyxia)", end=' ')
					if character.silenced:
						print("(silenced)", end=" ")
					if character.windfury:
						print("(windfury)", end=" ")
					if character.poisonous:
						print("(poisonous)", end=" ")
					if character.frozen:
						print("(frozen)", end=" ")
					if character.rush:
						print("(rush)", end=" ")
					if character.reborn:
						print("(reborn)", end=" ")
					if character.taunt:
						print("(taunt)", end=" ")
					if character.immune:
						print("(immune)", end=" ")
					if character.divine_shield:
						print("(divine_shield)", end=" ")
					if character.dormant>0:
						print("(dormant:%d)"%(character.dormant), end=" ")
					elif character.dormant<0:
						if character._sidequest_counter_>0:
							print("(dormant:%d)"%(character._sidequest_counter_), end=" ")
						else:
							print("(dormant)", end=" ")
					#if character._sidequest_counter_>0:
					#	if character.dormant==0:
					#		print("(sidequest:%d)"%(character._sidequest_counter_), end=" ")
				print("%s"%(adjust_text_by_spellpower(character.data.description, player.opponent, character)))
			print("========MY PLAYGROUND======")
			for character in player.characters:
				print("%s"%character, end='   : ')
				if character == player.hero:
					if player.weapon:
						print("(%2d/%2d/%2d+%d)(%s)"%(character.atk,player.weapon.durability,character.health,character.armor,player.weapon.data.name), end=" ")
					else:
						print("(%2d/%2d+%d)"%(character.atk,character.health,character.armor), end=" ")
				else :
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
				if character.can_attack():
					for target in character.targets:
						if character.can_attack(target):
							myH=character.health
							hisA=target.atk
							#if myH > hisA:
							myCandidate.append(Candidate(character, type=ActionType.ATTACK, target=target, turn=game.turn))
			if player.hero.power.is_usable():
				print("%s"%player.hero.power, end='   : ')
				print("<%2d>"%player.hero.power.cost, end=' ')
				print("%s"%adjust_text(player.hero.power.data.description))
				if player.hero.power.requires_target():
					for target in player.hero.power.targets:
						if player.hero.power.is_usable():
							myCandidate.append(Candidate(player.hero.power, type=BlockType.POWER, target=target, turn=game.turn))
				else:
					myCandidate.append(Candidate(player.hero.power, type=BlockType.POWER, target=None, turn=game.turn))
			print("========MY SECRETS======")
			for card in player.secrets:
				print("%s"%card, end='   : ')
				if hasattr(card, 'sidequest') or hasattr(card, 'questline'):
					print("(sidequest %d)"%card._sidequest_counter_, end="")
				print("%s"%(adjust_text(card.data.description)))
			print("========Your turn : %d/%d mana==(spell damage %d (fire %d))==="%(player.mana,player.max_mana,player.spellpower,player.spellpower_fire))
			print("[0] ターンを終了する")
			myCount = 1
			for myChoice in myCandidate:
				print('[%d]'%myCount, end=' ')
				myCard = myChoice.card
				print("%s"%myCard, end='  ')
				if myChoice.card2!=None:
					print("(%s)"%myChoice.card2, end=' ')
					if myCard.data.type==CardType.SPELL:
						print('<%2d> %s'%(myCard.cost, adjust_text_by_spellpower(myChoice.card2.data.description,player,myCard)), end=' ')
				else:
					if myCard.data.type==CardType.MINION:
						print('<%2d>(%2d/%2d)'%(myCard.cost, myCard.atk,myCard.health), end=' ')
					elif myCard.data.type==CardType.SPELL:
						print('<%2d> %s'%(myCard.cost, adjust_text_by_spellpower(myCard.data.description,player,myCard)), end=' ')
					elif myCard.data.type==CardType.WEAPON:
						print('<%2d> %s'%(myCard.cost, adjust_text_by_spellpower(myCard.data.description, player, myCard)), end=' ')
				if myChoice.type == ActionType.PLAY:
					print(' play', end=' ')
				if myChoice.type == ActionType.TRADE:
					print(' trade', end=' ')
				if myChoice.type == ActionType.ATTACK:
					print(' attack', end=' ')
				if myChoice.type == ActionType.POWER:
					print('<%2d> power'%(myCard.cost), end=' ')
				targetCard = myChoice.target
				if targetCard!=None:
					print("%s(%s)"%(targetCard, targetCard.controller.name), end=' ')
					if targetCard.data.type==CardType.MINION:
						print('(%2d/%2d)'%(targetCard.atk,targetCard.health), end=' ')
				myCount += 1
				print('')
			##analysis by vector
			vectorChoices=self.VectorKernel(game)
			print("Vector agent candidates:")
			for choice in vectorChoices:
				print("  %s"%(choice))
			##impout
			while True:
				str = input()
				try:
					inputNum = int(str)
					break;
				except ValueError:
					inputNum = 0
			if len(myCandidate)==0 or inputNum == 0:
				########################################
				#debug_board(new_game,game)###
				########################################
				break;
			if inputNum>0 and inputNum<=len(myCandidate):
				myChoice = myCandidate[inputNum-1]
				###################
				#executeAction(new_game, myChoice)#
				#postAction(new_game.current_player)#
				##################
				executeAction(game, myChoice)
				postAction(player)

	def HumanInputMulligan(self, choiceCards):
		myCount=1
		print("%s mulligan turn"%(self.name))
		for card in choiceCards:
			print("%d : %s"%(myCount,card), end='   : ')
			if card.data.type == CardType.MINION:
				print("%2d(%2d/%2d)%s"%(card.cost, card.atk, card.health, adjust_text(card.data.description)))
			elif card.data.type == CardType.SPELL:
				print("%2d : %s"%(card.cost, adjust_text(card.data.description)))
			elif card.data.type == CardType.WEAPON:
				print("%2d(%2d/%2d) : %s"%(card.cost, card.atk, card.durability, adjust_text(card.data.description)))
			myCount+=1
		print("Choose exchange cards (e.g. '1 3 4') ->")
		str = input()#やり直しはなし
		inputNums = str.split()#空白文字でスプリット
		cards_to_mulligan = []
		for inputStr in inputNums:
			try :
				inputNum = int(inputStr)
				cards_to_mulligan.append(choiceCards[inputNum-1])
			except ValueError :
				pass
		return cards_to_mulligan

	def HumanInputChoice(self, choiceCards):
		print("%s"%(self.choiceText))
		count=1
		for card in choiceCards:
			print("%d : %s (%s)"%(count, card.data.name, adjust_text(card.data.description)))
			count += 1
		str = input()#やり直しはなし
		try :
			inputNum = int(str)
			if inputNum>=1 and inputNum<=len(choiceCards):
				return choiceCards[inputNum-1]
		except ValueError :
			pass
		return random.choice(choiceCards)
	def VectorKernel(self, game):
		player=game.current_player
		cardList=[player.hero.id, player.hero.power.id]+list(set(player.starting_deck))
		myWeight=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]
		myCandidate = getCandidates(game)
		myChoices = []
		maxScore=-100000
		maxChoice = None
		for myChoice in myCandidate:
			tmpGame = fireplace_deepcopy(game)
			tmpGame.current_player.choiceStrategy=None
			result = executeAction(tmpGame, myChoice, debugLog=False)
			postAction(tmpGame.current_player)
			if result==ExceptionPlay.INVALID:
				stop=True
			if result==ExceptionPlay.GAMEOVER:
				score=100000
			elif myChoice.type==ExceptionPlay.TURNEND:
				score = self.vectorAgent.getStageScore(tmpGame,myWeight)
			else:
				loopCount=0
				while loopCount<20:
					loopCount+=1
					tmpCandidates = getCandidates(tmpGame)
					if len(tmpCandidates)>0:
						tmpChoice = random.choice(tmpCandidates)
						tmpResult = executeAction(tmpGame, tmpChoice, debugLog=False)
						postAction(tmpGame.current_player)
						if tmpResult==ExceptionPlay.GAMEOVER:
							score=100000
						elif tmpChoice.type==ExceptionPlay.TURNEND:
							score = self.vectorAgent.getStageScore(tmpGame,myWeight)
							break
						else:
							continue
					else:
						score = self.vectorAgent.getStageScore(tmpGame,myWeight)
						break
			if score > maxScore:
				maxScore = score
				myChoices = [myChoice]
				if score==100000:
					break
			elif score == maxScore:
				myChoices.append(myChoice)
		return myChoices

def weight_deepcopy(weight):
	wgt=[]
	for i in range(len(weight)):
		wgt.append(weight[i])
	return wgt



def debug_player_cards(player,old_player):
	print("=======%s HAND======"%(player))
	if len(player.hand)!=len(old_player.hand):
		print("length is different %d:%d"%(len(player.hand), len(old_player.hand)))
	for i in range(len(player.hand)):
		comment=""
		card = player.hand[i]
		if i>=len(old_player.hand):
			print ("XXX %s : no old cards here"%(card))
			continue
		old_card = old_player.hand[i]
		if card.id != old_card.id:
			print("XXX %s : old_name=%s"%(card,old_card))
		else:
			header=""
			footer=""
			if card.data.type == CardType.MINION:
				footer = "%s : %2d(%2d/%2d) "%(card, card.cost, card.atk, card.health)
				if card.cost != old_card.cost or card.atk != old_card.atk or card.health != old_card.health:
					footer += " old : %2d(%2d/%2d)"%(old_card.cost, old_card.atk, old_card.health)
					header = 'XXX'
				else:
					header = 'OOO'
			elif card.data.type == CardType.SPELL:
				footer = "%s : %2d  "%(card, card.cost)
				if card.cost != old_card.cost:
					footer += ", old : %2d"%(old_card.cost)
					header = 'XXX'
				else:
					header = 'OOO'
			elif card.data.type == CardType.WEAPON:
				footer = "%s : %2d(%2d/%2d)  "%(card, card.cost, card.atk, card.durability)
				if card.cost != old_card.cost or card.atk != old_card.atk or card.durability != old_card.durability:
					footer += ", old : %2d(%2d/%2d)"%(old_card.cost, old_card.atk, old_card.derability)
					header = 'XXX'
				else:
					header = 'OOO'
			print ("%s %s"%(header, footer))
		pass##
	print("========%s FIELD======"%(player))
	for i in range(len(player.characters)):
		header = footer =""
		character=player.characters[i]
		if i>=len(old_player.characters):
			print("XXX %s : no old card"%(character))
			continue
		old_character=old_player.characters[i]
		footer = "%s"%character
		if character.id != old_character.id:
			header = 'XXX'
			footer = "%s : old_name=%s"%(character, old_character)
		if character == player.hero:
			if player.weapon:
				footer += "(%2d/%2d/%2d+%d)"%(character.atk,player.weapon.durability,character.health,character.armor)
				if character.atk != old_character.atk or player.weapon.durability != old_player.weapon.durability or \
					character.health != old_character.health or character.armor != old_character.armor:
					footer += "(%2d/%2d/%2d+%d)"%(old_character.atk, old_player.weapon.durability, old_character.health, old_character.armor)
					header = 'XXX'
				else:
					header = 'OOO'
			else:
				footer += "(%2d/%2d+%d)"%(character.atk,character.health,character.armor)
				if character.atk != old_character.atk  or \
					character.health != old_character.health or character.armor != old_character.armor:
					footer += "(%2d/%2d+%d)"%(old_character.atk, old_character.health, old_character.armor)
					header = 'XXX'
				else:
					header = 'OOO'
		else :
			header = 'OOO'
			footer += "(%2d/%2d)"%(character.atk,character.health)
			if character.atk != old_character.atk or character.health != old_character.health:
				footer += "(%2d/%2d)"%(old_character.atk, old_character.health)
				header ='XXX'
			if character._Asphyxia_ == 'asphyxia':
				footer +="(Now Asphyxia %d)"%(character._sidequest_counter_)
				if old_character._Asphyxia != 'asphyxia':
					header ='XXX'
					footer += 'X'
			if character.silenced:
				footer +="(silenced)"
				if not old_character.silenced:
					header ='XXX'
					footer += 'X'
			if character.windfury:
				footer +="(windfury)"
				if not old_character.windfury:
					header ='XXX'
					footer += 'X'
			if character.poisonous:
				footer +="(poisonous)"
				if not old_character.poisonous:
					header ='XXX'
					footer += 'X'
			if character.frozen:
				footer +="(frozen)"
				if not old_character.frozen:
					header ='XXX'
					footer += 'X'
			if character.rush:
				footer +="(rush)"
				if not old_character.rush:
					header ='XXX'
					footer += 'X'
			if character.taunt:
				footer +="(taunt)"
				if not old_character.taunt:
					header ='XXX'
					footer += 'X'
			if character.immune:
				footer +="(immune)"
				if not old_character.immune:
					header ='XXX'
					footer += 'X'
			if character.stealthed:
				footer +="(stealthed)"
				if not old_character.stealthed:
					header ='XXX'
					footer += 'X'
			if character.divine_shield:
				footer +="(divine_shield)"
				if not old_character.divine_shield:
					header ='XXX'
					footer += 'X'
			if character.dormant>0:
				footer +="(dormant:%d)"%(character.dormant)
				if old_character.dormant<=0:
					header ='XXX'
					footer += 'X'
			elif character.dormant<0:
				if character._sidequest_counter_>0:
					footer +="(dormant:%d)"%(character._sidequest_counter_)
					if old_character.dormant>=0 or old_character._sidequest_counter_<=0:
						header ='XXX'
						footer += 'X'
				else:
					footer +="(dormant)"
			if character.spellpower>0:
				footer +="(spellpower:%d)"%(character.spellpower)
				if not old_character.spellpower > 0:
					header ='XXX'
					footer += 'X'
		print("%s %s"%(header, footer))
	if player.hero.power.is_usable():
		footer="%s<%2d>"%(player.hero.power, player.hero.power.cost)
		if player.hero.power != old_player.hero.power or player.hero.power.cost != old_player.hero.power.cost:
			footer += "%s<%2d>"%(old_player.hero.power, old_player.hero.power.cost)
			header ='XXX'
			footer += 'X'
		else:
			header = 'OOO'
		print("%s %s"%(header, footer))
	print("========%s SECRETS======"%(player))
	for i in range(len(player.secrets)):
		card = player.secrets[i]
		old_card = old_player.secrets[i]
		header = 'OOO'
		footer = "%s"%card
		if hasattr(card, 'sidequest') or hasattr(card, 'questline'):
			footer += "(sidequest %d)"%(card._sidequest_counter_)
			if card._sidequest_counter_ != old_card._sidequest_counter_:
				footer += "(sidequest %d)"%(old_card._sidequest_counter_)
				header = 'XXX'
		if card.id != old_card.id:
			footer += "(%s)"%old_card
			header = 'XXX'
	print("======== E N D =======")
	pass

def debug_board(new_game,old_game):
	player = new_game.current_player
	old_player = old_game.current_player
	print("========TURN : %d/%d mana==(spell damage %d (fire %d))==="%(player.mana,player.max_mana,player.spellpower,player.spellpower_fire))
	debug_player_cards(player,old_player)
	debug_player_cards(player.opponent,old_player.opponent)
	pass

def identityCandidates(can1, can2):
	if can1.card == None or can2.card == None:
		return False
	if can1.card.id != can2.card.id:
		return False
	if can1.card2 == None and can2.card2 != None:
		return False
	if can1.card2 != None and can2.card2 == None:
		return False
	if can1.card2 != None and can1.card2.id != can2.card2.id:
		return False
	if can1.type != can2.type:
		return False
	if can1.target != None and can2.target == None:
		return False
	if can1.target == None and can2.target != None:
		return False
	if can1.target != None and can2.target != None and can1.target.id != can2.target.id:
		return False
	return True

def compaireCandidates(old_can, new_can):
	print ("<><><><><><><><><comparing candidates starts<><><><><><><><><")
	for can1 in old_can:
		done = False
		for can2 in old_can:
			if identityCandidates(can1, can2):
				done = True
				break
			pass
		if not done:
			print(" %s(%s)%s does not exist in new candidates. "%(can1.card,can1.type,can1.target))
		pass
	for can2 in old_can:
		done = False
		for can1 in old_can:
			if identityCandidates(can1, can2):
				done = True
				break
			pass
		if not done:
			print(" %s(%s)%s does not exist in old candidates. "%(can2.card,can2.type,can2.target))
		pass
	print ("<><><><><><><><><comparing candidates ends<><><><><><><><><")
	pass

		
