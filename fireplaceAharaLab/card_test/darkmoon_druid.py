from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity

def SimulateGames_Darkmoon_Druid():
	PresetGame(pp_DMF_058)#

##################################

class pp_DMF_058(Preset_Play):
	""" Solar Eclipse
	Your next spell this turn casts twice. """
	const1 = 0
	const2 = 0
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('DMF_058',controller)#Solar Eclipse
		self.mark2=self.exchange_card('spell',controller)#spell
		self.mark3=self.exchange_card('vanilla',opponent)#vanilla
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark3, opponent)#バニラ
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller)#Solar Eclipse
		if self.mark2.requires_target():
			self.play_card(self.mark2, controller, target=self.mark3)#spell
		else:
			self.play_card(self.mark2, controller)#spell
		self.change_turn(controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		hero = controller.opponent.hero
		pass

##################################
