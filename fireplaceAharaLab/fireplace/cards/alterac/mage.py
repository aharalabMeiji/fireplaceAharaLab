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
		if len(cardlist)>0:
			card = random.choice(cardlist)
			target.game.trigger(target, [Give(target, card)],	event_args=None)
			pass
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
				if log.type==CardType.SPELL and log.spell_school==school:
					cards.append(log)
			if cards != []:
				card = random.choice(cards)
				CastSpell(card).trigger(self.controller)
			pass
		pass
		#ChangeHero(self).trigger(controller)
	pass
class AV_200p2:
	""" >Arcane Burst (Hero power)
	[x]&lt;b&gt;Hero Power&lt;/b&gt; Deal $@ damage. 
	&lt;b&gt;Honorable Kill:&lt;/b&gt; Gain +2 damage."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, }
	activate = HitScriptDataNum1(SELF, TARGET)
	honorable_kill = AddScriptDataNum1(SELF, 2)
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
	"""
	play = Summon(CONTROLLER, 'AV_282t3'), Give(CONTROLLER, 'AV_282t4')
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
	play = Summon(CONTROLLER, 'AV_282t5')
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
			card = RandomSpell(card_class=CardClass.MAGE).evaluate(source)[0]
			if card.cost + count <= 20:
				count += card.cost
				target = None
				if card.requires_target() and card.targets!=None and card.targets!=[]:
					target = random.choice(card.targets)
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
		card1=Give(CONTROLLER, RANDOM(FRIENDLY_DECK + SPELL)).trigger(self.controller)
		card1cost=5
		if card1!=[] and card1[0]!=[]:
			card1cost = card1[0][0].cost
			card1[0][0].cost = self.atk# =5
			self.atk=card1cost
		card2=Give(CONTROLLER, RANDOM(FRIENDLY_DECK + SPELL)).trigger(self.controller)
		card2cost=5
		if card2!=[] and card2[0]!=[]:
			card2cost = card2[0][0].cost
			card2[0][0].cost = self.max_health# =5
			self.max_health=card2cost
		pass
	pass
#AV_284e=buff(cost=SET(5))
#AV_284e2=buff(atk=SET(1),health=SET(1))

class AV_290:
	""" Iceblood Tower (10) lasts 3 turns
	At the end of your turn, cast another spell from your deck. Lasts 3 turns.	"""
	tags={GameTag.SIDEQUEST:True, }
	events=[
		OWN_TURN_END.on(CastSpell(RANDOM(FRIENDLY_DECK + SPELL))),
		OWN_TURN_BEGIN.on(SidequestCounter(SELF, 3, [Destroy(SELF)])),
		]
	pass


class ONY_006:# <4>[1626]
	""" Deep Breath
	Deal $@ damage to aminion and its neighbors.<i>(Improved by number of_other spells in your hand.)</i> """
	#
	pass

class ONY_007:# <4>[1626]
	""" Haleh, Matron Protectorate
	After you cast a spell, deal 4 damage randomly split among all enemies. """
	#
	pass

class ONY_029:# <4>[1626]
	""" Drakefire Amulet
	[Tradeable][Discover] 2 Dragons. Summon them. """
	#
	pass
