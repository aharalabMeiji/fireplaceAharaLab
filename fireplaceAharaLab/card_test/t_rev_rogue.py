from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def rev_rogue():

	#PresetGame(pp_MAW_018)##
	#PresetGame(pp_MAW_019)##
	#PresetGame(pp_MAW_020)##
	#PresetGame(pp_REV_750)##
	#PresetGame(pp_REV_785)##
	#PresetGame(pp_REV_795)##
	#PresetGame(pp_REV_825)##
	#PresetGame(pp_REV_826)##
	#PresetGame(pp_REV_827)##
	PresetGame(pp_REV_828a)### OK
	#PresetGame(pp_REV_829)##
	#PresetGame(pp_REV_938)##
	#PresetGame(pp_REV_939)##
	#PresetGame(pp_REV_940)##
	#PresetGame(pp_REV_959)##
	pass


##########MAW_018##########

class pp_MAW_018(Preset_Play):
	""" Perjury
	<b>Secret:</b> When your turn starts, <b>Discover</b> and cast a <b>Secret</b> from another class. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_018", self.controller)
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


##########MAW_019##########

class pp_MAW_019(Preset_Play):
	""" Murder Accusation
	Choose a minion. Destroy it after another enemy minion dies. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_019", self.controller)
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


##########MAW_020##########

class pp_MAW_020(Preset_Play):
	""" Scribbling Stenographer
	<b>Rush</b>. Costs (1) less for each card you've played this turn. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_020", self.controller)
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


##########REV_750##########

class pp_REV_750(Preset_Play):
	""" Sinstone Graveyard
	Summon a @/@ <b>Stealthed</b> Ghost. <i>(Has +1/+1 for each other card you played this turn!)</i> """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_750", self.controller)
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


##########REV_785##########

class pp_REV_785(Preset_Play):
	""" Necrolord Draka
	{0} {1} {2} {3} """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_785", self.controller)
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


##########REV_795##########

class pp_REV_795(Preset_Play):
	""" Sinstone Graveyard
	{0} {1} """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_795", self.controller)
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


##########REV_825##########

class pp_REV_825(Preset_Play):
	""" Double Cross
	<b>Secret:</b> When your opponent spends all their Mana, draw two cards. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_825", self.controller)
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


##########REV_826##########

class pp_REV_826(Preset_Play):
	""" Private Eye
	<b>Battlecry:</b> Cast a <b>Secret</b> from your deck. _<b>Combo:</b> Cast 2 instead. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_826", self.controller)
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


##########REV_827##########

class pp_REV_827(Preset_Play):
	""" Sticky Situation
	<b>Secret:</b> After your opponent casts a spell, summon a 3/4 Spider with <b>Stealth</b>. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_827", self.controller)
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


##########REV_828##########

class pp_REV_828a(Preset_Play):
	""" Kidnap
	<b>Secret:</b> After your opponent plays a minion, stuff it in a 0/4 Sack. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_828", self.controller)
		#elf.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		#self.con4=self.con4[0][0]
		self.opp1=self.exchange_card(self.card_choice("minionH3"), self.opponent)
		#self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		for card in self.controller.secrets:
			self.print_stats("secrets", card)
		self.change_turn()
		### opp
		self.play_card(self.opp1)
		assert self.controller.secrets==[], 'secrets'
		assert self.opponent.field==[], 'opponent field'
		self.con2=self.controller.field[0]
		assert self.con2.id=='REV_828t', 'REV_828t'
		print(self.con2.script_data_text_0)
		Hit(self.con2, 4).trigger(self.opponent)
		#self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
		print("See controller has a kidnapped card in his hand from opponent.")
	pass


##########REV_829##########

class pp_REV_829(Preset_Play):
	""" Halkias
	<b>Stealth</b>. <b>Deathrattle:</b> Store Halkias's soul inside of a friendly <b>Secret</b>. It resummons Halkias when triggered. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_829", self.controller)
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


##########REV_938##########

class pp_REV_938(Preset_Play):
	""" Door of Shadows
	Draw a spell. <b>Infuse (@):</b> Add a temporary copy of it to your hand. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_938", self.controller)
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


##########REV_939##########

class pp_REV_939(Preset_Play):
	""" Serrated Bone Spike
	Deal $3 damage to a  minion. If it dies, your  next card this turn  costs (2) less. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_939", self.controller)
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


##########REV_940##########

class pp_REV_940(Preset_Play):
	""" Necrolord Draka
	<b>Battlecry:</b> Equip a @/3 Dagger.  <i>(+1 Attack for each other  card you played this turn!)</i> """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_940", self.controller)
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


##########REV_959##########

class pp_REV_959(Preset_Play):
	""" Ghastly Gravedigger
	<b>Battlecry:</b> If you control a <b>Secret</b>, choose a card in your opponent's hand to _shuffle into their deck. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_959", self.controller)
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


