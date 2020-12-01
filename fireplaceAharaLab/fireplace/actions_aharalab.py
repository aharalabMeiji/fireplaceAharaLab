from .actions import GameAction, TargetedAction, ActionArg, IntArg
from .logging import log

class CounterIf(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		return (target.sidequestCounter >= amount)

class ResetCounter(TargetedAction):
	"""

	"""
	TARGET = ActionArg()# sidequest card
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		log.info("Setting Counter on %r to %i", target, amount)
		target.sidequestCounter = amount

class BuffCounter(TargetedAction):
	"""
	"""
	TARGET = ActionArg()# sidequest card
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		log.info("Setting Counter on %r is added by %i", target, amount)
		target.sidequestCounter += amount
		if target.sidequestCounter<0:
			target.sidequestCounter=0

from .actions import Summon
class CountUpSummon(TargetedAction):
	PLAYER=ActionArg()
	CARD=ActionArg()
	def do(self, source, player, card):
		yield Summon(player, MINION).on(BuffCounter(card,1))