
from ..utils import *

BG_Refreshing_Anomaly=True ## (1)
BG_Sellemental=True ## (1)
BG_Bubblette=False ## (1) ## new 24.0 banned 24.2

BG_Molten_Rock=True ## (2)
BG_Party_Elemental=True ## (2)

BG_Crackling_Cyclone=True ## (3)
BG_Smogger=True ## (3)
BG_Stasis_Elemental=False ## (3) ## banned when?
BG25__Felemental=True# 3/3/1 elemental/demon ## new 25.2.2

BG_Dazzling_Lightspawn=True ## (4)
BG_Recycling_Wraith=True # (4)
BG_Wildfire_Elemental=True # (4)

BG_Tavern_Tempest=True # (5)
BG_Lil_Rag=True # (5)
BG25__Magmaloc=True# (5/1/1) murloc ## new 25.2.2

BG_Gentle_Djinni=True # (6)
BG_Lieutenant_Garr=True # (6)


BG_Minion_Elemental =[]
BG_PoolSet_Elemental=[[],[],[],[],[],[],[]]
BG_Elemental_Gold={}

#Refreshing Anomaly(1)  ### OK ###
if BG_Refreshing_Anomaly: # 
	BG_Minion_Elemental+=['BGS_116','TB_BaconUps_167']
	BG_PoolSet_Elemental[1].append('BGS_116')
	BG_Elemental_Gold['BGS_116']='TB_BaconUps_167'
class BGS_116:# <12>[1453] 
	""" Refreshing Anomaly
	[Battlecry:] Your next [Refresh] costs (0). """
	play = GetFreeRerole(CONTROLLER)
	pass
class TB_BaconUps_167:# <12>[1453]
	""" Refreshing Anomaly
	[Battlecry:] Your next two [Refreshes] cost (0). """
	play = GetFreeRerole(CONTROLLER) * 2
	pass


#Sellemental(1)  ### OK ###
if BG_Sellemental: # 
	BG_Minion_Elemental+=['BGS_115','BGS_115t','TB_BaconUps_156']
	BG_PoolSet_Elemental[1].append('BGS_115')
	BG_Elemental_Gold['BGS_115']='TB_BaconUps_156'
class BGS_115:# <12>[1453] ウレメンタル
	""" Sellemental
	When you sell this,add a 2/2 Elementalto your hand. """
	events = Sell(CONTROLLER, SELF).on(Give(CONTROLLER, 'BGS_115t'))
	pass
class BGS_115t:# <12>[1453] おつりちゃん
	""" Water Droplet  
	 """
	pass
class TB_BaconUps_156:# <12>[1453]
	""" Sellemental
	When you sell this,add two 2/2 Elementalsto your hand. """
	events = Sell(CONTROLLER, SELF).on(Give(CONTROLLER, 'BGS_115t') * 2)
	pass

if BG_Bubblette:
	BG_Minion_Elemental+=['BG_TID_713','BG_TID_713_G']
	BG_PoolSet_Elemental[1].append('BG_TID_713')
	BG_Elemental_Gold['BG_TID_713']='BG_TID_713_G'
class BG_TID_713:#あわわわ ## banned 24.2
	""" Bubblette
	After this minion takes  exactly one damage, destroy it. <i>(Pop!)</i>"""
	events = Damage(SELF, 1).on(Destroy(SELF))
class BG_TID_713_G:#あわわわ
	""" Bubblette
	After this minion takes  exactly two damage, destroy it. <i>(Pop!)</i>"""
	events = Damage(SELF, 2).on(Destroy(SELF))


##### tavern tier 2


if BG_Molten_Rock: # 
#Molten Rock(2)  ### MAYBE ###
	BG_Minion_Elemental+=['BGS_127','BGS_127e','TB_Baconups_202','TB_Baconups_202e']
	BG_PoolSet_Elemental[2].append('BGS_127')
	BG_Elemental_Gold['BGS_127']='TB_Baconups_202'
class BGS_127:# <12>[1453] ようがん
	""" Molten Rock
	[Taunt]. After you play an Elemental, gain +1 Health. """
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(Buff(SELF, 'BGS_127e'))
	pass
BGS_127e=buff(0,1)
class TB_Baconups_202:# <12>[1453]
	""" Molten Rock
	[Taunt]. After you play an Elemental, gain +2 Health. """
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(Buff(SELF, 'TB_Baconups_202e'))
	pass
TB_Baconups_202e=buff(0,2)



if BG_Party_Elemental: # ## MAYBE ###
#Party Elemental(2)  #(2/4/2)
	BG_Minion_Elemental+=['BGS_120','BGS_120e','TB_BaconUps_160']
	BG_PoolSet_Elemental[2].append('BGS_120')
	BG_Elemental_Gold['BGS_120']='TB_BaconUps_160'
class BGS_120:# <12>[1453]
	""" Party Elemental
	After you play an Elemental, give another random friendly Elemental +1/+1. """
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(Buff(RANDOM(FRIENDLY_MINIONS + ELEMENTAL - SELF), 'BGS_120e'))
	pass
BGS_120e=buff(1,1)
class TB_BaconUps_160:# <12>[1453]
	""" Party Elemental
	After you play an Elemental, give another random friendly Elemental +1/+1 twice. """
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(Buff(RANDOM(FRIENDLY_MINIONS + ELEMENTAL - SELF), 'BGS_120e') * 2)
	pass

#### tavern tier 3


if BG_Crackling_Cyclone: # 
#Crackling Cyclone(3)   ### OK ###
	BG_Minion_Elemental+=['BGS_119','TB_BaconUps_159']
	BG_PoolSet_Elemental[3].append('BGS_119')
	BG_Elemental_Gold['BGS_119']='TB_BaconUps_159'
class BGS_119:# <12>[1453] ばりばり
	""" Crackling Cyclone
	[Divine Shield][Windfury] """
	pass
class TB_BaconUps_159:# <12>[1453]
	""" Crackling Cyclone
	[Divine Shield][Mega-Windfury] """
	#<Tag enumID="189" name="WINDFURY" type="Int" value="3"/>
	pass


if BG_Smogger: # 
#Smogger(3)   ### need check ###
	BG_Minion_Elemental+=['BG21_021','BG21_021e','BG21_021_G',]
	BG_PoolSet_Elemental[3].append('BG21_021')
	BG_Elemental_Gold['BG21_021']='BG21_021_G'
class BG21_021:# <12>[1453]
	""" Smogger
	[Battlecry:] Give a friendly Elemental stats equal to your Tavern Tier. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0,
		PlayReq.REQ_TARGET_WITH_RACE:Race.ELEMENTAL,
		}
	def play(self):
		source = self
		target = self.target
		controller = self.controller
		tier = controller.tavern_tier
		if target:
			Buff(target, 'BG21_021e', atk=tier, max_health=tier).trigger(controller)
		pass
	pass
class BG21_021e:# <12>[1453]
	""" Smogged
	Increased stats. """
	pass
class BG21_021_G:# <12>[1453]
	""" Smogger
	[Battlecry:] Give a friendly Elemental stats equal to_your Tavern Tier twice. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0,
		PlayReq.REQ_TARGET_WITH_RACE:Race.ELEMENTAL,
		}
	def play(self):
		source = self
		target = self.target
		controller = self.controller
		tier = controller.tavern_tier
		if target:
			Buff(target, 'BG21_021e', atk=tier, max_health=tier).trigger(controller)
			Buff(target, 'BG21_021e', atk=tier, max_health=tier).trigger(controller)
		pass



#Stasis Elemental(3)   ### OK ###
if BG_Stasis_Elemental: # 
	BG_Minion_Elemental+=['BGS_122','TB_BaconUps_161']
	BG_PoolSet_Elemental[3].append('BGS_122')
	BG_Elemental_Gold['BGS_122']='TB_BaconUps_161'
class BGS_122:# <12>[1453] ###
	""" Stasis Elemental 
	[Battlecry:] Add another random Elemental to Bob's Tavern and [Freeze] it. """
	def play(self):
		bartender = self.controller.opponent
		tier = self.controller.tavern_tier
		elementals = []
		for gr in range(1, tier+1):
			elementals += BG_PoolSet_Elemental[gr]
		if 'BGS_122' in elementals:
			elementals.remove('BGS_122')
		if len(elementals)>0:
			newcard_id = random.choice(elementals)
			newcard = Summon(bartender,newcard_id).trigger(self)
			if newcard[0]==[]:
				return
			newcard[0][0].frozen=True
	pass
class TB_BaconUps_161:# <12>[1453]
	""" Stasis Elemental
	[Battlecry:] Add two other random Elementals to Bob's Tavern and [Freeze] them. """
	def play(self):
		bartender = self.controller.opponent
		tier = self.controller.tavern_tier
		elementals = []
		for gr in range(1, tier):
			elementals += BG_PoolSet_Elemental[gr]
		if 'BGS_122' in elementals:
			elementals.remove('BGS_122')
		if len(elementals)>0:		
			newcard_id = random.choice(elementals)
			newcard = Summon(bartender,newcard_id).trigger(self)
			if newcard[0]==[]:
				return
			newcard[0][0].frozen=True
			newcard_id = random.choice(elementals)
			newcard = Summon(bartender,newcard_id).trigger(self)
			if newcard[0]==[]:
				return
			newcard[0][0].frozen=True
	pass


if BG25__Felemental:# 3/3/1 elemental/demon ## new 25.2.2 ##
	BG_Minion_Elemental+=['BG25_041','BG25_041_G','BG25_041e','BG25_041e2']
	BG_PoolSet_Elemental[3].append('BG25_041')
	BG_Elemental_Gold['BG25_041']='BG25_041_G'
class BG25_041_Action(GameAction):
	def do(self, source):
		source.controller.felemental_powered_up+=1
class BG25_041:# (minion)
	""" Felemental
	<b>Battlecry:</b> Minions in Bob's Tavern have +1/+1 __for the rest of the game. """
	play = BG25_041_Action()
	pass
class BG25_041_G_Action(GameAction):
	def do(self, source):
		source.controller.felemental_powered_up+=2
class BG25_041_G:# (minion)
	""" Felemental
	<b>Battlecry:</b> Minions in Bob's Tavern have +2/+2 __for the rest of the game. """
	play = BG25_041_G_Action()
	pass
class BG25_041e:# (enchantment)
	""" Felfire Player Enchant
	Increased stats. """
	pass
class BG25_041e2:# (enchantment)
	""" Felementality
	Increased stats. """
	pass



#### tavern tier 4



#Dazzling Lightspawn(4) ### OK ###
if BG_Dazzling_Lightspawn: # 
	BG_Minion_Elemental+=['BG21_020','BG21_020e','BG21_020pe','BG21_020_G']
	BG_PoolSet_Elemental[4].append('BG21_020')
	BG_Elemental_Gold['BG21_020']='BG21_020_G'
class BG21_020_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		controller = target
		controller.lightspawn_powered_up += amount
		#buffsize=controller.lightspawn_powered_up
		#BG21_020pe.atk = lambda self,i:i+buffsize
		#BG21_020pe.max_health= lambda self,i:i+buffsize
class BG21_020:# <12>[1453] ライトスポーン
	""" Dazzling Lightspawn
	[Avenge (2):] Elementals inBob's Tavern have +1/+1__for the rest of the game. """
	events = Death(FRIENDLY).on(Avenge(SELF, 2, [BG21_020_Action(CONTROLLER, 1)]))
	pass
class BG21_020e:# <12>[1453]
	""" Dazzled
	Increased stats. """
	pass
BG21_020pe=buff(1,1)# <12>[1453]
""" Dazzling Lightspawn Player Enchant
Increased stats. """
class BG21_020_G:# <12>[1453]
	""" Dazzling Lightspawn
	[Avenge (2):] Elementals inBob's Tavern have +2/+2__for the rest of the game. """
	events = Death(FRIENDLY).on(Avenge(SELF, 2, [BG21_020_Action(CONTROLLER, 2)]))
	pass


#Recycling Wraith(4)   ### maybe ###
if BG_Recycling_Wraith: # 
	BG_Minion_Elemental+=['BG21_040','BG21_040_G']
	BG_PoolSet_Elemental[4].append('BG21_040')
	BG_Elemental_Gold['BG21_040']='BG21_040_G'
class BG21_040:# <12>[1453] レイス
	""" Recycling Wraith
	After you play an Elemental, your next [Refresh] costs (1) less. """
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(GetFreeRerole(CONTROLLER))
	pass
class BG21_040_G:# <12>[1453]
	""" Recycling Wraith
	After you play anElemental, your next two[Refreshes] cost (1) less. """
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(GetFreeRerole(CONTROLLER)*2)
	pass



#Wildfire Elemental(4) ### OK ###
if BG_Wildfire_Elemental: # 
	BG_Minion_Elemental+=['BGS_126','TB_BaconUps_166']
	BG_PoolSet_Elemental[4].append('BGS_126')
	BG_Elemental_Gold['BGS_126']='TB_BaconUps_166'
class BGS_126_Action(TargetedAction):
	TARGET = ActionArg()
	LVL = IntArg()
	def do(self, source, target, lvl):
		attacker = source
		defender = target
		adjacents = defender.adjacent_minions
		amount = attacker.atk - defender.health
		if amount>0 and len(adjacents)>0:
			if lvl==1:
				Hit(random.choice(adjacents), amount).trigger(source.controller)
			else:
				for card in adjacents:
					Hit(card, amount).trigger(source.controller)
class BGS_126:# <12>[1453]
	""" Wildfire Elemental
	After this attacks and kills a minion, deal excess damage to a random adjacent minion. """
	events = Attack(SELF, ENEMY_MINIONS).on(BGS_126_Action(Attack.DEFENDER, 1))
	pass
class TB_BaconUps_166:# <12>[1453]
	""" Wildfire Elemental
	After this attacks and killsa minion, deal excess damage to both adjacent minions. """
	events = Attack(SELF, ENEMY_MINIONS).on(BGS_126_Action(Attack.DEFENDER, 2))
	pass

#### tavern tier 5

#Tavern Tempest(5)   ### need check ###
if BG_Tavern_Tempest: # 
	BG_Minion_Elemental+=['BGS_123','TB_BaconUps_162']
	BG_PoolSet_Elemental[5].append('BGS_123')
	BG_Elemental_Gold['BGS_123']='TB_BaconUps_162'
class BGS_123:# <12>[1453] 逆巻き風
	""" Tavern Tempest
	[Battlecry:] Add another random Elemental to your hand. """
	def play(self):
		controller = self.controller
		tier = self.controller.tavern_tier
		elemental = []
		for gr in range(tier):
			elemental += BG_PoolSet_Elemental[gr-1]
		if 'BGS_123' in elemental:
			elemental.remove('BGS_123')
		if len(elemental):
			newcard_id = random.choice(elemental)
			Give(controller,newcard_id).trigger(self)
	pass
class TB_BaconUps_162:# <12>[1453]
	""" Tavern Tempest
	[Battlecry:] Add two other random Elementals to your hand. """
	def play(self):
		controller = self.controller
		tier = self.controller.tavern_tier
		elemental = []
		for gr in range(tier):
			elemental += BG_PoolSet_Elemental[gr-1]
		if 'BGS_123' in elemental:
			elemental.remove('BGS_123')
		if len(elemental):
			newcard_id = random.choice(elemental)
			Give(controller,newcard_id).trigger(self)
			newcard_id = random.choice(elemental)
			Give(controller,newcard_id).trigger(self)
	pass



#Lil' Rag (6->5, 24.0.3)   ### OK ###
if BG_Lil_Rag: # 
	BG_Minion_Elemental+=['BGS_100','BGS_100e','TB_BaconUps_200']
	BG_PoolSet_Elemental[5].append('BGS_100')
	BG_Elemental_Gold['BGS_100']='TB_BaconUps_200'
class BGS_100_Action(TargetedAction):
	TARGET = ActionArg()
	CARDS = CardArg()
	def do(self, source, target, cards):
		if not isinstance(cards, list):
			cards = [cards]
		controller = target
		tier = cards[0].tech_level
		if controller.field != []:
			card = random.choice(controller.field)
			Buff(card, 'BGS_100e', atk=tier, max_health=tier).trigger(source)
			pass
class BGS_100:# <12>[1453] チビラグ
	""" Lil' Rag
	After you play an Elemental,give a friendly minion stats equal to the Elemental's Tavern Tier. """
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(BGS_100_Action(CONTROLLER, BG_Play.CARD))
	pass
class BGS_100e:
	pass
class TB_BaconUps_200:# <12>[1453]
	""" Lil' Rag
	After you play an Elemental,give a friendly minion statsequal to the Elemental'sTavern Tier twice. """
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(BGS_100_Action(CONTROLLER, BG_Play.CARD)*2)
	pass

if BG25__Magmaloc:# 5/1/1 murloc ## new 25.2.2
	BG_Minion_Elemental+=['BG25_046','BG25_046e','BG25_046_G','BG25_046_Ge']
	BG_PoolSet_Elemental[5].append('BG25_046')
	BG_Elemental_Gold['BG25_046']='BG25_046_G'
class BG25_046_Action(GameAction):
	def do(self, source):
		amount = len([log for log in  source.controller._play_log if log.card.type==CardType.MINION and log.turn==source.controller.game.turn ])
		Buff(source, 'BG25_046e', atk=amount+1, max_health=amount+1).trigger(source)
class BG25_046:# (minion)(murloc)
	""" Magmaloc
	At the end of your turn, gain +1/+1. Repeat for each minion you played this turn. """
	events = OWN_TURN_END.on(BG25_046_Action())
	pass
class BG25_046e:# (enchantment)
	""" Magma!
	+1/+1. """
	#
	pass
class BG25_046_G_Action(GameAction):
	def do(self, source):
		amount = len([log for log in  source.controller._play_log if log.type==CardType.MINION and log.turn==source.controller.game.turn ])
		Buff(source, 'BG25_046_Ge', atk=2*amount+2, max_health=2*amount+2).trigger(source)
class BG25_046_G:# (minion)(murloc)
	""" Magmaloc
	At the end of your turn, gain +2/+2. Repeat for each minion you played this turn. """
	events = OWN_TURN_END.on(BG25_046_G_Action())
	pass
class BG25_046_Ge:# (enchantment)
	""" Magma!
	+2/+2. """
	#
	pass



#### tavern tier 6

#Gentle Djinni(6)   ### OK ###
if BG_Gentle_Djinni: # 
	BG_Minion_Elemental+=['BGS_121','TB_BaconUps_165']
	BG_PoolSet_Elemental[6].append('BGS_121')
	BG_Elemental_Gold['BGS_121']='TB_BaconUps_165'
class BGS_121_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		controller = target
		tier = controller.tavern_tier
		elemental = []
		for gr in range(1,tier+1):
			elemental += BG_PoolSet_Elemental[gr]
		if 'BGS_121' in elemental:
			elemental.remove('BGS_121')
		if len(elemental):
			for repeat in range(amount):
				newcard_id = random.choice(elemental)
				Summon(controller,newcard_id).trigger(source)
				if controller.deepcopy_original!=None:
					Give(controller.deepcopy_original, newcard_id).trigger(source)
	pass
class BGS_121:# <12>[1453] ランプの精
	""" Gentle Djinni
	[Taunt]. [Deathrattle:] Summon another random Elemental and add a copy of it to your hand. """
	deathrattle = BGS_121_Action(CONTROLLER, 1)
	pass
class TB_BaconUps_165:# <12>[1453]
	""" Gentle Djinni
	[Taunt]. [Deathrattle:] Summon two other random Elementals and add copies of them to your hand. """
	deathrattle = BGS_121_Action(CONTROLLER, 2)
	pass



# Lieutenant Garr (6)(8/8) ### HP OK ###
if BG_Lieutenant_Garr: # 
	BG_Minion_Elemental+=['BGS_124','BGS_124e','TB_BaconUps_163','TB_BaconUps_163e']
	BG_PoolSet_Elemental[6].append('BGS_124')
	BG_Elemental_Gold['BGS_124']='TB_BaconUps_163'
class BGS_124_Action(TargetedAction):
	TARGET = ActionArg()# SELF
	BUFF = ActionArg()#'BGS_124e'
	AMOUNT = IntArg()
	def do(self, source, target, buff, amount):
		#count = len([card for card in source.controller.field if card.race==Race.ELEMENTAL])
		count = len([card for card in source.controller.field if race_identity(card, Race.ELEMENTAL)])
		Buff(target, buff, max_health=count*amount).trigger(source)
class BGS_124: #
	""" Lieutenant Garr
	[Taunt]. After you play an Elemental, gain +1 Health for each Elemental you have """
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).after(BGS_124_Action(SELF, 'BGS_124e', 1))
	pass
class BGS_124e:
	pass
class TB_BaconUps_163:
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).after(BGS_124_Action(SELF, 'TB_BaconUps_163e', 2))
	pass
class TB_BaconUps_163e:
	pass














