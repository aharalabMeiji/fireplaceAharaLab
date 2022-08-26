from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity

def stormwind_priest():

	#PresetGame(pp_BOM_05_Bolvar_007p)##
	#PresetGame(pp_BOM_05_Xyrella_006e)##
	#PresetGame(pp_BOM_05_Xyrella_006hb)##
	#PresetGame(pp_BOM_05_Xyrella_006p)##
	#PresetGame(pp_BOM_07_Scabbs_Xyrella_008t)##
	#PresetGame(pp_DED_512)##
	#PresetGame(pp_DED_513)##
	#PresetGame(pp_DED_514)##
	#PresetGame(pp_Story_10_Tyrande)##
	#PresetGame(pp_SW_012)##
	#PresetGame(pp_SW_433)##
	#PresetGame(pp_SW_440)##
	#PresetGame(pp_SW_441)##
	#PresetGame(pp_SW_442)##
	#PresetGame(pp_SW_443)##
	#PresetGame(pp_SW_444)##
	#PresetGame(pp_SW_445)##
	#PresetGame(pp_SW_446)##
	#PresetGame(pp_SW_448)##


##########BOM_05_Bolvar_007p##########

class pp_BOM_05_Bolvar_007p(Preset_Play):
	""" For the Alliance!
	[Hero Power]Summon five minions from your deck. Give them +3 Health and [Taunt]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_Bolvar_007p", self.controller)
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


##########BOM_05_Xyrella_006e##########

class pp_BOM_05_Xyrella_006e(Preset_Play):
	""" Holy Empowerment
	Costs (2) less. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_Xyrella_006e", self.controller)
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


##########BOM_05_Xyrella_006hb##########

class pp_BOM_05_Xyrella_006hb(Preset_Play):
	""" Xyrella
	Xyrella sought knowledgeof the naaru's power, butfound Tamsin at StormwindCathedral instead. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_Xyrella_006hb", self.controller)
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


##########BOM_05_Xyrella_006p##########

class pp_BOM_05_Xyrella_006p(Preset_Play):
	""" Naaru's Light
	[Passive Hero Power]Your Holy Spellscost (2) less. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_05_Xyrella_006p", self.controller)
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


##########BOM_07_Scabbs_Xyrella_008t##########

class pp_BOM_07_Scabbs_Xyrella_008t(Preset_Play):
	""" Xyrella
	[Lifesteal][Deathrattle]: Return thisto your hand. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_07_Scabbs_Xyrella_008t", self.controller)
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


##########DED_512##########

class pp_DED_512(Preset_Play):
	""" Amulet of Undying
	[Tradeable]Resurrect @ friendly[Deathrattle] |4(minion, minions).<i>(Upgrades when [Traded]!)</i> """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_512", self.controller)
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


##########DED_513##########

class pp_DED_513(Preset_Play):
	""" Defias Leper
	[Battlecry:] If you're holdinga Shadow spell, deal2 damage. """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_513", self.controller)
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


##########DED_514##########

class pp_DED_514(Preset_Play):
	""" Copycat
	[Battlecry:] Add a copy of the next card your opponent plays to your hand. """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_514", self.controller)
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


##########Story_10_Tyrande##########

class pp_Story_10_Tyrande(Preset_Play):
	""" Tyrande Whisperwind
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("Story_10_Tyrande", self.controller)
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


##########SW_012##########

class pp_SW_012(Preset_Play):
	""" Shadowcloth Needle
	After you cast a Shadowspell, deal 1 damageto all enemies.Lose 1 Durability. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_012", self.controller)
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


##########SW_433##########

class pp_SW_433(Preset_Play):
	""" Seek Guidance
	[Questline:] Play a 2, 3,and 4-Cost card.[Reward:] [Discover] a cardfrom your deck. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_433", self.controller)
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


##########SW_440##########

class pp_SW_440(Preset_Play):
	""" Call of the Grave
	[Discover] a [Deathrattle]minion. If you haveenough Mana to play it,trigger its [Deathrattle]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_440", self.controller)
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


##########SW_441##########

class pp_SW_441(Preset_Play):
	""" Shard of the Naaru
	[Tradeable][Silence] all enemy minions. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_441", self.controller)
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


##########SW_442##########

class pp_SW_442(Preset_Play):
	""" Void Shard
	[Lifesteal]Deal $4 damage. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_442", self.controller)
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


##########SW_443##########

class pp_SW_443(Preset_Play):
	""" Elekk Mount
	Give a minion +4/+7 and [Taunt]. When it dies, summon an Elekk. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_443", self.controller)
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


##########SW_444##########

class pp_SW_444(Preset_Play):
	""" Twilight Deceptor
	[Battlecry:] If any hero took damage this turn, draw a Shadow spell. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_444", self.controller)
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


##########SW_445##########

class pp_SW_445(Preset_Play):
	""" Psyfiend
	After you cast a Shadow spell, deal 2 damage to each hero. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_445", self.controller)
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


##########SW_446##########

class pp_SW_446(Preset_Play):
	""" Voidtouched Attendant
	Both heroes take one extra damage from all sources. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_446", self.controller)
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


##########SW_448##########

class pp_SW_448(Preset_Play):
	""" Darkbishop Benedictus
	[Start of Game:] If the spells in your deck are all Shadow, enter Shadowform. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_448", self.controller)
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


