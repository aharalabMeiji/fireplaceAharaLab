from ..utils import *

class ALT_HUN_1:
	""" Ice Trap (2) frost
	Secret: When your opponent casts a spell, return it to their hand instead. It costs (1) more."""
	secret = Play(OPPONENT, SPELL).on(
		Reveal(SELF),
		Bounce(Play.CARD),
		Buff(Play.CARD,'ALT_HUN_1e')
		)
	pass
ALT_HUN_1e=buff(cost=1)

class ALT_HUN_2:
	""" Stormpike Battle Ram (4/4/3) beast
	Rush Deathrattle: Your next Beast costs (2) less."""
	deathrattle = Buff(FRIENDLY_HAND + BEAST, 'ALT_HUN_2e')
	pass
class ALT_HUN_2e:
	cost = lambda self, i : max(0,i-2)
	events = Play(CONTROLLER, FRIENDLY_HAND+BEAST).on(Destroy(SELF))

class ALT_HUN_3:
	""" Mountain Bear (7/5/6) beast
	[Taunt] [Deathrattle]: Summon two 2/4 Cubs with [Taunt]."""
	deathrattle = Summon(CONTROLLER, 'ALT_HUN_3t') * 2
	pass
class ALT_HUN_3t:
	"""  """
	pass

class ALT_HUN_4:
	"""Beaststalker Tavish (6/*/5) Hero
	Battlecry: Discover and cast 2 Improved Secrets."""
	play = Discover(CONTROLLER, RandomSpell(secret=True)) #, # improved_secret=True
		### ChangeHero(SELF)
	pass

class ALT_HUN_5:
	""" Spring the Trap (4)
	Deal 3 damage to a minion and cast a Secret from your deck. Honorable Kill: Cast 2."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0,}
	play = Hit(TARGET, 3)#,
		#CastSecret(RANDOM(FRIENDLY_DECK + SECRET)) # Play?
	#honorable_kill = CastSecret(RANDOM(FRIENDLY_DECK + SECRET))
	pass

class ALT_HUN_6:
	""" Ram Tamer (3/4/3)
	Battlecry: If you control a Secret, gain +1/+1 and Stealth."""
	play = Find(FRIENDLY_SECRETS) & Buff(SELF, 'ALT_HUN_6e')
	pass
ALT_HUN_6e=buff(atk=1,health=1,stealth=True)

class ALT_HUN_7: ###?????maybe
	""" Revive Pet (3) nature
	Discover a friendly Beast that died this game. Summon it. """
	play = GenericChoiceBattlecry(CONTROLLER, RANDOM(FRIENDLY_KILLED + BEAST))
	pass

class ALT_HUN_8: ################################ need the latter half
	""" Wing Commander Ichman (9/5/4)
	[Battlecry]: Summon a Beast from your deck and give it [Rush]. If it kills a minion this turn, repeat."""
	play = Summon(CONTROLLER, RANDOM(FRIENDLY_DECK + BEAST)).then(Buff(Summon.CARD, 'ALT_HUN_8e'))
	pass
ALT_HUN_8e=buff(rush=True)

class ALT_HUN_9:
	""" Dun Baldar Bunker (2) Lasts
	At the end of your turn, draw a Secret and set its Cost to (1). Lasts 3 turns."""
	tags={GameTag.SIDEQUEST:True, }
	events = [
		OWN_TURN_END.on(Give(CONTROLLER, RandomSpell(secret=True)).then(Buff(Give.CARD,'ALT_HUN_9e'))),
		OWN_TURN_BEGIN.on(SidequestCounter(SELF, 3, [Destroy(SELF)])),
		]	
	pass
ALT_HUN_9e=buff(cost=SET(1))

class ALT_HUN_10:
	""" Bloodseeker (2/2/2) weapon
	Honorable Kill: Gain +1/+1."""
	honorable_kill = Buff(SELF, 'ALT_HUN_10e')
	pass
ALT_HUN_10e=buff(1,1)

