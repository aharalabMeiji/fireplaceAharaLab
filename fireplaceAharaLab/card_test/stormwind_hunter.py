from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity, CardClass
from fireplace.actions import Hit

def SimulateGames_Stormwind_Hunter():
	#PresetGame(pp_SW_457)#OK
	pass

##################################

class pp_SW_457(Preset_Play):
	""" Leatherworking Kit
	After three friendly Beasts die, draw a Beast and give it +1/+1.Lose 1 Durability. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('SW_457',controller)#
		self.mark2=self.exchange_card('beast',controller)#
		self.mark3=self.exchange_card('minionA7',opponent)#
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
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark3, opponent)#
		#self.play_card(self.mark1, opponent)#
		self.change_turn(opponent)
		##########controller
		self.change_turn(controller)
		##########opponent
		self.attack_card(self.mark3, self.mark2, opponent)#
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		print("What happens after %s was killed" % self.mark2)
		for card in controller.hand:
			self.print_stats ("controller.hand",card,show_buff=True)
		pass

##################################


