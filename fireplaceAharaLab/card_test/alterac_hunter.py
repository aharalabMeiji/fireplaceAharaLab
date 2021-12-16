from .simulate_game import Preset_Play,PresetGame
from utils import postAction

#Alterac_Hunter=['AV_113','AV_113p','AV_147','AV_147e','AV_224','AV_226','AV_226e','AV_244','AV_244e','AV_333','AV_334','AV_334e','AV_335','AV_335e','AV_336','AV_336e','AV_337','AV_337t',	]
def SimulateGames_Alterac_Hunter():
	#PresetGame(pp_AV_113)########## imporoved secret....
	#PresetGame(pp_AV_147)##OK
	#PresetGame(pp_AV_224)##OK
	#PresetGame(pp_AV_226)##OK
	#PresetGame(pp_AV_244)##OK
	PresetGame(pp_AV_333)##
	#PresetGame(pp_AV_334)##
	#PresetGame(pp_AV_335)##
	#PresetGame(pp_AV_336)##
	#PresetGame(pp_AV_337)##
	pass

#########################

class pp_AV_113(Preset_Play):
	"""Beaststalker Tavish (6/*/5) Hero
	Battlecry: Discover and cast 2 Improved Secrets."""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_113',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
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
			print("%s :  cost %d <= %d"%(card, card.cost, card.data.cost))
	pass
		
#########################

class pp_AV_147(Preset_Play):
	""" Dun Baldar Bunker (2) Lasts
	At the end of your turn, draw a Secret and set its Cost to (1). Lasts 3 turns."""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_147',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		self.change_turn(controller)
		########## opponent
		self.change_turn(opponent)
		########## controller
		self.change_turn(controller)
		########## opponent
		self.change_turn(opponent)
		########## controller
		self.change_turn(controller)
		########## opponent
		self.change_turn(opponent)
		########## controller
		self.change_turn(controller)
		########## opponent
		self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			print("%s :  cost %d <= %d"%(card, card.cost, card.data.cost))
	pass
		
#########################

class pp_AV_224(Preset_Play):
	""" Spring the Trap (4)
	Deal 3 damage to a minion and cast a Secret from your deck. Honorable Kill: Cast 2."""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_224',controller)
		self.mark2=self.exchange_card('vanillaH3',opponent)# or H2
		self.mark3=self.append_deck_shuffle('secret',controller)
		self.mark4=self.append_deck_shuffle('secret',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#self.play_card(self.mark1, controller)
		self.change_turn(controller)
		########## opponent
		self.play_card(self.mark2, opponent)
		self.change_turn(opponent)
		########## controller
		self.play_card(self.mark1, controller,target=self.mark2)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		#mark2にdamage 3が与えられるかどうか
		print("%s is damaged %d -> %d"%(self.mark2, self.mark2.data.health, self.mark2.health))
		print ("honorablly killed = %s"%(self.mark2.honorably_killed))
		#secretがcastされるかどうか
		for card in controller.secrets:
			print ("secret: %s"%(card))
		#honorable killの場合に、発動するかどうか
	pass
		
#########################

class pp_AV_226(Preset_Play):
	""" Ice Trap (2) frost
	Secret: When your opponent casts a spell, return it to their hand instead. It costs (1) more."""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_226',controller)
		self.mark2=self.exchange_card('spell',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		self.change_turn(controller)
		########## opponent
		self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		if controller.secrets==[]:
			print(" no secrets")
		for card in controller.secrets:
			print ("secret: %s"%(card))
		for card in controller.opponent.hand:
			print ("op. hand: %s (cost %d<=%d)"%(card, card.cost, card.data.cost))
	pass
		
#########################

class pp_AV_244(Preset_Play):
	""" Bloodseeker (2/2/2) weapon
	Honorable Kill: Gain +1/+1."""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_244',controller)
		self.mark2=self.exchange_card('vanillaH2',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		self.change_turn(controller)
		########## opponent
		self.play_card(self.mark2, opponent)
		self.change_turn(opponent)
		########## controller
		self.attack_card(controller.hero, self.mark2, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		# honocably kill が成立しているかどうか。
		print("%s was honorably killed : %s"%(self.mark2, self.mark2.honorably_killed))
		# カードにバフが付いているかどうか
		print ("%s has a buff : %d"%(self.mark1, len(self.mark1.buffs)))
		# スタッツに1/1がついているかどうか
		print ("%s : stats : %d/%d <- %d/%d"%(self.mark1,self.mark1.atk,self.mark1.durability,self.mark1.data.atk, self.mark1.data.durability))
	pass
		
#########################

class pp_AV_333(Preset_Play):
	""" Revive Pet (3) nature
	Discover a friendly Beast that died this game. Summon it. """
	mark5=None
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_333',opponent)
		self.mark2=self.exchange_card('beast',opponent)
		self.mark3=self.exchange_card('beast',opponent)
		self.mark4=self.exchange_card('minionH7',controller)
		self.mark5=self.exchange_card('minionH7',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark4, controller)
		self.change_turn(controller)
		########## opponent
		self.play_card(self.mark2, opponent)
		self.play_card(self.mark3, opponent)
		self.change_turn(opponent)
		########## controller
		self.play_card(self.mark5, controller)
		self.attack_card(self.mark4,self.mark2, controller)
		self.change_turn(controller)
		########## opponent
		self.change_turn(opponent)
		########## controller
		self.attack_card(self.mark5, self.mark3, controller)
		self.attack_card(self.mark4, self.mark3, controller)
		self.change_turn(controller)
		########## opponent
		print(">>>>>> %s (%s): zone=%s"%(self.mark1, self.mark1.controller, self.mark1.zone))
		print(">>>>>> %s (%s): zone=%s"%(self.mark2, self.mark2.controller, self.mark2.zone))
		print(">>>>>> %s (%s): zone=%s"%(self.mark3, self.mark3.controller, self.mark3.zone))
		print(">>>>>> %s (%s): zone=%s"%(self.mark4, self.mark4.controller, self.mark4.zone))
		print(">>>>>> %s (%s): zone=%s"%(self.mark5, self.mark5.controller, self.mark5.zone))
		self.play_card(self.mark1, opponent)
		postAction(opponent)
		self.change_turn(opponent)
		
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			print("%s :  cost %d <= %d"%(card, card.cost, card.data.cost))
	pass
		
#########################

class pp_AV_334(Preset_Play):
	""" 
	"""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_113',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
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
			print("%s :  cost %d <= %d"%(card, card.cost, card.data.cost))
	pass
		
#########################

class pp_AV_335(Preset_Play):
	""" 
	"""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_113',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
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
			print("%s :  cost %d <= %d"%(card, card.cost, card.data.cost))
	pass
		
#########################

class pp_AV_336(Preset_Play):
	""" 
	"""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_113',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
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
			print("%s :  cost %d <= %d"%(card, card.cost, card.data.cost))
	pass
		
#########################

class pp_AV_337(Preset_Play):
	""" 
	"""
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_113',controller)
		self.mark2=self.exchange_card('vanillaH3',controller)
		self.mark3=self.exchange_card('minionH7',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
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
			print("%s :  cost %d <= %d"%(card, card.cost, card.data.cost))
	pass
		
########################