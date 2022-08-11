
from ..utils import *

Barrens_Warrior=['BAR_334','BAR_840','BAR_841','BAR_841e',
'BAR_842','BAR_842e','BAR_842e2','BAR_842e3','BAR_842t','BAR_842t2','BAR_843',
'BAR_846','BAR_847','BAR_847e','BAR_896','BAR_896e',
'WC_024','WC_024e','WC_025','WC_025e','WC_026','WC_026t',]
#'BAR_844','BAR_845',

class BAR_334:##OK <10>[1525]
	""" Overlord Saurfang
	[Battlecry:] Resurrect 2 friendly [Frenzy] minions. Deal 1 damage to all other minions. """
	def play(self):
		controller = self.controller
		minionList = controller.death_log
		frenzyList = []
		for card in minionList:
			if hasattr(card,'frenzy') and card.frenzy:
				frenzyList.append(card)
		if len(frenzyList)>2:
			surrectList = random.sample(frenzyList, 2)
		else:
			surrectList = frenzyList
		for card in surrectList:
			yield Summon(controller, card.id)
		yield Hit(ALL_MINIONS - SELF, 1)
		pass
	pass

class BAR_840:##OK <10>[1525]
	""" Whirling Combatant
	[Battlecry and Frenzy:]Deal 1 damage to allother minions. """
	events = Damage(SELF).on(Frenzy(SELF, Hit(ALL_MINIONS - SELF, 1)))
	pass

class BAR_841:##OK <10>[1525]
	""" Bulk Up
	Give a random [Taunt] minion in your hand +1/+1 and copy it. """
	def play(self):
		controller = self.controller
		tauntList=[]
		for card in controller.hand:
			if hasattr(card,'taunt') and card.taunt:
				tauntList.append(card)
		if len(tauntList)>0:
			card = random.choice(tauntList)##
			Buff(card,'BAR_841e').trigger(controller)
			new_card = Give(controller, card.id).trigger(controller)
			if new_card[0] != []:
				new_card = new_card[0][0]
				Buff(new_card, 'BAR_841e').trigger(controller)
		pass
	pass

BAR_841e=buff(1,1)# <10>[1525]
#	""" Swoll
#	+1/+1. """

class BAR_842:##OK <10>[1525]
	""" Conditioning (Rank 1)
	Give minions in your hand +1/+1. <i>(Upgrades when you have 5 Mana.)</i> """
	play = Buff(FRIENDLY_HAND, 'BAR_842e')
	pass
BAR_842e=buff(1,1)# <12>[1525]
class BAR_842t:# <10>[1525]
	""" Conditioning (Rank 2)
	Give minions in your hand +2/+2. <i>(Upgradeswhen you have 10 Mana.)</i> """
	play = Buff(FRIENDLY_HAND, 'BAR_842e2')
	pass
BAR_842e2=buff(2,2)# <12>[1525]
class BAR_842t2:# <10>[1525]
	""" Conditioning (Rank 3)
	Give minions in your hand +3/+3. """
	play = Buff(FRIENDLY_HAND, 'BAR_842e3')
	pass
BAR_842e3=buff(3,3)# <12>[1525]

class BAR_843_Action(TargetedAction):
	TARGET = ActionArg()
	CARDS = CardArg()
	def do(self, source, target, cards):
		controller = target.controller
		if hasattr(target, 'atk'):
			target.atk += len(cards)
		pass
	pass
class BAR_843:##OK <10>[1525]
	""" Warsong Envoy
	[Frenzy:] Gain +1  Attackfor each damaged character. """
	events = Damage(SELF).on(Frenzy(
		SELF, BAR_843_Action(SELF, FRIENDLY_CHARACTERS + DAMAGED)
		))
	pass

#class BAR_844:### bigWarrior
#	"""Outrider's Axe
#	After your hero attacks and kills a minion, draw a card."""
#	events = Attack(FRIENDLY_HERO, ALL_MINIONS).after(
#		Dead(ALL_MINIONS + Attack.DEFENDER) & Draw(CONTROLLER))
#	pass

#class BAR_845:###OK   bigWarrior
#	"""Rancor
#	Deal 2 damage to all minions. Gain 2 Armor for each destroyed."""
#	# 生の苦悩、ケルスザード校長らへんが参考になりそうだがわからん
#	# これでよいなら・・・動いているような感じはある。
#	play = Hit(ALL_MINIONS, 2).then( Dead(ALL_MINIONS + Hit.TARGET) & GainArmor(FRIENDLY_HERO, 2))
#	pass

class BAR_846:##OK <10>[1525]
	""" Mor'shan Elite
	[Taunt]. [Battlecry:] If your hero attacked this turn, summon a copy of this. """
	def play(self):
		controller = self.controller
		hero = controller.hero
		playList = controller.play_this_turn
		for card in playList:
			if card.type == CardType.WEAPON:
				yield Summon(CONTROLLER, ExactCopy(SELF))
				return
		pass
	pass

class BAR_847:##OK <10>[1525]
	""" Rokara
	[Rush]After a friendly minion attacks and survives, give it +1/+1. """
	events = Attack(FRIENDLY_MINIONS).after( 
		-Dead(FRIENDLY_MINIONS+Attack.ATTACKER) & Buff(FRIENDLY_MINIONS+Attack.ATTACKER,'BAR_847e'))
	pass
BAR_847e=buff(1,1)# <12>[1525]

class BAR_896:##OK <10>[1525]
	""" Stonemaul Anchorman
	[Rush][Frenzy:] Draw a card. """
	events = Damage(SELF).on(Frenzy(SELF,
		Draw(CONTROLLER)
		))
	pass
BAR_896e=buff(atk=1)# <10>[1525] # no use
""" Incensed
Increased Attack. """

class WC_024:##OK <10>[1525]
	""" Man-at-Arms
	[Battlecry:] If you have a weapon equipped, gain +1/+1. """
	play = Find(FRIENDLY_WEAPON) & Buff(SELF, 'WC_024e')
	pass

WC_024e=buff(1,1)# <10>[1525]
""" Armed
+1/+1 """

class WC_025:##OK <10>[1525]
	""" Whetstone Hatchet
	After your hero attacks, give a minion in your hand +1 Attack. """
	events = Attack(FRIENDLY_HERO).on(Buff(RANDOM(FRIENDLY_HAND), 'WC_025e'))
	pass

WC_025e=buff(atk=1)# <10>[1525]
""" Armed
+1 Attack """

class WC_026:##OK <10>[1525]
	""" Kresh, Lord of Turtling
	[Frenzy:] Gain 8 Armor. [Deathrattle:] Equip a 2/5 Turtle Spike. """
	events = Damage(SELF).on(Frenzy(SELF, 
		GainArmor(FRIENDLY_HERO, 8)
		))
	deathrattle = Summon(CONTROLLER, 'WC_026t')
	pass

class WC_026t:# <10>[1525]
	""" Turtle Spike
	 """
	#
	pass

