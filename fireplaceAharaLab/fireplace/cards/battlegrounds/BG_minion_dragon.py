
from ..utils import *

BG_Minion_Dragon =[
	'BG21_027','BG21_027e','BG21_027_G','BG21_027_Ge',#Evolving Chromawing(1) ###OK
	'BGS_019','TB_BaconUps_102',#Red Whelp(1)
	'BGS_045','BGS_045e','TB_BaconUps_115','TB_BaconUps_115e',#Glyph Guardian(2)
	'BGS_034','TB_BaconUps_149',#Bronze Warden(3)
	'BGS_067','BGS_067e','TB_BaconUps_117','TB_BaconUps_117e',#Drakonid Enforcer(3)
	'BGS_038','BGS_038e','TB_BaconUps_108','TB_BaconUps_108e',#Twilight Emissary(3)
	'ICC_029','ICC_029e','TB_BaconUps_120','TB_BaconUps_120e',#Cobalt Scalebane(4)
	'BG21_012','BG21_012_G',#Prestor's Pyrospawn(4)
	'BG21_014','BG21_014e','BG21_014_G',#Prized Promo-Drake(4)
	'BG21_015','BG21_015_G',#Tarecgosa(4)
	'BGS_043','TB_BaconUps_110',#Murozond(5)
	'BGS_036','BGS_036e','TB_BaconUps_106','TB_BaconUps_106e',#Razorgore, the Untamed (5)
	'BGS_041','BGS_041e','TB_BaconUps_109','TB_BaconUps_109e',#Kalecgos, Arcane Aspect (6)
	]

BG_PoolSet_Dragon=[
	['BG21_027','BGS_019',],
	['BGS_045',],
	['BGS_034','BGS_067','BGS_038',],
	['ICC_029','BG21_012','BG21_014','BG21_015',],
	['BGS_043','BGS_036',],
	['BGS_041',],
	]

BG_Dragon_Gold={
	'BG21_027':'BG21_027_G',#Evolving Chromawing(1)
	'BGS_019':'TB_BaconUps_102',#Red Whelp(1)
	'BGS_045':'TB_BaconUps_115',#Glyph Guardian(2)
	'BGS_034':'TB_BaconUps_149',#Bronze Warden(3)
	'BGS_067':'TB_BaconUps_117',#Drakonid Enforcer(3)
	'BGS_038':'TB_BaconUps_108',#Twilight Emissary(3)
	'ICC_029':'TB_BaconUps_120',#Cobalt Scalebane(4)
	'BG21_012':'BG21_012_G',#Prestor's Pyrospawn(4)
	'BG21_014':'BG21_014_G',#Prized Promo-Drake(4)
	'BG21_015':'BG21_015_G',#Tarecgosa(4)
	'BGS_043':'TB_BaconUps_110',#Murozond(5)
	'BGS_036':'TB_BaconUps_106',#Razorgore, the Untamed (5)
	'BGS_041':'TB_BaconUps_109',#Kalecgos, Arcane Aspect (6)
	}


#Evolving Chromawing(1)  ### OK ###
class BG21_027_Buff(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, buff, amount):
		Buff(target, buff).trigger(source)
		buff = target.buffs[-1]
		buff.tags[GameTag.ATK] = target.atk*amount
class BG21_027:# <12>[1453]
	""" Evolving Chromawing
	After you upgrade your Tavern Tier, double this minion's Attack. """
	events = UpgradeTier(CONTROLLER).after(BG21_027_Buff(SELF, 'BG21_027e',1 ))
	pass
class BG21_027e:
	pass
class BG21_027_G:# <12>[1453]
	""" Evolving Chromawing
	After you upgrade your Tavern Tier, triple this minion's Attack. """
	events = UpgradeTier(CONTROLLER).after(BG21_027_Buff(SELF, 'BG21_027_Ge', 2))
	pass
class BG21_027_Ge:
	pass



#Red Whelp(1) ### need check ###
class BGS_019:# <12>[1453]
	""" Red Whelp
	[Start of Combat:] Deal1 damage per friendly Dragon to one random enemy minion. """
	events = BeginBattle(CONTROLLER).on(Hit(RANDOM(ENEMY_MINIONS), Count(FRIENDLY_MINIONS + DRAGON)))
	pass
class TB_BaconUps_102:# <12>[1453]
	""" Red Whelp
	[Start of Combat:] Deal1 damage per friendlyDragon to one randomenemy minion twice. """
	events = BeginBattle(CONTROLLER).on(Hit(RANDOM(ENEMY_MINIONS), Count(FRIENDLY_MINIONS + DRAGON)),Hit(RANDOM(ENEMY_MINIONS), Count(FRIENDLY_MINIONS + DRAGON)))
	pass



#Glyph Guardian(2)   ### need check ###
class BGS_045_Buff(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, buff, amount):
		Buff(target, buff).trigger(source)
		buff = target.buffs[-1]
		atk_buff  = target.atk*amount
		buff.tags[GameTag.ATK] = atk_buff
class BGS_045:# <4>[1453]
	""" Glyph Guardian
	Whenever this attacks, double its Attack. """
	events = BG_Attack(SELF).on(BGS_045_Buff(SELF,'BGS_045e',1))
	pass
class BGS_045e:
	pass
class TB_BaconUps_115:# <4>[1453]
	""" Glyph Guardian
	Whenever this attacks, triple its Attack. """
	events = BG_Attack(SELF).on(BGS_045_Buff(SELF,'TB_BaconUps_115e',2))
	pass
class TB_BaconUps_115e:
	pass



#Bronze Warden(3)  ### OK ###
class BGS_034:# <12>[1453]
	""" Bronze Warden
	[Divine Shield][Reborn] """
	#<Tag enumID="194" name="DIVINE_SHIELD" type="Int" value="1"/>
	#<Tag enumID="1085" name="REBORN" type="Int" value="1"/>
	pass
class TB_BaconUps_149:# <12>[1453]
	""" Bronze Warden
	[Divine Shield][Reborn] """
	pass



#Drakonid Enforcer(3)  ### OK ##
class BGS_067:# <12>[1453]
	""" Drakonid Enforcer
	After a friendly minion loses [Divine Shield], gain_+2/+2. """
	events = LoseDivineShield(FRIENDLY_MINIONS).on(Buff(SELF,'BGS_067e'))
	pass
BGS_067e=buff(2,2)
class TB_BaconUps_117:# <12>[1453]
	""" Drakonid Enforcer
	After a friendly minion loses [Divine Shield], gain_+4/+4. """
	events = LoseDivineShield(FRIENDLY_MINIONS).on(Buff(SELF,'TB_BaconUps_117e'))
	pass
TB_BaconUps_117e=buff(4,4)




#Twilight Emissary(3)  ### OK ###
class BGS_038:# <12>[1453]
	""" Twilight Emissary
	[Taunt][Battlecry:] Give a friendly Dragon +2/+2. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE:Race.DRAGON }
	play = Buff(TARGET, 'BGS_038e')
	pass
BGS_038e=buff(2,2)
class TB_BaconUps_108:# <12>[1453]
	""" Twilight Emissary
	[Taunt][Battlecry:] Give a friendly Dragon +4/+4. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE:Race.DRAGON } 
	play = Buff(TARGET, 'TB_BaconUps_108e')
	pass
TB_BaconUps_108e=buff(4,4)



#Cobalt Scalebane(4)  ### OK ###
class ICC_029:
	""" Cobalt Scalebane
	At the end of your turn, give another random friendly minion +3 Attack. """
	events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_MINIONS), 'ICC_029e'))
ICC_029e=buff(3,0)
class TB_BaconUps_120:# <12>[1453]
	""" Cobalt Scalebane
	At the end of your turn, give another random friendly minion +6 Attack. """
	events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_MINIONS), 'TB_BaconUps_120e'))
TB_BaconUps_120e=buff(6,0)



#Prestor's Pyrospawn(4)  ### maybe ###
class BG21_012:# <12>[1453]
	""" Prestor's Pyrospawn
	Whenever another friendlyDragon attacks, deal 3 damage to its target. """
	events = BG_Attack(FRIENDLY + DRAGON - SELF).on(Hit(BG_Attack.OTHER, 3))
	pass
class BG21_012_G:# <12>[1453]
	""" Prestor's Pyrospawn
	Whenever another friendlyDragon attacks, deal 6 damage to its target. """
	events = BG_Attack(FRIENDLY + DRAGON - SELF).on(Hit(Attack.DEFENDER, 6))
	pass



#Prized Promo-Drake(4)   ### maybe ###
class BG21_014_Action(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, buff, amount):
		if not isinstance(target, list):
			target = [target]
		count=0
		for card in target.controller.field:
			if card.race==Race.DRAGON:
				count += amount
		for card in target:
			Buff(card, buff).trigger(target.controller)
			buff = card.buffs[-1]
			buff.tags[GameTag.ATK] = count
			buff.tags[GameTag.HEALTH] = count
class BG21_014:# <12>[1453]
	""" Prized Promo-Drake
	[Start of Combat:] Give adjacent minions +1/+1__for each friendly Dragon. """
	events = BeginBattle(CONTROLLER).on(BG21_014_Action(SELF_ADJACENT, 'BG21_014e', 1))
	pass
class BG21_014e:# <12>[1453]
	""" Promoted
	Increased stats from Promo-Drake """
	pass
class BG21_014_G:# <12>[1453]
	""" Prized Promo-Drake
	[Start of Combat:] Giveadjacent minions +2/+2__for each friendly Dragon. """
	events = BeginBattle(CONTROLLER).on(BG21_014_Action(SELF_ADJACENT, 'BG21_014e', 2))
	pass



#Tarecgosa(4)    ## OK ###
class BG21_015_Action0(TargetedAction):
	TARGET = ActionArg()# self
	def do(self, source, target):
		target.sidequest_list0 = [] 
class BG21_015_Action1(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	def do(self, source, target, buff):
		#target = target[0]
		if not isinstance(buff, list):
			buff = [buff]
		target.sidequest_list0 += buff
class BG21_015_Action2(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		#target = target[0]
		for buff in target.sidequest_list0:
			buff.apply(target.deepcopy_original)
class BG21_015_Action3(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		#target = target[0]
		for buff in target.sidequest_list0:
			buff.apply(target.deepcopy_original)
			buff.apply(target.deepcopy_original)
class BG21_015:# <12>[1453]
	""" Tarecgosa
	This permanently keeps enchantments from combat. """
	events = [
		BeginBattle(CONTROLLER).on(BG21_015_Action0(SELF)),
		Buff(SELF).on(BG21_015_Action1(SELF, Buff.BUFF)),
		EndBattle(CONTROLLER).on(BG21_015_Action2(SELF))
	]
	pass
class BG21_015_G:# <12>[1453]
	""" Tarecgosa
	This permanently doubles and keeps enchantments from combat. """
	events = [
		BeginBattle(CONTROLLER).on(BG21_015_Action0(SELF)),
		Buff(SELF).on(BG21_015_Action1(SELF, Buff.BUFF)),
		EndBattle(CONTROLLER).on(BG21_015_Action3(SELF))
	]
	pass



#Murozond(5)   ### OK ####
class BGS_043:# <12>[1453]
	""" Murozond
	[Battlecry:] Add a minion from your last opponent's warband to your hand. """
	def play(self):
		controller = self.controller
		gamemaster = controller.game.parent
		last_warband = gamemaster.last_warband(controller)
		if len(last_warband)>0:
			new_card = random.choice(last_warband)
			Give(controller, new_card).trigger(self)
	pass
class TB_BaconUps_110:# <12>[1453]
	""" Murozond
	[Battlecry:] Add a minion from your last opponent's warband to your hand.Make it Golden! """
	def play(self):
		controller = self.controller
		gamemaster = controller.game.parent
		last_warband = gamemaster.last_warband(controller)
		if len(last_warband)>0:
			new_card = random.choice(last_warband)
			gold_id = gamemaster.BG_Gold[new_card]
			Give(controller, gold_id).trigger(self)## I want to check whether no error before excuting
	pass



#Razorgore, the Untamed (5)  ### need check (alternative) ###
class BGS_036_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		controller = target.controller
		count = 0
		for card in controller.field:
			if card.race == Race.DRAGON:
				count += amount
		Buff(target, 'BGS_036e').trigger(controller)
		buff = target.buffs[-1]
		buff.tags[GameTag.ATK] = count
		buff.tags[GameTag.HEALTH] = count
class BGS_036:# <12>[1453]
	""" Razorgore, the Untamed
	At the end of your turn, gain +1/+1 for each Dragon you have. """
	events = OWN_TURN_END.on(BGS_036_Action(SELF, 1))
	#events = OWN_TURN_END.on(Buff(SELF, 'BGS_036e') * Count(FRIENDLY_MINIONS + DRAGON))
	pass
BGS_036e=buff(1,1)
class TB_BaconUps_106:# <12>[1453]
	""" Razorgore, the Untamed
	At the end of your turn, gain +2/+2 for each Dragon you have. """
	events = OWN_TURN_END.on(BGS_036_Action(SELF, 2))
	#events = OWN_TURN_END.on(Buff(SELF, 'TB_BaconUps_106e') * Count(FRIENDLY_MINIONS + DRAGON))
	pass
TB_BaconUps_106e=buff(2,2)



#Kalecgos, Arcane Aspect (6)  ### maybe ###
class BGS_041:# <12>[1453]
	""" Kalecgos, Arcane Aspect
	After you play a minion with [Battlecry], give your Dragons +1/+1. """
	events = BG_Play(CONTROLLER, FRIENDLY + BATTLECRY).on(Buff(FRIENDLY_MINIONS + DRAGON, 'BGS_041e'))
	pass
BGS_041e=buff(1,1)
class TB_BaconUps_109:# <12>[1453]
	""" Kalecgos, Arcane Aspect
	After you play a minion with [Battlecry], give your Dragons +2/+2. """
	events = BG_Play(CONTROLLER, FRIENDLY + BATTLECRY).on(Buff(FRIENDLY_MINIONS + DRAGON, 'TB_BaconUps_109e'))
	pass
TB_BaconUps_109e=buff(2,2)





