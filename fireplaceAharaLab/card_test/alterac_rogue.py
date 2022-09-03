from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def alterac_rogue():

	#PresetGame(pp_AV_201)##
	#PresetGame(pp_AV_203)##
	#PresetGame(pp_AV_298)##
	#PresetGame(pp_AV_400)##
	#PresetGame(pp_AV_402)##
	#PresetGame(pp_AV_403)##
	#PresetGame(pp_AV_405)##
	#PresetGame(pp_AV_601)##
	#PresetGame(pp_AV_710)##
	#PresetGame(pp_AV_711)##
	#PresetGame(pp_BOM_08_Scabbs_002t)##
	#PresetGame(pp_BOM_08_Scabbs_003t)##
	#PresetGame(pp_BOM_08_Scabbs_005t)##
	#PresetGame(pp_BOM_08_Scabbs_008t)##
	#PresetGame(pp_BOM_09_Scabbs_008t)##
	#PresetGame(pp_BOM_09_Snivvle_004hb)##
	#PresetGame(pp_BOM_09_Togwaggle_004t)##
	#PresetGame(pp_BOM_10_Scabbs_001t)##
	#PresetGame(pp_BOM_10_Valeera_003t)##
	#PresetGame(pp_ONY_030)##
	#PresetGame(pp_ONY_031)##
	#PresetGame(pp_ONY_032)##
	#PresetGame(pp_TB_01_BOM_Mercs_Scabbs_001p)##
	pass


##########AV_201##########

class pp_AV_201(Preset_Play):
	""" Coldtooth Yeti
	[Combo:] Gain +3 Attack. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("AV_201", self.controller)
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


##########AV_203##########

class pp_AV_203(Preset_Play):
	""" Shadowcrafter Scabbs
	[Battlecry:] Return all minions to their owner's  hands. Summon two 4/2 Shadows with [Stealth]. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("AV_203", self.controller)
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


##########AV_298##########

class pp_AV_298(Preset_Play):
	""" Wildpaw Gnoll
	[Rush] Costs (1) less for each card you've added to your hand _from another class. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("AV_298", self.controller)
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


##########AV_400##########

class pp_AV_400(Preset_Play):
	""" Snowfall Graveyard
	Your [Deathrattles] trigger twice. Lasts 3 turns. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("AV_400", self.controller)
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


##########AV_402##########

class pp_AV_402(Preset_Play):
	""" The Lobotomizer
	[Honorable Kill:] Get a copy of the top card of your opponent's deck. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("AV_402", self.controller)
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


##########AV_403##########

class pp_AV_403(Preset_Play):
	""" Cera'thine Fleetrunner
	[Battlecry:] Replace your minions in hand and deck  with ones from other classes. They cost (2) less. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("AV_403", self.controller)
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


##########AV_405##########

class pp_AV_405(Preset_Play):
	""" Contraband Stash
	Replay 5 cards from other classes you've played this game. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("AV_405", self.controller)
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


##########AV_601##########

class pp_AV_601(Preset_Play):
	""" Forsaken Lieutenant
	[[Stealth].] After you play a [Deathrattle] minion, become a 2/2 copy of it with [Rush]. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("AV_601", self.controller)
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


##########AV_710##########

class pp_AV_710(Preset_Play):
	""" Reconnaissance
	[Discover] a [Deathrattle] minion from another class. It costs (2) less. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("AV_710", self.controller)
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


##########AV_711##########

class pp_AV_711(Preset_Play):
	""" Double Agent
	[Battlecry:] If you're holding a card from another class, _summon a copy of this. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("AV_711", self.controller)
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


##########BOM_08_Scabbs_002t##########

class pp_BOM_08_Scabbs_002t(Preset_Play):
	""" Scabbs
	[Honorable Kill]: Draw a card. [Revive]: (3) """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_08_Scabbs_002t", self.controller)
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


##########BOM_08_Scabbs_003t##########

class pp_BOM_08_Scabbs_003t(Preset_Play):
	""" Scabbs
	[Honorable Kill]: Draw a card. [Revive]: (3) """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_08_Scabbs_003t", self.controller)
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


##########BOM_08_Scabbs_005t##########

class pp_BOM_08_Scabbs_005t(Preset_Play):
	""" Scabbs
	[Honorable Kill]: Draw a card. [Revive]: (3) """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_08_Scabbs_005t", self.controller)
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


##########BOM_08_Scabbs_008t##########

class pp_BOM_08_Scabbs_008t(Preset_Play):
	""" Scabbs
	[Honorable Kill]: Draw a card. [Revive]: (2) """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_08_Scabbs_008t", self.controller)
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


##########BOM_09_Scabbs_008t##########

class pp_BOM_09_Scabbs_008t(Preset_Play):
	""" Scabbs
	[Honorable Kill]: Draw a card. [Revive]: (3) """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Scabbs_008t", self.controller)
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


##########BOM_09_Snivvle_004hb##########

class pp_BOM_09_Snivvle_004hb(Preset_Play):
	""" Taskmaster Snivvle
	<i>They say whoever wears the lantern crown is the kobold king.</i> """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Snivvle_004hb", self.controller)
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


##########BOM_09_Togwaggle_004t##########

class pp_BOM_09_Togwaggle_004t(Preset_Play):
	""" Miner Togwaggle
	[Revive:] (2) """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_09_Togwaggle_004t", self.controller)
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


##########BOM_10_Scabbs_001t##########

class pp_BOM_10_Scabbs_001t(Preset_Play):
	""" Scabbs, Top Agent
	[Honorable Kill:] Draw a card. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_10_Scabbs_001t", self.controller)
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


##########BOM_10_Valeera_003t##########

class pp_BOM_10_Valeera_003t(Preset_Play):
	""" Valeera Sanguinar
	Whenever this is attacked, throw a Fan of Knives. [Deathrattle:] Advance fight. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("BOM_10_Valeera_003t", self.controller)
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


##########ONY_030##########

class pp_ONY_030(Preset_Play):
	""" SI:7 Smuggler
	[Battlecry:] Summon a random @-Cost minion. <i>(Upgraded for each other SI:7 card you _have played this game.)</i> """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("ONY_030", self.controller)
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


##########ONY_031##########

class pp_ONY_031(Preset_Play):
	""" Smokescreen
	Draw 5 cards. Trigger any [Deathrattles] drawn. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("ONY_031", self.controller)
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


##########ONY_032##########

class pp_ONY_032(Preset_Play):
	""" Tooth of Nefarian
	Deal $3 damage. [Honorable Kill:] [Discover] a spell from another class. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("ONY_032", self.controller)
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


##########TB_01_BOM_Mercs_Scabbs_001p##########

class pp_TB_01_BOM_Mercs_Scabbs_001p(Preset_Play):
	""" Scabbs
	[Hero Power] Give a minion [Poisonous]. [Combo]: Also give it [Stealth] for 1 turn. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("TB_01_BOM_Mercs_Scabbs_001p", self.controller)
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


