from ..utils import *
from fireplace.battlegrounds.BG_actions import *

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

BG_Hero1=[
	'TB_BaconShop_HERO_16','TB_BaconShop_HP_044','TB_BaconShop_HERO_16_Buddy','TB_BaconShop_HERO_16_Buddy_e','TB_BaconShop_HERO_16_Buddy_G','TB_BaconShop_HERO_16_Buddy_G_e',#01#A. F. Kay 
	'TB_BaconShop_HERO_76','TB_BaconShop_HP_086','TB_BaconShop_HERO_76_Buddy','TB_BaconShop_HERO_76_Buddy_e','TB_BaconShop_HERO_76_Buddy_G',#02#Al'Akir
	'TB_BaconShop_HERO_56','TB_BaconShop_HP_064','TB_BaconShop_HERO_56_Buddy',#03#Alexstrasza
	'BG22_HERO_201','BG22_HERO_201p','BG22_HERO_201pe','BG22_HERO_201_Buddy','BG22_HERO_201_Buddy_G',#04#Ambassador Faelin
	'TB_BaconShop_HERO_59','TB_BaconShop_HP_065','TB_BaconShop_HP_065pe','TB_BaconShop_HP_065t2','TB_BaconShop_HERO_59_Buddy','TB_BaconShop_HERO_59_Buddy_G','TB_BaconShop_HERO_59t',#05#Aranna Starseeker
	'TB_BaconShop_HERO_45','TB_BaconShop_HP_053','TB_BaconShop_HERO_45_Buddy','TB_BaconShop_HERO_45_Buddy_G',#06#Arch-Villain Rafaam
	'BG22_HERO_001','BG22_HERO_001p','BG22_HERO_001p_t1','BG22_HERO_001p_t1_s','BG22_HERO_001p_t1e','BG22_HERO_001p_t1et','BG22_HERO_001p_t2','BG22_HERO_001p_t2_s','BG22_HERO_001p_t2e','BG22_HERO_001p_t3','BG22_HERO_001p_t3_s','BG22_HERO_001p_t3e','BG22_HERO_001p_t4','BG22_HERO_001p_t4_s','BG22_HERO_001_Buddy','BG22_HERO_001_Buddy_e','BG22_HERO_001_Buddy_e1','BG22_HERO_001_Buddy_e2','BG22_HERO_001_Buddy_e3','BG22_HERO_001_Buddy_e4','BG22_HERO_001_Buddy_G',#BG22_HERO_001#07#Bru'kan
	'TB_BaconShop_HERO_29','TB_BaconShop_HP_104','TB_BaconShop_HP_104e','TB_BaconShop_HERO_29_Buddy','TB_BaconShop_HERO_29_Buddy_e','TB_BaconShop_HERO_29_Buddy_G','TB_BaconShop_HERO_29_Buddy_Ge',#08#C'Thun
	'TB_BaconShop_HERO_64','TB_BaconShop_HP_074','TB_BaconShop_HERO_64_Buddy','TB_BaconShop_HERO_64_Buddy_e','TB_BaconShop_HERO_64_Buddy_G','TB_BaconShop_HERO_64_Buddy_G_e',#09#Captain Eudora
	'TB_BaconShop_HERO_67','TB_BaconShop_HP_075','TB_BaconShop_HERO_67_Buddy','TB_BaconShop_HERO_67_Buddy_G',#10#Captain Hooktusk
	'BG21_HERO_000','BG21_HERO_000e','BG21_HERO_000p','BG21_HERO_000pe','BG21_HERO_000p2','BG21_HERO_000p3','BG21_HERO_000_Buddy','BG21_HERO_000_Buddy_e','BG21_HERO_000_Buddy_G','BG21_HERO_000_Buddy_G_e',#11#Cariel Roame
	'TB_BaconShop_HERO_78','TB_BaconShop_HP_088','TB_BaconShop_HERO_78_Buddy','TB_BaconShop_HERO_78_Buddy_G',#12#Chenvaala
	'BG21_HERO_020','BG21_HERO_020p','BG21_HERO_020_Buddy','BG21_HERO_020_Buddy_G',#13#Cookie the Cook
	'TB_BaconShop_HERO_36','TB_BaconShop_HP_042','TB_BaconShop_HP_042e','TB_BaconShop_HERO_36_Buddy','TB_BaconShop_HERO_36_Buddy_e','TB_BaconShop_HERO_36_Buddy_G','TB_BaconShop_HERO_36_Buddy_Ge',#14#Dancin' Deryl
	'BG20_HERO_103','BG20_HERO_103p','BG20_HERO_103_Buddy','BG20_HERO_103_Buddy_G',#Death Speaker Blackthorn
	'TB_BaconShop_HERO_52','TB_BaconShop_HP_061','TB_BaconShop_HP_061e','TB_BaconShop_HERO_52_Buddy','TB_BaconShop_HERO_52_Buddy_e','TB_BaconShop_HERO_52_Buddy_G','TB_BaconShop_HERO_52_Buddy_G_e',#16#Deathwing
	'TB_BaconShop_HERO_43','TB_BaconShop_HP_048','TB_BaconShop_HP_048e','TB_BaconShop_HERO_43_Buddy','TB_BaconShop_HERO_43_Buddy_G',#17#Dinotamer Brann
]

BG_PoolSet_Hero1=[
	'TB_BaconShop_HERO_16','TB_BaconShop_HERO_76','TB_BaconShop_HERO_56','BG22_HERO_201','TB_BaconShop_HERO_59','TB_BaconShop_HERO_45','BG22_HERO_001','TB_BaconShop_HERO_29','TB_BaconShop_HERO_64','TB_BaconShop_HERO_67','BG21_HERO_000','TB_BaconShop_HERO_78','BG21_HERO_020','TB_BaconShop_HERO_36','BG20_HERO_103','TB_BaconShop_HERO_52','TB_BaconShop_HERO_43'
	]

BG_Hero1_Buddy={
	'TB_BaconShop_HERO_16':'TB_BaconShop_HERO_16_Buddy',#01#A. F. Kay 
	'TB_BaconShop_HERO_76':'TB_BaconShop_HERO_76_Buddy',#02#Al'Akir
	'TB_BaconShop_HERO_56':'TB_BaconShop_HERO_56_Buddy',#03#Alexstrasza
	'BG22_HERO_201':'BG22_HERO_201_Buddy',#04#Ambassador Faelin
	'TB_BaconShop_HERO_59':'TB_BaconShop_HERO_59_Buddy',#05#Aranna 
	'TB_BaconShop_HERO_45':'TB_BaconShop_HERO_45_Buddy',#06#Arch-Villain Rafaam
	'BG22_HERO_001':'BG22_HERO_001_Buddy',#BG22_HERO_001#07#Bru'kan
	'TB_BaconShop_HERO_29':'TB_BaconShop_HERO_29_Buddy',#08#C'Thun
	'TB_BaconShop_HERO_64':'TB_BaconShop_HERO_64_Buddy',#09#Captain Eudora
	'TB_BaconShop_HERO_67':'TB_BaconShop_HERO_67_Buddy',#10#Captain Hooktusk
	'BG21_HERO_000':'BG21_HERO_000_Buddy',#11#Cariel Roame
	'TB_BaconShop_HERO_78':'TB_BaconShop_HERO_78_Buddy',#12#Chenvaala
	'BG21_HERO_020':'BG21_HERO_020_Buddy',#13#Cookie the Cook
	'TB_BaconShop_HERO_36':'TB_BaconShop_HERO_36_Buddy',#14#Dancin' Deryl
	'BG20_HERO_103':'BG20_HERO_103_Buddy',#Death Speaker Blackthorn
	'TB_BaconShop_HERO_52':'TB_BaconShop_HERO_52_Buddy',#16#Deathwing
	'TB_BaconShop_HERO_43':'TB_BaconShop_HERO_43_Buddy',#17#Dinotamer Brann
	}

BG_Hero1_Buddy_Gold={
	'TB_BaconShop_HERO_16_Buddy':'TB_BaconShop_HERO_16_Buddy_G',#01#A. F. Kay 
	'TB_BaconShop_HERO_76_Buddy':'TB_BaconShop_HERO_76_Buddy_G',#02#Al'Akir
	'TB_BaconShop_HERO_56_Buddy':'TB_BaconShop_HERO_56_Buddy_G',#03#Alexstrasza
	'BG22_HERO_201_Buddy':'BG22_HERO_201_Buddy_G',#04#Ambassador Faelin
	'TB_BaconShop_HERO_59_Buddy':'TB_BaconShop_HERO_59_Buddy_G',#05#Aranna Starseeker
	'TB_BaconShop_HERO_45_Buddy':'TB_BaconShop_HERO_45_Buddy_G',#06#Arch-Villain Rafaam
	'BG22_HERO_001_Buddy':'BG22_HERO_001_Buddy_G',##07#Bru'kan
	'TB_BaconShop_HERO_29_Buddy':'TB_BaconShop_HERO_29_Buddy_G',#08#C'Thun
	'TB_BaconShop_HERO_64_Buddy':'TB_BaconShop_HERO_64_Buddy_G',#09#Captain Eudora
	'TB_BaconShop_HERO_67_Buddy':'TB_BaconShop_HERO_67_Buddy_G',#10#Captain Hooktusk
	'BG21_HERO_000_Buddy':'BG21_HERO_000_Buddy_G',#11#Cariel Roame
	'TB_BaconShop_HERO_78_Buddy':'TB_BaconShop_HERO_78_Buddy_G',#12#Chenvaala
	'BG21_HERO_020_Buddy':'BG21_HERO_020_Buddy_G',#13#Cookie the Cook
	'TB_BaconShop_HERO_36_Buddy':'TB_BaconShop_HERO_36_Buddy_G',#14#Dancin' Deryl
	'BG20_HERO_103_Buddy':'BG20_HERO_103_Buddy_G',#Death Speaker Blackthorn
	'TB_BaconShop_HERO_52_Buddy':'TB_BaconShop_HERO_52_Buddy_G',#16#Deathwing
	'TB_BaconShop_HERO_43_Buddy':'TB_BaconShop_HERO_43_Buddy_G',#17#Dinotamer Brann
	}

BG_Hero1_Armor={
	'TB_BaconShop_HERO_16':0,#01#A. F. Kay 
	'TB_BaconShop_HERO_76':5,#02#Al'Akir
	'TB_BaconShop_HERO_56':3,#03#Alexstrasza
	'BG22_HERO_201':4,#04#Ambassador Faelin
	'TB_BaconShop_HERO_59':0,#05#Aranna 
	'TB_BaconShop_HERO_45':5,#06#Arch-Villain Rafaam
	'BG22_HERO_001':'BG22_HERO_001_Buddy',#BG22_HERO_001#07#Bru'kan
	'TB_BaconShop_HERO_29':5,#08#C'Thun
	'TB_BaconShop_HERO_64':6,#09#Captain Eudora
	'TB_BaconShop_HERO_67':6,#10#Captain Hooktusk
	'BG21_HERO_000':0,#11#Cariel Roame
	'TB_BaconShop_HERO_78':0,#12#Chenvaala
	'BG21_HERO_020':0,#13#Cookie the Cook
	'TB_BaconShop_HERO_36':'TB_BaconShop_HERO_36_Buddy',#14#Dancin' Deryl
	'BG20_HERO_103':'BG20_HERO_103_Buddy',#Death Speaker Blackthorn
	'TB_BaconShop_HERO_52':'TB_BaconShop_HERO_52_Buddy',#16#Deathwing
	'TB_BaconShop_HERO_43':'TB_BaconShop_HERO_43_Buddy',#17#Dinotamer Brann
	}
########### source


#01#A. F. Kay 
class TB_BaconShop_HERO_16:# <12>[1453]
	""" A. F. Kay
	 """
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
	#
	pass
TB_BaconShop_HERO_16_Buddy_e=buff(1,2)# <12>[1453]
""" Snack-Filled
+1/+2. """
class TB_BaconShop_HERO_16_Buddy_G:# <12>[1453]
	""" Snack Vendor
	At the end of your turn, give your Tavern Tier 3 minions +2/+4. """
	#
	pass
TB_BaconShop_HERO_16_Buddy_G_e=buff(2,4)# <12>[1453]
""" Snack-Filled
+2/+4. """


#02#Al'Akir
class TB_BaconShop_HERO_76:# <12>[1453]
	""" Al'Akir
	 """
class TB_BaconShop_HP_086_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		if len(target.field)>0:
			card = target.field[0]
			card.windfury=True
			card.divine_shield=True
			card.taunt=True
class TB_BaconShop_HP_086:
	""" Swatting Insects
	<b>Passive</b><b>Start of Combat:</b> Give yourleft-most minion <b>Windfury</b>,___<b>Divine Shield</b>, and <b>Taunt</b>."""
	events = BeginBattle(CONTROLLER).on(TB_BaconShop_HP_086_Action(CONTROLLER))
	pass
class TB_BaconShop_HERO_76_Buddy:
	"""Spirit of Air
	<b>Deathrattle:</b> Give a random friendly minion <b>Windfury</b>,___<b>Divine Shield</b>, and <b>Taunt</b>.___"""
	pass
class TB_BaconShop_HERO_76_Buddy_e:# <12>[1453]
	""" Blessing of Air
	[Windfury], [Divine Shield], and [Taunt]. """
	#
	pass
class TB_BaconShop_HERO_76_Buddy_G:
	""" Spirit of Air
	<b>Deathrattle:</b> Give 2 randomfriendly minions <b>Windfury</b>,<b>Divine Shield</b>, and <b>Taunt</b>."""
	pass

#03#Alexstrasza
class TB_BaconShop_HERO_56:# <12>[1453]
	""" Alexstrasza
	"""
class TB_BaconShop_HP_064_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		if target.Tier==5:
			DiscoverTwice(controller, RandomBGDragon(tech_level_less=5)*3).trigger(source)
class TB_BaconShop_HP_064:
	""" Queen of Dragons
	<b>Passive</b>After you upgrade Bob's Tavern to Tavern Tier 5,_<b>Discover</b> two Dragons."""
	events = UpgradeTier(CONTROLLER).on(TB_BaconShop_HP_064_Action(CONTROLLER))
	pass
class TB_BaconShop_HERO_56_Buddy:
	""" Vaelastrasz
	<b>Battlecry:</b> Add a random Dragon of your Tavern Tier to your hand."""
class TB_BaconShop_HERO_56_Buddy_G:
	""" Vaelastrasz
	&lt;b&gt;Battlecry:&lt;/b&gt; Add two random Dragons of your Tavern Tier to your hand."""


###Ambassador Faelin
class BG22_HERO_201:# <12>[1453]
	""" Ambassador Faelin
	"""
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
		if controller.Tier>= tier:
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
	#
	pass

class BG22_HERO_201_Buddy_G:# <12>[1453]
	""" Submersible Chef
	[Battlecry:] Add a random Tier 1, 3, and 5 minion to your hand twice. """
	#
	pass


#05#Aranna Starseeker # アランナ
class TB_BaconShop_HERO_59:# <12>[1453]
	""" Aranna Starseeker
	"""
class TB_BaconShop_HP_065:
	""" Demon Hunter Training
	<b>Passive</b> After you <b>Refresh</b> 5 times, Bob always has 7 minions.
<i>(@ left!)</i>"""
	events = Rerole(CONTROLLER).on(SidequestCounter(SELF, 5, [SetAttr(CONTROLLER, 'BobsTmpFieldSize', 7)]))
	pass
class TB_BaconShop_HP_065pe:
	"""  Aranna Watcher
	"""
class TB_BaconShop_HP_065t2:###  条件が満たされるとヒロパが交代になる
	""" Spectral Sight
	<b>Passive</b>Bob's Tavern refreshes with 7 minions."""
class TB_BaconShop_HERO_59_Buddy:# <12>[1453]
	""" Sklibb, Demon Hunter
	After you play a minion,your next [Refresh] costs (0). """
	#
	pass
class TB_BaconShop_HERO_59_Buddy_G:# <12>[1453]
	""" Sklibb, Demon Hunter
	After you play a minion, your next two [Refreshes] cost (0). """
	#
	pass
class TB_BaconShop_HERO_59t:# <12>[1453]
	""" Aranna, Unleashed
	"""
	#
	pass


#06#Arch-Villain Rafaam
class TB_BaconShop_HERO_45:# <12>[1453]
	""" Arch-Villain Rafaam
	"""
class TB_BaconShop_HP_053_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		if controller.FirstKillMinion!=None:
			Give(controller,controller.FirstKillMinion).trigger(source)
			gold_card_id = controller.game.BG_find_triple()## トリプルを判定
			if gold_card_id:
				controller.game.BG_deal_gold(gold_card_id)
class TB_BaconShop_HP_053:
	""" I'll Take That!
	Next combat, add a plain copy of the first minion you kill to your hand."""
	events = BeginBar(CONTROLLER).on(TB_BaconShop_HP_053_Action(CONTROLLER))
class TB_BaconShop_HERO_45_Buddy:# <12>[1453]
	""" Loyal Henchman
	After you kill a secondminion each combat,get a plain copy of it. """
	#
	pass
class TB_BaconShop_HERO_45_Buddy_G:# <12>[1453]
	""" Loyal Henchman
	After you kill a secondminion each combat,_get 2 plain copies of it. """
	#
	pass

###Bru'kan
class BG22_HERO_001:# <12>[1453]
	""" Bru'kan
	"""
class BG22_HERO_001p:# <12>[1453]
	""" Embrace the Elements
	Choose an Element.[Start of Combat:] Call upon that Element. """
	#<ReferencedTag enumID="1531" name="START_OF_COMBAT" type="Int" value="1"/>
	#
	pass
class BG22_HERO_001p_t1:# <12>[1453]
	""" Earth Invocation
	[Start of Combat:] Give 4random friendly minions"[Deathrattle:] Summona 1/1 Elemental." """
	#
	pass
class BG22_HERO_001p_t1_s:# <8>[1453]
	""" Earth Invocation
	Give 4 random friendly minions "[Deathrattle:] Summon a 1/1 Elemental." """
	#
	pass
class BG22_HERO_001p_t1e:# <12>[1453]
	""" Element: Earth
	[Deathrattle:] Summon a 1/1 Elemental. """
	#
	pass
class BG22_HERO_001p_t1et:# <12>[1453]
	""" Stone Elemental
	 """
	#
	pass
class BG22_HERO_001p_t2:# <12>[1453]
	""" Fire Invocation
	[Start of Combat:] Double your left-most minion's Attack. """
	#
	pass

class BG22_HERO_001p_t2_s:# <8>[1453]
	""" Fire Invocation
	Double your left-most minion's Attack. """
	#
	pass

class BG22_HERO_001p_t2e:# <12>[1453]
	""" Element: Fire
	This minion's Attack has been doubled. """
	#
	pass
class BG22_HERO_001p_t3:# <12>[1453]
	""" Water Invocation
	[Start of Combat:] Giveyour right-most minion+3 Health and [Taunt]. """
	#
	pass
class BG22_HERO_001p_t3_s:# <8>[1453]
	""" Water Invocation
	Give your right-most minion +3 Healthand [Taunt]. """
	#
	pass
class BG22_HERO_001p_t3e:# <12>[1453]
	""" Element: Water
	+3 Health and [Taunt]. """
	#
	pass
class BG22_HERO_001p_t4:# <12>[1453]
	""" Lightning Invocation
	[Start of Combat:] Deal 1 damage to 5 random enemy minions. """
	#
	pass
class BG22_HERO_001p_t4_s:# <8>[1453]
	""" Lightning Invocation
	Deal 1 damage to 5random enemy minions. """
	#
	pass
class BG22_HERO_001_Buddy:# <12>[1453]
	""" Spirit Raptor
	After you call upon a newElement, this remembers it.[Deathrattle:] Call uponthose Elements. """
	#
	pass
class BG22_HERO_001_Buddy_e:# <12>[1453]
	""" Elemental Recollection
	Remembering an Element. """
	#
	pass
class BG22_HERO_001_Buddy_e1:# <12>[1453]
	""" Earth Recollection
	Remembering Earth Invocation. """
	#
	pass
class BG22_HERO_001_Buddy_e2:# <12>[1453]
	""" Fire Recollection
	Remembering Fire Invocation. """
	#
	pass
class BG22_HERO_001_Buddy_e3:# <12>[1453]
	""" Water Recollection
	Remembering Water Invocation. """
	#
	pass
class BG22_HERO_001_Buddy_e4:# <12>[1453]
	""" Lightning Recollection
	Remembering Lightning Invocation. """
	#
	pass
class BG22_HERO_001_Buddy_G:# <12>[1453]
	""" Spirit Raptor
	After you call upon a newElement, this remembers it.[Deathrattle:] Call upon thoseElements twice. """
	#
	pass


#08#C'Thun
class TB_BaconShop_HERO_29:# <12>[1453]
	""" C'Thun
	"""
class TB_BaconShop_HP_104:
	""" Saturday C'Thuns!
	At end of turn, give a friendly minion +1/+1.__Repeat @ |4(time, times).<i>__(Upgrades after each use!)</i>"""
TB_BaconShop_HP_104e=buff(1,1)
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

#09#Captain Eudora
class TB_BaconShop_HERO_64:# <12>[1453]
	""" Captain Eudora
	"""
class TB_BaconShop_HP_074:
	""" Buried Treasure
	_Dig for a Golden minion! <i>(@ |4(Dig, Digs) left.)</i>"""
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


#10#Captain Hooktusk
class TB_BaconShop_HERO_67:# <12>[1453]
	""" Captain Hooktusk
	"""
class TB_BaconShop_HP_075:
	""" Trash for Treasure
	Remove a friendly minion. Choose one of two from a Tavern Tier lower to keep."""
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


#11#Cariel Roame
class BG21_HERO_000:# <5>[1453]
	""" Cariel Roame
	"""
	pass
class BG21_HERO_000e:
	"""Cariel Watcher
	"""
	pass
class BG21_HERO_000p:
	""" Conviction (Rank 1)
	Give a random friendly minion +1/+1. <i>(Upgrades at Tavern Tier 3.)</i>"""
	play = Buff(RANDOM_FRIENDLY_MINION,'BG21_HERO_000pe')
	pass
BG21_HERO_000pe=buff(1,1)
class BG21_HERO_000p2:
	"""Conviction (Rank 2)
	Give three random friendly minions +1/+1. <i>(Upgrades at Tavern Tier 5.)</i>"""
	play = Buff(RANDOM_FRIENDLY_MINION,'BG21_HERO_000pe') * 3
	pass
class BG21_HERO_000p3:
	"""Conviction (Rank 3)
	Give five random _friendly minions +1/+1."""
	play = Buff(RANDOM_FRIENDLY_MINION,'BG21_HERO_000pe') * 5
class BG21_HERO_000_Buddy:# <12>[1453]
	""" Captain Fairmount
	At the end of your turn, give five random friendly minions +1/+1. """
	events = OWN_TURN_END.on(Buff(RANDOM_FRIENDLY_MINION,'BG21_HERO_000_Buddy_e') * 5)
	pass
BG21_HERO_000_Buddy_e=buff(1,1)
class BG21_HERO_000_Buddy_G:# <12>[1453]
	""" Captain Fairmount
	At the end of your turn, give five random friendly minions +2/+2. """
	events = OWN_TURN_END.on(Buff(RANDOM_FRIENDLY_MINION,'BG21_HERO_000_Buddy_G_e') * 5)
	pass
BG21_HERO_000_Buddy_G_e=buff(2,2)

#12#Chenvaala
class TB_BaconShop_HERO_78:# <12>[1453]
	""" Chenvaala
	"""
class TB_BaconShop_HP_088:
	""" Avalanche
	<b>Passive</b> After you play 3 Elementals, reduce the cost of upgrading Bob's Tavern by (3)."""
class TB_BaconShop_HERO_78_Buddy:
	""" Snow Elemental
	Bob always offers an extra <b>Frozen</b> Elemental whenever the Tavern is <b>Refreshed</b>."""
class TB_BaconShop_HERO_78_Buddy_G:
	""" Snow Elemental
	Bob always offers 2 extra <b>Frozen</b> Elementals whenever the Tavern is <b>Refreshed</b>."""


#13#Cookie the Cook
class BG21_HERO_020:# <12>[1453]
	""" Cookie the Cook
	 """
	pass
class BG21_HERO_020p:# <12>[1453]
	""" Stir the Pot
	Throw a minion in your pot. When you've gathered 3,[Discover] from their minion types. <i>(@ left!)</i> """
	#
	pass
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



#14#Dancin' Deryl
class TB_BaconShop_HERO_36:# <12>[1453]
	""" Dancin' Deryl
	 """
class TB_BaconShop_HP_042:
	""" Hat Trick
	&lt;b&gt;Passive.&lt;/b&gt; After you sell a minion, randomly give a minion in Bob's Tavern +1/+1 three times."""
TB_BaconShop_HP_042e=buff(1,1)
class TB_BaconShop_HERO_36_Buddy:# <12>[1453]
	""" Asher the Haberdasher
	After you sell a minion, gain +1/+1. """
	#
	pass
TB_BaconShop_HERO_36_Buddy_e=buff(1,1)# <12>[1453]
""" Dashing Hat
+1/+1. """
class TB_BaconShop_HERO_36_Buddy_G:# <12>[1453]
	""" Asher the Haberdasher
	After you sell a minion, gain +2/+2. """
	#
	pass
TB_BaconShop_HERO_36_Buddy_Ge=buff(2,2)# <12>[1453]
""" Dashing Hat
+2/+2. """


'BG20_HERO_103','BG20_HERO_103p',
#15#Death Speaker Blackthorn
class BG20_HERO_103:# <12>[1453]
	""" Death Speaker Blackthorn
	 """
class BG20_HERO_103p:# <12>[1453]
	""" Bloodbound
	[Passive]After you upgradeBob's Tavern, gain2 [Blood Gems]. """
	#
	pass
class BG20_HERO_103_Buddy:
	""" Death's Head Sage
	After you gain a <b>Blood Gem</b>, gain an extra one. """
class BG20_HERO_103_Buddy_G:
	""" Death's Head Sage
	After you gain a <b>Blood Gem</b>, gain two extra. """


#16#Deathwing
class TB_BaconShop_HERO_52:
	""" Deathwing
	"""
class TB_BaconShop_HP_061:
	""" ALL Will Burn!
	[x]&lt;b&gt;Passive&lt;/b&gt; ALL minions have +2 Attack."""
TB_BaconShop_HP_061e=buff(2,0)
class TB_BaconShop_HERO_52_Buddy:
	""" Lady Sinestra
	Your minions have +3_Attack. """
TB_BaconShop_HERO_52_Buddy_e=buff(3,0)
class TB_BaconShop_HERO_52_Buddy_G:
	""" Lady Sinestra
	Your minions have +6_Attack. """
TB_BaconShop_HERO_52_Buddy_G_e=buff(3,0)


#17#Dinotamer Brann
class TB_BaconShop_HERO_43:# <12>[1453]
	""" Dinotamer Brann
	 """
class TB_BaconShop_HP_048:
	""" Battle Brand
	<b>Passive.</b> After you buy 5 <b>Battlecry</b> minions, add Brann Bronzebeard to your _hand. <i>(Once per game.)</i>@[x]<b>Passive.</b> After you buy 5 <b>Battlecry</b> minions, add Brann Bronzebeard to your hand. <i>({0} left!)</i>"""
class TB_BaconShop_HP_048e:
	"""
	"""
class TB_BaconShop_HERO_43_Buddy:# <12>[1453]
	""" Brann's Epic Egg
	[Taunt]. [Deathrattle:] Summona random [Battlecry] minionand add a copy of itto your hand. """
	#
	pass
class TB_BaconShop_HERO_43_Buddy_G:# <12>[1453]
	""" Brann's Epic Egg
	[Taunt]. [Deathrattle:] Summon2 random [Battlecry] minionsand add copies of themto your hand. """
	#
	pass



#################################################




	
	
