from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity,CardClass, GameTag

from fireplace.actions import *
from utils import postAction
from fireplace.config import Config


##################################

def core_druid():
	## 23.6
	#PresetGame(pp_CORE_BOT_453)
	#PresetGame(pp_CORE_CS2_023)
	#PresetGame(pp_CORE_CS2_028)
	#PresetGame(pp_CORE_CS2_029)
	#PresetGame(pp_CORE_CS2_032)
	#PresetGame(pp_CORE_DAL_609)
	#PresetGame(pp_CORE_EX1_275)
	#PresetGame(pp_CORE_EX1_279)
	#PresetGame(pp_CORE_EX1_287)
	#PresetGame(pp_CORE_EX1_289)
	#PresetGame(pp_CORE_GIL_801)
	#PresetGame(pp_CORE_KAR_009)
	#PresetGame(pp_CORE_LOE_003)
	#PresetGame(pp_CORE_LOOT_101)
	#PresetGame(pp_CORE_TRL_315)
	#PresetGame(pp_CORE_UNG_020)
	PresetGame(pp_CS3_001)
	## 22.6

	pass

##################################

################CORE_BOT_453#################

class pp_CORE_BOT_453(Preset_Play):# <12>[1637]
	""" Shooting Star
	Deal $1 damage to a minion and the minions next to it. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_BOT_453',controller)#
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
		pass
	pass

################CORE_CS2_023#################

class pp_CORE_CS2_023(Preset_Play):# <12>[1637]
	""" Arcane Intellect
	Draw 2 cards. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_023',controller)#
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
		pass
	pass

################CORE_CS2_028#################

class pp_CORE_CS2_028(Preset_Play):# <12>[1637]
	""" Blizzard
	Deal $2 damage to all enemy minions and [Freeze] them. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_028',controller)#
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
		pass
	pass

################CORE_CS2_029#################

class pp_CORE_CS2_029(Preset_Play):# <12>[1637]
	""" Fireball
	Deal $6 damage. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_029',controller)#
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
		pass
	pass

################CORE_CS2_032#################

class pp_CORE_CS2_032(Preset_Play):# <12>[1637]
	""" Flamestrike
	Deal $5 damage to all enemy minions. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_032',controller)#
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
		pass
	pass

################CORE_DAL_609#################

class pp_CORE_DAL_609(Preset_Play):# <12>[1637]
	""" Kalecgos
	Your first spell each turn costs (0).[Battlecry:] [Discover]a spell. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_DAL_609',controller)#
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
		pass
	pass

################CORE_EX1_275#################

class pp_CORE_EX1_275(Preset_Play):# <12>[1637]
	""" Cone of Cold
	[Freeze] a minion and the minions next to it, and deal $1 damage to them. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_275',controller)#
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
		pass
	pass

################CORE_EX1_279#################

class pp_CORE_EX1_279(Preset_Play):# <12>[1637]
	""" Pyroblast
	Deal $10 damage. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_279',controller)#
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
		pass
	pass

################CORE_EX1_287#################

class pp_CORE_EX1_287(Preset_Play):# <12>[1637]
	""" Counterspell
	[Secret:] When your opponent casts a spell, [Counter] it. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_287',controller)#
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
		pass
	pass

################CORE_EX1_289#################

class pp_CORE_EX1_289(Preset_Play):# <12>[1637]
	""" Ice Barrier
	[Secret:] When your hero is attacked, gain 8 Armor. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_289',controller)#
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
		pass
	pass

################CORE_GIL_801#################

class pp_CORE_GIL_801(Preset_Play):# <12>[1637]
	""" Snap Freeze
	[Freeze] a minion.If it's already [Frozen], destroy it. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_GIL_801',controller)#
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
		pass
	pass

################CORE_KAR_009#################

class pp_CORE_KAR_009(Preset_Play):# <12>[1637]
	""" Babbling Book
	[Battlecry:] Add a random Mage spell to your hand. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_KAR_009',controller)#
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
		pass
	pass

################CORE_LOE_003#################

class pp_CORE_LOE_003(Preset_Play):# <12>[1637]
	""" Ethereal Conjurer
	[Battlecry: Discover] a spell. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_LOE_003',controller)#
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
		pass
	pass

################CORE_LOOT_101#################

class pp_CORE_LOOT_101(Preset_Play):# <12>[1637]
	""" Explosive Runes
	[Secret:] After your opponent plays a minion, deal $6 damage to it and any excess to their hero. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_LOOT_101',controller)#
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
		pass
	pass

################CORE_TRL_315#################

class pp_CORE_TRL_315(Preset_Play):# <12>[1637]
	""" Pyromaniac
	Whenever your Hero Power_kills a minion, draw a card. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_TRL_315',controller)#
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
		pass
	pass

################CORE_UNG_020#################

class pp_CORE_UNG_020(Preset_Play):# <12>[1637]
	""" Arcanologist
	[Battlecry:] Draw a [Secret]. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_UNG_020',controller)#
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
		pass
	pass

################CS3_001#################

class pp_CS3_001(Preset_Play):# <12>[1637]
	""" Aegwynn, the Guardian
	[Spell Damage +2][Deathrattle:] The next minion_you draw inherits these powers. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CS3_001',controller)#
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
		pass
	pass

######################################
