from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Summon, Hit, Shuffle
from hearthstone.enums import CardClass, Race

def barrens_rogue():
	PresetGame(pp_WC_017)#### OKOK
	pass


##########WC_017###############

class pp_WC_017(Preset_Play):# 
	""" Savory Deviate Delight
	Transform a minion in both players' hands into a Pirate or [Stealth] minion. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE	
	def preset_deck(self):
		self.mark1=self.exchange_card('WC_017', self.controller)
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
		print("check the transformations")
		assert len(self.controller.hand)==3, "hand"
		for card in self.controller.hand:
			self.print_stats("controller.hand", card)
			if hasattr(card,'race'):	
				print("pirate=%s,"%(card.race==Race.PIRATE), end='')
			if hasattr(card,'stealthed'):	
				print("stealth=%s"%(card.stealthed))
		for card in self.opponent.hand:
			self.print_stats("opponent.hand", card)
			if hasattr(card,'race'):	
				print("pirate=%s,"%(card.race==Race.PIRATE), end='')
			if hasattr(card,'stealthed'):	
				print("stealth=%s"%(card.stealthed))
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

