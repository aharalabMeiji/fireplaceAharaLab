from ..utils import *

################# NO CHECKED ##################

class SCH_509:
	"""Brain Freeze	Rare"""
	#&lt;b&gt;Freeze&lt;/b&gt; a minion. &lt;b&gt;Combo:&lt;/b&gt; Also deal $3 damage to it.	
	requirements={PlayReq.REQ_ENEMY_TARGET: 0,
			PlayReq.REQ_TARGET_IF_AVAILABLE: 0,}
	play = Freeze(TARGET), Hit(TARGET, 3)
	pass

class SCH_235:
	"""Devolving Missiles	Epic"""
	#[x]Shoot three missiles at random enemy minions that transform them into ones that cost (1) less.
	requirements = {PlayReq.REQ_MINIMUM_ENEMY_MINIONS: 0}
	play = Evolve(ENEMY_MINIONS, -1) * 3

class SCH_310:
	"""Lab Partner	Common"""
	#&lt;b&gt;Spell Damage +1&lt;/b&gt;
	pass

class SCH_270:
	"""Primordial Studies	Common"""
	#&lt;b&gt;Discover&lt;/b&gt; a &lt;b&gt;Spell Damage&lt;/b&gt; minion. Your next one costs (1) less.
	play = DISCOVER(RandomCollectible(spellpower=True))
	
class SCH_350:
	"""Wand Thief	Common"""
	#&lt;b&gt;Combo:&lt;/b&gt; &lt;b&gt;Discover&lt;/b&gt; a Mage_spell.
	combo = DISCOVER(RandomSpell(card_class=CardClass.MAGE))

class SCH_353:
	"""Cram Session	Rare"""
	#Draw $1 |4(card, cards) &lt;i&gt;(improved by &lt;b&gt;Spell Damage&lt;/b&gt;)&lt;/i&gt;.
	play = Draw(CONTROLLER)

class SCH_537:
	"""Trick Totem	Rare"""
	#At the end of your turn, cast a random spell that costs (3) or less.
	events = OWN_TURN_END.on(CastSpell(RandomSpell(cost=3))) 

class SCH_348:
	"""Combustion	Epic"""
	#[x]Deal $4 damage to a minion. Any excess damages both neighbors. 
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = HitAndExcess(TARGET, 4)

class SCH_241:
	"""Firebrand	Common"""
	#&lt;b&gt;&lt;b&gt;Spellburst&lt;/b&gt;:&lt;/b&gt; Deal 4 damage randomly split among all_enemy minions.
	play = OWN_SPELL_PLAY.on(
		Hit(RANDOM(ENEMY_MINIONS),1) * 4
		)

class SCH_352:
	"""Potion of Illusion	Epic"""
	#Add 1/1 copies of your minions to your hand. They cost (1).
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_FRIENDLY_TARGET: 0}
	play = Buff(TARGET, "SCH_352e"), Give(CONTROLLER, Copy(TARGET))
SCH_352e = buff(1,1,cost = 1)
"""Potion of Illusion"""


class SCH_351:#OK
	"""Jandice Barov	Legendary"""
	#[x]&lt;b&gt;Battlecry:&lt;/b&gt; Summon two random 5-Cost minions. Secretly pick one that dies _when it takes damage.
	import random
	def play(self):
		enchantments=["SCH_351e","SCH_351e2"]
		random.shuffle(enchantments)
		cards = Summon(CONTROLLER, RandomMinion(cost=5)).trigger(self)
		card1=cards[0][0]
		Buff(card1, enchantments[0]).trigger(self)
		cards = Summon(CONTROLLER, RandomMinion(cost=5)).trigger(self)
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

class SCH_400:
	"""Mozaki, Master Duelist	Legendary"""
	#After you cast a spell, gain &lt;b&gt;Spell Damage +1&lt;/b&gt;.
	play = OWN_SPELL_PLAY.after(Buff(SELF,"SCH_400e2")
		)
SCH_400e2 = buff(spellpower=1)
"""Magic Master"""

class SCH_273:
	"""Ras Frostwhisper	Legendary"""
	#At the end of your turn, deal $1 damage to all enemies &lt;i&gt;(improved by &lt;b&gt;Spell Damage&lt;/b&gt;)&lt;/i&gt;.
	play = OWN_TURN_END.on(Hit(ENEMY_MINIONS, 1))

class SCH_243:
	"""Wyrm Weaver	Rare"""
	#&lt;b&gt;Spellburst:&lt;/b&gt; Summon two 1/3 Mana Wyrms.
	play = OWN_SPELL_PLAY.on(Summon(CONTROLLER,"NEW1_012"))
