from ..utils import *

BG_Gems=[	'BG20_GEM','BG20_GEMe','BG20_GEMe2','GAME_005',##Blood Gem
		'TB_BaconShop_Triples_01',#### triple card
		'BGS_Treasures_000','BGS_Treasures_000e',## big banana
		'BGS_Treasures_001','BGS_Treasures_003',
		'BGS_Treasures_004','BGS_Treasures_006','BGS_Treasures_007','BGS_Treasures_007e',
		'BGS_Treasures_009','BGS_Treasures_009e','BGS_Treasures_010','BGS_Treasures_011',
		'BGS_Treasures_012','BGS_Treasures_013','BGS_Treasures_013e1','BGS_Treasures_013pe',
		'BGS_Treasures_014','BGS_Treasures_014e','BGS_Treasures_015',
		'BGS_Treasures_016','BGS_Treasures_018','BGS_Treasures_018e','BGS_Treasures_019',
		'BGS_Treasures_020','BGS_Treasures_022','BGS_Treasures_022e','BGS_Treasures_022pe',
		'BGS_Treasures_023',
		'BGS_Treasures_025','BGS_Treasures_026','BGS_Treasures_026e',
		'BGS_Treasures_028','BGS_Treasures_028e','BGS_Treasures_029','BGS_Treasures_030',
		'BGS_Treasures_030e',
		'BGS_Treasures_032','BGS_Treasures_033','BGS_Treasures_033e','BGS_Treasures_034',
		'BGS_Treasures_034e','BGS_Treasures_036','BGS_Treasures_036e','BGS_Treasures_037',
		'BGS_Treasures_040',
	]+['TB_Bacon_Secrets_01','TB_Bacon_Secrets_02','TB_Bacon_Secrets_04',
			'TB_Bacon_Secrets_05','TB_Bacon_Secrets_07','TB_Bacon_Secrets_08',
			'TB_Bacon_Secrets_10','TB_Bacon_Secrets_11','TB_Bacon_Secrets_12',
			'TB_Bacon_Secrets_13',]

BG_DarkmoonTicket=[
	[],
	['BGS_Treasures_004','BGS_Treasures_006','BGS_Treasures_007','BGS_Treasures_012','BGS_Treasures_015','BGS_Treasures_018',],#1 #BGS_Treasures_032
	['BGS_Treasures_001','BGS_Treasures_010','BGS_Treasures_013','BGS_Treasures_016','BGS_Treasures_019','BGS_Treasures_022','BGS_Treasures_023','BGS_Treasures_025','BGS_Treasures_026','BGS_Treasures_029',],#2 ## 'BGS_Treasures_011',
	['BGS_Treasures_000','BGS_Treasures_009','BGS_Treasures_014','BGS_Treasures_020','BGS_Treasures_028','BGS_Treasures_030','BGS_Treasures_033','BGS_Treasures_036','BGS_Treasures_037','BGS_Treasures_040'],#3
	]
##
##  Blood gem
##TB_Bacon_Secrets

class BG20_GEM:# <12>[1453]
	""" Blood Gem
	Give a friendly minion +@/+@. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0,}
	play = ApplyGem(TARGET, 'BG20_GEM')
	pass

class BG20_GEM_No_Impact:# <12>[1453]
	""" Blood Gem No Impact
	 """
	#
	pass

BG20_GEMe=buff(1,1)# <12>[1453]
""" Blood Gem
Increased stats from Blood Gem (but invisible banner) """


BG20_GEMe2=buff(3,3)# <12>[1453]
""" Blood Gems
+@/+@. """

class GAME_005:# <12> 1637 #OK
	""" The Coin
	Gain 1 Mana Crystal this turn only. """
	play = ManaThisTurnOnly(CONTROLLER, 1)
	pass



class BG20_GEMt:# <12>[1453]
	""" Mass Blood Gem
	Give a friendly minions +@/+@. """
	#
	pass

##
## bananas
##

class BGS_Treasures_000:# <12>[1453] ## OK ##
	""" Big Banana
	Give a minion +2/+2. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0,}
	play = ApplyBanana(TARGET, 'BGS_Treasures_000e')
	pass
BGS_Treasures_000e=buff(2,2)# <12>[1453]
""" Big Banana , Has +2/+2. """

class TB_BaconShop_Triples_01_Action(GameAction):
	def do(self, source):
		controller=source.controller
		tech_level = min(controller.tavern_tier+1,6)
		Discover(controller, RandomBGAdmissible(tech_level=tech_level)).trigger(source)
class TB_BaconShop_Triples_01:# <12>[1453]
	""" Triple Reward
	[Discover] a minion from [Tavern Tier @]. """
	play = TB_BaconShop_Triples_01_Action()
	pass



#########  appendix  ########


class BGS_Treasures_001:# <7>[1453] ### maybe ##
	""" Pocket Change
	Add 2 Gold Coins to your hand. """
	play = Give(CONTROLLER, 'GAME_005')*2
	pass

class BGS_Treasures_003:# <12>[1453] ### maybe ##
	""" Regular Discount
	Reduce the cost of upgrading Bob's Tavern by (3). """
	play = ReduceTierUpCost(CONTROLLER, 3)	
	pass

class BGS_Treasures_004:# <12>[1453] ### maybe ##
	""" Gacha Gift
	[Discover] a minion from [Tavern Tier 1]. """
	play = Discover(CONTROLLER, RandomBGAdmissible(tech_level=1))
	pass

class BGS_Treasures_006:# <8>[1453] ### maybe ##
	""" Evolving Tavern
	Replace all minions in Bob's Tavern with ones of a higher Tavern Tier. """
	def play(self):
		controller = self.controller
		bartender = controller.opponent
		new_field = []
		for card in bartender.field:
			tier = min(card.tech_level+1, 6)
			new_card = RandomBGAdmissible(tech_level=tier).evaluate(controller)
			if hasattr(new_card, '__iter__'):
				new_card=new_card[0]
			new_field.append(bartender.card(new_card))
		for card in reversed(bartender.field):
			card.zone = Zone.GRAVEYARD
		for card in new_field:
			card.zone = Zone.PLAY
	pass

class BGS_Treasures_007:# <12>[1453] ### maybe ##
	""" Might of Stormwind
	Give 3 random friendly minions +1/+1. """
	play = Buff(RANDOM(FRIENDLY_MINIONS), 'BGS_Treasures_007e'),Buff(RANDOM(FRIENDLY_MINIONS), 'BGS_Treasures_007e'),Buff(RANDOM(FRIENDLY_MINIONS), 'BGS_Treasures_007e')
	pass
BGS_Treasures_007e=buff(1,1)# <12>[1453]
""" Might of Stormwind, 	+1/+1. """

class BGS_Treasures_009:# <12>[1453] ### maybe ## 
	""" Gruul Rules 
	Give a friendly minion "At the end of your turn, gain +2/+2." """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0,}
	play = Buff(TARGET, 'BGS_Treasures_009e')
	pass
class BGS_Treasures_009e:# <12>[1453]
	""" Gruul Rules
	Gains +2/+2 at the end of your turn. """
	events = OWN_TURN_END.on(SetTag(SELF, {GameTag.ATK:2, GameTag.HEALTH:2}))
	pass

class BGS_Treasures_010:# <12>[1453] ### need check ##
	""" Time Thief
	[Discover] a minion from your last opponent's warband. """
	def play(self):
		controller = self.controller
		gamemaster = controller.game.parent
		last_warband = gamemaster.last_warband(controller)
		if len(last_warband)>0:
			if len(last_warband)>3:
				self.entourage = random.sample(last_warband,3)
			else:
				self.entourage = last_warband
			Discover(controller, RandomEntourage()).trigger(self)
	pass

class BGS_Treasures_011:# <12>[1453] ## put off ###
	""" Training Session
	[Discover] a new Hero Power. """
	#
	pass

class BGS_Treasures_012:# <12>[1453] ### maybe ##
	""" On the House
	[Discover] a minion from your current [Tavern Tier]. """
	play = Discover(CONTROLLER, RandomBGAdmissible(tech_level=TIER(CONTROLLER)))
	pass

class BGS_Treasures_013:# <12>[1453]
	""" The Good Stuff
	Give minions in Bob's Tavern +1 Attack for the rest of the game. """
	play = Buff(CONTROLLER, 'BGS_Treasures_013pe')
	pass
BGS_Treasures_013e1=buff(1,0)
""" Good Stuff, 	Increased stats. """
class BGS_Treasures_013pe:# <12>[1453]
	""" The Good Stuff Player Enchant
	Minions in Bob's Shop have increased stats. """
	####  go to Deal
	pass

class BGS_Treasures_014:# <12>[1453] ### need check ##
	""" The Unlimited Coin
	Gain 1 Gold this turn only. Return this to your hand at end of turn. """
	play = ManaThisTurnOnly(CONTROLLER, 1),Buff(CONTROLLER,'BGS_Treasures_014e')
	pass
class BGS_Treasures_014e:# <12>[1453]
	""" Unlimited Coin Return to Hand
	Return the Unlimited Coin to your hand at end of turn. """
	events = OWN_TURN_END.on(Give(CONTROLLER, 'BGS_Treasures_014'), Destroy(SELF))
	pass

class BGS_Treasures_015:# <5>[1453] ### need check widely ##
	""" Buy the Holy Light
	Give a friendly minion [Divine Shield]. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0,}
	play = SetTag(TARGET, (GameTag.DIVINE_SHIELD,)) #? 
	pass

class BGS_Treasures_016:# <12>[1453] ### maybe ##
	""" Raise the Stakes
	Make a friendly minion Golden and return it to your hand. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0,}
	def play(self):
		target = self.target
		new_card = MorphGold(target).trigger(self.controller)## And bounce it?
		new_card.zone = Zone.HAND
	pass

class BGS_Treasures_018:# <12>[1453] ### need check ##
	""" I'm Still Just a Rat in a Cage
	Give a minion +2 Attack, then double its Attack. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0,}
	def play(self):
		target = self.target
		atkbuff = target.atk + 4
		Buff(target, 'BGS_Treasures_018e', atk=atkbuff).trigger(self)
	pass
class BGS_Treasures_018e:# <12>[1453]
	""" Rat in a Cage
	This minion's Attack has been doubled. """
	pass

class BGS_Treasures_019:# <12>[1453] ### maybe ##
	""" B.A.N.A.N.A.S.
	Fill your hand with Bananas. """
	play = Give(CONTROLLER, 'DMF_065t')*10
	pass

class BGS_Treasures_020:# <12>[1453] ### maybe ##
	""" Top Shelf
	[Discover] a minion from [Tavern Tier 6]. """
	play = Discover(CONTROLLER, RandomBGAdmissible(tech_level=6))
	pass

class BGS_Treasures_022:# <12>[1453] ### maybe ##
	""" Friends and Family Discount
	For the rest of the game, minions in Bob's Tavern cost (1) less. """
	def play(self):
		self.controller.game.minionCost -= 1  ## BG_Bar
	pass
class BGS_Treasures_022e:# <12>[1453]
	""" Discounted
	Costs less. """
	pass
class BGS_Treasures_022pe:# <12>[1453]
	""" Friends and Family Discount Player Enchant
	 """
	#
	pass

class BGS_Treasures_023_Action(GameAction): ### maybe ##
	def do(self, source):
		controller=source.controller
		controller.game.rerole_free = 5
class BGS_Treasures_023:# <12>[1453]
	""" Open Bar
	Your first 5 [Refreshes]each turn cost (0). """
	events = BeginBar(CONTROLLER).on(BGS_Treasures_023_Action())
	pass
class BGS_Treasures_023pe:# <12>[1453]
	""" Refresh Cost 0
	[Refresh] costs (0). """
	#
	pass

class BGS_Treasures_025:# <12>[1453] ### maybe ##
	""" Fresh Tab
	Refresh your Gold. """
	def play(self):
		self.controller.used_mana = min(self.controller.used_mana, 0)
	pass

class BGS_Treasures_026:# <12>[1453]
	""" The Bouncer
	Give a friendly minion +6/+6 and [Taunt]. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0,}
	play = Buff(TARGET, 'BGS_Treasures_026e')
	pass
BGS_Treasures_026e=buff(6,6, taunt=True)# <12>[1453]
""" Bouncy Bouncy, 	+6/+6 and [Taunt]. """

class BGS_Treasures_028:# <12>[1453] ### Maybe ##
	""" Give A Dog A Bone
	Give a friendly minion [Divine Shield], [Windfury], and +10/+10. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0,}
	play = Buff(TARGET, 'BGS_Treasures_028e'),GiveDivineShield(TARGET) 
	pass
BGS_Treasures_028e=buff(10,10, windfury=True)# <12>[1453]
""" Dog Bone, 	Has +10/+10, [Divine Shield], and [Windfury]. """

class BGS_Treasures_029:# <12>[1453] ### maybe ##
	""" Rocking and Rolling
	Your next three [Refreshes] cost (0). """
	def play(self):
		self.controller.game.rerole_free += 3
	pass

class BGS_Treasures_030:# <12>[1453] ### maybe ##
	""" Brann's Blessing
	Your [Battlecries] trigger twice this turn. """
	play = Buff(CONTROLLER, 'BGS_Treasures_030e')
	pass
class BGS_Treasures_030e:# <0>[1453]
	""" Brann's Blessing
	Your [Battlecries] trigger twice this turn. """
	#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>
	update = Refresh(CONTROLLER, {GameTag.EXTRA_BATTLECRIES_BASE: True})
	pass

class BGS_Treasures_032:# <12>[1453] ### put off ##
	""" Big Winner!
	[Discover] a Darkmoon Prize from each of the previous Prize turns. """
	#
	pass

class BGS_Treasures_033:# <0>[1453]
	""" New Recruit
	Add a minion to Bob's Tavern for the rest of the game. """
	def play(self):
		self.controller.opponent.extra_len_bobs_field=1
	pass
class BGS_Treasures_033e:# <0>[1453]
	""" New Recruit
	Add a minion to Bob's Tavern for the rest of the game. """
	#
	pass

class BGS_Treasures_034:# <12>[1453]
	""" Repeat Customer
	Return a friendly non-golden minion to your hand. Give it +2/+2. """
	requirements = {
		PlayReq.REQ_TARGET_TO_PLAY:0, 
		PlayReq.REQ_MINION_TARGET:0, 
		PlayReq.REQ_FRIENDLY_TARGET:0,
		1003:0 # REQ_NONGOLDEN_TARGET#
		}
	play = Bounce(TARGET).on(Buff(Bounce.TARGET, 'BGS_Treasures_034e'))
	pass
BGS_Treasures_034e=buff(2,2)# <0>[1453]
""" Repeat Customer
+2/+2. """

class BGS_Treasures_036:# <12>[1453]### maybe ##
	""" Great Deal
	Reduce the cost of upgrading Bob's Tavern by (5). (24.0.3)"""
	##Reduce the cost of upgrading Bob's Tavern by (6). (24.0)"""
	##For the rest of the game, reduce the cost of upgrading Bob's Tavern by (3) at the end of your turn. """
	def play(self):
		self.controller.tavern_tierup_cost = max(self.controller.tavern_tierup_cost-5, 0)
		#self.controller.extra_tavern_tierup_reduce_cost=2
	pass
class BGS_Treasures_036e:# <0>[1453]
	""" Great Deal
	At the end of each turn, reduce the cost of upgrading Bob's Tavern by (3). [DNT] """
	pass

class BGS_Treasures_037:# <12>[1453]### maybe ##
	""" All That Glitters
	Make a random minion in Bob's Tavern Golden. """
	def play(self):
		bartender = self.controller.opponent
		tavern = bartender.field
		if len(tavern)>0:
			card = random.choice(tavern)
			MorphGold(card).trigger(self.controller)## 
	pass


class BGS_Treasures_040: ### maybe ##
	""" Banana Bunch
	Add 2 Bananas to your hand. """
	play = Give(CONTROLLER, 'DMF_065t')*2
	pass


##
## secret
##


class TB_Bacon_Secrets_01:# <3>[1453]
	""" Venomstrike Trap
	[Secret:] When one of your minions is attacked, summon a 2/3_[Poisonous] Cobra. """
	secret = BG_Attack(ENEMY, FRIENDLY_MINIONS).on(
		Summon(CONTROLLER, 'TB_Bacon_Secrets_01t'),
		DestroyOriginal(SELF)
		)
	pass
@custom_card
class TB_Bacon_Secrets_01t:
	tags = {
		GameTag.CARDNAME: "猛毒コブラ",#猛毒コブラ#Poisonous Cobra
		GameTag.CARDTEXT: "",
		GameTag.CARDTYPE: CardType.MINION,
		GameTag.ATK: 2,
		GameTag.HEALTH: 3,
		GameTag.TECH_LEVEL: 1,
		GameTag.POISONOUS: 1,
	}
class TB_Bacon_Secrets_02:# <3>[1453]
	""" Snake Trap
	[Secret:] When one of your minions is attacked, summon three 1/1 Snakes. """
	secret = BG_Attack(CHARACTER, FRIENDLY_MINIONS).on(
		Summon(CONTROLLER, 'TB_Bacon_Secrets_02t')*3,
		DestroyOriginal(SELF)
	)
	pass
@custom_card
class TB_Bacon_Secrets_02t:
	tags = {
		GameTag.CARDNAME: "ヘビ",#ヘビ#Snake
		GameTag.CARDTEXT: "",
		GameTag.CARDTYPE: CardType.MINION,
		GameTag.ATK: 1,
		GameTag.HEALTH: 1,
		GameTag.TECH_LEVEL: 1,
	}
class TB_Bacon_Secrets_04:# <4>[1453]
	""" Splitting Image
	[Secret:] When one of your minions is attacked, summon a copy of it. """
	secret = BG_Attack(CHARACTER, FRIENDLY_MINIONS).on(
		Summon(CONTROLLER, ExactCopy(Attack.DEFENDER)),
		DestroyOriginal(SELF)
		)
	pass
class TB_Bacon_Secrets_05:# <4>[1453]
	""" Effigy
	[Secret:] When a friendly minion dies, summon a random minion with the same Cost. """
	secret = Death(FRIENDLY + MINION).on(
		Summon(CONTROLLER, RandomBGAdmissible(tech_level=TECH_LEVEL(Death.ENTITY))),
		DestroyOriginal(SELF)
		)
	pass

class TB_Bacon_Secrets_07:# <5>[1453]
	""" Autodefense Matrix
	[Secret:] When one of your minions is attacked, give it [Divine Shield]. """
	secret = BG_Attack(CHARACTER, FRIENDLY_MINIONS).on(
		GiveDivineShield(Attack.DEFENDER),
		DestroyOriginal(SELF)
		)
	pass

class TB_Bacon_Secrets_08:# <5>[1453]
	""" Avenge
	[Secret:] When one of your minions dies, give a random friendly minion +3/+2. """
	secret = Death(FRIENDLY + MINION).on( 
		Buff(RANDOM_FRIENDLY_MINION, 'TB_Bacon_Secrets_08e') ,
		DestroyOriginal(SELF)
		)
	pass
@custom_card
class TB_Bacon_Secrets_08e:
	tags = {
		GameTag.CARDNAME: "Avenge buff",
		GameTag.CARDTEXT: "",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.ATK: 3,
		GameTag.HEALTH: 2,
	}

class TB_Bacon_Secrets_10:# <5>[1453]
	""" Redemption
	[Secret:] When a friendly minion dies, return it to life with 1 Health. """
	secret = Death(FRIENDLY_MINIONS).on(
		SetAttr(Death.ENTITY, 'reborn', True),
		DestroyOriginal(SELF)
		)
	pass

class TB_Bacon_Secrets_11:# <5>[1453]
	""" Hand of Salvation
	[Secret:] When your second minion dies in a turn, return it to life. """
	#secret = ?????
	pass

class TB_Bacon_Secrets_12:# <4>[1453]
	""" Ice Block
	[Secret:] When your hero takes fatal damage, prevent it and become [Immune] this turn. """
	#?????
	pass

class TB_Bacon_Secrets_13:# <5>[1453]
	""" Competitive Spirit
	[Secret:] When your turn starts, give your minions +1/+1. """
	secret = BeginBattleTurn(CONTROLLER).on(
		Buff(FRIENDLY_MINIONS,'TB_Bacon_Secrets_13e'),
		DestroyOriginal(SELF)
		)
	pass

TB_Bacon_Secrets_13e=buff(1,1)# <12>[1453]

##
##  button and others
##

class TB_BaconShop_1P_PlayerE:# <12>[1453]
	""" BaconShop1PlayerEnchant
	 """
	#
	pass

class TB_BaconShop_1p_Reroll_Button:# <12>[1453]
	""" Refresh
	Replace Bob's Tavern with new minions. """
	#
	pass

class TB_BaconShop_3ofKindChecke:# <12>[1453]
	""" 3ofKindCheckPlayerEnchant
	 """
	#
	pass

class TB_BaconShop_8P_PlayerE:# <12>[1453]
	""" BaconShop8PlayerEnchant
	 """
	#
	pass

class TB_BaconShop_8p_Reroll_Button:# <12>[1453]
	""" Refresh
	Replace Bob's Tavern with new minions. """
	#
	pass

class TB_BaconShop_CheckPtntlTriples:# <12>[1453]
	""" Check Potential Triples
	3ofKindCheck [DNT] """
	#
	pass

class TB_BaconShop_CheckTriples:# <12>[1453]
	""" Check Triples
	3ofKindCheck [DNT] """
	#
	pass

class TB_BaconShop_DragBuy:# <12>[1453]
	""" Drag To Buy
	 """
	#
	pass

class TB_BaconShop_DragSell:# <12>[1453]
	""" Drag To Sell
	 """
	#
	pass

class TB_BaconShop_FXWatcher:# <12>[1453]
	""" Leaderboard FX Watcher [DNT]
	 """
	#
	pass


class TB_BaconShop_IncreasedStats:# <12>[1453]
	""" Increased Stats for Triple
	 """
	#
	pass


class TB_BaconShop_UpdateDmgCap:# <12>[1453]
	""" Update Damage Cap [DNT]
	Checks if any players are dead and updates the Damage Cap tag on the GameEntity accordingly. [DNT] """
	#
	pass

class TB_BaconShopBadsongE:# <2>[1453]
	""" Costs 0
	Costs (0). """
	#
	pass


class TB_BaconShopBob_SKIN_A:# <12>[1453]
	""" Ragnaros, Tikilord
	 """
	#
	pass

class TB_BaconShopBob_SKIN_B:# <12>[1453]
	""" Ve'nari
	 """
	#
	pass

class TB_BaconShopBob_SKIN_C:# <12>[1453]
	""" Dragonspeaker Bob
	 """
	#
	pass

class TB_BaconShopBob_SKIN_D:# <12>[1453]
	""" Fizzy
	 """
	#
	pass

class TB_BaconShopBob_SKIN_E:# <12>[1453]
	""" Mega Bob
	 """
	#
	pass

class TB_BaconShopBob_SKIN_F:# <12>[1453]
	""" Gala Medivh
	 """
	#
	pass

class TB_BaconShopBob_SKIN_G:# <12>[1453]
	""" Pirate Bob
	 """
	#
	pass

class TB_BaconShopBob_SKIN_H:# <12>[1453]
	""" Flightmaster Dungar
	 """
	#
	pass

class TB_BaconShopBob_SKIN_I:# <12>[1453]
	""" Alterac Bob
	 """
	#
	pass

class TB_BaconShopBob_SKIN_J:# <12>[1453]
	""" Bartendotron
	 """
	#
	pass

class TB_BaconShopBob_SKIN_K:# <12>[1453]
	""" Greatfather Boom
	 """
	#
	pass

class TB_BaconShopBob_SKIN_L:# <12>[1453]
	""" Elder Starsong
	 """
	#
	pass

class TB_BaconShopBob_SKIN_M:# <12>[1453]
	""" Algalon
	 """
	#
	pass

class TB_BaconShopLockAll_Button:# <12>[1453]
	""" Freeze
	[Freeze] / [Unfreeze] the minions in Bob's Tavern. """
	#
	pass

class TB_BaconShopTechUp02_Button:# <12>[1453]
	""" Tavern Tier 2
	Bob sells higher tier minions when you [Refresh]. """
	#
	pass

class TB_BaconShopTechUp03_Button:# <12>[1453]
	""" Tavern Tier 3
	Bob sells higher tier minions when you [Refresh]. """
	#
	pass

class TB_BaconShopTechUp04_Button:# <12>[1453]
	""" Tavern Tier 4
	Bob sells higher tier minions when you [Refresh]. """
	#
	pass

class TB_BaconShopTechUp05_Button:# <12>[1453]
	""" Tavern Tier 5
	Bob sells higher tier minions when you [Refresh]. """
	#
	pass

class TB_BaconShopTechUp06_Button:# <12>[1453]
	""" Tavern Tier 6
	Bob sells higher tier minions when you [Refresh]. """
	#
	pass

