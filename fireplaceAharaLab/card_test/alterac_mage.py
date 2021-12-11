from .simulate_game import Preset_Play,PresetGame

#Alterac_Mage=['AV_114','AV_114e','AV_115','AV_115e','AV_116','AV_200','AV_212','AV_212e','AV_218','AV_218t','AV_282','AV_282t','AV_282t2','AV_282t3','AV_282t4','AV_282t5','AV_283','AV_284','AV_290',]

def SimulateGames_Alterac_Druid():
	#PresetGame(pp_AV_205)# Hero ####OK
	#PresetGame(pp_AV_210)#################
	#PresetGame(pp_AV_211)####OK
	#PresetGame(pp_AV_291)####OK
	#PresetGame(pp_AV_292)####OK
	#PresetGame(pp_AV_293)####OK
	#PresetGame(pp_AV_294)####OK
	#PresetGame(pp_AV_295)####OK
	#PresetGame(pp_AV_296)####OK
	#PresetGame(pp_AV_360)####OK
	pass

#########################

class pp_AV_205(Preset_Play):
	""" Wildheart Guff ( 5/*/5) Hero
	Battlecry: Set your maximum Mana to 20. Gain a Mana Crystal. Draw a card."""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_205',controller)
		self.mark2=self.exchange_card('weapon',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark2, controller)
		self.play_card(self.mark1, controller)
		self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		self.change_turn(opponent)
		########## controller
		self.activate_heropower(controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		print ("New hero = %s"%(self.mark1))
		print ("Hero health = %s"%(controller.hero.health))
		print ("Weapon = %s"%(controller.weapon))
		print ("Mana = %d/%d"%(controller.mana, controller.max_mana))
		print ("Armor = %s"%(controller.hero.armor))
		print ("Atk = %s"%(controller.hero.atk))
		print ("HeroPower = %s"%(controller.hero.power))
		print ("Cost HeroPower = %s"%(controller.hero.power.cost))
	pass
		
#########################

