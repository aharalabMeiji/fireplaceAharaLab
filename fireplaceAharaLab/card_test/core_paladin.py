from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity,CardClass, GameTag

from fireplace.actions import *
from utils import postAction
from fireplace.config import Config


##################################

def core_paladin():
	## 23.6
	#PresetGame(pp_CORE_AT_075)
	#PresetGame(pp_CORE_CS2_092)
	#PresetGame(pp_CORE_CS2_093)
	#PresetGame(pp_CORE_CS2_097)
	#PresetGame(pp_CORE_DRG_226)
	#PresetGame(pp_CORE_DRG_229)
	#PresetGame(pp_CORE_EX1_130)
	#PresetGame(pp_CORE_EX1_362)
	#PresetGame(pp_CORE_EX1_382)
	#PresetGame(pp_CORE_EX1_383)
	#PresetGame(pp_CORE_EX1_619)
	#PresetGame(pp_CORE_FP1_020)
	#PresetGame(pp_CORE_ICC_038)
	#PresetGame(pp_CORE_OG_229)
	#PresetGame(pp_CORE_OG_273)
	#PresetGame(pp_CORE_TRL_307)
	PresetGame(pp_CS3_016) ## need check -> ## OKOK
	## 22.6
	#PresetGame(CORE_CS2_088)
	#PresetGame(CORE_CS2_089)
	#PresetGame(CS3_029)


	pass

################CORE_AT_075#################

class pp_CORE_AT_075(Preset_Play):# <12>[1637]
	""" Warhorse Trainer
	Your Silver Hand Recruits have +1 Attack. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('CORE_AT_075',controller)#
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


################CORE_CS2_092#################

class pp_CORE_CS2_092(Preset_Play):# <12>[1637]
	""" Blessing of Kings
	Give a minion +4/+4. <i>(+4 Attack/+4 Health)</i> """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('CORE_CS2_092',controller)#
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

################CORE_CS2_093#################

class pp_CORE_CS2_093(Preset_Play):# <12>[1637]
	""" Consecration
	Deal $2 damage to all enemies. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('CORE_CS2_093',controller)#
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

################CORE_CS2_097#################

class pp_CORE_CS2_097(Preset_Play):# <12>[1637]
	""" Truesilver Champion
	Whenever your hero attacks, restore #2_Health to it. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('CORE_CS2_097',controller)#
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

################CORE_DRG_226#################

class pp_CORE_DRG_226(Preset_Play):# <12>[1637]
	""" Amber Watcher
	[Battlecry:] Restore #8_Health. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('CORE_DRG_226',controller)#
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

################CORE_DRG_229#################

class pp_CORE_DRG_229(Preset_Play):# <12>[1637]
	""" Bronze Explorer
	[Lifesteal][Battlecry:] [Discover] a Dragon. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('CORE_DRG_229',controller)#
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

################CORE_EX1_130#################

class pp_CORE_EX1_130(Preset_Play):# <12>[1637]
	""" Noble Sacrifice
	[Secret:] When an enemy attacks, summon a 2/1 Defender as the new target. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('CORE_EX1_130',controller)#
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

################CORE_EX1_362#################

class pp_CORE_EX1_362(Preset_Play):# <12>[1637]
	""" Argent Protector
	[Battlecry:] Give a friendly minion [Divine Shield]. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('CORE_EX1_362',controller)#
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

################CORE_EX1_382#################

class pp_CORE_EX1_382(Preset_Play):# <12>[1637]
	""" Aldor Peacekeeper
	[Battlecry:] Change an_enemy minion's Attack to 1. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('CORE_EX1_382',controller)#
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

################CORE_EX1_383#################

class pp_CORE_EX1_383(Preset_Play):# <12>[1637]
	""" Tirion Fordring
	[[Divine Shield],] [Taunt] [Deathrattle:] Equip a 5/3_Ashbringer. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('CORE_EX1_383',controller)#
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

################CORE_EX1_619#################

class pp_CORE_EX1_619(Preset_Play):# <12>[1637]
	""" Equality
	Change the Health of ALL minions to 1. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('CORE_EX1_619',controller)#
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

################CORE_FP1_020#################

class pp_CORE_FP1_020(Preset_Play):# <12>[1637]
	""" Avenge
	[Secret:] When one of your minions dies, give a random friendly minion +3/+2. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('CORE_FP1_020',controller)#
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

################CORE_ICC_038#################

class pp_CORE_ICC_038(Preset_Play):# <12>[1637]
	""" Righteous Protector
	[Taunt][Divine Shield] """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('CORE_ICC_038',controller)#
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

################CORE_OG_229#################

class pp_CORE_OG_229(Preset_Play):# <12>[1637]
	""" Ragnaros, Lightlord
	At the end of your turn, restore #8 Health to a damaged friendly character. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('CORE_OG_229',controller)#
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

################CORE_OG_273#################

class pp_CORE_OG_273(Preset_Play):# <12>[1637]
	""" Stand Against Darkness
	Summon five 1/1 Silver Hand Recruits. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('CORE_OG_273',controller)#
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

################CORE_TRL_307#################

class pp_CORE_TRL_307(Preset_Play):# <12>[1637]
	""" Flash of Light
	Restore #4 Health. Draw a card. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('CORE_TRL_307',controller)#
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

################CS3_016#################

class pp_CS3_016(Preset_Play):# <12>[1637]
	""" Reckoning
	[Secret:] After an enemy minion deals 3 or more damage, destroy it. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CS3_016',controller)#
		self.mark2=self.exchange_card('minionH4',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller=self.player
		opponent = controller.opponent
		### con
		self.play_card(self.mark1)
		self.change_turn(controller)
		### opp
		self.play_card(self.mark2)
		self.change_turn(opponent)
		### con
		self.change_turn(controller)
		### opp
		self.attack_card(self.mark2, self.player.hero, opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.mark1.zone==Zone.GRAVEYARD, "zone"
		assert self.mark2.zone==Zone.GRAVEYARD, "zone"
		pass
	pass

################XXXX#################


