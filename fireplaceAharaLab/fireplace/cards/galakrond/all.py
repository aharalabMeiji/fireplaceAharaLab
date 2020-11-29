from ..utils import *

####### galakrond #######


##hunter##

class YOD_005:
	"""Fresh Scent
	&lt;b&gt;Twinspell&lt;/b&gt;Give a Beast +2/+2."""
	requirements = {PlayReq.REQ_FRIENDLY_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Find(TARGET + BEAST) & Buff(TARGET, "YOD_005e")
YOD_005e = buff(2,2)


class YOD_004:
	"""Chopshop Copter
	After a friendly Mech dies, add a random Mech to your hand."""
	events = Death(FRIENDLY_MINIONS + MECH).on(Give(CONTROLLER, RandomMech()))

class YOD_036:
	"""Rotnest Drake
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; If you're holding
	a Dragon, destroy a random
	enemy minion."""
	powered_up = HOLDING_DRAGON
	play = powered_up & Destroy(RANDOM_ENEMY_MINION)

## mage ##
class YOD_008:
	"""Arcane Amplifier
	Your Hero Power deals 2_extra damage."""
	update = RefreshHeroPower( {GameTag.ATK: 2})#??????

class YOD_007:##########################################   impossible now
	"""Animated Avalanche
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; If you played
	an Elemental last turn,
	summon a copy of this."""
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABE_AND_ELEMENTAL_PLAYED_LAST_TURN: 0}## not implemented
	#play = Summon( who? )

class YOD_009:
	"""The Amazing Reno
	&lt;b&gt;Battlecry:&lt;/b&gt; Make all minions disappear. &lt;i&gt;*Poof!*&lt;/i&gt;"""
	play = Destroy(ALL_MINIONS)

#others##
#Boom Squad
#Cleric of Scales
#Fiendish Servant
#Risky Skipper
#Air Raid
#Explosive Evolution
#Licensed Adventurer
#Rising Winds
#Shotbot
#Skyvateer
#Steel Beetle
#Twisted Knowledge
#Waxmancy
#Bomb Wrangler
#Chaos Gazer
#Dark Prophecy
#Skydiving Instructor
#Escaped Manasaber
#Frenzied Felwing
#Grand Lackey Erkh
#Sky Gen'ral Kragg
#The Fist of Ra-den
#Boompistol Bully
#Hailbringer
#Scalelord
#Shadow Sculptor
#Aeon Reaver
#Winged Guardian
#Eye of the Storm


