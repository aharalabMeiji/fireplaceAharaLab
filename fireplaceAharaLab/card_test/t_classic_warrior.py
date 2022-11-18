from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity

def classic_warrior():

	#PresetGame(pp_VAN_CS2_102_H3)##
	#PresetGame(pp_VAN_CS2_103)##
	#PresetGame(pp_VAN_CS2_104)##
	#PresetGame(pp_VAN_CS2_105)##
	#PresetGame(pp_VAN_CS2_106)##
	#PresetGame(pp_VAN_CS2_108)##
	#PresetGame(pp_VAN_CS2_112)##
	#PresetGame(pp_VAN_CS2_114)##
	#PresetGame(pp_VAN_EX1_084)##
	#PresetGame(pp_VAN_EX1_391)##
	#PresetGame(pp_VAN_EX1_392)##
	#PresetGame(pp_VAN_EX1_398)##
	#PresetGame(pp_VAN_EX1_400)##
	#PresetGame(pp_VAN_EX1_402)##
	#PresetGame(pp_VAN_EX1_407)##
	#PresetGame(pp_VAN_EX1_408)##
	#PresetGame(pp_VAN_EX1_409)##
	#PresetGame(pp_VAN_EX1_410)##
	#PresetGame(pp_VAN_EX1_411)##
	#PresetGame(pp_VAN_EX1_414)##
	#PresetGame(pp_VAN_EX1_603)##
	#PresetGame(pp_VAN_EX1_604)##
	#PresetGame(pp_VAN_EX1_606)##
	#PresetGame(pp_VAN_EX1_607)##
	#PresetGame(pp_VAN_HERO_01bp)##
	#PresetGame(pp_VAN_NEW1_011)##
	#PresetGame(pp_VAN_NEW1_036)##


##########VAN_CS2_102_H3##########

class pp_VAN_CS2_102_H3(Preset_Play):
	""" Armor Up!
	[Hero Power]Gain 2 Armor. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_102_H3", self.controller)
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


##########VAN_CS2_103##########

class pp_VAN_CS2_103(Preset_Play):
	""" Charge
	Give a friendly minion +2 Attack and [Charge]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_103", self.controller)
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


##########VAN_CS2_104##########

class pp_VAN_CS2_104(Preset_Play):
	""" Rampage
	Give a damaged minion +3/+3. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_104", self.controller)
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


##########VAN_CS2_105##########

class pp_VAN_CS2_105(Preset_Play):
	""" Heroic Strike
	Give your hero +4_Attack this turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_105", self.controller)
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


##########VAN_CS2_106##########

class pp_VAN_CS2_106(Preset_Play):
	""" Fiery War Axe
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_106", self.controller)
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


##########VAN_CS2_108##########

class pp_VAN_CS2_108(Preset_Play):
	""" Execute
	Destroy a damaged enemy minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_108", self.controller)
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


##########VAN_CS2_112##########

class pp_VAN_CS2_112(Preset_Play):
	""" Arcanite Reaper
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_112", self.controller)
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


##########VAN_CS2_114##########

class pp_VAN_CS2_114(Preset_Play):
	""" Cleave
	Deal $2 damage totwo random enemyminions. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_114", self.controller)
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


##########VAN_EX1_084##########

class pp_VAN_EX1_084(Preset_Play):
	""" Warsong Commander
	Whenever you summon a minion with 3 or less Attack, give it [Charge]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_084", self.controller)
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


##########VAN_EX1_391##########

class pp_VAN_EX1_391(Preset_Play):
	""" Slam
	Deal $2 damage to a minion. If it survives, draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_391", self.controller)
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


##########VAN_EX1_392##########

class pp_VAN_EX1_392(Preset_Play):
	""" Battle Rage
	Draw a card for each damaged friendly character. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_392", self.controller)
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


##########VAN_EX1_398##########

class pp_VAN_EX1_398(Preset_Play):
	""" Arathi Weaponsmith
	[Battlecry:] Equip a 2/2_weapon. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_398", self.controller)
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


##########VAN_EX1_400##########

class pp_VAN_EX1_400(Preset_Play):
	""" Whirlwind
	Deal $1 damage to ALL_minions. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_400", self.controller)
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


##########VAN_EX1_402##########

class pp_VAN_EX1_402(Preset_Play):
	""" Armorsmith
	Whenever a friendly minion_takes damage, gain 1 Armor. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_402", self.controller)
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


##########VAN_EX1_407##########

class pp_VAN_EX1_407(Preset_Play):
	""" Brawl
	Destroy all minions except one. <i>(chosen randomly)</i> """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_407", self.controller)
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


##########VAN_EX1_408##########

class pp_VAN_EX1_408(Preset_Play):
	""" Mortal Strike
	Deal $4 damage. If you have 12 or less Health, deal $6 instead. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_408", self.controller)
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


##########VAN_EX1_409##########

class pp_VAN_EX1_409(Preset_Play):
	""" Upgrade!
	If you have a weapon, give it +1/+1. Otherwise equip a 1/3 weapon. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_409", self.controller)
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


##########VAN_EX1_410##########

class pp_VAN_EX1_410(Preset_Play):
	""" Shield Slam
	Deal 1 damage to a minion for each Armor you have. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_410", self.controller)
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


##########VAN_EX1_411##########

class pp_VAN_EX1_411(Preset_Play):
	""" Gorehowl
	Attacking a minion costs 1 Attack instead of 1 Durability. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_411", self.controller)
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


##########VAN_EX1_414##########

class pp_VAN_EX1_414(Preset_Play):
	""" Grommash Hellscream
	[Charge][Enrage:] +6 Attack """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_414", self.controller)
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


##########VAN_EX1_603##########

class pp_VAN_EX1_603(Preset_Play):
	""" Cruel Taskmaster
	[Battlecry:] Deal 1 damage to a minion and give it +2_Attack. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_603", self.controller)
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


##########VAN_EX1_604##########

class pp_VAN_EX1_604(Preset_Play):
	""" Frothing Berserker
	Whenever a minion takes damage, gain +1 Attack. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_604", self.controller)
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


##########VAN_EX1_606##########

class pp_VAN_EX1_606(Preset_Play):
	""" Shield Block
	Gain 5 Armor.Draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_606", self.controller)
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


##########VAN_EX1_607##########

class pp_VAN_EX1_607(Preset_Play):
	""" Inner Rage
	Deal $1 damage to a minion and give it +2_Attack. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_607", self.controller)
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


##########VAN_HERO_01bp##########

class pp_VAN_HERO_01bp(Preset_Play):
	""" Armor Up!
	[Hero Power]Gain 2 Armor. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_HERO_01bp", self.controller)
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


##########VAN_NEW1_011##########

class pp_VAN_NEW1_011(Preset_Play):
	""" Kor'kron Elite
	[Charge] """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_NEW1_011", self.controller)
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


##########VAN_NEW1_036##########

class pp_VAN_NEW1_036(Preset_Play):
	""" Commanding Shout
	Your minions can't be reduced below 1 Health this turn. Draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_NEW1_036", self.controller)
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


