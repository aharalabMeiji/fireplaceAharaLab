from ..utils import *

Classic_Paladin=[]

Classic_Blessing_of_Might=True
Classic_Guardian_of_Kings=True
Classic_Holy_Light=True
Classic_Lights_Justice=True
Classic_Blessing_of_Kings=True
Classic_Consecration=True
Classic_Hammer_of_Wrath=True
Classic_Truesilver_Champion=True
Classic_Silver_Hand_Recruit=True
Classic_Noble_Sacrifice=True
Classic_Eye_for_an_Eye=True
Classic_Redemption=True
Classic_Divine_Favor=True
Classic_Lay_on_Hands=True
Classic_Blessed_Champion=True
Classic_Humility=True
Classic_Argent_Protector=True
Classic_Blessing_of_Wisdom=True
Classic_Holy_Wrath=True
Classic_Sword_of_Justice=True
Classic_Hand_of_Protection=True
Classic_Repentance=True
Classic_Aldor_Peacekeeper=True
Classic_Tirion_Fordring=True
Classic_Avenging_Wrath=True
Classic_Equality=True
Classic_Reinforce=False# HP


if Classic_Blessing_of_Might:# ### OK ###
	Classic_Paladin+=['VAN_CS2_087','CS2_087e']
class VAN_CS2_087:# <5>[1646]
	""" Blessing of Might
	Give a minion +3_Attack. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "CS2_087e")
	pass
CS2_087e = buff(atk=3)

if Classic_Guardian_of_Kings:# ### OK ###
	Classic_Paladin+=['VAN_CS2_088']
class VAN_CS2_088:# <5>[1646]
	""" Guardian of Kings
	[Battlecry:] Restore #6 Health to your hero. """
	play = Heal(FRIENDLY_HERO, 6)
	pass

if Classic_Holy_Light:# ### OK ###
	Classic_Paladin+=['VAN_CS2_089']
class VAN_CS2_089:# <5>[1646]
	""" Holy Light
	Restore #6 Health. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Heal(TARGET, 6)
	pass

if Classic_Lights_Justice:# ### OK ###
	Classic_Paladin+=['VAN_CS2_091']
class VAN_CS2_091:# <5>[1646]
	""" Light's Justice
	 """
	#
	pass

if Classic_Blessing_of_Kings:# ### OK ###
	Classic_Paladin+=['VAN_CS2_092','CS2_092e']
class VAN_CS2_092:# <5>[1646]
	""" Blessing of Kings
	Give a minion +4/+4. <i>(+4 Attack/+4 Health)</i> """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "CS2_092e")
	pass
CS2_092e = buff(+4, +4)

if Classic_Consecration:# ### OK ###
	Classic_Paladin+=['VAN_CS2_093']
class VAN_CS2_093:# <5>[1646]
	""" Consecration
	Deal $2 damage to all enemies. """
	play = Hit(ENEMY_CHARACTERS, 2)
	pass

if Classic_Hammer_of_Wrath:# ### OK ###
	Classic_Paladin+=['VAN_CS2_094']
class VAN_CS2_094:# <5>[1646]
	""" Hammer of Wrath
	Deal $3 damage.Draw a card. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 3), Draw(CONTROLLER)
	pass

if Classic_Truesilver_Champion:# ### OK ###
	Classic_Paladin+=['VAN_CS2_097']
class VAN_CS2_097:# <5>[1646]
	""" Truesilver Champion
	Whenever your hero attacks, restore #2_Health to it. """
	events = Attack(FRIENDLY_HERO).on(Heal(FRIENDLY_HERO, 2))
	pass

if Classic_Silver_Hand_Recruit:# ### OK ###
	Classic_Paladin+=['VAN_CS2_101t']
class VAN_CS2_101t:# <5>[1646]
	""" Silver Hand Recruit
	 """
	#
	pass

if Classic_Noble_Sacrifice:# ### OK ###
	Classic_Paladin+=['VAN_EX1_130']
	Classic_Paladin+=['VAN_EX1_130a']
class VAN_EX1_130:# <5>[1646]
	""" Noble Sacrifice
	[Secret:] When an enemy attacks, summon a 2/1 Defender as the new target. """
	secret = Attack(ENEMY_MINIONS).on(FULL_BOARD | (
		Reveal(SELF), Retarget(Attack.ATTACKER, Summon(CONTROLLER, "VAN_EX1_130a"))
	))
	pass

class VAN_EX1_130a:# <5>[1646]
	""" Defender
	 """
	#
	pass

if Classic_Eye_for_an_Eye:# ### OK ###
	Classic_Paladin+=['VAN_EX1_132']
class VAN_EX1_132:# <5>[1646]
	""" Eye for an Eye
	[Secret:] When your hero takes damage, deal_that much damage to the enemy hero. """
	secret = Damage(FRIENDLY_HERO).on(
		Reveal(SELF), Hit(ENEMY_HERO, Damage.AMOUNT)
	)
	pass

if Classic_Redemption:# checking
	Classic_Paladin+=['VAN_EX1_136']
class VAN_EX1_136_Action(TargetedAction):
	## Summon(CONTROLLER, Copy(Death.ENTITY)).then(SetCurrentHealth(Summon.CARD, 1))
	def do(self, source, target):
		if isinstance(target, list):
			target=target[0]
		newcard=Summon(source.controller, target.id).trigger(source)
		newcard=newcard[0][0];
		newcard.max_health=1
class VAN_EX1_136:# <5>[1646]
	""" Redemption
	[Secret:] When a friendly minion dies, return it to life with 1 Health. """
	secret = Death(FRIENDLY + MINION).on(
		Reveal(SELF),
		VAN_EX1_136_Action(Death.ENTITY)
	)
	pass

if Classic_Divine_Favor:# ### OK ###
	Classic_Paladin+=['VAN_EX1_349']
class VAN_EX1_349:# <5>[1646]
	""" Divine Favor
	Draw cards until you have as many in hand as your opponent. """
	play = DrawUntil(CONTROLLER, Count(ENEMY_HAND))
	pass

if Classic_Lay_on_Hands:# ### OK ###
	Classic_Paladin+=['VAN_EX1_354']
class VAN_EX1_354:# <5>[1646]
	""" Lay on Hands
	Restore #8 Health. Draw_3 cards. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Heal(TARGET, 8), Draw(CONTROLLER) * 3
	pass

if Classic_Blessed_Champion:# ### OK ###
	Classic_Paladin+=['VAN_EX1_355','EX1_355e']
class VAN_EX1_355:# <5>[1646]
	""" Blessed Champion
	Double a minion's Attack. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "EX1_355e")
	pass
class EX1_355e:
	atk = lambda self, i: i * 2

if Classic_Humility:# ### OK ###
	Classic_Paladin+=['VAN_EX1_360','EX1_360e']
class VAN_EX1_360:# <5>[1646]
	""" Humility
	Change a minion's Attack to 1. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "EX1_360e")
	pass
class EX1_360e:
	atk = SET(1)

if Classic_Argent_Protector:# ### OK ###
	Classic_Paladin+=['VAN_EX1_362']
class VAN_EX1_362:# <5>[1646]
	""" Argent Protector
	[Battlecry:] Give a friendly minion [Divine Shield]. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_NONSELF_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = GiveDivineShield(TARGET)
	pass

if Classic_Blessing_of_Wisdom:# ### OK ###
	Classic_Paladin+=['VAN_EX1_363','EX1_363e']
class VAN_EX1_363:# <5>[1646]
	""" Blessing of Wisdom
	Choose a minion. Whenever it attacks, draw a card. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "EX1_363e")
	pass
class EX1_363e:
	events = Attack(OWNER).on(Draw(CONTROLLER))

if Classic_Holy_Wrath:# ### OK ###
	Classic_Paladin+=['VAN_EX1_365']
class VAN_EX1_365:# <5>[1646]
	""" Holy Wrath
	Draw a card and deal_damage equal to_its Cost. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Draw(CONTROLLER).then(Hit(TARGET, COST(Draw.CARD)))
	pass

if Classic_Sword_of_Justice:# checking
	Classic_Paladin+=['VAN_EX1_366','EX1_366e']
class VAN_EX1_366_Action(TargetedAction):
	def do(self, source, target):
		if target:
			if isinstance(target,list):
				target=target[0]
			Buff(target, 'EX1_366e').trigger(source)
			source.damage += 1
		pass
class VAN_EX1_366:# <5>[1646]
	""" Sword of Justice
	After you summon a minion, give it +1/+1 and this loses 1_Durability. """
	events = Summon(CONTROLLER, MINION).after(
		#VAN_EX1_366_Action(Summon.CARD)
		Buff(Summon.CARD, "EX1_366e"),
		Hit(SELF, 1)
	)
	pass
EX1_366e = buff(+1, +1)

if Classic_Hand_of_Protection:# checking
	Classic_Paladin+=['VAN_EX1_371']
class VAN_EX1_371:# <5>[1646]
	""" Hand of Protection
	Give a minion [Divine Shield]. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = GiveDivineShield(TARGET)
	pass

if Classic_Repentance:# ### OK ###
	Classic_Paladin+=['VAN_EX1_379','EX1_379e']
class VAN_EX1_379:# <5>[1646]
	""" Repentance
	[Secret:] After your opponent plays a minion, reduce its Health to 1. """
	secret = Play(OPPONENT, MINION | HERO).after(
		Reveal(SELF), Buff(Play.CARD, "EX1_379e")
	)
	pass
class EX1_379e:
	max_health = SET(1)

if Classic_Aldor_Peacekeeper:# ### OK ###
	Classic_Paladin+=['VAN_EX1_382','EX1_382e']
class VAN_EX1_382:# <5>[1646]
	""" Aldor Peacekeeper
	[Battlecry:] Change an_enemy minion's Attack to 1. """
	requirements = {
		PlayReq.REQ_ENEMY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Buff(TARGET, "EX1_382e")
	pass
class EX1_382e:
	atk = SET(1)

if Classic_Tirion_Fordring:# ### OK ###
	Classic_Paladin+=['VAN_EX1_383','EX1_383t']
class VAN_EX1_383:# <5>[1646]
	""" Tirion Fordring
	[[Divine Shield],] [Taunt] [Deathrattle:] Equip a 5/3_Ashbringer. """
	deathrattle = Summon(CONTROLLER, "EX1_383t")
	pass
class EX1_383t:
	pass

if Classic_Avenging_Wrath:# checking
	Classic_Paladin+=['VAN_EX1_384']
class VAN_EX1_384:# <5>[1646]
	""" Avenging Wrath
	Deal $8 damage randomly split among all enemy characters. """
	#def play(self):
	#count = self.controller.get_spell_damage(8)
	play = SplitHit(CONTROLLER, ENEMY_CHARACTERS, 8)
	pass

if Classic_Equality:# ### OK ###
	Classic_Paladin+=['VAN_EX1_619','EX1_619e']
class VAN_EX1_619:# <5>[1646]
	""" Equality
	Change the Health of ALL minions to 1. """
	play = Buff(ALL_MINIONS, "EX1_619e")
	pass
class EX1_619e:
	max_health = SET(1)

if Classic_Reinforce:# 
	Classic_Paladin+=['VAN_HERO_04bp','VAN_CS2_101t']
	Classic_Paladin+=['VAN_HERO_04bp2']
class VAN_HERO_04bp:# <5>[1646]
	""" Reinforce
	[Hero Power]Summon a 1/1 Silver Hand Recruit. """
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	activate = Summon(CONTROLLER, "VAN_CS2_101t")
	pass

class VAN_HERO_04bp2:# <5>[1646]
	""" The Silver Hand
	[Hero Power]Summon two 1/1 Recruits. """
	#
	pass

