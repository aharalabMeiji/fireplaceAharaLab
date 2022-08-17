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

BG_Hero1=[
	'TB_BaconShop_HERO_16','TB_BaconShop_HP_044','TB_BaconShop_HERO_16_Buddy','TB_BaconShop_HERO_16_Buddy_e','TB_BaconShop_HERO_16_Buddy_G','TB_BaconShop_HERO_16_Buddy_G_e',#00#A. F. Kay 
	'TB_BaconShop_HERO_76','TB_BaconShop_HP_086','TB_BaconShop_HERO_76_Buddy','TB_BaconShop_HERO_76_Buddy_e','TB_BaconShop_HERO_76_Buddy_G',#01#Al'Akir
	'TB_BaconShop_HERO_56','TB_BaconShop_HP_064','TB_BaconShop_HERO_56_Buddy',#02#Alexstrasza
	'BG22_HERO_201','BG22_HERO_201p','BG22_HERO_201pe','BG22_HERO_201_Buddy','BG22_HERO_201_Buddy_G',#03#Ambassador Faelin
	'TB_BaconShop_HERO_59','TB_BaconShop_HP_065','TB_BaconShop_HP_065pe','TB_BaconShop_HP_065t2','TB_BaconShop_HERO_59_Buddy','TB_BaconShop_HERO_59_Buddy_G','TB_BaconShop_HERO_59t',#04#Aranna Starseeker
	'TB_BaconShop_HERO_45','TB_BaconShop_HP_053','TB_BaconShop_HERO_45_Buddy','TB_BaconShop_HERO_45_Buddy_G',#05#Arch-Villain Rafaam
	'BG22_HERO_001','BG22_HERO_001p','BG22_HERO_001p_t1','BG22_HERO_001p_t1_s','BG22_HERO_001p_t1e','BG22_HERO_001p_t1et','BG22_HERO_001p_t2','BG22_HERO_001p_t2_s','BG22_HERO_001p_t2e','BG22_HERO_001p_t3','BG22_HERO_001p_t3_s','BG22_HERO_001p_t3e','BG22_HERO_001p_t4','BG22_HERO_001p_t4_s','BG22_HERO_001_Buddy','BG22_HERO_001_Buddy_e','BG22_HERO_001_Buddy_e1','BG22_HERO_001_Buddy_e2','BG22_HERO_001_Buddy_e3','BG22_HERO_001_Buddy_e4','BG22_HERO_001_Buddy_G',#BG22_HERO_001#06#Bru'kan
	'TB_BaconShop_HERO_29','TB_BaconShop_HP_104','TB_BaconShop_HP_104e','TB_BaconShop_HERO_29_Buddy','TB_BaconShop_HERO_29_Buddy_e','TB_BaconShop_HERO_29_Buddy_G','TB_BaconShop_HERO_29_Buddy_Ge',#07#C'Thun
	'TB_BaconShop_HERO_64','TB_BaconShop_HP_074','TB_BaconShop_HERO_64_Buddy','TB_BaconShop_HERO_64_Buddy_e','TB_BaconShop_HERO_64_Buddy_G','TB_BaconShop_HERO_64_Buddy_G_e',#08#Captain Eudora
	'TB_BaconShop_HERO_67','TB_BaconShop_HP_075','TB_BaconShop_HERO_67_Buddy','TB_BaconShop_HERO_67_Buddy_G',#09#Captain Hooktusk
	'BG21_HERO_000','BG21_HERO_000e','BG21_HERO_000p','BG21_HERO_000pe','BG21_HERO_000p2','BG21_HERO_000p3','BG21_HERO_000_Buddy','BG21_HERO_000_Buddy_e','BG21_HERO_000_Buddy_G','BG21_HERO_000_Buddy_G_e',#10#Cariel Roame
	'TB_BaconShop_HERO_78','TB_BaconShop_HP_088','TB_BaconShop_HERO_78_Buddy','TB_BaconShop_HERO_78_Buddy_G',#11#Chenvaala
	'BG21_HERO_020','BG21_HERO_020p','BG21_HERO_020_Buddy','BG21_HERO_020_Buddy_G',#12#Cookie the Cook
	'TB_BaconShop_HERO_36','TB_BaconShop_HP_042','TB_BaconShop_HP_042e','TB_BaconShop_HERO_36_Buddy','TB_BaconShop_HERO_36_Buddy_e','TB_BaconShop_HERO_36_Buddy_G','TB_BaconShop_HERO_36_Buddy_Ge',#13#Dancin' Deryl
	'BG20_HERO_103','BG20_HERO_103p','BG20_HERO_103_Buddy','BG20_HERO_103_Buddy_G',#14#Death Speaker Blackthorn
	'TB_BaconShop_HERO_52','TB_BaconShop_HP_061','TB_BaconShop_HP_061e','TB_BaconShop_HERO_52_Buddy','TB_BaconShop_HERO_52_Buddy_e','TB_BaconShop_HERO_52_Buddy_G','TB_BaconShop_HERO_52_Buddy_G_e',#15#Deathwing
	'TB_BaconShop_HERO_43','TB_BaconShop_HP_048','TB_BaconShop_HP_048e','TB_BaconShop_HERO_43_Buddy','TB_BaconShop_HERO_43_Buddy_G',#16#Dinotamer Brann
]

BG_PoolSet_Hero1=[
	'TB_BaconShop_HERO_16',#00
	'TB_BaconShop_HERO_76',#01
	'TB_BaconShop_HERO_56',#02#2 dragon ban
	'BG22_HERO_201',#03
	'TB_BaconShop_HERO_59',#04
	'TB_BaconShop_HERO_45',#05
	#'BG22_HERO_001',#06
	'TB_BaconShop_HERO_29',#07
	'TB_BaconShop_HERO_64',#08
	'TB_BaconShop_HERO_67',#09
	'BG21_HERO_000',#10
	'TB_BaconShop_HERO_78',#11 elemental ban
	'BG21_HERO_020',#12
	'TB_BaconShop_HERO_36',#13
	'BG20_HERO_103',#14
	#'TB_BaconShop_HERO_52',#15
	'TB_BaconShop_HERO_43',#16
	]

BG_Hero1_Buddy={
	'TB_BaconShop_HERO_16':'TB_BaconShop_HERO_16_Buddy',#00#A. F. Kay 
	'TB_BaconShop_HERO_76':'TB_BaconShop_HERO_76_Buddy',#01#Al'Akir
	'TB_BaconShop_HERO_56':'TB_BaconShop_HERO_56_Buddy',#02#Alexstrasza
	'BG22_HERO_201':'BG22_HERO_201_Buddy',#03#Ambassador Faelin
	'TB_BaconShop_HERO_59':'TB_BaconShop_HERO_59_Buddy',#04#Aranna 
	'TB_BaconShop_HERO_45':'TB_BaconShop_HERO_45_Buddy',#05#Arch-Villain Rafaam
	'BG22_HERO_001':'BG22_HERO_001_Buddy',#BG22_HERO_001#06#Bru'kan
	'TB_BaconShop_HERO_29':'TB_BaconShop_HERO_29_Buddy',#07#C'Thun
	'TB_BaconShop_HERO_64':'TB_BaconShop_HERO_64_Buddy',#08#Captain Eudora
	'TB_BaconShop_HERO_67':'TB_BaconShop_HERO_67_Buddy',#09#Captain Hooktusk
	'BG21_HERO_000':'BG21_HERO_000_Buddy',#10#Cariel Roame
	'TB_BaconShop_HERO_78':'TB_BaconShop_HERO_78_Buddy',#11#Chenvaala
	'BG21_HERO_020':'BG21_HERO_020_Buddy',#12#Cookie the Cook
	'TB_BaconShop_HERO_36':'TB_BaconShop_HERO_36_Buddy',#13#Dancin' Deryl
	'BG20_HERO_103':'BG20_HERO_103_Buddy',#14#Death Speaker Blackthorn
	'TB_BaconShop_HERO_52':'TB_BaconShop_HERO_52_Buddy',#15#Deathwing
	'TB_BaconShop_HERO_43':'TB_BaconShop_HERO_43_Buddy',#16#Dinotamer Brann
	}

BG_Hero1_Buddy_Gold={
	'TB_BaconShop_HERO_16_Buddy':'TB_BaconShop_HERO_16_Buddy_G',#
	'TB_BaconShop_HERO_76_Buddy':'TB_BaconShop_HERO_76_Buddy_G',#
	'TB_BaconShop_HERO_56_Buddy':'TB_BaconShop_HERO_56_Buddy_G',#
	'BG22_HERO_201_Buddy':'BG22_HERO_201_Buddy_G',#
	'TB_BaconShop_HERO_59_Buddy':'TB_BaconShop_HERO_59_Buddy_G',#
	'TB_BaconShop_HERO_45_Buddy':'TB_BaconShop_HERO_45_Buddy_G',#
	'BG22_HERO_001_Buddy':'BG22_HERO_001_Buddy_G',##
	'TB_BaconShop_HERO_29_Buddy':'TB_BaconShop_HERO_29_Buddy_G',#
	'TB_BaconShop_HERO_64_Buddy':'TB_BaconShop_HERO_64_Buddy_G',#
	'TB_BaconShop_HERO_67_Buddy':'TB_BaconShop_HERO_67_Buddy_G',#
	'BG21_HERO_000_Buddy':'BG21_HERO_000_Buddy_G',#
	'TB_BaconShop_HERO_78_Buddy':'TB_BaconShop_HERO_78_Buddy_G',#
	'BG21_HERO_020_Buddy':'BG21_HERO_020_Buddy_G',#
	'TB_BaconShop_HERO_36_Buddy':'TB_BaconShop_HERO_36_Buddy_G',#
	'BG20_HERO_103_Buddy':'BG20_HERO_103_Buddy_G',#
	'TB_BaconShop_HERO_52_Buddy':'TB_BaconShop_HERO_52_Buddy_G',#
	'TB_BaconShop_HERO_43_Buddy':'TB_BaconShop_HERO_43_Buddy_G',#
	}


########### source


#00#A. F. Kay   ### OK ###
class TB_BaconShop_HERO_16:# <12>[1453]
	""" A. F. Kay	 """
	pass
class TB_BaconShop_HP_044_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		bar = target.game
		turn = bar.turn
		if turn==1 or turn==2:
			SetMaxMana(controller,0).trigger(bar)
		if turn==3:
			SetMaxMana(controller,5).trigger(bar)
			DiscoverTwice(controller, RandomBGMinion(tech_level = 3)*3).trigger(source)#tech_level=3
class TB_BaconShop_HP_044:#<12>[1453]
	""" Procrastinate
	<b>Passive</b> Skip your first two turns.Start with two minions from Tavern Tier 3."""
	events = BeginBar(CONTROLLER).on(TB_BaconShop_HP_044_Action(CONTROLLER))
	pass
class TB_BaconShop_HERO_16_Buddy:# <12>[1453]
	""" Snack Vendor
	At the end of your turn, give your Tavern Tier 3 minions +1/+2. """
	events = OWN_TURN_END.on(Buff(FRIENDLY_MINIONS + TIER3, 'TB_BaconShop_HERO_16_Buddy_e'))
	pass
TB_BaconShop_HERO_16_Buddy_e=buff(1,2)# <12>[1453]
""" Snack-Filled
+1/+2. """
class TB_BaconShop_HERO_16_Buddy_G:# <12>[1453]
	""" Snack Vendor
	At the end of your turn, give your Tavern Tier 3 minions +2/+4. """
	events = OWN_TURN_END.on(Buff(FRIENDLY_MINIONS + TIER3, 'TB_BaconShop_HERO_16_Buddy_G_e'))
	pass
TB_BaconShop_HERO_16_Buddy_G_e=buff(2,4)# <12>[1453]
""" Snack-Filled
+2/+4. """


#01#Al'Akir  ### OK ###
class TB_BaconShop_HERO_76:# <12>[1453]
	""" Al'Akir	 """
class TB_BaconShop_HP_086_Action(TargetedAction):
	TARGET = ActionArg()# controller
	def do(self, source, target):
		if len(target.field)>0:
			card = target.field[0]
			card.windfury=1
			card.divine_shield=True
			card.taunt=True
class TB_BaconShop_HP_086:
	""" Swatting Insects
	<b>Passive</b><b>Start of Combat:</b> Give yourleft-most minion <b>Windfury</b>,___<b>Divine Shield</b>, and <b>Taunt</b>."""
	events = BeginBattle(CONTROLLER).on(TB_BaconShop_HP_086_Action(CONTROLLER))
	pass
class TB_BaconShop_HP_086_BuddyAction(TargetedAction):
	TARGET = ActionArg()# target
	def do(self, source, target):
		if not isinstance(target,list):
			target = [target]
		for card in target:
			card.windfury=1
			card.divine_shield=True
			card.taunt=True
class TB_BaconShop_HERO_76_Buddy:
	"""Spirit of Air
	<b>Deathrattle:</b> Give a random friendly minion <b>Windfury</b>,___<b>Divine Shield</b>, and <b>Taunt</b>.___"""
	deathrattle = TB_BaconShop_HP_086_BuddyAction(RANDOM_FRIENDLY_MINION)
	pass
class TB_BaconShop_HERO_76_Buddy_e:# <12>[1453]
	""" Blessing of Air,[Windfury], [Divine Shield], and [Taunt]. """
class TB_BaconShop_HERO_76_Buddy_G:
	""" Spirit of Air
	<b>Deathrattle:</b> Give 2 random friendly minions <b>Windfury</b>,<b>Divine Shield</b>, and <b>Taunt</b>."""
	deathrattle =  TB_BaconShop_HP_086_BuddyAction(RANDOM_FRIENDLY_MINION) * 2
	pass



#02#Alexstrasza   ### OK ###
class TB_BaconShop_HERO_56:# <12>[1453]
	""" Alexstrasza	"""
class TB_BaconShop_HP_064_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		if target.tavern_tier==5:
			DiscoverTwice(controller, RandomBGDragon()*3).trigger(source)
class TB_BaconShop_HP_064:
	""" Queen of Dragons
	<b>Passive</b>After you upgrade Bob's Tavern to Tavern Tier 5,_<b>Discover</b> two Dragons."""
	events = UpgradeTier(CONTROLLER).on(TB_BaconShop_HP_064_Action(UpgradeTier.TARGET))
	pass
class TB_BaconShop_HERO_56_Buddy:
	""" Vaelastrasz
	<b>Battlecry:</b> Add a random Dragon of your Tavern Tier to your hand."""
	play = Give(CONTROLLER, RandomBGDragon(tech_level=TIER(CONTROLLER)))
class TB_BaconShop_HERO_56_Buddy_G:
	""" Vaelastrasz
	<b>Battlecry:</b> Add two random Dragons of your Tavern Tier to your hand."""
	play = Give(CONTROLLER, RandomBGDragon(tech_level=TIER(CONTROLLER))) * 2



#03##Ambassador Faelin ### OK ###
class BG22_HERO_201:# <12>[1453]
	""" Ambassador Faelin	"""
class BG22_HERO_201p_Choice(Choice):
	def choose(self, card):
		source = self.source
		source._sidequest_counter_ += 1
		if source._sidequest_counter_>=3:
			self.next_choice=None
		else:
			self.next_choice=self
		super().choose(card)
		card.zone = Zone.HAND
		cards = self._args[1]
		if source._sidequest_counter_==1:
			Buff(card, 'BG22_HERO_201pe').trigger(source)		
			cards = RandomBGMinion(tech_level=4)*3
		elif source._sidequest_counter_==2:
			Buff(card, 'BG22_HERO_201pe').trigger(source)		
			cards = RandomBGMinion(tech_level=6)*3
		elif source._sidequest_counter_==3:
			Buff(card, 'BG22_HERO_201pe').trigger(source)	
			pass	
		if isinstance(cards, LazyValue):
			self.cards = cards.evaluate(source)
class BG22_HERO_201p_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		bar = target.game
		turn = bar.turn
		if turn==1:
			controller.max_mana = 0
			BG22_HERO_201p_Choice(controller, RandomBGMinion(tech_level=2)*3).trigger(source)
		if turn==2:# maybe no need
			controller.max_mana = 4# maybe no need
		pass
class BG22_HERO_201p:# <12>[1453]
	""" Expedition Plans
	[Passive.] Skip your first turn. [Discover] a Tier 2, 4, and 6 minion to get at those Tiers. """
	events = BeginBar(CONTROLLER).on(BG22_HERO_201p_Action(CONTROLLER))
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
	events = UpgradeTier(CONTROLLER).on(BG22_HERO_201pe_Action(OWNER,Destroy(SELF)))
	pass
class BG22_HERO_201_Buddy:# <12>[1453]
	""" Submersible Chef
	[Battlecry:] Add a random Tier 1, 3, and 5 minion to your hand. """
	play = (
		Give(CONTROLLER, RandomBGMinion(tech_level=1)),
		Give(CONTROLLER, RandomBGMinion(tech_level=3)),
		Give(CONTROLLER, RandomBGMinion(tech_level=5)),)
	pass
class BG22_HERO_201_Buddy_G:# <12>[1453]
	""" Submersible Chef
	[Battlecry:] Add a random Tier 1, 3, and 5 minion to your hand twice. """
	play = (
		Give(CONTROLLER, RandomBGMinion(tech_level=1)),
		Give(CONTROLLER, RandomBGMinion(tech_level=3)),
		Give(CONTROLLER, RandomBGMinion(tech_level=5)),
		Give(CONTROLLER, RandomBGMinion(tech_level=1)),
		Give(CONTROLLER, RandomBGMinion(tech_level=3)),
		Give(CONTROLLER, RandomBGMinion(tech_level=5)),)
	pass



#04#Aranna Starseeker # アランナ ### OK ###
class TB_BaconShop_HERO_59:# <12>[1453]
	""" Aranna Starseeker
	"""
class TB_BaconShop_HP_065:
	""" Demon Hunter Training
	<b>Passive</b> After you <b>Refresh</b> 5 times, Bob always has 7 minions.
<i>(@ left!)</i>"""
	events = Rerole(CONTROLLER).on(SidequestCounter(SELF, 5, \
		[ ChangeHeroPower(CONTROLLER, 'TB_BaconShop_HP_065t2'),\
		SetAttr(CONTROLLER, 'len_bobs_field', 7)]\
		))
	pass
class TB_BaconShop_HP_065pe:
	"""  Aranna Watcher
	"""
class TB_BaconShop_HP_065t2:### 条件が満たされるとヒロパが交代になる
	""" Spectral Sight
	<b>Passive</b>Bob's Tavern refreshes with 7 minions."""
class TB_BaconShop_HERO_59_Buddy:# <12>[1453]
	""" Sklibb, Demon Hunter
	After you play a minion,your next [Refresh] costs (0). """
	events = BG_Play(CONTROLLER, MINION).on(GetFreeRerole(CONTROLLER))
	pass
class TB_BaconShop_HERO_59_Buddy_G:# <12>[1453]
	""" Sklibb, Demon Hunter
	After you play a minion, your next two [Refreshes] cost (0). """
	events = BG_Play(CONTROLLER, MINION).after(GetFreeRerole(CONTROLLER) * 2)
	pass
class TB_BaconShop_HERO_59t:# <12>[1453]
	""" Aranna, Unleashed ヒロパ交代後のヒーロー
	"""
	pass



#05#Arch-Villain Rafaam ### OK ###
class TB_BaconShop_HERO_45:# <12>[1453]
	""" Arch-Villain Rafaam
	"""
class TB_BaconShop_HP_053_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		if controller.first_dead_minion!=None:
			Give(controller,controller.first_dead_minion).trigger(source)
			gold_card_id = controller.game.BG_find_triple()##
			if gold_card_id:
				controller.game.BG_deal_gold(gold_card_id)
class TB_BaconShop_HP_053:
	""" I'll Take That!
	Next combat, add a plain copy of the first minion you kill to your hand."""
	tags={GameTag.HIDE_COST:1}
	events = BeginBar(CONTROLLER).on(TB_BaconShop_HP_053_Action(CONTROLLER))
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
class TB_BaconShop_HERO_45_Buddy_G_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		if controller.second_dead_minion!=None:
			Give(controller,controller.second_dead_minion).trigger(source)
			Give(controller,controller.second_dead_minion).trigger(source)
			gold_card_id = controller.game.BG_find_triple()##
			if gold_card_id:
				controller.game.BG_deal_gold(gold_card_id)
class TB_BaconShop_HERO_45_Buddy_G:# <12>[1453]
	""" Loyal Henchman
	After you kill a second minion each combat,_get 2 plain copies of it. """
	events = BeginBar(CONTROLLER).on(TB_BaconShop_HERO_45_Buddy_G_Action(CONTROLLER))
	pass



#06##Bru'kan   #################################
class BG22_HERO_001:# <12>[1453]
	""" Bru'kan 	"""
class BG22_HERO_001p:# <12>[1453]
	""" Embrace the Elements
	Choose an Element.[Start of Combat:] Call upon that Element. """
	#<ReferencedTag enumID="1531" name="START_OF_COMBAT" type="Int" value="1"/>
	entourage=['BG22_HERO_001p_t1','BG22_HERO_001p_t2','BG22_HERO_001p_t3','BG22_HERO_001p_t4']
	activate = GenericChoiceChangeHeropower(CONTROLLER, RandomEntourage()*4)
	pass
class BG22_HERO_001p_t1:# <12>[1453]
	""" Earth Invocation
	[Start of Combat:] Give 4random friendly minions"[Deathrattle:] Summona 1/1 Elemental." """
	events = BeginBattle(CONTROLLER).on(CastSpell('BG22_HERO_001p_t1_s'))
	pass
class BG22_HERO_001p_t1_s:# <8>[1453]
	""" Earth Invocation
	Give 4 random friendly minions "[Deathrattle:] Summon a 1/1 Elemental." """
	play = Buff(RANDOM_FRIENDLY_MINION, 'BG22_HERO_001p_t1e') * 4
	pass
class BG22_HERO_001p_t1e:# <12>[1453]
	""" Element: Earth
	[Deathrattle:] Summon a 1/1 Elemental. """
	tags={GameTag.DEATHRATTLE:1}
	deathrattle = Summon(CONTROLLER,'BG22_HERO_001p_t1et')
	pass
class BG22_HERO_001p_t1et:# <12>[1453]
	""" Stone Elemental 	 """
	pass
class BG22_HERO_001p_t2:# <12>[1453]
	""" Fire Invocation
	[Start of Combat:] Double your left-most minion's Attack. """
	events = BeginBattle(CONTROLLER).on(CastSpell('BG22_HERO_001p_t2_s'))
	pass
class BG22_HERO_001p_t2_s:# <8>[1453]
	""" Fire Invocation
	Double your left-most minion's Attack. """
	def play(self):
		controller = self.controller
		if len(controller.field)>0:
			card = controller.field[0]
			Buff(card, 'BG22_HERO_001p_t2_s').trigger(controller)
	pass
class BG22_HERO_001p_t2e:# <12>[1453]
	""" Element: Fire
	This minion's Attack has been doubled. """
	atk = lambda self, k : k*2
	pass
class BG22_HERO_001p_t3:# <12>[1453]
	""" Water Invocation
	[Start of Combat:] Giveyour right-most minion+3 Health and [Taunt]. """
	events = BeginBattle(CONTROLLER).on(CastSpell(ID('BG22_HERO_001p_t3_s')))
	pass
class BG22_HERO_001p_t3_s:# <8>[1453]
	""" Water Invocation
	Give your right-most minion +3 Health and [Taunt]. """
	def play(self):
		controller = self.controller
		if len(controller.field)>0:
			card = controller.field[-1]
			Buff(card, 'BG22_HERO_001p_t3_s').trigger(controller)
	pass
class BG22_HERO_001p_t3e:# <12>[1453]
	""" Element: Water
	+3 Health and [Taunt]. """
	max_health = lambda self, i : i+3
	taunt = True
	pass
class BG22_HERO_001p_t4:# <12>[1453]
	""" Lightning Invocation
	[Start of Combat:] Deal 1 damage to 5 random enemy minions. """
	events = BeginBattle(CONTROLLER).on(CastSpell('BG22_HERO_001p_t4_s'))
	pass
class BG22_HERO_001p_t4_s:# <8>[1453]
	""" Lightning Invocation
	Deal 1 damage to 5 random enemy minions. """
	play = Hit(RANDOM(ENEMY_MINIONS),1) * 5
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



#07#C'Thun   ### HP OK ####
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
class TB_BaconShop_HERO_29_Buddy:# <12>[1453]
	""" Tentacle of C'Thun
	After a different friendly minion gains stats, gain_+1/+1 until your next turn. """
	#
	pass
class TB_BaconShop_HERO_29_Buddy_e:# <12>[1453]
	""" All Eyes On Me
	+1/+1. """
	#
	pass
class TB_BaconShop_HERO_29_Buddy_G:# <12>[1453]
	""" Tentacle of C'Thun
	After a different friendly minion gains stats, gain_+2/+2  until your next turn. """
	#
	pass
class TB_BaconShop_HERO_29_Buddy_Ge:# <12>[1453]
	""" All Eyes On Me
	+2/+2. """
	#
	pass



#08#Captain Eudora   #### OK ####
class TB_BaconShop_HERO_64:# <12>[1453]
	""" Captain Eudora
	"""
class TB_BaconShop_HP_074_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = target
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
	activate = TB_BaconShop_HP_074_Action(CONTROLLER)
######## BUDDY
class TB_BaconShop_HERO_64_Buddy:
	""" Dagwik Stickytoe
	At the end of your turn, give a random friendly Golden minion +5/+5."""
TB_BaconShop_HERO_64_Buddy_e=buff(5,5)# <12>[1453]
""" Gold Abound
+5/+5. """
class TB_BaconShop_HERO_64_Buddy_G:
	""" Dagwik Stickytoe 
	At the end of your turn, give a random friendly Golden minion +10/+10. """
TB_BaconShop_HERO_64_Buddy_G_e=buff(10,10)# <12>[1453]
""" Gold Abound
+10/+10. """



#09#Captain Hooktusk  #### OK ####
class TB_BaconShop_HERO_67:# <12>[1453]
	""" Captain Hooktusk
	"""
class TB_BaconShop_HP_075_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = source.controller
		tier = max(target.tech_level-1, 1)
		Destroy(target).trigger(source)
		GenericChoice(controller, RandomBGMinion(tech_level=tier)*2).trigger(source)
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
	#
	pass
class TB_BaconShop_HERO_67_Buddy_G:# <12>[1453]
	""" Raging Contender
	'Trash for Treasure' offers 4 options instead of 2. """
	#
	pass



#10#Cariel Roame ### OK ###
class BG21_HERO_000:# <5>[1453]
	""" Cariel Roame	"""
	pass
class BG21_HERO_000e:
	"""Cariel Watcher	"""
	pass
class BuffRandomFriendlyMinion(TargetedAction):
	TARGET = ActionArg()#controller
	BUFF = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, buff, amount):
		controller = target
		if amount >= len(controller.field):
			samples = controller.field
		else:
			samples = random.sample(controller.field, amount)
		for card in samples:
			Buff(card, buff).trigger(controller)
		pass
	pass
class BG21_HERO_000p_Action(TargetedAction):
	TARGET = ActionArg()
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
	Give a random friendly minion +1/+1. <i>(Upgrades at Tavern Tier 3.)</i>"""
	activate = BuffRandomFriendlyMinion(CONTROLLER,'BG21_HERO_000pe',2)## 1 until 23.4.3, 
	events = UpgradeTier(CONTROLLER).on(BG21_HERO_000p_Action(CONTROLLER, 3, 'BG21_HERO_000p2')) 
	pass
BG21_HERO_000pe=buff(1,1)
class BG21_HERO_000p2:
	"""Conviction (Rank 2)
	Give three random friendly minions +1/+1. <i>(Upgrades at Tavern Tier 5.)</i>"""
	activate = BuffRandomFriendlyMinion(CONTROLLER,'BG21_HERO_000pe', 4)## 4 until 23.4.3
	events = UpgradeTier(CONTROLLER).on(BG21_HERO_000p_Action(CONTROLLER, 5, 'BG21_HERO_000p3')) 
	pass
class BG21_HERO_000p3:
	"""Conviction (Rank 3)
	Give five random _friendly minions +1/+1."""
	activate = BuffRandomFriendlyMinion(CONTROLLER,'BG21_HERO_000pe', 7)## 5 until 23.4.3
######## BUDDY
class BG21_HERO_000_Buddy:# <12>[1453]
	""" Captain Fairmount
	At the end of your turn, give five random friendly minions +1/+1. """
	events = OWN_TURN_END.on(BuffRandomFriendlyMinion(CONTROLLER,'BG21_HERO_000_Buddy_e', 5))
	pass
BG21_HERO_000_Buddy_e=buff(1,1)
class BG21_HERO_000_Buddy_G:# <12>[1453]
	""" Captain Fairmount
	At the end of your turn, give five random friendly minions +2/+2. """
	events = OWN_TURN_END.on(BuffRandomFriendlyMinion(CONTROLLER,'BG21_HERO_000_Buddy_G_e', 5))
	pass
BG21_HERO_000_Buddy_G_e=buff(2,2)



#11#Chenvaala ### HP OK ###
class TB_BaconShop_HERO_78:# <12>[1453]
	""" Chenvaala
	"""
class TB_BaconShop_HP_088:
	""" Avalanche
	<b>Passive</b> After you play 3 Elementals, reduce the cost of upgrading Bob's Tavern by (3)."""
	events = BG_Play(CONTROLLER, FRIENDLY + ELEMENTAL).on(SidequestCounter(SELF, 3, [ReduceTierUpCost(CONTROLLER, 3)]))
class TB_BaconShop_HERO_78_Buddy:
	""" Snow Elemental
	Bob always offers an extra <b>Frozen</b> Elemental whenever the Tavern is <b>Refreshed</b>."""
class TB_BaconShop_HERO_78_Buddy_G:
	""" Snow Elemental
	Bob always offers 2 extra <b>Frozen</b> Elementals whenever the Tavern is <b>Refreshed</b>."""



#12#Cookie the Cook  #### difficult ###  
class BG21_HERO_020:# <12>[1453]
	""" Cookie the Cook
	 """
	pass
class BG21_HERO_020p_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		from fireplace.cards import battlegrounds
		controller=source.controller
		race = target.race
		Destroy(target).trigger(source)
		gamemaster=controller.game.parent
		source.sidequest_list0.append(target.race)
		source.script_data_num_1 -= 1 
		if source.script_data_num_1== 0:
			source.script_data_num_1 = 3
			deck=[]
			entourage=[]
			tier=source.controller.tavern_tier
			for i in range(1,tier+1):
				if Race.BEAST in source.sidequest_list0:
					deck += battlegrounds.BG_minion_beast.BG_PoolSet_Beast[i]
				if Race.DEMON in source.sidequest_list0:
					deck += battlegrounds.BG_minion_demon.BG_PoolSet_Demon[i]
				if Race.DRAGON in source.sidequest_list0:
					deck += battlegrounds.BG_minion_dragon.BG_PoolSet_Dragon[i]
				if Race.ELEMENTAL in source.sidequest_list0:
					deck += battlegrounds.BG_minion_elemental.BG_PoolSet_Elemental[i]
				if Race.MECHANICAL in source.sidequest_list0:
					deck += battlegrounds.BG_minion_mecha.BG_PoolSet_Mecha[i]
				if Race.MURLOC in source.sidequest_list0:
					deck += battlegrounds.BG_minion_murloc.BG_PoolSet_Murloc[i]
				if Race.NAGA in source.sidequest_list0:
					deck += battlegrounds.BG_minion_naga.BG_PoolSet_Naga[i]
				if Race.PIRATE in source.sidequest_list0:
					deck += battlegrounds.BG_minion_pirate.BG_PoolSet_Pirate[i]
				if Race.QUILBOAR in source.sidequest_list0:
					deck += battlegrounds.BG_minion_quilboar.BG_PoolSet_Quilboar[i]
			source.sidequest_list0=[]
			source.entourage = random.sample(deck,3)
			Discover(controller, RandomEntourage()).trigger(source)
class BG21_HERO_020p:# <12>[1453]
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
	#
	pass
class BG21_HERO_020_Buddy_G:# <12>[1453]
	""" Sous Chef
	You can use your Hero Power 2 extra times each_turn. """
	#
	pass



#13#Dancin' Deryl ### need check ###
class TB_BaconShop_HERO_36:# <12>[1453]
	""" Dancin' Deryl
	 """
class TB_BaconShop_HP_042:
	""" Hat Trick
	<b>Passive.</b> After you sell a minion, randomly give a minion in Bob's Tavern +1/+1 three times."""
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


#14#Death Speaker Blackthorn  ### HP OK ###
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
	After you gain a <b>Blood Gem</b>, gain an extra one. """
	events = Give(CONTROLLER, ID('BG20_GEM')).after(Give(CONTROLLER, 'BG20_GEM'))
class BG20_HERO_103_Buddy_G:
	""" Death's Head Sage
	After you gain a <b>Blood Gem</b>, gain two extra. """
	events = Give(CONTROLLER, ID('BG20_GEM')).after(Give(CONTROLLER, 'BG20_GEM')*2)



#15#Deathwing    ### not good for enemy's minions in the battle ###
class TB_BaconShop_HERO_52:
	""" Deathwing
	"""
class TB_BaconShop_HP_061:
	""" ALL Will Burn!
	[x]<b>Passive</b> ALL minions have +2 Attack."""
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



#16#Dinotamer Brann   ### HP OK ###
class TB_BaconShop_HERO_43:# <12>[1453]
	""" Dinotamer Brann
	 """
class TB_BaconShop_HP_048:
	""" Battle Brand
	<b>Passive.</b> After you buy 5 <b>Battlecry</b> minions, add Brann Bronzebeard to your _hand. <i>(Once per game.)</i>@[x]<b>Passive.</b> After you buy 5 <b>Battlecry</b> minions, add Brann Bronzebeard to your hand. <i>({0} left!)</i>"""
	events = Buy(CONTROLLER, MINION + BATTLECRY).on(SidequestCounterText0(SELF, 5, \
		[Give(CONTROLLER,"LOE_077"), SetAttr(SELF,'cant_play',True)]))
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
	deathrattle = TB_BaconShop_HERO_43_Buddy_Action(CONTROLLER, RandomBGMinion(has_battlecry=True, tech_level_less=TIER(CONTROLLER)))
	pass
class TB_BaconShop_HERO_43_Buddy_G:# <12>[1453]
	""" Brann's Epic Egg
	[Taunt]. [Deathrattle:] Summon2 random [Battlecry] minionsand add copies of themto your hand. """
	deathrattle = (\
		Summon(CONTROLLER, RandomBGMinion(has_battlecry=True)).then(Give(CONTROLLER,Copy(Summon.CARD))),\
		Summon(CONTROLLER, RandomBGMinion(has_battlecry=True)).then(Give(CONTROLLER,Copy(Summon.CARD)))\
	)
	pass



#################################################




	
	
