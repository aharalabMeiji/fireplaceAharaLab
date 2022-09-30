from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def rev_hunter():

	#PresetGame(pp_MAW_009)##
	#PresetGame(pp_MAW_010)##
	#PresetGame(pp_MAW_011)##
	#PresetGame(pp_REV_350)##
	#PresetGame(pp_REV_352)##
	#PresetGame(pp_REV_353)##
	#PresetGame(pp_REV_356)##
	#PresetGame(pp_REV_360)##
	#PresetGame(pp_REV_361)##
	#PresetGame(pp_REV_362)##
	#PresetGame(pp_REV_363)##
	#PresetGame(pp_REV_364)##
	#PresetGame(pp_REV_369)##
	#PresetGame(pp_REV_780)##
	#PresetGame(pp_REV_790)##
	pass


##########MAW_009##########

class pp_MAW_009(Preset_Play):
	""" Shadehound
	Whenever this attacks, give your other Beasts +2/+2. <b>Infuse (@ Beasts):</b> Gain <b>Rush</b>. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_009", self.controller)
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


##########MAW_010##########

class pp_MAW_010(Preset_Play):
	""" Motion Denied
	<b>Secret:</b> After your opponent plays three cards in a turn, deal $6 damage to the enemy hero. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_010", self.controller)
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


##########MAW_011##########

class pp_MAW_011(Preset_Play):
	""" Defense Attorney Nathanos
	<b>Battlecry:</b> <b>Discover</b> a friendly <b>Deathrattle</b> minion that died this game. Trigger and gain its <b>Deathrattle</b>. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_011", self.controller)
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


##########REV_350##########

class pp_REV_350(Preset_Play):
	""" Frenzied Fangs
	Summon two 2/1 Bats. <b>Infuse (@):</b> Give them +1/+2. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_350", self.controller)
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


##########REV_352##########

class pp_REV_352(Preset_Play):
	""" Stonebound Gargon
	<b>Rush</b> <b>Infuse (@):</b> Also damages the minions next to __whomever this attacks. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_352", self.controller)
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


##########REV_353##########

class pp_REV_353(Preset_Play):
	""" Huntsman Altimor
	<b>Battlecry:</b> Summon a Gargon Companion. <b>Infuse ({0}):</b> Summon another. _<b>Infuse ({1}):</b> And another! """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_353", self.controller)
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


##########REV_356##########

class pp_REV_356(Preset_Play):
	""" Batty Guest
	<b>Deathrattle:</b> Summon a 2/1 Bat. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_356", self.controller)
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


##########REV_360##########

class pp_REV_360(Preset_Play):
	""" Spirit Poacher
	<b>Battlecry:</b> Summon a random <b>Dormant</b> Wildseed. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_360", self.controller)
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


##########REV_361##########

class pp_REV_361(Preset_Play):
	""" Wild Spirits
	Summon two different  <b>Dormant</b> Wildseeds.  Make your Wildseeds  awaken 1 turn sooner. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_361", self.controller)
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


##########REV_362##########

class pp_REV_362(Preset_Play):
	""" Castle Kennels
	Give a friendly minion  +2 Attack. If it's a  Beast, give it <b>Rush</b>. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_362", self.controller)
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


##########REV_363##########

class pp_REV_363(Preset_Play):
	""" Ara'lon
	<b>Battlecry:</b> Summon one of each <b>Dormant</b> Wildseed. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_363", self.controller)
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


##########REV_364##########

class pp_REV_364(Preset_Play):
	""" Stag Charge
	Deal $3 damage. Summon a random <b>Dormant</b> Wildseed. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_364", self.controller)
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


##########REV_369##########

class pp_REV_369(Preset_Play):
	""" Collateral Damage
	Deal $6 damage to three  random enemy minions.  Excess damage hits  the enemy hero. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_369", self.controller)
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


##########REV_780##########

class pp_REV_780(Preset_Play):
	""" Ara'lon
	{0} {1} {2} {3} """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_780", self.controller)
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


##########REV_790##########

class pp_REV_790(Preset_Play):
	""" Castle Kennels
	{0} {1} """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("REV_790", self.controller)
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


