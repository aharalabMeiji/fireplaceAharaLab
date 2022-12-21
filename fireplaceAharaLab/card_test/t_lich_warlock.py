from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def lich_warlock():

	PresetGame(pp_RLK_531)##
	PresetGame(pp_RLK_532)##
	PresetGame(pp_RLK_533)##
	#PresetGame(pp_RLK_534)##
	#PresetGame(pp_RLK_535)##
	PresetGame(pp_RLK_536)##
	PresetGame(pp_RLK_537)##
	PresetGame(pp_RLK_538)##
	#PresetGame(pp_RLK_539)##
	PresetGame(pp_RLK_540)##
	pass


##########RLK_531##########

class pp_RLK_531(Preset_Play):
	""" Infantry Reanimator
	<b>Battlecry:</b> Resurrect a friendly Undead. Give it <b>Reborn</b>. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_531", self.controller)
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


##########RLK_532##########

class pp_RLK_532(Preset_Play):
	""" Walking Dead
	<b>Taunt</b> If you discard this minion, summon it. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_532", self.controller)
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


##########RLK_533##########

class pp_RLK_533(Preset_Play):
	""" Scourge Supplies
	Draw 3 cards. Choose one to discard. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_533", self.controller)
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


##########RLK_534##########

class pp_RLK_534(Preset_Play):
	""" Soul Barrage
	When you play or discard this, deal $6 damage randomly split among all enemies. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_534", self.controller)
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


##########RLK_535##########

class pp_RLK_535(Preset_Play):
	""" Savage Ymirjar
	<b>Rush</b> <b>Battlecry:</b> Discard 2 cards. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_535", self.controller)
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


##########RLK_536##########

class pp_RLK_536(Preset_Play):
	""" Shallow Grave
	Trigger a friendly minion's <b>Deathrattle</b>, then destroy it. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_536", self.controller)
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


##########RLK_537##########

class pp_RLK_537(Preset_Play):
	""" Twisted Tether
	Destroy a minion. Give its stats to a random Undead in your hand. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_537", self.controller)
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


##########RLK_538##########

class pp_RLK_538(Preset_Play):
	""" Devourer of Souls
	After a friendly minion dies, gain its <b>Deathrattle</b>. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_538", self.controller)
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


##########RLK_539##########

class pp_RLK_539(Preset_Play):
	""" Dar'Khan Drathir
	<b>Lifesteal</b> At the end of your turn, deal 6 damage to the enemy hero. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_539", self.controller)
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


##########RLK_540##########

class pp_RLK_540(Preset_Play):
	""" Amorphous Slime
	<b>Battlecry:</b> Discard a random Undead. <b>Deathrattle:</b> Summon a copy of it. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_540", self.controller)
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


