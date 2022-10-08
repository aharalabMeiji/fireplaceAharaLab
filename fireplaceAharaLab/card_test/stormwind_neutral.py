from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity, CardClass
from utils import postAction
from fireplace.actions import Buff, Hit, Heal, Summon

def stormwind_neutral():
	#PresetGame(pp_SW_059)#OK
	PresetGame(pp_SW_069)# ### OK ###
	#PresetGame(pp_SW_079)#OK
	pass



##########SW_059 ###############

class pp_SW_059 (Preset_Play):# 
	""" Deeprun Engineer
	[Battlecry:] [Discover] a Mech. It costs (1) less. """
	def preset_deck(self):
		self.mark1=self.exchange_card('SW_059', self.controller)
		self.mark4=Summon(self.controller, self.card_choice('minionH3')).trigger(self.opponent)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.choose_action()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card, old_cost=True)
			buffIds=[buff.id for buff in card.buffs]
			if 'SW_059e' in buffIds:
				assert card.cost == card.data.cost-1, "cost"
				theCard=card
		for action in self.controller._targetedaction_log:
			if isinstance(action['class'],Buff) and action['target'].id==theCard.id:
				assert action['source'].id=="SW_059", "source"
				print("'source' is SW_059")
	pass


##########SW_069##########

class pp_SW_069(Preset_Play):
	""" Enthusiastic Banker (3/2/3)
	[x]At the end of your turn, store a card from your deck. [Deathrattle:] Add the stored cards to your hand. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("SW_069", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		print(self.con1.sidequest_list0)
		self.change_turn()
		### con
		self.change_turn()
		### opp
		print(self.con1.sidequest_list0)
		Hit(self.con1,3).trigger(self.opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass

#############SW_079#####################

class pp_SW_079(Preset_Play):
	""" Flightmaster Dungar
	[x][Battlecry:] Choose a flightpath and go [Dormant.] Awaken with a bonus __when you complete it! """
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

