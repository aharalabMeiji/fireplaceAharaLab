from ..utils import *

BG_Hero2=[
	#18	#Drek'Thar#BG22_HERO_002
	'BG22_HERO_002','BG22_HERO_002p','BG22_HERO_002pe','BG22_HERO_002_Buddy','BG22_HERO_002_Buddy_e','BG22_HERO_002_Buddy_G','BG22_HERO_002_Buddy_Ge',
	#19#Edwin VanCleef
	'TB_BaconShop_HERO_01','TB_BaconShop_HP_001','TB_BaconShop_HP_001e','TB_BaconShop_HERO_01_Buddy','TB_BaconShop_HERO_01_Buddy_e','TB_BaconShop_HERO_01_Buddy_G','TB_BaconShop_HERO_01_Buddy_G_e',
	#20#Elise Starseeker
	'TB_BaconShop_HERO_42','TB_BaconShop_HP_047','TB_BaconShop_HP_047t','TB_BaconShop_HERO_42_Buddy','TB_BaconShop_HERO_42_Buddy_e','TB_BaconShop_HERO_42_Buddy_G','TB_BaconShop_HERO_42_Buddy_G_e',
#21#Forest Warden Omu
#22#Fungalmancer Flurgl
#23#Galakrond
#24#Galewing
#25#George the Fallen
#26#Greybough
#27#Guff Runetotem
#28#Illidan Stormrage
#29#Infinite Toki
#30#Jandice Barov
#31#Kael'thas Sunstrider
#32#King Mukla
#33#Kurtrus Ashfallen
#34#Lich Baz'hial
#35#Lord Barov

]
BG_PoolSet_Hero2=[
	'BG22_HERO_002',
	'TB_BaconShop_HERO_01',
	]

BG_Hero2_Buddy={
	'BG22_HERO_002':'BG22_HERO_002_Buddy',
	'TB_BaconShop_HERO_01':'TB_BaconShop_HERO_01_Buddy',
	}

BG_Hero2_Buddy_Gold={
	'BG22_HERO_002_Buddy':'BG22_HERO_002_Buddy_G',
	'TB_BaconShop_HERO_01_Buddy':'TB_BaconShop_HERO_01_Buddy_G',
	}

############ source ################################################

#BG22_HERO_002#Drek'Thar
#18	#Drek'Thar#BG22_HERO_002
class BG22_HERO_002:# <12>[1453]
	""" Drek'Thar 	 """
class BG22_HERO_002p_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		controller = target.controller
		Buff(target.buff).trigger(controller)
		buffcard = target.buffs[-1]
		highest_atk = 0
		for card in controller.field:
			if highest_atk <card.atk:
				highest_atk = card.atk
		buffcard.atk = SET(highest_atk)
class BG22_HERO_002p:# <12>[1453]
	""" Lead the Frostwolves
	Choose a friendly minion.It copies the Attack of your highest Attack minion for next combat only. """
	requirements = {PlqyReq.REQ_TARGET_TO_PLAY:0, PlqyReq.REQ_FRIENDLY_TARGET:0, PlqyReq.REQ_MINIONS_TARGET:0}
	activate = BG22_HERO_002p_Action(TARGET, 'BG22_HERO_002pe')
	pass
class BG22_HERO_002pe:# <12>[1453]
	""" Frostwolf Fervor
	Copied highest Attack. """
	events = EndBattle(CONTROLLER).Destroy(SELF)
	pass
class BG22_HERO_002pe2:# <12>[1453]
	""" Attack Set Next Combat Only
	 """
	pass
class BG22_HERO_002pe3:# <12>[1453]
	""" Modified Attack Next Combat Only
	Attack is increased or decreased for next combat only. """
	pass
class BG22_HERO_002_Buddy:# <12>[1453]
	""" Frostwolf Lieutenant
	[Avenge (2):] Give your minions +1 Attack permanently. """
	events=Death(FRIENDLY + MINION).on(Avenge(SELF, 2, [BuffPermanently(FRIENDLY_MINIONS, 'BG22_HERO_002_Buddy_e')]))
	pass
BG22_HERO_002_Buddy_e=buff(1,0)# <12>[1453]
""" Lieutenant's Leadership, +1 Attack. """
class BG22_HERO_002_Buddy_G:# <12>[1453]
	""" Frostwolf Lieutenant
	[Avenge (2):] Give your minions +2 Attack permanently. """
	events=Death(FRIENDLY + MINION).on(Avenge(SELF, 2, [BuffPermanently(FRIENDLY_MINIONS, 'BG22_HERO_002_Buddy_Ge')]))
	pass
BG22_HERO_002_Buddy_Ge=buff(2,0)# <12>[1453]
""" Lieutenant's Leadership,+2 Attack. """




#19#Edwin VanCleef
class TB_BaconShop_HERO_01:# <12>[1453]
	""" Edwin VanCleef  """
class TB_BaconShop_HP_001:
	""" Sharpen Blades 
	Give a friendly minion +2/+1 for each minion _you've bought this turn."""
class TB_BaconShop_HP_001e:
	pass
class TB_BaconShop_HERO_01_Buddy:# <12>[1453]
	""" SI:7 Scout
	After you buy a minion, gain +1/+1. """
	#
	pass
TB_BaconShop_HERO_01_Buddy_e=buff(1,1)# <12>[1453]
""" Scouting +1/+1. """
class TB_BaconShop_HERO_01_Buddy_G:# <12>[1453]
	""" SI:7 Scout
	After you buy a minion, gain +2/+2. """
	#
	pass
TB_BaconShop_HERO_01_Buddy_G_e=buff(2,2)# <12>[1453]
""" Scouting +2/+2. """




#20#Elise Starseeker
class TB_BaconShop_HERO_42:# <12>[1453]
	""" Elise Starseeker """
class TB_BaconShop_HP_047:
	""" Lead Explorer
	&lt;b&gt;Passive&lt;/b&gt; When you upgrade  Bob's Tavern get a 'Recruitment Map'."""
class TB_BaconShop_HP_047t:
	""" Recruitment Map
	&lt;b&gt;Discover&lt;/b&gt; a minion from &lt;b&gt;Tavern Tier @&lt;/b&gt;."""
class TB_BaconShop_HERO_42_Buddy:# <12>[1453]
	""" Jr. Navigator
	At the start of your turn,get a 'Recruitment Map.'Your Maps cost (1). """
	#
	pass
TB_BaconShop_HERO_42_Buddy_e=buff(cost=-1)# <12>[1453]
""" In The Distance,	Costs (1) less. """
class TB_BaconShop_HERO_42_Buddy_G:# <12>[1453]
	""" Jr. Navigator
	At the start of your turn,get 2 'Recruitment Maps.'Your Maps cost (1). """
	#
	pass
TB_BaconShop_HERO_42_Buddy_G_e=buff(cost=-2)# <12>[1453]
""" In The Distance, 	Costs (2) less. """



#21#Forest Warden Omu
class TB_BaconShop_HERO_74:# <12>[1453]
	""" Forest Warden Omu  """
class TB_BaconShop_HP_082:
	""" Everbloom
	&lt;b&gt;Passive&lt;/b&gt; After you upgrade Bob's Tavern, gain 2 Gold this turn only."""
class TB_BaconShop_HERO_74_Buddy:# <12>[1453]
	""" Evergreen Botani
	At the end of your turn, adda random minion of your_Tavern Tier to your hand. """
	#
	pass
class TB_BaconShop_HERO_74_Buddy_e:# <10>[1453]
	""" Evergreen Increased stats. """
class TB_BaconShop_HERO_74_Buddy_G:# <12>[1453]
	""" Evergreen Botani
	At the end of your turn, add2 random minions of your_Tavern Tier to your hand. """
	#
	pass


#22#Fungalmancer Flurgl
class TB_BaconShop_HERO_55:# <12>[1453]
	""" Fungalmancer Flurgl  """
	pass
class TB_BaconShop_HP_056:
	""" Gone Fishing
	&lt;b&gt;Passive&lt;/b&gt; After you sell a minion, add a random Murloc to Bob's Tavern."""
	pass
class TB_BaconShop_HERO_55_Buddy:
	pass
class TB_BaconShop_HERO_55_Buddy_G:
	pass



#23#Galakrond
class TB_BaconShop_HERO_02:# <12>[1453]
	""" Galakrond """
class TB_BaconShop_HP_011:
	""" Galakrond's Greed
	Choose a minion in Bob's Tavern. &lt;b&gt;Discover&lt;/b&gt; a higher Tier minion to replace it."""
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



#24#Galewing
class BG20_HERO_283:# <12>[1453]
	""" Galewing """
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
BG20_HERO_283p_t1e=buff(1,0)# <12>[1453]
""" Westfall,	+2 Attack. """
class BG20_HERO_283p_t2:# <12>[1453]
	""" Ironforge
	[Passive.] In 3 turns,[Discover] a minion of yourTavern Tier. <i>(@ left!)</i> """
	#
	pass
class BG20_HERO_283p_t3:# <12>[1453]
	""" Eastern Plaguelands
	[Passive.] In 5 turns, your next Tavern Tier upgrade costs (5) less. <i>(@ left!)</i> """
	#
	pass
class BG20_HERO_283_Buddy:# <12>[1453]
	""" Flight Trainer
	At the end of your turn, progress your flight path by_1 turn. """
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



#25#George the Fallen
class TB_BaconShop_HERO_15:# <12>[1453]
	""" George the Fallen  """
class TB_BaconShop_HP_010:
	""" Boon of Light
	Give a minion &lt;b&gt;Divine Shield&lt;/b&gt;."""
	## divine shield without buff
class TB_BaconShop_HERO_15_Buddy:# <12>[1453]
	""" Karl the Lost
	After you use your Hero Power, give your [Divine Shield] minions +2_Attack. """
	#
	pass
TB_BaconShop_HERO_15_Buddy_e=buff(2,0)# <12>[1453]
""" Lost and Found,	+2 Attack. """
class TB_BaconShop_HERO_15_Buddy_G:# <12>[1453]
	""" Karl the Lost
	After you use your Hero Power, give your [Divine Shield] minions +4_Attack. """
	#
	pass
TB_BaconShop_HERO_15_Buddy_G_e=buff(4,0)# <12>[1453]
""" Lost and Found,	+4 Attack. """




#26#Greybough
class TB_BaconShop_HERO_95:# <12>[1453]
	""" Greybough  """
class TB_BaconShop_HP_107:
	""" Sprout It Out!
	&lt;b&gt;Passive&lt;/b&gt; Give +1/+2 and &lt;b&gt;Taunt&lt;/b&gt; to minions you summon during combat."""
	pass
class TB_BaconShop_HP_107e:
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



#27#Guff Runetotem
class BG20_HERO_242:# <2>[1453]
	""" Guff Runetotem """
class BG20_HERO_242p:# <2>[1453]
	""" Natural Balance
	Give a friendly minion of each Tavern Tier +1/+1. """
	#
	pass
class BG20_HERO_242pe:# <12>[1453]
	""" Guff's Buff
	+1/+1. """
	#
	pass
class BG20_HERO_242_Buddy:
	pass
class BG20_HERO_242_Buddy_G:
	pass


#28#Illidan Stormrage
class TB_BaconShop_HERO_08:# <12>[1453]
	""" Illidan Stormrage  """
class TB_BaconShop_HP_069:
	""" Wingmen
	&lt;b&gt;Passive.&lt;/b&gt; &lt;b&gt;Start of Combat:&lt;/b&gt; Your left and right-most minions gain +2 Attack __and attack immediately. """
	pass
TB_BaconShop_HP_069e=buff(2,0)
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




#29#Infinite Toki
class TB_BaconShop_HERO_28:# <12>[1453]
	""" Infinite Toki  """





#30#Jandice Barov


#31#Kael'thas Sunstrider


#32#King Mukla


#33#Kurtrus Ashfallen
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

#34#Lich Baz'hial
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


#35#Lord Barov





###############################


