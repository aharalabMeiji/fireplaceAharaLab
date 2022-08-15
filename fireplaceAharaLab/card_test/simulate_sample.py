from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Summon, Hit, Shuffle

def XXX_YYY():
	#PresetGame(pp_ZZZZ)
	pass

##########ZZZZ###############

class pp_ZZZZ(Preset_Play):# 
	""" Z
	Z """
	def preset_deck(self):
		self.mark1=self.exchange_card('ZZZZ', self.controller)
		self.mark4=Summon(self.controller, self.card_choice('minionH3')).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
		
#########################

