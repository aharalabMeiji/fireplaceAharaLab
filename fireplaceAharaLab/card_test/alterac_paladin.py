from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity

def alterac_paladin():

	#PresetGame(pp_AV_146)##OKOK
	#PresetGame(pp_AV_206)##
	#PresetGame(pp_AV_213)##
	#PresetGame(pp_AV_338)##
	#PresetGame(pp_AV_339)##
	#PresetGame(pp_AV_340)##
	#PresetGame(pp_AV_341)##
	#PresetGame(pp_AV_342)##
	#PresetGame(pp_AV_343)##
	#PresetGame(pp_AV_344)##
	PresetGame(pp_AV_345)## ### OKOK
	#PresetGame(pp_ONY_020)##
	#PresetGame(pp_ONY_022)##
	#PresetGame(pp_ONY_027)##
	pass

##########AV_146##########

class pp_AV_146(Preset_Play):# <5>[1626] (7/2/5)
	""" The Immovable Object
	This doesn't lose Durability. Your hero takes half damage, rounded up. """
	def preset_deck(self):
		self.mark1=self.exchange_card('AV_146',self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		########## controller
		self.play_card(self.mark1)
		self.attack_card(self.controller.hero, self.opponent.hero)
		self.change_turn()
		########## opponent
		Hit(self.controller.hero,5).trigger(self.opponent)
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		print("controller.hero.health=%d"%(self.controller.hero.health))
		assert self.controller.hero.health==30-3, "health"
		print("opponent.hero.health=%d"%(self.opponent.hero.health))
		assert self.opponent.hero.health==30-2, "health"
		print("%d"%(self.controller.weapon.durability))
		assert self.controller.weapon.durability== self.controller.weapon.data.durability, "no less durability"
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########AV_206##########

class pp_AV_206(Preset_Play):
	""" Lightforged Cariel
	[Battlecry:] Deal 2damage to all enemies.Equip a 2/5Immovable Object. """
	def preset_deck(self):
		self.mark1=self.exchange_card("AV_206", self.controller)
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


##########AV_213##########

class pp_AV_213(Preset_Play):
	""" Vitality Surge
	Draw a minion.Restore Health to your hero equal to its Cost. """
	def preset_deck(self):
		self.mark1=self.exchange_card("AV_213", self.controller)
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


##########AV_338##########

class pp_AV_338(Preset_Play):
	""" Hold the Bridge
	Give a minion +2/+1and [Divine Shield].It gains [Lifesteal] untilend of turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("AV_338", self.controller)
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


##########AV_339##########

class pp_AV_339(Preset_Play):
	""" Templar Captain
	[Rush]. After this attacksa minion, summon a 5/5Defender with [Taunt]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("AV_339", self.controller)
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


##########AV_340##########

class pp_AV_340(Preset_Play):
	""" Brasswing
	At the end of your turn, deal2 damage to all enemies.[Honorable Kill:] Restore 4Health to your hero. """
	def preset_deck(self):
		self.mark1=self.exchange_card("AV_340", self.controller)
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


##########AV_341##########

class pp_AV_341(Preset_Play):
	""" Cavalry Horn
	[Deathrattle:] Summon the lowest Cost minion in your hand. """
	def preset_deck(self):
		self.mark1=self.exchange_card("AV_341", self.controller)
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


##########AV_342##########

class pp_AV_342(Preset_Play):
	""" Protect the Innocent
	Summon a 5/5 Defender with [Taunt]. If your hero was healed this turn, summon another. """
	def preset_deck(self):
		self.mark1=self.exchange_card("AV_342", self.controller)
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


##########AV_343##########

class pp_AV_343(Preset_Play):
	""" Stonehearth Vindicator
	[Battlecry:] Draw a spellthat costs (3) or less.It costs (0) this turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("AV_343", self.controller)
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


##########AV_344##########

class pp_AV_344(Preset_Play):
	""" Dun Baldar Bridge
	After you summon aminion, give it +2/+2.Lasts 3 turns. """
	def preset_deck(self):
		self.mark1=self.exchange_card("AV_344", self.controller)
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


##########AV_345##########

class pp_AV_345(Preset_Play):
	""" Saidan the Scarlet
	[Rush.] Whenever this minion gains Attack or Health, double that amount <i>(wherever this is)</i>. """
	def preset_deck(self):
		self.mark1=self.exchange_card("AV_345", self.controller)
		self.mark2=self.exchange_card("CORE_CS2_092", self.controller)
		self.mark3=self.exchange_card("CORE_CS2_188", self.controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		print("stats=%d/%d"%(self.mark1.atk, self.mark1.health))#(2/2)
		self.play_card(self.mark2, target=self.mark1)
		print("(2,2)->(+4/+4)*2-> %d/%d"%(self.mark1.atk, self.mark1.health))
		assert self.mark1.atk==10, "stats"
		assert self.mark1.health==10, "stats"
		self.change_turn()
		### opp
		self.change_turn()
		### con
		self.play_card(self.mark3, target=self.mark1)
		print("(10,10)->(+2/0)*2->%d/%d"%(self.mark1.atk, self.mark1.health))
		assert self.mark1.atk==14, "stats"
		assert self.mark1.health==10, "stats"
		self.change_turn()
		print("(10,10)->(0/0)->%d/%d"%(self.mark1.atk, self.mark1.health))
		assert self.mark1.atk==10, "stats"
		assert self.mark1.health==10, "stats"
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########ONY_020##########

class pp_ONY_020(Preset_Play):
	""" Stormwind Avenger
	After you cast a spell on this minion, it gains +2 Attack. """
	def preset_deck(self):
		self.mark1=self.exchange_card("ONY_020", self.controller)
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


##########ONY_022##########

class pp_ONY_022(Preset_Play):
	""" Battle Vicar
	[Battlecry:] [Discover] aHoly spell. """
	def preset_deck(self):
		self.mark1=self.exchange_card("ONY_022", self.controller)
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


##########ONY_027##########

class pp_ONY_027(Preset_Play):
	""" Ring of Courage
	[Tradeable]Give a minion +1/+1. Repeat for each enemy minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("ONY_027", self.controller)
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







