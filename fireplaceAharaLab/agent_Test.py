import random
import copy
from fireplace.exceptions import GameOver
from hearthstone.enums import CardType, BlockType, CardClass
from utils import ExceptionPlay, Candidate, executeAction, getCandidates, postAction, Agent
from fireplace.actions import Action
from fireplace.card import Card
from fireplace.game import Game
from fireplace.utils import ActionType
from enum import IntEnum


class TestHumanAgent(Agent):
	def __init__(self, myName: str, myFunction, myOption=[], myClass: CardClass = CardClass.HUNTER, rating=1000, mulliganStrategy=None, choiceStrategy=None):
		super().__init__(myName, myFunction, myOption, myClass,
						 rating, mulliganStrategy=mulliganStrategy, choiceStrategy=choiceStrategy)
		pass

	def HumanInput(self, game, option=None, gameLog=[], debugLog=True):
		player = game.current_player
		while True:
			myCandidate = []
			# for character in player.characters:
			#	 if hasattr(character, 'zone_position'):
			#		 print(f"{character}のポジションは{character.zone_position}")
			# for character in player.opponent.characters:
			#	 if hasattr(character, 'zone_position'):
			#		 print(f"{character}のポジションは{character.zone_position}")
		
			print("========My HAND======")
			for card in player.hand:
				print("%s" % card, end='   : ')
				if card.data.type == CardType.MINION:
					print("%2d(%2d/%2d)%s" % (card.cost, card.atk, card.health,
							adjust_text_bt_spellpower(card.data.description, player)))
				elif card.data.type == CardType.SPELL:
					print("%2d : %s" % (card.cost, adjust_text_bt_spellpower(
						card.data.description, player)))
				elif card.data.type == CardType.WEAPON:
					print("%2d(%2d/%2d) : %s" % (card.cost, card.atk, card.durability,
							adjust_text_bt_spellpower(card.data.description, player)))
					##
				if card.is_playable():
					if card.must_choose_one:
						for card2 in card.choose_cards:
							if card2.is_playable():
								if card2.requires_target():
									for target in card2.targets:
										myCandidate.append(Candidate(
											card, card2=card2, type=ActionType.PLAY, target=target, turn=game.turn))
								else:
									myCandidate.append(Candidate(
										card, card2=card2, type=ActionType.PLAY, target=None, turn=game.turn))
					else:  # card2=None
						if card.requires_target():
							for target in card.targets:
								myCandidate.append(
									Candidate(card, type=ActionType.PLAY, target=target, turn=game.turn))
						else:
							myCandidate.append(
								Candidate(card, type=ActionType.PLAY, target=None, turn=game.turn))
				_yes, _option = card.can_trade()
				if _yes:
					myCandidate.append(
						Candidate(card, type=ActionType.TRADE, target=None, turn=game.turn))
			print("========OPPONENT'S PLAYGROUND======")
			for character in player.opponent.characters:
				print("%s" % character, end='   : ')
				if character == player.opponent.hero:
					if player.opponent.weapon:
						print("(%2d/%2d/%2d+%d)(%s)"%(character.atk, player.opponent.weapon.durability, character.health,character.armor,player.opponent.weapon.data.name), end=" ")
					else:
						print("(%2d/%2d+%d)"%(character.atk, character.health, character.armor), end=" ")
				else:
					print("(%2d/%2d)" %(character.atk, character.health), end=" ")
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
					# if character.reborn:
					#	print("(reborn)", end=" ")
					if character.taunt:
						print("(taunt)", end=" ")
					if character.immune:
						print("(immune)", end=" ")
					if character.divine_shield:
						print("(divine_shield)", end=" ")
					if character.dormant > 0:
						print("(dormant:%d)" % (character.dormant), end=" ")
					elif character.dormant < 0:
						if character._sidequest_counter_ > 0:
							print("(dormant:%d)" % (character._sidequest_counter_), end=" ")
						else:
							print("(dormant)", end=" ")
					# if character._sidequest_counter_>0:
					#	if character.dormant==0:
					#		print("(sidequest:%d)"%(character._sidequest_counter_), end=" ")
				print("%s" % (adjust_text_bt_spellpower(character.data.description, player.opponent)))
			print("========MY PLAYGROUND======")
			for character in player.characters:
				print("%s" % character, end='   : ')
				if character == player.hero:
					if player.weapon:
						print("(%2d/%2d/%2d+%d)(%s)"%(character.atk, player.weapon.durability, character.health,character.armor,player.weapon.data.name), end=" ")
					else:
						print("(%2d/%2d+%d)"%(character.atk, character.health, character.armor), end=" ")
				else:
					print("(%2d/%2d)" %(character.atk, character.health), end=" ")
					if character._Asphyxia_ == 'asphyxia':
						print("(Now Asphyxia %d)" % (character._sidequest_counter_), end=' ')
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
					# if character.reborn:
					#	print("(reborn)", end=" ")
					if character.taunt:
						print("(taunt)", end=" ")
					if character.immune:
						print("(immune)", end=" ")
					if character.stealthed:
						print("(stealthed)", end=" ")
					if character.divine_shield:
						print("(divine_shield)", end=" ")
					if character.dormant > 0:
						print("(dormant:%d)" % (character.dormant), end=" ")
					elif character.dormant < 0:
						if character._sidequest_counter_ > 0:
							print("(dormant:%d)" % (character._sidequest_counter_), end=" ")
						else:
							print("(dormant)", end=" ")
					if character.spellpower > 0:
						print("(spellpower:%d)" % (character.spellpower), end=" ")
				print("%s" % (adjust_text_bt_spellpower(character.data.description, player)))
				if character.can_attack():
					for target in character.targets:
						if character.can_attack(target):
							myH = character.health
							hisA = target.atk
							# if myH > hisA:
							myCandidate.append(
								Candidate(character, type=ActionType.ATTACK, target=target, turn=game.turn))
			if player.hero.power.is_usable():
				print("%s" % player.hero.power, end='   : ')
				print("<%2d>" % player.hero.power.cost, end=' ')
				print("%s"%player.hero.power.data.description.replace('\n', '').replace('[x]', '').replace('[','[').replace(']',']'))
				if player.hero.power.requires_target():
					for target in player.hero.power.targets:
						if player.hero.power.is_usable():
							myCandidate.append(Candidate(
								player.hero.power, type=BlockType.POWER, target=target, turn=game.turn))
				else:
					myCandidate.append(Candidate(
						player.hero.power, type=BlockType.POWER, target=None, turn=game.turn))
			print("========MY SECRETS======")
			for card in player.secrets:
				print("%s" % card, end='   : ')
				if hasattr(card, 'sidequest') or hasattr(card, 'questline'):
					print("(sidequest %d)" % card._sidequest_counter_, end="")
				print("%s" %(adjust_text_bt_spellpower(card.data.description, 0)))
			print("========Your turn : %d/%d mana==(spell damage %d)==="%(player.mana, player.max_mana, player.spellpower))
			print("[0] ターンを終了する")
			myCount = 1
			for myChoice in myCandidate:
				print('[%d]' % myCount, end=' ')
				myCard = myChoice.card
				print("%s" % myCard, end='  ')
				if myChoice.card2 != None:
					print("(%s)" % myChoice.card2, end=' ')
				if myCard.data.type == CardType.MINION:
					print('<%2d>(%2d/%2d)' %(myCard.cost, myCard.atk, myCard.health), end=' ')
				elif myCard.data.type == CardType.SPELL:
					print('<%2d> %s' %(myCard.cost, adjust_text_bt_spellpower(myCard.data.description, player)), end=' ')
				elif myCard.data.type == CardType.WEAPON:
					print('<%2d> %s' % (myCard.cost, adjust_text_bt_spellpower(myCard.data.description, player)), end=' ')
				if myChoice.type == ActionType.PLAY:
					print(' play', end=' ')
				if myChoice.type == ActionType.TRADE:
					print(' trade', end=' ')
				if myChoice.type == ActionType.ATTACK:
					print(' attack', end=' ')
				if myChoice.type == ActionType.POWER:
					print('<%2d> power' % (myCard.cost), end=' ')
				targetCard = myChoice.target
				if targetCard != None:
					print("%s(%s)" % (targetCard, targetCard.controller.name), end=' ')
					if targetCard.data.type == CardType.MINION:
						print('(%2d/%2d)' %(targetCard.atk, targetCard.health), end=' ')
				myCount += 1
				print('')
			while True:
				str = input()
				try:
					inputNum = int(str)
					break
				except ValueError:
					inputNum = 0
			if len(myCandidate) == 0 or inputNum == 0:
				break
			if inputNum > 0 and inputNum<=len(myCandidate):
				myChoice = myCandidate[inputNum-1]
				executeAction(game, myChoice)
				postAction(player)

	def HumanInputMulligan(self, choiceCards):
		myCount = 1
		print("%s mulligan turn" % (self.name))
		for card in choiceCards:
			print("%d : %s" %(myCount, card), end='   : ')
			if card.data.type == CardType.MINION:
				print("%2d(%2d/%2d)%s"%(card.cost, card.atk, card.health, card.data.description.replace('\n', '').replace('[x]', '').replace('[','[').replace(']',']')))
			elif card.data.type == CardType.SPELL:
				print("%2d : %s"%(card.cost, card.data.description.replace('\n', '').replace('[x]', '').replace('[','[').replace(']',']')))
			elif card.data.type == CardType.WEAPON:
				print("%2d(%2d/%2d) : %s"%(card.cost, card.atk, card.durability, card.data.description.replace('\n', '').replace('[x]', '').replace('[','[').replace(']',']')))
			myCount += 1
		print("Choose exchange cards (e.g. '1 3 4') ->")
		str = input()  # やり直しはなし
		inputNums = str.split()  # 空白文字でスプリット
		cards_to_mulligan = []
		for inputStr in inputNums:
			try:
				inputNum = int(inputStr)
				cards_to_mulligan.append(choiceCards[inputNum-1])
			except ValueError:
				pass
		return cards_to_mulligan

	def HumanInputChoice(self, choiceCards):
		print("%s"%(self.choiceText))
		count=1
		for card in choiceCards:
			print("%d : %s (%d) %s"%(count, card.data.name, card.cost, adjust_text_bt_spellpower(card.data.description, self)))
			count += 1
		str = input()#やり直しはなし
		try :
			inputNum = int(str)
			if inputNum>=1 and inputNum<=len(choiceCards):
				return choiceCards[inputNum-1]
		except ValueError :
			pass
		return random.choice(choiceCards)

def adjust_text_bt_spellpower(text, player):
	_catch_number=-1
	_new_text=text.replace('\n','').replace('[x]','').replace('[','[').replace(']',']')
	_len=len(_new_text)
	for _i in range(_len):
		if _new_text[_i]=='$':
			if _i+1<_len and _new_text[_i+1] in ['0','1','2','3','4','5','6','7','8','9']:
				_catch_number = int(_new_text[_i+1])
				_latter_text = _new_text[_i+2:]
				if _i+2<_len and _new_text[_i+2] in ['0','1','2','3','4','5','6','7','8','9']:
					_catch_number *= 10
					_catch_number += int(_new_text[_i+2])
					_latter_text = _new_text[_i+3:]
				_catch_number += player.spellpower
				for _repeat in range(player.spellpower_double):
					_catch_number *= 2
				_new_text = _new_text[:_i] + "*" +str(_catch_number) +"*" + _latter_text
	return _new_text
