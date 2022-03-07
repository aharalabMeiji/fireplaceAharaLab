from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone, CardType, Rarity, CardClass

def SimulateGames_Scholo_Paladin():
	#PresetGame(pp_SCH_138)#
	pass

##########################################

class pp_SCH_138(Preset_Play):
	"""Blessing of Authority		5	-	-	Spell	Rare	-	-	
	Give a minion +8/+8. It_can't attack heroes this turn."""
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('SCH_138',controller)#
		self.mark2=self.exchange_card('minionH3',controller)#
		self.mark3=self.exchange_card('minionH3',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark2, controller)
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark3, opponent)#
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller, target=self.mark2)#
		#self.change_turn(controller)# optional
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		print("cannot_attack_heros = %s"%self.mark2.cannot_attack_heroes)
		for card in self.mark2.attack_targets:
			self.print_stats("mark2.attack_targets",card)
		pass

