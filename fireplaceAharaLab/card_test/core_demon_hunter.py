from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity,CardClass, GameTag, Race

#from fireplace.cards.core.core_hunter import * 
from fireplace.actions import *
from utils import postAction
from fireplace.config import Config

################################

def core_demonhunter():
	## 23.6
	#PresetGame(pp_CORE_BT_035)##
	#PresetGame(pp_CORE_BT_036)##
	#PresetGame(pp_CORE_BT_235)##
	#PresetGame(pp_CORE_BT_271)##### need check
	#PresetGame(pp_CORE_BT_323)### may check
	#PresetGame(pp_CORE_BT_351)##
	#PresetGame(pp_CORE_BT_355)#### not yet #
	#PresetGame(pp_CORE_BT_416)##
	#PresetGame(pp_CORE_BT_427)##
	PresetGame(pp_CORE_BT_429)##
	#PresetGame(pp_CORE_BT_480)##
	#PresetGame(pp_CORE_BT_491)##
	#PresetGame(pp_CORE_BT_801)##
	#PresetGame(pp_CORE_BT_921)##
	#PresetGame(pp_CS3_017)##
	#PresetGame(pp_CS3_019)##
	#PresetGame(pp_CS3_020)## may check it
	pass




################CORE_BT_035#################

class pp_CORE_BT_035(Preset_Play):# <12>[1637]
	""" Chaos Strike
	Give your hero +2_Attack this turn. Draw a card. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_BT_035',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		app='hand'
		for card in getattr(self.player, app):
			self.print_stats(app, card)
		pass
	pass

################CORE_BT_036#################

class pp_CORE_BT_036(Preset_Play):# <12>[1637]
	""" Coordinated Strike
	Summon three 1/1_Illidari with [Rush]. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_BT_036',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		app='hand'
		for card in getattr(self.player, app):
			self.print_stats(app, card)
		pass
	pass

################CORE_BT_235#################

class pp_CORE_BT_235(Preset_Play):# <12>[1637]
	""" Chaos Nova
	Deal $4 damage to all_minions. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_BT_235',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		app='hand'
		for card in getattr(self.player, app):
			self.print_stats(app, card)
		pass
	pass

################CORE_BT_271#################

class pp_CORE_BT_271(Preset_Play):# <12>[1637]
	""" Flamereaper
	Also damages the minions next to whomever your hero_attacks. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_BT_271',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		app='hand'
		for card in getattr(self.player, app):
			self.print_stats(app, card)
		pass
	pass

################CORE_BT_323#################

class pp_CORE_BT_323(Preset_Play):# <12>[1637]
	""" Sightless Watcher
	[Battlecry:] Look at 3 cards in your deck. Choose one to put on top. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_BT_323',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		app='hand'
		for card in getattr(self.player, app):
			self.print_stats(app, card)
		pass
	pass

################CORE_BT_351#################

class pp_CORE_BT_351(Preset_Play):# <12>[1637]
	""" Battlefiend
	After your hero attacks, gain +1 Attack. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_BT_351',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		app='hand'
		for card in getattr(self.player, app):
			self.print_stats(app, card)
		pass
	pass

################CORE_BT_355#################

class pp_CORE_BT_355(Preset_Play):# <12>[1637]
	""" Q
	D """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_BT_355',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		app='hand'
		for card in getattr(self.player, app):
			self.print_stats(app, card)
		pass
	pass

################CORE_BT_416#################

class pp_CORE_BT_416(Preset_Play):# <12>[1637]
	""" Raging Felscreamer
	[Battlecry:] The next Demon you play costs (2) less. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_BT_416',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		app='hand'
		for card in getattr(self.player, app):
			self.print_stats(app, card)
		pass
	pass

################CORE_BT_427#################

class pp_CORE_BT_427(Preset_Play):# <12>[1637]
	""" Feast of Souls
	Draw a card for each friendly minion that died this turn. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_BT_427',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		app='hand'
		for card in getattr(self.player, app):
			self.print_stats(app, card)
		pass
	pass

################CORE_BT_429#################

class pp_CORE_BT_429(Preset_Play):# <12>[1637]
	""" Metamorphosis
	Swap your Hero Power to "Deal 4 damage." After 2 uses, swap it back. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_BT_429',controller)#
		self.mark2=self.exchange_card('minionH2',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark2)
		self.play_card(self.mark1)
		self.activate_heropower(target=self.mark2)
		self.change_turn()
		self.change_turn()
		self.activate_heropower(target=self.mark1)
		self.change_turn()
		self.change_turn()
		assert self.controller.hero.power.id == 'HERO_10bp', "heropower"
		pass
	def result_inspection(self):
		super().result_inspection()
		app='hand'
		for card in getattr(self.player, app):
			self.print_stats(app, card)
		pass
	pass

################CORE_BT_480#################

class pp_CORE_BT_480(Preset_Play):# <12>[1637]
	""" Crimson Sigil Runner
	[Outcast:] Draw a card. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_BT_480',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		app='hand'
		for card in getattr(self.player, app):
			self.print_stats(app, card)
		pass
	pass

################CORE_BT_491#################

class pp_CORE_BT_491(Preset_Play):# <12>[1637]
	""" Spectral Sight
	Draw a card.[Outcast:] Draw another. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_BT_491',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		app='hand'
		for card in getattr(self.player, app):
			self.print_stats(app, card)
		pass
	pass

################CORE_BT_801#################

class pp_CORE_BT_801(Preset_Play):# <12>[1637]
	""" Eye Beam
	[Lifesteal]. Deal $3 damage to a minion.[Outcast:] This costs (1). """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_BT_801',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		app='hand'
		for card in getattr(self.player, app):
			self.print_stats(app, card)
		pass
	pass

################CORE_BT_921#################

class pp_CORE_BT_921(Preset_Play):# <12>[1637]
	""" Aldrachi Warblades
	[Lifesteal] """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_BT_921',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		app='hand'
		for card in getattr(self.player, app):
			self.print_stats(app, card)
		pass
	pass

################CS3_017#################

class pp_CS3_017(Preset_Play):# <12>[1637]
	""" Gan'arg Glaivesmith
	[Outcast:] Give your hero +3_Attack this turn. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CS3_017',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		app='hand'
		for card in getattr(self.player, app):
			self.print_stats(app, card)
		pass
	pass

################CS3_019#################

class pp_CS3_019(Preset_Play):# <12>[1637]
	""" Kor'vas Bloodthorn
	[Charge], [Lifesteal]After you play a card with[Outcast], return this toyour hand. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CS3_019',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		app='hand'
		for card in getattr(self.player, app):
			self.print_stats(app, card)
		pass
	pass

################CS3_020#################

class pp_CS3_020(Preset_Play):# <12>[1637]
	""" Illidari Inquisitor
	[Rush]. After your hero attacks an enemy, this attacks it too. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CS3_020',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		app='hand'
		for card in getattr(self.player, app):
			self.print_stats(app, card)
		pass
	pass

####################################


