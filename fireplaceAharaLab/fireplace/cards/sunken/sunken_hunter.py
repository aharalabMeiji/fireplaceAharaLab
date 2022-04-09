
from ..utils import *

sunken_hunter=['TSC_023','TSC_070','TSC_071','TSC_071e','TSC_071e2','TSC_072','TSC_073','TSC_929','TSC_929t','TSC_945','TSC_945t','TSC_946','TSC_946e','TSC_946e2','TSC_947','TSC_947e','TSC_947t','TSC_950','TSC_950t','TSC_950t2',]

class TSC_023:# <3>[1658]
	""" Barbed Nets
	Deal $2 damage to an enemy. If you played a Naga while holding this,choose a second target. """
	play = Hit(RANDOM(ENEMY_CHARACTERS),2)
	class Hand:
		events = Play(CONTROLLER, MINION + NAGA).on(GiveBattlecry(SELF, Hit(RANDOM(ENEMY_CHARACTERS),2)))
	pass

class TSC_070_Action(Dredge):
	def choose(self, card):
		super.choose(card)
		if card.race == Race.BEAST:
			card.cost = max(0, card.cost-2)
class TSC_070:# <3>[1658]
	""" Harpoon Gun
	After your hero attacks, [Dredge]. If it's a Beast, reduce its Cost by (2). """
	events = Attack(FRIENDLY_HERO).after(TSC_070_Action(CONTROLLER))
	pass

class TSC_071:# <3>[1658]
	""" Twinbow Terrorcoil
	[Battlecry:] If you've cast aspell while holding this, your next spell casts twice. """
	class Hand:
		events = OWN_SPELL_PLAY.on(Buff(FRIENDLY_HAND + SPELL, 'TSC_071e'))
	pass

class DuplicateBattlecry(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = self.controller
		battlecry = controller.scripts.play
		controller.scripts.play += battlecry
		pass
class TSC_071e:# <3>[1658] #### これでは「2回実行」になってない。
	""" Twinned
	Your next spell casts twice. """
	events = OWN_SPELL_PLAY.on([DuplicateBattlecry(OWNER), Destroy(SELF)])

	pass

class TSC_071e2:# <3>[1658]　####なんだこれは？
	""" Twinning
	Your next spell casts twice. """
	#
	pass

class TSC_072:# <3>[1658]
	""" Conch's Call
	Draw a Naga and a spell. """
	play = Give(FRIENDLY_DECK + NAGA), Give(FRIENDLY_DECK + SPELL)
	pass

class TSC_073:# <3>[1658]
	""" Raj Naz'jan
	After you cast a spell, deal damage equal to its Cost to the enemy Hero. """
	events = OWN_SPELL_PLAY.after(Hit(DENEMY_HERO, COST(Play.CARD))) 
	pass

class TSC_929_Action(TargetedAction):
	TARGET = ActionArg()
	CARD = CardArg()
	def do(self, source, target, card):
		controller = self.controller
		card=Summon(controller, Copy(card)).trigger(controller)
		card = card[0][0]
		SetTag(card, {GameTag.DORMANT: 1}).trigger(controller)
		setattr(card, 'dormant',1)
class TSC_929:# <3>[1658]
	""" Emergency Maneuvers
	[Secret:] When a friendly minion dies, summon a copy of it.It's [Dormant] for 1 turn. """
	secret = Death(FRIENDLY_MINIONS).on(TSC_929_Action(CONTROLLER, Death.ENTITY))
	pass

class TSC_929t:# <3>[1658]
	""" Improved Emergency Maneuvers
	[Secret:] When a friendly minion dies, summon two copies of it.They're [Dormant] for 1 turn. """
	secret = Death(FRIENDLY_MINIONS).on(TSC_929_Action(CONTROLLER, Death.ENTITY), TSC_929_Action(CONTROLLER, Death.ENTITY))
	pass

class TSC_945:# <3>[1658]
	""" Azsharan Saber
	[[Rush].] [Deathrattle:] Put a'Sunken Saber' on thebottom of your deck. """
	#
	pass

class TSC_945t:# <3>[1658]
	""" Sunken Saber
	[[Rush].] [Deathrattle:] Summon a Beast from your deck. """
	#
	pass

class TSC_946:# <3>[1658]
	""" Urchin Spines
	Your spells this turn are [Poisonous]. """
	#
	pass

class TSC_946e:# <3>[1658]
	""" Poisonous Urchin
	Your spells are [Poisonous]. """
	#
	pass

class TSC_946e2:# <3>[1658]
	""" Poisonous
	 """
	#
	pass

class TSC_947:# <3>[1658]
	""" Naga's Pride
	Summon two 2/2 Lionfish. If you played a Naga while holding this, give them +1/+1. """
	#
	pass

class TSC_947e:# <3>[1658]
	""" Well-fed Fish
	+1/+1. """
	#
	pass

class TSC_947t:# <3>[1658]
	""" Lionfish
	 """
	#
	pass

class TSC_950:# <3>[1658]
	""" Hydralodon
	[Colossal +2][Battlecry:] Give your_Hydralodon Heads [Rush]. """
	#
	pass

class TSC_950t:# <3>[1658]
	""" Hydralodon Head
	[Deathrattle:] If you control Hydralodon, summon 2 Hydralodon Heads. """
	#
	pass

class TSC_950t2:# <3>[1658]
	""" Hydralodon Head
	[Deathrattle:] If you control Hydralodon, summon 2 Hydralodon Heads. """
	#
	pass

