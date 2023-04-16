from ..utils import *

BG_Icky_Imp=True ##(1) banned 24.2 ## renew 25.2.2
BG24__Picky_Eater=True ## (1) new 24.2

BG_Imprisoner=False ##(2)->(1)-> banned when? 
BG_Impulsive_Trickster=True ##(1)->(2)
BG_Mind_Muck=True #(2) new 24.2
BG_Nathrezim_Overseer=False ##(2) banned 24.2
BG_Piggyback_Imp=True #(2) new 24.2

#BG_Felemental : -> ELEMENTAL
BG_Kathra_natir=True ##(3)
BG_Leeching_Felhound=True ## 3/3/3 new 25.6 #########
BG_Legion_Overseer=True## (3) new 24.2 
BG_Soul_Devourer=False ##(3) banned 24.2

BG_Bigfernal=True ##(4)
BG_Ring_Matron=True ##(4)

BG_Annihilan_Battlemaster=True ##(5)
BG_Insatiable_Ur_zul=True ##(5)
BG_Voidlord=True ##(5)

BG_Famished_Felbat=True ##(6)
BG_Imp_Mama=False ##(6) ## banned? 25.2.2
BG25__Felstomper=True# 6/3/7 demon/beast ## new 25.2.2
BG25__Mecha_Jaraxxus=True# 6/3/15 MECH/DEMON ## new 25.2.2


BG_Minion_Demon =[]

BG_PoolSet_Demon=[[],[],[],[],[],[],[]]

BG_Demon_Gold={}

#################### インプ ### OK ### banned 24.2 ## renew 25.2.2
if BG_Icky_Imp:
	BG_Minion_Demon +=['BG21_029','BG_BRM_006t','BG21_029_G','TB_BaconUps_030t']
	BG_PoolSet_Demon[1].append('BG21_029')
	BG_Demon_Gold['BG21_029']='BG21_029_G'
class BG21_029:# <12>[1453]
	""" Icky Imp (1)
	[Deathrattle:] Summon two 1/1 Imps. """
	deathrattle = Summon(CONTROLLER, 'BG_BRM_006t') * 2
	pass
class BRM_006t:#
	""" imp (1/1)"""
	pass
class BG21_029_G:# <12>[1453]
	""" Icky Imp
	[Deathrattle:] Summon two 2/2 Imps. """
	deathrattle = Summon(CONTROLLER, 'TB_BaconUps_030t') * 2
	pass
class TB_BaconUps_030t:#
	""" Imp (2/2)
	"""

if BG24__Picky_Eater:# (1) #### visually OK###
	BG_Minion_Demon+=['BG24_009','BG24_009e','BG24_009_G']
	BG_PoolSet_Demon[1].append('BG24_009')
	BG_Demon_Gold['BG24_009']='BG24_009_G'
class BG24_009:# (minion)(demon)
	""" Picky Eater
	[Battlecry:] Consume a random minion in Bob's_Tavern to gain its stats. """
	def play(self):
		if len(self.controller.opponent.field)>0:
			card=random.choice(self.controller.opponent.field)
			Buff(self, 'BG24_009e', atk=card.atk, max_health=card.max_health).trigger(self)
			Destroy(card).trigger(self)
	pass
class BG24_009e:# (enchantment)
	""" Ate a Taverngoer
	Consumed the stats of minion. """
	pass
class BG24_009_G:# (minion)(demon)
	""" Picky Eater
	[Battlecry:] Consume a random minion in Bob's_Tavern to gain double its stats. """
	def play(self):
		if len(self.controller.opponent.field)>0:
			card=random.choice(self.controller.opponent.field)
			Buff(self, 'BG24_009e', atk=card.atk*2, max_health=card.max_health*2).trigger(self)
			Destroy(card).trigger(self)
	pass


############# tavern tier 2

#################### トリックスター(1)->(2)  ### OK ###
if BG_Impulsive_Trickster:
	BG_Minion_Demon +=['BG21_006','BG21_006e','BG21_006_G']
	BG_PoolSet_Demon[2].append('BG21_006')
	BG_Demon_Gold['BG21_006']='BG21_006_G'
class BG21_006_Action(TargetedAction):
	TARGET = ActionArg()
	CONTRO = ActionArg()
	def do(self, source, target, contro):
		# controller : trickstar card
		# target = friendly minion
		# sourceは、この事象が発生する大もとのカード
		if isinstance(contro, list):
			contro = contro[0]
		controller = contro
		if target.type == CardType.ENCHANTMENT:#ないとは思うが、一度あった
			target = target.owner
		buff_health = source.max_health
		if target!=None and target!=[]:
			Buff(target, 'BG21_006e', max_health = buff_health).trigger(source)
		pass
class BG21_006:# <12>[1453]
	""" Impulsive Trickster(1)
	[Deathrattle:] Give this minion's maximum Health__to another friendly minion._ """
	deathrattle = BG21_006_Action(RANDOM(FRIENDLY_MINIONS),CONTROLLER)
	pass
class BG21_006e:# <12>[1453]
	""" Impulsive
	Increased Health. """
	pass
class BG21_006_G:# <12>[1453]
	""" Impulsive Trickster
	[Deathrattle:] Give thisminion's maximum Healthto another friendly minion twice. """
	deathrattle = BG21_006_Action(RANDOM(FRIENDLY_MINIONS),CONTROLLER) * 2
	pass

#########BG23_357(2)############
if BG_Mind_Muck: #(2) new 24.2
	BG_Minion_Demon +=['BG23_357','BG23_357_G']
	BG_PoolSet_Demon[2].append('BG23_357')
	BG_Demon_Gold['BG23_357']='BG23_357_G'
class BG23_357:# 
	""" Mind Muck(2)
	[Battlecry:] Choose a friendly Demon. It consumes a minion in Bob's Tavern to gain its stats."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	def play(self):
		if self.target!=None and len(self.controller.opponent.field)>0:
			card=random.choice(self.controller.opponent.field)
			Buff(self.target, 'BG24_009e', atk=card.atk, max_health=card.max_health).trigger(self)
			Destroy(card).trigger(self)
	pass
class BG23_357_G:# 
	""" Mind Muck
	[Battlecry:] Choose a friendly Demon. It consumes a _minion in Bob's Tavern __to gain double its stats."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	def play(self):
		if self.target!=None and len(self.controller.opponent.field)>0:
			card=random.choice(self.controller.opponent.field)
			Buff(self.target, 'BG24_009e', atk=card.atk*2, max_health=card.max_health*2).trigger(self)
			Destroy(card).trigger(self)
	pass

####### BG_AV_309 ############
if BG_Piggyback_Imp: #(2) new 24.2
	BG_Minion_Demon +=['BG_AV_309','BG_AV_309t','BG_AV_309_G','BG_AV_309_Gt']
	BG_PoolSet_Demon[2].append('BG_AV_309')
	BG_Demon_Gold['BG_AV_309']='BG_AV_309_G'
class BG_AV_309:# 
	""" Piggyback Imp(2)
	[Deathrattle:] Summon a 4/1 Imp(BG_AV_309t)."""
	deathrattle=Summon(CONTROLLER, 'BG_AV_309t')
class BG_AV_309t:
	pass
class BG_AV_309_G:# 
	""" Mind Muck
	[Deathrattle:] Summon a 8/2 Imp."""
	deathrattle=Summon(CONTROLLER, 'BG_AV_309_Gt')
class BG_AV_309_Gt:
	pass


####################ナスレズィム (2)### OK ### banned 24.2
if BG_Nathrezim_Overseer:
	BG_Minion_Demon +=['BGS_001','BGS_001e','TB_BaconUps_062','TB_BaconUps_062e']
	BG_PoolSet_Demon[2].append('BGS_001')
	BG_Demon_Gold['BGS_001']='TB_BaconUps_062'
class BGS_001:# <12>[1453] 
	""" Nathrezim Overseer (2)
	[Battlecry:] Give a friendly Demon +2/+2. """
	requirements = {
		PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_TARGET_WITH_RACE:Race.DEMON, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0, 
		}
	play = Buff(TARGET, 'BGS_001e')
	pass
BGS_001e=buff(2,2)
class TB_BaconUps_062:# <12>[1453]
	""" Nathrezim Overseer
	[Battlecry:] Give a friendly Demon +4/+4. """
	requirements = {
		PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_TARGET_WITH_RACE:Race.DEMON, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0,
		}
	play = Buff(TARGET, 'TB_BaconUps_062e')
	pass
TB_BaconUps_062e=buff(4,4)



####################  禁固番  (1) ### OK ### banned when?
if BG_Imprisoner:
	BG_Minion_Demon +=['BGS_014','BRM_006t','TB_BaconUps_113','TB_BaconUps_030t']
	BG_PoolSet_Demon[1].append('BGS_014')
	BG_Demon_Gold['BGS_014']='TB_BaconUps_113'
class BGS_014:# <12>[1453]
	""" Imprisoner (2)
	[Taunt][Deathrattle:] Summon a 1/1 Imp. """
	deathrattle = Summon(CONTROLLER, 'BRM_006t')
	pass
class TB_BaconUps_113:# <12>[1453]
	""" Imprisoner
	[Taunt][Deathrattle:] Summon a 2/2 Imp. """
	deathrattle = Summon(CONTROLLER, 'TB_BaconUps_030t')
	pass



########### tavern tier 3


#################### カスラナティール（カステラ） (3)### maybe OK ###
if BG_Kathra_natir:
	BG_Minion_Demon +=['BG21_039','BG21_039e','BG21_039_G','BG21_039_Ge']
	BG_PoolSet_Demon[3].append('BG21_039')
	BG_Demon_Gold['BG21_039']='BG21_039_G'
class BG21_039:# <12>[1453]
	""" Kathra'natir (3)
	Your other Demons have +2 Attack.Your Hero is [Immune]. """
	update = Refresh(FRIENDLY + DEMON, buff='BG21_039e'),Refresh(FRIENDLY_HERO, {GameTag.IMMUNE:True})
	pass
BG21_039e=buff(2,0)
class BG21_039_G:# <12>[1453]
	""" Kathra'natir
	Your other Demonshave +4 Attack.Your Hero is [Immune]. """
	update = Refresh(FRIENDLY + DEMON, buff='BG21_039_Ge'),Refresh(FRIENDLY_HERO, {GameTag.IMMUNE:True})
	pass
BG21_039_Ge=buff(4,0)


## Leeching Felhound 3/3/3
if BG_Leeching_Felhound: ## 3/3/3 new 25.6 #########
	BG_Minion_Demon +=['BG25_520','BG25_520_G']
	BG_PoolSet_Demon[3].append('BG25_520')
	BG_Demon_Gold['BG25_520']='BG25_520_G'
class BG25_520:
	""" Leeching Felhound
	This costs Health instead of Gold to buy."""
class BG25_520_G:
	""" Leeching Felhound
	This costs Health instead of Gold to buy."""




#### BG23_361 #####
if BG_Legion_Overseer:## (3) new 24.2 
	BG_Minion_Demon +=['BG23_361','BG23_361e','BG23_361_G']
	BG_PoolSet_Demon[3].append('BG23_361')
	BG_Demon_Gold['BG23_361']='BG23_361_G'
class BG23_361:
	""" Legion Overseer (3)
	Minions in Bob's_Tavern have +2/+2."""
	update = Refresh(ENEMY_MINIONS, buff='BG23_361e')
	pass
#BG23_361e=buff(2,2)
BG23_361e=buff(2,1) #24.2.2
class BG23_361_G:
	""" Legion Overseer (3)
	Minions in Bob's_Tavern have +4/+4."""
	update = Refresh(ENEMY_MINIONS, buff='BG23_361_Ge')
	pass
@custom_card
class BG23_361_Ge:
	tags = {
		GameTag.CARDNAME: "Legion Overseer",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		#GameTag.ATK:4,
		#GameTag.HEALTH:4
		GameTag.ATK:4,
		GameTag.HEALTH:2
	}

####################   魂喰らい魔 (3)### maybe OK ### banned 24.2
if BG_Soul_Devourer:
	BG_Minion_Demon +=['BGS_059','BGS_059e','TB_BaconUps_119']
	BG_PoolSet_Demon[3].append('BGS_059')
	BG_Demon_Gold['BGS_059']='TB_BaconUps_119'
class BGS_059_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		controller = source.controller
		Buff(source, 'BGS_059e',
			atk = target.atk * amount,
			max_health = target.max_health * amount
			).trigger(source)
		Destroy(target).trigger(source)
		ManaThisTurnOnly(controller, 3 * amount).trigger(source)
class BGS_059:# <12>[1453] ## 動いている感じはある
	""" Soul Devourer (3)
	[Battlecry:] Choose a friendly Demon. Remove it to gain its stats and 3 Gold. """
	requirements={
		PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_TARGET_WITH_RACE:Race.DEMON, PlayReq.REQ_FRIENDLY_TARGET:0, 
		}
	play = BGS_059_Action(TARGET,  1)
	#play = EatsMinion(SELF, TARGET, 1, 'BGS_059e'),ManaThisTurn(controller, 3)
	pass
class BGS_059e:
	pass
class TB_BaconUps_119:# <12>[1453]
	""" Soul Devourer
	[Battlecry:] Choose afriendly Demon. Removeit to gain double its statsand 6 Gold. """
	requirements={
		PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_TARGET_WITH_RACE:Race.DEMON, PlayReq.REQ_FRIENDLY_TARGET:0, 
		}
	play = BGS_059_Action(TARGET, 2)
	#play = EatsMinion(SELF, TARGET, 2, 'BGS_059e'),ManaThisTurn(controller, 6)
	pass

from .BG_minion_elemental import BG25__Felemental
if BG25__Felemental:# 3/3/1 elemental/demon ## new 25.2.2 ##
	##BG_Minion_Demon+=['BG25_041','BG25_041_G','BG25_041e','BG25_041e2']## no need
	BG_PoolSet_Demon[3].append('BG25_041')
	BG_Demon_Gold['BG25_041']='BG25_041_G'

############ tavern tier 4

################### 焦熱の圧鬼（あっき）(4)### maybe ###
if BG_Bigfernal:
	BG_Minion_Demon +=['BGS_204','BGS_204e','TB_BaconUps_304','TB_BaconUps_304e']
	BG_PoolSet_Demon[4].append('BGS_204')
	BG_Demon_Gold['BGS_204']='TB_BaconUps_304'
class BGS_204:# <12>[1453]
	""" Bigfernal (4)
	After you summon a Demon, gain +1/+1 permanently. """
	events = Summon(CONTROLLER, FRIENDLY + DEMON).after(BuffPermanently(SELF, 'BGS_204e' ))
	pass
BGS_204e=buff(1,1)
class TB_BaconUps_304:# <12>[1453]
	""" Bigfernal
	After you summon a Demon, gain +2/+2 permanently. """
	events = Summon(CONTROLLER, FRIENDLY + DEMON).after(BuffPermanently(SELF, 'TB_BaconUps_304e' ))
	pass
TB_BaconUps_304e=buff(2,2)


###################  火の輪くぐらせ嬢  (4)### OK ###
if BG_Ring_Matron:
	BG_Minion_Demon +=['BG_DMF_533','DMF_533t','TB_BaconUps_309','TB_BaconUps_309t']
	BG_PoolSet_Demon[4].append('BG_DMF_533')
	BG_Demon_Gold['BG_DMF_533']='TB_BaconUps_309'
class DMF_533:# <9>[1453]
	""" Ring Matron (4)
	[Taunt][Deathrattle:] Summon two 3/2 Imps. """
	deathrattle = Summon(CONTROLLER, 'DMF_533t')*2
	pass
class DMF_533t:
	pass
class TB_BaconUps_309:# <9>[1453]
	""" Ring Matron
	[Taunt][Deathrattle:] Summontwo 6/4 Imps. """
	deathrattle = Summon(CONTROLLER, 'TB_BaconUps_309t')*2
	pass
class TB_BaconUps_309t:# <9>[1453]
	""" Fiery Imp
	 """
	pass


######### tavern tier 5


####################   アニヒラン  (5)### OK ###
if BG_Annihilan_Battlemaster:
	BG_Minion_Demon +=['BGS_010','TB_BaconUps_083']
	BG_PoolSet_Demon[5].append('BGS_010')
	BG_Demon_Gold['BGS_010']='TB_BaconUps_083'
class BGS_010:# <12>[1453]
	""" Annihilan Battlemaster (5)
	[Battlecry:] Gain +1 Health for each Health your hero_is missing. """
	def play(self):
		hero = self.controller.hero
		self.max_health += hero.damage
	pass
class TB_BaconUps_083:# <12>[1453]
	""" Annihilan Battlemaster
	[Battlecry:] Gain +2 Health for each Health your hero_is missing. """
	def play(self):
		hero = self.controller.hero
		self.max_health += hero.damage*2
	pass


####################   ウルズール  (5)### need check ###
if BG_Insatiable_Ur_zul:
	BG_Minion_Demon +=['BG21_004','BG21_004e','BG21_004_G']
	BG_PoolSet_Demon[5].append('BG21_004')
	BG_Demon_Gold['BG21_004']='BG21_004_G'
class BG21_004:# <12>[1453]
	""" Insatiable Ur'zul (5)
	[[Taunt].] After you play a Demon, consume a minion in Bob's Tavern to gain its stats. """
	events = BG_Play(CONTROLLER, FRIENDLY + DEMON).on(EatsMinion(SELF, RANDOM(ENEMY_MINIONS), 1, 'BG21_004e'))
	pass
class BG21_004e:# <12>[1453]
	""" Sated
	Increased Stats """
	#
	pass
class BG21_004_G:# <12>[1453]
	""" Insatiable Ur'zul
	[[Taunt].] After you play aDemon, consume a minionin Bob's Tavern to gain double its stats. """
	events = BG_Play(CONTROLLER, FRIENDLY + DEMON).on(EatsMinion(SELF, RANDOM(ENEMY_MINIONS), 2, 'BG21_004e'))
	pass


#################### ヴォイドロード (5)### OK ###
if BG_Voidlord:
	BG_Minion_Demon +=['BG_LOOT_368','CS2_065','TB_BaconUps_059','TB_BaconUps_059t']
	BG_PoolSet_Demon[5].append('BG_LOOT_368')
	BG_Demon_Gold['BG_LOOT_368']='TB_BaconUps_059'
class BG_LOOT_368:# <9>[1453]
	""" Voidlord (5)
	[Taunt] [Deathrattle:] Summon three 1/3 Demons with [Taunt]. """
	deathrattle = Summon(CONTROLLER, 'CS2_065')*3
	pass
class CS2_065:
	"""  """
	pass
class TB_BaconUps_059:# <9>[1453]
	""" Voidlord
	[Taunt] [Deathrattle:] Summon three2/6 Demons with [Taunt]. """
	deathrattle = Summon(CONTROLLER, 'TB_BaconUps_059t')*3
	pass
class TB_BaconUps_059t:# <9>[1453]
	""" Voidwalker
	[Taunt] """
	pass


######### tavern tier 6

####################   フェルバット (6)### need check ###
if BG_Famished_Felbat:
	BG_Minion_Demon +=['BG21_005','BG21_005e','BG21_005_G']
	BG_PoolSet_Demon[6].append('BG21_005')
	BG_Demon_Gold['BG21_005']='BG21_005_G'
class BG21_005:# <12>[1453]
	""" Famished Felbat (6)
	At the end of your turn, eachfriendly Demon consumes aminion in Bob's Tavern to__gain its stats. """
	events = OWN_TURN_END.on(EatsMinion(FRIENDLY + DEMON, RANDOM(ENEMY_MINIONS), 1, 'BG21_005e'))
	pass
class BG21_005e:# <12>[1453]
	""" Fed by the Felbat
	Consumed the stats of minion. """
	#
	pass
class BG21_005_G:# <12>[1453]
	""" Famished Felbat
	At the end of your turn, eachfriendly Demon consumes aminion in Bob's Tavern to__gain double its stats. """
	events = OWN_TURN_END.on(EatsMinion(FRIENDLY + DEMON, RANDOM(ENEMY_MINIONS), 2, 'BG21_005e'))
	pass


#################### ママ  (6)### maybe ### banned? 25.2.2
if BG_Imp_Mama:
	BG_Minion_Demon +=['BGS_044','BGS_044e','TB_BaconUps_116']
	BG_PoolSet_Demon[6].append('BGS_044')
	BG_Demon_Gold['BGS_044']='TB_BaconUps_116'
class BGS_044:# <9>[1453]
	""" Imp Mama (6)
	Whenever this minion takes damage, summon a random Demon and give it [Taunt]. """
	events = Damage(SELF).on(Summon(CONTROLLER, RandomBGDemon()).then(Buff(Summon.CARD, 'BGS_044e')))
	pass
BGS_044e=buff(taunt=True)
class TB_BaconUps_116:# <9>[1453]
	""" Imp Mama
	Whenever this miniontakes damage, summon2 random Demons andgive them [Taunt]. """
	events = Damage(SELF).on(Summon(CONTROLLER, RandomBGDemon()).then(Buff(Summon.CARD, 'BGS_044e')), Summon(CONTROLLER, RandomBGDemon()).then(Buff(Summon.CARD, 'BGS_044e')))
	#
	pass



if BG25__Mecha_Jaraxxus:# 6/3/15 MECH/DEMON ## new 25.2.2 #########################
	BG_Minion_Demon+=['BG25_807','BG25_807_G','BG25_807e','BG25_807e2','BG25_807e3']
	BG_Minion_Demon+=['BG25_807t','BG25_807t_G','BG25_807t2','BG25_807t2_G','BG25_807t3','BG25_807t3_G']
	BG_PoolSet_Demon[6].append('BG25_807')
	BG_Demon_Gold['BG25_807']='BG25_807_G'
	BG_Demon_Gold['BG25_807t']='BG25_807t_G'
	BG_Demon_Gold['BG25_807t2']='BG25_807t2_G'
	BG_Demon_Gold['BG25_807t3']='BG25_807t3_G'
class BG25_807_Action(GameAction):
	def do(self, source):
		card = random.choice(['BG25_807t','BG25_807t2','BG25_807t3'])
		Give(source.controller, card).trigger(source)
class BG25_807:# (minion)(demon)
	""" Mecha-Jaraxxus
	<b>Battlecry:</b> Add a random Mecha-Demon to your hand. """
	play = BG25_807_Action()
	pass
class BG25_807_G_Action(GameAction):
	def do(self, source):
		cards = random.sample(['BG25_807t','BG25_807t2','BG25_807t3'],2)
		Give(source.controller, cards[0]).trigger(source)
		Give(source.controller, cards[1]).trigger(source)
class BG25_807_G:# (minion)(demon)
	""" Mecha-Jaraxxus
	<b>Battlecry:</b> Add 2 random Mecha-Demons to your hand. """
	play = BG25_807_G_Action()
	pass
class BG25_807e:# (enchantment)
	""" Rusted Reggie
	<b>Windfury</b> """
	tags = {GameTag.WINDFURY:1, 
		GameTag.ATK:5,
		GameTag.HEALTH:5}
@custom_card
class BG25_807t_Ge:
	tags = {
		GameTag.CARDNAME: "Rusted Reggie",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.WINDFURY:3, 
		GameTag.ATK:10,
		GameTag.HEALTH:10	}
class BG25_807e2:# (enchantment)
	""" Magtheridon Prime
	<b>Taunt</b> """
	tags = {GameTag.TAUNT:True, 
		GameTag.ATK:1,
		GameTag.HEALTH:10}
@custom_card
class BG25_807t2_Ge:
	tags = {
		GameTag.CARDNAME: "Magtheridon Prime",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.TAUNT:True, 
		GameTag.ATK:2,
		GameTag.HEALTH:20	}
class BG25_807e3:# (enchantment)
	""" Baltharak
	<b>Reborn</b> """
	tags = {GameTag.REBORN:True, 
		GameTag.ATK:10,
		GameTag.HEALTH:1}
@custom_card
class BG25_807t3_Ge:
	tags = {
		GameTag.CARDNAME: "Baltharak",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.REBORN:True, 
		GameTag.ATK:20,
		GameTag.HEALTH:2	}
class BG25_807t:# (minion)
	""" Rusted Reggie */5/5
	<b>Windfury</b> Can <b>Magnetize</b> to Mechs <i>and</i>__Demons. """
	play = Magnetic(SELF, ['BG25_807e'])
	pass
class BG25_807t_G:# (minion)
	""" Rusted Reggie */10/10
	<b>Mega-Windfury</b> Can <b>Magnetize</b> to Mechs <i>and</i>__Demons. """
	play = Magnetic(SELF, ['BG25_807t_Ge'])
	pass
class BG25_807t2:# (minion)
	""" Magtheridon Prime */1/10
	<b>Taunt</b> Can <b>Magnetize</b> to Mechs <i>and</i>__Demons. """
	play = Magnetic(SELF, ['BG25_807e2'])
	pass
class BG25_807t2_G:# (minion)
	""" Magtheridon Prime */2/20
	<b>Taunt</b> Can <b>Magnetize</b> to Mechs <i>and</i>__Demons. """
	play = Magnetic(SELF, ['BG25_807t2_Ge'])
	pass
class BG25_807t3:# (minion)
	""" Baltharak */10/1
	<b>Reborn</b> Can <b>Magnetize</b> to Mechs <i>and</i>__Demons. """
	play = Magnetic(SELF, ['BG25_807e3'])
	pass
class BG25_807t3_G:# (minion)
	""" Baltharak */20/2
	<b>Reborn</b> Can <b>Magnetize</b> to Mechs <i>and</i>__Demons. """
	play = Magnetic(SELF, ['BG25_807t3_Ge'])
	pass



if BG25__Felstomper:# 6/3/7 demon/beast ## new 25.2.2 ### need check##############
	BG_Minion_Demon+=['BG25_042','BG25_042_G','BG25_042_Ge','BG25_042e']
	BG_PoolSet_Demon[6].append('BG25_042')
	BG_Demon_Gold['BG25_042']='BG25_042_G'
class BG25_042_Action(GameAction):
	def do(self,source):
		if source.controller.game.this_is_battle:
			for card in source.controller.field:
				Buff(card, 'BG25_042e').trigger(source)
class BG25_042:# (minion)(demon)
	""" Felstomper
	After you summon a _minion in combat, give ___your minions +3 Attack. """
	events = Summon(CONTROLLER, FRIENDLY + MINION).on(BG25_042_Action())
	pass
BG25_042e=buff(3,0)# (enchantment)
""" Felgorged	+3 Attack. """
class BG25_042_G_Action(GameAction):
	def do(self,source):
		if source.controller.game.this_is_battle:
			for card in source.controller.field:
				Buff(card, 'BG25_042_Ge').trigger(source)
class BG25_042_G:# (minion)(demon)
	""" Felstomper
	After you summon a _minion in combat, give ___your minions +6 Attack. """
	events = Summon(CONTROLLER, FRIENDLY+MINION).on(BG25_042_G_Action())
	pass
BG25_042_Ge=buff(6,0)
""" Felgorged	+6 Attack. """


####################



