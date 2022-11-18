from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity

def classic_mage():

	#PresetGame(pp_Story_11_Frostbolt)##
	#PresetGame(pp_Story_11_PyroblastPuzzle)##
	#PresetGame(pp_VAN_CS2_022)##
	#PresetGame(pp_VAN_CS2_023)##
	#PresetGame(pp_VAN_CS2_024)##
	#PresetGame(pp_VAN_CS2_025)##
	#PresetGame(pp_VAN_CS2_026)##
	#PresetGame(pp_VAN_CS2_027)##
	#PresetGame(pp_VAN_CS2_028)##
	#PresetGame(pp_VAN_CS2_029)##
	#PresetGame(pp_VAN_CS2_031)##
	#PresetGame(pp_VAN_CS2_032)##
	#PresetGame(pp_VAN_CS2_033)##
	#PresetGame(pp_VAN_CS2_mirror)##
	#PresetGame(pp_VAN_EX1_274)##
	#PresetGame(pp_VAN_EX1_275)##
	#PresetGame(pp_VAN_EX1_277)##
	#PresetGame(pp_VAN_EX1_279)##
	#PresetGame(pp_VAN_EX1_287)##
	#PresetGame(pp_VAN_EX1_289)##
	#PresetGame(pp_VAN_EX1_294)##
	#PresetGame(pp_VAN_EX1_295)##
	#PresetGame(pp_VAN_EX1_559)##
	#PresetGame(pp_VAN_EX1_594)##
	#PresetGame(pp_VAN_EX1_608)##
	#PresetGame(pp_VAN_EX1_612)##
	#PresetGame(pp_VAN_HERO_08bp)##
	#PresetGame(pp_VAN_NEW1_012)##
	#PresetGame(pp_VAN_tt_010)##


##########Story_11_Frostbolt##########

class pp_Story_11_Frostbolt(Preset_Play):
	""" Frostbolt
	Deal $3 damage to a_character and [Freeze] it. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_Frostbolt", self.controller)
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


##########Story_11_PyroblastPuzzle##########

class pp_Story_11_PyroblastPuzzle(Preset_Play):
	""" Pyroblast
	Deal $10 damage. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_PyroblastPuzzle", self.controller)
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


##########VAN_CS2_022##########

class pp_VAN_CS2_022(Preset_Play):
	""" Polymorph
	Transform a minioninto a 1/1 Sheep. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_022", self.controller)
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


##########VAN_CS2_023##########

class pp_VAN_CS2_023(Preset_Play):
	""" Arcane Intellect
	Draw 2 cards. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_023", self.controller)
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


##########VAN_CS2_024##########

class pp_VAN_CS2_024(Preset_Play):
	""" Frostbolt
	Deal $3 damage to a_character and [Freeze] it. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_024", self.controller)
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


##########VAN_CS2_025##########

class pp_VAN_CS2_025(Preset_Play):
	""" Arcane Explosion
	Deal $1 damage to all enemy minions. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_025", self.controller)
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


##########VAN_CS2_026##########

class pp_VAN_CS2_026(Preset_Play):
	""" Frost Nova
	[Freeze] all enemy minions. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_026", self.controller)
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


##########VAN_CS2_027##########

class pp_VAN_CS2_027(Preset_Play):
	""" Mirror Image
	Summon two 0/2 minions with [Taunt]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_027", self.controller)
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


##########VAN_CS2_028##########

class pp_VAN_CS2_028(Preset_Play):
	""" Blizzard
	Deal $2 damage to all enemy minions and [Freeze] them. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_028", self.controller)
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


##########VAN_CS2_029##########

class pp_VAN_CS2_029(Preset_Play):
	""" Fireball
	Deal $6 damage. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_029", self.controller)
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


##########VAN_CS2_031##########

class pp_VAN_CS2_031(Preset_Play):
	""" Ice Lance
	[Freeze] a character. If it was already [Frozen], deal $4 damage instead. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_031", self.controller)
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


##########VAN_CS2_032##########

class pp_VAN_CS2_032(Preset_Play):
	""" Flamestrike
	Deal $4 damage to all enemy minions. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_032", self.controller)
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


##########VAN_CS2_033##########

class pp_VAN_CS2_033(Preset_Play):
	""" Water Elemental
	[Freeze] any character damaged by this minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_033", self.controller)
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


##########VAN_CS2_mirror##########

class pp_VAN_CS2_mirror(Preset_Play):
	""" Mirror Image
	[Taunt] """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_mirror", self.controller)
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


##########VAN_EX1_274##########

class pp_VAN_EX1_274(Preset_Play):
	""" Ethereal Arcanist
	If you control a [Secret] at_the end of your turn, gain +2/+2. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_274", self.controller)
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


##########VAN_EX1_275##########

class pp_VAN_EX1_275(Preset_Play):
	""" Cone of Cold
	[Freeze] a minion and the minions next to it, and deal $1 damage to them. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_275", self.controller)
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


##########VAN_EX1_277##########

class pp_VAN_EX1_277(Preset_Play):
	""" Arcane Missiles
	Deal $3 damage randomly split among all enemy characters. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_277", self.controller)
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


##########VAN_EX1_279##########

class pp_VAN_EX1_279(Preset_Play):
	""" Pyroblast
	Deal $10 damage. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_279", self.controller)
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


##########VAN_EX1_287##########

class pp_VAN_EX1_287(Preset_Play):
	""" Counterspell
	[Secret:] When your opponent casts a spell, [Counter] it. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_287", self.controller)
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


##########VAN_EX1_289##########

class pp_VAN_EX1_289(Preset_Play):
	""" Ice Barrier
	[Secret:] As soon as yourhero is attacked, gain8 Armor. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_289", self.controller)
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


##########VAN_EX1_294##########

class pp_VAN_EX1_294(Preset_Play):
	""" Mirror Entity
	[Secret:] Whenyour opponent plays aminion, summon a copyof it. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_294", self.controller)
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


##########VAN_EX1_295##########

class pp_VAN_EX1_295(Preset_Play):
	""" Ice Block
	[Secret:] When your hero takes fatal damage, prevent it and become [Immune] this turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_295", self.controller)
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


##########VAN_EX1_559##########

class pp_VAN_EX1_559(Preset_Play):
	""" Archmage Antonidas
	Whenever you cast a spell, add a 'Fireball' spell to_your hand. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_559", self.controller)
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


##########VAN_EX1_594##########

class pp_VAN_EX1_594(Preset_Play):
	""" Vaporize
	[Secret:] When a minion attacks your hero, destroy it. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_594", self.controller)
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


##########VAN_EX1_608##########

class pp_VAN_EX1_608(Preset_Play):
	""" Sorcerer's Apprentice
	Your spells cost (1) less. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_608", self.controller)
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


##########VAN_EX1_612##########

class pp_VAN_EX1_612(Preset_Play):
	""" Kirin Tor Mage
	[Battlecry:] The next [Secret]you play this turn costs (0). """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_612", self.controller)
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


##########VAN_HERO_08bp##########

class pp_VAN_HERO_08bp(Preset_Play):
	""" Fireblast
	[Hero Power]Deal $1 damage. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_HERO_08bp", self.controller)
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


##########VAN_NEW1_012##########

class pp_VAN_NEW1_012(Preset_Play):
	""" Mana Wyrm
	Whenever you cast a spell, gain +1 Attack. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_NEW1_012", self.controller)
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


##########VAN_tt_010##########

class pp_VAN_tt_010(Preset_Play):
	""" Spellbender
	[Secret:] When an enemy casts a spell on a minion, summon a 1/3 as the new target. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_tt_010", self.controller)
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


