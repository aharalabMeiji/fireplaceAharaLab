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
	#PresetGame(pp_CORE_EX1_312)#OK
	#PresetGame(pp_CORE_EX1_319)#OK
	#PresetGame(pp_CORE_EX1_323)#OK
	#PresetGame(pp_CORE_GIL_191)#OK
	#PresetGame(pp_CORE_ICC_055)#OK
	#PresetGame(pp_CORE_OG_241)#OK
	#PresetGame(pp_CORE_UNG_833)#OK
	#PresetGame(pp_CS3_002)#OK
	#PresetGame(pp_CS3_003)#OK
	PresetGame(pp_CS3_021)#
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


class pp_CORE_EX1_319(Preset_Play):
	""" Flame Imp
	[Battlecry:] Deal 3 damage to your hero. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_319',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.hero
		# hero に３ダメついていること
		for card in [controller.hero]:
			print ("%s: (%d/%d) zone->%s"%(card, card.atk, card.health,card.zone))
		pass

####################


class pp_CORE_EX1_323(Preset_Play):
	""" Lord Jaraxxus
	[Battlecry:] Equip a 3/8 Blood Fury. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_323',controller)#
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
		self.activate_heropower(controller)#
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.hero
		# hero が差し替えられていること
		for card in [controller.hero]:
			print ("%s: (%d/%d) zone->%s"%(card, card.atk, card.health,card.zone))
		# weaponが差し替えられていること
		print ("weapon: %s"%(hero.controller.weapon))
		# ヒロパで召喚されていることを目視
		for card in controller.field:
			print ("%s: (%d/%d) zone->%s"%(card, card.atk, card.health,card.zone))
		pass

####################

class pp_CORE_GIL_191(Preset_Play):
	""" Fiendish Circle
	Summon four 1/1 Imps. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_GIL_191',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.hero
		# フィールドを目視
		for card in controller.field:
			print ("%s: (%d/%d) zone->%s"%(card, card.atk, card.health,card.zone))
		pass

####################

class pp_CORE_ICC_055(Preset_Play):
	""" Drain Soul
	[Lifesteal]Deal $3 damage to a minion. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_ICC_055',controller)#
		self.mark2=self.exchange_card('minionA5',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark2, opponent)#
		self.change_turn(opponent)
		self.change_turn(controller)
		self.attack_card(self.mark2, controller.hero, opponent)#
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller, target=self.mark2)#
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.hero
		# 敵フィールドと自ヒーローを目視
		for card in controller.opponent.field+[controller.hero]:
			print ("%s: (%d/%d) zone->%s"%(card, card.atk, card.health,card.zone))
		pass

####################

class pp_CORE_OG_241(Preset_Play):
	""" Possessed Villager
	[Deathrattle:] Summon a 1/1 Shadowbeast. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_OG_241',controller)#
		self.mark2=self.exchange_card('vanilla',opponent)#
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
		self.play_card(self.mark2, opponent)#
		self.change_turn(opponent)
		##########controller
		self.change_turn(controller)
		##########opponent
		self.attack_card(self.mark2, self.mark1, opponent)#
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.hero
		# 自フィールドを目視
		for card in [self.mark1, self.mark2]:
			print ("%s: (%d/%d) zone->%s"%(card, card.atk, card.health,card.zone))
		for card in controller.field:
			print ("field: %s: (%d/%d) zone->%s"%(card, card.atk, card.health,card.zone))
		pass

####################

class pp_CORE_UNG_833(Preset_Play):
	""" Lakkari Felhound
	[Taunt][Battlecry:] Discard your two lowest-Cost cards. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	count1 = []
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_UNG_833',controller)#
		self.mark2=self.exchange_card('vanilla',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.change_turn(controller)
		self.change_turn(opponent)
		self.count1 = []
		for card in controller.hand:
			self.count1.append(card)
		self.play_card(self.mark1, controller)#
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.hero
		# 自フィールドを目視
		for card in self.count1:
			print ("starting_hand: %s: (%d/**/%d) zone->%s"%(card, card.cost, card.health,card.zone))
		for card in controller.hand:
			print ("hand: %s: (%d/%d) zone->%s"%(card, card.atk, card.health,card.zone))
		pass

####################

class pp_CS3_002(Preset_Play):
	""" Ritual of Doom
	Destroy a friendly minion. If you had 5 or more, summon a 5/5 Demon. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	count1 = []
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CS3_002',controller)#
		self.mark2=self.exchange_card('vanillaH2',controller)#
		self.mark3=self.exchange_card('vanillaH1',controller)#
		self.mark4=self.exchange_card('vanillaH2',controller)#
		self.mark5=self.exchange_card('vanillaH1',controller)#
		self.mark6=self.exchange_card('vanillaH2',controller)#
		super().preset_deck()
		##player1._start_hand_size=7
		##player2._start_hand_size=7
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark2, controller)#
		self.play_card(self.mark3, controller)#
		self.play_card(self.mark4, controller)#
		self.change_turn(controller)
		##########opponent
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark5, controller)#
		self.play_card(self.mark6, controller)#comment out/in
		self.play_card(self.mark1, controller, target=self.mark4)#
		##########opponent
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.hero
		# 自フィールドを目視
		for card in controller.field:
			print ("field: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone))
		pass

####################

class pp_CS3_003(Preset_Play):
	""" Felsoul Jailer
	[Battlecry:] Your opponent discards a minion.[Deathrattle:] Return it. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	count1 = []
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CS3_003',controller)#
		self.mark2=self.exchange_card('vanilla',opponent)#
		self.mark3=self.exchange_card('minionA6',opponent)#
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
		self.play_card(self.mark3, opponent)#
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller, target=self.mark2)#
		self.change_turn(controller)
		##########opponent
		self.attack_card(self.mark3, self.mark1, opponent)

		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.hero
		# 相手フィールドを目視
		for card in controller.opponent.field:
			print ("op. field: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone))
		pass

####################

class pp_CS3_021(Preset_Play):
	""" Enslaved Fel Lord
	[Taunt]. Also damages the minions next to whomever this attacks. """
	class1=CardClass.WARLOCK
	class2=CardClass.WARLOCK
	count1 = []
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CS3_021',controller)#
		self.mark2=self.exchange_card('vanillaH2',opponent)#
		self.mark3=self.exchange_card('vanillaH1',opponent)#
		self.mark4=self.exchange_card('vanillaH2',opponent)#
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
		self.play_card(self.mark2, opponent)#
		self.play_card(self.mark3, opponent)#
		self.play_card(self.mark4, opponent)#
		self.change_turn(opponent)
		##########controller
		self.attack_card(self.mark1, self.mark3, opponent)
		#self.change_turn(controller)
		##########opponent

		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.hero
		# 相手フィールドを目視
		for card in controller.opponent.field:
			print ("op. field: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone))
		pass

####################