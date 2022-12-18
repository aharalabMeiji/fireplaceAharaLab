from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def lich_mage():

	#PresetGame(pp_RLK_541)##
	#PresetGame(pp_RLK_542)##
	#PresetGame(pp_RLK_543)##
	#PresetGame(pp_RLK_544)##
	#PresetGame(pp_RLK_545)##
	#PresetGame(pp_RLK_546)##
	#PresetGame(pp_RLK_547)##
	#PresetGame(pp_RLK_548)##
	#PresetGame(pp_RLK_803)##
	#PresetGame(pp_RLK_843)##
	pass


##########RLK_541##########

class pp_RLK_541(Preset_Play):
	""" Vexallus
	Your Arcane spells cast twice. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_541", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
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
	pass


##########RLK_542##########

class pp_RLK_542(Preset_Play):
	""" Arcsplitter
	<b>Deathrattle:</b> Add 2 Arcane Bolts to your hand. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_542", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
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
	pass


##########RLK_543##########

class pp_RLK_543(Preset_Play):
	""" Magister's Apprentice
	Your Arcane spells cost (1) less. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_543", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
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
	pass


##########RLK_544##########

class pp_RLK_544(Preset_Play):
	""" Arcane Defenders
	Summon two 5/6 Golems with <b>Taunt</b> and "Can't be targeted by spells or Hero Powers." """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_544", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
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
	pass


##########RLK_545##########

class pp_RLK_545(Preset_Play):
	""" Energy Shaper
	<b>Battlecry:</b> Transform all spells in your hand into ones that cost (2) more. <i>(They keep their original Cost.)</i> """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_545", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
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
	pass


##########RLK_546##########

class pp_RLK_546(Preset_Play):
	""" Vast Wisdom
	<b>Discover</b> two spells that cost (3) or less. Swap their Costs. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_546", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
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
	pass


##########RLK_547##########

class pp_RLK_547(Preset_Play):
	""" Prismatic Elemental
	<b>Battlecry:</b> <b>Discover</b> a spell from any class. It costs (1) less. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_547", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
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
	pass


##########RLK_548##########

class pp_RLK_548(Preset_Play):
	""" Arcane Wyrm
	<b>Battlecry:</b> Add an Arcane Bolt to your hand. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_548", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
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
	pass


##########RLK_803##########

class pp_RLK_803(Preset_Play):
	""" Grand Magister Rommath
	<b>Battlecry:</b> Recast each spell you've cast this game that didn't start in your deck. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_803", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
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
	pass


##########RLK_843##########

class pp_RLK_843(Preset_Play):
	""" Arcane Bolt
	Deal $2 damage. <b>Manathirst (8):</b> Deal $3 damage instead. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_843", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
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
	pass


