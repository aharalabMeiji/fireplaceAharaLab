from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Summon, Hit, Shuffle
from hearthstone.enums import CardClass, CardType

def sunken_druid():
	PresetGame(pp_TSC_658)#OK
	pass

##########TSC_658###############

class pp_TSC_658(Preset_Play):# 
	""" Hedra the Heretic
	[Battlecry:] For each spell you've cast while holding this, summon a minion of that spell's Cost. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID	
	def preset_deck(self):
		self.mark1=self.exchange_card('TSC_658', self.controller)
		self.mark2=self.exchange_card('spellC2', self.controller)
		self.mark3=self.exchange_card('spellC3', self.controller)
		self.mark4=Summon(self.controller, self.card_choice('minionH3')).trigger(self.opponent)
		self.mark4=self.mark4[0][0]
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
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("field", card, old_cost=True)
		costs=[]
		for action in self.controller._targetedaction_log:
			if isinstance(action['class'],Summon) and action['source'].id=='TSC_658':
				minion = action['target_args'][0][0]
				assert minion.type==CardType.MINION, "type"
				costs.append(minion.cost)
		assert len(costs)==2, "costs"
		assert costs[0]==2 and costs[1]==3, "costs"

		pass
		
#########################
