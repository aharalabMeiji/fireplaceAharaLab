from ..utils import *

class SCH_509:#OK
	"""Brain Freeze	Rare"""
	#<b>Freeze</b> a minion. <b>Combo:</b> Also deal $3 damage to it.	
	requirements={PlayReq.REQ_ENEMY_TARGET: 0,
			PlayReq.REQ_TARGET_IF_AVAILABLE: 0,}
	#play = SetTag(TARGET,(GameTag.FROZEN, ))
	play = Freeze(TARGET)
	combo = Hit(TARGET, 3),Freeze(TARGET)
	pass

class SCH_235:#OK
	"""Devolving Missiles	Epic"""
	#[x]Shoot three missiles at random enemy minions that transform them into ones that cost (1) less.
	requirements = {PlayReq.REQ_MINIMUM_ENEMY_MINIONS: 0}
	play = Evolve(RANDOM_ENEMY_MINION, -1) * 3

class SCH_310:#OK
	"""Lab Partner	Common"""
	#<b>Spell Damage +1</b>
	pass

class SCH_270:#OK
	"""Primordial Studies	Common"""
	#<b>Discover</b> a <b>Spell Damage</b> minion. Your next one costs (1) less.
	play = Choice(CONTROLLER, RandomMinion(spellpower=1)*3).then(Give(CONTROLLER, Choice.CARD).then(Buff(CONTROLLER, "SCH_270e")))
class SCH_270e:
	update = Refresh(FRIENDLY_HAND+SPELLPOWER, {GameTag.COST: -1})#OK
	events = Play(CONTROLLER, SPELLPOWER).on(Destroy(SELF))#OK
SCH_270e2 = buff(cost=-1)	
class SCH_350:#OK
	"""Wand Thief	Common"""
	#<b>Combo:</b> <b>Discover</b> a Mage_spell.
	combo = DISCOVER(RandomSpell(card_class=CardClass.MAGE))

class SCH_353:#OK
	"""Cram Session	Rare"""
	#Draw $1 |4(card, cards) <i>(improved by <b>Spell Damage</b>)</i>.
	play = Draw(CONTROLLER,1)

class SCH_537:#OK
	"""Trick Totem	Rare"""
	#At the end of your turn, cast a random spell that costs (3) or less.
	events = OWN_TURN_END.on(Summon(CONTROLLER,RandomSpell(cost=[1,2,3]))) 

class SCH_348:#OK
	"""Combustion	Epic"""
	#[x]Deal $4 damage to a minion. Any excess damages both neighbors. 
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = HitAndExcess(TARGET, 4)

class SCH_241:#OK
	"""Firebrand	Common"""
	#<b><b>Spellburst</b>:</b> Deal 4 damage randomly split among all_enemy minions.
	play = OWN_SPELL_PLAY.on(Hit(RANDOM(ENEMY_MINIONS),1) * 4 )

class SCH_352:#OK
	"""Potion of Illusion	Epic"""
	#Add 1/1 copies of your minions to your hand. They cost (1).
	play = Give(CONTROLLER, Copy(FRIENDLY_MINIONS)).then(Buff(Give.CARD, "SCH_352e"))
class SCH_352e:
   atk=SET(1)
   max_health=SET(1)
   cost=SET(1)
"""Potion of Illusion"""

class SCH_351:#OK
	"""Jandice Barov	Legendary"""
	#[x]<b>Battlecry:</b> Summon two random 5-Cost minions. Secretly pick one that dies _when it takes damage.
	import random
	def play(self):
		enchantments=["SCH_351e","SCH_351e2"]
		random.shuffle(enchantments)
		cards = Summon(CONTROLLER, RandomMinion(cost=5)).trigger(self)
		if cards[0] != []:
			card1=cards[0][0]
			Buff(card1, enchantments[0]).trigger(self)
			cards = Summon(CONTROLLER, RandomMinion(cost=5)).trigger(self)
			if cards[0] != []:
				card2=cards[0][0]
				Buff(card2, enchantments[1]).trigger(self)
	pass
class SCH_351a:
	"""This is an Illusion."""
	play = Buff(OWNER, "SCH_351e")
class SCH_351b:
	"""This is not an Illusion."""
	play = Buff(OWNER, "SCH_351e2")
class SCH_351e:
	"""Illusion"""
	pass
class SCH_351e2:
	"""Illusion"""
	##This might be an illusion that dies when it takes damage."""
	events = Damage(OWNER).on(Destroy(OWNER))## Damage(OWNER)?

class SCH_400:#OK
	"""Mozaki, Master Duelist	Legendary"""
	#After you cast a spell, gain <b>Spell Damage +1</b>.
	play = OWN_SPELL_PLAY.after(Buff(SELF,"SCH_400e2")
		)
SCH_400e2 = buff(spellpower=1)
"""Magic Master"""

class SCH_273:#OK
	"""Ras Frostwhisper	Legendary"""
	#At the end of your turn, deal $1 damage to all enemies <i>(improved by <b>Spell Damage</b>)</i>.
	events = OWN_TURN_END.on(Hit(ENEMY_MINIONS, 1))

class SCH_243:#OK
	"""Wyrm Weaver	Rare"""
	#<b>Spellburst:</b> Summon two 1/3 Mana Wyrms.
	play = OWN_SPELL_PLAY.on(Summon(CONTROLLER,"NEW1_012")* 2) 
