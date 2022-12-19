from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def lich_warrior():

	#PresetGame(pp_RLK_600)##
	#PresetGame(pp_RLK_601)##
	#PresetGame(pp_RLK_602)##
	#PresetGame(pp_RLK_603)##
	#PresetGame(pp_RLK_604)##
	#PresetGame(pp_RLK_605)##
	#PresetGame(pp_RLK_607)##
	#PresetGame(pp_RLK_608)##
	#PresetGame(pp_RLK_609)##
	#PresetGame(pp_RLK_960)##
	pass


##########RLK_600##########

class pp_RLK_600(Preset_Play):
	""" Sunfire Smithing
	Equip a 4/2 Sword. Give a random minion in your hand +4/+2. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_600", self.controller)
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


##########RLK_601##########

class pp_RLK_601(Preset_Play):
	""" Last Stand
	Draw a <b>Taunt</b> minion. Double its stats. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_601", self.controller)
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


##########RLK_602##########

class pp_RLK_602(Preset_Play):
	""" Silverfury Stalwart
	<b><b>Taunt</b>, Rush</b> Can't be targeted by spells or Hero Powers. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_602", self.controller)
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


##########RLK_603##########

class pp_RLK_603(Preset_Play):
	""" Light of the Phoenix
	Draw 2 cards. Costs (1) less for each damaged friendly character. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_603", self.controller)
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


##########RLK_604##########

class pp_RLK_604(Preset_Play):
	""" Thori'belore
	<b>Rush</b>. <b>Deathrattle:</b> Go <b>Dormant</b>. Cast a Fire spell to revive Thori'belore! <i>(Revives 2 times.)</i> """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_604", self.controller)
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


##########RLK_605##########

class pp_RLK_605(Preset_Play):
	""" Blazing Power
	Give a minion +1/+1. Repeat for each damaged friendly character. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_605", self.controller)
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


##########RLK_607##########

class pp_RLK_607(Preset_Play):
	""" Disruptive Spellbreaker
	At the end of your turn, your opponent discards a spell. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_607", self.controller)
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


##########RLK_608##########

class pp_RLK_608(Preset_Play):
	""" Asvedon, the Grandshield
	<b>Battlecry:</b> Cast a copy of the last spell your opponent played. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_608", self.controller)
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


##########RLK_609##########

class pp_RLK_609(Preset_Play):
	""" Sunfury Champion
	After you cast a Fire spell, deal 1 damage to all minions. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_609", self.controller)
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


##########RLK_960##########

class pp_RLK_960(Preset_Play):
	""" Embers of Strength
	Summon two 1/2 Guards with <b>Taunt</b>. <b>Manathirst (6):</b> Give them +1/+2. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_960", self.controller)
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


