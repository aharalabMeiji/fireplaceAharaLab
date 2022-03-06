from ..utils import *


class SW_320:#OK
	""" Rats of Extraordinary Size
	[x]Summon seven 1/1 Rats. Any that can't fit on the battlefield go to your hand with +4/+4. """
	play = (
		((Count(FRIENDLY_MINIONS) < 8) & Summon(CONTROLLER,'SW_455t') | Give(CONTROLLER,'SW_455t').then(Buff(Give.CARD,'SW_320e'))),
		((Count(FRIENDLY_MINIONS) < 8) & Summon(CONTROLLER,'SW_455t') | Give(CONTROLLER,'SW_455t').then(Buff(Give.CARD,'SW_320e'))),
		((Count(FRIENDLY_MINIONS) < 8) & Summon(CONTROLLER,'SW_455t') | Give(CONTROLLER,'SW_455t').then(Buff(Give.CARD,'SW_320e'))),
		((Count(FRIENDLY_MINIONS) < 8) & Summon(CONTROLLER,'SW_455t') | Give(CONTROLLER,'SW_455t').then(Buff(Give.CARD,'SW_320e'))),
		((Count(FRIENDLY_MINIONS) < 8) & Summon(CONTROLLER,'SW_455t') | Give(CONTROLLER,'SW_455t').then(Buff(Give.CARD,'SW_320e'))),
		((Count(FRIENDLY_MINIONS) < 8) & Summon(CONTROLLER,'SW_455t') | Give(CONTROLLER,'SW_455t').then(Buff(Give.CARD,'SW_320e'))),
		((Count(FRIENDLY_MINIONS) < 8) & Summon(CONTROLLER,'SW_455t') | Give(CONTROLLER,'SW_455t').then(Buff(Give.CARD,'SW_320e')))
		)
	pass
SW_320e=buff(atk=4,health=4)


class SW_321:#OK
	""" Aimed Shot
	Deal $3 damage. Your next Hero Power deals 2 more damage. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_HERO_OR_MINION_TARGET:0}
	play = (Hit(TARGET,3),Buff(CONTROLLER,'SW_321e'))
	pass

class SW_321e:
	""" Aiming
	Your next Hero Power deals 2 more damage. """
	events=Activate(CONTROLLER, HERO_POWER).on(Hit(ENEMY_HERO, 2),Destroy(SELF))
	pass

class SW_322:#OK
	""" Defend the Dwarven District
	[Questline:] Deal damage with 2 spells. [Reward:] Your Hero Power can target minions. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Damage(ENEMY_CHARACTERS).on(SpellAndDamage(CONTROLLER,
		SidequestCounter(SELF, 2, [\
			ChangeHeroPower(CONTROLLER, "HERO_05dbp"),Summon(CONTROLLER,'SW_322t'),Destroy(SELF)\
		])))
	#events = OWN_SPELL_PLAY.on( Damage(ENEMY_CHARACTERS).on(SidequestCounter(SELF, 2, [ChangeHeroPower(CONTROLLER, "HERO_05dbp")])) )
	pass

class SW_322t:#OK
	""" Take the High Ground
	[Questline:] Deal damage with 2 spells.[Reward:] Set the Cost ofyour Hero Power to (0). """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Damage(ENEMY_CHARACTERS).on(SpellAndDamage(CONTROLLER,
		SidequestCounter(SELF, 2, [\
			SetTag(FRIENDLY_HERO_POWER, {GameTag.COST: 0}),Summon(CONTROLLER,'SW_322t2'),Destroy(SELF)\
		])))
	pass

class SW_322t2:#OK
	""" Knock 'Em Down
	[Questline:] Dealdamage with 2 spells.[Reward:] Tavish,Master Marksman. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Damage(ENEMY_CHARACTERS).on(SpellAndDamage(CONTROLLER,
		SidequestCounter(SELF, 2, [\
			Summon(CONTROLLER,'SW_322t4'),Destroy(SELF)\
		]))) 
	pass

class SW_322t4:#OK
	""" Tavish, Master Marksman
	[Battlecry:] For the rest of the game, spells you cast refresh your Hero Power. """
	events = OWN_SPELL_PLAY.on(RefreshHeroPower(FRIENDLY_HERO_POWER))
	pass

class SW_323:#OK できた気がする。
	""" The Rat King
	[Rush]. [Deathrattle:] Go[Dormant]. Revive after 5 friendly minions die. """
	events = Death(FRIENDLY + MINION).on(Asphyxia(SELF))
	pass

class SW_323e:
	""" Rat King's Slumber
		[Dormant]. Awaken after @ |4(friendly minion dies., friendly minions die.) """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	#pass

class SW_455:#OK
	""" Rodent Nest
	[Deathrattle:] Summon five 1/1 Rats. """
	deathrattle = Summon(CONTROLLER,'SW_455t') * 5
	pass

class SW_455t:
	""" Rat
	 """
	#
	pass

class SW_457:#OK
	""" Leatherworking Kit
	After three friendly Beasts die, draw a Beast and give it +1/+1.Lose 1 Durability. """
	events = Death(FRIENDLY + BEAST).on(SidequestCounter(SELF,3,[Give(CONTROLLER, RANDOM(FRIENDLY_DECK + BEAST)).then(Buff(Give.CARD,'SW_457e')), Heal(SELF,-1)]))
	pass
SW_457e=buff(atk=1,health=1)


class SW_458:#
	""" Ramming Mount
	Give a minion +2/+2 and [Immune] while attacking. When it dies,summon a Ram. """
	requirements = { PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0} 
	play = Buff(TARGET,'SW_458e')
	pass

class SW_458e:
	""" On a Ram
	+2/+2 and [Immune] while attacking. [Deathrattle:] Summon a Ram. """
	deathrattle = Summon(CONTROLLER, "SW_458t")
	tags = {
		GameTag.ATK: +2,
		GameTag.HEALTH: +1,
		GameTag.DEATHRATTLE: True,
		GameTag.IMMUNE_WHILE_ATTACKING: True
	}

class SW_458t:### 
	""" Tavish's Ram
	[Immune] while attacking. """
	#<Tag enumID="373" name="IMMUNE_WHILE_ATTACKING" type="Int" value="1"/>
	pass

class SW_459:#OK
	""" Stormwind Piper
	After this minion attacks,give your Beasts +1/+1. """
	events = Attack(SELF, ENEMY_CHARACTERS).on(Buff(FRIENDLY_MINIONS+BEAST,'SW_459e'))
	pass

SW_459e=buff(atk=1,health=1)
""" Entranced
	+1/+1. """
#

class SW_460_AttackByAll(TargetedAction):
	"""   """
	TARGET = ActionArg()
	def do(self, source, target):
		for attacker in source.controller.field:
			Attack(attacker,target).trigger(source)
			if attacker.health==0:
				log.info("%r revives into the hand",attacker)
				Give(source.controller,Copy(ID(attacker))).trigger(source.controller)

class SW_460:#OK
	""" Devouring Swarm
	Choose an enemy minion.Your minions attack it,then return any that die to your hand. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0}
	play = SW_460_AttackByAll(TARGET)
	pass

class SW_463:#OK
	""" Imported Tarantula
	[Tradeable] [Deathrattle:] Summon two1/1 Spiders with[Poisonous] and [Rush]. """
	deathrattle = Summon(CONTROLLER,'SW_463t') * 2
	pass

class SW_463t:
	""" Invasive Spiderling
	[Poisonous][Rush] """
	#
	pass

