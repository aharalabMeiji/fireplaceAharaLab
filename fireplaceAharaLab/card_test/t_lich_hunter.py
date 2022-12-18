from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def lich_hunter():

	#PresetGame(pp_RLK_804)##
	#PresetGame(pp_RLK_817)##
	#PresetGame(pp_RLK_818)##
	#PresetGame(pp_RLK_819)##
	#PresetGame(pp_RLK_820)##
	#PresetGame(pp_RLK_821)##
	#PresetGame(pp_RLK_825)##
	#PresetGame(pp_RLK_826)##
	#PresetGame(pp_RLK_827)##
	#PresetGame(pp_RLK_828)##
	#PresetGame(pp_RLK_Prologue_804)##
	#PresetGame(pp_RLK_Prologue_Bow_003w)##
	#PresetGame(pp_RLK_Prologue_RLK_817)##
	#PresetGame(pp_RLK_Prologue_RLK_826)##
	#PresetGame(pp_RLK_Prologue_Sylvanas_003hb)##
	#PresetGame(pp_RLK_Prologue_Sylvanas_003p)##
	#PresetGame(pp_RLK_Prologue_SylvanasB_003hb2)##
	pass


##########RLK_804##########

class pp_RLK_804(Preset_Play):
	""" Conjured Arrow
	Deal $2 damage to a minion. <b>Manathirst (6):</b> Draw that many cards. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_804", self.controller)
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


##########RLK_817##########

class pp_RLK_817(Preset_Play):
	""" Arcane Quiver
	<b>Discover</b> a spell from your deck. If it's Arcane, give it <b>Spell Damage +1</b>. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_817", self.controller)
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


##########RLK_818##########

class pp_RLK_818(Preset_Play):
	""" Ricochet Shot
	Deal $1 damage to three random enemies. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_818", self.controller)
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


##########RLK_819##########

class pp_RLK_819(Preset_Play):
	""" Eversong Portal
	Summon $1 4/4 |4(Lynx, Lynxes) with <b>Rush</b> <i>(improved by <b>Spell Damage</b>)</i>. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_819", self.controller)
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


##########RLK_820##########

class pp_RLK_820(Preset_Play):
	""" Halduron Brightwing
	<b>Battlecry:</b> Give all Arcane spells in your deck <b>Spell Damage +1</b>. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_820", self.controller)
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


##########RLK_821##########

class pp_RLK_821(Preset_Play):
	""" Scourge Tamer
	<b>Battlecry:</b> Craft a custom Zombeast. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_821", self.controller)
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


##########RLK_825##########

class pp_RLK_825(Preset_Play):
	""" Shockspitter
	<b>Battlecry:</b> Deal @ damage. <i>(Improved by your hero attacks this game!)</i> """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_825", self.controller)
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


##########RLK_826##########

class pp_RLK_826(Preset_Play):
	""" Silvermoon Farstrider
	<b>Battlecry:</b> Give all Arcane spells in your hand <b>Spell Damage +1</b>. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_826", self.controller)
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


##########RLK_827##########

class pp_RLK_827(Preset_Play):
	""" Keeneye Spotter
	Whenever your hero attacks a minion, set its Health to 1. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_827", self.controller)
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


##########RLK_828##########

class pp_RLK_828(Preset_Play):
	""" Hope of Quel'Thalas
	After your hero attacks, give your minions +1/+1 <i>(wherever they are).</i> """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_828", self.controller)
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


##########RLK_Prologue_804##########

class pp_RLK_Prologue_804(Preset_Play):
	""" Conjured Arrow
	Deal $2 damage to a minion and draw 2 cards. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_804", self.controller)
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


##########RLK_Prologue_Bow_003w##########

class pp_RLK_Prologue_Bow_003w(Preset_Play):
	""" Windrunner's Bow
	After your hero attacks, summon two Silvermoon Sentinels. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_Bow_003w", self.controller)
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


##########RLK_Prologue_RLK_817##########

class pp_RLK_Prologue_RLK_817(Preset_Play):
	""" Arcane Quiver
	<b>Discover</b> a spell from your deck. If it's Arcane, give it <b>Spell Damage +1</b>. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_RLK_817", self.controller)
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


##########RLK_Prologue_RLK_826##########

class pp_RLK_Prologue_RLK_826(Preset_Play):
	""" Silvermoon Farstrider
	<b>Battlecry:</b> Give all Arcane spells in your hand <b>Spell Damage +1</b>. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_RLK_826", self.controller)
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


##########RLK_Prologue_Sylvanas_003hb##########

class pp_RLK_Prologue_Sylvanas_003hb(Preset_Play):
	""" Sylvanas Windrunner
	 """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_Sylvanas_003hb", self.controller)
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


##########RLK_Prologue_Sylvanas_003p##########

class pp_RLK_Prologue_Sylvanas_003p(Preset_Play):
	""" Quick Fire
	<b>Hero Power</b> Deal $1 damage to two random enemy minions. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_Sylvanas_003p", self.controller)
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


##########RLK_Prologue_SylvanasB_003hb2##########

class pp_RLK_Prologue_SylvanasB_003hb2(Preset_Play):
	""" Sylvanas Windrunner
	 """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_SylvanasB_003hb2", self.controller)
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


