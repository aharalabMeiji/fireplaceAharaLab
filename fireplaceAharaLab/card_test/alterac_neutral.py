from .simulate_game import PresetGame,Preset_Play

def SimulateGames_Alterac_Neutral():

	#PresetGame(pp_AV_100,1)####OK
	#PresetGame(pp_AV_101,1)####OK
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
	PresetGame(pp_AV_131,1)
	#PresetGame(pp_AV_132,1)
	#PresetGame(pp_AV_133,1)
	#PresetGame(pp_AV_134,1)
	#PresetGame(pp_AV_135,1)
	#PresetGame(pp_AV_136,1)
	#PresetGame(pp_AV_137,1)
	#PresetGame(pp_AV_138,1)
	#PresetGame(pp_AV_139,1)
	#PresetGame(pp_AV_141t,1)
	#PresetGame(pp_AV_142t,1)
	#PresetGame(pp_AV_143,1)
	#PresetGame(pp_AV_215,2)####OK
	#PresetGame(pp_AV_219,1)
	#PresetGame(pp_AV_222,1)
	#PresetGame(pp_AV_223,1)
	#PresetGame(pp_AV_238,1)
	#PresetGame(pp_AV_256,1)
	#PresetGame(pp_AV_309,1)
	#PresetGame(pp_AV_401,1)
	#PresetGame(pp_AV_704,1)
	pass

from hearthstone.enums import Zone,CardType

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
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_101',controller)
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
		## 自然系のカードを一枚引いている
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
		self.mark3=self.exchange_card('vanillaH3',controller)### (2,3) or (3,2) or (3,6)
		self.mark4=self.exchange_card('minionH6',controller)### 
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




