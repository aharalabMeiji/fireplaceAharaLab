from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity,CardClass

def SimulateGames_Core_Neutral():
	PresetGame(pp_CORE_EX1_189)#OK
	pass

##################################

class pp_CORE_EX1_189(Preset_Play):# <6>[1637]
	""" Brightwing
	[Battlecry:] Add a random [Legendary] minion to your_hand. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_189',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark1, controller)
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark3, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.opponent.hero
		for card in controller.hand:
			self.print_stats ("controller.hand", card)
		pass

##################################

