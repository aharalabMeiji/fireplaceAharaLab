from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import CardClass
from utils import postAction

#Alteric_Druid=['AV_205','AV_210','AV_210e','AV_211','AV_211t','AV_291','AV_292','AV_292e','AV_292e2','AV_293','AV_293e','AV_294','AV_294e','AV_293t','AV_295','AV_295a','AV_295b','AV_296','AV_296e','AV_296e2','AV_360',   ]

def alterac_druid():
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
	#PresetGame(pp_ONY_018)####OK
	PresetGame(pp_ONY_019)####OK
	#PresetGame(pp_ONY_021)####OK
	pass

#########################

class pp_AV_205(Preset_Play):
	""" Wildheart Guff ( 5/*/5) Hero
	Battlecry: Set your maximum Mana to 20. Gain a Mana Crystal. Draw a card."""
	class1=CardClass.DRUID
	class2=CardClass.DRUID
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
		self.activate_heropower(controller, None)
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

class pp_AV_210(Preset_Play):
	""" Pathmaker (3/3/4) 
	Battlecry: Cast the other choice from the last [Choose One] spell you've cast.  """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
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
	class1=CardClass.DRUID
	class2=CardClass.DRUID
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
	class1=CardClass.DRUID
	class2=CardClass.DRUID
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
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_292',controller)
		self.mark2=self.exchange_card('beast',controller)
		self.mark3=self.exchange_card('dragon',controller)
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
		self.play_card(self.mark1, controller,target=self.mark3)###(1,3),(1,2)
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
		if not self.contains_buff(card,'AV_292e2'):
			print("OK. %s does not has a buff AV_292e2"%(card))
	pass
		
#########################


class pp_AV_293(Preset_Play):
	""" Wing Commander Mulverick (4/2/5)
	[Rush]. Your minions have "Honorable Kill: Summon a 2/2 Wyvern with Rush." """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_293',controller)
		self.mark2=self.exchange_card('vanillaA3',controller)
		self.mark3=self.exchange_card('vanillaH3',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark2, controller)###
		self.change_turn(controller)
		########## opponent
		self.play_card(self.mark3, controller)###
		self.change_turn(opponent)
		########## controller
		self.play_card(self.mark1, controller)###
		self.attack_card(self.mark2, self.mark3, controller)#
		#self.attack_card(self.mark1, self.mark2, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		print("%s honorablly killed %s. 目視"%(self.mark2, self.mark3))
		for card in controller.field:
			print("field: %s(%s). "%(card, card.id))
	pass
		
#########################

class pp_AV_294(Preset_Play):
	""" Clawfury Adept (2/2/3) beast
	[Battlecry]: Give all other friendly characters +1 Attack this turn. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_294',controller)
		self.mark2=self.exchange_card('vanilla',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark2, controller)###
		self.play_card(self.mark1, controller)###
		hero = controller.hero
		card1 = self.mark1
		card2 = self.mark2
		print ("Hero: (%d/%d)<-(%d/%d)"%(hero.atk,hero.health, hero.data.atk, hero.data.health))
		print ("card1: (%d/%d)<-(%d/%d)"%(card1.atk, card1.health, card1.data.atk, card1.data.health))
		print ("card2: (%d/%d)<-(%d/%d)"%(card2.atk, card2.health, card2.data.atk, card2.data.health))
		self.change_turn(controller)
		########## opponent
		self.change_turn(opponent)
		########## controller
		print ("Hero: (%d/%d)<-(%d/%d)"%(hero.atk,hero.health, hero.data.atk, hero.data.health))
		print ("card1: (%d/%d)<-(%d/%d)"%(card1.atk, card1.health, card1.data.atk, card1.data.health))
		print ("card2: (%d/%d)<-(%d/%d)"%(card2.atk, card2.health, card2.data.atk, card2.data.health))
		#self.attack_card(self.mark1, self.mark2, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
	pass
		
#########################

class pp_AV_295(Preset_Play):
	""" Capture Coldtooth Mine (2)
	[Choose One] - Draw your lowest Cost card; or Draw your highest Cost card. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_295',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[0])###option1
		#self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[1])###option2
		self.mark1.choose_both=True
		self.play_card(self.mark1, controller)
		self.change_turn(controller)
		########## opponent
		#self.change_turn(opponent)
		#self.attack_card(self.mark1, self.mark2, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		print("引いたカードは　%s (コスト%d). 目視"%(self.player.hand[-1], self.player.hand[-1].cost))
		for card in controller.hand:
			self.print_stats("hand",card, old_cost=True)
	pass
		
#########################

class pp_AV_296(Preset_Play):
	""" Pride Seeker (3/2/4)
	[Battlecry]: Your next [Choose One] card costs (2) less."""
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_296',controller)
		self.mark2=self.exchange_card('chooseone',controller)
		self.mark3=self.exchange_card('chooseone',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)###
		print ("cost of card2(%s) = %d <- %d"%(self.mark2, self.mark2.cost, self.mark2.data.cost))
		print ("cost of card3(%s) = %d <- %d"%(self.mark3, self.mark3.cost, self.mark3.data.cost))
		self.play_card(self.mark2, controller, choose=self.mark2.choose_cards[0])###
		print ("cost of card2(%s) = %d <- %d"%(self.mark2, self.mark2.cost, self.mark2.data.cost))
		print ("cost of card3(%s) = %d <- %d"%(self.mark3, self.mark3.cost, self.mark3.data.cost))
		self.change_turn(controller)
		########## opponent
		#self.change_turn(opponent)
		#self.attack_card(self.mark1, self.mark2, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		print("引いたカードは　%s (コスト%d). 目視"%(self.player.hand[-1], self.player.hand[-1].cost))
	pass
		
#########################

class pp_AV_360(Preset_Play):
	""" Frostwolf Kennels (3) Lasts
	At the end of your turn, summon a 2/2 Wolf with Stealth. Lasts 3 turns. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('AV_360',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)###
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
		for card in controller.field:
			print("field: %s(%s). "%(card, card.id))
	pass
		
#########################

class pp_ONY_018(Preset_Play):
	""" Boomkin
	[Choose One - ]Restore8 Health to your hero; or Deal 4 damage. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('ONY_018',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[0])#option1
		#self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[1])#option2
		self.mark1.choose_both=True#option3
		self.play_card(self.mark1, controller)#option3
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		########## controller
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			self.print_stats("hand",card, show_buff=True)
	pass
		
#########################

class pp_ONY_019(Preset_Play):
	""" Raid Negotiator
	[Battlecry:] [Discover] a[Choose One] card. It has both effects combined. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('ONY_019',controller)
		self.mark2=self.exchange_card('ONY_018',controller)
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
		#self.play_card(self.mark2, opponent)
		self.change_turn(opponent)
		########## controller
		self.play_card(controller.hand[-2], controller)
		#self.play_card(self.mark2, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			self.print_stats("hand",card, show_buff=True)
			print("%s choose_both %s"%(card, card.choose_both))
		for card in controller.field:
			self.print_stats("field",card, show_buff=True)
			print("%s choose_both %s"%(card, card.choose_both))
	pass
		
#########################

class pp_ONY_021(Preset_Play):
	""" Scale of Onyxia
	Fill your board with 2/1 Whelps with [Rush]. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('ONY_021',controller)
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
		for card in controller.field:
			self.print_stats("field",card, show_buff=True)
	pass
		
#########################