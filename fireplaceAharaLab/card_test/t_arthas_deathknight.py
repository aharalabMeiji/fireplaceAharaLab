from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def arthas_deathknight():

	#PresetGame(pp_RLK_015)##
	#PresetGame(pp_RLK_018)##
	#PresetGame(pp_RLK_038)##
	#PresetGame(pp_RLK_042)##
	#PresetGame(pp_RLK_056)##
	#PresetGame(pp_RLK_057)##
	#PresetGame(pp_RLK_062)##
	#PresetGame(pp_RLK_063)##
	PresetGame(pp_RLK_066)##OK
	#PresetGame(pp_RLK_083)##
	#PresetGame(pp_RLK_086)##
	#PresetGame(pp_RLK_087)##
	#PresetGame(pp_RLK_110)##
	#PresetGame(pp_RLK_118)##
	#PresetGame(pp_RLK_122)##
	#PresetGame(pp_RLK_504)##
	#PresetGame(pp_RLK_505)##
	#PresetGame(pp_RLK_506t)##
	#PresetGame(pp_RLK_512)##
	#PresetGame(pp_RLK_516)##
	#PresetGame(pp_RLK_710e)##
	#PresetGame(pp_RLK_711)##
	#PresetGame(pp_RLK_712)##
	#PresetGame(pp_RLK_713)##
	#PresetGame(pp_RLK_730)##
	#PresetGame(pp_RLK_731)##
	#PresetGame(pp_RLK_740)##
	#PresetGame(pp_RLK_745)##

	pass


##########RLK_015##########

class pp_RLK_015(Preset_Play):
	""" Howling Blast
	Deal $3 damage to an enemy and <b>Freeze</b> it. Deal $1 damage to all other enemies. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_015", self.controller)
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


##########RLK_018##########

class pp_RLK_018(Preset_Play):
	""" Plague Strike
	Deal $3 damage to a minion. If that kills it, summon a 2/2 Zombie with <b>Rush</b>. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_018", self.controller)
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


##########RLK_038##########

class pp_RLK_038(Preset_Play):
	""" Icy Touch
	Deal $2 damage to an enemy and <b>Freeze</b> it. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_038", self.controller)
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


##########RLK_042##########

class pp_RLK_042(Preset_Play):
	""" Horn of Winter
	Refresh 2 Mana Crystals. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_042", self.controller)
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


##########RLK_056##########

class pp_RLK_056(Preset_Play):
	""" Unholy Frenzy
	Choose an enemy minion. Your minions attack it. Resummon any that die. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_056", self.controller)
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


##########RLK_057##########

class pp_RLK_057(Preset_Play):
	""" Dark Transformation
	Transform an Undead into a 4/5 Undead Monstrosity with <b>Rush</b>. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_057", self.controller)
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


##########RLK_062##########

class pp_RLK_062(Preset_Play):
	""" Nerubian Swarmguard
	<b>Taunt</b> <b>Battlecry:</b> Summon two copies of this minion. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_062", self.controller)
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


##########RLK_063##########

class pp_RLK_063(Preset_Play):
	""" Frostwyrm's Fury
	Deal $5 damage. <b>Freeze</b> all enemy minions. Summon a 5/5 Frostwyrm. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_063", self.controller)
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


##########RLK_066##########

class pp_RLK_066(Preset_Play):
	""" Hematurge
	<b>Battlecry:</b> Spend a <b>Corpse</b> to <b>Discover</b> a Blood Rune card. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_066", self.controller)
		self.controller.corpse=1
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.con2=self.choose_action()
		self.asserting2("self.con2.cost_blood>0")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_083##########

class pp_RLK_083(Preset_Play):
	""" Deathchiller
	After you cast a spell, deal 1 damage to two random enemies. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_083", self.controller)
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


##########RLK_086##########

class pp_RLK_086(Preset_Play):
	""" Frostmourne
	<b>Deathrattle:</b> Summon every minion killed by this weapon. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_086", self.controller)
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


##########RLK_087##########

class pp_RLK_087(Preset_Play):
	""" Asphyxiate
	Destroy the highest Attack enemy minion. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_087", self.controller)
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


##########RLK_110##########

class pp_RLK_110(Preset_Play):
	""" Ymirjar Frostbreaker
	<b>Battlecry:</b> Gain +1_Attack for each Frost spell in your hand. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_110", self.controller)
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


##########RLK_118##########

class pp_RLK_118(Preset_Play):
	""" Tomb Guardians
	Summon two 2/2 Zombies with <b>Taunt</b>. Spend 4 <b>Corpses</b> to give them <b>Reborn</b>. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_118", self.controller)
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


##########RLK_122##########

class pp_RLK_122(Preset_Play):
	""" The Scourge
	Fill your board with random Undead. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_122", self.controller)
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


##########RLK_504##########

class pp_RLK_504(Preset_Play):
	""" Corpse Bride
	<b>Battlecry:</b> Spend up to 8 <b>Corpses</b>. Summon a Risen Groom with stats equal to the amount spent. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_504", self.controller)
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


##########RLK_505##########

class pp_RLK_505(Preset_Play):
	""" Marrow Manipulator
	<b>Battlecry:</b> Spend up to 5 <b>Corpses</b>. Deal 2 damage to a random enemy for each. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_505", self.controller)
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


##########RLK_506t##########

class pp_RLK_506t(Preset_Play):
	""" Risen Groom
	<i>Doesn't leave a <b>Corpse</b>.</i> """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_506t", self.controller)
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


##########RLK_512##########

class pp_RLK_512(Preset_Play):
	""" Glacial Advance
	Deal $4 damage. Your next spell this turn costs (2) less. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_512", self.controller)
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


##########RLK_516##########

class pp_RLK_516(Preset_Play):
	""" Bone Breaker
	After your hero attacks a minion, deal 2 damage to the enemy hero. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_516", self.controller)
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


##########RLK_710e##########

class pp_RLK_710e(Preset_Play):
	""" Freezy Breezy
	Costs (1) less. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_710e", self.controller)
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


##########RLK_711##########

class pp_RLK_711(Preset_Play):
	""" Vicious Bloodworm
	<b>Battlecry:</b> Give a minion in your hand Attack equal to this minion's Attack. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_711", self.controller)
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


##########RLK_712##########

class pp_RLK_712(Preset_Play):
	""" Blood Tap
	Give all minions in your hand +1/+1. Spend 3 <b>Corpses</b> to give them +1/+1 more. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_712", self.controller)
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


##########RLK_713##########

class pp_RLK_713(Preset_Play):
	""" Lady Deathwhisper
	<b>Deathrattle:</b> Copy all Frost spells in your hand. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_713", self.controller)
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


##########RLK_730##########

class pp_RLK_730(Preset_Play):
	""" Blood Boil
	<b>Lifesteal</b> Infect all enemy minions. At the end of your turns, they take 2 damage. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_730", self.controller)
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


##########RLK_731##########

class pp_RLK_731(Preset_Play):
	""" Darkfallen Neophyte
	<b>Battlecry:</b> Spend 2 <b>Corpses</b> to give all minions in your hand +2 Attack. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_731", self.controller)
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


##########RLK_740##########

class pp_RLK_740(Preset_Play):
	""" Might of Menethil
	<b>Battlecry:</b> Spend up to 3 <b>Corpses</b>. <b>Freeze</b> that many enemy minions. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_740", self.controller)
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


##########RLK_745##########

class pp_RLK_745(Preset_Play):
	""" Malignant Horror
	<b>Reborn</b> At the end of your turn, spend 5 <b>Corpses</b> to summon a copy of this minion. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_745", self.controller)
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


