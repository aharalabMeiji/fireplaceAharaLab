from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity, CardClass

def SimulateGames_Scholo_Neutral():
	PresetGame(pp_SCH_605)#

##################################

class pp_SCH_605(Preset_Play):
	""" Lake Thresher"""
	#Also damages the minions next to whomever this attacks."""
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('SCH_605',opponent)#湖のスレッシャー
		self.mark2=self.exchange_card('SCH_609',controller)#適者生存SCH_609
		self.mark3=self.exchange_card('vanilla',controller)#vanilla
		self.mark4=self.exchange_card('vanilla',controller)#vanilla
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark2, controller)#適者生存SCH_609
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark1, opponent)#湖のスレッシャー
		self.change_turn(opponent)
		##########controller
		self.activate_heropower(controller)#爪=heropower
		self.play_card(self.mark3, controller)#vanilla
		self.play_card(self.mark4, controller)
		self.change_turn(controller)
		##########opponent
		self.activate_heropower(opponent)#爪=heropower
		self.attack_card(self.mark1, self.mark3, opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		hero = controller.opponent.hero
		print ("%s:"%(card1))
		print ("STATS: %d/%d"%(card1.atk, card1.health))
		print ("RUSH: %s"%(card1.rush))
		print ("DIVINE SHIELD: %s"%(card1.divine_shield))
		print ("TAUNT: %s"%(card1.taunt))
		pass

##################################
