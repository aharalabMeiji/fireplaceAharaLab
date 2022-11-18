from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def rev_paladin():

	#PresetGame(pp_MAW_015)##
	#PresetGame(pp_MAW_016)##
	#PresetGame(pp_MAW_017)##
	#PresetGame(pp_REV_784)##
	#PresetGame(pp_REV_794)##
	#PresetGame(pp_REV_842)##
	#PresetGame(pp_REV_947)##
	#PresetGame(pp_REV_948)## OK
	#PresetGame(pp_REV_950)##
	#PresetGame(pp_REV_951)##
	#PresetGame(pp_REV_952)##
	#PresetGame(pp_REV_955)##
	#PresetGame(pp_REV_958)##
	#PresetGame(pp_REV_961)##
	#PresetGame(pp_REV_983)##
	pass


##########MAW_015##########

class pp_MAW_015(Preset_Play):
	""" Jury Duty
	Summon two Silver Hand Recruits. Give your Silver Hand Recruits +1/+1. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_015", self.controller)
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


##########MAW_016##########

class pp_MAW_016(Preset_Play):
	""" Order in the Court
	Reorder your deck from highest Cost to lowest Cost. Draw a card. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_016", self.controller)
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


##########MAW_017##########

class pp_MAW_017(Preset_Play):
	""" Class Action Lawyer
	<b>Battlecry:</b> If your deck has no Neutral cards, set _a minion's stats to 1/1. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_017", self.controller)
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


##########REV_784##########

class pp_REV_784(Preset_Play):
	""" Stewart the Steward
	{0} {1} {2} {3} """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_784", self.controller)
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


##########REV_794##########

class pp_REV_794(Preset_Play):
	""" Great Hall
	{0} {1} """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_794", self.controller)
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


##########REV_842##########

class pp_REV_842(Preset_Play):
	""" Promotion
	Give a Silver Hand Recruit +3/+3 and <b>Taunt</b>. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_842", self.controller)
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


##########REV_947##########

class pp_REV_947(Preset_Play):
	""" Muckborn Servant
	<b>Taunt</b> <b>Battlecry:</b> <b>Discover</b> a Paladin card. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_947", self.controller)
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


##########REV_948##########

class pp_REV_948(Preset_Play):
	""" Service Bell
	<b>Discover</b> a Class card from your deck and draw all copies of it. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_948", self.controller)
		#self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		#self.con4=self.con4[0][0]
		#self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		#self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.choose_action()
		#self.change_turn()
		### opp
		#self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
		rpint("See if the chosen card was moved to controller's hand.")
	pass


##########REV_950##########

class pp_REV_950(Preset_Play):
	""" Divine Toll
	Shoot 5 rays at random minions. They give friendly minions +2/+2, and deal $2 damage to enemy minions. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_950", self.controller)
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


##########REV_951##########

class pp_REV_951(Preset_Play):
	""" The Countess
	<b>Battlecry:</b> If your deck  has no Neutral cards, add  3 <b>Legendary </b>Invitations  to your hand. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_951", self.controller)
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


##########REV_952##########

class pp_REV_952(Preset_Play):
	""" Sinful Sous Chef
	<b>Deathrattle:</b> Add 2 Silver Hand Recruits to your hand. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_952", self.controller)
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


##########REV_955##########

class pp_REV_955(Preset_Play):
	""" Stewart the Steward
	<b>Deathrattle:</b> Give the next Silver Hand Recruit you summon +3/+3 and this <b>Deathrattle</b>. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_955", self.controller)
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


##########REV_958##########

class pp_REV_958(Preset_Play):
	""" Buffet Biggun
	<b>Battlecry:</b> Summon two Silver  Hand Recruits. <b>Infuse (@):</b>  Give them +2 Attack  and <b>Divine Shield</b>. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_958", self.controller)
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


##########REV_961##########

class pp_REV_961(Preset_Play):
	""" Elitist Snob
	<b>Battlecry:</b> For each Paladin card in your hand, randomly  gain <b>Divine Shield</b>, <b>Lifesteal</b>,  <b>Rush</b>, or <b>Taunt</b>. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_961", self.controller)
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


##########REV_983##########

class pp_REV_983(Preset_Play):
	""" Great Hall
	Set a minion's Attack and Health to 3. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("REV_983", self.controller)
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


