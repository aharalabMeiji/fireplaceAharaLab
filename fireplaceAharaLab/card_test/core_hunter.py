from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity,CardClass, GameTag, Race

#from fireplace.cards.core.core_hunter import * 
from fireplace.actions import *
from utils import postAction
from fireplace.config import Config

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
	#PresetGame(pp_CORE_EX1_617)
	#PresetGame(pp_CORE_GIL_650)
	#PresetGame(pp_CORE_GIL_828)
	#PresetGame(pp_CORE_KAR_006)
	#PresetGame(pp_CORE_LOOT_222)
	#PresetGame(pp_CORE_NEW1_031)
	#PresetGame(pp_NEW1_033)
	#PresetGame(pp_CORE_TRL_348)
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
		while True:
			Destroy(self.player.hand[0]).trigger(self.player)
			if len(self.player.hand)==1:
				break;
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
		assert "Hit,%s,%s,2,None"%(self.mark1, self.mark2) in Config.LOGINFO_LOG, "loginfo"
		assert "Hit,%s,%s,2,None"%(self.mark1, self.player.opponent.hero) in Config.LOGINFO_LOG, "loginfo"
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
		self.mark2=self.exchange_card('minionH4',opponent)#
		self.mark3=self.exchange_card('minionH4',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.change_turn()
		### opp
		self.play_card(self.mark2)
		self.play_card(self.mark3)
		self.n1 = len(self.player.opponent.field)
		for card in self.player.opponent.field:
			self.print_stats("field", card)
		self.change_turn()
		### con
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.player.opponent.field:
			self.print_stats("field", card)
		assert len(self.player.opponent.field)==self.n1-1, "field=%d"%(len(self.player.opponent.field))
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
		self.mark2=self.exchange_card('minionH4',controller)#
		self.mark3=self.exchange_card('minionH4',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark2)
		self.play_card(self.mark3)
		self.change_turn()
		### opp
		self.change_turn()
		### con
		self.play_card(self.mark1)
		assert self.mark2.rush==True, "rush"
		assert self.mark3.rush==True, "rush"
		Hit(self.mark1,10).trigger(self.player)
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.mark2.rush==False, "rush"
		assert self.mark3.rush==False, "rush"
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
		self.mark2=self.exchange_card('beast',controller)#
		self.n1=self.mark2.atk
		self.n2=self.mark2.health
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########controller
		assert self.mark2.race==Race.BEAST, "race"
		self.play_card(self.mark2)
		self.play_card(self.mark1, target=self.mark2)
		pass
	def result_inspection(self):
		super().result_inspection()
		assert len(self.mark2.buffs)>0, "buff"
		assert self.mark2.atk == self.n1+3, "atk up = %d"%(self.mark2.atk - self.n1)
		assert self.mark2.health== self.n2+3, "health"
		for card in self.player.deck:
			if card.id==self.mark2.id:
				assert len(card.buffs)>0, "buff"
				assert card.atk == self.n1+3, "atk"
				assert card.health== self.n2+3, "health"
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
		self.mark2=self.exchange_card('secret',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########controller
		self.play_card(self.mark1)
		for card in self.player.hand:
			self.print_stats("hand", card,old_cost=True)
			if card.data.secret:
				assert card.cost==0, "cost"
		Hit(self.mark1, 10).trigger(self.player)
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.player.hand:
			self.print_stats("hand", card,old_cost=True)
			if card.data.secret:
				assert card.cost!=0, "cost"
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
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_LOOT_222',controller)#
		self.mark3=self.exchange_card('minionA5',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########controller
		self.play_card(self.mark1)
		assert self.player.hero.immune_while_attacking==True, "immune"
		#self.play_card(self.mark2)
		assert self.player.hero.atk>0, "hero atk"
		self.change_turn()
		### opp
		self.play_card(self.mark3)
		self.n0=self.mark3.health
		self.change_turn()
		### con
		self.n1=self.player.hero.health
		assert self.player.hero.immune_while_attacking==True, "immune"
		self.attack_card(self.player.hero, self.mark3)
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.player.hero.health==self.n1, "health"
		assert 'Hit,%s,%s,1,None'%(self.player.hero, self.mark3) in Config.LOGINFO_LOG, "loginfo"
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
		card = self.player.field[0]
		assert card.id=='NEW1_032' or card.id=='NEW1_033' or card.id=='NEW1_034', "beast companion"
		pass
	pass

#################NEW1_033################

class pp_NEW1_033(Preset_Play):# <12>[1637]
	"""Leokk 
	Your other minions have +1 Attack."""
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		#opponent = controller.opponent
		self.mark1=self.exchange_card('NEW1_033',controller)#
		self.mark2=self.exchange_card('minionH4',controller)#
		self.n1=self.mark2.atk
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		##########controller
		self.play_card(self.mark1)
		self.play_card(self.mark2)
		assert self.mark2.atk==self.n1+1, "attack"
		Hit(self.mark1,10).trigger(self.player)
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.mark2.atk==self.n1, "attack"
		pass
	pass

#################CORE_TRL_348################

class pp_CORE_TRL_348(Preset_Play):# <12>[1637]
	""" Springpaw
	[Rush][Battlecry:] Add a 1/1 Lynxwith [Rush] to your hand."""
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
		exist=False
		for card in self.player.hand:
			self.print_stats("hand", card)
			if card.id=='TRL_348t':
				exist=True
		assert exist==True, "exist"
		pass
	pass

#################CS3_015################

class pp_CS3_015(Preset_Play):# <12>[1637]
	""" Selective Breeder
	[Battlecry:] [Discover] a copy of a Beast in your deck. """
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
		postAction(self.player)
		self.newcard = self.player.hand[-1]
		assert self.newcard.race==Race.BEAST, "beast"
		self.n1=self.newcard.id
		pass
	def result_inspection(self):
		super().result_inspection()
		exist=False
		for card in self.player.deck:
			if card.id==self.n1:
				exist=True
		assert exist==True, "exist"
		pass
	pass

