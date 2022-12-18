from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Summon, Hit, Shuffle

def barrens_warlock():
	PresetGame(pp_WC_023)
	pass

##########WC_023###############

class pp_WC_023(Preset_Play):# 
	""" Stealer of Souls
	After you draw a card, change its Cost to Health instead of Mana. """
	def preset_deck(self):
		self.mark1=self.exchange_card('WC_023', self.controller)
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
		self.change_turn()
		### con
		self.mark2 = self.controller.hand[-1]
		assert hasattr(self.mark2, 'card_costs_health')==True, "buff"
		assert self.mark2.card_costs_health==True, "card_cost_health"
		assert self.controller.hero.health == 30, "hero_health"
		mana= self.controller.mana
		self.play_card(self.mark2)
		assert self.controller.hero.health == 30 - self.mark2.cost, "card_cost_health"
		assert self.controller.mana == mana, "mana"
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
		
#########################





