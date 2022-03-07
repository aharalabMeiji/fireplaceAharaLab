from ..utils import *

#STORMWIND_DRUID=[
#'SW_419','SW_422','SW_422a','SW_422b','SW_422e','SW_422t',
#'SW_428','SW_428t','SW_428t2','SW_428t4','SW_428t4e',
#'SW_429','SW_429t','SW_431','SW_431e','SW_432','SW_432e','SW_432t',
#'SW_436','SW_436e','SW_437','SW_437e','SW_439','SW_439t','SW_439t2',
#'SW_447','SW_447e','SW_447e2',]

class SW_419:# <2>[1578] ###OK
	""" Oracle of Elune
	After you play a minion that costs (2) or less,summon a copy of it. """
	events = Play(CONTROLLER, MINION  + (COST<3)).on(Summon(CONTROLLER,ExactCopy(Play.CARD)))
	pass
#
class SW_422:# <2>[1578] ###OK
	""" Sow the Soil
	[Choose One] - Give your minions +1 Attack; or_ Summon a 2/2 Treant. """
	choose = ("SW_422a", "SW_422b")
	play = ChooseBoth(SELF) & (
		Summon(CONTROLLER, 'SW_422t'), Buff(FRIENDLY_MINIONS, "SW_422e")
	)

class SW_422a:# <2>[1578]
	""" New Growth
	Summon a 2/2 Treant. """
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	play = Summon(CONTROLLER, 'SW_422t')
	pass

class SW_422b:# <2>[1578]
	""" Fertilizer
	Give your minions+1 Attack. """
	play = Buff(FRIENDLY_MINIONS, "SW_422e")
	pass

SW_422e=buff(atk=1)# <2>[1578]
""" Replanted
+1 Attack. """

class SW_422t:# <2>[1578]
	""" Treant
	 """
	#
	pass

class SW_428:# OK <2>[1578]
	""" Lost in the Park
	[Questline:] Gain 4 Attack with your hero. [Reward:] Gain 5 Armor. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Buff(FRIENDLY_HERO).on(
		SidequestLostInTheParkCounter(SELF, 4, [
			GainArmor(FRIENDLY_HERO,5),
			Summon(CONTROLLER,'SW_428t'), 
			Destroy(SELF)])
		)
	pass

class SW_428t:#OK <2>[1578]
	""" Defend the Squirrels
	[Questline:] Gain 5 Attack with your hero. [Reward:] Gain 5 Armor and draw a card. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Buff(FRIENDLY_HERO).on(
		SidequestLostInTheParkCounter(SELF, 5, [
			GainArmor(FRIENDLY_HERO,5),
			Summon(CONTROLLER,'SW_428t2'), 
			Draw(CONTROLLER),Destroy(SELF)
			])
		)
	pass

class SW_428t2:#OK  <2>[1578]
	""" Feral Friendsy
	[Questline:] Gain 6Attack with your hero.[Reward:] Guff the Tough. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Buff(FRIENDLY_HERO).on(
		SidequestLostInTheParkCounter(SELF, 6, [
			Give(CONTROLLER,'SW_428t4'), 
			Destroy(SELF)
			])
		)
	pass

class SW_428t4:#OK <2>[1578]
	""" Guff the Tough
	[Taunt]. [Battlecry:] Give your hero +8 Attack this turn.Gain 8 Armor. """
	play = Buff(FRIENDLY_HERO,'SW_428t4e'), GainArmor(FRIENDLY_HERO, 8)
	pass

SW_428t4e=buff(atk=8)# <2>[1578]##ONE_TURN_EFFECT
""" Guff's Buff
Your hero has Attack this turn. """
#

class SW_429:#OK <2>[1578]
	""" Best in Shell
	[Tradeable]Summon two 2/7_Turtles with [Taunt]. """
	play = Summon(CONTROLLER, 'SW_429t') * 2
	pass

class SW_429t:# <2>[1578]
	""" Goldshell Turtle
	[Taunt] """
	#
	pass

class SW_431:#OK <2>[1578]
	""" Park Panther
	[Rush]. Whenever this attacks, give your hero+3 Attack this turn. """
	events = Attack(SELF).on(Buff(FRIENDLY_HERO,'SW_431e'))
	pass

SW_431e=buff(atk=3)# <2>[1578] # ONE_TURN_EFFECT
""" Rawr!
+3 Attack this turn. """

class SW_432:#OK <2>[1578]
	""" Kodo Mount
	Give a minion +4/+2 and [Rush]. When it dies, summon a Kodo. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0}
	play = Buff(TARGET, 'SW_432e')
	pass

class SW_432e:# <2>[1578]
	""" On a Kodo
	+4/+2 and [Rush]. [Deathrattle:] Summon a Kodo. """
	tags = {GameTag.DEATHRATTLE:True, GameTag.RUSH:True}
	atk = lambda self,i: i+4
	max_health = lambda self,i: i+2
	deathrattle = Summon(CONTROLLER, 'SW_432t')
	pass

class SW_432t:# <2>[1578]
	""" Guff's Kodo
	[Rush] """
	#
	pass

class SW_436:#OK <2>[1578]
	""" Wickerclaw
	After your hero gains Attack, this minion gains +2 Attack. """
	events = Buff(FRIENDLY_HERO).on(Buff(SELF, 'SW_436e'))
	pass

SW_436e=buff(atk=2)# <2>[1578]
""" Wicked Claws
+2 Attack. """

class SW_437:#OK <2>[1578]
	""" Composting
	Give your minions"[Deathrattle:] Draw__a card." """
	play = Buff(FRIENDLY_MINIONS,'SW_437e')
	pass
class SW_437e:#<12>[1578]
	tags = {GameTag.DEATHRATTLE:True,}
	deathrattle = Draw(CONTROLLER)
	pass
class SW_439:# <2>[1578]
	""" Vibrant Squirrel
	[Deathrattle:] Shuffle 4 Acorns into your deck. When drawn,summon a 2/1 Squirrel. """
	deathrattle = Shuffle(CONTROLLER,'SW_439t')*4
	pass

class SW_439t:# <2>[1578] # CASTSWHENDRAWN
	""" Acorn
	[Casts When Drawn]Summon a 2/1 Squirrel. """
	play = Summon(CONTROLLER,'SW_439t2')
	pass

class SW_439t2:# <2>[1578]
	""" Satisfied Squirrel
	 """
	#
	pass

class SW_447:# <2>[1578]
	""" Sheldras Moontree
	[Battlecry:] The next 3 spells you draw are[Cast When Drawn]. """
	play = Buff(SELF, 'SW_447e')
	pass

class SW_447e_Action(TargetedAction):
	TARGET = ActionArg()
	CARD = CardArg()
	def do(self, source, target, card):
		controller = source.controller
		owner = source.owner
		amount = 3
		CastSpell(card).trigger(controller)
		Discard(card).trigger(controller)
		log.info("Setting Counter on %r -> %i", target, (owner._sidequest_counter_+1))
		owner._sidequest_counter_ += 1
		if owner._sidequest_counter_== amount:
			owner.buffs.remove(target)
			target.zone = Zone.GRAVEYARD
		pass
	pass

class SW_447e:# <2>[1578]
	""" Elune's Guidance
	Your next 3 spells are [Cast When Drawn]. """
	events = Draw(CONTROLLER,SPELL).on(SW_447e_Action(SELF, Draw.CARD))
	pass

class SW_447e2:# <2>[1578]
	""" Elune's Guidance 2
	Your next 3 spells are [Cast When Drawn]. """
	pass

