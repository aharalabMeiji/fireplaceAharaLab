from .simulate_game import Preset_Play,PresetGame

#Scholomance_Druid=['SCH_427 ]

def SimulateGames_Scholo_Druid():
	PresetGame(pp_SCH_427)# 
	pass

#########################

class pp_SCH_427(Preset_Play):
	"""Lightning Bloom
	Gain 2 Mana Crystals this turn only. Overload: (2)"""
	str1=""
	str2=""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('SCH_427',controller)
		super().preset_deck()
		controller=max_mana=3
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		self.str1 = ">>>>>>>>>> mana %d/%d"%(controller.mana, controller.max_mana)
		self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		self.change_turn(opponent)
		########## controller
		self.str2 = ">>>>>>>>>> mana %d/%d"%(controller.mana, controller.max_mana)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		print(self.str1)
		print(self.str2)
	pass
	
