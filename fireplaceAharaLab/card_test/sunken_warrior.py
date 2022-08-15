#sunken_warrior
from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Summon, Hit, Shuffle

def sunken_warrior():
	#PresetGame(pp_TSC_660)###OK!
	pass

##########TSC_660###############

class pp_TSC_660(Preset_Play):# 
	""" Nellie, the Great Thresher
	[Colossal +1][Battlecry:] [Discover] 3 Pirates to crew Nellie's Ship! """
	def preset_deck(self):
		self.mark1=self.exchange_card('TSC_660', self.controller)
		self.mark4=Summon(self.controller, self.card_choice('minionH3')).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		for card in self.controller.field:
			if card.id=='TSC_660t':
				self.mark2=card
				break
		self.choose_action()
		self.change_turn()
		### opp
		Hit(self.mark2, 10).trigger(self.opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
		print("The last three must be the new comers (Nellie's Pirate crew)")
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


