from ..utils import *

####### mage in dragon #######


class DRG_106:#OK
	"""Arcane Breath
	Deal $2 damage to a minion. If you're holding a Dragon, <b>Discover</b> a spell."""
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 2), HOLDING_DRAGON & Discover(CONTROLLER, RandomSpell())
	pass 

class DRG_324:#OK
	"""Elemental Allies
	[x]<b>Sidequest:</b> Play an
	Elemental 2 turns in a row.
	<b>Reward:</b> Draw 3 spells
	from your deck."""
	#<Tag enumID="535" name="QUEST_PROGRESS_TOTAL" type="Int" value="2"/>
	#<Tag enumID="1089" name="QUEST_REWARD_DATABASE_ID" type="Int" value="395"/>
	#<Tag enumID="1192" name="SIDEQUEST" type="Int" value="1"/>
	events = Play(CONTROLLER, EnumSelector(Race.ELEMENTAL)).on(SidequestCounter(SELF,2,[ForceDraw(RANDOM(FRIENDLY_DECK+SPELL))*3, Destroy(SELF)]))
	

class DRG_323:#OK
	"""Learn Draconic
	[x]<b>Sidequest:</b> Spend
	8 Mana on spells.
	<b>Reward:</b> Summon a
	6/6 Dragon."""
	#<Tag enumID="535" name="QUEST_PROGRESS_TOTAL" type="Int" value="8"/>
	#<Tag enumID="1089" name="QUEST_REWARD_DATABASE_ID" type="Int" value="55282"/>
	#<Tag enumID="1192" name="SIDEQUEST" type="Int" value="1"/>
	events = Play(CONTROLLER,SPELL).on(
		SidequestManaCounter(SELF, Play.CARD,8, [Summon(CONTROLLER,"DRG_323t"), Destroy(SELF)])
		)
class DRG_323t:# 55282
	"""Draconic Emissary
	vanilla """

class DRG_107:#OK
	"""Violet Spellwing
	<b>Deathrattle:</b> Add an 'Arcane Missiles' spell to_your hand."""
	deathrattle = Give(CONTROLLER, "EX1_277")

class DRG_104:#OK
	"""Chenvaala
	After you cast three spells in a turn, summon a 5/5_Elemental."""
	events = [OWN_SPELL_PLAY.on(SidequestCounter(SELF,3,[Summon(CONTROLLER,"DRG_104t2")])),
	OWN_TURN_END.on(SidequestCounterClear(SELF))]
class DRG_104t2:
	"""Snow Elemental
	vanilla """
	pass

class DRG_102:#OK
	"""Azure Explorer
	<b>Spell Damage +2</b>
	<b>Battlecry:</b> <b>Discover</b> a Dragon."""
	play = DISCOVER(RandomDragon())

class DRG_270:#OK
	"""Malygos, Aspect of Magic
	[x]<b>Battlecry:</b> If you're holding
	a Dragon, <b>Discover</b> an
	upgraded Mage spell."""
	entourage = ["DRG_270t1","DRG_270t2","DRG_270t4","DRG_270t5","DRG_270t6","DRG_270t7","DRG_270t8","DRG_270t9","DRG_270t11"]
	play = HOLDING_DRAGON & Discover(CONTROLLER, RandomEntourage())
class DRG_270t1:#OK
	""" Malygos's Intellect
	Draw 4 cards."""
	play = Draw(CONTROLLER) * 4
	pass
class DRG_270t2:#OK
	""" Malygos's Tome
	Add 3 random Mage spells to your hand."""
	play = Give(CONTROLLER, RandomSpell()) * 3
	pass
class DRG_270t4:#OK
	""" Malygos's Explosion
	Deal $2 damage to all enemy minions."""
	play = Hit(ENEMY_MINIONS,2)
	pass
class DRG_270t5:#OK
	""" Malygos's Nova
	<b>Freeze</b> all enemy minions."""
	play = Freeze(ENEMY_MINIONS)
	pass
class DRG_270t6:#OK
	""" Malygos's Polymorph
	Transform a minion into a 1/1 Sheep."""
	play = Morph(RANDOM(ENEMY_MINIONS),"DRG_270t6t")
	pass
class DRG_270t6t:
	"""Malygos's Sheep 
	vanilla"""
class DRG_270t7:#OK
	""" Malygos's Flamestrike
	Deal $8 damage to all enemy minions."""
	play = Hit(ENEMY_MINIONS, 8)
	pass
class DRG_270t8:#OK
	""" Malygos's Frostbolt
	Deal $3 damage to a_character and <b>Freeze</b> it."""
	requirements = { PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 3), Freeze(TARGET)
	pass
class DRG_270t9:#OK
	""" Malygos's Fireball
	Deal $8 damage."""
	requirements = { PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 8)
	pass
class DRG_270t11:#OK
	""" Malygos's Missiles
	Deal $6 damage randomly split among all enemies."""
	play = Hit(RANDOM(ENEMY_CHARACTERS), 1) * 6
	pass

class DRG_321:#OK
	"""Rolling Fireball
	Deal $8 damage to a minion. Any excess damage continues to
	the left or right."""
	requirements = { PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = HitAndExcess(TARGET, 8)


class DRG_322:#OK
	"""Dragoncaster
	<b>Battlecry:</b> If you're holding a Dragon, your next spell this turn costs (0)."""
	play = HOLDING_DRAGON & Buff(CONTROLLER, "DRG_322e")
class DRG_322e:
	""" Draconic Magic
	"""
	update = Refresh(FRIENDLY_HAND + SPELL, {GameTag.COST: SET(0)})
	events = Play(CONTROLLER, SPELL).on(Destroy(SELF))

class DRG_109:#OK
	"""Mana Giant
	[x]Costs (1) less for each
	card you've played this
	game that didn't start
	in your deck."""
	cost_mod = - Attr(CONTROLLER, "times_card_to_play_out_of_deck")