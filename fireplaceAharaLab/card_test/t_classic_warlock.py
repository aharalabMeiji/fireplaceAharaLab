from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity

def classic_warlock():


	#PresetGame(pp_VAN_CS2_057)##
	#PresetGame(pp_VAN_CS2_059)##
	#PresetGame(pp_VAN_CS2_061)##
	#PresetGame(pp_VAN_CS2_062)##
	#PresetGame(pp_VAN_CS2_063)##
	#PresetGame(pp_VAN_CS2_064)##
	#PresetGame(pp_VAN_CS2_065)##
	#PresetGame(pp_VAN_EX1_301)##
	PresetGame(pp_VAN_EX1_302)##
	#PresetGame(pp_VAN_EX1_303)##
	PresetGame(pp_VAN_EX1_304)##
	#PresetGame(pp_VAN_EX1_306)##
	#PresetGame(pp_VAN_EX1_308)##
	#PresetGame(pp_VAN_EX1_309)##
	PresetGame(pp_VAN_EX1_310)##
	#PresetGame(pp_VAN_EX1_312)##
	#PresetGame(pp_VAN_EX1_313)##
	#PresetGame(pp_VAN_EX1_315)##
	PresetGame(pp_VAN_EX1_316)##
	PresetGame(pp_VAN_EX1_317)##
	#PresetGame(pp_VAN_EX1_319)##
	PresetGame(pp_VAN_EX1_320)##
	PresetGame(pp_VAN_EX1_323)##
	#PresetGame(pp_VAN_EX1_596)##
	#PresetGame(pp_VAN_EX1_tk33)##
	#PresetGame(pp_VAN_EX1_tk34)##
	#PresetGame(pp_VAN_HERO_07bp)##
	#PresetGame(pp_VAN_NEW1_003)##



##########VAN_CS2_057##########

class pp_VAN_CS2_057(Preset_Play):
	""" Shadow Bolt
	Deal $4 damageto a minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_057", self.controller)
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


##########VAN_CS2_059##########

class pp_VAN_CS2_059(Preset_Play):
	""" Blood Imp
	  [Stealth]. At the end of your  turn, give another random friendly minion +1 Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_059", self.controller)
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


##########VAN_CS2_061##########

class pp_VAN_CS2_061(Preset_Play):
	""" Drain Life
	Deal $2 damage. Restore #2 Health to your hero. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_061", self.controller)
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


##########VAN_CS2_062##########

class pp_VAN_CS2_062(Preset_Play):
	""" Hellfire
	Deal $3 damage to ALL_characters. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_062", self.controller)
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


##########VAN_CS2_063##########

class pp_VAN_CS2_063(Preset_Play):
	""" Corruption
	Choose an enemy minion. At the start of your turn, destroy it. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_063", self.controller)
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


##########VAN_CS2_064##########

class pp_VAN_CS2_064(Preset_Play):
	""" Dread Infernal
	[Battlecry:] Deal 1 damage to ALL other characters. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_064", self.controller)
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


##########VAN_CS2_065##########

class pp_VAN_CS2_065(Preset_Play):
	""" Voidwalker
	[Taunt] """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_065", self.controller)
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


##########VAN_EX1_301##########

class pp_VAN_EX1_301(Preset_Play):
	""" Felguard
	[Taunt][Battlecry:] Destroy one of your Mana Crystals. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_301", self.controller)
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


##########VAN_EX1_302##########

class pp_VAN_EX1_302(Preset_Play):
	""" Mortal Coil
	Deal $1 damage to a minion. If that kills it, draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_302", self.controller)
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


##########VAN_EX1_303##########

class pp_VAN_EX1_303(Preset_Play):
	""" Shadowflame
	Destroy a friendly minion and deal its Attack damage to all enemy minions. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_303", self.controller)
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


##########VAN_EX1_304##########

class pp_VAN_EX1_304(Preset_Play):
	""" Void Terror
	[Battlecry:] Destroy bothadjacent minions and gain their Attack and Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_304", self.controller)
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


##########VAN_EX1_306##########

class pp_VAN_EX1_306(Preset_Play):
	""" Felstalker
	[Battlecry:] Discard a random card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_306", self.controller)
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


##########VAN_EX1_308##########

class pp_VAN_EX1_308(Preset_Play):
	""" Soulfire
	Deal $4 damage.Discard a random card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_308", self.controller)
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


##########VAN_EX1_309##########

class pp_VAN_EX1_309(Preset_Play):
	""" Siphon Soul
	Destroy a minion. Restore #3 Health to_your hero. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_309", self.controller)
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


##########VAN_EX1_310##########

class pp_VAN_EX1_310(Preset_Play):
	""" Doomguard
	[Charge]. [Battlecry:] Discard two random cards. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_310", self.controller)
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


##########VAN_EX1_312##########

class pp_VAN_EX1_312(Preset_Play):
	""" Twisting Nether
	Destroy all minions. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_312", self.controller)
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


##########VAN_EX1_313##########

class pp_VAN_EX1_313(Preset_Play):
	""" Pit Lord
	[Battlecry:] Deal 5 damage to your hero. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_313", self.controller)
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


##########VAN_EX1_315##########

class pp_VAN_EX1_315(Preset_Play):
	""" Summoning Portal
	Your minions cost (2) less, but not less than (1). """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_315", self.controller)
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


##########VAN_EX1_316##########

class pp_VAN_EX1_316(Preset_Play):
	""" Power Overwhelming
	Give a friendly minion +4/+4 until end of turn. Then, it dies. Horribly. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_316", self.controller)
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


##########VAN_EX1_317##########

class pp_VAN_EX1_317(Preset_Play):
	""" Sense Demons
	Draw 2 Demonsfrom your deck. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_317", self.controller)
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


##########VAN_EX1_319##########

class pp_VAN_EX1_319(Preset_Play):
	""" Flame Imp
	[Battlecry:] Deal 3 damage to your hero. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_319", self.controller)
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


##########VAN_EX1_320##########

class pp_VAN_EX1_320(Preset_Play):
	""" Bane of Doom
	Deal $2 damage to_a character. If that kills it, summon a random Demon. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_320", self.controller)
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


##########VAN_EX1_323##########

class pp_VAN_EX1_323(Preset_Play):
	""" Lord Jaraxxus
	[Battlecry:] Destroy your hero and replace it with Lord Jaraxxus. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_323", self.controller)
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


##########VAN_EX1_596##########

class pp_VAN_EX1_596(Preset_Play):
	""" Demonfire
	Deal $2 damage to a minion. If itÅfs a friendly Demon, give it +2/+2 instead. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_596", self.controller)
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


##########VAN_EX1_tk33##########

class pp_VAN_EX1_tk33(Preset_Play):
	""" INFERNO!
	[Hero Power]Summon a 6/6 Infernal. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_tk33", self.controller)
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


##########VAN_EX1_tk34##########

class pp_VAN_EX1_tk34(Preset_Play):
	""" Infernal
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_tk34", self.controller)
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


##########VAN_HERO_07bp##########

class pp_VAN_HERO_07bp(Preset_Play):
	""" Life Tap
	[Hero Power]Draw a card and take $2_damage. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_HERO_07bp", self.controller)
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


##########VAN_NEW1_003##########

class pp_VAN_NEW1_003(Preset_Play):
	""" Sacrificial Pact
	Destroy a Demon. Restore #5 Health to your hero. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_NEW1_003", self.controller)
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


