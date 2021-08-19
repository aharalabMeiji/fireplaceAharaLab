from ..utils import *

## mage@uldum,,10,,,,,,

class ULD_433:#OK
	"""Raid the Sky Temple,,1,-,-,Spell,Legendary,-,Quest
	<b>Quest:</b> Cast 10 spells.
	<b>Reward: </b>Ascendant Scroll."""
	tags={GameTag.SIDEQUEST:True}
	events = OWN_SPELL_PLAY.on(SidequestCounter(SELF, 2, [Summon(CONTROLLER, "ULD_433p"), Destroy(SELF)] ))
class ULD_433p:
	""" Ascendant Scroll
	<b>Hero Power</b>
	Add a random Mage
	spell to your hand.
	It costs (2) less."""
	activate = Give(CONTROLLER, RandomSpell()).then(Buff(Give.CARD,"ULD_433e"))
ULD_433e = buff(cost=-2)

class ULD_726:#OK
	"""Ancient Mysteries,,2,-,-,Spell,Common,-,Secret
	Draw a <b>Secret</b> from your deck. It costs (0)."""
	play = Give(CONTROLLER, RANDOM(FRIENDLY_DECK + SECRET)).then(Buff(Give.CARD, "ULD_726e"))
class ULD_726e:
	cost = SET(0)

class ULD_240:#OK
	"""Arcane Flakmage,,2,3,2,Minion,Rare,-,Secret
	After you play a <b>Secret</b>, deal 2 damage to all enemy minions."""
	events = Play(CONTROLLER,SECRET).after(Hit(ENEMY_MINIONS, 2))

class ULD_329:#OK
	"""Dune Sculptor,,3,3,3,Minion,Rare,-,-
	[x]After you cast a spell,
	add a random Mage
	minion to your hand."""
	events = Play(CONTROLLER,SPELL).after(Give(CONTROLLER, RandomMinion(card_class=CardClass.MAGE)))

class ULD_239:#OK
	"""Flame Ward,,3,-,-,Spell,Common,-,Secret
	<b>Secret:</b> After a minion attacks your hero, deal $3 damage to all enemy minions."""
	secret = Attack(ENEMY_MINIONS, FRIENDLY_HERO).after(Hit(ENEMY_MINIONS, 3))

class ULD_293:#OK
	"""Cloud Prince,,5,4,4,Minion,Common,Elemental,Battlecry
	<b>Battlecry:</b> If you control a <b>Secret</b>, deal 6 damage."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0}
	play = Find(FRIENDLY_SECRETS) & Hit(TARGET, 6)

class ULD_435:#OK
	"""Naga Sand Witch,,5,5,5,Minion,Rare,-,Battlecry
	[x]<b>Battlecry:</b> Change the Cost
	of spells in your hand to (5)."""
	play = Buff(FRIENDLY_HAND + SPELL, "ULD_435e")
class ULD_435e:
	""" Sandwitched """
	cost = SET(5)

class ULD_238:#OK
	"""Reno the Relicologist,,6,4,6,Minion,Legendary,-,Battlecry
	<b>Battlecry:</b> If your deck has no duplicates, deal 10 damage randomly split among all enemy minions."""
	powered_up = -FindDuplicates(FRIENDLY_DECK)
	play = powered_up & Hit(RANDOM(ENEMY_MINIONS),1)*10

class ULD_236:#OK 
	"""Tortollan Pilgrim,,8,5,5,Minion,Epic,-,Battlecry
	[x]<b>Battlecry</b>: <b>Discover</b> a spell
	in your deck and cast it
	with random targets."""
	play = Choice(CONTROLLER, RANDOM(FRIENDLY_DECK+SPELL)*3).then(Summon(CONTROLLER, Copy(Choice.CARD)))

class ULD_216:#OK
	"""Puzzle Box of Yogg-Saron,,10,-,-,Spell,Epic,-,-
	Cast 10 random spells <i>(targets chosen randomly).</i>"""
	play = CastSpell(RandomSpell()) * 10