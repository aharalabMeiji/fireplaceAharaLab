from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity,CardClass, GameTag

from fireplace.cards.core.core_neutral import * 
from fireplace.actions import *

##################################

def core_druid():
	## 23.6
	#PresetGame(pp_CORE_AT_037a)
	#PresetGame(pp_CORE_AT_037b)
	PresetGame(pp_CORE_AT_037ab)
	PresetGame(pp_CORE_CS2_009)
	PresetGame(pp_CORE_CS2_013)
	PresetGame(pp_CORE_EX1_154a)
	PresetGame(pp_CORE_EX1_154b)
	PresetGame(pp_CORE_EX1_154ab)
	PresetGame(pp_CORE_EX1_158)
	PresetGame(pp_CORE_EX1_160a)
	PresetGame(pp_CORE_EX1_160b)
	PresetGame(pp_CORE_EX1_160ab)
	PresetGame(pp_CORE_EX1_164a)
	PresetGame(pp_CORE_EX1_164b)
	PresetGame(pp_CORE_EX1_164ab)
	PresetGame(pp_CORE_EX1_165a)
	PresetGame(pp_CORE_EX1_165b)
	PresetGame(pp_CORE_EX1_165ab)
	PresetGame(pp_CORE_EX1_169)
	PresetGame(pp_CORE_EX1_571)
	PresetGame(pp_CORE_EX1_573a)
	PresetGame(pp_CORE_EX1_573b)
	PresetGame(pp_CORE_EX1_573ab)
	PresetGame(pp_CORE_LOE_050)
	PresetGame(pp_CORE_NEW1_008a)
	PresetGame(pp_CORE_NEW1_008b)
	PresetGame(pp_CORE_NEW1_008ab)
	PresetGame(pp_CORE_OG_044)
	PresetGame(pp_CORE_OG_047a)
	PresetGame(pp_CORE_OG_047b)
	PresetGame(pp_CORE_OG_047ab)
	PresetGame(pp_CORE_TRL_243)
	PresetGame(pp_CORE_UNG_108)
	PresetGame(pp_CS3_012)
	## 22.6
##############CORE_AT_037###################

class pp_CORE_AT_037a(Preset_Play):# <12>[1637]
	""" Living Roots
	[Choose One -] Deal $2 damage; or Summon two 1/1 Saplings. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_037',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[0], target=opponent.hero)
		print ("check 2 damage on opponent's hero")
		assert opponent.hero.health == 30-2, "damage 2"
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass

class pp_CORE_AT_037b(Preset_Play):# <12>[1637]
	""" Living Roots
	[Choose One -] Deal $2 damage; or Summon two 1/1 Saplings. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_037',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[1])
		print("check a summoned minion")
		assert len(controller.field)==2, "field"
		assert controller.field[0].id=='AT_037t', "summoned minion 1"
		assert controller.field[1].id=='AT_037t', "summoned minion 2"
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
class pp_CORE_AT_037ab(Preset_Play):# <12>[1637]
	""" Living Roots
	[Choose One -] Deal $2 damage; or Summon two 1/1 Saplings. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_037',controller)#
		#setattr(controller,'choose_both', True)
		controller.tags[GameTag.CHOOSE_BOTH]=True
		controller.choose_both=True
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller, target=opponent.hero)
		print ("check 2 damage on opponent's hero")
		assert opponent.hero.health == 30-2, "damage 2"
		print("check a summoned minion")
		assert len(controller.field)==2, "field"
		assert controller.field[0].id=='AT_037t', "summoned minion 1"
		assert controller.field[1].id=='AT_037t', "summoned minion 2"
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass#################CORE_CS2_009#################

class pp_CORE_CS2_009(Preset_Play):# <12>[1637]
	""" Mark of the Wild
	Give a minion [Taunt] and +2/+3.<i>(+2 Attack/+3 Health)</i> """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_009',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
################CORE_CS2_013##################

class pp_CORE_CS2_013(Preset_Play):# <12>[1637]
	""" Wild Growth
	Gain an empty Mana Crystal. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_013',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
##################CORE_EX1_154################

class pp_CORE_EX1_154a(Preset_Play):# <12>[1637]
	""" Wrath
	[Choose One -]Deal $3 damage to a minion; or $1 damageand draw a card. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_154',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
class pp_CORE_EX1_154b(Preset_Play):# <12>[1637]
	""" Wrath
	[Choose One -]Deal $3 damage to a minion; or $1 damageand draw a card. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_154',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
class pp_CORE_EX1_154ab(Preset_Play):# <12>[1637]
	""" Wrath
	[Choose One -]Deal $3 damage to a minion; or $1 damageand draw a card. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_154',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
#################CORE_EX1_158#################

class pp_CORE_EX1_158(Preset_Play):# <12>[1637]
	""" Soul of the Forest
	Give your minions "[Deathrattle:] Summon a 2/2 Treant." """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_158',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
################CORE_EX1_160##################

class pp_CORE_EX1_160a(Preset_Play):# <12>[1637]
	""" Power of the Wild
	[Choose One -] Give your minions +1/+1; or Summon a 3/2 Panther. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_160',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
class pp_CORE_EX1_160b(Preset_Play):# <12>[1637]
	""" Power of the Wild
	[Choose One -] Give your minions +1/+1; or Summon a 3/2 Panther. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_160',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
class pp_CORE_EX1_160ab(Preset_Play):# <12>[1637]
	""" Power of the Wild
	[Choose One -] Give your minions +1/+1; or Summon a 3/2 Panther. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_160',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
################CORE_EX1_164##################

class pp_CORE_EX1_164a(Preset_Play):# <12>[1637]
	""" Nourish
	[Choose One -] Gain 2_Mana Crystals; or Draw 3 cards. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_164',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
class pp_CORE_EX1_164b(Preset_Play):# <12>[1637]
	""" Nourish
	[Choose One -] Gain 2_Mana Crystals; or Draw 3 cards. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_164',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
class pp_CORE_EX1_164ab(Preset_Play):# <12>[1637]
	""" Nourish
	[Choose One -] Gain 2_Mana Crystals; or Draw 3 cards. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_164',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
################CORE_EX1_165##################

class pp_CORE_EX1_165a(Preset_Play):# <12>[1637]
	""" Druid of the Claw
	[Choose One -] Transforminto a 5/4 with [Rush];or a 5/6 with [Taunt]. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_165',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
class pp_CORE_EX1_165b(Preset_Play):# <12>[1637]
	""" Druid of the Claw
	[Choose One -] Transforminto a 5/4 with [Rush];or a 5/6 with [Taunt]. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_165',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
class pp_CORE_EX1_165ab(Preset_Play):# <12>[1637]
	""" Druid of the Claw
	[Choose One -] Transforminto a 5/4 with [Rush];or a 5/6 with [Taunt]. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_165',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
################CORE_EX1_169##################

class pp_CORE_EX1_169(Preset_Play):# <12>[1637]
	""" Innervate
	Gain 1 Mana Crystal this turn only. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_169',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
################CORE_EX1_571##################

class pp_CORE_EX1_571(Preset_Play):# <12>[1637]
	""" Force of Nature
	Summon three 2/2 Treants. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_571',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
################CORE_EX1_573##################

class pp_CORE_EX1_573a(Preset_Play):# <12>[1637]
	""" Cenarius
	[Choose One -] Give your other minions +2/+2; or Summon two 2/2 Treants with [Taunt]. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_573',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
class pp_CORE_EX1_573b(Preset_Play):# <12>[1637]
	""" Cenarius
	[Choose One -] Give your other minions +2/+2; or Summon two 2/2 Treants with [Taunt]. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_573',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
class pp_CORE_EX1_573ab(Preset_Play):# <12>[1637]
	""" Cenarius
	[Choose One -] Give your other minions +2/+2; or Summon two 2/2 Treants with [Taunt]. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_573',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
###############CORE_LOE_050###################

class pp_CORE_LOE_050(Preset_Play):# <12>[1637]
	""" Mounted Raptor
	[Deathrattle:] Summon a random 1-Cost minion. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_LOE_050',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
################CORE_NEW1_008##################

class pp_CORE_NEW1_008a(Preset_Play):# <12>[1637]
	""" Ancient of Lore
	[Choose One -] Draw 2 cards; or Restore #5 Health. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_NEW1_008',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
class pp_CORE_NEW1_008b(Preset_Play):# <12>[1637]
	""" Ancient of Lore
	[Choose One -] Draw 2 cards; or Restore #5 Health. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_NEW1_008',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
class pp_CORE_NEW1_008ab(Preset_Play):# <12>[1637]
	""" Ancient of Lore
	[Choose One -] Draw 2 cards; or Restore #5 Health. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_NEW1_008',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
###############CORE_OG_044###################

class pp_CORE_OG_044(Preset_Play):# <12>[1637]
	""" Fandral Staghelm
	Your [Choose One] cards and powers have both effects combined. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_OG_044',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
###############CORE_OG_047###################

class pp_CORE_OG_047a(Preset_Play):# <12>[1637]
	""" Feral Rage
	[Choose One -] Give your hero +4 Attack this turn; or Gain 8 Armor. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_OG_047',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
class pp_CORE_OG_047b(Preset_Play):# <12>[1637]
	""" Feral Rage
	[Choose One -] Give your hero +4 Attack this turn; or Gain 8 Armor. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_OG_047',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
class pp_CORE_OG_047ab(Preset_Play):# <12>[1637]
	""" Feral Rage
	[Choose One -] Give your hero +4 Attack this turn; or Gain 8 Armor. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_OG_047',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
###############CORE_TRL_243###################

class pp_CORE_TRL_243(Preset_Play):# <12>[1637]
	""" Pounce
	Give your hero +2_Attack this turn. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_TRL_243',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass###############CORE_UNG_108###################

class pp_CORE_UNG_108(Preset_Play):# <12>[1637]
	""" Earthen Scales
	Give a friendly minion +1/+1, then gain Armor equal to its Attack. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_UNG_108',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
###############CS3_012###################

class pp_CS3_012(Preset_Play):# <12>[1637]
	""" Nordrassil Druid
	[Battlecry:] The next spell you cast this turn costs_(3)_less. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CS3_012',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		pass
	pass
##################################






