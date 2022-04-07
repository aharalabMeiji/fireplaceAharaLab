from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import CardClass
from utils import postAction

#sunken_druid=['TSC_026','TSC_026t','TSC_650','TSC_650a','TSC_650d','TSC_650t','TSC_650t4','TSC_651','TSC_651e','TSC_652','TSC_653','TSC_654','TSC_656','TSC_656t','TSC_657','TSC_657e','TSC_658','TSC_927','TSC_927e','TSC_927t',]

def sunken_druid():
	#PresetGame(pp_TSC_026)# OK
	#PresetGame(pp_TSC_650)# OK
	#PresetGame(pp_TSC_651)# OK
	#PresetGame(pp_TSC_652)# OK
	#PresetGame(pp_TSC_653)# OK
	#PresetGame(pp_TSC_654)# OK
	#PresetGame(pp_TSC_656)# OK
	#PresetGame(pp_TSC_657)# OK
	#PresetGame(pp_TSC_658)# OK
	PresetGame(pp_TSC_927)# OK
	pass

#########################

class pp_TSC_026(Preset_Play):
	""" Colaque
	[Colossal +1] [Immune] while you control Colaque's Shell. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_026',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark1, controller)
		#from fireplace.actions import Hit
		#Hit(controller.field[1],10).trigger(controller)# optional
		self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.field:
			self.print_stats("field", card)
			print("immune = %s"%(card.immune))
		for card in [controller.hero]:
			self.print_stats("field", card)
			print("armor = %s"%(card.armor))
	pass
		
#########################

class pp_TSC_650(Preset_Play):
	""" Flipper Friends
	[Choose One] - Summon a 6/6 Orca with [Taunt]; or six 1/1 Otters with [Rush]. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_650',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[0])
		self.play_card(self.mark1, controller, choose=self.mark1.choose_cards[1])
		self.change_turn(controller)
		########## opponent
		#self.play_card(self.mark2, opponent)
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.field:
			self.print_stats("field", card)
			print("rush = %s"% card.rush)
			print("taunt = %s"% card.taunt)
	pass
		
#########################

class pp_TSC_651(Preset_Play):
	""" Seaweed Strike
	Deal $4 damage to a minion.If you played a Naga while holding this, also give your hero +4 Attack this turn. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_651',controller)
		self.mark2=self.exchange_card('minionH6',opponent)
		self.mark3=self.exchange_card('TSC_652',controller)#naga
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		#self.play_card(self.mark3, controller)
		self.change_turn(controller)
		########## opponent
		self.play_card(self.mark2, opponent)
		self.change_turn(opponent)
		########## controller
		self.play_card(self.mark1, controller, target=self.mark2)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		card = controller.hero
		self.print_stats("hero", card)
		for card in controller.field:
			self.print_stats("field", card)
		for card in controller.opponent.field:
			self.print_stats("op-field", card)
	pass
		
#########################

class pp_TSC_652(Preset_Play):
	""" Green-Thumb Gardener (NAGA)
	[Battlecry:] Refresh empty Mana Crystals equal to the Cost of the most expensive spell in your hand. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_652',controller)
		self.mark2=self.exchange_card('fire',controller)
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
		print("mana = %d"%controller.mana)
	pass
		
#########################

from fireplace.actions import Hit
class pp_TSC_653(Preset_Play):
	""" Bottomfeeder (1/1/3)
	[Deathrattle:] Add a Bottomfeeder to the bottom of your deck with permanent +2/+2. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_653',controller)
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
		Hit(self.mark1, 4).trigger(opponent)
		#self.play_card(self.mark2, opponent)
		self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.deck:
			self.print_stats("deck", card)
	pass
		
#########################

class pp_TSC_654(Preset_Play):
	""" Aquatic Form (cost=0)
	[Dredge]. If you have the Mana to play the card this turn, draw it. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_654',controller)
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
		for card in controller.deck:
			self.print_stats("deck", card)
		for card in controller.hand:
			self.print_stats("hand", card)
	pass
		
#########################

class pp_TSC_656(Preset_Play):
	""" Miracle Growth
	Draw 3 cards.Summon a Plant with [Taunt] and stats equal to your hand size. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_656',controller)
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
		print("hand size = %d"%(len(controller.hand)))
	pass
		
#########################

class pp_TSC_657(Preset_Play):
	""" Dozing Kelpkeeper
	[Rush]. Starts [Dormant].After you've cast 5 Mana worth of spells, awaken. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_657',controller)
		self.mark2=self.exchange_card('fire',controller)
		self.mark3=self.exchange_card('frost',controller)
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
		self.play_card(self.mark2, controller)
		self.play_card(self.mark3, controller)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller=self.player
		for card in controller.field:
			self.print_stats("field", card)
			print("dormant = %d"%card.dormant)
	pass
		
#########################

class pp_TSC_658(Preset_Play):
	""" Hedra the Heretic
	[Battlecry:] For each spellyou've cast while holdingthis, summon a minionof that spell's Cost. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_658',controller)
		self.mark2=self.exchange_card('fire',controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		########## controller
		self.play_card(self.mark2, controller)
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
	pass
		
#########################

class pp_TSC_927(Preset_Play):
	""" Azsharan Gardens
	Give all minions in your hand +1/+1. Put a 'Sunken Gardens' on the bottom of your deck. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('TSC_927',controller)
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
		for card in controller.hand:
			self.print_stats("hand", card)
		for card in controller.deck:
			self.print_stats("deck", card)
	pass
		
#########################

