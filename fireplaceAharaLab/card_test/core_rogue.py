from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType,Rarity,CardClass
from fireplace.actions import Hit

def SimulateGames_Core_Rogue():
	#PresetGame(pp_CORE_CS2_072)#OK
	#PresetGame(pp_CORE_CS2_073)#OK
	#PresetGame(pp_CORE_CS2_074)#OK
	#PresetGame(pp_CORE_CS2_075)#OK
	#PresetGame(pp_CORE_CS2_076)#OK
	#PresetGame(pp_CORE_CS2_077)#OK
	#PresetGame(pp_CORE_CS2_080)#OK
	#PresetGame(pp_CORE_EX1_134)#OK
	#PresetGame(pp_CORE_EX1_144)#OK
	#PresetGame(pp_CORE_EX1_145)#OK
	#PresetGame(pp_CORE_EX1_522)#OK
	#PresetGame(pp_CORE_ICC_809)#OK
	#PresetGame(pp_CORE_KAR_069)#OK
	#PresetGame(pp_CORE_LOE_012)#OK
	#PresetGame(pp_CORE_OG_070)#OK
	#PresetGame(pp_CS3_005)	#OK
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
		self.mark2=self.exchange_card('minionH6',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark2, opponent)#
		#Hit(self.mark2,1).trigger(self.mark1)
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller, target=self.mark2)#
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		card2=self.mark2
		print(" %r が%rに2ダメージ与えているかどうかを視認"%(card1,card2))
		print(" Hit があるならNO,　HitがないならYES が正しい")
		#print ("%s:"%(card1.buffs))
		for card in [card2]:
			print ("%r: %d/%d <- %d/%d"%(
				card, card.atk, card.health, card.data.atk, card.data.health
				))
		pass


class pp_CORE_CS2_073(Preset_Play):# <7>[1637]
	""" Cold Blood
	Give a minion +2 Attack. [Combo:] +4 Attack instead. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_073',controller)#
		self.mark2=self.exchange_card('minionH6',opponent)#
		self.mark3=self.exchange_card('minionH2',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		X1=self.mark1
		Y2=self.mark2
		X3=self.mark3
		##########controller
		#self.play_card(self.mark1, controller)#
		self.change_turn(controller)
		##########opponent
		self.play_card(Y2, opponent)#
		self.change_turn(opponent)
		##########controller
		#self.play_card(X3, controller)#この行をつければcombo
		self.play_card(X1, controller, target=Y2)#
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		X1=self.mark1
		Y2=self.mark2
		X3=self.mark3
		print(" %r がコンボでないなら+2/0を、コンボならば+4/+0をつけているかどうかを視認"%(Y2))
		for card in [Y2]:
			print ("%r: %d/%d <- %d/%d"%(
				card, card.atk, card.health, card.data.atk, card.data.health
				))
		pass

class pp_CORE_CS2_074(Preset_Play):# <7>[1637]
	""" Deadly Poison
	Give your weapon +2_Attack. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_074',controller)#
		self.mark2=self.exchange_card('weapon',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark2, controller)#
		self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" ヒーロー の攻撃力が２上がっているかどうかを視認")
		for card in [self.mark2]:
			self.print_stats ("friendly weapon",card)
		pass

class pp_CORE_CS2_075(Preset_Play):# <7>[1637]
	""" Sinister Strike
	Deal $3 damage to the_enemy hero. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_075',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %rのhealthが 3 減っているかどうかを視認"%(controller.opponent.hero))
		for card in [controller.opponent.hero]:
			self.print_stats("enemy hero",card)
		pass

class pp_CORE_CS2_076(Preset_Play):# <7>[1637]
	""" Assassinate
	Destroy an enemy minion. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_076',controller)#
		self.mark2=self.exchange_card('minionH7',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark2, opponent)#
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller, target=self.mark2)#
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		print(" %r が破壊されているかどうかを視認"%(self.mark2))
		for card in [self.mark2]:
			self.print_stats("enemy",card)
		pass

class pp_CORE_CS2_077(Preset_Play):# <7>[1637]
	""" Sprint
	Draw 4 cards. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_077',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		print(" カードを４枚引いたかどうかを視認")
		for card in controller.hand:
			self.print_stats("friendly hand",card)
		pass

class pp_CORE_CS2_080(Preset_Play):# <7>[1637]
	""" Assassin's Blade
	#vanilla	 """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_080',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r が武器を装備しているかどうかを視認"%(card1))
		for card in [controller.hero]:
			self.print_stats("friendly hand",card)
		pass

class pp_CORE_EX1_134(Preset_Play):# <7>[1637]
	""" SI:7 Agent
	[Combo:] Deal 2 damage. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_134',controller)#
		self.mark2=self.exchange_card('minionH4',opponent)#
		self.mark3=self.exchange_card('minionH4',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark2, opponent)#
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark3, controller)# combo
		self.play_card(self.mark1, controller, target=self.mark2)#
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r がコンボの時に限り２ダメージ受けているかどうかを視認"%(self.mark2))
		self.print_stats("card2", self.mark2)

class pp_CORE_EX1_144(Preset_Play):# <7>[1637]
	""" Shadowstep
	Return a friendly minion to your hand. It_costs (2) less. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_144',controller)#
		self.mark2=self.exchange_card('minionH4',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark2, controller)#
		self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller, target=self.mark2)#
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		print(" %r が手元にあるかどうかを視認"%(self.mark2))
		print(" %r のコストが２減っているかを視認"%(self.mark2))
		self.print_stats("card2",self.mark2)
		print("cost = %d<-%d" % (self.mark2.cost,self.mark2.data.cost))
		pass

class pp_CORE_EX1_145(Preset_Play):# <7>[1637]##
	""" Preparation
	The next spell you cast this turn costs (2) less. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_145',controller)#
		self.mark2=self.exchange_card('nature',controller)#
		self.mark3=self.exchange_card('fire',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark1, controller)#
		self.play_card(self.mark2, controller)# on/off
		#self.change_turn(controller)# on/off
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" スペルのコストが2下がっているかどうかを視認")
		print("C1だした瞬間・C1出してスペルをプレイした直後・C1出してターンエンド")
		for card in controller.hand:
			self.print_stats("friendly hand",card, old_cost=True)
		pass

class pp_CORE_EX1_522(Preset_Play):# <7>[1637]#
	""" Patient Assassin
	[Stealth] [Poisonous] """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_522',controller)#
		self.mark2=self.exchange_card('minionH8',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark1, controller)#
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark2, opponent)#
		self.change_turn(opponent)
		##########controller
		self.attack_card(self.mark1, self.mark2, controller)#poisonaousの確認
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r がpoisonousで死んでいるかどうかを視認"%(self.mark2))
		self.print_stats ("card2:",self.mark2)
		pass

class pp_CORE_ICC_809(Preset_Play):# <7>[1637]#
	""" Plague Scientist
	[Combo:] Give a friendly minion [Poisonous]. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_ICC_809',controller)#
		self.mark2=self.exchange_card('minionH2',controller)#
		self.mark3=self.exchange_card('minionH2',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark2, controller)#
		#self.change_turn(controller) # to make it no-combo
		#self.change_turn(opponent)
		self.play_card(self.mark1, controller, target=self.mark2)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r がpoisonousかどうかを視認"%(self.mark2))
		self.print_stats("card2",self.mark2, show_buff=True)
		print ("poisonous: %s"%(self.mark2.poisonous))
		pass

class pp_CORE_KAR_069(Preset_Play):# <7>[1637]
	""" Swashburglar
	[Battlecry:] Add a random card from another class to_your hand. """
	class1=CardClass.ROGUE
	#class2=CardClass.WARRIOR#10
	class2=CardClass.HUNTER#3
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_KAR_069',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" ハンドにカードが入っているかどうかを視認")
		for card in controller.hand:
			self.print_stats ("controller hand",card)
		print("card class = %r"%(controller.hand[-1].card_class))
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
		self.mark1=self.exchange_card('CORE_LOE_012',controller)#
		self.mark2=self.exchange_card('minionA5',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark2, opponent)#
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller)#
		self.change_turn(controller)
		##########opponent
		self.attack_card(self.mark2, self.mark1, opponent)#
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" 最後にコインが配給されているかどうかを視認")
		for card in controller.hand:
			self.print_stats("hand",card)
		pass

class pp_CORE_OG_070(Preset_Play):# <7>[1637]
	""" Bladed Cultist
	[Combo:] Gain +1/+1. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_OG_070',controller)#
		self.mark2=self.exchange_card('minionH1',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark2, controller)#
		self.play_card(self.mark1, controller)#combo
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark1, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" %r が+1/+1を持っているかどうかを視認"%(card1))
		self.print_stats("mark1",self.mark1,show_buff=True)
		pass

class pp_CS3_005(Preset_Play):# <7>[1637]#
	""" Vanessa VanCleef
	[Combo:] Add a copy of the last card your opponent played to your hand. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CS3_005',controller)#
		self.mark2=self.exchange_card('minionH2',controller)#
		self.mark3=self.exchange_card('minionH2',opponent)#
		self.mark4=self.exchange_card('minionH2',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		#self.play_card(self.mark1, controller)#
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark3, opponent)#
		self.play_card(self.mark4, opponent)# last played card
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark2, controller)#
		self.play_card(self.mark1, controller)# combo
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" ハンドにmark4があるかどうかを視認")
		for card in [self.mark3,self.mark4]:
			self.print_stats("played",card)
		for card in controller.hand:
			self.print_stats("hand",card)

########################################