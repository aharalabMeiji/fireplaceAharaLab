from ..utils import *
import copy
from fireplace.battlegrounds import BG_utils



BG_Hero3=[]
BG_PoolSet_Hero3=[]
BG_Hero3_Buddy={}
BG_Hero3_Buddy_Gold={}

#### source ####################################################


##Lady Vashj ### HP OK ## BUDDY OK ###
BG_Hero3+=[
	'BG23_HERO_304','BG23_HERO_304p', 
	'BG23_HERO_304_Buddy','BG23_HERO_304_Buddy_G']#
BG_PoolSet_Hero3.append('BG23_HERO_304')
BG_Hero3_Buddy['BG23_HERO_304']='BG23_HERO_304_Buddy'
BG_Hero3_Buddy_Gold['BG23_HERO_304_Buddy']='BG23_HERO_304_Buddy_G'
class BG23_HERO_304:
	""" Lady Vashj """
class BG23_HERO_304p_Action(TargetedAction):
	BUFF=ActionArg()
	def do(self, source, buff):
		if hasattr(buff.source,'spellcraft_spellcard') or buff.data.tags.get(2594)==1:### 2594 = spellcraft_buff
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
###### buddy #####
class BG23_HERO_304_Buddy_Action(GameAction):
	def do(self, source):
		controller = source.controller
		cards=[card for card in controller.opponent.field if getattr(card, 'spellcraft', None)!=None]
		if len(cards):
			for card in cards:
				spellcardID=getattr(card, 'spellcraft', None)
				if spellcardID!=None:
					Give(controller, spellcardID).trigger(source)
		pass
class BG23_HERO_304_Buddy:
	""" Coilfang Elite
	After a [Spellcraft] minion appears in Bob's Tavern, get a copy of its spell."""
	events = Rerole(CONTROLLER).after(BG23_HERO_304_Buddy_Action())
	pass
class BG23_HERO_304_Buddy_G_Action(GameAction):
	def do(self, source):
		controller = source.controller
		cards=[card for card in controller.opponent.field if getattr(card, 'spellcraft', None)!=None]
		if len(cards):
			for card in cards:
				spellcardIDD=getattr(card, 'spellcraft', None)
				if spellcardID!=None:
					Give(controller, spellcardID).trigger(source)
					Give(controller, spellcardID).trigger(source)
		pass
class BG23_HERO_304_Buddy_G:
	""" Coilfang Elite
	After a [Spellcraft] minion appears in Bob's Tavern, get 2 copies of its spell."""
	events = Rerole(CONTROLLER).after(BG23_HERO_304_Buddy_G_Action())
	pass



##Lich Baz'hial ### HP OK ###
BG_Hero3+=['TB_BaconShop_HERO_25','TB_BaconShop_HP_049','TB_BaconShop_HERO_25_Buddy','TB_BaconShop_HERO_25_Buddy_e','TB_BaconShop_HERO_25_Buddy_G','TB_BaconShop_HERO_25_Buddy_Ge',]
BG_PoolSet_Hero3+=['TB_BaconShop_HERO_25']
BG_Hero3_Buddy['TB_BaconShop_HERO_25']='TB_BaconShop_HERO_25_Buddy'
BG_Hero3_Buddy_Gold['TB_BaconShop_HERO_25_Buddy']='TB_BaconShop_HERO_25_Buddy_G'
class TB_BaconShop_HERO_25:# <12>[1453]
	""" Lich Baz'hial	 """
class TB_BaconShop_HP_049:
	""" Graveyard Shift
	Take $4 damage. Gain 2 Gold. """ ## 25.?
	## Take $4 damage. Gain 2 Gold this turn only.""" # 24.0.3
	## Take $2_damage and add a Gold Coin to your hand. 24.0
	activate = Hit(FRIENDLY_HERO, 4), Give(CONTROLLER, 'GAME_005')*2
	pass
######## BUDDY
class TB_BaconShop_HERO_25_Buddy_Action(TargetedAction):# <12>[1453]
	TARGET=ActionArg()
	def do(self, source, target):
		target.predamage=0
		Buff(source, 'TB_BaconShop_HERO_25_Buddy_e').trigger(source)
		pass
class TB_BaconShop_HERO_25_Buddy:# <12>[1453]
	""" Unearthed Underling
	Whenever your hero takes damage, this minion gains +2/+2 instead.<i>(@ left this turn.)</i> """
	###Whenever your hero takes damage, this minion gains +3/+3 instead.<i>(@ left this turn.)</i> """
	#<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="2"/>
	events = Predamage(FRIENDLY_HERO).on(TB_BaconShop_HERO_25_Buddy_Action(Predamage.TARGET))
	pass
TB_BaconShop_HERO_25_Buddy_e=buff(2,2)# <12>[1453]
class TB_BaconShop_HERO_25_Buddy_G_Action(TargetedAction):# <12>[1453]
	TARGET=ActionArg()
	def do(self, source, target):
		target.predamage=0
		Buff(source, 'TB_BaconShop_HERO_25_Buddy_Ge').trigger(source)
		pass
class TB_BaconShop_HERO_25_Buddy_G:# <12>[1453]
	""" Unearthed Underling
	Whenever your hero takes damage, this minion gains +4/+4 instead.<i>(@ left this turn.)</i> """
	##Whenever your hero takesdamage, this miniongains +6/+6 instead.<i>(@ left this turn.)</i> """
	events = Predamage(FRIENDLY_HERO).on(TB_BaconShop_HERO_25_Buddy_G_Action(Predamage.TARGET))
	pass
TB_BaconShop_HERO_25_Buddy_Ge=buff(4,4)# <12>[1453]
""" Recovery,+6/+6. """




##Lord Barov  #### HP OK  ###
BG_Hero3+=['TB_BaconShop_HERO_72','TB_BaconShop_HP_081','TB_BaconShop_HERO_72_Buddy','TB_BaconShop_HERO_72_Buddy_G',]
BG_PoolSet_Hero3+=['TB_BaconShop_HERO_72']
BG_Hero3_Buddy['TB_BaconShop_HERO_72']='TB_BaconShop_HERO_72_Buddy'
BG_Hero3_Buddy_Gold['TB_BaconShop_HERO_72_Buddy']='TB_BaconShop_HERO_72_Buddy_G'
class TB_BaconShop_HERO_72:# <12>[1453]
	""" Lord Barov	 """
class TB_BaconShop_HP_081_Choice(Choice):
	def choose(self, card):
		#record the card data in self.source.source.script_data_text_1
		super().choose(card)
		self.next_choice=None
		self.player.choice=None
		self.source.sidequest_list0=[card.id]	
		pass
class TB_BaconShop_HP_081_Action1(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=target
		gamemaster=controller.game.parent
		thisMatch=[]
		# choose randomly a next battle
		for match in gamemaster.matches:
			if gamemaster.BG_Bars[match[0]].controller!=controller and gamemaster.BG_Bars[match[1]].controller!=controller:
				thisMatch.append(match)
		thisMatch = random.choice(thisMatch)
		# make a choice data from the next battle
		matchChoice=[
			gamemaster.BG_Bars[match[0]].controller.hero.id,
			gamemaster.BG_Bars[match[1]].controller.hero.id
			]	
		# trigger TB_BaconShop_HP_081_Choice 
		TB_BaconShop_HP_081_Choice(controller, RandomID(*matchChoice)*2).trigger(source)
		choiceAction(controller)
		pass
class TB_BaconShop_HP_081_Action2(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=target
		#from gamemaster investigate the result of the battle
		#match it with source.sctipt_data_text_1
		if source.sidequest_list0!=[] and source.sidequest_list0[0] in controller.game.parent.winners:
			#if correct, give the controller three coins.
			Give(controller, 'GAME_005').trigger(source)
			Give(controller, 'GAME_005').trigger(source)
			Give(controller, 'GAME_005').trigger(source)
		if source.sidequest_list0!=[] and source.sidequest_list0[0] in controller.game.parent.drawers:
			#if correct, give the controller three coins.
			Give(controller, 'GAME_005').trigger(source)
		source.sidequest_list0=[]## clear the guess
class TB_BaconShop_HP_081: ############# impossible
	"""Friendly Wager
	Guess which player will win their next combat. _If they win, get 3 Coins."""
	activate=TB_BaconShop_HP_081_Action1(CONTROLLER)
	events = BeginBar(CONTROLLER).on(TB_BaconShop_HP_081_Action2(CONTROLLER))
######## BUDDY
class TB_BaconShop_HERO_72_Buddy:# <12>[1453]
	""" Barov's Apprentice
	After you play a Gold Coin, gain 1 Gold this turn only. """
	BG_Play(CONTROLLER, 'GAME_005').after(ManaThisTurn(CONTROLLER, 1))
	pass
class TB_BaconShop_HERO_72_Buddy_G:# <12>[1453]
	""" Barov's Apprentice
	After you play a Gold Coin, gain 2 Gold this turn only. """
	BG_Play(CONTROLLER, 'GAME_005').after(ManaThisTurn(CONTROLLER, 2))
	pass



##Lord Jaraxxus ### HP OK ### BUDDY maybe ###
BG_Hero3 += [
	'TB_BaconShop_HERO_37','TB_BaconShop_HP_036','TB_BaconShop_HP_036e2',
	'TB_BaconShop_HERO_37_Buddy','TB_BaconShop_HERO_37_Buddy_G',	]# 
BG_PoolSet_Hero3 +=['TB_BaconShop_HERO_37',]#
BG_Hero3_Buddy['TB_BaconShop_HERO_37']='TB_BaconShop_HERO_37_Buddy'#
BG_Hero3_Buddy_Gold['TB_BaconShop_HERO_37_Buddy']='TB_BaconShop_HERO_37_Buddy_G'#
class TB_BaconShop_HERO_37:# <12>[1453]
	""" Lord Jaraxxus """
class TB_BaconShop_HP_036_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		target=get00(target)
		if len(source.controller.opponent.field) and target!=None:
			controller =source.controller
			card = random.choice(controller.opponent.field)
			atk=card.atk
			hlt=card.max_health
			Destroy(card).trigger(source)
			Buff(target, 'TB_BaconShop_HP_036e2', atk=atk, max_health=hlt).trigger(source)
class TB_BaconShop_HP_036:
	""" Bloodfury
	Choose a friendly Demon. It consumes a minion in Bob's Tavern to gain its stats."""
	###Give your Demons +1/+1."""
	requirements = { PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE:Race.DEMON}
	activate = TB_BaconShop_HP_036_Action(TARGET)
class TB_BaconShop_HP_036e2:
	pass
######## BUDDY
class TB_BaconShop_HERO_37_Buddy_Action(GameAction):
	def do(self, source):
		original_controller=source.controller.deepcopy_original
		newcard=RandomBGDemon(tech_level_less=source.controller.tavern_tier).evaluate(source)
		newcard=get00(newcard)
		newcard.controller = original_controller
		newcard.zone=Zone.HAND
class TB_BaconShop_HERO_37_Buddy:
	"""Kil'rek
	[Taunt] [Deathrattle:] Add a random Demon to your hand."""
	deathrattle = TB_BaconShop_HERO_37_Buddy_Action()
class TB_BaconShop_HERO_37_Buddy_G_Action(GameAction):
	def do(self, source):
		original_controller=source.controller.deepcopy_original
		newcard0=RandomBGDemon(tech_level_less=source.controller.tavern_tier).evaluate(source)
		newcard0=get00(newcard0)
		newcard0.controller = original_controller
		newcard0.zone=Zone.HAND
		newcard1=RandomBGDemon(tech_level_less=source.controller.tavern_tier).evaluate(source)
		newcard1=get00(newcard1)
		newcard1.controller = original_controller
		newcard1.zone=Zone.HAND
class TB_BaconShop_HERO_37_Buddy_G:
	""" Kil'rek
	[Taunt] [Deathrattle:] Add 2 random Demons to your hand."""
	deathrattle = TB_BaconShop_HERO_37_Buddy_G_Action()
	pass




##Maiev Shadowsong  ### HP OK ###
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
		target.zone=Zone.SETASIDE
		target.controller = controller
		target.zone = Zone.HAND
		if target in bartender.field:
			bartender.field.remove(target)
		Buff(target, 'TB_BaconShop_HP_068e').trigger(source.owner)
		pass
class TB_BaconShop_HP_068pe:
	"""ImprisonedWatcher	"""
	def apply(self, target):
		source=self.owner## TB_BaconShop_HP_068
		if source.action_option>0:
			source.action_option -= 1
			target.dormant=2
		else:
			target.dormant=3
	events = Awaken().on(TB_BaconShop_HP_068pe_Action(CONTROLLER, Awaken.TARGET),Destroy(SELF))
	pass
TB_BaconShop_HP_068e=buff(2,2)
class TB_BaconShop_HP_068e2:
	pass
######## BUDDY
class TB_BaconShop_HERO_62_Buddy_Action:# <12>[1453]
	def do(self, source):
		source.controller.hero.power.action_option=1
class TB_BaconShop_HERO_62_Buddy:# <12>[1453]
	""" Shadow Warden
	[Battlecry:] Your next Hero Power makes the target Golden and awaken 1 turn faster. """
	play = TB_BaconShop_HERO_62_Buddy_Action()
	pass
class TB_BaconShop_HERO_62_Buddy_e:# <12>[1453]
	""" Next Hero Power Goldens
	Your next Hero Power makes the target Golden. """
	#
class TB_BaconShop_HERO_62_Buddy_G_Action:# <12>[1453]
	def do(self, source):
		source.controller.hero.power.action_option=2
class TB_BaconShop_HERO_62_Buddy_G:# <12>[1453]
	""" Shadow Warden
	[Battlecry:] Your next 2 Hero Powers make the target Golden and awaken 1 turn faster. """
	play = TB_BaconShop_HERO_62_Buddy_G_Action()
	pass



##Malygos ###  HP OK ###
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
		option_tier = source.action_option
		tier = min(target.tech_level+option_tier,6)
		newcard = RandomBGAdmissible(tech_level=tier).evaluate(bartender)
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
class TB_BaconShop_HERO_58_Buddy_Action(GameAction):
	def do(self, source):
		source.controller.hero.power.action_option=1
		pass
class TB_BaconShop_HERO_58_Buddy:# <12>[1453]
	""" Nexus Lord
	'Arcane Alteration'replaces with a minion one Tavern Tier higher. """
	play = TB_BaconShop_HERO_58_Buddy_Action()
	pass
class TB_BaconShop_HERO_58_Buddy_G_Action(GameAction):
	def do(self, source):
		source.controller.hero.power.action_option=2
		pass
class TB_BaconShop_HERO_58_Buddy_G:# <12>[1453]
	""" Nexus Lord
	'Arcane Alteration'replaces with a minion two Tavern Tiers higher. """
	play = TB_BaconShop_HERO_58_Buddy_G_Action()
	pass



##Master Nguyen ### same phenomena ###
BG_Hero3 += ['BG20_HERO_202','BG20_HERO_202p','BG20_HERO_202pe','BG20_HERO_202pt','BG20_HERO_202_Buddy','BG20_HERO_202_Buddy_G',]# 
BG_PoolSet_Hero3 +=['BG20_HERO_202',]#
BG_Hero3_Buddy['BG20_HERO_202']='BG20_HERO_202_Buddy'#
BG_Hero3_Buddy_Gold['BG20_HERO_202_Buddy']='BG20_HERO_202_Buddy_G'#
class BG20_HERO_202:# <12>[1453]
	""" Master Nguyen """
class BG20_HERO_202p_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		ChangeHeroPower(self.player, card.id).trigger(self.source)
		if not 'BG20_HERO_202pe' in [buff.id for buff in self.source.controller.buffs]:
			Buff(self.source.controller,'BG20_HERO_202pe').trigger(self.source)
		self.player.choice=None
class BG20_HERO_202p_Action(GameAction):
	def do(self, source):
		controller=source.controller
		heroes=[hero for hero in controller.game.parent.Heroes if hero!='BG20_HERO_202']
		if getattr(source, 'this_is_enchantment', False):
			choice_number=2+source.source.action_option
		else:## this_is_heropower
			choice_number=2+source.action_option
		if len(heroes)>choice_number:
			heroes = random.sample(heroes,choice_number)
		BG20_HERO_202p_Choice(controller, RandomID(*heroes)*choice_number).trigger(source)
		choiceAction(controller)
		pass
class BG20_HERO_202p:# <12>[1453]
	""" Power of the Storm
	[Passive]At the start of every turn, choose from 2 new Hero Powers. """
	events = BeginBar(CONTROLLER).on(BG20_HERO_202p_Action())	#
	pass
class BG20_HERO_202pe:# <12>[1453]
	""" Shifting Hero Power
	Each turn, transform into a random Hero Power. """
	#
	events = BeginBar(CONTROLLER).on(BG20_HERO_202p_Action())
	pass
class BG20_HERO_202pt:# <12>[1453]
	""" Shift your Hero Power
	Trigger Power of the Storm effect """
	#
	pass
######## BUDDY
class BG20_HERO_202_Buddy_Action(GameAction):# <12>[1453]
	def do(self, source):
		source.controller.hero.power.action_option=1
		pass
class BG20_HERO_202_Buddy:# <12>[1453]
	""" Lei Flamepaw
	'Power of the Storm' offers 3 options instead of 2. """
	play = BG20_HERO_202_Buddy_Action()
	pass
class BG20_HERO_202_Buddy_G_Action(GameAction):# <12>[1453]
	def do(self, source):
		source.controller.hero.power.action_option=2
		pass
class BG20_HERO_202_Buddy_G:# <12>[1453]
	""" Lei Flamepaw
	'Power of the Storm' offers 4 options instead of 2. """
	play = BG20_HERO_202_Buddy_G_Action()
	pass



##Millhouse Manastorm  ### HP OK ###
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
class TB_BaconShop_HERO_49_Buddy_Action(TargetedAction):# <12>[1453]
	CARD=CardArg()
	def do(self, source, card):
		card=get00(card)
		tier=card.tech_level
		newcard=RandomBGMinion(tech_level=tier).evaluate(source)
		newcard=get00(newcard)
		newcard.zone=Zone.SETASIDE
		newcard.controller=source.controller.opponent
		newcard.zone=Zone.PLAY#Bob's Tavern
class TB_BaconShop_HERO_49_Buddy:# <12>[1453]
	""" Magnus Manastorm
	After you buy a minion,add one of the same TavernTier to Bob's Tavern. """
	events = Buy(CONTROLLER).after(TB_BaconShop_HERO_49_Buddy_Action(Buy.CARD))
	pass
class TB_BaconShop_HERO_49_Buddy_G_Action(TargetedAction):# <12>[1453]
	CARD=CardArg()
	def do(self, source, card):
		card=get00(card)
		tier=card.tech_level
		for repeat in range(2):
			newcard=RandomBGMinion(tech_level=tier).evaluate(source)
			newcard=get00(newcard)
			newcard.zone=Zone.SETASIDE
			newcard.controller=source.controller.opponent
			newcard.zone=Zone.PLAY#Bob's Tavern
		pass
class TB_BaconShop_HERO_49_Buddy_G:# <12>[1453]
	""" Magnus Manastorm
	After you buy a minion,add two of the same TavernTier to Bob's Tavern. """
	events = Buy(CONTROLLER).after(TB_BaconShop_HERO_49_Buddy_G_Action(Buy.CARD))
	pass





##Millificent Manastorm ### HP ###
BG_Hero3 += ['TB_BaconShop_HERO_17','TB_BaconShop_HP_015','TB_BaconShop_HP_015e','TB_BaconShop_HERO_17_Buddy','TB_BaconShop_HERO_17_Buddy_G',]# 
BG_PoolSet_Hero3 +=['TB_BaconShop_HERO_17',]#
BG_Hero3_Buddy['TB_BaconShop_HERO_17']='TB_BaconShop_HERO_17_Buddy'#
BG_Hero3_Buddy_Gold['TB_BaconShop_HERO_17_Buddy']='TB_BaconShop_HERO_17_Buddy_G'#
class TB_BaconShop_HERO_17:# <12>[1453]
	""" Millificent Manastorm """
	pass
class TB_BaconShop_HP_015_Action(GameAction):### old
	def do(self, source):
		controller=source.controller
		if hasattr(controller.game,'this_is_tavern'):
			bartender = controller.opponent
			for card in bartender.field:
				#if card.race==Race.MECHANICAL:
				if race_identity(card,Race.MECHANICAL):
					for buff in card.buffs:
						if buff.id=='TB_BaconShop_HP_015e':
							break
					else:
						Buff(card, 'TB_BaconShop_HP_015e').trigger(source)
		pass
class TB_BaconShop_HP_015:
	""" Tinker
	&lt;b&gt;Passive&lt;/b&gt; Whenever you summon a Mech, give it +2 Attack."""
	### [Passive]Mechs in Bob's Tavern have +1/+1.
	events = Summon(CONTROLLER, FRIENDLY + MINION + MECH).on(Buff(Summon.CARD, 'TB_BaconShop_HP_015e'))
	#events = [
	#	BeginBar(CONTROLLER).on(TB_BaconShop_HP_015_Action()),
	#	Rerole(CONTROLLER).on(TB_BaconShop_HP_015_Action()),
	#]
TB_BaconShop_HP_015e=buff(2,0)
#TB_BaconShop_HP_015e=buff(1,1)
######## BUDDY
class TB_BaconShop_HERO_17_Buddy_Deathrattle(GameAction):
	def do(self, source):
		controller = source.controller
		amount=0
		for card in controller.death_log:
			if race_identity(card, Race.MECHANICAL):
				amount += 1
		for repeat in range(amount):
			if len(controller.opponent.field):
				card = random.choice(controller.opponent.field)
				Hit(card,2).trigger(source)
class TB_BaconShop_HERO_17_Buddy:# <12>[1453] 
	""" Elementium Squirrel Bomb
	&lt;b&gt;Deathrattle:&lt;/b&gt; Deal 2 damage to a random enemy minion for each of your Mechs that died this combat."""
	###[Deathrattle:] Deal 3 damage to a random enemy minion for each of your Mechs that died this combat. """
	deathrattle = TB_BaconShop_HERO_17_Buddy_Deathrattle()
	pass
class TB_BaconShop_HERO_17_Buddy_G_Deathrattle(GameAction):
	def do(self, source):
		controller = source.controller
		amount=0
		for card in controller.death_log:
			if race_identity(card, Race.MECHANICAL):
				amount += 1
		for repeat in range(amount):
			if len(controller.opponent.field):
				card = random.choice(controller.opponent.field)
				Hit(card,4).trigger(source)
class TB_BaconShop_HERO_17_Buddy_G:
	""" 
	[Deathrattle:] Deal 4 damage to a random enemy minion for each of your Mechs that died this combat.""" 
	deathrattle = TB_BaconShop_HERO_17_Buddy_G_Deathrattle()

from fireplace.cards import db


##Mr. Bigglesworth  ### OK ###
BG_Hero3 += ['TB_BaconShop_HERO_70','TB_BaconShop_HP_080','TB_BaconShop_HERO_70_Buddy','TB_BaconShop_HERO_70_Buddy_G',]# 
BG_PoolSet_Hero3 +=['TB_BaconShop_HERO_70',]#
BG_Hero3_Buddy['TB_BaconShop_HERO_70']='TB_BaconShop_HERO_70_Buddy'#
BG_Hero3_Buddy_Gold['TB_BaconShop_HERO_70_Buddy']='TB_BaconShop_HERO_70_Buddy_G'#
class TB_BaconShop_HERO_70:# <12>[1453]
	""" Mr. Bigglesworth """
class TB_BaconShop_HP_080_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		self.player.choice=None
		super().choose(card)
		#card.zone=Zone.SETASIDE
		card.controller=self.player
		card.zone=Zone.HAND
		choices=[cd for cd in self.player.game.parent.warbandDeceased[0] if cd.id==card.id]
		if len(choices)>0:
			choice=choices[0]
			for bf in choice.buffs:
				bf.apply(card)
		self.player.game.parent.warbandDeceased=[]
		pass
	pass
class TB_BaconShop_HP_080_Action(GameAction):
	def do(self, source):
		controller=source.controller
		if len(controller.game.parent.warbandDeceased):
			field = random.choice(controller.game.parent.warbandDeceased)
			controller.game.parent.warbandDeceased=[field]###
			amount=len(field)
			if amount>3:
				field=random.sample(field, 3)
				amount=3
			if Config.LOGINFO:
				Config.log("TB_BaconShop_HP_080_Action","get 3 samples")
			fieldIDs=[cd.id for cd in field]
			TB_BaconShop_HP_080_Choice(controller, RandomID(*fieldIDs)*amount).trigger(source)
			choiceAction(controller)
		pass
class TB_BaconShop_HP_080:
	""" Kel'Thuzad's Kitty
	[Passive] When a player dies, [Discover] a minion from their warband. It keeps any enchantments."""
	# controller.game.parent.warbandDeceased : list of the field cards of killed heroes.
	events = BeginBar(CONTROLLER).on(TB_BaconShop_HP_080_Action())
######## BUDDY
class TB_BaconShop_HERO_70_Buddy_Action(GameAction):
	def do(self, source):
		controller = source.controller
		gamemaster = controller.game.parent
		next_warband = gamemaster.next_warband(controller)
		low=[]
		low_hlt=9999
		if len(next_warband):
			for card in next_warband:
				hlt = db[card].health
				if low==[]:
					low = [card]
					low_hlt=hlt
				elif hlt<low_hlt:
					low = [card]
					low_hlt=hlt
				elif hlt==low_hlt:
					low.append(card)
			card = random.choice(low)
			newcard = controller.card(card)
			newcard.zone=Zone.HAND
		pass		
class TB_BaconShop_HERO_70_Buddy:# <12>[1453]
	""" Lil' K.T.
	At the start of your turn,get a plain minion from your lowest Health opponent's warband. """
	events = BeginBar(CONTROLLER).on(TB_BaconShop_HERO_70_Buddy_Action())
	pass
class TB_BaconShop_HERO_70_Buddy_G_Action(GameAction):
	def do(self, source):
		controller = source.controller
		gamemaster = controller.game.parent
		next_warband = gamemaster.next_warband(controller)
		low=[]
		if len(next_warband):
			for card in next_warband:
				hlt = db[card].health
				if low==[]:
					low = [card]
					low_hlt=hlt
				elif hlt<low_hlt:
					low = [card]
					low_hlt=hlt
				elif hlt==low_hlt:
					low.append(card)
			card = random.choice(low)
			newcard0 = controller.card(card.id)
			newcard0.zone=Zone.HAND
			card = random.choice(low)
			newcard1 = controller.card(card.id)
			newcard1.zone=Zone.HAND
		pass		
class TB_BaconShop_HERO_70_Buddy_G:# <12>[1453]
	""" Lil' K.T.
	At the start of your turn,get 2 plain minions fromyour lowest Health opponent's warband. """
	events = BeginBar(CONTROLLER).on(TB_BaconShop_HERO_70_Buddy_G_Action())
	pass


## Murloc Holmes ###BG23_HERO_303## new 24.2 #### HP OK #####        ###
BG_Hero3 += ['BG23_HERO_303','BG23_HERO_303p2','BG23_HERO_303pt','BG23_HERO_303_Buddy','BG23_HERO_303_Buddy_G']# 
BG_PoolSet_Hero3 +=['BG23_HERO_303',]#
BG_Hero3_Buddy['BG23_HERO_303']='BG23_HERO_303_Buddy'#
BG_Hero3_Buddy_Gold['BG23_HERO_303_Buddy']='BG23_HERO_303_Buddy_G'#
class BG23_HERO_303:
	""" Murloc Holmes
	"""
class BG23_HERO_303p2_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		if card.id==self.source.sidequest_list0[0]:
			Give(self.source.controller, 'GAME_005').trigger(self.source)
			if len([cd for cd in self.source.controller.field if cd.id=='BG23_HERO_303_Buddy']):
				Give(self.source.controller, card.id).trigger(self.source)
			if len([cd for cd in self.source.controller.field if cd.id=='BG23_HERO_303_Buddy_G']):
				Give(self.source.controller, card.id).trigger(self.source)
				Give(self.source.controller, card.id).trigger(self.source)
		self.player.choice=None
class BG23_HERO_303p2_Action(GameAction):
	def do(self, source):
		controller = source.controller
		gamemaster = controller.game.parent
		next_warband = gamemaster.next_warband(controller)
		if len(next_warband)>0:
			cardID1 = random.choice(next_warband)
			tavern_tier=db[cardID1].tags.get(GameTag.TECH_LEVEL,1)
			cardID2=None
			for repeat in range(10):
				card2=RandomBGAdmissible(tech_level=tavern_tier).evaluate(source)
				card2 = card2[0]
				cardID2 = card2.id
				card2.discard()
				if not cardID2 in next_warband:
					break
			if cardID2!=None:
				source.sidequest_list0=[cardID1]
				BG23_HERO_303p2_Choice(controller, RandomID(cardID1, cardID2)*2).trigger(source)
				choiceAction(controller)
		pass
class BG23_HERO_303p2:
	""" Detective for Hire
	Look at 2 minions. Guess which one your next opponent had last combat for a Coin."""
	activate = BG23_HERO_303p2_Action()
	pass
class BG23_HERO_303pt:
	pass
###### Buddy ######
class BG23_HERO_303_Buddy:
	""" Watfin
	After you guess correctly with 'Detective for Hire', get a plain copy of the minion. """
	pass
class BG23_HERO_303_Buddy_G:
	""" Watfin
	After you guess correctly with 'Detective for Hire', get 2 plain copies of the minion. """
	pass




##Mutanus the Devourer ### HP OK ###
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
		extra_minions=1
		if len([cd for cd in controller.field if cd.id=='BG20_HERO_301_Buddy']):
			extra_minions=2
		if len([cd for cd in controller.field if cd.id=='BG20_HERO_301_G_Buddy']):
			extra_minions=4
		if len(controller.field)>=2:
			Destroy(card).trigger(source)
			if len(controller.field)>extra_minions:
				othercards = random.sample(controller.field, extra_minions)
			else:
				othercards = controller.field
			for anothercard in othercards:
				Buff(anothercard, 'BG20_HERO_301pe', atk=atk, max_health=health).trigger(source)
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



##N'Zoth  ### HP OK ###
BG_Hero3 += [
	'TB_BaconShop_HERO_93','TB_BaconShop_HP_105','TB_BaconShop_HP_105t','TB_BaconUps_307',
	'TB_BaconShop_HERO_93_Buddy','TB_BaconShop_HERO_93_Buddy_G',]# 
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
		#deathrattles = source.deathrattles
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
	""" Fish of N'Zoth """
	events = [
		BeginBattle(CONTROLLER).on(TB_BaconShop_HP_105_Action2(SELF)),
		Deathrattle(FRIENDLY).on(TB_BaconShop_HP_105_Action(SELF, Deathrattle.TARGET))
	]
	tags = {GameTag.DEATHRATTLE:True}
class TB_BaconUps_307_Action(TargetedAction):
	TARGET=ActionArg()
	CARD=ActionArg()
	def do(self, source, target, card):
		new_deathrattles = card.deathrattles
		old_deathrattles = source.data.scripts.deathrattle
		ret = []
		for deathrattle in old_deathrattles:
			ret.append(deathrattle)
		for deathrattle in old_deathrattles:
			ret.append(deathrattle)
		ret += new_deathrattles[0]
		source.data.scripts.deathrattle=tuple(ret)
		#deathrattles = source.deathrattles
		print("%r->%s"%(source.deathrattles,source))
		pass
class TB_BaconUps_307:### Gold card
	""" Fish of N'Zoth 
	After a friendly &lt;b&gt;Deathrattle&lt;/b&gt; minion dies, gain its &lt;b&gt;Deathrattle&lt;/b&gt; twice."""
	events = [
		BeginBattle(CONTROLLER).on(TB_BaconShop_HP_105_Action2(SELF)),
		Deathrattle(FRIENDLY).on(TB_BaconUps_307_Action(SELF, Deathrattle.TARGET))
	]
	tags = {GameTag.DEATHRATTLE:True}
######## BUDDY
class TB_BaconShop_HERO_93_Buddy_Action(GameAction):# <12>[1453]
	def do(self, source):
		cards=[cd for cd in source.controller.field if cd.has_deathrattle==True]
		if len(cards):
			card = random.choice(cards)
			source.controller.game.BG_morph_gold(card)### remove AN old card and add a new gold card
			pass
class TB_BaconShop_HERO_93_Buddy:# <12>[1453]
	""" Baby N'Zoth
	[Battlecry:] Make a friendly[Deathrattle] minion Golden. """
	play = TB_BaconShop_HERO_93_Buddy_Action()
	pass
class TB_BaconShop_HERO_93_Buddy_G_Action(GameAction):# <12>[1453]
	def do(self, source):
		cards=[cd for cd in source.controller.field if cd.has_deathrattle==True]
		if len(cards):
			for card in cards:
				source.controller.game.BG_morph_gold(card)### remove AN old card and add a new gold card
class TB_BaconShop_HERO_93_Buddy_G:# <12>[1453]
	""" Baby N'Zoth
	[Battlecry:] Make all friendly[Deathrattle] minions Golden. """
	play = TB_BaconShop_HERO_93_Buddy_G_Action()
	pass




##Nozdormu  ### HP OK ###
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
class TB_BaconShop_HERO_57_Buddy_Action0(GameAction):# <12>[1453]
	def do(self, source):
		source.action_option=0
		pass
class TB_BaconShop_HERO_57_Buddy_Action1(GameAction):# <12>[1453]
	def do(self, source):
		source.action_option+=1
		for cd in source.controller.field:
			Buff(cd, 'TB_BaconShop_HERO_57_Buddy_e', atk=source.action_option, max_health=source.action_option).trigger(source)
		pass
class TB_BaconShop_HERO_57_Buddy:# <12>[1453]
	""" Chromie
	Minions in Bob's Tavern have +1/+1 for each time it was [Refreshed] this turn. """
	events = [
		BeginBar(CONTROLLER).on(TB_BaconShop_HERO_57_Buddy_Action0()),
		Rerole(CONTROLLER).on(TB_BaconShop_HERO_57_Buddy_Action1())
		]
	pass
class TB_BaconShop_HERO_57_Buddy_e:# <12>[1453]
	""" Flow of Time
	Stats increased by Chromie. """
	#
	pass
class TB_BaconShop_HERO_57_Buddy_Action2(GameAction):# <12>[1453]
	def do(self, source):
		source.action_option+=2
		for cd in source.controller.field:
			Buff(cd, 'TB_BaconShop_HERO_57_Buddy_e', atk=source.action_option, max_health=source.action_option).trigger(source)
		pass
class TB_BaconShop_HERO_57_Buddy_G:# <12>[1453]
	""" Chromie
	Minions in Bob's Tavernhave +2/+2 for each time itwas [Refreshed] this turn. """
	events = [
		BeginBar(CONTROLLER).on(TB_BaconShop_HERO_57_Buddy_Action0()),
		Rerole(CONTROLLER).on(TB_BaconShop_HERO_57_Buddy_Action2())
		]
	pass





##Onyxia ### HP OK ###
BG_Hero3 += [
	'BG22_HERO_305','BG22_HERO_305p','BG22_HERO_305t',
	'BG22_HERO_305_Buddy','BG22_HERO_305_Buddy_e','BG22_HERO_305_Buddy_G','BG22_HERO_305_Buddy_Ge',]# 
BG_PoolSet_Hero3 +=['BG22_HERO_305',]#
BG_Hero3_Buddy['BG22_HERO_305']='BG22_HERO_305_Buddy'#
BG_Hero3_Buddy_Gold['BG22_HERO_305_Buddy']='BG22_HERO_305_Buddy_G'#
class BG22_HERO_305:# <12>[1453]
	""" Onyxia """
class BG22_HERO_305p_Action(GameAction):
	def do(self, source):
		controller=source.controller
		newcard = Summon(controller, 'BG22_HERO_305t').trigger(source)
		if newcard[0]==[]:
			return
		newcard = newcard[0][0]
		if len(controller.opponent.field)>0:
			target = random.choice(controller.opponent.field)
			BG_Attack(newcard, target).trigger(source)
		pass
class BG22_HERO_305p:# <12>[1453]
	""" Broodmother
	[Passive][Avenge (4):] Summona 3/1 Whelp. It attacks immediately. """
	events = Death(FRIENDLY + MINION).on(Avenge(SELF, 4, [BG22_HERO_305p_Action()]))
	pass
class BG22_HERO_305t:# <12>[1453]
	""" Onyxian Whelp
	"""
######## BUDDY
class BG22_HERO_305_Buddy:# <12>[1453]
	""" Many Whelps
	Whenever you summon a Whelp, gain +2/+2 permanently. """
	events = Summon(CONTROLLER, ID('BG22_HERO_305t')).after(BuffPermanently(SELF, 'BG22_HERO_305_Buddy_e'))
	pass
BG22_HERO_305_Buddy_e=buff(2,2)# <12>[1453]
class BG22_HERO_305_Buddy_G:# <12>[1453]
	""" Many Whelps
	Whenever you summon a Whelp, gain +4/+4 permanently. """
	events = Summon(CONTROLLER, ID('BG22_HERO_305t')).after(BuffPermanently(SELF, 'BG22_HERO_305_Buddy_Ge'))
	pass
BG22_HERO_305_Buddy_Ge=buff(4,4)# <12>[1453]






##Overlord Saurfang ### HP OK ###
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
		if len([cd for cd in source.source.controller.field if cd.id=='BG20_HERO_102_Buddy']):
			Buff(card, 'BG20_HERO_102pe2', atk=amount, max_health=amount).trigger(source)
		elif len([cd for cd in source.source.controller.field if cd.id=='BG20_HERO_102_Buddy_G']):
			Buff(card, 'BG20_HERO_102pe2', atk=amount, max_health=amount*2).trigger(source)
		else:
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
	pass
class BG20_HERO_102_Buddy:# <12>[1453]
	""" Dranosh Saurfang
	'For the Horde!' also grants Health. """
	pass
class BG20_HERO_102_Buddy_G:# <12>[1453]
	""" Dranosh Saurfang
	'For the Horde!' also grants Health twice. """
	pass


## Ozumat ######### HP OK ######### need check buddy 23/4/5
BG_Hero3 += ['BG23_HERO_201','BG23_HERO_201p','BG23_HERO_201pt','BG23_HERO_201_Buddy','BG23_HERO_201_Buddy_G']# 
BG_PoolSet_Hero3 +=['BG23_HERO_201',]#
BG_Hero3_Buddy['BG23_HERO_201']='BG23_HERO_201_Buddy'#
BG_Hero3_Buddy_Gold['BG23_HERO_201_Buddy']='BG23_HERO_201_Buddy_G'#
class BG23_HERO_201:
	""" Ozumat
	"""
class BG23_HERO_201p_Action(GameAction):
	def do(self, source):
		#summon a tentacle with enchantment BG23_HERO_201pte
		controller=source.controller
		newcard=Summon(controller, 'BG23_HERO_201pt').trigger(source)
		if newcard[0]==[]:
			return
		newcard=newcard[0][0]
		Buff(newcard, 'BG23_HERO_201pte', atk=source.script_data_num_1-2, max_health=source.script_data_num_1-2 ).trigger(source)
		pass
class BG23_HERO_201p:
	""" Tentacular
	[Passive. Start of Combat:] Summon a @/@ Tentacle with [Taunt]. (Gains +1/+1 after you sell a minion!)"""
	#after selling a minion, add 1 to self.script_data_num_1
	# at BeginBattle, summon a tentacle with enchantment BG23_HERO_201pte
	#<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="2"/>
	events=[
		Sell(CONTROLLER).after(AddScriptDataNum1(SELF, 1)),	
		BeginBattle(CONTROLLER).on(BG23_HERO_201p_Action())
		]
class BG23_HERO_201pt:
	""" Ozumat's Tentacle
	"""
	pass
@custom_card
class BG23_HERO_201pte:
	tags = {
		GameTag.CARDNAME: "Ozumat's Tentacle",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
	}
###### Buddy ######
class BG23_HERO_201_Buddy_Action(GameAction):
	def do(self, source):
		controller=source.controller
		heropower=controller.hero.power
		heropower.script_data_num_1 += 1
class BG23_HERO_201_Buddy:
	""" Tamuzo
	[Avenge (2):] Upgrade 'Tentacular' by +1/+1. """
	events=Death(FRIENDLY + MINION).on(Avenge(SELF, 2, [BG23_HERO_201_Buddy_Action()]))
class BG23_HERO_201_Buddy_G_Action(GameAction):
	def do(self, source):
		controller=source.controller
		heropower=controller.hero.power
		heropower.script_data_num_1 += 2
class BG23_HERO_201_Buddy_G:
	""" Tamuzo
	[Avenge (2):] Upgrade 'Tentacular' by +2/+2. """
	events=Death(FRIENDLY + MINION).on(Avenge(SELF, 2, [BG23_HERO_201_Buddy_G_Action()]))



##Patches the Pirate ### HP OK ###
BG_Hero3 += ['TB_BaconShop_HERO_18','TB_BaconShop_HP_072','TB_BaconShop_HERO_18_Buddy','TB_BaconShop_HERO_18_Buddy_e','TB_BaconShop_HERO_18_Buddy_G',]# 
BG_PoolSet_Hero3 +=['TB_BaconShop_HERO_18',]#
BG_Hero3_Buddy['TB_BaconShop_HERO_18']='TB_BaconShop_HERO_18_Buddy'#
BG_Hero3_Buddy_Gold['TB_BaconShop_HERO_18_Buddy']='TB_BaconShop_HERO_18_Buddy_G'#
class TB_BaconShop_HERO_18:# <12>[1453]
	""" Patches the Pirate """
class TB_BaconShop_HP_072_Action(GameAction):
	def do(self, source):
		controller=source.controller
		Give(controller, RandomBGPirate(tech_level_less=TIER(CONTROLLER))).trigger(source)
		gold_card_id = controller.game.BG_find_triple()## 
		if gold_card_id:
			controller.game.BG_deal_gold(gold_card_id)
		for i in range(len(source.buffs)):
			source.buffs.remove(source.buffs[0])
		pass
class TB_BaconShop_HP_072:
	"""Pirate Parrrrty!
	Get a Pirate. After you buy a Pirate, your next Hero Power costs (1) less."""
	activate = TB_BaconShop_HP_072_Action()
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



##Patchwerk  ### HP OK ###
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


##Professor Putricide BG25_HERO_100
BG_Hero3 += ['BG25_HERO_100','BG25_HERO_100p','BG25_HERO_100_Buddy','BG25_HERO_100_Buddy_G','BG25_HERO_100pt',]# 
BG_PoolSet_Hero3 +=['BG25_HERO_100',]#
BG_Hero3_Buddy['BG25_HERO_100']='BG25_HERO_100_Buddy'#
BG_Hero3_Buddy_Gold['BG25_HERO_100_Buddy']='BG25_HERO_100_Buddy_G'#
class BG25_HERO_100:
	""" Professor Putricide
	"""
class BG25_HERO_100p:
	""" Build-An-Undead
	[x]Craft a custom Undead. &lt;i&gt;(@ Creations left!)&lt;/i&gt;"""
class BG25_HERO_100_Buddy:
	""" Festergut
	[Deathrattle:] Summon a random Undead Creation."""
class BG25_HERO_100_Buddy_G:
	""" Festergut
	[x][Deathrattle:] Summon 2 random Undead Creations."""
class BG25_HERO_100pt:
	""" Putricide's Creation
	"""


##Pyramad   ### maybe OK ###
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



## Queen Axshara #### HP OK ####
BG_Hero3+=['BG22_HERO_007','BG22_HERO_007p','BG22_HERO_007p2','BG22_HERO_007t','BG22_HERO_007_Buddy', 'BG22_HERO_007_Buddy_G',]#
BG_PoolSet_Hero3.append('BG22_HERO_007')
BG_Hero3_Buddy['BG22_HERO_007']='BG22_HERO_007_Buddy'#
BG_Hero3_Buddy_Gold['BG22_HERO_007_Buddy']='BG22_HERO_007_Buddy_G'#
class BG22_HERO_007:
	""" Queen Axshara 	"""
class BG22_HERO_007p_Action(GameAction):
	def do(self, source):
		controller=source.controller
		if getattr(controller.game,'this_is_tavern',False):
			amount = sum([card.atk for card in controller.field])
			source.script_data_text_0=max(30-amount,0)
			if amount>= 30:#source.script_data_num_2:
				ChangeHeroPower(controller, 'BG22_HERO_007p2').trigger(source)
		pass
class BG22_HERO_007p:
	""" Azshara's Ambition
	[Passive.] When your warband reaches 30 total Attack, begin your Naga Conquest.@[x][Passive.] When your warband reaches 30 total Attack, begin your Naga Conquest. <i>({0} left!)</i>"""
	#<Tag enumID="3" name="TAG_SCRIPT_DATA_NUM_2" type="Int" value="30"/>
	events = [
		Play(CONTROLLER).on(BG22_HERO_007p_Action()),
		Summon(CONTROLLER).on(BG22_HERO_007p_Action()),
		Buff(FRIENDLY_MINIONS).on(BG22_HERO_007p_Action()),
		BeginBar(CONTROLLER).on(BG22_HERO_007p_Action())
		]
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
##### Buddy ######
class BG22_HERO_007_Buddy_Action(TargetedAction):
	CARD=ActionArg()
	TARGET=ActionArg()
	def do(self, source, buff, target):
		pass
class BG22_HERO_007_Buddy:
	""" Imperial Defender
	Whenever you cast a [Spellcraft] spell on a _different minion, you also cast it on this."""
	events = Spellcraft(FRIENDLY + MINION - SELF).on(BG22_HERO_007_Buddy_Action(Spellcraft.SPELLCARD,Spellcraft.TARGET))
class BG22_HERO_007_Buddy_G:
	""" Imperial Defender
	Whenever you cast a [Spellcraft] spell on a _different minion, you also cast it on this twice."""



##Queen Wagtoggle ### HP OK ### need check buddy 23/4/6
BG_Hero3 += ['TB_BaconShop_HERO_14','TB_BaconShop_HP_037a','TB_BaconShop_HP_037te','TB_BaconShop_HERO_14_Buddy','TB_BaconShop_HERO_14_Buddy_G',]# 
BG_PoolSet_Hero3 +=['TB_BaconShop_HERO_14',]#
BG_Hero3_Buddy['TB_BaconShop_HERO_14']='TB_BaconShop_HERO_14_Buddy'#
BG_Hero3_Buddy_Gold['TB_BaconShop_HERO_14_Buddy']='TB_BaconShop_HERO_14_Buddy_G'#
class TB_BaconShop_HERO_14:# <12>[1453]
	""" Queen Wagtoggle """
class TB_BaconShop_HP_037a_Action(GameAction):
	def do(self, source):
		controller = source.controller
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
	activate = TB_BaconShop_HP_037a_Action()
TB_BaconShop_HP_037te=buff(1,1)
######## BUDDY
class TB_BaconShop_HERO_14_Buddy_Action(GameAction):
	def do(self, source):
		controller=source.controller
		count=0
		races=BG_utils.getRacesInCards(controller.field)
		count=len(races)
		for repeat in range(count):
			Give(controller, 'GAME_005').trigger(source)
class TB_BaconShop_HERO_14_Buddy:# <12>[1453]################################
	""" Elder Taggawag
	Whenever you play a minionof a type you don't control,trigger your Hero Power.<i>(@ left this turn.)</i> #old buddy
	[Battlecry:] Gain 1 Gold for each minion type you control. """
	play = TB_BaconShop_HERO_14_Buddy_Action()
	pass
class TB_BaconShop_HERO_14_Buddy_G_Action(GameAction):
	def do(self, source):
		controller=source.controller
		count=0
		races=BG_utils.getRacesInCards(controller.field)
		count=len(races)*2
		for repeat in range(count):
			Give(controller, 'GAME_005').trigger(source)
class TB_BaconShop_HERO_14_Buddy_G:# <12>[1453]###################################
	""" Elder Taggawag
	Whenever you play a minionof a type you don't control,trigger your Hero Power__twice. <i>(@ left this turn.)</i> ## old buddy
	[Battlecry:] Gain 2 Gold for each minion type you control."""
	play = TB_BaconShop_HERO_14_Buddy_G_Action()
	pass








###################################################



