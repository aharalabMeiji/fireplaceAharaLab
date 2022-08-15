from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Summon, Hit, Shuffle

def sunken_hunter():
	PresetGame(pp_TID_099)###OK
	pass

##########TID_099###############

class pp_TID_099(Preset_Play):# 
	""" K9_0tron
	[Battlecry:] [Dredge].If it's a 1-Cost minion, summon it. """
	def preset_deck(self):
		self.mark1=self.exchange_card('TID_099', self.controller)
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
		for card in self.controller.field:
			self.print_stats("field", card)
		# We cannnot build artificially the situation that cost-1 card is drawn.
	pass
		
#########################


