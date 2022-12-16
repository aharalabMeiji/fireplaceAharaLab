from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def lich_deathknight():

	#PresetGame(pp_PVPDR_Sai_T3e1)##
	#PresetGame(pp_RLK_012)##
	#PresetGame(pp_RLK_025e)##
	#PresetGame(pp_RLK_025o)##
	#PresetGame(pp_RLK_035)##
	#PresetGame(pp_RLK_051)##
	#PresetGame(pp_RLK_066e)##
	#PresetGame(pp_RLK_085e)##
	#PresetGame(pp_RLK_116)##
	#PresetGame(pp_RLK_120)##
	#PresetGame(pp_RLK_121)##
	#PresetGame(pp_RLK_225)##
	#PresetGame(pp_RLK_506)##
	#PresetGame(pp_RLK_706)##
	#PresetGame(pp_RLK_707e)##
	#PresetGame(pp_RLK_715e)##
	#PresetGame(pp_RLK_741)##
	#PresetGame(pp_RLK_753e)##
	#PresetGame(pp_RLK_958e)##
	#PresetGame(pp_RLK_Prologue_025)##
	#PresetGame(pp_RLK_Prologue_056)##
	#PresetGame(pp_RLK_Prologue_066)##
	#PresetGame(pp_RLK_Prologue_Arthas_002hp)##
	#PresetGame(pp_RLK_Prologue_Arthas_002p)##
	#PresetGame(pp_RLK_Prologue_Arthas_003hp)##
	#PresetGame(pp_RLK_Prologue_Arthas_003p)##
	#PresetGame(pp_RLK_Prologue_Arthas_004hp)##
	#PresetGame(pp_RLK_Prologue_Arthas_004p)##
	#PresetGame(pp_RLK_Prologue_Frostmourne_001)##
	#PresetGame(pp_RLK_Prologue_LichKing_004hp2)##
	#PresetGame(pp_RLK_Prologue_MalGanis_001hb)##
	#PresetGame(pp_RLK_Prologue_MalGanis_001p)##
	#PresetGame(pp_RLK_Prologue_RLK_012)##
	#PresetGame(pp_RLK_Prologue_RLK_025e)##
	#PresetGame(pp_RLK_Prologue_RLK_025o)##
	#PresetGame(pp_RLK_Prologue_RLK_035)##
	#PresetGame(pp_RLK_Prologue_RLK_051)##
	#PresetGame(pp_RLK_Prologue_RLK_120)##
	#PresetGame(pp_RLK_Prologue_RLK_506)##
	#PresetGame(pp_RLK_Prologue_RLK_707e)##
	#PresetGame(pp_RLK_Prologue_RLK_741)##
	#PresetGame(pp_RLK_Prologue_RLK_753e)##
	#PresetGame(pp_RLK_Prologue_TheScourge_003s)##
	#PresetGame(pp_RLK_Shop_DKBlood)##
	#PresetGame(pp_RLK_Shop_DKFrost)##
	#PresetGame(pp_RLK_Shop_DKUnholy)##
	pass


##########PVPDR_Sai_T3e1##########

class pp_PVPDR_Sai_T3e1(Preset_Play):
	""" Icy Remembrance
	{0} """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("PVPDR_Sai_T3e1", self.controller)
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


##########RLK_012##########

class pp_RLK_012(Preset_Play):
	""" Soulbreaker
	After your hero attacks and kills a minion, gain 2 <b>Corpses</b>. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_012", self.controller)
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


##########RLK_025e##########

class pp_RLK_025e(Preset_Play):
	""" Glacial Advance
	The next spell you cast this turn costs (2) less. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_025e", self.controller)
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


##########RLK_025o##########

class pp_RLK_025o(Preset_Play):
	""" Glacial Advance
	The next spell you cast this turn costs (2) less. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_025o", self.controller)
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


##########RLK_035##########

class pp_RLK_035(Preset_Play):
	""" Corpse Explosion
	Detonate a <b>Corpse</b> to deal $1 damage to all minions. If any are still alive, repeat this. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_035", self.controller)
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


##########RLK_051##########

class pp_RLK_051(Preset_Play):
	""" Vampiric Blood
	Give your hero +5 Health. Spend 3 <b>Corpses</b> to gain 5 more and draw a card. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_051", self.controller)
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


##########RLK_066e##########

class pp_RLK_066e(Preset_Play):
	""" Winter's Gift
	Increased Health. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_066e", self.controller)
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


##########RLK_085e##########

class pp_RLK_085e(Preset_Play):
	""" Bonestorm
	+2/+2. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_085e", self.controller)
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


##########RLK_116##########

class pp_RLK_116(Preset_Play):
	""" Necrotic Mortician
	<b>Battlecry:</b> If a friendly Undead died after your last turn, <b>Discover</b> an Unholy Rune card. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_116", self.controller)
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


##########RLK_120##########

class pp_RLK_120(Preset_Play):
	""" Meat Grinder
	<b>Battlecry:</b> Shred a random minion in your deck to gain 3 <b>Corpses.</b> """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_120", self.controller)
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


##########RLK_121##########

class pp_RLK_121(Preset_Play):
	""" Acolyte of Death
	After a friendly Undead dies, draw a card. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_121", self.controller)
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


##########RLK_225##########

class pp_RLK_225(Preset_Play):
	""" Blightfang
	<b>Battlecry:</b> Infect all enemy minions. When they die, you summon a 2/2 Zombie with <b>Taunt</b>. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_225", self.controller)
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


##########RLK_506##########

class pp_RLK_506(Preset_Play):
	""" Boneguard Commander
	<b>Taunt</b> <b>Battlecry:</b> Raise up to 6 <b>Corpses</b> as 1/2 Risen Footmen with <b>Taunt</b>. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_506", self.controller)
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


##########RLK_706##########

class pp_RLK_706(Preset_Play):
	""" Alexandros Mograine
	<b>Battlecry:</b> For the rest of the game, deal 3 damage to your opponent at the end of your turns. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_706", self.controller)
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


##########RLK_707e##########

class pp_RLK_707e(Preset_Play):
	""" Grave Mark
	+1 Attack. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_707e", self.controller)
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


##########RLK_715e##########

class pp_RLK_715e(Preset_Play):
	""" Runeforged
	Costs (1) less. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_715e", self.controller)
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


##########RLK_741##########

class pp_RLK_741(Preset_Play):
	""" Soulstealer
	<b>Battlecry:</b> Destroy all other minions. Gain 1 <b>Corpse</b> for each enemy destroyed. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_741", self.controller)
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


##########RLK_753e##########

class pp_RLK_753e(Preset_Play):
	""" Dug Up
	+1/+2. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_753e", self.controller)
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


##########RLK_958e##########

class pp_RLK_958e(Preset_Play):
	""" Thrown a Bone
	+2 Attack. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_958e", self.controller)
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


##########RLK_Prologue_025##########

class pp_RLK_Prologue_025(Preset_Play):
	""" Frost Strike
	Deal $3 damage to a minion. If that kills it, <b>Discover</b> a Frost Rune card. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_025", self.controller)
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


##########RLK_Prologue_056##########

class pp_RLK_Prologue_056(Preset_Play):
	""" Unholy Frenzy
	Choose an enemy minion. Your minions attack it. Resummon any that die. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_056", self.controller)
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


##########RLK_Prologue_066##########

class pp_RLK_Prologue_066(Preset_Play):
	""" Hematurge
	<b>Battlecry:</b> Spend a <b>Corpse</b> to <b>Discover</b> a Blood Rune card. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_066", self.controller)
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


##########RLK_Prologue_Arthas_002hp##########

class pp_RLK_Prologue_Arthas_002hp(Preset_Play):
	""" Arthas
	 """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_Arthas_002hp", self.controller)
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


##########RLK_Prologue_Arthas_002p##########

class pp_RLK_Prologue_Arthas_002p(Preset_Play):
	""" Ghoul Charge
	<b>Hero Power</b> Summon a 1/1 Ghoul with <b>Charge</b>. It dies at end of turn. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_Arthas_002p", self.controller)
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


##########RLK_Prologue_Arthas_003hp##########

class pp_RLK_Prologue_Arthas_003hp(Preset_Play):
	""" Arthas
	 """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_Arthas_003hp", self.controller)
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


##########RLK_Prologue_Arthas_003p##########

class pp_RLK_Prologue_Arthas_003p(Preset_Play):
	""" Ghoul Charge
	<b>Hero Power</b> Summon a 1/1 Ghoul with <b>Charge</b>. It dies at end of turn. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_Arthas_003p", self.controller)
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


##########RLK_Prologue_Arthas_004hp##########

class pp_RLK_Prologue_Arthas_004hp(Preset_Play):
	""" Arthas
	 """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_Arthas_004hp", self.controller)
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


##########RLK_Prologue_Arthas_004p##########

class pp_RLK_Prologue_Arthas_004p(Preset_Play):
	""" Ghoul Charge
	<b>Hero Power</b> Summon a 1/1 Ghoul with <b>Charge</b>. It dies at end of turn. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_Arthas_004p", self.controller)
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


##########RLK_Prologue_Frostmourne_001##########

class pp_RLK_Prologue_Frostmourne_001(Preset_Play):
	""" Frostmourne
	<b>Deathrattle:</b> Summon every minion killed by this weapon. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_Frostmourne_001", self.controller)
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


##########RLK_Prologue_LichKing_004hp2##########

class pp_RLK_Prologue_LichKing_004hp2(Preset_Play):
	""" The Lich King
	 """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_LichKing_004hp2", self.controller)
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


##########RLK_Prologue_MalGanis_001hb##########

class pp_RLK_Prologue_MalGanis_001hb(Preset_Play):
	""" Mal'Ganis
	 """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_MalGanis_001hb", self.controller)
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


##########RLK_Prologue_MalGanis_001p##########

class pp_RLK_Prologue_MalGanis_001p(Preset_Play):
	""" Ghoul Charge
	<b>Hero Power</b> Summon a 1/1 Ghoul with <b>Charge</b>. It dies at end of turn. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_MalGanis_001p", self.controller)
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


##########RLK_Prologue_RLK_012##########

class pp_RLK_Prologue_RLK_012(Preset_Play):
	""" Soulbreaker
	After your hero attacks and kills a minion, gain 2 <b>Corpses</b>. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_RLK_012", self.controller)
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


##########RLK_Prologue_RLK_025e##########

class pp_RLK_Prologue_RLK_025e(Preset_Play):
	""" Glacial Advance
	The next spell you cast this turn costs (2) less. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_RLK_025e", self.controller)
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


##########RLK_Prologue_RLK_025o##########

class pp_RLK_Prologue_RLK_025o(Preset_Play):
	""" Glacial Advance
	The next spell you cast this turn costs (2) less. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_RLK_025o", self.controller)
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


##########RLK_Prologue_RLK_035##########

class pp_RLK_Prologue_RLK_035(Preset_Play):
	""" Corpse Explosion
	Detonate a <b>Corpse</b> to deal $1 damage to all minions. If any are still alive, repeat this. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_RLK_035", self.controller)
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


##########RLK_Prologue_RLK_051##########

class pp_RLK_Prologue_RLK_051(Preset_Play):
	""" Vampiric Blood
	Give your hero +5 Health. Spend 3 <b>Corpses</b> to gain 5 more and draw a card. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_RLK_051", self.controller)
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


##########RLK_Prologue_RLK_120##########

class pp_RLK_Prologue_RLK_120(Preset_Play):
	""" Meat Grinder
	<b>Battlecry:</b> Shred a random minion in your deck to gain 3 <b>Corpses.</b> """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_RLK_120", self.controller)
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


##########RLK_Prologue_RLK_506##########

class pp_RLK_Prologue_RLK_506(Preset_Play):
	""" Boneguard Commander
	<b>Taunt</b> <b>Battlecry:</b> Raise up to 6 <b>Corpses</b> as 1/2 Risen Footmen with <b>Taunt</b>. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_RLK_506", self.controller)
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


##########RLK_Prologue_RLK_707e##########

class pp_RLK_Prologue_RLK_707e(Preset_Play):
	""" Grave Mark
	+1 Attack. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_RLK_707e", self.controller)
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


##########RLK_Prologue_RLK_741##########

class pp_RLK_Prologue_RLK_741(Preset_Play):
	""" Soulstealer
	<b>Battlecry:</b> Destroy all other minions. Gain 1 <b>Corpse</b> for each enemy destroyed. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_RLK_741", self.controller)
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


##########RLK_Prologue_RLK_753e##########

class pp_RLK_Prologue_RLK_753e(Preset_Play):
	""" Dug Up
	+1/+2. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_RLK_753e", self.controller)
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


##########RLK_Prologue_TheScourge_003s##########

class pp_RLK_Prologue_TheScourge_003s(Preset_Play):
	""" The Scourge
	Fill your board with random Undead. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_TheScourge_003s", self.controller)
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


##########RLK_Shop_DKBlood##########

class pp_RLK_Shop_DKBlood(Preset_Play):
	""" Blood Deck Art
	 """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Shop_DKBlood", self.controller)
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


##########RLK_Shop_DKFrost##########

class pp_RLK_Shop_DKFrost(Preset_Play):
	""" Frost Deck Art
	 """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Shop_DKFrost", self.controller)
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


##########RLK_Shop_DKUnholy##########

class pp_RLK_Shop_DKUnholy(Preset_Play):
	""" Unholy Deck Art
	 """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Shop_DKUnholy", self.controller)
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


