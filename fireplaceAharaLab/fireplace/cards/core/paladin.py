from ..utils import *
##嶋田君の仕事！！

class CORE_AT_075:# <5>[1637]#OK

    """ Warhorse Trainer
    Your Silver Hand Recruits have +1 Attack. """
    update = Refresh(FRIENDLY + ID("CS2_101t"), buff="AT_075e")
    pass

AT_075e = buff(atk=1)

class CORE_CS2_088:# <5>[1637]#OK
    """ Guardian of Kings
    [Taunt][Battlecry:] Restore #6 Health to your hero. """
    #
    play = Heal(FRIENDLY_HERO, 6)
    pass

class CORE_CS2_089:# <5>[1637]#OK
    """ Holy Light
    Restore #8 Health to your hero. """
    #
    play = Heal(FRIENDLY_HERO, 8)
    pass

class CORE_CS2_092:# <5>[1637]#OK
	""" Blessing of Kings
	Give a minion +4/+4. <i>(+4 Attack/+4 Health)</i> """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "CS2_092e")
	pass

CS2_092e = buff(+4, +4)

class CORE_CS2_093:# <5>[1637]#OK
    """ Consecration
    Deal $2 damage to all enemies. """
    #
    play = Hit(ENEMY_CHARACTERS, 2)
    pass

class CORE_CS2_097:# <5>[1637]#OK
    """ Truesilver Champion
    Whenever your hero attacks, restore #2_Health to it. """
    #
    events = Attack(FRIENDLY_HERO, ENEMY_CHARACTERS).on(Heal(FRIENDLY_HERO,2))
    pass


class CORE_EX1_130:# <5>[1637]
	""" Noble Sacrifice
	[Secret:] When an enemy attacks, summon a 2/1 Defender as the new target. """
	#
	sercret = Attack(ENEMY_MINIONS).on(FULL_BOARD | (
		Reveal(SELF), Retarget(Attack.ATTACKER, Summon(CONTROLLER, "EX1_130a"))
	))
	pass

class EX1_130a:
	""" Defender vanilla """
	pass

class CORE_EX1_362:# <5>[1637]
	""" Argent Protector
	[Battlecry:] Give a friendly minion [Divine Shield]. """
	#
	pass

class CORE_EX1_382:# <5>[1637]
	""" Aldor Peacekeeper
	[Battlecry:] Change an_enemy minion's Attack to 1. """
	#
	pass

class CORE_EX1_383:# <5>[1637]
	""" Tirion Fordring
	[[Divine Shield],] [Taunt] [Deathrattle:] Equip a 5/3_Ashbringer. """
	#
	pass

class CORE_EX1_619:# <5>[1637]
	""" Equality
	Change the Health of ALL minions to 1. """
	#
	pass

class CORE_FP1_020:# <5>[1637]
	""" Avenge
	[Secret:] When one of your minions dies, give a random friendly minion +3/+2. """
	#
	pass

class CORE_ICC_038:# <5>[1637]
	""" Righteous Protector
	[Taunt][Divine Shield] """
	#
	pass

class CORE_OG_273:# <5>[1637]
	""" Stand Against Darkness
	Summon five 1/1 Silver Hand Recruits. """
	#
	pass

class CS3_016:# <5>[1637]
	""" Reckoning
	[Secret:] After an enemy minion deals 3 or more damage, destroy it. """
	#
	secret = Attack(ENEMY_MINIONS, FRIENDLY_CHARACTERS).after(
		Reveal(SELF),
		Destroy(Attack.ATTACKER)
		)
	pass

class CS3_029:# <5>[1637]
	""" Pursuit of Justice
	Give +1 Attack to Silver Hand Recruits you summon this game. """
	#
	pass

class CS3_029e:# <5>[1637]
	""" Pursuit of Justice
	Your Silver Hand Recruits have +1 Attack. """
	#
	pass

class CS3_029e2:# <5>[1637]
	""" Pursuit of Justice
	+1 Attack. """
	#
	pass

