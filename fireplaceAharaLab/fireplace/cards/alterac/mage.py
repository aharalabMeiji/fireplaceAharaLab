from ..utils import *

#Alterac_Mage=['AV_114','AV_114e','AV_115','AV_115e5','AV_116','AV_200','AV_212','AV_212e','AV_218','AV_218t','AV_282','AV_282t','AV_282t2','AV_282t3','AV_282t4','AV_282t5','AV_283','AV_284','AV_290',]

class AV_114_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		highestcost=[]
		for card in target.hand:
			if len(highestcost)==0:
				highestcost = [card]
			elif highestcost[0].cost < card.cost:
				highestcost = [card]
			elif highestcost[0].cost == card.cost:
				highestcost.append(card)
		for card in highestcost:
			target.game.trigger(target, [Buff(card, 'AV_114e')], event_args=None)
		pass
	pass
class AV_114:
	""" Shivering Sorceress (1/2/2)
	Battlecry: Reduce the Cost of the highest Cost spell in your hand by (1).
	"""
	play = AV_114_Action(CONTROLLER)
	pass
AV_114e=buff(cost=-1)

class AV_115:
	""" Amplified Snowflurry (2/2/3)
	Battlecry: Your next Hero Power costs (0) and Freezes the target.
	"""
	play = Buff(CONTROLLER, 'AV_115e5')
	pass
class AV_115e5:
	update = Refresh(FRIENDLY_HERO_POWER, {GameTag.COST:SET(0)})
	events = Activate(CONTROLLER, HERO_POWER).on(Freeze(Activate.TARGET), Destroy(SELF))

class AV_116_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		cardlist = []
		for card in target.deck:
			if card.cost >6:
				cardlist.append(card)
		card = random.choice(cardlist)
		target.game.trigger(target, [Give(target, card)], event_args=None)
		pass
	pass
class AV_116:
	""" Arcane Brilliance (4) Arcane
	Add a copy of a 7, 8, 9, and 10-Cost spell in your deck to your hand.
	"""
	play = AV_116_Action(CONTROLLER)
	pass

class AV_200:
	""" Magister Dawngrasp (8/*/5) Hero
	Battlecry: Recast a spell from each spell school you've cast this game.
	"""
	def play(self):
		for school in [SpellSchool.ARCANE, SpellSchool.NATURE, SpellSchool.FEL, SpellSchool.FIRE, SpellSchool.FROST, SpellSchool.HOLY, SpellSchool.SHADOW]:
			cards = []
			for log in self.controller.play_log:
				if log.CardType==CardType.SPELL and log.spell_school==school:
					cards.append(log)
			if log != []:
				card = random.choice(cards)
				Summon(CONTROLLER, card.id)
			pass
		pass
		#ChangeHero(self).trigger(controller)
	pass

class AV_212:
	""" Siphon Mana (2) Arcane
	Deal 2 damage. Honorable Kill: Reduce the Cost of spells in your hand by (1).
	"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0  }
	play = Hit(TARGET, 2)
	honorable_kill = Buff(FRIENDLY_HAND, 'AV_212e')
	pass
AV_212e=buff(cost=-1)

class AV_218:
	""" Mass Polymorph (7) Arcane
	Transform all minions into 1/1 Sheep."""
	play = Morph(ALL_MINIONS, 'AV_218t')
	pass
class AV_218t:
	"""  sheep """
	pass

class AV_282:
	""" Build a Snowman (3) Frost
	Summon a 3/3 Snowman that Freezes.  Add 'Build a Snowbrute' to your hand.
	"""
	play = Summon(CONTROLLER, 'AV_282t'), Give(CONTROLLER, 'AV_282t2')
	pass
class AV_282t:
	""" Snowman (3/3/3) Elemental
	Freeze any character damaged by this minion
	"""
	events = Attack(SELF, ENEMY_CHARACTERS).on(Freeze(Attack.DEFENDER))
	pass
class AV_282t2:
	""" Build a Snowbrute (6) Frost
	Summon a 6/6 Snowbrute that Freezes.  Add 'Build a Snowgre' to your hand.
	play = Summon(CONTROLLER, 'ALT_MAG_9t3'), Give(CONTROLLER, 'ALT_MAG_9t4')
	"""
	pass
class AV_282t3:
	""" Snowbrute (6/6/6) Elemental
	Freeze any character damaged by this minion.
	"""
	events = Attack(SELF, ENEMY_CHARACTERS).on(Freeze(Attack.DEFENDER))
	pass
class AV_282t4:
	""" Build a Snowgre (9) Frost
	Summon a 9/9 Sbiwgre tgat Freezes.
	"""
	play = Summon(CONTROLLER, 'ALT_MAG_9t5')
	pass
class AV_282t5:
	""" Snowgre (9/9/9) Elemental
	Freeze any character damaged by this minion.
	"""
	events = Attack(SELF, ENEMY_CHARACTERS).on(Freeze(Attack.DEFENDER))
	pass

class AV_283_Action(TargetedAction):#
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		count = 0
		while True:	
			card = RandomSpell(card_class=CardClass.MAGE).evaluate(source)
			if card.cost + count <= 20:
				count += card.cost
				target = None
				if card.requires_target():
					target = random.choice(controller.opponent.characters)
				controller.game.trigger(controller, [Play(card,target,None,None)],event_args=None)
			else:
				break
			pass
		pass
	pass
class AV_283:
	""" Rune of the Archmage (9)
	Cast 20 Mana worth of Mage spells at enemies.
	"""
	play = AV_283_Action(CONTROLLER)
	pass

class AV_284:
	""" Balinda Stonehearth (6/5/5)
	Battlecry: Draw 2 spells. Swap their Costs with this minion's stats."""
	def play(self):
		card1=Give(CONTROLLER, RANDOM(FRIENDLY_DECK + SPELL))
		card1cost=5
		if card1!=[]:
			card1cost = card1[0][0].cost
			card1[0][0].cost = self.atk
			self.atk=card1cost
		card2=Give(CONTROLLER, RANDOM(FRIENDLY_DECK + SPELL))
		card2cost=5
		if card2!=[]:
			card2cost = card2[0][0].cost
			card2[0][0].cost = self.max_health
			self.max_helth=card2cost
		pass
	pass

class AV_290:
	""" Iceblood Tower (10)
	At the end of your turn, cast another spell from your deck. Lasts 3 turns.	"""
	events=[
		OWN_TURN_END.on(Play(RANDOM(FRIENDLY_DECK + SPELL))),
		OWN_TURN_BEGIN.on(SidequestCounter(CONTROLLER, 3, [Destroy(SELF)])),
		]
	pass

