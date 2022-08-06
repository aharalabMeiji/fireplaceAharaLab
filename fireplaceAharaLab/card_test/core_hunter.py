from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity,CardClass, GameTag

#from fireplace.cards.core.core_hunter import * 
from fireplace.actions import *
from utils import postAction

##################################

def core_hunter():
	## 23.6
	#PresetGame(pp_CORE_BRM_013x)
	#PresetGame(pp_CORE_BRM_013y)
	#PresetGame(pp_CORE_DAL_371)
	#PresetGame(pp_CORE_DS1_184)
	#PresetGame(pp_CORE_DS1_185)
	#PresetGame(pp_CORE_EX1_534)
	#PresetGame(pp_CORE_EX1_543)
	#PresetGame(pp_CORE_EX1_554)
	#PresetGame(pp_CORE_EX1_610)
	#PresetGame(pp_CORE_EX1_611)
	PresetGame(pp_CORE_EX1_617)
	PresetGame(pp_CORE_GIL_650)
	PresetGame(pp_CORE_GIL_828)
	PresetGame(pp_CORE_KAR_006)
	PresetGame(pp_CORE_LOOT_222)
	PresetGame(pp_CORE_NEW1_031)
	PresetGame(pp_NEW1_033)
	PresetGame(pp_CORE_TRL_348)
	PresetGame(pp_CS3_015)
	## 22.6
	#PresetGame(pp_CORE_AT_061)
	#PresetGame(pp_CORE_EX1_531)
	#PresetGame(pp_CORE_FP1_011)
	#PresetGame(pp_CORE_ICC_419)
	#PresetGame(pp_CORE_TRL_111)

################CORE_BRM_013#################

class pp_CORE_BRM_013x(Preset_Play):# <12>[1637]
	""" Quick Shot
	Deal $3 damage.If your hand is empty, draw a card. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_BRM_013',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########controller
		self.play_card(self.mark1, target=self.player.opponent.hero)
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.player.opponent.hero.health==30-3, "damage"
		pass
	pass
class pp_CORE_BRM_013y(Preset_Play):# <12>[1637]
	""" Quick Shot
	Deal $3 damage.If your hand is empty, draw a card. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_BRM_013',controller)#
		for card in self.player.hand:
			self.print_stats("hand", card)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########controller
		self.play_card(self.player.hand[0])
		self.play_card(self.player.hand[0])
		self.change_turn()
		self.change_turn()
		self.play_card(self.player.hand[0])
		self.play_card(self.mark1, target=self.player.opponent.hero)
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.player.opponent.hero.health==30-3, "damage"
		for card in self.player.hand:
			self.print_stats("hand", card)
		assert len(self.player.hand)==1, "hand"
		pass
	pass

################CORE_DAL_371#################

class pp_CORE_DAL_371(Preset_Play):# <12>[1637]
	""" Marked Shot
	Deal $4 damage to_a_minion. [Discover]_a_spell. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.controller=self.player
		self.opponent = self.controller.opponent
		self.mark1=self.exchange_card('CORE_DAL_371',self.controller)#
		self.mark2=self.exchange_card('minionH5',self.opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########controller
		self.change_turn()
		### opp
		self.play_card(self.mark2)
		self.change_turn()
		### con
		self.play_card(self.mark1, target=self.mark2)
		postAction(self.controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.mark2.health==5-4, "health=%d"%(self.mark2.health)
		assert self.controller.hand[-1].type==CardType.SPELL, "draw spell"
		pass
	pass

################CORE_DS1_184#################

class pp_CORE_DS1_184(Preset_Play):# <12>[1637]
	""" Tracking
	[Discover] a card from your deck. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.controller=self.player
		self.opponent = self.controller.opponent
		self.mark1=self.exchange_card('CORE_DS1_184',self.controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########controller
		self.ids=[]
		for card in self.controller.hand:
			self.print_stats("hand", card)
			self.ids.append(card.id)
		self.play_card(self.mark1)
		postAction(self.controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		ids2=[]
		for card in self.controller.hand:
			self.print_stats("hand", card)
			ids2.append(card.id)
		assert self.ids[0]==ids2[0] and self.ids[1]==ids2[1] and self.ids[2]==ids2[2], "card"
		assert len(self.controller.hand)==4, "hand"
		pass
	pass

#################CORE_DS1_185################

class pp_CORE_DS1_185(Preset_Play):# <12>[1637]
	""" Arcane Shot
	Deal $2 damage. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.controller=self.player
		self.opponent = self.controller.opponent
		self.mark1=self.exchange_card('CORE_DS1_185',self.controller)#
		self.mark2=self.exchange_card('minionH4',self.opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########controller
		self.change_turn()
		### opp
		self.play_card(self.mark2)
		self.change_turn()
		### con
		self.play_card(self.mark1, target=self.mark2)
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.mark2.health==self.mark2.data.health-2
		pass
	pass

################CORE_EX1_534#################

class pp_CORE_EX1_534(Preset_Play):# <12>[1637] 
	""" Savannah Highmane (6/6/5)
	[Deathrattle:] Summon two 2/2 Hyenas. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.controller=self.player
		self.opponent = self.controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_534',self.controller)#
		self.mark2=self.exchange_card('minionA6',self.opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########controller
		self.change_turn()
		### opp
		self.play_card(self.mark2)
		self.change_turn()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.attack_card(self.mark2, self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("field", card)
		assert self.controller.field[-1].id=='EX1_534t', "field"
		assert self.controller.field[-2].id=='EX1_534t', "field"
		pass
	pass

################CORE_EX1_543#################

class pp_CORE_EX1_543(Preset_Play):# <12>[1637]
	""" King Krush
	[Charge] """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_543',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########controller
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.mark1.charge==True, "charge"
		assert self.mark1.attack_targets[0]==self.player.opponent.hero, "target"
		pass
	pass

#################CORE_EX1_554################

class pp_CORE_EX1_554(Preset_Play):# <12>[1637]
	""" Snake Trap
	[Secret:] When one of your minions is attacked, summon three 1/1 Snakes. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_554',controller)#
		self.mark2=self.exchange_card('minionH5',controller)#
		self.mark3=self.exchange_card('minionA4',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########con
		self.play_card(self.mark1)
		self.change_turn()
		####
		self.play_card(self.mark3)
		self.change_turn()
		####
		self.play_card(self.mark2)
		self.change_turn()
		####
		self.attack_card(self.mark3, self.mark2)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		assert controller.secrets==[], "secret"
		assert controller.field[-1].id=='EX1_554t', 'field'
		assert controller.field[-2].id=='EX1_554t', 'field'
		assert controller.field[-3].id=='EX1_554t', 'field'
		pass
	pass

#################CORE_EX1_610################

class pp_CORE_EX1_610(Preset_Play):# <12>[1637]
	""" Explosive Trap
	[Secret:] When your hero is attacked, deal $2 damage to all enemies. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_610',controller)#
		self.mark2=self.exchange_card('minionH4',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		#### con
		self.play_card(self.mark1)
		self.change_turn()
		#### opp
		self.play_card(self.mark2)
		self.change_turn()
		#### con
		self.change_turn()
		#### opp
		self.attack_card(self.mark2, self.player.hero)
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.mark2.health==4-2, "health"
		assert self.player.opponent.hero.health==30-2, "health=%d"%(self.player.opponent.hero.health)
		assert self.player.secrets==[]
		pass
	pass

#################CORE_EX1_611################

class pp_CORE_EX1_611(Preset_Play):# <12>[1637]
	""" Freezing Trap
	[Secret:] When an enemy minion attacks, return it to its owner's hand. It costs (2) more. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_611',controller)#
		self.mark2=self.exchange_card('minionH4',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.play_card(self.mark2)
		self.change_turn()
		### con
		self.change_turn()
		### opp
		self.attack_card(self.mark2, self.player.hero)
		pass
	def result_inspection(self):
		super().result_inspection()
		assert len(self.player.opponent.field)==0, "opp field"
		assert self.mark2 in self.player.opponent.hand, "hand"
		assert self.mark2.cost==self.mark2.data.cost+2, "cost"
		assert self.player.secrets==[], "secret"
		pass
	pass

#################CORE_EX1_617################

class pp_CORE_EX1_617(Preset_Play):# <12>[1637]
	""" Deadly Shot
	Destroy a random enemy minion. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_617',controller)#
		self.mark1=self.exchange_card('minionH4',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########controller
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		pass
	pass

#################CORE_GIL_650################

class pp_CORE_GIL_650(Preset_Play):# <12>[1637]
	""" Houndmaster Shaw
	Your other minions have[Rush]. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_GIL_650',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########controller
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		pass
	pass

#################CORE_GIL_828################

class pp_CORE_GIL_828(Preset_Play):# <12>[1637]
	""" Dire Frenzy
	Give a Beast +3/+3. Shuffle 3 copies into your deck with +3/+3. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_GIL_828',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########controller
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		pass
	pass

#################CORE_KAR_006################

class pp_CORE_KAR_006(Preset_Play):# <12>[1637]
	""" Cloaked Huntress
	Your [Secrets] cost (0). """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_KAR_006',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########controller
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		pass
	pass

#################CORE_LOOT_222################

class pp_CORE_LOOT_222(Preset_Play):# <12>[1637]
	""" Candleshot
	Your hero is [Immune] while attacking. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_LOOT_222',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########controller
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		pass
	pass

#################CORE_NEW1_031################

class pp_CORE_NEW1_031(Preset_Play):# <12>[1637]
	""" Animal Companion
	Summon a random Beast Companion. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_NEW1_031',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########controller
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		pass
	pass

#################NEW1_033################

class pp_NEW1_033(Preset_Play):# <12>[1637]
	"""Leokk 
	"""
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('NEW1_033',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########controller
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		pass
	pass

#################CORE_TRL_348################

class pp_CORE_TRL_348(Preset_Play):# <12>[1637]
	""" Selective Breeder
	[Battlecry:] [Discover] a copy of a Beast in your deck. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_TRL_348',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########controller
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		pass
	pass

#################CS3_015################

class pp_CS3_015(Preset_Play):# <12>[1637]
	""" Living Roots
	[Choose One -] Deal $2 damage; or Summon two 1/1 Saplings. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('CS3_015',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########controller
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		pass
	pass

