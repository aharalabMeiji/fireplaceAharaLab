from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity, CardClass
from fireplace.actions import Hit

def SimulateGames_Stormwind_Mage():
	#PresetGame(pp_SW_111)#OK
	pass

##################################

class pp_SW_111(Preset_Play):
	""" Sanctum Chandler
	After you cast a Fire spell, draw a spell. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('SW_111',controller)#
		self.mark2=self.exchange_card('fire',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark1, controller)#
		self.play_card(self.mark2, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark3, opponent)#
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		print("See how to get a new card into the hand")
		for card in controller.hand:
			self.print_stats ("controller.hand",card,show_buff=True)
		pass

##################################


