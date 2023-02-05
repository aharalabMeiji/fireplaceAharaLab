from ..utils import *

BG_Rockpool_Hunter=True ##(1) 
BG_Swampstriker=True ## (1)

BG_Murloc_Warleader=True ## (2)
BG_Saltscale_Honcho=True ## (2)
BG_Tad=True ## (2)
BG_Blazing_Sklyfin=True ## (2/1/3)

BG_Coldlight_Seer=True ## (3)
BG_Felfin_Navigator=True ## (3)
BG_Swolefin=True ## (3)

BG_Primalfin_Lookout=True ## (4)

BG_King_Bagurgle=True ## (5)
BG_SI_Sefin=False ## (5) banned 4.2
BG_Toxfin=True ##(4) new 24.2 -> (6) ## 25.2.2 (5)

BG_Young_Murk_Eye=True ## (6) 


BG_Minion_Murloc =[]

BG_PoolSet_Murloc=[[],[],[],[],[],[],[]]

BG_Murloc_Gold={}


#Rockpool Hunter (1)  ## OK ##
if BG_Rockpool_Hunter:
	BG_Minion_Murloc+=['BG_UNG_073','UNG_073e','TB_BaconUps_061','TB_BaconUps_061e',]
	BG_PoolSet_Murloc[1].append('BG_UNG_073')
	BG_Murloc_Gold['BG_UNG_073']='TB_BaconUps_061'
class BG_UNG_073:
	""" >Rockpool Hunter
	[Battlecry:] Give a friendly Murloc +1/+1. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.MURLOC }
	play = Buff(TARGET, 'UNG_073e')
	pass
UNG_073e=buff(1,1)
class TB_BaconUps_061:# <12>[1453]
	""" Rockpool Hunter
	[Battlecry:] Give a friendly Murloc +2/+2. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.MURLOC }
	play = Buff(TARGET, 'TB_BaconUps_061e')
	pass
TB_BaconUps_061e=buff(2,2)


#Swampstriker (1)  ## OK ##
if BG_Swampstriker:
	BG_Minion_Murloc+=['BG22_401','BG22_401e','BG22_401_G','BG22_401_Ge',]
	BG_PoolSet_Murloc[1].append('BG22_401')
	BG_Murloc_Gold['BG22_401']='BG22_401_G'
class BG22_401:# <12>[1453]
	""" Swampstriker
	After you summon a Murloc, gain +1 Attack. """
	events = Summon(CONTROLLER, FRIENDLY + MURLOC).after(Buff(SELF, 'BG22_401e'))
	pass
BG22_401e=buff(1,0)
class BG22_401_G:# <12>[1453]
	""" Swampstriker
	After you summon a Murloc, gain +2 Attack. """
	events = Summon(CONTROLLER, FRIENDLY + MURLOC).after(Buff(SELF, 'BG22_401_Ge'))
	pass
BG22_401_Ge=buff(2,0)



#Murloc Warleader (2)  ### maybe ###
if BG_Murloc_Warleader:
	BG_Minion_Murloc+=['BG_EX1_507','EX1_507e','TB_BaconUps_008','TB_BaconUps_008e',]
	BG_PoolSet_Murloc[2].append('BG_EX1_507')
	BG_Murloc_Gold['BG_EX1_507']='TB_BaconUps_008'
class BG_EX1_507:
	"""Murloc Warleader 戦隊長
	"""
	update = Refresh(FRIENDLY_MINIONS + MURLOC - SELF, buff="EX1_507e")
	pass
EX1_507e=buff(2,0)
class TB_BaconUps_008:# <12>[1453]
	""" Murloc Warleader
	Your other Murlocs have +4 Attack. """
	update = Refresh(FRIENDLY_MINIONS + MURLOC - SELF, buff="TB_BaconUps_008e")
	pass
TB_BaconUps_008e=buff(4,0)# <12>[1453]
""" Mrgglaargl!,  +4 Attack from Murloc Warleader. """



#Saltscale Honcho (2) ### maybe ###
if BG_Saltscale_Honcho:
	BG_Minion_Murloc+=['BG21_008','BG21_008e','BG21_008_G','BG21_008_Ge',]
	BG_PoolSet_Murloc[2].append('BG21_008')
	BG_Murloc_Gold['BG21_008']='BG21_008_G'
class BG21_008:# <12>[1453] そるとすけいる
	""" Saltscale Honcho
	After you play a Murloc, give two other friendly Murlocs +1 Health. """
	events = BG_Play(CONTROLLER, FRIENDLY + MURLOC).after(Buff(RANDOM(FRIENDLY_MINIONS + MURLOC - SELF),'BG21_008e') * 2)
	pass
BG21_008e=buff(0,1)# <12>[1453]
""" Salty, +1 Health. """
class BG21_008_G:# <12>[1453]
	""" Saltscale Honcho
	After you play a Murloc, give two other friendly Murlocs +2 Health. """
	events = BG_Play(CONTROLLER, FRIENDLY+MURLOC).after(Buff(RANDOM(FRIENDLY_MINIONS + MURLOC - SELF),'BG21_008_Ge') * 2)
	pass
BG21_008_Ge=buff(0,2)# <12>[1453]
""" Extra Salty
+2 Health. """



#Tad (2) ### maybe ###
if BG_Tad:
	BG_Minion_Murloc+=['BG22_202','BG22_202_G',]
	BG_PoolSet_Murloc[2].append('BG22_202')
	BG_Murloc_Gold['BG22_202']='BG22_202_G'
class BG22_202:# <12>[1453]
	""" Tad
	When you sell this,add another random Murloc to your hand. """
	events = Sell(CONTROLLER, SELF).on(Give(CONTROLLER, RandomBGMurloc(tech_level_less=TIER(CONTROLLER))))
	pass
class BG22_202_G:# <12>[1453]
	""" Tad
	When you sell this,add 2 other randomMurlocs to your hand. """
	events = Sell(CONTROLLER, SELF).on(Give(CONTROLLER, RandomMurloc())*2)
	pass


### Blazing Skyfin (2/1/3) ## new 25.2.2
if BG_Blazing_Sklyfin:
	BG_Minion_Murloc+=['BG25_040','BG25_040_G','BG25_040e','BG25_040_Ge']
	BG_PoolSet_Murloc[2].append('BG25_040')
	BG_Murloc_Gold['BG25_040']='BG25_040_G'
class BG25_040:
	""" Blazing Skyfin (2/1/3)
	After you play a [Battlecry] minion, gain +1/+1."""
	events = Play(CONTROLLER, FRIENDLY + BATTLECRY).after(Buff(SELF, 'BG25_040e'))
	pass
BG25_040e=buff(1,1)
class BG25_040_G:
	""" Blazing Skyfin (2/2/6)
	After you play a [Battlecry] minion, gain +2/+2."""
	events = Play(CONTROLLER, FRIENDLY + BATTLECRY).after(Buff(SELF, 'BG25_040_Ge'))
	pass
BG25_040_Ge=buff(2,2)

###### tavern tier 3

#Coldlight Seer (3)
if BG_Coldlight_Seer:
	BG_Minion_Murloc+=['BG_EX1_103','EX1_103e','TB_BaconUps_064','TB_BaconUps_064e',]
	BG_PoolSet_Murloc[3].append('BG_EX1_103')
	BG_Murloc_Gold['BG_EX1_103']='TB_BaconUps_064'
class BG_EX1_103:
	""" Coldlight Seer
	[Battlecry:] Give your other Murlocs +2 Health. """
	play = Buff(FRIENDLY_MINIONS + MURLOC - SELF, 'EX1_103e')
	pass
EX1_103e=buff(0,2)
class TB_BaconUps_064:# <12>[1453]
	""" Coldlight Seer
	[Battlecry:] Give your other Murlocs +4 Health. """
	play = Buff(FRIENDLY_MINIONS + MURLOC - SELF, 'TB_BaconUps_064e')
	pass
TB_BaconUps_064e=buff(0,4)



#Felfin Navigator (3) ### maybe ###
if BG_Felfin_Navigator:
	BG_Minion_Murloc+=['BG_BT_010','BT_010e','TB_BaconUps_124','TB_BaconUps_124e',]
	BG_PoolSet_Murloc[3].append('BG_BT_010')
	BG_Murloc_Gold['BG_BT_010']='TB_BaconUps_124'
class BG_BT_010:
	""" Felfin Navigator
	[Battlecry:] Give your other Murlocs +1/+1. """
	play =  Buff(FRIENDLY_MINIONS + MURLOC - SELF, 'BT_010e')
BT_010e=buff(1,1)
class TB_BaconUps_124:# <12>[1453]
	""" Felfin Navigator
	[Battlecry:] Give your other Murlocs +2/+2. """
	play =  Buff(FRIENDLY_MINIONS + MURLOC - SELF, 'TB_BaconUps_124e')
	pass
TB_BaconUps_124e=buff(2,2)



#Swolefin (3) ### need check ###
if BG_Swolefin:
	BG_Minion_Murloc+=['BG21_010','BG21_010e','BG21_010_G','BG21_010_Ge',]
	BG_PoolSet_Murloc[3].append('BG21_010')
	BG_Murloc_Gold['BG21_010']='BG21_010_G'
class BG21_010:# <12>[1453] ムキムキ
	""" Swolefin
	[Battlecry:] Gain +2/+1 for each other friendly Murloc. """
	play = Buff(SELF, 'BG21_010e') * Count(FRIENDLY_MINIONS + MURLOC - SELF)
	pass
BG21_010e=buff(2,1)# <12>[1453]
""" Swole
+2/+1. """
class BG21_010_G:# <12>[1453]
	""" Swolefin
	[Battlecry:] Gain +4/+2 foreach other friendly Murloc. """
	play = Buff(SELF, 'BG21_010_Ge') * Count(FRIENDLY_MINIONS + MURLOC - SELF)
	pass
BG21_010_Ge=buff(4,2)# <12>[1453]
""" Swoler
+4/+2. """



#Primalfin Lookout (4) ### maybe ###
if BG_Primalfin_Lookout:
	BG_Minion_Murloc+=['BGS_020','TB_BaconUps_089',]
	BG_PoolSet_Murloc[4].append('BGS_020')
	BG_Murloc_Gold['BGS_020']='TB_BaconUps_089'
class BGS_020_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		card.zone=Zone.HAND
		pass
class BGS_020_Action(GameAction):
	def do(self, source):
		controller=source.controller
		#cards=[card for card in controller.field if card!=source and card.type==CardType.MINION and card.race==Race.MURLOC]
		cards=[card for card in controller.field if card!=source and race_identity(card,Race.MURLOC)]
		if len(cards):
			BGS_020_Choice(controller, RandomBGMurloc(tech_level_less=TIER(CONTROLLER))*3).trigger(source)
class BGS_020:# <12>[1453] 見張り番
	""" Primalfin Lookout
	[Battlecry:] If you control another Murloc, [Discover] a_Murloc. """
	play = BGS_020_Action()
	pass
class BGS_020_Choice2(Choice):
	def choose(self, card):
		card.zone=Zone.HAND
		self.source.sidequest_counter+=1
		if self.source.sidequest_counter==1:
			self.next_choice=self
		else:
			self.next_choice=None
		super().choose(card)
		pass
class BGS_020_Action2(GameAction):
	def do(self, source):
		controller=source.controller
		#cards=[card for card in controller.field if card!=source and card.type==CardType.MINION and card.race==Race.MURLOC]
		cards=[card for card in controller.field if card!=source and race_identity(card,Race.MURLOC)]
		if len(cards):
			BGS_020_Choice2(controller, RandomBGMurloc(tech_level_less=TIER(CONTROLLER))*3).trigger(source)
class TB_BaconUps_089:# <12>[1453]
	""" Primalfin Lookout
	[Battlecry:] If you control another Murloc, [Discover] two_Murlocs. """
	play = BGS_020_Action2()
	pass


if BG_Toxfin: ##(4) new 24.2 -> (6) 25.0.4
	BG_Minion_Murloc+=['BG_DAL_077','TB_BaconUps_152']
	BG_PoolSet_Murloc[6].append('BG_DAL_077')
	BG_Murloc_Gold['BG_DAL_077']='TB_BaconUps_152'
class BG_DAL_077:
	""" Toxfin (4)-> (6) 25.0.4
	[Battlecry:] Give a friendly Murloc [Poisonous].""" 
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE:Race.MURLOC }	
	play = SetTag(TARGET, (GameTag.POISONOUS,))
class TB_BaconUps_152:
	""" Toxfin
	[Battlecry:] Give a friendly Murloc [Poisonous]."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE:Race.MURLOC }
	play = SetTag(TARGET, (GameTag.POISONOUS,))



#King Bagurgle (5) ### OK ###
if BG_King_Bagurgle:
	BG_Minion_Murloc+=['BGS_030','BGS_030e','TB_BaconUps_100','TB_BaconUps_100e',]
	BG_PoolSet_Murloc[5].append('BGS_030')
	BG_Murloc_Gold['BGS_030']='TB_BaconUps_100'
class BGS_030:# <12>[1453] バガァグル
	""" King Bagurgle
	[Battlecry and Deathrattle:] Give your other Murlocs +2/+2. """
	play = Buff(FRIENDLY_MINIONS + MURLOC, 'BGS_030e')
	deathrattle = Buff(FRIENDLY_MINIONS + MURLOC, 'BGS_030e')
	pass
BGS_030e=buff(2,2)
class TB_BaconUps_100:# <12>[1453]
	""" King Bagurgle
	[Battlecry and Deathrattle:] Give your other Murlocs +4/+4. """
	play = Buff(FRIENDLY_MINIONS + MURLOC, 'TB_BaconUps_100e')
	deathrattle = Buff(FRIENDLY_MINIONS + MURLOC, 'TB_BaconUps_100e')
	pass
TB_BaconUps_100e=buff(4,4)



#SI:Sefin (5)  ### maybe ### banned 24.2
if BG_SI_Sefin:
	BG_Minion_Murloc+=['BG21_009','BG21_009e','BG21_009_G',]
	BG_PoolSet_Murloc[5].append('BG21_009')
	BG_Murloc_Gold['BG21_009']='BG21_009_G'
class BG21_009:# <12>[1453] セブリ
	""" SI:Sefin
	[Avenge (3):] Give a friendly Murloc [Poisonous] permanently. """
	events = Death(FRIENDLY).on(Avenge(SELF, 3, [BuffPermanently(RANDOM(FRIENDLY_MINIONS + MURLOC), 'BG21_009e')])) #
	pass
BG21_009e=buff(poisonous=True)# <12>[1453]
""" SI:7 Training
[Poisonous] """
class BG21_009_G:# <12>[1453]
	""" SI:Sefin
	[Avenge (3):] Give 2 friendly Murlocs [Poisonous] permanently. """
	events = Death(FRIENDLY).on(Avenge(SELF, 3, [BuffPermanently(RANDOM(FRIENDLY_MINIONS + MURLOC), 'BG21_009e'), BuffPermanently(RANDOM(FRIENDLY_MINIONS + MURLOC - SELF), 'BG21_009e')])) #
	pass





##### tavern tier 6

## Young Murk-Eye (6) 
if BG_Young_Murk_Eye:
	BG_Minion_Murloc+=['BG22_403','BG22_403_G']
	BG_PoolSet_Murloc[6].append('BG22_403')
	BG_Murloc_Gold['BG22_403']='BG22_403_G'
class BG22_403:
	""" Young Murk-Eye (6) 
	At the end of your turn, the Murloc to the left of this triggers its [Battlecry]."""
	pass
class BG22_403_G:
	""" (6) 
	At the end of your turn, adjacent Murlocs trigger their [Battlecries]."""
	pass



