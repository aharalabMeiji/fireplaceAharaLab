from ..utils import *

##
##   Bartenders
##

Bartenders=['TB_BaconShopBob','TB_BaconShop_HERO_31','TB_KTRAF_H_1']

class TB_BaconShopBob:# <12>[1453]
	""" Bartender Bob
	 """
	#
	pass
class TB_BaconShop_HERO_31:# <12>[1453]
	""" Bartendotron
	 """
	#
	pass


class TB_KTRAF_H_1:
	""" Kel'Thuzad
	""" 
	pass
class TB_BaconShop_HERO_KelThuzad:# <12>[1453]
	""" Kel'Thuzad
	"""
	pass

BG_Hero1=[]

BG_PoolSet_Hero1=[]

BG_Hero1_Buddy={}

BG_Hero1_Buddy_Gold={}

########### index 

######HERO1

##A. F. Kay TB_BaconShop_HERO_16
##Al'Akir TB_BaconShop_HERO_76
##Alexstrasza  TB_BaconShop_HERO_56
##Ambassador Faelin BG22_HERO_201
##Aranna Starseeker TB_BaconShop_HERO_59
##Arch-Villain Rafaam TB_BaconShop_HERO_45
##Bru'kan BG22_HERO_001
##C'Thun TB_BaconShop_HERO_29
##Captain Eudora TB_BaconShop_HERO_64
##Captain Hooktusk TB_BaconShop_HERO_67
##Cariel Roame BG21_HERO_000
##Chenvaala TB_BaconShop_HERO_78
##Cookie the Cook BG21_HERO_020
##Dancin' Deryl TB_BaconShop_HERO_36
##Death Speaker Blackthorn BG20_HERO_103
##Deathwing TB_BaconShop_HERO_52
##Dinotamer Brann TB_BaconShop_HERO_43
##Drek'Thar BG22_HERO_002

######HERO2

#  E - K
## E.T.C., Band Manager BG25_HERO_105
##Edwin VanCleef TB_BaconShop_HERO_01
##Elise Starseeker TB_BaconShop_HERO_42
##Enhance-o Mechano BG24_HERO_204 ## new 25.0
##Forest Warden Omu TB_BaconShop_HERO_74
##Fungalmancer Flurgl TB_BaconShop_HERO_55
##Galakrond TB_BaconShop_HERO_02
##Galewing BG20_HERO_283
##George the Fallen TB_BaconShop_HERO_15
##Greybough TB_BaconShop_HERO_95
##Guff Runetotem  BG20_HERO_242
##Heistbaron Togwaggle BG23_HERO_305
##Illidan Stormrage  TB_BaconShop_HERO_08
##Infinite Toki  TB_BaconShop_HERO_28
##Ini Stormcoil BG22_HERO_200
##Jandice Barov TB_BaconShop_HERO_71
##Kael'thas Sunstrider  TB_BaconShop_HERO_60
##King Mukla  TB_BaconShop_HERO_38
##Kurtrus Ashfallen  BG20_HERO_280


###### HERO3 ####### L - Q

##Lady Vashj BG23_HERO_304
##Lich Baz'hial TB_BaconShop_HERO_25
##Lord Barov TB_BaconShop_HERO_72 
##Lord Jaraxxus TB_BaconShop_HERO_37
##Maiev Shadowsong TB_BaconShop_HERO_62
##Malygos TB_BaconShop_HERO_58
##Master Nguyen BG20_HERO_202 
##Millhouse Manastorm TB_BaconShop_HERO_49
##Millificent Manastorm TB_BaconShop_HERO_17
##Mr. Bigglesworth TB_BaconShop_HERO_70 
##Murloc Holmes BG23_HERO_303 
##Mutanus the Devourer BG20_HERO_301
##N'Zoth TB_BaconShop_HERO_93
##Nozdormu TB_BaconShop_HERO_57
##Onyxia BG22_HERO_305
##Overlord Saurfang BG20_HERO_102
##Ozumat BG23_HERO_201 
##Patches the Pirate TB_BaconShop_HERO_18
##Patchwerk TB_BaconShop_HERO_34
##Professor Putricide BG25_HERO_100
##Pyramad TB_BaconShop_HERO_39
##Queen Axshara BG22_HERO_007
##Queen Wagtoggle  TB_BaconShop_HERO_14


######  HERO4 ## R - S
	
##Ragnaros the Firelord TB_BaconShop_HERO_11	
##Rakanishu TB_BaconShop_HERO_75
##Reno Jackson TB_BaconShop_HERO_41
##Rokara BG20_HERO_100 
##Scabbs Cutterbutter BG21_HERO_010
##Shudderwock TB_BaconShop_HERO_23
##Silas Darkmoon TB_BaconShop_HERO_90
##Sindragosa TB_BaconShop_HERO_27
##Sir Finley Mrrgglton TB_BaconShop_HERO_40
##Sire Denathrius  BG24_HERO_100 #####difficult##### banned 
##Skycap'n Kragg TB_BaconShop_HERO_68
##Sneed BG21_HERO_030
##Sylvanas Windrunner BG23_HERO_306


###### HERO5 ## T-Z

##Tamsin Roame BG20_HERO_282
##Tavish Stormpike BG22_HERO_000
##Teron Gorefiend BG25_HERO_103
##Tess Greymane TB_BaconShop_HERO_50
##The Curator TB_BaconShop_HERO_33		
##The Great Akazamzarak TB_BaconShop_HERO_21
##The Jailer TB_BaconShop_HERO_702 ## new 24.6 
##The Lich King TB_BaconShop_HERO_22
##The Rat King TB_BaconShop_HERO_12	
##Tickatus TB_BaconShop_HERO_94
##Trade Prince Gallywix TB_BaconShop_HERO_10
##Vanndar Stormpike BG22_HERO_003
##Varden Dawngrasp BG22_HERO_004
##Vol'jin BG20_HERO_201
##Xyrella BG20_HERO_101
##Y'Shaarj TB_BaconShop_HERO_92
##Yogg-Saron, Hope's End TB_BaconShop_HERO_35
##Ysera TB_BaconShop_HERO_53
##Zephrys, the Great TB_BaconShop_HERO_91

########### source

##A. F. Kay   ### visually check 23/4/5 ### 
BG_Hero1 += ['TB_BaconShop_HERO_16','TB_BaconShop_HP_044','TB_BaconShop_HERO_16_Buddy','TB_BaconShop_HERO_16_Buddy_e','TB_BaconShop_HERO_16_Buddy_G','TB_BaconShop_HERO_16_Buddy_G_e',]#00#A. F. Kay 
BG_PoolSet_Hero1 +=['TB_BaconShop_HERO_16',]
BG_Hero1_Buddy['TB_BaconShop_HERO_16']='TB_BaconShop_HERO_16_Buddy'
BG_Hero1_Buddy_Gold['TB_BaconShop_HERO_16_Buddy']='TB_BaconShop_HERO_16_Buddy_G'
class TB_BaconShop_HERO_16:# <12>[1453]
	""" A. F. Kay	 """
	pass
class TB_BaconShop_HP_044_Action(GameAction):
	def do(self, source):
		controller = source.controller
		bar = controller.game
		turn = bar.turn
		if turn==1 or turn==2:
			SetMaxMana(controller,0).trigger(bar)
		if turn==3:
			SetMaxMana(controller,5).trigger(bar)
			DiscoverTwice(controller, RandomBGAdmissible(tech_level = 3)*3).trigger(source)#tech_level=3
class TB_BaconShop_HP_044:#<12>[1453]
	""" Procrastinate
	[Passive] Skip your first two turns.Start with two minions from Tavern Tier 3."""
	events = BeginBar(CONTROLLER).on(TB_BaconShop_HP_044_Action())
	pass
### buddy ###
class TB_BaconShop_HERO_16_Buddy_Action(GameAction):
	def do(self, source):
		controller = source.controller
		cards = [card for card in controller.field if card.tech_level==3]
		if len(cards):
			for card in cards:
				Buff(card, 'TB_BaconShop_HERO_16_Buddy_e').trigger(controller)
class TB_BaconShop_HERO_16_Buddy:# <12>[1453] #########################
	""" Snack Vendor
	At the end of your turn, give your Tavern Tier 3 minions +1/+2."""
	events = OWN_TURN_END.on(TB_BaconShop_HERO_16_Buddy_Action())
	pass
TB_BaconShop_HERO_16_Buddy_e=buff(1,2)# <12>[1453] """ Snack-Filled +1/+2. """
class TB_BaconShop_HERO_16_Buddy_G_Action(GameAction):
	def do(self, source):
		controller = source.controller
		cards = [card for card in controller.field if card.tech_level==3]
		if len(cards):
			for card in cards:
				Buff(card, 'TB_BaconShop_HERO_16_Buddy_G_e').trigger(controller)
class TB_BaconShop_HERO_16_Buddy_G:# <12>[1453]##########################
	""" Snack Vendor
	At the end of your turn, give your Tavern Tier 3 minions +2/+4. """
	events = OWN_TURN_END.on(TB_BaconShop_HERO_16_Buddy_G_Action())
	pass
TB_BaconShop_HERO_16_Buddy_G_e=buff(2,4)# <12>[1453] """ Snack-Filled +2/+4. """





##Al'Akir  ### OK ### visually check 23/4/5
BG_Hero1 += ['TB_BaconShop_HERO_76','TB_BaconShop_HP_086','TB_BaconShop_HERO_76_Buddy','TB_BaconShop_HERO_76_Buddy_e','TB_BaconShop_HERO_76_Buddy_G',]#01#Al'Akir
BG_PoolSet_Hero1 +=['TB_BaconShop_HERO_76',]
BG_Hero1_Buddy['TB_BaconShop_HERO_76']='TB_BaconShop_HERO_76_Buddy'
BG_Hero1_Buddy_Gold['TB_BaconShop_HERO_76_Buddy']='TB_BaconShop_HERO_76_Buddy_G'
class TB_BaconShop_HERO_76:# <12>[1453]
	""" Al'Akir	 """
class TB_BaconShop_HP_086_Action(GameAction):
	def do(self, source):
		controller=source.controller
		if len(controller.field)>0:
			card = controller.field[0]
			card.windfury=1
			card.divine_shield=True
			card.taunt=True
class TB_BaconShop_HP_086:
	""" Swatting Insects
	[Passive][Start of Combat:] Give yourleft-most minion [Windfury],___[Divine Shield], and [Taunt]."""
	events = BeginBattle(CONTROLLER).on(TB_BaconShop_HP_086_Action())
	pass
### buddy ###
class TB_BaconShop_HP_086_BuddyAction(GameAction):
	def do(self, source):
		controller=source.controller
		card = random.choice(controller.field)
		card.windfury=1
		card.divine_shield=True
		card.taunt=True
class TB_BaconShop_HERO_76_Buddy:######################################
	"""Spirit of Air
	[Deathrattle:] Give a random friendly minion [Windfury],___[Divine Shield], and [Taunt].___
	"""
	deathrattle = TB_BaconShop_HP_086_BuddyAction()
	pass
class TB_BaconShop_HERO_76_Buddy_e:# <12>[1453]
	""" Blessing of Air,[Windfury], [Divine Shield], and [Taunt]. """
class TB_BaconShop_HP_086_Buddy_G_Action(GameAction):
	def do(self, source):
		controller=source.controller
		cards=[]
		if len(controller.field)==1 or len(controller.field)==2:
			cards=controller.field
		elif len(controller.field)>=3:
			cards=random.sample(controller.field, 2)
		for card in cards:
			card.windfury=1
			card.divine_shield=True
			card.taunt=True
class TB_BaconShop_HERO_76_Buddy_G:
	""" Spirit of Air
	[Deathrattle:] Give 2 random friendly minions [Windfury],[Divine Shield], and [Taunt]."""
	deathrattle =  TB_BaconShop_HP_086_Buddy_G_Action()
	pass


##Alexstrasza   ### OK ### visually check 23/4/5
BG_Hero1 += ['TB_BaconShop_HERO_56','TB_BaconShop_HP_064','TB_BaconShop_HERO_56_Buddy','TB_BaconShop_HERO_56_Buddy_G']#02#Alexstrasza]
BG_PoolSet_Hero1 +=['TB_BaconShop_HERO_56',]
BG_Hero1_Buddy['TB_BaconShop_HERO_56']='TB_BaconShop_HERO_56_Buddy'
BG_Hero1_Buddy_Gold['TB_BaconShop_HERO_56_Buddy']='TB_BaconShop_HERO_56_Buddy_G'
class TB_BaconShop_HERO_56:# <12>[1453]
	""" Alexstrasza	"""
class TB_BaconShop_HP_064_Action(GameAction):
	TARGET = ActionArg()
	def do(self, source):
		controller=source.controller
		if controller.tavern_tier==5:
			DiscoverTwice(controller, RandomBGDragon()*3).trigger(source)
class TB_BaconShop_HP_064:
	""" Queen of Dragons
	[Passive]After you upgrade Bob's Tavern to Tavern Tier 5,_[Discover] two Dragons."""
	events = UpgradeTier(CONTROLLER).on(TB_BaconShop_HP_064_Action())
	pass
class TB_BaconShop_HERO_56_Buddy:
	""" Vaelastrasz
	[Battlecry:] Add a random Dragon of your Tavern Tier to your hand."""
	play = Give(CONTROLLER, RandomBGDragon(tech_level=TIER(CONTROLLER)))
class TB_BaconShop_HERO_56_Buddy_G:
	""" Vaelastrasz
	[Battlecry:] Add two random Dragons of your Tavern Tier to your hand."""
	play = Give(CONTROLLER, RandomBGDragon(tech_level=TIER(CONTROLLER))) * 2



##Ambassador Faelin ### OK ### visually check 23/4/5
BG_Hero1 += ['BG22_HERO_201','BG22_HERO_201p','BG22_HERO_201pe','BG22_HERO_201_Buddy','BG22_HERO_201_Buddy_G',]#03#Ambassador Faelin]
BG_PoolSet_Hero1 +=['BG22_HERO_201',]
BG_Hero1_Buddy['BG22_HERO_201']='BG22_HERO_201_Buddy'
BG_Hero1_Buddy_Gold['BG22_HERO_201_Buddy']='BG22_HERO_201_Buddy_G'
class BG22_HERO_201:# <12>[1453]
	""" Ambassador Faelin	"""
class BG22_HERO_201p_Choice(Choice):
	def choose(self, card):
		source = self.source
		source.sidequest_counter += 1
		if source.sidequest_counter>=3:
			self.next_choice=None
		else:
			self.next_choice=self
		super().choose(card)
		card.zone = Zone.HAND
		cards = self._args[1]
		if source.sidequest_counter==1:
			Buff(card, 'BG22_HERO_201pe').trigger(source)		
			cards = RandomBGAdmissible(tech_level=4)*3
		elif source.sidequest_counter==2:
			Buff(card, 'BG22_HERO_201pe').trigger(source)		
			cards = RandomBGAdmissible(tech_level=6)*3
		elif source.sidequest_counter==3:
			Buff(card, 'BG22_HERO_201pe').trigger(source)	
			pass	
		if isinstance(cards, LazyValue):
			self.cards = cards.evaluate(source)
class BG22_HERO_201p_Action(GameAction):
	def do(self, source):
		controller = source.controller
		bar = controller.game
		turn = bar.turn
		if turn==1:
			controller.max_mana = 0
			BG22_HERO_201p_Choice(controller, RandomBGAdmissible(tech_level=2)*3).trigger(source)
		if turn==2:# maybe no need
			controller.max_mana = 4# maybe no need
		pass
class BG22_HERO_201p:# <12>[1453]
	""" Expedition Plans
	[Passive.] Skip your first turn. [Discover] a Tier 2, 4, and 6 minion to get at those Tiers. """
	events = BeginBar(CONTROLLER).on(BG22_HERO_201p_Action())
	pass
class BG22_HERO_201pe_Action(TargetedAction):
	TARGET = ActionArg()
	TARGETEDACTION = ActionArg()
	def do(self, source, target, targetedaction):
		#source = Buff card
		#target = owner card
		controller = target.controller
		self.owner = target
		tier = self.owner.tech_level
		if controller.tavern_tier>= tier:
			self.owner.cant_play=False
			targetedaction.trigger(source)
		pass
class BG22_HERO_201pe:# <12>[1453]
	""" Unplayable
	"""
	def apply(self, target):
		self.owner = target
		self.owner.cant_play=True
	#play = SetAttr(OWNER, 'cant_play', True)
	events = UpgradeTier(CONTROLLER).on(BG22_HERO_201pe_Action(OWNER, Destroy(SELF)))
	pass
###### buddy ######
class BG22_HERO_201_Buddy:# <12>[1453]
	""" Submersible Chef
	[Battlecry:] Add a random Tier 1, 3, and 5 minion to your hand. """
	play = (
		Give(CONTROLLER, RandomBGAdmissible(tech_level=1)),
		Give(CONTROLLER, RandomBGAdmissible(tech_level=3)),
		Give(CONTROLLER, RandomBGAdmissible(tech_level=5)),)
	pass
class BG22_HERO_201_Buddy_G:# <12>[1453]
	""" Submersible Chef
	[Battlecry:] Add a random Tier 1, 3, and 5 minion to your hand twice. """
	play = (
		Give(CONTROLLER, RandomBGAdmissible(tech_level=1)),
		Give(CONTROLLER, RandomBGAdmissible(tech_level=3)),
		Give(CONTROLLER, RandomBGAdmissible(tech_level=5)),
		Give(CONTROLLER, RandomBGAdmissible(tech_level=1)),
		Give(CONTROLLER, RandomBGAdmissible(tech_level=3)),
		Give(CONTROLLER, RandomBGAdmissible(tech_level=5)),)
	pass



##Aranna Starseeker # アランナ ### HP OK ### BUDDY OK ###
BG_Hero1 += ['TB_BaconShop_HERO_59','TB_BaconShop_HP_065','TB_BaconShop_HP_065pe','TB_BaconShop_HP_065t2','TB_BaconShop_HERO_59_Buddy','TB_BaconShop_HERO_59_Buddy_G','TB_BaconShop_HERO_59t',]#04#Aranna Starseeker]
BG_PoolSet_Hero1 +=['TB_BaconShop_HERO_59',]
BG_Hero1_Buddy['TB_BaconShop_HERO_59']='TB_BaconShop_HERO_59_Buddy'
BG_Hero1_Buddy_Gold['TB_BaconShop_HERO_59_Buddy']='TB_BaconShop_HERO_59_Buddy_G'
class TB_BaconShop_HERO_59:# <12>[1453]
	""" Aranna Starseeker
	"""
class TB_BaconShop_HP_065:
	""" Demon Hunter Training
	[Passive] After you [Refresh] 5 times, Bob always has 7 minions.<i>(@ left!)</i>"""
	events = Rerole(CONTROLLER).on(SidequestCounter(SELF, 5, \
		[ ChangeHeroPower(CONTROLLER, 'TB_BaconShop_HP_065t2'),\
		SetAttr(CONTROLLER, 'len_bobs_field', 7)]\
		))
	pass
class TB_BaconShop_HP_065pe:
	"""  Aranna Watcher
	"""
class TB_BaconShop_HERO_59t:# <12>[1453]
	""" Aranna, Unleashed ヒロパ交代後のヒーロー
	"""
class TB_BaconShop_HP_065t2:### 条件が満たされるとヒロパが交代になる
	""" Spectral Sight
	[Passive]Bob's Tavern refreshes with 7 minions."""
### BUDDY ###
class TB_BaconShop_HERO_59_Buddy:# <12>[1453]
	""" Sklibb, Demon Hunter
	After you buy a minion, your next [Refresh] costs (0)."""
	### After you play a minion,your next [Refresh] costs (0). ### old one -25.6
	events = Buy(CONTROLLER, MINION).on(GetFreeRerole(CONTROLLER))
	pass
class TB_BaconShop_HERO_59_Buddy_G:# <12>[1453]
	""" Sklibb, Demon Hunter
	After you buy a minion, your next two [Refreshes] cost (0)."""
	### After you play a minion, your next two [Refreshes] cost (0). ### old one -25.6
	events = Buy(CONTROLLER, MINION).after(GetFreeRerole(CONTROLLER), GetFreeRerole(CONTROLLER))
	pass



##Arch-Villain Rafaam ### OK ### # BUDDY MAYBE #
BG_Hero1 += ['TB_BaconShop_HERO_45','TB_BaconShop_HP_053','TB_BaconShop_HERO_45_Buddy','TB_BaconShop_HERO_45_Buddy_G',]#05#Arch-Villain Rafaam]
BG_PoolSet_Hero1 +=['TB_BaconShop_HERO_45',]
BG_Hero1_Buddy['TB_BaconShop_HERO_45']='TB_BaconShop_HERO_45_Buddy'
BG_Hero1_Buddy_Gold['TB_BaconShop_HERO_45_Buddy']='TB_BaconShop_HERO_45_Buddy_G'
class TB_BaconShop_HERO_45:# <12>[1453]
	""" Arch-Villain Rafaam
	"""
class TB_BaconShop_HP_053_Action(GameAction):
	def do(self, source):
		controller = source.controller
		if controller.first_dead_minion!=None:
			Give(controller,controller.first_dead_minion).trigger(source)
			gold_card_id = controller.game.BG_find_triple()##
			if gold_card_id:
				controller.game.BG_deal_gold(gold_card_id)
class TB_BaconShop_HP_053:
	""" I'll Take That!
	Next combat, add a plain copy of the first minion you kill to your hand."""
	tags={GameTag.HIDE_COST:1}
	events = BeginBar(CONTROLLER).on(TB_BaconShop_HP_053_Action())
### BUDDY ###
class TB_BaconShop_HERO_45_Buddy_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		if controller.second_dead_minion!=None:
			Give(controller,controller.second_dead_minion).trigger(source)
			gold_card_id = controller.game.BG_find_triple()##
			if gold_card_id:
				controller.game.BG_deal_gold(gold_card_id)
class TB_BaconShop_HERO_45_Buddy:# <12>[1453]
	""" Loyal Henchman
	After you kill a second minion each combat,get a plain copy of it. """
	events = BeginBar(CONTROLLER).on(TB_BaconShop_HERO_45_Buddy_Action(CONTROLLER))
	pass
class TB_BaconShop_HERO_45_Buddy_G_Action(GameAction):
	def do(self, source):
		controller = source.controller
		if controller.second_dead_minion!=None:
			Give(controller,controller.second_dead_minion).trigger(source)
			Give(controller,controller.second_dead_minion).trigger(source)
			gold_card_id = controller.game.BG_find_triple()##
			if gold_card_id:
				controller.game.BG_deal_gold(gold_card_id)
class TB_BaconShop_HERO_45_Buddy_G:# <12>[1453]
	""" Loyal Henchman
	After you kill a second minion each combat,_get 2 plain copies of it. """
	events = BeginBar(CONTROLLER).on(TB_BaconShop_HERO_45_Buddy_G_Action())
	pass



###Bru'kan   ###### HP OK ###### BUDDY MAYBE #
BG_Hero1 += ['BG22_HERO_001','BG22_HERO_001p','BG22_HERO_001p_t1','BG22_HERO_001p_t1_s','BG22_HERO_001p_t1e','BG22_HERO_001p_t1et','BG22_HERO_001p_t2','BG22_HERO_001p_t2_s','BG22_HERO_001p_t2e','BG22_HERO_001p_t3','BG22_HERO_001p_t3_s','BG22_HERO_001p_t3e','BG22_HERO_001p_t4','BG22_HERO_001p_t4_s','BG22_HERO_001_Buddy','BG22_HERO_001_Buddy_e','BG22_HERO_001_Buddy_e1','BG22_HERO_001_Buddy_e2','BG22_HERO_001_Buddy_e3','BG22_HERO_001_Buddy_e4','BG22_HERO_001_Buddy_G',]#BG22_HERO_001#06#Bru'kan]
BG_PoolSet_Hero1 +=['BG22_HERO_001',]
BG_Hero1_Buddy['BG22_HERO_001']='BG22_HERO_001_Buddy'
BG_Hero1_Buddy_Gold['BG22_HERO_001_Buddy']='BG22_HERO_001_Buddy_G'
class BG22_HERO_001:# <12>[1453]
	""" Bru'kan 	"""
class BG22_HERO_001p_Choice(Choice):
	def do(self, source, target, cards, option=None):
		super().do(source, target, cards, option)
		choiceAction(target)
		pass
	def choose(self, card):
		super().choose(card)
		if card.type != CardType.HERO_POWER:
			return
		ChangeHeroPower(self.player, card).trigger(self.source)
		card.activate()
		self.next_choice=None
		self.player.choice=None
		pass
class BG22_HERO_001p:# <12>[1453]#
	""" Embrace the Elements
	Choose an Element.[Start of Combat:] Call upon that Element. """
	#<ReferencedTag enumID="1531" name="START_OF_COMBAT" type="Int" value="1"/>
	entourage=['BG22_HERO_001p_t1','BG22_HERO_001p_t2','BG22_HERO_001p_t3','BG22_HERO_001p_t4']
	activate = BG22_HERO_001p_Choice(CONTROLLER, RandomEntourage()*4)
	pass
class BG22_HERO_001_CastSpell(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		controller = target
		card = controller.card(buff)
		CastSpell(card).trigger(source)
		pass
class BG22_HERO_001p_t1:# <12>[1453]
	""" Earth Invocation (hero power)
	[Start of Combat:] Give 4random friendly minions"[Deathrattle:] Summona 1/1 Elemental." """
	events = [
		BeginBattle(CONTROLLER).on(BG22_HERO_001_CastSpell(CONTROLLER, 'BG22_HERO_001p_t1_s')),
		BeginBar(CONTROLLER).on(ChangeHeroPower(CONTROLLER, 'BG22_HERO_001p'))]
	pass
class BG22_HERO_001p_t1_s:# <8>[1453]
	""" Earth Invocation (spell)
	Give 4 random friendly minions "[Deathrattle:] Summon a 1/1 Elemental." """
	def play(self):
		cards = [card for card in self.controller.field]
		if len(cards)>4:
			cards=random.sample(cards,4)
		for card in cards:
			Buff(card, 'BG22_HERO_001p_t1e').trigger(self)
	pass
class BG22_HERO_001p_t1e:# <12>[1453]
	""" Element: Earth (enchantment)
	[Deathrattle:] Summon a 1/1 Elemental. """
	tags={GameTag.DEATHRATTLE:1}
	deathrattle = Summon(CONTROLLER,'BG22_HERO_001p_t1et')
	pass
class BG22_HERO_001p_t1et:# <12>[1453]
	""" Stone Elemental 	 """
	pass
class BG22_HERO_001p_t2:# <12>[1453]
	""" Fire Invocation (hero power)
	[Start of Combat:] Double your left-most minion's Attack. """
	events = [
		BeginBattle(CONTROLLER).on(BG22_HERO_001_CastSpell(CONTROLLER, 'BG22_HERO_001p_t2_s')),
		BeginBar(CONTROLLER).on(ChangeHeroPower(CONTROLLER, 'BG22_HERO_001p'))]
	pass
class BG22_HERO_001p_t2_s:# <8>[1453]
	""" Fire Invocation (spell)
	Double your left-most minion's Attack. """
	def play(self):
		controller = self.controller
		if len(controller.field)>0:
			card = controller.field[0]
			Buff(card, 'BG22_HERO_001p_t2e', atk=card.atk).trigger(controller)
	pass
class BG22_HERO_001p_t2e:# <12>[1453]
	""" Element: Fire
	This minion's Attack has been doubled. """
	pass
class BG22_HERO_001p_t3:# <12>[1453]
	""" Water Invocation
	[Start of Combat:] Giveyour right-most minion+3 Health and [Taunt]. """
	events = [
		BeginBattle(CONTROLLER).on(BG22_HERO_001_CastSpell(CONTROLLER, 'BG22_HERO_001p_t3_s')),
		BeginBar(CONTROLLER).on(ChangeHeroPower(CONTROLLER, 'BG22_HERO_001p'))]
	pass
class BG22_HERO_001p_t3_s:# <8>[1453]
	""" Water Invocation
	Give your right-most minion +3 Health and [Taunt]. """
	def play(self):
		controller = self.controller
		if len(controller.field)>0:
			card = controller.field[-1]
			Buff(card, 'BG22_HERO_001p_t3e').trigger(controller)
	pass
class BG22_HERO_001p_t3e:# <12>[1453]
	""" Element: Water
	+3 Health and [Taunt]. """
	tags = {
		GameTag.HEALTH:3,
		GameTag.TAUNT:1
		}
	pass
class BG22_HERO_001p_t4:# <12>[1453]
	""" Lightning Invocation
	[Start of Combat:] Deal 1 damage to 5 random enemy minions. """
	events = [
		BeginBattle(CONTROLLER).on(BG22_HERO_001_CastSpell(CONTROLLER, 'BG22_HERO_001p_t4_s')),
		BeginBar(CONTROLLER).on(ChangeHeroPower(CONTROLLER, 'BG22_HERO_001p'))]
	pass
class BG22_HERO_001p_t4_s:# <8>[1453]
	""" Lightning Invocation
	Deal 1 damage to 5 random enemy minions. """
	play = SplitHit(CONTROLLER, ENEMY_MINIONS,5)
	pass
######## BUDDY
class BG22_HERO_001_Buddy_Events(TargetedAction):
	TARGET = ActionArg()
	CARD = ActionArg()
	def do(self, source, target, card):
		controller = target.controller
		if isinstance(card,list):
			card = card[0]
		if card.id=='BG22_HERO_001p_t1':
			if not 'BG22_HERO_001p_t1_s' in target.sidequest_list0:
				target.sidequest_list0.append('BG22_HERO_001p_t1_s')
		elif card.id=='BG22_HERO_001p_t2':
			if not 'BG22_HERO_001p_t2_s' in target.sidequest_list0:
				target.sidequest_list0.append('BG22_HERO_001p_t2_s')
		elif card.id=='BG22_HERO_001p_t3':
			if not 'BG22_HERO_001p_t3_s' in target.sidequest_list0:
				target.sidequest_list0.append('BG22_HERO_001p_t3_s')
		elif card.id=='BG22_HERO_001p_t4':
			if not 'BG22_HERO_001p_t4_s' in target.sidequest_list0:
				target.sidequest_list0.append('BG22_HERO_001p_t4_s')
class BG22_HERO_001_Buddy_Deathrattle(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		controller = target.controller
		for cardId in target.sidequest_list0:
			for repeat in range(amount):
				Play(CONTROLLER,cardID).trigger(controller)
		pass
	pass
class BG22_HERO_001_Buddy:# <12>[1453]
	""" Spirit Raptor
	After you call upon a new Element, this remembers it.[Deathrattle:] Call upon those Elements. """
	events = Play(CONTROLLER).on(BG22_HERO_001_Buddy_Events(SELF, Play.CARD))
	deathrattle = BG22_HERO_001_Buddy_Deathrattle(SELF,1)
	pass
class BG22_HERO_001_Buddy_G:# <12>[1453]
	""" Spirit Raptor
	After you call upon a newElement, this remembers it.[Deathrattle:] Call upon thoseElements twice. """
	events = Play(CONTROLLER).on(BG22_HERO_001_Buddy_Events(SELF, Play.CARD))
	deathrattle = BG22_HERO_001_Buddy_Deathrattle(SELF,2)
	pass



##C'Thun   ### HP OK ###### BUDDY MAYBE #
BG_Hero1 += [
	'TB_BaconShop_HERO_29','TB_BaconShop_HP_104','TB_BaconShop_HP_104e',
	'TB_BaconShop_HERO_29_Buddy','TB_BaconShop_HERO_29_Buddy_e',
	'TB_BaconShop_HERO_29_Buddy_G','TB_BaconShop_HERO_29_Buddy_Ge',]#07#C'Thun]
BG_PoolSet_Hero1 +=['TB_BaconShop_HERO_29',]
BG_Hero1_Buddy['TB_BaconShop_HERO_29']='TB_BaconShop_HERO_29_Buddy'
BG_Hero1_Buddy_Gold['TB_BaconShop_HERO_29_Buddy']='TB_BaconShop_HERO_29_Buddy_G'
class TB_BaconShop_HERO_29:# <12>[1453]
	""" C'Thun	"""
class TB_BaconShop_HP_104_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF = ActionArg()
	def do(self, source, target, buff):
		if len(source.sidequest_list0)>0 and len(source.controller.field)>0:
			for repeat in range(source.script_data_num_1):
				target = random.choice(source.controller.field)
				Buff(target, buff).trigger(source)
			source.script_data_num_1 += 1
			source.sidequest_list0=[]
		pass
class TB_BaconShop_HP_104:
	""" Saturday C'Thuns!
	At end of turn, give a friendly minion +1/+1.__Repeat @ |4(time, times).<i>__(Upgrades after each use!)</i>"""
	def activate(self):
		self.sidequest_list0=[1]
	events = [
		BeginGame(CONTROLLER).on(SetScriptDataNum1(SELF, 1)),
		OWN_TURN_END.on(TB_BaconShop_HP_104_Action(SELF,'TB_BaconShop_HP_104e'))
	]
TB_BaconShop_HP_104e=buff(1,1)
######## BUDDY
class TB_BaconShop_HERO_29_Buddy_Action(TargetedAction):# <12>[1453]
	TARGET=ActionArg()
	def do(self, source, target):
		buff = target
		if buff.atk>0 or buff.max_health>0:
			Buff(source, 'TB_BaconShop_HERO_29_Buddy_e').trigger(source)
class TB_BaconShop_HERO_29_Buddy:# <12>[1453]
	""" Tentacle of C'Thun
	After a different friendly minion gains stats, gain_+1/+1 until your next turn. """
	events = [
		Buff(FRIENDLY + MINION - SELF).after(TB_BaconShop_HERO_29_Buddy_Action(Buff.BUFF)),
		BeginBar(CONTROLLER).on(RemoveBuff(SELF, 'TB_BaconShop_HERO_29_Buddy_e'))
	]
	pass
TB_BaconShop_HERO_29_Buddy_e=buff(1,1)# <12>[1453]
class TB_BaconShop_HERO_29_Buddy_G_Action(TargetedAction):# <12>[1453]
	TARGET=ActionArg()
	def do(self, source, target):
		buff = target
		if buff.atk>0 or buff.max_health>0:
			Buff(source, 'TB_BaconShop_HERO_29_Buddy_Ge').trigger(source)
class TB_BaconShop_HERO_29_Buddy_G:# <12>[1453]
	""" Tentacle of C'Thun
	After a different friendly minion gains stats, gain_+2/+2  until your next turn. """
	events = [
		Buff(FRIENDLY + MINION - SELF).after(TB_BaconShop_HERO_29_Buddy_G_Action(Buff.BUFF)),
		BeginBar(CONTROLLER).on(RemoveBuff(SELF, 'TB_BaconShop_HERO_29_Buddy_Ge'))
	]
	pass
TB_BaconShop_HERO_29_Buddy_Ge=buff(2,2)# <12>[1453]



##Captain Eudora   #### OK #### BUDDY MAYBE ###
BG_Hero1 += ['TB_BaconShop_HERO_64','TB_BaconShop_HP_074','TB_BaconShop_HERO_64_Buddy','TB_BaconShop_HERO_64_Buddy_e','TB_BaconShop_HERO_64_Buddy_G','TB_BaconShop_HERO_64_Buddy_G_e',]#08#Captain Eudora
BG_PoolSet_Hero1 +=['TB_BaconShop_HERO_64',]
BG_Hero1_Buddy['TB_BaconShop_HERO_64']='TB_BaconShop_HERO_64_Buddy'
BG_Hero1_Buddy_Gold['TB_BaconShop_HERO_64_Buddy']='TB_BaconShop_HERO_64_Buddy_G'
class TB_BaconShop_HERO_64:# <12>[1453]
	""" Captain Eudora
	"""
class TB_BaconShop_HP_074_Action(GameAction):
	def do(self, source):
		controller = source.controller
		gamemaster=controller.game.parent
		source.script_data_num_1 -= 1 
		if source.script_data_num_1== 0:
			source.script_data_num_1 = 5
			deck=[]
			for i in range(1, controller.tavern_tier+1):
				deck += gamemaster.BG_decks[i]
			goldcardid=gamemaster.BG_Gold[random.choice(deck)]
			if goldcardid:
				card = controller.card(goldcardid)
				card.zone=Zone.HAND

class TB_BaconShop_HP_074:
	""" Buried Treasure
	_Dig for a Golden minion! <i>(@ |4(Dig, Digs) left.)</i>"""
	#<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="5"/>
	activate = TB_BaconShop_HP_074_Action()
######## BUDDY
class TB_BaconShop_HERO_64_Buddy:
	""" Dagwik Stickytoe
	At the end of your turn, give a random friendly Golden minion +5/+5."""
	events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_MINIONS + GOLDEN), 'TB_BaconShop_HERO_64_Buddy_e'))
TB_BaconShop_HERO_64_Buddy_e=buff(5,5)# <12>[1453]
class TB_BaconShop_HERO_64_Buddy_G:
	""" Dagwik Stickytoe 
	At the end of your turn, give a random friendly Golden minion +10/+10. """
	events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_MINIONS + GOLDEN), 'TB_BaconShop_HERO_64_Buddy_G_e'))
TB_BaconShop_HERO_64_Buddy_G_e=buff(10,10)# <12>[1453]



##Captain Hooktusk  #### OK #### BUDDY MAYBE ###
BG_Hero1 += ['TB_BaconShop_HERO_67','TB_BaconShop_HP_075','TB_BaconShop_HERO_67_Buddy','TB_BaconShop_HERO_67_Buddy_G',]#09#Captain Hooktusk]
BG_PoolSet_Hero1 +=['TB_BaconShop_HERO_67',]
BG_Hero1_Buddy['TB_BaconShop_HERO_67']='TB_BaconShop_HERO_67_Buddy'
BG_Hero1_Buddy_Gold['TB_BaconShop_HERO_67_Buddy']='TB_BaconShop_HERO_67_Buddy_G'
class TB_BaconShop_HERO_67:# <12>[1453]
	""" Captain Hooktusk
	"""
class TB_BaconShop_HP_075_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = source.controller
		tier = max(target.tech_level-1, 1)
		amount=2
		if len([card for card in controller.field if card.id=='TB_BaconShop_HERO_67_Buddy'])>0:
			amount=3
		if len([card for card in controller.field if card.id=='TB_BaconShop_HERO_67_Buddy_G'])>0:
			amount=4
		Destroy(target).trigger(source)
		GenericChoice(controller, RandomBGAdmissible(tech_level=tier)*amount).trigger(source)
class TB_BaconShop_HP_075:
	""" Trash for Treasure
	Remove a friendly minion. Choose one of two from a Tavern Tier lower to keep."""
	requirements = {
		PlayReq.REQ_TARGET_TO_PLAY:0,
		PlayReq.REQ_MINION_TARGET:0,
		PlayReq.REQ_FRIENDLY_TARGET:0,
		}
	activate = TB_BaconShop_HP_075_Action(TARGET)
######## BUDDY
class TB_BaconShop_HERO_67_Buddy:# <12>[1453]
	""" Raging Contender
	'Trash for Treasure' offers 3 options instead of 2. """
	pass
class TB_BaconShop_HERO_67_Buddy_G:# <12>[1453]
	""" Raging Contender
	'Trash for Treasure' offers 4 options instead of 2. """
	pass



##Cariel Roame ### OK ### BUDDY MABY ###
BG_Hero1 += [
	'BG21_HERO_000','BG21_HERO_000e',
	'BG21_HERO_000p','BG21_HERO_000pe','BG21_HERO_000p2','BG21_HERO_000p3',
	'BG21_HERO_000_Buddy','BG21_HERO_000_Buddyt','BG21_HERO_000_Buddyt2',
	'BG21_HERO_000_Buddy_G','BG21_HERO_000_Buddy_Gt','BG21_HERO_000_Buddyt_Gt2']#10#Cariel Roame]
BG_PoolSet_Hero1 +=['BG21_HERO_000',]
BG_Hero1_Buddy['BG21_HERO_000']='BG21_HERO_000_Buddy'
BG_Hero1_Buddy_Gold['BG21_HERO_000_Buddy']='BG21_HERO_000_Buddy_G'
class BG21_HERO_000:# <5>[1453]
	""" Cariel Roame	"""
	pass
class BG21_HERO_000e:
	"""Cariel Watcher	"""
	pass
class BG21_HERO_000p_Action0(TargetedAction):
	TARGET = ActionArg()#controller
	BUFF = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, buff, amount):
		controller = target
		if amount >= len(controller.field):
			samples = controller.field
		else:
			samples = random.sample(controller.field, amount)
		atk=source.script_data_num_1
		hlt=source.script_data_num_2
		if len([cd for cd in controller.field if cd.id=='BG21_HERO_000_Buddyt'])>0:
			atk += 2
		elif len([cd for cd in controller.field if cd.id=='BG21_HERO_000_Buddyt2'])>0:
			hlt += 2
		elif len([cd for cd in controller.field if cd.id=='BG21_HERO_000_Buddy_Gt'])>0:
			atk += 4
		elif len([cd for cd in controller.field if cd.id=='BG21_HERO_000_Buddy_Gt2'])>0:
			hlt += 4
		for card in samples:
			Buff(card, buff, atk=atk, max_health=hlt).trigger(controller)
		pass
	pass
class BG21_HERO_000p_Action(TargetedAction):
	TARGET = ActionArg()#controller
	AMOUNT = IntArg()
	NEWPOWER = ActionArg()
	def do(self, source, target, amount, newpower):
		controller = target
		tier = controller.tavern_tier
		if tier==amount:
			ChangeHeroPower(controller, newpower).trigger(controller)
		pass

class BG21_HERO_000p:
	""" Conviction (Rank 1)
	Give two random friendly minions +{0}/+{1}. &lt;i&gt;(Upgrades at Tavern Tier 3.)&lt;/i&gt;"""
	#Give a random friendly minion +1/+1. <i>(Upgrades at Tavern Tier 3.)</i>""" ### old
	#<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="1"/>
	#<Tag enumID="3" name="TAG_SCRIPT_DATA_NUM_2" type="Int" value="1"/>
	activate = BG21_HERO_000p_Action0(CONTROLLER,'BG21_HERO_000pe',2)## 1 until 23.4.3, 
	events = UpgradeTier(CONTROLLER).on(BG21_HERO_000p_Action(CONTROLLER, 3, 'BG21_HERO_000p2')) 
	pass
BG21_HERO_000pe=buff(1,1)
class BG21_HERO_000p2:
	"""Conviction (Rank 2)
	Give three random friendly minions +1/+1. <i>(Upgrades at Tavern Tier 5.)</i>"""
	activate = BG21_HERO_000p_Action0(CONTROLLER,'BG21_HERO_000pe', 4)## 4 until 23.4.3
	events = UpgradeTier(CONTROLLER).on(BG21_HERO_000p_Action(CONTROLLER, 5, 'BG21_HERO_000p3')) 
	pass
class BG21_HERO_000p3:
	"""Conviction (Rank 3)
	Give five random _friendly minions +1/+1."""
	activate = BG21_HERO_000p_Action0(CONTROLLER,'BG21_HERO_000pe', 7)## 5 until 23.4.3
######## BUDDY
class BG21_HERO_000_Buddy:# <12>[1453]
	""" Captain Fairmount
	[Choose One] - 'Conviction' gives an additional +2 Attack for the rest of the game; or +2 Health."""
	### At the end of your turn, give five random friendly minions +1/+1. ### old
	###events = OWN_TURN_END.on(BuffRandomFriendlyMinion(CONTROLLER,'BG21_HERO_000_Buddy_e', 5))
	choose = ('BG21_HERO_000_Buddyt', 'BG21_HERO_000_Buddyt2')
	pass
class BG21_HERO_000_Buddyt:
	pass
class BG21_HERO_000_Buddyt2:
	pass
class BG21_HERO_000_Buddy_G:# <12>[1453]
	""" Captain Fairmount
	[Choose One] - 'Conviction' gives an additional +4 Attack for the rest of the game; or +4 Health."""
	###At the end of your turn, give five random friendly minions +2/+2. 
	###events = OWN_TURN_END.on(BuffRandomFriendlyMinion(CONTROLLER,'BG21_HERO_000_Buddy_G_e', 5))
	choose = ('BG21_HERO_000_Buddy_Gt', 'BG21_HERO_000_Buddy_Gt2')
	pass
class BG21_HERO_000_Buddy_Gt:
	pass
class BG21_HERO_000_Buddy_Gt2:
	pass


##Chenvaala ### HP OK ### BUDDY MAYBE ###
BG_Hero1 += ['TB_BaconShop_HERO_78','TB_BaconShop_HP_088','TB_BaconShop_HERO_78_Buddy','TB_BaconShop_HERO_78_Buddy_G',]#11#Chenvaala]
BG_PoolSet_Hero1 +=['TB_BaconShop_HERO_78',]
BG_Hero1_Buddy['TB_BaconShop_HERO_78']='TB_BaconShop_HERO_78_Buddy'
BG_Hero1_Buddy_Gold['TB_BaconShop_HERO_78_Buddy']='TB_BaconShop_HERO_78_Buddy_G'
class TB_BaconShop_HERO_78:# <12>[1453]
	""" Chenvaala
	"""
class TB_BaconShop_HP_088:
	""" Avalanche
	[Passive] After you play 3 Elementals, reduce the cost of upgrading Bob's Tavern by (3)."""
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(SidequestCounter(SELF, 3, [ReduceTierUpCost(CONTROLLER, 3)]))
#### BUDDY ####
class TB_BaconShop_HERO_78_Buddy_Action(GameAction):
	def do(self, source):
		controller = source.controller
		bartender = controller.opponent
		newcard = RandomBGElemental().evaluate(source)
		newcard = get00(newcard)
		newcard.frozen=True
		newcard.zone=Zone.SETASIDE
		newcard.controller=bartender
		newcard.zone=Zone.PLAY
class TB_BaconShop_HERO_78_Buddy:
	""" Snow Elemental
	Bob always offers an extra [Frozen] Elemental whenever the Tavern is [Refreshed]."""
	events = Rerole(CONTROLLER).after(TB_BaconShop_HERO_78_Buddy_Action())
class TB_BaconShop_HERO_78_Buddy_G:
	""" Snow Elemental
	Bob always offers 2 extra [Frozen] Elementals whenever the Tavern is [Refreshed]."""
	events = Rerole(CONTROLLER).after(TB_BaconShop_HERO_78_Buddy_Action(), TB_BaconShop_HERO_78_Buddy_Action())



##Cookie the Cook  #### HP NG ###  
BG_Hero1 += ['BG21_HERO_020','BG21_HERO_020p','BG21_HERO_020_Buddy','BG21_HERO_020_Buddy_G',]#12#Cookie the Cook]
BG_PoolSet_Hero1 +=['BG21_HERO_020',]
BG_Hero1_Buddy['BG21_HERO_020']='BG21_HERO_020_Buddy'
BG_Hero1_Buddy_Gold['BG21_HERO_020_Buddy']='BG21_HERO_020_Buddy_G'
class BG21_HERO_020:# <12>[1453]
	""" Cookie the Cook
	 """
	pass
class BG21_HERO_020p_Choice(Choice):
	def choose(self, card):
		self.source.sidequest_counter += 1
		if self.source.sidequest_counter>=self.source.choice_limit:		
			self.next_choice=None
		else:
			cards=[]
			tier=self.source.controller.tavern_tier
			for rc in self.source.sidequest_list0:
				newcard = RandomBGMinion(race=rc, tech_level_less=tier).evaluate(self.source)
				newcard=get00(newcard)
				cards.append(newcard.id)
				newcard.discard()
			self.next_choice=BG21_HERO_020p_Choice(self.player, RandomID(*cards)*3)
			self.next_choice.trigger(self.source)
		super().choose(card)
		card.zone=Zone.SETASIDE
		card.controller=self.player
		card.zone=Zone.HAND
class BG21_HERO_020p_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller=source.controller
		Destroy(target).trigger(source)
		if len(source.sidequest_list0)>=3:
			source.sidequest_list0=[]
		source.sidequest_list0.append(target.race)
		source.script_data_num_1 -= 1 
		if source.script_data_num_1== 0:
			source.choice_limit=1
			if len([cd for cd in controller.field if cd.id=="BG21_HERO_020_Buddy"]):
				source.choice_limit+=1
			if len([cd for cd in controller.field if cd.id=="BG21_HERO_020_Buddy_G"]):
				source.choice_limit+=2
			source.script_data_num_1 = 3
			cards=[]
			tier=source.controller.tavern_tier
			for rc in source.sidequest_list0:
				newcard = RandomBGMinion(race=rc, tech_level_less=tier).evaluate(source)
				newcard=get00(newcard)
				cards.append(newcard.id)
				newcard.discard()
			BG21_HERO_020p_Choice(controller, RandomID(*cards)*3).trigger(source)

class BG21_HERO_020p:# <12>[1453] ####### difficult
	""" Stir the Pot
	Throw a minion in your pot. When you've gathered 3,[Discover] from their minion types. <i>(@ left!)</i> """
	requirements = {
		PlayReq.REQ_TARGET_TO_PLAY:0,
		PlayReq.REQ_MINION_TARGET:0,
		1002:Race.INVALID,# REQ_TARGET_WITHOUT_RACE
		}
	activate = BG21_HERO_020p_Action(TARGET)
	pass
######## BUDDY
class BG21_HERO_020_Buddy:# <12>[1453]
	""" Sous Chef
	You can use your Hero Power an extra time each_turn. """
	pass
class BG21_HERO_020_Buddy_G:# <12>[1453]
	""" Sous Chef
	You can use your Hero Power 2 extra times each_turn. """
	#
	pass



##Dancin' Deryl ### HP maybe ### ## BUDDY MAYBE #
BG_Hero1 += ['TB_BaconShop_HERO_36','TB_BaconShop_HP_042','TB_BaconShop_HP_042e','TB_BaconShop_HERO_36_Buddy','TB_BaconShop_HERO_36_Buddy_e','TB_BaconShop_HERO_36_Buddy_G','TB_BaconShop_HERO_36_Buddy_Ge',]#13#Dancin' Deryl]
BG_PoolSet_Hero1 +=['TB_BaconShop_HERO_36']
BG_Hero1_Buddy['TB_BaconShop_HERO_36']='TB_BaconShop_HERO_36_Buddy'
BG_Hero1_Buddy_Gold['TB_BaconShop_HERO_36_Buddy']='TB_BaconShop_HERO_36_Buddy_G'
class TB_BaconShop_HERO_36:# <12>[1453]
	""" Dancin' Deryl
	 """
class TB_BaconShop_HP_042:
	""" Hat Trick
	[Passive.] After you sell a minion, randomly give a minion in Bob's Tavern +1/+1 three times."""
	events = Sell(CONTROLLER).after(Buff(RANDOM(ENEMY_MINIONS), 'TB_BaconShop_HERO_36_Buddy_e')*3)
TB_BaconShop_HP_042e=buff(1,1)
class TB_BaconShop_HERO_36_Buddy:# <12>[1453]
	""" Asher the Haberdasher
	After you sell a minion, gain +1/+1. """
	events = Sell(CONTROLLER).after(Buff(SELF, 'TB_BaconShop_HERO_36_Buddy_e'))
	pass
TB_BaconShop_HERO_36_Buddy_e=buff(1,1)# <12>[1453]
""" Dashing Hat,+1/+1. """
class TB_BaconShop_HERO_36_Buddy_G:# <12>[1453]
	""" Asher the Haberdasher
	After you sell a minion, gain +2/+2. """
	events = Sell(CONTROLLER).after(Buff(SELF, 'TB_BaconShop_HERO_36_Buddy_Ge'))
	pass
TB_BaconShop_HERO_36_Buddy_Ge=buff(2,2)# <12>[1453]
""" Dashing Hat,+2/+2. """


##Death Speaker Blackthorn  ### HP OK ### ## BUDDY MAYBE #
BG_Hero1 += ['BG20_HERO_103','BG20_HERO_103p','BG20_HERO_103_Buddy','BG20_HERO_103_Buddy_G',]#14#Death Speaker Blackthorn]
BG_PoolSet_Hero1 +=['BG20_HERO_103',]
BG_Hero1_Buddy['BG20_HERO_103']='BG20_HERO_103_Buddy'
BG_Hero1_Buddy_Gold['BG20_HERO_103_Buddy']='BG20_HERO_103_Buddy_G'
class BG20_HERO_103:# <12>[1453]
	""" Death Speaker Blackthorn	 """
class BG20_HERO_103p:# <12>[1453]
	""" Bloodbound
	[Passive]After you upgrade Bob's Tavern, gain 2 [Blood Gems]. """
	tags={GameTag.HIDE_COST:True}
	events = UpgradeTier(CONTROLLER).on(Give(CONTROLLER, 'BG20_GEM')*2)
	pass
########  BUDDY
class BG20_HERO_103_Buddy:
	""" Death's Head Sage
	After you gain a [Blood Gem], gain an extra one. """
	events = Give(CONTROLLER, ID('BG20_GEM')).after(Give(CONTROLLER, 'BG20_GEM'))
class BG20_HERO_103_Buddy_G:
	""" Death's Head Sage
	After you gain a [Blood Gem], gain two extra. """
	events = Give(CONTROLLER, ID('BG20_GEM')).after(Give(CONTROLLER, 'BG20_GEM')*2)



##Deathwing    ## HP OK ## BUDDY MAYBE #
BG_Hero1 += ['TB_BaconShop_HERO_52','TB_BaconShop_HP_061','TB_BaconShop_HP_061e','TB_BaconShop_HERO_52_Buddy','TB_BaconShop_HERO_52_Buddy_e','TB_BaconShop_HERO_52_Buddy_G','TB_BaconShop_HERO_52_Buddy_G_e',]
BG_PoolSet_Hero1 +=['TB_BaconShop_HERO_52',]
BG_Hero1_Buddy['TB_BaconShop_HERO_52']='TB_BaconShop_HERO_52_Buddy'
BG_Hero1_Buddy_Gold['TB_BaconShop_HERO_52_Buddy']='TB_BaconShop_HERO_52_Buddy_G'
class TB_BaconShop_HERO_52:
	""" Deathwing
	"""
class TB_BaconShop_HP_061:
	""" ALL Will Burn!
	[x][Passive] ALL minions have +3 Attack."""
	update = Refresh(ALL_MINIONS, buff='TB_BaconShop_HP_061e')
#TB_BaconShop_HP_061e=buff(2,0) ## until 24.0
TB_BaconShop_HP_061e=buff(3,0) ## 24.0.3
########  BUDDY
class TB_BaconShop_HERO_52_Buddy:
	""" Lady Sinestra
	Your minions have +3_Attack. """
	update = Refresh(FRIENDLY_MINIONS, buff='TB_BaconShop_HERO_52_Buddy_e')
TB_BaconShop_HERO_52_Buddy_e=buff(3,0)
class TB_BaconShop_HERO_52_Buddy_G:
	""" Lady Sinestra
	Your minions have +6_Attack. """
	update = Refresh(FRIENDLY_MINIONS, buff='TB_BaconShop_HERO_52_Buddy_G_e')
TB_BaconShop_HERO_52_Buddy_G_e=buff(6,0)



##Dinotamer Brann   ### HP OK ### BUDDY MAYBE ###
BG_Hero1 += [
	'TB_BaconShop_HERO_43','TB_BaconShop_HP_048','TB_BaconShop_HP_048e',
	'TB_BaconShop_HERO_43_Buddy','TB_BaconShop_HERO_43_Buddy_G',
	]#16#Dinotamer Brann]
BG_PoolSet_Hero1 +=['TB_BaconShop_HERO_43',]
BG_Hero1_Buddy['TB_BaconShop_HERO_43']='TB_BaconShop_HERO_43_Buddy'
BG_Hero1_Buddy_Gold['TB_BaconShop_HERO_43_Buddy']='TB_BaconShop_HERO_43_Buddy_G'
class TB_BaconShop_HERO_43:# <12>[1453]
	""" Dinotamer Brann
	 """
class TB_BaconShop_HP_048:
	""" Battle Brand
	[Passive.] After you buy 5 [Battlecry] minions, add Brann Bronzebeard to your _hand. <i>(Once per game.)</i>@[x][Passive.] After you buy 5 [Battlecry] minions, add Brann Bronzebeard to your hand. <i>({0} left!)</i>"""
	events = Buy(CONTROLLER, MINION + BATTLECRY).on(SidequestCounterText0(SELF, 5, \
		[Give(CONTROLLER,"BG_LOE_077"), SetAttr(SELF,'cant_play',True)]))
class TB_BaconShop_HP_048e:
	""" 	"""
######## BUDDY
class TB_BaconShop_HERO_43_Buddy_Action(TargetedAction):
	TARGET = ActionArg()
	CARD = CardArg()
	def do(self, source, target, card):
		controller = target
		if isinstance(card,list):
			card = card[0]
		Summon(controller, card).trigger(controller)
		Give(controller.deepcopy_original, card.id).trigger(controller)
		pass
class TB_BaconShop_HERO_43_Buddy:# <12>[1453]
	""" Brann's Epic Egg
	[Taunt]. [Deathrattle:] Summon a random [Battlecry] minion and add a copy of it to your hand. """
	deathrattle = TB_BaconShop_HERO_43_Buddy_Action(CONTROLLER, RandomBGAdmissible(has_battlecry=True, tech_level_less=TIER(CONTROLLER)))
	pass
class TB_BaconShop_HERO_43_Buddy_G:# <12>[1453]
	""" Brann's Epic Egg
	[Taunt]. [Deathrattle:] Summon2 random [Battlecry] minionsand add copies of themto your hand. """
	deathrattle = (\
		Summon(CONTROLLER, RandomBGAdmissible(has_battlecry=True)).then(Give(CONTROLLER,Copy(Summon.CARD))),\
		Summon(CONTROLLER, RandomBGAdmissible(has_battlecry=True)).then(Give(CONTROLLER,Copy(Summon.CARD)))\
	)
	pass


##Drek'Thar #BG22_HERO_002   ### HP OK ### visually checked 23/4/6
BG_Hero1+=['BG22_HERO_002','BG22_HERO_002p','BG22_HERO_002pe',
		'BG22_HERO_002_Buddy','BG22_HERO_002_Buddy_e',
		'BG22_HERO_002_Buddy_G','BG22_HERO_002_Buddy_Ge'
		]
BG_PoolSet_Hero1+=['BG22_HERO_002']
BG_Hero1_Buddy['BG22_HERO_002']='BG22_HERO_002_Buddy'
BG_Hero1_Buddy_Gold['BG22_HERO_002_Buddy']='BG22_HERO_002_Buddy_G'
class BG22_HERO_002:# <12>[1453]
	""" Drek'Thar 	 """
class BG22_HERO_002p_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		controller = target.controller
		highest_atk = 0
		for card in controller.field:
			if highest_atk <card.atk:
				highest_atk = card.atk
		Buff(target, buff, atk=highest_atk-target.atk).trigger(controller)
class BG22_HERO_002p_Action2(GameAction):
	def do(self, source):
		controller=source.controller
		cards = [card for card in controller.field if card.type==CardType.MINION]
		for card in cards:
			BuffPermanently(card, 'BG22_HERO_002pe').trigger(source)
		pass
class BG22_HERO_002p:# <12>[1453]
	""" Lead the Frostwolves
	[Passive] [Avenge (3):] Give your minions +1 Attack permanently.""" ### new 24.2
	events = Death(FRIENDLY + MINION).on(Avenge(SELF, 3, [BG22_HERO_002p_Action2()]))
	##Choose a friendly minion.It copies the Attack of your highest Attack minion for next combat only. (until 23.4.3)
	##Choose a minion. It copies the Attack of the highest Attack minion until next turn.(until 24.0.3)
	#requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, 
	#			 #PlayReq.REQ_FRIENDLY_TARGET:0, ## valid until 23.4.3 
	#			 PlayReq.REQ_MINION_TARGET:0}
	#activate = BG22_HERO_002p_Action(TARGET, 'BG22_HERO_002pe')
	pass
BG22_HERO_002pe=buff(1,0)
#class BG22_HERO_002pe:# <12>[1453]
#	""" Frostwolf Fervor
#	Copied highest Attack. """
#	events = EndBattle(CONTROLLER).on(Destroy(SELF))
#	pass
class BG22_HERO_002pe2:# <12>[1453]
	""" Attack Set Next Combat Only
	 """
	pass
class BG22_HERO_002pe3:# <12>[1453]
	""" Modified Attack Next Combat Only
	Attack is increased or decreased for next combat only. """
	pass
###### Buddy ######
class BG22_HERO_002_Buddy:# <12>[1453]
	""" Frostwolf Lieutenant
	[Avenge (2):] Give your minions +1 Attack permanently. """
	events=Death(FRIENDLY + MINION).on(Avenge(SELF, 2, [BuffPermanently(FRIENDLY_MINIONS, 'BG22_HERO_002_Buddy_e')]))
	pass
BG22_HERO_002_Buddy_e=buff(1,0)# <12>[1453]
""" Lieutenant's Leadership, +1 Attack. """
class BG22_HERO_002_Buddy_G:# <12>[1453]
	""" Frostwolf Lieutenant
	[Avenge (2):] Give your minions +2 Attack permanently. """
	events = Death(FRIENDLY + MINION).on(Avenge(SELF, 2, [BuffPermanently(FRIENDLY_MINIONS, 'BG22_HERO_002_Buddy_Ge')]))
	pass
BG22_HERO_002_Buddy_Ge=buff(2,0)# <12>[1453]
""" Lieutenant's Leadership,+2 Attack. """



#################################################




	
	
