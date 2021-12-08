from .simulate_game import Preset_Play,PresetGame

#Alteric_Druid=['AV_205','AV_210','AV_210e','AV_211','AV_211t','AV_291','AV_292','AV_292e','AV_292e2','AV_293','AV_293e','AV_294','AV_294e','AV_293t','AV_295','AV_295a','AV_295b','AV_296','AV_296e','AV_296e2','AV_360',   ]

def SimulateGames_Alterac_Druid():
	#PresetGame(pp_AV_205)# Hero
	#PresetGame(pp_AV_210)#################
	PresetGame(pp_AV_211)
	#PresetGame(pp_AV_291)
	#PresetGame(pp_AV_291)
	#PresetGame(pp_AV_291)
	#PresetGame(pp_AV_291)
	#PresetGame(pp_AV_291)
	#PresetGame(pp_AV_291)
	#PresetGame(pp_AV_360)
	pass

#########################

class pp_AV_210(Preset_Play):
	""" Pathmaker (3/3/4) 
	Battlecry: Cast the other choice from the last [Choose One] spell you've cast.  """
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_210',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#self.play_card(self.mark1, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		print ("%s（目視）"%(self.mark1))
	pass
		
#########################

class pp_AV_211(Preset_Play):
	""" Dire Frostwolf (4/4/4) beast
	[Stealth] [Deathrattle]: Summon a 2/2 Wolf with Stealth. """
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_211',controller)
		self.mark2=self.exchange_card('minionA5',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		self.change_turn(controller)
		########## opponent
		self.play_card(self.mark2, opponent)
		self.change_turn(opponent)
		########## controller
		self.attack_card(self.mark1, self.mark2, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		print ("%s（目視）"%(self.mark1))
	pass
		
#########################
