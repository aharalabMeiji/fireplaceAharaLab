from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType,Rarity,CardClass
from utils import postAction

def SimulateGames_Darkmoon_Hunter():
	#PresetGame(pp_YOP_028)#OK
	pass

#########################

class pp_YOP_028(Preset_Play):
	""" Saddlemaster
	After you play a Beast, add_a random Beast to_your hand. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('YOP_028',controller)
		self.mark2=self.exchange_card('beast',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		self.play_card(self.mark2, controller)
		#self.change_turn(controller)
		########## opponent
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		opponent=controller.opponent
		for card in controller.hand:
			self.print_stats("controller.hand", card)
	pass
		
#########################

