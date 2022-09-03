from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def alterac_priest():

	#PresetGame(pp_AV_207)##
	#PresetGame(pp_AV_315)##
	#PresetGame(pp_AV_324)##
	#PresetGame(pp_AV_325)##
	#PresetGame(pp_AV_326)##
	#PresetGame(pp_AV_328)##
	#PresetGame(pp_AV_329)##
	#PresetGame(pp_AV_330)##
	#PresetGame(pp_AV_331)##
	#PresetGame(pp_AV_664)##
	#PresetGame(pp_BOM_08_Kazakus_007hb)##
	#PresetGame(pp_BOM_08_Kazakusan_007hb2)##
	#PresetGame(pp_BOM_08_Xyrella_002t)##
	#PresetGame(pp_BOM_08_Xyrella_003t)##
	#PresetGame(pp_BOM_08_Xyrella_008t)##
	#PresetGame(pp_BOM_09_Xyrella_008t)##
	#PresetGame(pp_BOM_10_DarkNaaru_008hb)##
	#PresetGame(pp_BOM_10_DarkNaaru_008p)##
	#PresetGame(pp_BOM_10_LightNaaru_008hb2)##
	#PresetGame(pp_BOM_10_ShardOfTheNaaru_008s)##
	#PresetGame(pp_BOM_10_Xyrella_004t)##
	#PresetGame(pp_ONY_017)##
	#PresetGame(pp_ONY_026)##
	#PresetGame(pp_ONY_028)##
	#PresetGame(pp_TB_01_BOM_Mercs_Xyrella_001p)##
	pass


##########AV_207##########

class pp_AV_207(Preset_Play):
	""" Xyrella, the Devout
	[Battlecry:] Trigger the [Deathrattle] of every friendly minion that died this game. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("AV_207", self.controller)
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


##########AV_315##########

class pp_AV_315(Preset_Play):
	""" Deliverance
	Deal $3 damage to a minion. [Honorable Kill:] Summon a new 3/3 copy of it. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("AV_315", self.controller)
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


##########AV_324##########

class pp_AV_324(Preset_Play):
	""" Shadow Word: Devour
	Choose a minion. It steals 1 Health from _ALL other minions. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("AV_324", self.controller)
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


##########AV_325##########

class pp_AV_325(Preset_Play):
	""" Undying Disciple
	[Taunt] [Deathrattle:] Deal damage equal to this minion's Attack to all enemy minions. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("AV_325", self.controller)
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


##########AV_326##########

class pp_AV_326(Preset_Play):
	""" Luminous Geode
	After a friendly minion is healed, give it +2 Attack. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("AV_326", self.controller)
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


##########AV_328##########

class pp_AV_328(Preset_Play):
	""" Spirit Guide
	[Taunt] [Deathrattle:] Draw a Holy spell and a Shadow spell. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("AV_328", self.controller)
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


##########AV_329##########

class pp_AV_329(Preset_Play):
	""" Bless
	Give a minion +2 Health, then set its Attack to be equal to its Health. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("AV_329", self.controller)
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


##########AV_330##########

class pp_AV_330(Preset_Play):
	""" Gift of the Naaru
	Restore #3 Health to all characters. If any are still damaged, draw a card. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("AV_330", self.controller)
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


##########AV_331##########

class pp_AV_331(Preset_Play):
	""" Najak Hexxen
	[Battlecry:] Take control of an enemy minion. [Deathrattle:] Give the minion back. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("AV_331", self.controller)
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


##########AV_664##########

class pp_AV_664(Preset_Play):
	""" Stormpike Aid Station
	At the end of your turn, give your minions +2 Health. Lasts 3 turns. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("AV_664", self.controller)
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


##########BOM_08_Kazakus_007hb##########

class pp_BOM_08_Kazakus_007hb(Preset_Play):
	""" Kazakus
	<i>Kazakus has encased Guff's companions in ice. Tavish must set them free.</i> """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_08_Kazakus_007hb", self.controller)
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


##########BOM_08_Kazakusan_007hb2##########

class pp_BOM_08_Kazakusan_007hb2(Preset_Play):
	""" Kazakusan
	<i>Dragons often wear disguises to meddle in the_affairs_of_mortals.</i> """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_08_Kazakusan_007hb2", self.controller)
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


##########BOM_08_Xyrella_002t##########

class pp_BOM_08_Xyrella_002t(Preset_Play):
	""" Xyrella
	[Honorable Kill]: Restore your minions to full Health. [Revive]:_(3) """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_08_Xyrella_002t", self.controller)
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


##########BOM_08_Xyrella_003t##########

class pp_BOM_08_Xyrella_003t(Preset_Play):
	""" Xyrella
	[Honorable Kill]: Restore your minions to full Health. [Revive]:_(3) """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_08_Xyrella_003t", self.controller)
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


##########BOM_08_Xyrella_008t##########

class pp_BOM_08_Xyrella_008t(Preset_Play):
	""" Xyrella
	[Honorable Kill]: Restore your minions to full Health. [Revive]:_(2) """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_08_Xyrella_008t", self.controller)
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


##########BOM_09_Xyrella_008t##########

class pp_BOM_09_Xyrella_008t(Preset_Play):
	""" Xyrella
	[Honorable Kill]: Restore your minions to full Health. [Revive]:_(2) """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Xyrella_008t", self.controller)
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


##########BOM_10_DarkNaaru_008hb##########

class pp_BOM_10_DarkNaaru_008hb(Preset_Play):
	""" Mi'da, Pure Void
	<i>On the Exodar, Dawngrasp and Xyrella reassemble the naaru. Now they must restore it to the Light.</i> """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_10_DarkNaaru_008hb", self.controller)
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


##########BOM_10_DarkNaaru_008p##########

class pp_BOM_10_DarkNaaru_008p(Preset_Play):
	""" Void Nightmare
	[Hero Power] Summon a Nightmare from the past. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_10_DarkNaaru_008p", self.controller)
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


##########BOM_10_LightNaaru_008hb2##########

class pp_BOM_10_LightNaaru_008hb2(Preset_Play):
	""" Mi'da, Pure Light
	 """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_10_LightNaaru_008hb2", self.controller)
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


##########BOM_10_ShardOfTheNaaru_008s##########

class pp_BOM_10_ShardOfTheNaaru_008s(Preset_Play):
	""" Shard of the Naaru
	[Tradeable] [Silence] all enemy minions. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_10_ShardOfTheNaaru_008s", self.controller)
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


##########BOM_10_Xyrella_004t##########

class pp_BOM_10_Xyrella_004t(Preset_Play):
	""" Xyrella, Hopeful Mother
	[Lifesteal] """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_10_Xyrella_004t", self.controller)
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


##########ONY_017##########

class pp_ONY_017(Preset_Play):
	""" Horn of Wrathion
	Draw a minion. If it's a Dragon, summon two 2/1 Whelps with [Rush]. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("ONY_017", self.controller)
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


##########ONY_026##########

class pp_ONY_026(Preset_Play):
	""" Lightmaw Netherdrake
	[Battlecry:] If you're holding a Holy and a Shadow spell, deal 3 damage to all other minions. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("ONY_026", self.controller)
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


##########ONY_028##########

class pp_ONY_028(Preset_Play):
	""" Mi'da, Pure Light
	[Divine Shield], [Lifesteal] [Deathrattle:] Shuffle a Fragment into your deck that resummons Mi'da when drawn. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("ONY_028", self.controller)
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


##########TB_01_BOM_Mercs_Xyrella_001p##########

class pp_TB_01_BOM_Mercs_Xyrella_001p(Preset_Play):
	""" Xyrella
	[Hero Power] Restore 3 Health to a character. If it's still damaged, draw a card. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("TB_01_BOM_Mercs_Xyrella_001p", self.controller)
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


