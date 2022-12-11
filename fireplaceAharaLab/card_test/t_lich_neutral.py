from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def lich_neutral():

	#PresetGame(pp_RLK_018t)##
	#PresetGame(pp_RLK_029)##
	#PresetGame(pp_RLK_070)##
	#PresetGame(pp_RLK_104)##
	#PresetGame(pp_RLK_113)##
	#PresetGame(pp_RLK_117)##
	#PresetGame(pp_RLK_119)##
	#PresetGame(pp_RLK_123)##
	#PresetGame(pp_RLK_218)##
	#PresetGame(pp_RLK_219)##
	#PresetGame(pp_RLK_220)##
	#PresetGame(pp_RLK_221)##
	#PresetGame(pp_RLK_222)##
	#PresetGame(pp_RLK_518)##
	#PresetGame(pp_RLK_590)##
	#PresetGame(pp_RLK_591)##
	#PresetGame(pp_RLK_592)##
	#PresetGame(pp_RLK_593)##
	#PresetGame(pp_RLK_653)##
	#PresetGame(pp_RLK_677)##
	#PresetGame(pp_RLK_824)##
	#PresetGame(pp_RLK_826e)##
	#PresetGame(pp_RLK_830)##
	#PresetGame(pp_RLK_831)##
	#PresetGame(pp_RLK_833)##
	#PresetGame(pp_RLK_834)##
	#PresetGame(pp_RLK_867)##
	#PresetGame(pp_RLK_900)##
	#PresetGame(pp_RLK_914)##
	#PresetGame(pp_RLK_915)##
	#PresetGame(pp_RLK_926)##
	#PresetGame(pp_RLK_950)##
	#PresetGame(pp_RLK_951)##
	#PresetGame(pp_RLK_952)##
	#PresetGame(pp_RLK_955)##
	#PresetGame(pp_RLK_957)##
	#PresetGame(pp_RLK_970)##
	pass


##########RLK_018t##########

class pp_RLK_018t(Preset_Play):
	""" Rampaging Zombie
	<b>Rush</b> """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_018t", self.controller)
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


##########RLK_029##########

class pp_RLK_029(Preset_Play):
	""" Shatterskin Gargoyle
	<b>Taunt</b> <b>Deathrattle:</b> Deal 4 damage to a random enemy. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_029", self.controller)
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


##########RLK_070##########

class pp_RLK_070(Preset_Play):
	""" Infected Peasant
	<b>Deathrattle:</b> Summon a 2/2 Undead Peasant. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_070", self.controller)
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


##########RLK_104##########

class pp_RLK_104(Preset_Play):
	""" Street Sweeper
	<b>Battlecry:</b> Deal 2 damage to all other minions. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_104", self.controller)
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


##########RLK_113##########

class pp_RLK_113(Preset_Play):
	""" Brittleskin Zombie
	<b>Deathrattle:</b> If it's your opponent's turn, deal 3 damage to them. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_113", self.controller)
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


##########RLK_117##########

class pp_RLK_117(Preset_Play):
	""" Incorporeal Corporal
	After this minion attacks, destroy it. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_117", self.controller)
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


##########RLK_119##########

class pp_RLK_119(Preset_Play):
	""" Drakkari Embalmer
	<b>Battlecry:</b> Give a friendly Undead <b>Reborn</b>. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_119", self.controller)
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


##########RLK_123##########

class pp_RLK_123(Preset_Play):
	""" Bone Flinger
	<b>Battlecry:</b> If a friendly Undead died after your last turn, deal 2 damage. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_123", self.controller)
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


##########RLK_218##########

class pp_RLK_218(Preset_Play):
	""" Silvermoon Arcanist
	<b>Spell Damage +2</b> <b>Battlecry:</b> Your spells canÅft target heroes this turn. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_218", self.controller)
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


##########RLK_219##########

class pp_RLK_219(Preset_Play):
	""" Sunfury Clergy
	<b>Battlecry:</b> Restore 3 Health to all friendly characters. <b>Manathirst (6):</b> Restore 6 Health instead. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_219", self.controller)
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


##########RLK_220##########

class pp_RLK_220(Preset_Play):
	""" Tenacious San'layn
	<b>Lifesteal</b> Whenever this attacks, deal 2 damage to the enemy hero. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_220", self.controller)
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


##########RLK_221##########

class pp_RLK_221(Preset_Play):
	""" Crystal Broker
	<b>Manathirst (5):</b> Summon a random 3-Cost minion. <b>Manathirst (10):</b> Summon an 8-Cost minion instead. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_221", self.controller)
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


##########RLK_222##########

class pp_RLK_222(Preset_Play):
	""" Astalor Bloodsworn
	<b>Battlecry:</b> Add Astalor, the Protector to your hand. <b>Manathirst (@):</b> Deal 2 damage. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_222", self.controller)
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


##########RLK_518##########

class pp_RLK_518(Preset_Play):
	""" Silvermoon Sentinel
	<b>Taunt</b> <b>Manathirst (@):</b> Gain +2/+2 and <b>Divine Shield</b>. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_518", self.controller)
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


##########RLK_590##########

class pp_RLK_590(Preset_Play):
	""" The Sunwell
	Fill your hand with random spells. Costs (1) less for each other card in your hand. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_590", self.controller)
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


##########RLK_591##########

class pp_RLK_591(Preset_Play):
	""" Bonelord Frostwhisper
	<b>Deathrattle:</b> For the rest of the game, your first card each turn costs (0). You die in 3 turns. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_591", self.controller)
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


##########RLK_592##########

class pp_RLK_592(Preset_Play):
	""" Invincible
	<b>Reborn</b> <b>Battlecry and Deathrattle:</b> Give a random friendly Undead +5/+5 and <b>Taunt</b>. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_592", self.controller)
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


##########RLK_593##########

class pp_RLK_593(Preset_Play):
	""" Lor'themar Theron
	<b>Battlecry:</b> Double the stats of all minions in your deck. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_593", self.controller)
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


##########RLK_653##########

class pp_RLK_653(Preset_Play):
	""" Infectious Ghoul
	<b>Deathrattle:</b> Give a random friendly minion "<b>Deathrattle:</b> Summon an Infectious Ghoul." """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_653", self.controller)
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


##########RLK_677##########

class pp_RLK_677(Preset_Play):
	""" Sanctum Spellbender
	Whenever your opponent targets another minion with a spell, redirect it to this. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_677", self.controller)
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


##########RLK_824##########

class pp_RLK_824(Preset_Play):
	""" Arms Dealer
	After you summon an Undead, give it +1 Attack. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_824", self.controller)
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


##########RLK_826e##########

class pp_RLK_826e(Preset_Play):
	""" Silvermoon Farstrider Spellpower
	<b>Spell Damage +1</b>. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_826e", self.controller)
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


##########RLK_830##########

class pp_RLK_830(Preset_Play):
	""" Flesh Behemoth
	<b>Taunt</b> <b>Deathrattle:</b> Draw another Undead and summon a copy of it. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_830", self.controller)
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


##########RLK_831##########

class pp_RLK_831(Preset_Play):
	""" Plaguespreader
	<b>Deathrattle:</b> Transform a random minion in your opponent's hand into a Plaguespreader. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_831", self.controller)
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


##########RLK_833##########

class pp_RLK_833(Preset_Play):
	""" Foul Egg
	<b>Deathrattle:</b> Summon a 3/3 Undead Chicken. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_833", self.controller)
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


##########RLK_834##########

class pp_RLK_834(Preset_Play):
	""" Nerubian Vizier
	<b>Battlecry:</b> <b>Discover</b> a spell. If a friendly Undead died after your last turn, it costs (2) less. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_834", self.controller)
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


##########RLK_867##########

class pp_RLK_867(Preset_Play):
	""" Vrykul Necrolyte
	<b>Battlecry:</b> Give a friendly minion "<b>Deathrattle:</b> Summon a 2/2 Zombie with <b>Rush</b>." """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_867", self.controller)
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


##########RLK_900##########

class pp_RLK_900(Preset_Play):
	""" Scourge Rager
	<b>Reborn</b> <b>Battlecry:</b> Die. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_900", self.controller)
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


##########RLK_914##########

class pp_RLK_914(Preset_Play):
	""" Umbral Geist
	<b>Deathrattle:</b> Add a random Shadow spell to your hand. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_914", self.controller)
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


##########RLK_915##########

class pp_RLK_915(Preset_Play):
	""" Amber Whelp
	<b>Battlecry:</b> If you're holding a Dragon, deal 3 damage. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_915", self.controller)
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


##########RLK_926##########

class pp_RLK_926(Preset_Play):
	""" Bloodied Knight
	At the end of your turn, deal 2 damage to your hero. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_926", self.controller)
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


##########RLK_950##########

class pp_RLK_950(Preset_Play):
	""" Translocation Instructor
	<b>Battlecry:</b> Choose an enemy minion. Swap it with a random one in their deck. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_950", self.controller)
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


##########RLK_951##########

class pp_RLK_951(Preset_Play):
	""" Coroner
	<b>Battlecry:</b> <b>Freeze</b> an enemy minion. <b>Manathirst (6):</b> <b>Silence</b> it first. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_951", self.controller)
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


##########RLK_952##########

class pp_RLK_952(Preset_Play):
	""" Enchanter
	Enemy minions take double damage during your turn. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_952", self.controller)
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


##########RLK_955##########

class pp_RLK_955(Preset_Play):
	""" Silvermoon Armorer
	<b>Rush</b> <b>Manathirst (@):</b> Gain +2/+2. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_955", self.controller)
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


##########RLK_957##########

class pp_RLK_957(Preset_Play):
	""" Banshee
	<b>Deathrattle:</b> Give a random friendly Undead +2/+1. """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_957", self.controller)
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


##########RLK_970##########

class pp_RLK_970(Preset_Play):
	""" Hawkstrider Rancher
	After you play a minion, give it +1/+1 and "<b>Deathrattle:</b> Summon a 1/1 Hawkstrider." """
	class1=CardClass.NEUTRAL
	class2=CardClass.NEUTRAL
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_970", self.controller)
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


