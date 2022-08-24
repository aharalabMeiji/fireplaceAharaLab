from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity

def sunken_demonhunter():

	#PresetGame(pp_TID_703)##
	#PresetGame(pp_TID_704)##
	#PresetGame(pp_TID_706)##
	#PresetGame(pp_TSC_006)##
	#PresetGame(pp_TSC_057)##
	#PresetGame(pp_TSC_058)##
	#PresetGame(pp_TSC_217)##
	#PresetGame(pp_TSC_218)##
	#PresetGame(pp_TSC_219)##
	#PresetGame(pp_TSC_608)##
	#PresetGame(pp_TSC_609)##
	#PresetGame(pp_TSC_610)##
	#PresetGame(pp_TSC_915)##
	pass

##########TID_703##########

class pp_TID_703(Preset_Play):
	""" Topple the Idol
	[Dredge]. Reveal it anddeal damage equal to_its Cost to all minions. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TID_703", self.controller)
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


##########TID_704##########

class pp_TID_704(Preset_Play):
	""" Fossil Fanatic
	After your hero attacks, draw a Fel spell. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TID_704", self.controller)
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


##########TID_706##########

class pp_TID_706(Preset_Play):
	""" Herald of Chaos
	[Lifesteal][Battlecry:] If you've cast aFel spell while holding this,gain [Rush]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TID_706", self.controller)
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


##########TSC_006##########

class pp_TSC_006(Preset_Play):
	""" Multi-Strike
	Give your hero +2 Attack this turn. They may attack an additional enemy minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_006", self.controller)
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


##########TSC_057##########

class pp_TSC_057(Preset_Play):
	""" Azsharan Defector
	[Rush]. [Deathrattle:] Put a'Sunken Defector' on the_bottom of your deck. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_057", self.controller)
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


##########TSC_058##########

class pp_TSC_058(Preset_Play):
	""" Predation
	Deal $3 damage.Costs (0) if you played a Naga while holding this. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_058", self.controller)
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


##########TSC_217##########

class pp_TSC_217(Preset_Play):
	""" Wayward Sage
	[Outcast:] Reduce the Costof the left and right-most_cards in your hand by (1). """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_217", self.controller)
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


##########TSC_218##########

class pp_TSC_218(Preset_Play):
	""" Lady S'theno
	[Immune] while attacking.After you cast a spell, attackthe lowest Health enemy. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_218", self.controller)
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


##########TSC_219##########

class pp_TSC_219(Preset_Play):
	""" Xhilag of the Abyss
	[Colossal +4]At the start of your turn,increase the damage ofXhilag's Stalks by 1. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_219", self.controller)
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


##########TSC_608##########

class pp_TSC_608(Preset_Play):
	""" Abyssal Depths
	Draw your two lowest Cost minions. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_608", self.controller)
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


##########TSC_609##########

class pp_TSC_609(Preset_Play):
	""" Coilskar Commander
	[Taunt]. [Battlecry:] If you'vecast three spells whileholding this, summon two__copies of this.@ <i>({0} left!)</i>@ <i>(Ready!)</i> """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_609", self.controller)
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


##########TSC_610##########

class pp_TSC_610(Preset_Play):
	""" Glaiveshark
	[Battlecry:] If your heroattacked this turn, deal 2damage to all enemies. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_610", self.controller)
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


##########TSC_915##########

class pp_TSC_915(Preset_Play):
	""" Bone Glaive
	[Battlecry:] [Dredge]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_915", self.controller)
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


