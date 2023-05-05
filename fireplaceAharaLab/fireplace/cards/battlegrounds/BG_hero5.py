from ..utils import *

BG_Hero5=[]
BG_PoolSet_Hero5=[]
BG_Hero5_Buddy={}
BG_Hero5_Buddy_Gold={}

######## source #################################################################

##Tamsin Roame ### HP OK ###  BUDDY MAYBE ###
BG_Hero5+=['BG20_HERO_282','BG20_HERO_282p','BG20_HERO_282pe','BG20_HERO_282_Buddy','BG20_HERO_282_Buddye','BG20_HERO_282_Buddy_G',]
BG_PoolSet_Hero5.append('BG20_HERO_282')
BG_Hero5_Buddy['BG20_HERO_282']='BG20_HERO_282_Buddy'
BG_Hero5_Buddy_Gold['BG20_HERO_282_Buddy']='BG20_HERO_282_Buddy_G'
class BG20_HERO_282:# <9>[1453]
	""" Tamsin Roame """
	pass
class BG20_HERO_282p_Action(GameAction):
	def do(self, source):
		controller = source.controller
		lowesthealth=[]
		if len(controller.field)<2:
			return
		for card in controller.field:
			if lowesthealth==[]:
				lowesthealth=[card]
			elif card.max_health<lowesthealth[0].max_health:
				lowesthealth=[card]
			elif card.max_health==lowesthealth[0].max_health:
				lowesthealth.append(card)
		lowestcard = random.choice(lowesthealth)
		atk=lowestcard.atk
		health=lowestcard.max_health
		lowestcard.zone=Zone.GRAVEYARD
		if lowestcard in controller.field:
			controller.field.remove(lowestcard)
		if len(controller.field)>5: ## 23.4.3
			coleagues = random.sample(controller.field, 5) ## 23.4.3
		else:
			coleagues = controller.field
		for card in coleagues:
			Buff(card, 'BG20_HERO_282pe', atk=atk, max_health=health).trigger(source)
		pass
class BG20_HERO_282p:# <9>[1453]
	""" Fragrant Phylactery
	[Start of Combat:]Destroy your lowest Health minion. Give its stats_to five friendly minions. """
	events = BeginBattle(CONTROLLER).on(BG20_HERO_282p_Action())
	pass
class BG20_HERO_282pe:# <12>[1453]
	""" Fragrant
	Increased stats. """
	pass
######## BUDDY
class BG20_HERO_282_Buddy_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		atk=target.atk
		#hlt=target.max_health
		Buff(source, 'BG20_HERO_282_Buddye', atk=atk).trigger(source.controller)
class BG20_HERO_282_Buddy:# <12>[1453]
	""" Monstrosity
	After a friendly minion dies, gain its Attack. """
	events = Death(FRIENDLY + MINION).after(BG20_HERO_282_Buddy_Action(Death.ENTITY))
	pass
class BG20_HERO_282_Buddye:# <12>[1453]
	""" Consumed
	Increased Attack. """
class BG20_HERO_282_Buddy_G_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		atk=target.atk*2
		##hlt=target.max_health*2
		Buff(source, 'BG20_HERO_282_Buddye', atk=atk).trigger(source.controller)
class BG20_HERO_282_Buddy_G:# <12>[1453]
	""" Monstrosity
	After a friendly minion dies, gain its Attack twice. """
	events = Death(FRIENDLY + MINION).after(BG20_HERO_282_Buddy_G_Action(Death.ENTITY))
	pass





###Tavish Stormpike ### HP OK ### BUDDY OK  ###
BG_Hero5+=['BG22_HERO_000',
		'BG22_HERO_000p','BG22_HERO_000p_t1','BG22_HERO_000p_t2','BG22_HERO_000p_t3','BG22_HERO_000p_t4',
		'BG22_HERO_000_Buddy','BG22_HERO_000_Buddy_e','BG22_HERO_000_Buddy_G',]
BG_PoolSet_Hero5.append('BG22_HERO_000')
BG_Hero5_Buddy['BG22_HERO_000']='BG22_HERO_000_Buddy'
BG_Hero5_Buddy_Gold['BG22_HERO_000_Buddy']='BG22_HERO_000_Buddy_G'
class BG22_HERO_000:# <12>[1453]
	""" Tavish Stormpike """
	pass
class BG22_HERO_000p:# <12>[1453]
	""" Deadeye
	Take aim![Start of Combat]: Deal@ damage to your target.<i>(Upgrades each turn!)</i> """
	entourage=['BG22_HERO_000p_t1','BG22_HERO_000p_t2','BG22_HERO_000p_t3','BG22_HERO_000p_t4']
	activate = GenericChoice(CONTROLLER, RandomEntourage()*4)
	events = [
		BeginGame(CONTROLLER).on(SetScriptDataNum1(SELF,0)),
		BeginBar(CONTROLLER).on(AddScriptDataNum1(SELF,1))
		]
	pass
class  BG22_HERO_000p_t1_Action(GameAction):
	def do(self, source):
		controller=source.controller
		field=controller.opponent.field
		if len(field)==0:
			return
		targetcard=field[0]
		amount=source.script_data_num_1
		print("Aim Left! by Tavish Stormpike(%d damage to %s)"%(amount, targetcard))
		ActivateHit(targetcard, amount).trigger(source)
class BG22_HERO_000p_t1:# <12>[1453]
	""" Aim Left!
	[PassiveStart of Combat]: Deal@ damage to the left-most enemy minion. """
	events = [
		BeginBattle(CONTROLLER).on(BG22_HERO_000p_t1_Action()),
		BeginBar(CONTROLLER).on(AddScriptDataNum1(SELF,1),ChangeHeroPower(CONTROLLER, 'BG22_HERO_000p'))
		]
	pass
class  BG22_HERO_000p_t2_Action(GameAction):
	def do(self, source):
		controller=source.controller
		field=controller.opponent.field
		if len(field)==0:
			return
		targets=[]
		for card in field:
			if targets==[]:
				targets=[card]
			elif targets[0].max_health>card.max_health:
				targets=[card]
			elif targets[0].max_health==card.max_health:
				targets.append(card)
		targetcard = random.choice(targets)
		amount=source.script_data_num_1
		print("Aim Low! by Tavish Stormpike(%d damage to %s)"%(amount, targetcard))
		ActivateHit(targetcard, amount).trigger(source)
class BG22_HERO_000p_t2:# <12>[1453]
	""" Aim Low!
	[PassiveStart of Combat]: Deal@ damage to the lowest Health enemy minion. """
	events = [
		BeginBattle(CONTROLLER).on(BG22_HERO_000p_t2_Action()),
		BeginBar(CONTROLLER).on(AddScriptDataNum1(SELF,1),ChangeHeroPower(CONTROLLER, 'BG22_HERO_000p'))
		]
	pass
class  BG22_HERO_000p_t3_Action(GameAction):
	def do(self, source):
		controller=source.controller
		field=controller.opponent.field
		if len(field)==0:
			return
		targets=[]
		for card in field:
			if targets==[]:
				targets=[card]
			elif targets[0].max_health<card.max_health:
				targets=[card]
			elif targets[0].max_health==card.max_health:
				targets.append(card)
		targetcard = random.choice(targets)
		amount=source.script_data_num_1
		print("Aim High! by Tavish Stormpike(%d damage to %s)"%(amount, targetcard))
		ActivateHit(targetcard, amount).trigger(source)
class BG22_HERO_000p_t3:# <12>[1453]
	""" Aim High!
	[Passive Start of Combat]: Deal@ damage to the highestHealth enemy minion. """
	events = [
		BeginBattle(CONTROLLER).on(BG22_HERO_000p_t3_Action()),
		BeginBar(CONTROLLER).on(AddScriptDataNum1(SELF,1),ChangeHeroPower(CONTROLLER, 'BG22_HERO_000p'))
		]
	pass
class  BG22_HERO_000p_t4_Action(GameAction):
	def do(self, source):
		controller=source.controller
		field=controller.opponent.field
		if len(field)==0:
			return
		targetcard=field[-1]
		amount=source.script_data_num_1
		print("Aim Right! by Tavish Stormpike(%d damage to %s)"%(amount, targetcard))
		ActivateHit(targetcard, amount).trigger(source)
class BG22_HERO_000p_t4:# <12>[1453]
	""" Aim Right!
	[Passive Start of Combat]: Deal@ damage to the right-most enemy minion. """
	events = [
		BeginBattle(CONTROLLER).on(BG22_HERO_000p_t4_Action()),
		BeginBar(CONTROLLER).on(AddScriptDataNum1(SELF,1),ChangeHeroPower(CONTROLLER, 'BG22_HERO_000p'))
		]		
	pass
######## BUDDY
class BG22_HERO_000_Buddy_Action(TargetedAction):
	TARGET=ActionArg()
	AMOUNT=IntArg()
	def do(self, source, target, amount):
		index = source.controller.field.index(source)
		if index>0:
			Buff(source.controller.field[index-1], 'BG22_HERO_000_Buddy_e', atk=amount, max_health=amount).trigger(source)
		if index<len(source.controller.field)-1:
			Buff(source.controller.field[index+1], 'BG22_HERO_000_Buddy_e', atk=amount, max_health=amount).trigger(source)
class BG22_HERO_000_Buddy:# <12>[1453]
	""" Crabby
	After your Hero Power fires,give adjacent minions stats__equal to the damage dealt._ """
	events = ActivateHit(ENEMY + MINION).after(BG22_HERO_000_Buddy_Action(ActivateHit.TARGET, ActivateHit.AMOUNT))
	pass
class BG22_HERO_000_Buddy_e:# <12>[1453]
	""" Crabby
	Increased stats. """
	pass
class BG22_HERO_000_Buddy_G_Action(TargetedAction):
	TARGET=ActionArg()
	AMOUNT=IntArg()
	def do(self, source, target, amount):
		index = source.controller.field(source)
		if index>0:
			Buff(source.controller.field[index-1], 'BG22_HERO_000_Buddy_e', atk=amount*2, max_health=amount*2).trigger(source)
		if index<len(source.controller.field)-1:
			Buff(source.controller.field[index+1], 'BG22_HERO_000_Buddy_e', atk=amount*2, max_health=amount*2).trigger(source)
class BG22_HERO_000_Buddy_G:# <12>[1453]
	""" Crabby
	After your Hero Power fires, give adjacent minions stats equal to twice the damage dealt. """
	events = ActivateHit(ENEMY + MINION).after(BG22_HERO_000_Buddy_G_Action(ActivateHit.TARGET, ActivateHit.AMOUNT))
	pass



##Teron Gorefiend BG25_HERO_103 #### HP OK #### BUDDY OK ####
BG_Hero5+=['BG25_HERO_103','BG25_HERO_103p','BG25_HERO_103_Buddy','BG25_HERO_103_Buddye','BG25_HERO_103_Buddy_G','BG25_HERO_103_Buddy_Ge',]
BG_PoolSet_Hero5.append('BG25_HERO_103')
BG_Hero5_Buddy['BG25_HERO_103']='BG25_HERO_103_Buddy'
BG_Hero5_Buddy_Gold['BG25_HERO_103_Buddy']='TB_BaconShop_HERO_50_Buddy_G'
class BG25_HERO_103:
	""" Teron Gorefiend
	"""
class BG25_HERO_103p_Activate(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		target=get00(target)
		source.sidequest_list0.append(target.id)
		source.sidequest_counter=1
		pass
class BG25_HERO_103p_Action(GameAction):
	def do(self, source):
		if source.sidequest_counter==1 and len(source.sidequest_list0):
			targetID=source.sidequest_list0[0]
			cards = [cd for cd in source.controller.deepcopy_original.field if cd.id==targetID] 
			if len(cards):
				card=cards[0]
				Destroy(card).trigger(source)
				card.zone=Zone.SETASIDE
				if len(source.controller.field)<7:
					card.zone=Zone.PLAY
					source.controller.gorefiend_cardID=None
				else:
					source.controller.gorefiend_cardID=card.id
				source.sidequest_list0=[]
				source.sidequest_counter=0
class BG25_HERO_103p:
	""" Rapid Reanimation
	[x]Choose a friendly minion. [Start of Combat:] Destroy it. Once you have space, ___resummon an exact copy."""
	##### do we need 'activation'? when we determin the target?
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0}
	activate = BG25_HERO_103p_Activate(TARGET)
	events = BeginBattle(CONTROLLER).on(BG25_HERO_103p_Action())
###### Buddy ######
class BG25_HERO_103_Buddy_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		index = source.controller.field.index(target)
		if index>0:
			Buff(source.controller.field[index-1], buff).trigger(source)
		if index<len(source.controller.field)-1:
			Buff(source.controller.field[index+1], buff).trigger(source)
class BG25_HERO_103_Buddy:
	""" Shadowy Construct
	[x]After a friendly minion dies, give its neighbors +1/+1."""
	events = Death(FRIENDLY + MINION).on(BG25_HERO_103_Buddy_Action(Death.ENTITY, 'BG25_HERO_103_Buddye'))
BG25_HERO_103_Buddye=buff(1,1)
class BG25_HERO_103_Buddy_G:
	""" Shadowy Construct
	[x]After a friendly minion dies, give its neighbors +2/+2."""
	events = Death(FRIENDLY + MINION).on(BG25_HERO_103_Buddy_Action(Death.ENTITY, 'BG25_HERO_103_Buddy_Ge'))
BG25_HERO_103_Buddy_Ge=buff(2,2)



##Tess Greymane ### HP OK ###
BG_Hero5+=['TB_BaconShop_HERO_50','TB_BaconShop_HERO_50_Buddy','TB_BaconShop_HERO_50_Buddy_G','TB_BaconShop_HP_077',]
BG_PoolSet_Hero5.append('TB_BaconShop_HERO_50')
BG_Hero5_Buddy['TB_BaconShop_HERO_50']='TB_BaconShop_HERO_50_Buddy'
BG_Hero5_Buddy_Gold['TB_BaconShop_HERO_50_Buddy']='TB_BaconShop_HERO_50_Buddy_G'
class TB_BaconShop_HERO_50:# <12>[1453]
	""" Tess Greymane """
	pass
class TB_BaconShop_HP_077_Action(GameAction):
	def do(self, source):
		controller = source.controller
		gamemaster = controller.game.parent
		bartender = controller.opponent

		last_warband = gamemaster.last_warband(controller)
		for card in reversed(bartender.field):
			bartender.field.remove(card)
			card.zone=Zone.GRAVEYARD
		for cardid in last_warband:
			card = bartender.card(cardid)
			card.controller = bartender
			card.zone=Zone.PLAY
		if bartender.len_bobs_field-len(last_warband)>0:
			for repeat in range(bartender.len_bobs_field-len(last_warband)):
				card = gamemaster.DealCard(bartender, controller.tavern_tier)
		pass
class TB_BaconShop_HP_077:
	"""  
	[Refresh] Bob's Tavern with your last opponent's warband."""
	activate = TB_BaconShop_HP_077_Action()
	pass
######## BUDDY
class TB_BaconShop_HERO_50_Buddy_Action(GameAction):# <12>[1453]
	def do(self, source):
		controller = source.controller 
		my_bar = controller.game
		gamemaster = my_bar.parent
		last_matches = gamemaster.prevMatches
		for match in range(len(last_matches)):
			the_match = last_matches[match]
			if my_bar == gamemaster.BG_Bars[the_match[0]]:
				last_heroID = gamemaster.BG_Bars[the_match[1]].controller.hero.id
				last_hero_buddyID = gamemaster.BG_Hero_Buddy[last_heroID]
				Give(controller, last_hero_buddyID).trigger(source)
				break
			elif my_bar == gamemaster.BG_Bars[the_match[1]]:
				last_heroID = gamemaster.BG_Bars[the_match[0]].controller.hero.id
				last_hero_buddyID = gamemaster.BG_Hero_Buddy[last_heroID]
				Give(controller, last_hero_buddyID).trigger(source)
				break
		pass
class TB_BaconShop_HERO_50_Buddy:# <12>[1453]
	""" Hunter of Old
	At the start of your turn,add your last opponent's Buddy to your hand. """
	events = BeginBar(CONTROLLER).on(TB_BaconShop_HERO_50_Buddy_Action)
	pass
class TB_BaconShop_HERO_50_Buddy_G_Action(GameAction):# <12>[1453]
	def do(self, source):
		controller = source.controller 
		my_bar = controller.game
		gamemaster = my_bar.parent
		last_matches = gamemaster.prevMatches
		for match in range(len(last_matches)):
			the_match = last_matches[match]
			if my_bar == gamemaster.BG_Bars[the_match[0]]:
				last_heroID = gamemaster.BG_Bars[the_match[1]].controller.hero.id
				last_hero_buddyID = gamemaster.BG_Hero_Buddy[last_heroID]
				Give(controller, last_hero_buddyID).trigger(source)
				Give(controller, last_hero_buddyID).trigger(source)
				break
			elif my_bar == gamemaster.BG_Bars[the_match[1]]:
				last_heroID = gamemaster.BG_Bars[the_match[0]].controller.hero.id
				last_hero_buddyID = gamemaster.BG_Hero_Buddy[last_heroID]
				Give(controller, last_hero_buddyID).trigger(source)
				Give(controller, last_hero_buddyID).trigger(source)
				break
		pass
class TB_BaconShop_HERO_50_Buddy_G:# <12>[1453]
	""" Hunter of Old
	At the start of your turn, add 2 of your last opponent's Buddy to your hand. """
	events = BeginBar(CONTROLLER).on(TB_BaconShop_HERO_50_Buddy_G_Action())
	pass





##The Curator   ### HP OK ###
BG_Hero5+=['TB_BaconShop_HERO_33','TB_BaconShop_HERO_33_Buddy','TB_BaconShop_HERO_33_Buddy_e','TB_BaconShop_HERO_33_Buddy_G','TB_BaconShop_HP_033','TB_BaconShop_HP_033t',]
BG_PoolSet_Hero5.append('TB_BaconShop_HERO_33')
BG_Hero5_Buddy['TB_BaconShop_HERO_33']='TB_BaconShop_HERO_33_Buddy'
BG_Hero5_Buddy_Gold['TB_BaconShop_HERO_33_Buddy']='TB_BaconShop_HERO_33_Buddy_G'
class TB_BaconShop_HERO_33:# <12>[1453]
	""" The Curator	 """
	pass
class TB_BaconShop_HP_033:
	"""  
	[Passive] Start the game with a 2/2 Amalgam with all minion types."""
	events = BeginGame(CONTROLLER).on(Summon(CONTROLLER, 'TB_BaconShop_HP_033t'))
class TB_BaconShop_HP_033t:
	"""  2/2 Amalgam """
########  BUDDY
class TB_BaconShop_HERO_33_Buddy_Action(TargetedAction):# <12>[1453]
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		target=get00(target)
		if target.id=='TB_BaconShop_HP_033t':
			atk=buff.atk
			hlt=buff.max_health
			Buff(source, 'TB_BaconShop_HERO_33_Buddy_e', atk=atk, max_health=hlt).trigger(source)
class TB_BaconShop_HERO_33_Buddy:# <12>[1453]
	"""  Mishmash
	Whenever your Amalgam gains stats, this gains them too."""
	events = Buff(FRIENDLY + MINION).on(TB_BaconShop_HERO_33_Buddy_Action(Buff.TARGET, Buff.BUFF))
class TB_BaconShop_HERO_33_Buddy_e:# <12>[1453]
	""" Amalfam
	Increased stats. """
	#
	pass
class TB_BaconShop_HERO_33_Buddy_G_Action(TargetedAction):# <12>[1453]
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		target=get00(target)
		if target.id=='TB_BaconShop_HP_033t':
			atk=buff.atk*2
			hlt=buff.max_health*2
			Buff(source, 'TB_BaconShop_HERO_33_Buddy_e', atk=atk, max_health=hlt).trigger(source)
class TB_BaconShop_HERO_33_Buddy_G:# <12>[1453]
	"""  Mishmash
	Whenever your Amalgam gains stats, this gains them twice."""
	events = Buff(FRIENDLY + MINION).on(TB_BaconShop_HERO_33_Buddy_G_Action(Buff.TARGET, Buff.BUFF))




##The Great Akazamzarak  ### OK ###
BG_Hero5+=['TB_BaconShop_HERO_21','TB_BaconShop_HERO_21_Buddy','TB_BaconShop_HERO_21_Buddy_G','TB_BaconShop_HP_020',]
BG_PoolSet_Hero5.append('TB_BaconShop_HERO_21')
BG_Hero5_Buddy['TB_BaconShop_HERO_21']='TB_BaconShop_HERO_21_Buddy'
BG_Hero5_Buddy_Gold['TB_BaconShop_HERO_21_Buddy']='TB_BaconShop_HERO_21_Buddy_G'
class TB_BaconShop_HERO_21:# <12>[1453]
	""" The Great Akazamzarak """
	pass
class TB_BaconShop_HP_020:
	"""  [Discover] a [Secret]. Put it into the battlefield."""
	entourage=[
		'TB_Bacon_Secrets_01','TB_Bacon_Secrets_02','TB_Bacon_Secrets_04',
		'TB_Bacon_Secrets_05','TB_Bacon_Secrets_07','TB_Bacon_Secrets_08',
			#'TB_Bacon_Secrets_10',#'TB_Bacon_Secrets_11','TB_Bacon_Secrets_12',
			#'TB_Bacon_Secrets_13',
		]
	activate=GenericChoiceSecret(CONTROLLER, RandomEntourage()*3)
########  BUDDY
class TB_BaconShop_HERO_21_Buddy:# <12>[1453]
	""" Street Magician
	[Deathrattle:] Put a random [Secret] into the battlefield. """
	entourage=[
		'TB_Bacon_Secrets_01','TB_Bacon_Secrets_02','TB_Bacon_Secrets_04',
		'TB_Bacon_Secrets_05','TB_Bacon_Secrets_07','TB_Bacon_Secrets_08',]	
	deathrattle = CastSecret(CONTROLLER, RandomID(*entourage))
	pass
class TB_BaconShop_HERO_21_Buddy_G:# <12>[1453]
	""" Street Magician
	[Deathrattle:] Put 2 random[Secrets] into the battlefield. """
	entourage=[
		'TB_Bacon_Secrets_01','TB_Bacon_Secrets_02','TB_Bacon_Secrets_04',
		'TB_Bacon_Secrets_05','TB_Bacon_Secrets_07','TB_Bacon_Secrets_08',]	
	deathrattle = CastSecret(CONTROLLER, RandomID(*entourage))*2
	pass


##The Jailer TB_BaconShop_HERO_702 ## new 24.6 ### OK ###
BG_Hero5+=['TB_BaconShop_HERO_702','TB_BaconShop_HP_702','TB_BaconShop_HERO_702_Buddy','TB_BaconShop_HERO_22_Buddy_G']
BG_PoolSet_Hero5.append('TB_BaconShop_HERO_702')
BG_Hero5_Buddy['TB_BaconShop_HERO_702']='TB_BaconShop_HERO_702_Buddy'
BG_Hero5_Buddy_Gold['TB_BaconShop_HERO_22_Buddy']='TB_BaconShop_HERO_22_Buddy_G'
class TB_BaconShop_HERO_702:
	""" The Jailer """
class TB_BaconShop_HP_702_Action1(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		#controller=source.controller
		amount = source.script_data_num_1
		if Config.LOGINFO:
			Config.log("TB_BaconShop_HP_702_Action1.do","Buff %d/%d on %r"%(amount, amount, target))
		source.script_data_num_1 += 1
		source.script_data_text_0 = str(source.script_data_num_1)
		source.script_data_text_1 = str(source.script_data_num_2)
		Buff(target, 'TB_BaconShop_HP_702e', atk=amount, max_health=amount).trigger(source)
		source.cant_play=True
		pass
class TB_BaconShop_HP_702_Action2(TargetedAction):
	PLAYER=ActionArg()
	def do(self, source, player):
		controller=player
		amount = 9
		if Config.LOGINFO:
			Config.log("TB_BaconShop_HP_702_Action2.do","Setting Counter on %r -> %i"%(source, (source.sidequest_counter+1)))
		if source.game.this_is_battle:
			original_source=source.deepcopy_original
			if original_source!=None and original_source.cant_play==True:
				original_source.sidequest_counter += 1
				original_source.script_data_num_2 = amount - original_source.sidequest_counter
				original_source.script_data_text_1 = str(original_source.script_data_num_2)
				if original_source.sidequest_counter== amount:
					original_source.sidequest_counter = 0
					original_source.script_data_num_2 = amount
					original_source.cant_play=False
		pass
class TB_BaconShop_HP_702:
	""" Runic Empowerment
	Give a minion +{0}/+{0}. Upgrades after nine  friendly minions die.  &lt;i&gt;({1} left!)&lt;/i&gt;"""
	#<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="1"/>
	#<Tag enumID="3" name="TAG_SCRIPT_DATA_NUM_2" type="Int" value="9"/>
	#<Tag enumID="48" name="COST" type="Int" value="1"/>
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	activate = TB_BaconShop_HP_702_Action1(TARGET)
	events = Death(FRIENDLY + MINION).on(TB_BaconShop_HP_702_Action2(CONTROLLER))
@custom_card
class TB_BaconShop_HP_702e:
	tags = {
		GameTag.CARDNAME: "Runic Empowerment",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
	}
	pass
###### buddy ######
class TB_BaconShop_HERO_702_Buddy:
	""" Mawsworn Soulkeeper
	&lt;b&gt;Deathrattle:&lt;/b&gt; Summon 3 random Tier 1 minions."""
	deathrattle = Summon(CONTROLLER, RandomBGMinion(tech_level=3))
class TB_BaconShop_HERO_702_Buddy_G:
	""" Mawsworn Soulkeeper
	&lt;b&gt;Deathrattle:&lt;/b&gt; Summon 6 random Tier 1 minions."""
	deathrattle = Summon(CONTROLLER, RandomBGMinion(tech_level=6))
	pass




##The Lich King  ### HP OK ###
BG_Hero5+=['TB_BaconShop_HERO_22','TB_BaconShop_HERO_22_Buddy','TB_BaconShop_HERO_22_Buddy_G','TB_BaconShop_HP_024','TB_BaconShop_HP_024e2',]
BG_PoolSet_Hero5.append('TB_BaconShop_HERO_22')
BG_Hero5_Buddy['TB_BaconShop_HERO_22']='TB_BaconShop_HERO_22_Buddy'
BG_Hero5_Buddy_Gold['TB_BaconShop_HERO_22_Buddy']='TB_BaconShop_HERO_22_Buddy_G'
class TB_BaconShop_HERO_22:# <12>[1453]
	""" The Lich King """
	pass
class TB_BaconShop_HP_024:
	"""  
	Give a friendly minion [Reborn] until next turn."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0}
	activate = Buff(TARGET, 'TB_BaconShop_HP_024e2')
class TB_BaconShop_HP_024e2:
	tags={GameTag.REBORN:True,}
	events=BeginBar(CONTROLLER).on(Destroy(SELF))
########  BUDDY
class TB_BaconShop_HERO_22_Buddy_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		atk=target.atk
		Buff(source, 'TB_BaconShop_HERO_22_Buddye', atk=atk).trigger(source)
class TB_BaconShop_HERO_22_Buddy:
	""" Arfus 
	After a friendly minion is &lt;b&gt;Reborn&lt;/b&gt;, give it this minion's Attack."""
	events = Reborn(FRIENDLY + MINION).on(TB_BaconShop_HERO_22_Buddy_Action(Reborn.TARGET))
class TB_BaconShop_HERO_22_Buddye:
	pass
class TB_BaconShop_HERO_22_Buddy_G_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		atk=target.atk*2
		Buff(source, 'TB_BaconShop_HERO_22_Buddye', atk=atk).trigger(source)
class TB_BaconShop_HERO_22_Buddy_G:
	""" Arfus 
	After a friendly minion is &lt;b&gt;Reborn&lt;/b&gt;, give it this minion's Attack twice."""
	events = Reborn(FRIENDLY + MINION).on(TB_BaconShop_HERO_22_Buddy_G_Action(Reborn.TARGET))




##The Rat King ##   ### OK ###
BG_Hero5+=[
	'TB_BaconShop_HERO_12',
	'TB_BaconShop_HP_041','TB_BaconShop_HP_041a','TB_BaconShop_HP_041b','TB_BaconShop_HP_041c','TB_BaconShop_HP_041d','TB_BaconShop_HP_041e','TB_BaconShop_HP_041f','TB_BaconShop_HP_041g','TB_BaconShop_HP_041h','TB_BaconShop_HP_041i','TB_BaconShop_HP_041j','TB_BaconShop_HP_041k',
	'TB_BaconShop_HERO_12_Buddy','TB_BaconShop_HERO_12_Buddy_G',
	]
BG_PoolSet_Hero5.append('TB_BaconShop_HERO_12')
BG_Hero5_Buddy['TB_BaconShop_HERO_12']='TB_BaconShop_HERO_12_Buddy'
BG_Hero5_Buddy_Gold['TB_BaconShop_HERO_12_Buddy']='TB_BaconShop_HERO_12_Buddy_G'
class TB_BaconShop_HERO_12:# <12>[1453]
	""" The Rat King """
	pass
class TB_BaconShop_HP_041_Action(GameAction):
	def do(self, source):
		controller = source.controller
		races = controller.game.parent.BG_races
		choices=[]
		if 'beast' in races:
			choices.append('TB_BaconShop_HP_041a')
		if 'demon' in races:
			choices.append('TB_BaconShop_HP_041d')
		if 'dragon' in races:
			choices.append('TB_BaconShop_HP_041f')
		if 'elemental' in races:
			choices.append('TB_BaconShop_HP_041h')
		if 'mecha' in races:
			choices.append('TB_BaconShop_HP_041b')
		if 'murloc' in races:
			choices.append('TB_BaconShop_HP_041c')
		if 'naga' in races:
			choices.append('TB_BaconShop_HP_041j')
		if 'pirate' in races:
			choices.append('TB_BaconShop_HP_041g')
		if 'quilboar' in races:
			choices.append('TB_BaconShop_HP_041i')
		if 'undead' in races:
			choices.append('TB_BaconShop_HP_041k')
		new_hp=random.choice(choices)
		ChangeHeroPower(controller, new_hp).trigger(source)
		pass
class TB_BaconShop_HP_041:
	"""  
	&lt;b&gt;Discover&lt;/b&gt; a minion of a specific minion type. Swaps type each turn."""
	###[Passive] Whenever you buy a minion of a specific type, give it +2/+2. Swaps type each turn.
	events = BeginBar(CONTROLLER).on(TB_BaconShop_HP_041_Action())
	pass	
class TB_BaconShop_HP_041a:
	""" beast """
	activate = Discover(CONTROLLER, RandomBGBeast(tech_level_less=TIER(CONTROLLER)))
	events = [
		#Buy(CONTROLLER, BEAST).on(Buff(Buy.CARD,'TB_BaconShop_HP_041e')),
		BeginBar(CONTROLLER).on(TB_BaconShop_HP_041_Action())
		]
class TB_BaconShop_HP_041b:
	""" mech """
	activate = Discover(CONTROLLER, RandomBGMecha(tech_level_less=TIER(CONTROLLER)))
	events = [
		#Buy(CONTROLLER, MECH).on(Buff(Buy.CARD,'TB_BaconShop_HP_041e')),
		BeginBar(CONTROLLER).on(TB_BaconShop_HP_041_Action())
		]
class TB_BaconShop_HP_041c:
	""" murloc """
	activate = Discover(CONTROLLER, RandomBGMurloc(tech_level_less=TIER(CONTROLLER)))
	events = [
		#Buy(CONTROLLER, MURLOC).on(Buff(Buy.CARD,'TB_BaconShop_HP_041e')),
		BeginBar(CONTROLLER).on(TB_BaconShop_HP_041_Action())
		]
class TB_BaconShop_HP_041d:
	""" demon """
	activate = Discover(CONTROLLER, RandomBGDemon(tech_level_less=TIER(CONTROLLER)))
	events = [
		#Buy(CONTROLLER, DEMON).on(Buff(Buy.CARD,'TB_BaconShop_HP_041e')),
		BeginBar(CONTROLLER).on(TB_BaconShop_HP_041_Action())
		]
TB_BaconShop_HP_041e=buff(2,2)
class TB_BaconShop_HP_041f:
	""" dragon """
	activate = Discover(CONTROLLER, RandomBGDragon(tech_level_less=TIER(CONTROLLER)))
	events = [
		#Buy(CONTROLLER, DRAGON).on(Buff(Buy.CARD,'TB_BaconShop_HP_041e')),
		BeginBar(CONTROLLER).on(TB_BaconShop_HP_041_Action())
		]
class TB_BaconShop_HP_041g:
	""" pirate """
	activate = Discover(CONTROLLER, RandomBGPirate(tech_level_less=TIER(CONTROLLER)))
	events = [
		#Buy(CONTROLLER, PIRATE).on(Buff(Buy.CARD,'TB_BaconShop_HP_041e')),
		BeginBar(CONTROLLER).on(TB_BaconShop_HP_041_Action())
		]
class TB_BaconShop_HP_041h:
	""" elemental """
	activate = Discover(CONTROLLER, RandomBGElemental(tech_level_less=TIER(CONTROLLER)))
	events = [
		#Buy(CONTROLLER, ELEMENTAL).on(Buff(Buy.CARD,'TB_BaconShop_HP_041e')),
		BeginBar(CONTROLLER).on(TB_BaconShop_HP_041_Action())
		]
class TB_BaconShop_HP_041i:
	""" quilboar """
	activate = Discover(CONTROLLER, RandomBGQuilboar(tech_level_less=TIER(CONTROLLER)))
	events = [
		#Buy(CONTROLLER, QUILBOAR).on(Buff(Buy.CARD,'TB_BaconShop_HP_041e')),
		BeginBar(CONTROLLER).on(TB_BaconShop_HP_041_Action())
		]
class TB_BaconShop_HP_041j:
	""" naga """
	activate = Discover(CONTROLLER, RandomBGNaga(tech_level_less=TIER(CONTROLLER)))
	events = [
		#Buy(CONTROLLER, NAGA).on(Buff(Buy.CARD,'TB_BaconShop_HP_041e')),
		BeginBar(CONTROLLER).on(TB_BaconShop_HP_041_Action())
		]
class TB_BaconShop_HP_041k:
	""" undead """
	activate = Discover(CONTROLLER, RandomBGUndead(tech_level_less=TIER(CONTROLLER)))
	events = [
		#Buy(CONTROLLER, UNDEAD).on(Buff(Buy.CARD,'TB_BaconShop_HP_041e')),
		BeginBar(CONTROLLER).on(TB_BaconShop_HP_041_Action())
		]
######## BUDDY
class TB_BaconShop_HERO_12_Buddy_Action(GameAction):
	def do(self, source):
		heropowerID=source.controller.hero.power.id
		if heropowerID=='TB_BaconShop_HP_041a':
			cards=[card for card in source.controller.opponent.field if card.race==Race.BEAST]
		elif heropowerID=='TB_BaconShop_HP_041b':
			cards=[card for card in source.controller.opponent.field if card.race==Race.MECHANICAL]
		elif heropowerID=='TB_BaconShop_HP_041c':
			cards=[card for card in source.controller.opponent.field if card.race==Race.MURLOC]
		elif heropowerID=='TB_BaconShop_HP_041d':
			cards=[card for card in source.controller.opponent.field if card.race==Race.DEMON]
		elif heropowerID=='TB_BaconShop_HP_041e':
			cards=[card for card in source.controller.opponent.field if card.race==Race.DRAGON]
		elif heropowerID=='TB_BaconShop_HP_041f':
			cards=[card for card in source.controller.opponent.field if card.race==Race.PIRATE]
		elif heropowerID=='TB_BaconShop_HP_041g':
			cards=[card for card in source.controller.opponent.field if card.race==Race.ELEMENTAL]
		elif heropowerID=='TB_BaconShop_HP_041h':
			cards=[card for card in source.controller.opponent.field if card.race==Race.QUILBOAR]
		elif heropowerID=='TB_BaconShop_HP_041i':
			cards=[card for card in source.controller.opponent.field if card.race==Race.NAGA]
		elif heropowerID=='TB_BaconShop_HP_041j':
			cards=[card for card in source.controller.opponent.field if card.race==Race.UNDEAD]
		if len(cards)==0:
			source.controller.game.free_rerole = 1
			source.controller.game.reroleCost = 0
		else:
			source.controller.game.free_rerole = 0
			source.controller.game.reroleCost = 1
		pass
class TB_BaconShop_HERO_12_Buddy:# <12>[1453]
	""" Pigeon Lord
	Your [Refreshes] cost (0) while Bob's Tavern doesn't have the minion type of your Hero Power. """
	events = Rerole(CONTROLLER).after(TB_BaconShop_HERO_12_Buddy_Action())
	pass
class TB_BaconShop_HERO_12_Buddy_G:# <12>[1453]
	""" Pigeon Lord
	Your [Refreshes] cost (0) while Bob's Tavern doesn't have the minion type of your Hero Power. """
	events = Rerole(CONTROLLER).after(TB_BaconShop_HERO_12_Buddy_Action())
	#
	pass




##Tickatus   ### HP OK ###
BG_Hero5+=['TB_BaconShop_HERO_94','TB_BaconShop_HP_106','TB_BaconShop_HERO_94_Buddy','TB_BaconShop_HERO_94_Buddy_G',]#
BG_PoolSet_Hero5.append('TB_BaconShop_HERO_94')
BG_Hero5_Buddy['TB_BaconShop_HERO_94']='TB_BaconShop_HERO_94_Buddy'
BG_Hero5_Buddy_Gold['TB_BaconShop_HERO_94_Buddy']='TB_BaconShop_HERO_94_Buddy_G'
class TB_BaconShop_HERO_94:# <12>[1453]
	""" Tickatus """
class TB_BaconShop_HP_106_Action(GameAction):
	def do(self, source):
		controller=source.controller
		darkmoon_ticket4=['BGS_Treasures_004','BGS_Treasures_006','BGS_Treasures_007','BGS_Treasures_012','BGS_Treasures_015','BGS_Treasures_018',]#1 #BGS_Treasures_032
		darkmoon_ticket8=['BGS_Treasures_001','BGS_Treasures_010','BGS_Treasures_013','BGS_Treasures_016','BGS_Treasures_019','BGS_Treasures_022','BGS_Treasures_023','BGS_Treasures_025','BGS_Treasures_026','BGS_Treasures_029',]#2 ## 'BGS_Treasures_011',
		darkmoon_ticket12=['BGS_Treasures_000','BGS_Treasures_009','BGS_Treasures_014','BGS_Treasures_020','BGS_Treasures_028','BGS_Treasures_030','BGS_Treasures_033','BGS_Treasures_036','BGS_Treasures_037','BGS_Treasures_040']#3
		source.script_data_num_1 = (103-controller.game.turn)%4+1
		if controller.game.turn==4:
			Discover(controller, RandomID(*darkmoon_ticket4)).trigger(source)
		elif controller.game.turn==8:
			Discover(controller, RandomID(*darkmoon_ticket8)).trigger(source)
		elif controller.game.turn%4==0:
			Discover(controller, RandomID(*darkmoon_ticket12)).trigger(source)
		pass
class TB_BaconShop_HP_106:
	""" Prize Wall 
	[Passive] Every 4 turns, [Discover] a Darkmoon Prize. <i>(@ |4(turn, turns) left!)</i>"""
	events = BeginBar(CONTROLLER).on(TB_BaconShop_HP_106_Action())
	pass
## darkmoon prize -> BGS_Treasures_000 ~ BGS_Treasures_037
###### BUDDY #######
class TB_BaconShop_HERO_94_Buddy_Action(GameAction):# <12>[1453]
	def do(self, source):
		darkmoon_ticket4=['BGS_Treasures_004','BGS_Treasures_006','BGS_Treasures_007','BGS_Treasures_012','BGS_Treasures_015','BGS_Treasures_018',]#1 #BGS_Treasures_032
		darkmoon_ticket8=['BGS_Treasures_001','BGS_Treasures_010','BGS_Treasures_013','BGS_Treasures_016','BGS_Treasures_019','BGS_Treasures_022','BGS_Treasures_023','BGS_Treasures_025','BGS_Treasures_026','BGS_Treasures_029',]#2 ## 'BGS_Treasures_011',
		darkmoon_ticket12=['BGS_Treasures_000','BGS_Treasures_009','BGS_Treasures_014','BGS_Treasures_020','BGS_Treasures_028','BGS_Treasures_030','BGS_Treasures_033','BGS_Treasures_036','BGS_Treasures_037','BGS_Treasures_040']#3
		if source.controller.game.turn<4:
			Discover(source.controller, RandomID(*darkmoon_ticket4)).trigger(source)
		elif source.controller.game.turn<8:
			Discover(source.controller, RandomID(*darkmoon_ticket8)).trigger(source)
		else:
			Discover(source.controller, RandomID(*darkmoon_ticket12)).trigger(source)
		pass
class TB_BaconShop_HERO_94_Buddy:# <12>[1453]
	""" Ticket Collector
	[Battlecry:] [Discover] a Darkmoon Prize fromthe next Prize turn. """
	play = TB_BaconShop_HERO_94_Buddy_Action()
	pass
class TB_BaconShop_HERO_94_Buddy_G_Choice(Choice):# <12>[1453]
	def choose(self, card):
		self.source.sidequest_counter += 1
		if self.source.sidequest_counter>=2:
			self.next_choice=None
		else:
			self.next_choice=self
		super().choose(card)
		card.zone=Zone.HAND
class TB_BaconShop_HERO_94_Buddy_G_Action(GameAction):# <12>[1453]
	def do(self, source):
		darkmoon_ticket4=['BGS_Treasures_004','BGS_Treasures_006','BGS_Treasures_007','BGS_Treasures_012','BGS_Treasures_015','BGS_Treasures_018',]#1 #BGS_Treasures_032
		darkmoon_ticket8=['BGS_Treasures_001','BGS_Treasures_010','BGS_Treasures_013','BGS_Treasures_016','BGS_Treasures_019','BGS_Treasures_022','BGS_Treasures_023','BGS_Treasures_025','BGS_Treasures_026','BGS_Treasures_029',]#2 ## 'BGS_Treasures_011',
		darkmoon_ticket12=['BGS_Treasures_000','BGS_Treasures_009','BGS_Treasures_014','BGS_Treasures_020','BGS_Treasures_028','BGS_Treasures_030','BGS_Treasures_033','BGS_Treasures_036','BGS_Treasures_037','BGS_Treasures_040']#3
		if source.controller.game.turn<4:
			TB_BaconShop_HERO_94_Buddy_G_Choice(source.controller, RandomID(*darkmoon_ticket4)*3).trigger(source)
		elif source.controller.game.turn<8:
			TB_BaconShop_HERO_94_Buddy_G_Choice(source.controller, RandomID(*darkmoon_ticket8)*3).trigger(source)
		else:
			TB_BaconShop_HERO_94_Buddy_G_Choice(source.controller, RandomID(*darkmoon_ticket12)*3).trigger(source)
		pass
class TB_BaconShop_HERO_94_Buddy_G:# <12>[1453]
	""" Ticket Collector
	[Battlecry:] [Discover] 2 Darkmoon Prizes from the next Prize turn. """
	play = TB_BaconShop_HERO_94_Buddy_G_Action()
	pass





##Trade Prince Gallywix  ### HP OK ###
BG_Hero5+=['TB_BaconShop_HERO_10','TB_BaconShop_HP_008','TB_BaconShop_HP_008a','TB_BaconShop_HERO_10_Buddy','TB_BaconShop_HERO_10_Buddye','TB_BaconShop_HERO_10_Buddy_G',]#
BG_PoolSet_Hero5.append('TB_BaconShop_HERO_10')
BG_Hero5_Buddy['TB_BaconShop_HERO_10']='TB_BaconShop_HERO_10_Buddy'
BG_Hero5_Buddy_Gold['TB_BaconShop_HERO_10_Buddy']='TB_BaconShop_HERO_10_Buddy_G'
class TB_BaconShop_HERO_10:# <12>[1453]
	""" Trade Prince Gallywix """
class TB_BaconShop_HP_008:
	""" 
	[Passive] After you sell a minion, get 1 extra Gold next turn. <i>(Can exceed 10.)</i>"""
	### proceed in BG_main
	pass
class TB_BaconShop_HP_008a:
	""" """
###### buddy ######
class TB_BaconShop_HERO_10_Buddy_Action(TargetedAction):# <12>[1453]
	TARGET=ActionArg()
	def do(self, source, target):
		amount = max(source.controller.total_used_mana_this_turn,0)
		Buff(target, 'TB_BaconShop_HERO_10_Buddye', atk=amount, max_health=amount).trigger(source)
class TB_BaconShop_HERO_10_Buddy:# <12>[1453]
	""" Bilgewater Mogul
	[Battlecry:] Give a minion +1/+1 for each Gold spent this turn. """
	reuqirements = { PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0 }
	play = TB_BaconShop_HERO_10_Buddy_Action(TARGET)
	pass
class TB_BaconShop_HERO_10_Buddye:# <12>[1453]
	""" Brutal Luxury 	Increased stats. """
	pass
class TB_BaconShop_HERO_10_Buddy_G_Action(TargetedAction):# <12>[1453]
	TARGET=ActionArg()
	def do(self, source, target):
		amount = max(source.controller.total_used_mana_this_turn,0) * 2
		Buff(target, 'TB_BaconShop_HERO_10_Buddye', atk=amount, max_health=amount).trigger(source)
class TB_BaconShop_HERO_10_Buddy_G:# <12>[1453]
	""" Bilgewater Mogul
	[Battlecry:] Give a minion +2/+2 for each Gold spent this turn. """
	reuqirements = { PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0 }
	play = TB_BaconShop_HERO_10_Buddy_G_Action(TARGET)
	pass




##Vanndar Stormpike   ## HP OK ## BUDDY OK ##
BG_Hero5+=['BG22_HERO_003','BG22_HERO_003p','BG22_HERO_003pe','BG22_HERO_003pe2','BG22_HERO_003pe3','BG22_HERO_003_Buddy','BG22_HERO_003_Buddy_e','BG22_HERO_003_Buddy_G','BG22_HERO_003_Buddy_Ge',]#
BG_PoolSet_Hero5.append('BG22_HERO_003')
BG_Hero5_Buddy['BG22_HERO_003']='BG22_HERO_003_Buddy'
BG_Hero5_Buddy_Gold['BG22_HERO_003_Buddy']='BG22_HERO_003_Buddy_G'
class BG22_HERO_003:# <12>[1453]
	""" Vanndar Stormpike """
class BG22_HERO_003p:# <12>[1453]
	""" Lead the Stormpikes
	[Passive] [Avenge (2):] Give your minions +1 Health permanently.""" ## new 24.2
	events = Death(FRIENDLY + MINION).on(Avenge(SELF, 2, [BuffPermanently(FRIENDLY_MINIONS, 'BG22_HERO_003pe')]))
	#Choose a friendly minion.It copies the Health of your highest Health minion for next combat only. ### old 
	#requirements = { 
	#	PlayReq.REQ_TARGET_TO_PLAY:0, 
	#	#PlayReq.REQ_FRIENDLY_TARGET:0, ## was valid until 23.4.3 
	#	PlayReq.REQ_MINION_TARGET:0, 
	#	1001:2 }
	#activate = Buff(TARGET,'BG22_HERO_003pe3' )
	pass
BG22_HERO_003pe=buff(0,1)
#class BG22_HERO_003pe:# <12>[1453]
#	""" Stormpike Strength
#	Copied highest Health. """
#	events = EndBattle(CONTROLLER).on(Destroy(SELF))
#	pass
class BG22_HERO_003pe2:# <12>[1453]
	""" Health Set Next Combat Only
	 """
	pass
class BG22_HERO_003p_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source,target):
		controller = source.controller
		highest_health=0
		for card in controller.field:
			if highest_health<card.max_health:
				highest_health=card.max_health
		Buff(target, 'BG22_HERO_003pe', max_health = highest_health - target.max_health).trigger(source)
class BG22_HERO_003pe3:# <12>[1453]
	""" Modified Health Next Combat Only
	Health is increased or decreased for next combat only. """
	events = [
		EndTurn(CONTROLLER).on(BG22_HERO_003p_Action(OWNER)),
		EndBattle(CONTROLLER).on(Destroy(SELF))
		]
	pass
###### BUDDY ######
class BG22_HERO_003_Buddy_Action(GameAction):# <12>[1453]
	def do(self, source):
		if getattr(source.controller, 'deepcopy_original', None)!=None:
			source.controller.deepcopy_original.stormpike_powered_up += 1
class BG22_HERO_003_Buddy:# <12>[1453]
	""" Stormpike Lieutenant
	&lt;b&gt;Avenge (2):&lt;/b&gt; Minions in Bob's Tavern have +1 Health for the rest of the game."""
	### [Avenge (2):] Give your minions +1 Health permanently. 
	###events = Death(FRIENDLY + MINION).on(Avenge(SELF, 2, [BuffPermanently(FRIENDLY_MINIONS, 'BG22_HERO_003_Buddy_e')]))
	events = Death(FRIENDLY + MINION).on(Avenge(SELF, 2, [BG22_HERO_003_Buddy_Action()]))
	pass
class BG22_HERO_003_Buddy_e:# <12>[1453]
	pass
class BG22_HERO_003_Buddy_G_Action(GameAction):# <12>[1453]
	def do(self, source):
		if getattr(source.controller, 'deepcopy_original', None)!=None:
			source.controller.deepcopy_original.stormpike_powered_up += 2
class BG22_HERO_003_Buddy_G:# <12>[1453]
	""" Stormpike Lieutenant
	&lt;b&gt;Avenge (2):&lt;/b&gt; Minions in Bob's Tavern have +2 Health for the rest of the game."""
	###[Avenge (2):] Give your minions +2 Health permanently. """
	###events = Death(FRIENDLY + MINION).on(Avenge(SELF, 2, [BuffPermanently(FRIENDLY_MINIONS, 'BG22_HERO_003_Buddy_Ge')]))
	events = Death(FRIENDLY + MINION).on(Avenge(SELF, 2, [BG22_HERO_003_Buddy_G_Action()]))
	pass
BG22_HERO_003_Buddy_Ge=buff(0,2)# <12>[1453]





##Varden Dawngrasp ## HP OK ## BUDDY OK ###
BG_Hero5+=['BG22_HERO_004','BG22_HERO_004p','BG22_HERO_004_Buddy','BG22_HERO_004_Buddy_e2','BG22_HERO_004_Buddy_G',]#
BG_PoolSet_Hero5.append('BG22_HERO_004')
BG_Hero5_Buddy['BG22_HERO_004']='BG22_HERO_004_Buddy'
BG_Hero5_Buddy_Gold['BG22_HERO_004_Buddy']='BG22_HERO_004_Buddy_G'
class BG22_HERO_004:# <4>[1453]
	""" Varden Dawngrasp """
class BG22_HERO_004p_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = source.controller
		bartender = controller.opponent
		if isinstance(target, list):
			target = target[0]
		target.frozen=True
		index = bartender.field.index(target)
		newcard = bartender.card(target.id)
		newcard._summon_index = index+1
		newcard.zone = Zone.PLAY
		newcard.frozen = True
		tavern_tier=source.controller.tavern_tier
		if source.sidequest_counter>=1:
			Buff(target, 'BG22_HERO_004_Buddy_e2', atk=tavern_tier*source.sidequest_counter, max_health=tavern_tier*source.sidequest_counter).trigger(source)
			Buff(newcard, 'BG22_HERO_004_Buddy_e2', atk=tavern_tier*source.sidequest_counter, max_health=tavern_tier*source.sidequest_counter).trigger(source)
class BG22_HERO_004p:# <12>[1453]
	""" Twice as Nice
	[Passive.] After Bob's Tavern is [Refreshed], copy his highest Tier minion _and [Freeze] them both. """
	events = Rerole(CONTROLLER).after(BG22_HERO_004p_Action(HIGHEST_TIER(ENEMY_MINIONS)))
	pass
###### BUDDY ######
class BG22_HERO_004_Buddy_Action(GameAction):# <12>[1453]
	def do(self, source):
		heropower=source.controller.hero.power
		heropower.sidequest_counter=1
		pass
class BG22_HERO_004_Buddy:# <12>[1453]
	""" Varden's Aquarrior
	'Twice as Nice' also gives the copy stats equal to your Tavern Tier. """
	play = BG22_HERO_004_Buddy_Action()
	pass
class BG22_HERO_004_Buddy_e2:# <12>[1453]
	""" Frosted
	Increased stats. """
	#
	pass
class BG22_HERO_004_Buddy_G_Action(GameAction):# <12>[1453]
	def do(self, source):
		heropower=source.controller.hero.power
		heropower.sidequest_counter=2
		pass
class BG22_HERO_004_Buddy_G:# <12>[1453]
	""" Varden's Aquarrior
	'Twice as Nice' also givesthe copy stats equal toyour Tavern Tier twice. """
	play = BG22_HERO_004_Buddy_G_Action()
	pass





##Vol'jin   ### HP OK ### BUDDY OK###
BG_Hero5+=[
	'BG20_HERO_201','BG20_HERO_201e','BG20_HERO_201e2','BG20_HERO_201e3',
	'BG20_HERO_201p','BG20_HERO_201p2','BG20_HERO_201p2e','BG20_HERO_201p3e',
	'BG20_HERO_201_Buddy','BG20_HERO_201_Buddy_e','BG20_HERO_201_Buddy_e2','BG20_HERO_201_Buddy_G',]#
BG_PoolSet_Hero5.append('BG20_HERO_201')
BG_Hero5_Buddy['BG20_HERO_201']='BG20_HERO_201_Buddy'
BG_Hero5_Buddy_Gold['BG20_HERO_201_Buddy']='BG20_HERO_201_Buddy_G'
class BG20_HERO_201:# <12>[1453]
	""" Vol'jin  """
class ChooseTwice(Choice):
	card1=None
	card2=None
	def choose(self, card):
		self.source.sidequest_counter += 1
		if self.source.sidequest_counter>=2:
			self.next_choice=None
		else:
			self.next_choice=self
		super().choose(card)
		if self.source.sidequest_counter==1:
			self.card1=card
			#self.cards = self._args[1]
			self.cards = self.source.controller.field
		else:
			self.card2=card
			atk_mod=self.card2.atk-self.card1.atk
			hlt_mod=self.card2.max_health-self.card1.max_health
			Buff(self.card1, 'BG20_HERO_201e', atk=atk_mod, max_health=hlt_mod).trigger(self.source)
			Buff(self.card2, 'BG20_HERO_201e2', atk=-atk_mod, max_health=-hlt_mod).trigger(self.source)
			if Config.LOGINFO:
				print("(ChooseTwice.choose)Swaping stats between %s and %s"%(self.card1, self.card2))
class BG20_HERO_201p:# <12>[1453]
	""" Spirit Swap
	Choose two minions. Swap their stats. """
	requirements = {1001:2} ## original gametag.  need "{value} or more" field minions.
	activate = ChooseTwice(CONTROLLER, FRIENDLY_MINIONS)
	pass
class BG20_HERO_201p2:# <12>[1453]
	""" Spirit Swap
	Choose a minion. Swap its stats with {0}. """
	#
	pass
class BG20_HERO_201e:# <12>[1453]
	""" Modified Attack,	Attack is increased or decreased. """
	pass
class BG20_HERO_201e2:# <12>[1453]
	""" Modified Health,	Health is increased or decreased. """
	pass
class BG20_HERO_201e3:# <12>[1453]
	""" Stats Set	 """
	pass
class BG20_HERO_201p2e:# <12>[1453]
	""" Spirit Swapped
	Stats swapped with another minion. """
	#
	pass
class BG20_HERO_201p3e:# <12>[1453]
	""" Marked for Swap
	Stats can be swapped. """
	#
	pass
###### BUDDY ######
class BG20_HERO_201_Buddy_Action(GameAction):# <12>[1453]
	def do(self, source):
		index=source.controller.field.index(source)
		if index>0:
			card=source.controller.field[index-1]
			Buff(card, 'BG20_HERO_201_Buddy_e', atk=(source.atk-card.atk)).trigger(source)
		pass
class BG20_HERO_201_Buddy:# <12>[1453]
	""" Master Gadrin
	At the end of your turn,the minion to the leftof this copies this minion's Attack. """
	#自分のターンの終了時これの左隣のミニオンはこのミニオンの攻撃力をコピーする。
	events = OWN_TURN_END.on(BG20_HERO_201_Buddy_Action())
	pass
class BG20_HERO_201_Buddy_e:# <12>[1453]
	""" Blessed Hands
	Copied Gadrin's Attack. """
	#
	pass
class BG20_HERO_201_Buddy_e2:# <12>[1453]
	""" Attack Set
	 """
	#
	pass
class BG20_HERO_201_Buddy_G_Action(GameAction):# <12>[1453]
	def do(self, source):
		index=source.controller.field.index(source)
		if index>0:
			card=source.controller.field[index-1]
			Buff(card, 'BG20_HERO_201_Buddy_e', atk=(source.atk-card.atk)).trigger(source)
		if index<len(source.controller.field)-1:
			card=source.controller.field[index+1]
			Buff(card, 'BG20_HERO_201_Buddy_e', atk=(source.atk-card.atk)).trigger(source)
		pass
class BG20_HERO_201_Buddy_G:# <12>[1453]
	""" Master Gadrin
	At the end of your turn,adjacent minions copythis minion's Attack. """
	events = OWN_TURN_END.on(BG20_HERO_201_Buddy_G_Action())
	pass



##Xyrella  ### HP OK ### BUDDY OK ###
BG_Hero5+=['BG20_HERO_101','BG20_HERO_101p','BG20_HERO_101pe2','BG20_HERO_101_Buddy','BG20_HERO_101_Buddy_e','BG20_HERO_101_Buddy_G','BG20_HERO_101_Buddy_Ge',]#
BG_PoolSet_Hero5.append('BG20_HERO_101')
BG_Hero5_Buddy['BG20_HERO_101']='BG20_HERO_101_Buddy'
BG_Hero5_Buddy_Gold['BG20_HERO_101_Buddy']='BG20_HERO_101_Buddy_G'
class BG20_HERO_101:# <12>[1453]
	""" Xyrella """
class BG20_HERO_101p_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = source.controller
		target.zone=Zone.SETASIDE
		target.controller=controller
		target.zone=Zone.HAND
		target.frozen=False
		Buff(target, 'BG20_HERO_101pe2').trigger(source)
class BG20_HERO_101p:
	""" See the Light
	Choose a minion in Bob's Tavern to add to your hand. Set its stats to 2."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_ENEMY_TARGET:0,PlayReq.REQ_MINION_TARGET:0,}
	activate = BG20_HERO_101p_Action(TARGET)
class BG20_HERO_101pe2:
	max_health = SET(2)
	atk = SET(2)
	pass
###### BUDDY ######
class BG20_HERO_101_Buddy_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self,source,target,buff):
		if hasattr(target,'atk') and hasattr(target,'max_health'):
			if target.max_health==target.atk:
				Buff(source,buff).trigger(source)
class BG20_HERO_101_Buddy:### OK ###
	""" Baby Elekk
	After you play a minion with Attack equal to its Health, gain +2/+2. """
	events = BG_Play(CONTROLLER, FRIENDLY + MINION).on(BG20_HERO_101_Buddy_Action(BG_Play.CARD, 'BG20_HERO_101_Buddy_e'))
	pass
BG20_HERO_101_Buddy_e=buff(2,2)
class BG20_HERO_101_Buddy_G:
	""" 
	After you play a minion with Attack equal to its Health, gain +4/+4.""" 
	events = BG_Play(CONTROLLER, FRIENDLY + MINION).on(BG20_HERO_101_Buddy_Action(BG_Play.CARD, 'BG20_HERO_101_Buddy_Ge'))
	pass
BG20_HERO_101_Buddy_Ge=buff(4,4)



##Y'Shaarj   ### HP OK ###　BUDDY OK ###
BG_Hero5+=['TB_BaconShop_HERO_92','TB_BaconShop_HP_103','TB_BaconShop_HERO_92_Buddy','TB_BaconShop_HERO_92_Buddy_e','TB_BaconShop_HERO_92_Buddy_G','TB_BaconShop_HERO_92_Buddy_G_e',]#
BG_PoolSet_Hero5.append('TB_BaconShop_HERO_92')
BG_Hero5_Buddy['TB_BaconShop_HERO_92']='TB_BaconShop_HERO_92_Buddy'
BG_Hero5_Buddy_Gold['TB_BaconShop_HERO_92_Buddy']='TB_BaconShop_HERO_92_Buddy_G'
class TB_BaconShop_HERO_92:# <12>[1453]
	""" Y'Shaarj """
class TB_BaconShop_HP_103_Action(GameAction):
	def do(self, source):
		controller = source.controller# in the battle
		gm = controller.game.parent
		tier = controller.tavern_tier
		card = random.choice(gm.BG_decks[tier])
		if len(controller.field)<7:
			Summon(controller, card).trigger(source)
			Give(controller.deepcopy_original, card).trigger(controller.deepcopy_original)
class TB_BaconShop_HP_103:
	"""  Embrace Your Rage
	[Start of Combat:] Summon a minion from your Tavern Tier. Add a copy to your hand."""
	events = BeginBattle(CONTROLLER).on(TB_BaconShop_HP_103_Action())
	pass
###### BUDDY ######
class TB_BaconShop_HERO_92_Buddy_Action(TargetedAction):# <12>[1453]
	TARGET=ActionArg()
	def do(self, source, target):
		card = get00(target)
		if getattr(card, 'this_is_minion', False)==True:
			if getattr(source.controller.game, 'this_is_battle', False)==True:
				if card.tech_level==source.controller.tavern_tier:
					Buff(card, 'TB_BaconShop_HERO_92_Buddy_e').trigger(source)
		pass
class TB_BaconShop_HERO_92_Buddy:# <12>[1453]
	""" Baby Y'Shaarj
	Whenever you summon a minion of your current Tavern Tier, give it +4/+4. """
	events = Summon(CONTROLLER).on(TB_BaconShop_HERO_92_Buddy_Action(Summon.CARD))
	pass
TB_BaconShop_HERO_92_Buddy_e=buff(4,4)# <12>[1453]
class TB_BaconShop_HERO_92_Buddy_G_Action(TargetedAction):# <12>[1453]
	TARGET=ActionArg()
	def do(self, source, target):
		card = get00(target)
		if getattr(card, 'this_is_minion', False)==True:
			if card.tech_level==source.controller.tavern_tier:
				if card.tech_level==source.controller.tavern_tier:
					Buff(card, 'TB_BaconShop_HERO_92_Buddy_G_e').trigger(source)
		pass
class TB_BaconShop_HERO_92_Buddy_G:# <12>[1453]
	""" Baby Y'Shaarj
	Whenever you summon a minion of your current Tavern Tier, give it +8/+8. """
	events = Summon(CONTROLLER).on(TB_BaconShop_HERO_92_Buddy_G_Action(Summon.CARD))
	pass
TB_BaconShop_HERO_92_Buddy_G_e=buff(8,8)# <12>[1453]





##Yogg-Saron, Hope's End #   ### HP OK ### BUDDY OK ###
BG_Hero5+=['TB_BaconShop_HERO_35','TB_BaconShop_HP_039','TB_BaconShop_HP_039e',
		   'TB_BaconShop_HERO_35_Buddy','TB_BaconShop_HERO_35_Buddy_t1','TB_BaconShop_HERO_35_Buddy_t1e',
		   'TB_BaconShop_HERO_35_Buddy_t2',
		   'TB_BaconShop_HERO_35_Buddy_t3','TB_BaconShop_HERO_35_Buddy_t3e','TB_BaconShop_HERO_35_Buddy_t3f',
		   'TB_BaconShop_HERO_35_Buddy_t4',
		   'TB_BaconShop_HERO_35_Buddy_t5',
		   'TB_BaconShop_HERO_35_Buddy_t6','TB_BaconShop_HERO_35_Buddy_t6e','TB_BaconShop_HERO_35_Buddy_t6t',
		   'TB_BaconShop_HERO_35_Buddy_t7','TB_BaconShop_HERO_35_Buddy_G',]#
BG_PoolSet_Hero5.append('TB_BaconShop_HERO_35')
BG_Hero5_Buddy['TB_BaconShop_HERO_35']='TB_BaconShop_HERO_35_Buddy'
BG_Hero5_Buddy_Gold['TB_BaconShop_HERO_35_Buddy']='TB_BaconShop_HERO_35_Buddy_G'
class TB_BaconShop_HERO_35:# <12>[1453]
	""" Yogg-Saron, Hope's End """
class TB_BaconShop_HP_039_Action(GameAction):
	def do(self, source):
		controller = source.controller # in the bar
		bartender = controller.opponent
		if len(bartender.field)>0:
			card = random.choice(bartender.field)
			card.zone=Zone.SETASIDE
			#bartender.field.remove(card)
			card.controller = controller
			card.zone=Zone.HAND
			Buff(card, 'TB_BaconShop_HP_039e').trigger(source)
			if source.script_data_num_1>0 and len(bartender.field)>0:
				card = random.choice(bartender.field)
				card.zone=Zone.SETASIDE
				#bartender.field.remove(card)
				card.controller = controller
				card.zone=Zone.HAND
				Buff(card, 'TB_BaconShop_HP_039e').trigger(source)
class TB_BaconShop_HP_039: ### OK ###
	""" Puzzle Box
	Add a random minion in Bob's Tavern to your hand. Give it +1/+1."""
	activate = TB_BaconShop_HP_039_Action()
	pass
TB_BaconShop_HP_039e=buff(1,1)
###### buddy ######
class TB_BaconShop_HERO_35_Buddy_Action(GameAction):
	def do(self, source):
		cards=['TB_BaconShop_HERO_35_Buddy_t1','TB_BaconShop_HERO_35_Buddy_t2','TB_BaconShop_HERO_35_Buddy_t3','TB_BaconShop_HERO_35_Buddy_t4','TB_BaconShop_HERO_35_Buddy_t5','TB_BaconShop_HERO_35_Buddy_t6','TB_BaconShop_HERO_35_Buddy_t7',]
		card = random.choice(cards)
		Give(source.controller, card).trigger(source)
		pass
class TB_BaconShop_HERO_35_Buddy:### OK ###
	""" Acolyte of Yogg-Saron
	When you sell this, spin the Wheel of Yogg-Saron."""
	events = Sell(CONTROLLER, SELF).on(TB_BaconShop_HERO_35_Buddy_Action())
	pass
class TB_BaconShop_HERO_35_Buddy_t1_Action(GameAction):# <12>[1453]
	def do(self, source):
		source.controller.hero.power.script_data_num_1=1
		pass
class TB_BaconShop_HERO_35_Buddy_t1:# <12>[1453] ### OK ###
	""" Mysterybox
	For the rest of the game,your Hero Power triggers an extra time when used. """
	play = TB_BaconShop_HERO_35_Buddy_t1_Action()
	pass
class TB_BaconShop_HERO_35_Buddy_t1e:# <12>[1453]
	""" Mysterybox
	Your Hero Power triggers an extra time. """
	#
	pass
class TB_BaconShop_HERO_35_Buddy_t2_Action(GameAction):
	"""Hand of Fate """
	def do(self, source):
		controller=source.controller
		cards=['BGS_Treasures_004', 'BGS_Treasures_006', 'BGS_Treasures_007', 'BGS_Treasures_012', 'BGS_Treasures_015', 'BGS_Treasures_018', 'BGS_Treasures_001', 'BGS_Treasures_010', 'BGS_Treasures_013', 'BGS_Treasures_016', 'BGS_Treasures_019', 'BGS_Treasures_022', 'BGS_Treasures_023', 'BGS_Treasures_025', 'BGS_Treasures_026', 'BGS_Treasures_029', 'BGS_Treasures_000', 'BGS_Treasures_009', 'BGS_Treasures_014', 'BGS_Treasures_020', 'BGS_Treasures_028', 'BGS_Treasures_030', 'BGS_Treasures_033', 'BGS_Treasures_036', 'BGS_Treasures_037', 'BGS_Treasures_040']
		cards=random.sample(cards, 2)
		Give(controller, cards[0]).trigger(source)
		Give(controller, cards[1]).trigger(source)
		pass
class TB_BaconShop_HERO_35_Buddy_t2:# <12>[1453]### OK ##
	""" Hand of Fate
	Add 2 random Darkmoon Prizes to your hand. """
	play = TB_BaconShop_HERO_35_Buddy_t2_Action()
	pass
class TB_BaconShop_HERO_35_Buddy_t3_Action(TargetedAction):
	"""Curse of Flesh """
	CONTROLLER = ActionArg()
	def do(self, source, controller):
		cards=[card for card in controller.field if card.type==CardType.MINION]
		for card in cards:
			Buff(card, 'TB_BaconShop_HERO_35_Buddy_t3e', atk=3, max_health=3).trigger(source)
		if len(cards)>=2:
			cards=random.sample(cards, 2)
			atk=cards[1].atk-cards[0].atk
			hlt=cards[1].max_health-cards[0].max_health
			Buff(cards[0], 'TB_BaconShop_HERO_35_Buddy_t3f', atk=atk, max_health=hlt).trigger(source)
			Buff(cards[1], 'TB_BaconShop_HERO_35_Buddy_t3f', atk=-atk, max_health=-hlt).trigger(source)
			if Config.LOGINFO:
				Config.log("TB_BaconShop_HERO_35_Buddy_t3_Action.do","changes stats of %s and %s "%(cards[0],cards[1]))
		pass

class TB_BaconShop_HERO_35_Buddy_t3:# <12>[1453] ### OK ###
	""" Curse of Flesh
	Give your minions +3/+3, then randomly shuffle their stats. """
	play = TB_BaconShop_HERO_35_Buddy_t3_Action(CONTROLLER)
	pass
class TB_BaconShop_HERO_35_Buddy_t3e:# <12>[1453]
	""" Fleshy
	+3/+3 """
	pass
class TB_BaconShop_HERO_35_Buddy_t3f:# <12>[1453]
	""" Curse of Fleshed
	Stats shuffled with other minions. """
	#
	pass
class TB_BaconShop_HERO_35_Buddy_t4_Action(TargetedAction):
	"""Curse of Flesh """
	CONTROLLER = ActionArg()
	def do(self, source, controller):
		for card in reversed(controller.opponent.field):
			card.zone=Zone.SETASIDE
			card.controller=controller
			card.zone=Zone.HAND
		controller.game.free_rerole=1	
		Rerole(controller).trigger(source)
		pass
class TB_BaconShop_HERO_35_Buddy_t4:# <12>[1453] ### OK ###
	""" Mindflayer Goggles
	Steal all minions in Bob's Tavern, then [Refresh] it. """
	play = TB_BaconShop_HERO_35_Buddy_t4_Action(CONTROLLER)
	pass
class TB_BaconShop_HERO_35_Buddy_t5_Action(TargetedAction):
	"""Curse of Flesh """
	CONTROLLER = ActionArg()
	def do(self, source, controller):
		if len(controller.field)>0 and len(controller.opponent.field)>0:
			for card in reversed(controller.opponent.field):
				card2 = random.choice(controller.field)
				if card.type==CardType.MINION and card2.type==CardType.MINION:
					Buff(card2, 'TB_BaconShop_HERO_35_Buddy_t5e', atk=card.atk, max_health=card.max_health).trigger(source)
					card.discard()	
			controller.game.free_rerole=1
			Rerole(controller).trigger(source)
		pass
@custom_card
class TB_BaconShop_HERO_35_Buddy_t5e:
	tags = {
		GameTag.CARDNAME: "Devouring Hunger",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
	}
class TB_BaconShop_HERO_35_Buddy_t5:# <12>[1453] ### OK ###
	""" Devouring Hunger
	Consume Bob's Tavern and give the stats to your minions.Then [Refresh] it. """
	play=TB_BaconShop_HERO_35_Buddy_t5_Action(CONTROLLER)
	pass
class TB_BaconShop_HERO_35_Buddy_t6_Action(TargetedAction):
	"""Curse of Flesh """
	CONTROLLER = ActionArg()
	def do(self, source, controller):
		cards = controller.game.characters
		for repeat in range(len(cards)):
			card = random.choice(cards)
			if card==controller.hero or card==controller.opponent.hero:
				if Config.LOGINFO:
					Config.log("TB_BaconShop_HERO_35_Buddy_t6_Action.do","Choice is hero and quits.")
				break
			else:
				if Config.LOGINFO:
					Config.log("TB_BaconShop_HERO_35_Buddy_t6_Action.do","Choice is a minion and buffs Pyrobuff.")
				Buff(card, 'TB_BaconShop_HERO_35_Buddy_t6e').trigger(source)
		pass
class TB_BaconShop_HERO_35_Buddy_t6:# <12>[1453] ### OK ###
	""" Rod of Roasting
	Cast 'Pyrobuff' randomly to give minions +4/+4 until one hits your bartender or hero. """
	play = TB_BaconShop_HERO_35_Buddy_t6_Action(CONTROLLER)
	pass
TB_BaconShop_HERO_35_Buddy_t6e=buff(4,4)
""" Pyrobuffed	+4/+4 """
class TB_BaconShop_HERO_35_Buddy_t6t:# <12>[1453]
	""" Pyrobuff
	Give a minion +4/+4. """
	pass
class TB_BaconShop_HERO_35_Buddy_t7_Action(TargetedAction):
	"""  Mysterybox """
	CONTROLLER = ActionArg()
	def do(self, source, controller):
		if controller.game.this_is_tavern:
			if len(controller.opponent.field):
				card = random.choice(controller.opponent.field)
				controller.game.BG_morph_gold(card)
		pass
class TB_BaconShop_HERO_35_Buddy_t7:### OK ###
	""" Mysterybox
	Make a random minion in Bob's Tavern Golden."""
	play = TB_BaconShop_HERO_35_Buddy_t7_Action(CONTROLLER)
	pass
class TB_BaconShop_HERO_35_Buddy_G:
	""" Acolyte of Yogg-Saron
	When you sell this, spin the Wheel of Yogg-Saron twice."""
	events = Sell(CONTROLLER, SELF).on(TB_BaconShop_HERO_35_Buddy_Action(), TB_BaconShop_HERO_35_Buddy_Action())
	pass




##Ysera ####### HP OK ##### BUDDY OK ###
BG_Hero5+=['TB_BaconShop_HERO_53','TB_BaconShop_HP_062',
		   'TB_BaconShop_HERO_53_Buddy','TB_BaconShop_HERO_53_Buddy_e','TB_BaconShop_HERO_53_Buddy_G',]#
BG_PoolSet_Hero5.append('TB_BaconShop_HERO_53')
BG_Hero5_Buddy['TB_BaconShop_HERO_53']='TB_BaconShop_HERO_53_Buddy'
BG_Hero5_Buddy_Gold['TB_BaconShop_HERO_53_Buddy']='TB_BaconShop_HERO_53_Buddy_G'
class TB_BaconShop_HERO_53:# <12>[1453]  ## if dragon is not banned
	""" Ysera """
class TB_BaconShop_HP_062_Action(GameAction):
	def do(self, source):
		from fireplace import cards
		controller = source.controller # in the bar
		bartender = controller.opponent
		gm=controller.game.parent
		tier = controller.tavern_tier
		dk=[]
		for i in range(1,tier+1):
			dk += cards.battlegrounds.BG_minion_dragon.BG_PoolSet_Dragon[i]
		cardID=random.choice(dk)
		card = bartender.card(cardID)
		if cardID in gm.BG_decks[card.tech_level]:
			gm.BG_decks[card.tech_level].remove(cardID)
		card.controller = bartender# maybe deletable
		card.zone = Zone.PLAY

class TB_BaconShop_HP_062:
	"""  Dream Portal
	[Passive] Bob always offers an extra Dragon whenever the Tavern is [Refreshed]."""
	events = Rerole(CONTROLLER).after(TB_BaconShop_HP_062_Action())
	pass
class TB_BaconShop_HERO_53_Buddy_Action(GameAction):
	def do(self, source):
		controller=source.controller
		cards=[card for card in controller.opponent.field if card.race==Race.DRAGON]
		if len(cards):
			for card in cards:
				Buff(card, "TB_BaconShop_HERO_53_Buddy_e", atk=3, max_health=3).trigger(source)
class TB_BaconShop_HERO_53_Buddy:
	""" Valithria Dreamwalker
	Dragons in Bob's Tavern have +3/+3."""
	play = TB_BaconShop_HERO_53_Buddy_Action()
	events = Sell(CONTROLLER, SELF).on(RemoveBuff(ENEMY_MINIONS, "TB_BaconShop_HERO_53_Buddy_e"))
	pass
class TB_BaconShop_HERO_53_Buddy_e:# <12>[1453]
	pass
class TB_BaconShop_HERO_53_Buddy_G_Action(GameAction):
	def do(self, source):
		controller=source.controller
		cards=[card for card in controller.opponent.field if card.race==Race.DRAGON]
		if len(cards):
			for card in cards:
				Buff(card, "TB_BaconShop_HERO_53_Buddy_e", atk=6, max_health=6).trigger(source)
class TB_BaconShop_HERO_53_Buddy_G:
	""" Valithria Dreamwalker
	Dragons in Bob's Tavern have +6/+6."""
	play = TB_BaconShop_HERO_53_Buddy_G_Action()
	events = Sell(CONTROLLER, SELF).on(RemoveBuff(ENEMY_MINIONS + DRAGON, "TB_BaconShop_HERO_53_Buddy_e"))
	pass




##Zephrys, the Great  ##### HP OK ####
BG_Hero5+=['TB_BaconShop_HERO_91','TB_BaconShop_HP_102','TB_BaconShop_HERO_91_Buddy','TB_BaconShop_HERO_91_Buddy_G',]#
BG_PoolSet_Hero5.append('TB_BaconShop_HERO_91')
BG_Hero5_Buddy['TB_BaconShop_HERO_91']='TB_BaconShop_HERO_91_Buddy'
BG_Hero5_Buddy_Gold['TB_BaconShop_HERO_91_Buddy']='TB_BaconShop_HERO_91_Buddy_G'
class TB_BaconShop_HERO_91:# <12>[1453]
	""" Zephrys, the Great """
class TB_BaconShop_HP_102_Action(GameAction):
	def do(self, source):
		controller = source.controller # in the bar
		bartender = controller.opponent
		gm=controller.game.parent
		source.script_data_num_1=source.tags[GameTag.SCORE_VALUE_1]
		if source.script_data_num_1>0:
			gold_card_id = controller.game.BG_find_double()## ダブルを判定
			if gold_card_id:
				controller.game.BG_deal_gold(gold_card_id)
				source.script_data_num_1 -= 1
				source.tags[GameTag.SCORE_VALUE_1]=source.script_data_num_1

class TB_BaconShop_HP_102:
	"""  Three Wishes
	If you have two copies of a minion, find the third. <i>(@ |4(Wish, Wishes) left!)</i>"""
	activate = TB_BaconShop_HP_102_Action()
	pass
class TB_BaconShop_HERO_91_Buddy_Action(GameAction):
	def isolate(self, card, cards):
		count=len([cd for cd in cards if cd.id==card.id])
		return count==1
	def do(self, source):
		cardsId=[card.id for card in source.controller.field if self.isolate(card, source.controller.field)==True]
		Discover(source.controller, RandomID(*cardsId)*3).trigger(source)
		pass
class TB_BaconShop_HERO_91_Buddy:
	"""  Phyresz
	[Battlecry: Discover] a plain copy of a minion that you have exactly one of."""
	play = TB_BaconShop_HERO_91_Buddy_Action()
	pass
class TB_BaconShop_HERO_91_Buddy_G_Choice(Choice):
	def choose(self, card):
		self.source.sidequest_counter += 1
		if self.source.sidequest_counter>=2:
			self.next_choice=None
		else:
			self.next_choice=self
		super().choose(card)
		new_card = self.player.card(card.id)# make a new copy
		new_card.zone = Zone.HAND
		pass
class TB_BaconShop_HERO_91_Buddy_G_Action(GameAction):
	def isolate(self, card, cards):
		count=len([cd for cd in cards if cd.id==card.id])
		return count==1
	def do(self, source):
		cardsId=[card.id for card in source.controller.field if self.isolate(card, source.controller.field)==True]
		self.source.sidequest_counter=0
		TB_BaconShop_HERO_91_Buddy_G_Choice(source.controller, RandomID(*cardsId)*3).trigger(source)
		pass
class TB_BaconShop_HERO_91_Buddy_G:
	""" Phyresz 
	[Battlecry: Discover] a plain copy of a minion that you have exactly one of twice."""
	play = TB_BaconShop_HERO_91_Buddy_G_Action()
	pass






####################################################################################