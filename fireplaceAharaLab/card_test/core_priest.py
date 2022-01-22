from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity,CardClass

def SimulateGames_Core_Priest():
	#PresetGame(pp_CORE_AT_055)#OK
	#PresetGame(pp_CORE_CS1_112)#OK
	#PresetGame(pp_CORE_CS1_130)#OK
	PresetGame(pp_CORE_EX1_193)#
	#PresetGame(pp_CORE_EX1_194)#
	#PresetGame(pp_CORE_EX1_195)#
	#PresetGame(pp_CORE_EX1_197)#
	#PresetGame(pp_CORE_EX1_198)#
	#PresetGame(pp_CORE_EX1_335)#
	#PresetGame(pp_CORE_EX1_622)#
	#PresetGame(pp_CORE_EX1_623)#
	#PresetGame(pp_CORE_EX1_625)#
	#PresetGame(pp_CS3_013)#
	#PresetGame(pp_CS3_014)#
	#PresetGame(pp_CS3_027)#
	pass

##################################

class pp_CORE_AT_055(Preset_Play):# <6>[1637]
	""" Flash Heal
	Restore #5 Health. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_055',controller)#
		self.mark2=self.exchange_card('minionH8',controller)#
		self.mark3=self.exchange_card('minionA5',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark4, controller)
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark3, opponent)#
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark2, controller)#
		self.change_turn(controller)
		##########opponent
		self.attack_card(self.mark3, self.mark2, opponent)#
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller, target=self.mark2)#
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.opponent.hero
		for card in controller.field:
			print ("op. field: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone))
		pass

##################################


class pp_CORE_CS1_112(Preset_Play):# <6>[1637]
	""" Holy Nova
	Deal $2 damage to all enemy minions. Restore #2 Health to all friendly characters. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS1_112',controller)#
		self.mark2=self.exchange_card('minionH6',controller)#
		self.mark3=self.exchange_card('minionH4',opponent)#
		self.mark4=self.exchange_card('vanillaA3',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark4, controller)
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark3, opponent)#
		self.play_card(self.mark4, opponent)#
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark2, controller)
		self.change_turn(controller)
		##########opponent
		self.attack_card(self.mark3, controller.hero, opponent)#
		self.attack_card(self.mark4, self.mark2, opponent)#
		for card in controller.opponent.field:
			print ("oppo. field: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone))
		for card in controller.field+[controller.hero]:
			print ("contr. field: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone))
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.opponent.hero
		for card in controller.opponent.field:
			print ("oppo. field: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone))
		for card in controller.field+[controller.hero]:
			print ("contr. field: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone))
		pass

##################################

class pp_CORE_CS1_130(Preset_Play):# <6>[1637]
	""" Holy Smite
	Deal $3 damage to a minion. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS1_130',controller)#
		self.mark2=self.exchange_card('minionH4',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark4, controller)
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark2, opponent)#
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller,target=self.mark2)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.opponent.hero
		# self.mark2が３ダメを受けているか目視
		for card in controller.field:
			print ("op. field: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone),end='')
			print("<-(%d/%d)" % (card.data.atk, card.data.health))
		pass

##################################

class pp_CORE_EX1_193(Preset_Play):# <6>[1637]## 
	""" Psychic Conjurer
	[Battlecry:] Copy a card in your opponent’s deck and add it to your hand. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_193',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark1, controller)
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.opponent.hero
		print("#最後に配られたカードが敵方のデッキにあるかどうかを目視")
		for card in controller.hand:
			if hasattr(card, 'atk') and hasattr(card, 'health'):
				print ("con. hand: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone))
			else:
				print ("con. hand: %s: (%d) zone->%s"%(card, card.cost, card.zone))
		for card in controller.opponent.deck:
			if hasattr(card, 'atk') and hasattr(card, 'health'):
				print ("opp. deck: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone))
			else:
				print ("con. hand: %s: (%d) zone->%s"%(card, card.cost, card.zone))
		pass

##################################

class pp_CORE_EX1_194(Preset_Play):# <6>[1637]## no EX1_194 card 
	""" Power Infusion
	Give a minion +2/+6. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_194',controller)#
		self.mark2=self.exchange_card('vanillaH2',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark2, controller)
		self.play_card(self.mark1, controller, target=self.mark2)
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.opponent.hero
		for card in controller.field:
			print ("con. field: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone))
		pass

##################################

class pp_CORE_EX1_195(Preset_Play):# <6>[1637]## no EX1_195 but similar as EX1_623
	""" Kul Tiran Chaplain
	[Battlecry:] Give a friendly minion +2 Health. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_1952',controller)#Minefield
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark4, controller)
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.opponent.hero
		#for card in controller.field:
		#	print ("op. field: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone))
		pass

##################################

class pp_CORE_EX1_197(Preset_Play):# <6>[1637]## no EX1_197 but same as EX1_622
	""" Shadow Word: Ruin
	Destroy all minions with 5 or more Attack. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('DMF_522',controller)#Minefield
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark4, controller)
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.opponent.hero
		#for card in controller.field:
		#	print ("op. field: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone))
		pass

##################################

class pp_CORE_EX1_198(Preset_Play):# <6>[1637]##
	""" Natalie Seline
	[Battlecry:] Destroy a minion and gain its Health. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('DMF_522',controller)#Minefield
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark4, controller)
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.opponent.hero
		#for card in controller.field:
		#	print ("op. field: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone))
		pass

##################################


class pp_CORE_EX1_335(Preset_Play):# <6>[1637]
	""" Lightspawn
	This minion's Attack is always equal to its Health. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('DMF_522',controller)#Minefield
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark4, controller)
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.opponent.hero
		#for card in controller.field:
		#	print ("op. field: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone))
		pass

##################################

class pp_CORE_EX1_622(Preset_Play):# <6>[1637]
	""" Shadow Word: Death
	Destroy a minion with 5_or more Attack. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('DMF_522',controller)#Minefield
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark4, controller)
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.opponent.hero
		#for card in controller.field:
		#	print ("op. field: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone))
		pass

##################################

class pp_CORE_EX1_623(Preset_Play):# <6>[1637]
	""" Temple Enforcer
	[Battlecry:] Give a friendly minion +3 Health. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('DMF_522',controller)#Minefield
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark4, controller)
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.opponent.hero
		#for card in controller.field:
		#	print ("op. field: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone))
		pass

##################################

class pp_CORE_EX1_625(Preset_Play):# <6>[1637]
	""" Shadowform
	Your Hero Power becomes 'Deal 2 damage.' """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('DMF_522',controller)#Minefield
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark4, controller)
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.opponent.hero
		#for card in controller.field:
		#	print ("op. field: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone))
		pass
##################################

class pp_CS3_013(Preset_Play):# <6>[1637]
	""" Shadowed Spirit
	[Deathrattle:] Deal 3 damage to the enemy hero. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('DMF_522',controller)#Minefield
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark4, controller)
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.opponent.hero
		#for card in controller.field:
		#	print ("op. field: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone))
		pass

##################################

class pp_CS3_014(Preset_Play):# <6>[1637]
	""" Crimson Clergy
	After a friendly character is healed, gain +1 Attack. """
	#
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('DMF_522',controller)#Minefield
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark4, controller)
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.opponent.hero
		#for card in controller.field:
		#	print ("op. field: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone))
		pass

##################################

class pp_CS3_027(Preset_Play):# <6>[1637]
	""" Focused Will
	[Silence] a minion, then give it +3 Health. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('DMF_522',controller)#Minefield
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark4, controller)
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.opponent.hero
		#for card in controller.field:
		#	print ("op. field: %s: (%d/%d/%d) zone->%s"%(card, card.cost,card.atk, card.health,card.zone))
		pass

##################################


