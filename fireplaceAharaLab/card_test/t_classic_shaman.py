from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity

def classic_shaman():

	#PresetGame(pp_VAN_CS2_037)##
	PresetGame(pp_VAN_CS2_038)##
	#PresetGame(pp_VAN_CS2_039)##
	#PresetGame(pp_VAN_CS2_041)##
	#PresetGame(pp_VAN_CS2_042)##
	#PresetGame(pp_VAN_CS2_045)##
	#PresetGame(pp_VAN_CS2_046)##
	#PresetGame(pp_VAN_CS2_050)##
	#PresetGame(pp_VAN_CS2_051)##
	PresetGame(pp_VAN_CS2_052)##
	#PresetGame(pp_VAN_CS2_053)##
	#PresetGame(pp_VAN_EX1_238)##
	#PresetGame(pp_VAN_EX1_241)##
	#PresetGame(pp_VAN_EX1_243)##
	#PresetGame(pp_VAN_EX1_244)##
	#PresetGame(pp_VAN_EX1_245)##
	#PresetGame(pp_VAN_EX1_246)##
	#PresetGame(pp_VAN_EX1_247)##
	#PresetGame(pp_VAN_EX1_248)##
	#PresetGame(pp_VAN_EX1_250)##
	PresetGame(pp_VAN_EX1_251)##
	#PresetGame(pp_VAN_EX1_258)##
	PresetGame(pp_VAN_EX1_259)##
	#PresetGame(pp_VAN_EX1_565)##
	#PresetGame(pp_VAN_EX1_567)##
	#PresetGame(pp_VAN_EX1_575)##
	#PresetGame(pp_VAN_EX1_587)##
	#PresetGame(pp_VAN_EX1_tk11)##
	#PresetGame(pp_VAN_HERO_02bp)##
	#PresetGame(pp_VAN_HERO_02e2)##
	#PresetGame(pp_VAN_NEW1_009)##
	#PresetGame(pp_VAN_NEW1_010)##


##########VAN_CS2_037##########

class pp_VAN_CS2_037(Preset_Play):
	""" Frost Shock
	Deal $1 damage to an enemy character and [Freeze] it. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_037", self.controller)
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


##########VAN_CS2_038##########

class pp_VAN_CS2_038(Preset_Play):
	""" Ancestral Spirit
	Choose a minion. When that minion is destroyed, return it to the battlefield. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_038", self.controller)
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


##########VAN_CS2_039##########

class pp_VAN_CS2_039(Preset_Play):
	""" Windfury
	Give a minion [Windfury]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_039", self.controller)
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


##########VAN_CS2_041##########

class pp_VAN_CS2_041(Preset_Play):
	""" Ancestral Healing
	Restore a minionto full Health andgive it [Taunt]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_041", self.controller)
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


##########VAN_CS2_042##########

class pp_VAN_CS2_042(Preset_Play):
	""" Fire Elemental
	[Battlecry:] Deal 3 damage. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_042", self.controller)
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


##########VAN_CS2_045##########

class pp_VAN_CS2_045(Preset_Play):
	""" Rockbiter Weapon
	Give a friendly character +3 Attack this turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_045", self.controller)
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


##########VAN_CS2_046##########

class pp_VAN_CS2_046(Preset_Play):
	""" Bloodlust
	Give your minions +3_Attack this turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_046", self.controller)
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


##########VAN_CS2_050##########

class pp_VAN_CS2_050(Preset_Play):
	""" Searing Totem
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_050", self.controller)
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


##########VAN_CS2_051##########

class pp_VAN_CS2_051(Preset_Play):
	""" Stoneclaw Totem
	[Taunt] """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_051", self.controller)
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


##########VAN_CS2_052##########

class pp_VAN_CS2_052(Preset_Play):
	""" Wrath of Air Totem
	[Spell Damage +1] """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_052", self.controller)
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


##########VAN_CS2_053##########

class pp_VAN_CS2_053(Preset_Play):
	""" Far Sight
	Draw a card. That card costs (3) less. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_053", self.controller)
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


##########VAN_EX1_238##########

class pp_VAN_EX1_238(Preset_Play):
	""" Lightning Bolt
	Deal $3 damage. [Overload:] (1) """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_238", self.controller)
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


##########VAN_EX1_241##########

class pp_VAN_EX1_241(Preset_Play):
	""" Lava Burst
	Deal $5 damage. [Overload:] (2) """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_241", self.controller)
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


##########VAN_EX1_243##########

class pp_VAN_EX1_243(Preset_Play):
	""" Dust Devil
	[Windfury]. [Overload:] (2) """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_243", self.controller)
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


##########VAN_EX1_244##########

class pp_VAN_EX1_244(Preset_Play):
	""" Totemic Might
	Give your Totems +2_Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_244", self.controller)
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


##########VAN_EX1_245##########

class pp_VAN_EX1_245(Preset_Play):
	""" Earth Shock
	[Silence] a minion, then deal $1 damage to it. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_245", self.controller)
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


##########VAN_EX1_246##########

class pp_VAN_EX1_246(Preset_Play):
	""" Hex
	Transform a minion into a 0/1 Frog with [Taunt]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_246", self.controller)
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


##########VAN_EX1_247##########

class pp_VAN_EX1_247(Preset_Play):
	""" Stormforged Axe
	[Overload:] (1) """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_247", self.controller)
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


##########VAN_EX1_248##########

class pp_VAN_EX1_248(Preset_Play):
	""" Feral Spirit
	Summon two 2/3 Spirit Wolves with [Taunt]. [Overload:] (2) """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_248", self.controller)
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


##########VAN_EX1_250##########

class pp_VAN_EX1_250(Preset_Play):
	""" Earth Elemental
	[Taunt]. [[Overload]:] (3) """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_250", self.controller)
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


##########VAN_EX1_251##########

class pp_VAN_EX1_251(Preset_Play):
	""" Forked Lightning
	Deal $2 damage to 2_random enemy minions. [Overload:] (2) """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_251", self.controller)
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


##########VAN_EX1_258##########

class pp_VAN_EX1_258(Preset_Play):
	""" Unbound Elemental
	Whenever you play a card_with [Overload], gain_+1/+1. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_258", self.controller)
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


##########VAN_EX1_259##########

class pp_VAN_EX1_259(Preset_Play):
	""" Lightning Storm
	Deal $2-$3 damage to all enemy minions. [Overload:] (2) """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_259", self.controller)
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


##########VAN_EX1_565##########

class pp_VAN_EX1_565(Preset_Play):
	""" Flametongue Totem
	Adjacent minions have +2_Attack. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_565", self.controller)
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


##########VAN_EX1_567##########

class pp_VAN_EX1_567(Preset_Play):
	""" Doomhammer
	[Windfury, Overload:] (2) """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_567", self.controller)
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


##########VAN_EX1_575##########

class pp_VAN_EX1_575(Preset_Play):
	""" Mana Tide Totem
	At the end of your turn, draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_575", self.controller)
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


##########VAN_EX1_587##########

class pp_VAN_EX1_587(Preset_Play):
	""" Windspeaker
	[Battlecry:] Give a friendly minion [Windfury]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_587", self.controller)
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


##########VAN_EX1_tk11##########

class pp_VAN_EX1_tk11(Preset_Play):
	""" Spirit Wolf
	[Taunt] """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_tk11", self.controller)
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


##########VAN_HERO_02bp##########

class pp_VAN_HERO_02bp(Preset_Play):
	""" Totemic Call
	[Hero Power]Summon a random Totem. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_HERO_02bp", self.controller)
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


##########VAN_HERO_02e2##########

class pp_VAN_HERO_02e2(Preset_Play):
	""" Strength of Earth
	+1 Attack. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_HERO_02e2", self.controller)
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


##########VAN_NEW1_009##########

class pp_VAN_NEW1_009(Preset_Play):
	""" Healing Totem
	At the end of your turn, restore #1 Health to all friendly minions. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_NEW1_009", self.controller)
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


##########VAN_NEW1_010##########

class pp_VAN_NEW1_010(Preset_Play):
	""" Al'Akir the Windlord
	[Charge, Divine Shield, Taunt, Windfury] """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_NEW1_010", self.controller)
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


