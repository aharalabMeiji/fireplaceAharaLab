from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity

def classic_rogue():

	#PresetGame(pp_VAN_CS2_072)##
	#PresetGame(pp_VAN_CS2_073)##
	#PresetGame(pp_VAN_CS2_074)##
	#PresetGame(pp_VAN_CS2_075)##
	#PresetGame(pp_VAN_CS2_076)##
	#PresetGame(pp_VAN_CS2_077)##
	#PresetGame(pp_VAN_CS2_080)##
	#PresetGame(pp_VAN_CS2_082)##
	#PresetGame(pp_VAN_CS2_233)##
	#PresetGame(pp_VAN_EX1_124)##
	#PresetGame(pp_VAN_EX1_126)## OK
	#PresetGame(pp_VAN_EX1_128)## OK
	#PresetGame(pp_VAN_EX1_129)##
	#PresetGame(pp_VAN_EX1_131)##
	#PresetGame(pp_VAN_EX1_133)##
	#PresetGame(pp_VAN_EX1_134)##
	#PresetGame(pp_VAN_EX1_137)## OK
	#PresetGame(pp_VAN_EX1_144)##
	#PresetGame(pp_VAN_EX1_145)## OK
	#PresetGame(pp_VAN_EX1_278)##
	#PresetGame(pp_VAN_EX1_522)##
	#PresetGame(pp_VAN_EX1_581)##
	#PresetGame(pp_VAN_EX1_613)##
	#PresetGame(pp_VAN_HERO_03bp)## HP
	#PresetGame(pp_VAN_NEW1_004)##
	#PresetGame(pp_VAN_NEW1_005)##
	#PresetGame(pp_VAN_NEW1_014)##
	pass

##########VAN_CS2_072##########

class pp_VAN_CS2_072(Preset_Play):
	""" Backstab
	Deal $2 damage to an undamaged minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_072", self.controller)
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


##########VAN_CS2_073##########

class pp_VAN_CS2_073(Preset_Play):
	""" Cold Blood
	Give a minion +2 Attack. [Combo:] +4 Attack instead. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_073", self.controller)
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


##########VAN_CS2_074##########

class pp_VAN_CS2_074(Preset_Play):
	""" Deadly Poison
	Give your weapon +2_Attack. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_074", self.controller)
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


##########VAN_CS2_075##########

class pp_VAN_CS2_075(Preset_Play):
	""" Sinister Strike
	Deal $3 damage to the_enemy hero. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_075", self.controller)
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


##########VAN_CS2_076##########

class pp_VAN_CS2_076(Preset_Play):
	""" Assassinate
	Destroy an enemy minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_076", self.controller)
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


##########VAN_CS2_077##########

class pp_VAN_CS2_077(Preset_Play):
	""" Sprint
	Draw 4 cards. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_077", self.controller)
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


##########VAN_CS2_080##########

class pp_VAN_CS2_080(Preset_Play):
	""" Assassin's Blade
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_080", self.controller)
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


##########VAN_CS2_082##########

class pp_VAN_CS2_082(Preset_Play):
	""" Wicked Knife
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_082", self.controller)
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


##########VAN_CS2_233##########

class pp_VAN_CS2_233(Preset_Play):
	""" Blade Flurry
	Destroy your weapon and deal its damage to all enemies. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_233", self.controller)
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


##########VAN_EX1_124##########

class pp_VAN_EX1_124(Preset_Play):
	""" Eviscerate
	Deal $2 damage. [Combo:] Deal $4 damage instead. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_124", self.controller)
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


##########VAN_EX1_126##########

class pp_VAN_EX1_126(Preset_Play):
	""" Betrayal
	Force an enemy minion to deal its damage to the minions next to it. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_126", self.controller)
		self.mark2=self.summon_card(self.opponent, self.card_choice("minionH3"))
		self.mark3=self.summon_card(self.opponent, self.card_choice("minionA2"))
		self.mark4=self.summon_card(self.opponent, self.card_choice("minionH3"))
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1, target=self.mark3)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.opponent.field:
			self.print_stats("opponent.field", card)
	pass


##########VAN_EX1_128##########

class pp_VAN_EX1_128(Preset_Play):
	""" Conceal
	Give your minions [Stealth] until your next_turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_128", self.controller)
		self.mark4=self.summon_card(self.controller, self.card_choice("minionH3"))
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.asserting(self.mark4.stealthed==True,"self.mark4.stealthed==True")
		self.change_turn()
		### opp
		self.asserting(self.mark4.stealthed==True,"self.mark4.stealthed==True")
		self.change_turn()
		### con
		self.asserting(self.mark4.stealthed==False,"self.mark4.stealthed==False")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_EX1_129##########

class pp_VAN_EX1_129(Preset_Play):
	""" Fan of Knives
	Deal $1 damage to all enemy minions. Draw_a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_129", self.controller)
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


##########VAN_EX1_131##########

class pp_VAN_EX1_131(Preset_Play):
	""" Defias Ringleader
	[Combo:] Summon a 2/1 Defias Bandit. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_131", self.controller)
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


##########VAN_EX1_133##########

class pp_VAN_EX1_133(Preset_Play):
	""" Perdition's Blade
	[Battlecry:] Deal 1 damage. [Combo:] Deal 2 instead. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_133", self.controller)
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


##########VAN_EX1_134##########

class pp_VAN_EX1_134(Preset_Play):
	""" SI:7 Agent
	[Combo:] Deal 2 damage. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_134", self.controller)
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


##########VAN_EX1_137##########

class pp_VAN_EX1_137(Preset_Play):
	""" Headcrack
	Deal $2 damage to the enemy hero. [Combo:] Return this to your hand next turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_137", self.controller)
		self.mark4=self.exchange_card(self.card_choice("minionH3"), self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark4)
		self.play_card(self.mark1)
		self.asserting(self.opponent.hero.damage==2, "self.opponent.hero.damage==2")
		self.change_turn()
		### opp
		self.change_turn()
		cards=[card.id for card in self.controller.hand]
		self.asserting('VAN_EX1_137' in cards, "'VAN_EX1_137' in cards")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_EX1_144##########

class pp_VAN_EX1_144(Preset_Play):
	""" Shadowstep
	Return a friendly minion to your hand. It_costs (2) less. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_144", self.controller)
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


##########VAN_EX1_145##########

class pp_VAN_EX1_145(Preset_Play):
	""" Preparation
	The next spell you cast this turn costs (3) less. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_145", self.controller)
		self.mark2=self.exchange_card("spell", self.controller)
		self.mark3=self.exchange_card("spell", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.asserting(self.mark2.cost==max(self.mark2.data.cost-3,0),"self.mark2.cost==max(self.mark2.data.cost-3,0)") 
		self.play_card(self.mark2)
		self.asserting(self.mark3.cost==max(self.mark3.data.cost,0),"self.mark3.cost==max(self.mark3.data.cost,0)") 
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_EX1_278##########

class pp_VAN_EX1_278(Preset_Play):
	""" Shiv
	Deal $1 damage.Draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_278", self.controller)
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


##########VAN_EX1_522##########

class pp_VAN_EX1_522(Preset_Play):
	""" Patient Assassin
	[Stealth]. Destroy any minion damaged by this minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_522", self.controller)
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


##########VAN_EX1_581##########

class pp_VAN_EX1_581(Preset_Play):
	""" Sap
	Return an enemy minion to your opponent's hand. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_581", self.controller)
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


##########VAN_EX1_613##########

class pp_VAN_EX1_613(Preset_Play):
	""" Edwin VanCleef
	[Combo:] Gain +2/+2 for each card played earlier this turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_613", self.controller)
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


##########VAN_HERO_03bp##########

class pp_VAN_HERO_03bp(Preset_Play):
	""" Dagger Mastery
	[Hero Power]Equip a 1/2 Dagger. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_HERO_03bp", self.controller)
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


##########VAN_NEW1_004##########

class pp_VAN_NEW1_004(Preset_Play):
	""" Vanish
	Return all minions to their owner's hand. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_NEW1_004", self.controller)
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


##########VAN_NEW1_005##########

class pp_VAN_NEW1_005(Preset_Play):
	""" Kidnapper
	[Combo:] Return a minion to_its owner's hand. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_NEW1_005", self.controller)
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


##########VAN_NEW1_014##########

class pp_VAN_NEW1_014(Preset_Play):
	""" Master of Disguise
	[Battlecry:] Give a friendly minion [Stealth]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_NEW1_014", self.controller)
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


