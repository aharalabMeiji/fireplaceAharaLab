from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity, CardClass

def stormwind_rogue():
	#PresetGame(pp_DED_004)##
	#PresetGame(pp_DED_005)##
	#PresetGame(pp_DED_510)##
	#PresetGame(pp_SW_050)##
	#PresetGame(pp_SW_052)##
	#PresetGame(pp_SW_310)##  OK
	#PresetGame(pp_SW_311x)##  OK
	#PresetGame(pp_SW_311y)##  OK
	#PresetGame(pp_SW_405)##
	#PresetGame(pp_SW_411)##
	#PresetGame(pp_SW_412)##
	#PresetGame(pp_SW_413)##
	PresetGame(pp_SW_417_1)##
	PresetGame(pp_SW_417_2)##
	#PresetGame(pp_SW_434)##
	pass

##########DED_004##########

class pp_DED_004(Preset_Play):
	""" Blackwater Cutlass
	[Tradeable]After you [Trade] this,reduce the cost of a spellin your hand by (1). """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_004", self.controller)
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


##########DED_005##########

class pp_DED_005(Preset_Play):
	""" Parrrley
	Swap this for a card in your opponent's deck. """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_005", self.controller)
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


##########DED_510##########

class pp_DED_510(Preset_Play):
	""" Edwin, Defias Kingpin
	[Battlecry:] Draw a card. If youplay it this turn, gain +2/+2and repeat this effect. """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_510", self.controller)
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


##########Story_10_WardensDetermination##########

class pp_Story_10_WardensDetermination(Preset_Play):
	""" Warden's Determination
	Give +2/+2 to all minions in your hand, deck, and battlefield. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_10_WardensDetermination", self.controller)
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


##########Story_10_WardensGlaive##########

class pp_Story_10_WardensGlaive(Preset_Play):
	""" Warden's Glaive
	If this kills an enemy minion, adjacent minions go [Dormant] for 2 turns. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_10_WardensGlaive", self.controller)
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


##########Story_11_ParrrleyPuzzle##########

class pp_Story_11_ParrrleyPuzzle(Preset_Play):
	""" Parrrley
	Swap this for a card in your opponent's deck. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_ParrrleyPuzzle", self.controller)
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


##########SW_050##########

class pp_SW_050(Preset_Play):
	""" Maestra of the Masquerade
	You start the game as a different class until you play a Rogue card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_050", self.controller)
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


##########SW_052##########

class pp_SW_052(Preset_Play):
	""" Find the Imposter
	[Questline:] Play 2SI:7 cards.[Reward:] Add a Spy Gizmo to your hand. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_052", self.controller)
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


##########SW_310##########

class pp_SW_310(Preset_Play):
	""" Counterfeit Blade
	[Battlecry:] Gain a randomfriendly [Deathrattle] that_triggered this game. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_310", self.controller)
		self.mark2=self.exchange_card("deathrattle", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark2)
		self.change_turn()
		### opp
		Hit(self.mark2,10).trigger(self.opponent)
		self.change_turn()
		### con
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.mark1.deathrattles!=[], "deathrattle"
		print(self.mark2.deathrattles[0])
		print(self.mark1.deathrattles[0])
		print('visually check whether these two actions coinside.')
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########SW_311##########

class pp_SW_311x(Preset_Play):
	""" Garrote
	Deal $2 damage to theenemy hero. Shuffle 2Bleeds into your deck thatdeal $2 more when drawn. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_311", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
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
		assert self.opponent.hero.health==30-2, "health"
		cards = [card for card in self.controller.deck if card.id=='SW_311t']
		assert len(cards)==2, "deck"
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_SW_311y(Preset_Play):
	""" Garrote
	Deal $2 damage to theenemy hero. Shuffle 2Bleeds into your deck thatdeal $2 more when drawn. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_311", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		Give(self.controller, 'SW_311t').trigger(self.controller)
		#self.change_turn()
		### opp
		#self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.opponent.hero.health==30-2, "health"
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########SW_405##########

class pp_SW_405(Preset_Play):
	""" Sketchy Information
	Draw a [Deathrattle] cardthat costs (4) or less.Trigger its [Deathrattle.] """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_405", self.controller)
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


##########SW_411##########

class pp_SW_411(Preset_Play):
	""" SI:7 Informant
	[Battlecry:] Gain +1/+1 for each other SI:7 card you've played this game. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_411", self.controller)
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


##########SW_412##########

class pp_SW_412(Preset_Play):
	""" SI:7 Extortion
	[Tradeable]Deal $3 damage to an undamaged character. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_412", self.controller)
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


##########SW_413##########

class pp_SW_413(Preset_Play):
	""" SI:7 Operative
	[Rush]After this attacks a minion, gain [Stealth]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_413", self.controller)
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


##########SW_417##########

class pp_SW_417_1(Preset_Play):
	""" SI:7 Assassin
	Costs (1) less for each SI:7card you've played this game.[Combo:] Destroy an enemy minion. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_417", self.controller)
		self.mark2=self.exchange_card("SI7", self.controller)
		self.mark3=self.exchange_card("SI7", self.controller)
		self.mark4=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark2)
		self.play_card(self.mark1, target=self.mark4)
		#self.change_turn()
		### opp
		#self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.mark4.zone==Zone.GRAVEYARD, "death"
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_SW_417_2(Preset_Play):
	""" SI:7 Assassin
	Costs (1) less for each SI:7card you've played this game.[Combo:] Destroy an enemy minion. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.mark2=self.exchange_card("SI7", self.controller)
		self.mark1=self.exchange_card("SW_417", self.controller)
		self.mark3=self.exchange_card("SI7", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark2)
		self.play_card(self.mark3)
		self.change_turn()
		### opp
		Hit(self.mark3, 10).trigger(self.opponent)
		self.change_turn()
		assert self.mark1.cost==self.mark1.data.cost-2, "cost=%d"%(self.mark1.cost)
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########SW_434##########

class pp_SW_434(Preset_Play):
	""" Loan Shark
	[Battlecry:] Give youropponent a Coin.__[Deathrattle:] You get two. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_434", self.controller)
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


