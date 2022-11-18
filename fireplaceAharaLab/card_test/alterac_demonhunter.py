from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity

def alterac_demonhunter():

	#PresetGame(pp_AV_118)##
	#PresetGame(pp_AV_204)##
	#PresetGame(pp_AV_209)##
	#PresetGame(pp_AV_261)##
	#PresetGame(pp_AV_262)##
	#PresetGame(pp_AV_264)##
	#PresetGame(pp_AV_265)##
	#PresetGame(pp_AV_267)##
	#PresetGame(pp_AV_269)##
	#PresetGame(pp_AV_661)##
	#PresetGame(pp_ONY_014)##
	#PresetGame(pp_ONY_016)##
	#PresetGame(pp_ONY_036)##
	pass

##########AV_118##########

class pp_AV_118(Preset_Play):
	""" Battleworn Vanguard
	After your hero attacks,summon two 1/1 Felwings. """
	def preset_deck(self):
		self.mark1=self.exchange_card("AV_118", self.controller)
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


##########AV_204##########

class pp_AV_204(Preset_Play):
	""" Kurtrus, Demon-Render
	[Battlecry:] Summon two@/4 Demons with [Rush].<i>(Improved by your heroattacks this game.)</i> """
	def preset_deck(self):
		self.mark1=self.exchange_card("AV_204", self.controller)
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


##########AV_209##########

class pp_AV_209(Preset_Play):
	""" Dreadprison Glaive
	[Honorable Kill:] Dealdamage equal to yourhero's Attack to theenemy hero. """
	def preset_deck(self):
		self.mark1=self.exchange_card("AV_209", self.controller)
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


##########AV_261##########

class pp_AV_261(Preset_Play):
	""" Flag Runner
	Whenever a friendly minion dies, gain +1 Attack. """
	def preset_deck(self):
		self.mark1=self.exchange_card("AV_261", self.controller)
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


##########AV_262##########

class pp_AV_262(Preset_Play):
	""" Warden of Chains
	[Taunt][Battlecry:] If you're holdinga Demon that costs (5) ormore, gain +1/+2. """
	def preset_deck(self):
		self.mark1=self.exchange_card("AV_262", self.controller)
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


##########AV_264##########

class pp_AV_264(Preset_Play):
	""" Sigil of Reckoning
	At the start of your next turn, summon a random Demon from your hand. """
	def preset_deck(self):
		self.mark1=self.exchange_card("AV_264", self.controller)
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


##########AV_265##########

class pp_AV_265(Preset_Play):
	""" Ur'zul Giant
	Costs (1) less for each friendly minion that died this game. """
	def preset_deck(self):
		self.mark1=self.exchange_card("AV_265", self.controller)
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


##########AV_267##########

class pp_AV_267(Preset_Play):
	""" Caria Felsoul
	[Battlecry:] Transform into a 7/7 copy of a Demon in your deck. """
	def preset_deck(self):
		self.mark1=self.exchange_card("AV_267", self.controller)
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


##########AV_269##########

class pp_AV_269(Preset_Play):
	""" Flanking Maneuver
	Summon a 4/2 Demon with [Rush]. If it dies this turn, summon another. """
	def preset_deck(self):
		self.mark1=self.exchange_card("AV_269", self.controller)
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


##########AV_661##########

class pp_AV_661(Preset_Play):
	""" Field of Strife
	Your minions have+1 Attack.Lasts 3 turns. """
	def preset_deck(self):
		self.mark1=self.exchange_card("AV_661", self.controller)
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


##########ONY_014##########

class pp_ONY_014(Preset_Play):
	""" Keen Reflex
	Deal $1 damage to allminions. [Honorable Kill:]Gain +1 Attack this turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("ONY_014", self.controller)
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


##########ONY_016##########

class pp_ONY_016(Preset_Play):
	""" Wings of Hate (Rank 1)
	Summon two 1/1Felwings. <i>(Upgradeswhen you have 5 Mana.)</i> """
	def preset_deck(self):
		self.mark1=self.exchange_card("ONY_016", self.controller)
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


##########ONY_036##########

class pp_ONY_036(Preset_Play):
	""" Razorglaive Sentinel
	After you play the left or right-most card in your hand, draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("ONY_036", self.controller)
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




