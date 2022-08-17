from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity, CardClass
from utils import postAction
from fireplace.actions import Hit, Heal, Summon

def stormwind_neutral():
	PresetGame(pp_SW_079)#OK

##################################

class pp_SW_079(Preset_Play):
	""" Flightmaster Dungar
	[x]<b>Battlecry:</b> Choose a flightpath and go <b>Dormant.</b> Awaken with a bonus __when you complete it! """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('SW_079',controller)#Flightmaster Dungar
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark1)#
		postAction(controller)
		self.dormant = self.mark1.dormant
		assert self.dormant==1 or self.dormant==3 or self.dormant==5, "dormant"
		print("dormant==1 or dormant==3 or dormant==5")
		for count in range(self.dormant):
			self.change_turn()
			self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		if self.dormant==5:
			count=0
			for action in self.controller._targetedaction_log:
				if isinstance(action['class'],Hit) and action['source'].id=='SW_079':
					count += 1
			assert count>10, "hit"
			print("SW_079t3 OK")
		elif self.dormant==3:
			count=0
			for action in self.controller._targetedaction_log:
				if isinstance(action['class'],Heal) and action['target']==self.controller.hero:
					count += 1
			assert count>0, "heal"
			print("SW_079t2 OK")
		elif self.dormant==1:
			count=0
			for action in self.controller._targetedaction_log:
				if isinstance(action['class'],Summon) and action['target'].id in ['WC_034t','WC_034t2','WC_034t3','WC_034t4','WC_034t5','WC_034t6','WC_034t7','WC_034t7',]:
					count += 1
			assert count>0, "summon"
			print("SW_079t OK")
		print("There are three patterns of dormant with 1,3,5 turns.")
		pass

##################################

