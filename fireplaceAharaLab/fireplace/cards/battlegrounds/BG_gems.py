from ..utils import *

BG_Gems=[
	'BG20_GEM','BG20_GEMe','BG20_GEMe2','GAME_005'
	]

##
##  Blood gem
##

class BG20_GEM:# <12>[1453]
	""" Blood Gem
	Give a friendly minion +@/+@. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0,}
	play = ApplyGem(TARGET, 'BG20_GEM')
	pass

class BG20_GEM_No_Impact:# <12>[1453]
	""" Blood Gem No Impact
	 """
	#
	pass

BG20_GEMe=buff(1,1)# <12>[1453]
""" Blood Gem
Increased stats from Blood Gem (but invisible banner) """


BG20_GEMe2=buff(3,3)# <12>[1453]
""" Blood Gems
+@/+@. """

class GAME_005:# <12> 1637 #OK
	""" The Coin
	Gain 1 Mana Crystal this turn only. """
	play = ManaThisTurn(CONTROLLER, 1)
	pass



class BG20_GEMt:# <12>[1453]
	""" Mass Blood Gem
	Give a friendly minions +@/+@. """
	#
	pass

##
## treasures
##

class BGS_Treasures_000:# <12>[1453]
	""" Big Banana
	Give a minion +2/+2. """
	#
	pass

class BGS_Treasures_000e:# <12>[1453]
	""" Big Banana
	Has +2/+2. """
	#
	pass

class BGS_Treasures_001:# <7>[1453]
	""" Pocket Change
	Add 2 Gold Coins to your hand. """
	#
	pass

class BGS_Treasures_003:# <12>[1453]
	""" Regular Discount
	Reduce the cost of upgrading Bob's Tavern by (3). """
	#
	pass

class BGS_Treasures_004:# <12>[1453]
	""" Gacha Gift
	[Discover] a minion from [Tavern Tier 1]. """
	#
	pass

class BGS_Treasures_006:# <8>[1453]
	""" Evolving Tavern
	Replace all minions in Bob's Tavern with ones of a higher Tavern Tier. """
	#
	pass

class BGS_Treasures_007:# <12>[1453]
	""" Might of Stormwind
	Give 3 random friendly minions +1/+1. """
	#
	pass

class BGS_Treasures_007e:# <12>[1453]
	""" Might of Stormwind
	+1/+1. """
	#
	pass

class BGS_Treasures_009:# <12>[1453]
	""" Gruul Rules
	Give a friendly minion "At the end of your turn, gain +2/+2." """
	#
	pass

class BGS_Treasures_009e:# <12>[1453]
	""" Gruul Rules
	Gains +2/+2 at the end of your turn. """
	#
	pass

class BGS_Treasures_010:# <12>[1453]
	""" Time Thief
	[Discover] a minion from your last opponent's warband. """
	#
	pass

class BGS_Treasures_011:# <12>[1453]
	""" Training Session
	[Discover] a new Hero Power. """
	#
	pass

class BGS_Treasures_012:# <12>[1453]
	""" On the House
	[Discover] a minion from your current [Tavern Tier]. """
	#
	pass

class BGS_Treasures_013:# <12>[1453]
	""" The Good Stuff
	Give minions in Bob's Tavern +2 Health for the rest of the game. """
	#
	pass

class BGS_Treasures_013e1:# <12>[1453]
	""" Good Stuff
	Increased stats. """
	#
	pass

class BGS_Treasures_013e2:# <12>[1453]
	""" Good Stuff
	Increased stats. """
	#
	pass

class BGS_Treasures_013pe:# <12>[1453]
	""" The Good Stuff Player Enchant
	Minions in Bob's Shop have increased stats. """
	#
	pass

class BGS_Treasures_014:# <12>[1453]
	""" The Unlimited Coin
	Gain 1 Gold this turn only. Return this to your hand at end of turn. """
	#
	pass

class BGS_Treasures_014e:# <12>[1453]
	""" Unlimited Coin Return to Hand
	Return the Unlimited Coin to your hand at end of turn. """
	#
	pass

class BGS_Treasures_015:# <5>[1453]
	""" Buy the Holy Light
	Give a friendly minion [Divine Shield]. """
	#
	pass

class BGS_Treasures_016:# <12>[1453]
	""" Raise the Stakes
	Make a friendly minion Golden and return it to your hand. """
	#
	pass

class BGS_Treasures_018:# <12>[1453]
	""" I'm Still Just a Rat in a Cage
	Double a minion's Attack. """
	#
	pass

class BGS_Treasures_018e:# <12>[1453]
	""" Rat in a Cage
	This minion's Attack has been doubled. """
	#
	pass

class BGS_Treasures_019:# <12>[1453]
	""" B.A.N.A.N.A.S.
	Fill your hand with Bananas. """
	#
	pass

class BGS_Treasures_020:# <12>[1453]
	""" Top Shelf
	[Discover] a minion from [Tavern Tier 6]. """
	#
	pass

class BGS_Treasures_022:# <12>[1453]
	""" Friends and Family Discount
	For the rest of the game, minions in Bob's Tavern cost (1) less. """
	#
	pass

class BGS_Treasures_022e:# <12>[1453]
	""" Discounted
	Costs less. """
	#
	pass

class BGS_Treasures_022pe:# <12>[1453]
	""" Friends and Family Discount Player Enchant
	 """
	#
	pass

class BGS_Treasures_023:# <12>[1453]
	""" Open Bar
	Your first 5 [Refreshes]each turn cost (0). """
	#
	pass

class BGS_Treasures_023pe:# <12>[1453]
	""" Refresh Cost 0
	[Refresh] costs (0). """
	#
	pass

class BGS_Treasures_025:# <12>[1453]
	""" Fresh Tab
	Refresh your Gold. """
	#
	pass

class BGS_Treasures_026:# <12>[1453]
	""" The Bouncer
	Give a friendly minion +5/+5 and [Taunt]. """
	#
	pass

class BGS_Treasures_026e:# <12>[1453]
	""" Bouncy Bouncy
	+5/+5 and [Taunt]. """
	#
	pass

class BGS_Treasures_028:# <12>[1453]
	""" Give A Dog A Bone
	Give a friendly minion [Divine Shield], [Windfury], and +10/+10. """
	#
	pass

class BGS_Treasures_028e:# <12>[1453]
	""" Dog Bone
	Has +10/+10, [Divine Shield], and [Windfury]. """
	#
	pass

class BGS_Treasures_029:# <12>[1453]
	""" Rocking and Rolling
	Your next three [Refreshes] cost (0). """
	#
	pass

class BGS_Treasures_030:# <12>[1453]
	""" Brann's Blessing
	Your [Battlecries] trigger twice this turn. """
	#
	pass

class BGS_Treasures_030e:# <0>[1453]
	""" Brann's Blessing
	Your [Battlecries] trigger twice this turn. """
	#
	pass

class BGS_Treasures_032:# <12>[1453]
	""" Big Winner!
	[Discover] a Darkmoon Prize from each of the previous Prize turns. """
	#
	pass

class BGS_Treasures_033:# <0>[1453]
	""" New Recruit
	Add a minion to Bob's Tavern for the rest of the game. """
	#
	pass

class BGS_Treasures_033e:# <0>[1453]
	""" New Recruit
	Add a minion to Bob's Tavern for the rest of the game. """
	#
	pass

class BGS_Treasures_034:# <12>[1453]
	""" Repeat Customer
	Return a friendly non-golden minion to your hand. Give it +2/+2. """
	#
	pass

class BGS_Treasures_034e:# <0>[1453]
	""" Repeat Customer
	+2/+2. """
	#
	pass

class BGS_Treasures_036:# <12>[1453]
	""" Great Deal
	For the rest of the game, reduce the cost of upgrading Bob's Tavern by (3) at the end of your turn. """
	#
	pass

class BGS_Treasures_036e:# <0>[1453]
	""" Great Deal
	At the end of each turn, reduce the cost of upgrading Bob's Tavern by (3). [DNT] """
	#
	pass

class BGS_Treasures_037:# <12>[1453]
	""" All That Glitters
	Make a random minion in Bob's Tavern Golden. """
	#
	pass

##
## secret
##


class TB_Bacon_Secrets_01:# <3>[1453]
	""" Venomstrike Trap
	[Secret:] When one of your minions is attacked, summon a 2/3_[Poisonous] Cobra. """
	#
	pass

class TB_Bacon_Secrets_02:# <3>[1453]
	""" Snake Trap
	[Secret:] When one of your minions is attacked, summon three 1/1 Snakes. """
	#
	pass

class TB_Bacon_Secrets_04:# <4>[1453]
	""" Splitting Image
	[Secret:] When one of your minions is attacked, summon a copy of it. """
	#
	pass

class TB_Bacon_Secrets_05:# <4>[1453]
	""" Effigy
	[Secret:] When a friendly minion dies, summon a random minion with the same Cost. """
	#
	pass

class TB_Bacon_Secrets_07:# <5>[1453]
	""" Autodefense Matrix
	[Secret:] When one of your minions is attacked, give it [Divine Shield]. """
	#
	pass

class TB_Bacon_Secrets_08:# <5>[1453]
	""" Avenge
	[Secret:] When one of your minions dies, give a random friendly minion +3/+2. """
	#
	pass

class TB_Bacon_Secrets_10:# <5>[1453]
	""" Redemption
	[Secret:] When a friendly minion dies, return it to life with 1 Health. """
	#
	pass

class TB_Bacon_Secrets_11:# <5>[1453]
	""" Hand of Salvation
	[Secret:] When your second minion dies in a turn, return it to life. """
	#
	pass

class TB_Bacon_Secrets_12:# <4>[1453]
	""" Ice Block
	[Secret:] When your hero takes fatal damage, prevent it and become [Immune] this turn. """
	#
	pass

class TB_Bacon_Secrets_13:# <5>[1453]
	""" Competitive Spirit
	[Secret:] When your turn starts, give your minions +1/+1. """
	#
	pass

class TB_Bacon_Secrets_13e:# <12>[1453]
	""" Competitive Spirit
	+1/+1. """
	#
	pass

##
##  button and others
##

class TB_BaconShop_1P_PlayerE:# <12>[1453]
	""" BaconShop1PlayerEnchant
	 """
	#
	pass

class TB_BaconShop_1p_Reroll_Button:# <12>[1453]
	""" Refresh
	Replace Bob's Tavern with new minions. """
	#
	pass

class TB_BaconShop_3ofKindChecke:# <12>[1453]
	""" 3ofKindCheckPlayerEnchant
	 """
	#
	pass

class TB_BaconShop_8P_PlayerE:# <12>[1453]
	""" BaconShop8PlayerEnchant
	 """
	#
	pass

class TB_BaconShop_8p_Reroll_Button:# <12>[1453]
	""" Refresh
	Replace Bob's Tavern with new minions. """
	#
	pass

class TB_BaconShop_CheckPtntlTriples:# <12>[1453]
	""" Check Potential Triples
	3ofKindCheck [DNT] """
	#
	pass

class TB_BaconShop_CheckTriples:# <12>[1453]
	""" Check Triples
	3ofKindCheck [DNT] """
	#
	pass

class TB_BaconShop_DragBuy:# <12>[1453]
	""" Drag To Buy
	 """
	#
	pass

class TB_BaconShop_DragSell:# <12>[1453]
	""" Drag To Sell
	 """
	#
	pass

class TB_BaconShop_FXWatcher:# <12>[1453]
	""" Leaderboard FX Watcher [DNT]
	 """
	#
	pass


class TB_BaconShop_IncreasedStats:# <12>[1453]
	""" Increased Stats for Triple
	 """
	#
	pass

class TB_BaconShop_Triples_01:# <12>[1453]
	""" Triple Reward
	[Discover] a minionfrom [Tavern Tier @]. """
	#
	pass

class TB_BaconShop_UpdateDmgCap:# <12>[1453]
	""" Update Damage Cap [DNT]
	Checks if any players are dead and updates the Damage Cap tag on the GameEntity accordingly. [DNT] """
	#
	pass

class TB_BaconShopBadsongE:# <2>[1453]
	""" Costs 0
	Costs (0). """
	#
	pass


class TB_BaconShopBob_SKIN_A:# <12>[1453]
	""" Ragnaros, Tikilord
	 """
	#
	pass

class TB_BaconShopBob_SKIN_B:# <12>[1453]
	""" Ve'nari
	 """
	#
	pass

class TB_BaconShopBob_SKIN_C:# <12>[1453]
	""" Dragonspeaker Bob
	 """
	#
	pass

class TB_BaconShopBob_SKIN_D:# <12>[1453]
	""" Fizzy
	 """
	#
	pass

class TB_BaconShopBob_SKIN_E:# <12>[1453]
	""" Mega Bob
	 """
	#
	pass

class TB_BaconShopBob_SKIN_F:# <12>[1453]
	""" Gala Medivh
	 """
	#
	pass

class TB_BaconShopBob_SKIN_G:# <12>[1453]
	""" Pirate Bob
	 """
	#
	pass

class TB_BaconShopBob_SKIN_H:# <12>[1453]
	""" Flightmaster Dungar
	 """
	#
	pass

class TB_BaconShopBob_SKIN_I:# <12>[1453]
	""" Alterac Bob
	 """
	#
	pass

class TB_BaconShopBob_SKIN_J:# <12>[1453]
	""" Bartendotron
	 """
	#
	pass

class TB_BaconShopBob_SKIN_K:# <12>[1453]
	""" Greatfather Boom
	 """
	#
	pass

class TB_BaconShopBob_SKIN_L:# <12>[1453]
	""" Elder Starsong
	 """
	#
	pass

class TB_BaconShopBob_SKIN_M:# <12>[1453]
	""" Algalon
	 """
	#
	pass

class TB_BaconShopLockAll_Button:# <12>[1453]
	""" Freeze
	[Freeze] / [Unfreeze] the minions in Bob's Tavern. """
	#
	pass

class TB_BaconShopTechUp02_Button:# <12>[1453]
	""" Tavern Tier 2
	Bob sells higher tier minions when you [Refresh]. """
	#
	pass

class TB_BaconShopTechUp03_Button:# <12>[1453]
	""" Tavern Tier 3
	Bob sells higher tier minions when you [Refresh]. """
	#
	pass

class TB_BaconShopTechUp04_Button:# <12>[1453]
	""" Tavern Tier 4
	Bob sells higher tier minions when you [Refresh]. """
	#
	pass

class TB_BaconShopTechUp05_Button:# <12>[1453]
	""" Tavern Tier 5
	Bob sells higher tier minions when you [Refresh]. """
	#
	pass

class TB_BaconShopTechUp06_Button:# <12>[1453]
	""" Tavern Tier 6
	Bob sells higher tier minions when you [Refresh]. """
	#
	pass

