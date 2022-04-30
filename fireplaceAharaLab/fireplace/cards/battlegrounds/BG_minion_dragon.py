
from ..utils import *

BG_Minion_Dragon =[
	'BG21_027','BG21_027e','BG21_027_G',#Evolving Chromawing(1) ###OK
	'BGS_019','TB_BaconUps_102',#Red Whelp(1)
	'BGS_045','BGS_045e','TB_BaconUps_115','TB_BaconUps_115e',#Glyph Guardian(2)
	'BGS_034','TB_BaconUps_149',#Bronze Warden(3)
	'BGS_067','BGS_067e','TB_BaconUps_117','TB_BaconUps_117e',#Drakonid Enforcer(3)
	'BGS_038','TB_BaconUps_108',#Twilight Emissary(3)
	'ICC_029','TB_BaconUps_120',#Cobalt Scalebane(4)
	'BG21_012','BG21_012_G',#Prestor's Pyrospawn(4)
	'BG21_014','BG21_014e','BG21_014_G',#Prized Promo-Drake(4)
	'BG21_015','BG21_015_G',#Tarecgosa(4)
	'BGS_043','TB_BaconUps_110',#Murozond(5)
	'BGS_036','TB_BaconUps_106',#Razorgore, the Untamed (5)
	'BGS_041','TB_BaconUps_109',#Kalecgos, Arcane Aspect (6)
	]

BG_PoolSet_Dragon=[
	['BG21_027','BGS_019',],
	['BGS_045',],
	['BGS_034','BGS_067','BGS_038',],
	['ICC_029','BG21_012','BG21_014','BG21_015',],
	['BGS_043','BGS_036',],
	['BGS_041',],
	]

BG_Dragon_Gold={
	'BG21_027':'BG21_027_G',#Evolving Chromawing(1)
	'BGS_019':'TB_BaconUps_102',#Red Whelp(1)
	'BGS_045':'TB_BaconUps_115',#Glyph Guardian(2)
	'BGS_034':'TB_BaconUps_149',#Bronze Warden(3)
	'BGS_067':'TB_BaconUps_117',#Drakonid Enforcer(3)
	'BGS_038':'TB_BaconUps_108',#Twilight Emissary(3)
	'ICC_029':'TB_BaconUps_120',#Cobalt Scalebane(4)
	'BG21_012':'BG21_012_G',#Prestor's Pyrospawn(4)
	'BG21_014':'BG21_014_G',#Prized Promo-Drake(4)
	'BG21_015':'BG21_015_G',#Tarecgosa(4)
	'BGS_043':'TB_BaconUps_110',#Murozond(5)
	'BGS_036':'TB_BaconUps_106',#Razorgore, the Untamed (5)
	'BGS_041':'TB_BaconUps_109',#Kalecgos, Arcane Aspect (6)
	}


#Evolving Chromawing(1)
class BG21_027:# <12>[1453]
	""" Evolving Chromawing
	After you upgrade your Tavern Tier, double this minion's Attack. """
	events = UpgradeTier(CONTROLLER).after(Buff(SELF, 'BG21_027e'))
	pass
class BG21_027e:
	atk = lambda self, i: i*2
	pass
class BG21_027_G:# <12>[1453]
	""" Evolving Chromawing
	After you upgrade your Tavern Tier, triple this minion's Attack. """
	events = UpgradeTier(CONTROLLER).after(Buff(SELF, 'BG21_027_Ge'))
	pass
class BG21_027_Ge:
	atk = lambda self, i: i*3
	pass

#Red Whelp(1)
class BGS_019:# <12>[1453]
	""" Red Whelp
	[Start of Combat:] Deal1 damage per friendly Dragon to one random enemy minion. """
	events = BeginBattle(CONTROLLER).on(Hit(RANDOM(ENEMY_MINIONS, Count(FRIENDLY_MINIONS + DRAGON))))
	pass
class TB_BaconUps_102:# <12>[1453]
	""" Red Whelp
	[Start of Combat:] Deal1 damage per friendlyDragon to one randomenemy minion twice. """
	events = BeginBattle(CONTROLLER).on(Hit(RANDOM(ENEMY_MINIONS, Count(FRIENDLY_MINIONS + DRAGON))),Hit(RANDOM(ENEMY_MINIONS, Count(FRIENDLY_MINIONS + DRAGON))))
	pass

#Glyph Guardian(2)
class BGS_045:# <4>[1453]
	""" Glyph Guardian
	Whenever this attacks, double its Attack. """
	events = Attack(SELF).on(Buff(SELF,'BGS_045e'))
	pass
class BGS_045e:
	atk = lambda self, i: i*2
class TB_BaconUps_115:# <4>[1453]
	""" Glyph Guardian
	Whenever this attacks, triple its Attack. """
	events = Attack(SELF).on(Buff(SELF,'TB_BaconUps_115e'))
	pass
class TB_BaconUps_115e:
	atk = lambda self, i: i*3
	pass

#Bronze Warden(3)
class BGS_034:# <12>[1453]
	""" Bronze Warden
	[Divine Shield][Reborn] """
	#<Tag enumID="194" name="DIVINE_SHIELD" type="Int" value="1"/>
	#<Tag enumID="1085" name="REBORN" type="Int" value="1"/>
	pass
class TB_BaconUps_149:# <12>[1453]
	""" Bronze Warden
	[Divine Shield][Reborn] """
	pass

#Drakonid Enforcer(3)
class BGS_067:# <12>[1453]
	""" Drakonid Enforcer
	After a friendly minion loses [Divine Shield], gain_+2/+2. """
	events = LoseDivineShield(FRIENDLY_MINIONS).on(Buff(SELF,'BGS_067e'))
	pass
BGS_067e=buff(2,2)
class TB_BaconUps_117:# <12>[1453]
	""" Drakonid Enforcer
	After a friendly minion loses [Divine Shield], gain_+4/+4. """
	events = LoseDivineShield(FRIENDLY_MINIONS).on(Buff(SELF,'TB_BaconUps_117e'))
	pass
TB_BaconUps_117e=buff(4,4)
#Twilight Emissary(3)
class BGS_038:# <12>[1453]
	""" Twilight Emissary
	[Taunt][Battlecry:] Give a friendly Dragon +2/+2. """
	#
	pass
class TB_BaconUps_108:# <12>[1453]
	""" Twilight Emissary
	[Taunt][Battlecry:] Give a friendly Dragon +4/+4. """
	#
	pass

#Cobalt Scalebane(4)
class ICC_029:
	""" Cobalt Scalebane
	At the end of your turn, give another random friendly minion +3 Attack. """
class TB_BaconUps_120:# <12>[1453]
	""" Cobalt Scalebane
	At the end of your turn, give another random friendly minion +6 Attack. """
	#
	pass

#Prestor's Pyrospawn(4)
class BG21_012:# <12>[1453]
	""" Prestor's Pyrospawn
	Whenever another friendlyDragon attacks, deal3 damage to its target. """
	#
	pass

class BG21_012_G:# <12>[1453]
	""" Prestor's Pyrospawn
	Whenever another friendlyDragon attacks, deal6 damage to its target. """
	#
	pass

#Prized Promo-Drake(4)
class BG21_014:# <12>[1453]
	""" Prized Promo-Drake
	[Start of Combat:] Giveadjacent minions +1/+1__for each friendly Dragon. """
	#
	pass
class BG21_014e:# <12>[1453]
	""" Promoted
	Increased stats from Promo-Drake """
	#
	pass
class BG21_014_G:# <12>[1453]
	""" Prized Promo-Drake
	[Start of Combat:] Giveadjacent minions +2/+2__for each friendly Dragon. """
	#
	pass

#Tarecgosa(4)
class BG21_015:# <12>[1453]
	""" Tarecgosa
	This permanently keeps enchantments from combat. """
	#
	pass

class BG21_015_G:# <12>[1453]
	""" Tarecgosa
	This permanently doubles and keeps enchantments from combat. """
	#
	pass

#Murozond(5)
class BGS_043:# <12>[1453]
	""" Murozond
	[Battlecry:] Add a minionfrom your last opponent'swarband to your hand. """
	#
	pass
class TB_BaconUps_110:# <12>[1453]
	""" Murozond
	[Battlecry:] Add a minionfrom your last opponent'swarband to your hand.Make it Golden! """
	#
	pass

#Razorgore, the Untamed (5)
class BGS_036:# <12>[1453]
	""" Razorgore, the Untamed
	At the end of your turn, gain +1/+1 for each Dragon you have. """
	#
	pass
class TB_BaconUps_106:# <12>[1453]
	""" Razorgore, the Untamed
	At the end of your turn, gain +2/+2 for each Dragon you have. """
	#
	pass

#Kalecgos, Arcane Aspect (6)
class BGS_041:# <12>[1453]
	""" Kalecgos, Arcane Aspect
	After you play a minion with [Battlecry], give your Dragons +1/+1. """
	#
	pass
class TB_BaconUps_109:# <12>[1453]
	""" Kalecgos, Arcane Aspect
	After you play a minion with [Battlecry], give your Dragons +2/+2. """
	#
	pass






