from .simulate_game import PresetGame,Preset_Play
from hearthstone.enums import Zone,CardType, Rarity

#Alterac_Warrior=['AV_108','AV_109','AV_119','AV_119e','AV_145','AV_145e','AV_202','AV_202p','AV_202t2','AV_321','AV_322','AV_323','AV_323t','AV_565','AV_660',]

def SimulateGames_Alterac_Neutral():
	""" simulate games  """
	PresetGame(pp_AV_108)####OK
	#PresetGame(pp_AV_109)####OK
	#PresetGame(pp_AV_119)####OK
	#PresetGame(pp_AV_145)####OK
	#PresetGame(pp_AV_202)####OK
	#PresetGame(pp_AV_321)####OK
	#PresetGame(pp_AV_322)####OK
	#PresetGame(pp_AV_323)####OK
	#PresetGame(pp_AV_565)####OK
	#PresetGame(pp_AV_660)####OK
	pass

#######################

class pp_AV_108(Preset_Play):
	"""Shield Shatter (10) frost
	Deal 5 damage to all minions. Costs (1) less for each Armor you have. """
	msg1=''
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_108',controller)
		self.mark2=self.exchange_card('armor',controller)
		self.mark3=self.exchange_card('minionH6',opponent)
		self.mark4=self.exchange_card('minionH3',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark2, controller)
		self.change_turn(controller)
		########## opponent
		self.play_card(self.mark3, opponent)
		self.play_card(self.mark4, opponent)
		self.change_turn(opponent)
		########## controller
		self.msg1 = "the cost of %s is %d"%(self.mark1, self.mark1.cost)
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		# コストを☑
		print("%s"%(self.msg1))

		pass
	pass

#######################

