from ..utils import *

####### mage in shadows #######

#### mage-shadows,,10,,,,,,

class DAL_608:#OK
	"""Magic Trick,,1,-,-,Spell,Rare,-,Discover
	<b>Discover</b> a spell that costs (3) or less."""
	play = Discover(CONTROLLER, RandomSpell(cost=[1,2,3]))

class DAL_577:#OK
	"""Ray of Frost,,1,-,-,Spell,Common,-,Freeze
	<b>Twinspell</b>
	<b>Freeze</b> a minion.
	If it's already <b>Frozen</b>,
	deal $2 damage to it."""
	requirements={PlayReq.REQ_ENEMY_TARGET: 0, PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0,}
	play = Find(TARGET + FROZEN) & Hit(TARGET, 2) | Freeze(TARGET), Give(CONTROLLER, "DAL_577ts")
class DAL_577ts:
	requirements={PlayReq.REQ_ENEMY_TARGET: 0, PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0,}
	play = Find(TARGET + FROZEN) & Hit(TARGET, 2) | Freeze(TARGET)

class DAL_575:#OK
	"""Khadgar,,2,2,2,Minion,Legendary,-,-
	Your cards that summon minions summon twice_as_many."""
	events = Play(CONTROLLER, MINION).after(Summon(CONTROLLER, Copy(Summon.CARD)))
	#events = Summon(CONTROLLER, MINION).after(Summon(CONTROLLER, Copy(Summon.CARD)))###### infinte loop

class DAL_182:#OK 
	"""Magic Dart Frog,,2,1,3,Minion,Common,Beast,-
	After you cast a spell, deal 1 damage to a random enemy minion."""
	play = Play(CONTROLLER, SPELL).after(Hit(RANDOM(ENEMY_MINIONS),1))

class DAL_603:#OK
	"""Mana Cyclone,,2,2,2,Minion,Epic,Elemental,Battlecry
	[x]<b>Battlecry:</b> For each spell
	you've cast this turn, add
	a random Mage spell
	to your hand."""
	def play(self):
		for repeat in range(self.controller.times_spells_played_this_turn):
			yield Give(CONTROLLER, RandomSpell(card_class=CardClass.MAGE))

class DAL_163:#OK
	"""Messenger Raven,,3,3,2,Minion,Common,Beast,Battlecry
	<b>Battlecry:</b> <b>Discover</b> a
	Mage minion."""
	play = Discover(CONTROLLER, RandomMinion(card_class=CardClass.MAGE))

class DAL_177:#OK
	"""Conjurer's Calling,,4,-,-,Spell,Rare,-,Twinspell
	<b>Twinspell</b>
	Destroy a minion. Summon 2 minions of the same Cost to replace it."""
	requirements={PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0,}	
	play = Summon(CONTROLLER, RandomMinion(cost=COST(TARGET))) * 2, Destroy(TARGET),Give(CONTROLLER, "DAL_177ts")
class DAL_177ts:
	requirements={PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0,}	
	play = Summon(CONTROLLER, RandomMinion(cost=COST(TARGET))) * 2, Destroy(TARGET)

class DAL_576:#OK
	"""Kirin Tor Tricaster,,4,3,3,Minion,Rare,-,Spell Damage
	<b>Spell Damage +3</b>
	Your spells cost (1) more."""
	play = Buff(FRIENDLY_HAND + SPELL, "DAL_576e")
DAL_576e = buff(cost=1)

class DAL_578:#OK
	"""Power of Creation,,8,-,-,Spell,Epic,-,Discover
	<b>Discover</b> a 6-Cost minion. Summon two copies of it."""
	play = Choice(CONTROLLER, RandomMinion(cost=6)*3).then(Summon(CONTROLLER, Copy(Choice.CARD))*2)

class DAL_609:#OK
	"""Kalecgos,,10,4,12,Minion,Legendary,Dragon,Battlecry
	Your first spell each
	turn costs (0).
	<b>Battlecry:</b> <b>Discover</b>
	a spell."""
	events = OWN_TURN_BEGIN.on(Buff(FRIENDLY_HAND + SPELL, "DAL_609e"))
	play = Discover(CONTROLLER, RandomSpell())
class DAL_609e:
	cost = SET(0)
	events =  OWN_SPELL_PLAY.after(Destroy(SELF))