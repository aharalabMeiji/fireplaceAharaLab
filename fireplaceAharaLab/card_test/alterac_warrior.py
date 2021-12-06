from .simulate_game import PresetGame, Preset_Play
from hearthstone.enums import Zone,CardType, Rarity

#Alterac_Warrior=['AV_108','AV_109','AV_109e','AV_119','AV_119e','AV_145','AV_145e','AV_202','AV_202p','AV_202t2','AV_321','AV_322','AV_323','AV_323t','AV_565','AV_660',]

def SimulateGames_Alterac_Warrior():
	""" simulate games  """
	#PresetGame(pp_AV_108)####OK
	#PresetGame(pp_AV_109)####OK
	PresetGame(pp_AV_119)#
	#PresetGame(pp_AV_145)##
	#PresetGame(pp_AV_202)##
	#PresetGame(pp_AV_321)##
	#PresetGame(pp_AV_322)#
	#PresetGame(pp_AV_323)##
	#PresetGame(pp_AV_565)##
	#PresetGame(pp_AV_660)##
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
		self.mark4=self.exchange_card('vanillaH3',opponent)
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
		print("%s <- %d - %d"%(self.msg1, self.mark1.cost, self.player.hero.armor))
		pass
	pass

#######################

class pp_AV_109(Preset_Play):
	""" Frozen Buckler (2) frost
	Gain 10 Armor. At the start of your next turn, lose 5 Armor. """
	msg1=''
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_109',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		self.msg1 = "Armor of %s is %d:"%(self.mark1, controller.hero.armor)
		self.change_turn(controller)
		########## opponent
		self.change_turn(opponent)
		########## controller
		pass
	def result_inspection(self):
		super().result_inspection()
		# check armor
		print("%s -> %d (10->5)"%(self.msg1, self.player.hero.armor))
		#最終ターン、AV_109eが破壊されることを目視。
		if not self.contains_buff(self.player,'AV_109e'):
			print("check OK")

		pass
	pass

#######################

class pp_AV_119(Preset_Play):
	""" To the Front! (2) 
	Your minions cost (2) less this turn (but not less than 1). """
	msg1=''
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_119',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		# check costs
		for card in self.player.hand:
			print("cost of %s = %d <- %d - 2"%(card, card.cost, card.data.cost), end=':')
			if self.contains_buff(card,'AV_119e'):
				print("check OK")

		pass
	pass

#######################

