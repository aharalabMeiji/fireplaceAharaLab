from ..utils import *

#Barrens_Druid=['BAR_533','BAR_533t','BAR_534','BAR_534e',
#'BAR_535','BAR_536','BAR_536t','BAR_536t2','BAR_536e','BAR_536te','BAR_536t2e',
#'BAR_537','BAR_537e','BAR_538','BAR_538t',
#'BAR_539','BAR_539e','BAR_540','BAR_549','BAR_549e','BAR_720','BAR_720e',
#'WC_004','WC_004t','WC_006','WC_006e','WC_036','WC_036t1',]

class BAR_533:#OK <2>[1525]
	""" Thorngrowth Sentries
	Summon two 1/2 Turtles with [Taunt]. """
	play = Summon(CONTROLLER, 'BAR_533t') * 2
	pass

class BAR_533t:# <2>[1525]
	""" Thornguard Turtle
	[Taunt] """
	#####
	pass

class BAR_534:#OK <2>[1525]
	""" Pride's Fury
	Give your minions +1/+3. """
	play = Buff(FRIENDLY_MINIONS, 'BAR_534e')
	pass
BAR_534e=buff(1,3)# <2>[1525]
""" Overrun
+1/+3. """

class BAR_535:#OK <2>[1525]
	""" Thickhide Kodo
	[Taunt][Deathrattle:] Gain 5 Armor. """
	deathrattle = GainArmor(FRIENDLY_HERO, 5)
	pass

class BAR_536:#OK <2>[1525]
	""" Living Seed (Rank 1)
	Draw a Beast. Reduce its Cost by (1). <i>(Upgrades when you have 5 Mana.)</i> """
	play = Give(CONTROLLER, RANDOM(FRIENDLY_DECK + BEAST)).then(Buff(Give.CARD, "BAR_536e"))
	pass
BAR_536e=buff(cost=-1)#<8>[1525]

class BAR_536t:#OK <2>[1525]
	""" Living Seed (Rank 2)
	Draw a Beast. Reduce its Cost by (2). <i>(Upgrades when youhave 10 Mana.)</i> """
	play = Give(CONTROLLER, RANDOM(FRIENDLY_DECK + BEAST)).then(Buff(Give.CARD, "BAR_536te"))
	pass
BAR_536te=buff(cost=-2)#<8>[1525]

class BAR_536t2:#OK <2>[1525]
	""" Living Seed (Rank 3)
	Draw a Beast.Reduce its Cost by (3). """
	play = Give(CONTROLLER, RANDOM(FRIENDLY_DECK + BEAST)).then(Buff(Give.CARD, "BAR_536t2e"))
	pass
BAR_536t2e=buff(cost=-3)#<8>[1525]

class BAR_537:#OK <2>[1525]
	""" Razormane Battleguard
	The first [Taunt] minion you_play each turn costs_(2) less. """
	play = Buff(FRIENDLY_HAND + TAUNT, 'BAR_537e')
	events = OWN_TURN_BEGIN.on(Buff(FRIENDLY_HAND + TAUNT, 'BAR_537e'))
	pass

class BAR_537e:# <2>[1525]
	""" Razorforced
	Each turn, your first [ Taunt] minion costs (2) less. """
	cost = lambda self, i : max(i-2, 0)
	events = [
		Play(CONTROLLER, FRIENDLY_MINIONS + TAUNT).on(Destroy(SELF)),
		OWN_TURN_END.on(Destroy(SELF)),
		]
	pass

class BAR_538:#OK <2>[1525]
	""" Druid of the Plains
	[Rush][Frenzy:] Transform into a 6/7 Kodo with [Taunt]. """
	events = Damage(SELF).on(Frenzy(SELF,Morph(SELF, 'BAR_538t')))
	pass

class BAR_538t:# <2>[1525]
	""" Druid of the Plains
	[Taunt] """
	#
	pass

class BAR_539:#OK <2>[1525]
	""" Celestial Alignment
	Set each player to 0 Mana Crystals. Set the Cost of cards in all hands and decks to (1). """
	def play(self):
		controller = self.controller
		opponent = controller.opponent
		controller.max_mana = 0
		opponent.max_mana = 0
		yield Buff(FRIENDLY_HAND,'BAR_539e')
		yield Buff(FRIENDLY_DECK,'BAR_539e')
		yield Buff(ENEMY_HAND,'BAR_539e')
		yield Buff(ENEMY_DECK,'BAR_539e')
	pass

class BAR_539e:# <2>[1525]
	""" Vortexed
	Costs (1). """
	cost = SET(1)
	pass

class BAR_540_Action(TargetedAction):
	TARGET = ActionArg
	def do(self, source, target):
		new_card = target
		new_card.taunt = False
		new_card.zone = Zone.PLAY
		pass
	pass
class BAR_540:#OK <2>[1525]
	""" Plaguemaw the Rotting
	After a friendly minion with [Taunt] dies, summon a new_copy of it without [Taunt]. """
	events = Death(FRIENDLY + TAUNT).on(BAR_540_Action(ExactCopy(Death.ENTITY)))
	pass

class BAR_549:#OK <2>[1525]
	""" Mark of the Spikeshell
	Give a minion +2/+2.If it has [Taunt], add a copy of it to your hand. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0}
	def play(self):
		yield Buff(TARGET,'BAR_549e')
		if self.target.taunt:
			yield Give(CONTROLLER, Copy(TARGET))
	pass

BAR_549e=buff(2,2)# <2>[1525]
""" Everbark
+2/+2. """

class BAR_720:#OK <2>[1525]
	""" Guff Runetotem
	After you cast a Nature spell, give another friendly minion +2/+2. """
	events = Play(CONTROLLER, SPELL + NATURE).on(Buff(RANDOM(FRIENDLY_MINIONS - SELF),'BAR_720e'))
	pass
BAR_720e=buff(2,2)# <2>[1525]
""" Guff's Buff
+2/+2. """

class WC_004:#OK <2>[1525]
	""" Fangbound Druid
	[Taunt][Deathrattle:] Reduce the Cost of a Beast in your hand by (2). """
	deathrattle = Buff(RANDOM(FRIENDLY_HAND + BEAST),'WC_004t')
	pass
WC_004t=buff(cost=-2)# <2>[1525]
""" Nightmare Trapped
Costs (2) less. """
#
pass

class WC_006:#OK <2>[1525]
	""" Lady Anacondra
	Your Nature spells cost (2) less. """
	play = Buff(FRIENDLY_HAND + NATURE, 'WC_006e')
	pass
WC_006e=buff(cost=-2)# <2>[1525]
""" Natural Empowerment
Costs (2) less. """

class WC_036:#OK <2>[1525]
	""" Deviate Dreadfang
	After you cast a Nature spell, summon a 4/2 Viper with [Rush]. """
	events = Play(CONTROLLER, SPELL+ NATURE).on(Summon(CONTROLLER, 'WC_036t1'))
	pass

class WC_036t1:# <2>[1525]
	""" Deviate Viper
	[Rush] """
	#
	pass

