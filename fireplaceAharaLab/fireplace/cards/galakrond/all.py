from ..utils import *

####### galakrond #######


##hunter##

class YOD_005:#OK
	"""Fresh Scent
	&lt;b&gt;Twinspell&lt;/b&gt;Give a Beast +2/+2."""
	requirements = {PlayReq.REQ_FRIENDLY_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Find(TARGET + BEAST) & Buff(TARGET, "YOD_005e"), Give(CONTROLLER,"YOD_005ts")
YOD_005e = buff(2,2)
class YOD_005ts:
	"""Fresh Scent"""
	requirements = {PlayReq.REQ_FRIENDLY_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Find(TARGET + BEAST) & Buff(TARGET, "YOD_005e")

class YOD_004:#OK
	"""Chopshop Copter
	After a friendly Mech dies, add a random Mech to your hand."""
	events = Death(FRIENDLY + MECH).on(Give(CONTROLLER, RandomMech()))

class YOD_036:#OK
	"""Rotnest Drake
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; If you're holding
	a Dragon, destroy a random
	enemy minion."""
	powered_up = HOLDING_DRAGON
	play = powered_up & Destroy(RANDOM_ENEMY_MINION)

## mage ##
class YOD_008:#OK
	"""Arcane Amplifier
	Your Hero Power deals 2_extra damage."""
	#<Tag enumID="217" name="DEATHRATTLE" type="Int" value="1"/>
	tags = {
		GameTag.DEATHRATTLE: 1,
	}
	play = Summon(CONTROLLER, "HERO_08bp2")
	deathrattle = Summon(CONTROLLER, "HERO_08bp")
class HERO_08bp2:
	"""Fireblast 2 (Jaina Proudmoore)"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	activate = Hit(TARGET, 2)

class YOD_007:#OK
	"""Animated Avalanche
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; If you played
	an Elemental last turn,
	summon a copy of this."""
	def play(self):
		current_turn = self.controller.game.turn
		for candidate in self.controller.game.__myLog__:
			if candidate.turn == current_turn-2: #it is my last turn
				if hasattr(candidate.card, 'race'):
					if candidate.card.race == Race.ELEMENTAL:
						Summon(self.controller, candidate.card.id).trigger(self)
		pass

## hero

class YOD_009:#HERO
	"""The Amazing Reno
	&lt;b&gt;Battlecry:&lt;/b&gt; Make all minions disappear. &lt;i&gt;*Poof!*&lt;/i&gt;"""
	play = Destroy(ALL_MINIONS)

## neutral ##

class YOD_030:#OK
	"""Licensed Adventurer
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; If you control
	a &lt;b&gt;Quest&lt;/b&gt;, add a Coin
	to your hand."""
	# no way to access quest
	powered_up = Find(EnumSelector(Zone.SECRET) + FRIENDLY + EnumSelector(GameTag.SIDEQUEST))
	play = powered_up & Give(CONTROLLER, "GAME_005")
class YOD_028:#OK
	"""Skydiving Instructor
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; Summon a
	1-Cost minion from
	your deck."""
	play = Summon(CONTROLLER, RandomMinion(cost=1))
class YOD_006:#OK
	"""Escaped Manasaber
	[x]&lt;b&gt;Stealth&lt;/b&gt;
	Whenever this attacks,
	gain 1 Mana Crystal
	this turn only."""
	play = Attack(SELF,ALL_MINIONS).on(ManaThisTurn(CONTROLLER,1))
class YOD_032:#OK
	"""Frenzied Felwing
	Costs (1) less for each damage dealt to your opponent this turn."""
	class Hand:
		events = Attack(FRIENDLY_CHARACTERS, ENEMY_CHARACTERS).on(Buff(SELF, "YOD_032e")*ATK(Attack.ATTACKER))##not strict
class YOD_032e:
	#update = Refresh(OWNER,tags={GameTag.COST: -1})
	cost = lambda self, i:i-1
	#events = OWN_TURN_BEGIN.on(Destroy(SELF))

class YOD_035:#OK
	"""Grand Lackey Erkh
	After you play a &lt;b&gt;Lackey&lt;/b&gt;, add a &lt;b&gt;Lackey&lt;/b&gt; to your hand."""
	entourage = ["DAL_613", "DAL_614", "DAL_615", "DAL_739",\
	   "DAL_741", "DRG_052" ,"LOOT_306","ULD_616"]
	play = Play(CONTROLLER, EnumSelector(GameTag.MARK_OF_EVIL)).after(Give(CONTROLLER, RandomEntourage()))
class YOD_038:#OK
	"""Sky Gen'ral Kragg
	[x]&lt;b&gt;Taunt&lt;/b&gt;
	&lt;b&gt;Battlecry:&lt;/b&gt; If you've played a
	&lt;b&gt;Quest&lt;/b&gt; this game, summon a
	4/2 Parrot with &lt;b&gt;Rush&lt;/b&gt;."""
	#     no quest controll
	play = Find(EnumSelector(Zone.SECRET) + FRIENDLY + EnumSelector(GameTag.SIDEQUEST)) & Summon(CONTROLLER, "YOD_038t")
class YOD_038t:
	""" Sharkbait """
	pass
class YOD_033:#OK
	"""Boompistol Bully
	&lt;b&gt;Battlecry:&lt;/b&gt; Enemy &lt;b&gt;Battlecry&lt;/b&gt;_cards cost (5)_more next turn."""
	play = Buff(SELF, "YOD_033e")
class YOD_033e:
	update = Refresh(ENEMY_HAND+BATTLECRY, {GameTag.COST: +5})
	events = OWN_TURN_BEGIN.on(Destroy(SELF))
	
class YOD_029:#OK
	"""Hailbringer
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; Summon two 1/1
	Ice Shards that &lt;b&gt;Freeze&lt;/b&gt;."""
	play = Summon(CONTROLLER, "YOD_029t") * 2
class YOD_029t:
	"""Ice Shard
	&lt;b&gt;Freeze&lt;/b&gt; any character damaged by this minion."""
	requirements = {PlayReq.REQ_MINION_TARGET: 0}
	#play = Attack(SELF,TARGET).on(SetTag(TARGET,(GameTag.FROZEN, )))
	play = Attack(SELF,TARGET).on(Freeze(TARGET))

## paladin ##

class YOD_012:#OK
	""" Air Raid
	&lt;b&gt;Twinspell&lt;/b&gt;
	Summon two 1/1 Silver_Hand Recruits with &lt;b&gt;Taunt&lt;/b&gt;."""
	## CS2_101t: Silver Hand Recruit
	play = Summon(CONTROLLER,"CS2_101t")*2, Give(CONTROLLER,"YOD_012ts")
class YOD_012ts:#OK
	""" Air Raid
	Summon two 1/1 Silver Hand Recruits with &lt;b&gt;Taunt&lt;/b&gt;."""
	play = Summon(CONTROLLER,"CS2_101t")*2
class YOD_010:#OK
	""" Shotbot
	&lt;b&gt;Reborn&lt;/b&gt;"""
class YOD_043:#OK
	"""Scalelord
	&lt;b&gt;Battlecry:&lt;/b&gt; Give your Murlocs &lt;b&gt;Divine Shield&lt;/b&gt;."""
	play = SetTag(FRIENDLY_MINIONS + MURLOC, (GameTag.DIVINE_SHIELD,))


#others##
#Boom Squad
#Cleric of Scales
#Fiendish Servant
#Risky Skipper
#Explosive Evolution
#Rising Winds
#Skyvateer
#Steel Beetle
#Twisted Knowledge
#Waxmancy
#Bomb Wrangler
#Chaos Gazer
#Dark Prophecy
#The Fist of Ra-den
#Shadow Sculptor
#Aeon Reaver
#Winged Guardian
#Eye of the Storm


