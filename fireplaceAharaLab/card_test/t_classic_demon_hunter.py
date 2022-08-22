from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity

def classic_demonhunter():

	#PresetGame(pp_VAN_HERO_10bp)##
	#PresetGame(pp_VAN_HERO_10pe2)##


##########VAN_HERO_10bp##########

class pp_VAN_HERO_10bp(Preset_Play):
	""" Demon Claws
	[Hero Power]+1 Attack this turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_HERO_10bp", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_HERO_10pe2##########

class pp_VAN_HERO_10pe2(Preset_Play):
	""" Demon's Bite
	Your hero has +2 Attack this turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_HERO_10pe2", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


