from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity

def classic_hunter():

	#PresetGame(pp_VAN_CS2_084)##
	#PresetGame(pp_VAN_CS2_237)##
	#PresetGame(pp_VAN_DS1_070)##
	#PresetGame(pp_VAN_DS1_175)##
	#PresetGame(pp_VAN_DS1_178)##
	#PresetGame(pp_VAN_DS1_183)##
	#PresetGame(pp_VAN_DS1_184)##
	#PresetGame(pp_VAN_DS1_185)##
	#PresetGame(pp_VAN_DS1_188)##
	#PresetGame(pp_VAN_EX1_531)##
	#PresetGame(pp_VAN_EX1_533)##
	#PresetGame(pp_VAN_EX1_534)##
	#PresetGame(pp_VAN_EX1_536)##
	#PresetGame(pp_VAN_EX1_537)##
	#PresetGame(pp_VAN_EX1_538)##
	#PresetGame(pp_VAN_EX1_539)##
	#PresetGame(pp_VAN_EX1_543)##
	#PresetGame(pp_VAN_EX1_544)##
	#PresetGame(pp_VAN_EX1_549)##
	PresetGame(pp_VAN_EX1_554)##
	PresetGame(pp_VAN_EX1_609)##
	#PresetGame(pp_VAN_EX1_610)##
	PresetGame(pp_VAN_EX1_611)##
	#PresetGame(pp_VAN_EX1_617)##
	#PresetGame(pp_VAN_HERO_05bp)##
	#PresetGame(pp_VAN_NEW1_031)##
	#PresetGame(pp_VAN_NEW1_032)##
	#PresetGame(pp_VAN_NEW1_033)##
	#PresetGame(pp_VAN_NEW1_034)##


##########VAN_CS2_084##########

class pp_VAN_CS2_084(Preset_Play):
	""" Hunter's Mark
	Change a minion's Health to 1. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_084", self.controller)
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


##########VAN_CS2_237##########

class pp_VAN_CS2_237(Preset_Play):
	""" Starving Buzzard
	Whenever you summon a Beast, draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_237", self.controller)
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


##########VAN_DS1_070##########

class pp_VAN_DS1_070(Preset_Play):
	""" Houndmaster
	[Battlecry:] Give a friendly Beast +2/+2 and [Taunt]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_DS1_070", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("beast")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark4)
		self.play_card(self.mark1, target=self.mark4)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.mark4.taunt==True, "True"
		for card in self.controller.field:
			self.print_stats("field", card, show_buff=True)
	pass


##########VAN_DS1_175##########

class pp_VAN_DS1_175(Preset_Play):
	""" Timber Wolf
	Your other Beasts have +1_Attack. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_DS1_175", self.controller)
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


##########VAN_DS1_178##########

class pp_VAN_DS1_178(Preset_Play):
	""" Tundra Rhino
	Your Beasts have [Charge]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_DS1_178", self.controller)
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


##########VAN_DS1_183##########

class pp_VAN_DS1_183(Preset_Play):
	""" Multi-Shot
	Deal $3 damage to two random enemy minions. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_DS1_183", self.controller)
		self.mark2=Summon(self.opponent, self.card_choice("minionH4")).trigger(self.opponent)
		self.mark2=self.mark2[0][0]
		self.mark3=Summon(self.opponent, self.card_choice("minionH4")).trigger(self.opponent)
		self.mark3=self.mark3[0][0]
		self.mark4=Summon(self.opponent, self.card_choice("minionH4")).trigger(self.opponent)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		#self.change_turn()
		### opp
		#self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.opponent.field:
			self.print_stats("enemy field", card)
	pass


##########VAN_DS1_184##########

class pp_VAN_DS1_184(Preset_Play):
	""" Tracking
	Look at the top 3 cards of your deck. Draw one and discard the others. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_DS1_184", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.choose_action()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_DS1_185##########

class pp_VAN_DS1_185(Preset_Play):
	""" Arcane Shot
	Deal $2 damage. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_DS1_185", self.controller)
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


##########VAN_DS1_188##########

class pp_VAN_DS1_188(Preset_Play):
	""" Gladiator's Longbow
	Your hero is [Immune] while attacking. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_DS1_188", self.controller)
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


##########VAN_EX1_531##########

class pp_VAN_EX1_531(Preset_Play):
	""" Scavenging Hyena
	Whenever a friendly Beast dies, gain +2/+1. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_531", self.controller)
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


##########VAN_EX1_533##########

class pp_VAN_EX1_533(Preset_Play):
	""" Misdirection
	[Secret:] When an enemy attacks your hero, instead it attacks another random character. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_533", self.controller)
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


##########VAN_EX1_534##########

class pp_VAN_EX1_534(Preset_Play):
	""" Savannah Highmane
	[Deathrattle:] Summon two 2/2 Hyenas. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_534", self.controller)
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


##########VAN_EX1_536##########

class pp_VAN_EX1_536(Preset_Play):
	""" Eaglehorn Bow
	Whenever a [Secret] is revealed, gain +1 Durability. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_536", self.controller)
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


##########VAN_EX1_537##########

class pp_VAN_EX1_537(Preset_Play):
	""" Explosive Shot
	Deal $5 damage to a minion and $2 damage to adjacent ones. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_537", self.controller)
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


##########VAN_EX1_538##########

class pp_VAN_EX1_538(Preset_Play):
	""" Unleash the Hounds
	For each enemy minion, summon a 1/1 Hound with [Charge]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_538", self.controller)
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


##########VAN_EX1_539##########

class pp_VAN_EX1_539(Preset_Play):
	""" Kill Command
	Deal $3 damage. If you control a Beast, deal$5 damage instead. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_539", self.controller)
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


##########VAN_EX1_543##########

class pp_VAN_EX1_543(Preset_Play):
	""" King Krush
	[Charge] """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_543", self.controller)
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


##########VAN_EX1_544##########

class pp_VAN_EX1_544(Preset_Play):
	""" Flare
	All minions lose [Stealth]. Destroy all enemy [Secrets]. Draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_544", self.controller)
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


##########VAN_EX1_549##########

class pp_VAN_EX1_549(Preset_Play):
	""" Bestial Wrath
	Give a Beast +2 Attack and [Immune] this turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_549", self.controller)
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


##########VAN_EX1_554##########

class pp_VAN_EX1_554(Preset_Play):
	""" Snake Trap
	[Secret:] When one of your minions is attacked, summon three 1/1 Snakes. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_554", self.controller)
		self.mark2=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.controller)
		self.mark2=self.mark2[0][0]
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.cast_secret(self.mark1)
		self.change_turn()
		### opp
		self.attack_card(self.mark2, self.mark4)
		#self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("field", card)
	pass


##########VAN_EX1_609##########

class pp_VAN_EX1_609(Preset_Play):
	""" Snipe
	[Secret:] After your opponent plays a minion, deal $4 damage to it. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_609", self.controller)
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


##########VAN_EX1_610##########

class pp_VAN_EX1_610(Preset_Play):
	""" Explosive Trap
	[Secret:] When your hero is attacked, deal $2 damage to all enemies. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_610", self.controller)
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


##########VAN_EX1_611##########

class pp_VAN_EX1_611(Preset_Play):
	""" Freezing Trap
	[Secret:] When an enemy minion attacks, return it to its owner's hand. It costs (2) more. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_611", self.controller)
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


##########VAN_EX1_617##########

class pp_VAN_EX1_617(Preset_Play):
	""" Deadly Shot
	Destroy a random enemy minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_617", self.controller)
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


##########VAN_HERO_05bp##########

class pp_VAN_HERO_05bp(Preset_Play):
	""" Steady Shot
	[Hero Power]Deal $2 damage to the enemy hero.@[Hero Power]Deal $2 damage. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_HERO_05bp", self.controller)
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


##########VAN_NEW1_031##########

class pp_VAN_NEW1_031(Preset_Play):
	""" Animal Companion
	Summon a random Beast Companion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_NEW1_031", self.controller)
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


##########VAN_NEW1_032##########

class pp_VAN_NEW1_032(Preset_Play):
	""" Misha
	[Taunt] """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_NEW1_032", self.controller)
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


##########VAN_NEW1_033##########

class pp_VAN_NEW1_033(Preset_Play):
	""" Leokk
	Your other minions have +1 Attack. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_NEW1_033", self.controller)
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


##########VAN_NEW1_034##########

class pp_VAN_NEW1_034(Preset_Play):
	""" Huffer
	[Charge] """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_NEW1_034", self.controller)
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


