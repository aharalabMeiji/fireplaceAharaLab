from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity

def stormwind_demonhunter():

	#PresetGame(pp_DED_506)##
	#PresetGame(pp_DED_507)##
	#PresetGame(pp_DED_508)##
	#PresetGame(pp_SW_037)##
	#PresetGame(pp_SW_039)##
	#PresetGame(pp_SW_040)##
	#PresetGame(pp_SW_041)##
	#PresetGame(pp_SW_042)##
	#PresetGame(pp_SW_043)##
	#PresetGame(pp_SW_044)##
	#PresetGame(pp_SW_451)##
	#PresetGame(pp_SW_452)##
	#PresetGame(pp_SW_454)##
	pass

##########BOM_05_FelFanatic_001e##########

##########DED_506##########

class pp_DED_506(Preset_Play):
	""" Need for Greed
	[Tradeable]Draw 3 cards. If drawn this turn, this costs (3). """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_506", self.controller)
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


##########DED_507##########

class pp_DED_507(Preset_Play):
	""" Crow's Nest Lookout
	[Battlecry:] Deal 2 damageto the left and right-mostenemy minions. """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_507", self.controller)
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


##########DED_508##########

class pp_DED_508(Preset_Play):
	""" Proving Grounds
	Summon two minions from your deck.They fight! """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_508", self.controller)
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


##########SW_037##########

class pp_SW_037(Preset_Play):
	""" Irebound Brute
	[Taunt]Costs (1) less for eachcard drawn this turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_037", self.controller)
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


##########SW_039##########

class pp_SW_039(Preset_Play):
	""" Final Showdown
	[Questline:] Draw 4 cards in one turn. [Reward:] Reduce the Cost of the cards drawn by (1). """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_039", self.controller)
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


##########SW_040##########

class pp_SW_040(Preset_Play):
	""" Fel Barrage
	Deal $2 damage tothe lowest Healthenemy, twice. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_040", self.controller)
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


##########SW_041##########

class pp_SW_041(Preset_Play):
	""" Sigil of Alacrity
	At the start of your nextturn, draw a card and_reduce its Cost by (1). """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_041", self.controller)
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


##########SW_042##########

class pp_SW_042(Preset_Play):
	""" Persistent Peddler
	[Tradeable][Deathrattle:] Summon a Persistent Peddler from your deck. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_042", self.controller)
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


##########SW_043##########

class pp_SW_043(Preset_Play):
	""" Felgorger
	[Battlecry:] Draw a Fel spell. Reduce its Cost by (2). """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_043", self.controller)
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


##########SW_044##########

class pp_SW_044(Preset_Play):
	""" Jace Darkweaver
	[Battlecry:] Cast all Fel spells you've played this game <i>(targets enemies if possible)</i>. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_044", self.controller)
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


##########SW_451##########

class pp_SW_451(Preset_Play):
	""" Metamorfin
	[Taunt][Battlecry:] If you've cast a Fel spell this turn, gain +2/+2. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_451", self.controller)
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


##########SW_452##########

class pp_SW_452(Preset_Play):
	""" Chaos Leech
	[Lifesteal]. Deal $3 damage to a minion.[Outcast:] Deal $5 instead. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_452", self.controller)
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


##########SW_454##########

class pp_SW_454(Preset_Play):
	""" Lion's Frenzy
	Has Attack equal to the number of cards you've drawn this turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_454", self.controller)
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


