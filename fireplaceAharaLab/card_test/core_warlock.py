from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity,CardClass
from fireplace.actions import Discard 

def SimulateGames_CoreWarlock():
	#PresetGame(pp_CORE_AT_021)#OK
	#PresetGame(pp_CORE_CS2_062)#OK
	#PresetGame(pp_CORE_CS2_064)#OK
	#PresetGame(pp_CORE_EX1_302)#OK
	#PresetGame(pp_CORE_EX1_304)#OK
	#PresetGame(pp_CORE_EX1_309)#OK
	PresetGame(pp_CORE_EX1_312)#OK
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

class pp_CORE_CS2_062(Preset_Play):
	""" Hellfire
	Deal $3 damage to ALL_characters. """
	const1 = 0
	const2 = 0
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_062',controller)#
		self.mark2=self.exchange_card('vanilla',controller)#
		self.mark3=self.exchange_card('vanilla',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark2, controller)#
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark3, opponent)#
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller)#
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card2=self.mark2
		card3=self.mark3
		hero1 = controller.hero
		hero2 = controller.opponent.hero
		print ("%s: %d/%d <- %d/%d"%(card2, card2.atk, card2.health, card2.data.atk, card2.data.health))
		print ("%s: %d/%d <- %d/%d"%(card3, card3.atk, card3.health, card3.data.atk, card3.data.health))
		print ("%s: %d/%d <- %d/%d"%(hero1, hero1.atk, hero1.health, hero1.data.atk, hero1.data.health))
		print ("%s: %d/%d <- %d/%d"%(hero2, hero2.atk, hero2.health, hero2.data.atk, hero2.data.health))
		pass

##################################

class pp_CORE_CS2_064(Preset_Play):
	""" Dread Infernal
	[Battlecry:] Deal 1 damage to ALL other characters. """
	const1 = 0
	const2 = 0
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_064',controller)#
		self.mark2=self.exchange_card('vanilla',controller)#
		self.mark3=self.exchange_card('vanilla',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark2, controller)#
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark3, opponent)#
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller)#
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card2=self.mark2
		card3=self.mark3
		hero1 = controller.hero
		hero2 = controller.opponent.hero
		print ("%s: %d/%d <- %d/%d"%(card2, card2.atk, card2.health, card2.data.atk, card2.data.health))
		print ("%s: %d/%d <- %d/%d"%(card3, card3.atk, card3.health, card3.data.atk, card3.data.health))
		print ("%s: %d/%d <- %d/%d"%(hero1, hero1.atk, hero1.health, hero1.data.atk, hero1.data.health))
		print ("%s: %d/%d <- %d/%d"%(hero2, hero2.atk, hero2.health, hero2.data.atk, hero2.data.health))
		pass

##################################

class pp_CORE_EX1_302(Preset_Play):
	""" Mortal Coil
	Deal $1 damage to a minion. If that kills it, draw a card. """
	const1 = 0
	const2 = 0
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_302',controller)#
		self.mark2=self.exchange_card('vanilla',controller)#
		self.mark3=self.exchange_card('vanillaH2',opponent)# or 'vanillaH2'
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark2, controller)#
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark3, opponent)#
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller,target=self.mark3)#
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card3=self.mark3
		print ("%s: %d/%d <- %d/%d"%(card3, card3.atk, card3.health, card3.data.atk, card3.data.health))
		#死んでいるときにカードを引いていること、死んでいないときにカードを引いていないことを目視する
		pass

##################################

class pp_CORE_EX1_304(Preset_Play):
	""" Void Terror
	[Battlecry:] Destroy both adjacent minions and gain their Attack and Health. """
	const1 = 0
	const2 = 0
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_304',controller)#
		self.mark2=self.exchange_card('vanilla',controller)#
		self.mark3=self.exchange_card('vanilla',opponent)# 
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark2, controller)#
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark3, opponent)#
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller)#
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		card2=self.mark2
		#mark2が破壊されていること
		print ("%s: (%d/%d) zone->%s"%(card2, card2.atk, card2.health,card2.zone))
		##mark2のスタッツをmark1が食べていること
		print ("%s: %d/%d <- %d/%d"%(card1, card1.atk, card1.health, card1.data.atk, card1.data.health))
		pass

####################


class pp_CORE_EX1_309(Preset_Play):
	""" Siphon Soul
	Destroy a minion. Restore #3 Health to_your hero. """
	const1 = 0
	const2 = 0
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_309',controller)#
		self.mark2=self.exchange_card('minionH5',opponent)# 
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark2, opponent)#
		self.change_turn(opponent)
		##########controller
		self.change_turn(controller)
		##########opponent
		self.attack_card(self.mark2, controller.hero, opponent)#
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller, target=self.mark2)#
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.hero
		card2=self.mark2
		#mark2が破壊されていること
		print ("%s: (%d/%d) zone->%s"%(card2, card2.atk, card2.health,card2.zone))
		##hero に +3 がついていること（基本目視）
		print ("%s: %d/%d　=30 - 5 + 3"%(hero, hero.atk, hero.health))
		pass

####################

class pp_CORE_EX1_312(Preset_Play):
	""" Twisting Nether
	Destroy all minions. """
	const1 = 0
	const2 = 0
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_312',controller)#
		self.mark2=self.exchange_card('minionH5',controller)# 
		self.mark3=self.exchange_card('minionH5',opponent)# 
		self.mark4=self.exchange_card('vanilla',opponent)# 
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark2, controller)#
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark3, opponent)#
		self.play_card(self.mark4, opponent)#
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller)#
		self.change_turn(controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.hero
		for card in [self.mark2,self.mark3,self.mark4]:
			#mark2,3,4が破壊されていること
			print ("%s: (%d/%d) zone->%s"%(card, card.atk, card.health,card.zone))
		pass

####################
