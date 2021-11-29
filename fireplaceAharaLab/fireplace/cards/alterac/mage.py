from ..utils import *


class ALT_MAG_1_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		cardlist = []
		for card in target.deck:
			if card.cost >6:
				cardlist.append(card)
		card = random.choice(cardlist)
		target.game.trigger(target, [Give(target, card)], action_arg=None)
		pass
	pass
class ALT_MAG_1:
	""" Arcane Brilliance (4) Arcane
	Add a copy of a 7, 8, 9, and 10-Cost spell in your deck to your hand.
	"""
	play = ALT_MAG_1_Action(CONTROLLER)
	pass

class ALT_MAG_2_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		highestcost=[]
		for card in target.hand:
			if len(hightestcost)==0:
				highestcost = [card]
			elif highestcost[0].cost < card.cost:
				highestcost = [card]
			elif highestcost[0].cost == card.cost:
				highestcost.append(card)
		for card in highestcost:
			target.game.trigger(target, [Buff(card, 'ALT_MAG_2e')], action_arg=None)
		pass
	pass
class ALT_MAG_2:
	""" Shivering Sorceress (1/2/2)
	Battlecry: Reduce the Cost of the highest Cost spell in your hand by (1).
	"""
	play = ALT_MAG_2_Action(CONTROLLER)
	pass
ALT_MAG_2e=buff(cost=-1)

class ALT_MAG_3:
	""" Amplified Snowflurry (2/2/3)
	Battlecry: Your next Hero Power costs (0) and Freezes the target.
	"""
	play = Buff(FRIENDLY_HERO_POWER, 'ALT_MAG_3e')
	pass
class ALT_MAG_3e:
	cost = lambda self, i:0
	events = Activate(CONTROLLER, HERO_POWER).on(
		Freeze(Activate.TARGET),
		Destroy(SELF)
		)

class ALT_MAG_4:
	""" Rune of the Archmage (9)
	Cast 20 Mana worth of Mage spells at enemies.
	"""
	pass

class ALT_MAG_5:
	""" Magister Dawngrasp (8/*/5) Hero
	Battlecry: Recast a spell from each spell school you've cast this game.
	"""
	pass

class ALT_MAG_6:
	""" Mass Polymorph (7) Arcane
	Transform all minions into 1/1 Sheep.
	"""
	pass

class ALT_MAG_7:
	""" Iceblood Tower (10)
	t the end of your turn, cast another spell from your deck. Lasts 3 turns.
	"""
	pass

class ALT_MAG_8:
	""" Balinda Stonehearth (6/5/5)
	Battlecry: Draw 2 spells. Swap their Costs with this minion's stats.
	"""
	pass

class ALT_MAG_9t:
	""" Build a Snowman (3) Frost
	Summon a 3/3 Snowman that Freezes.  Add 'Build a Snowbrute' to your hand.
	"""
	play = Summon(CONTROLLER, 'ALT_MAG_9t'), Give(CONTROLLER, 'ALT_MAG_9t2')
	pass
class ALT_MAG_9t:
	""" Snowman (3/3/3) Elemental
	Freeze any character damaged by this minion
	"""
	events = Attack(SELF, ENEMY_CHARACTERS).on(Freeze(Attack.DEFENDER))
	pass
class ALT_MAG_9t2:
	""" Build a Snowbrute (6) Frost
	Summon a 6/6 Snowbrute that Freezes.  Add 'Build a Snowgre' to your hand.
	play = Summon(CONTROLLER, 'ALT_MAG_9t3'), Give(CONTROLLER, 'ALT_MAG_9t4')
	"""
	pass
class ALT_MAG_9t3:
	""" Snowbrute (6/6/6) Elemental
	Freeze any character damaged by this minion.
	"""
	events = Attack(SELF, ENEMY_CHARACTERS).on(Freeze(Attack.DEFENDER))
	pass
class ALT_MAG_9t4:
	""" Build a Snowgre (9) Frost
	Summon a 9/9 Sbiwgre tgat Freezes.
	"""
	play = Summon(CONTROLLER, 'ALT_MAG_9t5')
	pass
class ALT_MAG_9t5:
	""" Snowgre (9/9/9) Elemental
	Freeze any character damaged by this minion.
	"""
	events = Attack(SELF, ENEMY_CHARACTERS).on(Freeze(Attack.DEFENDER))
	pass

class ALT_MAG_10:
	""" Siphon Mana (2) Arcane
	Deal 2 damage. Honorable Kill: Reduce the Cost of spells in your hand by (1).
	"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0  }
	play = Hit(TARGET, 2)
	honorable_kill = Buff(FRIENDLY_HAND, 'ALT_MAG_10e')
	pass
ALT_MAG_10e=buff(cost=-1)
