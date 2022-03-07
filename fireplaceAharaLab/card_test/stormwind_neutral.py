from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity, CardClass
from utils import postAction

def SimulateGames_Stormwind_Neutral():
	PresetGame(pp_SW_079)#OK

##################################

class pp_SW_079(Preset_Play):
	""" Flightmaster Dungar
	[x]<b>Battlecry:</b> Choose a flightpath and go <b>Dormant.</b> Awaken with a bonus __when you complete it! """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('SW_079',controller)#Flightmaster Dungar
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark1, controller)#
		postAction(controller)
		self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		self.change_turn(opponent)
		##########controller
		self.change_turn(controller)
		##########opponent
		self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		print("There are three patterns of dormant with 1,3,5 turns.")
		pass

##################################

