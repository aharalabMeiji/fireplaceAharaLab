
from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity, CardClass

def core_warrior():
	PresetGame(pp_CORE_EX1_411)### 完全ではないが、とりあえずと言う感じ。
	pass

##################################

class pp_CORE_EX1_411(Preset_Play):# <6>[1637]
	""" Brightwing
	[Battlecry:] Add a random [Legendary] minion to your_hand. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_411',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark1, controller)
		self.attack_card(controller.hero, opponent.hero,controller)
		self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark3, opponent)#
		self.change_turn(opponent)
		##########controller
		self.attack_card(controller.hero, opponent.hero,controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.opponent.hero
		self.print_stats("weapon",self.mark1)
		for card in [controller.hero, controller.opponent.hero]:
			self.print_stats ("controller.hero", card)
		pass

##################################

