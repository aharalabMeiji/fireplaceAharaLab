from ast import Return
from ..utils import *

BG_Hero2=[
	'BG22_HERO_002','BG22_HERO_002p','BG22_HERO_002pe','BG22_HERO_002_Buddy','BG22_HERO_002_Buddy_e','BG22_HERO_002_Buddy_G','BG22_HERO_002_Buddy_Ge',	#17	#Drek'Thar#BG22_HERO_002
	'TB_BaconShop_HERO_01','TB_BaconShop_HP_001','TB_BaconShop_HP_001e','TB_BaconShop_HERO_01_Buddy','TB_BaconShop_HERO_01_Buddy_e','TB_BaconShop_HERO_01_Buddy_G','TB_BaconShop_HERO_01_Buddy_G_e',	#18#Edwin VanCleef
	'TB_BaconShop_HERO_42','TB_BaconShop_HP_047','TB_BaconShop_HP_047t','TB_BaconShop_HERO_42_Buddy','TB_BaconShop_HERO_42_Buddy_e','TB_BaconShop_HERO_42_Buddy_G','TB_BaconShop_HERO_42_Buddy_G_e',	#19#Elise Starseeker
	'TB_BaconShop_HERO_74','TB_BaconShop_HP_082','TB_BaconShop_HERO_74_Buddy','TB_BaconShop_HERO_74_Buddy_e','TB_BaconShop_HERO_74_Buddy_G',	#20#Forest Warden Omu
	'TB_BaconShop_HERO_55','TB_BaconShop_HP_056','TB_BaconShop_HERO_55_Buddy','TB_BaconShop_HERO_55_Buddy_G',	#21#Fungalmancer Flurgl
	'TB_BaconShop_HERO_02','TB_BaconShop_HP_011','TB_BaconShop_HERO_02_Buddy','TB_BaconShop_HERO_02_Buddy_G',	#22#Galakrond
	'BG20_HERO_283','BG20_HERO_283p','BG20_HERO_283p_t1','BG20_HERO_283p_t1e','BG20_HERO_283p_t2','BG20_HERO_283p_t3','BG20_HERO_283_Buddy','BG20_HERO_283_Buddy_e','BG20_HERO_283_Buddy_G','BG20_HERO_283_Buddy_G_e',	#23#Galewing
	'TB_BaconShop_HERO_15','TB_BaconShop_HP_010','TB_BaconShop_HERO_15_Buddy','TB_BaconShop_HERO_15_Buddy_e','TB_BaconShop_HERO_15_Buddy_G','TB_BaconShop_HERO_15_Buddy_G_e',	#24#George the Fallen
	'TB_BaconShop_HERO_95','TB_BaconShop_HP_107','TB_BaconShop_HP_107e','TB_BaconShop_HERO_95_Buddy','TB_BaconShop_HERO_95_Buddy_e','TB_BaconShop_HERO_95_Buddy_G','TB_BaconShop_HERO_95_Buddy_G_e',	#25#Greybough
	'BG20_HERO_242','BG20_HERO_242p','BG20_HERO_242pe','BG20_HERO_242_Buddy','BG20_HERO_242_Buddy_G',	#26#Guff Runetotem
	'TB_BaconShop_HERO_08','TB_BaconShop_HP_069','TB_BaconShop_HP_069e','TB_BaconShop_HERO_08_Buddy','TB_BaconShop_HERO_08_Buddy_e','TB_BaconShop_HERO_08_Buddy_G',	#27#Illidan Stormrage
	'TB_BaconShop_HERO_28','TB_BaconShop_HP_028','TB_BaconShop_HERO_28_Buddy','TB_BaconShop_HERO_28_Buddy_G',	#28#Infinite Toki
	'TB_BaconShop_HERO_71','TB_BaconShop_HP_084','TB_BaconShop_HERO_71_Buddy','TB_BaconShop_HERO_71_Buddy_e','TB_BaconShop_HERO_71_Buddy_G',	#29#Jandice Barov
	'TB_BaconShop_HERO_60','TB_BaconShop_HP_066','TB_BaconShop_HP_066e','TB_BaconShop_HERO_60_Buddy','TB_BaconShop_HERO_60_Buddy_e','TB_BaconShop_HERO_60_Buddy_G','TB_BaconShop_HERO_60_Buddy_G_e',	#30#Kael'thas Sunstrider
	'TB_BaconShop_HERO_38','TB_BaconShop_HP_038','DMF_065t','DMF_065e','TB_BaconShop_HERO_38_Buddy','TB_BaconShop_HERO_38_Buddy_e','TB_BaconShop_HERO_38_Buddy_G','TB_BaconShop_HERO_38_Buddy_Ge',	#31#King Mukla
	'BG20_HERO_280','BG20_HERO_280e','BG20_HERO_280p','BG20_HERO_280pe','BG20_HERO_280p2','BG20_HERO_280p2e','BG20_HERO_280p2e2','BG20_HERO_280p3','BG20_HERO_280p3e2','BG20_HERO_280_Buddy','BG20_HERO_280_Buddye','BG20_HERO_280_Buddy_G','BG20_HERO_280_Buddye2',	#32#Kurtrus Ashfallen
	'TB_BaconShop_HERO_25','TB_BaconShop_HP_049','TB_BaconShop_HERO_25_Buddy','TB_BaconShop_HERO_25_Buddy_e','TB_BaconShop_HERO_25_Buddy_G','TB_BaconShop_HERO_25_Buddy_Ge',	#33#Lich Baz'hial
	'TB_BaconShop_HERO_72','TB_BaconShop_HP_081','TB_BaconShop_HERO_72_Buddy','TB_BaconShop_HERO_72_Buddy_G',	#34#Lord Barov

]
BG_PoolSet_Hero2=[
	'BG22_HERO_002',#17
	'TB_BaconShop_HERO_01',#18
	'TB_BaconShop_HERO_42',#19
	'TB_BaconShop_HERO_74',#20
	'TB_BaconShop_HERO_55',#21#21 Murloc ban
	'TB_BaconShop_HERO_02',#22
	#'BG20_HERO_283',#23#23 XX
	'TB_BaconShop_HERO_15',#24
	'TB_BaconShop_HERO_95',#25
	'BG20_HERO_242',#26
	'TB_BaconShop_HERO_08',#27
	'TB_BaconShop_HERO_28',#28
	'TB_BaconShop_HERO_71',#29
	'TB_BaconShop_HERO_60',#30
	'TB_BaconShop_HERO_38',#31
	'BG20_HERO_280',#32
	'TB_BaconShop_HERO_25',#33
	#'TB_BaconShop_HERO_72',#34#34 XimpossibleXXX
	]

BG_Hero2_Buddy={
	'BG22_HERO_002':'BG22_HERO_002_Buddy',
	'TB_BaconShop_HERO_01':'TB_BaconShop_HERO_01_Buddy',
	'TB_BaconShop_HERO_42':'TB_BaconShop_HERO_42_Buddy',
	'TB_BaconShop_HERO_74':'TB_BaconShop_HERO_74_Buddy',
	'TB_BaconShop_HERO_55':'TB_BaconShop_HERO_55_Buddy',
	'TB_BaconShop_HERO_02':'TB_BaconShop_HERO_02_Buddy',
	'BG20_HERO_283':'BG20_HERO_283_Buddy',
	'TB_BaconShop_HERO_15':'TB_BaconShop_HERO_15_Buddy',
	'TB_BaconShop_HERO_95':'TB_BaconShop_HERO_95_Buddy',
	'BG20_HERO_242':'BG20_HERO_242_Buddy',
	'TB_BaconShop_HERO_08':'TB_BaconShop_HERO_08_Buddy',
	'TB_BaconShop_HERO_28':'TB_BaconShop_HERO_28_Buddy',
	'TB_BaconShop_HERO_71':'TB_BaconShop_HERO_71_Buddy',
	'TB_BaconShop_HERO_60':'TB_BaconShop_HERO_60_Buddy',
	'TB_BaconShop_HERO_38':'TB_BaconShop_HERO_38_Buddy',
	'BG20_HERO_280':'BG20_HERO_280_Buddy',
	'TB_BaconShop_HERO_25':'TB_BaconShop_HERO_25_Buddy',
	'TB_BaconShop_HERO_72':'TB_BaconShop_HERO_72_Buddy',
	}

BG_Hero2_Buddy_Gold={
	'BG22_HERO_002_Buddy':'BG22_HERO_002_Buddy_G',
	'TB_BaconShop_HERO_01_Buddy':'TB_BaconShop_HERO_01_Buddy_G',
	'TB_BaconShop_HERO_42_Buddy':'TB_BaconShop_HERO_42_Buddy_G',
	'TB_BaconShop_HERO_74_Buddy':'TB_BaconShop_HERO_74_Buddy_G',
	'TB_BaconShop_HERO_55_Buddy':'TB_BaconShop_HERO_55_Buddy_G',
	'TB_BaconShop_HERO_02_Buddy':'TB_BaconShop_HERO_02_Buddy_G',
	'BG20_HERO_283_Buddy':'BG20_HERO_283_Buddy_G',
	'TB_BaconShop_HERO_15_Buddy':'TB_BaconShop_HERO_15_Buddy_G',
	'TB_BaconShop_HERO_95_Buddy':'TB_BaconShop_HERO_95_Buddy_G',
	'BG20_HERO_242_Buddy':'BG20_HERO_242_Buddy_G',
	'TB_BaconShop_HERO_08_Buddy':'TB_BaconShop_HERO_08_Buddy_G',
	'TB_BaconShop_HERO_28_Buddy':'TB_BaconShop_HERO_28_Buddy_G',
	'TB_BaconShop_HERO_71_Buddy':'TB_BaconShop_HERO_71_Buddy_G',
	'TB_BaconShop_HERO_60_Buddy':'TB_BaconShop_HERO_60_Buddy_G',
	'TB_BaconShop_HERO_38_Buddy':'TB_BaconShop_HERO_38_Buddy_G',
	'BG20_HERO_280_Buddy':'BG20_HERO_280_Buddy_G',
	'TB_BaconShop_HERO_25_Buddy':'TB_BaconShop_HERO_25_Buddy_G',
	'TB_BaconShop_HERO_72_Buddy':'TB_BaconShop_HERO_72_Buddy_G',
	}

############ source ################################################

#17	#Drek'Thar#BG22_HERO_002   ### HP OK ###
class BG22_HERO_002:# <12>[1453]
	""" Drek'Thar 	 """
class BG22_HERO_002p_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		controller = target.controller
		highest_atk = 0
		for card in controller.field:
			if highest_atk <card.atk:
				highest_atk = card.atk
		Buff(target, buff, atk=highest_atk-target.atk).trigger(controller)
class BG22_HERO_002p:# <12>[1453]
	""" Lead the Frostwolves
	Choose a friendly minion.It copies the Attack of your highest Attack minion for next combat only. (until 23.4.3)
	Choose a minion. It copies the Attack of the highest Attack minion until next turn.
	"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, 
				 #PlayReq.REQ_FRIENDLY_TARGET:0, ## valid until 23.4.3 
				 PlayReq.REQ_MINION_TARGET:0}
	activate = BG22_HERO_002p_Action(TARGET, 'BG22_HERO_002pe')
	pass
class BG22_HERO_002pe:# <12>[1453]
	""" Frostwolf Fervor
	Copied highest Attack. """
	events = EndBattle(CONTROLLER).on(Destroy(SELF))
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




#18#Edwin VanCleef ### HP OK ###
class TB_BaconShop_HERO_01:# <12>[1453]
	""" Edwin VanCleef  """
class TB_BaconShop_HP_001_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = source.controller
		amount = len(controller.buy_this_turn_log())
		if amount>0:
			Buff(target, 'TB_BaconShop_HP_001e', 
				atk=2*amount, max_health=amount
				).trigger(source)
		pass
class TB_BaconShop_HP_001:
	""" Sharpen Blades 
	Give a friendly minion +2/+1 for each minion _you've bought this turn."""
	requirements = {
		PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0
		}
	activate = TB_BaconShop_HP_001_Action(TARGET)
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




#19#Elise Starseeker #### HP OK ###
class TB_BaconShop_HERO_42:# <12>[1453]
	""" Elise Starseeker """
class TB_BaconShop_HP_047:
	""" Lead Explorer
	<b>Passive</b> When you upgrade  Bob's Tavern get a 'Recruitment Map'."""
	events = UpgradeTier(CONTROLLER).after(Give(CONTROLLER, 'TB_BaconShop_HP_047t').then(SetScriptDataNum1(Give.CARD, TIER(CONTROLLER))))
class TB_BaconShop_HP_047t_Choice(Choice):
	def choose(self, card):
		super().choose(card)
		card.BG_cost=self.player.game.minionCost
		card.controller = self.player
		card.zone=Zone.HAND
class TB_BaconShop_HP_047t:
	""" Recruitment Map
	<b>Discover</b> a minion from <b>Tavern Tier @</b>."""
	play = TB_BaconShop_HP_047t_Choice(CONTROLLER, RandomBGMinion(tech_level=TIER(CONTROLLER))*3)
	# Here we activate 'choicecard.BG_cost = bar.cardCost'
######## BUDDY
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



#20#Forest Warden Omu #### HP OK ###
class TB_BaconShop_HERO_74:# <12>[1453]
	""" Forest Warden Omu  """
class TB_BaconShop_HP_082:
	""" Everbloom
	<b>Passive</b> After you upgrade Bob's Tavern, gain 2 Gold this turn only."""
	events = UpgradeTier(CONTROLLER).after(ManaThisTurnOnly(CONTROLLER,2))
######## BUDDY
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


#21#Fungalmancer Flurgl ### OK ###
class TB_BaconShop_HERO_55:# <12>[1453]
	""" Fungalmancer Flurgl  """
	pass
class TB_BaconShop_HP_056:
	""" Gone Fishing
	<b>Passive</b> After you sell two minions, add a random Murloc to Bob's Tavern."""
	events = Sell(CONTROLLER).on(SidequestCounter(SELF, 2, 
		[Summon(OPPONENT, RandomBGMurloc(tech_level_less=TIER(CONTROLLER)))] #
	))
	pass
######## BUDDY
class TB_BaconShop_HERO_55_Buddy:
	pass
class TB_BaconShop_HERO_55_Buddy_G:
	pass



#22#Galakrond  ### HP OK ###
class TB_BaconShop_HERO_02:# <12>[1453]
	""" Galakrond """
class TB_BaconShop_HP_011_Choice(Choice):
	def choose(self, card):
		super().choose(card)
		card.controller = card.controller.opponent# bartender
		card.zone=Zone.PLAY
class TB_BaconShop_HP_011_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source,target):
		controller = source.controller
		tier = min(target.tech_level+1,6)
		target.zone = Zone.GRAVEYARD ### let deathrattle does not happen
		TB_BaconShop_HP_011_Choice(controller, RandomBGMinion(tech_level=tier)*3).trigger(source)
class TB_BaconShop_HP_011:
	""" Galakrond's Greed
	Choose a minion in Bob's Tavern. <b>Discover</b> a higher Tier minion to replace it."""
	requirements = {
		PlayReq.REQ_TARGET_TO_PLAY:0,
		PlayReq.REQ_ENEMY_TARGET:0,
		PlayReq.REQ_MINION_TARGET:0,
		}
	activate = TB_BaconShop_HP_011_Action(TARGET)
	pass
######## BUDDY
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



#23#Galewing   ### under construction ###
class BG20_HERO_283:# <12>[1453]
	""" Galewing """
class BG20_HERO_283p:# <12>[1453]
	""" Dungar's Gryphon
	Choose a flightpath. Complete it to get a bonus! """
	entourage=['BG20_HERO_283p_t1','BG20_HERO_283p_t2','BG20_HERO_283p_t3']
	activate = GenericChoiceChangeHeropower(CONTROLLER, RandomEntourage()*3)
	pass
class BG20_HERO_283p_t1:# <12>[1453]
	""" Westfall
	[Passive.] In 1 turn, give your left-most minion+2 Attack. <i>(@ left!)</i> """
	#
	pass
BG20_HERO_283p_t1e=buff(2,0)# <12>[1453]
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
######## BUDDY
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



#24#George the Fallen #### OK ####
class TB_BaconShop_HERO_15:# <12>[1453]
	""" George the Fallen  """
class TB_BaconShop_HP_010:
	""" Boon of Light
	Give a minion <b>Divine Shield</b>."""
	## divine shield without buff
	requirements = {
		PlayReq.REQ_TARGET_TO_PLAY:0,
		PlayReq.REQ_FRIENDLY_TARGET:0,
		PlayReq.REQ_MINION_TARGET:0,
		}
	activate = GiveDivineShield(TARGET)
######## BUDDY
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



from fireplace.battlegrounds.BG_bar import BG_Bar

#25#Greybough  ### HP OK ###
class TB_BaconShop_HERO_95:# <12>[1453]
	""" Greybough  """
class TB_BaconShop_HP_107_Action(TargetedAction):
	TARGET=ActionArg()
	def do(delf, source, target):
		controller = source.controller
		if isinstance(controller.game, BG_Bar):
			return
		Buff(target, 'TB_BaconShop_HP_107e').trigger(source)
class TB_BaconShop_HP_107:
	""" Sprout It Out!
	<b>Passive</b> Give +1/+2 and <b>Taunt</b> to minions you summon during combat."""
	events = Summon(CONTROLLER, FRIENDLY + MINION).on(TB_BaconShop_HP_107_Action(Summon.CARD))
TB_BaconShop_HP_107e=buff(1,2,taunt=True)
######## BUDDY
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



#26#Guff Runetotem  ### HP OK ###
class BG20_HERO_242:# <2>[1453]
	""" Guff Runetotem """
class BG20_HERO_242p:# <2>[1453]
	""" Natural Balance
	Give a friendly minion of each Tavern Tier +1/+1. """
	def activate(self):
		controller = self.controller
		field = copy(controller.field)
		random.shuffle(field)
		tiers=[]
		cards=[]
		for card in field:
			if tiers==[] or not card.tech_level in tiers:
				tiers.append(card.tech_level)
				cards.append(card)
		for card in cards:
			Buff(card, 'BG20_HERO_242pe').trigger(self)
		pass
	pass
#BG20_HERO_242pe=buff(1,1)# <12>[1453] ## until 23.4.3
BG20_HERO_242pe=buff(2,3)### after 23.6
""" Guff's Buff,	+1/+1. """
######## BUDDY
class BG20_HERO_242_Buddy:
	pass
class BG20_HERO_242_Buddy_G:
	pass



#27#Illidan Stormrage  ### HP, maybe OK ###
class TB_BaconShop_HERO_08:# <12>[1453]
	""" Illidan Stormrage  """
class TB_BaconShop_HP_069_Action(TargetedAction):
	CONTROLLER = ActionArg()
	def do(self, source, controller):
		field = controller.field
		op_field = controller.opponent.field
		if len(op_field)==0:
			return
		if len(field)>0:
			left = field[0]
			right = field[-1]
			Buff(left, 'TB_BaconShop_HP_069e').trigger(source)
			BG_Attack(left, random.choice(op_field)).trigger(source)
			if right!=left:
				Buff(left, 'TB_BaconShop_HP_069e').trigger(source)
				BG_Attack(right, random.choice(op_field)).trigger(source)
class TB_BaconShop_HP_069:
	""" Wingmen
	<b>Passive.</b> <b>Start of Combat:</b> Your left and right-most minions gain +2 Attack __and attack immediately. """
	events = BeginBattle(CONTROLLER).on(TB_BaconShop_HP_069_Action(CONTROLLER))
	pass
TB_BaconShop_HP_069e=buff(2,0)
######## BUDDY
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




#28#Infinite Toki  ### OK ###
class TB_BaconShop_HERO_28:# <12>[1453]
	""" Infinite Toki  """
class TB_BaconShop_HP_028_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		bartender = controller.opponent
		Rerole(controller).trigger(controller)
		tier=controller.tavern_tier+1## 
		if tier==7:
			tier=6
		cardID = random.choice(controller.game.parent.BG_decks[tier])
		card = bartender.card(cardID)
		card.controller = bartender
		card.zone = Zone.PLAY
		controller.game.parent.BG_decks[tier].remove(cardID)
class TB_BaconShop_HP_028:
	"""  Temporal Tavern
	<b>Refresh</b> Bob's Tavern. Include a minion from a higher Tavern Tier."""
	activate = TB_BaconShop_HP_028_Action(CONTROLLER)
	pass
######## BUDDY
class TB_BaconShop_HERO_28_Buddy:# <12>[1453]
	""" Clockwork Assistant
	<b>Battlecry:</b> <b>Discover</b> a minion from a higher Tavern Tier. """
	play = Discover(CONTROLLER, RandomBGMinion(tech_level=(TIER(CONTROLLER)+1)))
	pass
class TB_BaconShop_HERO_28_Buddy_G:# <12>[1453]
	"""
	&lt;b&gt;Battlecry:&lt;/b&gt; &lt;b&gt;Discover&lt;/b&gt; two minions from a higher Tavern Tier."""
	play = DiscoverTwice(CONTROLLER, RandomBGMinion(tech_level=(TIER(CONTROLLER)+1))*3)
	pass





#29#Jandice Barov #### OK ####
class TB_BaconShop_HERO_71:# <12>[1453]
	""" Jandice Barov """
class TB_BaconShop_HP_084:
	""" Swap, Lock, &amp; Shop It
	Swap a friendly non-golden minion with a random one in Bob's Tavern."""
	requirements = {
		PlayReq.REQ_TARGET_TO_PLAY:0,
		PlayReq.REQ_FRIENDLY_TARGET:0,
		PlayReq.REQ_MINION_TARGET:0,
		}
	def activate(self):
		controller = self.controller
		bartender = controller.opponent
		target = self.target ## minion
		if bartender.field==[]:
			return 
		card = random.choice(bartender.field)
		target.zone=Zone.GRAVEYARD
		card.zone=Zone.GRAVEYARD
		target.controller = bartender
		for buff in target.buffs:
			buff.zone=Zone.REMOVEDFROMGAME
		card.controller = controller
		target.zone=Zone.PLAY
		card.zone=Zone.PLAY
	pass
######## BUDDY
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



#30#Kael'thas Sunstrider  ### OK ###
class TB_BaconShop_HERO_60:# <12>[1453]
	""" Kael'thas Sunstrider """
class TB_BaconShop_HP_066:
	""" Verdant Spheres
	<b>Passive</b> Every third minion you buy gains +2/+2."""
	events = Buy(CONTROLLER).on(SidequestCounter(SELF, 3, [Buff(Buy.CARD, 'TB_BaconShop_HP_066e' )]))
TB_BaconShop_HP_066e=buff(2,2)
######## BUDDY
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




#31#King Mukla  #### half OK  ####
class TB_BaconShop_HERO_38:# <12>[1453]
	""" King Mukla  """
class TB_BaconShop_HP_038_Action(TargetedAction):
	TARGET=ActionArg()
	COIN=ActionArg()
	def do(self, source, target, coin):
		gamemaster = source.controller.game.parent
		for bar in gamemaster.BG_Bars:
			player = bar.controller
			if player != source.controller:
				player.gifts.append(coin)
		pass
class TB_BaconShop_HP_038:
	""" Bananarama
	Get 2 Bananas. At the end of your turn, _give everyone else one."""
	activate = Give(CONTROLLER, random.choice(['DMF_065t', 'BGS_Treasures_000'])), Give(CONTROLLER, random.choice(['DMF_065t', 'BGS_Treasures_000'])), TB_BaconShop_HP_038_Action(CONTROLLER, 'DMF_065t')
	pass
TB_BaconShop_HP_038e=buff(1,1)## no use
class DMF_065t:### alternative TB_BaconShop_HP_038t
	""" Wild Banana
	Give a friendly minion +1/+1. """
	requirements = { PlayReq.REQ_TARGET_TO_PLAY:0,  PlayReq.REQ_MINION_TARGET:0,  PlayReq.REQ_FRIENDLY_TARGET:0 }
	play = ApplyBanana(TARGET, 'DMF_065e')
DMF_065e=buff(1,1)## 
######## BUDDY
class TB_BaconShop_HERO_38_Buddy:# <12>[1453]
	""" Crazy Monkey
	After you feed a minion a Banana, give it +1/+1."""
	events = ApplyBanana(FRIENDLY + MINION).after(Buff(ApplyBanana.TARGET, 'TB_BaconShop_HERO_38_Buddy_e'))
	pass
TB_BaconShop_HERO_38_Buddy_e=buff(1,1)# <12>[1453] �o�i�i�̔�
""" Banana Peel,	+1/+1. """
class TB_BaconShop_HERO_38_Buddy_G:# <12>[1453]
	""" Crazy Monkey
	After you feed a minion a Banana, give it +2/+2."""
	events = ApplyBanana(FRIENDLY + MINION).after(Buff(ApplyBanana.TARGET, 'TB_BaconShop_HERO_38_Buddy_Ge'))
	pass
TB_BaconShop_HERO_38_Buddy_Ge=buff(2,2)# <12>[1453]



#32#Kurtrus Ashfallen  #### HP OK #### 
class BG20_HERO_280:# <14>[1453]
	""" Kurtrus Ashfallen """
class BG20_HERO_280e:# <12>[1453]
	""" Kurtrus Watcher """
class BG20_HERO_280p_Action1(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		source.sidequest_list0.append(target)
		source.script_data_num_1 -= 1
		if source.script_data_num_1<=0:
			for card in source.sidequest_list0:
				if card in source.controller.field or card in source.controller.hand:
					Buff(card, 'BG20_HERO_280pe').trigger(source)
			source.sidequest_list0=[]
			source.script_data_num_1 = 4
			ChangeHeroPower(CONTROLLER, 'BG20_HERO_280p2').trigger(source)
class BG20_HERO_280p_Action0(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		target.sidequest_list0=[]
		target.script_data_num_1=3
		pass
class BG20_HERO_280p:# <14>[1453]
	""" Final Showdown
	[Passive]Buy 3 minions in 1 turn to give them +2/+2 and_progress this. <i>(@ left!)</i> """
	events = [
		Buy(CONTROLLER).on(BG20_HERO_280p_Action1(Buy.CARD)),
		OWN_TURN_END.on(BG20_HERO_280p_Action0(SELF))
	]
	pass
BG20_HERO_280pe=buff(2,2)# <12>[1453]
""" Showdown Preparation+2/+2. """
class BG20_HERO_280p_Action2(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		source.sidequest_list0.append(target)
		source.script_data_num_1 -= 1
		if source.script_data_num_1<=0:
			for card in source.controller.field:
				Buff(card, 'BG20_HERO_280p2e').trigger(source)
			for card in source.controller.hand:
				Buff(card, 'BG20_HERO_280p2e').trigger(source)
			source.sidequest_list0=[]
			source.script_data_num_1 = 5
			ChangeHeroPower(CONTROLLER, 'BG20_HERO_280p3').trigger(source)
class BG20_HERO_280p_Action02(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		target.sidequest_list0=[]
		target.script_data_num_1=4
		pass
class BG20_HERO_280p2:# <14>[1453]
	""" Gain Momentum
	[Passive.] Buy 4 minions in1 turn to give your hand and board +2/+2 and_progress this. <i>(@ left!)</i> """
	events = [
		Buy(CONTROLLER).on(BG20_HERO_280p_Action2(Buy.CARD)),
		OWN_TURN_END.on(BG20_HERO_280p_Action02(SELF))
	]
	pass
BG20_HERO_280p2e=buff(2,2)# <12>[1453]
""" Momentum,	+2/+2. """
class BG20_HERO_280p2e2:# <12>[1453]
	""" Marked for Showdown,	Will be buffed by Final Showdown. """
class BG20_HERO_280p_Action3(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		source.sidequest_list0.append(target)
		source.script_data_num_1 -= 1
		if source.script_data_num_1<=0:
			for card in source.controller.field:
				Buff(card, 'BG20_HERO_280p3e2').trigger(source)
			for card in source.controller.hand:
				Buff(card, 'BG20_HERO_280p3e2').trigger(source)
			source.sidequest_list0=[]
			source.script_data_num_1 = 5
class BG20_HERO_280p_Action03(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		target.sidequest_list0=[]
		target.script_data_num_1=5
		pass
class BG20_HERO_280p3:# <14>[1453]
	""" Close the Portal
	[Passive.] Buy 5 minions in1 turn to give ALL yourminions this game +2/+2__and complete this. <i>({0} left!)</i>@[Passive.] Buy 5 minions in1 turn to give ALL yourminions this game +2/+2.<i>(Complete!)</i> """
	events = [
		Buy(CONTROLLER).on(BG20_HERO_280p_Action3(Buy.CARD)),
		OWN_TURN_END.on(BG20_HERO_280p_Action03(SELF))
	]
	pass
BG20_HERO_280p3e2=buff(2,2)# <12>[1453]
""" Portal Closure,	+2/+2 """
######## BUDDY
class BG20_HERO_280_Buddy:# <12>[1453]
	""" Living Nightmare
	After you buy a minion,minions in Bob's Tavern have +1/+1 this turn. """
	#
	pass
class BG20_HERO_280_Buddye:# <12>[1453]
	""" Living Nightmare Player Enchant Increased stats. """
	pass
class BG20_HERO_280_Buddy_G:# <12>[1453]
	""" Living Nightmare
	After you buy a minion,minions in Bob's Tavernhave +2/+2 this turn. """
	#
	pass
class BG20_HERO_280_Buddye2:# <12>[1453]
	""" Nightshot Increased stats. """
	pass




#33#Lich Baz'hial ### HP OK ###
class TB_BaconShop_HERO_25:# <12>[1453]
	""" Lich Baz'hial	 """
class TB_BaconShop_HP_049:
	""" Graveyard Shift
	Take $2_damage and add a Gold Coin to your hand."""
	activate = Hit(FRIENDLY_HERO, 2), Give(CONTROLLER, 'GAME_005')
	pass
######## BUDDY
class TB_BaconShop_HERO_25_Buddy:# <12>[1453]
	""" Unearthed Underling
	Whenever your hero takesdamage, this miniongains +3/+3 instead.<i>(@ left this turn.)</i> """
	#
	pass
TB_BaconShop_HERO_25_Buddy_e=buff(3,3)# <12>[1453]
""" Recovery,+3/+3. """
class TB_BaconShop_HERO_25_Buddy_G:# <12>[1453]
	""" Unearthed Underling
	Whenever your hero takesdamage, this miniongains +6/+6 instead.<i>(@ left this turn.)</i> """
	#
	pass
TB_BaconShop_HERO_25_Buddy_Ge=buff(6,6)# <12>[1453]
""" Recovery,+6/+6. """




#34#Lord Barov  #### impossible ###
class TB_BaconShop_HERO_72:# <12>[1453]
	""" Lord Barov	 """
class TB_BaconShop_HP_081:
	"""Friendly Wager
	Guess which player will win their next combat. _If they win, get 3 Coins."""
	#####################
######## BUDDY
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



###############################


