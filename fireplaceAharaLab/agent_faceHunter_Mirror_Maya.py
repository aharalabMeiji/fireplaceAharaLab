#faceHunter_Mirror_Maya
import os.path
import numpy as np
import random
from bisect import bisect
from importlib import import_module
from pkgutil import iter_modules
from typing import List
import copy
from hearthstone.enums import CardClass, CardType,PlayState, Zone,State#
import time#
import sys
from fireplace.card import Card
from fireplace.exceptions import GameOver
from fireplace.utils import random_draft,CardList
from fireplace.deck import Deck
from utils import *
import gc
class faceHunter_Mirror_Maya(Agent):
	"""docstring for faceHunter_Mirror_Maya"""
	def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000 ):
		#hp_self,mp_self,Hand_num,Sumpow_self,Maxpow_self,Manaratio_1_self,oppo,
		super().__init__(myName, myFunction, myOption, myClass, rating )
		pass
	def faceHunter_Mirror_MayaAI(self, game: Game, option=[0, -0.3263461334873176, -0.4323907113138038,0,0, 0.6836399534561048,-0.4784578333894103,0,0,0, 0.10124717099389445,0], gameLog=[], debugLog=False):
		while True:
			self.taking_action=self.choose_action(game)
			if self.taking_action.type ==ExceptionPlay.TURNEND:
				return ExceptionPlay.VALID
				pass
			self.exc=executeAction(game, self.taking_action,debugLog=True)
			postAction(game.current_player)
			if self.exc==ExceptionPlay.GAMEOVER:
				return ExceptionPlay.GAMEOVER
			else:
				continue
		return ExceptionPlay.VALID
	def choose_action(self,_game):
		#
		self.copyGame=_game
		self.candidates=getCandidates(_game,_includeTurnEnd=True)
		if len(self.candidates)==0:
			return self.candidates[0]
			pass
		games=[copy.deepcopy(self.copyGame) for i in self.candidates]
		score_for_action=list(map(self.evaluate_action,games,self.candidates))
		return self.candidates[score_for_action.index(max(score_for_action))]
		pass
	def evaluate_action(self,_game,_candidate,_recursive=0):
		if _candidate.type==ExceptionPlay.TURNEND or _recursive>1:
			return self.calculate_score(_game)#score
			pass
		executeAction(_game,_candidate,debugLog=False)
		postAction(_game.current_player)
		candidates=getCandidates(_game,_includeTurnEnd=False)
		if len(candidates)==0:
			gc.collect()
			return self.calculate_score(_game)#score
			pass
		else:
			new_games=[copy.deepcopy(_game) for i in candidates]
			recursive=[_recursive+1 for i in range(len(candidates))]
			return max(list(map(self.evaluate_action,new_games,candidates,recursive)))
		pass
	def calculate_score(self,_game:Game):
		if _game.state==State.COMPLETE:
			#print("the game has been finished")
			if _game.current_player.playstate == PlayState.WON:
				return 10000000
			else :
				return -10000000
			pass
		self.my_player=_game.current_player
		self.enemy=self.my_player.opponent
		my_HP=self.my_player.hero.health
		my_MP=self.my_player.mana
		hand_num=len(self.my_player.hand)
		my_characters_power=list(map(lambda char:char.atk,self.my_player.characters))
		num_minion_self=len(self.my_player.characters)
		sumpow_self=sum(my_characters_power)
		maxpow_self=max(my_characters_power)
		enemy_HP=self.enemy.hero.health
		enemy_MP=self.enemy.mana
		enemy_Hand_num=len(self.enemy.hand)
		enemy_characters_power=list(map(lambda char:char.atk,self.enemy.characters))
		num_minion_enemy=len(self.enemy.characters)
		sumpow_enemy=sum(enemy_characters_power)
		maxpow_enemy=max(enemy_characters_power)
		factors=[my_HP,my_MP,hand_num,sumpow_self,num_minion_enemy,maxpow_self,enemy_HP,enemy_MP,enemy_Hand_num,num_minion_enemy,sumpow_enemy,maxpow_enemy]
		return np.dot(np.array(self.option),np.array(factors))
		pass
