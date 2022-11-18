from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Summon, Hit, Shuffle, RefreshMana

def sunken_mage():
	PresetGame(pp_TSC_620x)
	PresetGame(pp_TSC_620y)
	pass

##########TSC_620###############

class pp_TSC_620x(Preset_Play):# 
	""" Spitelash Siren
	After you play a Naga,refresh two Mana Crystals.<i>(Then switch to spell!)</i>@After you cast a spell,refresh two Mana Crystals.<i>(Then switch to Naga!)</i> """
	def preset_deck(self):
		self.mark1=self.exchange_card('TSC_620', self.controller)
		self.mark2=self.exchange_card('naga', self.controller)
		self.mark3=self.exchange_card('spellC2', self.controller)
		self.mark4=Summon(self.controller, self.card_choice('minionH3')).trigger(self.opponent)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.play_card(self.mark2)
		self.play_card(self.mark3)
		self.change_turn()
		### opp
		self.change_turn()
		### con
		pass
	def result_inspection(self):
		super().result_inspection()
		count=0
		for action in self.controller._targetedaction_log:
			if isinstance(action['class'], RefreshMana):
				assert action['target_args'][0]==2, "target_args"
				print("action['target_args'][0]==2")
				count+=1
		assert count==2, "count"
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_TSC_620y(Preset_Play):# 
	""" Spitelash Siren
	After you play a Naga,refresh two Mana Crystals.<i>(Then switch to spell!)</i>@After you cast a spell,refresh two Mana Crystals.<i>(Then switch to Naga!)</i> """
	def preset_deck(self):
		self.mark1=self.exchange_card('TSC_620', self.controller)
		self.mark2=self.exchange_card('naga', self.controller)
		self.mark3=self.exchange_card('spellC2', self.controller)
		self.mark4=Summon(self.controller, self.card_choice('minionH3')).trigger(self.opponent)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.play_card(self.mark3)
		self.play_card(self.mark2)
		self.change_turn()
		### opp
		self.change_turn()
		### con
		pass
	def result_inspection(self):
		super().result_inspection()
		count=0
		for action in self.controller._targetedaction_log:
			if isinstance(action['class'], RefreshMana):
				assert action['target_args'][0]==2, "target_args"
				print("action['target_args'][0]==2")
				count+=1
		assert count==1, "count"
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
		
#########################
