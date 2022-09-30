from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def rev_shaman():

	#PresetGame(pp_MAW_003)##
	#PresetGame(pp_MAW_005)##
	#PresetGame(pp_MAW_030)##
	#PresetGame(pp_REV_517)##
	#PresetGame(pp_REV_788)##
	#PresetGame(pp_REV_798)##
	#PresetGame(pp_REV_838)##
	#PresetGame(pp_REV_917)##
	#PresetGame(pp_REV_920)##
	#PresetGame(pp_REV_921)##
	#PresetGame(pp_REV_923)##
	#PresetGame(pp_REV_924)##
	#PresetGame(pp_REV_925)##
	#PresetGame(pp_REV_935)##
	#PresetGame(pp_REV_936)##
	#PresetGame(pp_REV_942e2)##
	pass


##########MAW_003##########

class pp_MAW_003(Preset_Play):
	""" Totemic Evidence
	Choose a basic Totem and summon it. <b>Infuse (@ Totems):</b> Summon all 4 instead. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_003", self.controller)
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


##########MAW_005##########

class pp_MAW_005(Preset_Play):
	""" Framester
	<b>Battlecry:</b> Shuffle 3 'Framed' cards into the opponent's deck. When drawn, they <b>Overload</b> for (2). """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_005", self.controller)
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


##########MAW_030##########

class pp_MAW_030(Preset_Play):
	""" Torghast Custodian
	<b>Battlecry:</b> For each enemy minion, randomly gain <b>Rush</b>, <b>Divine Shield</b>, or <b>Windfury</b>. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_030", self.controller)
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


##########REV_517##########

class pp_REV_517(Preset_Play):
	""" Criminal Lineup
	Choose a friendly minion. Summon 3 copies of it. <b>Overload:</b> (2) """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_517", self.controller)
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


##########REV_788##########

class pp_REV_788(Preset_Play):
	""" Baroness Vashj
	{0} {1} {2} {3} """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_788", self.controller)
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


##########REV_798##########

class pp_REV_798(Preset_Play):
	""" Muck Pools
	{0} {1} """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_798", self.controller)
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


##########REV_838##########

class pp_REV_838(Preset_Play):
	""" Gigantotem
	Costs (1) less for each Totem you've summoned this game. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_838", self.controller)
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


##########REV_917##########

class pp_REV_917(Preset_Play):
	""" Carving Chisel
	After your hero attacks, summon a random basic Totem. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_917", self.controller)
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


##########REV_920##########

class pp_REV_920(Preset_Play):
	""" Convincing Disguise
	Transform a friendly minion into one that costs (2) more. <b>Infuse (@):</b> Transform all friendly minions instead. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_920", self.controller)
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


##########REV_921##########

class pp_REV_921(Preset_Play):
	""" The Stonewright
	<b>Battlecry:</b> For the rest of the game, your Totems have +2 Attack. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_921", self.controller)
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


##########REV_923##########

class pp_REV_923(Preset_Play):
	""" Muck Pools
	Transform a friendly minion into one that costs (1) more. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_923", self.controller)
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


##########REV_924##########

class pp_REV_924(Preset_Play):
	""" Primordial Wave
	Transform enemy minions  into ones that cost (1) less  and friendly minions into  ones that cost (1) more. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_924", self.controller)
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


##########REV_925##########

class pp_REV_925(Preset_Play):
	""" Baroness Vashj
	If this would transform into a minion, summon that minion instead. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_925", self.controller)
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


##########REV_935##########

class pp_REV_935(Preset_Play):
	""" Party Favor Totem
	At the end of your turn,  summon a random basic  Totem. <b>Infuse (@):</b>  Summon two instead. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_935", self.controller)
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


##########REV_936##########

class pp_REV_936(Preset_Play):
	""" Crud Caretaker
	<b>Battlecry</b>: Summon a 3/5 Elemental with <b>Taunt</b>. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_936", self.controller)
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


##########REV_942e2##########

class pp_REV_942e2(Preset_Play):
	""" Relics of Old
	Your next spell this turn casts twice. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_942e2", self.controller)
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


