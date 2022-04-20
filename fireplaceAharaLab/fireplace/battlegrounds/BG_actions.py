from fireplace.actions import GameAction, TargetedAction, EventListener, ActionArg, IntArg
from hearthstone.enums import Zone

import random

## Battlegrounds actions

class ReduceUpgradingCost(TargetedAction):
	TARGET=ActionArg()
	AMOUNT=IntArg()
	def do(self, source, target, amount):
		if hasattr(target,'UpgradeCost'):
			target.UpgradeCost = max(target.UpgradeCost-amount, 0)
		pass

class Avenge(TargetedAction):
	TARGET=ActionArg()
	AMOUNT=IntArg()
	ACTIONS=ActionArg()
	def do(self, source, target, amount, actions):
		log.info("Avenge Counter on %r -> %i, %r", source, (source._sidequest_counter_+1), actions)
		source._sidequest_counter_ += 1
		if source._sidequest_counter_== amount:
			source._sidequest_counter_ = 0
			if actions!=None:
				if not isinstance(targetaction,list):
					targetaction = [targetaction]
				for action in targetaction:
					if isinstance(action, TargetedAction):
						action.trigger(source)

class UpgradeTier(TargetedAction):
	TARGET=ActionArg()#controller
	def do(self, source, target):
		TierUpCost={1:5, 2:7, 3:9, 4:12, 5:11}
		controller = target
		bar = target.game
		if controller.Tier<=5 and controller.mana >= controller.TierUpCost:
			controller.Tier += 1
			controller.used_mana += controller.TierUpCost
			controller.TierUpCost = TierUpCost[controller.Tier]
			self.broadcast(source, EventListener.ON, controller)
			self.broadcast(source, EventListener.AFTER, controller)
	pass

class Rerole(TargetedAction): ## battlegrounds
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		game = controller.game
		bartender = game.bartender
		if controller.mana>=game.reroleCost:
			self.broadcast(source, EventListener.ON, target)
			controller.used_mana += game.reroleCost
			for i in range(len(bartender.field)):
				card=bartender.field[0]
				game.parent.ReturnCard(card)
			for card in range(bartender.BobsTmpFieldSize):
				card = game.parent.DealCard(bartender, controller.Tier)
				card.controller = bartender#たぶん不要
				card.zone = Zone.PLAY
			self.broadcast(source, EventListener.AFTER, target)
		pass


