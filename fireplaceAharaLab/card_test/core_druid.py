from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity,CardClass, GameTag

from fireplace.cards.core.core_neutral import * 
from fireplace.actions import *

##################################

def core_druid():
	## 23.6
	#PresetGame(pp_CORE_AT_037a)
	#PresetGame(pp_CORE_AT_037b)
	#PresetGame(pp_CORE_AT_037ab)
	#PresetGame(pp_CORE_CS2_009)
	#PresetGame(pp_CORE_CS2_013)
	#PresetGame(pp_CORE_EX1_154a)
	#PresetGame(pp_CORE_EX1_154b)
	#PresetGame(pp_CORE_EX1_154ab)
	#PresetGame(pp_CORE_EX1_158)
	#PresetGame(pp_CORE_EX1_160a)
	#PresetGame(pp_CORE_EX1_160b)
	#PresetGame(pp_CORE_EX1_160ab)
	#PresetGame(pp_CORE_EX1_164a)
	#PresetGame(pp_CORE_EX1_164b)
	#PresetGame(pp_CORE_EX1_164ab)
	#PresetGame(pp_CORE_EX1_165a)
	#PresetGame(pp_CORE_EX1_165b)
	#PresetGame(pp_CORE_EX1_165ab)
	#PresetGame(pp_CORE_EX1_169)
	#PresetGame(pp_CORE_EX1_571)
	#PresetGame(pp_CORE_EX1_573a)
	#PresetGame(pp_CORE_EX1_573b)
	#PresetGame(pp_CORE_EX1_573ab)
	#PresetGame(pp_CORE_LOE_050)
	#PresetGame(pp_CORE_NEW1_008a)
	#PresetGame(pp_CORE_NEW1_008b)
	#PresetGame(pp_CORE_NEW1_008ab)
	#PresetGame(pp_CORE_OG_044)
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
		self.mark2=self.exchange_card('CORE_OG_044',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark2, controller, target=opponent.hero)
		assert controller.choose_both==True, "tag"
		self.play_card(self.mark1, controller, target=opponent.hero)
		print ("check 2 damage on opponent's hero")
		assert opponent.hero.health == 30-2, "damage 2"
		print("check a summoned minion")
		assert len(controller.field)==2+1, "field"
		assert controller.field[-1].id=='AT_037t', "summoned minion 1"
		assert controller.field[-2].id=='AT_037t', "summoned minion 2"
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
		self.mark2=self.exchange_card('noTaunt',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark2, controller)
		self.play_card(self.mark1, controller, target=self.mark2)
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.mark2.taunt==True, "Taunt"
		assert self.mark2.atk==self.mark2.data.atk+2, "atk buff"
		assert self.mark2.health==self.mark2.data.health+3, "health buff" 
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
		controller.max_mana=6
		self.mark1=self.exchange_card('CORE_CS2_013',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		manaN=controller.mana
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		print("check max mana")
		assert controller.max_mana==6+1, "mana"
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
		self.mark2=self.exchange_card("minionH4",opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.change_turn(controller)
		self.play_card(self.mark2, opponent)
		self.change_turn(opponent)
		self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[0], target=self.mark2)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		print("check opponents HP")
		assert self.mark2.health==self.mark2.data.health-3, "3 damage"
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
		self.mark2=self.exchange_card("minionH4",opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.change_turn(controller)
		self.play_card(self.mark2, opponent)
		self.change_turn(opponent)
		for card in controller.hand:
			self.print_stats ("controller.hand", card)
		self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[1], target=self.mark2)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		print("check opponents HP")
		assert self.mark2.health==self.mark2.data.health-1, "3 damage"
		print("check number of hands")
		for card in controller.hand:
			self.print_stats ("controller.hand", card)
		assert len(controller.hand)==4, "check number of hands"
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
		self.mark2=self.exchange_card("minionH5",opponent)
		self.mark3=self.exchange_card('CORE_OG_044',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark3,controller)
		self.change_turn(controller)
		self.play_card(self.mark2, opponent)
		self.change_turn(opponent)
		for card in controller.hand:
			self.print_stats ("controller.hand", card)
		self.play_card(self.mark1, controller, target=self.mark2)
		pass
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		print("check opponents HP")
		assert self.mark2.health==self.mark2.data.health-4, "4 damage"
		print("check number of hands")
		for card in controller.hand:
			self.print_stats ("controller.hand", card)
		assert len(controller.hand)==3, "check number of hands"
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
		self.mark2=self.exchange_card('minionA5',opponent)#
		self.mark3=self.exchange_card('minionH4',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark3, controller)
		self.change_turn(controller)
		self.play_card(self.mark2, opponent)
		self.change_turn(opponent)
		self.play_card(self.mark1, controller)
		print("check if mark3 has deathrattle")
		assert self.mark3.has_deathrattle==True, "deathrattle"
		assert self.mark3.deathrattles!=[], "deathrattle"
		self.change_turn(controller)
		self.attack_card(self.mark2, self.mark3, opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		exist=False
		for card in controller.field:
			self.print_stats ("controller.field", card)
			if card.id=='EX1_158t':
				exist=True
		assert exist==True, "treant"
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
		self.mark1=self.exchange_card('CORE_EX1_160',controller)#
		self.mark2=self.exchange_card('minionH4',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		##########controller
		self.play_card(self.mark2, controller)
		self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[0])		
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.mark2.atk==self.mark2.data.atk+1, "atk"
		assert self.mark2.health==self.mark2.data.health+1, "health"
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
		##########controller
		self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[1])		
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.field:
			self.print_stats ("controller.field", card)
		assert controller.field[-1].id=='EX1_160t', "panther"
		pass
	pass
class pp_CORE_EX1_160ab(Preset_Play):# <12>[1637]
	""" Power of the Wild
	[Choose One -] Give your minions +1/+1; or Summon a 3/2 Panther. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('CORE_EX1_160',controller)#
		self.mark2=self.exchange_card('minionH4',controller)#
		self.mark3=self.exchange_card('CORE_OG_044',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark3, controller)
		self.change_turn(controller)
		self.change_turn(opponent)
		self.play_card(self.mark2, controller)
		self.play_card(self.mark1, controller)		
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		assert self.mark2.atk==self.mark2.data.atk+1, "atk"
		assert self.mark2.health==self.mark2.data.health+1, "health"
		for card in controller.field:
			self.print_stats ("controller.field", card)
		assert controller.field[-1].id=='EX1_160t', "panther"
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
		controller.max_mana=6
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		##########controller
		self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[0])
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		print("count max mana")
		assert controller.max_mana==6+2, "max mana"
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
		self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[1])
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		print("more three hand cards")
		for card in controller.hand:
			self.print_stats ("controller.hand", card)
		assert len(controller.hand)==6, "hand cards"
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
		self.mark3=self.exchange_card('CORE_OG_044',controller)#
		controller.max_mana=6
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark3, controller)
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		print("count max mana")
		assert controller.max_mana==6+2, "max mana"
		print("more three hand cards")
		for card in controller.hand:
			self.print_stats ("controller.hand", card)
		assert len(controller.hand)==5, "hand cards"
		pass
	pass
################CORE_EX1_165##################

class pp_CORE_EX1_165a(Preset_Play):# <12>[1637]
	""" Druid of the Claw
	[Choose One -] Transform into a 5/4 with [Rush];or a 5/6 with [Taunt]. """
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
		self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[0])
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card = controller.field[0]
		assert card.atk==5, "atk"
		assert card.health==4, "health"
		assert card.rush==True, "rush"
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
		self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[1])
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card = controller.field[0]
		assert card.atk==5, "atk"
		assert card.health==6, "health"
		assert card.taunt==True, "taunt"
		pass
	pass
class pp_CORE_EX1_165ab(Preset_Play):# <12>[1637]
	""" Druid of the Claw
	[Choose One -] Transform into a 5/4 with [Rush];or a 5/6 with [Taunt]. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_165',controller)#
		self.mark3=self.exchange_card('CORE_OG_044',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark3, controller)
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.field:
			self.print_stats ("controller.field", card)
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
		self.mark1=self.exchange_card('CORE_EX1_169',controller)#
		controller.max_mana=6
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		assert controller.mana == 6 - self.mark1.cost + 1, "mana"
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
		self.mark1=self.exchange_card('CORE_EX1_571',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.field:
			self.print_stats("field", card)
		assert controller.field[-1].id=='EX1_158t', "treant"
		assert controller.field[-2].id=='EX1_158t', "treant"
		assert controller.field[-3].id=='EX1_158t', "treant"
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
		self.mark2=self.exchange_card('minionH4',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark2, controller)
		self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[0])
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.mark2.atk==self.mark2.data.atk+2, "atk"
		assert self.mark2.health==self.mark2.data.health+2, "health"
		pass
	pass
class pp_CORE_EX1_573b(Preset_Play):# <12>[1637]
	""" Cenarius
	[Choose One -] Give your other minions +2/+2; or Summon two 2/2 Treants with [Taunt]. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('CORE_EX1_573',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		##########controller
		self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[1])
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		id1=id2=-1
		for card in controller.field:
			self.print_stats("field", card)
			if card.id=='EX1_573t':
				if id1==-1:
					id1 = controller.field.index(card)
				else:
					id2 = controller.field.index(card)
		assert id2!=-1, "two treants"
		assert controller.field[id1].id=='EX1_573t', "treant"
		assert controller.field[id2].id=='EX1_573t', "treant"
		assert controller.field[id1].taunt==True, "taune"
		assert controller.field[id2].taunt==True, "taune"
		pass
	pass
class pp_CORE_EX1_573ab(Preset_Play):# <12>[1637]
	""" Cenarius
	[Choose One -] Give your other minions +2/+2; or Summon two 2/2 Treants with [Taunt]. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player

		self.mark1=self.exchange_card('CORE_EX1_573',controller)#
		self.mark2=self.exchange_card('minionH4',controller)#
		self.mark3=self.exchange_card('CORE_OG_044',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		##########controller
		self.play_card(self.mark3, controller)
		self.play_card(self.mark2, controller)
		self.change_turn(controller)
		self.change_turn(controller.opponent)
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		assert self.mark2.buff!=[], "buff"
		assert self.mark2.atk==self.mark2.data.atk+2, "atk"
		assert self.mark2.health==self.mark2.data.health+2, "health"
		id1=id2=-1
		for card in controller.field:
			self.print_stats("field", card)
			if card.id=='EX1_573t':
				if id1==-1:
					id1 = controller.field.index(card)
				else:
					id2 = controller.field.index(card)
		assert id2!=-1, "two treants"
		assert controller.field[id1].id=='EX1_573t', "treant"
		assert controller.field[id2].id=='EX1_573t', "treant"
		assert controller.field[id1].taunt==True, "taune"
		assert controller.field[id2].taunt==True, "taune"
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
		self.mark2=self.exchange_card('minionA4',opponent)#
		self.mark3=self.exchange_card('minionA4',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.change_turn(controller)
		self.play_card(self.mark2, opponent)
		self.play_card(self.mark3, opponent)
		self.change_turn(opponent)
		self.play_card(self.mark1, controller)
		self.change_turn(controller)
		self.attack_card(self.mark3, self.mark1, opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.field:
			self.print_stats("field", card)
		assert controller.field[-1].cost==1, "cost"
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
		##########controller
		self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[0])
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("hand", card)
		assert len(controller.hand)==5, "hand cards"
		
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

		##########controller
		Hit(controller.hero, 10).trigger(self.mark1)
		self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[1], target=controller.hero)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.hero
		assert hero.health==30-10+5, "health"
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
		self.mark3=self.exchange_card('CORE_OG_044',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark3, controller)
		Hit(controller.hero, 10).trigger(self.mark1)
		self.play_card(self.mark1, controller, target=controller.hero)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("hand", card)
		assert len(controller.hand)==4, "hand cards"
		hero = controller.hero
		assert hero.health==30-10+5, "health"
		pass
	pass
###############CORE_OG_044###################

class pp_CORE_OG_044(Preset_Play):# <12>[1637](4/3/5)
	""" Fandral Staghelm
	Your [Choose One] cards and powers have both effects combined. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_OG_044',controller)#
		self.mark2=self.exchange_card('CORE_NEW1_008',controller)#
		self.mark3=self.exchange_card('minionA5',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)
		assert controller.choose_both==True, "buff"
		assert controller.game.active_aura_buffs!=[], "aura-buff"
		self.change_turn(controller)
		self.play_card(self.mark3,opponent)
		self.change_turn(opponent)
		self.change_turn(controller)
		self.attack_card(self.mark3, self.mark1, opponent)
		self.change_turn(opponent)
		assert controller.game.active_aura_buffs==[], "aura-buff"
		assert controller.choose_both==False, "buff"
		self.play_card(self.mark2, controller)
		
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player

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






