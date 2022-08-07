from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity, CardClass

def core_warrior():
	## 23.6
	PresetGame(pp_CORE_AT_064)##new
	#PresetGame(pp_CORE_CS2_106)
	#PresetGame(pp_CORE_CS2_108)
	#PresetGame(pp_CORE_EX1_391)
	#PresetGame(pp_CORE_EX1_400)
	#PresetGame(pp_CORE_EX1_402)
	#PresetGame(pp_CORE_EX1_407)
	#PresetGame(pp_CORE_EX1_410)
	#PresetGame(pp_CORE_EX1_411)
	PresetGame(pp_CORE_EX1_414)###difficult
	#PresetGame(pp_CORE_EX1_603)
	#PresetGame(pp_CORE_EX1_604)
	PresetGame(pp_CORE_EX1_606)##new
	PresetGame(pp_CORE_GIL_547)##new
	#PresetGame(pp_CORE_GVG_053)
	PresetGame(pp_CORE_OG_218)##new
	#PresetGame(pp_CS3_008)
	##22.6
	#CORE_EX1_084
	#CS3_009
	#CS3_030

	pass
###############CORE_AT_064###################

class pp_CORE_AT_064(Preset_Play):# <6>[1637]
	""" Bash
	Deal $3 damage.Gain 3 Armor. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_064',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.player.field:
			self.print_stats ("field", card)
		pass

###############CORE_CS2_106###################

class pp_CORE_CS2_106(Preset_Play):# <6>[1637]
	""" Fiery War Axe
	 """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_106',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.player.field:
			self.print_stats ("field", card)
		pass

###############CORE_CS2_108###################

class pp_CORE_CS2_108(Preset_Play):# <6>[1637]
	""" Execute
	Destroy a damaged enemy minion. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_108',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.player.field:
			self.print_stats ("field", card)
		pass

###############CORE_EX1_391###################

class pp_CORE_EX1_391(Preset_Play):# <6>[1637]
	""" Slam
	Deal $2 damage to a minion. If it survives, draw a card. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_391',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.player.field:
			self.print_stats ("field", card)
		pass

###############CORE_EX1_400###################

class pp_CORE_EX1_400(Preset_Play):# <6>[1637]
	""" Whirlwind
	Deal $1 damage to ALL_minions. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_400',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.player.field:
			self.print_stats ("field", card)
		pass

###############CORE_EX1_402###################

class pp_CORE_EX1_402(Preset_Play):# <6>[1637]
	""" Armorsmith
	Whenever a friendly minion_takes damage, gain 1 Armor. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_402',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.player.field:
			self.print_stats ("field", card)
		pass

###############CORE_EX1_407###################

class pp_CORE_EX1_407(Preset_Play):# <6>[1637]
	""" Brawl
	Destroy all minions except one. <i>(chosen randomly)</i> """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_407',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.player.field:
			self.print_stats ("field", card)
		pass

###############CORE_EX1_410###################

class pp_CORE_EX1_410(Preset_Play):# <6>[1637]
	""" Shield Slam
	Deal 1 damage to a minion for each Armor you have. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_410',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.player.field:
			self.print_stats ("field", card)
		pass

###############CORE_EX1_411###################

class pp_CORE_EX1_411(Preset_Play):# <6>[1637]
	""" Brightwing
	[Battlecry:] Add a random [Legendary] minion to your_hand. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_411',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark1, controller)
		self.attack_card(controller.hero, opponent.hero,controller)
		self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark3, opponent)#
		self.change_turn(opponent)
		##########controller
		self.attack_card(controller.hero, opponent.hero,controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.opponent.hero
		self.print_stats("weapon",self.mark1)
		for card in [controller.hero, controller.opponent.hero]:
			self.print_stats ("controller.hero", card)
		pass

###############CORE_EX1_414###################

class pp_CORE_EX1_414(Preset_Play):# <6>[1637]
	""" Grommash Hellscream
	[Charge]Has +6 Attack while damaged. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_414',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.player.field:
			self.print_stats ("field", card)
		pass

###############CORE_EX1_603###################

class pp_CORE_EX1_603(Preset_Play):# <6>[1637]
	""" Cruel Taskmaster
	[Battlecry:] Deal 1 damage to a minion and give it +2_Attack. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_603',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.player.field:
			self.print_stats ("field", card)
		pass

###############CORE_EX1_604###################

class pp_CORE_EX1_604(Preset_Play):# <6>[1637]
	""" Frothing Berserker
	Whenever a minion takes damage, gain +1 Attack. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_604',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.player.field:
			self.print_stats ("field", card)
		pass

###############CORE_EX1_606###################

class pp_CORE_EX1_606(Preset_Play):# <6>[1637]
	""" Shield Block
	Gain 5 Armor.Draw a card. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_606',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.player.field:
			self.print_stats ("field", card)
		pass

###############CORE_GIL_547###################

class pp_CORE_GIL_547(Preset_Play):# <6>[1637]
	""" Darius Crowley
	[Rush]After this attacks and killsa minion, gain +2/+2. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_GIL_547',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.player.field:
			self.print_stats ("field", card)
		pass

###############CORE_GVG_053###################

class pp_CORE_GVG_053(Preset_Play):# <6>[1637]
	""" Shieldmaiden
	[Battlecry:] Gain 5 Armor. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_GVG_053',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.player.field:
			self.print_stats ("field", card)
		pass

###############CORE_OG_218###################

class pp_CORE_OG_218(Preset_Play):# <6>[1637]
	""" Bloodhoof Brave
	[Taunt]Has +3 Attack while damaged. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_OG_218',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.player.field:
			self.print_stats ("field", card)
		pass

###############CS3_008###################

class pp_CS3_008(Preset_Play):# <6>[1637]
	""" Bloodsail Deckhand
	[Battlecry:] The nextweapon you play costs(1) less. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CS3_008',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.player.field:
			self.print_stats ("field", card)
		pass

###############XXXX###################

class pp_(Preset_Play):# <6>[1637]
	""" g
	d. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.player.field:
			self.print_stats ("field", card)
		pass


##################################


##################################

