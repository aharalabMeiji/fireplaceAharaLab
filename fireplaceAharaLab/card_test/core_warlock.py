from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity,CardClass
from fireplace.actions import Discard 

def SimulateGames_CoreWarlock():
	PresetGame(pp_CORE_AT_021)#
	#PresetGame(pp_CORE_CS2_062)#
	#PresetGame(pp_CORE_CS2_064)#
	#PresetGame(pp_CORE_EX1_302)#
	#PresetGame(pp_CORE_EX1_304)#
	#PresetGame(pp_CORE_EX1_309)#
	#PresetGame(pp_CORE_EX1_312)#
	#PresetGame(pp_CORE_EX1_319)#
	#PresetGame(pp_CORE_EX1_323)#
	#PresetGame(pp_CORE_GIL_191)#
	#PresetGame(pp_CORE_ICC_055)#
	#PresetGame(pp_CORE_OG_241)#
	#PresetGame(pp_CORE_UNG_833)#
	#PresetGame(pp_CS3_002)#
	#PresetGame(pp_CS3_003)#
	#PresetGame(pp_CS3_021)#
	pass

##################################

class pp_CORE_AT_021(Preset_Play):
	""" Tiny Knight of Evil
	Whenever you discard a card, gain +1/+1. """
	const1 = 0
	const2 = 0
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_021',controller)#
		self.mark2=self.exchange_card('vanilla',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark1, controller)#
		self.change_turn(controller)
		##########opponent
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark2, controller)#
		Discard(self.mark2).trigger(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		# card1 に+1/+1のバフが付いているかどうかを確認
		print ("%s:"%(card1.buffs))
		print ("STATS: %d/%d <- %d/%d"%(card1.atk, card1.health, card1.data.atk, card1.data.health))
		pass

##################################
