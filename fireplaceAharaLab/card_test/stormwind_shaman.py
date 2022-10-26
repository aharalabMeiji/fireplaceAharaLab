from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def stormwind_shaman():

	#PresetGame(pp_DED_509)### OK ###
	#PresetGame(pp_DED_511)##
	#PresetGame(pp_DED_522)##
	#PresetGame(pp_SW_025)##
	#PresetGame(pp_SW_026)##
	#PresetGame(pp_SW_031)##
	#PresetGame(pp_SW_032)##
	#PresetGame(pp_SW_033)##
	#PresetGame(pp_SW_034)##
	#PresetGame(pp_SW_035)##
	#PresetGame(pp_SW_095)##
	#PresetGame(pp_SW_114)##
	#PresetGame(pp_SW_115)##
	pass

##########DED_509##########

class pp_DED_509(Preset_Play):
	""" Brilliant Macaw
	[Battlecry:] Repeat the last [Battlecry] you played. """
	class1 = CardClass.SHAMAN
	class2 = CardClass.SHAMAN
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_509", self.controller)
		self.mark2=self.exchange_card("DED_523", self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("beast")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]		
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark2, target=self.opp1)
		self.change_turn()
		### opp
		self.change_turn()
		### con
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		print ("Check if mark1 battlecry is similar as that of mark2.")
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########DED_511##########

class pp_DED_511(Preset_Play):
	""" Suckerhook
	At the end of your turn,transform your weapon intoone that costs (1) more. """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_511", self.controller)
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


##########DED_522##########

class pp_DED_522(Preset_Play):
	""" Cookie the Cook
	[Lifesteal][Deathrattle:] Equip a 2/3__Stirring Rod with [Lifesteal]._ """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_522", self.controller)
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


##########SW_025##########

class pp_SW_025(Preset_Play):
	""" Auctionhouse Gavel
	After your hero attacks,reduce the Cost of a[Battlecry] minion inyour hand by (1). """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_025", self.controller)
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


##########SW_026##########

class pp_SW_026(Preset_Play):
	""" Spirit Alpha
	After you play a card with[Overload], summon a 2/3Spirit Wolf with [Taunt]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_026", self.controller)
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


##########SW_031##########

class pp_SW_031(Preset_Play):
	""" Command the Elements
	[Questline:] Play 3 cards with [Overload].[Reward:] Unlock your[Overloaded] Mana Crystals. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_031", self.controller)
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


##########SW_032##########

class pp_SW_032(Preset_Play):
	""" Granite Forgeborn
	[Battlecry:] Reduce the cost of Elementals in your hand and deck by (1). """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_032", self.controller)
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


##########SW_033##########

class pp_SW_033(Preset_Play):
	""" Canal Slogger
	[Rush], [Lifesteal][Overload:] (1) """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_033", self.controller)
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


##########SW_034##########

class pp_SW_034(Preset_Play):
	""" Tiny Toys
	Summon four random 5-Cost minions.Make them 2/2. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_034", self.controller)
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


##########SW_035##########

class pp_SW_035(Preset_Play):
	""" Charged Call
	[Discover] a @-Costminion and summon it. <i>(Upgraded for each [Overload] card you played this game!)</i> """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_035", self.controller)
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


##########SW_095##########

class pp_SW_095(Preset_Play):
	""" Investment Opportunity
	Draw an [Overload] card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_095", self.controller)
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


##########SW_114##########

class pp_SW_114(Preset_Play):
	""" Overdraft
	[Tradeable]Unlock your [Overloaded]Mana Crystals to dealthat much damage. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_114", self.controller)
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


##########SW_115##########

class pp_SW_115(Preset_Play):
	""" Bolner Hammerbeak
	After you play a [Battlecry]minion, repeat the first__[Battlecry] played this turn._ """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_115", self.controller)
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


