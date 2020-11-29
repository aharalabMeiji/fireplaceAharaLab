from ..utils import *

####### hunter in dragon #######

class DRG_251:
	"""Clear the Way
	[x]&lt;b&gt;Sidequest:&lt;/b&gt; Summon
	3 &lt;b&gt;Rush&lt;/b&gt; minions.
	&lt;b&gt;Reward:&lt;/b&gt; Summon a
	4/4 Gryphon with &lt;b&gt;Rush&lt;/b&gt;."""
	#<Tag enumID="535" name="QUEST_PROGRESS_TOTAL" type="Int" value="3"/>
	#<Tag enumID="1192" name="SIDEQUEST" type="Int" value="1"/>
	#<ReferencedTag enumID="791" name="RUSH" type="Int" value="1"/>
	pass 

class DRG_253:
	"""Dwarven Sharpshooter
	Your Hero Power can target_minions."""
	update = Refresh(CONTROLLER, {GameTag.STEADY_SHOT_CAN_TARGET: True})
	##  might use RefreshHeroPower
	#play = RefreshHeroPower("HERO_08bp")
	#events = Death(SELF).after(RefreshHeroPower(FRIENDLY_HERO_POWER))

class DRG_255:
	"""Toxic Reinforcements
	[x]&lt;b&gt;Sidequest:&lt;/b&gt; Use your Hero
	Power three times.
	&lt;b&gt;Reward:&lt;/b&gt; Summon three
	1/1 Leper Gnomes."""
	#<Tag enumID="535" name="QUEST_PROGRESS_TOTAL" type="Int" value="3"/>
	#<Tag enumID="1089" name="QUEST_REWARD_DATABASE_ID" type="Int" value="41127"/>
	#<Tag enumID="1192" name="SIDEQUEST" type="Int" value="1"/>
class DRG_255t2:
	"""Leper Gnome
	"""
	pass
class DRG_006:
	"""Corrosive Breath
	[x]Deal $3 damage to a
	minion. If you're holding
	a Dragon, it also hits
	the enemy hero."""
	play = Hit(TARGET,3), HOLDING_DRAGON & Hit(ENEMY_HERO,3)

class DRG_252:
	"""Phase Stalker
	[x]After you use your Hero
	Power, cast a &lt;b&gt;Secret&lt;/b&gt;
	from your deck."""
	play = Activate(CONTROLLER, HERO_POWER).on(Summon(CONTROLLER, RANDOM(FRIENDLY_DECK + SECRET)))


class DRG_010:
	"""Diving Gryphon
	&lt;b&gt;Rush&lt;/b&gt;
	&lt;b&gt;Battlecry:&lt;/b&gt; Draw a &lt;b&gt;Rush&lt;/b&gt; minion_from_your_deck."""


class DRG_254:
	"""Primordial Explorer
	&lt;b&gt;Poisonous&lt;/b&gt;
	&lt;b&gt;Battlecry:&lt;/b&gt; &lt;b&gt;Discover&lt;/b&gt; a Dragon."""


class DRG_007:
	"""Stormhammer
	Doesn't lose Durability while you control a_Dragon."""


class DRG_256:
	"""Dragonbane
	After you use your Hero Power, deal 5 damage to a random enemy."""
	play = Activate(CONTROLLER, HERO_POWER).on(Hit(RANDOM_ENEMY_CHARACTER, 5))

class DRG_095:
	"""Veranus
	&lt;b&gt;Battlecry:&lt;/b&gt; Change the Health of all enemy minions to 1"""
	play = 
