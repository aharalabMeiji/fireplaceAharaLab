from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity

def SimulateGames_Barrens_Druid():
	#PresetGame(pp_BAR_536)#OK
	pass

##################################

class pp_BAR_536(Preset_Play):
	""" Living Seed (Rank 1)
	Draw a Beast. Reduce its Cost by (1). <i>(Upgrades when you have 5 Mana.)</i> """
	const1 = 0
	const2 = 0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('BAR_536',controller)#Living Seed
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(controller.hand[-1], controller)#
		#self.change_turn(controller)
		##########opponent
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

##################################