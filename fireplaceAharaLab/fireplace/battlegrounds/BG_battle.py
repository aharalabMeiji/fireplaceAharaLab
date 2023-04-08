from fireplace.game import Game
from fireplace.deepcopy import deepcopy_game
from fireplace.actions import BG_Attack, Deaths, BeginBattle, EndBattle, BeginBattleTurn
import random
from hearthstone.enums import PlayState, Zone
from fireplace.config import Config
from fireplace.targeting import is_valid_target
import sys


class BG_Battle(Game):
	def __init__(self, bars):
		#we construct the battlefield from the data of players
		self.bar1=bars[0]
		self.bar2=bars[1]
		for card in self.bar1.controller.field:
			card.killed_in_former_battle=False
		for card in self.bar2.controller.field:
			card.killed_in_former_battle=False
		self.game1=deepcopy_game(bars[0], bars[0].controller, 0)
		self.game2=deepcopy_game(bars[1], bars[1].controller, 0)
		self.player1 = self.game1.player1
		self.player1.buddy_gauge = bars[0].controller.buddy_gauge
		self.player2 = self.game2.player1
		self.player2.buddy_gauge = bars[1].controller.buddy_gauge
		self.player1.deepcopy_original = bars[0].controller
		self.player2.deepcopy_original = bars[1].controller
		self.this_is_battle=True
		self.this_is_tavern=False

		super().__init__([self.player1, self.player2])
		## re-numbering for entity_id's
		count=1000
		for e in self.entities:
			e.entity_id = count
			count += 1
		for player,game in [(self.player1,self.game1), (self.player2,self.game2)]:## reviving aurabuff
			for buff in game.active_aura_buffs:
				for card in player.field:
					if buff in card.buffs:
						buff.tick = self.tick
						self.active_aura_buffs.append(buff)
		pass
	def __str__(self):
		return "BG_Battle(%s)vs(%s)"%(self.player1.name, self.player2.name)

	def battle(self):
		print("=============start the battle====================")
		#set their opponents
		self.player1.opponent=self.player2
		self.player2.opponent=self.player1
		if Config.BUDDY_SYSTEM:
			# move buddy gauges
			self.player1.buddy_gauge += (len(self.player1.field)*2+2)
			self.player2.buddy_gauge += (len(self.player2.field)*2+2)
		#determing first and second （if they have the same num of cards, random dice will be used.）
		#self.first  #self.second 
		if len(self.player1.field)>len(self.player2.field):
			self.first = self.player1
			self.second = self.player2
		elif len(self.player1.field)<len(self.player2.field):
			self.first = self.player2
			self.second = self.player1
		else:
			self.first = random.choice([self.player1, self.player2])
			self.second = self.first.opponent
		#let playstate be PLAYING.
		for player in self.players:
			player.playstate = PlayState.PLAYING
		#turn_begin for the event broadcasting
		BeginBattle(self.first).trigger(self)## trigger by game
		BeginBattle(self.second).trigger(self)## trigger by game
		#some parameters
		self.current_player=self.first
		self.first.attacker_index=0
		self.second.attacker_index=0
		self.first.controller.deepcopy_original.first_dead_minion=None
		self.second.controller.deepcopy_original.first_dead_minion=None
		self.first.controller.deepcopy_original.second_dead_minion=None
		self.second.controller.deepcopy_original.second_dead_minion=None
		# starting the infinite loop
		while True:
			BeginBattleTurn(self.current_player)
			# display the field
			self.printField()
			# check if the battle ends
			if len(self.first.field)==0 or len(self.second.field)==0:
				break
			#attacker
			attacker = self.current_player.field[self.current_player.attacker_index]
			if attacker.atk>0:
				for repeat in range(attacker.windfury+1):## procedure for windfury
					#defender
					taunts=[]
					for card in self.current_player.opponent.field:
						if card.taunt:
							taunts.append(card)
					if len(taunts)>0:
						defenders = taunts
					else:
						defenders = [card for card in attacker.attack_targets if card in self.current_player.opponent.field]
					if len(defenders)>0:
						if attacker.id =='BGS_022' or attacker.id=='TB_BaconUps_091':## Zapp Slywick
							lowest_attack=[]
							for card in defenders:
								if lowest_attack==[]:
									lowest_attack = [card]
								elif lowest_attack[0].atk>card.atk:
									lowest_attack = [card]
								elif lowest_attack[0].atk==card.atk:
									lowest_attack.append(card)
							defenders = lowest_attack
						defender=random.choice(defenders)
						#attack
						#print("%s(%s) -> %s(%s) : "%(attacker, attacker.controller, defender, defender.controller))
						BG_Attack(attacker, defender).trigger(attacker.controller)
						#move buddy gauge, before 23.1
						if Config.BUDDY_SYSTEM:
							self.player1.buddy_gauge += (attacker.atk+defender.atk)*0.5
							self.player2.buddy_gauge += (attacker.atk+defender.atk)*0.5
						##procedures of deathrattle
						#Deaths().trigger(self)
						if attacker.zone==Zone.GRAVEYARD:
							if defender.controller.deepcopy_original.first_dead_minion==None:
								defender.controller.deepcopy_original.first_dead_minion=attacker.id
							elif defender.controller.deepcopy_original.second_dead_minion==None:
								defender.controller.deepcopy_original.second_dead_minion=attacker.id
						if defender.zone==Zone.GRAVEYARD:
							if attacker.controller.deepcopy_original.first_dead_minion==None:
								attacker.controller.deepcopy_original.first_dead_minion=defender.id
							elif attacker.controller.deepcopy_original.second_dead_minion==None:
								attacker.controller.deepcopy_original.second_dead_minion=defender.id
						if len(self.first.field)==0 or len(self.second.field)==0:
							break
						if sum([card.atk for card in self.first.field])==0 and sum([card.atk for card in self.second.field])==0:
							break
						if attacker.zone==Zone.GRAVEYARD:
							self.current_player.attacker_index-=1##adjustion
							break;
			# change the turn (no freeze nor one_turn_effect)
			self.current_player.attacker_index+=1
			if self.current_player.attacker_index>= len(self.current_player.field):
				self.current_player.attacker_index=0
			self.current_player = self.current_player.opponent
			if self.current_player.attacker_index>= len(self.current_player.field):
				self.current_player.attacker_index=0
			pass
		#end of the battle
		#self.state = State.COMPLETE
		#self.manager.step(self.next_step, Step.FINAL_WRAPUP)
		#self.manager.step(self.next_step, Step.FINAL_GAMEOVER)
		#self.manager.step(self.next_step)
		print("=============end the battle====================")
		EndBattle(self.first).trigger(player)
		EndBattle(self.second).trigger(player)
		# draw
		if (len(self.first.field)==0 and len(self.second.field)==0) or (sum([card.atk for card in self.first.field])==0 and sum([card.atk for card in self.second.field])==0):
			#move buddy gauge
			if Config.NEW_BUDDY_SYSTEM:
				self.player1.buddy_gauge = max(self.player1.buddy_gauge-3, 0)
				self.player2.buddy_gauge = max(self.player2.buddy_gauge-3, 0)
			elif Config.BUDDY_SYSTEM:
				self.player1.buddy_gauge += 1
				self.player2.buddy_gauge += 1
			ret = 0,0,self.player1.buddy_gauge,self.player2.buddy_gauge
			del self.game1
			del self.game2
			return ret #
		elif len(self.player1.field)==0:
			# get "sum of tech_levels of the winner + winners tier"
			damage = self.player2.tavern_tier
			for card in self.player2.field:
				if hasattr(card,'tech_level'):
					damage += card.tech_level
				else:
					damage += card.cost# or 1?
			# return the damages for heroes
			if Config.NEW_BUDDY_SYSTEM:
				self.player1.buddy_gauge = max(self.player1.buddy_gauge-2, 0)
				self.player2.buddy_gauge = max(self.player2.buddy_gauge-3, 0)
			elif Config.BUDDY_SYSTEM:
				self.player1.buddy_gauge += (damage)
				self.player1.buddy_gauge += 3
			ret = damage, 0,self.player1.buddy_gauge,self.player2.buddy_gauge
			del self.game1
			del self.game2
			return ret #
		else:#if len(self.player2.field)==0:
			# get "sum of tech_levels of the winner + winners tier"
			damage = self.player1.tavern_tier
			for card in self.player1.field:
				if hasattr(card,'tech_level'):
					damage += card.tech_level
				else:
					damage += card.cost# or 1?
			# return the damages for heroes
			if Config.NEW_BUDDY_SYSTEM:
				self.player1.buddy_gauge = max(self.player1.buddy_gauge-3, 0)
				self.player2.buddy_gauge = max(self.player2.buddy_gauge-2, 0)
			elif Config.BUDDY_SYSTEM:
				self.player2.buddy_gauge += (damage)
				self.player2.buddy_gauge += 3
			ret= 0, damage, self.player1.buddy_gauge, self.player2.buddy_gauge
			del self.game1
			del self.game2
			return ret #
		pass

	def printField(self):
		print("========%s========"%self.first.name)
		for card in self.first.field:
			print("%s:%s"%(self.first.name, self.card_stats(card)))
		print("--------%s--------"%self.second.name)
		for card in self.second.field:
			print("%s:%s"%(self.second.name, self.card_stats(card)))
		print("========[over]========")
	
	def card_stats(self, card):
		ret = ' %s'%(card)
		ret += '(%d/%d)'%(card.atk,card.health)
		if card.cant_play:
			ret += "(can't play)"
		if card.frozen:
			ret += "(frozen)"
		if card.taunt:
			ret += "(taunt)"
		if card.divine_shield:
			ret += "(divine_shield)"
		if card.windfury:
			ret += "(windfury)"
		if card.poisonous:
			ret += "(poisonous)"
		if card.reborn:
			ret += "(reborn)"
		if card.stealthed:
			ret += "(stealthed)"
		return ret

	def BG_morph_gold(self, card):
		if not card:
			return
		controller = card.controller
		if not card in controller.field:
			return
		index = controller.field.index(card)
		gold_id = self.parent.BG_Gold.get(card.id, 0)
		if not gold_id:
			return
		buffs=[]
		for buff in card.buffs:## inherits buffs
			buffs.append(buff)
		card.discard()
		newcard = controller.card(gold_id)
		for buff in buffs:## inherits buffs
			buff.apply(newcard)
		newcard._summon_index=index
		newcard.zone = Zone.PLAY #something wrong? 
		return newcard
