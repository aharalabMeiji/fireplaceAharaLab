from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity, CardClass
from fireplace.actions import Hit

def stormwind_druid():
	PresetGame(pp_DED_002)###
	pass

################DED_002##################

class pp_DED_002(Preset_Play):
	""" Moonlit Guidance
	[Discover] a copy of a card in your deck.If you play it this turn,draw the original. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.mark1=self.exchange_card('DED_002',self.controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########controller
		self.play_card(self.mark1, self.controller)#
		self.mark2=self.choose_action()
		self.play_card(self.mark2)
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats ("controller.hand",card,show_buff=True)
		pass

##################################


