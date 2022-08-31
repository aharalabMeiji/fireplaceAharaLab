from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def sunken_priest():

	#PresetGame(pp_AIBot_PriestTrainee_006_hb)##
	#PresetGame(pp_Story_11_BehemothsLure)##
	#PresetGame(pp_Story_11_Bubblebote)##
	#PresetGame(pp_Story_11_BubbleUp)##
	#PresetGame(pp_Story_11_Caye_012hp)##
	#PresetGame(pp_Story_11_Caye_012p)##
	#PresetGame(pp_Story_11_Caye_013hp)##
	#PresetGame(pp_Story_11_Caye_013p)##
	#PresetGame(pp_Story_11_Caye_1)##
	#PresetGame(pp_Story_11_Caye_2)##
	#PresetGame(pp_Story_11_Caye_3)##
	#PresetGame(pp_Story_11_DreamTeam)##
	#PresetGame(pp_Story_11_ExceptionalAide)##
	#PresetGame(pp_Story_11_FreezingPotione)##
	#PresetGame(pp_Story_11_Handmaiden_015hb)##
	#PresetGame(pp_Story_11_HighSeasRevengee)##
	#PresetGame(pp_Story_11_InisToolkite)##
	#PresetGame(pp_Story_11_Motivate3)##
	#PresetGame(pp_Story_11_SerpentWig)##
	#PresetGame(pp_Story_11_ShipShape)##
	#PresetGame(pp_Story_11_Statue_010p)##
	#PresetGame(pp_Story_11_SuperiorEfficiency)##
	#PresetGame(pp_Story_11_TrashedDreamse)##
	#PresetGame(pp_Story_11_TrueHeroism2e)##
	#PresetGame(pp_Story_11_TrueHeroisme)##
	#PresetGame(pp_Story_11_UpliftingPresence)##
	#PresetGame(pp_TID_085)##
	#PresetGame(pp_TID_700)##
	#PresetGame(pp_TID_920)##
	#PresetGame(pp_TSC_209)##
	#PresetGame(pp_TSC_210)##
	#PresetGame(pp_TSC_211)##
	#PresetGame(pp_TSC_212)##
	#PresetGame(pp_TSC_213)##
	#PresetGame(pp_TSC_215)##
	#PresetGame(pp_TSC_216)##
	#PresetGame(pp_TSC_702)##
	#PresetGame(pp_TSC_775)##
	#PresetGame(pp_TSC_828)##
	pass


##########AIBot_PriestTrainee_006_hb##########

class pp_AIBot_PriestTrainee_006_hb(Preset_Play):
	""" Priest Trainee
	 """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("AIBot_PriestTrainee_006_hb", self.controller)
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


##########Story_11_BehemothsLure##########

class pp_Story_11_BehemothsLure(Preset_Play):
	""" Behemoth's Lure
	Gives Bioluminescence when attacked. At the end of your turn, force a random enemy minion to attack the Blackwater Behemoth. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_BehemothsLure", self.controller)
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


##########Story_11_Bubblebote##########

class pp_Story_11_Bubblebote(Preset_Play):
	""" Spit It Out
	[Deathrattle:] Summon the minion it last attacked. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_Bubblebote", self.controller)
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


##########Story_11_BubbleUp##########

class pp_Story_11_BubbleUp(Preset_Play):
	""" Bubble Up
	Give Caye [Deathrattle:] Give [Divine Shield] to a random friendly minion. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_BubbleUp", self.controller)
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


##########Story_11_Caye_012hp##########

class pp_Story_11_Caye_012hp(Preset_Play):
	""" Caye Stardusk
	 """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_Caye_012hp", self.controller)
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


##########Story_11_Caye_012p##########

class pp_Story_11_Caye_012p(Preset_Play):
	""" Motivate
	[Hero Power] Give a random minion in your hand +1/+1 and draw a card. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_Caye_012p", self.controller)
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


##########Story_11_Caye_013hp##########

class pp_Story_11_Caye_013hp(Preset_Play):
	""" Caye Stardusk
	 """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_Caye_013hp", self.controller)
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


##########Story_11_Caye_013p##########

class pp_Story_11_Caye_013p(Preset_Play):
	""" Motivate Rank 2
	[Hero Power] Give a random minion in your hand +2/+2 and draw a card. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_Caye_013p", self.controller)
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


##########Story_11_Caye_1##########

class pp_Story_11_Caye_1(Preset_Play):
	""" Caye Stardusk
	[Battlecry:] [Discover] an ability. [Deathrattle:] Go  [Dormant] for 2 turns. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_Caye_1", self.controller)
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


##########Story_11_Caye_2##########

class pp_Story_11_Caye_2(Preset_Play):
	""" Caye Stardusk
	[Battlecry:] [Discover] an ability. [Deathrattle:] Go  [Dormant] for 2 turns. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_Caye_2", self.controller)
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


##########Story_11_Caye_3##########

class pp_Story_11_Caye_3(Preset_Play):
	""" Caye Stardusk
	[Battlecry:] [Discover] an ability. [Deathrattle:] Go  [Dormant] for 2 turns. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_Caye_3", self.controller)
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


##########Story_11_DreamTeam##########

class pp_Story_11_DreamTeam(Preset_Play):
	""" Dream Team
	Caye gives your [Legendary] minions +1/+2. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_DreamTeam", self.controller)
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


##########Story_11_ExceptionalAide##########

class pp_Story_11_ExceptionalAide(Preset_Play):
	""" Exceptional Aide
	Give Caye's attacks the ability to restore 2 Health to your hero. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_ExceptionalAide", self.controller)
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


##########Story_11_FreezingPotione##########

class pp_Story_11_FreezingPotione(Preset_Play):
	""" Spit It Out
	[Deathrattle:] Summon the minion it last attacked. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_FreezingPotione", self.controller)
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


##########Story_11_Handmaiden_015hb##########

class pp_Story_11_Handmaiden_015hb(Preset_Play):
	""" Handmaiden Zainra
	<i>Dedicated to the court at an early age, Zainra never approved of your friendship with Dathril.</i> """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_Handmaiden_015hb", self.controller)
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


##########Story_11_HighSeasRevengee##########

class pp_Story_11_HighSeasRevengee(Preset_Play):
	""" High Seas Revenge
	[Deathrattle:] Draw a card for each enemy minion on the board. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_HighSeasRevengee", self.controller)
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


##########Story_11_InisToolkite##########

class pp_Story_11_InisToolkite(Preset_Play):
	""" Spit It Out
	[Deathrattle:] Summon the minion it last attacked. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_InisToolkite", self.controller)
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


##########Story_11_Motivate3##########

class pp_Story_11_Motivate3(Preset_Play):
	""" Motivate Rank 3
	Give Caye [Deathrattle:] Give a random minion in your hand +3/+3 and draw a card. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_Motivate3", self.controller)
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


##########Story_11_SerpentWig##########

class pp_Story_11_SerpentWig(Preset_Play):
	""" Serpent Wig
	Give a minion +1/+2. If you played a Naga while holding this, add a Serpent Wig to your hand. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_SerpentWig", self.controller)
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


##########Story_11_ShipShape##########

class pp_Story_11_ShipShape(Preset_Play):
	""" Ship Shape
	Give Caye the ability to grant adjacent minions +1/+1. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_ShipShape", self.controller)
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


##########Story_11_Statue_010p##########

class pp_Story_11_Statue_010p(Preset_Play):
	""" Zin-Azshari Crystal
	[Passive Hero Power] Friendly minion attacks restore Health to random friendly characters. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_Statue_010p", self.controller)
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


##########Story_11_SuperiorEfficiency##########

class pp_Story_11_SuperiorEfficiency(Preset_Play):
	""" Superior Efficiency
	Caye reduces the cost of your Hero Power by (1). """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_SuperiorEfficiency", self.controller)
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


##########Story_11_TrashedDreamse##########

class pp_Story_11_TrashedDreamse(Preset_Play):
	""" Trashed Dreams
	[Deathrattle:] Summon a 0/10 Rubbish Pile. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_TrashedDreamse", self.controller)
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


##########Story_11_TrueHeroism2e##########

class pp_Story_11_TrueHeroism2e(Preset_Play):
	""" Uplifted Heroism
	[Deathrattle:] Restore 18 Health to random friendly characters. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_TrueHeroism2e", self.controller)
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


##########Story_11_TrueHeroisme##########

class pp_Story_11_TrueHeroisme(Preset_Play):
	""" True Heroism
	[Deathrattle:] Restore 15 Health to random friendly characters. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_TrueHeroisme", self.controller)
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


##########Story_11_UpliftingPresence##########

class pp_Story_11_UpliftingPresence(Preset_Play):
	""" Uplifting Presence
	Caye improves your chosen crewmember's ability. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_UpliftingPresence", self.controller)
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


##########TID_085##########

class pp_TID_085(Preset_Play):
	""" Herald of Light
	[Battlecry:] If you've cast a Holy spell while holding this, restore #6 Health to all friendly characters. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("TID_085", self.controller)
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


##########TID_700##########

class pp_TID_700(Preset_Play):
	""" Disarming Elemental
	[Battlecry:] [Dredge] for your opponent. Set its Cost to (6). """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("TID_700", self.controller)
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


##########TID_920##########

class pp_TID_920(Preset_Play):
	""" Drown
	Put an enemy minion on the bottom of your deck. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("TID_920", self.controller)
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


##########TSC_209##########

class pp_TSC_209(Preset_Play):
	""" Whirlpool
	Destroy all minions and all copies of them <i>(wherever they are)</i>. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_209", self.controller)
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


##########TSC_210##########

class pp_TSC_210(Preset_Play):
	""" Illuminate
	[Dredge]. If it's a spell, reduce its Cost by (3). """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_210", self.controller)
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


##########TSC_211##########

class pp_TSC_211(Preset_Play):
	""" Whispers of the Deep
	[Silence] a friendly minion, then deal damage equal to its Attack randomly split among all enemy minions. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_211", self.controller)
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


##########TSC_212##########

class pp_TSC_212(Preset_Play):
	""" Handmaiden
	[Battlecry:] If you've cast three spells while holding this, draw 3 cards.@ <i>({0} left!)</i>@ <i>(Ready!)</i> """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_212", self.controller)
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


##########TSC_213##########

class pp_TSC_213(Preset_Play):
	""" Queensguard
	[Battlecry:] Gain +1/+1 for each spell you've cast this turn. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_213", self.controller)
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


##########TSC_215##########

class pp_TSC_215(Preset_Play):
	""" Serpent Wig
	Give a minion +1/+2. If you played a Naga while holding this, add a Serpent Wig to your hand. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_215", self.controller)
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


##########TSC_216##########

class pp_TSC_216(Preset_Play):
	""" Blackwater Behemoth
	[Colossal +1] [Lifesteal] """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_216", self.controller)
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


##########TSC_702##########

class pp_TSC_702(Preset_Play):
	""" Switcheroo
	Draw 2 minions. Swap their Health. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_702", self.controller)
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


##########TSC_775##########

class pp_TSC_775(Preset_Play):
	""" Azsharan Ritual
	[Silence] a minion and summon a copy of it. Put a 'Sunken Ritual' on the bottom of your deck. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_775", self.controller)
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


##########TSC_828##########

class pp_TSC_828(Preset_Play):
	""" Priestess Valishj
	[Battlecry:] Refresh an empty Mana Crystal for each spell ___you've cast this turn.@ <i>(@)</i> """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_828", self.controller)
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


