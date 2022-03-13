from .simulate_game import Preset_Play,PresetGame

def alterac_paladin():
	#PresetGame(pp_AV_146)
	pass

#########################

class pp_AV_146(Preset_Play):# <5>[1626] (7/2/5)
	""" The Immovable Object
	This doesn't lose Durability. Your hero takes half damage, rounded up. """
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_146',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
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
			self.print_stats("hand", card)
	pass
		
#########################

