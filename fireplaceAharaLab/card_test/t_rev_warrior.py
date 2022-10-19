from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def rev_warrior():

	#PresetGame(pp_MAW_027)##
	#PresetGame(pp_MAW_028)##
	#PresetGame(pp_MAW_029)##
	#PresetGame(pp_REV_006)## ### OK ###
	#PresetGame(pp_REV_316)##
	#PresetGame(pp_REV_332)##
	#PresetGame(pp_REV_334)##
	#PresetGame(pp_REV_337)##
	#PresetGame(pp_REV_783)##
	#PresetGame(pp_REV_793)##
	#PresetGame(pp_REV_930)##
	#PresetGame(pp_REV_931)##
	#PresetGame(pp_REV_933)##
	#PresetGame(pp_REV_934)##
	#PresetGame(pp_REV_990)##
	pass


##########MAW_027##########

class pp_MAW_027(Preset_Play):
	""" Call to the Stand
	Your opponent summons a random minion from their hand. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_027", self.controller)
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


##########MAW_028##########

class pp_MAW_028(Preset_Play):
	""" Mawsworn Bailiff
	<b><b>Taunt</b>.</b> <b>Battlecry:</b> If you have 4 or more Armor, gain +4/+4. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_028", self.controller)
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


##########MAW_029##########

class pp_MAW_029(Preset_Play):
	""" Weapons Expert
	<b>Battlecry:</b> If you have a weapon equipped, give it +1/+1. Otherwise, draw a weapon. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_029", self.controller)
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


##########REV_006##########

class pp_REV_006(Preset_Play):
	""" Suspicious Pirate
	<b>Battlecry:</b> <b>Discover</b> a weapon. If your opponent guesses your choice, they get a copy. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("REV_006", self.controller)
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
		self.change_turn()
		### opp
		self.choose_action()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.opponent.hand:
			self.print_stats("opponent.hand", card)
	pass


##########REV_316##########

class pp_REV_316(Preset_Play):
	""" Remornia, Living Blade
	<b>Rush</b> After this attacks, equip it. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("REV_316", self.controller)
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


##########REV_332##########

class pp_REV_332(Preset_Play):
	""" Anima Extractor
	Whenever a friendly minion takes damage, give a random minion in your hand +1/+1. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("REV_332", self.controller)
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


##########REV_334##########

class pp_REV_334(Preset_Play):
	""" Burden of Pride
	Summon three 1/3 Jailers with <b>Taunt</b>. If you have 20 or less Health, give them +1/+1. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("REV_334", self.controller)
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


##########REV_337##########

class pp_REV_337(Preset_Play):
	""" Riot!
	Your minions can't be  reduced below 1 Health  this turn. They each attack  a random enemy minion. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("REV_337", self.controller)
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


##########REV_783##########

class pp_REV_783(Preset_Play):
	""" Decimator Olgra
	{0} {1} {2} {3} """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("REV_783", self.controller)
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


##########REV_793##########

class pp_REV_793(Preset_Play):
	""" Sanguine Depths
	{0} {1} """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("REV_793", self.controller)
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


##########REV_930##########

class pp_REV_930(Preset_Play):
	""" Crazed Wretch
	Has +2 Attack and <b>Charge</b> while damaged. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("REV_930", self.controller)
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


##########REV_931##########

class pp_REV_931(Preset_Play):
	""" Conqueror's Banner
	Reveal a card from each player's deck, three times. Draw any of yours that cost more. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("REV_931", self.controller)
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


##########REV_933##########

class pp_REV_933(Preset_Play):
	""" Imbued Axe
	After your hero attacks, give your damaged minions +1/+2. <b>Infuse (@):</b> +2/+2 instead. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("REV_933", self.controller)
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


##########REV_934##########

class pp_REV_934(Preset_Play):
	""" Decimator Olgra
	<b>Battlecry:</b> Gain +1/+1 for each damaged minion, _then attack all enemies. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("REV_934", self.controller)
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


##########REV_990##########

class pp_REV_990(Preset_Play):
	""" Sanguine Depths
	Deal 1 damage to a  minion and give it  +2 Attack. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("REV_990", self.controller)
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


