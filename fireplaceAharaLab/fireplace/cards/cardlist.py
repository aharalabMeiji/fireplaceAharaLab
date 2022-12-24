from fireplace.cards import core
from fireplace.config import Config

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
from fireplace.cards.alterac import alterac_demon_hunter, alterac_druid, alterac_hunter, alterac_mage, alterac_neutral, alterac_paladin, alterac_priest, alterac_rogue, alterac_shaman, alterac_warlock, alterac_warrior
Alterac_DemonHunter=alterac_demon_hunter.Alterac_DemonHunter
Alterac_Druid=alterac_druid.Alterac_Druid
Alterac_Hunter=alterac_hunter.Alterac_Hunter
Alterac_Mage=alterac_mage.Alterac_Mage
Alterac_Neutral=alterac_neutral.Alterac_Neutral
Alterac_Paladin=alterac_paladin.Alterac_Paladin
Alterac_Priest=alterac_priest.Alterac_Priest
Alterac_Rogue=alterac_rogue.Alterac_Rogue
Alterac_Shaman=alterac_shaman.Alterac_Shaman
Alterac_Warlock=alterac_warlock.Alterac_Warlock
Alterac_Warrior=alterac_warrior.Alterac_Warrior
Alterac_Cards=[Alterac_DemonHunter, Alterac_Druid, Alterac_Hunter, Alterac_Mage, Alterac_Neutral, Alterac_Paladin, Alterac_Priest, Alterac_Rogue, Alterac_Shaman, Alterac_Warlock, Alterac_Warrior,]

## THE_SUNKEN_CITY = 1658  # Voyage to the Sunken City
from fireplace.cards.sunken import sunken_demon_hunter, sunken_druid, sunken_hunter, sunken_mage, sunken_neutral, sunken_paladin, sunken_priest, sunken_rogue, sunken_shaman, sunken_warlock, sunken_warrior
Sunken_DemonHunter=sunken_demon_hunter.Sunken_DemonHunter
Sunken_Druid=sunken_druid.Sunken_Druid
Sunken_Hunter=sunken_hunter.Sunken_Hunter
Sunken_Mage=sunken_mage.Sunken_Mage
Sunken_Neutral=sunken_neutral.Sunken_Neutral
Sunken_Paladin=sunken_paladin.Sunken_Paladin
Sunken_Priest=sunken_priest.Sunken_Priest
Sunken_Rogue=sunken_rogue.Sunken_Rogue
Sunken_Shaman=sunken_shaman.Sunken_Shaman
Sunken_Warlock=sunken_warlock.Sunken_Warlock
Sunken_Warrior=sunken_warrior.Sunken_Warrior
Sunken_Cards=[Sunken_DemonHunter, Sunken_Druid,Sunken_Hunter,Sunken_Mage,Sunken_Neutral, Sunken_Paladin, Sunken_Priest, Sunken_Rogue, Sunken_Shaman, Sunken_Warlock, Sunken_Warrior]

## REVENDRETH = 1691  # Murder at Castle Nathria
from fireplace.cards.revendreth import rev_neutral,\
	rev_demonhunter, rev_druid, rev_hunter, rev_mage,\
	rev_paladin, rev_priest, rev_rogue, rev_shaman, \
	rev_warlock, rev_warrior
Revendreth_DemonHunter=rev_demonhunter.Rev_DemonHunter
Revendreth_Druid=rev_druid.Rev_Druid
Revendreth_Neutral=rev_neutral.Rev_Neutral
Revendreth_Hunter=rev_hunter.Rev_Hunter
Revendreth_Mage = rev_mage.Rev_Mage
Revendreth_Neutral=rev_neutral.Rev_Neutral
Revendreth_Paladin=rev_paladin.Rev_Paladin
Revendreth_Priest=rev_priest.Rev_Priest
Revendreth_Rogue=rev_rogue.Rev_Rogue
Revendreth_Shaman=rev_shaman.Rev_Shaman
Revendreth_Warlock=rev_warlock.Rev_Warlock
Revendreth_Warrior=rev_warrior.Rev_Warrior
Revendreth_Cards=[Revendreth_DemonHunter,Revendreth_Druid,Revendreth_Hunter,\
	Revendreth_Mage,Revendreth_Neutral,Revendreth_Paladin,\
	Revendreth_Priest,Revendreth_Priest,Revendreth_Rogue,\
	Revendreth_Shaman,Revendreth_Warlock,Revendreth_Warrior]

from fireplace.cards.lichking import lich_deathknight, lich_demonhunter, lich_druid, lich_hunter, lich_mage, lich_neutral,lich_paladin, lich_priest, lich_rogue, lich_shaman, lich_warlock, lich_warrior
from fireplace.cards.arthas import arthas_deathknight
Arthas_Deathknight=arthas_deathknight.Arthas_DeathKnight
Lichking_DeathKnight=lich_deathknight.Lich_DeathKnight
Lichking_DemonHunter=lich_demonhunter.Lich_DemonHunter
Lichking_Druid=lich_druid.Lich_Druid
Lichking_Hunter=lich_hunter.Lich_Hunter
Lichking_Mage=lich_mage.Lich_Mage
Lichking_Neutral=lich_neutral.Lich_Neutral
Lichking_Paladin=lich_paladin.Lich_Paladin
Lichking_Priest=lich_priest.Lich_Priest
Lichking_Rogue=lich_rogue.Lich_Rogue
Lichking_Shaman=lich_shaman.Lich_Shaman
Lichking_Warlock=lich_warlock.Lich_Warlock
Lichking_Warrior=lich_warrior.Lich_Warrior
Lichking_Cards=[Lichking_DeathKnight, Lichking_DemonHunter, Lichking_Druid, Lichking_Hunter, Lichking_Mage, Lichking_Neutral, Lichking_Paladin, Lichking_Priest, Lichking_Rogue, Lichking_Shaman, Lichking_Warlock, Lichking_Warrior, Arthas_Deathknight]

# Hero
from fireplace.cards.hero_dream import hero, dream
Heroes=hero.Heroes
Dream= ['DREAM_01','DREAM_02','DREAM_03','DREAM_04','DREAM_05','DREAM_05e']
Etc = ['SCH_307t']

from fireplace.cards.bigDecks.faceHunter import FaceHunter#faceHunter,bigWarrior, clownDruid
from fireplace.cards.bigDecks.bigWarrior import BigWarrior
from fireplace.cards.bigDecks.clownDruid import ClownDruid
bigDecks=[FaceHunter, BigWarrior, ClownDruid]

#+Classic_Cards\
# VANILLA = 1646
from fireplace.cards.classic import classic_demon_hunter, classic_druid, classic_hunter, classic_mage, classic_neutral
from fireplace.cards.classic import classic_paladin, classic_priest, classic_rogue, classic_shaman, classic_warlock, classic_warrior
Classic_DemonHunter=classic_demon_hunter.Classic_DemonHunter
Classic_Druid=classic_druid.Classic_Druid
Classic_Hunter=classic_hunter.Classic_Hunter
Classic_Mage = classic_mage.Classic_Mage
Classic_Neutral=classic_neutral.Classic_Neutral
Classic_Paladin=classic_paladin.Classic_Paladin
Classic_Priest=classic_priest.Classic_Priest
Classic_Rogue=classic_rogue.Classic_Rogue
Classic_Shaman=classic_shaman.Classic_Shaman
Classic_Warlock=classic_warlock.Classic_Warlock
Classic_Warrior=classic_warrior.Classic_Warrior

Classic_Cards=[Classic_DemonHunter, Classic_Druid, Classic_Hunter, Classic_Mage, Classic_Neutral, Classic_Paladin, Classic_Priest, Classic_Rogue, Classic_Shaman, Classic_Warlock, Classic_Warrior, Heroes, Dream]

if Config.HEARTHSTONE!=4 or Config.CARD_TEST_SET!="VANILLA":
	All=Core_Cards + Lichking_Cards + [Heroes,Dream,Etc]
	###Barrens_Cards + StormWind_Cards + Alterac_Cards + Sunken_Cards + Revendreth_Cards +\
else:
	All=Classic_Cards + bigDecks

