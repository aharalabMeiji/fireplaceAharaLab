from ..utils import *

############# L - Q

BG_Hero3=[]

BG_PoolSet_Hero3=[]
#'BG20_HERO_202',#38#38 X
#40 mech ban
#'TB_BaconShop_HERO_70',#41 XX
#47  pirate ban
BG_Hero3_Buddy={}
BG_Hero3_Buddy_Gold={}

#### source ####################################################


####Lady Vashj ### HP OK ##
BG_Hero3+=['BG23_HERO_304','BG23_HERO_304p', ]#
BG_PoolSet_Hero3.append('BG23_HERO_304')
class BG23_HERO_304:
	""" Lady Vashj """
class BG23_HERO_304p_Action(TargetedAction):
	BUFF=ActionArg()
	def do(self, source, buff):
		if hasattr(buff.source,'spellcraft_spellcard'):
			if source.script_data_num_1<1:
				buff.permanent_buff = True
				source.script_data_num_1+=1
class BG23_HERO_304p_Action2(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		source.script_data_num_1=0
class BG23_HERO_304p:
	""" Relics of the Deep
	[Discover] a [Spellcraft] spell of your Tier or lower. [Passive:] Your first one __each turn is permanent."""
	events = [
		Buff(FRIENDLY).on(BG23_HERO_304p_Action(Buff.BUFF)),
		BeginBar(CONTROLLER).on(BG23_HERO_304p_Action2(SELF))
	]
	activate = Discover(CONTROLLER, RandomBGSpellcraftSpellcard(tech_level_less=TIER(CONTROLLER)))
	pass




#33#Lich Baz'hial ### HP OK ###
BG_Hero3+=['TB_BaconShop_HERO_25','TB_BaconShop_HP_049','TB_BaconShop_HERO_25_Buddy','TB_BaconShop_HERO_25_Buddy_e','TB_BaconShop_HERO_25_Buddy_G','TB_BaconShop_HERO_25_Buddy_Ge',]
BG_PoolSet_Hero3+=['TB_BaconShop_HERO_25']
BG_Hero3_Buddy['TB_BaconShop_HERO_25']='TB_BaconShop_HERO_25_Buddy'
BG_Hero3_Buddy_Gold['TB_BaconShop_HERO_25_Buddy']='TB_BaconShop_HERO_25_Buddy_G'
class TB_BaconShop_HERO_25:# <12>[1453]
	""" Lich Baz'hial	 """
class TB_BaconShop_HP_049:
	""" Graveyard Shift
	Take $4 damage. Gain 2 Gold this turn only.""" # 24.0.3
	## Take $2_damage and add a Gold Coin to your hand. 24.0
	activate = Hit(FRIENDLY_HERO, 4), Give(CONTROLLER, 'GAME_005')*2
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
##BG_Hero3+=['TB_BaconShop_HERO_72','TB_BaconShop_HP_081','TB_BaconShop_HERO_72_Buddy','TB_BaconShop_HERO_72_Buddy_G',]
##BG_PoolSet_Hero3+=['TB_BaconShop_HERO_72']
##BG_Hero3_Buddy['TB_BaconShop_HERO_72']='TB_BaconShop_HERO_72_Buddy'
##BG_Hero3_Buddy_Gold['TB_BaconShop_HERO_72_Buddy']='TB_BaconShop_HERO_72_Buddy_G'
class TB_BaconShop_HERO_72:# <12>[1453]
	""" Lord Barov	 """
class TB_BaconShop_HP_081: ############# impossible
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



#Lord Jaraxxus ### HP OK ###
BG_Hero3 += ['TB_BaconShop_HERO_37','TB_BaconShop_HP_036','TB_BaconShop_HERO_37_Buddy','TB_BaconShop_HERO_37_Buddy_G',	]# 
BG_PoolSet_Hero3 +=['TB_BaconShop_HERO_37',]#
BG_Hero3_Buddy['TB_BaconShop_HERO_37']='TB_BaconShop_HERO_37_Buddy'#
BG_Hero3_Buddy_Gold['TB_BaconShop_HERO_37_Buddy']='TB_BaconShop_HERO_37_Buddy_G'#
class TB_BaconShop_HERO_37:# <12>[1453]
	""" Lord Jaraxxus """
class TB_BaconShop_HP_036:
	""" Bloodfury
	Give your Demons +1/+1."""
	activate = Buff(FRIENDLY_MINIONS + DEMON, 'TB_Bacon_Secrets_08e')
@custom_card
class TB_Bacon_Secrets_08e:
	tags = {
		GameTag.CARDNAME: "Bloodfury buff",
		GameTag.CARDTEXT: "",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.ATK: 1,
		GameTag.HEALTH: 1,
	}
######## BUDDY
class TB_BaconShop_HERO_37_Buddy:
	"""Kil'rek
	[Taunt] [Deathrattle:] Add a random Demon to your hand."""
class TB_BaconShop_HERO_37_Buddy_G:
	""" Kil'rek
	[Taunt] [Deathrattle:] Add 2 random Demons to your hand."""
	pass




#36#Maiev Shadowsong  ### HP OK ###
BG_Hero3 += ['TB_BaconShop_HERO_62','TB_BaconShop_HP_068','TB_BaconShop_HP_068pe','TB_BaconShop_HP_068e','TB_BaconShop_HP_068e2','TB_BaconShop_HERO_62_Buddy','TB_BaconShop_HERO_62_Buddy_e','TB_BaconShop_HERO_62_Buddy_G',]# 
BG_PoolSet_Hero3 +=['TB_BaconShop_HERO_62',]#
BG_Hero3_Buddy['TB_BaconShop_HERO_62']='TB_BaconShop_HERO_62_Buddy'#
BG_Hero3_Buddy_Gold['TB_BaconShop_HERO_62_Buddy']='TB_BaconShop_HERO_62_Buddy_G'#
class TB_BaconShop_HERO_62:# <12>[1453]
	""" Maiev Shadowsong """
class TB_BaconShop_HP_068:
	""" Imprison
	Make a minion in Bob's Tavern [Dormant]. After 3 __turns, get it with +2/+2 """
	requirements = {
		PlayReq.REQ_TARGET_TO_PLAY:0,
		PlayReq.REQ_ENEMY_TARGET:0,
		PlayReq.REQ_MINION_TARGET:0,
		}
	activate = Buff(TARGET,'TB_BaconShop_HP_068pe')
class TB_BaconShop_HP_068pe_Action(TargetedAction):
	CONTROLLER=ActionArg()
	TARGET=ActionArg()
	def do(self, source, controller, target):
		bartender = target.controller
		target.zone=Zone.GRAVEYARD
		target.controller = controller
		target.zone = Zone.HAND
		if target in bartender.field:
			bartender.field.remove(target)
		Buff(target, 'TB_BaconShop_HP_068e').trigger(source.owner)
		pass
class TB_BaconShop_HP_068pe:
	"""ImprisonedWatcher	"""
	def apply(self, target):
		target.dormant=3
	events = Awaken().on(TB_BaconShop_HP_068pe_Action(CONTROLLER, Awaken.TARGET),Destroy(SELF))
	pass
TB_BaconShop_HP_068e=buff(2,2)
class TB_BaconShop_HP_068e2:
	pass
######## BUDDY
class TB_BaconShop_HERO_62_Buddy:# <12>[1453]
	""" Shadow Warden
	[Battlecry:] Your next Hero Power makes the target Golden and awaken 1 turn faster. """
	#
	pass
class TB_BaconShop_HERO_62_Buddy_e:# <12>[1453]
	""" Next Hero Power Goldens
	Your next Hero Power makes the target Golden. """
	#
	pass
class TB_BaconShop_HERO_62_Buddy_G:# <12>[1453]
	""" Shadow Warden
	[Battlecry:] Your next 2 Hero Powers make the target Golden and awaken 1 turn faster. """
	#
	pass



#37#Malygos ###  HP OK ###
BG_Hero3 += ['TB_BaconShop_HERO_58','TB_BaconShop_HP_052','TB_BaconShop_HERO_58_Buddy','TB_BaconShop_HERO_58_Buddy_G',]# 
BG_PoolSet_Hero3 +=['TB_BaconShop_HERO_58',]#
BG_Hero3_Buddy['TB_BaconShop_HERO_58']='TB_BaconShop_HERO_58_Buddy'#
BG_Hero3_Buddy_Gold['TB_BaconShop_HERO_58_Buddy']='TB_BaconShop_HERO_58_Buddy_G'#
class TB_BaconShop_HERO_58:# <12>[1453]
	""" Malygos """
class TB_BaconShop_HP_052_Action(TargetedAction):
	CONTROLLER=ActionArg()
	TARGET=ActionArg()
	def do(self, source, controller, target):
		if hasattr(target,'__iter__'):
			target = target[0]
		target.zone=Zone.GRAVEYARD
		bartender = controller.opponent
		tier=target.tech_level
		newcard = RandomBGMinion(tech_level=tier).evaluate(bartender)
		Summon(CONTROLLER, newcard).trigger(bartender)
		pass
class TB_BaconShop_HP_052:
	""" Arcane Alteration
	Replace a minion with a random one of the same Tavern Tier. <i>(Twice per turn.)</i>"""
	tags={GameTag.HEROPOWER_ADDITIONAL_ACTIVATIONS:1}
	requirements = {
		PlayReq.REQ_TARGET_TO_PLAY:0,
		PlayReq.REQ_MINION_TARGET:0,
		PlayReq.REQ_ENEMY_TARGET:0,
		}
	activate = TB_BaconShop_HP_052_Action(CONTROLLER, TARGET)
######## BUDDY
class TB_BaconShop_HERO_58_Buddy:# <12>[1453]
	""" Nexus Lord
	'Arcane Alteration'replaces with a minionone Tavern Tier higher. """
	#
	pass
class TB_BaconShop_HERO_58_Buddy_G:# <12>[1453]
	""" Nexus Lord
	'Arcane Alteration'replaces with a minion_two Tavern Tiers higher. """
	#
	pass



#38#Master Nguyen ##########????????????####
BG_Hero3 += ['BG20_HERO_202','BG20_HERO_202p','BG20_HERO_202pe','BG20_HERO_202pt','BG20_HERO_202_Buddy','BG20_HERO_202_Buddy_G',]# 
BG_PoolSet_Hero3 +=['BG20_HERO_202',]#
BG_Hero3_Buddy['BG20_HERO_202']='BG20_HERO_202_Buddy'#
BG_Hero3_Buddy_Gold['BG20_HERO_202_Buddy']='BG20_HERO_202_Buddy_G'#
class BG20_HERO_202:# <12>[1453]
	""" Master Nguyen """
	entourage=['TB_BaconShop_HP_036','TB_BaconShop_HP_052']
	events = BeginBar(CONTROLLER).on(GenericChoiceChangeHeropower(CONTROLLER, RandomEntourage()*2))
class BG20_HERO_202p:# <12>[1453]
	""" Power of the Storm
	[Passive]At the start of every turn, choose from 2 new Hero Powers. """
	#
	pass
class BG20_HERO_202pe:# <12>[1453]
	""" Shifting Hero Power
	Each turn, transform into a random Hero Power. """
	#
	pass
class BG20_HERO_202pt:# <12>[1453]
	""" Shift your Hero Power
	Trigger Power of the Storm effect """
	#
	pass
######## BUDDY
class BG20_HERO_202_Buddy:# <12>[1453]
	""" Lei Flamepaw
	'Power of the Storm' offers3 options instead of 2. """
	#
	pass
class BG20_HERO_202_Buddy_G:# <12>[1453]
	""" Lei Flamepaw
	'Power of the Storm' offers4 options instead of 2. """
	#
	pass


#39#Millhouse Manastorm  ### HP OK ###
BG_Hero3 += ['TB_BaconShop_HERO_49','TB_BaconShop_HP_054','TB_Baconshop_HP_054e','TB_BaconShop_HERO_49_Buddy','TB_BaconShop_HERO_49_Buddy_G',]# 
BG_PoolSet_Hero3 +=['TB_BaconShop_HERO_49',]#
BG_Hero3_Buddy['TB_BaconShop_HERO_49']='TB_BaconShop_HERO_49_Buddy'#
BG_Hero3_Buddy_Gold['TB_BaconShop_HERO_49_Buddy']='TB_BaconShop_HERO_49_Buddy_G'#
class TB_BaconShop_HERO_49:# <12>[1453]
	""" Millhouse Manastorm """
	pass
class TB_BaconShop_HP_054:
	""" Manastorm
	[Passive] Minions cost 2 Gold. [Refresh] costs 2 Gold. _Tavern Tiers cost (1) more."""
class TB_Baconshop_HP_054e:
	""" Costs (1) less."""
######## BUDDY
class TB_BaconShop_HERO_49_Buddy:# <12>[1453]
	""" Magnus Manastorm
	After you buy a minion,add one of the same TavernTier to Bob's Tavern. """
	#
	pass
class TB_BaconShop_HERO_49_Buddy_G:# <12>[1453]
	""" Magnus Manastorm
	After you buy a minion,add two of the same TavernTier to Bob's Tavern. """
	#
	pass





#40#Millificent Manastorm ### HP ###
BG_Hero3 += ['TB_BaconShop_HERO_17','TB_BaconShop_HP_015','TB_BaconShop_HP_015e','TB_BaconShop_HERO_17_Buddy','TB_BaconShop_HERO_17_Buddy_G',]# 
BG_PoolSet_Hero3 +=['TB_BaconShop_HERO_17',]#
BG_Hero3_Buddy['TB_BaconShop_HERO_17']='TB_BaconShop_HERO_17_Buddy'#
BG_Hero3_Buddy_Gold['TB_BaconShop_HERO_17_Buddy']='TB_BaconShop_HERO_17_Buddy_G'#
class TB_BaconShop_HERO_17:# <12>[1453]
	""" Millificent Manastorm """
	pass
class TB_BaconShop_HP_015_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=target
		if hasattr(controller.game,'this_is_tavern'):
			bartender = controller.opponent
			for card in bartender.field:
				if card.race==Race.MECHANICAL:
					for buff in card.buffs:
						if buff.id=='TB_BaconShop_HP_015e':
							break
					else:
						Buff(card, 'TB_BaconShop_HP_015e').trigger(source)
		pass
class TB_BaconShop_HP_015:
	""" Tinker
	[Passive]Mechs in Bob's Tavern have +1/+1."""
	events = [
		BeginBar(CONTROLLER).on(TB_BaconShop_HP_015_Action(CONTROLLER)),
		Rerole(CONTROLLER).on(TB_BaconShop_HP_015_Action(CONTROLLER)),
	]
TB_BaconShop_HP_015e=buff(1,1)
######## BUDDY
class TB_BaconShop_HERO_17_Buddy:# <12>[1453] 
	""" Elementium Squirrel Bomb
	[Deathrattle:] Deal 3 damage to a random enemy minion for each of your Mechs that died this combat. """
	#
	pass
class TB_BaconShop_HERO_17_Buddy_G:
	""" 
	[Deathrattle:] Deal 6 damage to a random enemy minion for each of your Mechs that died this combat.""" 



#41#Mr. Bigglesworth  ### impossible ###
##BG_Hero3 += ['TB_BaconShop_HERO_70','TB_BaconShop_HP_080','TB_BaconShop_HERO_70_Buddy','TB_BaconShop_HERO_70_Buddy_G',]# 
##BG_PoolSet_Hero3 +=['TB_BaconShop_HERO_70',]#
##BG_Hero3_Buddy['TB_BaconShop_HERO_70']='TB_BaconShop_HERO_70_Buddy'#
##BG_Hero3_Buddy_Gold['TB_BaconShop_HERO_70_Buddy']='TB_BaconShop_HERO_70_Buddy_G'#
class TB_BaconShop_HERO_70:# <12>[1453]
	""" Mr. Bigglesworth """
class TB_BaconShop_HP_080:
	""" Kel'Thuzad's Kitty
	[Passive] When a player dies, [Discover] a minion from their warband. It keeps any enchantments."""
######## BUDDY
class TB_BaconShop_HERO_70_Buddy:# <12>[1453]
	""" Lil' K.T.
	At the start of your turn,get a plain minion fromyour lowest Healthopponent's warband. """
	#
	pass
class TB_BaconShop_HERO_70_Buddy_G:# <12>[1453]
	""" Lil' K.T.
	At the start of your turn,get 2 plain minions fromyour lowest Health opponent's warband. """
	#
	pass



### Murloc Holmes ###BG23_HERO_303## new 24.2 ####################################
BG_Hero3 += ['BG23_HERO_303','BG23_HERO_303p2','BG23_HERO_303pt']# 
BG_PoolSet_Hero3 +=['BG23_HERO_303',]#
class BG23_HERO_303:
	""" Murloc Holmes
	"""
class BG23_HERO_303p2:
	""" Detective for Hire
	Look at 2 minions. Guess which one your next opponent had last combat for a Coin."""
	pass
class BG23_HERO_303pt:
	pass



#42#Mutanus the Devourer ### HP OK ###
BG_Hero3 += ['BG20_HERO_301','BG20_HERO_301p','BG20_HERO_301_Buddy','BG20_HERO_301_Buddy_G',]# 
BG_PoolSet_Hero3 +=['BG20_HERO_301',]#
BG_Hero3_Buddy['BG20_HERO_301']='BG20_HERO_301_Buddy'#
BG_Hero3_Buddy_Gold['BG20_HERO_301_Buddy']='BG20_HERO_301_Buddy_G'#
class BG20_HERO_301: ## 
	""" Mutanus the Devourer	"""
class BG20_HERO_301p_Action(TargetedAction):
	TARGET=ActionArg()
	CARD=ActionArg()
	def do(self, source, target, card):
		if hasattr(card, '__iter__') and len(card)>0:
			card = card[0]
		controller=target
		atk = card.atk
		health = card.max_health
		Destroy(card).trigger(source)
		anothercard = random.choice(controller.field)
		Buff(anothercard, 'BG20_HERO_301pe',
			atk=atk, max_health=health
			).trigger(source)
		Give(controller, 'GAME_005').trigger(source)
		pass
class BG20_HERO_301p:
	""" Devour
	Remove a friendly minion. Spit its stats onto another. Get 1 Gold."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, 
				 PlayReq.REQ_FRIENDLY_TARGET:0,}
	activate = BG20_HERO_301p_Action(CONTROLLER, TARGET)
@custom_card
class BG20_HERO_301pe:
	tags = {
		GameTag.CARDNAME: "Devour buff",
		GameTag.CARDTEXT: "",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
	}
######## BUDDY
class BG20_HERO_301_Buddy:
	"""Nightmare Ectoplasm
	When you 'Devour' this, spit its stats onto 2 extra_minions."""
class BG20_HERO_301_Buddy_G:
	"""Nightmare Ectoplasm
	When you 'Devour' this, spit its stats onto 4 extra_minions."""



#43#N'Zoth  ### HP OK ###
BG_Hero3 += ['TB_BaconShop_HERO_93','TB_BaconShop_HP_105','TB_BaconShop_HP_105t','TB_BaconShop_HERO_93_Buddy','TB_BaconShop_HERO_93_Buddy_G',]# 
BG_PoolSet_Hero3 +=['TB_BaconShop_HERO_93',]#
BG_Hero3_Buddy['TB_BaconShop_HERO_93']='TB_BaconShop_HERO_93_Buddy'#
BG_Hero3_Buddy_Gold['TB_BaconShop_HERO_93_Buddy']='TB_BaconShop_HERO_93_Buddy_G'#
class TB_BaconShop_HERO_93:# <12>[1453]
	""" N'Zoth 	 """
class TB_BaconShop_HP_105_Action(TargetedAction):
	TARGET=ActionArg()
	CARD=ActionArg()
	def do(self, source, target, card):
		new_deathrattles = card.deathrattles
		old_deathrattles = source.data.scripts.deathrattle
		ret = []
		for deathrattle in old_deathrattles:
			ret.append(deathrattle)
		ret += new_deathrattles[0]
		source.data.scripts.deathrattle=tuple(ret)
		deathrattles = source.deathrattles
		print("%r->%s"%(source.deathrattles,source))
		pass
class TB_BaconShop_HP_105_Action2(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		source.data.scripts.deathrattle=[]
		pass
class TB_BaconShop_HP_105:
	""" Avatar of N'Zoth
	[Passive] Start the game with a 2/2 Fish that gains all your [Deathrattles] in combat."""
	events = BeginGame(CONTROLLER).on(Summon(CONTROLLER,'TB_BaconShop_HP_105t'))
class TB_BaconShop_HP_105t:
	""" fish """
	events = [
		BeginBattle(CONTROLLER).on(TB_BaconShop_HP_105_Action2(SELF)),
		Deathrattle(FRIENDLY).on(TB_BaconShop_HP_105_Action(SELF, Deathrattle.TARGET))
	]
	tags = {GameTag.DEATHRATTLE:True}
######## BUDDY
class TB_BaconShop_HERO_93_Buddy:# <12>[1453]
	""" Baby N'Zoth
	[Battlecry:] Make a friendly[Deathrattle] minion Golden. """
	#
	pass
class TB_BaconShop_HERO_93_Buddy_G:# <12>[1453]
	""" Baby N'Zoth
	[Battlecry:] Make all friendly[Deathrattle] minions Golden. """
	#
	pass




#44#Nozdormu  ### HP OK ###
BG_Hero3 += ['TB_BaconShop_HERO_57','TB_BaconShop_HP_063','TB_BaconShop_HERO_57_Buddy','TB_BaconShop_HERO_57_Buddy_e','TB_BaconShop_HERO_57_Buddy_G',]# 
BG_PoolSet_Hero3 +=['TB_BaconShop_HERO_57',]#
BG_Hero3_Buddy['TB_BaconShop_HERO_57']='TB_BaconShop_HERO_57_Buddy'#
BG_Hero3_Buddy_Gold['TB_BaconShop_HERO_57_Buddy']='TB_BaconShop_HERO_57_Buddy_G'#
class TB_BaconShop_HERO_57:# <12>[1453]
	""" Nozdormu  """
class TB_BaconShop_HP_063:
	""" Clairvoyance
	[Passive] Your first [Refresh] each turn costs (0)"""
	events = BeginBar(CONTROLLER).on(GetFreeRerole(CONTROLLER))
######## BUDDY
class TB_BaconShop_HERO_57_Buddy:# <12>[1453]
	""" Chromie
	Minions in Bob's Tavernhave +1/+1 for each time itwas [Refreshed] this turn. """
	#
	pass
class TB_BaconShop_HERO_57_Buddy_e:# <12>[1453]
	""" Flow of Time
	Stats increased by Chromie. """
	#
	pass
class TB_BaconShop_HERO_57_Buddy_G:# <12>[1453]
	""" Chromie
	Minions in Bob's Tavernhave +2/+2 for each time itwas [Refreshed] this turn. """
	#
	pass





#45#Onyxia ### HP OK ###
BG_Hero3 += ['BG22_HERO_305','BG22_HERO_305p','BG22_HERO_305t','BG22_HERO_305_Buddy','BG22_HERO_305_Buddy_e','BG22_HERO_305_Buddy_G','BG22_HERO_305_Buddy_Ge',]# 
BG_PoolSet_Hero3 +=['BG22_HERO_305',]#
BG_Hero3_Buddy['BG22_HERO_305']='BG22_HERO_305_Buddy'#
BG_Hero3_Buddy_Gold['BG22_HERO_305_Buddy']='BG22_HERO_305_Buddy_G'#
class BG22_HERO_305:# <12>[1453]
	""" Onyxia """
class BG22_HERO_305p_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=target
		newcard = Summon(controller, 'BG22_HERO_305t').trigger(source)
		newcard = newcard[0][0]
		if len(controller.opponent.field)>0:
			target = random.choice(controller.opponent.field)
			BG_Attack(newcard, target).trigger(source)
		pass
class BG22_HERO_305p:# <12>[1453]
	""" Broodmother
	[Passive][Avenge (4):] Summona 3/1 Whelp. It attacks immediately. """
	events = Death(FRIENDLY + MINION).on(Avenge(SELF, 4, [BG22_HERO_305p_Action(CONTROLLER)]))
	pass
class BG22_HERO_305t:# <12>[1453]
	""" Onyxian Whelp
	"""
######## BUDDY
class BG22_HERO_305_Buddy:# <12>[1453]
	""" Many Whelps
	Whenever you summon a Whelp, gain +2/+2 permanently. """
	#
	pass
class BG22_HERO_305_Buddy_e:# <12>[1453]
	""" Swarming
	+2/+2. """
	#
	pass
class BG22_HERO_305_Buddy_G:# <12>[1453]
	""" Many Whelps
	Whenever you summon a Whelp, gain +4/+4 permanently. """
	#
	pass
class BG22_HERO_305_Buddy_Ge:# <12>[1453]
	""" Swarming
	+4/+4. """
	#
	pass






#46#Overlord Saurfang ### HP OK ###
BG_Hero3 += ['BG20_HERO_102','BG20_HERO_102p','BG20_HERO_102pe','BG20_HERO_102pe2','BG20_HERO_102pe3','BG20_HERO_102_Buddy','BG20_HERO_102_Buddy_G','BG20_HERO_102pe_Buddy',]# 
BG_PoolSet_Hero3 +=['BG20_HERO_102',]#
BG_Hero3_Buddy['BG20_HERO_102']='BG20_HERO_102_Buddy'#
BG_Hero3_Buddy_Gold['BG20_HERO_102_Buddy']='BG20_HERO_102_Buddy_G'#
class BG20_HERO_102:# <12>[1453]
	""" Overlord Saurfang """
class BG20_HERO_102pe_Action(TargetedAction):
	TARGET=ActionArg()
	CARD=ActionArg()
	def do(self, source, target, card):
		controller=target
		if hasattr(card, '__iter__'):
			card = card[0]
		amount = source.source.script_data_num_1
		Buff(card, 'BG20_HERO_102pe2', atk=amount).trigger(source)
		#source.destroy()
		pass
class BG20_HERO_102p:# <10>[1453]
	""" For the Horde!
	Give +@ Attack to the next minion you buy this turn.<i>(Upgrades each turn!)</i> """
	activate = Buff(CONTROLLER, 'BG20_HERO_102pe')
	events = [
		BeginGame(CONTROLLER).on(SetScriptDataNum1(SELF,0)),
		BeginBar(CONTROLLER).on(AddScriptDataNum1(SELF,1))
		]
	pass
class BG20_HERO_102pe:# <12>[1453]
	""" Saurfang Player Enchantment
	Give extra Attack to the next minion you buy this turn. """
	events = [
		Buy(CONTROLLER).on(
			BG20_HERO_102pe_Action(CONTROLLER, Buy.CARD),
			Destroy(SELF)
			),
		#OWN_TURN_END.on(Destroy(SELF)),##valid until 23.4.3
		]
class BG20_HERO_102pe2:# <12>[1453]
	""" For the Horde!
	Increased Attack. """
class BG20_HERO_102pe3:# <12>[1453] Why? lol
	""" For the Horde!
	Increased Health. """
######## BUDDY
class BG20_HERO_102pe_Buddy:# <12>[1453]
	""" Saurfang Player Enchantment (Buddy)
	Give extra Health to the next minion you buy this turn. """
	#
	pass
class BG20_HERO_102_Buddy:# <12>[1453]
	""" Dranosh Saurfang
	'For the Horde!' also grants Health. """
	#
	pass
class BG20_HERO_102_Buddy_G:# <12>[1453]
	""" Dranosh Saurfang
	'For the Horde!' also grants Health twice. """
	#
	pass



#47#Patches the Pirate ### HP OK ###
BG_Hero3 += ['TB_BaconShop_HERO_18','TB_BaconShop_HP_072','TB_BaconShop_HERO_18_Buddy','TB_BaconShop_HERO_18_Buddy_e','TB_BaconShop_HERO_18_Buddy_G',]# 
BG_PoolSet_Hero3 +=['TB_BaconShop_HERO_18',]#
BG_Hero3_Buddy['TB_BaconShop_HERO_18']='TB_BaconShop_HERO_18_Buddy'#
BG_Hero3_Buddy_Gold['TB_BaconShop_HERO_18_Buddy']='TB_BaconShop_HERO_18_Buddy_G'#
class TB_BaconShop_HERO_18:# <12>[1453]
	""" Patches the Pirate """
class TB_BaconShop_HP_072_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=target
		Give(controller, RandomBGPirate(tech_level_less=TIER(CONTROLLER))).trigger(source)
		gold_card_id = controller.game.BG_find_triple()## �g���v���𔻒�
		if gold_card_id:
			controller.game.BG_deal_gold(gold_card_id)
		for i in range(len(source.buffs)):
			source.buffs.remove(source.buffs[0])
		pass
class TB_BaconShop_HP_072:
	"""Pirate Parrrrty!
	Get a Pirate. After you buy a Pirate, your next Hero Power costs (1) less."""
	activate = TB_BaconShop_HP_072_Action(CONTROLLER)
	events = Buy(CONTROLLER, PIRATE).on(Buff(SELF,'TB_BaconShop_HP_072e'))
@custom_card
class TB_BaconShop_HP_072e:
	tags = {
		GameTag.CARDNAME: "Pirate Parrrrty! buff",
		GameTag.CARDTEXT: "",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.COST: -1,
	}
	#events = OWN_TURN_END.on(Destroy(SELF))
######## BUDDY
class TB_BaconShop_HERO_18_Buddy:# <12>[1453]
	"""Tuskarr Raider
	[Battlecry:] Give a minion +1/+1 for each Pirate you played this game."""
class TB_BaconShop_HERO_18_Buddy_e:# <12>[1453]
	""" Raiding with Tuskarr
	Increased stats. """
	#
	pass
class TB_BaconShop_HERO_18_Buddy_G:
	"""
	[Battlecry:] Give a minion +2/+2 for each Pirate you played this game."""



#48#Patchwerk  ### HP OK ###
BG_Hero3 += ['TB_BaconShop_HERO_34','TB_BaconShop_HP_035','TB_BaconShop_HERO_34_Buddy','TB_BaconShop_HERO_34_Buddy_e','TB_BaconShop_HERO_34_Buddy_G',]# 
BG_PoolSet_Hero3 +=['TB_BaconShop_HERO_34',]#
BG_Hero3_Buddy['TB_BaconShop_HERO_34']='TB_BaconShop_HERO_34_Buddy'#
BG_Hero3_Buddy_Gold['TB_BaconShop_HERO_34_Buddy']='TB_BaconShop_HERO_34_Buddy_G'#
class TB_BaconShop_HERO_34:# <12>[1453]
	""" Patchwerk  """
	#<Tag enumID="45" name="HEALTH" type="Int" value="60"/>
	pass
class TB_BaconShop_HP_035:
	""" All Patched Up
	[Passive] Start with 60 Health instead of 40."""  ### new 24.2
	##[Passive] Start with 55 Health instead of 40.""" old
######## BUDDY
class TB_BaconShop_HERO_34_Buddy:# <12>[1453]
	""" Weebomination
	[Battlecry:] Give a minion +1_Health for each Health your hero is missing. """
	#
	pass
class TB_BaconShop_HERO_34_Buddy_e:# <12>[1453]
	""" Patched Up
	Increased Health. """
	#
	pass
class TB_BaconShop_HERO_34_Buddy_G:# <12>[1453]
	""" Weebomination
	[Battlecry:] Give a minion +2_Health for each Health your hero is missing. """
	#
	pass



#49#Pyramad   ### maybe OK ###
BG_Hero3 += ['TB_BaconShop_HERO_39','TB_BaconShop_HP_040','TB_BaconShop_HP_040e','TB_BaconShop_HERO_39_Buddy','TB_BaconShop_HERO_39_Buddy_e','TB_BaconShop_HERO_39_Buddy_G',]# 
BG_PoolSet_Hero3 +=['TB_BaconShop_HERO_39',]#
BG_Hero3_Buddy['TB_BaconShop_HERO_39']='TB_BaconShop_HERO_39_Buddy'#
BG_Hero3_Buddy_Gold['TB_BaconShop_HERO_39_Buddy']='TB_BaconShop_HERO_39_Buddy_G'#
class TB_BaconShop_HERO_39:# <12>[1453]
	""" Pyramad	 """
class TB_BaconShop_HP_040_Action1(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	def do(self, source, target, buff):
		if hasattr(target,'__iter__') and len(target)>0:
			target=target[0]
		if target:
			Buff(target, buff, max_health=source.script_data_num_1).trigger(source)
		pass
class TB_BaconShop_HP_040_Action2(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		if not target.exhausted:
			source.script_data_num_1 += 1
class TB_BaconShop_HP_040:
	""" Brick by Brick
	Give a minion +@ Health. <i>(Gains +1 Health each turn you don't use this!)</i> """ #23.6
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, 
				 PlayReq.REQ_FRIENDLY_TARGET:0,}	
	activate = TB_BaconShop_HP_040_Action1(TARGET, 'TB_BaconShop_HP_040e')
	events = EndTurn(CONTROLLER).on(TB_BaconShop_HP_040_Action2(SELF))
	## Give a random friendly minion +4_Health. (old version , -2022.6)
	## <Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="2"/>
class TB_BaconShop_HP_040e:
	pass
######## BUDDY
class TB_BaconShop_HERO_39_Buddy:# <12>[1453]
	""" Titanic Guardian
	Whenever a different friendly minion gains Health, this gains it too. """
	#
	pass
class TB_BaconShop_HERO_39_Buddy_e:# <12>[1453]
	""" Fractured, Focused
	Increased Health """
	#
	pass
class TB_BaconShop_HERO_39_Buddy_G:# <12>[1453]
	""" Titanic Guardian
	Whenever a different friendly minion gains Health, this gains twice that amount. """
	#
	pass



## Queen Axshara
BG_Hero3+=['BG22_HERO_007','BG22_HERO_007p','BG22_HERO_007p2','BG22_HERO_007t',]#
BG_PoolSet_Hero3.append('BG22_HERO_007')
class BG22_HERO_007:
	""" Queen Axshara 	"""
class BG22_HERO_007p:
	""" Azshara's Ambition
	[Passive.] When your warband reaches 30 total Attack, begin your Naga Conquest.@[x][Passive.] When your warband reaches 30 total Attack, begin your Naga Conquest. <i>({0} left!)</i>"""
	pass
class BG22_HERO_007p2:
	""" Naga Conquest
	[Discover] a Naga."""
	activate = Discover(CONTROLLER, RandomBGNaga(tech_level_less=TIER(CONTROLLER)))
	pass
class BG22_HERO_007t:
	""" Naga Queen Azshara
	"""
	pass


#50#Queen Wagtoggle ### HP OK ### 
BG_Hero3 += ['TB_BaconShop_HERO_14','TB_BaconShop_HP_037a','TB_BaconShop_HP_037te','TB_BaconShop_HERO_14_Buddy','TB_BaconShop_HERO_14_Buddy_G',]# 
BG_PoolSet_Hero3 +=['TB_BaconShop_HERO_14',]#
BG_Hero3_Buddy['TB_BaconShop_HERO_14']='TB_BaconShop_HERO_14_Buddy'#
BG_Hero3_Buddy_Gold['TB_BaconShop_HERO_14_Buddy']='TB_BaconShop_HERO_14_Buddy_G'#
class TB_BaconShop_HERO_14:# <12>[1453]
	""" Queen Wagtoggle """
class TB_BaconShop_HP_037a_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = target
		races=[]
		cards=[]
		field = copy(controller.field)
		random.shuffle(field)
		for card in field:
			if card.race==Race.INVALID:
				pass
			elif card.race==Race.ALL:
				races.append(card.race)
				cards.append(card)
			elif not card.race in races:
				races.append(card.race)
				cards.append(card)
		for card in cards:
			Buff(card, 'TB_BaconShop_HP_037te').trigger(source)
class TB_BaconShop_HP_037a:
	""" Wax Warband
	Give a friendly minion of each minion type +1/+1.""" 
	activate = TB_BaconShop_HP_037a_Action(CONTROLLER)
TB_BaconShop_HP_037te=buff(1,1)
######## BUDDY
class TB_BaconShop_HERO_14_Buddy:# <12>[1453]
	""" Elder Taggawag
	Whenever you play a minionof a type you don't control,trigger your Hero Power.<i>(@ left this turn.)</i> """
	#
	pass
class TB_BaconShop_HERO_14_Buddy_G:# <12>[1453]
	""" Elder Taggawag
	Whenever you play a minionof a type you don't control,trigger your Hero Power__twice. <i>(@ left this turn.)</i> """
	#
	pass








###################################################



