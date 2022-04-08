from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import CardClass
from utils import postAction

#sunken_neutral=['TSC_001','TSC_002','TSC_003','TSC_003e','TSC_007','TSC_013','TSC_017','TSC_020','TSC_020e','TSC_020e2','TSC_032','TSC_032t','TSC_032t2','TSC_034','TSC_052','TSC_052t','TSC_053','TSC_064','TSC_065','TSC_067','TSC_069','TSC_083e','TSC_632','TSC_632e','TSC_638','TSC_638e','TSC_638t','TSC_638t2','TSC_638t3','TSC_638t4','TSC_640','TSC_641','TSC_641ta','TSC_641tae','TSC_641tb','TSC_641tc','TSC_641td','TSC_641tde','TSC_645','TSC_646','TSC_646t','TSC_647','TSC_647e','TSC_649','TSC_649e2','TSC_823','TSC_823e','TSC_826','TSC_827','TSC_827e','TSC_829','TSC_908','TSC_909','TSC_911','TSC_919','TSC_919t','TSC_926','TSC_928','TSC_935','TSC_938','TSC_960','TSC_COIN1','TSC_COIN2',]

def sunken_neutral_test():
	#PresetGame(pp_TSC_001)# OK
	#PresetGame(pp_TSC_002)# OK
	#PresetGame(pp_TSC_003)# 
	#PresetGame(pp_TSC_007)# OK
	#PresetGame(pp_TSC_013)# OK
	PresetGame(pp_TSC_017)# 
	#PresetGame(pp_TSC_020)# 
	#PresetGame(pp_TSC_032)# 
	#PresetGame(pp_TSC_034)# 
	#PresetGame(pp_TSC_052)# 
	#PresetGame(pp_TSC_053)# 
	#PresetGame(pp_TSC_064)# 
	#PresetGame(pp_TSC_065)# 
	#PresetGame(pp_TSC_067)# 
	#PresetGame(pp_TSC_069)# 
	#PresetGame(pp_TSC_632)# 
	#PresetGame(pp_TSC_638)# 
	#PresetGame(pp_TSC_640)# 
	#PresetGame(pp_TSC_641)# 
	#PresetGame(pp_TSC_641ta)# OK
	#PresetGame(pp_TSC_641tb)# 
	#PresetGame(pp_TSC_641tc)# 
	#PresetGame(pp_TSC_641td)# 
	#PresetGame(pp_TSC_911)# OK
	pass

#########################

class pp_TSC_001(Preset_Play):
	""" Naval Mine
	[Deathrattle:] Deal 4 damage to the enemy hero. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_001',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		from fireplace.actions import Hit
		Hit(self.mark1, 10).trigger(controller)
		self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in [controller.opponent.hero]:
			self.print_stats("op hero", card)
	pass

#########################

class pp_TSC_002(Preset_Play):
	""" Pufferfist
	After your hero attacks, deal 1 damage to all enemies. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_002',controller)
		self.mark2=self.exchange_card('weapon',controller)
		self.mark3=self.exchange_card('minionH2',opponent)
		self.mark4=self.exchange_card('minionH5',opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		self.change_turn(controller)
		########## opponent
		self.play_card(self.mark3, opponent)
		self.play_card(self.mark4, opponent)
		self.change_turn(opponent)
		########## controller
		self.play_card(self.mark2, controller)
		self.attack_card(controller.hero, opponent.hero, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.opponent.field:
			self.print_stats("op-field", card)
	pass

#########################

class pp_TSC_003(Preset_Play):
	""" Coilfang Constrictor
	[Battlecry:] Look at 3 cards in your opponent's hand and choose one. It can't be played next turn. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_003',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.opponent.hand:
			self.print_stats("op-hand", card, show_buff=True)
		for card in controller.field:
			self.print_stats("field", card)
	pass

#########################

class pp_TSC_007(Preset_Play):
	""" Gangplank Diver
	[Dormant] for 1 turn.[Rush]. [Immune] while attacking. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_007',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		self.change_turn(opponent)
		########## controller
		#self.change_turn(controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.field:
			self.print_stats("field", card)
			print("dormant = %d, rush = %d, immune_while_attacking=%d"%(card.dormant, card.rush, card.immune_while_attacking))
	pass

#########################

class pp_TSC_013(Preset_Play):
	""" Slimescale Diver
	[Dormant] for 1 turn.[Rush], [Poisonous] """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_013',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.field:
			self.print_stats("field", card)
			print("dormant = %d, rush = %d, poisonous = %d"%(card.dormant, card.rush, card.poisonous))
	pass

#########################

class pp_TSC_(Preset_Play):
	""" 
	"""
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#self.play_card(self.mark3, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			self.print_stats("hand", card)
		for card in controller.field:
			self.print_stats("field", card)
	pass

#########################

class pp_TSC_(Preset_Play):
	""" 
	"""
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#self.play_card(self.mark3, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			self.print_stats("hand", card)
		for card in controller.field:
			self.print_stats("field", card)
	pass

#########################

class pp_TSC_(Preset_Play):
	""" 
	"""
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#self.play_card(self.mark3, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			self.print_stats("hand", card)
		for card in controller.field:
			self.print_stats("field", card)
	pass

#########################

class pp_TSC_(Preset_Play):
	""" 
	"""
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#self.play_card(self.mark3, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			self.print_stats("hand", card)
		for card in controller.field:
			self.print_stats("field", card)
	pass

#########################

class pp_TSC_(Preset_Play):
	""" 
	"""
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#self.play_card(self.mark3, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			self.print_stats("hand", card)
		for card in controller.field:
			self.print_stats("field", card)
	pass

#########################

class pp_TSC_(Preset_Play):
	""" 
	"""
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#self.play_card(self.mark3, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			self.print_stats("hand", card)
		for card in controller.field:
			self.print_stats("field", card)
	pass

#########################

class pp_TSC_(Preset_Play):
	""" 
	"""
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#self.play_card(self.mark3, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			self.print_stats("hand", card)
		for card in controller.field:
			self.print_stats("field", card)
	pass

#########################

class pp_TSC_(Preset_Play):
	""" 
	"""
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#self.play_card(self.mark3, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			self.print_stats("hand", card)
		for card in controller.field:
			self.print_stats("field", card)
	pass

#########################

class pp_TSC_(Preset_Play):
	""" 
	"""
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#self.play_card(self.mark3, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			self.print_stats("hand", card)
		for card in controller.field:
			self.print_stats("field", card)
	pass

#########################

class pp_TSC_(Preset_Play):
	""" 
	"""
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#self.play_card(self.mark3, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			self.print_stats("hand", card)
		for card in controller.field:
			self.print_stats("field", card)
	pass

#########################

class pp_TSC_(Preset_Play):
	""" 
	"""
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#self.play_card(self.mark3, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			self.print_stats("hand", card)
		for card in controller.field:
			self.print_stats("field", card)
	pass

#########################

class pp_TSC_(Preset_Play):
	""" 
	"""
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#self.play_card(self.mark3, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			self.print_stats("hand", card)
		for card in controller.field:
			self.print_stats("field", card)
	pass

#########################

class pp_TSC_(Preset_Play):
	""" 
	"""
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#self.play_card(self.mark3, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			self.print_stats("hand", card)
		for card in controller.field:
			self.print_stats("field", card)
	pass

#########################

class pp_TSC_(Preset_Play):
	""" 
	"""
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#self.play_card(self.mark3, controller)
		#self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			self.print_stats("hand", card)
		for card in controller.field:
			self.print_stats("field", card)
	pass

#########################

class pp_TSC_641ta(Preset_Play):
	""" Ring of Tides
	After you cast a spell, this becomes a copy of it that costs (1). """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_641ta',controller)
		self.mark2=self.exchange_card('AV_292',controller)#Give a minion +2/+2, then give your Beasts +1/+1.
		self.mark3=self.exchange_card('beast',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark3, controller)
		self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		self.change_turn(opponent)
		########## controller
		self.play_card(self.mark2, controller, target=self.mark3)
		self.play_card(self.mark1, controller, target=self.mark3)# 繰り返しバフがつく
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			self.print_stats("hand", card)
		for card in controller.field:
			self.print_stats("field", card)
	pass
		
#########################

class pp_TSC_911(Preset_Play):
	""" Excavation Specialist
	[Battlecry:] [Dredge].Reduce its Cost by (1). """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_911',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.hand:
			self.print_stats("hand", card)
		for card in controller.deck:
			self.print_stats("deck", card, old_cost=True)
	pass

#########################

