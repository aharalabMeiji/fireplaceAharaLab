from .simulate_game import Preset_Play,PresetGame

#Alteric_Druid=['AV_205','AV_210','AV_210e','AV_211','AV_211t','AV_291','AV_292','AV_292e','AV_292e2','AV_293','AV_293e','AV_294','AV_294e','AV_293t','AV_295','AV_295a','AV_295b','AV_296','AV_296e','AV_296e2','AV_360',   ]

def SimulateGames_Alterac_Druid():
	#PresetGame(pp_AV_205)# Hero
	#PresetGame(pp_AV_210)#################
	#PresetGame(pp_AV_211)####OK
	#PresetGame(pp_AV_291)####OK
	#PresetGame(pp_AV_292)####OK
	PresetGame(pp_AV_293)
	#PresetGame(pp_AV_294)
	#PresetGame(pp_AV_295)
	#PresetGame(pp_AV_296)
	#PresetGame(pp_AV_360)
	pass

#########################

class pp_AV_210(Preset_Play):
	""" Pathmaker (3/3/4) 
	Battlecry: Cast the other choice from the last [Choose One] spell you've cast.  """
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_210',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#self.play_card(self.mark1, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		print ("%s（目視）"%(self.mark1))
	pass
		
#########################

class pp_AV_211(Preset_Play):
	""" Dire Frostwolf (4/4/4) beast
	[Stealth] [Deathrattle]: Summon a 2/2 Wolf with Stealth. """
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_211',controller)
		self.mark2=self.exchange_card('minionA5',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)###stealth
		self.change_turn(controller)
		########## opponent
		self.play_card(self.mark2, opponent)
		self.change_turn(opponent)
		########## controller
		self.attack_card(self.mark1, self.mark2, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		card=controller.field[-1]
		print ("%s（目視）(%d/%d) stealth=%s"%(card, card.atk, card.health, card.stealthed))
	pass
		
#########################

class pp_AV_291(Preset_Play):
	""" Frostsaber Matriarch (7/4/5) beast
	[Taunt]. Costs (1) less for each Beast you've summoned this game. """
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_291',controller)
		self.mark2=self.exchange_card('beast',controller)
		self.mark3=self.exchange_card('beast',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark2, controller)###
		self.play_card(self.mark3, controller)###
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		########## controller
		#self.attack_card(self.mark1, self.mark2, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		card=self.mark1
		print ("%s（目視）cost:%d <- %d "%(card, card.cost, card.data.cost))
	pass
		
#########################

class pp_AV_292(Preset_Play):
	""" Heart of the Wild (3)
	Give a minion +2/+2, then give your Beasts +1/+1."""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_292',controller)
		self.mark2=self.exchange_card('beast',controller)
		self.mark3=self.exchange_card('beast',controller)
		self.mark4=self.exchange_card('dragon',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark2, controller)###
		self.play_card(self.mark3, controller)###
		self.change_turn(controller)
		########## opponent
		self.change_turn(opponent)
		########## controller
		self.play_card(self.mark4, controller)###
		self.play_card(self.mark1, controller,target=self.mark2)###(1,4),(1,2)
		#self.attack_card(self.mark1, self.mark2, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		card=self.mark2
		if self.contains_buff(card,'AV_292e'):
			print("OK. %s has a buff AV_292e"%(card))
		card=self.mark2
		if self.contains_buff(card,'AV_292e2'):
			print("OK. %s has a buff AV_292e2"%(card))
		card=self.mark3
		if self.contains_buff(card,'AV_292e2'):
			print("OK. %s has a buff AV_292e2"%(card))
	pass
		
#########################


class pp_AV_293(Preset_Play):
	""" Wing Commander Mulverick (4/2/5)
	[Rush]. Your minions have "Honorable Kill: Summon a 2/2 Wyvern with Rush." """
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_293',controller)
		self.mark2=self.exchange_card('beast',controller)
		self.mark3=self.exchange_card('beast',controller)
		self.mark4=self.exchange_card('dragon',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark2, controller)###
		self.play_card(self.mark3, controller)###
		self.change_turn(controller)
		########## opponent
		self.change_turn(opponent)
		########## controller
		self.play_card(self.mark4, controller)###
		self.play_card(self.mark1, controller,target=self.mark2)###(1,4),(1,2)
		#self.attack_card(self.mark1, self.mark2, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		card=self.mark2
		if self.contains_buff(card,'AV_292e'):
			print("OK. %s has a buff AV_292e"%(card))
		card=self.mark2
		if self.contains_buff(card,'AV_292e2'):
			print("OK. %s has a buff AV_292e2"%(card))
		card=self.mark3
		if self.contains_buff(card,'AV_292e2'):
			print("OK. %s has a buff AV_292e2"%(card))
	pass
		
#########################
