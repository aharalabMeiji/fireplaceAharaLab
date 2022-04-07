from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import CardClass
from utils import postAction

#sunken_neutral=['TSC_001','TSC_002','TSC_003','TSC_003e','TSC_007','TSC_013','TSC_017','TSC_020','TSC_020e','TSC_020e2','TSC_032','TSC_032t','TSC_032t2','TSC_034','TSC_052','TSC_052t','TSC_053','TSC_064','TSC_065','TSC_067','TSC_069','TSC_083e','TSC_632','TSC_632e','TSC_638','TSC_638e','TSC_638t','TSC_638t2','TSC_638t3','TSC_638t4','TSC_640','TSC_641','TSC_641ta','TSC_641tae','TSC_641tb','TSC_641tc','TSC_641td','TSC_641tde','TSC_645','TSC_646','TSC_646t','TSC_647','TSC_647e','TSC_649','TSC_649e2','TSC_823','TSC_823e','TSC_826','TSC_827','TSC_827e','TSC_829','TSC_908','TSC_909','TSC_911','TSC_919','TSC_919t','TSC_926','TSC_928','TSC_935','TSC_938','TSC_960','TSC_COIN1','TSC_COIN2',]

def sunken_neutral_test():
	PresetGame(pp_TSC_641ta)# 

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
		self.mark2=self.exchange_card('nature',controller)
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
		for card in controller.hand:
			self.print_stats("hand", card)
	pass
		
