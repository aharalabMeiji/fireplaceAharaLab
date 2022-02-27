from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone, CardType, Rarity, CardClass
from utils import postAction

def SimulateGames_Scholo_Hunter():
	PresetGame(pp_SCH_538)#
	#PresetGame(pp_SCH_607)#OK
	pass

##########################################

class pp_SCH_538(Preset_Play):
	##Ace Hunter Kreen SCH_538
	#Your other characters are <b>Immune</b> while attacking.
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('SCH_607',controller)#Shan'do Wildclaw
		self.mark2=self.exchange_card('beast',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark2, controller)
		self.play_card(self.mark1, controller, target=self.mark2,  choose=self.mark1.choose_cards[0])#
		#self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[1])#
		self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		hero = controller.opponent.hero
		pass

##########################################


class pp_SCH_607(Preset_Play):
	""" Shan'do Wildclaw SCH_607
	[x]<b>Choose One -</b> Give Beasts in your deck +1/+1; or Transform into a copy of a friendly Beast. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('SCH_607',controller)#Shan'do Wildclaw
		self.mark2=self.exchange_card('beast',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark2, controller)
		self.play_card(self.mark1, controller, target=self.mark2,  choose=self.mark1.choose_cards[0])#
		#self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[1])#
		self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		hero = controller.opponent.hero
		pass

##################################
