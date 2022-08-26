from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity

def stormwind_rogue():

	#PresetGame(pp_BOM_05_EllingTrias_005hb)##
	#PresetGame(pp_BOM_05_Hooktusk_002hb)##
	#PresetGame(pp_BOM_06_Cariel_001p)##
	#PresetGame(pp_BOM_07_PickTheLock_004s)##
	#PresetGame(pp_BOM_07_Scabbs_Bob_001hb)##
	#PresetGame(pp_BOM_07_Scabbs_Cookie_007p)##
	#PresetGame(pp_BOM_07_Scabbs_EdwinVanCleef_008hb)##
	#PresetGame(pp_BOM_07_Scabbs_EdwinVanCleef_e)##
	#PresetGame(pp_BOM_07_Scabbs_Scabbs_001hp)##
	#PresetGame(pp_BOM_07_Scabbs_Scabbs_001p)##
	#PresetGame(pp_BOM_07_Scabbs_Scabbs_002hp)##
	#PresetGame(pp_BOM_07_Scabbs_Scabbs_002p)##
	#PresetGame(pp_BOM_07_Scabbs_Scabbs_003hp)##
	#PresetGame(pp_BOM_07_Scabbs_Scabbs_003p)##
	#PresetGame(pp_BOM_07_Scabbs_Scabbs_004hp)##
	#PresetGame(pp_BOM_07_Scabbs_Scabbs_004p)##
	#PresetGame(pp_BOM_07_Scabbs_Scabbs_005hp)##
	#PresetGame(pp_BOM_07_Scabbs_Scabbs_006hp)##
	#PresetGame(pp_BOM_07_Scabbs_Scabbs_007hp)##
	#PresetGame(pp_BOM_07_Scabbs_Scabbs_008hp)##
	#PresetGame(pp_BOM_07_Scabbs_Scabbs_008p)##
	#PresetGame(pp_BOM_07_Scabbs_Sneed_005hb)##
	#PresetGame(pp_BOM_07_SubtleButter_005s)##
	#PresetGame(pp_DED_004)##
	#PresetGame(pp_DED_005)##
	#PresetGame(pp_DED_510)##
	#PresetGame(pp_Story_10_WardensDetermination)##
	#PresetGame(pp_Story_10_WardensGlaive)##
	#PresetGame(pp_Story_11_ParrrleyPuzzle)##
	#PresetGame(pp_SW_050)##
	#PresetGame(pp_SW_052)##
	#PresetGame(pp_SW_310)##
	#PresetGame(pp_SW_311)##
	#PresetGame(pp_SW_405)##
	#PresetGame(pp_SW_411)##
	#PresetGame(pp_SW_412)##
	#PresetGame(pp_SW_413)##
	#PresetGame(pp_SW_417)##
	#PresetGame(pp_SW_434)##


##########BOM_05_EllingTrias_005hb##########

class pp_BOM_05_EllingTrias_005hb(Preset_Play):
	""" A Cheesemonger
	Undercover SI:7 agents areall over Stormwind, in placesyou would never suspect. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_EllingTrias_005hb", self.controller)
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


##########BOM_05_Hooktusk_002hb##########

class pp_BOM_05_Hooktusk_002hb(Preset_Play):
	""" Hooktusk
	Booty Bay is quite close to Gurubashi Arena, don't you know. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_Hooktusk_002hb", self.controller)
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


##########BOM_06_Cariel_001p##########

class pp_BOM_06_Cariel_001p(Preset_Play):
	""" Dagger Mastery
	[Hero Power]Equip a 1/2 Dagger. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_06_Cariel_001p", self.controller)
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


##########BOM_07_PickTheLock_004s##########

class pp_BOM_07_PickTheLock_004s(Preset_Play):
	""" Pick the Lock
	Pick a lock to helpyou escape. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_07_PickTheLock_004s", self.controller)
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


##########BOM_07_Scabbs_Bob_001hb##########

class pp_BOM_07_Scabbs_Bob_001hb(Preset_Play):
	""" Bob the Bartender
	<i>An open-eared publican is the ideal informant, and Scabbs's former_mentoris_the_best.</i> """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_07_Scabbs_Bob_001hb", self.controller)
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


##########BOM_07_Scabbs_Cookie_007p##########

class pp_BOM_07_Scabbs_Cookie_007p(Preset_Play):
	""" What's Cooking?
	[Passive Hero Power]Every three turns,Cookie ducks inside his cauldron for a turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_07_Scabbs_Cookie_007p", self.controller)
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


##########BOM_07_Scabbs_EdwinVanCleef_008hb##########

class pp_BOM_07_Scabbs_EdwinVanCleef_008hb(Preset_Play):
	""" Edwin VanCleef
	<i>Callous bosses radicalized the Defias laborers.Now all will know their fury and pain.</i> """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_07_Scabbs_EdwinVanCleef_008hb", self.controller)
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


##########BOM_07_Scabbs_EdwinVanCleef_e##########

class pp_BOM_07_Scabbs_EdwinVanCleef_e(Preset_Play):
	""" Dangerous Defiant
	Increased stats. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_07_Scabbs_EdwinVanCleef_e", self.controller)
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


##########BOM_07_Scabbs_Scabbs_001hp##########

class pp_BOM_07_Scabbs_Scabbs_001hp(Preset_Play):
	""" Scabbs Cutterbutter
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_07_Scabbs_Scabbs_001hp", self.controller)
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


##########BOM_07_Scabbs_Scabbs_001p##########

class pp_BOM_07_Scabbs_Scabbs_001p(Preset_Play):
	""" Dagger Mastery
	[Hero Power]Equip a 1/2 Dagger. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_07_Scabbs_Scabbs_001p", self.controller)
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


##########BOM_07_Scabbs_Scabbs_002hp##########

class pp_BOM_07_Scabbs_Scabbs_002hp(Preset_Play):
	""" Scabbs Cutterbutter
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_07_Scabbs_Scabbs_002hp", self.controller)
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


##########BOM_07_Scabbs_Scabbs_002p##########

class pp_BOM_07_Scabbs_Scabbs_002p(Preset_Play):
	""" Dagger Mastery
	[Hero Power]Equip a 1/2 Dagger. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_07_Scabbs_Scabbs_002p", self.controller)
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


##########BOM_07_Scabbs_Scabbs_003hp##########

class pp_BOM_07_Scabbs_Scabbs_003hp(Preset_Play):
	""" Scabbs Cutterbutter
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_07_Scabbs_Scabbs_003hp", self.controller)
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


##########BOM_07_Scabbs_Scabbs_003p##########

class pp_BOM_07_Scabbs_Scabbs_003p(Preset_Play):
	""" Poisoned Daggers
	[Hero Power]Equip a 2/2 Dagger. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_07_Scabbs_Scabbs_003p", self.controller)
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


##########BOM_07_Scabbs_Scabbs_004hp##########

class pp_BOM_07_Scabbs_Scabbs_004hp(Preset_Play):
	""" Scabbs Cutterbutter
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_07_Scabbs_Scabbs_004hp", self.controller)
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


##########BOM_07_Scabbs_Scabbs_004p##########

class pp_BOM_07_Scabbs_Scabbs_004p(Preset_Play):
	""" Poisoned Daggers
	[Hero Power]Equip a 2/2 Dagger. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_07_Scabbs_Scabbs_004p", self.controller)
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


##########BOM_07_Scabbs_Scabbs_005hp##########

class pp_BOM_07_Scabbs_Scabbs_005hp(Preset_Play):
	""" Scabbs Cutterbutter
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_07_Scabbs_Scabbs_005hp", self.controller)
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


##########BOM_07_Scabbs_Scabbs_006hp##########

class pp_BOM_07_Scabbs_Scabbs_006hp(Preset_Play):
	""" Scabbs Cutterbutter
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_07_Scabbs_Scabbs_006hp", self.controller)
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


##########BOM_07_Scabbs_Scabbs_007hp##########

class pp_BOM_07_Scabbs_Scabbs_007hp(Preset_Play):
	""" Scabbs Cutterbutter
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_07_Scabbs_Scabbs_007hp", self.controller)
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


##########BOM_07_Scabbs_Scabbs_008hp##########

class pp_BOM_07_Scabbs_Scabbs_008hp(Preset_Play):
	""" Scabbs Cutterbutter
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_07_Scabbs_Scabbs_008hp", self.controller)
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


##########BOM_07_Scabbs_Scabbs_008p##########

class pp_BOM_07_Scabbs_Scabbs_008p(Preset_Play):
	""" Poisoned Daggers
	[Hero Power]Equip a 2/2 Dagger. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_07_Scabbs_Scabbs_008p", self.controller)
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


##########BOM_07_Scabbs_Sneed_005hb##########

class pp_BOM_07_Scabbs_Sneed_005hb(Preset_Play):
	""" Sneed
	<i>The Defias Brotherhood has_filled_its_hideout_with traps_and_armed_guards.</i> """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_07_Scabbs_Sneed_005hb", self.controller)
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


##########BOM_07_SubtleButter_005s##########

class pp_BOM_07_SubtleButter_005s(Preset_Play):
	""" Subtle Butter
	Add four Spy Gizmosto your hand. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_07_SubtleButter_005s", self.controller)
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


##########DED_004##########

class pp_DED_004(Preset_Play):
	""" Blackwater Cutlass
	[Tradeable]After you [Trade] this,reduce the cost of a spellin your hand by (1). """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_004", self.controller)
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


##########DED_005##########

class pp_DED_005(Preset_Play):
	""" Parrrley
	Swap this for a card in your opponent's deck. """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_005", self.controller)
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


##########DED_510##########

class pp_DED_510(Preset_Play):
	""" Edwin, Defias Kingpin
	[Battlecry:] Draw a card. If youplay it this turn, gain +2/+2and repeat this effect. """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_510", self.controller)
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


##########Story_10_WardensDetermination##########

class pp_Story_10_WardensDetermination(Preset_Play):
	""" Warden's Determination
	Give +2/+2 to all minions in your hand, deck, and battlefield. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_10_WardensDetermination", self.controller)
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


##########Story_10_WardensGlaive##########

class pp_Story_10_WardensGlaive(Preset_Play):
	""" Warden's Glaive
	If this kills an enemy minion, adjacent minions go [Dormant] for 2 turns. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_10_WardensGlaive", self.controller)
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


##########Story_11_ParrrleyPuzzle##########

class pp_Story_11_ParrrleyPuzzle(Preset_Play):
	""" Parrrley
	Swap this for a card in your opponent's deck. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_ParrrleyPuzzle", self.controller)
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


##########SW_050##########

class pp_SW_050(Preset_Play):
	""" Maestra of the Masquerade
	You start the game as a different class until you play a Rogue card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_050", self.controller)
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


##########SW_052##########

class pp_SW_052(Preset_Play):
	""" Find the Imposter
	[Questline:] Play 2SI:7 cards.[Reward:] Add a Spy Gizmo to your hand. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_052", self.controller)
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


##########SW_310##########

class pp_SW_310(Preset_Play):
	""" Counterfeit Blade
	[Battlecry:] Gain a randomfriendly [Deathrattle] that_triggered this game. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_310", self.controller)
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


##########SW_311##########

class pp_SW_311(Preset_Play):
	""" Garrote
	Deal $2 damage to theenemy hero. Shuffle 2Bleeds into your deck thatdeal $2 more when drawn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_311", self.controller)
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


##########SW_405##########

class pp_SW_405(Preset_Play):
	""" Sketchy Information
	Draw a [Deathrattle] cardthat costs (4) or less.Trigger its [Deathrattle.] """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_405", self.controller)
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


##########SW_411##########

class pp_SW_411(Preset_Play):
	""" SI:7 Informant
	[Battlecry:] Gain +1/+1 for each other SI:7 card you've played this game. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_411", self.controller)
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


##########SW_412##########

class pp_SW_412(Preset_Play):
	""" SI:7 Extortion
	[Tradeable]Deal $3 damage to an undamaged character. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_412", self.controller)
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


##########SW_413##########

class pp_SW_413(Preset_Play):
	""" SI:7 Operative
	[Rush]After this attacks a minion, gain [Stealth]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_413", self.controller)
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


##########SW_417##########

class pp_SW_417(Preset_Play):
	""" SI:7 Assassin
	Costs (1) less for each SI:7card you've played this game.[Combo:] Destroy anenemy minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_417", self.controller)
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


##########SW_434##########

class pp_SW_434(Preset_Play):
	""" Loan Shark
	[Battlecry:] Give youropponent a Coin.__[Deathrattle:] You get two. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_434", self.controller)
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


