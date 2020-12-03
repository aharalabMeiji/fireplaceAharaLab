from ..utils import *

####### mage in dragon #######


class DRG_106:
	"""Arcane Breath
	Deal $2 damage to a minion. If you're holding a Dragon, &lt;b&gt;Discover&lt;/b&gt; a spell."""
	requirements = {PlayReq.REQ_MINION_TARGET: 0}
	play = Hit(TARGET, 2), HOLDING_DRAGON & Discover(CONTROLLER, SPELL)
	pass 

class DRG_324:
	"""Elemental Allies
	[x]&lt;b&gt;Sidequest:&lt;/b&gt; Play an
	Elemental 2 turns in a row.
	&lt;b&gt;Reward:&lt;/b&gt; Draw 3 spells
	from your deck."""
	#<Tag enumID="535" name="QUEST_PROGRESS_TOTAL" type="Int" value="2"/>
	#<Tag enumID="1089" name="QUEST_REWARD_DATABASE_ID" type="Int" value="395"/>
	#<Tag enumID="1192" name="SIDEQUEST" type="Int" value="1"/>
	event = Play(CONTROLLER, EnumSelector(Race.MECHANICAL)).on(
		SidequestCounter(SELF,2,Draw(CONTROLLER,FRIENDLY_DECK+SPELL)*2) ## no implementation of 'in a row'.
		)
	

class DRG_323:
	"""Learn Draconic
	[x]&lt;b&gt;Sidequest:&lt;/b&gt; Spend
	8 Mana on spells.
	&lt;b&gt;Reward:&lt;/b&gt; Summon a
	6/6 Dragon."""
	#<Tag enumID="535" name="QUEST_PROGRESS_TOTAL" type="Int" value="8"/>
	#<Tag enumID="1089" name="QUEST_REWARD_DATABASE_ID" type="Int" value="55282"/>
	#<Tag enumID="1192" name="SIDEQUEST" type="Int" value="1"/>
	event = Play(CONTROLLER,SPELL).on(
		SidequestManaCounter(SELF, Play.CARD,8,Summon(CONTROLLER,"DRG_323t"))
		)
	
class DRG_323t:# 55282
	"""Draconic Emissary
	vanilla """

class DRG_107:
	"""Violet Spellwing
	&lt;b&gt;Deathrattle:&lt;/b&gt; Add an 'Arcane Missiles' spell to_your hand."""
	deathrattle = Give(CONTROLLER, "EX1_277")

class DRG_104:############################################################
	"""Chenvaala
	After you cast three spells in a turn, summon a 5/5_Elemental."""

class DRG_104t2:
	pass

class DRG_102:
	"""Azure Explorer
	&lt;b&gt;Spell Damage +2&lt;/b&gt;
	&lt;b&gt;Battlecry:&lt;/b&gt; &lt;b&gt;Discover&lt;/b&gt; a Dragon."""
	play = Discover(CONTROLLER, DRAGON)

class DRG_270:
	"""Malygos, Aspect of Magic
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; If you're holding
	a Dragon, &lt;b&gt;Discover&lt;/b&gt; an
	 upgraded Mage spell."""
	play = HOLDING_DRAGON | Discover(CONTROLLER, RandomSpell(card_class=CardClass.MAGE, upgrade_counter=1))#####   need process of 'Upgrade()'?

class DRG_321:
	"""Rolling Fireball
	Deal $8 damage to a minion. Any excess damage continues to
	the left or right."""
	requirements = { PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 8)#######################################


class DRG_322:
	"""Dragoncaster
	&lt;b&gt;Battlecry:&lt;/b&gt; If you're holding a Dragon, your next spell this turn costs (0)."""


class DRG_109:
	"""Mana Giant
	[x]Costs (1) less for each
	card you've played this
	game that didn't start
	in your deck."""