from ..utils import *



BG_Hero3=[
#36#Lord Jaraxxus
#37#Maiev Shadowsong
#38#Malygos
#39#Master Nguyen
'BG20_HERO_202','BG20_HERO_202p','BG20_HERO_202pe','BG20_HERO_202pt','BG20_HERO_202_Buddy','BG20_HERO_202_Buddy_G',
#40#Millhouse Manastorm
#41#Millificent Manastorm
#42#Mr. Bigglesworth
#43#Mutanus the Devourer
#44#N'Zoth
#45#Nozdormu
#46#BG22_HERO_305#Onyxia
#47#Overlord Saurfang
'BG20_HERO_102','BG20_HERO_102p','BG20_HERO_102pe','BG20_HERO_102pe2','BG20_HERO_102pe3','BG20_HERO_102_Buddy','BG20_HERO_102_Buddy_G','BG20_HERO_102pe_Buddy',
#48#Patches the Pirate
#49#Patchwerk
#50#Pyramad
#51#Queen Wagtoggle
#52#Ragnaros the Firelord
]

BG_PoolSet_Hero3=[
	]
BG_Hero3_Buddy={
	}
BG_Hero3_Buddy_Gold={
	}

#### source ####################################################

#36#Lord Jaraxxus
class TB_BaconShop_HERO_37:# <12>[1453]
	""" Lord Jaraxxus """
class TB_BaconShop_HP_036:
	""" Bloodfury
	Give your Demons +1/+1."""
class TB_BaconShop_HERO_37_Buddy:
	"""Kil'rek
	<b>Taunt</b> <b>Deathrattle:</b> Add a random Demon to your hand."""
class TB_BaconShop_HERO_37_Buddy_G:
	""" Kil'rek
	<b>Taunt</b> <b>Deathrattle:</b> Add 2 random Demons to your hand."""

#37#Maiev Shadowsong
class TB_BaconShop_HERO_62:# <12>[1453]
	""" Maiev Shadowsong
	 """
	#
	pass
class TB_BaconShop_HP_068:
	""" Imprison
	Make a minion in Bob's Tavern <b>Dormant</b>. After 3 __turns, get it with +2/+2 """
class TB_BaconShop_HP_068pe:
	"""ImprisonedWatcher	"""
	pass
class TB_BaconShop_HP_068e:
	pass
class TB_BaconShop_HP_068e2:
	pass
class TB_BaconShop_HERO_62_Buddy:# <12>[1453]
	""" Shadow Warden
	[Battlecry:] Your next Hero Power makes the target Golden and awaken 1 turn faster. """
	#
	pass
class TB_BaconShop_HERO_62_Buddy_e:# <12>[1453]
	""" Next Hero Power Goldens
	Your next Hero Power makes the target Golden. """
	#
	pass
class TB_BaconShop_HERO_62_Buddy_G:# <12>[1453]
	""" Shadow Warden
	[Battlecry:] Your next 2 Hero Powers make the target Golden and awaken 1 turn faster. """
	#
	pass



#38#Malygos
class TB_BaconShop_HERO_58:# <12>[1453]
	""" Malygos
	 """
	#
	pass
class TB_BaconShop_HP_052:
	""" Arcane Alteration
	Replace a minion with a random one of the same Tavern Tier. <i>(Twice per turn.)</i>"""
class TB_BaconShop_HERO_58_Buddy:# <12>[1453]
	""" Nexus Lord
	'Arcane Alteration'replaces with a minionone Tavern Tier higher. """
	#
	pass
class TB_BaconShop_HERO_58_Buddy_G:# <12>[1453]
	""" Nexus Lord
	'Arcane Alteration'replaces with a minion_two Tavern Tiers higher. """
	#
	pass



#39#Master Nguyen
class BG20_HERO_202:# <12>[1453]
	""" Master Nguyen
	 """
	#
	pass
class BG20_HERO_202p:# <12>[1453]
	""" Power of the Storm
	[Passive]At the start of every turn, choose from 2 new Hero Powers. """
	#
	pass
class BG20_HERO_202pe:# <12>[1453]
	""" Shifting Hero Power
	Each turn, transform into a random Hero Power. """
	#
	pass
class BG20_HERO_202pt:# <12>[1453]
	""" Shift your Hero Power
	Trigger Power of the Storm effect """
	#
	pass
class BG20_HERO_202_Buddy:# <12>[1453]
	""" Lei Flamepaw
	'Power of the Storm' offers3 options instead of 2. """
	#
	pass
class BG20_HERO_202_Buddy_G:# <12>[1453]
	""" Lei Flamepaw
	'Power of the Storm' offers4 options instead of 2. """
	#
	pass


#40#Millhouse Manastorm
class TB_BaconShop_HERO_49:# <12>[1453]
	""" Millhouse Manastorm
	 """
	#
	pass
class TB_BaconShop_HP_054:
	""" Manastorm
	<b>Passive</b> Minions cost 2 Gold. <b>Refresh</b> costs 2 Gold. _Tavern Tiers cost (1) more."""
class TB_Baconshop_HP_054e:
	""" Costs (1) less."""
class TB_BaconShop_HERO_49_Buddy:# <12>[1453]
	""" Magnus Manastorm
	After you buy a minion,add one of the same TavernTier to Bob's Tavern. """
	#
	pass
class TB_BaconShop_HERO_49_Buddy_G:# <12>[1453]
	""" Magnus Manastorm
	After you buy a minion,add two of the same TavernTier to Bob's Tavern. """
	#
	pass





#41#Millificent Manastorm
class TB_BaconShop_HERO_17:# <12>[1453]
	""" Millificent Manastorm
	 """
	#
	pass
class TB_BaconShop_HP_015:
	""" Tinker
	<b>Passive</b>
Mechs in Bob's Tavern
have +1/+1."""
TB_BaconShop_HP_015e=buff(1,1)
class TB_BaconShop_HERO_17_Buddy:# <12>[1453]
	""" Elementium Squirrel Bomb
	<b>Deathrattle:</b> Deal 3 damage
to a random enemy minion
for each of your Mechs that
died this combat. """
	#
	pass
class TB_BaconShop_HERO_17_Buddy_G:
	""" 
	<b>Deathrattle:</b> Deal 6 damage
to a random enemy minion
for each of your Mechs that
died this combat.""" 



#42#Mr. Bigglesworth
class TB_BaconShop_HERO_70:# <12>[1453]
	""" Mr. Bigglesworth
	 """
	#
	pass
class TB_BaconShop_HP_080:
	""" Kel'Thuzad's Kitty
	<b>Passive</b>
When a player dies, <b>Discover</b>
a minion from their warband.
It keeps any enchantments."""
class TB_BaconShop_HERO_70_Buddy:# <12>[1453]
	""" Lil' K.T.
	At the start of your turn,get a plain minion fromyour lowest Healthopponent's warband. """
	#
	pass

class TB_BaconShop_HERO_70_Buddy_G:# <12>[1453]
	""" Lil' K.T.
	At the start of your turn,get 2 plain minions fromyour lowest Healthopponent's warband. """
	#
	pass





#43#Mutanus the Devourer
class BG20_HERO_301:
	"""
	"""
class BG20_HERO_301p:
	""" Devour
	Remove a friendly minion.
Spit its stats onto another.
Get 1 Gold."""
class BG20_HERO_301_Buddy:
	"""Nightmare Ectoplasm
	When you 'Devour' this, spit its stats onto 2 extra_minions."""
class BG20_HERO_301_Buddy_G:
	"""Nightmare Ectoplasm
	When you 'Devour' this, spit its stats onto 4 extra_minions."""



#44#N'Zoth
class TB_BaconShop_HERO_93:# <12>[1453]
	""" N'Zoth
	 """
	#
	pass
class TB_BaconShop_HP_105:
	""" Avatar of N'Zoth
	<b>Passive</b>
Start the game with a 2/2
Fish that gains all your
<b>Deathrattles</b> in combat."""
class TB_BaconShop_HERO_93_Buddy:# <12>[1453]
	""" Baby N'Zoth
	[Battlecry:] Make a friendly[Deathrattle] minion Golden. """
	#
	pass

class TB_BaconShop_HERO_93_Buddy_G:# <12>[1453]
	""" Baby N'Zoth
	[Battlecry:] Make all friendly[Deathrattle] minions Golden. """
	#
	pass




#45#Nozdormu
class TB_BaconShop_HERO_57:# <12>[1453]
	""" Nozdormu
	 """
	#
	pass
class TB_BaconShop_HP_063:
	""" Clairvoyance
	<b>Passive</b>
Your first <b>Refresh</b> each
turn costs (0)"""
class TB_BaconShop_HERO_57_Buddy:# <12>[1453]
	""" Chromie
	Minions in Bob's Tavernhave +1/+1 for each time itwas [Refreshed] this turn. """
	#
	pass
class TB_BaconShop_HERO_57_Buddy_e:# <12>[1453]
	""" Flow of Time
	Stats increased by Chromie. """
	#
	pass
class TB_BaconShop_HERO_57_Buddy_G:# <12>[1453]
	""" Chromie
	Minions in Bob's Tavernhave +2/+2 for each time itwas [Refreshed] this turn. """
	#
	pass





#46#Onyxia
class BG22_HERO_305:# <12>[1453]
	""" Onyxia
	 """
	#
	pass
class BG22_HERO_305p:# <12>[1453]
	""" Broodmother
	[Passive][Avenge (4):] Summona 2/1 Whelp. It attacksimmediately. """
	#
	pass
class BG22_HERO_305t:# <12>[1453]
	""" Onyxian Whelp
	 """
	#
	pass
class BG22_HERO_305_Buddy:# <12>[1453]
	""" Many Whelps
	Whenever you summon a Whelp, gain +2/+2 permanently. """
	#
	pass
class BG22_HERO_305_Buddy_e:# <12>[1453]
	""" Swarming
	+2/+2. """
	#
	pass
class BG22_HERO_305_Buddy_G:# <12>[1453]
	""" Many Whelps
	Whenever you summon a Whelp, gain +4/+4 permanently. """
	#
	pass
class BG22_HERO_305_Buddy_Ge:# <12>[1453]
	""" Swarming
	+4/+4. """
	#
	pass








#47#Overlord Saurfang
class BG20_HERO_102:# <12>[1453]
	""" Overlord Saurfang
	 """
	#
	pass
class BG20_HERO_102p:# <10>[1453]
	""" For the Horde!
	Give +@ Attack to the nextminion you buy this turn.<i>(Upgrades each turn!)</i> """
	#
	pass
class BG20_HERO_102pe:# <12>[1453]
	""" Saurfang Player Enchantment
	Give extra Attack to the next minion you buy this turn. """
	#
	pass
class BG20_HERO_102pe2:# <12>[1453]
	""" For the Horde!
	Increased Attack. """
	#
	pass

class BG20_HERO_102pe3:# <12>[1453]
	""" For the Horde!
	Increased Health. """
	#
	pass
class BG20_HERO_102pe_Buddy:# <12>[1453]
	""" Saurfang Player Enchantment (Buddy)
	Give extra Health to the next minion you buy this turn. """
	#
	pass
class BG20_HERO_102_Buddy:# <12>[1453]
	""" Dranosh Saurfang
	'For the Horde!' also grants Health. """
	#
	pass
class BG20_HERO_102_Buddy_G:# <12>[1453]
	""" Dranosh Saurfang
	'For the Horde!' also grants Health twice. """
	#
	pass





#48#Patches the Pirate
class TB_BaconShop_HERO_18:# <12>[1453]
	""" Patches the Pirate
	 """
	#
	pass
class TB_BaconShop_HP_072:
	"""Pirate Parrrrty!
	Get a Pirate. After you buy
a Pirate, your next Hero
Power costs (1) less."""

class TB_BaconShop_HERO_18_Buddy:# <12>[1453]
	"""Tuskarr Raider
	<b>Battlecry:</b> Give a minion +1/+1 for each Pirate you played this game."""
class TB_BaconShop_HERO_18_Buddy_e:# <12>[1453]
	""" Raiding with Tuskarr
	Increased stats. """
	#
	pass
class TB_BaconShop_HERO_18_Buddy_G:
	"""
	<b>Battlecry:</b> Give a minion +2/+2 for each Pirate you played this game."""



#49#Patchwerk
class TB_BaconShop_HERO_34:# <12>[1453]
	""" Patchwerk
	 """
	#
	pass
class TB_BaconShop_HP_035:
	""" All Patched Up
	<b>Passive</b> Start with 55 Health instead of 40."""
class TB_BaconShop_HERO_34_Buddy:# <12>[1453]
	""" Weebomination
	[Battlecry:] Give a minion +1_Health for each Health your hero is missing. """
	#
	pass
class TB_BaconShop_HERO_34_Buddy_e:# <12>[1453]
	""" Patched Up
	Increased Health. """
	#
	pass
class TB_BaconShop_HERO_34_Buddy_G:# <12>[1453]
	""" Weebomination
	[Battlecry:] Give a minion +2_Health for each Health your hero is missing. """
	#
	pass



#50#Pyramad
class TB_BaconShop_HERO_39:# <12>[1453]
	""" Pyramad
	 """
	#
	pass
class TB_BaconShop_HP_040:
	""" Brick by Brick
	Give a random friendly minion +4_Health."""
TB_BaconShop_HP_040e=buff(4,4)
class TB_BaconShop_HERO_39_Buddy:# <12>[1453]
	""" Titanic Guardian
	Whenever a different friendly minion gains Health, this gains it too. """
	#
	pass

class TB_BaconShop_HERO_39_Buddy_e:# <12>[1453]
	""" Fractured, Focused
	Increased Health """
	#
	pass

class TB_BaconShop_HERO_39_Buddy_G:# <12>[1453]
	""" Titanic Guardian
	Whenever a different friendly minion gains Health, this gains twice that amount. """
	#
	pass




#51#Queen Wagtoggle
class TB_BaconShop_HERO_14:# <12>[1453]
	""" Queen Wagtoggle
	 """
	#
	pass
class TB_BaconShop_HP_037a:
	""" Wax Warband
	Give a friendly minion of each minion type +1/+1."""
TB_BaconShop_HP_037te=buff(1,1)
class TB_BaconShop_HERO_14_Buddy:# <12>[1453]
	""" Elder Taggawag
	Whenever you play a minionof a type you don't control,trigger your Hero Power.<i>(@ left this turn.)</i> """
	#
	pass

class TB_BaconShop_HERO_14_Buddy_G:# <12>[1453]
	""" Elder Taggawag
	Whenever you play a minionof a type you don't control,trigger your Hero Power__twice. <i>(@ left this turn.)</i> """
	#
	pass





#52#Ragnaros the Firelord
class TB_BaconShop_HERO_11:# <12>[1453]
	""" Ragnaros the Firelord
	 """
	#
	pass
class TB_BaconShop_HP_087:
	""" DIE, INSECTS!
	<b>Passive</b>
After you kill 25 enemy
minions, get Sulfuras.
<i>(@ left!)</i>"""
class TB_BaconShop_HERO_11_Buddy:# <12>[1453]
	""" Lucifron
	Your end of turn effects trigger twice. """
	#
	pass

class TB_BaconShop_HERO_11_Buddy_e:# <12>[1453]
	""" Dark Magics
	Your end of turn effects trigger twice. """
	#
	pass

class TB_BaconShop_HERO_11_Buddy_G:# <12>[1453]
	""" Lucifron
	Your end of turn effects trigger three times. """
	#
	pass

class TB_BaconShop_HERO_11_Buddy_G_e:# <12>[1453]
	""" Dark Magics
	Your end of turn effects trigger three times. """
	#
	pass



###################################################



