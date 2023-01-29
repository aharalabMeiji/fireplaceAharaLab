from ..utils import *



BG25__Risen_Rider=True
BG25__Rot_Hide_Gnoll=True
BG25__Eternal_Knight=True
BG25__Nerubian_Deathswarmer=True
BG25__Scarlet_Skull=True
BG25__Corpse_Refiner=True# 2/2/3 undead ## new 25.2.2

BG25__Ghoul_of_the_Feast=True # 3
BG25__Jelly_Belly=True
BG25__Lich_Doctor=True
BG25__Anubarak_Nerubian_King=True
BG25__Handless_Forsaken=True
BG25__Possessive_Banshee=True
BG25__Hungering_Abomination=True
BG24__Sinrunner_Blanchy=True
BG25__Soulsplitter=True
BG25__Colossus_of_the_Sun=True
BG25__Eternal_Summoner=True
BG25__Sister_Deathwhisper=True

BG_Minion_Undead = []
BG_PoolSet_Undead=[ [],[],[],[],[],[],[]]
BG_Undead_Gold={}


#Risen Rider 1/2/1/Undead	Reborn, Taunt
if BG25__Risen_Rider:# 
	BG_Minion_Undead+=['BG25_001']
	BG_Minion_Undead+=['BG25_001_G']
class BG25_001:# (minion)
	""" Risen Rider
	<b>Taunt</b> <b>Reborn</b> """
	#
	pass

class BG25_001_G:# (minion)
	""" Risen Rider
	<b>Taunt</b> <b>Reborn</b> """
	#
	pass

#Rot Hide Gnoll 1/1/4/Undead	-
if BG25__Rot_Hide_Gnoll:# 
	BG_Minion_Undead+=['BG25_013']
	BG_Minion_Undead+=['BG25_013_G']
class BG25_013:# (minion)
	""" Rot Hide Gnoll
	Has +1 Attack for each friendly minion that died this combat. """
	#
	pass

class BG25_013_G:# (minion)
	""" Rot Hide Gnoll
	Has +2 Attack for each friendly minion that died this combat. """
	#
	pass

#Eternal Knight 2/3/1/Undead	-
if BG25__Eternal_Knight:# 
	BG25_+=['BG25_008']
	BG25_+=['BG25_008_e']
	BG25_+=['BG25_008_G']
	BG25_+=['BG25_008pe']
class BG25_008:# (minion)
	""" Eternal Knight
	Has +1/+1 for each friendly Eternal Knight that died this __game <i>(wherever this is)</i>. """
	#
	pass

class BG25_008_e:# (enchantment)
	""" Eternal Legion
	+@/+@. """
	#
	pass

class BG25_008_G:# (minion)
	""" Eternal Knight
	Has +2/+2 for each friendly Eternal Knight that died this __game <i>(wherever this is)</i>. """
	#
	pass
class BG25_008pe:# (enchantment)
	""" Eternal Knight Player Enchant
	Counts the number of Eternal Knights that died. """
	#
	pass

#Nerubian Deathswarmer 2/1/3/Undead	Battlecry
if BG25__Nerubian_Deathswarmer:# 
	BG25_+=['BG25_011']
	BG25_+=['BG25_011_G']
	BG25_+=['BG25_011e2']
	BG25_+=['BG25_011pe']
class BG25_011:# (minion)
	""" Nerubian Deathswarmer
	<b>Battlecry:</b> Give your Undead +1 Attack for the rest of the game <i>(wherever they are)</i>. """
	#
	pass

class BG25_011_G:# (minion)
	""" Nerubian Deathswarmer
	<b>Battlecry:</b> Give your Undead +2 Attack for the rest of the game <i>(wherever they are)</i>. """
	#
	pass

class BG25_011e2:# (enchantment)
	""" Undead Army
	+@ Attack """
	#
	pass

class BG25_011pe:# (enchantment)
	""" Undead Bonus Attack Player Enchant [DNT]
	Give Attack to Undead. """
	#
	pass

#Scarlet Skull 2/1/2/Undead	Deathrattle, Reborn
if BG25__Scarlet_Skull:# 
	BG25_+=['BG25_022']
	BG25_+=['BG25_022_G']
	BG25_+=['BG25_022_Ge']
	BG25_+=['BG25_022e']
class BG25_022:# (minion)
	""" Scarlet Skull
	<b>Reborn</b> <b>Deathrattle:</b> Give a friendly Undead +1/+2. """
	#
	pass

class BG25_022_G:# (minion)
	""" Scarlet Skull
	<b>Reborn</b> <b>Deathrattle:</b> Give a friendly Undead +2/+4. """
	#
	pass

class BG25_022_Ge:# (enchantment)
	""" Scarlet Fear
	+2/+4. """
	#
	pass

class BG25_022e:# (enchantment)
	""" Scarlet Fear
	+1/+2. """
	#
	pass


if BG25__Corpse_Refiner:# 2/2/3 undead ## new 25.2.2
	BG25_+=['BG25_033']
class BG25_033:# (minion)
	""" Corpse Refiner
	<b>Avenge (4):</b> This minion sells for 1 more Gold.@<b>Avenge (4):</b> This minion sells for 1 more Gold. __<i>(Sells for {0} extra Gold!)</i> """
	#
	pass

	BG25_+=['BG25_033_G']
class BG25_033_G:# (minion)
	""" Corpse Refiner
	<b>Avenge (4):</b> This minion sells for 2 more Gold.@<b>Avenge (4):</b> This minion sells for 2 more Gold. __<i>(Sells for {0} extra Gold!)</i> """
	#
	pass

###### tavern tier 3

#Ghoul of the Feast 3/2/4/Undead	Avenge (X)
if BG25__Ghoul_of_the_Feast:# 
	BG25_+=['BG25_002']
class BG25_002:# (minion)
	""" Ghoul of the Feast
	<b>Avenge (1):</b> Give a friendly minion of each minion type +3 Attack. """
	#
	pass

	BG25_+=['BG25_002_G']
class BG25_002_G:# (minion)
	""" Ghoul of the Feast
	<b>Avenge (1):</b> Give a friendly minion of each minion type +6 Attack. """
	#
	pass

	BG25_+=['BG25_002_Ge']
class BG25_002_Ge:# (enchantment)
	""" Tasty Treat
	+6 Attack. """
	#
	pass

	BG25_+=['BG25_002e']
class BG25_002e:# (enchantment)
	""" Tasty Treat
	+3 Attack. """
	#
	pass

#Jelly Belly 3/3/5/Undead	Reborn
if BG25__Jelly_Belly:# 
	BG25_+=['BG25_005']
class BG25_005:# (minion)
	""" Jelly Belly
	After a friendly minion is <b>Reborn</b>, gain +3/+3. """
	#
	pass

	BG25_+=['BG25_005_G']
class BG25_005_G:# (minion)
	""" Jelly Belly
	After a friendly minion is <b>Reborn</b>, gain +6/+6. """
	#
	pass

	BG25_+=['BG25_005_Ge']
class BG25_005_Ge:# (enchantment)
	""" Jellied
	+6/+6 """
	#
	pass

	BG25_+=['BG25_005e']
class BG25_005e:# (enchantment)
	""" Jellied
	+3/+3 """
	#
	pass

#Lich Doctor 3/3/2/Undead	Taunt
if BG25__Lich_Doctor:# 
	BG25_+=['BG25_006']
class BG25_006:# (minion)
	""" Lich Doctor
	<b>Taunt</b>. At the start of your turn, give your minions that _died last combat +1/+1. """
	#
	pass

	BG25_+=['BG25_006_G']
class BG25_006_G:# (minion)
	""" Lich Doctor
	<b>Taunt</b>. At the start of your turn, give your minions that _died last combat +2/+2. """
	#
	pass

	BG25_+=['BG25_006_Ge']
class BG25_006_Ge:# (enchantment)
	""" Just What Was Ordered
	+2/+2 """
	#
	pass

	BG25_+=['BG25_006e']
class BG25_006e:# (enchantment)
	""" Just What Was Ordered
	+1/+1 """
	#
	pass

#Anub'arak, Nerubian King 4/4/3/Undead	Deathrattle
if BG25__Anubarak_Nerubian_King:# 
	BG25_+=['BG25_007']
class BG25_007:# (minion)
	""" Anub'arak, Nerubian King
	<b>Deathrattle:</b> Your Undead have +2 Attack for the rest of the game <i>(wherever they are)</i>. """
	#
	pass

	BG25_+=['BG25_007_G']
class BG25_007_G:# (minion)
	""" Anub'arak, Nerubian King
	<b>Deathrattle:</b> Your Undead have +4 Attack for the rest of the game <i>(wherever they are)</i>. """
	#
	pass


#Handless Forsaken 4/2/3/Undead	Deathrattle, Reborn
if BG25__Handless_Forsaken:# 
	BG25_+=['BG25_010']
class BG25_010:# (minion)
	""" Handless Forsaken
	<b>Deathrattle:</b> Summon a 2/2 Hand with <b>Reborn</b>. """
	#
	pass

	BG25_+=['BG25_010_G']
class BG25_010_G:# (minion)
	""" Handless Forsaken
	<b>Deathrattle:</b> Summon a 4/4 Hand with <b>Reborn</b>. """
	#
	pass

	BG25_+=['BG25_010_Gt']
class BG25_010_Gt:# (minion)
	""" Helping Hand
	<b>Reborn</b> """
	#
	pass

	BG25_+=['BG25_010t']
class BG25_010t:# (minion)
	""" Helping Hand
	<b>Reborn</b> """
	#
	pass


#Possessive Banshee 4/2/7/Undead	Battlecry
if BG25__Possessive_Banshee:# 
	BG25_+=['BG25_004']
class BG25_004:# (minion)
	""" Possessive Banshee
	<b>Battlecry:</b> Give an Undead +2/+7. """
	#
	pass

	BG25_+=['BG25_004_G']
class BG25_004_G:# (minion)
	""" Possessive Banshee
	<b>Battlecry:</b> Give an Undead +4/+14. """
	#
	pass

	BG25_+=['BG25_004_Ge']
class BG25_004_Ge:# (enchantment)
	""" MINE!!!
	+4/+14 """
	#
	pass

	BG25_+=['BG25_004e']
class BG25_004e:# (enchantment)
	""" MINE!!!
	+2/+7 """
	#
	pass

#Hungering Abomination 5/3/4/Undead	Avenge (X)
if BG25__Hungering_Abomination:# 
	BG25_+=['BG25_014']
class BG25_014:# (minion)
	""" Hungering Abomination
	<b>Avenge (1):</b> Gain +1/+1 permanently. """
	#
	pass

	BG25_+=['BG25_014_G']
class BG25_014_G:# (minion)
	""" Hungering Abomination
	<b>Avenge (1):</b> Gain +2/+2 permanently. """
	#
	pass

	BG25_+=['BG25_014_Ge']
class BG25_014_Ge:# (enchantment)
	""" OM NOM NOM
	+2/+2 """
	#
	pass

	BG25_+=['BG25_014e']
class BG25_014e:# (enchantment)
	""" OM NOM NOM
	+1/+1 """
	#
	pass

#Sinrunner Blanchy 5/3/3/Beast, Undead	Reborn
#BG24_005
if BG24__Sinrunner_Blanchy:
	BG_Minion_Undead += []
class BG24_005:
	""" Sinrunner Branky (5/4/4)
	Reborn """
	##< when reborn, effects and max_health will be preserved.>
	pass

class BG24_005_G:
	""" KIGA-reshimono
	Avenge (1) Get 1/1 permanently"""
		events = Death(FRIENDLY).on(Avenge(SELF, 1,[BuffPermanently(SELF, 'BG_UND_534e')]))
BG24_005e=buff(1,1)


#Soulsplitter 5/5/2/Undead	Reborn, Start of Combat
if BG25__Soulsplitter:# 
	BG25_+=['BG25_023']
class BG25_023:# (minion)
	""" Soulsplitter
	<b>Reborn</b> <b>Start of Combat:</b> Give a ___friendly Undead <b>Reborn</b>. """
	#
	pass

	BG25_+=['BG25_023_G']
class BG25_023_G:# (minion)
	""" Soulsplitter
	<b>Reborn</b> <b>Start of Combat:</b> Give 2 ___friendly Undead <b>Reborn</b>. """
	#
	pass

	BG25_+=['BG25_023e']
class BG25_023e:# (enchantment)
	""" Soul Doubled
	<b>Reborn</b> """
	#
	pass


#Colossus of the Sun 6/6/6/Undead	Divine Shield, Reborn
if BG25__Colossus_of_the_Sun:# 
	BG25_+=['BG25_050']
class BG25_050:# (minion)
	""" Colossus of the Sun
	<b>Divine Shield</b> <b>Reborn</b> """
	#
	pass

	BG25_+=['BG25_050_G']
class BG25_050_G:# (minion)
	""" Colossus of the Sun
	<b>Divine Shield</b> <b>Reborn</b> """
	#
	pass


#Eternal Summoner 6/6/1/Undead	Deathrattle, Reborn
if BG25__Eternal_Summoner:# 
	BG25_+=['BG25_009']
class BG25_009:# (minion)
	""" Eternal Summoner
	<b>Deathrattle:</b> Summon 2 Eternal Knights. """
	#
	pass

	BG25_+=['BG25_009_G']
class BG25_009_G:# (minion)
	""" Eternal Summoner
	<b>Deathrattle:</b> Summon 4 Eternal Knights. """
	#
	pass


#Sister Deathwhisper 6/4/9/Undead	Reborn
if BG25__Sister_Deathwhisper:# 
	BG25_+=['BG25_020']
class BG25_020:# (minion)
	""" Sister Deathwhisper
	After a friendly minion is <b>Reborn</b>, give your Undead +1/+3 permanently. """
	#
	pass

	BG25_+=['BG25_020_G']
class BG25_020_G:# (minion)
	""" Sister Deathwhisper
	After a friendly minion is <b>Reborn</b>, give your Undead +2/+6  permanently. """
	#
	pass

	BG25_+=['BG25_020_Ge']
class BG25_020_Ge:# (enchantment)
	""" Dark Whispers
	+2/+6 """
	#
	pass

	BG25_+=['BG25_020e']
class BG25_020e:# (enchantment)
	""" Dark Whispers
	+1/+3 """
	#
	pass


##Rekka no skyfin <marloc+undead> (2/1/3) 
if BG_:
	BG_Minion_Undead += ['BG_CFM_315','BG_CFM_315t','TB_BaconUps_093','TB_BaconUps_093t',]#Alleycat
	BG_PoolSet_Undead[2].append('BG_CFM_315')
	BG_Undead_Gold['BG_CFM_315']='TB_BaconUps_093'
class BG_UND_213:#   
	""" Rekka no skyfin <undead> (1/1)
	."""
	events = BG_Play(CONTROLLER, MINION+BATTLECRY).on(Buff(SELF, 'BG_UND_213e'))
	pass
BG_UND_213e=buff(1,1)
class TB_BaconUps_UND_213:#
	""" Alleycat <beast> (2//2/6)
	"""
	events = BG_Play(CONTROLLER, MINION+BATTLECRY).on(Buff(SELF, 'TB_BaconUps_UND_213'))
	pass
TB_BaconUps_UND_213=buff(2,2)



class BG_UND_666:
	"""
	divine shield, reborn"""
	pass
