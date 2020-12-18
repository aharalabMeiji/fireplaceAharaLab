from ..utils import *

##### paladin@uldum,,,10,,,,,

class ULD_145:
	"""Brazen Zealot,,1,2,1,Minion,Rare,-,-
	Whenever you summon a minion, gain +1 Attack."""
	events = Summon(CONTROLLER, MINION).on(Buff(SELF, "ULD_145e"))
ULD_145e = buff(1,0)

class ULD_431:###################################
	"""Making Mummies,,1,-,-,Spell,Legendary,-,Quest
	[x]&lt;b&gt;Quest:&lt;/b&gt; Play 5 &lt;b&gt;Reborn&lt;/b&gt;
	minions.
	&lt;b&gt;Reward:&lt;/b&gt; Emperor Wraps."""
	events = Play(CONTROLLER, MINION + {GameTag.REBORN:True}).on(SidequestCounter(SELF, 5, Summon(CONTROLLER, "ULD_431p")))
class ULD_431e:
	atk = SET(2)
	health = SET(2)
	pass
class ULD_431p:
	""" Emperor Wraps
	[x]&lt;b&gt;Hero Power&lt;/b&gt;
	Summon a 2/2 copy
	of a friendly minion."""
	activate = Summon(CONTROLLER, Buff(Copy(RANDOM(FRIENDLY_MINIONS)), "ULD_431e"))

class ULD_217:
	"""Micro Mummy,,2,1,2,Minion,Epic,Mech,Reborn
	[x]&lt;b&gt;Reborn&lt;/b&gt;
	At the end of your turn, give
	another random friendly
	minion +1 Attack."""
	events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_MINIONS), "ULD_217e"))
class ULD_217e:
	atk=1

class ULD_439:
	"""Sandwasp Queen,,2,3,1,Minion,Common,Beast,Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Add two 2/1 Sandwasps to your hand."""
	play = Give(CONTROLLER, "ULD_439t") * 2
class ULD_439t:
	pass

class ULD_500:
	"""Sir Finley of the Sands,,2,2,3,Minion,Legendary,Murloc,Battlecry
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; If your deck has
	no duplicates, &lt;b&gt;Discover&lt;/b&gt; an
	upgraded Hero Power."""
	## HERO_04bp,HERO_04fbp : hero.power:&lt;b&gt;Hero Power&lt;/b&gt;Summon a 1/1 Silver Hand Recruit.
	## HERO_04bp2,HERO_04fbp2:&lt;b&gt;Hero Power&lt;/b&gt;Summon two 1/1 Recruits.
	entourage = ['HERO_01bp2', 'HERO_02bp2', 'HERO_03bp2', 'HERO_04bp2','HERO_05bp2','HERO_06bp2', 'HERO_07bp2', 'HERO_08bp2', 'HERO_09bp2']
	powered_up = -FindDuplicates(FRIENDLY_DECK)
	play = powered_up & Discover(CONTROLLER, RandomEntourage()).then(Summon(CONTROLLER, Discover.CARDS))
class HERO_01bp2:
	""" Tank Up!
	&lt;b&gt;Hero Power&lt;/b&gt;
	Gain 4 Armor."""
	activate = GainArmor(FRIENDLY_HERO, 4)
class HERO_02bp2:
	""" Totemic Slam
	&lt;b&gt;Hero Power&lt;/b&gt;
	Summon a Totem of your choice."""
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	choose = ("AT_132_SHAMANa", "AT_132_SHAMANb", "AT_132_SHAMANc", "AT_132_SHAMANd")
class HERO_03bp2:
	""" Poisoned Daggers
	&lt;b&gt;Hero Power&lt;/b&gt;
	Equip a 2/2 Weapon."""
	activate = Summon(CONTROLLER, "AT_132_ROGUEt")
class HERO_04bp2:
	""" The Silver Hand
	&lt;b&gt;Hero Power&lt;/b&gt;
	Summon two 1/1 Recruits."""
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	activate = Summon(CONTROLLER, "CS2_101t") * 2
class HERO_05bp2:
	"""Ballista Shot
	&lt;b&gt;Hero Power&lt;/b&gt;
	Deal $3 damage to the enemy hero.@&lt;b&gt;Hero Power&lt;/b&gt;
	Deal $3 damage."""
	requirements = {PlayReq.REQ_MINION_OR_ENEMY_HERO: 0, PlayReq.REQ_STEADY_SHOT: 0}
	activate = Hit(ENEMY_HERO, 3)
class HERO_06bp2:
	"""Dire Shapeshift
	&lt;b&gt;Hero Power&lt;/b&gt;
	+2 Attack this turn.
	+2 Armor."""
	activate = Buff(FRIENDLY_HERO, "AT_132_DRUIDe"), GainArmor(FRIENDLY_HERO, 2)
AT_132_DRUIDe = buff(atk=2)
class HERO_07bp2:
	"""Soul Tap
	&lt;b&gt;Hero Power&lt;/b&gt;
	Draw a card."""
	activate = Draw(CONTROLLER)
class HERO_08bp2:
	"""Fireblast Rank 2
	&lt;b&gt;Hero Power&lt;/b&gt;
	Deal $2 damage."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	activate = Hit(TARGET, 2)
class HERO_09bp2:
	"""Heal
	&lt;b&gt;Hero Power&lt;/b&gt;
	Restore #4 Health."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	activate = Heal(TARGET, 4)



class ULD_728:
	"""Subdue,,2,-,-,Spell,Common,-,-
	Set a minion's Attack and Health to 1."""
	requirements = {PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_TO_PLAY:0}
	play = Buff(TARGET,"ULD_728e")
class ULD_728e:
	atk=SET(1)
	health=SET(1)

class ULD_438:
	"""Salhet's Pride,,3,3,1,Minion,Rare,Beast,Deathrattle
	&lt;b&gt;Deathrattle:&lt;/b&gt; Draw two
	1-Health minions from your_deck."""
	deathrattle = ForceDraw(RANDOM(FRIENDLY_DECK + MINION + (COST == 1))) * 2

class ULD_207:
	"""Ancestral Guardian,,4,4,2,Minion,Common,-,Lifesteal
	&lt;b&gt;Lifesteal&lt;/b&gt;
	&lt;b&gt;Reborn&lt;/b&gt;"""

class ULD_143:
	"""Pharaoh's Blessing,,6,-,-,Spell,Rare,-,Divine Shield
	Give a minion +4/+4, &lt;b&gt;Divine Shield&lt;/b&gt;, and &lt;b&gt;Taunt&lt;/b&gt;."""
	requirements = {PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_TO_PLAY:0}
	play = Buff(TARGET,"ULD_143e"), SetTag(TARGET, (GameTag.DIVINE_SHIELD, GameTag.TAUNT))
ULD_143e = buff(4,4)

class ULD_716:
	"""Tip the Scales,,8,-,-,Spell,Epic,-,-
	Summon 7 Murlocs from your deck."""
	play = Summon(CONTROLLER, RANDOM(FRIENDLY_DECK + MURLOC)) * 7