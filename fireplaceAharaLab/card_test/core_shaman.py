
from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType,Rarity,CardClass,Race
from fireplace.actions import Hit

def SimulateGames_Core_Shaman():
	#PresetGame(pp_CORE_AT_047)#OK
	#PresetGame(pp_CORE_BOT_533)#OK
	#PresetGame(pp_CORE_CS2_039)#OK
	#PresetGame(pp_CORE_CS2_042)#OK
	#PresetGame(pp_CORE_CS2_045)#OK
	#PresetGame(pp_CORE_EX1_238)#OK
	#PresetGame(pp_CORE_EX1_246)#OK
	#PresetGame(pp_CORE_EX1_248)#OK
	#PresetGame(pp_CORE_EX1_250)#OK
	#PresetGame(pp_CORE_EX1_258)#OK
	#PresetGame(pp_CORE_EX1_259)#OK
	#PresetGame(pp_CORE_EX1_567)#OK
	#PresetGame(pp_CORE_EX1_575)#OK
	#PresetGame(pp_CORE_NEW1_010)#OK
	#PresetGame(pp_CORE_UNG_817)#OK
	#PresetGame(pp_CS3_007)#OK
	#PresetGame(pp_CS3_016)#
	PresetGame(pp_CORE_AT_075)#
	pass

class pp_CORE_AT_047(Preset_Play):# <8>[1637]
	""" Draenei Totemcarver
	[Battlecry:] Gain +1/+1 for each friendly Totem. """
	class1=CardClass.SHAMAN
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_047',controller)#
		self.mark2=self.exchange_card('totem',controller)#
		self.mark3=self.exchange_card('totem',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark2, controller)#
		self.play_card(self.mark3, controller)#
		self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		card2=self.mark2
		print(" +1+1のバフがついているかどうかを視認"%())
		for card in [card1]:
			self.print_stats ("***",card, show_buff=True)
	pass

class pp_CORE_BOT_533(Preset_Play):# <8>[1637]
	""" Menacing Nimbus
	[Battlecry:] Add a random Elemental to your hand. """
	class1=CardClass.SHAMAN
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_BOT_533',controller)#
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
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		card2=self.mark2
		print(" エレメンタル(%r)のカードがハンドに含まれているかどうかを視認"%(Race.ELEMENTAL))
		for card in controller.hand:
			self.print_stats ("***",card, show_race=True)
	pass

class pp_CORE_CS2_039(Preset_Play):# <8>[1637]
	""" Windfury
	Give a minion [Windfury]. """
	class1=CardClass.SHAMAN
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_039',controller)#
		self.mark2=self.exchange_card('minionH3',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark2, controller)#
		self.play_card(self.mark1, controller, target=self.mark2)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		card2=self.mark2
		print("mark2に疾風がついているかどうかを視認"%())
		self.print_stats ("***",self.mark2, show_buff=True)
		print("windfury=%d" % self.mark2.windfury)
	pass

class pp_CORE_CS2_042(Preset_Play):# <8>[1637]
	""" Fire Elemental
	[Battlecry:] Deal 4 damage. """
	class1=CardClass.SHAMAN
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_042',controller)#
		self.mark2=self.exchange_card('minionH6',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
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
		card1=self.mark1
		card2=self.mark2
		print(" mark2に４ダメいっているかどうかを視認"%())
		for card in [card2]:
			self.print_stats ("***",card)
	pass

class pp_CORE_CS2_045(Preset_Play):# <8>[1637]
	""" Rockbiter Weapon
	Give a friendly character +3 Attack this turn. """
	class1=CardClass.SHAMAN
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_045',controller)#
		self.mark2=self.exchange_card('minionH2',controller)#
		self.mark3=self.exchange_card('minionH6',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark2, controller)#
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark3, opponent)#
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller,target=self.mark2)#
		#self.attack_card(self.mark2, self.mark3, controller)
		print(" mark2からmark3への攻撃が+3されているかどうかを視認"%())
		for card in [self.mark1, self.mark2, self.mark3]:
			self.print_stats ("***",card)
		self.change_turn(controller)
		##########opponent
		self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		card2=self.mark2
		print(" mark2.atkが戻っているかどうかを視認"%())
		for card in [self.mark1, self.mark2, self.mark3]:
			self.print_stats ("***",card)
	pass

class pp_CORE_EX1_238(Preset_Play):# <8>[1637]
	""" Lightning Bolt
	Deal $3 damage. [Overload:] (1) """
	class1=CardClass.SHAMAN
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_238',controller)#
		self.mark2=self.exchange_card('minionH6',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
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
		card1=self.mark1
		card2=self.mark2
		print(" mark2が３ダメを受けているかどうかを視認"%())
		for card in [card2]:
			self.print_stats ("***",card)
		print(" controllerがoverload=1かどうかを視認"%())
		print("overload=%d" % controller.overloaded)
	pass

class pp_CORE_EX1_246(Preset_Play):# <8>[1637]
	""" Hex
	Transform a minion into a 0/1 Frog with [Taunt]. """
	class1=CardClass.SHAMAN
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_246',controller)#
		self.mark2=self.exchange_card('minionH6',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
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
		card1=self.mark1
		card2=self.mark2
		print(" 敵側のフィールドにカエルがいるかどうかを視認"%())
		for card in controller.opponent.field:
			self.print_stats ("opponent.field",card)
	pass

class pp_CORE_EX1_248(Preset_Play):# <8>[1637]
	""" Feral Spirit
	Summon two 2/3 Spirit Wolves with [Taunt]. [Overload:] (1) """
	class1=CardClass.SHAMAN
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_248',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		card2=self.mark2
		print(" tauntつきオオカミが2匹いるかどうかを視認"%())
		for card in controller.field:
			self.print_stats ("controller.field",card)
			print("taunt=%d" % card.taunt)
		print(" overloadが１かどうかを視認"%())
		print("overload=%d" % controller.overloaded)

	pass

class pp_CORE_EX1_250(Preset_Play):# <8>[1637]
	""" Earth Elemental
	[Taunt][[Overload]:] (2) """
	class1=CardClass.SHAMAN
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_250',controller)#
		self.mark2=self.exchange_card('minionH6',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		card2=self.mark2
		print(" overloadが２かどうかを視認"%())
		print("overload=%d" % controller.overloaded)
	pass

class pp_CORE_EX1_258(Preset_Play):# <8>[1637]
	""" Unbound Elemental
	After you play a card_with [Overload], gain_+1/+1. """
	class1=CardClass.SHAMAN
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_258',controller)#
		self.mark2=self.exchange_card('CORE_EX1_250',controller)#overload
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)#
		self.play_card(self.mark2, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		card2=self.mark2
		print(" mark1に+1/+1がついているかどうかを視認"%())
		for card in [card1]:
			self.print_stats ("***",card, show_buff=True)
		pass

class pp_CORE_EX1_259(Preset_Play):# <8>[1637]
	""" Lightning Storm
	Deal $3 damage to all_enemy minions. [Overload:] (2) """
	class1=CardClass.SHAMAN
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_259',controller)#
		self.mark2=self.exchange_card('minionH4',opponent)#
		self.mark3=self.exchange_card('minionH4',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark2, opponent)#
		self.play_card(self.mark3, opponent)#
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller)#
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		card2=self.mark2
		print(" 敵のフィールドに３ダメージがあるかどうかを視認"%())
		for card in controller.opponent.field:
			self.print_stats ("opponent.field",card)
		print(" overloadが２かどうかを視認"%())
		print("overload=%d" % controller.overloaded)
	pass

class pp_CORE_EX1_567(Preset_Play):# <8>[1637]
	""" Doomhammer
	[Windfury, Overload:] (2) """
	class1=CardClass.SHAMAN
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_567',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		print(" overloadが２かどうかを視認"%())
		print("overload=%d" % controller.overloaded)
		print(" windfuryかどうかを視認"%())
		print(" windfury=%d" % self.mark1.windfury)
	pass

class pp_CORE_EX1_575(Preset_Play):# <8>[1637]
	""" Mana Tide Totem
	At the end of your turn, draw a card. """
	class1=CardClass.SHAMAN
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_575',controller)#
		self.mark2=self.exchange_card('minionH6',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)#
		self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		card2=self.mark2
		print(" カードを一枚引いているかどうかを視認"%())
		for card in controller.hand:
			self.print_stats ("controller.hand",card)
	pass

class pp_CORE_NEW1_010(Preset_Play):# <8>[1637]
	""" Al'Akir the Windlord
	[Charge, Divine Shield, Taunt, Windfury] """
	class1=CardClass.SHAMAN
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_NEW1_010',controller)#
		self.mark2=self.exchange_card('minionH6',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print("charge=%d"%(card1.charge))
		print("shield=%d"%(card1.divine_shield))
		print("taunt=%d"%(card1.taunt))
		print("windfury=%d"%(card1.windfury))
		

class pp_CORE_UNG_817(Preset_Play):# <8>[1637]
	""" Tidal Surge
	[Lifesteal]Deal $4 damage to a_minion. """
	class1=CardClass.SHAMAN
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_UNG_817',controller)#
		self.mark2=self.exchange_card('minionH6',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		#self.play_card(self.mark1, controller)#
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark2, opponent)#
		Hit(controller.hero, 5).trigger(self.mark2)
		self.change_turn(opponent)
		##########controller
		self.play_card(self.mark1, controller, target=self.mark2)#
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		card2=self.mark2
		for card in [controller.hero, self.mark2]:
			self.print_stats ("***",card)
	pass

class pp_CS3_007(Preset_Play):# <8>[1637]
	""" Novice Zapper
	[Spell Damage +1] [Overload:] (1) """
	class1=CardClass.SHAMAN
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CS3_007',controller)#
		#self.mark2=self.exchange_card('minionH6',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		#self.play_card(self.mark1, controller)#
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" spellpowerとoverloadの値を視認"%())
		print("spellpower=%d" % controller.spellpower)
		print("overload=%d" % controller.overloaded)
		for card in [card1]:
			self.print_stats ("***",card)
	pass

class pp_CS3_016(Preset_Play):# <8>[1637]
	""" Novice Zapper
	[Spell Damage +1] [Overload:] (1) """
	class1=CardClass.PALADIN
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CS3_016',controller)#
		self.mark2=self.exchange_card('minionH2',opponent)#もしくはH3
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)#secretを設置
		self.change_turn(controller)
		##########opponent
		self.play_card(self.mark2, opponent)#ミニオンを場に出す
		self.change_turn(opponent)
		##########controller
		self.change_turn(controller)
		##########opponent
		self.attack_card(self.mark2, controller.hero, opponent)#敵ミニオンで自ヒーローを攻撃
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" controllerの秘策、self.mark2 の生死"%())
		print("secrets=%d" % controller.secrets)
		for card in [self.mark2]:
			self.print_stats ("***",card)
	pass

class pp_CORE_AT_075(Preset_Play):
	""" Warhorse Trainer
	Your Silver Hand Recruits have +1 Attack. """
	class1=CardClass.PALADIN
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_AT_075',controller)#
		self.mark2=self.exchange_card('CS2_101t',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		##########controller
		self.play_card(self.mark1, controller)#
		#self.play_card(self.mark2, controller)#
		self.activate_heropower(controller)
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark2, opponent)#ミニオンを場に出す
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		card1=self.mark1
		print(" シルバーハンドにバフが付いていることを目視"%())
		for card in controller.hand:
			self.print_stats ("hand",card, show_buff=True, old_cost=True)
		for card in controller.field:
			self.print_stats ("field",card, show_buff=True, old_cost=True)
	pass
