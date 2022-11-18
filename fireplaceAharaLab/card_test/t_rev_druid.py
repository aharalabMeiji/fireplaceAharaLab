from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def rev_druid():

	#PresetGame(pp_MAW_024)##
	#PresetGame(pp_MAW_025)##
	#PresetGame(pp_MAW_026)##
	#PresetGame(pp_REV_307)##
	#PresetGame(pp_REV_310)##
	#PresetGame(pp_REV_311)##
	#PresetGame(pp_REV_313)##
	#PresetGame(pp_REV_314)##
	#PresetGame(pp_REV_318)##
	#PresetGame(pp_REV_319)##
	#PresetGame(pp_REV_333)##
	#PresetGame(pp_REV_336)##
	#PresetGame(pp_REV_365)##
	#PresetGame(pp_REV_782)##
	#PresetGame(pp_REV_792)##
	pass


##########MAW_024##########

class pp_MAW_024(Preset_Play):
	""" Dew Process
	For the rest of the game, players draw an extra card at the start of their turn. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_024", self.controller)
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


##########MAW_025##########

class pp_MAW_025(Preset_Play):
	""" Attorney-at-Maw
	<b>Choose One -</b> <b>Silence</b> a minion; or Give a minion <b>Immune</b> this turn. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_025", self.controller)
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


##########MAW_026##########

class pp_MAW_026(Preset_Play):
	""" Incarceration
	Choose a minion. It goes <b>Dormant</b> for 3 turns. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_026", self.controller)
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


##########REV_307##########

class pp_REV_307(Preset_Play):
	""" Natural Causes
	Deal $2 damage. Summon a 2/2 Treant. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("REV_307", self.controller)
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


##########REV_310##########

class pp_REV_310(Preset_Play):
	""" Death Blossom Whomper
	<b>Battlecry:</b> Draw a <b>Deathrattle</b> minion and gain its <b>Deathrattle.</b> """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("REV_310", self.controller)
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


##########REV_311##########

class pp_REV_311(Preset_Play):
	""" Nightshade Bud
	<b>Choose One - </b><b>Discover</b> a minion from your deck to summon; or a spell to cast. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("REV_311", self.controller)
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


##########REV_313##########

class pp_REV_313(Preset_Play):
	""" Planted Evidence
	<b>Discover</b> a spell. It costs (2) less this turn. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("REV_313", self.controller)
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


##########REV_314##########

class pp_REV_314(Preset_Play):
	""" Topior the Shrubbagazzor
	<b>Battlecry:</b> For the rest of the game, after you cast a Nature spell, summon a 3/3 Whelp with <b>Rush</b>. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("REV_314", self.controller)
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


##########REV_318##########

class pp_REV_318(Preset_Play):
	""" Widowbloom Seedsman
	<b>Battlecry:</b> Draw a Nature spell. Gain an empty Mana Crystal. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("REV_318", self.controller)
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


##########REV_319##########

class pp_REV_319(Preset_Play):
	""" Sesselie of the Fae Court
	<b>Taunt</b> <b>Deathrattle</b>: Draw a minion. Reduce its Cost by (8). """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("REV_319", self.controller)
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


##########REV_333##########

class pp_REV_333(Preset_Play):
	""" Hedge Maze
	Trigger a friendly minion's <b>Deathrattle</b>. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("REV_333", self.controller)
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


##########REV_336##########

class pp_REV_336(Preset_Play):
	""" Plot of Sin
	Summon two 2/2  Treants. <b>Infuse (@):</b> Two  5/5 Ancients instead. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("REV_336", self.controller)
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


##########REV_365##########

class pp_REV_365(Preset_Play):
	""" Convoke the Spirits
	Cast 8 random Druid spells <i>(targets chosen randomly)</i>. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("REV_365", self.controller)
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


##########REV_782##########

class pp_REV_782(Preset_Play):
	""" Sesselie of the Fae Court
	{0} {1} {2} {3} """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("REV_782", self.controller)
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


##########REV_792##########

class pp_REV_792(Preset_Play):
	""" Hedge Maze
	{0} {1} """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("REV_792", self.controller)
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


