from ..utils import *

####### hunter in dragon #######

class DRG_251:#OK
	"""Clear the Way
	[x]<b>Sidequest:</b> Summon
	3 <b>Rush</b> minions.
	<b>Reward:</b> Summon a
	4/4 Gryphon with <b>Rush</b>."""
	#<Tag enumID="535" name="QUEST_PROGRESS_TOTAL" type="Int" value="3"/>
	#<Tag enumID="1192" name="SIDEQUEST" type="Int" value="1"/>
	#<ReferencedTag enumID="791" name="RUSH" type="Int" value="1"/>
	events = (
		Summon(CONTROLLER, MINION + EnumSelector(GameTag.RUSH)).on(#
			SidequestCounter(SELF,3,[Summon(CONTROLLER,"DRG_251t"), Destroy(SELF)])#
		)
	)
	pass 
class DRG_251t:
	""" Gryphon
	Rush """

class DRG_253:#OK!
	"""Dwarven Sharpshooter
	Your Hero Power can target_minions."""
	## deal 2 damage to enemy hero HERO_05bp, HERO_05dbp
	## deal 3 damage to enemy hero HERO_05bp2
	play = ChangeHeroPower(CONTROLLER, "HERO_05dbp")
	# see also fireplace.actions.Death.do

class HERO_05dbp:
	"""Steady Shot (Rexxar)"""
	requirements = { 
		PlayReq.REQ_ENEMY_TARGET: 0, 
		PlayReq.REQ_HERO_OR_MINION_TARGET: 0, #new comer
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	activate = Hit(TARGET, 2)

class DRG_255:#OK
	"""Toxic Reinforcements
	[x]<b>Sidequest:</b> Use your Hero
	Power three times.
	<b>Reward:</b> Summon three
	1/1 Leper Gnomes."""
	#<Tag enumID="535" name="QUEST_PROGRESS_TOTAL" type="Int" value="3"/>
	#<Tag enumID="1089" name="QUEST_REWARD_DATABASE_ID" type="Int" value="41127"/>
	#<Tag enumID="1192" name="SIDEQUEST" type="Int" value="1"/>
	events = Activate(CONTROLLER).on( SidequestCounter(SELF,2,[Summon(CONTROLLER,"DRG_255t2")*3, Destroy(SELF)])) 
class DRG_255t2:
	"""Leper Gnome
	"""
	pass
class DRG_006:#OK
	"""Corrosive Breath
	[x]Deal $3 damage to a
	minion. If you're holding
	a Dragon, it also hits
	the enemy hero."""
	requirements = {PlayReq.REQ_ENEMY_TARGET: 0, PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET,3), HOLDING_DRAGON & Hit(ENEMY_HERO,3)

class DRG_252:#OK
	"""Phase Stalker
	[x]After you use your Hero
	Power, cast a <b>Secret</b>
	from your deck."""
	events = Activate(CONTROLLER, HERO_POWER).on(Summon(CONTROLLER, RANDOM(FRIENDLY_DECK + SECRET)))

class DRG_010:#OK
	"""Diving Gryphon
	<b>Rush</b>
	<b>Battlecry:</b> Draw a <b>Rush</b> minion_from_your_deck."""
	play = Draw(CONTROLLER,RANDOM(FRIENDLY_DECK + EnumSelector(GameTag.RUSH)))

class DRG_254:#OK
	"""Primordial Explorer
	<b>Poisonous</b>
	<b>Battlecry:</b> <b>Discover</b> a Dragon."""
	play = DISCOVER(RandomDragon())

class DRG_007:#OK
	"""Stormhammer
	Doesn't lose Durability while you control a_Dragon."""
	play = HOLDING_DRAGON & Attack(FRIENDLY_HERO, ENEMY).on(Buff(FRIENDLY_WEAPON,"DRG_007e"))
DRG_007e = buff(health=+1)# fixing 'durability=health'

class DRG_256:#OK
	"""Dragonbane
	After you use your Hero Power, deal 5 damage to a random enemy."""
	play = Activate(CONTROLLER, HERO_POWER).on(Hit(RANDOM_ENEMY_CHARACTER, 5))

class DRG_095:#OK
	"""Veranus
	<b>Battlecry:</b> Change the Health of all enemy minions to 1"""
	play = SetCurrentHealth(ENEMY_MINIONS,1) 
