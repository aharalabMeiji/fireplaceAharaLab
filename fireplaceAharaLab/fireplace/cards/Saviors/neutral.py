from ..utils import *

####### neutral in savior,  45 cards#######

class ULD_191:
	"""Beaming Sidekick		1	1	2	Minion	Common	-	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Give a friendly minion +2 Health."""
	play = Buff(RANDOM(FRIENDLY_MINIONS), "ULD_191e")
ULD_191e = buff(0,2)

class ULD_282:
	"""Jar Dealer		1	1	1	Minion	Common	-	Deathrattle
	[x]&lt;b&gt;Deathrattle:&lt;/b&gt; Add a random
	1-Cost minion to your hand."""
	deathrattle = Give(CONTROLLER,RandomMinion(cost=1))

class ULD_705:
	"""Mogu Cultist		1	1	1	Minion	Epic	-	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; If your board is full of Mogu Cultists, sacrifice them all and summon Highkeeper Ra."""
	powered_up = Count(FRIENDLY_MINION + ID('ULD_705'))==8
	play powered_up & Destroy(FRIENDLY_MINION + ID('ULD_705')), Summon(CONTROLLER, "ULD_705t")
class ULD_705t:
	""" Highkeeper Ra
	At the end of your turn, deal 20 damage to all_enemies."""
	play = OWN_TURN_END.on(Damage(ENEMY_CHARACTERS,20))

class ULD_723:
	"""Murmy		1	1	1	Minion	Common	Murloc	Reborn
	&lt;b&gt;Reborn&lt;/b&gt;"""

class ULD_712:
	"""Bug Collector		2	2	1	Minion	Common	-	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Summon a 1/1 Locust with &lt;b&gt;Rush&lt;/b&gt;."""
	play = Summon(CONTROLLER, "ULD_430t")

class ULD_309:
	"""Dwarven Archaeologist		2	2	3	Minion	Epic	-	Discover
	After you &lt;b&gt;Discover&lt;/b&gt; a card, reduce its cost by (1)."""
	play = Discover(RandomCollectible()).after(Buff(Discover.CARDS, "ULD_309e")
class ULD_309e:
	cost = SET(1)

class ULD_289:
	"""Fishflinger		2	3	2	Minion	Common	Murloc	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Add a
	random Murloc to each player's_hand."""
	play = Give(CONTROLLER, RandomMurloc()), Give(OPPONENT, RandomMurloc())

class ULD_271:
	"""Injured Tol'vir		2	2	6	Minion	Common	-	Battlecry
	&lt;b&gt;Taunt&lt;/b&gt;
	&lt;b&gt;Battlecry:&lt;/b&gt; Deal 3 damage to this minion."""
	play = Hit(SELF, 3)

class ULD_184:
	"""Kobold Sandtrooper		2	2	1	Minion	Common	-	Deathrattle
	&lt;b&gt;Deathrattle:&lt;/b&gt; Deal 3 damage to the enemy_hero."""
	deathrattle = Hit(ENEMY_HERO, 3)

class ULD_196:
	"""Neferset Ritualist		2	2	3	Minion	Rare	-	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Restore adjacent minions to full_Health."""
	play = FullHeal(SELF_ADJACENT)

##### 10 #####


class ULD_157:
	"""Questing Explorer		2	2	3	Minion	Rare	-	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; If you control a &lt;b&gt;Quest&lt;/b&gt;, draw a card."""

class ULD_197:
	"""Quicksand Elemental		2	3	2	Minion	Rare	Elemental	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Give all enemy minions -2 Attack this_turn."""
class ULD_174:
	"""Serpent Egg		2	0	3	Minion	Common	-	Deathrattle
	&lt;b&gt;Deathrattle:&lt;/b&gt; Summon a 3/4 Sea Serpent."""
class ULD_174t:
	"""Sea Serpent """
	pass
class ULD_182:
	"""Spitting Camel		2	2	4	Minion	Common	Beast	-
	[x]At the end of your turn,
	__deal 1 damage to another__
	random friendly minion."""
class ULD_185:
	"""Temple Berserker		2	1	2	Minion	Common	-	Reborn
	&lt;b&gt;Reborn&lt;/b&gt;
	Has +2 Attack while damaged."""
class ULD_450:
	"""Vilefiend		2	2	2	Minion	Common	Demon	Lifesteal
	&lt;b&gt;Lifesteal&lt;/b&gt;"""
class ULD_:
	"""Zephrys the Great		2	3	2	Minion	Legendary	Elemental	Battlecry
	"""
class ULD_:
	"""Candletaker		3	3	2	Minion	Common	-	Reborn
	"""
class ULD_:
	"""Desert Hare		3	1	1	Minion	Common	Beast	Battlecry
	"""
class ULD_:
	"""Generous Mummy		3	5	4	Minion	Rare	-	Reborn
	"""

#####20#####

class ULD_:
	"""Golden Scarab		3	2	2	Minion	Common	Beast	Battlecry
	"""
class ULD_:
	"""History Buff		3	3	4	Minion	Epic	-	-
	"""
class ULD_:
	"""Infested Goblin		3	2	3	Minion	Rare	-	Deathrattle
	"""
class ULD_:
	"""Mischief Maker		3	3	3	Minion	Epic	-	Battlecry
	"""
class ULD_:
	"""Vulpera Scoundrel		3	2	3	Minion	Epic	-	Battlecry
	"""
class ULD_:
	"""Body Wrapper		4	4	4	Minion	Epic	-	Battlecry
	"""
class ULD_:
	"""Bone Wraith		4	2	5	Minion	Common	-	Reborn
	"""
class ULD_:
	"""Conjured Mirage		4	3	10	Minion	Rare	-	Taunt
	"""
class ULD_:
	"""Sunstruck Henchman		4	6	5	Minion	Rare	-	-
	"""
class ULD_:
	"""Desert Obelisk		5	0	5	Minion	Epic	-	-
	"""

##### 30 #####


class ULD_:
	"""Faceless Lurker		5	3	3	Minion	Common	-	Battlecry
	"""
class ULD_:
	"""Mortuary Machine		5	8	8	Minion	Epic	Mech	Reborn
	"""

class ULD_:
	"""Phalanx Commander		5	4	5	Minion	Common	-	Taunt
	"""
class ULD_:
	"""Wasteland Assassin		5	4	2	Minion	Common	-	Reborn
	"""
class ULD_:
	"""Blatant Decoy		6	5	5	Minion	Epic	-	Deathrattle
	"""
class ULD_:
	"""Khartut Defender		6	3	4	Minion	Rare	-	Deathrattle
	"""
class ULD_:
	"""Siamat		7	6	6	Minion	Legendary	Elemental	Battlecry
	"""
class ULD_:
	"""Wasteland Scorpid		7	3	9	Minion	Common	Beast	Poisonous
	"""
class ULD_:
	"""Wrapped Golem		7	7	5	Minion	Rare	-	Reborn
	"""
class ULD_:
	"""Octosari		8	8	8	Minion	Legendary	Beast	Deathrattle
	"""


##### 40 #####

class ULD_:
	"""Pit Crocolisk		8	5	6	Minion	Common	Beast	Battlecry
	"""
class ULD_:
	"""Anubisath Warbringer		9	9	6	Minion	Common	-	Deathrattle
	"""
class ULD_:
	"""Colossus of the Moon		10	10	10	Minion	Legendary	-	Divine Shield
	"""
class ULD_:
	"""King Phaoris		10	5	5	Minion	Legendary	-	Battlecry
	"""
class ULD_:
	"""Living Monument		10	10	10	Minion	Common	-	Taunt
	"""
