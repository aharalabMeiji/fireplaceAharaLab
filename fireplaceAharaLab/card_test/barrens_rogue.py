from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Summon, Hit, Shuffle
from hearthstone.enums import CardClass, Race, CardType

def barrens_rogue():
	#PresetGame(pp_WC_016)## OK
	#PresetGame(pp_WC_017)#### OKOK
	#PresetGame(pp_BAR_323a)## OK
	#PresetGame(pp_BAR_323b)## OK
	pass

##########WC_016###############

class pp_WC_016(Preset_Play):# 
	""" Shroud of Concealment
	Draw 2 minions. Any played this turn gain [Stealth] for 1 turn. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE	
	def preset_deck(self):
		self.mark1=self.exchange_card('WC_016', self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		for card in self.controller.hand:
			self.print_stats("hand", card, show_buff=True)
			if 'WC_016e' in [buff.id for buff in card.buffs]:
				self.mark2=card
		self.play_card(self.mark2)
		for card in self.controller.field:
			self.print_stats("field", card, show_buff=True)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("field", card, show_buff=True)
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

##########pp_BAR_323##########

class pp_BAR_323a(Preset_Play):
	""" Yoink!
	[Discover] a Hero Power and set its Cost to (0). Swap back after 2 uses. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("BAR_323", self.controller)
		#self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		#self.con4=self.con4[0][0]
		#self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		#self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
		print("Check if a heropower card is in hand")
	pass

class pp_BAR_323b(Preset_Play):
	""" Yoink!
	[Discover] a Hero Power and set its Cost to (0). Swap back after 2 uses. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("BAR_323", self.controller)
		#self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		#self.con4=self.con4[0][0]
		#self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		#self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.choose_action()
		for card in self.controller.hand:
			if card.type==CardType.HERO_POWER:
				self.con2=card
				self.play_card(self.con2)
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
		self.print_stats("heropower", self.controller.hero.power)
		print("Check if a heropower is in a proper position.")
	pass


#########################

