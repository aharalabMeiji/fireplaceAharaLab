
from ..utils import *


BG_Minion_Elemental =[
	'BGS_116','TB_BaconUps_167',#Refreshing Anomaly(1)
	'BGS_115','BGS_115t','TB_BaconUps_156',#Sellemental(1)
	'BGS_127','BGS_127e','TB_Baconups_202','TB_Baconups_202e',#Molten Rock(2)
	'BGS_120','BGS_120e','TB_BaconUps_160',#Party Elemental(2)
	'BGS_119','TB_BaconUps_159',#Crackling Cyclone(3)
	'BG21_021','BG21_021e','BG21_021_G',#Smogger(3)
	'BGS_122','TB_BaconUps_161',#Stasis Elemental(3)
	'BG21_020','BG21_020e','BG21_020pe','BG21_020_G',#Dazzling Lightspawn(4)
	'BG21_040','BG21_040_G',#Recycling Wraith(4)
	'BGS_126','TB_BaconUps_166',#Wildfire Elemental(4)
	'BGS_123','TB_BaconUps_162',#Tavern Tempest(5)
	'BGS_121','TB_BaconUps_165',#Gentle Djinni(6)
	'BGS_100','BGS_100e','TB_BaconUps_200',#Lil' Rag (6->5) 24.0.3
	'BGS_124','BGS_124e','TB_BaconUps_163','TB_BaconUps_163e',# Lieutenant Garr (6)
]

BG_PoolSet_Elemental=[
	['BGS_116','BGS_115',],
	['BGS_127','BGS_120',],
	['BGS_119','BG21_021','BGS_122',],
	['BG21_020','BG21_040','BGS_126',],
	['BGS_123','BGS_100',],
	['BGS_121','BGS_124',],
	]

BG_Elemental_Gold={
	'BGS_116':'TB_BaconUps_167',#Refreshing Anomaly(1)
	'BGS_115':'TB_BaconUps_156',#Sellemental(1)
	'BGS_127':'TB_Baconups_202',#Molten Rock(2)
	'BGS_120':'TB_BaconUps_160',#Party Elemental(2)
	'BGS_119':'TB_BaconUps_159',#Crackling Cyclone(3)
	'BG21_021':'BG21_021_G',#Smogger(3)
	'BGS_122':'TB_BaconUps_161',#Stasis Elemental(3)
	'BG21_020':'BG21_020_G',#Dazzling Lightspawn(4)
	'BG21_040':'BG21_040_G',#Recycling Wraith(4)
	'BGS_126':'TB_BaconUps_166',#Wildfire Elemental(4)
	'BGS_123':'TB_BaconUps_162',#Tavern Tempest(5)
	'BGS_121':'TB_BaconUps_165',#Gentle Djinni(6)
	'BGS_100':'TB_BaconUps_200',#Lil' Rag (6->5)
	'BGS_124':'TB_BaconUps_163',# Lieutenant Garr (6)
	}


#Refreshing Anomaly(1)  ### OK ###
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
class BGS_115:# <12>[1453]　ウレメンタル
	""" Sellemental
	When you sell this,add a 2/2 Elementalto your hand. """
	events = Sell(CONTROLLER, SELF).on(Give(CONTROLLER, 'BGS_115t'))
	pass
class BGS_115t:# <12>[1453]　おつりちゃん
	""" Water Droplet  
	 """
	pass
class TB_BaconUps_156:# <12>[1453]
	""" Sellemental
	When you sell this,add two 2/2 Elementalsto your hand. """
	events = Sell(CONTROLLER, SELF).on(Give(CONTROLLER, 'BGS_115t') * 2)
	pass



#Molten Rock(2)  ### MAYBE ###
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



#Party Elemental(2)  ### MAYBE ###
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



#Crackling Cyclone(3)   ### OK ###
class BGS_119:# <12>[1453] ばりばり
	""" Crackling Cyclone
	[Divine Shield][Windfury] """
	pass
class TB_BaconUps_159:# <12>[1453]
	""" Crackling Cyclone
	[Divine Shield][Mega-Windfury] """
	#<Tag enumID="189" name="WINDFURY" type="Int" value="3"/>
	pass


#Smogger(3)   ### need check ###
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



#Stasis Elemental(3)   ### need check ###
class BGS_122:# <12>[1453] ###
	""" Stasis Elemental 
	[Battlecry:] Add another random Elemental to Bob's Tavern and [Freeze] it. """
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
			newcard[0][0].frozen=True
			newcard_id = random.choice(elementals)
			newcard = Summon(bartender,newcard_id).trigger(self)
			newcard[0][0].frozen=True
	pass



#Dazzling Lightspawn(4) ### OK ###
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



#Tavern Tempest(5)   ### need check ###
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
		newcard_id = random.choice(elemental)
		Give(controller,newcard_id).trigger(self)
		newcard_id = random.choice(elemental)
		Give(controller,newcard_id).trigger(self)
	pass



#Gentle Djinni(6)   ### OK ###
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
		for repeat in range(amount):
			newcard_id = random.choice(elemental)
			Summon(controller,newcard_id).trigger(source)
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




#Lil' Rag (6)   ### OK ###
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


class BGS_124: ## Lieutenant Garr (6)(8/8)
	""" Lieutenant Garr
	&lt;b&gt;Taunt&lt;/b&gt;. After you play an Elemental, gain +1 Health for each Elemental you have """
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).after(Buff(SELF, 'BGS_124e', max_health=Count(FRIENDLY_MINIONS + ELEMENTAL) ))
	pass
BGS_124e=buff(0,1)
class TB_BaconUps_163:
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).after(Buff(SELF, 'BGS_124e', max_health=Count(FRIENDLY_MINIONS + ELEMENTAL) ))
	pass
TB_BaconUps_163e=buff(0,2)














