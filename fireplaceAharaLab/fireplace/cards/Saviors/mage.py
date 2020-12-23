from ..utils import *

##### mage@uldum,,10,,,,,,

class ULD_433:
	"""Raid the Sky Temple,,1,-,-,Spell,Legendary,-,Quest
	&lt;b&gt;Quest:&lt;/b&gt; Cast 10 spells.
	&lt;b&gt;Reward: &lt;/b&gt;Ascendant Scroll."""
	events = OWN_SPELL_PLAY.on(SidequestCounter(SELF, 10, Summon(CONTROLLER, "ULD_433p") ))
class ULD_433e:
	cost=-2
	pass
class ULD_433p:
	""" Ascendant Scroll
	&lt;b&gt;Hero Power&lt;/b&gt;
	Add a random Mage
	spell to your hand.
	It costs (2) less."""
	play = Give(CONTROLLER, Buff(RandomSpell(),"ULD_433e"))
class ULD_726:
	"""Ancient Mysteries,,2,-,-,Spell,Common,-,Secret
	Draw a &lt;b&gt;Secret&lt;/b&gt; from your deck. It costs (0)."""
	play = Give(CONTROLLER, Buff(RANDOM(FRIENDLY_DECK + SECRET), "ULD_726e"))
class ULD_726e:
	cost = SET(0)
class ULD_240:
	"""Arcane Flakmage,,2,3,2,Minion,Rare,-,Secret
	After you play a &lt;b&gt;Secret&lt;/b&gt;, deal 2 damage to all enemy minions."""
	events = Play(CONTROLLER,SECRET).after(Hit(ENEMY_MINIONS, 2))
class ULD_329:
	"""Dune Sculptor,,3,3,3,Minion,Rare,-,-
	[x]After you cast a spell,
	add a random Mage
	minion to your hand."""
	events = Play(CONTROLLER,SPELL).after(Give(CONTROLLER, RandomMinion(card_class=CardClass.MAGE)))
class ULD_239:
	"""Flame Ward,,3,-,-,Spell,Common,-,Secret
	&lt;b&gt;Secret:&lt;/b&gt; After a minion attacks your hero, deal $3 damage to all enemy minions."""
	secret = Attack(ENEMY_MINIONS, FRIENDLY_HERO).after(Hit(ENEMY_MINIONS, 3))
class ULD_293:
	"""Cloud Prince,,5,4,4,Minion,Common,Elemental,Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; If you control a &lt;b&gt;Secret&lt;/b&gt;, deal 6 damage."""
	play = Find(FRIENDLY_SECRETS) & Hit(RANDOM(ENEMY_CHARACTERS), 6)
class ULD_435:
	"""Naga Sand Witch,,5,5,5,Minion,Rare,-,Battlecry
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; Change the Cost
	of spells in your hand to (5)."""
	play = Buff(FRIENDLY_HAND + SPELL, "ULD_435e")
class ULD_435e:
	""" Sandwitched """
	cost = SET(5)
class ULD_238:
	"""Reno the Relicologist,,6,4,6,Minion,Legendary,-,Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; If your deck has no duplicates, deal 10 damage randomly split among all enemy minions."""
	powered_up = -FindDuplicates(FRIENDLY_DECK)
	play = powered_up & Hit(RANDOM(ENEMY_MINIONS),1)*10
class ULD_236:
	"""Tortollan Pilgrim,,8,5,5,Minion,Epic,-,Battlecry
	[x]&lt;b&gt;Battlecry&lt;/b&gt;: &lt;b&gt;Discover&lt;/b&gt; a spell
	in your deck and cast it
	with random targets."""
	play = Discover(CONTROLLER, FRIENDLY_DECK + SPELL).after(CastSpell(Discover.CARDS))
class ULD_216:
	"""Puzzle Box of Yogg-Saron,,10,-,-,Spell,Epic,-,-
	Cast 10 random spells &lt;i&gt;(targets chosen randomly).&lt;/i&gt;"""
	play = CastSpell(RandomSpell()) * 10