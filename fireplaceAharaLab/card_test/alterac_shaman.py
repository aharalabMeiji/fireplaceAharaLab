from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def alterac_shaman():

	#PresetGame(pp_AV_107)##
	#PresetGame(pp_AV_250)##
	#PresetGame(pp_AV_251)##
	#PresetGame(pp_AV_255)##
	#PresetGame(pp_AV_257)##
	#PresetGame(pp_AV_258)##
	#PresetGame(pp_AV_259)##
	#PresetGame(pp_AV_260)##
	#PresetGame(pp_AV_266)##
	#PresetGame(pp_AV_268)##
	#PresetGame(pp_BOM_08_Brukan_003t)##
	#PresetGame(pp_BOM_08_Brukan_007t)##
	#PresetGame(pp_BOM_08_Brukan_008t)##
	#PresetGame(pp_BOM_08_Campfire_004hb)##
	#PresetGame(pp_BOM_08_DrekThar_006hb)##
	#PresetGame(pp_BOM_08_Morloch_002hb)##
	#PresetGame(pp_BOM_08_Tavish_Drekthar_006p)##
	#PresetGame(pp_BOM_09_Brukan_001hp)##
	#PresetGame(pp_BOM_09_Brukan_001p)##
	#PresetGame(pp_BOM_09_Brukan_002hp)##
	#PresetGame(pp_BOM_09_Brukan_002p)##
	#PresetGame(pp_BOM_09_Brukan_003hp)##
	#PresetGame(pp_BOM_09_Brukan_004hp)##
	#PresetGame(pp_BOM_09_Brukan_004p)##
	#PresetGame(pp_BOM_09_Brukan_005hp)##
	#PresetGame(pp_BOM_09_Brukan_005p)##
	#PresetGame(pp_BOM_09_Brukan_006hp)##
	#PresetGame(pp_BOM_09_Brukan_006p)##
	#PresetGame(pp_BOM_09_Brukan_007hp)##
	#PresetGame(pp_BOM_09_Brukan_007p)##
	#PresetGame(pp_BOM_09_Brukan_008hp)##
	#PresetGame(pp_BOM_09_Brukan_008p)##
	#PresetGame(pp_BOM_09_BrukansLesson_003s)##
	#PresetGame(pp_BOM_09_Campfire_002hb)##
	#PresetGame(pp_BOM_09_DrekThar_005t)##
	#PresetGame(pp_BOM_09_KnockOff_007s)##
	#PresetGame(pp_BOM_09_Lokholar_006hb)##
	#PresetGame(pp_BOM_09_Lokholar_006p)##
	#PresetGame(pp_BOM_09_Primalist_005hb)##
	#PresetGame(pp_BOM_09_Thrall_005t)##
	#PresetGame(pp_BOM_10_BellowingRoar_006s)##
	#PresetGame(pp_BOM_10_Memorial_001hb)##
	#PresetGame(pp_BOM_10_Memorial_001p)##
	#PresetGame(pp_ONY_011)##
	#PresetGame(pp_ONY_012)##
	#PresetGame(pp_ONY_013)##
	#PresetGame(pp_TB_01_BOM_Mercs_Brukan_001p)##
	pass


##########AV_107##########

class pp_AV_107(Preset_Play):
	""" Glaciate
	[Discover] an 8-Cost minion. Summon and [Freeze] it. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("AV_107", self.controller)
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


##########AV_250##########

class pp_AV_250(Preset_Play):
	""" Snowball Fight!
	Deal $1 damage to a minion and [Freeze] it. If it survives, repeat this on another minion! """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("AV_250", self.controller)
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


##########AV_251##########

class pp_AV_251(Preset_Play):
	""" Cheaty Snobold
	After an enemy is [Frozen], deal 3 damage to it. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("AV_251", self.controller)
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


##########AV_255##########

class pp_AV_255(Preset_Play):
	""" Snowfall Guardian
	[Battlecry:] [Freeze] all other minions. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("AV_255", self.controller)
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


##########AV_257##########

class pp_AV_257(Preset_Play):
	""" Bearon Gla'shear
	[Battlecry:] For each Frost spell you've cast this game, summon a 3/4 Elemental that [Freezes].@ <i>(@)</i> """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("AV_257", self.controller)
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


##########AV_258##########

class pp_AV_258(Preset_Play):
	""" Bru'kan of the Elements
	[Battlecry:] Call upon the power of two Elements! """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("AV_258", self.controller)
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


##########AV_259##########

class pp_AV_259(Preset_Play):
	""" Frostbite
	Deal $3 damage. [Honorable Kill:] Your opponent's next spell costs (2) more. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("AV_259", self.controller)
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


##########AV_260##########

class pp_AV_260(Preset_Play):
	""" Sleetbreaker
	[Battlecry:] Add a Windchill to your hand. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("AV_260", self.controller)
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


##########AV_266##########

class pp_AV_266(Preset_Play):
	""" Windchill
	[Freeze] a minion. Draw a card. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("AV_266", self.controller)
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


##########AV_268##########

class pp_AV_268(Preset_Play):
	""" Wildpaw Cavern
	At the end of your turn, summon a 3/4 Elemental that [Freezes]. Lasts 3 turns. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("AV_268", self.controller)
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


##########BOM_08_Brukan_003t##########

class pp_BOM_08_Brukan_003t(Preset_Play):
	""" Bru'kan
	[Frenzy]: Deal 2 damage to all enemy minions. [Revive]:_(3) """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_08_Brukan_003t", self.controller)
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


##########BOM_08_Brukan_007t##########

class pp_BOM_08_Brukan_007t(Preset_Play):
	""" Bru'kan on Ice
	Permanently Frozen. Break the ice to set free. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_08_Brukan_007t", self.controller)
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


##########BOM_08_Brukan_008t##########

class pp_BOM_08_Brukan_008t(Preset_Play):
	""" Bru'kan
	[Frenzy]: Deal 2 damage to all enemy minions. [Revive]:_(2) """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_08_Brukan_008t", self.controller)
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


##########BOM_08_Campfire_004hb##########

class pp_BOM_08_Campfire_004hb(Preset_Play):
	""" Campfire
	<i>The mercenaries stare into the fire and wonder if this is the last night some of them will ever see.</i> """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_08_Campfire_004hb", self.controller)
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


##########BOM_08_DrekThar_006hb##########

class pp_BOM_08_DrekThar_006hb(Preset_Play):
	""" Drek'Thar
	<i>The only way to reach Vanndar's fortress is over_Dun_Baldar_Bridge.</i> """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_08_DrekThar_006hb", self.controller)
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


##########BOM_08_Morloch_002hb##########

class pp_BOM_08_Morloch_002hb(Preset_Play):
	""" Morloch
	<i>Tavish suspects this mission from Vanndar is meant to get rid of one problem or_another.</i> """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_08_Morloch_002hb", self.controller)
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


##########BOM_08_Tavish_Drekthar_006p##########

class pp_BOM_08_Tavish_Drekthar_006p(Preset_Play):
	""" Shamanic Trial
	[Hero Power] Summon an Elemental. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_08_Tavish_Drekthar_006p", self.controller)
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


##########BOM_09_Brukan_001hp##########

class pp_BOM_09_Brukan_001hp(Preset_Play):
	""" Bru'kan
	 """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Brukan_001hp", self.controller)
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


##########BOM_09_Brukan_001p##########

class pp_BOM_09_Brukan_001p(Preset_Play):
	""" Totemic Talent
	[Hero Power] Summon a random Totem. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Brukan_001p", self.controller)
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


##########BOM_09_Brukan_002hp##########

class pp_BOM_09_Brukan_002hp(Preset_Play):
	""" Bru'kan
	 """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Brukan_002hp", self.controller)
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


##########BOM_09_Brukan_002p##########

class pp_BOM_09_Brukan_002p(Preset_Play):
	""" Totemic Talent
	[Hero Power] Summon a random Totem. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Brukan_002p", self.controller)
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


##########BOM_09_Brukan_003hp##########

class pp_BOM_09_Brukan_003hp(Preset_Play):
	""" Bru'kan
	 """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Brukan_003hp", self.controller)
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


##########BOM_09_Brukan_004hp##########

class pp_BOM_09_Brukan_004hp(Preset_Play):
	""" Bru'kan
	 """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Brukan_004hp", self.controller)
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


##########BOM_09_Brukan_004p##########

class pp_BOM_09_Brukan_004p(Preset_Play):
	""" Totemic Talent
	[Hero Power] Summon a random Totem. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Brukan_004p", self.controller)
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


##########BOM_09_Brukan_005hp##########

class pp_BOM_09_Brukan_005hp(Preset_Play):
	""" Bru'kan
	 """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Brukan_005hp", self.controller)
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


##########BOM_09_Brukan_005p##########

class pp_BOM_09_Brukan_005p(Preset_Play):
	""" Totemic Talent
	[Hero Power] Summon a random Totem. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Brukan_005p", self.controller)
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


##########BOM_09_Brukan_006hp##########

class pp_BOM_09_Brukan_006hp(Preset_Play):
	""" Bru'kan
	 """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Brukan_006hp", self.controller)
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


##########BOM_09_Brukan_006p##########

class pp_BOM_09_Brukan_006p(Preset_Play):
	""" Totemic Talent
	[Hero Power] Summon a random Totem. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Brukan_006p", self.controller)
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


##########BOM_09_Brukan_007hp##########

class pp_BOM_09_Brukan_007hp(Preset_Play):
	""" Bru'kan
	 """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Brukan_007hp", self.controller)
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


##########BOM_09_Brukan_007p##########

class pp_BOM_09_Brukan_007p(Preset_Play):
	""" Windchill
	[Hero Power] [Freeze] a minion. Draw a card. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Brukan_007p", self.controller)
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


##########BOM_09_Brukan_008hp##########

class pp_BOM_09_Brukan_008hp(Preset_Play):
	""" Bru'kan
	 """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Brukan_008hp", self.controller)
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


##########BOM_09_Brukan_008p##########

class pp_BOM_09_Brukan_008p(Preset_Play):
	""" Windchill
	[Hero Power] [Freeze] a minion. Draw a card. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Brukan_008p", self.controller)
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


##########BOM_09_BrukansLesson_003s##########

class pp_BOM_09_BrukansLesson_003s(Preset_Play):
	""" Bru'kan's Lesson
	Call upon the power of two Elements! """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_BrukansLesson_003s", self.controller)
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


##########BOM_09_Campfire_002hb##########

class pp_BOM_09_Campfire_002hb(Preset_Play):
	""" Campfire
	<i>The campfire burns, granting a brief reprieve from_the_darkness...</i> """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Campfire_002hb", self.controller)
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


##########BOM_09_DrekThar_005t##########

class pp_BOM_09_DrekThar_005t(Preset_Play):
	""" Drek'Thar
	At the start of your turn, summon a basic Totem.  [Deathrattle:] Advance fight. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_DrekThar_005t", self.controller)
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


##########BOM_09_KnockOff_007s##########

class pp_BOM_09_KnockOff_007s(Preset_Play):
	""" Knock Off
	Destroy the enemy minion with the lowest Health. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_KnockOff_007s", self.controller)
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


##########BOM_09_Lokholar_006hb##########

class pp_BOM_09_Lokholar_006hb(Preset_Play):
	""" Lokholar, the Ice Lord
	<i>Lokholar draws power from the mortal conflict in Alterac.</i> """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Lokholar_006hb", self.controller)
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


##########BOM_09_Lokholar_006p##########

class pp_BOM_09_Lokholar_006p(Preset_Play):
	""" Windchill
	[Hero Power] [Freeze] a minion. Draw a card. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Lokholar_006p", self.controller)
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


##########BOM_09_Primalist_005hb##########

class pp_BOM_09_Primalist_005hb(Preset_Play):
	""" The Primalist
	<i>To master the elements, Bru'kan must face the sins of his past.</i> """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Primalist_005hb", self.controller)
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


##########BOM_09_Thrall_005t##########

class pp_BOM_09_Thrall_005t(Preset_Play):
	""" Warchief Thrall
	Your hero is [Immune]. [Deathrattle:] Advance Fight. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Thrall_005t", self.controller)
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


##########BOM_10_BellowingRoar_006s##########

class pp_BOM_10_BellowingRoar_006s(Preset_Play):
	""" Bellowing Roar
	Gain 7 Armor. Fill your board with 2/1 Whelps. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_10_BellowingRoar_006s", self.controller)
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


##########BOM_10_Memorial_001hb##########

class pp_BOM_10_Memorial_001hb(Preset_Play):
	""" Memorial
	<i>Bru'kan and Tamsin are gone. Now the remaining mercenaries must pick up the pieces.</i> """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_10_Memorial_001hb", self.controller)
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


##########BOM_10_Memorial_001p##########

class pp_BOM_10_Memorial_001p(Preset_Play):
	""" Keep the Peace
	[Hero Power] Let no harm come to the mercenaries. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_10_Memorial_001p", self.controller)
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


##########ONY_011##########

class pp_ONY_011(Preset_Play):
	""" Don't Stand in the Fire!
	Deal $10 damage randomly split among all enemy minions. [Overload:] (1) """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("ONY_011", self.controller)
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


##########ONY_012##########

class pp_ONY_012(Preset_Play):
	""" Spirit Mount
	Give a minion +1/+2 and [Spell Damage +1]. When it dies, summon a Spirit Raptor. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("ONY_012", self.controller)
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


##########ONY_013##########

class pp_ONY_013(Preset_Play):
	""" Bracing Cold
	Restore #5 Health to your hero. Reduce the Cost of a random spell in your hand by (2). """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("ONY_013", self.controller)
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


##########TB_01_BOM_Mercs_Brukan_001p##########

class pp_TB_01_BOM_Mercs_Brukan_001p(Preset_Play):
	""" Bru'kan
	[Hero Power] +1 Attack and [Windfury] this turn. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("TB_01_BOM_Mercs_Brukan_001p", self.controller)
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


