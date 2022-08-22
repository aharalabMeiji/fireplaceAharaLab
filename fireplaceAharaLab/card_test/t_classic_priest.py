from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity

def classic_priest():

	#PresetGame(pp_VAN_CS1_112)##
	#PresetGame(pp_VAN_CS1_113)##
	#PresetGame(pp_VAN_CS1_129)##
	#PresetGame(pp_VAN_CS1_130)##
	#PresetGame(pp_VAN_CS2_003)##
	#PresetGame(pp_VAN_CS2_004)##
	#PresetGame(pp_VAN_CS2_234)##
	#PresetGame(pp_VAN_CS2_235)##
	#PresetGame(pp_VAN_CS2_236)##
	#PresetGame(pp_VAN_DS1_233)##
	#PresetGame(pp_VAN_EX1_091)##
	#PresetGame(pp_VAN_EX1_332)##
	#PresetGame(pp_VAN_EX1_334)##
	#PresetGame(pp_VAN_EX1_335)##
	#PresetGame(pp_VAN_EX1_339)##
	#PresetGame(pp_VAN_EX1_341)##
	#PresetGame(pp_VAN_EX1_345)##
	#PresetGame(pp_VAN_EX1_350)##
	#PresetGame(pp_VAN_EX1_591)##
	#PresetGame(pp_VAN_EX1_621)##
	#PresetGame(pp_VAN_EX1_622)##
	#PresetGame(pp_VAN_EX1_623)##
	#PresetGame(pp_VAN_EX1_624)##
	#PresetGame(pp_VAN_EX1_625)##
	#PresetGame(pp_VAN_EX1_626)##
	#PresetGame(pp_VAN_EX1_tk31)##
	#PresetGame(pp_VAN_HERO_09bp)##
	#PresetGame(pp_VAN_HERO_09e1)##


##########VAN_CS1_112##########

class pp_VAN_CS1_112(Preset_Play):
	""" Holy Nova
	Deal $2 damage to all enemies. Restore #2 Health to all friendly characters. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS1_112", self.controller)
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


##########VAN_CS1_113##########

class pp_VAN_CS1_113(Preset_Play):
	""" Mind Control
	Take control of an enemy minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS1_113", self.controller)
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


##########VAN_CS1_129##########

class pp_VAN_CS1_129(Preset_Play):
	""" Inner Fire
	Change a minion's Attack to be equal to its Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS1_129", self.controller)
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


##########VAN_CS1_130##########

class pp_VAN_CS1_130(Preset_Play):
	""" Holy Smite
	Deal $2 damage. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS1_130", self.controller)
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


##########VAN_CS2_003##########

class pp_VAN_CS2_003(Preset_Play):
	""" Mind Vision
	Put a copy of a random card in your opponent's hand into your hand. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_003", self.controller)
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


##########VAN_CS2_004##########

class pp_VAN_CS2_004(Preset_Play):
	""" Power Word: Shield
	Give a minion +2_Health.Draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_004", self.controller)
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


##########VAN_CS2_234##########

class pp_VAN_CS2_234(Preset_Play):
	""" Shadow Word: Pain
	Destroy a minion with 3_or less Attack. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_234", self.controller)
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


##########VAN_CS2_235##########

class pp_VAN_CS2_235(Preset_Play):
	""" Northshire Cleric
	Whenever a minion is healed, draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_235", self.controller)
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


##########VAN_CS2_236##########

class pp_VAN_CS2_236(Preset_Play):
	""" Divine Spirit
	Double a minion's Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_236", self.controller)
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


##########VAN_DS1_233##########

class pp_VAN_DS1_233(Preset_Play):
	""" Mind Blast
	Deal $5 damage to the enemy hero. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_DS1_233", self.controller)
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


##########VAN_EX1_091##########

class pp_VAN_EX1_091(Preset_Play):
	""" Cabal Shadow Priest
	[Battlecry:] Take control of an enemy minion that has 2 or less Attack. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_091", self.controller)
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


##########VAN_EX1_332##########

class pp_VAN_EX1_332(Preset_Play):
	""" Silence
	[Silence] a minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_332", self.controller)
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


##########VAN_EX1_334##########

class pp_VAN_EX1_334(Preset_Play):
	""" Shadow Madness
	Gain control of an enemy minion with 3 or less Attack until end of turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_334", self.controller)
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


##########VAN_EX1_335##########

class pp_VAN_EX1_335(Preset_Play):
	""" Lightspawn
	This minion's Attack is always equal to its Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_335", self.controller)
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


##########VAN_EX1_339##########

class pp_VAN_EX1_339(Preset_Play):
	""" Thoughtsteal
	Copy 2 cards in your opponent's deck and add them to your hand. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_339", self.controller)
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


##########VAN_EX1_341##########

class pp_VAN_EX1_341(Preset_Play):
	""" Lightwell
	At the start of your turn, restore #3 Health to a damaged friendly character. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_341", self.controller)
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


##########VAN_EX1_345##########

class pp_VAN_EX1_345(Preset_Play):
	""" Mindgames
	Put a copy ofa random minion fromyour opponent's deck into the battlefield. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_345", self.controller)
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


##########VAN_EX1_350##########

class pp_VAN_EX1_350(Preset_Play):
	""" Prophet Velen
	Double the damage and healing of your spells and Hero Power. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_350", self.controller)
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


##########VAN_EX1_591##########

class pp_VAN_EX1_591(Preset_Play):
	""" Auchenai Soulpriest
	Your cards and powers that restore Health now deal damage instead. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_591", self.controller)
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


##########VAN_EX1_621##########

class pp_VAN_EX1_621(Preset_Play):
	""" Circle of Healing
	Restore #4 Health to ALL_minions. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_621", self.controller)
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


##########VAN_EX1_622##########

class pp_VAN_EX1_622(Preset_Play):
	""" Shadow Word: Death
	Destroy a minion with 5_or more Attack. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_622", self.controller)
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


##########VAN_EX1_623##########

class pp_VAN_EX1_623(Preset_Play):
	""" Temple Enforcer
	[Battlecry:] Give a friendly minion +3 Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_623", self.controller)
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


##########VAN_EX1_624##########

class pp_VAN_EX1_624(Preset_Play):
	""" Holy Fire
	Deal $5 damage. Restore #5 Health to your hero. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_624", self.controller)
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


##########VAN_EX1_625##########

class pp_VAN_EX1_625(Preset_Play):
	""" Shadowform
	Your Hero Power becomes 'Deal 2 damage.' If already in Shadowform: 3 damage. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_625", self.controller)
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


##########VAN_EX1_626##########

class pp_VAN_EX1_626(Preset_Play):
	""" Mass Dispel
	[Silence] all enemy minions. Draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_626", self.controller)
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


##########VAN_EX1_tk31##########

class pp_VAN_EX1_tk31(Preset_Play):
	""" Mind Controlling
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_tk31", self.controller)
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


##########VAN_HERO_09bp##########

class pp_VAN_HERO_09bp(Preset_Play):
	""" Lesser Heal
	[Hero Power]Restore #2 Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_HERO_09bp", self.controller)
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


##########VAN_HERO_09e1##########

class pp_VAN_HERO_09e1(Preset_Play):
	""" Lesser Fortitude
	+1 Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_HERO_09e1", self.controller)
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


