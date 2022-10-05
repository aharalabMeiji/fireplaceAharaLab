from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def rev_demonhunter():

	#PresetGame(pp_MAW_008)##
	#PresetGame(pp_MAW_012)##
	#PresetGame(pp_MAW_014)##
	#PresetGame(pp_REV_506)##
	#PresetGame(pp_REV_507)##
	#PresetGame(pp_REV_508)##
	#PresetGame(pp_REV_509)##
	#PresetGame(pp_REV_510)##
	#PresetGame(pp_REV_511)##
	#PresetGame(pp_REV_787)##
	#PresetGame(pp_REV_797)##
	#PresetGame(pp_REV_834)##
	#PresetGame(pp_REV_937)##
	#PresetGame(pp_REV_942)##
	PresetGame(pp_REV_943)##
	pass


##########MAW_008##########

class pp_MAW_008(Preset_Play):
	""" Sightless Magistrate
	<b>Battlecry:</b> Both players draw until they have 5 cards. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_008", self.controller)
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


##########MAW_012##########

class pp_MAW_012(Preset_Play):
	""" All Fel Breaks Loose
	Summon a friendly Demon that died this game. <b>Infuse (@ Demons):</b> Summon three instead. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_012", self.controller)
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


##########MAW_014##########

class pp_MAW_014(Preset_Play):
	""" Prosecutor Mel'tranix
	<b>Battlecry:</b> Your opponent can only play their left-  and right-most cards on  their next turn. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_014", self.controller)
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


##########REV_506##########

class pp_REV_506(Preset_Play):
	""" Sinful Brand
	Brand an enemy minion. Whenever it takes damage, deal 2 damage to the enemy hero. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_506", self.controller)
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


##########REV_507##########

class pp_REV_507(Preset_Play):
	""" Dispose of Evidence
	Give your hero +3 Attack this turn. Choose a card in your hand to shuffle into your deck. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_507", self.controller)
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


##########REV_508##########

class pp_REV_508(Preset_Play):
	""" Relic of Dimensions
	Draw two cards  and reduce their Cost  by (@). Improve your  future Relics. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_508", self.controller)
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


##########REV_509##########

class pp_REV_509(Preset_Play):
	""" Magnifying Glaive
	After your hero attacks, draw until you have 3 cards. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_509", self.controller)
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


##########REV_510##########

class pp_REV_510(Preset_Play):
	""" Kryxis the Voracious
	<b>Battlecry</b>: Discard your hand. <b>Deathrattle:</b> Draw 3 cards. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_510", self.controller)
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


##########REV_511##########

class pp_REV_511(Preset_Play):
	""" Bibliomite
	<b>Battlecry</b>: Choose a card  in your hand to shuffle  into your deck. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_511", self.controller)
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


##########REV_787##########

class pp_REV_787(Preset_Play):
	""" Artificer Xy'mox
	{0} {1} {2} {3} """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_787", self.controller)
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


##########REV_797##########

class pp_REV_797(Preset_Play):
	""" Relic Vault
	{0} {1} """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_797", self.controller)
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


##########REV_834##########

class pp_REV_834(Preset_Play):
	""" Relic of Extinction
	Deal $@ damage to a random enemy minion, twice. Improve your future Relics. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_834", self.controller)
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


##########REV_937##########

class pp_REV_937(Preset_Play):
	""" Artificer Xy'mox
	<b>Battlecry:</b> <b>Discover</b> and  cast a Relic. <b>Infuse (@):</b>  Cast all three instead. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_937", self.controller)
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


##########REV_942##########

class pp_REV_942(Preset_Play):
	""" Relic Vault
	The next Relic you play this turn casts twice. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_942", self.controller)
		self.con4=Summon(self.controller, self.card_choice("REV_943")).trigger(self.controller)
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


##########REV_943##########

class pp_REV_943(Preset_Play):
	""" Relic of Phantasms
	Summon two @/@ Spirits. Improve your future Relics. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_943", self.controller)
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


