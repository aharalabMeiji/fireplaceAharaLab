from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def rev_neutral():

	#PresetGame(pp_MAW_004)##
	#PresetGame(pp_MAW_031)##
	#PresetGame(pp_MAW_032)##
	#PresetGame(pp_MAW_033)##
	#PresetGame(pp_MAW_034)##
	#PresetGame(pp_REV_012)##
	#PresetGame(pp_REV_013)## OK
	#PresetGame(pp_REV_013t)## OK
	#PresetGame(pp_REV_014)##
	#PresetGame(pp_REV_015)##
	#PresetGame(pp_REV_016)##
	#PresetGame(pp_REV_017a)## OK
	#PresetGame(pp_REV_017b)## OK
	#PresetGame(pp_REV_017c)## OK
	#PresetGame(pp_REV_018)##
	#PresetGame(pp_REV_019)##
	#PresetGame(pp_REV_020)##
	#PresetGame(pp_REV_021)##
	#PresetGame(pp_REV_022)##
	#PresetGame(pp_REV_023)##
	#PresetGame(pp_REV_238)##
	#PresetGame(pp_REV_251)##
	#PresetGame(pp_REV_308)##
	#PresetGame(pp_REV_338)##
	#PresetGame(pp_REV_351)##
	#PresetGame(pp_REV_370)##
	#PresetGame(pp_REV_375)##
	#PresetGame(pp_REV_377)##
	#PresetGame(pp_REV_378)##
	#PresetGame(pp_REV_515e)##
	#PresetGame(pp_REV_770)##
	#PresetGame(pp_REV_771)##
	#PresetGame(pp_REV_837)##
	#PresetGame(pp_REV_839)##
	#PresetGame(pp_REV_841)##
	#PresetGame(pp_REV_843)##
	#PresetGame(pp_REV_845)##
	#PresetGame(pp_REV_900)##
	#PresetGame(pp_REV_901)##
	#PresetGame(pp_REV_906)##
	#PresetGame(pp_REV_916)##
	#PresetGame(pp_REV_945)##
	#PresetGame(pp_REV_946)##
	#PresetGame(pp_REV_956)##
	#PresetGame(pp_REV_957)##
	#PresetGame(pp_REV_960)##
	#PresetGame(pp_REV_COIN1)##
	#PresetGame(pp_REV_COIN2)##
	pass


##########MAW_004##########

class pp_MAW_004(Preset_Play):
	""" Soul Seeker
	<b>Battlecry:</b> Swap this with a random minion from your opponent's deck. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_004", self.controller)
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


##########MAW_031##########

class pp_MAW_031(Preset_Play):
	""" Afterlife Attendant
	Your <b>Infuse</b> cards also <b>Infuse</b> while in your deck. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_031", self.controller)
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


##########MAW_032##########

class pp_MAW_032(Preset_Play):
	""" Tight-Lipped Witness
	<b>Secrets</b> can't be revealed. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_032", self.controller)
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


##########MAW_033##########

class pp_MAW_033(Preset_Play):
	""" Sylvanas, the Accused
	<b>Battlecry:</b> Destroy an enemy minion. <b>Infuse (@):</b> Take control of it instead. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_033", self.controller)
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


##########MAW_034##########

class pp_MAW_034(Preset_Play):
	""" The Jailer
	<b>Battlecry:</b> Destroy your  deck. For the rest of the game, your minions are <b>Immune</b>. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_034", self.controller)
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


##########REV_012##########

class pp_REV_012(Preset_Play):
	""" Bog Beast
	<b><b>Taunt</b></b>  <b>Deathrattle:</b> Summon a 2/4  Muckmare with <b>Taunt</b>. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_012", self.controller)
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


##########REV_013##########

class pp_REV_013(Preset_Play):
	""" Stoneborn Accuser
	<b>Infuse (@):</b> Gain "<b>Battlecry:</b> Deal 5 damage." """
	def preset_deck(self):
		self.con1=self.exchange_card("REV_013", self.controller)
		self.con1.script_data_num_1=2## originally it is 5
		self.con2=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con2=self.con2[0][0]
		self.con3=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con3=self.con3[0][0]
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.change_turn()
		### opp
		Hit(self.con2,3).trigger(self.opponent)
		Hit(self.con3,3).trigger(self.opponent)
		Hit(self.con3,3).trigger(self.opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_REV_013t(Preset_Play):
	""" Stoneborn Accuser
	<b>Infused</b> <b>Battlecry:</b> Deal 5 damage. """
	def preset_deck(self):
		self.con1=self.exchange_card("REV_013t", self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionH6")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1, target=self.opp1)
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.opponent.field:
			self.print_stats("field", card)
	pass


##########REV_014##########

class pp_REV_014(Preset_Play):
	""" Red Herring
	<b>Taunt</b> Your non-Red Herring minions have <b>Stealth</b>. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_014", self.controller)
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


##########REV_015##########

class pp_REV_015(Preset_Play):
	""" Masked Reveler
	<b>Rush</b> <b>Deathrattle:</b> Summon a 2/2 copy of another minion in your deck. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_015", self.controller)
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


##########REV_016##########

class pp_REV_016(Preset_Play):
	""" Crooked Cook
	At the end of your turn,  if you dealt 3 or more  damage to the enemy  hero, draw a card. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_016", self.controller)
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


##########REV_017##########

class pp_REV_017a(Preset_Play):
	""" Insatiable Devourer
	<b>Battlecry:</b> Devour an enemy  minion and gain its stats.  _<b>Infuse (@):</b> And its neighbors. """
	def preset_deck(self):
		self.con1=self.exchange_card("REV_017", self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1, target=self.opp1)
		#self.change_turn()
		### opp
		#self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("field", card, show_buff=True)
		
	pass
class pp_REV_017b(Preset_Play):
	""" Insatiable Devourer
	<b>Battlecry:</b> Devour an enemy  minion and gain its stats.  _<b>Infuse (@):</b> And its neighbors. """
	def preset_deck(self):
		self.con1=self.exchange_card("REV_017", self.controller)
		self.con1.script_data_num_1=2
		self.con2=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con2=self.con2[0][0]
		self.con3=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con3=self.con3[0][0]
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		#self.play_card(self.con1)
		self.change_turn()
		### opp
		Hit(self.con2,3).trigger(self.opponent)
		Hit(self.con3,3).trigger(self.opponent)
		Hit(self.con4,3).trigger(self.opponent)
		#self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_REV_017c(Preset_Play):
	""" Insatiable Devourer
	<b>Battlecry:</b> Devour an enemy  minion and gain its stats.  _<b>Infuse (@):</b> And its neighbors. """
	def preset_deck(self):
		self.con1=self.exchange_card("REV_017t", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		self.opp2=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp2=self.opp2[0][0]
		self.opp3=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp3=self.opp3[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1, target=self.opp2)
		#self.change_turn()
		### opp
		#self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("field", card, show_buff=True)
		for card in self.opponent.field:
			self.print_stats("field", card)
	pass


##########REV_018##########

class pp_REV_018(Preset_Play):
	""" Prince Renathal
	Your deck size and  starting Health are 40. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_018", self.controller)
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


##########REV_019##########

class pp_REV_019(Preset_Play):
	""" Famished Fool
	<b>Battlecry:</b> Draw a card. <b>Infuse (@):</b> Draw 3 instead. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_019", self.controller)
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


##########REV_020##########

class pp_REV_020(Preset_Play):
	""" Dinner Performer
	<b>Battlecry:</b> Summon a random minion from your deck that you can afford to play. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_020", self.controller)
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


##########REV_021##########

class pp_REV_021(Preset_Play):
	""" Kael'thas Sinstrider
	Every third minion you play each turn costs (0). """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_021", self.controller)
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


##########REV_022##########

class pp_REV_022(Preset_Play):
	""" Murloc Holmes
	<b>Battlecry:</b> Solve 3 Clues  about your opponent's cards  to get copies of them. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_022", self.controller)
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


##########REV_023##########

class pp_REV_023(Preset_Play):
	""" Demolition Renovator
	<b>Battlecry:</b> Destroy  an enemy location. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_023", self.controller)
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


##########REV_238##########

class pp_REV_238(Preset_Play):
	""" Theotar, the Mad Duke
	<b>Battlecry:</b> <b>Discover</b> a card in each player's hand and swap them. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_238", self.controller)
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


##########REV_251##########

class pp_REV_251(Preset_Play):
	""" Sinrunner
	<b>Deathrattle:</b> Destroy a random enemy minion. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_251", self.controller)
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


##########REV_308##########

class pp_REV_308(Preset_Play):
	""" Maze Guide
	<b>Battlecry</b>: Summon a random 2-Cost minion. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_308", self.controller)
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


##########REV_338##########

class pp_REV_338(Preset_Play):
	""" Dredger Staff
	<b>Battlecry:</b> Give minions  in your hand +1 Health. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_338", self.controller)
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


##########REV_351##########

class pp_REV_351(Preset_Play):
	""" Roosting Gargoyle
	<b>Battlecry:</b> Give a friendly Beast +2 Attack. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_351", self.controller)
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


##########REV_370##########

class pp_REV_370(Preset_Play):
	""" Party Crasher
	<b>Battlecry:</b> Choose an enemy minion. Throw a random minion from your hand at it. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_370", self.controller)
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


##########REV_375##########

class pp_REV_375(Preset_Play):
	""" Stoneborn General
	<b>Rush</b>  __<b>Deathrattle:</b> Summon an  ___8/8 Gravewing with <b>Rush</b>._ """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_375", self.controller)
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


##########REV_377##########

class pp_REV_377(Preset_Play):
	""" Invitation Courier
	After a card is added to your hand from another class, copy it. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_377", self.controller)
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


##########REV_378##########

class pp_REV_378(Preset_Play):
	""" Forensic Duster
	<b>Battlecry:</b> Your  opponent's minions  cost (1) more next turn. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_378", self.controller)
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


##########REV_515e##########

class pp_REV_515e(Preset_Play):
	""" Cosmic Power
	+2/+2. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_515e", self.controller)
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


##########REV_770##########

class pp_REV_770(Preset_Play):
	""" Murloc Holmes
	 """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_770", self.controller)
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


##########REV_771##########

class pp_REV_771(Preset_Play):
	""" Investigate
	Search for clues. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_771", self.controller)
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


##########REV_837##########

class pp_REV_837(Preset_Play):
	""" Muck Plumber
	ALL minions cost (2) more. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_837", self.controller)
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


##########REV_839##########

class pp_REV_839(Preset_Play):
	""" Sinstone Totem
	At the end of your turn, gain +1 Health. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_839", self.controller)
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


##########REV_841##########

class pp_REV_841(Preset_Play):
	""" Anonymous Informant
	<b>Battlecry:</b> The next <b>Secret</b> you play costs (0). """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_841", self.controller)
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


##########REV_843##########

class pp_REV_843(Preset_Play):
	""" Sinfueled Golem
	<b>Infuse (@):</b> Gain stats equal to the Attack of the minions that <b>Infused</b> this. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_843", self.controller)
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


##########REV_845##########

class pp_REV_845(Preset_Play):
	""" Volatile Skeleton
	<b>Deathrattle:</b> Deal 2 damage to a random enemy. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_845", self.controller)
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


##########REV_900##########

class pp_REV_900(Preset_Play):
	""" Scuttlebutt Ghoul
	<b>Taunt</b> <b>Battlecry:</b> If you control a <b>Secret</b>, summon a copy of this. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_900", self.controller)
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


##########REV_901##########

class pp_REV_901(Preset_Play):
	""" Dispossessed Soul
	<b>Battlecry:</b> If you control a location, <b>Discover</b> a copy of a card in your deck. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_901", self.controller)
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


##########REV_906##########

class pp_REV_906(Preset_Play):
	""" Sire Denathrius
	<b><b>Lifesteal</b>.</b> <b>Battlecry:</b> Deal 5 damage amongst enemies. <b>Endlessly Infuse (1):</b> Deal 1 more. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_906", self.controller)
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


##########REV_916##########

class pp_REV_916(Preset_Play):
	""" Creepy Painting
	After another minion dies, become a copy of it. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_916", self.controller)
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


##########REV_945##########

class pp_REV_945(Preset_Play):
	""" Sketchy Stranger
	<b>Battlecry:</b> <b>Discover</b> a <b>Secret</b> from another class. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_945", self.controller)
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


##########REV_946##########

class pp_REV_946(Preset_Play):
	""" Steamcleaner
	<b>Battlecry:</b> Destroy ALL cards in both players' decks that didn't start there. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_946", self.controller)
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


##########REV_956##########

class pp_REV_956(Preset_Play):
	""" Priest of the Deceased
	<b>Taunt</b> <b>Infuse (@):</b> Gain +2/+2. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_956", self.controller)
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


##########REV_957##########

class pp_REV_957(Preset_Play):
	""" Murlocula
	<b>Lifesteal</b> <b>Infuse (@):</b> This costs (0). """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_957", self.controller)
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


##########REV_960##########

class pp_REV_960(Preset_Play):
	""" Ashen Elemental
	<b>Battlecry:</b> Whenever your opponent draws a card next turn, they take 2 damage. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_960", self.controller)
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


##########REV_COIN1##########

class pp_REV_COIN1(Preset_Play):
	""" The Coin
	Gain 1 Mana Crystal this turn only. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_COIN1", self.controller)
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


##########REV_COIN2##########

class pp_REV_COIN2(Preset_Play):
	""" The Coin
	Gain 1 Mana Crystal this turn only. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("REV_COIN2", self.controller)
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


