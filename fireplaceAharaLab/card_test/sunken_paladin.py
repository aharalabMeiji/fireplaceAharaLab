from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity

def sunken_paladin():

	#PresetGame(pp_AIBot_PaladinTrainee_005_hb)##
	#PresetGame(pp_Story_11_AzsharanMoonPuzzle)##
	#PresetGame(pp_Story_11_BrightIdea)##
	#PresetGame(pp_Story_11_BubblebotPuzzle)##
	#PresetGame(pp_Story_11_ExplorersPride)##
	#PresetGame(pp_Story_11_Finley_009hp)##
	#PresetGame(pp_Story_11_Finley_1)##
	#PresetGame(pp_Story_11_Finley_2)##
	#PresetGame(pp_Story_11_Finley_3)##
	#PresetGame(pp_Story_11_FinleyPrologue)##
	#PresetGame(pp_Story_11_FinleysCompass)##
	#PresetGame(pp_Story_11_FinleysPithHelmet)##
	#PresetGame(pp_Story_11_FrontLines)##
	#PresetGame(pp_Story_11_LeviathansClawPuzzle)##
	#PresetGame(pp_Story_11_PowerUp)##
	#PresetGame(pp_Story_11_QuickFix)##
	#PresetGame(pp_Story_11_RadarDetector)##
	#PresetGame(pp_Story_11_SeafloorSaviorPuzzle)##
	#PresetGame(pp_Story_11_SecretsoftheSands)##
	#PresetGame(pp_Story_11_SplosiveSolutions)##
	#PresetGame(pp_Story_11_SupportBot)##
	#PresetGame(pp_Story_11_Swap)##
	#PresetGame(pp_Story_11_Valiance)##
	#PresetGame(pp_TID_077)##
	#PresetGame(pp_TID_098)##
	#PresetGame(pp_TID_949)##
	#PresetGame(pp_TSC_030)##
	#PresetGame(pp_TSC_032e3)##
	#PresetGame(pp_TSC_059)##
	#PresetGame(pp_TSC_060)##
	#PresetGame(pp_TSC_061)##
	#PresetGame(pp_TSC_074)##
	#PresetGame(pp_TSC_076)##
	#PresetGame(pp_TSC_079)##
	#PresetGame(pp_TSC_083)##
	#PresetGame(pp_TSC_644)##
	#PresetGame(pp_TSC_928e)##
	#PresetGame(pp_TSC_952)##


##########AIBot_PaladinTrainee_005_hb##########

class pp_AIBot_PaladinTrainee_005_hb(Preset_Play):
	""" Paladin Trainee
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("AIBot_PaladinTrainee_005_hb", self.controller)
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


##########Story_11_AzsharanMoonPuzzle##########

class pp_Story_11_AzsharanMoonPuzzle(Preset_Play):
	""" Azsharan Mooncatcher
	[Divine Shield]. [Battlecry:] Puta 'Sunken Mooncatcher' onthe bottom of your deck. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_AzsharanMoonPuzzle", self.controller)
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


##########Story_11_BrightIdea##########

class pp_Story_11_BrightIdea(Preset_Play):
	""" Bright Idea
	Gives Ini [Frenzy:] Add a Seafloor Savior to your hand. It costs (0). """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_BrightIdea", self.controller)
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


##########Story_11_BubblebotPuzzle##########

class pp_Story_11_BubblebotPuzzle(Preset_Play):
	""" Bubblebot
	[Battlecry:] Give your otherMechs [Divine Shield]and [Taunt]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_BubblebotPuzzle", self.controller)
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


##########Story_11_ExplorersPride##########

class pp_Story_11_ExplorersPride(Preset_Play):
	""" Explorer's Pride
	Add a random Paladin spell to your deck each turn. It will only last in your hand for 1 turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_ExplorersPride", self.controller)
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


##########Story_11_Finley_009hp##########

class pp_Story_11_Finley_009hp(Preset_Play):
	""" Sir Finley
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_Finley_009hp", self.controller)
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


##########Story_11_Finley_1##########

class pp_Story_11_Finley_1(Preset_Play):
	""" Sir Finley Mrrgglton
	[Battlecry:] [Discover] an ability.[Deathrattle:] Go [Dormant] for 2 turns. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_Finley_1", self.controller)
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


##########Story_11_Finley_2##########

class pp_Story_11_Finley_2(Preset_Play):
	""" Sir Finley Mrrgglton
	[Battlecry:] [Discover] an ability.[Deathrattle:] Go [Dormant] for 2 turns. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_Finley_2", self.controller)
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


##########Story_11_Finley_3##########

class pp_Story_11_Finley_3(Preset_Play):
	""" Sir Finley Mrrgglton
	[Battlecry:] [Discover] an ability.[Deathrattle:] Go [Dormant] for 2 turns. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_Finley_3", self.controller)
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


##########Story_11_FinleyPrologue##########

class pp_Story_11_FinleyPrologue(Preset_Play):
	""" Sir Finley Mrrgglton
	<i>This esteemed murloc relies on versatility and swapping cards to outsmart his foes.</i> """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_FinleyPrologue", self.controller)
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


##########Story_11_FinleysCompass##########

class pp_Story_11_FinleysCompass(Preset_Play):
	""" Finley's Compass
	Finley deals 1 damage to a random enemy minion for each friendly minion at the end of your turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_FinleysCompass", self.controller)
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


##########Story_11_FinleysPithHelmet##########

class pp_Story_11_FinleysPithHelmet(Preset_Play):
	""" Finley's Pith Helmet
	At the start of your turn, give all friendly minions +2 Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_FinleysPithHelmet", self.controller)
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


##########Story_11_FrontLines##########

class pp_Story_11_FrontLines(Preset_Play):
	""" Front Lines
	Summon a minion fromboth player's decks.Repeat until either sideof the battlefield is full. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_FrontLines", self.controller)
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


##########Story_11_LeviathansClawPuzzle##########

class pp_Story_11_LeviathansClawPuzzle(Preset_Play):
	""" The Leviathan's Claw
	[Rush], [Divine Shield]After this attacks,draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_LeviathansClawPuzzle", self.controller)
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


##########Story_11_PowerUp##########

class pp_Story_11_PowerUp(Preset_Play):
	""" Power Up!
	Give Finley [Divine Shield] and [Windfury]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_PowerUp", self.controller)
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


##########Story_11_QuickFix##########

class pp_Story_11_QuickFix(Preset_Play):
	""" Quick Fix
	Give Ini [Spellburst]: Throw a random weapon to your hand. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_QuickFix", self.controller)
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


##########Story_11_RadarDetector##########

class pp_Story_11_RadarDetector(Preset_Play):
	""" Radar Detector
	Scan the bottom 5 cardsof your deck. Draw anyMechs found this way,then shuffle your deck. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_RadarDetector", self.controller)
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


##########Story_11_SeafloorSaviorPuzzle##########

class pp_Story_11_SeafloorSaviorPuzzle(Preset_Play):
	""" Seafloor Savior
	[Battlecry:] [Dredge].If it's a minion, give itthis minion's Attackand Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_SeafloorSaviorPuzzle", self.controller)
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


##########Story_11_SecretsoftheSands##########

class pp_Story_11_SecretsoftheSands(Preset_Play):
	""" Secrets of the Sands
	Gives Finley [Battlecry:] Receive an upgraded hero power. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_SecretsoftheSands", self.controller)
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


##########Story_11_SplosiveSolutions##########

class pp_Story_11_SplosiveSolutions(Preset_Play):
	""" 'Splosive Solutions
	Give Ini a 50% chance to throw a bomb into the opponent's deck when they cast a spell. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_SplosiveSolutions", self.controller)
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


##########Story_11_SupportBot##########

class pp_Story_11_SupportBot(Preset_Play):
	""" Support Bot
	Gives Ini [Frenzy:] Add a Bubblebot to your hand. It costs (0). """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_SupportBot", self.controller)
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


##########Story_11_Swap##########

class pp_Story_11_Swap(Preset_Play):
	""" Swap
	Give Finley [Spellburst]: Add a Swap spell to your hand. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_Swap", self.controller)
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


##########Story_11_Valiance##########

class pp_Story_11_Valiance(Preset_Play):
	""" Valiance
	Gives Finley [Frenzy:] Summon a random murloc. """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_11_Valiance", self.controller)
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


##########TID_077##########

class pp_TID_077(Preset_Play):
	""" Lightray
	[Taunt]Costs (1) less for each Paladin card you've played this game. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TID_077", self.controller)
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


##########TID_098##########

class pp_TID_098(Preset_Play):
	""" Myrmidon
	After you cast a spell on this minion, draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TID_098", self.controller)
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


##########TID_949##########

class pp_TID_949(Preset_Play):
	""" Front Lines
	Summon a minionfrom each player's deck.Repeat until either sideof the battlefield is full. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TID_949", self.controller)
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


##########TSC_030##########

class pp_TSC_030(Preset_Play):
	""" The Leviathan
	[Colossal +1][Rush], [Divine Shield]After this attacks,[Dredge]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_030", self.controller)
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


##########TSC_032e3##########

class pp_TSC_032e3(Preset_Play):
	""" Blade Counter
	This [Counters] the next [Secretly] chosen minion or spell your opponent plays.@Okani will [Secretly] [Counter] the next minion your opponent plays.@Okani will [Secretly] [Counter] the next spell your opponent plays. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_032e3", self.controller)
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


##########TSC_059##########

class pp_TSC_059(Preset_Play):
	""" Bubblebot
	[Battlecry:] Give your otherMechs [Divine Shield]and [Taunt]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_059", self.controller)
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


##########TSC_060##########

class pp_TSC_060(Preset_Play):
	""" Shimmering Sunfish
	[Battlecry:] If you're holding a Holy Spell, gain [Taunt] and [Divine Shield]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_060", self.controller)
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


##########TSC_061##########

class pp_TSC_061(Preset_Play):
	""" The Garden's Grace
	Give a minion +5/+5 and[Divine Shield]. Costs (1) lessfor each Mana you've spenton Holy spells this game. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_061", self.controller)
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


##########TSC_074##########

class pp_TSC_074(Preset_Play):
	""" Kotori Lightblade
	After you cast a Holy spellon this, cast it again on__another friendly minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_074", self.controller)
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


##########TSC_076##########

class pp_TSC_076(Preset_Play):
	""" Immortalized in Stone
	Summon a 1/2, 2/4 and 4/8 Elemental with [Taunt]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_076", self.controller)
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


##########TSC_079##########

class pp_TSC_079(Preset_Play):
	""" Radar Detector
	Scan the bottom 5 cardsof your deck. Draw anyMechs found this way,then shuffle your deck. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_079", self.controller)
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


##########TSC_083##########

class pp_TSC_083(Preset_Play):
	""" Seafloor Savior
	[Battlecry:] [Dredge].If it's a minion, give itthis minion's Attackand Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_083", self.controller)
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


##########TSC_644##########

class pp_TSC_644(Preset_Play):
	""" Azsharan Mooncatcher
	[Divine Shield]. [Battlecry:] Puta 'Sunken Mooncatcher' onthe bottom of your deck. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_644", self.controller)
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


##########TSC_928e##########

class pp_TSC_928e(Preset_Play):
	""" Overclocked
	+1/+1. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_928e", self.controller)
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


##########TSC_952##########

class pp_TSC_952(Preset_Play):
	""" Holy Maki Roll
	Restore #2 Health. Repeatable this turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_952", self.controller)
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


