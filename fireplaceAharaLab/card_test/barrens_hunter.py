from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity

def barrens_hunter():
	PresetGame(pp_BAR_034x)#
	PresetGame(pp_BAR_034y)#
	pass

##################################

class pp_BAR_034x(Preset_Play):
	""" Tame Beast (Rank 1)
	Summon a 2/2 Beast with <b>Rush</b>. <i>(Upgrades when you have 5 Mana.)</i>	"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('BAR_034',controller)#
		controller.max_mana=4
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		handID = [card.id for card in controller.hand]
		assert 'BAR_034' in handID, "hand"
		self.change_turn()
		### opp
		self.change_turn()
		### con
		handID = [card.id for card in controller.hand]
		assert 'BAR_034t' in handID, "hand"
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass
class pp_BAR_034y(Preset_Play):
	""" Tame Beast (Rank 1)
	Summon a 2/2 Beast with <b>Rush</b>. <i>(Upgrades when you have 5 Mana.)</i>	"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('BAR_034t',controller)#
		controller.max_mana=9
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		handID = [card.id for card in controller.hand]
		assert 'BAR_034t' in handID, "hand"
		self.change_turn()
		### opp
		self.change_turn()
		### con
		handID = [card.id for card in controller.hand]
		assert 'BAR_034t2' in handID, "hand"
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

##################################