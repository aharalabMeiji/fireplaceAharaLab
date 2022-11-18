from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity

def classic_paladin():

	#PresetGame(pp_VAN_CS2_087)##
	#PresetGame(pp_VAN_CS2_088)##
	#PresetGame(pp_VAN_CS2_089)##
	#PresetGame(pp_VAN_CS2_091)##
	#PresetGame(pp_VAN_CS2_092)##
	#PresetGame(pp_VAN_CS2_093)##
	#PresetGame(pp_VAN_CS2_094)##
	#PresetGame(pp_VAN_CS2_097)##
	#PresetGame(pp_VAN_CS2_101t)##
	#PresetGame(pp_VAN_EX1_130)##
	#PresetGame(pp_VAN_EX1_132)##
	#PresetGame(pp_VAN_EX1_136)##
	#PresetGame(pp_VAN_EX1_349)##
	#PresetGame(pp_VAN_EX1_354)##
	#PresetGame(pp_VAN_EX1_355)##
	#PresetGame(pp_VAN_EX1_360)##
	#PresetGame(pp_VAN_EX1_362)##
	#PresetGame(pp_VAN_EX1_363)##
	#PresetGame(pp_VAN_EX1_365)##
	#PresetGame(pp_VAN_EX1_366)##
	#PresetGame(pp_VAN_EX1_371)##
	#PresetGame(pp_VAN_EX1_379)##
	#PresetGame(pp_VAN_EX1_382)##
	#PresetGame(pp_VAN_EX1_383)##
	#PresetGame(pp_VAN_EX1_384)##
	#PresetGame(pp_VAN_EX1_619)##
	#PresetGame(pp_VAN_HERO_04bp)##


##########VAN_CS2_087##########

class pp_VAN_CS2_087(Preset_Play):
	""" Blessing of Might
	Give a minion +3_Attack. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_087", self.controller)
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


##########VAN_CS2_088##########

class pp_VAN_CS2_088(Preset_Play):
	""" Guardian of Kings
	[Battlecry:] Restore #6 Health to your hero. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_088", self.controller)
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


##########VAN_CS2_089##########

class pp_VAN_CS2_089(Preset_Play):
	""" Holy Light
	Restore #6 Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_089", self.controller)
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


##########VAN_CS2_091##########

class pp_VAN_CS2_091(Preset_Play):
	""" Light's Justice
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_091", self.controller)
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


##########VAN_CS2_092##########

class pp_VAN_CS2_092(Preset_Play):
	""" Blessing of Kings
	Give a minion +4/+4. <i>(+4 Attack/+4 Health)</i> """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_092", self.controller)
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


##########VAN_CS2_093##########

class pp_VAN_CS2_093(Preset_Play):
	""" Consecration
	Deal $2 damage to all enemies. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_093", self.controller)
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


##########VAN_CS2_094##########

class pp_VAN_CS2_094(Preset_Play):
	""" Hammer of Wrath
	Deal $3 damage.Draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_094", self.controller)
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


##########VAN_CS2_097##########

class pp_VAN_CS2_097(Preset_Play):
	""" Truesilver Champion
	Whenever your hero attacks, restore #2_Health to it. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_097", self.controller)
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


##########VAN_CS2_101t##########

class pp_VAN_CS2_101t(Preset_Play):
	""" Silver Hand Recruit
	 """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_CS2_101t", self.controller)
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


##########VAN_EX1_130##########

class pp_VAN_EX1_130(Preset_Play):
	""" Noble Sacrifice
	[Secret:] When an enemy attacks, summon a 2/1 Defender as the new target. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_130", self.controller)
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


##########VAN_EX1_132##########

class pp_VAN_EX1_132(Preset_Play):
	""" Eye for an Eye
	[Secret:] When your hero takes damage, deal_that much damage to the enemy hero. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_132", self.controller)
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


##########VAN_EX1_136##########

class pp_VAN_EX1_136(Preset_Play):
	""" Redemption
	[Secret:] When a friendly minion dies, return it to life with 1 Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_136", self.controller)
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


##########VAN_EX1_349##########

class pp_VAN_EX1_349(Preset_Play):
	""" Divine Favor
	Draw cards until you have as many in hand as your opponent. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_349", self.controller)
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


##########VAN_EX1_354##########

class pp_VAN_EX1_354(Preset_Play):
	""" Lay on Hands
	Restore #8 Health. Draw_3 cards. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_354", self.controller)
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


##########VAN_EX1_355##########

class pp_VAN_EX1_355(Preset_Play):
	""" Blessed Champion
	Double a minion's Attack. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_355", self.controller)
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


##########VAN_EX1_360##########

class pp_VAN_EX1_360(Preset_Play):
	""" Humility
	Change a minion's Attack to 1. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_360", self.controller)
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


##########VAN_EX1_362##########

class pp_VAN_EX1_362(Preset_Play):
	""" Argent Protector
	[Battlecry:] Give a friendly minion [Divine Shield]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_362", self.controller)
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


##########VAN_EX1_363##########

class pp_VAN_EX1_363(Preset_Play):
	""" Blessing of Wisdom
	Choose a minion. Whenever it attacks, draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_363", self.controller)
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


##########VAN_EX1_365##########

class pp_VAN_EX1_365(Preset_Play):
	""" Holy Wrath
	Draw a card and deal_damage equal to_its Cost. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_365", self.controller)
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


##########VAN_EX1_366##########

class pp_VAN_EX1_366(Preset_Play):
	""" Sword of Justice
	After you summon a minion, give it +1/+1 and this loses 1_Durability. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_366", self.controller)
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


##########VAN_EX1_371##########

class pp_VAN_EX1_371(Preset_Play):
	""" Hand of Protection
	Give a minion [Divine Shield]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_371", self.controller)
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


##########VAN_EX1_379##########

class pp_VAN_EX1_379(Preset_Play):
	""" Repentance
	[Secret:] After your opponent plays a minion, reduce its Health to 1. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_379", self.controller)
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


##########VAN_EX1_382##########

class pp_VAN_EX1_382(Preset_Play):
	""" Aldor Peacekeeper
	[Battlecry:] Change an_enemy minion's Attack to 1. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_382", self.controller)
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


##########VAN_EX1_383##########

class pp_VAN_EX1_383(Preset_Play):
	""" Tirion Fordring
	[[Divine Shield],] [Taunt] [Deathrattle:] Equip a 5/3_Ashbringer. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_383", self.controller)
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


##########VAN_EX1_384##########

class pp_VAN_EX1_384(Preset_Play):
	""" Avenging Wrath
	Deal $8 damage randomly split among all enemy characters. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_384", self.controller)
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


##########VAN_EX1_619##########

class pp_VAN_EX1_619(Preset_Play):
	""" Equality
	Change the Health of ALL minions to 1. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_EX1_619", self.controller)
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


##########VAN_HERO_04bp##########

class pp_VAN_HERO_04bp(Preset_Play):
	""" Reinforce
	[Hero Power]Summon a 1/1 Silver Hand Recruit. """
	def preset_deck(self):
		self.mark1=self.exchange_card("VAN_HERO_04bp", self.controller)
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


