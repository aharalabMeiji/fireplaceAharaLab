from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit

def SimulateGames_Alterac_Neutral():

	#PresetGame(pp_AV_100,1)####OK
	#PresetGame(pp_AV_101,1)####OK###OK(2-10-22)
	#PresetGame(pp_AV_102,1)####OK
	#PresetGame(pp_AV_112,1)####OK
	#PresetGame(pp_AV_121,1)####OK
	#PresetGame(pp_AV_122,1)####OK
	#PresetGame(pp_AV_123,1)####OK
	#PresetGame(pp_AV_124,2)####OK
	#PresetGame(pp_AV_125,1)####OK
	#PresetGame(pp_AV_126,1)####OK
	#PresetGame(pp_AV_127,1)####OK
	#PresetGame(pp_AV_129,1)####OK
	#PresetGame(pp_AV_130,1)####OK
	#PresetGame(pp_AV_131,1)####OK
	#PresetGame(pp_AV_132,1)####OK
	#PresetGame(pp_AV_133,1)####OK
	#PresetGame(pp_AV_134,1)####OK
	#PresetGame(pp_AV_135,1)####OK
	#PresetGame(pp_AV_136,1)####OK
	#PresetGame(pp_AV_136t,1)###OK
	#PresetGame(pp_AV_137,1)####OK
	#PresetGame(pp_AV_138,1)####TRY SOME TIMES ####OK
	#PresetGame(pp_AV_139,1)####OK
	#PresetGame(pp_AV_141t,1)###OK
	#PresetGame(pp_AV_142t,1)###OK
	#PresetGame(pp_AV_143,1)####OK
	#PresetGame(pp_AV_215,2)####OK
	#PresetGame(pp_AV_219,1)####OK
	#PresetGame(pp_AV_222,1)####OK
	#PresetGame(pp_AV_223,1)####OK
	#PresetGame(pp_AV_238,1)####OK
	#PresetGame(pp_AV_256,1)####OK
	#PresetGame(pp_AV_309,1)####OK
	#PresetGame(pp_AV_401,1)####OK
	#PresetGame(pp_AV_704,1)####OK
	#PresetGame(pp_ONY_001,1)####OK
	#PresetGame(pp_ONY_002,1)####OK
	#PresetGame(pp_ONY_003,1)####OK
	#PresetGame(pp_ONY_004,1)####OK
	#PresetGame(pp_ONY_005,1)#### now under pending
	pass

from hearthstone.enums import Zone,CardType, Rarity

class pp_AV_100(Preset_Play):
	"""Drek'Thar (4/4/4)
	[Battlecry]: If this costs more than every minion in your deck, summon 2 of them. """
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		deck = controller.deck
		leng = len(deck)
		i=0
		while True:
			card = deck[i]
			if card.cost>=4 and card.type==CardType.MINION:
				card.zone=Zone.GRAVEYARD
				leng -= 1
			else:
				i += 1
			if leng==i:
				break
			pass
		self.mark1=self.exchange_card('AV_100',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		###########
		self.play_card(self.mark1, controller)
	def result_inspection(self):
		super().result_inspection()
		# デッキからカードを2枚召喚しているかどうかをチェック

		pass
	pass

class pp_AV_101(Preset_Play):
	""" Herald of Lokholar (4/3/5)
	[Battlecry]: Draw a Frost spell."""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_101',controller)
		self.mark2=self.append_deck_shuffle('frost',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		self.play_card(self.mark1, controller)
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		## 自然系のカードをデッキから一枚引いているできればself.mark2
		for card in controller.hand:
			self.print_stats("controller.hand",card)
		for card in [self.mark2]:
			self.print_stats("self.mark2",card)

		pass
	pass

class pp_AV_102(Preset_Play):
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_102',controller)
		self.mark2=self.exchange_card('vanillaH3',opponent)
		self.mark3=self.exchange_card('vanilla',opponent)
		self.mark4=self.exchange_card('vanilla',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		self.play_card(self.mark1, controller)
		self.change_turn(controller)
		##########
		self.play_card(self.mark2, opponent)
		self.play_card(self.mark3, opponent)
		self.play_card(self.mark4, opponent)
		self.change_turn(opponent)
		#############
		self.attack_card(self.mark1, self.mark2, controller)
	def result_inspection(self):
		super().result_inspection()
		#ミニオン2体が凍っている
		if self.mark3.frozen:
			print("check 1 OK")
		if self.mark4.frozen:
			print("check 1 OK")
		pass
	pass

class pp_AV_112(Preset_Play):
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_112',controller)
		self.mark2=self.exchange_card('frost',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		self.play_card(self.mark1, controller)
	def result_inspection(self):
		super().result_inspection()
		#armorが5増えてる
		if self.player.hero.armor == 5:
			print("check 1 OK")
	pass
	pass

class pp_AV_121(Preset_Play):
	const=0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_121',controller)
		self.const = self.mark1.atk
		self.mark2=self.exchange_card('vanillaH1',opponent)
		self.mark3=self.exchange_card('vanillaH2',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########
		self.play_card(self.mark1, controller)
		self.change_turn(controller)
		##########
		self.play_card(self.mark2, opponent)
		self.change_turn(opponent)
		#############
		self.attack_card(self.mark1, self.mark2, controller)
	def result_inspection(self):
		super().result_inspection()
		if self.contains_buff(self.mark1, 'AV_121e'):
			print("check 1 OK")
		if self.mark1.atk - self.const == 2:
			print("check 2 OK")
		pass
	pass

class pp_AV_122(Preset_Play):
	""" Honorable Kill: Give your other minions Divine Shield."""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_122',controller)
		self.mark2=self.exchange_card('vanillaH2',opponent)
		self.mark3=self.exchange_card('vanilla',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		self.play_card(self.mark1, controller)
		self.play_card(self.mark3, controller)
		self.change_turn(controller)
		##########
		self.play_card(self.mark2, opponent)
		self.change_turn(opponent)
		#############
		self.attack_card(self.mark1, self.mark2, controller)
	def result_inspection(self):
		super().result_inspection()
		#mark3にdivine shieldがついているかどうかを見る。
		if self.mark3.divine_shield:
			print("check 1 OK")
		pass
	pass

class pp_AV_123(Preset_Play):
	""" Sneaky Scout (2/3/2)
	[Stealth] [Honorable Kill]: Your next Hero Power costs (0). """
	const1=0
	const2=0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_123',controller)
		self.mark2=self.exchange_card('vanillaH3',opponent)
		self.mark3=self.exchange_card('vanilla',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########
		self.play_card(self.mark1, controller)
		self.const1 = controller.hero.power.cost
		self.change_turn(controller)
		##########
		self.play_card(self.mark2, opponent)
		self.change_turn(opponent)
		#############
		self.attack_card(self.mark1, self.mark2, controller)
		self.const2 = controller.hero.power.cost
	def result_inspection(self):
		super().result_inspection()
		#ヒロパのコストが０になる。
		print ("The cost of hero-power: %d -> %d"%(self.const1, self.const2))
		pass
	pass

class pp_AV_124(Preset_Play):
	const1=0
	const2=0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_124',controller)
		self.mark2=self.exchange_card('vanilla',controller)
		if self.testNr==0:
			self.mark3=self.exchange_card('vanillaH2',opponent)
		if self.testNr==1:
			self.mark3=self.exchange_card('vanillaH1',opponent)
		self.mark4=self.exchange_card('vanilla',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		self.play_card(self.mark1, controller)
		self.play_card(self.mark2, controller)
		self.change_turn(controller)
		##########
		self.play_card(self.mark3, opponent)
		self.play_card(self.mark4, opponent)
		self.change_turn(opponent)
		#############
		self.const1 = self.mark1.atk
		self.const2 = self.mark3.health
		self.attack_card(self.mark1, self.mark3, controller)
	def result_inspection(self):
		super().result_inspection()
		#mark1がhonorable_killタグをもっているか。
		if hasattr(self.mark1, 'honorable_kill') and self.mark1.honorable_kill:
			print("check 1 OK")
		#Honorable Kill 発動条件
		print("%d - %d == 0"%(self.const1, self.const2))
		#Honorable Kill 発動しているか
		if self.card_in_field(self.player, 'AV_211t'):
			print("check 2 OK")
		else:
			print("check 2 NG")

class pp_AV_125(Preset_Play):
	""" Tower Sergeant (4/4/4)
	[Battlecry]: If you control at least 2 other minions, gain +2/+2."""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_125',controller)
		self.mark2=self.exchange_card('vanillaH1',controller)
		self.mark3=self.exchange_card('vanillaH2',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		self.play_card(self.mark2, controller)
		self.play_card(self.mark3, controller)
		self.play_card(self.mark1, controller)
	def result_inspection(self):
		super().result_inspection()
		if self.contains_buff(self.mark1,'AV_125e'):
			print ("check 1 OK: stats is %d/%d"%(self.mark1.atk, self.mark1.health))
		pass
	pass

class pp_AV_126(Preset_Play):
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_126',controller)
		self.mark2=self.exchange_card('vanilla',controller)
		self.mark3=self.exchange_card('vanilla',opponent)
		self.mark4=self.exchange_card('vanilla',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		self.play_card(self.mark2, controller)
		self.change_turn(controller)
		##########
		self.play_card(self.mark3, opponent)
		self.play_card(self.mark4, opponent)
		self.change_turn(opponent)
		#############
		self.play_card(self.mark1, controller)
	def result_inspection(self):
		super().result_inspection()
		## mark3がダメージ1を受けているか
		## mark4がダメージ1を受けているか
		## mark4をプレイしなければダメージ攻撃がないか
	pass

class pp_AV_127(Preset_Play):
	""" Ice Revenant (4/4/5)
	Whenever you cast a Frost spell, gain +2/+2. """
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_127',controller)
		self.mark2=self.exchange_card('frost',controller)
		self.mark3=self.exchange_card('frost',opponent)
		self.mark4=self.exchange_card('vanilla',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		self.play_card(self.mark1, controller)
		self.play_card(self.mark2, controller)
		self.play_card(self.mark3, controller)
	def result_inspection(self):
		super().result_inspection()
		## AV_127eがついているか
		if self.contains_buff(self.mark1,'AV_127e'):
			print ("check 1 OK: stats is %d/%d (8/9)"%(self.mark1.atk, self.mark1.health))
	pass

class pp_AV_129(Preset_Play):
	const = 0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_129',controller)
		self.const = self.mark1.atk
		self.mark2=self.exchange_card('vanilla',controller)
		self.mark3=self.exchange_card('vanilla',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		self.play_card(self.mark2, controller)
		self.change_turn(controller)
		##########
		self.play_card(self.mark3, opponent)
		self.change_turn(opponent)
		#############
		self.play_card(self.mark1, controller)
		self.change_turn(controller)
		#############
		self.attack_card(self.mark3, self.mark1, opponent)
	def result_inspection(self):
		super().result_inspection()
		if self.mark1.zone==Zone.GRAVEYARD:
			print("OK")
		print("%d - %d == 1"%(self.mark1.atk, self.const))
		if self.contains_buff(self.mark1, 'AV_129e'):
			print("OK")
		if self.contains_buff(self.mark2, 'AV_129e'):
			print("OK")

##################################

class pp_AV_130(Preset_Play):
	""" Legionnaire (6/9/3)
	Deathrattle: Give all minions in your hand +2/+2. """	
	const1 = 0
	const2 = 0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_130',opponent)
		self.mark2=self.exchange_card('vanilla',opponent)
		self.const1 = self.mark2.atk
		self.const2 = self.mark2.health
		self.mark3=self.exchange_card('vanillaA3',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########
		self.play_card(self.mark3, controller)
		self.change_turn(controller)
		##########
		self.play_card(self.mark1, opponent)
		self.change_turn(opponent)
		##########
		self.attack_card(self.mark3, self.mark1, controller)
	def result_inspection(self):
		super().result_inspection()
		if self.mark1.zone==Zone.GRAVEYARD:
			print("Check 1 OK")
		if self.contains_buff(self.mark2, 'AV_130e'):
			print("check 2 OK")
			print("(%d/%d) + (2/2) -> (%d/%d)"%(self.const1, self.const2, self.mark2.atk, self.mark2.health))
	pass

##################################

class pp_AV_131(Preset_Play):
	"""Knight-Captain (5/3/3)
	[Battlecry]: Deal 3 damage. [Honorable Kill]: Gain +3/+3."""
	const1 = 0
	const2 = 0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_131',opponent)
		self.mark2=self.exchange_card('vanilla',opponent)
		self.mark3=self.exchange_card('vanillaH2',controller)### (2,3) or (3,2) or (3,6)
		self.mark4=self.exchange_card('vanillaH3',controller)### 
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########
		self.play_card(self.mark3, controller)
		self.play_card(self.mark4, controller)
		self.change_turn(controller)
		##########
		self.play_card(self.mark1, opponent, target=self.mark3)
		self.const1=self.mark1.atk
		self.const2=self.mark1.health
		self.change_turn(opponent)
		##########
		self.change_turn(controller)
		##########
		self.attack_card(self.mark1, self.mark4, opponent)
	def result_inspection(self):
		super().result_inspection()
		if self.contains_buff(self.mark1, 'AV_131e'):
			print("check 1 OK")
			print("(3/3) -> (%d/%d)"%(self.const1, self.const2))
			print(" -> (%d/%d)"%(self.mark1.atk, self.mark1.health))
	pass

##################################

class pp_AV_132(Preset_Play):
	""" Troll Centurion (8/8/8)
	[Rush]. [Honorable Kill]: Deal 8 damage to the enemy hero."""
	const1 = 0
	const2 = 0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_132',controller)
		self.mark3=self.exchange_card('minionH8',opponent)### 
		self.mark4=self.exchange_card('minionH7',opponent)### 
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########
		self.play_card(self.mark1, controller)
		self.change_turn(controller)
		##########
		self.play_card(self.mark3, opponent)
		self.play_card(self.mark4, opponent)
		self.change_turn(opponent)
		##########
		self.attack_card(self.mark1, self.mark3, controller)### (1,3) or (1,4)
		##########
	def result_inspection(self):
		super().result_inspection()
		opponent = self.player.opponent
		enemy_hero = opponent.hero
		if enemy_hero.health==30-8:
			print("check 1 OK")
		print("enemy_hero.health (%d)"%(enemy_hero.health))
	pass

##################################

class pp_AV_133(Preset_Play):
	""" Icehoof Protector (6/2/10)
	[Taunt] [Freeze] any character damaged by this minion."""
	const1 = 0
	const2 = 0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_133',controller)
		self.mark3=self.exchange_card('minionH4',opponent)### 
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########
		self.play_card(self.mark1, controller)
		self.change_turn(controller)
		##########
		self.play_card(self.mark3, opponent)
		self.play_card(self.mark4, opponent)
		self.change_turn(opponent)
		##########
		self.attack_card(self.mark1, self.mark3, controller)### (1,3) 
		##########
	def result_inspection(self):
		super().result_inspection()
		opponent = self.player.opponent
		if self.mark3.frozen:
			print("check 1 OK")
	pass

##################################

class pp_AV_134(Preset_Play):
	""" Frostwolf Warmaster (4/3/5)
	Costs (1) less for each card you've played this turn."""
	const1 = 0
	const2 = 0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_134',controller)
		self.mark2=self.exchange_card('vanilla',controller)
		self.mark3=self.exchange_card('vanillaH2',controller)
		self.mark4=self.exchange_card('vanillaA3',controller)### 
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########
		self.play_card(self.mark2, controller)
		self.const1 = self.mark1.cost
		self.change_turn(controller)
		##########
		self.change_turn(opponent)
		##########
		self.play_card(self.mark3, controller)
		self.play_card(self.mark4, controller)
		self.const2 = self.mark1.cost
		self.change_turn(controller)
	def result_inspection(self):
		super().result_inspection()
		opponent = self.player.opponent
		print("4 -> %d(=3) -> %d(=2)"%(self.const1, self.const2))
	pass

##################################

class pp_AV_135(Preset_Play):
	""" Stormpike Marshal (4/2/6)
	[Taunt] If you took 5 or more damage on your opponent's turn, this costs (1)."""
	const1 = 0
	const2 = 0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_135',controller)
		self.mark2=self.exchange_card('minionH8',controller)
		self.mark3=self.exchange_card('vanillaA3',opponent)
		self.mark4=self.exchange_card('vanillaA3',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark2, controller)
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark3, opponent)
		self.play_card(self.mark4, opponent)
		self.change_turn(opponent)
		##########controller
		self.change_turn(controller)
		##########opponent
		self.attack_card(self.mark3, self.mark2, opponent)
		self.attack_card(self.mark4, self.mark2, opponent)### if this quits, cost will be still 4.
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		print("cost of %s id %d (=1)."%(self.mark1, self.mark1.cost))
	pass
##################################

class pp_AV_136(Preset_Play):
	""" Kobold Taskmaster (3/2/4)
	[Battlecry]: Add 2 Armor Scraps to your hand that give +2 Health to a minion."""
	const1 = 0
	const2 = 0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_136',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########start
		self.play_card(self.mark1, controller)
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1 = controller.hand[-2]
		card2 = controller.hand[-1]
		if card1.id=='AV_136t' and card2.id=='AV_136t':
			print("check 1 OK")
	pass

##################################

class pp_AV_136t(Preset_Play):
	""" Armor Scrap 
	Give a minion +2 Health. """
	const1 = 0
	const2 = 0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_136t',controller)
		self.mark2=self.exchange_card('vanilla',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########start
		self.play_card(self.mark2, controller)
		self.const1 = self.mark2.health
		self.play_card(self.mark1, controller, target=self.mark2)
		self.const2 = self.mark2.health
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		if self.contains_buff(self.mark2, 'AV_136e'):
			print("check 1 OK")
			print ("%d -> %d (=%d)"%(self.const1,self.const2,self.const1+2))
	pass

##################################

class pp_AV_137(Preset_Play):
	""" Irondeep Trogg (1/1/2)
	After your opponent casts a spell, summon a copy of this."""
	const1 = 0
	const2 = 0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_137',controller)
		self.mark2=self.exchange_card('spell',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		card1=self.mark1
		card2=self.mark2
		card3=self.mark3
		card4=self.mark4
		##########start
		self.play_card(card1, controller)
		self.change_turn(controller)
		########
		self.play_card(card2, opponent)
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		card2=self.mark2
		minion1 = controller.field[-1]
		print("%s"%(minion1))
		if minion1.id == 'AV_137':
			print("check 1 OK")
	pass

##################################

class pp_AV_138(Preset_Play):
	""" Grimtotem Bounty Hunter (3/4/2)
	[Battlecry]: Destroy an enemy [Legendary] minion."""
	const1 = 0
	const2 = 0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_138',opponent)
		self.mark2=self.exchange_card('minionH8',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		card1=self.mark1
		card2=self.mark2
		##########start
		self.play_card(card2, controller)
		self.change_turn(controller)
		########
		self.play_card(card1, opponent, target=card2)
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		card2=self.mark2
		if card2.rarity == Rarity.LEGENDARY:
			print("%s is legendary."%(card2))
		else:
			print("%s is not legendary."%(card2))
		if card2.zone == Zone.GRAVEYARD:
			print("%s is now in graveyard"%(card2))
		else:
			print("%s is still alive."%(card2))
	pass

##################################

class pp_AV_139(Preset_Play):
	"""Abominable Lieutenant (8/3/5)
	At the end of your turn, eat a random enemy minion and gain its stats. """
	const1 = 0
	const2 = 0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_139',opponent)
		self.mark2=self.exchange_card('minionH4',controller)
		self.mark3=self.exchange_card('minionH5',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		card1=self.mark1
		card2=self.mark2
		card3=self.mark3
		##########start
		self.play_card(card2, controller)
		self.play_card(card3, controller)
		self.const1=[card2.atk, card2.health]
		self.const2=[card3.atk, card3.health]
		self.change_turn(controller)
		########
		self.play_card(card1, opponent, target=card2)
		self.change_turn(opponent)
		########
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		card2=self.mark2
		card3=self.mark3
		print ("(3/5) -> (%d/%d)"%(card1.atk, card1.health))
		if card2.zone==Zone.GRAVEYARD:
			print ("check 1 OK")
		if card3.zone==Zone.GRAVEYARD:
			print ("check 1 OK")
		if card1.atk-3==self.const1[0] and card1.health-5==self.const1[1]:
			print ("check 2 OK")
		elif card1.atk-3==self.const2[0] and card1.health-5==self.const2[1]:
			print ("check 2 OK")
		else:
			print ("failure")
		pass

##################################

class pp_AV_141t(Preset_Play):
	""" Lokholar the Ice Lord (10/8/8) Elemental
	[Rush], [Windfury] Costs (5) less if you have 15 Health or less. """
	const1 = 0
	const2 = 0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_141t',opponent)
		self.mark2=self.exchange_card('minionA7',controller)
		self.mark3=self.exchange_card('minionA7',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		card1=self.mark1
		card2=self.mark2
		card3=self.mark3
		##########start
		self.play_card(card2, controller)
		self.play_card(card3, controller)
		#self.play_card(card4, controller)
		self.change_turn(controller)
		########
		self.change_turn(opponent)
		########
		self.attack_card(card2, opponent.hero, controller )
		self.attack_card(card3, opponent.hero, controller )
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		card2=self.mark2
		card3=self.mark3
		hero = controller.opponent.hero
		print ("hero's health is %s"%(hero.health))
		print ("The cost of %s is %d"%(card1, card1.cost))
		if hero.health<=15 and card1.cost==5:
			print("check 1 OK")
		elif hero.health>15 and card1.cost==10:
			print("check 1 OK")
		else:
			print ("check 1 NNGG")
		pass

##################################

class pp_AV_142t(Preset_Play):
	""" Ivus, the Forest Lord(1/1/1)
	[Battlecry]: Spend the rest of your Mana and gain +2/+2, [Rush], [Divine Shield], or [Taunt] at random for each."""
	const1 = 0
	const2 = 0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_142t',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		card1=self.mark1
		##########start
		self.play_card(card1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		hero = controller.opponent.hero
		print ("%s:"%(card1))
		print ("STATS: %d/%d"%(card1.atk, card1.health))
		print ("RUSH: %s"%(card1.rush))
		print ("DIVINE SHIELD: %s"%(card1.divine_shield))
		print ("TAUNT: %s"%(card1.taunt))
		pass

##################################

class pp_AV_143(Preset_Play):
	""" Korrak the Bloodrager (4/3/5)
	Deathrattle: If this wasn't Honorably Killed, resummon Korrak."""
	const1 = 0
	const2 = 0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_143',opponent)
		self.mark2=self.exchange_card('minionA6',controller)## 5 or 6
		self.mark3=self.exchange_card('vanilla',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		card1=self.mark1
		card2=self.mark2
		card3=self.mark3
		##########start
		self.play_card(card2, controller)
		self.change_turn(controller)
		##########
		self.play_card(card1, opponent)
		self.play_card(card3, opponent)
		self.change_turn(opponent)
		##########
		if card2.atk==card1.health:
			self.const1=1
		self.attack_card(card2, card1,controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		card2=self.mark2
		hero = controller.opponent.hero
		if self.const1==1:
			print("%s was honorably killed."%(card1))
		else:
			print("%s was not honorably killed."%(card1))
		if controller.opponent.field[-1].id == 'AV_143':
			print("%s was resummoned."%(card1))
			if self.const1!=1:
				print("check 1 OK")
		else:
			print("%s was not resummoned."%(card1))
			if self.const1==1:
				print("check 1 OK")
		pass

##################################

class pp_AV_215(Preset_Play):
	const1=0
	const2=0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_215',controller)
		self.mark2=self.exchange_card('vanilla',controller)
		if self.testNr==0:
			self.mark3=self.exchange_card('vanillaH3',opponent)
		if self.testNr==1:
			self.mark3=self.exchange_card('vanillaH2',opponent)
		self.mark4=self.exchange_card('vanilla',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		self.play_card(self.mark1, controller)
		self.play_card(self.mark2, controller)
		self.change_turn(controller)
		##########
		self.play_card(self.mark3, opponent)
		self.play_card(self.mark4, opponent)
		self.change_turn(opponent)
		#############
		self.const1 = self.mark1.atk
		self.const2 = self.mark3.health
		self.attack_card(self.mark1, self.mark3, controller)
	def result_inspection(self):
		super().result_inspection()
		#mark1がhonorable_killタグをもっているか。
		if hasattr(self.mark1, 'honorable_kill') and self.mark1.honorable_kill:
			print("check 1 OK")
		#Honorable Kill 発動条件
		print("%d - %d == 0"%(self.const1, self.const2))
		#Honorable Kill 発動しているか
		if hasattr(self.mark1, "windfury") and self.mark1.windfury:
			print("check 2 OK")
		else:
			print("check 2 NG")

##################################

class pp_AV_219(Preset_Play):
	""" Ram Commander (2/2/2)
	[Battlecry]: Add two 1/1 Rams with Rush to your hand."""
	const1=0
	const2=0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_219',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		card1=self.mark1
		##########start
		self.play_card(card1, controller)
		#self.change_turn(controller)
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		#ハンドの中身を検証
		card2=controller.hand[-1]
		card3=controller.hand[-2]
		if card2.id=='AV_219t' and card3.id=='AV_219t':
			print("check 1 OK")
		else:
			print("check 1 NG")
		
#########################

class pp_AV_222(Preset_Play):
	""" Spammy Arcanist (5/3/4)
	[Battlecry]: Deal 1 damage to all other minions. If any die, repeat this."""
	const1=0
	const2=0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_222',controller)
		self.mark2=self.exchange_card('vanillaH1',controller)###(1,2,3), (1,2,4), (1,3,4), etc
		self.mark3=self.exchange_card('vanillaH2',opponent)
		self.mark4=self.exchange_card('vanillaH3',opponent)
		#self.mark4=self.exchange_card('minionH4',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########start
		self.play_card(self.mark2, controller)
		self.change_turn(controller)
		##########
		self.play_card(self.mark3, opponent)
		self.play_card(self.mark4, opponent)
		self.change_turn(controller)
		##########
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		#フィールドのカードの生き死にを確認
		if self.mark2.zone==Zone.GRAVEYARD:
			print("%s was killed."%(self.mark2))
			print("check 1 OK")
		else:
			print("check 1 NG")
		if self.mark3.zone==Zone.GRAVEYARD:##if (1,2,4), (1,2,3) then yes, (1,3,4) then no.
			print("%s was killed."%(self.mark3))
		if self.mark4.zone==Zone.GRAVEYARD:##if (1,2,3), (1,2,2) then yes, (1,2,4) then no.
			print("%s was killed."%(self.mark4))
		
#########################

class pp_AV_223(Preset_Play):
	"""Vanndar Stormpike (4/4/4)
	[Battlecry]: If this costs less than every minion in your deck, reduce their Cost by (3)."""
	const1=0
	const2=0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_223',controller)
		super().preset_deck()
		nr=0
		while True:
			card = controller.deck[nr]
			if card.cost<=4:
				card.zone = Zone.GRAVEYARD
			else:
				nr += 1
			if len(controller.deck)<=nr:
				break
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########start
		self.play_card(self.mark1, controller)
		#self.change_turn(controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		#デッキにバフがついているかどうかを確認
		for card in controller.deck:
			if card.type==CardType.MINION:
				if self.contains_buff(card, 'AV_223e'):
					print("OK (cost=%d)"%(card.cost))
				else:
					print("NG ")

#########################

class pp_AV_238(Preset_Play):
	""" Gankster (2/4/2)
	[Stealth] After your opponents plays a minion, attack it"""
	const1=0
	const2=0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_238',controller)
		self.mark2=self.exchange_card('vanilla',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########start
		self.play_card(self.mark1, controller)
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark2, opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		print ("%s が攻撃を受けているかどうかを確認(目視)"%(self.mark2))
		#mark1のstealthが解除ざれているかどうかを確認
		if self.mark1.stealthed == False:
			print("sheck2 OK")
	pass
		
#########################


class pp_AV_256(Preset_Play):
	""" Reflecto Engineer (3/2/4)
	[Battlecry]: Swap the Attack and Health of all minions in both players' hands."""
	const1=0
	const2=0
	const3=0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_256',controller)
		self.mark2=self.exchange_card('vanilla',controller)
		self.mark3=self.exchange_card('vanilla',opponent)
		self.const1 = [self.mark1.atk,self.mark1.health,self.mark2.atk,self.mark2.health,self.mark3.atk,self.mark3.health,]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########start
		self.play_card(self.mark1, controller)
		self.play_card(self.mark2, controller)
		self.change_turn(controller)
		##########opponent
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		cst=self.const1
		print ("%s のスタッツが交換されているか %d/%d -> %d/%d (no)"%(self.mark1, cst[0],cst[1],self.mark1.atk,self.mark1.health))
		print ("%s のスタッツが交換されているか %d/%d -> %d/%d (yes)"%(self.mark2, cst[2],cst[3],self.mark2.atk,self.mark2.health))
		print ("%s のスタッツが交換されているか %d/%d -> %d/%d (yes)"%(self.mark3, cst[4],cst[5],self.mark3.atk,self.mark3.health))
	pass
		
#########################

#########################


class pp_AV_309(Preset_Play):
	""" Piggyback Imp (3/1/1) deamon
	Deathrattle: Summon a 4/1 Imp. """
	const1=0
	const2=0
	const3=0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_309',opponent)
		self.mark2=self.exchange_card('vanilla',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########start
		self.play_card(self.mark2, controller)
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark1, opponent)
		self.change_turn(opponent)
		########## controller
		self.attack_card(self.mark2, self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		cst=self.const1
		print ("%s のフィールドに4/1のインプがいるか "%(controller.opponent))
		card = controller.opponent.field[-1]
		print ("%s (%d/%d)"%(card,card.atk,card.health))
	pass
		
#########################


class pp_AV_401(Preset_Play):
	""" Stormpike Quartermaster (2/2/2)
	After you cast a spell, give a random minion in your hand +1/+1."""
	const1=0
	const2=0
	const3=0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_401',controller)
		self.mark2=self.exchange_card('spell',controller)
		self.mark3=self.exchange_card('vanilla',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########start
		self.play_card(self.mark1, controller)
		self.play_card(self.mark2, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		cst=self.const1
		print ("%sのハンドにAV_401e(+1/+1)がいるかどうか"%(controller))
		for card in controller.hand:
			if self.contains_buff(card,'AV_401e'):
				print("%s (%d/%d) <-(%d/%d)"%(card,card.atk,card.health,card.data.atk,card.data.health))
	pass
		
#########################

class pp_AV_704(Preset_Play):
	"""Humongous Owl(7/8/4)
	Deathrattle: Deal 8 damage to a random enemy."""
	const1=0
	const2=0
	const3=0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_704',opponent)
		self.mark2=self.exchange_card('minionH8',controller)
		self.mark3=self.exchange_card('minionA5',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########start
		self.play_card(self.mark2, controller)
		self.play_card(self.mark3, controller)
		self.change_turn(controller)
		########## opponent
		self.play_card(self.mark1, opponent)
		self.change_turn(opponent)
		##########  controller
		self.attack_card(self.mark3, self.mark1,controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		cst=self.const1
		print ("%sのミニオンに%sからの8点の攻撃があるかどうか（目視）"%(controller,self.mark1))
	pass
		
#########################

class pp_ONY_001(Preset_Play):
	""" Onyxian Warder
	[Battlecry:] If you're holdinga Dragon, summon two 2/1 Whelps with [Rush]. """
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('ONY_001',controller)
		self.mark2=self.exchange_card('dragon',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########start
		self.play_card(self.mark1, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		print("Chekc whether summon two 2/1 Whelps")
		for card in controller.field:
			self.print_stats("controller.field", card)
pass
		
#########################
class pp_ONY_002(Preset_Play):
	""" Gear Grubber
	[Taunt]. If you end your turn with any un spent mana, reduce this card's Cost by (1). """
	const1=0
	const2=0
	const3=0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('ONY_002',controller)
		self.mark2=self.exchange_card('minionH3',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########start
		self.play_card(self.mark2, controller)
		self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		print("Check whether reduce this card's Cost by (1)")
		for card in controller.hand:
			self.print_stats("controller.hand", card,old_cost=True)
	pass
		
#########################

class pp_ONY_003(Preset_Play):
	""" Whelp Bonker (3/1/5)
	[Frenzy and Honorable Kill:] Draw a card. """
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('ONY_003',controller)
		self.mark2=self.exchange_card('minionH2',opponent)
		self.mark3=self.exchange_card('minionH1',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########start
		self.play_card(self.mark1, controller)
		Hit(self.mark1, 2).trigger(controller)
		self.change_turn(controller)
		########## opponent
		self.play_card(self.mark2, opponent)
		self.play_card(self.mark3, opponent)
		self.change_turn(opponent)
		##########  controller
		self.attack_card(self.mark1, self.mark3, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		print("Check if controller drew two cards, once when frenzy and another when honorable kill.")
		for card in controller.hand:
			self.print_stats("hand", card)
	pass
		
#########################

class pp_ONY_004(Preset_Play):
	""" Raid Boss Onyxia
	[Rush]. [Immune] while you control a Whelp. [Battlecry:] Summon six_2/1 Whelps with [Rush]. """
	const1=0
	const2=0
	const3=0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('ONY_004',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########start
		self.play_card(self.mark1, controller)
		#Hit(controller.field[-1], 2).trigger(controller)# if this works, immune turns false.
		self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		cst=self.const1
		print("Check whether Whelps is in the field and the card is immune.")
		for card in controller.field:
			self.print_stats("controller.field", card)
		print("card immune = %s"%(self.mark1.immune))

	pass
		
#########################

class pp_ONY_005tb1(Preset_Play):
	""" Hyperblaster
	[Poisonous].Your hero is [Immune] while attacking. """
	const1=0
	const2=0
	const3=0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('ONY_005tb1',controller)
		self.mark2=self.exchange_card('minionH3',opponent)
		self.mark3=self.exchange_card('minionA5',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########start
		self.play_card(self.mark1, controller)
		self.print_stats("*+*+*+*+*+*+*+*+ ", controller.hero)
		self.change_turn(controller)
		########## opponent
		self.play_card(self.mark2, opponent)
		self.play_card(self.mark3, opponent)
		self.change_turn(opponent)
		##########  controller
		self.attack_card(controller.hero, self.mark2, controller)
		self.change_turn(controller)
		########## opponent
		self.attack_card(self.mark3, controller.hero, opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		cst=self.const1
		print("hero.immune_while_attacking:%s"%controller.hero.immune_while_attacking)
	pass
		
#########################

