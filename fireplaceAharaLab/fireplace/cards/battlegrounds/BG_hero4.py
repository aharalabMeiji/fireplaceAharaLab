from ..utils import *

BG_Hero4=[]


BG_PoolSet_Hero4=[]
BG_Hero4_Buddy={}
BG_Hero4_Buddy_Gold={}




######## source #################################################################

##Ragnaros the Firelord  ### HP OK ###
BG_Hero4 += ['TB_BaconShop_HERO_11','TB_BaconShop_HP_087','TB_BaconShop_HP_087t','TB_BaconShop_HP_087te','TB_BaconShop_HERO_11_Buddy','TB_BaconShop_HERO_11_Buddy_e','TB_BaconShop_HERO_11_Buddy_G','TB_BaconShop_HERO_11_Buddy_G_e',]# 
BG_PoolSet_Hero4 +=['TB_BaconShop_HERO_11',]#
BG_Hero4_Buddy['TB_BaconShop_HERO_11']='TB_BaconShop_HERO_11_Buddy'#
BG_Hero4_Buddy_Gold['TB_BaconShop_HERO_11_Buddy']='TB_BaconShop_HERO_11_Buddy_G'#
class TB_BaconShop_HERO_11:# <12>[1453]
	""" Ragnaros the Firelord """
class TB_BaconShop_HP_087t_Action(GameAction):
	def do(self, source):
		controller=source.controller
		if len(controller.field)>0:
			Buff(controller.field[0], 'TB_BaconShop_HP_087te').trigger(source)
			if len(controller.field)>1:
				Buff(controller.field[-1], 'TB_BaconShop_HP_087te').trigger(source)
		pass
class TB_BaconShop_HP_087_Action(GameAction):
	def do(self, source):
		controller=source.controller
		if hasattr(source.controller.game,'this_is_battle') and source.controller.game.this_is_battle:
			if source.deepcopy_original!=None:
				source.deepcopy_original.score_value_1 -= 1
				source.deepcopy_original.script_data_num_1 = source.deepcopy_original.score_value_1
				if source.deepcopy_original.script_data_num_1 <= 0: ###25
					ChangeHeroPower(controller.deepcopy_original, 'TB_BaconShop_HP_087t').trigger(source)
		pass
class TB_BaconShop_HP_087:
	""" DIE, INSECTS!
	[Passive] After you kill 25 enemy minions, get Sulfuras. <i>(@ left!)</i>"""
	events = Death(ENEMY + MINION).on(TB_BaconShop_HP_087_Action())
class TB_BaconShop_HP_087t:
	""" Sulfuras 
	[Passive] At the end of your turn, give your left- and right- most minions +3/+3."""
	events = OWN_TURN_END.on(TB_BaconShop_HP_087t_Action())
TB_BaconShop_HP_087te=buff(3,3)
######## BUDDY
class TB_BaconShop_HERO_11_Buddy:# <12>[1453]
	""" Lucifron
	Your end of turn effects trigger twice. """
	#
	pass
class TB_BaconShop_HERO_11_Buddy_e:# <12>[1453]
	""" Dark Magics
	Your end of turn effects trigger twice. """
	#
	pass
class TB_BaconShop_HERO_11_Buddy_G:# <12>[1453]
	""" Lucifron
	Your end of turn effects trigger three times. """
	#
	pass
class TB_BaconShop_HERO_11_Buddy_G_e:# <12>[1453]
	""" Dark Magics
	Your end of turn effects trigger three times. """
	#
	pass


##Rakanishu #  ### HP OK ###
BG_Hero4+=['TB_BaconShop_HERO_75','TB_BaconShop_HP_085','TB_BaconShop_HP_085e','TB_BaconShop_HERO_75_Buddy','TB_BaconShop_HERO_75_Buddy_G',]
BG_PoolSet_Hero4.append('TB_BaconShop_HERO_75')
BG_Hero4_Buddy['TB_BaconShop_HERO_75']='TB_BaconShop_HERO_75_Buddy'
BG_Hero4_Buddy_Gold['TB_BaconShop_HERO_75_Buddy']='TB_BaconShop_HERO_75_Buddy_G'
class TB_BaconShop_HERO_75:# <12>[1453]
	""" Rakanishu """
	pass
class TB_BaconShop_HERO_75_Action(TargetedAction):
	TARGET = ActionArg()
	OTHER = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, other, amount):
		controller = target
		if not isinstance(other, list):
			other = [other]
		tier = controller.tavern_tier
		for card in other:
			Buff(card, 'TB_BaconShop_HP_085e', atk=tier*amount, max_health=tier*amount).trigger(controller)
		pass
class TB_BaconShop_HP_085:
	""" Tavern Lighting 
	Give a minion stats equal to its Tavern Tier.""" # 24.2
	##Give a friendly minion stats equal to your Tavern Tier.""" ## old
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, }
	activate =  TB_BaconShop_HERO_75_Action(CONTROLLER, TARGET, 1)
class TB_BaconShop_HP_085e:
	"""  """
############# BUDDY 
class TB_BaconShop_HERO_75_Buddy:# <12>[1453]
	""" Lantern Tender
	At the end of your turn,give a random friendlyminion stats equal toyour Tavern Tier. """
	events = OWN_TURN_END.on(TB_BaconShop_HERO_75_Action(CONTROLLER, RANDOM_FRIENDLY_MINION, 1))
	pass
class TB_BaconShop_HERO_75_Buddy_G:# <12>[1453]
	""" Lantern Tender
	At the end of your turn,give a random friendlyminion stats equal to yourTavern Tier twice. """
	events = OWN_TURN_END.on(TB_BaconShop_HERO_75_Action(CONTROLLER, RANDOM_FRIENDLY_MINION, 2))
	pass





##Reno Jackson #  ### HP OK ###
BG_Hero4+=['TB_BaconShop_HERO_41','TB_BaconShop_HERO_41_Buddy','TB_BaconShop_HERO_41_Buddy_G','TB_BaconShop_HP_046',]
BG_PoolSet_Hero4.append('TB_BaconShop_HERO_41')
BG_Hero4_Buddy['TB_BaconShop_HERO_41']='TB_BaconShop_HERO_41_Buddy'
BG_Hero4_Buddy_Gold['TB_BaconShop_HERO_41_Buddy']='TB_BaconShop_HERO_41_Buddy_G'
class TB_BaconShop_HERO_41:# <12>[1453]
	""" Reno Jackson """
	pass

class TB_BaconShop_HP_046:
	"""  Gonna Be Rich!
	Make a friendly minion Golden. <i>(Once per game.)</i>"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, }
	activate = MorphGold(TARGET), MakeCardUnplayable(SELF)
	pass
############# BUDDY 
class TB_BaconShop_HERO_41_Buddy:# <12>[1453]
	""" Sr. Tomb Diver
	[Deathrattle:] Make your right-most minion Golden. """
	deathrattle = MorphGold(RIGHT_MOST(SELF))
	pass
class TB_BaconShop_HERO_41_Buddy_G:# <12>[1453]
	""" Sr. Tomb Diver
	[Deathrattle:] Make your two right-most minions Golden. """
	deathrattle = MorphGold(LEFT_OF(RIGHT_MOST(SELF)))
	deathrattle = MorphGold(RIGHT_MOST(SELF))
	pass





##Rokara #  ### OK ### 221107
BG_Hero4+=['BG20_HERO_100','BG20_HERO_100_Buddy','BG20_HERO_100_Buddy_e','BG20_HERO_100_Buddy_G','BG20_HERO_100_Buddy_Ge','BG20_HERO_100p','BG20_HERO_100p_e2']
BG_PoolSet_Hero4.append('BG20_HERO_100')
BG_Hero4_Buddy['BG20_HERO_100']='BG20_HERO_100_Buddy'
BG_Hero4_Buddy_Gold['BG20_HERO_100_Buddy']='BG20_HERO_100_Buddy_G'
class BG20_HERO_100:# <10>[1453] #### HP OK ####
	""" Rokara
	 """
	pass
class BG20_HERO_100_Action(TargetedAction):
	ATTACKER=ActionArg()
	DEFENDER=ActionArg()
	BUFF=ActionArg()
	def do(self, source, attacker, defender, buff):
		if defender.dead:
			BuffPermanently(attacker, buff).trigger(source)
		pass
class BG20_HERO_100p:# <10>[1453]
	""" Glory of Combat
	[Passive.] After a friendly minion kills an enemy, give it +1 Attack permanently. """
	events =  BG_Attack(FRIENDLY).after(BG20_HERO_100_Action(BG_Attack.TARGET, BG_Attack.OTHER, 'BG20_HERO_100p_e2'))
	pass
BG20_HERO_100p_e2=buff(1,0)
############# BUDDY 
class BG20_HERO_100_Buddy:# <12>[1453]
	""" Icesnarl the Mighty
	After a friendly minion kills an enemy, gain+1 Health permanently. """
	events =  BG_Attack(FRIENDLY).after(BG20_HERO_100_Action(BG_Attack.TARGET, BG_Attack.OTHER, 'BG20_HERO_100_Buddy_e'))
	pass
BG20_HERO_100_Buddy_e=buff(0,1)# <12>[1453]
class BG20_HERO_100_Buddy_G:# <12>[1453]
	""" Icesnarl the Mighty
	After a friendly minionkills an enemy, gain+2 Health permanently. """
	events =  BG_Attack(FRIENDLY).after(BG20_HERO_100_Action(BG_Attack.TARGET, BG_Attack.OTHER, 'BG20_HERO_100_Buddy_Ge'))
	pass
BG20_HERO_100_Buddy_Ge=buff(0,2)# <12>[1453]



##Scabbs Cutterbutter ### OK ###
BG_Hero4+=['BG21_HERO_010','BG21_HERO_010_Buddy','BG21_HERO_010_Buddy_G','BG21_HERO_010p',]
BG_PoolSet_Hero4.append('BG21_HERO_010')
BG_Hero4_Buddy['BG21_HERO_010']='BG21_HERO_010_Buddy'
BG_Hero4_Buddy_Gold['BG21_HERO_010_Buddy']='BG21_HERO_010_Buddy_G'
class BG21_HERO_010:# <7>[1453]
	""" Scabbs Cutterbutter	 """
	pass
class BG21_HERO_010p_Action(Choice):
	def get_args(self, source):
		controller = source.controller
		bartender = controller.opponent
		gamemaster = controller.game.parent
		next_warband = gamemaster.next_warband(controller)
		if len(next_warband)>3:
			next_warband=random.sample(next_warband,3)
		cards=[]
		for card in next_warband:
			cards.append(controller.card(card))
		return controller, cards
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		if Config.LOGINFO:
			print("(BG21_HERO_010p_Action.choose)%s chooses %r"%(card.controller.name, card))
		card.zone=Zone.HAND
class BG21_HERO_010p:# <7>[1453]
	""" I Spy
	[Discover] a plain copy of a minion from your next opponent's warband. """
	activate = BG21_HERO_010p_Action(CONTROLLER, [])
	pass
########### BUDDY
class BG21_HERO_010_Buddy:# <12>[1453]
	""" Warden Thelwater
	At the start of your turn, add your next opponent's Buddy to your hand. """
	#events = OWN_TURN_BEGIN.on(Give(CONTROLLER, ID(NEXT_OPPONENT_BUDDY)))
	pass
class BG21_HERO_010_Buddy_G:# <12>[1453]
	""" Warden Thelwater
	At the start of your turn, add 2 of your next opponent's Buddy to your hand. """
	#events = OWN_TURN_BEGIN.on(Give(CONTROLLER, ID(NEXT_OPPONENT_BUDDY))*2)
	pass



##Shudderwock ### OK ###
BG_Hero4+=['TB_BaconShop_HERO_23','TB_BaconShop_HERO_23_Buddy','TB_BaconShop_HERO_23_Buddy_e','TB_BaconShop_HERO_23_Buddy_G','TB_BaconShop_HERO_23_Buddy_Ge','TB_BaconShop_HP_022','TB_BaconShop_HP_022e','TB_BaconShop_HP_022t','TB_BaconShop_HP_022t_G',]
BG_PoolSet_Hero4.append('TB_BaconShop_HERO_23')
BG_Hero4_Buddy['TB_BaconShop_HERO_23']='TB_BaconShop_HERO_23_Buddy'
BG_Hero4_Buddy_Gold['TB_BaconShop_HERO_23_Buddy']='TB_BaconShop_HERO_23_Buddy_G'
class TB_BaconShop_HERO_23:# <12>[1453]
	""" Shudderwock """
	pass
class TB_BaconShop_HP_022_Action(GameAction):
	def do(self, source):
		controller = source.controller
		if source.script_data_num_1>0:
			Give(controller, 'TB_BaconShop_HP_022t').trigger(source)
			source.script_data_num_1-=1
		pass
class TB_BaconShop_HP_022:
	""" Snicker-snack
	Add a 1/1 Shudderling to your hand that repeats all [Battlecries] you've played. <i>(Twice per game.)</i>"""
	activate = TB_BaconShop_HP_022_Action()
	pass
class TB_BaconShop_HP_022e:
	pass
class TB_BaconShop_HP_022t_Action(GameAction):
	def do(self, source):
		#from fireplace.card import is_valid_target
		controller = source.controller
		cards=[]
		for action in controller._targetedaction_log: 
			card = action['target']
			if isinstance(action['class'], Battlecry)==True and card.id != source.id:## does it contain itself?
				if card.type==CardType.MINION and card.has_battlecry==True:
					newcard = controller.card(action['target'].id)
					cards.append(newcard)
		for card in cards:
			PlayBattlecry(card).trigger(source)
			newcard.discard()
		source.discard()
class TB_BaconShop_HP_022t:##[Battlecry:] Repeat all other [Battlecries] from cards you played this game <i>(targets chosen randomly)</i>.
	play = TB_BaconShop_HP_022t_Action()
	pass
class TB_BaconShop_HP_022t_G:
	pass
########## BUDDY
class TB_BaconShop_HERO_23_Buddy:# <12>[1453]
	""" Muckslinger
	After you play a minion,add a [Battlecry] minionto Bob's Tavern.Give it +2/+2. """
	pass
class TB_BaconShop_HERO_23_Buddy_e:# <12>[1453]
	""" Mucked Up
	+2/+2. """
	pass
class TB_BaconShop_HERO_23_Buddy_G:# <12>[1453]
	""" Muckslinger
	After you play a minion,add a [Battlecry] minionto Bob's Tavern.Give it +4/+4. """
	pass
class TB_BaconShop_HERO_23_Buddy_Ge:# <12>[1453]
	""" Mucked Up
	+4/+4. """
	pass



##Silas Darkmoon # ## OK ##
BG_Hero4+=['TB_BaconShop_HERO_90','TB_BaconShop_HERO_90_Buddy','TB_BaconShop_HERO_90_Buddy_G','TB_BaconShop_HP_101','TB_BaconShop_HP_101e','TB_BaconShop_HP_101t2',]
BG_PoolSet_Hero4.append('TB_BaconShop_HERO_90')
BG_Hero4_Buddy['TB_BaconShop_HERO_90']='TB_BaconShop_HERO_90_Buddy'
BG_Hero4_Buddy_Gold['TB_BaconShop_HERO_90_Buddy']='TB_BaconShop_HERO_90_Buddy_G'
class TB_BaconShop_HERO_90:# <12>[1453]
	""" Silas Darkmoon """
	pass
class TB_BaconShop_HP_101_Action(TargetedAction):
	TARGET = ActionArg()
	CARD = ActionArg()
	def do(self, source, target, card):
		controller = target
		if card.darkmoon_ticket:
			card.darkmoon_ticket=False
			source.sidequest_counter += 1 ## this is a counter.
			if source.sidequest_counter==3:
				source.sidequest_counter=0
				newcard=Give(controller, 'TB_BaconShop_HP_101t2').trigger(source)
				if newcard[0]!=[]:
					newcard[0][0].script_data_num_1=controller.tavern_tier
		pass
class TB_BaconShop_HP_101:
	"""  Come One, Come All!
	[Passive.] Darkmoon Tickets are in the Tavern! Get 3 to [Discover] a minion from your Tavern Tier."""
	### when reroling cards, put some of minions the enchantment below
	events = Buy(CONTROLLER).on(TB_BaconShop_HP_101_Action(CONTROLLER, Buy.CARD))
class TB_BaconShop_HP_101e:
	"""  """
class TB_BaconShop_HP_101t2:## discover card
	"""  """
	play = Discover(CONTROLLER, RandomBGAdmissible(tech_level=TIER(CONTROLLER)))
##### BUDDY
class TB_BaconShop_HERO_90_Buddy:# <12>[1453]
	""" Burth
	After you buy a minion with a Darkmoon Ticket, gain1_Gold this turn only. """
	pass
class TB_BaconShop_HERO_90_Buddy_G:# <12>[1453]
	""" Burth
	After you buy a minion witha Darkmoon Ticket, gain2_Gold this turn only. """
	pass




##Sindragosa  ### HP OK ###
BG_Hero4+=['TB_BaconShop_HERO_27','TB_BaconShop_HERO_27_Buddy','TB_BaconShop_HERO_27_Buddy_G','TB_BaconShop_HP_014','TB_BaconShop_HP_014e',]
BG_PoolSet_Hero4.append('TB_BaconShop_HERO_27')
BG_Hero4_Buddy['TB_BaconShop_HERO_27']='TB_BaconShop_HERO_27_Buddy'
BG_Hero4_Buddy_Gold['TB_BaconShop_HERO_27_Buddy']='TB_BaconShop_HERO_27_Buddy_G'
class TB_BaconShop_HERO_27:# <12>[1453]
	""" Sindragosa """
	pass
class TB_BaconShop_HP_014_Action(GameAction):
	def do(self, source):
		controller = source.controller
		bartender = controller.opponent
		for card in bartender.field:
			if card.frozen:
				Buff(card, 'TB_BaconShop_HP_014e').trigger(source)
		pass
class TB_BaconShop_HP_014:
	"""  
	[Freeze] a minion in Bob's Tavern. [Frozen] minions get +2/+1 each turn."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_ENEMY_TARGET:0, PlayReq.REQ_MINION_TARGET:0}
	activate = Freeze(TARGET)
	events = OWN_TURN_END.on(TB_BaconShop_HP_014_Action())
TB_BaconShop_HP_014e=buff(2,1)
######## BUDDY
class TB_BaconShop_HERO_27_Buddy:# <12>[1453]
	""" Thawed Champion
	At the end of your turn, adda random [Frozen] minionfrom Bob's Tavernto your hand. """
	pass
class TB_BaconShop_HERO_27_Buddy_G:# <12>[1453]
	""" Thawed Champion
	At the end of your turn, add2 random [Frozen] minionsfrom Bob's Tavernto your hand. """
	pass







##Sir Finley Mrrgglton     ### OK ###
BG_Hero4+=['TB_BaconShop_HERO_40','TB_BaconShop_HERO_40_Buddy','TB_BaconShop_HERO_40_Buddy_G','TB_BaconShop_HP_057',]
BG_PoolSet_Hero4.append('TB_BaconShop_HERO_40')
BG_Hero4_Buddy['TB_BaconShop_HERO_40']='TB_BaconShop_HERO_40_Buddy'
BG_Hero4_Buddy_Gold['TB_BaconShop_HERO_40_Buddy']='TB_BaconShop_HERO_40_Buddy_G'
class TB_BaconShop_HERO_40:# <12>[1453]
	""" Sir Finley Mrrgglton """
	pass
class TB_BaconShop_HP_057:
	"""  
	[Passive] At the start of the game, [Discover] a Hero Power."""
	entourage=['TB_BaconShop_HP_085','TB_BaconShop_HP_046','BG20_HERO_100p',]
	events = BeginGame(CONTROLLER).on(GenericChoiceChangeHeropower(CONTROLLER, RandomEntourage()*3))
######## BUDDY
class TB_BaconShop_HERO_40_Buddy:
	"""  """
class TB_BaconShop_HERO_40_Buddy_G:
	"""  """


### Sire Denathrius ### BG24_HERO_100 ### new 24.2 ####### banned 25?
##BG_Hero4+=['BG24_HERO_100','BG24_HERO_100p',]
##BG_PoolSet_Hero4.append('BG24_HERO_100')
#class BG24_HERO_100:
#	""" Sire Denathrius
#	"""
#class BG24_HERO_100p:
#	""" Whodunit?
#	[Passive.] At the start of the game, choose one of two [Quests]."""
#	pass


##Skycap'n Kragg     ### HP OK ###
BG_Hero4+=['TB_BaconShop_HERO_68','TB_BaconShop_HERO_68_Buddy','TB_BaconShop_HERO_68_Buddy_G','TB_BaconShop_HP_076',]
BG_PoolSet_Hero4.append('TB_BaconShop_HERO_68')
BG_Hero4_Buddy['TB_BaconShop_HERO_68']='TB_BaconShop_HERO_68_Buddy'
BG_Hero4_Buddy_Gold['TB_BaconShop_HERO_68_Buddy']='TB_BaconShop_HERO_68_Buddy_G'
class TB_BaconShop_HERO_68:# <12>[1453]
	""" Skycap'n Kragg """
	pass
class TB_BaconShop_HP_076_Action(GameAction):
	def do(self, source):
		controller = source.controller
		source.sidequest_counter+=1
		if source.sidequest_counter<=1:
			for repeat in range(min(source.script_data_num_1,10)):  
				#Give(controller, 'GAME_005').trigger(controller)
				ManaThisTurnOnly(CONTROLLER, 1).trigger(controller)
			SetAttr(source,'cant_play',True).trigger(controller)
		pass
class TB_BaconShop_HP_076:
	"""  
	Gain @ Gold this turn. Increases each turn. <i>(Once per game.)</i>"""
	activate = TB_BaconShop_HP_076_Action()
	events = OWN_TURN_END.on(AddScriptDataNum1(SELF,1))
	pass
######## BUDDY
class TB_BaconShop_HERO_68_Buddy:
	"""  """
	pass
class TB_BaconShop_HERO_68_Buddy_G:
	"""  """
	pass





##Sneed    ### OK ###
BG_Hero4+=['BG21_HERO_030','BG21_HERO_030_Buddy','BG21_HERO_030_Buddy_e','BG21_HERO_030_Buddy_G','BG21_HERO_030p','BG21_HERO_030pe',]
BG_PoolSet_Hero4.append('BG21_HERO_030')
BG_Hero4_Buddy['BG21_HERO_030']='BG21_HERO_030_Buddy'
BG_Hero4_Buddy_Gold['BG21_HERO_030_Buddy']='BG21_HERO_030_Buddy_G'
class BG21_HERO_030:# <10>[1453]
	""" Sneed """
	pass
class BG21_HERO_030p:# <12>[1453]
	""" Sneed's Replicator 24.0
	Give a minion: &quot;[Deathrattle:] Summon a random minion from a lower Tavern Tier.&quot; """ 
	#Give a friendly minion:"[Deathrattle]: Summon a random minion of the same Tavern Tier." """ <= 23.6
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, }
	activate = Buff(TARGET,'BG21_HERO_030pe')
	pass
class BG21_HERO_030pe:# <12>[1453]
	""" Replicate
	[Deathrattle]: Summon a random minion of the same Tavern Tier. """
	tags = {GameTag.DEATHRATTLE:True}
	#deathrattle = Summon(CONTROLLER, RandomBGAdmissible(tech_level=TECH_LEVEL(SELF)))#until 23.4.3
	deathrattle = Summon(CONTROLLER, RandomBGAdmissible(tech_level_plus1=TECH_LEVEL(SELF)))## after 23.6
	pass
######## BUDDY 
class BG21_HERO_030_Buddy_Action(TargetedAction):
	TARGET=ActionArg()
	BUFFCARD=ActionArg()
	AMOUNT=IntArg()
	def do(self,source,target,buffcard,amount):
		if target:
			additional=[]
			for d in target.deathrattle: ## may be a deepcopy?
				for repeat in amount:
					additional.append(d)
			Buff(source, buffcard, additional_deathrattles=additional).trigger(source)
class BG21_HERO_030_Buddy:# <12>[1453]
	""" Piloted Whirl-O-Tron
	[Battlecry:] Copy a friendly minion's [Deathrattles]. """
	requirements={PlayReq.REQ_TARGET_IF_AVAILABLE:0,  PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0,
			   PlayReq.REQ_TARGET_WITH_DEATHRATTLE:1}
	play = BG21_HERO_030_Buddy_Action(TARGET, 'BG21_HERO_030_Buddy_e',1) 
	pass
class BG21_HERO_030_Buddy_e:# <12>[1453]
	""" Whirling
	Copied [Deathrattles] from {0}. """
	tags={GameTag.DEATHRATTLE:True}
	pass
class BG21_HERO_030_Buddy_G:# <12>[1453]
	""" Piloted Whirl-O-Tron
	[Battlecry:] Copy a friendly minion's [Deathrattles] twice. """
	requirements={PlayReq.REQ_TARGET_IF_AVAILABLE:0,  PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0,
			   PlayReq.REQ_TARGET_WITH_DEATHRATTLE:1}
	play = BG21_HERO_030_Buddy_Action(TARGET, 'BG21_HERO_030_Buddy_e',2) 
	pass



##Sylvanas Windrunner    ### OK ### new 24.4
BG_Hero4+=['BG23_HERO_306','BG23_HERO_306p','BG23_HERO_306e','BG23_HERO_306_Buddy','BG23_HERO_306_Buddy_G']
BG_PoolSet_Hero4.append('BG23_HERO_306')
BG_Hero4_Buddy['BG23_HERO_306']='BG23_HERO_306_Buddy'
BG_Hero4_Buddy_Gold['BG23_HERO_306_Buddy']='BG23_HERO_306_Buddy_G'
class BG23_HERO_306:
	""" Sylvanas Windrunner """
	pass
class BG23_HERO_306p_Action0(GameAction):
	def do(self, source):
		controller = source.controller
		for card in controller.field:
			card.killed_in_former_battle=False
		pass
class BG23_HERO_306p_Action1(GameAction):
	def do(self, source):
		controller = source.controller
		for card in controller.field:
			if card.killed_in_former_battle:
				Buff(card, 'BG23_HERO_306e').trigger(source)
		pass
class BG23_HERO_306p_Action2(TargetedAction):
	ENTITY=ActionArg()
	def do(self, source, entity):## in actions.Death()
		if entity.controller.hero.power.id=='BG23_HERO_306p':
			if entity.game.this_is_battle and entity.deepcopy_original!=None:
				entity.deepcopy_original.killed_in_former_battle=True
	pass
class BG23_HERO_306p:
	""" Reclaimed Souls
	Give +2/+1 to your minions that died last combat."""
	activate = BG23_HERO_306p_Action1()
	events=[
		OWN_TURN_END.on(BG23_HERO_306p_Action0()),### no need, see BG_Battle.__init__()
		Death(FRIENDLY + MINION).on(BG23_HERO_306p_Action2(Death.ENTITY)) ## no need, see Death.do()
	]
	pass
BG23_HERO_306e=buff(2,1)
