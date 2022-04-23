from fireplace.actions import GameAction, TargetedAction, EventListener, ActionArg, CardArg, IntArg, Summon, Give, Choice
from fireplace.dsl import LazyNum, LazyValue, Selector
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
		TierUpCost={1:5, 2:7, 3:8, 4:11, 5:10}
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
		if game.free_rerole>0:
			game.reroleCost=0
			game.free_rerole -= 1
		elif game.free_rerole==0:
			game.reroleCost=1
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

class SummonOnce(Summon):
	"""
	Make player targets summon \a id onto their field.
	This works for equipping weapons as well as summoning minions.
	"""
	TARGET = ActionArg()
	CARD = CardArg()

	def do(self, source, target, cards):
		if target.type != CardType.PLAYER:
			log.info("<><><><><><><><><><><><>")
			log.info("%s is not a player, he/she cannot summon anything", target)
			log.info("<><><><><><><><><><><><>")
			return
		log.info("%s summons %r", target, cards)

		if not isinstance(cards, list):
			cards = [cards]

		for card in cards:
			if not hasattr(card, 'is_summonable') or not card.is_summonable():
				continue
			target.add_summon_log(card)
			if card.controller != target:
				card.controller = target
			if card.zone != Zone.PLAY:
				if source.type == CardType.MINION and source.zone == Zone.PLAY:
					source_index = source.controller.field.index(source)
					card._summon_index = source_index + ((self.trigger_index + 1) % 2)
				card.zone = Zone.PLAY
			## no broadcasting
		return cards

class GetFreeRerole(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		controller.game.free_rerole += 1
		pass
	pass

class DiscoverTwice(Choice):
	def choose(self, card):
		self.source._sidequest_counter_ += 1
		if self.source._sidequest_counter_>=2:
			self.next_choice=None
		else:
			self.next_choice=self
		super().choose(card)
		card.zone = Zone.HAND
		cards = self._args[1]
		if isinstance(cards, LazyValue):
			self.cards = cards.evaluate(self.source)

class Sell(TargetedAction):
	TARGET = ActionArg()
	CARD = CardArg()
	def do(self, source, target, card):
		controller = target
		if isinstance(card,list):
			card = card[0]
		for c in controller.field:
			if c==card:
				self.broadcast(source, EventListener.ON, target, card)
				self.broadcast(source, EventListener.AFTER, target, card)
				card.zone=Zone.GRAVEYARD
				controller.used_mana -= 1
				return
		pass
