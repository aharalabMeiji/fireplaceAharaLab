from ..utils import *

###########################

Core_DemonHunter=[]
Chaos_Strike=True##23.6
Coordinated_Strike=True##23.6
Chaos_Nova=True##23.6
Flamereaper=True##23.6
Sightless_Watcher=True##23.6
Battlefiend=True##23.6
Wrathscale_Naga=True##23.6
Raging_Felscreamer=True##23.6
Feast_of_Souls=True##23.6
Metamorphosis=True##23.6 ## OK
Crimson_Sigil_Runner=True##23.6
Spectral_Sight=True##23.6
Eye_Beam=True##23.6
Aldrachi_Warblades=True##23.6
Ganarg_Glaivesmith=True##23.6
Felfist=True##23.6
Korvas_Bloodthorn=True##23.6
Illidari_Inquisitor=True##23.6


if Chaos_Strike:# 
	Core_DemonHunter+=['CORE_BT_035','BT_035e']
class CORE_BT_035:# <14>[1637]##23.6 ## visually OK
	""" Chaos Strike
	Give your hero +2_Attack this turn. Draw a card. """
	play = Buff(FRIENDLY_HERO, "BT_035e"), Draw(CONTROLLER)
	pass
BT_035e = buff(atk=2)#ONE_TURN_EFFECT

if Coordinated_Strike:# 
	Core_DemonHunter+=['CORE_BT_036','BT_036t']
class CORE_BT_036:# <14>[1637]##23.6 ## visually OK
	""" Coordinated Strike
	Summon three 1/1_Illidari with [Rush]. """
	play = Summon(CONTROLLER, "BT_036t") * 3
	pass
class BT_036t:
	pass

if Chaos_Nova:# 
	Core_DemonHunter+=['CORE_BT_235']
class CORE_BT_235:# <14>[1637]##23.6 ## visually OK
	""" Chaos Nova
	Deal $4 damage to all_minions. """
	play = Hit(ALL_MINIONS,4)
	pass

if Flamereaper:# 
	Core_DemonHunter+=['CORE_BT_271']
class CORE_BT_271:# <14>[1637]##23.6 ####### need check 
	""" Flamereaper
	Also damages the minions next to whomever your hero_attacks. """
	events = Attack(FRIENDLY_HERO).on(Hit( ADJACENT(Attack.DEFENDER), ATK(FRIENDLY_HERO)))
	pass

if Sightless_Watcher:# 
	Core_DemonHunter+=['CORE_BT_323']
class CORE_BT_323:# <14>[1637]##23.6 # visually OK # may check
	""" Sightless Watcher
	[Battlecry:] Look at 3 cards in your deck. Choose one to put on top. """
	play = Choice(CONTROLLER, RANDOM(FRIENDLY_DECK) * 3).then(
		PutOnTop(CONTROLLER, Choice.CARD))
	pass

if Battlefiend:# 
	Core_DemonHunter+=['CORE_BT_351','BT_351e']
class CORE_BT_351:# <14>[1637]##23.6  # visually OK
	""" Battlefiend
	After your hero attacks, gain +1 Attack. """
	events = Attack(FRIENDLY_HERO).after(Buff(SELF, "BT_351e"))
	pass
BT_351e = buff(atk=1)

if Wrathscale_Naga:# 
	Core_DemonHunter+=['CORE_BT_355']
class CORE_BT_355:# <14>[1637]##23.6 ##### not yet #
	""" Wrathscale Naga
	After a friendly minion dies, deal 3 damage to a_random enemy. """
	events = Death(FRIENDLY_MINIONS).after(Hit(RANDOM(ENEMY_MINIONS),3))
	pass

if Raging_Felscreamer:# 
	Core_DemonHunter+=['CORE_BT_416','BT_416e']
class CORE_BT_416:# <14>[1637]##23.6 # visually OK
	""" Raging Felscreamer
	[Battlecry:] The next Demon you play costs (2) less. """
	play = Buff(CONTROLLER, "BT_416e")
	pass
class BT_416e:
	update = Refresh(FRIENDLY_HAND + DEMON, {GameTag.COST: -2})
	events = Play(CONTROLLER, DEMON).on(Destroy(SELF))

if Feast_of_Souls:# 
	Core_DemonHunter+=['CORE_BT_427','BT_429p','BT_429p2']
class CORE_BT_427:# <14>[1637]##23.6 # visually OK
	""" Feast of Souls
	Draw a card for each friendly minion that died this turn. """
	play = Draw(CONTROLLER) * Count(FRIENDLY + MINION + KILLED_THIS_TURN)
	pass




if Metamorphosis:# ### OK ###
	Core_DemonHunter+=['CORE_BT_429','BT_429p','BT_429p2']
class CORE_BT_429:# <14>[1637]##23.6 ### not yet 
	""" Metamorphosis
	Swap your Hero Power to "Deal 4 damage." After 2 uses, swap it back. """
	#ChangeHeroPower
	play = ChangeHeroPower(CONTROLLER, 'BT_429p')
	pass
class BT_429p:
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0,}
	activate = Hit(TARGET, 4), ChangeHeroPower(CONTROLLER, 'BT_429p2')
class BT_429p2:
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, }
	activate = Hit(TARGET, 4), ChangeHeroPower(CONTROLLER, 'HERO_10bp')
#class HERO_10bp:#
#	"""Demon Claws
#	[x][Hero Power]+1 Attack this turn."""
#	activate = Buff(FRIENDLY_HERO, 'HERO_10bpe')
#HERO_10bpe=buff(1,0)	
# BT_429p, BT_429e2


class CORE_BT_430:# <14>[1637] ##22.6 
	""" Warglaives of Azzinoth
	After attacking a minion, your hero may attack again. """
	events = Attack(FRIENDLY_HERO, ALL_MINIONS).after(
		ExtraAttack(FRIENDLY_HERO))
	pass

if Crimson_Sigil_Runner:# 
	Core_DemonHunter+=['CORE_BT_480']
class CORE_BT_480:# <14>[1637]##23.6 # visually OK
	""" Crimson Sigil Runner
	[Outcast:] Draw a card. """
	outcast = Draw(CONTROLLER)
	pass

if Spectral_Sight:# 
	Core_DemonHunter+=['CORE_BT_491']
class CORE_BT_491:# <14>[1637]##23.6 # visually OK
	""" Spectral Sight
	Draw a card.[Outcast:] Draw another. """
	play = Draw(CONTROLLER)
	outcast = Draw(CONTROLLER) * 2
	pass

if Eye_Beam:# 
	Core_DemonHunter+=['CORE_BT_801']
class CORE_BT_801:# <14>[1637]##23.6  # visually OK
	""" Eye Beam
	[Lifesteal]. Deal $3 damage to a minion.[Outcast:] This costs (1). """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 3)
	update = Refresh(OUTERMOST_HAND + SELF, {GameTag.COST: SET(1)})
	pass

if Aldrachi_Warblades:# 
	Core_DemonHunter+=['CORE_BT_921']
class CORE_BT_921:# <14>[1637]##23.6 # visually OK
	""" Aldrachi Warblades
	[Lifesteal] """
	#
	pass

if Ganarg_Glaivesmith:# 
	Core_DemonHunter+=['CS3_017']
	Core_DemonHunter+=['CS3_017e']
class CS3_017:# <14>[1637]##23.6 # visually OK
	""" Gan'arg Glaivesmith
	[Outcast:] Give your hero +3_Attack this turn. """
	outcast=Buff(FRIENDLY_HERO,'CS3_017e')
	pass
CS3_017e=buff(atk=3)# ONE_TURN_EFFECT# <14>[1637]
""" Felfist
+3 Attack this turn. """

if Korvas_Bloodthorn:# 
	Core_DemonHunter+=['CS3_019']##23.6 # visually OK
class CS3_019:# <14>[1637]
	""" Kor'vas Bloodthorn
	[Charge], [Lifesteal]After you play a card with[Outcast], return this to your hand. """
	events = Play(CONTROLLER, FRIENDLY_HAND + OUTCAST).after(Bounce(SELF))
	pass

if Illidari_Inquisitor:# 
	Core_DemonHunter+=['CS3_020']##23.6  # visually OK
class CS3_020:# <14>[1637]
	""" Illidari Inquisitor
	[Rush]. After your hero attacks an enemy, this attacks it too. """
	events = Attack(FRIENDLY_HERO, ENEMY_CHARACTERS).after(
		ExtraAttack(SELF))
	pass

