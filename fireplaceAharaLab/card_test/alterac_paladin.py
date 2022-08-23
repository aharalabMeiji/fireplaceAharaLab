from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity

def alterac_paladin():

	#PresetGame(pp_AV_146)##OK
	#PresetGame(pp_AV_206)##
	#PresetGame(pp_AV_213)##
	#PresetGame(pp_AV_338)##
	#PresetGame(pp_AV_339)##
	#PresetGame(pp_AV_340)##
	#PresetGame(pp_AV_341)##
	#PresetGame(pp_AV_342)##
	#PresetGame(pp_AV_343)##
	#PresetGame(pp_AV_344)##
	#PresetGame(pp_AV_345)##
	#PresetGame(pp_BOM_08_Cariel_002t)##
	#PresetGame(pp_BOM_08_Cariel_003t)##
	#PresetGame(pp_BOM_08_Cariel_006t)##
	#PresetGame(pp_BOM_09_Cariel_004t)##
	#PresetGame(pp_BOM_09_Cariel_006t)##
	#PresetGame(pp_BOM_09_Cariel_008t)##
	#PresetGame(pp_BOM_10_BackToBack_004s)##
	#PresetGame(pp_BOM_10_Cariel_004t)##
	#PresetGame(pp_ONY_020)##
	#PresetGame(pp_ONY_022)##
	#PresetGame(pp_ONY_027)##
	#PresetGame(pp_TB_01_BOM_Mercs_Cariel_001p)##


##########AV_146##########

class pp_AV_146(Preset_Play):
class pp_AV_146(Preset_Play):# <5>[1626] (7/2/5)
	""" The Immovable Object
	This doesn't lose Durability. Your hero takes half damage, rounded up. """
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_146',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		########## controller
		self.play_card(self.mark1, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
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


##########BOM_08_Cariel_002t##########

class pp_BOM_08_Cariel_002t(Preset_Play):
	""" Cariel
	[Taunt][Revive]: (3) """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_08_Cariel_002t", self.controller)
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


##########BOM_08_Cariel_003t##########

class pp_BOM_08_Cariel_003t(Preset_Play):
	""" Cariel
	[Taunt][Revive]: (3) """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_08_Cariel_003t", self.controller)
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


##########BOM_08_Cariel_006t##########

class pp_BOM_08_Cariel_006t(Preset_Play):
	""" Immovable Cariel
	[Taunt][Deathrattle]: You lose the game. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_08_Cariel_006t", self.controller)
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


##########BOM_09_Cariel_004t##########

class pp_BOM_09_Cariel_004t(Preset_Play):
	""" Cariel Roame
	[Taunt][Revive:] (3) """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_09_Cariel_004t", self.controller)
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


##########BOM_09_Cariel_006t##########

class pp_BOM_09_Cariel_006t(Preset_Play):
	""" Cariel
	[Taunt][Revive:] (3) """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_09_Cariel_006t", self.controller)
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


##########BOM_09_Cariel_008t##########

class pp_BOM_09_Cariel_008t(Preset_Play):
	""" Cariel
	[Taunt][Revive:] (3) """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_09_Cariel_008t", self.controller)
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


##########BOM_10_BackToBack_004s##########

class pp_BOM_10_BackToBack_004s(Preset_Play):
	""" Back to Back
	Kurtrus and Cariel are both [Immune] until your next turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_10_BackToBack_004s", self.controller)
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


##########BOM_10_Cariel_004t##########

class pp_BOM_10_Cariel_004t(Preset_Play):
	""" Cariel, Conflicted
	[Taunt] """
	def preset_deck(self):
		self.mark1=self.exchange_card("BOM_10_Cariel_004t", self.controller)
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


##########TB_01_BOM_Mercs_Cariel_001p##########

class pp_TB_01_BOM_Mercs_Cariel_001p(Preset_Play):
	""" Cariel
	[Hero Power]Summon a friendly minion that died this game with 1 Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TB_01_BOM_Mercs_Cariel_001p", self.controller)
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






