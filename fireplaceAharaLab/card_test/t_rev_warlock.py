from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def rev_warlock():

	#PresetGame(pp_MAW_000)##
	#PresetGame(pp_MAW_001)##
	#PresetGame(pp_MAW_002)##
	#PresetGame(pp_REV_239)##
	#PresetGame(pp_REV_240)##
	#PresetGame(pp_REV_242)##
	#PresetGame(pp_REV_244)##
	#PresetGame(pp_REV_245)##
	#PresetGame(pp_REV_371)##
	#PresetGame(pp_REV_372)##
	#PresetGame(pp_REV_373)##
	#PresetGame(pp_REV_374)##
	#PresetGame(pp_REV_789)##
	#PresetGame(pp_REV_799)##
	#PresetGame(pp_REV_835)##
	pass


##########MAW_000##########

class pp_MAW_000(Preset_Play):
	""" Imp-oster
	<b>Battlecry:</b> Choose a friendly Imp. Transform into a copy of it. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_000", self.controller)
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


##########MAW_001##########

class pp_MAW_001(Preset_Play):
	""" Arson Accusation
	Choose a minion. Destroy it after your hero takes damage. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_001", self.controller)
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


##########MAW_002##########

class pp_MAW_002(Preset_Play):
	""" Habeas Corpses
	<b>Discover</b> a friendly minion to resurrect and give it <b>Rush</b>. It dies at the end of turn. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_002", self.controller)
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


##########REV_239##########

class pp_REV_239(Preset_Play):
	""" Suffocating Shadows
	When you play or  discard this, destroy a  random enemy minion. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("REV_239", self.controller)
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


##########REV_240##########

class pp_REV_240(Preset_Play):
	""" Tome Tampering
	Shuffle 1-Cost  copies of cards in your  hand into your deck,  then discard your hand. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("REV_240", self.controller)
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


##########REV_242##########

class pp_REV_242(Preset_Play):
	""" Flustered Librarian
	Has +1 Attack for each Imp you control. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("REV_242", self.controller)
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


##########REV_244##########

class pp_REV_244(Preset_Play):
	""" Mischievous Imp
	<b>Battlecry:</b> Summon a copy of this. <b>Infuse (@):</b> Summon two copies instead. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("REV_244", self.controller)
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


##########REV_245##########

class pp_REV_245(Preset_Play):
	""" Impending Catastrophe
	Draw a card. Repeat for each Imp you control. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("REV_245", self.controller)
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


##########REV_371##########

class pp_REV_371(Preset_Play):
	""" Vile Library
	Give a friendly minion +1/+1 for each Imp you control. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("REV_371", self.controller)
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


##########REV_372##########

class pp_REV_372(Preset_Play):
	""" Shadow Waltz
	Summon a 3/5 Shadow with <b>Taunt</b>. If a minion died this turn, summon another. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("REV_372", self.controller)
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


##########REV_373##########

class pp_REV_373(Preset_Play):
	""" Lady Darkvein
	<b>Battlecry:</b> Summon two 2/1 Shades. Each gains a <b>Deathrattle</b> to cast your  last Shadow spell. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("REV_373", self.controller)
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


##########REV_374##########

class pp_REV_374(Preset_Play):
	""" Shadowborn
	<b>Deathrattle:</b> Reduce the Cost of the highest Cost Shadow spell in your hand by (3). """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("REV_374", self.controller)
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


##########REV_789##########

class pp_REV_789(Preset_Play):
	""" Imp King Rafaam
	{0} {1} {2} {3} """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("REV_789", self.controller)
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


##########REV_799##########

class pp_REV_799(Preset_Play):
	""" Vile Library
	{0} {1} """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("REV_799", self.controller)
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


##########REV_835##########

class pp_REV_835(Preset_Play):
	""" Imp King Rafaam
	<b>Battlecry:</b> Resurrect four friendly Imps. <b>Infuse (@):</b> Give your Imps +2/+2. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("REV_835", self.controller)
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


