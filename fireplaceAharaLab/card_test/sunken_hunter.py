from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Summon, Hit, Shuffle
from hearthstone.enums import CardClass

def sunken_hunter():
	#PresetGame(pp_TID_099)### OK
	#PresetGame(pp_TSC_023)### OK
	PresetGame(pp_TSC_023b)### OK
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
		
##########TSC_023##########

class pp_TSC_023(Preset_Play):
	""" Barbed Nets
	Deal $2 damage to an enemy. If you played a Naga while holding this,choose a second target. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_023", self.controller)
		self.con2=self.exchange_card("naga", self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionH4")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		#self.play_card(self.con2)
		self.play_card(self.con1, target=self.opp1)
		self.change_turn()
		### opp
		##self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_TSC_023b(Preset_Play):
	""" Barbed Nets
	Deal $2 damage to an enemy. If you played a Naga while holding this,choose a second target. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_023", self.controller)
		self.con2=self.exchange_card("naga", self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionH4")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con2)
		self.play_card(self.con1, target=self.opp1)
		self.change_turn()
		### opp
		##self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


#########################


