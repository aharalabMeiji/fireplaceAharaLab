from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity

def classic_druid():

	#PresetGame(pp_VAN_CS2_005)##
	#PresetGame(pp_VAN_CS2_007)##
	#PresetGame(pp_VAN_CS2_008)##
	#PresetGame(pp_VAN_CS2_009)##
	#PresetGame(pp_VAN_CS2_011)##
	#PresetGame(pp_VAN_CS2_012)##
	#PresetGame(pp_VAN_CS2_013)##
	#PresetGame(pp_VAN_CS2_232)##
	#PresetGame(pp_VAN_EX1_154)##
	#PresetGame(pp_VAN_EX1_155)##
	PresetGame(pp_VAN_EX1_158)##
	#PresetGame(pp_VAN_EX1_160)##
	#PresetGame(pp_VAN_EX1_161)##
	#PresetGame(pp_VAN_EX1_164)##
	PresetGame(pp_VAN_EX1_165)##
	#PresetGame(pp_VAN_EX1_166)##
	#PresetGame(pp_VAN_EX1_169)##
	#PresetGame(pp_VAN_EX1_173)##
	#PresetGame(pp_VAN_EX1_178)##
	#PresetGame(pp_VAN_EX1_570)##
	#PresetGame(pp_VAN_EX1_571)##
	#PresetGame(pp_VAN_EX1_573)##
	#PresetGame(pp_VAN_EX1_578)##
	#PresetGame(pp_VAN_EX1_tk9)##
	#PresetGame(pp_VAN_HERO_06bp)##
	#PresetGame(pp_VAN_NEW1_007)##
	#PresetGame(pp_VAN_NEW1_008)##


##########VAN_CS2_005##########

class pp_VAN_CS2_005(Preset_Play):
	""" Claw
	Give your hero +2_Attack this turn. Gain 2 Armor. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_005", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_CS2_007##########

class pp_VAN_CS2_007(Preset_Play):
	""" Healing Touch
	Restore #8 Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_007", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_CS2_008##########

class pp_VAN_CS2_008(Preset_Play):
	""" Moonfire
	Deal $1 damage. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_008", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_CS2_009##########

class pp_VAN_CS2_009(Preset_Play):
	""" Mark of the Wild
	Give a minion [Taunt] and +2/+2.<i>(+2 Attack/+2 Health)</i> """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_009", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_CS2_011##########

class pp_VAN_CS2_011(Preset_Play):
	""" Savage Roar
	Give your characters +2_Attack this turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_011", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_CS2_012##########

class pp_VAN_CS2_012(Preset_Play):
	""" Swipe
	Deal $4 damage to an enemy and $1 damage to all other enemies. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_012", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_CS2_013##########

class pp_VAN_CS2_013(Preset_Play):
	""" Wild Growth
	Gain an empty Mana Crystal. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_013", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_CS2_232##########

class pp_VAN_CS2_232(Preset_Play):
	""" Ironbark Protector
	[Taunt] """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_232", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_EX1_154##########

class pp_VAN_EX1_154(Preset_Play):
	""" Wrath
	[Choose One -]Deal $3 damage to a minion; or $1 damageand draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_154", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_EX1_155##########

class pp_VAN_EX1_155(Preset_Play):
	""" Mark of Nature
	[Choose One -] Give a minion +4 Attack; or +4 Health and [Taunt]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_155", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_EX1_158##########

class pp_VAN_EX1_158(Preset_Play):
	""" Soul of the Forest
	Give your minions "[Deathrattle:] Summon a 2/2 Treant." """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_158", self.controller)
		self.mark2=Summon(self.controller, self.card_choice("minionH2")).trigger(self.controller)
		self.mark2=self.mark2[0][0]
		self.mark4=Summon(self.controller, self.card_choice("minionH2")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark2)
		self.play_card(self.mark4)
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		Hit(self.mark2,3).trigger(self.opponent)
		Hit(self.mark4,3).trigger(self.opponent)
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("field", card)
	pass


##########VAN_EX1_160##########

class pp_VAN_EX1_160(Preset_Play):
	""" Power of the Wild
	[Choose One -] Give your minions +1/+1; or Summon a 3/2 Panther. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_160", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_EX1_161##########

class pp_VAN_EX1_161(Preset_Play):
	""" Naturalize
	Destroy a minion.Your opponent draws 2_cards. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_161", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_EX1_164##########

class pp_VAN_EX1_164(Preset_Play):
	""" Nourish
	[Choose One -] Gain 2_Mana Crystals; or Draw 3 cards. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_164", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_EX1_165##########

class pp_VAN_EX1_165(Preset_Play):
	""" Druid of the Claw
	[Choose One -] [Charge]; or +2 Health and [Taunt]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_165", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1, choose=self.mark1.choose_cards[0])## or [1]
		#self.change_turn()
		### opp
		#self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("field", card)
	pass


##########VAN_EX1_166##########

class pp_VAN_EX1_166(Preset_Play):
	""" Keeper of the Grove
	[Choose One -] Deal_2_damage; or [Silence] a minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_166", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_EX1_169##########

class pp_VAN_EX1_169(Preset_Play):
	""" Innervate
	Gain 2 Mana Crystals this turn only. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_169", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_EX1_173##########

class pp_VAN_EX1_173(Preset_Play):
	""" Starfire
	Deal $5 damage.Draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_173", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_EX1_178##########

class pp_VAN_EX1_178(Preset_Play):
	""" Ancient of War
	[Choose One -]+5 Attack; or +5 Health and [Taunt]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_178", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_EX1_570##########

class pp_VAN_EX1_570(Preset_Play):
	""" Bite
	Give your hero +4_Attack this turn. Gain 4 Armor. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_570", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_EX1_571##########

class pp_VAN_EX1_571(Preset_Play):
	""" Force of Nature
	Summon three 2/2 Treants with[Charge] that die at the end of the turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_571", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_EX1_573##########

class pp_VAN_EX1_573(Preset_Play):
	""" Cenarius
	[Choose One -] Give your other minions +2/+2; or Summon two 2/2 Treants with [Taunt]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_573", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_EX1_578##########

class pp_VAN_EX1_578(Preset_Play):
	""" Savagery
	Deal damage equal to your hero's Attack to a minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_578", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_EX1_tk9##########

class pp_VAN_EX1_tk9(Preset_Play):
	""" Treant
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_tk9", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_HERO_06bp##########

class pp_VAN_HERO_06bp(Preset_Play):
	""" Shapeshift
	[Hero Power]+1 Attack this turn.+1 Armor. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_HERO_06bp", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_NEW1_007##########

class pp_VAN_NEW1_007(Preset_Play):
	""" Starfall
	[Choose One -]Deal $5 damage to a minion; or $2 damage to all enemy minions. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_NEW1_007", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_NEW1_008##########

class pp_VAN_NEW1_008(Preset_Play):
	""" Ancient of Lore
	[Choose One -] Draw 2 cards; or Restore #5 Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_NEW1_008", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


