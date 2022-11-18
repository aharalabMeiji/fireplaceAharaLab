from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def stormwind_warlock():

	#PresetGame(pp_DED_503)##
	#PresetGame(pp_DED_504_1)## OK
	#PresetGame(pp_DED_504_2)## OK
	#PresetGame(pp_DED_505)##
	#PresetGame(pp_SW_003)##
	#PresetGame(pp_SW_084)##
	#PresetGame(pp_SW_085)##
	#PresetGame(pp_SW_086)##
	#PresetGame(pp_SW_087)##
	#PresetGame(pp_SW_088)##
	#PresetGame(pp_SW_089)##
	PresetGame(pp_SW_090)##
	#PresetGame(pp_SW_091)##
	#PresetGame(pp_SW_092)##
	pass

##########DED_503##########

class pp_DED_503(Preset_Play):
	""" Shadowblade Slinger
	[Battlecry:] If you've takendamage this turn, deal that_much to an enemy minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_503", self.controller)
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


##########DED_504##########

class pp_DED_504_1(Preset_Play):
	""" Wicked Shipment
	[Tradeable]Summon @ 1/1 |4(Imp, Imps).<i>(Upgrades by 2when [Traded]!)</i> """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK	
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_504", self.controller)
		#self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		#self.mark4=self.mark4[0][0]
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
		print("check if there is one Imp on the field.")
		cards = [card for card in self.controller.field if card.id=='EX1_598']
		assert len(cards)==1, "imp"
		for card in self.controller.field:
			self.print_stats("field", card)
	pass
class pp_DED_504_2(Preset_Play):
	""" Wicked Shipment
	[Tradeable]Summon @ 1/1 |4(Imp, Imps).<i>(Upgrades by 2when [Traded]!)</i> """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_504", self.controller)
		self.mark2=self.exchange_card("tradable", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.trade_card(self.mark2)
		self.play_card(self.mark1)
		#self.change_turn()
		### opp
		#self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		cards = [card for card in self.controller.field if card.id=='EX1_598']
		assert len(cards)==3, "imp"
		for card in self.controller.field:
			self.print_stats("field", card)
	pass

##########DED_505##########

class pp_DED_505(Preset_Play):
	""" Hullbreaker
	[Battlecry and Deathrattle:]Draw a spell. Your hero takesdamage equal to its Cost. """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_505", self.controller)
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


##########SW_003##########

class pp_SW_003(Preset_Play):
	""" Runed Mithril Rod
	After you draw 4 cards,reduce the Cost of cardsin your hand by (1).Lose 1 Durability. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_003", self.controller)
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


##########SW_084##########

class pp_SW_084(Preset_Play):
	""" Bloodbound Imp
	Whenever this attacks, deal 2 damage to your_hero. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_084", self.controller)
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


##########SW_085##########

class pp_SW_085(Preset_Play):
	""" Dark Alley Pact
	Summon a Fiendwith stats equal toyour hand size. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_085", self.controller)
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


##########SW_086##########

class pp_SW_086(Preset_Play):
	""" Shady Bartender
	[Tradeable][Battlecry:] Give your Demons +2/+2. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_086", self.controller)
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


##########SW_087##########

class pp_SW_087(Preset_Play):
	""" Dreaded Mount
	Give a minion +1/+1.When it dies, summonan endless Dreadsteed. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_087", self.controller)
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


##########SW_088##########

class pp_SW_088(Preset_Play):
	""" Demonic Assault
	Deal $3 damage.Summon two 1/3Voidwalkers with [Taunt]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_088", self.controller)
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


##########SW_089##########

class pp_SW_089(Preset_Play):
	""" Entitled Customer
	[Battlecry:] Deal damage equal to your hand size to all other minions. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_089", self.controller)
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


##########SW_090##########

class pp_SW_090(Preset_Play):
	""" Touch of the Nathrezim
	Deal $2 damage to a minion. If it dies, restore3 Health to your hero. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_090", self.controller)
		self.mark4=Summon(self.opponent, self.card_choice("minionH1")).trigger(self.opponent)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		Hit(self.controller.hero, 5).trigger(self.controller)
		self.play_card(self.mark1, target=self.mark4)
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########SW_091##########

class pp_SW_091(Preset_Play):
	""" The Demon Seed
	[Questline:] Take 8damage on your turns.[Reward:] [Lifesteal]. Deal $3damage to the enemy hero. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_091", self.controller)
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


##########SW_092##########

class pp_SW_092(Preset_Play):
	""" Anetheron
	Costs (1) if your hand is full. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_092", self.controller)
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


