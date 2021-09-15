import random
import copy
from fireplace.exceptions import GameOver
from hearthstone.enums import CardType, BlockType, CardClass, SpellSchool#
from utils import ExceptionPlay, Candidate, executeAction, getCandidates, postAction,Agent
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
				else:
					continue
			return ExceptionPlay.VALID


class StandardVectorAgent(Agent):
	def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000, mulliganStrategy=None):
		super().__init__(myName, myFunction, myOption, myClass, rating, mulliganStrategy=mulliganStrategy )
		self.__standard_agent__=StandardAgent("Standard",StandardAgent.StandardRandom, myClass=myClass)
		pass
	def StandardStep1(self, game, option=None, gameLog=[], debugLog=True):	
		debug=False
		if option==None:
			print ("StandardStep1 needs an option")
			return ExceptionPlay.INVALID
		myWeight=option
		myCandidate = getCandidates(game)
		myChoices = []
		maxScore=-100000
		maxChoice = None
		if debug:
			print(">>>>>>>>>>>>>>>>>>>")
		for myChoice in myCandidate:
			tmpGame = copy.deepcopy(game)
			if executeAction(tmpGame, myChoice, debugLog=False)==ExceptionPlay.GAMEOVER:
				score=100000
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
			ret = executeAction(game, myChoice,debugLog=debugLog)
			if ret==ExceptionPlay.GAMEOVER:
				return ExceptionPlay.GAMEOVER
			if ret==ExceptionPlay.INVALID:
				return ExceptionPlay.INVALID
			player = game.current_player
			postAction(player)
			return self.StandardStep1(game, option=myWeight, debugLog=debugLog)
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
		w[0] = myHero.health
		#w[1]=hisHeroH
		w[1] = hisHero.health
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
		pass
	def HumanInput(self, game, option=None, gameLog=[], debugLog=True):
		player = game.current_player
		while True:
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
					#if character.reborn:
					#	print("(reborn)", end=" ")
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
					#if character.reborn:
					#	print("(reborn)", end=" ")
					if character.taunt:
						print("(taunt)", end=" ")
					if character.immune:
						print("(immune)", end=" ")
					if character.stealthed:
						print("(stealthed)", end=" ")
					if character.divine_shield:
						print("(divine_shield)", end=" ")
					if character.dormant>0:
						print("(dormant:%d)"%(character.dormant), end=" ")
					elif character.dormant<0:
						if character._sidequest_counter_>0:
							print("(dormant:%d)"%(character._sidequest_counter_), end=" ")
						else:
							print("(dormant)", end=" ")
					if character.spellpower>0:
						print("(spellpower:%d)"%(character.spellpower), end=" ")
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
			while True:
				str = input()
				try:
					inputNum = int(str)
					break;
				except ValueError:
					inputNum = 0
			if len(myCandidate)==0 or inputNum == 0:
				break;
			if inputNum>0 and inputNum<=len(myCandidate):
				myChoice = myCandidate[inputNum-1]
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



def weight_deepcopy(weight):
	wgt=[]
	for i in range(len(weight)):
		wgt.append(weight[i])
	return wgt

