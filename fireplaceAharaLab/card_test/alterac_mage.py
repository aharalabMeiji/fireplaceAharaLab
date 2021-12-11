from .simulate_game import Preset_Play,PresetGame

#Alterac_Mage=['AV_114','AV_114e','AV_115','AV_115e5','AV_116','AV_200','AV_212','AV_212e','AV_218','AV_218t','AV_282','AV_282t','AV_282t2','AV_282t3','AV_282t4','AV_282t5','AV_283','AV_284','AV_290',]

def SimulateGames_Alterac_Mage():
	#PresetGame(pp_AV_114)##ok
	#PresetGame(pp_AV_115)##
	#PresetGame(pp_AV_116)##
	#PresetGame(pp_AV_200)##
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

