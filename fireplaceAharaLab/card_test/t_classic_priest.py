from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give, Draw
from hearthstone.enums import Zone, CardType, Rarity

def classic_priest():

	#PresetGame(pp_VAN_CS1_112)##OK
	#PresetGame(pp_VAN_CS1_113)##OK
	#PresetGame(pp_VAN_CS1_129)##OK
	#PresetGame(pp_VAN_CS1_130)##OK
	#PresetGame(pp_VAN_CS2_003)##OK
	#PresetGame(pp_VAN_CS2_004)##OK
	#PresetGame(pp_VAN_CS2_234)##
	#PresetGame(pp_VAN_CS2_235)##
	#PresetGame(pp_VAN_CS2_236)##
	#PresetGame(pp_VAN_DS1_233)##
	#PresetGame(pp_VAN_EX1_091)##
	#PresetGame(pp_VAN_EX1_332)##
	#PresetGame(pp_VAN_EX1_334)## OK
	#PresetGame(pp_VAN_EX1_335)##
	#PresetGame(pp_VAN_EX1_339)## OK
	#PresetGame(pp_VAN_EX1_341)##
	#PresetGame(pp_VAN_EX1_345)## OK
	#PresetGame(pp_VAN_EX1_350)##
	#PresetGame(pp_VAN_EX1_591)##
	#PresetGame(pp_VAN_EX1_621)##
	#PresetGame(pp_VAN_EX1_622)##
	#PresetGame(pp_VAN_EX1_623)##
	#PresetGame(pp_VAN_EX1_624)##
	PresetGame(pp_VAN_EX1_625)##
	#PresetGame(pp_VAN_EX1_626)##
	#PresetGame(pp_VAN_EX1_tk31)##

	pass

##########VAN_CS1_112##########

class pp_VAN_CS1_112(Preset_Play):
	""" Holy Nova
	Deal $2 damage to all enemies. Restore #2 Health to all friendly characters. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS1_112", self.controller)
		self.mark2=Summon(self.controller, self.card_choice("minionH5")).trigger(self.controller)
		self.mark2=self.mark2[0][0]
		self.mark3=Summon(self.opponent, self.card_choice("minionH1")).trigger(self.opponent)
		self.mark3=self.mark3[0][0]
		self.mark4=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.change_turn()
		### opp
		Hit(self.mark2, 3).trigger(self.opponent)
		self.change_turn()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.mark2.health==4, "health"
		assert self.mark3.zone==Zone.GRAVEYARD, "zone"
		assert self.mark4.health==1, "health"
		for card in self.controller.field:
			self.print_stats("field", card)
	pass


##########VAN_CS1_113##########

class pp_VAN_CS1_113(Preset_Play):
	""" Mind Control
	Take control of an enemy minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS1_113", self.controller)
		self.mark4=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1, target=self.mark4)
		#self.change_turn()
		### opp
		#self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.mark4.controller == self.controller, "controller"
		assert self.mark4.zone==Zone.PLAY, "zone"
		for card in self.controller.hand:
			self.print_stats("hand", card)
		for card in self.controller.field:
			self.print_stats("field", card)
	pass


##########VAN_CS1_129##########

class pp_VAN_CS1_129(Preset_Play):
	""" Inner Fire
	Change a minion's Attack to be equal to its Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS1_129", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1, target=self.mark4)
		#self.change_turn()
		### opp
		#self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.mark4.atk == self.mark4.health, "atk"
		for card in self.controller.field:
			self.print_stats("field", card)
	pass


##########VAN_CS1_130##########

class pp_VAN_CS1_130(Preset_Play):
	""" Holy Smite
	Deal $2 damage. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS1_130", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.opponent)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1, target=self.mark4)
		#self.change_turn()
		### opp
		#self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.mark4.health==1, "health"
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_CS2_003##########

class pp_VAN_CS2_003(Preset_Play):
	""" Mind Vision
	Put a copy of a random card in your opponent's hand into your hand. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_003", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.myhandId=[card.id for card in self.controller.hand]
		self.hishandId=[card.id for card in self.opponent.hand]
		self.play_card(self.mark1)
		self.newmyhandId=[card.id for card in self.controller.hand]
		#self.change_turn()
		### opp
		#self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		diff = [card for card in self.newmyhandId if not card in self.myhandId]
		diff=diff[0]
		assert diff in self.hishandId, "copy card"
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_CS2_004##########

class pp_VAN_CS2_004(Preset_Play):
	""" Power Word: Shield
	Give a minion +2_Health.Draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_004", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1, target=self.mark4)
		#self.change_turn()
		### opp
		#self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.mark4.health==3+2, "mark4"
		assert isinstance(self.controller._targetedaction_log[-1]['class'], Draw)==True, "draw"
		assert self.controller._targetedaction_log[-1]['target_args'][0]==self.controller.hand[-1] , "hand"
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_CS2_234##########

class pp_VAN_CS2_234(Preset_Play):
	""" Shadow Word: Pain
	Destroy a minion with 3_or less Attack. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_234", self.controller)
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


##########VAN_CS2_235##########

class pp_VAN_CS2_235(Preset_Play):
	""" Northshire Cleric
	Whenever a minion is healed, draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_235", self.controller)
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


##########VAN_CS2_236##########

class pp_VAN_CS2_236(Preset_Play):
	""" Divine Spirit
	Double a minion's Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_236", self.controller)
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


##########VAN_DS1_233##########

class pp_VAN_DS1_233(Preset_Play):
	""" Mind Blast
	Deal $5 damage to the enemy hero. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_DS1_233", self.controller)
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


##########VAN_EX1_091##########

class pp_VAN_EX1_091(Preset_Play):
	""" Cabal Shadow Priest
	[Battlecry:] Take control of an enemy minion that has 2 or less Attack. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_091", self.controller)
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


##########VAN_EX1_332##########

class pp_VAN_EX1_332(Preset_Play):
	""" Silence
	[Silence] a minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_332", self.controller)
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


##########VAN_EX1_334##########

class pp_VAN_EX1_334(Preset_Play):
	""" Shadow Madness
	Gain control of an enemy minion with 3 or less Attack until end of turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_334", self.controller)
		self.mark3=Summon(self.opponent, self.card_choice("minionA2")).trigger(self.opponent)
		self.mark3=self.mark3[0][0]
		self.mark4=Summon(self.opponent, self.card_choice("minionA4")).trigger(self.opponent)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1, target=self.mark3)#if mark4, nothing happens
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("field", card)
		self.asserting(len(self.controller.field)>0,'len(self.controller.field)>0')
		self.asserting(self.controller.field[0].atk<=3,'self.controller.field[0].atk<=3')
	pass


##########VAN_EX1_335##########

class pp_VAN_EX1_335(Preset_Play):
	""" Lightspawn
	This minion's Attack is always equal to its Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_335", self.controller)
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


##########VAN_EX1_339##########

class pp_VAN_EX1_339(Preset_Play):
	""" Thoughtsteal
	Copy 2 cards in your opponent's deck and add them to your hand. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_339", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
		opp_deck=[card.id for card in self.opponent.deck]
		self.asserting(self.controller.hand[-1].id in opp_deck,"self.controller.hand[-1].id in opp_deck")
		self.asserting(self.controller.hand[-2].id in opp_deck,"self.controller.hand[-2].id in opp_deck")
	pass


##########VAN_EX1_341##########

class pp_VAN_EX1_341(Preset_Play):
	""" Lightwell
	At the start of your turn, restore #3 Health to a damaged friendly character. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_341", self.controller)
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


##########VAN_EX1_345##########

class pp_VAN_EX1_345(Preset_Play):
	""" Mindgames
	Put a copy of a random minion from your opponent's deck into the battlefield. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_345", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("field", card)
		opp_deck=[card.id for card in self.opponent.deck]
		self.asserting(len(self.controller.field)>0,"len(self.controller.field)>0")
		self.asserting(self.controller.field[0].id in opp_deck, "self.controller.field[0].id in opp_deck")
	pass


##########VAN_EX1_350##########

class pp_VAN_EX1_350(Preset_Play):
	""" Prophet Velen
	Double the damage and healing of your spells and Hero Power. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_350", self.controller)
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


##########VAN_EX1_591##########

class pp_VAN_EX1_591(Preset_Play):
	""" Auchenai Soulpriest
	Your cards and powers that restore Health now deal damage instead. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_591", self.controller)
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


##########VAN_EX1_621##########

class pp_VAN_EX1_621(Preset_Play):
	""" Circle of Healing
	Restore #4 Health to ALL_minions. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_621", self.controller)
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


##########VAN_EX1_622##########

class pp_VAN_EX1_622(Preset_Play):
	""" Shadow Word: Death
	Destroy a minion with 5_or more Attack. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_622", self.controller)
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


##########VAN_EX1_623##########

class pp_VAN_EX1_623(Preset_Play):
	""" Temple Enforcer
	[Battlecry:] Give a friendly minion +3 Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_623", self.controller)
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


##########VAN_EX1_624##########

class pp_VAN_EX1_624(Preset_Play):
	""" Holy Fire
	Deal $5 damage. Restore #5 Health to your hero. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_624", self.controller)
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


##########VAN_EX1_625##########

class pp_VAN_EX1_625(Preset_Play):
	""" Shadowform
	Your Hero Power becomes 'Deal 2 damage.' If already in Shadowform: 3 damage. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_625", self.controller)
		self.mark2=self.exchange_card("VAN_EX1_625", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.activate_heropower(target=self.opponent.hero)
		self.asserting(self.opponent.hero.damage==2,"self.opponent.hero.damage==2")
		self.play_card(self.mark2)
		self.activate_heropower(target=self.opponent.hero)
		self.asserting(self.opponent.hero.damage==2+3,"self.opponent.hero.damage==2+3")
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########VAN_EX1_626##########

class pp_VAN_EX1_626(Preset_Play):
	""" Mass Dispel
	[Silence] all enemy minions. Draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_626", self.controller)
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


##########VAN_EX1_tk31##########

class pp_VAN_EX1_tk31(Preset_Play):
	""" Mind Controlling
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_tk31", self.controller)
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







