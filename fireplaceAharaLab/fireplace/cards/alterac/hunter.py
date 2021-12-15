from ..utils import *

Alterac_Hunter=['AV_113','AV_113p','AV_147','AV_147e','AV_224','AV_226','AV_226e','AV_244','AV_244e','AV_333','AV_334','AV_334e','AV_335','AV_335e','AV_336','AV_336e','AV_337','AV_337t',
	]

class AV_113:
	"""Beaststalker Tavish (6/*/5) Hero
	Battlecry: Discover and cast 2 Improved Secrets."""
	play = Discover(CONTROLLER, RandomSpell(secret=True)) #, # improved_secret=True
		### ChangeHero(SELF)
	pass
class AV_113p:
	""" Summon Pet (hero power)
	&lt;b&gt;Hero Power&lt;/b&gt;Summon an Animal Companion. """
	pass

class AV_147:
	""" Dun Baldar Bunker (2) Lasts
	At the end of your turn, draw a Secret and set its Cost to (1). Lasts 3 turns."""
	tags={GameTag.SIDEQUEST:True, }
	events = [
		OWN_TURN_END.on(Give(CONTROLLER, RandomSpell(secret=True)).then(Buff(Give.CARD,'AV_147e'))),
		OWN_TURN_BEGIN.on(SidequestCounter(SELF, 3, [Destroy(SELF)])),
		]	
	pass
class AV_147e:
	cost=SET(1)
	pass

class AV_224:##
	""" Spring the Trap (4)
	Deal 3 damage to a minion and cast a Secret from your deck. Honorable Kill: Cast 2."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0,}
	play = Hit(TARGET, 3),CastSecret(RANDOM(FRIENDLY_DECK + SECRET)) # Play?
	honorable_kill = CastSecret(RANDOM(FRIENDLY_DECK + SECRET))
	pass

class AV_226:
	""" Ice Trap (2) frost
	Secret: When your opponent casts a spell, return it to their hand instead. It costs (1) more."""
	secret = Play(OPPONENT, SPELL).on(
		Reveal(SELF),
		Bounce(Play.CARD),
		Buff(Play.CARD,'AV_226e')
		)
	pass
AV_226e=buff(cost=1)

class AV_244:
	""" Bloodseeker (2/2/2) weapon
	Honorable Kill: Gain +1/+1."""
	honorable_kill = Buff(SELF, 'AV_244e')
	pass
AV_244e=buff(1,1)

class AV_333: ###?????maybe
	""" Revive Pet (3) nature
	Discover a friendly Beast that died this game. Summon it. """
	play = GenericChoiceBattlecry(CONTROLLER, RANDOM(FRIENDLY_KILLED + BEAST))
	pass

class AV_334:
	""" Stormpike Battle Ram (4/4/3) beast
	Rush Deathrattle: Your next Beast costs (2) less."""
	deathrattle = Buff(FRIENDLY_HAND + BEAST, 'AV_334e')
	pass
class AV_334e:
	cost = lambda self, i : max(0,i-2)
	events = Play(CONTROLLER, FRIENDLY_HAND+BEAST).on(Destroy(SELF))

class AV_335:
	""" Ram Tamer (3/4/3)
	Battlecry: If you control a Secret, gain +1/+1 and Stealth."""
	play = Find(FRIENDLY_SECRETS) & Buff(SELF, 'AV_335e')
	pass
AV_335e=buff(atk=1,health=1,stealth=True)

class AV_336: ################################ need the latter half
	""" Wing Commander Ichman (9/5/4)
	[Battlecry]: Summon a Beast from your deck and give it [Rush]. If it kills a minion this turn, repeat."""
	play = Summon(CONTROLLER, RANDOM(FRIENDLY_DECK + BEAST)).then(Buff(Summon.CARD, 'AV_336e'))
	pass
AV_336e=buff(rush=True)

class AV_337:
	""" Mountain Bear (7/5/6) beast
	[Taunt] [Deathrattle]: Summon two 2/4 Cubs with [Taunt]."""
	deathrattle = Summon(CONTROLLER, 'AV_337t') * 2
	pass
class AV_337t:
	"""  """
	pass


