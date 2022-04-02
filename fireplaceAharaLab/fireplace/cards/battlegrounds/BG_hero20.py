from ..utils import *

#BattleGrounds_Hero=['BG20_HERO_100','BG20_HERO_100p','BG20_HERO_100p_e2',
#'BG20_HERO_101','BG20_HERO_101_SKIN_A','BG20_HERO_101_SKIN_B','BG20_HERO_102','BG20_HERO_102_SKIN_A','BG20_HERO_102_SKIN_B','BG20_HERO_102_SKIN_C','BG20_HERO_102_SKIN_D','BG20_HERO_103','BG20_HERO_103_SKIN_A','BG20_HERO_201','BG20_HERO_201_SKIN_A','BG20_HERO_201_SKIN_B','BG20_HERO_201_SKIN_C','BG20_HERO_202','BG20_HERO_202_SKIN_A','BG20_HERO_242','BG20_HERO_242_SKIN_A','BG20_HERO_242_SKIN_B','BG20_HERO_280','BG20_HERO_282','BG20_HERO_283','BG20_HERO_283_SKIN_A','BG20_HERO_301','BG20_HERO_301_SKIN_A','BG20_HERO_666','BG21_HERO_000','BG21_HERO_000_SKIN_A','BG21_HERO_010','BG21_HERO_020','BG21_HERO_030','BG22_HERO_000','BG22_HERO_001','BG22_HERO_002','BG22_HERO_003','BG22_HERO_004','BG22_HERO_201','BG22_HERO_305',]

BattleGrounds_Hero20=[
	'BG20_HERO_100','BG20_HERO_100p','BG20_HERO_100p_e2','BG20_HERO_100_Buddy','BG20_HERO_100_Buddy_e','BG20_HERO_100_Buddy_G','BG20_HERO_100_Buddy_Ge',#Rokara
	'BG20_HERO_101','BG20_HERO_101p','BG20_HERO_101pe2','BG20_HERO_101_Buddy','BG20_HERO_101_Buddy_e','BG20_HERO_101_Buddy_G','BG20_HERO_101_Buddy_Ge',#Xyrella
	'BG20_HERO_102','BG20_HERO_102p','BG20_HERO_102pe','BG20_HERO_102pe2','BG20_HERO_102pe3','BG20_HERO_102_Buddy','BG20_HERO_102_Buddy_G','BG20_HERO_102pe_Buddy',#Overlord Saurfang
	'BG20_HERO_103','BG20_HERO_103p',#Death Speaker Blackthorn
	'BG20_HERO_201','BG20_HERO_201e','BG20_HERO_201e2','BG20_HERO_201e3','BG20_HERO_201p','BG20_HERO_201p2','BG20_HERO_201p2e','BG20_HERO_201p3e','BG20_HERO_201_Buddy','BG20_HERO_201_Buddy_e','BG20_HERO_201_Buddy_e2','BG20_HERO_201_Buddy_G',#Vol'jin
	'BG20_HERO_202','BG20_HERO_202p','BG20_HERO_202pe','BG20_HERO_202pt','BG20_HERO_202_Buddy','BG20_HERO_202_Buddy_G',#Master Nguyen
	]
BG20_Heroes =[
	'BG20_HERO_100','BG20_HERO_101','BG20_HERO_102','BG20_HERO_103','BG20_HERO_201','BG20_HERO_202',
	]

#### 100 ####
class BG20_HERO_100:# <10>[1453]
	""" Rokara
	 """
	pass
class BG20_HERO_100p:# <10>[1453]
	""" Glory of Combat
	&lt;b&gt;Passive.&lt;/b&gt; After a friendly minion kills an enemy, give it +1 Attack permanently. """
	events =  Attack(FRIENDLY_MINIONS, ENEMY_CHARACTERS).on(Buff(Attack.ATTACKER, 'BG20_HERO_100p_e2'))
	pass
BG20_HERO_100p_e2=buff(1,0)
class BG20_HERO_100_Buddy:# <12>[1453]
	""" Icesnarl the Mighty
	After a friendly minionkills an enemy, gain+1 Health permanently. """
	events = Attack(FRIENDLY_MINIONS, ENEMY_CHARACTERS).on(Buff(SELF, 'BG20_HERO_100_Buddy_e'))
	pass
BG20_HERO_100_Buddy_e=buff(0,1)# <12>[1453]
class BG20_HERO_100_Buddy_G:# <12>[1453]
	""" Icesnarl the Mighty
	After a friendly minionkills an enemy, gain+2 Health permanently. """
	events = Attack(FRIENDLY_MINIONS, ENEMY_CHARACTERS).on(Buff(SELF, 'BG20_HERO_100_Buddy_Ge'))
	pass
BG20_HERO_100_Buddy_Ge=buff(0,2)# <12>[1453]

#### 101 ####
class BG20_HERO_101:# <12>[1453]
	""" Xyrella
	 """
	pass
class BG20_HERO_101p:
	""" See the Light
	Choose a minion in Bob's Tavern to add to your hand. Set its stats to 2."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_ENEMY_TARGET:0,PlayReq.REQ_MINION_TARGET:0,}
	play = Buy(CONTROLLER, TARGET).on(Buff(Buy.CARD,'BG20_HERO_101pe2'))
class BG20_HERO_101pe2:
	max_health = lambda self, i : 2
	atk = lambda self, i : 2
class BG20_HERO_101_Buddy_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self,source,target,buff):
		if isinstance(target,PlayableCard):
			if target.health==target.atk:
				Buff(source,buff).trigger(source)
class BG20_HERO_101_Buddy:#
	""" Baby Elekk
	After you play a minion with Attack equal to its Health, gain +2/+2. """
	events = Play(CONTROLLER, FRIENDLY_MINIONS).on(BG20_HERO_101_Buddy_Action(Play.CARD, 'BG20_HERO_101_Buddy_e'))
	pass
BG20_HERO_101_Buddy_e=buff(2,2)
class BG20_HERO_101_Buddy_G:
	""" 
	After you play a minion with Attack equal to its Health, gain +4/+4.""" 
	events = Play(CONTROLLER, FRIENDLY_MINIONS).on(BG20_HERO_101_Buddy_Action(Play.CARD, 'BG20_HERO_101_Buddy_Ge'))
	pass
BG20_HERO_101_Buddy_Ge=buff(4,4)

#### 102 ####
class BG20_HERO_102:# <12>[1453]
	""" Overlord Saurfang
	 """
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

#### 103 ####
class BG20_HERO_103:# <12>[1453]
	""" Death Speaker Blackthorn
	 """
	#
	pass
class BG20_HERO_103p:# <12>[1453]
	""" Bloodbound
	[Passive]After you upgradeBob's Tavern, gain2 [Blood Gems]. """
	#
	pass

#### 201 ####
class BG20_HERO_201:# <12>[1453]
	""" Vol'jin
	 """
	#
	pass
class BG20_HERO_201e:# <12>[1453]
	""" Modified Attack
	Attack is increased or decreased. """
	#
	pass
class BG20_HERO_201e2:# <12>[1453]
	""" Modified Health
	Health is increased or decreased. """
	#
	pass
class BG20_HERO_201e3:# <12>[1453]
	""" Stats Set
	 """
	#
	pass
class BG20_HERO_201p:# <12>[1453]
	""" Spirit Swap
	Choose two minions. Swap their stats. """
	#
	pass
class BG20_HERO_201p2:# <12>[1453]
	""" Spirit Swap
	Choose a minion. Swap its stats with {0}. """
	#
	pass
class BG20_HERO_201p2e:# <12>[1453]
	""" Spirit Swapped
	Stats swapped with another minion. """
	#
	pass
class BG20_HERO_201p3e:# <12>[1453]
	""" Marked for Swap
	Stats can be swapped. """
	#
	pass
class BG20_HERO_201_Buddy:# <12>[1453]
	""" Master Gadrin
	At the end of your turn,the minion to the leftof this copies thisminion's Attack. """
	#
	pass
class BG20_HERO_201_Buddy_e:# <12>[1453]
	""" Blessed Hands
	Copied Gadrin's Attack. """
	#
	pass
class BG20_HERO_201_Buddy_e2:# <12>[1453]
	""" Attack Set
	 """
	#
	pass
class BG20_HERO_201_Buddy_G:# <12>[1453]
	""" Master Gadrin
	At the end of your turn,adjacent minions copythis minion's Attack. """
	#
	pass

#### 202 ####
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

#### 242 ####
class BG20_HERO_242:# <2>[1453]
	""" Guff Runetotem
	 """
	#
	pass

class BG20_HERO_242_SKIN_A:# <2>[1453]
	""" Stormwind Guard Guff
	 """
	#
	pass

class BG20_HERO_242_SKIN_B:# <2>[1453]
	""" Oasis Guff
	 """
	#
	pass

class BG20_HERO_242p:# <2>[1453]
	""" Natural Balance
	Give a friendly minion ofeach Tavern Tier +1/+1. """
	#
	pass

class BG20_HERO_242pe:# <12>[1453]
	""" Guff's Buff
	+1/+1. """
	#
	pass

class BG20_HERO_280:# <14>[1453]
	""" Kurtrus Ashfallen
	 """
	#
	pass

class BG20_HERO_280_Buddy:# <12>[1453]
	""" Living Nightmare
	After you buy a minion,minions in Bob's Tavernhave +1/+1 this turn. """
	#
	pass

class BG20_HERO_280_Buddy_G:# <12>[1453]
	""" Living Nightmare
	After you buy a minion,minions in Bob's Tavernhave +2/+2 this turn. """
	#
	pass

class BG20_HERO_280_Buddye:# <12>[1453]
	""" Living Nightmare Player Enchant
	Increased stats. """
	#
	pass

class BG20_HERO_280_Buddye2:# <12>[1453]
	""" Nightshot
	Increased stats. """
	#
	pass

class BG20_HERO_280e:# <12>[1453]
	""" Kurtrus Watcher
	 """
	#
	pass

class BG20_HERO_280p:# <14>[1453]
	""" Final Showdown
	[Passive]Buy 3 minions in 1 turnto give them +2/+2 and_progress this. <i>(@ left!)</i> """
	#
	pass

class BG20_HERO_280p2:# <14>[1453]
	""" Gain Momentum
	[Passive.] Buy 4 minions in1 turn to give your handand board +2/+2 and_progress this. <i>(@ left!)</i> """
	#
	pass

class BG20_HERO_280p2e:# <12>[1453]
	""" Momentum
	+2/+2. """
	#
	pass

class BG20_HERO_280p2e2:# <12>[1453]
	""" Marked for Showdown
	Will be buffed by Final Showdown. """
	#
	pass

class BG20_HERO_280p3:# <14>[1453]
	""" Close the Portal
	[Passive.] Buy 5 minions in1 turn to give ALL yourminions this game +2/+2__and complete this. <i>({0} left!)</i>@[Passive.] Buy 5 minions in1 turn to give ALL yourminions this game +2/+2.<i>(Complete!)</i> """
	#
	pass

class BG20_HERO_280p3e2:# <12>[1453]
	""" Portal Closure
	+2/+2 """
	#
	pass

class BG20_HERO_280pe:# <12>[1453]
	""" Showdown Preparation
	+2/+2. """
	#
	pass

class BG20_HERO_282:# <9>[1453]
	""" Tamsin Roame
	 """
	#
	pass

class BG20_HERO_282_Buddy:# <12>[1453]
	""" Monstrosity
	After a friendly minion dies, gain its Attack. """
	#
	pass

class BG20_HERO_282_Buddy_G:# <12>[1453]
	""" Monstrosity
	After a friendly minion dies, gain its Attack twice. """
	#
	pass

class BG20_HERO_282_Buddye:# <12>[1453]
	""" Consumed
	Increased Attack. """
	#
	pass

class BG20_HERO_282p:# <9>[1453]
	""" Fragrant Phylactery
	[Start of Combat:]Destroy your lowest Healthminion. Give its stats_to four friendly minions. """
	#
	pass

class BG20_HERO_282pe:# <12>[1453]
	""" Fragrant
	Increased stats. """
	#
	pass

class BG20_HERO_283:# <12>[1453]
	""" Galewing
	 """
	#
	pass

class BG20_HERO_283_Buddy:# <12>[1453]
	""" Flight Trainer
	At the end of your turn, progress your flightpath by_1 turn. """
	#
	pass

class BG20_HERO_283_Buddy_e:# <12>[1453]
	""" Flight Trainer
	1 turn less. """
	#
	pass

class BG20_HERO_283_Buddy_G:# <12>[1453]
	""" Flight Trainer
	At the end of your turn, progress your flightpath by_2 turns. """
	#
	pass

class BG20_HERO_283_Buddy_G_e:# <12>[1453]
	""" Flight Trainer
	2 turns less. """
	#
	pass

class BG20_HERO_283_SKIN_A:# <12>[1453]
	""" Starblast Galewing
	 """
	#
	pass

class BG20_HERO_283p:# <12>[1453]
	""" Dungar's Gryphon
	Choose a flightpath. Complete it to get a bonus! """
	#
	pass

class BG20_HERO_283p_t1:# <12>[1453]
	""" Westfall
	[Passive.] In 1 turn, giveyour left-most minion+2 Attack. <i>(@ left!)</i> """
	#
	pass

class BG20_HERO_283p_t1e:# <12>[1453]
	""" Westfall
	+2 Attack. """
	#
	pass

class BG20_HERO_283p_t2:# <12>[1453]
	""" Ironforge
	[Passive.] In 3 turns,[Discover] a minion of yourTavern Tier. <i>(@ left!)</i> """
	#
	pass

class BG20_HERO_283p_t3:# <12>[1453]
	""" Eastern Plaguelands
	[Passive.] In 5 turns, yournext Tavern Tier upgradecosts (5) less. <i>(@ left!)</i> """
	#
	pass

class BG20_HERO_301:# <12>[1453]
	""" Mutanus the Devourer
	 """
	#
	pass

class BG20_HERO_301_Buddy:# <12>[1453]
	""" Nightmare Ectoplasm
	When you 'Devour' this, spit its stats onto 2 extra_minions. """
	#
	pass

class BG20_HERO_301_Buddy_G:# <12>[1453]
	""" Nightmare Ectoplasm
	When you 'Devour' this, spit its stats onto 4 extra_minions. """
	#
	pass

class BG20_HERO_301_SKIN_A:# <12>[1453]
	""" Stonecrash
	 """
	#
	pass

class BG20_HERO_301p:# <12>[1453]
	""" Devour
	Remove a friendly minion.Spit its stats onto another.Get 1 Gold. """
	#
	pass

class BG20_HERO_301pe:# <12>[1453]
	""" Spat Upon
	Increased Stats """
	#
	pass

class BG20_HERO_666:# <10>[1453]
	""" Diablo
	 """
	#
	pass

class BG20_HERO_666p:# <10>[1453]
	""" Realm of Terror
	[Passive.] Every 4 turns, ALLenemies fight the Lord ofTerror and your warband_for loot. <i>({0} |4(turn, turns) left!)</i>@[Passive.] Every 4 turns, ALLenemies fight the Lord ofTerror and your warband_for loot. <i>(Next combat!)</i> """
	#
	pass

class BG20_HERO_666p_t1a:# <10>[1453]
	""" Sigil of Hell
	[Start of Combat:] Deal 2 damage to 3 random enemy minions. """
	#
	pass

class BG20_HERO_666p_t1b:# <10>[1453]
	""" Magic Sigil of Hell
	[Start of Combat:] Deal 4 damage to 3 random enemy minions. """
	#
	pass

class BG20_HERO_666p_t1c:# <10>[1453]
	""" Rare Sigil of Hell
	[Start of Combat:] Deal 8 damage to 3 random enemy minions. """
	#
	pass

class BG20_HERO_666p_t1d:# <10>[1453]
	""" Unique Sigil of Hell
	[Start of Combat:] Deal 16 damage to 3 random enemy minions. """
	#
	pass

class BG20_HERO_666p_t3_e:# <10>[1453]
	""" Terrifying
	+{0}/+{1} for next combat only. """
	#
	pass

class BG20_HERO_666p_t3a:# <10>[1453]
	""" Claws of Terror
	Give a friendly minion +4/+4 for next combat_only. """
	#
	pass

class BG20_HERO_666p_t3b:# <10>[1453]
	""" Magic Claws of Terror
	Give a friendly minion +8/+8 for next combat_only. """
	#
	pass

class BG20_HERO_666p_t3c:# <10>[1453]
	""" Rare Claws of Terror
	Give a friendly minion +16/+16 for next combat only. """
	#
	pass

class BG20_HERO_666p_t3d:# <10>[1453]
	""" Unique Claws of Terror
	Double a friendly minion'sAttack and Healthfor next combat only. """
	#
	pass

class BG20_HERO_666p_t4a:# <10>[1453]
	""" Magma Horns
	Give a friendly minion [Windfury] for next combat only. """
	#
	pass

class BG20_HERO_666p_t4a_e:# <10>[1453]
	""" Furious Horns
	[Windfury] for next combat only. """
	#
	pass

class BG20_HERO_666p_t4a_e2:# <10>[1453]
	""" Resilient Horns
	[Reborn] for next combat only. """
	#
	pass

class BG20_HERO_666p_t4a_e3:# <10>[1453]
	""" Hardened Horns
	[Divine Shield] for next combat only. """
	#
	pass

class BG20_HERO_666p_t4b:# <10>[1453]
	""" Magic Magma Horns
	Give a friendly minion [Reborn] for next combat only. """
	#
	pass

class BG20_HERO_666p_t4c:# <10>[1453]
	""" Rare Magma Horns
	Give a friendly minion [Divine Shield] for next combat only. """
	#
	pass

class BG20_HERO_666p_t4d:# <10>[1453]
	""" Unique Magma Horns
	Give a friendly minion[Windfury], [Reborn], and[Divine Shield] for nextcombat only. """
	#
	pass

class BG20_HERO_666p_t5_e:# <10>[1453]
	""" Hooved
	+@ Attack for next combat only. """
	#
	pass

class BG20_HERO_666p_t5a:# <10>[1453]
	""" Hellfire Hooves
	Give your minions +2_Attack for next combat only. """
	#
	pass

class BG20_HERO_666p_t5b:# <10>[1453]
	""" Magic Hellfire Hooves
	Give your minions +4_Attack for next combat only. """
	#
	pass

class BG20_HERO_666p_t5c:# <10>[1453]
	""" Rare Hellfire Hooves
	Give your minions +8_Attack for next combat only. """
	#
	pass

class BG20_HERO_666p_t5d:# <10>[1453]
	""" Unique Hellfire Hooves
	Give your minions +16_Attack for next combat only. """
	#
	pass

class BG20_HERO_666p_t6a:# <10>[1453]
	""" Black Soulstone
	[Secret:] After your last minion dies, summon a random Demon. """
	#
	pass

class BG20_HERO_666p_t6b:# <10>[1453]
	""" Magic Black Soulstone
	[Secret:] After your last minion dies, summon 2 random Demons. """
	#
	pass

class BG20_HERO_666p_t6c:# <10>[1453]
	""" Rare Black Soulstone
	[Secret:] After your last minion dies, summon 3 random Demons. """
	#
	pass

class BG20_HERO_666p_t6d:# <10>[1453]
	""" Unique Black Soulstone
	[Secret:] After your last minion dies, summon 4 random Demons. """
	#
	pass


class TB_BaconShop_HERO_01:# <12>[1453]
	""" Edwin VanCleef
	 """
	#
	pass

class TB_BaconShop_HERO_01_Buddy:# <12>[1453]
	""" SI:7 Scout
	After you buy a minion, gain +1/+1. """
	#
	pass

class TB_BaconShop_HERO_01_Buddy_e:# <12>[1453]
	""" Scouting
	+1/+1. """
	#
	pass

class TB_BaconShop_HERO_01_Buddy_G:# <12>[1453]
	""" SI:7 Scout
	After you buy a minion, gain +2/+2. """
	#
	pass

class TB_BaconShop_HERO_01_Buddy_G_e:# <12>[1453]
	""" Scouting
	+2/+2. """
	#
	pass

class TB_BaconShop_HERO_01_SKIN_A:# <12>[1453]
	""" Kingpin Edwin
	 """
	#
	pass

class TB_BaconShop_HERO_01_SKIN_B:# <12>[1453]
	""" Edwin, the Dashing Scoundrel
	 """
	#
	pass

class TB_BaconShop_HERO_02:# <12>[1453]
	""" Galakrond
	 """
	#
	pass

class TB_BaconShop_HERO_02_Buddy:# <12>[1453]
	""" Apostle of Galakrond
	[Battlecry:] Replace minions in Bob's Tavern with ones of a higher Tavern Tier. """
	#
	pass

class TB_BaconShop_HERO_02_Buddy_G:# <12>[1453]
	""" Apostle of Galakrond
	[Battlecry:] Replaceminions in Bob's Tavernwith ones of a higherTavern Tier twice. """
	#
	pass

class TB_BaconShop_HERO_08:# <12>[1453]
	""" Illidan Stormrage
	 """
	#
	pass

class TB_BaconShop_HERO_08_Buddy:# <12>[1453]
	""" Eclipsion Illidari
	Your first minion thatattacks has "[Immune]while Attacking" for oneattack only. """
	#
	pass

class TB_BaconShop_HERO_08_Buddy_e:# <12>[1453]
	""" Darkened Heart
	[Immune] while Attacking. """
	#
	pass

class TB_BaconShop_HERO_08_Buddy_G:# <12>[1453]
	""" Eclipsion Illidari
	Your first two minions thatattack have "[Immune]while Attacking" for oneattack only. """
	#
	pass

class TB_BaconShop_HERO_08_SKIN_A:# <12>[1453]
	""" The Horned Devil
	 """
	#
	pass

class TB_BaconShop_HERO_08_SKIN_B:# <12>[1453]
	""" Illidan of the Second Sight
	 """
	#
	pass

class TB_BaconShop_HERO_10:# <12>[1453]
	""" Trade Prince Gallywix
	 """
	#
	pass

class TB_BaconShop_HERO_10_Buddy:# <12>[1453]
	""" Bilgewater Mogul
	[Battlecry:] Give a minion +1/+1 for each Gold spent this turn. """
	#
	pass

class TB_BaconShop_HERO_10_Buddy_G:# <12>[1453]
	""" Bilgewater Mogul
	[Battlecry:] Give a minion +2/+2 for each Gold spent this turn. """
	#
	pass

class TB_BaconShop_HERO_10_Buddye:# <12>[1453]
	""" Brutal Luxury
	Increased stats. """
	#
	pass

class TB_BaconShop_HERO_10_SKIN_A:# <12>[1453]
	""" Moneyhogger Gallywix
	 """
	#
	pass

class TB_BaconShop_HERO_10_SKIN_B:# <12>[1453]
	""" Dong Zhuo Gallywix
	 """
	#
	pass

class TB_BaconShop_HERO_11:# <12>[1453]
	""" Ragnaros the Firelord
	 """
	#
	pass

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

class TB_BaconShop_HERO_11_SKIN_A:# <12>[1453]
	""" Flamewarden Ragnaros
	 """
	#
	pass

class TB_BaconShop_HERO_11_SKIN_B:# <12>[1453]
	""" Infernojet Ragnaros
	 """
	#
	pass

class TB_BaconShop_HERO_12:# <12>[1453]
	""" The Rat King
	 """
	#
	pass

class TB_BaconShop_HERO_12_Buddy:# <12>[1453]
	""" Pigeon Lord
	Your [Refreshes] cost (0)while Bob's Tavern doesn'thave the minion type ofyour Hero Power. """
	#
	pass

class TB_BaconShop_HERO_12_Buddy_G:# <12>[1453]
	""" Pigeon Lord
	Your [Refreshes] cost (0)while Bob's Tavern doesn'thave the minion type ofyour Hero Power. """
	#
	pass

class TB_BaconShop_HERO_12_SKIN_A:# <12>[1453]
	""" The Martial Rat
	 """
	#
	pass

class TB_BaconShop_HERO_14:# <12>[1453]
	""" Queen Wagtoggle
	 """
	#
	pass

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

class TB_BaconShop_HERO_14_SKIN_A:# <12>[1453]
	""" Amalgamech Wagtoggle
	 """
	#
	pass

class TB_BaconShop_HERO_15:# <12>[1453]
	""" George the Fallen
	 """
	#
	pass

class TB_BaconShop_HERO_15_Buddy:# <12>[1453]
	""" Karl the Lost
	After you use your Hero Power, give your [Divine Shield] minions +2_Attack. """
	#
	pass

class TB_BaconShop_HERO_15_Buddy_e:# <12>[1453]
	""" Lost and Found
	+2 Attack. """
	#
	pass

class TB_BaconShop_HERO_15_Buddy_G:# <12>[1453]
	""" Karl the Lost
	After you use your Hero Power, give your [Divine Shield] minions +4_Attack. """
	#
	pass

class TB_BaconShop_HERO_15_Buddy_G_e:# <12>[1453]
	""" Lost and Found
	+4 Attack. """
	#
	pass

class TB_BaconShop_HERO_15_SKIN_A:# <12>[1453]
	""" George the Ascended
	 """
	#
	pass

class TB_BaconShop_HERO_15_SKIN_B:# <12>[1453]
	""" Light of the Naaru
	 """
	#
	pass

class TB_BaconShop_HERO_15_SKIN_C:# <12>[1453]
	""" Battle Healer George
	 """
	#
	pass

class TB_BaconShop_HERO_15_SKIN_D:# <12>[1453]
	""" George the Lightbringer
	 """
	#
	pass

class TB_BaconShop_HERO_16:# <12>[1453]
	""" A. F. Kay
	 """
	#
	pass

class TB_BaconShop_HERO_16_Buddy:# <12>[1453]
	""" Snack Vendor
	At the end of your turn, give your Tavern Tier 3 minions +1/+2. """
	#
	pass

class TB_BaconShop_HERO_16_Buddy_e:# <12>[1453]
	""" Snack-Filled
	+1/+2. """
	#
	pass

class TB_BaconShop_HERO_16_Buddy_G:# <12>[1453]
	""" Snack Vendor
	At the end of your turn, give your Tavern Tier 3 minions +2/+4. """
	#
	pass

class TB_BaconShop_HERO_16_Buddy_G_e:# <12>[1453]
	""" Snack-Filled
	+2/+4. """
	#
	pass

class TB_BaconShop_HERO_16_SKIN_A:# <12>[1453]
	""" Sunlounger A. F. Kay
	 """
	#
	pass

class TB_BaconShop_HERO_16_SKIN_B:# <12>[1453]
	""" A. F. Kay, the Tempest
	 """
	#
	pass

class TB_BaconShop_HERO_17:# <12>[1453]
	""" Millificent Manastorm
	 """
	#
	pass

class TB_BaconShop_HERO_17_SKIN_A:# <12>[1453]
	""" Missileshot
	 """
	#
	pass

class TB_BaconShop_HERO_18:# <12>[1453]
	""" Patches the Pirate
	 """
	#
	pass

class TB_BaconShop_HERO_18_Buddy_e:# <12>[1453]
	""" Raiding with Tuskarr
	Increased stats. """
	#
	pass

class TB_BaconShop_HERO_18_SKIN_A:# <12>[1453]
	""" Salteye Patches
	 """
	#
	pass

class TB_BaconShop_HERO_19:# <12>[1453]
	""" Giantfin
	 """
	#
	pass

class TB_BaconShop_HERO_20:# <12>[1453]
	""" Professor Putricide
	 """
	#
	pass

class TB_BaconShop_HERO_21:# <12>[1453]
	""" The Great Akazamzarak
	 """
	#
	pass

class TB_BaconShop_HERO_21_Buddy:# <12>[1453]
	""" Street Magician
	[Deathrattle:] Put a random [Secret] into the battlefield. """
	#
	pass

class TB_BaconShop_HERO_21_Buddy_G:# <12>[1453]
	""" Street Magician
	[Deathrattle:] Put 2 random[Secrets] into the battlefield. """
	#
	pass

class TB_BaconShop_HERO_21_SKIN_A:# <12>[1453]
	""" Crashin' Thrashin' Akazamzarak
	 """
	#
	pass

class TB_BaconShop_HERO_22:# <12>[1453]
	""" The Lich King
	 """
	#
	pass

class TB_BaconShop_HERO_22_SKIN_A:# <12>[1453]
	""" Grill King Bolvar
	 """
	#
	pass

class TB_BaconShop_HERO_22_SKIN_B:# <12>[1453]
	""" Invincible Lich King
	 """
	#
	pass

class TB_BaconShop_HERO_22_SKIN_C:# <12>[1453]
	""" Lü Bu Arthas
	 """
	#
	pass

class TB_BaconShop_HERO_23:# <12>[1453]
	""" Shudderwock
	 """
	#
	pass

class TB_BaconShop_HERO_23_Buddy:# <12>[1453]
	""" Muckslinger
	After you play a minion,add a [Battlecry] minionto Bob's Tavern.Give it +2/+2. """
	#
	pass

class TB_BaconShop_HERO_23_Buddy_e:# <12>[1453]
	""" Mucked Up
	+2/+2. """
	#
	pass

class TB_BaconShop_HERO_23_Buddy_G:# <12>[1453]
	""" Muckslinger
	After you play a minion,add a [Battlecry] minionto Bob's Tavern.Give it +4/+4. """
	#
	pass

class TB_BaconShop_HERO_23_Buddy_Ge:# <12>[1453]
	""" Mucked Up
	+4/+4. """
	#
	pass

class TB_BaconShop_HERO_23_SKIN_A:# <12>[1453]
	""" Gentleman Shudderwock
	 """
	#
	pass

class TB_BaconShop_HERO_25:# <12>[1453]
	""" Lich Baz'hial
	 """
	#
	pass

class TB_BaconShop_HERO_25_Buddy:# <12>[1453]
	""" Unearthed Underling
	Whenever your hero takesdamage, this miniongains +3/+3 instead.<i>(@ left this turn.)</i> """
	#
	pass

class TB_BaconShop_HERO_25_Buddy_e:# <12>[1453]
	""" Recovery
	+3/+3. """
	#
	pass

class TB_BaconShop_HERO_25_Buddy_G:# <12>[1453]
	""" Unearthed Underling
	Whenever your hero takesdamage, this miniongains +6/+6 instead.<i>(@ left this turn.)</i> """
	#
	pass

class TB_BaconShop_HERO_25_Buddy_Ge:# <12>[1453]
	""" Recovery
	+6/+6. """
	#
	pass

class TB_BaconShop_HERO_25_SKIN_A:# <12>[1453]
	""" Margrave Baz'hial
	 """
	#
	pass

class TB_BaconShop_HERO_27:# <12>[1453]
	""" Sindragosa
	 """
	#
	pass

class TB_BaconShop_HERO_27_Buddy:# <12>[1453]
	""" Thawed Champion
	At the end of your turn, adda random [Frozen] minionfrom Bob's Tavernto your hand. """
	#
	pass

class TB_BaconShop_HERO_27_Buddy_G:# <12>[1453]
	""" Thawed Champion
	At the end of your turn, add2 random [Frozen] minionsfrom Bob's Tavernto your hand. """
	#
	pass

class TB_BaconShop_HERO_27_SKIN_A:# <12>[1453]
	""" Sindragosa the Blue
	 """
	#
	pass

class TB_BaconShop_HERO_28:# <12>[1453]
	""" Infinite Toki
	 """
	#
	pass

class TB_BaconShop_HERO_28_SKIN_A:# <12>[1453]
	""" Toki the Clown
	 """
	#
	pass

class TB_BaconShop_HERO_28_SKIN_B:# <12>[1453]
	""" Toki, Wings of the Infinite
	 """
	#
	pass

class TB_BaconShop_HERO_29:# <12>[1453]
	""" C'Thun
	 """
	#
	pass

class TB_BaconShop_HERO_29_Buddy:# <12>[1453]
	""" Tentacle of C'Thun
	After a different friendly minion gains stats, gain_+1/+1 until your next turn. """
	#
	pass

class TB_BaconShop_HERO_29_Buddy_e:# <12>[1453]
	""" All Eyes On Me
	+1/+1. """
	#
	pass

class TB_BaconShop_HERO_29_Buddy_G:# <12>[1453]
	""" Tentacle of C'Thun
	After a different friendly minion gains stats, gain_+2/+2  until your next turn. """
	#
	pass

class TB_BaconShop_HERO_29_Buddy_Ge:# <12>[1453]
	""" All Eyes On Me
	+2/+2. """
	#
	pass

class TB_BaconShop_HERO_29_SKIN_A:# <12>[1453]
	""" Cute'Thun
	 """
	#
	pass

class TB_BaconShop_HERO_29_SKIN_B:# <12>[1453]
	""" Mecha'thun
	 """
	#
	pass

class TB_BaconShop_HERO_30:# <12>[1453]
	""" Nefarian
	 """
	#
	pass

class TB_BaconShop_HERO_31:# <12>[1453]
	""" Bartendotron
	 """
	#
	pass

class TB_BaconShop_HERO_33:# <12>[1453]
	""" The Curator
	 """
	#
	pass

class TB_BaconShop_HERO_33_Buddy_e:# <12>[1453]
	""" Amalfam
	Increased stats. """
	#
	pass

class TB_BaconShop_HERO_33_SKIN_A:# <12>[1453]
	""" Cuddly Curator
	 """
	#
	pass

class TB_BaconShop_HERO_34:# <12>[1453]
	""" Patchwerk
	 """
	#
	pass

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

class TB_BaconShop_HERO_34_SKIN_A:# <12>[1453]
	""" Necrolord Patchwerk
	 """
	#
	pass

class TB_BaconShop_HERO_34_SKIN_B:# <12>[1453]
	""" Gluthrider Patchwerk
	 """
	#
	pass

class TB_BaconShop_HERO_35:# <12>[1453]
	""" Yogg-Saron, Hope's End
	 """
	#
	pass

class TB_BaconShop_HERO_35_Buddy_t1:# <12>[1453]
	""" Mysterybox
	For the rest of the game,your Hero Power triggersan extra time when used. """
	#
	pass

class TB_BaconShop_HERO_35_Buddy_t1e:# <12>[1453]
	""" Mysterybox
	Your Hero Power triggers an extra time. """
	#
	pass

class TB_BaconShop_HERO_35_Buddy_t2:# <12>[1453]
	""" Hand of Fate
	Add 3 random Darkmoon Prizes to your hand. """
	#
	pass

class TB_BaconShop_HERO_35_Buddy_t3:# <12>[1453]
	""" Curse of Flesh
	Give your minions +3/+3, then randomly shuffle their stats. """
	#
	pass

class TB_BaconShop_HERO_35_Buddy_t3e:# <12>[1453]
	""" Fleshy
	+3/+3 """
	#
	pass

class TB_BaconShop_HERO_35_Buddy_t3f:# <12>[1453]
	""" Curse of Fleshed
	Stats shuffled with other minions. """
	#
	pass

class TB_BaconShop_HERO_35_Buddy_t4:# <12>[1453]
	""" Mindflayer Goggles
	Steal all minions in Bob's Tavern, then [Refresh] it. """
	#
	pass

class TB_BaconShop_HERO_35_Buddy_t5:# <12>[1453]
	""" Devouring Hunger
	Consume Bob's Tavern and give thestats to your minions.Then [Refresh] it. """
	#
	pass

class TB_BaconShop_HERO_35_Buddy_t6:# <12>[1453]
	""" Rod of Roasting
	Cast 'Pyrobuff' randomly to give minions +4/+4 until one hits your bartender or hero. """
	#
	pass

class TB_BaconShop_HERO_35_Buddy_t6e:# <12>[1453]
	""" Pyrobuffed
	+4/+4 """
	#
	pass

class TB_BaconShop_HERO_35_Buddy_t6t:# <12>[1453]
	""" Pyrobuff
	Give a minion +4/+4. """
	#
	pass

class TB_BaconShop_HERO_35_SKIN_A:# <12>[1453]
	""" Soggy Yoggy
	 """
	#
	pass

class TB_BaconShop_HERO_35_SKIN_B:# <12>[1453]
	""" Yogg-Saron, Devourer of Stars
	 """
	#
	pass

class TB_BaconShop_HERO_36:# <12>[1453]
	""" Dancin' Deryl
	 """
	#
	pass

class TB_BaconShop_HERO_36_Buddy:# <12>[1453]
	""" Asher the Haberdasher
	After you sell a minion, gain +1/+1. """
	#
	pass

class TB_BaconShop_HERO_36_Buddy_e:# <12>[1453]
	""" Dashing Hat
	+1/+1. """
	#
	pass

class TB_BaconShop_HERO_36_Buddy_G:# <12>[1453]
	""" Asher the Haberdasher
	After you sell a minion, gain +2/+2. """
	#
	pass

class TB_BaconShop_HERO_36_Buddy_Ge:# <12>[1453]
	""" Dashing Hat
	+2/+2. """
	#
	pass

class TB_BaconShop_HERO_36_SKIN_A:# <12>[1453]
	""" The Invisible Murloc
	 """
	#
	pass

class TB_BaconShop_HERO_37:# <12>[1453]
	""" Lord Jaraxxus
	 """
	#
	pass

class TB_BaconShop_HERO_37_SKIN_A:# <12>[1453]
	""" Shado-pan Jaraxxus
	 """
	#
	pass

class TB_BaconShop_HERO_37_SKIN_B:# <12>[1453]
	""" Malefic Jaraxxus
	 """
	#
	pass

class TB_BaconShop_HERO_38:# <12>[1453]
	""" King Mukla
	 """
	#
	pass

class TB_BaconShop_HERO_38_Buddy_e:# <12>[1453]
	""" Banana Peel
	+1/+1. """
	#
	pass

class TB_BaconShop_HERO_38_Buddy_Ge:# <12>[1453]
	""" Banana Peel
	+2/+2. """
	#
	pass

class TB_BaconShop_HERO_38_SKIN_A:# <12>[1453]
	""" Banana Man Mukla
	 """
	#
	pass

class TB_BaconShop_HERO_39:# <12>[1453]
	""" Pyramad
	 """
	#
	pass

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

class TB_BaconShop_HERO_39_SKIN_A:# <12>[1453]
	""" Pyramellow
	 """
	#
	pass

class TB_BaconShop_HERO_39_SKIN_B:# <12>[1453]
	""" Originator Pyramad
	 """
	#
	pass

class TB_BaconShop_HERO_40:# <12>[1453]
	""" Sir Finley Mrrgglton
	 """
	#
	pass

class TB_BaconShop_HERO_40_SKIN_A:# <12>[1453]
	""" Finley of the Kyrian
	 """
	#
	pass

class TB_BaconShop_HERO_40_SKIN_B:# <12>[1453]
	""" Fintastic Finley
	 """
	#
	pass

class TB_BaconShop_HERO_40_SKIN_C:# <12>[1453]
	""" Finley & Metzen
	 """
	#
	pass

class TB_BaconShop_HERO_41:# <12>[1453]
	""" Reno Jackson
	 """
	#
	pass

class TB_BaconShop_HERO_41_Buddy:# <12>[1453]
	""" Sr. Tomb Diver
	[Deathrattle:] Make your right-most minion Golden. """
	#
	pass

class TB_BaconShop_HERO_41_Buddy_G:# <12>[1453]
	""" Sr. Tomb Diver
	[Deathrattle:] Make your tworight-most minions Golden. """
	#
	pass

class TB_BaconShop_HERO_41_SKIN_A:# <12>[1453]
	""" Renogos
	 """
	#
	pass

class TB_BaconShop_HERO_41_SKIN_B:# <12>[1453]
	""" Reno-man
	 """
	#
	pass

class TB_BaconShop_HERO_41_SKIN_C:# <12>[1453]
	""" Tower-toppler Reno
	 """
	#
	pass

class TB_BaconShop_HERO_42:# <12>[1453]
	""" Elise Starseeker
	 """
	#
	pass

class TB_BaconShop_HERO_42_Buddy:# <12>[1453]
	""" Jr. Navigator
	At the start of your turn,get a 'Recruitment Map.'Your Maps cost (1). """
	#
	pass

class TB_BaconShop_HERO_42_Buddy_e:# <12>[1453]
	""" In The Distance
	Costs (1) less. """
	#
	pass

class TB_BaconShop_HERO_42_Buddy_G:# <12>[1453]
	""" Jr. Navigator
	At the start of your turn,get 2 'Recruitment Maps.'Your Maps cost (1). """
	#
	pass

class TB_BaconShop_HERO_42_Buddy_G_e:# <12>[1453]
	""" In The Distance
	Costs (2) less. """
	#
	pass

class TB_BaconShop_HERO_42_SKIN_A:# <12>[1453]
	""" Starseeker
	 """
	#
	pass

class TB_BaconShop_HERO_42_SKIN_B:# <12>[1453]
	""" Da Qiao Elise
	 """
	#
	pass

class TB_BaconShop_HERO_42_SKIN_C:# <12>[1453]
	""" Nightsong Elise
	 """
	#
	pass

class TB_BaconShop_HERO_43:# <12>[1453]
	""" Dinotamer Brann
	 """
	#
	pass

class TB_BaconShop_HERO_43_Buddy:# <12>[1453]
	""" Brann's Epic Egg
	[Taunt]. [Deathrattle:] Summona random [Battlecry] minionand add a copy of itto your hand. """
	#
	pass

class TB_BaconShop_HERO_43_Buddy_G:# <12>[1453]
	""" Brann's Epic Egg
	[Taunt]. [Deathrattle:] Summon2 random [Battlecry] minionsand add copies of themto your hand. """
	#
	pass

class TB_BaconShop_HERO_43_SKIN_A:# <12>[1453]
	""" Orgrimmar Grunt Brann
	 """
	#
	pass

class TB_BaconShop_HERO_43_SKIN_B:# <12>[1453]
	""" Yetitamer Brann
	 """
	#
	pass

class TB_BaconShop_HERO_43_SKIN_C:# <12>[1453]
	""" Gronnstalker Brann
	 """
	#
	pass

class TB_BaconShop_HERO_44:# <12>[1453]
	""" Sylvanas Windrunner
	 """
	#
	pass

class TB_BaconShop_HERO_45:# <12>[1453]
	""" Arch-Villain Rafaam
	 """
	#
	pass

class TB_BaconShop_HERO_45_Buddy:# <12>[1453]
	""" Loyal Henchman
	After you kill a secondminion each combat,get a plain copy of it. """
	#
	pass

class TB_BaconShop_HERO_45_Buddy_G:# <12>[1453]
	""" Loyal Henchman
	After you kill a secondminion each combat,_get 2 plain copies of it. """
	#
	pass

class TB_BaconShop_HERO_45_SKIN_A:# <12>[1453]
	""" Rafaam, Supreme Villain
	 """
	#
	pass

class TB_BaconShop_HERO_45_SKIN_B:# <12>[1453]
	""" Holofist Rafaam
	 """
	#
	pass

class TB_BaconShop_HERO_45_SKIN_C:# <12>[1453]
	""" Cao Cao Rafaam
	 """
	#
	pass

class TB_BaconShop_HERO_47:# <12>[1453]
	""" Tirion Fordring
	 """
	#
	pass

class TB_BaconShop_HERO_49:# <12>[1453]
	""" Millhouse Manastorm
	 """
	#
	pass

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

class TB_BaconShop_HERO_49_SKIN_A:# <12>[1453]
	""" Pyrospike Millhouse
	 """
	#
	pass

class TB_BaconShop_HERO_49_SKIN_B:# <12>[1453]
	""" The Brute
	 """
	#
	pass

class TB_BaconShop_HERO_49_SKIN_C:# <12>[1453]
	""" Prism Disc Millhouse
	 """
	#
	pass

class TB_BaconShop_HERO_50:# <12>[1453]
	""" Tess Greymane
	 """
	#
	pass

class TB_BaconShop_HERO_50_Buddy:# <12>[1453]
	""" Hunter of Old
	At the start of your turn,add your last opponent's Buddy to your hand. """
	#
	pass

class TB_BaconShop_HERO_50_Buddy_G:# <12>[1453]
	""" Hunter of Old
	At the start of your turn, add 2 of your last opponent's Buddy to your hand. """
	#
	pass

class TB_BaconShop_HERO_50_SKIN_A:# <12>[1453]
	""" Venthyr Tess
	 """
	#
	pass

class TB_BaconShop_HERO_50_SKIN_B:# <12>[1453]
	""" Tess, Stormpike Assassin
	 """
	#
	pass

class TB_BaconShop_HERO_50_SKIN_C:# <12>[1453]
	""" Riddling Tempest Tess
	 """
	#
	pass

class TB_BaconShop_HERO_52:# <12>[1453]
	""" Deathwing
	 """
	#
	pass

class TB_BaconShop_HERO_52_Buddy:# <12>[1453]
	""" Lady Sinestra
	Your minions have +3_Attack. """
	#
	pass

class TB_BaconShop_HERO_52_Buddy_e:# <12>[1453]
	""" Draconic Blessing
	+3 Attack """
	#
	pass

class TB_BaconShop_HERO_52_Buddy_G:# <12>[1453]
	""" Lady Sinestra
	Your minions have +6_Attack. """
	#
	pass

class TB_BaconShop_HERO_52_Buddy_G_e:# <12>[1453]
	""" Draconic Blessing
	+6 Attack """
	#
	pass

class TB_BaconShop_HERO_52_SKIN_A:# <12>[1453]
	""" Deathwing the Black
	 """
	#
	pass

class TB_BaconShop_HERO_53:# <12>[1453]
	""" Ysera
	 """
	#
	pass

class TB_BaconShop_HERO_53_Buddy_e:# <12>[1453]
	""" Pleasant Dream
	Stats increased by Valithria. """
	#
	pass

class TB_BaconShop_HERO_53_SKIN_A:# <12>[1453]
	""" Ysera of the Night Fae
	 """
	#
	pass

class TB_BaconShop_HERO_53_SKIN_B:# <12>[1453]
	""" Ysera the Green
	 """
	#
	pass

class TB_BaconShop_HERO_53_SKIN_C:# <12>[1453]
	""" Ysera, Embraced by Elune
	 """
	#
	pass

class TB_BaconShop_HERO_55:# <12>[1453]
	""" Fungalmancer Flurgl
	 """
	#
	pass

class TB_BaconShop_HERO_55_SKIN_A:# <12>[1453]
	""" Pyroloc
	 """
	#
	pass

class TB_BaconShop_HERO_55_SKIN_B:# <12>[1453]
	""" Horsemaster Flurgl
	 """
	#
	pass

class TB_BaconShop_HERO_56:# <12>[1453]
	""" Alexstrasza
	 """
	#
	pass

class TB_BaconShop_HERO_56_SKIN_A:# <12>[1453]
	""" Alexstrasza the Red
	 """
	#
	pass

class TB_BaconShop_HERO_57:# <12>[1453]
	""" Nozdormu
	 """
	#
	pass

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

class TB_BaconShop_HERO_57_SKIN_A:# <12>[1453]
	""" Nozdormu the Bronze
	 """
	#
	pass

class TB_BaconShop_HERO_58:# <12>[1453]
	""" Malygos
	 """
	#
	pass

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

class TB_BaconShop_HERO_58_SKIN_A:# <12>[1453]
	""" Malygos the Blue
	 """
	#
	pass

class TB_BaconShop_HERO_59:# <12>[1453]
	""" Aranna Starseeker
	 """
	#
	pass

class TB_BaconShop_HERO_59_Buddy:# <12>[1453]
	""" Sklibb, Demon Hunter
	After you play a minion,your next [Refresh] costs (0). """
	#
	pass

class TB_BaconShop_HERO_59_Buddy_G:# <12>[1453]
	""" Sklibb, Demon Hunter
	After you play a minion, your next two [Refreshes] cost (0). """
	#
	pass

class TB_BaconShop_HERO_59_SKIN_A:# <12>[1453]
	""" Fury
	 """
	#
	pass

class TB_BaconShop_HERO_59_SKIN_B:# <12>[1453]
	""" Warpfrenzy Aranna
	 """
	#
	pass

class TB_BaconShop_HERO_59_SKIN_C:# <12>[1453]
	""" Xiao Qiao Aranna
	 """
	#
	pass

class TB_BaconShop_HERO_59t:# <12>[1453]
	""" Aranna, Unleashed
	 """
	#
	pass

class TB_BaconShop_HERO_59t_SKIN_A:# <12>[1453]
	""" Fury, Unleashed
	 """
	#
	pass

class TB_BaconShop_HERO_59t_SKIN_B:# <12>[1453]
	""" Warpfrenzy Aranna, Unleashed
	 """
	#
	pass

class TB_BaconShop_HERO_59t_SKIN_Ct:# <12>[1453]
	""" Xiao Qiao Aranna, Unleashed
	 """
	#
	pass

class TB_BaconShop_HERO_60:# <12>[1453]
	""" Kael'thas Sunstrider
	 """
	#
	pass

class TB_BaconShop_HERO_60_Buddy:# <12>[1453]
	""" Crimson Hand Centurion
	After 'Verdant Spheres' triggers, give your hand and board +1/+1. """
	#
	pass

class TB_BaconShop_HERO_60_Buddy_e:# <12>[1453]
	""" Verdant
	+1/+1. """
	#
	pass

class TB_BaconShop_HERO_60_Buddy_G:# <12>[1453]
	""" Crimson Hand Centurion
	After 'Verdant Spheres' triggers, give your hand and board +2/+2. """
	#
	pass

class TB_BaconShop_HERO_60_Buddy_G_e:# <12>[1453]
	""" Verdant
	+2/+2. """
	#
	pass

class TB_BaconShop_HERO_60_SKIN_A:# <12>[1453]
	""" Chained Kael'thas
	 """
	#
	pass

class TB_BaconShop_HERO_60_SKIN_B:# <12>[1453]
	""" Winterflurry Kael'thas
	 """
	#
	pass

class TB_BaconShop_HERO_61:# <12>[1453]
	""" Lady Vashj
	 """
	#
	pass

class TB_BaconShop_HERO_62:# <12>[1453]
	""" Maiev Shadowsong
	 """
	#
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

class TB_BaconShop_HERO_62_SKIN_A:# <12>[1453]
	""" Pool Party Maiev
	 """
	#
	pass

class TB_BaconShop_HERO_62_SKIN_B:# <12>[1453]
	""" The Warden
	 """
	#
	pass

class TB_BaconShop_HERO_62_SKIN_C:# <12>[1453]
	""" Saberrider Maiev
	 """
	#
	pass

class TB_BaconShop_HERO_62_SKIN_D:# <12>[1453]
	""" Diao Chan Maiev
	 """
	#
	pass

class TB_BaconShop_HERO_64:# <12>[1453]
	""" Captain Eudora
	 """
	#
	pass

class TB_BaconShop_HERO_64_Buddy_e:# <12>[1453]
	""" Gold Abound
	+5/+5. """
	#
	pass

class TB_BaconShop_HERO_64_Buddy_G_e:# <12>[1453]
	""" Gold Abound
	+10/+10. """
	#
	pass

class TB_BaconShop_HERO_64_SKIN_A:# <12>[1453]
	""" Blasterfox
	 """
	#
	pass

class TB_BaconShop_HERO_64_SKIN_B:# <12>[1453]
	""" Snowblast Eudora
	 """
	#
	pass

class TB_BaconShop_HERO_67:# <12>[1453]
	""" Captain Hooktusk
	 """
	#
	pass

class TB_BaconShop_HERO_67_Buddy:# <12>[1453]
	""" Raging Contender
	'Trash for Treasure' offers 3 options instead of 2. """
	#
	pass

class TB_BaconShop_HERO_67_Buddy_G:# <12>[1453]
	""" Raging Contender
	'Trash for Treasure' offers 4 options instead of 2. """
	#
	pass

class TB_BaconShop_HERO_67_SKIN_A:# <12>[1453]
	""" Snowball Hooktusk
	 """
	#
	pass

class TB_BaconShop_HERO_67_SKIN_B:# <12>[1453]
	""" Sharkwrangler Hooktusk
	 """
	#
	pass

class TB_BaconShop_HERO_68:# <12>[1453]
	""" Skycap'n Kragg
	 """
	#
	pass

class TB_BaconShop_HERO_68_SKIN_A:# <12>[1453]
	""" Undercap'n Kragg
	 """
	#
	pass

class TB_BaconShop_HERO_70:# <12>[1453]
	""" Mr. Bigglesworth
	 """
	#
	pass

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

class TB_BaconShop_HERO_70_SKIN_A:# <12>[1453]
	""" Pet Salon Bigglesworth
	 """
	#
	pass

class TB_BaconShop_HERO_70_SKIN_B:# <12>[1453]
	""" Gifted Bigglesworth
	 """
	#
	pass

class TB_BaconShop_HERO_70_SKIN_C:# <12>[1453]
	""" Cosmic Bigglesworth
	 """
	#
	pass

class TB_BaconShop_HERO_71:# <12>[1453]
	""" Jandice Barov
	 """
	#
	pass

class TB_BaconShop_HERO_71_Buddy:# <12>[1453]
	""" Jandice's Apprentice
	After you swap minions, give them stats equal to your Tavern Tier. """
	#
	pass

class TB_BaconShop_HERO_71_Buddy_e:# <10>[1453]
	""" Spinning
	Increased Stats. """
	#
	pass

class TB_BaconShop_HERO_71_Buddy_G:# <12>[1453]
	""" Jandice's Apprentice
	After you swap minions,give them stats equal toyour Tavern Tier twice. """
	#
	pass

class TB_BaconShop_HERO_71_SKIN_A:# <12>[1453]
	""" Mirrorgrin
	 """
	#
	pass

class TB_BaconShop_HERO_71_SKIN_B:# <12>[1453]
	""" Shadowpanther Jandice
	 """
	#
	pass

class TB_BaconShop_HERO_72:# <12>[1453]
	""" Lord Barov
	 """
	#
	pass

class TB_BaconShop_HERO_72_Buddy:# <12>[1453]
	""" Barov's Apprentice
	After you play a Gold Coin, gain 1 Gold this turn only. """
	#
	pass

class TB_BaconShop_HERO_72_Buddy_G:# <12>[1453]
	""" Barov's Apprentice
	After you play a Gold Coin, gain 2 Gold this turn only. """
	#
	pass

class TB_BaconShop_HERO_72_SKIN_A:# <12>[1453]
	""" Stouthoof Barov
	 """
	#
	pass

class TB_BaconShop_HERO_74:# <12>[1453]
	""" Forest Warden Omu
	 """
	#
	pass

class TB_BaconShop_HERO_74_Buddy:# <12>[1453]
	""" Evergreen Botani
	At the end of your turn, adda random minion of your_Tavern Tier to your hand. """
	#
	pass

class TB_BaconShop_HERO_74_Buddy_e:# <10>[1453]
	""" Evergreen
	Increased stats. """
	#
	pass

class TB_BaconShop_HERO_74_Buddy_G:# <12>[1453]
	""" Evergreen Botani
	At the end of your turn, add2 random minions of your_Tavern Tier to your hand. """
	#
	pass

class TB_BaconShop_HERO_74_SKIN_A:# <12>[1453]
	""" Faewarden Omu
	 """
	#
	pass

class TB_BaconShop_HERO_74_SKIN_B:# <12>[1453]
	""" Pugilist Omu
	 """
	#
	pass

class TB_BaconShop_HERO_74_SKIN_C:# <12>[1453]
	""" Gingerbread Omu
	 """
	#
	pass

class TB_BaconShop_HERO_75:# <12>[1453]
	""" Rakanishu
	 """
	#
	pass

class TB_BaconShop_HERO_75_Buddy:# <12>[1453]
	""" Lantern Tender
	At the end of your turn,give a random friendlyminion stats equal toyour Tavern Tier. """
	#
	pass

class TB_BaconShop_HERO_75_Buddy_G:# <12>[1453]
	""" Lantern Tender
	At the end of your turn,give a random friendlyminion stats equal to yourTavern Tier twice. """
	#
	pass

class TB_BaconShop_HERO_75_SKIN_A:# <12>[1453]
	""" Deckwatch Rakanishu
	 """
	#
	pass

class TB_BaconShop_HERO_76:# <12>[1453]
	""" Al'Akir
	 """
	#
	pass

class TB_BaconShop_HERO_76_Buddy_e:# <12>[1453]
	""" Blessing of Air
	[Windfury], [Divine Shield], and [Taunt]. """
	#
	pass

class TB_BaconShop_HERO_76_SKIN_A:# <12>[1453]
	""" Mechastorm Al'Akir
	 """
	#
	pass

class TB_BaconShop_HERO_76_SKIN_B:# <12>[1453]
	""" Al'Akir the Skybreaker
	 """
	#
	pass

class TB_BaconShop_HERO_78:# <12>[1453]
	""" Chenvaala
	 """
	#
	pass

class TB_BaconShop_HERO_78_SKIN_A:# <12>[1453]
	""" Volcanic Chenvaala
	 """
	#
	pass

class TB_BaconShop_HERO_90:# <12>[1453]
	""" Silas Darkmoon
	 """
	#
	pass

class TB_BaconShop_HERO_90_Buddy:# <12>[1453]
	""" Burth
	After you buy a minion witha Darkmoon Ticket, gain1_Gold this turn only. """
	#
	pass

class TB_BaconShop_HERO_90_Buddy_G:# <12>[1453]
	""" Burth
	After you buy a minion witha Darkmoon Ticket, gain2_Gold this turn only. """
	#
	pass

class TB_BaconShop_HERO_90_SKIN_A:# <12>[1453]
	""" Port Authority Silas
	 """
	#
	pass

class TB_BaconShop_HERO_90_SKIN_B:# <12>[1453]
	""" Jinglepocket Silas
	 """
	#
	pass

class TB_BaconShop_HERO_91:# <12>[1453]
	""" Zephrys, the Great
	 """
	#
	pass

class TB_BaconShop_HERO_91_SKIN_A:# <12>[1453]
	""" Agent Z
	 """
	#
	pass

class TB_BaconShop_HERO_91_SKIN_B:# <12>[1453]
	""" Stockingstuffer Zephrys
	 """
	#
	pass

class TB_BaconShop_HERO_91_SKIN_C:# <12>[1453]
	""" Zhuge Liang Zephrys
	 """
	#
	pass

class TB_BaconShop_HERO_91_SKIN_D:# <12>[1453]
	""" Goldenstar Zephrys
	 """
	#
	pass

class TB_BaconShop_HERO_92:# <12>[1453]
	""" Y'Shaarj
	 """
	#
	pass

class TB_BaconShop_HERO_92_Buddy:# <12>[1453]
	""" Baby Y'Shaarj
	Whenever you summon a minion of your current Tavern Tier, give it +4/+4. """
	#
	pass

class TB_BaconShop_HERO_92_Buddy_e:# <12>[1453]
	""" Rage Unbound
	+4/+4. """
	#
	pass

class TB_BaconShop_HERO_92_Buddy_G:# <12>[1453]
	""" Baby Y'Shaarj
	Whenever you summon a minion of your current Tavern Tier, give it +8/+8. """
	#
	pass

class TB_BaconShop_HERO_92_Buddy_G_e:# <12>[1453]
	""" Rage Unbound
	+8/+8. """
	#
	pass

class TB_BaconShop_HERO_93:# <12>[1453]
	""" N'Zoth
	 """
	#
	pass

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

class TB_BaconShop_HERO_93_SKIN_A:# <12>[1453]
	""" Cowboy N'Zoth
	 """
	#
	pass

class TB_BaconShop_HERO_94:# <12>[1453]
	""" Tickatus
	 """
	#
	pass

class TB_BaconShop_HERO_94_Buddy:# <12>[1453]
	""" Ticket Collector
	[Battlecry:] [Discover] aDarkmoon Prize fromthe next Prize turn. """
	#
	pass

class TB_BaconShop_HERO_94_Buddy_G:# <12>[1453]
	""" Ticket Collector
	[Battlecry:] [Discover] 2Darkmoon Prizes fromthe next Prize turn. """
	#
	pass

class TB_BaconShop_HERO_94_SKIN_A:# <12>[1453]
	""" Flexfire Tickatus
	 """
	#
	pass

class TB_BaconShop_HERO_94_SKIN_B:# <12>[1453]
	""" Felblaze Tickatus
	 """
	#
	pass

class TB_BaconShop_HERO_95:# <12>[1453]
	""" Greybough
	 """
	#
	pass

class TB_BaconShop_HERO_95_Buddy:# <12>[1453]
	""" Wandering Treant
	Whenever you summon a [Taunt] minion, give it +2/+2. """
	#
	pass

class TB_BaconShop_HERO_95_Buddy_e:# <12>[1453]
	""" Happy Little Tree
	+2/+2. """
	#
	pass

class TB_BaconShop_HERO_95_Buddy_G:# <12>[1453]
	""" Wandering Treant
	Whenever you summon a [Taunt] minion, give it +4/+4. """
	#
	pass

class TB_BaconShop_HERO_95_Buddy_G_e:# <12>[1453]
	""" Happy Little Tree
	+4/+4. """
	#
	pass

class TB_BaconShop_HERO_95_SKIN_A:# <12>[1453]
	""" Winterbough
	 """
	#
	pass

class TB_BaconShop_HERO_KelThuzad:# <12>[1453]
	""" Kel'Thuzad
	 """
	#
	pass

class TB_BaconShop_HERO_PH:# <12>[1453]
	""" BaconPHhero
	 """
	#
	pass

