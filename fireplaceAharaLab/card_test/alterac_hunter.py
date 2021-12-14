from .simulate_game import Preset_Play,PresetGame

#Alterac_Hunter=['AV_113','AV_113p','AV_147','AV_147e','AV_224','AV_226','AV_226e','AV_244','AV_244e','AV_333','AV_334','AV_334e','AV_335','AV_335e','AV_336','AV_336e','AV_337','AV_337t',	]
def SimulateGames_Alterac_Hunter():
	#PresetGame(pp_AV_113)##
	#PresetGame(pp_AV_147)##
	#PresetGame(pp_AV_224)##
	#PresetGame(pp_AV_226)##
	#PresetGame(pp_AV_244)##
	#PresetGame(pp_AV_333)##
	#PresetGame(pp_AV_334)##
	#PresetGame(pp_AV_335)##
	#PresetGame(pp_AV_336)##
	#PresetGame(pp_AV_337)##
	pass

#########################

class pp_AV_113(Preset_Play):
	""" 
	"""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_113',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',opponent)
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

class pp_AV_147(Preset_Play):
	""" 
	"""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_113',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',opponent)
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

class pp_AV_224(Preset_Play):
	""" 
	"""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_113',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',opponent)
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

class pp_AV_226(Preset_Play):
	""" 
	"""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_113',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',opponent)
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

class pp_AV_244(Preset_Play):
	""" 
	"""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_113',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',opponent)
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

class pp_AV_333(Preset_Play):
	""" 
	"""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_113',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',opponent)
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

class pp_AV_334(Preset_Play):
	""" 
	"""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_113',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',opponent)
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

class pp_AV_335(Preset_Play):
	""" 
	"""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_113',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',opponent)
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

class pp_AV_336(Preset_Play):
	""" 
	"""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_113',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',opponent)
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

class pp_AV_337(Preset_Play):
	""" 
	"""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_113',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',opponent)
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
		
########################