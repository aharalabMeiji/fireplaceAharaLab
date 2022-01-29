from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType,Rarity,CardClass
from fireplace.actions import Discard 

def SimulateGames_Core_Rogue():
	PresetGame(pp_CORE_CS2_072)#
	#PresetGame(pp_CORE_CS2_073)#
	#PresetGame(pp_CORE_CS2_074)#
	#PresetGame(pp_CORE_CS2_075)#
	#PresetGame(pp_CORE_CS2_076)#
	#PresetGame(pp_CORE_CS2_077)#
	#PresetGame(pp_CORE_CS2_080)#
	#PresetGame(pp_CORE_EX1_134)#
	#PresetGame(pp_CORE_EX1_144)#
	#PresetGame(pp_CORE_EX1_145)#
	#PresetGame(pp_CORE_EX1_522)#
	#PresetGame(pp_CORE_ICC_809)#
	#PresetGame(pp_CORE_KAR_069)#
	#PresetGame(pp_CORE_LOE_012)#
	#PresetGame(pp_CORE_OG_070)#
	#PresetGame(pp_CS3_005)	
	pass

##################################

class pp_CORE_CS2_072(Preset_Play):# <7>[1637]
	""" Backstab
	Deal $2 damage to an undamaged minion. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_072',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r が＊＊＊かどうかを視認"%(card1))
		#print ("%s:"%(card1.buffs))
		#print ("STATS: %d/%d <- %d/%d"%(card1.atk, card1.health, card1.data.atk, card1.data.health))
		pass


class pp_CORE_CS2_073(Preset_Play):# <7>[1637]
	""" Cold Blood
	Give a minion +2 Attack. [Combo:] +4 Attack instead. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_021',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r が＊＊＊かどうかを視認"%(card1))
		#print ("%s:"%(card1.buffs))
		#print ("STATS: %d/%d <- %d/%d"%(card1.atk, card1.health, card1.data.atk, card1.data.health))
		pass

class pp_CORE_CS2_074(Preset_Play):# <7>[1637]
	""" Deadly Poison
	Give your weapon +2_Attack. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_021',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r が＊＊＊かどうかを視認"%(card1))
		#print ("%s:"%(card1.buffs))
		#print ("STATS: %d/%d <- %d/%d"%(card1.atk, card1.health, card1.data.atk, card1.data.health))
		pass

class pp_CORE_CS2_075(Preset_Play):# <7>[1637]
	""" Sinister Strike
	Deal $3 damage to the_enemy hero. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_021',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r が＊＊＊かどうかを視認"%(card1))
		#print ("%s:"%(card1.buffs))
		#print ("STATS: %d/%d <- %d/%d"%(card1.atk, card1.health, card1.data.atk, card1.data.health))
		pass

class pp_CORE_CS2_076(Preset_Play):# <7>[1637]
	""" Assassinate
	Destroy an enemy minion. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_021',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r が＊＊＊かどうかを視認"%(card1))
		#print ("%s:"%(card1.buffs))
		#print ("STATS: %d/%d <- %d/%d"%(card1.atk, card1.health, card1.data.atk, card1.data.health))
		pass

class pp_CORE_CS2_077(Preset_Play):# <7>[1637]
	""" Sprint
	Draw 4 cards. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_021',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r が＊＊＊かどうかを視認"%(card1))
		#print ("%s:"%(card1.buffs))
		#print ("STATS: %d/%d <- %d/%d"%(card1.atk, card1.health, card1.data.atk, card1.data.health))
		pass

class pp_CORE_CS2_080(Preset_Play):# <7>[1637]
	""" Assassin's Blade
	#vanilla	 """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_021',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r が＊＊＊かどうかを視認"%(card1))
		#print ("%s:"%(card1.buffs))
		#print ("STATS: %d/%d <- %d/%d"%(card1.atk, card1.health, card1.data.atk, card1.data.health))
		pass

class pp_CORE_EX1_134(Preset_Play):# <7>[1637]
	""" SI:7 Agent
	[Combo:] Deal 2 damage. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_021',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r が＊＊＊かどうかを視認"%(card1))
		#print ("%s:"%(card1.buffs))
		#print ("STATS: %d/%d <- %d/%d"%(card1.atk, card1.health, card1.data.atk, card1.data.health))
		pass

class pp_CORE_EX1_144(Preset_Play):# <7>[1637]
	""" Shadowstep
	Return a friendly minion to your hand. It_costs (2) less. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_021',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r が＊＊＊かどうかを視認"%(card1))
		#print ("%s:"%(card1.buffs))
		#print ("STATS: %d/%d <- %d/%d"%(card1.atk, card1.health, card1.data.atk, card1.data.health))
		pass

class pp_CORE_EX1_145(Preset_Play):# <7>[1637]##
	""" Preparation
	The next spell you cast this turn costs (2) less. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_021',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r が＊＊＊かどうかを視認"%(card1))
		#print ("%s:"%(card1.buffs))
		#print ("STATS: %d/%d <- %d/%d"%(card1.atk, card1.health, card1.data.atk, card1.data.health))
		pass

class pp_CORE_EX1_522(Preset_Play):# <7>[1637]#
	""" Patient Assassin
	[Stealth] [Poisonous] """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_021',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r が＊＊＊かどうかを視認"%(card1))
		#print ("%s:"%(card1.buffs))
		#print ("STATS: %d/%d <- %d/%d"%(card1.atk, card1.health, card1.data.atk, card1.data.health))
		pass

class pp_CORE_ICC_809(Preset_Play):# <7>[1637]#########################
	""" Plague Scientist
	[Combo:] Give a friendly minion [Poisonous]. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_021',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r が＊＊＊かどうかを視認"%(card1))
		#print ("%s:"%(card1.buffs))
		#print ("STATS: %d/%d <- %d/%d"%(card1.atk, card1.health, card1.data.atk, card1.data.health))
		pass

class pp_CORE_KAR_069(Preset_Play):# <7>[1637]
	""" Swashburglar
	[Battlecry:] Add a random card from another class to_your hand. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_021',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r が＊＊＊かどうかを視認"%(card1))
		#print ("%s:"%(card1.buffs))
		#print ("STATS: %d/%d <- %d/%d"%(card1.atk, card1.health, card1.data.atk, card1.data.health))
		pass

class pp_CORE_LOE_012(Preset_Play):# <7>[1637]
	""" Tomb Pillager
	[Deathrattle:] Add a Coin to your hand. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_021',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r が＊＊＊かどうかを視認"%(card1))
		#print ("%s:"%(card1.buffs))
		#print ("STATS: %d/%d <- %d/%d"%(card1.atk, card1.health, card1.data.atk, card1.data.health))
		pass

class pp_CORE_OG_070(Preset_Play):# <7>[1637]
	""" Bladed Cultist
	[Combo:] Gain +1/+1. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_021',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r が＊＊＊かどうかを視認"%(card1))
		#print ("%s:"%(card1.buffs))
		#print ("STATS: %d/%d <- %d/%d"%(card1.atk, card1.health, card1.data.atk, card1.data.health))
		pass
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_021',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r が＊＊＊かどうかを視認"%(card1))
		#print ("%s:"%(card1.buffs))
		#print ("STATS: %d/%d <- %d/%d"%(card1.atk, card1.health, card1.data.atk, card1.data.health))
		pass

class pp_CS3_005(Preset_Play):# <7>[1637]#
	""" Vanessa VanCleef
	[Combo:] Add a copy of the last card your opponent played to your hand. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_021',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r が＊＊＊かどうかを視認"%(card1))
		#print ("%s:"%(card1.buffs))
		#print ("STATS: %d/%d <- %d/%d"%(card1.atk, card1.health, card1.data.atk, card1.data.health))
		pass

########################################