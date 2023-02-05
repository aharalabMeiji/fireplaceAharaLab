from ast import If
from ..utils import *
from fireplace.battlegrounds.BG_battle import BG_Battle


Omega_Buster=True#Omega Buster(6)



BG_Micro_Mummy=True#(1) <-> undead/mecha
BG_Pupbot=True#(1)
BG_Harvest_Golem=True#(2)
BG_Kaboom_Bot=True#(2)
BG_Metaltooth_Leaper=True#(2)
BG_Deflect_o_Bot=True#(3)
BG_Replicating_Menace=True#(3)
BG_Screwjank_Clunker=False#(3)banned
BG_Iron_Sensei=True#(3)
BG_Annoy_o_Module=True#(4)
BG_Mechano_Eg_g=True#(4) banned  -> renew 25.0.4
BG_Mechano_Tank=False#(4) -> banned 25.0.4
BG_Wargear=True#(4) # after 23.6
BG_Holy_Mecherel=True#(5)
BG_Foe_Reaper_4000=True#(6)
BG_Omega_Buster=True#(6)
BG_Grease_Bot=True#(4->6) 23.6, 24.0.3
	
BG_Minion_Mecha =[]
BG_PoolSet_Mecha=[[],[],[],[],[],[],[]]
BG_Mecha_Gold={}

#25.2.2 -
#Micro Mummy 1/1/2/Mech, Undead	Reborn
#Micro Mummy(1) ### OK ###
if BG_Micro_Mummy:
	BG_Minion_Mecha+=['BG_ULD_217', 'ULD_217e','TB_BaconUps_250','TB_BaconUps_250e',]
	BG_PoolSet_Mecha[1].append('BG_ULD_217')
	BG_Mecha_Gold['BG_ULD_217']='TB_BaconUps_250'
class BG_ULD_217:
	"""
	[Reborn]At the end of your turn, giveanother random friendlyminion +1 Attack."""
	##<Tag enumID="2534" name="1" type="Int" value="1"/>(undead)
	events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_MINIONS - SELF), 'ULD_217e'))
	pass
ULD_217e=buff(1,0)
class TB_BaconUps_250:# <5>[1453]
	""" Micro Mummy
	[Reborn]At the end of your turn, giveanother random friendly minion +2 Attack. """
	events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_MINIONS - SELF), 'TB_BaconUps_250e'))
	pass
TB_BaconUps_250e=buff(2,0)

#Pupbot(1) ### OK ###
if BG_Pupbot:
	BG_Minion_Mecha+=['BG21_022','BG21_022_G',]
	BG_PoolSet_Mecha[1].append('BG21_022')
	BG_Mecha_Gold['BG21_022']='BG21_022_G'
class BG21_022:# <12>[1453]
	""" Pupbot
	[Divine Shield] """
	#<Tag enumID="194" name="DIVINE_SHIELD" type="Int" value="1"/>
	pass
class BG21_022_G:# <12>[1453]
	""" Pupbot
	[Divine Shield] """
	pass

#Harvest Golem(2) ### OK ###
if BG_Harvest_Golem:
	BG_Minion_Mecha+=['BG_EX1_556', 'BG_EX1_556t','TB_BaconUps_006','TB_BaconUps_006t',]
	BG_PoolSet_Mecha[2].append('BG_EX1_556')
	BG_Mecha_Gold['BG_EX1_556']='TB_BaconUps_006'
class BG_EX1_556:
	"""
	[Deathrattle:] Summon a 2/1 Damaged Golem."""
	deathrattle = Summon(CONTROLLER, "BG_EX1_556t")
	pass
class BG_EX1_556t:
	"""
	"""
class TB_BaconUps_006:# <12>[1453]
	""" Harvest Golem
	[Deathrattle:] Summon a 4/2 Damaged Golem. """
	deathrattle = Summon(CONTROLLER, "TB_BaconUps_006t")
	pass
class TB_BaconUps_006t:# <12>[1453]
	""" Damaged Golem
	 """
	#
	pass

#Kaboom Bot(2)  ### OK ###
if BG_Kaboom_Bot:
	BG_Minion_Mecha+=['BG_BOT_606', 'TB_BaconUps_028',]
	BG_PoolSet_Mecha[2].append('BG_BOT_606')
	BG_Mecha_Gold['BG_BOT_606']='TB_BaconUps_028'
class BG_BOT_606:
	"""
	[Deathrattle:] Deal 4_damage to a random enemy minion. """
	deathrattle = Hit(RANDOM(ENEMY_MINIONS), 4)
	pass
class TB_BaconUps_028:# <12>[1453]
	""" Kaboom Bot
	[Deathrattle:] Deal 4_damage to a random enemy minion twice. """
	deathrattle = Hit(RANDOM(ENEMY_MINIONS), 4) * 2
	pass


#Metaltooth Leaper(2) ### OK ###
if BG_Metaltooth_Leaper:
	BG_Minion_Mecha+=['BG_GVG_048','GVG_048e','TB_BaconUps_066','TB_BaconUps_066e',]
	BG_PoolSet_Mecha[2].append('BG_GVG_048')
	BG_Mecha_Gold['BG_GVG_048']='TB_BaconUps_066'
class BG_GVG_048:
	"""
	[Battlecry:] Give your other Mechs +2 Attack."""
	play = Buff(FRIENDLY_MINIONS + MECH - SELF,'GVG_048e')
GVG_048e=buff(2,0)
class TB_BaconUps_066:# <3>[1453]
	""" Metaltooth Leaper
	[Battlecry:] Give your other Mechs +4 Attack. """
	play = Buff(FRIENDLY_MINIONS + MECH - SELF, 'TB_BaconUps_066e')
	pass
TB_BaconUps_066e=buff(4,0)


#Deflect-o-Bot(3) ### OK ###
if BG_Deflect_o_Bot:
	BG_Minion_Mecha+=['BGS_071', 'BGS_071e', 'TB_BaconUps_123', 'TB_BaconUps_123e',]
	BG_PoolSet_Mecha[3].append('BGS_071')
	BG_Mecha_Gold['BGS_071']='TB_BaconUps_123'
class BGS_071_Action(TargetedAction):
	TARGET = ActionArg()#SELF
	BUFF = ActionArg()
	def do(self, source, target, buff):
		if isinstance(target.game, BG_Battle):##during combat
			Buff(target, buff).trigger(target.controller)
			SetDivineShield(target).trigger(target.controller)
class BGS_071:# <12>[1453]
	""" Deflect-o-Bot
	[Divine Shield]Whenever you summon a Mech during combat, gain +2 Attackand [Divine Shield]. """
	tags = {GameTag.DIVINE_SHIELD:True, }
	events = Summon(CONTROLLER, MECH).on(BGS_071_Action(SELF, 'BGS_071e'))
	pass
BGS_071e=buff(2,0)
class TB_BaconUps_123:# <12>[1453]
	""" Deflect-o-Bot
	[Divine Shield]Whenever you summon a Mechduring combat, gain +4 Attackand [Divine Shield]. """
	events = Summon(CONTROLLER, MECH).on(BGS_071_Action(SELF, 'TB_BaconUps_123e'))
	pass
TB_BaconUps_123e=buff(4,0)



#Replicating Menace(3)  ### OK ###
if BG_Replicating_Menace:
	BG_Minion_Mecha+=['BG_BOT_312', 'BG_BOT_312e','BG_BOT_312t','TB_BaconUps_032','TB_BaconUps_032e','TB_BaconUps_032t',]
	BG_PoolSet_Mecha[3].append('BG_BOT_312')
	BG_Mecha_Gold['BG_BOT_312']='TB_BaconUps_032'
class BG_BOT_312:
	"""Replicating Menace
	[Magnetic][Deathrattle:] Summon three 1/1 Microbots."""
	play = Magnetic(SELF, ['BG_BOT_312e'])
	deathrattle = Summon(CONTROLLER, 'BG_BOT_312t' ) * 3
class BG_BOT_312e:
	"""Replicating Menace
	"""
	tags = {GameTag.DEATHRATTLE:True, 
		GameTag.ATK:3,
		GameTag.HEALTH:1}
	deathrattle = Summon(CONTROLLER, 'BG_BOT_312t' ) * 3
	pass
class BG_BOT_312t:
	""" Microbot
	"""
	pass
class TB_BaconUps_032:# <12>[1453]
	""" Replicating Menace
	[Magnetic][Deathrattle:] Summon three 2/2 Microbots. """
	play = Magnetic(SELF, ['TB_BaconUps_032e'])
	deathrattle = Summon(CONTROLLER, 'TB_BaconUps_032t' ) * 3
	pass
class TB_BaconUps_032e:
	tags = {GameTag.DEATHRATTLE:True, 
		GameTag.ATK:6,
		GameTag.HEALTH:2}
	deathrattle = Summon(CONTROLLER, 'TB_BaconUps_032t' ) * 3
	pass
class TB_BaconUps_032t:# <12>[1453]
	""" Microbot
	 """
	pass



#Screwjank Clunker(3) ### OK ###
if BG_Screwjank_Clunker:
	BG_Minion_Mecha+=['GVG_055', 'GVG_055e', 'TB_BaconUps_069','TB_BaconUps_069e',]
	BG_PoolSet_Mecha[3].append('GVG_055')
	BG_Mecha_Gold['GVG_055']='TB_BaconUps_069'
class GVG_055:
	""" Screwjank Clunker
	[Battlecry:] Give a friendly Mech +2/+2 """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.MECHANICAL} 
	play = Buff(TARGET, 'GVG_055e')
	pass
GVG_055e=buff(2,2)
class TB_BaconUps_069:# <10>[1453]
	""" Screwjank Clunker
	[Battlecry:] Give a friendly Mech +4/+4. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.MECHANICAL} 
	play = Buff(TARGET, 'TB_BaconUps_069e')
	pass
TB_BaconUps_069e=buff(4,4)




if BG_Iron_Sensei:
	BG_Minion_Mecha+=['BG_GVG_027', 'GVG_027e', 'TB_BaconUps_044','TB_BaconUps_044e',]
	BG_PoolSet_Mecha[3].append('BG_GVG_027')
	BG_Mecha_Gold['BG_GVG_027']='TB_BaconUps_044'
class BG_GVG_027:
	"""Iron Sensei"""
	events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_MINIONS + MECH - SELF), "GVG_027e"))
GVG_027e = buff(+2, +2)
class TB_BaconUps_044:
	""" Iron Sensei
	At the end of your turn, give another friendly Mech +4/+4."""
	events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_MINIONS + MECH - SELF), "TB_BaconUps_044e"))
TB_BaconUps_044e = buff(4,4)

#Annoy-o-Module(4) ### OK ###
if BG_Annoy_o_Module:
	BG_Minion_Mecha+=['BG_BOT_911', 'BG_BOT_911e', 'TB_BaconUps_099','TB_BaconUps_099e',]
	BG_PoolSet_Mecha[4].append('BG_BOT_911')
	BG_Mecha_Gold['BG_BOT_911']='TB_BaconUps_099'
class BG_BOT_911:
	"""
	[Magnetic][Divine Shield][Taunt]"""
	## divine shield is a consumable buff. taunt is not
	play = Magnetic(SELF, ['BOT_911e'])
	pass
class BG_BOT_911e:
	def apply(self,target):
		target.divine_shield=True
		target.taunt=True
		self.tags[GameTag.ATK] = 2
		self.tags[GameTag.HEALTH] = 4
	pass
class TB_BaconUps_099:# <5>[1453]
	""" Annoy-o-Module
	[Magnetic][Divine Shield][Taunt] """
	play = Magnetic(SELF, ['TB_BaconUps_099e'])
	pass
class TB_BaconUps_099e:
	def apply(self,target):
		target.divine_shield=True
		target.taunt=True
		self.tags[GameTag.ATK] = 4
		self.tags[GameTag.HEALTH] = 8
	pass





#Mechano-Egg(4) ### OK ### -> renew 25.0.4
if BG_Mechano_Eg_g:
	BG_Minion_Mecha+=['BOT_537', 'BOT_537t','TB_BaconUps_039', 'TB_BaconUps_039t',]
	BG_PoolSet_Mecha[4].append('BOT_537')
	BG_Mecha_Gold['BOT_537']='TB_BaconUps_039'
class BOT_537:
	"""
	[Deathrattle:] Summon an 8/8 Robosaur."""
	deathrattle = Summon(CONTROLLER, 'BOT_537t')
class BOT_537t:
	""" Robosaur """
	pass
class TB_BaconUps_039:# <5>[1453]
	""" Mechano-Egg
	[Deathrattle:] Summon a 16/16 Robosaur. """
	deathrattle = Summon(CONTROLLER, 'TB_BaconUps_039t')
	pass
class TB_BaconUps_039t:
	""" Robosaur 	"""



#Mechano-Tank(4)-> banned 25.0.4
if BG_Mechano_Tank:
	BG_Minion_Mecha+=['BG21_023', 'BG21_023_G',]
	BG_PoolSet_Mecha[4].append('BG21_023')
	BG_Mecha_Gold['BG21_023']='BG21_023_G'
class BG21_023:# <12>[1453]
	""" Mechano-Tank
	[Avenge (2):] Deal 5 damage to the highest Health enemy minion. """
	events = Death(FRIENDLY_MINIONS).on(Avenge(SELF, 2, [Hit(HIGHEST_HEALTH(ENEMY_MINIONS), 5)]))
	pass
class BG21_023_G:# <12>[1453]
	""" Mechano-Tank
	[Avenge (2):] Deal 5 damage to the highest Health enemy minion twice. """
	events = Death(FRIENDLY_MINIONS).on(Avenge(SELF, 2, [Hit(HIGHEST_HEALTH(ENEMY_MINIONS), 5), Hit(HIGHEST_HEALTH(ENEMY_MINIONS), 5)]))
	pass

##  Wargear (4) 23.6  ### OK ###
if BG_Wargear:
	BG_Minion_Mecha+=['BG_BOT_563','BG_BOT_563e','BG_BOT_563_G','BG_BOT_563_Ge',]
	BG_PoolSet_Mecha[4].append('BG_BOT_563')
	BG_Mecha_Gold['BG_BOT_563']='BG_BOT_563_G'
class BG_BOT_563:
	""" Wargear
	[Magnetic]"""
	play = Magnetic(SELF, ['BG_BOT_563e'])
	pass
BG_BOT_563e=buff(5,5)
class BG_BOT_563_G:
	play = Magnetic(SELF, ['BG_BOT_563_Ge'])
	pass
BG_BOT_563_Ge=buff(10,10)


#Holy Mecherel(5)
if BG_Holy_Mecherel:
	BG_Minion_Mecha+=['BG20_401', 'BG20_401_G',]
	BG_PoolSet_Mecha[5].append('BG20_401')
	BG_Mecha_Gold['BG20_401']='BG20_401_G'
class BG20_401:# <12>[1453]
	""" Holy Mecherel  さば
	After another friendly minion loses [Divine Shield], gain [Divine Shield]. """
	events = LoseDivineShield(FRIENDLY_MINIONS - SELF).after(SetDivineShield(SELF))
	pass
class BG20_401_G:# <12>[1453]
	""" Holy Mecherel
	After another friendly minion loses [Divine Shield], gain [Divine Shield]. """
	events = LoseDivineShield(FRIENDLY_MINIONS - SELF).after(SetDivineShield(SELF))
	pass



#Foe Reaper 4000(6)
if BG_Foe_Reaper_4000:
	BG_Minion_Mecha+=['BG_GVG_113', 'TB_BaconUps_153',]
	BG_PoolSet_Mecha[6].append('BG_GVG_113')
	BG_Mecha_Gold['BG_GVG_113']='TB_BaconUps_153'
class BG_GVG_113:## エネリ
	""" Foe Reaper 4000
	Also damages the minions next to whomever it attacks. """
	events = BG_Attack(SELF, ENEMY_MINIONS).on(HitAdjacentMinions(BG_Attack.OTHER, ATK(SELF)))
	pass
class TB_BaconUps_153:# <12>[1453]
	""" Foe Reaper 4000
	Also damages the minions next to whomever it attacks. """
	events = BG_Attack(SELF, ENEMY_MINIONS).on(HitAdjacentMinions(BG_Attack.OTHER, ATK(SELF)))
	pass



#Omega Buster(6)
if BG_Omega_Buster:
	BG_Minion_Mecha+=['BG21_025','BG21_025e','BG21_025_G',]
	BG_PoolSet_Mecha[6].append('BG21_025')
	BG_Mecha_Gold['BG21_025']='BG21_025_G'
if Omega_Buster: #
	pass
class BG21_025_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source,target):
		controller = target
		summonnumber = 8-len(controller.field)# or 7-len(***) ?
		for repeat in range(summonnumber):
			yield Summon(CONTROLLER, 'BG_BOT_312t')
		if summonnumber<5:
			for repeat in range(5-summonnumber):
				yield Buff(FRIENDLY + MECH, 'BG21_025e')
class BG21_025:# <12>[1453] オメバス
	""" Omega Buster
	[Deathrattle:] Summon five 1/1 Microbots. For each that doesn't fit, give your Mechs +1/+1. """
	deathrattle = BG21_025_Action(CONTROLLER)
	pass
BG21_025e=buff(1,1)
class BG21_025_G:# <12>[1453]
	""" Omega Buster
	[Deathrattle:] Summon five 2/2 Microbots. For each that doesn't fit, give your Mechs +2/+2. """
	def do(self, source,target):
		controller = target
		summonnumber = 8-len(controller.field)# or 7-len(***) ?
		for repeat in range(summonnumber):
			yield Summon(CONTROLLER, 'TB_BaconUps_032t')
		if summonnumber<5:
			for repeat in range(5-summonnumber):
				yield Buff(FRIENDLY + MECH, 'BG21_025e2')
	pass
BG21_025e2=buff(2,2)
class TB_BaconUps_032t:
	""" Microbot (2/2)
	"""
	pass

#Grease Bot(4->6) 23.6
if BG_Grease_Bot:
	BG_Minion_Mecha+=['BG21_024', 'BG21_024e','BG21_024_G','BG21_024_Ge',]
	BG_PoolSet_Mecha[6].append('BG21_024')
	BG_Mecha_Gold['BG21_024']='BG21_024_G'
class BG21_024:# <12>[1453]
	""" Grease Bot
	After a friendly minion loses [Divine Shield], give it +2/+2_permanently. """
	events = LoseDivineShield(FRIENDLY_MINIONS).on(BuffPermanently(LoseDivineShield.TARGET, 'BG21_024e'))
	pass
BG21_024e=buff(2,2)#24.0.3
#BG21_024e=buff(3,2)# until 23.6
class BG21_024_G:# <12>[1453]
	""" Grease Bot
	After a friendly minion loses [Divine Shield], give it +4/+4_permanently. """
	events = LoseDivineShield(FRIENDLY_MINIONS).on(BuffPermanently(LoseDivineShield.TARGET, 'BG21_024_Ge'))
	pass
BG21_024_Ge=buff(4,4)# 24.0.3
#BG21_024_Ge=buff(6,4)# until 23.6

from .BG_minion_demon import BG25__Mecha_Jaraxxus
if BG25__Mecha_Jaraxxus:# 6/3/15 MECH/DEMON ## new 25.2.2 ##
	##BG_Minion_Mecha+=['BG25_807','BG25_807_G','BG25_807e','BG25_807e2','BG25_807e3']
	##BG_Minion_Mecha+=['BG25_807t','BG25_807t_G','BG25_807t2','BG25_807t2_G','BG25_807t3','BG25_807t3_G']
	BG_PoolSet_Mecha[6].append('BG25_807')
	BG_Mecha_Gold['BG25_807']='BG25_807_G'
	BG_Mecha_Gold['BG25_807t']='BG25_807t_G'
	BG_Mecha_Gold['BG25_807t2']='BG25_807t2_G'
	BG_Mecha_Gold['BG25_807t3']='BG25_807t3_G'
