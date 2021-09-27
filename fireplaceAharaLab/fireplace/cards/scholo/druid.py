from ..utils import *

#'SCH_182e','SCH_617e',
#class SCH_182e:# <2>[1443] <-> <12>[1443]
#	""" Outspoken
#	Increased stats. """
#	#
#	pass

class SCH_242:#OK <2>[1443]
	""" Gibberling
	[Spellburst:] Summon a Gibberling. """
	play = OWN_SPELL_PLAY.on(Summon(CONTROLLER, 'SCH_242'))#
	pass

#class SCH_333:# <2>[1443] -> clownDruid
#	""" Nature Studies
#	[Discover] a spell. Your next one costs (1) less. """
#	play = Discover(CONTROLLER, RandomSpell(card_class=FRIENDLY_CLASS)).then(Buff(FRIENDLY_HAND+SPELL,'SCH_333e'))
#	pass

#class SCH_333e:# <2>[1443] # ONE_TURN_EFFECT なし -> clownDruid
#	""" Nature Studies
#	Your next spell costs (1) less. """
#	cost = lambda self, i: max(0,i-1)
#	events = OWN_SPELL_PLAY.on(Destroy(SELF)),
class SCH_333e2:# <2>[1443]
	""" Studying Nature
	Costs (1) less. """
	#
	pass

#class SCH_427:# <2>[1443] # -> clownDruid
#	""" Lightning Bloom
#	Gain 2 Mana Crystals this turn only.[Overload:] (2) """
#	#
#	pass

class SCH_606:#OK <2>[1443]
	""" Partner Assignment
	Add a random 2-Cost and 3-Cost Beast to_your hand. """
	play = Give(CONTROLLER, RandomBeast(cost=2)),Give(CONTROLLER, RandomBeast(cost=3))
	pass

#class SCH_609:# <2>[1443] # -> clownDruid
#	""" Survival of the Fittest
#	Give +4/+4 to all minions in your hand, deck, and battlefield. """
#	#
#	pass

#class SCH_609e:# <2>[1443]
#	""" Survival of the Fittest
#	+4/+4. """
#	#
#	pass

class SCH_612:# <2>[1443]
	""" Runic Carvings
	[Choose One -] Summon four 2/2 Treant Totems; or [Overload:] (2) to summon them with [Rush]. """
	choose = ('SCH_612a','SCH_612b')
	play = ChooseBoth(CONTROLLER) & (
		Summon(CONTROLLER, 'SCH_612t')*4,

		)
	pass

class SCH_612a:# <2>[1443]
	""" Call to Aid
	Summon four 2/2 Treant Totems. """
	play = Summon(CONTROLLER, 'SCH_612t')*4
	pass

class SCH_612b:# <2>[1443]##
	""" Alarm the Forest
	Summon four 2/2 Treant Totems with [Rush].[Overload:] (2) """
	def play(self):
		controller = self.controller
		for repeat in range(4):
			new_card = Summon(controller, 'SCH_612t').trigger(controller)
			if new_card[0] != []:
				new_card=new_card[0][0]
				new_card.rush = True
		pass
	pass

class SCH_612t:# <2>[1443]
	""" Treant Totem
	 """
	#
	pass

class SCH_613:# <2>[1443]
	""" Groundskeeper
	[Taunt][Battlecry:] If you're holding aspell that costs (5) or more,restore 5 Health. """
	powered_up = Find(FRIENDLY_HAND + SPELL + (COST>4))
	play = powered_up & Heal(FRIENDLY_HERO, 5)
	pass

#class SCH_614:# <2>[1443] # clown-druid
#	""" Forest Warden Omu
#	[Spellburst:] Refresh your Mana Crystals. """
#	#
#	pass

#class SCH_616:# <2>[1443] # -> clownDruid
#	""" Twilight Runner
#	[Stealth]Whenever this attacks, draw 2 cards. """
#	events = Attack(SELF).on(Draw(CONTROLLER)*2)
#	pass

#class SCH_617e:# <2>[1443] <-> <3>[1443]
#	""" Adorable
#	+1/+1. """
#	#
#	pass


