from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Summon, Hit, Shuffle

def barrens_paladin():
	#PresetGame(pp_BAR_879)#OK
	PresetGame(pp_WC_032)#OK
	pass


##########BAR_879###############

class pp_BAR_879(Preset_Play):# 
	""" Cannonmaster Smythe
	[Battlecry:] Transform your [Secrets] into 3/3 Soldiers. They transform back when they die. """
	def preset_deck(self):
		self.mark1=self.exchange_card('BAR_879', self.controller)
		self.mark2=self.exchange_card('secret', self.controller)
		self.mark4=Summon(self.controller, self.card_choice('minionH3')).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark2)
		self.play_card(self.mark1)
		assert self.controller.secrets==[], "secret"
		self.mark3=[card for card in self.controller.field if card.id=='BAR_879t']
		self.mark3=self.mark3[0]
		assert self.mark3.buffs!=[], "buffs"
		assert self.mark3.buffs[-1].id=='BAR_879e'
		assert self.mark3.buffs[-1].smallbox[0]==self.mark2.id, "secret"
		self.change_turn()
		Hit(self.mark3, 10).trigger(self.mark4)
		assert self.controller.secrets!=[], "secret"
		assert self.controller.secrets[-1].id==self.mark2.id, "secret"
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
		
##########WC_032##########

class pp_WC_032(Preset_Play):
	""" Seedcloud Buckler   (weapon)
	[Deathrattle:] Give your_minions [Divine Shield]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("WC_032", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.attack_card(self.controller.hero, self.opponent.hero)
		assert self.player.weapon.durability==2, "durability"
		self.change_turn()
		### opp
		self.change_turn()
		### con
		self.attack_card(self.controller.hero, self.opponent.hero)
		assert self.player.weapon.durability==1, "durability"
		self.change_turn()
		### opp
		self.change_turn()
		### con
		self.attack_card(self.controller.hero, self.opponent.hero)
		assert self.mark4.divine_shield==True, "divine_shild"
		self.change_turn()
		### opp
		Hit(self.mark4, 1).trigger(self.opponent)
		assert self.mark4.divine_shield==False, "divine_shild"
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("field", card)
	pass


#########################

