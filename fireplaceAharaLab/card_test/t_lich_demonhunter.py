from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def lich_demonhunter():

	#PresetGame(pp_RLK_206)##
	#PresetGame(pp_RLK_207)##
	#PresetGame(pp_RLK_208)##
	#PresetGame(pp_RLK_209)##
	#PresetGame(pp_RLK_210)##
	#PresetGame(pp_RLK_211)##
	#PresetGame(pp_RLK_212)##
	#PresetGame(pp_RLK_213)##
	#PresetGame(pp_RLK_214)##
	#PresetGame(pp_RLK_215)##
	#PresetGame(pp_RLK_Prologue_FroznThrn_004hb3)##
	#PresetGame(pp_RLK_Prologue_Illidan_004hb)##
	#PresetGame(pp_RLK_Prologue_Illidan_004p)##
	#PresetGame(pp_RLK_Prologue_IllidanD_004hb2)##
	#PresetGame(pp_RLK_Prologue_Sylvanas_003e1)##
	pass


##########RLK_206##########

class pp_RLK_206(Preset_Play):
	""" Mark of Scorn
	Draw a card. If it's not a minion, deal $3 damage to the lowest Health enemy. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_206", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_207##########

class pp_RLK_207(Preset_Play):
	""" Fierce Outsider
	<b>Rush</b> <b>Outcast:</b> Your next <b>Outcast</b> card costs (1) less. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_207", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_208##########

class pp_RLK_208(Preset_Play):
	""" Fel'dorei Warband
	Deal $4 damage. If your deck has no minions, summon four 1/1 Illidari with <b>Rush</b>. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_208", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_209##########

class pp_RLK_209(Preset_Play):
	""" Unleash Fel
	Deal $1 damage to all enemies. <b>Manathirst_(4):</b> With <b>Lifesteal</b>. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_209", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_210##########

class pp_RLK_210(Preset_Play):
	""" Wretched Exile
	After you play an <b>Outcast</b> card, add a random <b>Outcast</b> card to your hand. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_210", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_211##########

class pp_RLK_211(Preset_Play):
	""" Deal with a Devil
	Summon two 3/3 Felfiends with <b>Lifesteal</b>. If your deck has no minions, summon another. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_211", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_212##########

class pp_RLK_212(Preset_Play):
	""" Brutal Annihilan
	<b>Taunt</b>, <b>Rush</b> After this minion survives damage, deal that amount to the enemy hero. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_212", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_213##########

class pp_RLK_213(Preset_Play):
	""" Vengeful Walloper
	<b>Rush</b>. Costs (1) less for each <b>Outcast</b> card you've played this game. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_213", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_214##########

class pp_RLK_214(Preset_Play):
	""" Souleater's Scythe
	<b>Start of Game:</b> Consume 3 different minions in your deck. Leave behind Souls that <b>Discover</b> them. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_214", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_215##########

class pp_RLK_215(Preset_Play):
	""" Felerin, the Forgotten
	<b>Battlecry:</b> Add a random <b>Outcast</b> card to the left and right sides of your hand. They cost (2) less. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_215", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_Prologue_FroznThrn_004hb3##########

class pp_RLK_Prologue_FroznThrn_004hb3(Preset_Play):
	""" The Frozen Throne
	 """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_FroznThrn_004hb3", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_Prologue_Illidan_004hb##########

class pp_RLK_Prologue_Illidan_004hb(Preset_Play):
	""" Illidan Stormrage
	 """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_Illidan_004hb", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_Prologue_Illidan_004p##########

class pp_RLK_Prologue_Illidan_004p(Preset_Play):
	""" Demon Claws
	<b>Hero Power</b> +2 Attack this turn. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_Illidan_004p", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_Prologue_IllidanD_004hb2##########

class pp_RLK_Prologue_IllidanD_004hb2(Preset_Play):
	""" Demonic Illidan
	 """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_IllidanD_004hb2", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_Prologue_Sylvanas_003e1##########

class pp_RLK_Prologue_Sylvanas_003e1(Preset_Play):
	""" Defensive Position
	Your hero has +2 Attack this turn. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_Sylvanas_003e1", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


