from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType,Rarity,CardClass
from utils import postAction
from fireplace.deepcopy import deepcopy_game

def SimulateGames_Darkmoon_Neutral():
	PresetGame(pp_DMF_082)#
	pass

#########################

class pp_DMF_082(Preset_Play):
	""" Saddlemaster
	After you play a Beast, add_a random Beast to_your hand. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	tmp_game=None
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('DMF_082',controller)
		self.mark2=self.exchange_card('minionH2',controller)
		self.mark3=self.exchange_card('minionH2',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark2, controller)
		self.change_turn(controller)
		########## opponent
		self.change_turn(opponent)
		########## controller
		self.play_card(self.mark1, controller)
		self.tmp_game=deepcopy_game(controller.game, controller, 0)
		self.play_card(self.tmp_game.current_player.hand[-1], self.tmp_game.current_player)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		opponent=controller.opponent
		tmp_controller=self.tmp_game.current_player
		for card in tmp_controller.field:
			self.print_stats("controller.field", card)
	pass
		
#########################

