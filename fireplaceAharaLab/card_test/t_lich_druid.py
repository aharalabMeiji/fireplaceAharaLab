from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def lich_druid():

	#PresetGame(pp_RLK_650)##
	#PresetGame(pp_RLK_651)##
	#PresetGame(pp_RLK_652)##
	#PresetGame(pp_RLK_654)##
	#PresetGame(pp_RLK_655)##
	#PresetGame(pp_RLK_656)##
	#PresetGame(pp_RLK_657)##
	#PresetGame(pp_RLK_658)##
	#PresetGame(pp_RLK_659)##
	#PresetGame(pp_RLK_956)##
	pass


##########RLK_650##########

class pp_RLK_650(Preset_Play):
	""" Lingering Zombie
	<b>Deathrattle:</b> Summon a 1/1 Disarmed Zombie with "<b>Deathrattle:</b> Summon a 1/1 Zombie." """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_650", self.controller)
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


##########RLK_651##########

class pp_RLK_651(Preset_Play):
	""" Crypt Keeper
	<b>Taunt</b>. Costs (1) less for each Armor you have. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_651", self.controller)
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


##########RLK_652##########

class pp_RLK_652(Preset_Play):
	""" Unending Swarm
	Resurrect all friendly minions that cost (2) or less. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_652", self.controller)
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


##########RLK_654##########

class pp_RLK_654(Preset_Play):
	""" Beetlemancy
	<b>Choose One</b> - Gain 12 Armor; or Summon two 3/3 Beetles with <b>Taunt</b>. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_654", self.controller)
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


##########RLK_655##########

class pp_RLK_655(Preset_Play):
	""" Wither
	Choose a minion. Each friendly Undead steals 1 Attack and Health from it. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_655", self.controller)
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


##########RLK_656##########

class pp_RLK_656(Preset_Play):
	""" Chitinous Plating
	Gain 4 Armor. At the start of your next turn, gain 4 more. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_656", self.controller)
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


##########RLK_657##########

class pp_RLK_657(Preset_Play):
	""" Underking
	<b>Rush</b> <b>Battlecry and Deathrattle:</b> Gain 6 Armor. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_657", self.controller)
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


##########RLK_658##########

class pp_RLK_658(Preset_Play):
	""" Elder Nadox
	<b>Battlecry:</b> Destroy a friendly Undead. Your minions gain its Attack. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_658", self.controller)
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


##########RLK_659##########

class pp_RLK_659(Preset_Play):
	""" Anub'Rekhan
	<b>Battlecry:</b> Gain 8 Armor. This turn, your minions cost Armor instead of Mana. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_659", self.controller)
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


##########RLK_956##########

class pp_RLK_956(Preset_Play):
	""" Nerubian Flyer
	<b>Battlecry:</b> If a friendly Undead died after your last turn, summon a 2/2 Nerubian. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_956", self.controller)
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


