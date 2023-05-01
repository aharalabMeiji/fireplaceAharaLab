from ..utils import *

BG_Tavern_Tipper=True ##(1/2/2) new 23.6
BG_Wrath_Weaver=True #(1/1/3)

BG_Acolyte_of_C_Thun=False## (2) banned 23.6
BG_Kooky_Chemist=False##(2) new 23.6 banned 24.2
BG_Menagerie_Mug=True##(2/2/2) banned 23.6 ### renew 24.6
BG_Patient_Scout=True ## (2/1/1) ## new 24.6 ### OK ###
BG_PoeticPenPal=True ## (2/2/4) ## new 25.6 ##
BG_Prophet_of_the_Boar=True##(2/2/3)
BG_Selfless_Hero=True##(2/2/1)
BG_Sparring_Partner=True##(2/3/2) new 23.6
BG_Spawn_of_N_Zoth=False##(2) ### banned 24.6
BG_Unstable_Ghoul=False##(2) banned 23.6
BG_Whelp_Smuggler=False##(2/2/5) banned when? ## renew 25.? ####
BG_Yrel=False##(2) new 23.6 ### banned 24.6

BG_Arm_of_the_Empire=True##(3/4/4)
BG_Bird_Buddy=True##(3/2/4)
BG_Boulderfist_Ogre=True##(3/6/7)
BG_Budding_Greenthumb=True##(3/1/4) banned 23.6 ## renew 25.2.2
BG_Faceless_Disciple=True ## (3/6/4) new 24.6 ### OK ###
BG_Houndmaster=False##(3/4/3) ### banned 25.6?
BG_Khadgar=False##(3) ## banned when? 
BG_Nightmare_Amalgam=False##(3) RENEW  23.2 ## banned 24.6
BG_Shifter_Zerus=False##(3) new 23.6 banned 24.2 ## revive 24.6 ## banned when?
BG_Soul_Juggler=True##(3/3/5)

BG_Ball_of_Minions=True ##(4) new 24.6  ### OK ###
BG_Champion_of_Y_Shaarj=False##(4)banned 23.6
BG_Defender_of_Argus=False##(4)banned 23.6
BG_Fireworks_Fanatic=True ##(4/4/3) new 25.6
BG_Impatient_Doomsayer=True##(4/2/6)
BG_Majordomo_Executus=False##(4) banned when?
BG_Master_of_Realities=True ##(5/6/6)->(4/4/4) when?
BG_Menagerie_Jug=True##(4/3/3)
BG_Reef_Explorer=False##(4)# NEW 23.2 ### banned 24.6
BG24__Rendle_the_Mistermind=False ## (4/4/5) new 24.2 banned 25.6
BG25__Sindorei_Straight_Shot=True ## (4/3/4) new 25.2.2
BG_Strongshell_Scavenger=True##(4/2/3)
BG_Treasure_Seeker_Elise=True ##(4/5/5) new 24.2
BG_Tunnel_Blaster=True##(4/3/7) new 23.6
BG_Vigilant_Stoneborn=True ## (4/2/6) new 24.6 ### OK ###
BG_Witchwing_Nestmatron=False ##(4) banned 24.2 renew 25.0.4 banned when?


BG_Baron_Rivendare=False##(5) ## banned 25.2.2
BG_Brann_Bronzebeard=True##(5/2/4)
BG_Deadly_Spore=False##(5)banned 23.6
BG_Interrogator_Whitemane=False ## (5) new 24.6  ## banned 25.0.4
BG_Kangor_s_Apprentice=True##(5/3/6)
BG_Leeroy_the_Reckless=True##(5/6/2) NEW 23.2
BG_Lightfang_Enforcer=True##(5/2/2)
BG_Mythrax_the_Unraveler=False ##(5) banned 24.2  ## revive 25.0.4 banned 25.2.2
BG_Nomi_Kitchen_Nightmare=True##(5/4/4)
BG25__Titus_Rivendare=True# 5/1/7 neutral ## new 25.2.2
BG24__Tortollan_Blue_Shell=True ## (5/4/7) new 24.2 ### OK ###

BG_Amalgadon=False##(6) banned 22.3
BG_Friend_of_a_Friend=False##(6)  banned 22.3
BG_Mantid_Queen=True ## (6/5/5) ## new when?
BG_Nadina_the_Red=True##(6/7/4)
BG_Orgozoa_the_Tender=True###(6/3/7) NEW 23.2
BG_Seafood_Slinger=True ##(6/5/5) banned -> resurrect 25.0.4
BG24__Tea_Master_Theotar=True# (6/6/6) new 24.2
BG24_The_Walking_Fort=False ##(6) new 24.6 ### banned until 25.2.2 ###
BG_Uther_the_Lightbringer=True ##(6/5/6) new 23.6
BG_Zapp_Slywick=True##(6/7/10)




BG_Minion=[]

BG_PoolSet_Minion=[
	[],[],[],[],[],[],[]
]

BG_Minion_Gold={}

#### TIER 1 ####


if BG_Tavern_Tipper:####Tavern Tipper (1) ### OK ### 23.6 new
	BG_Minion += ['BG23_352','BG23_352e','BG23_352_G','BG23_352_Ge',]#	
	BG_PoolSet_Minion[1].append('BG23_352')
	BG_Minion_Gold['BG23_352']='BG23_352_G'
	## Tavern Tipper (1) >= 23.6 #OK#
	pass
class BG23_352_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		controller = source.controller
		if controller.mana>0:
			Buff(target, buff).trigger(source)
			pass
class BG23_352:
	"""Tavern Tipper (1) >= 23.6
	If you have any unspent Gold at the end of your turn, gain +1/+2."""
	events = OWN_TURN_END.on(BG23_352_Action(SELF,'BG23_352e'))
	pass
BG23_352e=buff(1,2)
class BG23_352_G:
	"""
	If you have any unspent Gold at the end of __your turn, gain +2/+4."""
	events = OWN_TURN_END.on(BG23_352_Action(SELF,'BG23_352_Ge'))
	pass
BG23_352_Ge=buff(2,4)


if BG_Wrath_Weaver:#Wrath Weaver	1	1	3	-	-
	BG_Minion += ['BGS_004','BGS_004e','TB_BaconUps_079','TB_BaconUps_079e',]#Wrath Weaver	1
	BG_PoolSet_Minion[1].append('BGS_004')
	BG_Minion_Gold['BGS_004']='TB_BaconUps_079'
	pass
#Wrath Weaver	1	1	3	 ### maybe ###
class BGS_004:# <12>[1453] おりや
	""" Wrath Weaver
	After you play a Demon, deal 1 damage to your hero and gain +2/+2. """
	events = BG_Play(CONTROLLER, FRIENDLY + DEMON).after(Hit(FRIENDLY_HERO,1),Buff(SELF,'BGS_004e'))
	pass
BGS_004e=buff(2,2)# <12>[1453]
""" Wrath Woven, Increased stats. """
class TB_BaconUps_079:# <12>[1453]
	""" Wrath Weaver
	After you play a Demon, deal 1 damage to your hero and gain +4/+4. """
	events = BG_Play(CONTROLLER, FRIENDLY + DEMON).after(Hit(FRIENDLY_HERO,1),Buff(SELF,'TB_BaconUps_079e'))
	pass
TB_BaconUps_079e=buff(4,4)# <12>[1453]
""" Wrath Woven,	Increased stats. """


########### TIER 2 #################################

if BG_Acolyte_of_C_Thun:#Acolyte of C'Thun	2	2	3
	BG_Minion += ['BGS_106','TB_BaconUps_255',]#	1
	BG_PoolSet_Minion[2].append('BGS_106')
	BG_Minion_Gold['BGS_106']='TB_BaconUps_255'
	pass
#,#Acolyte of C'Thun	2 ##banned 23.6
class BGS_106:# <12>[1453] クトゥーンのじさい
	""" Acolyte of C'Thun
	[Taunt][Reborn] """
	pass
class TB_BaconUps_255:# <12>[1453]
	""" Acolyte of C'Thun
	[Taunt][Reborn] """
	pass


if BG_Kooky_Chemist:## Kooky Chemist (2) ### OK ### ## 23.6 new
	BG_Minion += ['BG_CFM_063','BG_CFM_063e','BG_CFM_063_G',]#	
	BG_PoolSet_Minion[2].append('BG_CFM_063')
	BG_Minion_Gold['BG_CFM_063']='BG_CFM_063_G'
	## Kooky Chemist (2) >= 23.6
	pass
class BG_CFM_063:
	""" Kooky Chemist (2) >= 23.6
	Battlecry: Swap the Attack and Health of a minion."""
	requirements = {PlayReq.REQ_MINION_TARGET: 0,
				 PlayReq.REQ_FRIENDLY_TARGET: 0,
				 PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Buff(TARGET, "BG_CFM_063e")
	pass
BG_CFM_063e = AttackHealthSwapBuff()
class BG_CFM_063_G:
	"""
	[Battlecry:] Swap the Attack and Health of a minion."""
	requirements = {PlayReq.REQ_MINION_TARGET: 0,
				 PlayReq.REQ_FRIENDLY_TARGET: 0,
				 PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Buff(TARGET, "BG_CFM_063e")
	pass



if BG_Menagerie_Mug:#Menagerie Mug	2	2	2 ### renew 24.6
	BG_Minion += ['BGS_082','BGS_082e','TB_BaconUps_144','TB_BaconUps_144e',]#	1
	BG_PoolSet_Minion[2].append('BGS_082')
	BG_Minion_Gold['BGS_082']='TB_BaconUps_144'
	pass
#Menagerie Mug	2	2	2	-		 ### OK ###
class BGS_082_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		controller = target
		field = controller.field
		flag = [0] * len(field)
		ret = []
		while True:
			if sum(flag)==len(field):
				break
			c =random.choice(field)
			addOK=True
			for d in ret:
				if c.race == d.race:
					flag[field.index(c)]=1
					addOK=False
					continue
			if addOK:
				flag[field.index(c)]=1
				if c.race != Race.INVALID:
					ret.append(c)
			pass
		if len(ret)<=3:
			sample = ret
		else:
			sample = random.sample(ret,3)
		for c in sample:
			Buff(c,buff).trigger(source)
class BGS_082:# <12>[1453]
	""" Menagerie Mug マナジェリ
	[Battlecry:] Give 3 random friendly minions of different minion types +1/+1. """
	play = BGS_082_Action(CONTROLLER,'BGS_082e')
	pass
BGS_082e=buff(1,1)# <12>[1453]
""" Sip of Tea, +1/+1. """
class TB_BaconUps_144:# <12>[1453]
	""" Menagerie Mug
	[Battlecry:] Give 3 randomfriendly minions of differentminion types +2/+2. """
	play = BGS_082_Action(CONTROLLER,'TB_BaconUps_144e')
	pass
TB_BaconUps_144e=buff(2,2)# <12>[1453]
""" Sip of Tea, +2/+2. """


#Patient Scout(BG24_715) ## new 24.6 ### OK ###
if BG_Patient_Scout:#Patient Scout	2	1	1	
	BG_Minion += ['BG24_715','BG24_715_G',]#	
	BG_PoolSet_Minion[2].append('BG24_715')
	BG_Minion_Gold['BG24_715']='BG24_715_G'
class BG24_715_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		card.zone=Zone.HAND
class BG24_715_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		BG24_715_Choice(source.controller, RandomBGAdmissible(tech_level=source.script_data_num_1)*3).trigger(source)
		pass
class BG24_715_Action2(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		source.script_data_num_1=min(source.script_data_num_1+1, 6)
		pass
class BG24_715:##
	""" Patient Scout
	When you sell this, [Discover] a Tier @ minion. &lt;i&gt;(Upgrades each turn!)&lt;/i&gt;"""
	# @ = self.script_data_num_1
	events = [
		Sell(CONTROLLER, SELF).on(BG24_715_Action(SELF)),
		BeginBar(CONTROLLER).on(BG24_715_Action2(SELF))
	]
	pass
class BG24_715_G_Choice(Choice):
	def choose(self, card):
		if self.source.sidequest_counter_1==0:
			self.next_choice=self
			self.source.sidequest_counter_1=1
		else:
			self.next_choice=None
		super().chooce(card)
		card.zone=Zone.HAND
class BG24_715_G_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		BG24_715_G_Choice(source.controller, RandomBGAdmissible(tech_level=source.script_data_num_1)*3).trigger(source)
		pass
class BG24_715_G:
	""" Patient Scout
	When you sell this, [Discover] two Tier @ minions. &lt;i&gt;(Upgrades each turn!)&lt;/i&gt;"""
	events = [
		Sell(CONTROLLER, SELF).on(BG24_715_G_Action(SELF)),
		BeginTurn(CONTROLLER).on(BG24_715_Action2(SELF))
	]
	pass

if BG_PoeticPenPal:## Poetic Pen Pal (BG25_105)(2/2/4) new 25.6
	BG_Minion += ['BG25_105','BG25_105_G',]#	1
	BG_PoolSet_Minion[2].append('BG25_105')
	BG_Minion_Gold['BG25_105']='BG25_105_G'
class BG25_105:##########################################
	""" Poetic Pen Pal (2/2/4)
	[Battlecry:] Reduce the Cost of your next Buddy by (2)."""
class BG25_105_G:
	""" Poetic Pen Pal (2/4/8)
	[Battlecry:] Reduce the Cost of your next Buddy by (4)."""


if BG_Prophet_of_the_Boar:#(BG20_203)Prophet of the Boar	2	3	3
	BG_Minion += ['BG20_203','BG20_203_G',]#	1
	BG_PoolSet_Minion[2].append('BG20_203')
	BG_Minion_Gold['BG20_203']='BG20_203_G'
	pass
#Prophet of the Boar	2	3	3	-		 ### OK ###
class BG20_203_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		controller = target
		#if controller.once_per_turn==0:
		for repeat in range(amount):
			Give(controller, 'BG20_GEM').trigger(source)
		#controller.once_per_turn=1
class BG20_203:# <12>[1453]
	""" Prophet of the Boar # renew 24.6
	[Taunt] After you play a Quilboar, get a [Blood Gem]. """
	##[Once per Turn:] After you play a Quilboar, gain a [Blood Gem]. """ # 
	events = [
		BG_Play(CONTROLLER, MINION + QUILBOAR).after(BG20_203_Action(CONTROLLER, 1)),
		#BeginBar(CONTROLLER).on(SetAttr(CONTROLLER, 'once_per_turn', 0))
		]
	pass
class BG20_203_G:# <12>[1453]
	""" Prophet of the Boar # renew 24.6
	[Taunt] After you play a Quilboar, get 2 [Blood Gems]."""
	#[Once per Turn:] After you play a Quilboar, gain 2 [Blood Gems]. """
	events = [
		BG_Play(CONTROLLER, MINION + QUILBOAR).after(BG20_203_Action(CONTROLLER, 2)),
		#BeginBar.on(SetAttr(CONTROLLER, 'once_per_turn', 0))
		]
	pass



if BG_Selfless_Hero:#Selfless Hero	2	2	1
	BG_Minion += ['BG_OG_221','TB_BaconUps_014',]#	
	BG_PoolSet_Minion[2].append('BG_OG_221')
	BG_Minion_Gold['BG_OG_221']='TB_BaconUps_014'
	pass
#Selfless Hero	2	2	1	-	### OK ###
class BG_OG_221_Action(TargetedAction):
	TARGET = ActionArg()# controller
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		controller=source.controller
		## assert controller==target
		cards = [card for card in controller.field if card.divine_shield==False]
		if len(cards)>amount:
			cards=random.sample(cards, amount)
		for card in cards:
			card.divine_shield=True
class BG_OG_221:
	"""Selfless Hero:  けんしん
	[Deathrattle:] Give a random friendly minion [Divine Shield]."""
	deathrattle = BG_OG_221_Action(CONTROLLER, 1)
class TB_BaconUps_014:# <5>[1453]
	""" Selfless Hero
	[Deathrattle:] Give 2_random friendly minions [Divine Shield]. """
	deathrattle = BG_OG_221_Action(CONTROLLER, 2)
	pass



if BG_Sparring_Partner:#### Sparring Partner (2/3/2) ### OK ####
	BG_Minion += ['BG_AT_069','BG_AT_069_G',]#	
	BG_PoolSet_Minion[2].append('BG_AT_069')
	BG_Minion_Gold['BG_AT_069']='BG_AT_069_G'
	## Sparring Partner (2) >= 23.6
	pass
class BG_AT_069:
	"""Sparring Partner (2/3/2) >= 23.6
	Taunt Battlecry: Give a minion Taunt."""
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_FRIENDLY_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Taunt(TARGET)
class BG_AT_069_G:
	"""
	[Taunt] [Battlecry:] Give a minion [Taunt]."""
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_FRIENDLY_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Taunt(TARGET)



if BG_Spawn_of_N_Zoth:#Spawn of N'Zoth	2	2	2	- ### OK ### banned 24.6
	BG_Minion += ['BG_OG_256','OG_256e','TB_BaconUps_025','TB_BaconUps_025e',]#	
	BG_PoolSet_Minion[2].append('BG_OG_256')
	BG_Minion_Gold['BG_OG_256']='TB_BaconUps_025'
	pass
class BG_OG_256:# んぞす
	""" Spawn of N'Zoth
	[Deathrattle:] Give your minions +1/+1. """
	deathrattle = Buff(FRIENDLY_MINIONS, 'OG_256e')#
	pass
OG_256e=buff(1,1)
class TB_BaconUps_025:# <12>[1453]
	""" Spawn of N'Zoth
	[Deathrattle:] Give your minions +2/+2. """
	deathrattle = Buff(FRIENDLY_MINIONS, 'TB_BaconUps_025e')#
	pass
TB_BaconUps_025e = buff(2,2)



if BG_Unstable_Ghoul:#Unstable Ghoul	2	1	3	-### OK ### ##banned 23.6
	BG_Minion += ['FP1_024','TB_BaconUps_118',]#	
	BG_PoolSet_Minion[2].append('FP1_024')
	BG_Minion_Gold['FP1_024']='TB_BaconUps_118'
	pass
class FP1_024:# <12>[1453] ぐうる
	""" Unstable Ghoul
	[Taunt]. [Deathrattle:] Deal 1 damage to all minions. """
	deathrattle = Hit(ALL_MINIONS, 1),Deaths()
	pass
class TB_BaconUps_118:# <12>[1453]
	""" Unstable Ghoul
	[Taunt][Deathrattle:] Deal 1 damage to all minions twice. """
	deathrattle = Hit(ALL_MINIONS, 1), Hit(ALL_MINIONS, 1), Deaths()
	pass



if BG_Whelp_Smuggler:#Whelp Smuggler	2	2	5	- ### OK ###
	BG_Minion += ['BG21_013','BG21_013e','BG21_013_G',]#	
	BG_PoolSet_Minion[2].append('BG21_013')
	BG_Minion_Gold['BG21_013']='BG21_013_G'
	pass
class BG21_013_Action(TargetedAction):## 密輸人
	TARGET = ActionArg()
	BUFF = ActionArg()
	TARGETBUFF = ActionArg()
	def do(self, source, target, buff, targetbuff):
		if buff.atk>0:
			Buff(target, targetbuff).trigger(target.controller)
			pass
class BG21_013:# <12>[1453]
	""" Whelp Smuggler
	After a friendly Dragon gains Attack, give it +1_Health. """
	events = Buff(FRIENDLY + DRAGON).on(BG21_013_Action(Buff.TARGET, Buff.BUFF, 'BG21_013e'))
	pass
BG21_013e=buff(0,1)
class BG21_013_G:# <12>[1453]
	""" Whelp Smuggler
	After a friendly Dragon gains Attack, give it +2_Health. """
	events = Buff(FRIENDLY + DRAGON).on(BG21_013_Action(Buff.TARGET, Buff.BUFF,'BG21_013e') * 2)
	pass




if BG_Yrel:## Yrel (2) ### need check ### banned 24.6
	BG_Minion += ['BG23_350','BG23_350e','BG23_350_G','BG23_350_Ge',]#	
	BG_PoolSet_Minion[2].append('BG23_350')
	BG_Minion_Gold['BG23_350']='BG23_350_G'
	##  Yrel (2) >=23.6
	pass
class BG23_350_Action(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	def do(self, source, target, buff):
		## in BG battle
		controller = target
		races = []
		for card in controller.field:
			if hasattr(card, 'race') and card.race != Race.INVALID and not card.race in races:
				races.append(card.race)
		if len(races)>0:
			for race in races:
				targets=[]
				if race != Race.ALL:
					for card in controller.field:
						if hasattr(card, 'race') and card.race == race:
							targets.append(card)
					if len(targets)>0:
						Buff(random.choice(targets),buff).trigger(source)
				else:
					for card in controller.field:
						if hasattr(card, 'race') and card.race == race:
							Buff(card,buff).trigger(source)
class BG23_350:
	"""Yrel (2) >=23.6
	After this attacks, give a friendly minion of each minion type +1/+2."""
	events = BG_Attack(SELF).on(BG23_350_Action(CONTROLLER, 'BG23_350e'))
BG23_350e=buff(1,2)
class BG23_350_G:
	"""Yrel (2) >=23.6
	After this attacks, give a friendly minion of each minion type +2/+4."""
	events = BG_Attack(SELF).on(BG23_350_Action(CONTROLLER, 'BG23_350_Ge'))
BG23_350_Ge=buff(2,4)


##################### TIER 3 ###################################


if BG_Arm_of_the_Empire:#Arm of the Empire	3	4	4	-		 ### maybe ###
	BG_Minion += ['BGS_110','BGS_110e','TB_BaconUps_302','TB_BaconUps_302e',]#	
	BG_PoolSet_Minion[3].append('BGS_110')
	BG_Minion_Gold['BGS_110']='TB_BaconUps_302'
	pass
class BGS_110:# <12>[1453] 帝国の腕
	""" Arm of the Empire
	Whenever a friendly [Taunt]minion is attacked,give it +2 Attack permanently. """
	events = BG_Attack(ENEMY, FRIENDLY + TAUNT).on(BuffPermanently(BG_Attack.OTHER,'BGS_110e'))
	pass
BGS_110e=buff(2,0)# <12>[1453]
""" Armed!, +2 Attack """
class TB_BaconUps_302:# <12>[1453]
	""" Arm of the Empire
	Whenever a friendly [Taunt]minion is attacked,give it +4 Attackpermanently. """
	events = BG_Attack(ENEMY, FRIENDLY + TAUNT).on(BuffPermanently(BG_Attack.OTHER,'TB_BaconUps_302e'))
	pass
TB_BaconUps_302e=buff(4,0)# <12>[1453]
""" Double Armed!, +4 Attack """



if BG_Bird_Buddy:#Bird Buddy	3	2	4	-		 ### maybe ###
	BG_Minion += ['BG21_002','BG21_002e','BG21_002_G','BG21_002_Ge',]#	
	BG_PoolSet_Minion[3].append('BG21_002')
	BG_Minion_Gold['BG21_002']='BG21_002_G'
	pass
class BG21_002:# <12>[1453]  愛鳥家
	""" Bird Buddy
	[Avenge (1):] Give your Beasts +1/+1. """
	events = Death(FRIENDLY + MINION).on(Avenge(SELF, 1, [Buff(FRIENDLY_MINIONS + BEAST, 'BG21_002e')]))
	pass
BG21_002e=buff(1,1)
""" Well Fed, +1/+1. """
class BG21_002_G:# <12>[1453]
	""" Bird Buddy
	[Avenge (1):] Give your Beasts +2/+2. """
	events = Death(FRIENDLY).on(Avenge(SELF, 1, \
		[Buff(FRIENDLY_MINIONS + BEAST, 'BG21_002_Ge')]\
		))
	pass
BG21_002_Ge=buff(2,2)# <12>[1453]
""" Well Fed,  +2/+2. """



if BG_Boulderfist_Ogre:## Boulderfist Ogre(3/6/7) ### new 25.6
	BG_Minion += ['BG_CS2_200','BG_CS2_200_G',]#	
	BG_PoolSet_Minion[3].append('BG_CS2_200')
	BG_Minion_Gold['BG_CS2_200']='BG_CS2_200_G'
class BG_CS2_200:
	""" Boulderfist Ogre
	"""
	pass
class BG_CS2_200_G:
	""" Boulderfist Ogre
	"""
	pass



if BG_Budding_Greenthumb:#Budding Greenthumb	3	1	4	-### maybe ### ##banned 23.6
	BG_Minion += ['BG21_030','BG21_030e','BG21_030_G','BG21_030_Ge',]#	
	BG_PoolSet_Minion[3].append('BG21_030')
	BG_Minion_Gold['BG21_030']='BG21_030_G'
	pass
class BG21_030:# <12>[1453]  栽培家
	""" Budding Greenthumb
	[Avenge (3):] Give adjacent minions +2/+1 permanently. """
	events = Death(FRIENDLY).on(Avenge(SELF, 3, [BuffPermanently(SELF_ADJACENT, 'BG21_030e')]))
	pass
BG21_030e=buff(2,1)
class BG21_030_G:# <12>[1453]
	""" Budding Greenthumb
	[Avenge (3):] Giveadjacent minions+4/+2 permanently. """
	events = Death(FRIENDLY).on(Avenge(SELF, 3, [BuffPermanently(SELF_ADJACENT, 'BG21_030_Ge')]))
	pass
BG21_030_Ge=buff(4,2)


#Faceless Disciple(3) (6/4) (BG24_719) ### OK ###
if BG_Faceless_Disciple:#Faceless Disciple(3) 
	BG_Minion += ['BG24_719','BG24_719_G',]#	
	BG_PoolSet_Minion[3].append('BG24_719')
	BG_Minion_Gold['BG24_719']='BG24_719_G'
class BG24_719_Target(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=source.controller
		tier=min(controller.tavern_tier+1,6)
		newcard=RandomBGAdmissible(tech_level=tier).evaluate(controller)
		Morph(target, newcard[0]).trigger(source)
		pass
class BG24_719:
	""" Faceless Disciple
	#[Battlecry:] Transform a minion into one from a Tavern Tier higher."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0  }
	play = BG24_719_Target(TARGET)
class BG24_719_G_Target(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=source.controller
		tier=min(controller.tavern_tier+2,6)
		newcard=RandomBGAdmissible(tech_level=tier).evaluate(controller)
		Morph(target, newcard[0]).trigger(source)
		pass
class BG24_719_G:
	""" Faceless Disciple
	#[Battlecry:] Transform a minion into one from 2 Tavern Tiers higher."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0  }
	play = BG24_719_G_Target(TARGET)



if BG_Houndmaster:#Houndmaster	3	4	3	-		 ### maybe ###
	BG_Minion += ['BG_DS1_070','DS1_070o','TB_BaconUps_068','TB_BaconUps_068e',]#	
	BG_PoolSet_Minion[3].append('BG_DS1_070')
	BG_Minion_Gold['BG_DS1_070']='TB_BaconUps_068'
	pass
class BG_DS1_070:# <3>[1453] 猟犬使い
	""" Houndmaster
	[Battlecry:] Give a friendly Beast +2/+2 and [Taunt]."""
	requirements = {
		PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_FRIENDLY_TARGET:0,PlayReq.REQ_MINION_TARGET:0, 
		PlayReq.REQ_TARGET_WITH_RACE:Race.BEAST }
	play = Buff(TARGET, 'DS1_070o')
	pass
DS1_070o=buff(2,2,taunt=True)
class TB_BaconUps_068:# <3>[1453]
	""" Houndmaster
	[Battlecry:] Give a friendly Beast +4/+4 and [Taunt]. """
	requirements = {
		PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_FRIENDLY_TARGET:0,PlayReq.REQ_MINION_TARGET:0, 
		PlayReq.REQ_TARGET_WITH_RACE:Race.BEAST }
	play = Buff(TARGET, 'TB_BaconUps_068e')
	pass
TB_BaconUps_068e=buff(4,4,taunt=True)# <3>[1453]
""" Master's Presence, +4/+4 and [Taunt]. """


if BG_Khadgar:#Khadgar	3	2	2	-	  	 ### maybe ###
	BG_Minion += ['BG_DAL_575','TB_BaconUps_034',]#	
	BG_PoolSet_Minion[3].append('BG_DAL_575')
	BG_Minion_Gold['BG_DAL_575']='TB_BaconUps_034'
	pass
class BG_DAL_575:#カドガー
	""" Khadgar
	Your cards that summon minions summon twice_as_many. """
	##############  infinite loop?
	events = Summon(CONTROLLER, FRIENDLY_MINIONS).after(SummonOnce(CONTROLLER, ExactCopy(Summon.CARD)))
	pass
class TB_BaconUps_034:# <4>[1453]
	""" Khadgar
	Your cards that summon minions summon three times as many. """
	events = Summon(CONTROLLER, FRIENDLY_MINIONS).after(SummonOnce(CONTROLLER, ExactCopy(Summon.CARD))*2)
	pass


if BG_Nightmare_Amalgam:##Nightmare Amalgam (3) RENEW  23.2 ## banned 24.6
	BG_Minion += ['BG_GIL_681','BG_GIL_681_G', ]#	
	BG_PoolSet_Minion[3].append('BG_GIL_681')
	BG_Minion_Gold['BG_GIL_681']='BG_GIL_681_G'
	# Nightmare Amalgam 3 RENEW  23.2
	pass
class BG_GIL_681:
	""" Nightmare Amalgam (3)
	<i>This has all minion types.</i>"""
	pass
class BG_GIL_681_G:
	""" Nightmare Amalgam (3)
	<i>This has all minion types.</i>"""
	pass


if BG_Shifter_Zerus:## Shifter Zerus (3) ### hard ### banned 24.2 ## come back 24.6
	BG_Minion += ['BGS_029','BGS_029e','TB_BaconUps_095', ]#	
	BG_PoolSet_Minion[3].append('BGS_029')
	BG_Minion_Gold['BGS_029']='TB_BaconUps_095'
	## Shifter Zerus (3) >=23.6
	pass
class BGS_029_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = source.controller
		card = RandomBGAdmissible(tech_level_less=controller.tavern_tier).evaluate(controller)
		if card[0]!=[]:
			Buff(card[0], 'BGS_029e').trigger(source)
			card[0].zone=Zone.HAND
			source.discard()
		pass
class BGS_029:## OK
	"""Shifter Zerus (3) >=23.6
	Each turn this is in your hand, transform it into a random minion."""
	class Hand:
		events = WhenDrawn(CONTROLLER, SELF).after(BGS_029_Action(SELF))
class BGS_029_Action2(TargetedAction):
	TARGET=ActionArg()## target = owner
	def do(self, source, target):
		controller = source.controller
		card = RandomBGAdmissible(tech_level_less=controller.tavern_tier).evaluate(controller)
		if card[0]!=[]:
			Buff(card[0], 'BGS_029e').trigger(source)
			card[0].zone=Zone.HAND
			target.discard()
		pass
class BGS_029e:
	class Hand:
		events = BeginBar(CONTROLLER,0).on(BGS_029_Action2(OWNER))
	pass
class TB_BaconUps_095:
	"""
	Each turn this is in your hand, transform it into a random Golden minion."""



if BG_Soul_Juggler:#Soul Juggler	3	3	5	-	 	 ### maybe ###
	BG_Minion += ['BGS_002','TB_BaconUps_075',]#	
	BG_PoolSet_Minion[3].append('BGS_002')
	BG_Minion_Gold['BGS_002']='TB_BaconUps_075'
	pass
class BGS_002:# <9>[1453] ソールジャグラー
	""" Soul Juggler
	After a friendly Demon dies, deal 3 damage to a random enemy minion. """
	events = Death(FRIENDLY + DEMON).on(Hit(RANDOM(ENEMY_MINIONS), 3))
	pass
class TB_BaconUps_075:# <9>[1453]
	""" Soul Juggler
	After a friendly Demon dies, deal 3 damage to a random enemy minion twice. """
	events = Death(FRIENDLY + DEMON).on(Hit(RANDOM(ENEMY_MINIONS), 3) * 2)
	pass



#################### TIER 4 ###################################

#regions
### Ball of Minions(BG24_017) ### OK ###
if BG_Ball_of_Minions:#Ball of Minions	4	5	5		
	BG_Minion += ['BG24_017','BG24_017e','BG24_017_G',]#	
	BG_PoolSet_Minion[4].append('BG24_017')
	BG_Minion_Gold['BG24_017']='BG24_017_G'
	pass
class BG24_017_Action(TargetedAction):
	TARGET=ActionArg()
	CARD=CardArg()
	AMOUNT=IntArg()
	def do(self, source, target, card, amount):
		controller=source.controller
		if isinstance(card, list):
			card=card[0]
		if len(controller.field):
			for repeat in range(amount):
				minion = random.choice(controller.field)
				Buff(minion, 'BG24_017e', atk=card.atk, max_health=card.max_health).trigger(source)
		pass
class BG24_017:
	""" Ball of Minions (4  5  5)
	When you sell this, give its stats to a random friendly minion."""
	events = Sell(CONTROLLER).on(BG24_017_Action(CONTROLLER, Sell.CARD, 1))
class BG24_017e:
	pass
class BG24_017_G:
	""" Ball of Minions
	When you sell this, give its stats to two random friendly minions.""" 
	events = Sell(CONTROLLER).on(BG24_017_Action(CONTROLLER, Sell.CARD, 2))
	pass



if BG_Champion_of_Y_Shaarj:#Champion of Y'Shaarj	4	4	4		 ### maybe #####banned 23.6
	BG_Minion += ['BGS_111','BGS_111e','TB_BaconUps_301','TB_BaconUps_301e',]#	
	BG_PoolSet_Minion[4].append('BGS_111')
	BG_Minion_Gold['BGS_111']='TB_BaconUps_301'
	pass
class BGS_111:# <12>[1453]  ヤシャラージュ
	""" Champion of Y'Shaarj
	Whenever a friendly [Taunt] minion is attacked, gain +1/+1 permanently. """
	events = BG_Attack(ENEMY, FRIENDLY + TAUNT).on(BuffPermanently(SELF, 'BGS_111e'))
	pass
BGS_111e=buff(1,1)# <12>[1453]
""" Y'Shaarj!!!,  +1/+1. """
class TB_BaconUps_301:# <12>[1453]
	""" Champion of Y'Shaarj
	Whenever a friendly [Taunt] minion is attacked, gain +2/+2 permanently. """
	events = BG_Attack(ENEMY, FRIENDLY + TAUNT).on(BuffPermanently(SELF, 'TB_BaconUps_301e'))
	pass
TB_BaconUps_301e=buff(2,2)# <12>[1453]
""" Y'Shaarj!!!!!!,  +2/+2. """



if BG_Defender_of_Argus:#Defender of Argus	4	3	3	 	 ### OK ###
	BG_Minion += ['EX1_093','EX1_093e','TB_BaconUps_009','TB_BaconUps_009e',]#	
	BG_PoolSet_Minion[4].append('EX1_093')
	BG_Minion_Gold['EX1_093']='TB_BaconUps_009'
	pass
class EX1_093:# <12>[1453]   アルガス
	""" Defender of Argus
	[Battlecry:] Give adjacent minions +1/+1 and [Taunt]. """
	play = Buff(SELF_ADJACENT, 'EX1_093e')
	pass
EX1_093e=buff(1,1,taunt=True)
""" Hand of Argus, +2/+2 and [Taunt]. """
class TB_BaconUps_009:# <12>[1453]
	""" Defender of Argus
	[Battlecry:] Give adjacent minions +2/+2 and [Taunt]. """
	play = Buff(SELF_ADJACENT, 'TB_BaconUps_009e')
	pass
TB_BaconUps_009e=buff(2,2,taunt=True)# <12>[1453]
""" Hand of Argus,  +2/+2 and [Taunt]. """


if BG_Fireworks_Fanatic: ##(4/4/3) new 25.6
	BG_Minion += ['BG25_922','BG25_922e','BG25_922_G','BG25_922_Ge',]#	
	BG_PoolSet_Minion[4].append('BG25_922')
	BG_Minion_Gold['BG25_922']='BG25_922_G'
	pass
class BG25_922: ######################################################
	""" Fireworks Fanatic
	Whenever you get a minion you already have, give your minions +1/+1."""
BG25_922e=buff(1,1)
class BG25_922_G:
	""" Fireworks Fanatic
	Whenever you get a minion you already have, give your minions +2/+2."""
BG25_922_Ge=buff(2,2)


if BG_Impatient_Doomsayer:#Impatient Doomsayer	4	2	6		 ### maybe ###
	BG_Minion += ['BG21_007','BG21_007_G',]#	
	BG_PoolSet_Minion[4].append('BG21_007')
	BG_Minion_Gold['BG21_007']='BG21_007_G'
	pass
	#Impatient Doomsayer	4
class BG21_007:# <12>[1453]  終魔通予言者
	""" Impatient Doomsayer
	[Avenge (4):] Add a random Demon to your hand. """
	events = Death(FRIENDLY).on(Avenge(SELF, 4, [GiveInBattle(CONTROLLER, RandomBGDemon())]))
	pass
class BG21_007_G:# <12>[1453]
	""" Impatient Doomsayer
	[Avenge (4):] Add 2 random Demons to your hand. """
	events = Death(FRIENDLY).on(Avenge(SELF, 4, [GiveInBattle(CONTROLLER, RandomBGDemon()), GiveInBattle(CONTROLLER, RandomBGDemon())]))
	pass



if BG_Majordomo_Executus:#Majordomo Executus	4	6	3		 ### OK ###
	BG_Minion += ['BGS_105','BGS_105e','TB_BaconUps_207',]#	
	BG_PoolSet_Minion[4].append('BGS_105')
	BG_Minion_Gold['BGS_105']='TB_BaconUps_207'
	pass
	#Majordomo Executus	4
class BGS_105_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		if len(controller.field)>0:
			left_card = controller.field[0]
			count=1
			for card in controller.play_this_turn:
				#if card.type==CardType.MINION and card.race==Race.ELEMENTAL:
				if race_identity(card, Race.ELEMENTAL):
					count += 1
			Buff(left_card, 'BGS_105e', atk=count, max_health=count).trigger(source)
		pass
	pass
class BGS_105:# <12>[1453]
	""" Majordomo Executus エグゼクタス
	At the end of your turn, give your left-most minion +1/+1. Repeat for each Elementalyou played this turn. """
	events = OWN_TURN_END.on(BGS_105_Action(CONTROLLER))
	pass
class BGS_105e:# <12>[1453]
	""" Aegis of the Firelord
	Increased stats. """
	pass
class TB_BaconUps_207_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		if len(controller.field)>0:
			left_card = controller.field[0]
			count=1
			for card in controller.play_this_turn:
				#if card.type==CardType.MINION and card.race==Race.ELEMENTAL:
				if race_identity(card, Race.ELEMENTAL):
					count += 1
			Buff(left_card, 'BGS_105e', atk=count*2, max_health=count*2).trigger(source)
		pass
	pass
class TB_BaconUps_207:# <12>[1453]
	""" Majordomo Executus
	At the end of your turn, giveyour left-most minion +2/+2.Repeat for each Elementalyou played this turn. """
	events = OWN_TURN_END.on(TB_BaconUps_207_Action(CONTROLLER))


#Master of Realities(4)	 ### maybe ###
if BG_Master_of_Realities:
	BG_Minion += ['BG21_036','BG21_036e','BG21_036_G','BG21_036_Ge',]#	
	BG_PoolSet_Minion[4].append('BG21_036')
	BG_Minion_Gold['BG21_036']='BG21_036_G'
	pass
# (5/6/6) -> (4/4/4) when?
class BG21_036_Action(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	def do(self, source, target, buff):
		if buff.id!='BG21_036e':
			if buff.atk>0 or buff.max_health>0:
				Buff(source, 'BG21_036e').trigger(source)
class BG21_036:# <12>[1453] 多重現実の支配者
	""" Master of Realities
	[[Taunt].] After a friendly Elemental gains stats, gain +1/+1. """
	events = Buff(FRIENDLY + ELEMENTAL).on(BG21_036_Action(SELF, Buff.BUFF))
	pass
BG21_036e=buff(1,1)
class BG21_036_G_Action(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	def do(self, source, target, buff):
		if buff.id!='BG21_036e':
			if buff.atk>0 or buff.max_health>0:
				Buff(source, 'BG21_036_Ge').trigger(source)
class BG21_036_G:# <12>[1453]
	""" Master of Realities
	[[Taunt].] After a friendly Elemental gains stats, gain +2/+2. """
	events = Buff(FRIENDLY + ELEMENTAL).on(BG21_036_G_Action(SELF, Buff.BUFF))
	pass
BG21_036_Ge=buff(2,2)# <12>[1453]
""" The Elemental Plane, +2/+2. """



if BG_Menagerie_Jug:#Menagerie Jug	4	3	3	-		 ### maybe ###
	BG_Minion += ['BGS_083','BGS_083e','TB_BaconUps_145','TB_BaconUps_145e',]#	
	BG_PoolSet_Minion[4].append('BGS_083')
	BG_Minion_Gold['BGS_083']='TB_BaconUps_145'
	pass
class BGS_083:# <12>[1453] ミナジェリ
	""" Menagerie Jug
	[Battlecry:] Give 3 random friendly minions of different minion types +2/+2. """
	play = BGS_082_Action(CONTROLLER,'BGS_083e')
	pass
BGS_083e=buff(2,2)# <12>[1453]
""" Gulp of Tea,  +2/+2. """
class TB_BaconUps_145:# <12>[1453]
	""" Menagerie Jug
	[Battlecry:] Give 3 randomfriendly minions of differentminion types +4/+4. """
	play = BGS_082_Action(CONTROLLER,'TB_BaconUps_145e')
	pass
TB_BaconUps_145e=buff(4,4)# <12>[1453]
""" Gulp of Tea,  +4/+4. """


## Reef Explorer(4) ### OK,  ### NEW 23.2 ### banned 24.6
if BG_Reef_Explorer:#
	BG_Minion += ['BG23_016','BG23_016_G', ]#	
	BG_PoolSet_Minion[4].append('BG23_016')
	BG_Minion_Gold['BG23_016']='BG23_016_G'
	# Reef Explorer 4 	
	pass
class BG23_016_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		if Config.LOGINFO:
			print("(BG23_016_Choice.choose)%s chooses %r"%(card.controller.name, card))
		card.zone=Zone.HAND
		self.player.choice=None
class BG23_016_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=target
		races = copy(random_picker.BG_races)
		tier=controller.tavern_tier
		for card in controller.field:
			if card.race in races:
				races.remove(card.race)
		BG23_016_Choice(controller, RandomBGMinion(race=races, tech_level_less=tier)*3).trigger(source)
		pass

class BG23_016:# <12>[1453]
	""" Reef Explorer(4)
	[Battlecry: Discover] a minion from a minion type you don't control."""
	play = BG23_016_Action(CONTROLLER)
	pass
class BG23_016_G_Choice(Choice):
	def choose(self, card):
		super().choose(card)
		if Config.LOGINFO:
			print("(BG23_016_Choice.choose)%s chooses %r"%(card.controller.name, card))
		card.zone=Zone.HAND
		if self.source.sidequest_counter>=1:
			self.next_choice=None
			self.player.choice=None
		else:
			self.player.choice=self.next_choice=self
			self.source.sidequest_counter=1
class BG23_016_G_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=target
		races = copy(random_picker.BG_races)
		tier=controller.tavern_tier
		for card in controller.field:
			if card.race in races:
				races.remove(card.race)
		BG23_016_G_Choice(controller, RandomBGMinion(race=races, tech_level_less=tier)*3).trigger(source)
		pass
class BG23_016_G:# <12>[1453]
	"""
	[Battlecry: Discover] 2 minions from minion types you don't control."""
	play = BG23_016_G_Action(CONTROLLER)
	pass


if BG24__Rendle_the_Mistermind:# # (4) new 24.2
	BG_Minion+=['BG24_022','BG24_022_G']
	BG_PoolSet_Minion[4].append('BG24_022')
	BG_Minion_Gold['BG24_022']='BG24_022_G'
class BG24_022_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = target
		if len(controller.opponent.field)>0:
			high=[]
			for card in controller.opponent.field:
				if high==[] or high[0].tech_level<card.tech_level:
					high=[card]
				elif high[0].tech_level==card.tech_level:
					high.append(card)
			card.zone=Zone.SETASIDE
			card.controller=controller
			card.zone=Zone.HAND
		pass
class BG24_022:# (minion)
	""" Rendle the Mistermind
	At the end of your turn, steal the highest Tier minion from Bob's_Tavern. """
	events = OWN_TURN_END.on(BG24_022_Action(CONTROLLER))
	pass
class BG24_022_G_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = target
		for repeat in range(2):
			if len(controller.opponent.field)>0:
				high=[]
				for card in controller.opponent.field:
					if high==[] or high[0].tech_level<card.tech_level:
						high=[card]
					elif high[0].tech_level==card.tech_level:
						high.append(card)
				card.zone=Zone.SETASIDE
				card.controller=controller
				card.zone=Zone.HAND
		pass
class BG24_022_G:# (minion)
	""" Rendle the Mistermind
	At the end of your turn, steal the 2 highest Tier minions from Bob's_Tavern. """
	events = OWN_TURN_END.on(BG24_022_G_Action(CONTROLLER))
	#
	pass


if BG25__Sindorei_Straight_Shot:# ## (4) new 25.2.2
	BG_Minion+=['BG25_016','BG25_016_G','BG25_016e','BG25_016e2']
	BG_PoolSet_Minion[4].append('BG25_016')
	BG_Minion_Gold['BG25_016']='BG25_016_G'
class BG25_016:# (minion)
	""" Sin'dorei Straight Shot
	<b>Windfury</b>. <b>Divine Shield</b>. Whenever this attacks, remove <b>Reborn</b> and <b>Taunt</b> from the target. """
	events = BG_Attack(SELF, ENEMY+MINION).on(Buff(BG_Attack.OTHER, 'BG25_016e'))
	pass
class BG25_016_G:# (minion)
	""" Sin'dorei Straight Shot
	<b>Mega-Windfury</b>. <b>Divine Shield</b>. Whenever this attacks, remove <b>Reborn</b> and <b>Taunt</b> from the target. """
	events = BG_Attack(SELF, ENEMY+MINION).on(Buff(BG_Attack.OTHER, 'BG25_016e'))
	pass
BG25_016e=buff(reborn=False,taunt=False)
BG25_016e2=buff(taunt=False)



if BG_Strongshell_Scavenger:#Strongshell Scavenger	4	2	3		 ### OK ###
	BG_Minion += ['BG_ICC_807',  'ICC_807e',  'TB_BaconUps_072', 'TB_BaconUps_072e',]#	
	BG_PoolSet_Minion[4].append('BG_ICC_807')
	BG_Minion_Gold['BG_ICC_807']='TB_BaconUps_072'
	pass
class BG_ICC_807:# <2>[1453]  クズ拾い
	""" Strongshell Scavenger
	[Battlecry:] Give your [Taunt] minions +2/+2. """
	play = Buff(FRIENDLY + TAUNT, 'ICC_807e')
	pass
ICC_807e=buff(2,2)# <12>[1453]
""" Strongshell,  +2/+2. """
class TB_BaconUps_072:# <2>[1453]
	""" Strongshell Scavenger
	[Battlecry:] Give your [Taunt] minions +4/+4. """
	play = Buff(FRIENDLY + TAUNT, 'TB_BaconUps_072e')
	pass
TB_BaconUps_072e=buff(4,4)# <12>[1453]
""" Strongshell,  +4/+4. """


if BG_Treasure_Seeker_Elise: ##(4) new 24.2
	BG_Minion += ['BG23_353','BG23_353_G', 'BG23_353_Gt']#	
	BG_PoolSet_Minion[4].append('BG23_353')
	BG_Minion_Gold['BG23_353']='BG23_353_G'
class BG23_353:
	""" Treasure-Seeker Elise
	After you [Refresh] 5 times, find the [Golden] Monkey(BG23_353_Gt)! [(@ left!)]"""
	events = Rerole(CONTROLLER).on(SidequestCounter(SELF, 5, [Give(CONTROLLER, 'BG23_353_Gt')]))
	pass
class BG23_353_G:
	""" Treasure-Seeker Elise
	After you [Refresh] 5 times, find two [Golden] Monkeys!(BG23_353_Gt) [(@ left!)]"""
	events = Rerole(CONTROLLER).on(SidequestCounter(SELF, 5, [Give(CONTROLLER, 'BG23_353_Gt'), Give(CONTROLLER, 'BG23_353_Gt')]))
	pass
class BG23_353_Gt:
	pass



if BG_Tunnel_Blaster:## Tunnel Blaster (4) ### OK ###
	BG_Minion += ['BG_DAL_775','BG_DAL_775_G', ]#	
	BG_PoolSet_Minion[4].append('BG_DAL_775')
	BG_Minion_Gold['BG_DAL_775']='BG_DAL_775_G'
	## Tunnel Blaster (4) >= 23.6
	pass
class BG_DAL_775: 
	"""Tunnel Blaster (4) >= 23.6
	Taunt Deathrattle: Deal 3 damage to all minions."""
	deathrattle = Hit(ALL_MINIONS, 3)
class BG_DAL_775_G:
	"""
	[Taunt] [Deathrattle:] Deal 3 damage to all minions twice."""
	deathrattle = Hit(ALL_MINIONS, 3) * 2




#Vigilant Stoneborn(4)(2/6)(BG24_023) ### OK ###
if BG_Vigilant_Stoneborn:#Vigilant Stoneborn	4	2	6		
	BG_Minion += ['BG24_023','BG24_023_G','BG24_023_Ge','BG24_023e']#	
	BG_PoolSet_Minion[4].append('BG24_023')
	BG_Minion_Gold['BG24_023']='BG24_023_G'
class BG24_023:
	""" Vigilant Stoneborn
	#[Battlecry:] Give a minion +6 Health and [Taunt]."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	play = Buff(TARGET, 'BG24_023e')
BG24_023e=buff(0,6, taunt=True)
class BG24_023_G:
	""" Vigilant Stoneborn
	#[Battlecry:] Give a minion +12 Health and [Taunt]."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }	# 
	play = Buff(TARGET, 'BG24_023_Ge')
BG24_023_Ge=buff(0,12, taunt=True)




#Witchwing Nestmatron	4	3	5### maybe ### banned 24.2 ## renew 25.0.4
if BG_Witchwing_Nestmatron:#
	BG_Minion += ['BG21_038','BG21_038_G',]#	
	BG_PoolSet_Minion[4].append('BG21_038')
	BG_Minion_Gold['BG21_038']='BG21_038_G'
	pass
class BG21_038:# <12>[1453] 巣母
	""" Witchwing Nestmatron
	[Avenge (3):] Add a random [Battlecry] minion to your_hand. """
	events = Death(FRIENDLY).on(Avenge(SELF, 3, [GiveInBattle(CONTROLLER, RandomBGAdmissible(has_battlecry=True))]))
	pass
class BG21_038_G:# <12>[1453]
	""" Witchwing Nestmatron
	[Avenge (3):] Add 2 random [Battlecry] minions to your_hand. """
	events = Death(FRIENDLY).on(Avenge(SELF, 3, [GiveInBattle(CONTROLLER, RandomBGAdmissible(has_battlecry=True)), Give(CONTROLLER, RandomMinion(has_battlecry=True))]))
	pass




######## TIER 5 ################


if BG_Baron_Rivendare:#Baron Rivendare	5	1	7		 ### maybe ###
	BG_Minion += ['BG_FP1_031','TB_BaconUps_055',]#	
	BG_PoolSet_Minion[5].append('BG_FP1_031')
	BG_Minion_Gold['BG_FP1_031']='TB_BaconUps_055'
	pass
class BG_FP1_031:# ばろん
	"""Baron Rivendare
	Your minions trigger their [Deathrattles] twice."""
	update = Refresh(CONTROLLER, {GameTag.EXTRA_DEATHRATTLES: True})
	pass
class TB_BaconUps_055:# <12>[1453]
	""" Baron Rivendare
	Your minions trigger their [Deathrattles] three times. """
	update = Refresh(CONTROLLER, {GameTag.EXTRA_DEATHRATTLES_ADDITIONAL: True})
	pass


if BG_Brann_Bronzebeard:#Brann Bronzebeard	5	2	4		 ### maybe ###
	BG_Minion += ['BG_LOE_077','LOE_077e','TB_BaconUps_045','TB_BaconUps_045e',]#	
	BG_PoolSet_Minion[5].append('BG_LOE_077')
	BG_Minion_Gold['BG_LOE_077']='TB_BaconUps_045'
	pass
class BG_LOE_077:#    ぶらん
	""" Brann Bronzebeard
	Your [Battlecries] trigger twice. """
	update = Refresh(CONTROLLER, {GameTag.EXTRA_BATTLECRIES_BASE: True})
	pass
class LOE_077e:# 
	""" Bronzebeard Battlecry
	Your [Battlecries] trigger twice. """
	pass
class TB_BaconUps_045:# <12>[1453]
	""" Brann Bronzebeard
	Your [Battlecries] trigger three times. """
	update = Refresh(CONTROLLER, {GameTag.EXTRA_BATTLECRIES_ADDITIONAL: True})
	pass
class TB_BaconUps_045e:# <12>[1453]
	""" Bronzebeard Battlecry
	Your [Battlecries] trigger three times. """
	pass




if BG_Deadly_Spore:##Deadly Spore	5	1	1	### OK #####banned 23.6
	BG_Minion += ['BGS_131','TB_BaconUps_251',]#	
	BG_PoolSet_Minion[5].append('BGS_131')
	BG_Minion_Gold['BGS_131']='TB_BaconUps_251'
	pass
class BGS_131:# <12>[1453]  横死の胞子
	""" Deadly Spore
	[Poisonous] """
	pass
class TB_BaconUps_251:# <12>[1453]
	""" Deadly Spore
	[Poisonous] """
	pass


#Interrogator Whitemane 5  5  8 (BG24_704) ## new 24.6 ### OK ###
if BG_Interrogator_Whitemane:#Interrogator Whitemane 5  5  8 (BG24_704) 
	BG_Minion += ['BG24_704','BG24_704_e','BG24_704_e_G','BG24_704_G']#	
	BG_PoolSet_Minion[5].append('BG24_704')
	BG_Minion_Gold['BG24_704']='BG24_704_G'
	pass
class BG24_704_Action1(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		controller=source.controller
		opponent=controller.opponent
		size1=len(controller.field)
		size2=len(opponent.field)
		index1 = controller.field.index(source)
		index2=int(-index1*1.0+(size1-1)*0.5+(size2-1)*0.5)
		if 0<=index2 and index2<size2:
			card=opponent.field[index2]
			Buff(card, buff).trigger(source)
		pass
class BG24_704:
	""" Interrogator Whitemane -> banned 25.0.4
	#[x][Start of Combat:] Give the enemies opposite this [Taunt]. They take double damage."""
	events = BeginBattle(CONTROLLER).on(BG24_704_Action1(SELF, 'BG24_704_e'))
class BG24_704_e:
	def apply(self, target):
		if target==None:
			return
		if hasattr(target, 'double_damage'):
			target.double_damage=1
		target.taunt=True
	pass

class BG24_704_G:
	""" Interrogator Whitemane
	#[Start of Combat:] Give the enemies opposite this [Taunt]. They take triple damage."""
	events = BeginBattle(CONTROLLER).on(BG24_704_Action1(SELF, 'BG24_704_e_G'))
class BG24_704_e_G:
	def apply(self, target):
		if target==None:
			return
		if hasattr(target, 'double_damage'):
			target.double_damage=2
		target.taunt=True
	pass



if BG_Kangor_s_Apprentice:#Kangor's Apprentice	5	3	6		 ### maybe ###
	BG_Minion += ['BGS_012','TB_BaconUps_087',]#	
	BG_PoolSet_Minion[5].append('BGS_012')
	BG_Minion_Gold['BGS_012']='TB_BaconUps_087'
	pass
class BGS_012_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		controller = target
		cards = []
		for card in controller.death_log:
			if race_identity(card,Race.MECHANICAL):
				cards.append(card)
		for repeat in range(amount):
			if repeat<len(cards):
				Summon(controller, cards[repeat].id).trigger(source)
class BGS_012:# <12>[1453]   ケンゴー
	""" Kangor's Apprentice
	[Deathrattle]: Summon the first 2 friendly Mechs that died this combat. """
	deathrattle = BGS_012_Action(CONTROLLER, 2)
	pass
class TB_BaconUps_087:# <12>[1453]
	""" Kangor's Apprentice
	[Deathrattle]: Summon the first 4 friendly Mechs that died this combat. """
	deathrattle = BGS_012_Action(CONTROLLER, 4)
	#
	pass



if BG_Leeroy_the_Reckless:## Leeroy the Reckless (5)  ### maybe ###
	BG_Minion += ['BG23_318','BG23_318_G', ]#	
	BG_PoolSet_Minion[5].append('BG23_318')
	BG_Minion_Gold['BG23_318']='BG23_318_G'
	# Leeroy the Reckless 5 NEW 23.2
	pass
class BG23_318_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		killer = target.attacker
		if hasattr(killer,'charge'):# instead of isinstance(killer, Minion)
			Destroy(killer).trigger(source.controller)
		pass
class BG23_318:# <12>[1453]
	""" Leeroy the Reckless (5)
	[Deathrattle:] Destroy the minion that killed this."""
	deathrattle = BG23_318_Action(SELF)
	pass
class BG23_318_G:# <12>[1453]
	"""
	[Deathrattle:] Destroy the minion that killed this."""
	deathrattle = BG23_318_Action(SELF)
	pass



if BG_Lightfang_Enforcer:#Lightfang Enforcer	5	2	2		 ### need check ###
	BG_Minion += ['BGS_009','BGS_009e','TB_BaconUps_082','TB_BaconUps_082e',]#	
	BG_PoolSet_Minion[5].append('BGS_009')
	BG_Minion_Gold['BGS_012']='TB_BaconUps_082'
	pass
class BGS_009_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		races=[]
		cards=[]
		for card in controller.field:
			if card.race==Race.INVALID:
				pass
			elif card.race==Race.ALL:
				races.append(card.race)
				cards.append(card)
			elif not card.race in races:
				races.append(card.race)
				cards.append(card)
		for card in cards:
			Buff(source, 'BGS_009e').trigger(source)
class BGS_009:# <12>[1453]  光牙
	""" Lightfang Enforcer
	At the end of your turn, give a friendly minion of each minion type +2/+2. """
	events = OWN_TURN_END.on(BGS_009_Action(CONTROLLER))
	pass
BGS_009e=buff(2,2)# <7>[1453]
""" Blessed,	Increased stats. """
class TB_BaconUps_082:# <12>[1453]
	""" Lightfang Enforcer
	At the end of your turn,give a friendly minionof each minion type+4/+4. """
	events = OWN_TURN_END.on(BGS_009_Action(CONTROLLER, 4))
	pass
class TB_BaconUps_082e:# <7>[1453]
	""" Blessed
	Increased stats. """





if BG_Mythrax_the_Unraveler:#Mythrax the Unraveler	5	4	4		 ### maybe ### banned 24.2 ## revive 25.0.4
	BG_Minion += ['BGS_202','BGS_202e','TB_BaconUps_258','TB_BaconUps_258e',]#	
	BG_PoolSet_Minion[5].append('BGS_202')
	BG_Minion_Gold['BG21_036']='TB_BaconUps_258'
	pass
class BGS_202_Action(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	def do(self, source, target, buff):
		controller = target
		races=[]
		for card in controller.field:
			if card.race==Race.INVALID:
				pass
			elif card.race==Race.ALL:
				races.append(card.race)
			elif not card.race in races:
				races.append(card.race)
		buffsize = len(races)
		for repeat in range(buffsize):
			Buff(source, buff).trigger(source)
class BGS_202:# <12>[1453] ミスラクス
	""" Mythrax the Unraveler
	At the end of your turn,gain +2/+2 for each__minion type you control. """
	events = OWN_TURN_END.on(BGS_202_Action(CONTROLLER, 'BGS_202e'))
	pass
BGS_202e=buff(2,2)# <12>[1453]
""" Void Echoes, +2/+2. """
class TB_BaconUps_258:# <12>[1453]
	""" Mythrax the Unraveler
	At the end of your turn,gain +4/+4 for each__minion type you control. """
	events = OWN_TURN_END.on(BGS_202_Action(CONTROLLER, 'TB_BaconUps_258e'))
	pass
TB_BaconUps_258e=buff(4,4)# <12>[1453]
""" Void Echoes, +4/+4. """




if BG_Nomi_Kitchen_Nightmare:#Nomi, Kitchen Nightmare	5	4	4	### OK ###
	BG_Minion += ['BGS_104','BGS_104e1','BGS_104pe','TB_BaconUps_201',]#	
	BG_PoolSet_Minion[5].append('BGS_104')
	BG_Minion_Gold['BGS_104']='TB_BaconUps_201'
	pass
class BGS_104_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		controller = target
		controller.nomi_powered_up += amount
class BGS_104:# <12>[1453]  ノミ（🐼）
	""" Nomi, Kitchen Nightmare
	After you play an Elemental,Elementals in Bob's Tavern have +1/+1 for the restof the game. """
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(BGS_104_Action(CONTROLLER, 1))
	pass
class BGS_104e1:# <12>[1453]
	""" Tavern Feast
	Increased stats. """
BGS_104pe=buff(1,1)# <12>[1453]
""" Nomi Player Enchant
Increased stats. """
class TB_BaconUps_201:# <12>[1453]
	""" Nomi, Kitchen Nightmare
	After you play an Elemental,Elementals in Bob's Tavernhave +2/+2 for the restof the game. """
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(BGS_104_Action(CONTROLLER, 2))
	pass



if BG25__Titus_Rivendare:# 5/1/7 neutral ## new 25.2.2
	BG_Minion+=['BG25_354','BG25_354_G']
	BG_PoolSet_Minion[5].append('BG25_354')
	BG_Minion_Gold['BG25_354']='BG25_354_G'
class BG25_354:# (minion)
	""" Titus Rivendare
	Your <b>Deathrattles</b> trigger an extra time. """
	update = Refresh(CONTROLLER, {GameTag.EXTRA_DEATHRATTLES: True})
	pass

class BG25_354_G:# (minion)
	""" Titus Rivendare
	Your <b>Deathrattles</b> trigger 2 extra times. """
	update = Refresh(CONTROLLER, {GameTag.EXTRA_DEATHRATTLES_ADDITIONAL: True})
	pass



if BG24__Tortollan_Blue_Shell:# new 24.2 (5) ### OK ###
	BG_Minion+=['BG24_018','BG24_018_G']
	BG_PoolSet_Minion[5].append('BG24_018')
	BG_Minion_Gold['BG24_018']='BG24_018_G'
class BG24_018_Action(TargetedAction):
	TARGET=ActionArg()#controller
	AMOUNT=IntArg()
	def do(self, source, target, amount):
		controller=source.controller
		## tag 1587 gambler_sell_price
		SetAttr(source, 'gambler_sell_price', amount).trigger(source)
class BG24_018:# (minion, 5)
	""" Tortollan Blue Shell
	If you lost your last combat, this minion sells for 5 Gold. """
	tags={1587:1}
	events = [
		LoseGame(CONTROLLER).on(BG24_018_Action(CONTROLLER,5)),
		TieGame(CONTROLLER).on(BG24_018_Action(CONTROLLER,1)),
		WinGame(CONTROLLER).on(BG24_018_Action(CONTROLLER,1))
	]
	pass
class BG24_018_G:# (minion)
	""" Tortollan Blue Shell
	If you lost your last combat, this minion sells for 10 Gold. """
	events = [
		LoseGame(CONTROLLER).on(BG24_018_Action(CONTROLLER,10)),
		TieGame(CONTROLLER).on(BG24_018_Action(CONTROLLER,1)),
		WinGame(CONTROLLER).on(BG24_018_Action(CONTROLLER,1))
	]
	pass


#############TIER 6######################


if BG_Amalgadon:#Amalgadon	6	6	6	*	 	 ### need check ###  banned 22.3
	BG_Minion += ['BGS_069','TB_BaconUps_121',]#	
	BG_PoolSet_Minion[6].append('BGS_069')
	BG_Minion_Gold['BGS_069']='TB_BaconUps_121'
	pass
class BGS_069_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, amount):
		controller = target
		races=[]
		for card in controller.field:
			if card.race==Race.INVALID:
				pass
			elif card.race==Race.ALL:
				races.append(card.race)
			elif not card.race in races:
				races.append(card.race)
		buffsize = len(races)*amount
		for repeat in range(buffsize):
			# adapting something
			buff = random.choice(['UNG_999t2e','UNG_999t3e','UNG_999t4e','UNG_999t6e','UNG_999t7e','UNG_999t8e','UNG_999t13e','UNG_999t14e'])
			Buff(source, buff).trigger(source)
		pass
class BGS_069:##  アマルガドン (アルマゲドンではない）
	""" Amalgadon
	[Battlecry:] For each different minion type you have among other minions, [Adapt] randomly."""
	play = BGS_069_Action(CONTROLLER, 1)	
	pass
class TB_BaconUps_121:
	""" Amalgadon
	[Battlecry:] For each different minion type you have among other minions, [Adapt] randomly twice."""
	play = BGS_069_Action(CONTROLLER, 2)
	pass

UNG_999t14e=buff(1,1)## 火山の力 ## +1/+1
UNG_999t13e=buff(poisonous=True)## 猛毒の唾 ## 猛毒
#class UNG_999t10e:## 霧隠れ ## 次の自分のターンまで隠れ身状態。
class UNG_999t8e:## 電気の盾 # 聖なる盾
	def apply(self,target):
		target.divine_shield=True
		pass
UNG_999t7e=buff(windfury=True)## 電光石火 # 疾風
UNG_999t6e=buff(taunt=True)## 巨体 # 挑発
#class UNG_999t5e:## 液状膜 ## 呪文とヒーローパワーの標的にならない。
UNG_999t4e=buff(0,3)## 岩状の甲殻 ## 体力+3
UNG_999t3e=buff(3,0)## 炎熱の爪 ##攻撃力+3
class UNG_999t2e:## 動き回る胞子 ##;断末魔:]1/1の植物を2体召喚する。
	tags={GameTag.DEATHRATTLE:True}
	deathrattle = Summon(CONTROLLER, 'UNG_999t2t1')*2
class UNG_999t2t1:## 植物
	""" """




if BG_Friend_of_a_Friend:#Friend of a Friend	(BAN)	6	5	6	-	Battlecry   BG22_404 BG22_404_G 
	BG_Minion += ['BG22_404','BG22_404_G',]#	
	BG_PoolSet_Minion[6].append('BG22_404')
	BG_Minion_Gold['BG22_404']='BG22_404_G'
	pass
class BG22_404:# <12>[1453] 友達の友達 ばん！##########################
	""" Friend of a Friend(BAN)
	[Battlecry: Discover] a Buddy. """
	#
	pass
class BG22_404_G:# <12>[1453]
	""" Friend of a Friend(BAN)
	[Battlecry: Discover]two Buddies. """
	#
	pass



if BG_Mantid_Queen:##########
	BG_Minion += ['BG22_402', 'BG22_402_G', 'BG22_402e', 'BG22_402e2', 'BG22_402e3', 'BG22_402e4' ]#	
	BG_PoolSet_Minion[6].append('BG22_402')
	BG_Minion_Gold['BG22_402']='BG22_402_G'
class BG22_402: ###########################################
	""" Mantid Queen
	[Poisonous]. [Start of Combat:] For each of your minion types gain +5/+5, [Windfury], ___[Divine Shield], or [Taunt]."""
	pass
class BG22_402_G: 
	""" Mantid Queen
	[Poisonous]. [Start of Combat:] For each of your minion types gain [Windfury], [Divine Shield], _[Taunt], or +5/+5, twice."""
	pass
BG22_402e=buff(5,5)
BG22_402e2=buff(windfury=True)
BG22_402e3=buff(divine_shield=True)
BG22_402e4=buff(taunt=True)



if BG_Nadina_the_Red:#Nadina the Red	6	7	4		 ### maybe OK ###
	BG_Minion += ['BGS_040','TB_BaconUps_154',]#	
	BG_PoolSet_Minion[6].append('BGS_040')
	BG_Minion_Gold['BGS_040']='TB_BaconUps_154'
	pass
class BGS_040:# <12>[1453]  ナディナ
	""" Nadina the Red
	[Deathrattle:] Give your Dragons [Divine Shield]. """
	deathrattle = GiveDivineShield(FRIENDLY_MINIONS + DRAGON)
	pass
class TB_BaconUps_154:# <12>[1453]
	""" Nadina the Red
	[Deathrattle:] Give your Dragons [Divine Shield]. """
	deathrattle = GiveDivineShield(FRIENDLY_MINIONS + DRAGON)
	pass



if BG_Orgozoa_the_Tender:### Orgozoa, the Tender(6) ### OK ### NEW 23.2
	BG_Minion += ['BG23_015','BG23_015t','BG23_015_G','BG23_015_Gt',]#	
	BG_PoolSet_Minion[6].append('BG23_015')
	BG_Minion_Gold['BG23_015']='BG23_015_G'
	pass
class BG23_015:# <12>[1453]
	""" Orgozoa, the Tender(6)
	[Spellcraft: Discover] a Naga."""
	play = Spellcraft(CONTROLLER,'BG23_015t')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG23_015t'))
	tags={2359:'BG23_015t'}
class BG23_015t:
	play = Discover(CONTROLLER, RandomBGNaga(tech_level_less=TIER(CONTROLLER)))
	tags = {GameTag.TECH_LEVEL:5}
	class Hand:
		events = EndTurn(CONTROLLER).on(Destroy(SELF))
pass
class BG23_015_G:# <12>[1453]
	"""
	[Spellcraft: Discover] 2 Naga.</enUS>"""
	play = Spellcraft(CONTROLLER,'BG23_015_Gt')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG23_015_Gt'))
	tags={2359:'BG23_015_Gt'}
	pass
class BG23_015_Gt:
	play = DiscoverTwice(CONTROLLER, RandomBGNaga(tech_level_less=TIER(CONTROLLER))*3)
	class Hand:
		events = EndTurn(CONTROLLER).on(Destroy(SELF))
	pass




if BG_Seafood_Slinger:#Seafood Slinger	6	5	5		 ### maybe ### ##banned -> resurrect 25.0.4
	BG_Minion += ['BG21_011','BG21_011e','BG21_011e2','BG21_011_G','BG21_011_Ge',]#	
	BG_PoolSet_Minion[6].append('BG21_011')
	BG_Minion_Gold['BG21_011']='BG21_011_G'
	pass
class BG21_011:# <12>[1453] 板前
	""" Seafood Slinger
	[Battlecry:] Make a Murloc Golden. """
	requirements={
		PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.MURLOC }
	play = MorphGold(TARGET)
	pass
BG21_011e=buff(3,3)# <12>[1453] ??????????????
class BG21_011e2:# <12>[1453]  ??????????????
	""" Battlecry Self-Trigger [DNT] """
class BG21_011_G:# <12>[1453]
	""" Seafood Slinger
	[Battlecry:] Make a Murloc Golden. """
	requirements={
		PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.MURLOC }
	play = MorphGold(TARGET)
	pass
BG21_011_Ge=buff(6,6)# <12>[1453]  ????????????


if BG24__Tea_Master_Theotar: # (6) new 24.2
	BG_Minion += ['BG24_020','BG24_020e','BG24_020_G','BG24_020_Ge', ]#	
	BG_PoolSet_Minion[6].append('BG24_020')
	BG_Minion_Gold['BG24_020']='BG24_020_G'
class BG24_020_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		if target.type==CardType.MINION and target.race==Race.INVALID:
			races=[]
			controller = source.controller
			for card in controller.field:
				if races==[] or not card.race in races:
					races.append(card.race)
			if len(races)>3:
				races = random.sample(races, 3)
			for race in races:
				cards = [card for card in controller.field if card.race==race]
				card = random.choice(cards)
				Buff(card, buff).trigger(source)
		pass
class BG24_020:	
	""" Tea Master Theotar
	After you play a minion with no_minion_type, give 3_friendly minions of different types +2/+2. """
	events = Play(CONTROLLER, MINION).on(BG24_020_Action(Play.CARD,'BG24_020e'))
	pass
BG24_020e=buff(2,2)
class BG24_020_G:# (minion)
	""" Tea Master Theotar
	After you play a minion with no_minion_type, give 3_friendly minions of different types +4/+4. """
	events = Play(CONTROLLER, MINION).on(BG24_020_Action(Play.CARD,'BG24_020_Ge'))
	#
	pass
BG24_020_Ge=buff(4,4)


if BG24_The_Walking_Fort: # (6) new 24.2 ### OK ###
	BG_Minion += ['BG24_712','BG24_712e','BG24_712_G','BG24_712e_G', ]#	
	BG_PoolSet_Minion[6].append('BG24_712')
	BG_Minion_Gold['BG24_712']='BG24_712_G'
class BG24_712_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		controller=target
		cards = [card for card in controller.field if card.type==CardType.MINION and card.taunt==True]
		if len(cards)>4:
			cards=random.sample(cards, 4)
		for card in cards:
			Buff(card, buff).trigger(source)
		pass
class BG24_712:
	""" The Walking Fort(BG24_712) 4/6
	At the end of your turn, give 4 friendly [Taunt] minions +4/+4. """
	events = OWN_TURN_END.on(BG24_712_Action(CONTROLLER, 'BG24_712e'))
	pass
BG24_712e=buff(4,4)
class BG24_712_G:
	"""
	At the end of your turn, give 4 friendly [Taunt] minions +8/+8."""
	events = OWN_TURN_END.on(BG24_712_Action(CONTROLLER, 'BG24_712e_G'))
	pass
BG24_712e_G=buff(8,8)


## Uther the Lightbringer (6) ### OK ###
if BG_Uther_the_Lightbringer: ##(6)
	BG_Minion += ['BG23_190','BG23_190e','BG23_190_G','BG23_190_Ge', ]#	
	BG_PoolSet_Minion[6].append('BG23_190')
	BG_Minion_Gold['BG23_190']='BG23_190_G'
	## Uther the Lightbringer (6) >= 23.6
	pass
class BG23_190_Action(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, buff, amount):
		if target:
			atk_buff = amount - target.atk
			hlt_buff = amount - target.health
			Buff(target, buff, atk=atk_buff, max_health=hlt_buff).trigger(source)
			pass
class BG23_190:
	"""Uther the Lightbringer (6) >= 23.6
	Battlecry: Set a minion's Attack and Health to 15."""
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_FRIENDLY_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}	
	play = BG23_190_Action(TARGET, 'BG23_190e', 15)
class BG23_190e:
	pass
class BG23_190_G:
	"""
	[Battlecry:] Set a minion's Attack and Health to 30."""
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_FRIENDLY_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}	
	play = BG23_190_Action(TARGET, 'BG23_190_Ge', 30)
class BG23_190_Ge:
	pass




if BG_Zapp_Slywick:#Zapp Slywick	6	7	10	 	 ### maybe ###
	BG_Minion += ['BGS_022','TB_BaconUps_091',]#	
	BG_PoolSet_Minion[6].append('BGS_022')
	BG_Minion_Gold['BGS_022']='TB_BaconUps_091'
	pass
class BGS_022:# <12>[1453] ざっぷ
	""" Zapp Slywick
	[Windfury]This minion always attacks the enemy minion with the lowest Attack. """
	#<ReferencedTag enumID="189" name="WINDFURY" type="Int" value="1"/> ### REF-TAGだ！
	tags = {GameTag.WINDFURY:1}
	#本体実装はBG_Battle.pyの80行あたり
	pass
class TB_BaconUps_091:# <12>[1453]
	""" Zapp Slywick
	[Mega-Windfury]This minion always attacksthe enemy minion withthe lowest Attack. """
	#<Tag enumID="189" name="WINDFURY" type="Int" value="3"/> ###これはオケ
	pass




#######################



#if BG25__Cyborg_Enhancement:# 
#	BG25_+=['BG25_901e']
#class BG25_901e:# (enchantment)
#	""" Cyborg Enhancement
#	+10 Attack. """
#	#
#	pass
#
#	BG25_+=['BG25_901e2']
#class BG25_901e2:# (enchantment)
#	""" Cyborg Enhancement
#	+20 Attack. """
#	#
#	pass

#if BG25__Yaharr:# 
#	BG25_+=['BG25_910t15e']
#class BG25_910t15e:# (enchantment)
#	""" Yaharr!!
#	+2/+2. """
#	#
#	pass

########################