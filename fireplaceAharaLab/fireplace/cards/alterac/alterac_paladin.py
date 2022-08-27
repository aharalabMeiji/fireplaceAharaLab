from ..utils import *

Alterac_Paladin=[]

Alterac_The_Immovable_Object=True
Alterac_Lightforged_Cariel=True
Alterac_Vitality_Surge=True
Alterac_Hold_the_Bridge=True
Alterac_Templar_Captain=True
Alterac_Brasswing=True
Alterac_Cavalry_Horn=True
Alterac_Protect_the_Innocent=True
Alterac_Stonehearth_Vindicator=True
Alterac_Dun_Baldar_Bridge=True
Alterac_Saidan_the_Scarlet=True
Alterac_Stormwind_Avenger=True
Alterac_Battle_Vicar=True
Alterac_Ring_of_Courage=True



if Alterac_The_Immovable_Object:# #### OKOK ####
	Alterac_Paladin+=['AV_146']
	Alterac_Paladin+=['AV_146e']
	Alterac_Paladin+=['AV_146e2']
class AV_146:# <5>[1626]
	""" The Immovable Object  (7/2/5)
	This doesn't loseDurability. Your hero takes half damage,rounded up. """
	play = Buff(SELF, 'AV_146e2'), Buff(CONTROLLER,'AV_146e')
	pass

class AV_146e:# <5>[1626]#
	""" Tough
	Take half damage, rounded up. """
	def apply(self, target):
		target.take_half_damage=True
	pass

class AV_146e2:# <5>[1626]
	""" Resilient Weapon
	No durability loss. """
	def apply(self, target):
		target.no_durability_loss=True
	pass

if Alterac_Lightforged_Cariel:# 
	Alterac_Paladin+=['AV_206']
	Alterac_Paladin+=['AV_206p']
	Alterac_Paladin+=['AV_206pe']
class AV_206:# <5>[1626]
	""" Lightforged Cariel
	[Battlecry:] Deal 2damage to all enemies.Equip a 2/5Immovable Object. """
	play = Hit(ENEMY_CHARACTERS, 2), Summon(CONTROLLER, 'AV_146')
	pass

class AV_206p:# <5>[1626]
	""" Blessing of Queens
	[Hero Power]Give a random minion in your hand +4/+4. """
	activate = Buff(RANDOM(FRIENDLY_HAND + MINION), 'AV_206pe')
	pass
AV_206pe=buff(4,4)# <5>[1626]

if Alterac_Vitality_Surge:# 
	Alterac_Paladin+=['AV_213']
class AV_213:# <5>[1626]
	""" Vitality Surge
	Draw a minion.Restore Health to your hero equal to its Cost. """
	#
	pass

if Alterac_Hold_the_Bridge:# 
	Alterac_Paladin+=['AV_338']
	Alterac_Paladin+=['AV_338e']
	Alterac_Paladin+=['AV_338e2']
class AV_338:# <5>[1626]
	""" Hold the Bridge
	Give a minion +2/+1and [Divine Shield].It gains [Lifesteal] untilend of turn. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0,}
	play = Buff(TARGET, 'AV_338e'), Buff(SELF, 'AV_338e2')
	pass

class AV_338e:# <5>[1626]
	""" High Morale
	+2/+1. """
	tags={
		GameTag.ATK:2,
		GameTag.HEALTH:1,
		}
	def apply(self, target):
		target.divine_shield=True
	pass

class AV_338e2:# <5>[1626]
	""" High Morale
	[Lifesteal] this turn. """
	tags={GameTag.LIFESTEAL:True, }
	#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>
	pass

if Alterac_Templar_Captain:# 
	Alterac_Paladin+=['AV_339']
class AV_339:# <5>[1626]
	""" Templar Captain
	[Rush]. After this attacks a minion, summon a 5/5 Defender(AV_342t) with [Taunt]. """
	events = Attack(SELF, ENEMY_MINIONS).after(Summon(CONTROLLER, 'AV_342t'))
	pass

if Alterac_Brasswing:# 
	Alterac_Paladin+=['AV_340']
class AV_340:# <5>[1626]
	""" Brasswing
	At the end of your turn, deal2 damage to all enemies.[Honorable Kill:] Restore 4 Health to your hero. """
	events = OWN_TURN_END.on(Hit(ENEMY_CHARACTERS, 2))
	honorable_kill = Heal(FRIENDLY_HERO, 4)
	pass

if Alterac_Cavalry_Horn:# 
	Alterac_Paladin+=['AV_341']
class AV_341_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		lowest=[]
		for card in target.hand:
			if card.type==CardType.MINION:
				if lowest==[] or lowest[0].cost>card.cost:
					lowest=[card]
				elif lowest[0].cost==card.cost:
					lowest.append(card)
		if len(lowest)==0:
			return
		Summon(target, random.choice(lowest)).trigger(source)
		pass
class AV_341:# <5>[1626]
	""" Cavalry Horn
	[Deathrattle:] Summon the lowest Cost minion in your hand. """
	deathrattle=AV_341_Action(CONTROLLER)
	pass

if Alterac_Protect_the_Innocent:# 
	Alterac_Paladin+=['AV_342']
	Alterac_Paladin+=['AV_342t']
class AV_342:# <5>[1626]
	""" Protect the Innocent
	Summon a 5/5 Defender with [Taunt]. If your hero was healed this turn, summon another. """
	def play(self): 
		Summon(CONTROLLER, 'AV_342t').trigger(self)
		actions=[action for action in self.controller._targetedaction_log if isinstance(action['class'],Heal) and action['target']==self.controller.hero]
		if len(actions)>0:
			Summon(CONTROLLER, 'AV_342t').trigger(self)
	pass

class AV_342t:# <5>[1626]
	""" Stormpike Defender
	[Taunt] """
	#
	pass

if Alterac_Stonehearth_Vindicator:# 
	Alterac_Paladin+=['AV_343']
	Alterac_Paladin+=['AV_343e']
class AV_343:# <5>[1626]
	""" Stonehearth Vindicator
	[Battlecry:] Draw a spell that costs (3) or less.It costs (0) this turn. """
	def play(self):
		cards=[card for card in self.controller.deck if card.cost<=3]
		if len(cards)>0:
			card = random.choice(cards)
			Buff(card,'AV_343e').trigger(self)
			card.zone=Zone.HAND
	pass

class AV_343e:# <5>[1626]
	""" Stone Fortitude
	Costs (0)  this turn. """
	#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>
	cost = lambda self, i : 0
	pass

if Alterac_Dun_Baldar_Bridge:# 
	Alterac_Paladin+=['AV_344']
	Alterac_Paladin+=['AV_344e']
class AV_344:# <5>[1626]
	""" Dun Baldar Bridge
	After you summon a minion, give it +2/+2.Lasts 3 turns. """
	tags={GameTag.SIDEQUEST:True, }	
	events = [
		Summon(CONTROLLER, FRIENDLY + MINION).after(Buff(Summon.CARD, 'AV_344e')),
		OWN_TURN_BEGIN.on(SidequestCounter(SELF, 3, [Destroy(SELF)])),
	]
	pass
AV_344e=buff(2,2)

if Alterac_Saidan_the_Scarlet:# 
	Alterac_Paladin+=['AV_345']
class AV_345_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self,source,target, buff):
		if buff.atk>0 or buff.health>0:
			Buff(target, buff.id).trigger(source)
class AV_345:# <5>[1626]
	""" Saidan the Scarlet
	[Rush.] Whenever this minion gains Attack or Health, double that amount <i>(wherever this is)</i>. """
	class Hand:
		events = Buff(SELF).on(AV_345_Action(SELF, Buff.BUFF))
	events = Buff(SELF).on(AV_345_Action(SELF, Buff.BUFF))
	pass


if Alterac_Stormwind_Avenger:# 
	Alterac_Paladin+=['ONY_020']
	Alterac_Paladin+=['ONY_020e']
class ONY_020:# <5>[1626]
	""" Stormwind Avenger
	After you cast a spell on this minion, it gains +2 Attack. """
	events = Play(CONTROLLER, SPELL, SELF).after(Buff(SELF,'ONY_020e'))
	pass
ONY_020e=buff(2,0)

if Alterac_Battle_Vicar:# 
	Alterac_Paladin+=['ONY_022']
class ONY_022:# <5>[1626]
	""" Battle Vicar
	[Battlecry:] [Discover] a Holy spell. """
	play = Discover(CONTROLLER, RandomSpell(spell_school=SpellSchool.HOLY))
	pass

if Alterac_Ring_of_Courage:# 
	Alterac_Paladin+=['ONY_027']
	Alterac_Paladin+=['ONY_027e']
class ONY_027:# <5>[1626]
	""" Ring of Courage
	[Tradeable]Give a minion +1/+1. Repeat for each enemy minion. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0, PlayReq.REQ_HERO_OR_MINION_TARGET:0}	
	play = Buff(TARGET,'ONY_027e'),Buff(TARGET,'ONY_027e')*Count(ENEMY_MINIONS)
	pass
ONY_027e=buff(1,1)


#######################

