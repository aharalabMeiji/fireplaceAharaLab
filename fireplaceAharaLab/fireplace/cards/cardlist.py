from fireplace.cards import core

# CORE <12><3><4>[1637]
from fireplace.cards.core import core_demon_hunter,core_druid,core_hunter,core_mage,core_neutral,core_paladin,core_priest,core_rogue,core_shaman,core_warrior,core_warlock
Core_DemonHunter=core_demon_hunter.Core_DemonHunter
Core_Druid=core_druid.Core_Druid
Core_Hunter=core_hunter.Core_Hunter
Core_Mage = core_mage.Core_Mage
Core_Neutral=core_neutral.Core_Neutral
Core_Paladin=core_paladin.Core_Paladin
Core_Priest=core_priest.Core_Priest
Core_Rogue=core_rogue.Core_Rogue
Core_Shaman=core_shaman.Core_Shaman
Core_Warlock=core_warlock.Core_Warlock
Core_Warrior=core_warrior.Core_Warrior

Core_Cards=[Core_DemonHunter,Core_Druid,Core_Hunter,Core_Mage,Core_Neutral,Core_Paladin,Core_Priest,Core_Priest,Core_Rogue,Core_Shaman,Core_Warlock,Core_Warrior]

#from fireplace.cards.classic import classic_priest
#Classic_Priest=classic_priest.Classic_Priest
#Classic_Cards=[Classic_Priest]


## DALARAN = 1130  # Rise of Shadows
## fireplace.cards.old_cards.shadows
## hunter,mage,neutral,paladin

## ULDUM = 1158  # Saviours of Uldum
## fireplace.cards.old_cards.saviors
## hunter,mage,neutral,paladin

## DRAGONS = 1347  # Descent of Dragons
## fireplace.cards.old_cards.dragon

## BLACK_TEMPLE = 1414  # Ashes of Outlands
## fireplace.cards.old_cards.aoo
## demon_hunter,druid,hunter,mage, neutral, warrior 

## SCHOLOMANCE = 1443  # Scholomance Academy
## fireplace.cards.old_cards.scholo
## druid,hunter,neutral,mage,paladin,warrior


## DARKMOON_FAIRE = 1466  # Madness at the Darkmoon Faire
## fireplace.cards.old_cards.darkmoon
## druid,hunter,mage,neutral,warrior

# THE_BARRENS = 1525  # Forged in the Barrens
from fireplace.cards.barrens import barrens_demon_hunter, barrens_druid, barrens_hunter, barrens_mage, barrens_neutral, barrens_paladin, barrens_priest, barrens_rogue, barrens_shaman, barrens_warlock, barrens_warrior
Barrens_DemonHunter=barrens_demon_hunter.Barrens_DemonHunter
Barrens_Druid=barrens_druid.Barrens_Druid
Barrens_Hunter=barrens_hunter.Barrens_Hunter
Barrens_Mage=barrens_mage.Barrens_Mage
Barrens_Neutral = barrens_neutral.Barrens_Neutral
Barrens_Warrior=barrens_warrior.Barrens_Warrior
Barrens_Paladin=barrens_paladin.Barrens_Paladin
Barrens_Priest=barrens_priest.Barrens_Priest
Barrens_Rogue=barrens_rogue.Barrens_Rogue
Barrens_Shaman = barrens_shaman.Barrens_Shaman
Barrens_Warlock = barrens_warlock.Barrens_Warlock
Barrens_Cards=[Barrens_DemonHunter, Barrens_Druid,Barrens_Hunter,Barrens_Mage,Barrens_Neutral, Barrens_Paladin, Barrens_Priest, Barrens_Rogue, Barrens_Shaman, Barrens_Warlock, Barrens_Warrior]

## STORMWIND = 1578  # United in Stormwind
from fireplace.cards.stormwind import stormwind_demon_hunter, stormwind_druid, stormwind_hunter, stormwind_mage, stormwind_neutral, stormwind_paladin, stormwind_priest, stormwind_rogue, stormwind_shaman, stormwind_warlock, stormwind_warrior
StormWind_Druid=stormwind_druid.StormWind_Druid
StormWind_Hunter=stormwind_hunter.StormWind_Hunter
StormWind_Mage=stormwind_mage.StormWind_Mage
StormWind_Neutral = stormwind_neutral.StormWind_Neutral
StormWind_DemonHunter=stormwind_demon_hunter.StormWind_DemonHunter
StormWind_Paladin=stormwind_paladin.StormWind_Paladin
StormWind_Priest=stormwind_priest.StormWind_Priest
StormWind_Rogue=stormwind_rogue.StormWind_Rogue
StormWind_Shaman=stormwind_shaman.StormWind_Shaman
StormWind_Warlock=stormwind_warlock.StormWind_Warlock
StormWind_Warrior=stormwind_warrior.StormWind_Warrior
StormWind_Cards=[StormWind_DemonHunter, StormWind_Druid,StormWind_Hunter,StormWind_Mage,StormWind_Neutral, StormWind_Paladin, StormWind_Priest, StormWind_Rogue, StormWind_Shaman, StormWind_Warlock, StormWind_Warrior]

## ALTERAC_VALLEY = 1626  # Fractured in Alterac Valley
from fireplace.cards.alterac import alterac_druid, alterac_hunter, alterac_mage, alterac_neutral, alterac_paladin, alterac_warrior
Alterac_Druid=alterac_druid.Alterac_Druid
Alterac_Hunter=alterac_hunter.Alterac_Hunter
Alterac_Mage=alterac_mage.Alterac_Mage
Alterac_Neutral = alterac_neutral.Alterac_Neutral
Alterac_Warrior=alterac_warrior.Alterac_Warrior
#Alterac_Demonhunter=
Alterac_Paladin=alterac_paladin.Alterac_Paladin
#Alterac_Priest=
#Alterac_Rogue=
#Alterac_Shaman =
#Alterac_Warlock=
Alterac_Cards=[Alterac_Druid,Alterac_Hunter,Alterac_Mage,Alterac_Neutral, Alterac_Paladin, Alterac_Warrior,]

## THE_SUNKEN_CITY = 1658  # Voyage to the Sunken City
from fireplace.cards.sunken import sunken_druid,sunken_hunter,sunken_mage,sunken_neutral, sunken_paladin, sunken_warrior
Sunken_Druid=sunken_druid.Sunken_Druid
Sunken_Hunter=sunken_hunter.Sunken_Hunter
Sunken_Mage=sunken_mage.Sunken_Mage
Sunken_Neutral=sunken_neutral.Sunken_Neutral
Sunken_Warrior=sunken_warrior.Sunken_Warrior
#Sunken_Demonhunter=
Sunken_Paladin=sunken_paladin.Sunken_Paladin
#Sunken_Priest=
#Sunken_Rogue=
#Sunken_Shaman =
#Sunken_Warlock=
Sunken_Cards=[Sunken_Druid,Sunken_Hunter,Sunken_Mage,Sunken_Neutral, Sunken_Paladin, Sunken_Warrior]

## REVENDRETH = 1691  # Murder at Castle Nathria
# Hero
Heroes=[
	'HERO_01',
	'HERO_01bp','HERO_01bp2',#Armor Up!
	'HERO_02',
	'HERO_02bp','HERO_02bp2',#Totemic Call
	"CS2_050", "CS2_051", "CS2_052", "NEW1_009",
	'HERO_03',
	'HERO_03bp','HERO_03bp2',#Dagger Mastery
	'AT_034','AT_034e','CS2_082','AT_132_ROGUEt',
	'HERO_04',
	'HERO_04bp','HERO_04bp2','CS2_101t',#steady shot
	'HERO_05',
	'HERO_05bp','HERO_05bp2','HERO_05dbp',#Reinforce 
	'HERO_06',	
	'HERO_06bp','CS2_017o','HERO_06bp2','AT_132_DRUIDe',#Shapeshift
	'HERO_07',
	'HERO_07bp','HERO_07bp2',#Life Tap
	'HERO_08',
	'HERO_08bp','HERO_08bp2',# Fireblast(<4>[1635])
	'HERO_09',
	'HERO_09bp','HERO_09bp2',# Lesser Heal
	'HERO_10',
	'HERO_10bp','HERO_10bpe','HERO_10bp2','HERO_10pe2',##Demon Claws
	]
Dream= ['DREAM_01','DREAM_02','DREAM_03','DREAM_04','DREAM_05','DREAM_05e']
Etc = ['SCH_307t']
faceHunter =[#old faceHunter
		'DRG_252','DRG_256','DRG_253','ULD_152',# wild
		'CORE_EX1_610','EX1_536','EX1_536e','EX1_539',# wild
		]
bigWarrior = [
	'CORE_EX1_169','SW_023','SCH_237','SCH_237e','CORE_EX1_410',
	'BT_124','BT_124e','DMF_522','BT_117','SW_094','BT_781',
	'BAR_845','BAR_844','YOP_005','YOP_005t','CORE_EX1_407',
	'SW_021','SCH_533','SW_024','SW_024e','SCH_337','SCH_337t',
	'SW_068','SCH_621',
	]
clownDruid = [
	#'SCH_427','SCH_333','SCH_333e','SCH_610','SCH_616','SCH_609','SCH_609e',
	#'DMF_075','DMF_075a','DMF_075a2',
	#'BT_130',
	#'CORE_EX1_169','CORE_CS2_013','CS2_013t',
	#'BAR_042',	
]
All=Core_Cards + Barrens_Cards + StormWind_Cards + Alterac_Cards + Sunken_Cards + [Heroes,Dream,Etc,faceHunter,bigWarrior,clownDruid]\
	
#+Classic_Cards\
# VANILLA = 1646
#from fireplace.cards.classic import classic_druid, classic_neutral
#from fireplace.cards.core import classic_demon_hunter, classic_hunter, classic_mage, classic_paladin, classic_priest, classic_rogue, classic_shaman, classic_warrior, classic_warlock
#Classic_DemonHunter=classic_demon_hunter.Classic_DemonHunter
#Classic_Druid=classic_druid.Classic_Druid
#Classic_Hunter=classic_hunter.Classic_Hunter
#Classic_Mage = classic_mage.Classic_Mage
#Classic_Neutral=classic_neutral.Classic_Neutral
#Classic_Paladin=classic_paladin.Classic_Paladin
#Classic_Priest=classic_priest.Classic_Priest
#Classic_Rogue=classic_rogue.Classic_Rogue
#Classic_Shaman=classic_shaman.Classic_Shaman
#Classic_Warlock=classic_warlock.Classic_Warlock
#Classic_Warrior=classic_warrior.Classic_Warrior

#Classic_Cards=[Classic_DemonHunter,Classic_Druid,Classic_Hunter,Classic_Mage,Classic_Neutral,Classic_Paladin,Classic_Priest,Classic_Priest,Classic_Rogue,Classic_Shaman,Classic_Warlock,Classic_Warrior]


