from .simulate_game import Preset_Play,PresetGame

#Alterac_Mage=['AV_114','AV_114e','AV_115','AV_115e5','AV_116','AV_200','AV_212','AV_212e','AV_218','AV_218t','AV_282','AV_282t','AV_282t2','AV_282t3','AV_282t4','AV_282t5','AV_283','AV_284','AV_290',]

def SimulateGames_Alterac_Mage():
	#PresetGame(pp_AV_114)##OK
	#PresetGame(pp_AV_115)##OK
	#PresetGame(pp_AV_116)##OK
	PresetGame(pp_AV_200,2)##
	#PresetGame(pp_AV_212)##
	#PresetGame(pp_AV_218)##
	#PresetGame(pp_AV_282)##
	#PresetGame(pp_AV_283)##
	#PresetGame(pp_AV_284)##
	#PresetGame(pp_AV_290)##
	pass

#########################

class pp_AV_114(Preset_Play):
	""" Shivering Sorceress (1/2/2)
	Battlecry: Reduce the Cost of the highest Cost spell in your hand by (1)."""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_114',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			print("%s :  cost %d <= %d"%(card, card.cost, card.data.cost))
	pass
		
#########################

class pp_AV_115(Preset_Play):
	""" Amplified Snowflurry (2/2/3)
	Battlecry: Your next Hero Power costs (0) and Freezes the target.
	"""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_115',controller)
		self.mark2=self.exchange_card('vanillaH3',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#print(">>>>>>>> cost of heropower is %d"%(controller.hero.power.cost))
		self.play_card(self.mark1, controller)
		print(">>>>>>>> cost of heropower is %d"%(controller.hero.power.cost))
		self.change_turn(controller)
		########## opponent
		self.play_card(self.mark2, opponent)
		self.change_turn(opponent)
		########## controller
		self.activate_heropower(controller, self.mark2)

		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		print(">>>>>>>> cost of heropower is %d"%(controller.hero.power.cost))
		print(">>>>>>>> health of target  : %d -> %d"%(self.mark2.data.health, self.mark2.health))
		print(">>>>>>>> target is frozen? : %d"%(self.mark2.frozen))

	pass
		
#########################

class pp_AV_116(Preset_Play):
	""" Arcane Brilliance (4) Arcane
	Add a copy of a 7, 8, 9, and 10-Cost spell in your deck to your hand.
	"""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_116',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			print("%s :  cost %d"%(card, card.cost))
		if controller.hand[-1].cost>=7:
			print("check OK")
	pass
		
#########################

class pp_AV_200(Preset_Play):
	""" Magister Dawngrasp (8/*/5) Hero
	Battlecry: Recast a spell from each spell school you've cast this game.
	"""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_200',controller)
		self.mark2=self.exchange_card('nature',controller)
		self.mark3=self.exchange_card('fire',controller)
		self.mark4=self.exchange_card('vanillaH1',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		if self.testNr==0:
			########## controller
			self.play_card(self.mark2, controller)
			self.play_card(self.mark3, controller)
			self.change_turn(controller)
			########## opponent
			self.play_card(opponent.hand[0], opponent)
			self.change_turn(opponent)
			########## controller
			self.play_card(self.mark1, controller)
		else:
			########## controller
			self.play_card(self.mark1, controller)
			self.change_turn(controller)
			########## opponent
			self.play_card(self.mark4, opponent)
			self.change_turn(opponent)
			########## controller
			self.activate_heropower(controller, target=self.mark4)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		if self.testNr==0:
			hero = controller.hero
			print("Hero : %s health %d "%(hero, hero.health))
			print("Armor : %d "%(hero.armor))
			print("HeroPower : %s cost %d "%(hero.power, hero.power.cost))
		else:
			print("%s health %d -> %d"%(self.mark4, self.mark4.data.health, self.mark4.health))
	pass
		
#########################

class pp_AV_212(Preset_Play):
	""" Siphon Mana (2) Arcane
	Deal 2 damage. Honorable Kill: Reduce the Cost of spells in your hand by (1).
	"""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_114',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			print("%s :  cost %d <= %d"%(card, card.cost, card.data.cost))
	pass
		
#########################

class pp_AV_218(Preset_Play):
	""" Mass Polymorph (7) Arcane
	Transform all minions into 1/1 Sheep."""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_114',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			print("%s :  cost %d <= %d"%(card, card.cost, card.data.cost))
	pass
		
#########################

class pp_AV_282(Preset_Play):
	""" Build a Snowman (3) Frost
	Summon a 3/3 Snowman that Freezes.  Add 'Build a Snowbrute' to your hand.
	"""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_114',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			print("%s :  cost %d <= %d"%(card, card.cost, card.data.cost))
	pass
		
#########################

class pp_AV_283(Preset_Play):
	""" Rune of the Archmage (9)
	Cast 20 Mana worth of Mage spells at enemies.
	"""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_114',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			print("%s :  cost %d <= %d"%(card, card.cost, card.data.cost))
	pass
		
#########################

class pp_AV_284(Preset_Play):
	""" Balinda Stonehearth (6/5/5)
	Battlecry: Draw 2 spells. Swap their Costs with this minion's stats."""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_114',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			print("%s :  cost %d <= %d"%(card, card.cost, card.data.cost))
	pass
		
#########################

class pp_AV_290(Preset_Play):
	""" Iceblood Tower (10)
	At the end of your turn, cast another spell from your deck. Lasts 3 turns.	"""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_114',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			print("%s :  cost %d <= %d"%(card, card.cost, card.data.cost))
	pass
		
#########################

