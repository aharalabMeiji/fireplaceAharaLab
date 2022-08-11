from ..utils import *

###############################




StormWind_Hunter=[]

StormWind_Defias_Blastfisher=True#OK
StormWind_Monstrous_Parrot=True#OK
StormWind_Doggie_Biscuit=True#OK


StormWind_Rats_of_Extraordinary_Size=True#OK

StormWind_Aimed_Shot=True#OK

StormWind_Defend_the_Dwarven_District=True#OK

StormWind_The_Rat_King=True#OK

StormWind_Rodent_Nest=True#OK

StormWind_Leatherworking_Kit=True#OK
StormWind_Ramming_Mount=True#OK

StormWind_Stormwind_Piper=True#OK

StormWind_Devouring_Swarm=True#OK
StormWind_Imported_Tarantula=True#OK






############################################################

if StormWind_Defias_Blastfisher:# 
	StormWind_Hunter+=['DED_007']
class DED_007:# <3>[1578] ###OK
	""" Defias Blastfisher
	[Battlecry:] Deal 2 damage to a random enemy. Repeat for each of your Beasts. """
	play = Hit(RANDOM(ENEMY_CHARACTERS),2), Hit(RANDOM(ENEMY_CHARACTERS),2) * Count(FRIENDLY_MINIONS + BEAST)
	pass




if StormWind_Monstrous_Parrot:# 
	StormWind_Hunter+=['DED_008']
class DED_008:# <3>[1578] ###OK
	""" Monstrous Parrot
	[Battlecry:] Repeat the last friendly [Deathrattle] that triggered. """
	def play(self):
		death_log = self.controller.death_log
		deathrattle = None
		for card in death_log:
			if card.has_deathrattle:
				deathrattle = card.deathrattles[-1]
				if isinstance(deathrattle,(list, tuple)):
					deathrattle = deathrattle[0]
		if deathrattle != None:
			deathrattle.trigger(self)
		pass
	pass



if StormWind_Doggie_Biscuit:# 
	StormWind_Hunter+=['DED_009','DED_009e']
class DED_009:# <3>[1578] ###OK
	""" Doggie Biscuit
	[Tradeable]Give a minion +2/+3.After you [Trade] this, give a friendly minion [Rush]. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0}
	play = Buff(TARGET, 'DED_009e')
	#trade = Buff(RANDOM(FRIENDLY_MINIONS),'DED_001at')-> game.trade_card()
	pass

DED_009e = buff(2,3)# <3>[1578]
""" Good Doggie!
+2/+3. """




if StormWind_Rats_of_Extraordinary_Size:# 
	StormWind_Hunter+=['SW_320','SW_320e']
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




if StormWind_Aimed_Shot:# 
	StormWind_Hunter+=['SW_321','SW_321e']
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




if StormWind_Defend_the_Dwarven_District:# 
	StormWind_Hunter+=['SW_322','SW_322t','SW_322t2','SW_322t4']
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




if StormWind_The_Rat_King:# 
	StormWind_Hunter+=['SW_323','SW_323e']
class SW_323:#OK できた気がする。
	""" The Rat King
	[Rush]. [Deathrattle:] Go[Dormant]. Revive after 5 friendly minions die. """
	events = Death(FRIENDLY + MINION).on(Asphyxia(SELF))
	pass

class SW_323e:
	""" Rat King's Slumber
		[Dormant]. Awaken after @ |4(friendly minion dies., friendly minions die.) """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	pass




if StormWind_Rodent_Nest:# 
	StormWind_Hunter+=['SW_455','SW_455t']
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




if StormWind_Leatherworking_Kit:# 
	StormWind_Hunter+=['SW_457','SW_457e']
class SW_457:#OK
	""" Leatherworking Kit
	After three friendly Beasts die, draw a Beast and give it +1/+1.Lose 1 Durability. """
	events = Death(FRIENDLY + BEAST).on(SidequestCounter(SELF,3,[Give(CONTROLLER, RANDOM(FRIENDLY_DECK + BEAST)).then(Buff(Give.CARD,'SW_457e')), Heal(SELF,-1)]))
	pass
SW_457e=buff(atk=1,health=1)



if StormWind_Ramming_Mount:# 
	StormWind_Hunter+=['SW_458','SW_458e','SW_458t']
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




if StormWind_Stormwind_Piper:# 
	StormWind_Hunter+=['SW_459','SW_459e']
class SW_459:#OK
	""" Stormwind Piper
	After this minion attacks,give your Beasts +1/+1. """
	events = Attack(SELF, ENEMY_CHARACTERS).on(Buff(FRIENDLY_MINIONS+BEAST,'SW_459e'))
	pass

SW_459e=buff(atk=1,health=1)
""" Entranced +1/+1. """




if StormWind_Devouring_Swarm:# 
	StormWind_Hunter+=['SW_460']
class SW_460_AttackByAll(TargetedAction):
	"""   """
	TARGET = ActionArg()
	def do(self, source, target):
		for attacker in source.controller.field:
			Attack(attacker,target).trigger(source)
			if attacker.health==0:
				if Config.LOGINFO:
					print("%r revives into the hand"%attacker)
				Give(source.controller,Copy(ID(attacker))).trigger(source.controller)

class SW_460:#OK
	""" Devouring Swarm
	Choose an enemy minion.Your minions attack it,then return any that die to your hand. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0}
	play = SW_460_AttackByAll(TARGET)
	pass




if StormWind_Imported_Tarantula:# 
	StormWind_Hunter+=['SW_463','SW_463t']
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



###############################


