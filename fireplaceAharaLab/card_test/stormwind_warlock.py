from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity

def stormwind_warlock():

	#PresetGame(pp_BOM_05_BigMindDemon_06t)##
	#PresetGame(pp_BOM_05_GatheredShadows_005e)##
	#PresetGame(pp_BOM_05_GatheredShadows_007e)##
	#PresetGame(pp_BOM_05_LittleMindDemon_06t)##
	#PresetGame(pp_BOM_05_MemoryBurn_08s)##
	#PresetGame(pp_BOM_05_Tamsin_001hp)##
	#PresetGame(pp_BOM_05_Tamsin_001p)##
	#PresetGame(pp_BOM_05_Tamsin_002hp)##
	#PresetGame(pp_BOM_05_Tamsin_002p)##
	#PresetGame(pp_BOM_05_Tamsin_003hp)##
	#PresetGame(pp_BOM_05_Tamsin_003p)##
	#PresetGame(pp_BOM_05_Tamsin_004hp)##
	#PresetGame(pp_BOM_05_Tamsin_004p)##
	#PresetGame(pp_BOM_05_Tamsin_005hp)##
	#PresetGame(pp_BOM_05_Tamsin_005p)##
	#PresetGame(pp_BOM_05_Tamsin_006hp)##
	#PresetGame(pp_BOM_05_Tamsin_006p)##
	#PresetGame(pp_BOM_05_Tamsin_007hp)##
	#PresetGame(pp_BOM_05_Tamsin_007p)##
	#PresetGame(pp_BOM_05_Tamsin_008hp)##
	#PresetGame(pp_BOM_06_Anetheron_005hb)##
	#PresetGame(pp_BOM_06_Anetheron_005p)##
	#PresetGame(pp_BOM_06_Anetheron_006hb)##
	#PresetGame(pp_BOM_06_Anetheron_006p)##
	#PresetGame(pp_BOM_06_CarrionSwarm_005s)##
	#PresetGame(pp_BOM_06_LeftHand_005t)##
	#PresetGame(pp_BOM_06_LeftHandWithKurtrus_005)##
	#PresetGame(pp_BOM_06_RightHand_005t)##
	#PresetGame(pp_BOM_06_Sleep_005s)##
	#PresetGame(pp_BOM_06_SummonInfernal_005s)##
	#PresetGame(pp_BOM_06_Tamsin_008hb)##
	#PresetGame(pp_BOM_06_Tamsin_008p)##
	#PresetGame(pp_BOM_06_ToweringInfernal_005s)##
	#PresetGame(pp_BOM_06_Xurgon_004hb)##
	#PresetGame(pp_BOM_06_Xurgon_004p)##
	#PresetGame(pp_DED_503)##
	#PresetGame(pp_DED_504)##
	#PresetGame(pp_DED_505)##
	#PresetGame(pp_Story_10_Magtheridon_005hb)##
	#PresetGame(pp_SW_003)##
	#PresetGame(pp_SW_084)##
	#PresetGame(pp_SW_085)##
	#PresetGame(pp_SW_086)##
	#PresetGame(pp_SW_087)##
	#PresetGame(pp_SW_088)##
	#PresetGame(pp_SW_089)##
	#PresetGame(pp_SW_090)##
	#PresetGame(pp_SW_091)##
	#PresetGame(pp_SW_092)##


##########BOM_05_BigMindDemon_06t##########

class pp_BOM_05_BigMindDemon_06t(Preset_Play):
	""" Big Mind Demon
	After this attacks, destroy the top 2 cards of your opponent's deck. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_BigMindDemon_06t", self.controller)
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


##########BOM_05_GatheredShadows_005e##########

class pp_BOM_05_GatheredShadows_005e(Preset_Play):
	""" Gathered Shadows
	Costs (1). """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_GatheredShadows_005e", self.controller)
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


##########BOM_05_GatheredShadows_007e##########

class pp_BOM_05_GatheredShadows_007e(Preset_Play):
	""" Gathered Shadows
	Costs (0). """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_GatheredShadows_007e", self.controller)
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


##########BOM_05_LittleMindDemon_06t##########

class pp_BOM_05_LittleMindDemon_06t(Preset_Play):
	""" Little Mind Demon
	After this attacks, destroy the top card of your opponent's deck. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_LittleMindDemon_06t", self.controller)
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


##########BOM_05_MemoryBurn_08s##########

class pp_BOM_05_MemoryBurn_08s(Preset_Play):
	""" Memory Burn
	Deal $3 damage to a minion. Destroy thetop 3 cards of your opponent's deck. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_MemoryBurn_08s", self.controller)
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


##########BOM_05_Tamsin_001hp##########

class pp_BOM_05_Tamsin_001hp(Preset_Play):
	""" Tamsin
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_Tamsin_001hp", self.controller)
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


##########BOM_05_Tamsin_001p##########

class pp_BOM_05_Tamsin_001p(Preset_Play):
	""" Swarm of Imps
	[Hero Power]Summon a 3/2 Imp Familiar. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_Tamsin_001p", self.controller)
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


##########BOM_05_Tamsin_002hp##########

class pp_BOM_05_Tamsin_002hp(Preset_Play):
	""" Tamsin
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_Tamsin_002hp", self.controller)
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


##########BOM_05_Tamsin_002p##########

class pp_BOM_05_Tamsin_002p(Preset_Play):
	""" Swarm of Imps
	[Hero Power]Summon two 3/2 Imp Familiars. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_Tamsin_002p", self.controller)
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


##########BOM_05_Tamsin_003hp##########

class pp_BOM_05_Tamsin_003hp(Preset_Play):
	""" Tamsin
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_Tamsin_003hp", self.controller)
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


##########BOM_05_Tamsin_003p##########

class pp_BOM_05_Tamsin_003p(Preset_Play):
	""" Yo Ho!
	[Hero Power]Add a random Pirateto_your_hand. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_Tamsin_003p", self.controller)
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


##########BOM_05_Tamsin_004hp##########

class pp_BOM_05_Tamsin_004hp(Preset_Play):
	""" Tamsin
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_Tamsin_004hp", self.controller)
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


##########BOM_05_Tamsin_004p##########

class pp_BOM_05_Tamsin_004p(Preset_Play):
	""" Swarm of Imps
	[Hero Power]Summon two 3/2 Imp Familiars. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_Tamsin_004p", self.controller)
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


##########BOM_05_Tamsin_005hp##########

class pp_BOM_05_Tamsin_005hp(Preset_Play):
	""" Tamsin
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_Tamsin_005hp", self.controller)
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


##########BOM_05_Tamsin_005p##########

class pp_BOM_05_Tamsin_005p(Preset_Play):
	""" Forsaken Fury
	[Passive Hero Power]Whenever you cast a Shadowspell that costs (2) or more,add a copy to your handthat costs (1). """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_Tamsin_005p", self.controller)
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


##########BOM_05_Tamsin_006hp##########

class pp_BOM_05_Tamsin_006hp(Preset_Play):
	""" Tamsin
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_Tamsin_006hp", self.controller)
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


##########BOM_05_Tamsin_006p##########

class pp_BOM_05_Tamsin_006p(Preset_Play):
	""" Forsaken Fury
	[Passive Hero Power]Whenever you cast a Shadowspell that costs (2) or more,add a copy to your handthat costs (1). """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_Tamsin_006p", self.controller)
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


##########BOM_05_Tamsin_007hp##########

class pp_BOM_05_Tamsin_007hp(Preset_Play):
	""" Tamsin
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_Tamsin_007hp", self.controller)
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


##########BOM_05_Tamsin_007p##########

class pp_BOM_05_Tamsin_007p(Preset_Play):
	""" Forsaken Fury
	[Passive Hero Power]Whenever you cast a Shadowspell that costs (1) or more,add a copy to your handthat costs (0). """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_Tamsin_007p", self.controller)
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


##########BOM_05_Tamsin_008hp##########

class pp_BOM_05_Tamsin_008hp(Preset_Play):
	""" Tamsin
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_Tamsin_008hp", self.controller)
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


##########BOM_06_Anetheron_005hb##########

class pp_BOM_06_Anetheron_005hb(Preset_Play):
	""" Anetheron
	Cariel finds Kurtrus inthe dreadlord's grip.She must free Kurtrus! """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_06_Anetheron_005hb", self.controller)
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


##########BOM_06_Anetheron_005p##########

class pp_BOM_06_Anetheron_005p(Preset_Play):
	""" Dreadlord's Slash
	[Hero Power]Deal 2 damage to the left-most enemy minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_06_Anetheron_005p", self.controller)
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


##########BOM_06_Anetheron_006hb##########

class pp_BOM_06_Anetheron_006hb(Preset_Play):
	""" Anetheron
	The dreadlord towers over the city. He must be stopped! """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_06_Anetheron_006hb", self.controller)
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


##########BOM_06_Anetheron_006p##########

class pp_BOM_06_Anetheron_006p(Preset_Play):
	""" Legion's Might
	[Hero Power]Add one of your Signature Spells to your hand. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_06_Anetheron_006p", self.controller)
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


##########BOM_06_CarrionSwarm_005s##########

class pp_BOM_06_CarrionSwarm_005s(Preset_Play):
	""" Carrion Swarm
	Infect all enemy minions. They take 1 damage at the start of each turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_06_CarrionSwarm_005s", self.controller)
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


##########BOM_06_LeftHand_005t##########

class pp_BOM_06_LeftHand_005t(Preset_Play):
	""" Left Hand
	[Taunt] """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_06_LeftHand_005t", self.controller)
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


##########BOM_06_LeftHandWithKurtrus_005##########

class pp_BOM_06_LeftHandWithKurtrus_005(Preset_Play):
	""" Left Hand With Kurtrus
	[Taunt][Deathrattle:] Free_Kurtrus and advance fight. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_06_LeftHandWithKurtrus_005", self.controller)
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


##########BOM_06_RightHand_005t##########

class pp_BOM_06_RightHand_005t(Preset_Play):
	""" Right Hand
	[Taunt] """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_06_RightHand_005t", self.controller)
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


##########BOM_06_Sleep_005s##########

class pp_BOM_06_Sleep_005s(Preset_Play):
	""" Sleep
	Target minion can't attack until the start of your next turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_06_Sleep_005s", self.controller)
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


##########BOM_06_SummonInfernal_005s##########

class pp_BOM_06_SummonInfernal_005s(Preset_Play):
	""" Summon Towering Infernal
	Summon a 6/6 Infernal. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_06_SummonInfernal_005s", self.controller)
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


##########BOM_06_Tamsin_008hb##########

class pp_BOM_06_Tamsin_008hb(Preset_Play):
	""" Tamsin
	Clinging to her memoriesof times long past,Cariel steps through the graveyard_to_face_her_sister. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_06_Tamsin_008hb", self.controller)
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


##########BOM_06_Tamsin_008p##########

class pp_BOM_06_Tamsin_008p(Preset_Play):
	""" Swarm of Imps
	[Hero Power]Summon two 3/2 Imp Familiars. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_06_Tamsin_008p", self.controller)
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


##########BOM_06_ToweringInfernal_005s##########

class pp_BOM_06_ToweringInfernal_005s(Preset_Play):
	""" Towering Infernal
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_06_ToweringInfernal_005s", self.controller)
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


##########BOM_06_Xurgon_004hb##########

class pp_BOM_06_Xurgon_004hb(Preset_Play):
	""" Xur'gon
	Demons are everywhere,and Cariel fights to securethe Dwarven District whereTavish is pinned down. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_06_Xurgon_004hb", self.controller)
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


##########BOM_06_Xurgon_004p##########

class pp_BOM_06_Xurgon_004p(Preset_Play):
	""" Demon Little Dream
	[Passive Hero Power]Xur'gon is flying.Only Tavish can reach her. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_06_Xurgon_004p", self.controller)
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


##########DED_503##########

class pp_DED_503(Preset_Play):
	""" Shadowblade Slinger
	[Battlecry:] If you've takendamage this turn, deal that_much to an enemy minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_503", self.controller)
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


##########DED_504##########

class pp_DED_504(Preset_Play):
	""" Wicked Shipment
	[Tradeable]Summon @ 1/1 |4(Imp, Imps).<i>(Upgrades by 2when [Traded]!)</i> """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_504", self.controller)
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


##########DED_505##########

class pp_DED_505(Preset_Play):
	""" Hullbreaker
	[Battlecry and Deathrattle:]Draw a spell. Your hero takesdamage equal to its Cost. """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_505", self.controller)
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


##########Story_10_Magtheridon_005hb##########

class pp_Story_10_Magtheridon_005hb(Preset_Play):
	""" Magtheridon
	<i>This pit lord has conquered the shattered world of Outland, or so he thinksÅc</i> """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_10_Magtheridon_005hb", self.controller)
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


##########SW_003##########

class pp_SW_003(Preset_Play):
	""" Runed Mithril Rod
	After you draw 4 cards,reduce the Cost of cardsin your hand by (1).Lose 1 Durability. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_003", self.controller)
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


##########SW_084##########

class pp_SW_084(Preset_Play):
	""" Bloodbound Imp
	Whenever this attacks, deal 2 damage to your_hero. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_084", self.controller)
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


##########SW_085##########

class pp_SW_085(Preset_Play):
	""" Dark Alley Pact
	Summon a Fiendwith stats equal toyour hand size. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_085", self.controller)
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


##########SW_086##########

class pp_SW_086(Preset_Play):
	""" Shady Bartender
	[Tradeable][Battlecry:] Give your Demons +2/+2. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_086", self.controller)
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


##########SW_087##########

class pp_SW_087(Preset_Play):
	""" Dreaded Mount
	Give a minion +1/+1.When it dies, summonan endless Dreadsteed. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_087", self.controller)
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


##########SW_088##########

class pp_SW_088(Preset_Play):
	""" Demonic Assault
	Deal $3 damage.Summon two 1/3Voidwalkers with [Taunt]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_088", self.controller)
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


##########SW_089##########

class pp_SW_089(Preset_Play):
	""" Entitled Customer
	[Battlecry:] Deal damage equal to your hand size to all other minions. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_089", self.controller)
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


##########SW_090##########

class pp_SW_090(Preset_Play):
	""" Touch of the Nathrezim
	Deal $2 damage to aminion. If it dies, restore3 Health to your hero. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_090", self.controller)
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


##########SW_091##########

class pp_SW_091(Preset_Play):
	""" The Demon Seed
	[Questline:] Take 8damage on your turns.[Reward:] [Lifesteal]. Deal $3damage to the enemy hero. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_091", self.controller)
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


##########SW_092##########

class pp_SW_092(Preset_Play):
	""" Anetheron
	Costs (1) if your hand is full. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_092", self.controller)
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


