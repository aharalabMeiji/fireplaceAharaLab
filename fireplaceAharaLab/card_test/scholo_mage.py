from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone, CardType, Rarity, CardClass
from utils import postAction

def SimulateGames_Scholo_Mage():
	PresetGame(pp_SCH_235)#OK

##########################################

class pp_SCH_235(Preset_Play):
	"""Devolving Missiles	Epic"""
	#[x]Shoot three missiles at random enemy minions that transform them into ones that cost (1) less.
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('SCH_235',controller)#
		self.mark2=self.exchange_card('minionH3',opponent)
		self.mark3=self.exchange_card('minionH4',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark2, opponent)#
		self.play_card(self.mark3, opponent)#
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller)#
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print("Check whether three time Morphs happen")
		pass

##################################
