from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def lich_deathknight():

	#PresetGame(pp_RLK_012)##
	#PresetGame(pp_RLK_035)##
	#PresetGame(pp_RLK_051)##
	#PresetGame(pp_RLK_116)##
	#PresetGame(pp_RLK_120)##
	#PresetGame(pp_RLK_121)##
	#PresetGame(pp_RLK_225)##
	#PresetGame(pp_RLK_506)##
	#PresetGame(pp_RLK_706)##
	#PresetGame(pp_RLK_741)##
	pass


##########RLK_012##########

class pp_RLK_012(Preset_Play):
	""" Soulbreaker
	After your hero attacks and kills a minion, gain 2 <b>Corpses</b>. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_012", self.controller)
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


##########RLK_035##########

class pp_RLK_035(Preset_Play):
	""" Corpse Explosion
	Detonate a <b>Corpse</b> to deal $1 damage to all minions. If any are still alive, repeat this. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_035", self.controller)
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


##########RLK_051##########

class pp_RLK_051(Preset_Play):
	""" Vampiric Blood
	Give your hero +5 Health. Spend 3 <b>Corpses</b> to gain 5 more and draw a card. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_051", self.controller)
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


##########RLK_116##########

class pp_RLK_116(Preset_Play):
	""" Necrotic Mortician
	<b>Battlecry:</b> If a friendly Undead died after your last turn, <b>Discover</b> an Unholy Rune card. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_116", self.controller)
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


##########RLK_120##########

class pp_RLK_120(Preset_Play):
	""" Meat Grinder
	<b>Battlecry:</b> Shred a random minion in your deck to gain 3 <b>Corpses.</b> """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_120", self.controller)
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


##########RLK_121##########

class pp_RLK_121(Preset_Play):
	""" Acolyte of Death
	After a friendly Undead dies, draw a card. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_121", self.controller)
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


##########RLK_225##########

class pp_RLK_225(Preset_Play):
	""" Blightfang
	<b>Battlecry:</b> Infect all enemy minions. When they die, you summon a 2/2 Zombie with <b>Taunt</b>. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_225", self.controller)
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


##########RLK_506##########

class pp_RLK_506(Preset_Play):
	""" Boneguard Commander
	<b>Taunt</b> <b>Battlecry:</b> Raise up to 6 <b>Corpses</b> as 1/2 Risen Footmen with <b>Taunt</b>. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_506", self.controller)
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


##########RLK_706##########

class pp_RLK_706(Preset_Play):
	""" Alexandros Mograine
	<b>Battlecry:</b> For the rest of the game, deal 3 damage to your opponent at the end of your turns. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_706", self.controller)
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


##########RLK_741##########

class pp_RLK_741(Preset_Play):
	""" Soulstealer
	<b>Battlecry:</b> Destroy all other minions. Gain 1 <b>Corpse</b> for each enemy destroyed. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_741", self.controller)
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



