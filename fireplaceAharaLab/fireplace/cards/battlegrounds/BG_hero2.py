from ..utils import *

BG_Hero2=[]
BG_PoolSet_Hero2=[]
BG_Hero2_Buddy={}
BG_Hero2_Buddy_Gold={}



############ source ############################

## E.T.C., Band Manager BG25_HERO_105 ##
BG_Hero2+=['BG25_HERO_105','BG25_HERO_105p','BG25_HERO_105_Buddy','BG25_HERO_105_Buddy_G']
BG_PoolSet_Hero2+=['BG25_HERO_105']
BG_Hero2_Buddy['BG25_HERO_105']='BG25_HERO_105_Buddy'
BG_Hero2_Buddy_Gold['BG25_HERO_105_Buddy']='BG25_HERO_105_Buddy_G'
class BG25_HERO_105:
	"""E.T.C., Band Manager
	"""
class BG25_HERO_105p_Action(GameAction):##
	def do(self, source):
		gamemaster = source.controller.game.parent
		buddies=gamemaster.BG_Hero_Buddy.values()
		buddies.remove('BG25_HERO_105_Buddy')
		Discover(source.controller, RandomID(*buddies)*3).trigger(source)
class BG25_HERO_105p:##
	""" Sign a New Artist
	[Discover] a Buddy. &lt;i&gt;(Unlocks at Tier 2.)&lt;/i&gt;"""
	requirements = { PlayReq.REQ_MINIMUM_TAVERN_TIER_LEVEL_TO_PLAY:2, }
	play = BG25_HERO_105p_Action()
###### BUDDY ######
class BG25_HERO_105_Buddy_Action(GameAction):###
	def do(self, source):
		gamemaster=source.controller.game.parent
		cards = [card for card in source.controller.field+source.controller.hand if card.id in gamemaster.BG_HeroBuddy.values()]
		if len(cards):
			card = random.choice(cards)
			source.controller.game.BG_deal_gold(card.id)
		pass
class BG25_HERO_105_Buddy:###
	""" Talent Scout
	[Battlecry:] Make a Buddy Golden."""
	play = BG25_HERO_105_Buddy_Action()
class BG25_HERO_105_Buddy_G:###
	""" Talent Scout
	[Battlecry:] Make a Buddy Golden."""
	play = BG25_HERO_105_Buddy_Action()
	pass



##Edwin VanCleef ### HP OK ###
BG_Hero2+=['TB_BaconShop_HERO_01','TB_BaconShop_HP_001','TB_BaconShop_HP_001e','TB_BaconShop_HERO_01_Buddy','TB_BaconShop_HERO_01_Buddy_e','TB_BaconShop_HERO_01_Buddy_G','TB_BaconShop_HERO_01_Buddy_G_e']
BG_PoolSet_Hero2+=['TB_BaconShop_HERO_01']
BG_Hero2_Buddy['TB_BaconShop_HERO_01']='TB_BaconShop_HERO_01_Buddy'
BG_Hero2_Buddy_Gold['TB_BaconShop_HERO_01_Buddy']='TB_BaconShop_HERO_01_Buddy_G'
class TB_BaconShop_HERO_01:# <12>[1453]
	""" Edwin VanCleef  """
class TB_BaconShop_HP_001_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = source.controller
		amount = len(controller.buy_this_turn_log())
		if amount>0:
			Buff(target, 'TB_BaconShop_HP_001e', 
				atk=2*amount, max_health=amount
				).trigger(source)
		pass
class TB_BaconShop_HP_001:
	""" Sharpen Blades 
	Give a minion +2/+1 for each minion you've bought this turn."""
	## Give a friendly minion +2/+1 for each minion _you've bought this turn.""" <= 23.6
	requirements = {
		PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0
		}
	activate = TB_BaconShop_HP_001_Action(TARGET)
class TB_BaconShop_HP_001e:
	pass
###### BUDDY ######
class TB_BaconShop_HERO_01_Buddy:# <12>[1453]
	""" SI:7 Scout
	After you buy a minion, gain +1/+1. """
	events = Buy(CONTROLLER).after(Buff(SELF, 'TB_BaconShop_HERO_01_Buddy_e'))
	pass
TB_BaconShop_HERO_01_Buddy_e=buff(1,1)# <12>[1453]
""" Scouting +1/+1. """
class TB_BaconShop_HERO_01_Buddy_G:# <12>[1453]
	""" SI:7 Scout
	After you buy a minion, gain +2/+2. """
	events = Buy(CONTROLLER).after(Buff(SELF, 'TB_BaconShop_HERO_01_Buddy_G_e'))
	pass
TB_BaconShop_HERO_01_Buddy_G_e=buff(2,2)# <12>[1453]
""" Scouting +2/+2. """




##Elise Starseeker #### HP OK 24.0.3
BG_Hero2+=['TB_BaconShop_HERO_42','TB_BaconShop_HP_047','TB_BaconShop_HP_047t','TB_BaconShop_HERO_42_Buddy','TB_BaconShop_HERO_42_Buddy_e','TB_BaconShop_HERO_42_Buddy_G','TB_BaconShop_HERO_42_Buddy_G_e',]
BG_PoolSet_Hero2+=['TB_BaconShop_HERO_42']
BG_Hero2_Buddy['TB_BaconShop_HERO_42']='TB_BaconShop_HERO_42_Buddy'
BG_Hero2_Buddy_Gold['TB_BaconShop_HERO_42_Buddy']='TB_BaconShop_HERO_42_Buddy_G'
class TB_BaconShop_HERO_42:# <12>[1453]
	""" Elise Starseeker """
class TB_BaconShop_HP_047_Choice(Choice):
	def do(self, source, player, cards, option=None):
		if len(cards)==1 and cards[0]==[]:
			if random_picker.BG_races==[]:
				random_picker.BG_races=player.game.parent.BG_races
			cards=[]
			for repeat in range(3):
				cards += RandomBGAdmissible(tech_level=player.tavern_tier).evaluate(source)
		super().do(source, player, cards, option)
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		card.controller = self.player
		card.zone=Zone.HAND

class TB_BaconShop_HP_047:
	""" Lead Explorer 
	[Discover] a minion from your Tavern tier. Costs (1) more after each use."""
	activate = TB_BaconShop_HP_047_Choice(CONTROLLER, RandomBGAdmissible(tech_level=TIER(CONTROLLER))*3),Buff(SELF,'TB_BaconShop_HP_047e')
	## until 24.0
	##[Passive] When you upgrade  Bob's Tavern get a 'Recruitment Map'."""
	##events = UpgradeTier(CONTROLLER).after(Give(CONTROLLER, 'TB_BaconShop_HP_047t').then(SetScriptDataNum1(Give.CARD, TIER(CONTROLLER))))
class TB_BaconShop_HP_047t_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		card.BG_cost=self.player.game.minionCost
		card.controller = self.player
		card.zone=Zone.HAND
class TB_BaconShop_HP_047t:
	""" Recruitment Map
	[Discover] a minion from [Tavern Tier @]."""
	play = TB_BaconShop_HP_047t_Choice(CONTROLLER, RandomBGAdmissible(tech_level=TIER(CONTROLLER))*3)
	# Here we activate 'choicecard.BG_cost = bar.cardCost'
@custom_card
class TB_BaconShop_HP_047e:
	tags = {
		GameTag.CARDNAME: "Lead Explorer",
		GameTag.CARDTEXT: "Costs (1) more",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.COST: 1,
	}
###### BUDDY ######
class TB_BaconShop_HERO_42_Buddy:# <12>[1453] ######################################################
	""" Jr. Navigator
	&lt;b&gt;Battlecry:&lt;/b&gt; Reduce the Cost of 'Lead Explorer' by (2)."""
	###At the start of your turn,get a 'Recruitment Map.'Your Maps cost (1). ### old one
	play = Buff(FRIENDLY_HERO_POWER, 'TB_BaconShop_HERO_42_Buddy_e')
	pass
TB_BaconShop_HERO_42_Buddy_e=buff(cost=-2)# <12>[1453]
""" In The Distance,	Costs (2) less. """
class TB_BaconShop_HERO_42_Buddy_G:# <12>[1453]
	""" Jr. Navigator
	&lt;b&gt;Battlecry:&lt;/b&gt; Reduce the Cost of 'Lead Explorer' by (4)."""
	###At the start of your turn,get 2 'Recruitment Maps.'Your Maps cost (1). ###
	play = Buff(FRIENDLY_HERO_POWER, 'TB_BaconShop_HERO_42_Buddy_G_e')
	pass
TB_BaconShop_HERO_42_Buddy_G_e=buff(cost=-4)# <12>[1453]
""" In The Distance, 	Costs (4) less. """



##Enhance-o Mechano BG24_HERO_204 ## new 25.0
BG_Hero2+=[
	'BG24_HERO_204','BG24_HERO_204p',
	'BG24_HERO_204_Buddy','BG24_HERO_204_Buddye2','BG24_HERO_204_Buddy_G']
BG_PoolSet_Hero2+=['BG24_HERO_204']
BG_Hero2_Buddy['BG24_HERO_204']='BG24_HERO_204_Buddy'
BG_Hero2_Buddy_Gold['BG24_HERO_204_Buddy']='BG24_HERO_204_Buddy_G'
class BG24_HERO_204:
	""" Enhance-o Mechano """
class BG24_HERO_204p_Action(GameAction):
	def do(self, source):
		controller=source.controller
		exts=['taunt','windfury','reborn','divine_shield']
		ext=random.choice(exts)
		card=random.choice(controller.opponent.field)
		if getattr(card, ext, False):
			exts.remove(ext)
			ext=random.choice(exts)
		if ext=='taunt':
			card.data.tags[GameTag.TAUNT]=True
		elif ext=='windfury':
			card.data.tags[GameTag.WINDFURY]=1
		elif ext=='reborn':
			card.data.tags[GameTag.REBORN]=True
		elif ext=='divine_shield':
			card.data.tags[GameTag.DIVINE_SHIELD]=True
class BG24_HERO_204p:
	""" Enhancification
	[x][Passive.] After each [Refresh], give a minion in Bob's Tavern [Taunt], [Windfury], _[Reborn], or [Divine Shield]."""
	events = Rerole(CONTROLLER).after(BG24_HERO_204p_Action())
###### Buddy ######
class BG24_HERO_204_Buddy_Action(GameAction):
	def do(self, source):
		for card in source.controller.opponent.field:
			if card.taunt:
				Buff(card, 'BG24_HERO_204_Buddye2', atk=2, max_health=2).trigger(source)
			if card.reborn:
				Buff(card, 'BG24_HERO_204_Buddye2', atk=2, max_health=2).trigger(source)
			if card.windfury>0:
				Buff(card, 'BG24_HERO_204_Buddye2', atk=2, max_health=2).trigger(source)
			if card.devine_shield:
				Buff(card, 'BG24_HERO_204_Buddye2', atk=2, max_health=2).trigger(source)
class BG24_HERO_204_Buddy:
	""" Enhance-o Medico
	Minions in Bob's Tavern with &lt;b&gt;Taunt&lt;/b&gt;, &lt;b&gt;Reborn&lt;/b&gt;, &lt;b&gt;Windfury&lt;/b&gt;, or &lt;b&gt;Divine Shield&lt;/b&gt; have +2/+2 for each."""
	events = Rerole(CONTROLLER).on(BG24_HERO_204_Buddy_Action())
	pass
class BG24_HERO_204_Buddye2:
	pass
class BG24_HERO_204_Buddy_G_Action(GameAction):
	def do(self, source):
		for card in source.controller.opponent.field:
			if card.taunt:
				Buff(card, 'BG24_HERO_204_Buddye2', atk=4, max_health=4).trigger(source)
			if card.reborn:
				Buff(card, 'BG24_HERO_204_Buddye2', atk=4, max_health=4).trigger(source)
			if card.windfury>0:
				Buff(card, 'BG24_HERO_204_Buddye2', atk=4, max_health=4).trigger(source)
			if card.devine_shield:
				Buff(card, 'BG24_HERO_204_Buddye2', atk=4, max_health=4).trigger(source)
class BG24_HERO_204_Buddy_G:
	""" Enhance-o Medico
	Minions in Bob's Tavern with &lt;b&gt;Taunt&lt;/b&gt;, &lt;b&gt;Reborn&lt;/b&gt;, &lt;b&gt;Windfury&lt;/b&gt;, or &lt;b&gt;Divine Shield&lt;/b&gt; have +4/+4  for each."""
	events = Rerole(CONTROLLER).on(BG24_HERO_204_Buddy_G_Action())
	pass




##Forest Warden Omu #### HP OK ###
BG_Hero2+=['TB_BaconShop_HERO_74','TB_BaconShop_HP_082','TB_BaconShop_HERO_74_Buddy','TB_BaconShop_HERO_74_Buddy_e','TB_BaconShop_HERO_74_Buddy_G',]
BG_PoolSet_Hero2+=['TB_BaconShop_HERO_74']
BG_Hero2_Buddy['TB_BaconShop_HERO_74']='TB_BaconShop_HERO_74_Buddy'
BG_Hero2_Buddy_Gold['TB_BaconShop_HERO_74_Buddy']='TB_BaconShop_HERO_74_Buddy_G'
class TB_BaconShop_HERO_74:# <12>[1453]
	""" Forest Warden Omu  """
class TB_BaconShop_HP_082:
	""" Everbloom
	[Passive] After you upgrade Bob's Tavern, gain 2 Gold this turn only."""
	events = UpgradeTier(CONTROLLER).after(ManaThisTurnOnly(CONTROLLER,2))
######## BUDDY
class TB_BaconShop_HERO_74_Buddy:# <12>[1453]
	""" Evergreen Botani
	At the end of your turn, add a random minion of your_Tavern Tier to your hand. """
	events = OWN_TURN_END.on(Give(CONTROLLER, RandomBGMinion(tech_level=TIER(CONTROLLER))))
	pass
class TB_BaconShop_HERO_74_Buddy_e:# <10>[1453]
	""" Evergreen Increased stats. """
class TB_BaconShop_HERO_74_Buddy_G:# <12>[1453]
	""" Evergreen Botani
	At the end of your turn, add2 random minions of your_Tavern Tier to your hand. """
	events = OWN_TURN_END.on(Give(CONTROLLER, RandomBGMinion(tech_level=TIER(CONTROLLER))), Give(CONTROLLER, RandomBGMinion(tech_level=TIER(CONTROLLER))))
	pass




##Fungalmancer Flurgl ### OK ###
BG_Hero2+=['TB_BaconShop_HERO_55','TB_BaconShop_HP_056','TB_BaconShop_HERO_55_Buddy','TB_BaconShop_HERO_55_Buddy_G',]
BG_PoolSet_Hero2+=['TB_BaconShop_HERO_55']
BG_Hero2_Buddy['TB_BaconShop_HERO_55']='TB_BaconShop_HERO_55_Buddy'
BG_Hero2_Buddy_Gold['TB_BaconShop_HERO_55_Buddy']='TB_BaconShop_HERO_55_Buddy_G'
class TB_BaconShop_HERO_55:# <12>[1453]
	""" Fungalmancer Flurgl  """
	pass
class TB_BaconShop_HP_056:
	""" Gone Fishing
	[Passive.] After you sell 5 minions, get a random Murloc. (@ left.) """ ## new 24.4.3
	events = Sell(CONTROLLER).on(SidequestCounter(SELF, 5, [Give(CONTROLLER, RandomBGMurloc())]))
	##[Passive.] After you sell 4 minions, get a random Murloc. (@ left.) """ ## new 24.2
	##[Passive] After you sell two minions, add a random Murloc to Bob's Tavern. old 
	#events = Sell(CONTROLLER).on(SidequestCounter(SELF, 2, 
	#	[Summon(OPPONENT, RandomBGMurloc(tech_level_less=TIER(CONTROLLER)))] #
	#))
	pass
###### BUDDY ######
class TB_BaconShop_HERO_55_Buddy_Action(GameAction):
	def do(self, source):
		controller=source.controller
		for card in reversed(controller.field):
			tier=card.tech_level
			Morph(card, RandomBGMurloc(tech_level=tier)).trigger(source)
class TB_BaconShop_HERO_55_Buddy:
	""" Sparkfin Soothsayer
	&lt;b&gt;Battlecry:&lt;/b&gt; Transform minions in Bob's Tavern into Murlocs of the same Tavern Tier."""
	play = TB_BaconShop_HERO_55_Buddy_Action()
	pass
class TB_BaconShop_HERO_55_Buddy_G_Action(GameAction):
	def do(self, source):
		controller=source.controller
		for card in reversed(controller.field):
			tier=min(card.tech_level+1,6)
			Morph(card, RandomBGMurloc(tech_level=tier)).trigger(source)
class TB_BaconShop_HERO_55_Buddy_G:
	""" Sparkfin Soothsayer
	&lt;b&gt;Battlecry:&lt;/b&gt; Transform minions in Bob's Tavern into Murlocs of a higher Tavern Tier."""
	play = TB_BaconShop_HERO_55_Buddy_G_Action()
	pass




##Galakrond  ### HP OK ###
BG_Hero2+=['TB_BaconShop_HERO_02','TB_BaconShop_HP_011','TB_BaconShop_HERO_02_Buddy','TB_BaconShop_HERO_02_Buddy_G',]
BG_PoolSet_Hero2+=['TB_BaconShop_HERO_02']
BG_Hero2_Buddy['TB_BaconShop_HERO_02']='TB_BaconShop_HERO_02_Buddy'
BG_Hero2_Buddy_Gold['TB_BaconShop_HERO_02_Buddy']='TB_BaconShop_HERO_02_Buddy_G'
class TB_BaconShop_HERO_02:# <12>[1453]
	""" Galakrond """
class TB_BaconShop_HP_011_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		card.controller = card.controller.opponent# bartender
		card.zone=Zone.PLAY
class TB_BaconShop_HP_011_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source,target):
		controller = source.controller
		tier = min(target.tech_level+1,6)
		target.zone = Zone.GRAVEYARD ### let deathrattle does not happen
		TB_BaconShop_HP_011_Choice(controller, RandomBGAdmissible(tech_level=tier)*3).trigger(source)
class TB_BaconShop_HP_011:
	""" Galakrond's Greed
	Choose a minion in Bob's Tavern. [Discover] a higher Tier minion to replace it."""
	requirements = {
		PlayReq.REQ_TARGET_TO_PLAY:0,
		PlayReq.REQ_ENEMY_TARGET:0,
		PlayReq.REQ_MINION_TARGET:0,
		}
	activate = TB_BaconShop_HP_011_Action(TARGET)
	pass
######## BUDDY
class TB_BaconShop_HERO_02_Buddy_Action(GameAction):
	def do(self, source):
		controller=source.controller
		for card in reversed(controller.field):
			tier=min(card.tech_level+1,6)
			Morph(card, RandomBGMinion(tech_level=tier)).trigger(source)
class TB_BaconShop_HERO_02_Buddy:# <12>[1453]
	""" Apostle of Galakrond
	[Battlecry:] Replace minions in Bob's Tavern with ones of a higher Tavern Tier. """
	play = TB_BaconShop_HERO_02_Buddy_Action()
	pass
class TB_BaconShop_HERO_02_Buddy_G_Action(GameAction):
	def do(self, source):
		controller=source.controller
		for card in reversed(controller.field):
			tier=min(card.tech_level+2,6)
			Morph(card, RandomBGMinion(tech_level=tier)).trigger(source)
class TB_BaconShop_HERO_02_Buddy_G:# <12>[1453]
	""" Apostle of Galakrond
	[Battlecry:] Replaceminions in Bob's Tavernwith ones of a higherTavern Tier twice. """
	play = TB_BaconShop_HERO_02_Buddy_G_Action()
	pass



##Galewing   ### HP OK ###
BG_Hero2+=[
	'BG20_HERO_283',
	'BG20_HERO_283p','BG20_HERO_283p_t1','BG20_HERO_283p_t1e','BG20_HERO_283p_t2','BG20_HERO_283p_t3',
	'BG20_HERO_283_Buddy',
	'BG20_HERO_283_Buddy_G',]
BG_PoolSet_Hero2+=['BG20_HERO_283']
BG_Hero2_Buddy['BG20_HERO_283']='BG20_HERO_283_Buddy'
BG_Hero2_Buddy_Gold['BG20_HERO_283_Buddy']='BG20_HERO_283_Buddy_G'
class BG20_HERO_283:# <12>[1453]
	""" Galewing """
class BG20_HERO_283p_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		controller = self.player
		if card.type != CardType.HERO_POWER:
			return
		ChangeHeroPower(controller, card).trigger(self.source)
		card.activate()
	pass
class BG20_HERO_283p:# <12>[1453]#
	""" Dungar's Gryphon
	Choose a flightpath. Complete it to get a bonus! """
	entourage=['BG20_HERO_283p_t1','BG20_HERO_283p_t2','BG20_HERO_283p_t3']
	activate = BG20_HERO_283p_Choice(CONTROLLER, RandomEntourage()*3)
	pass
class BG20_HERO_283p_t1_Action(GameAction):
	def do(self, source):
		controller = source.controller
		if controller.field!=[]:
			Buff(controller.field[0], 'BG20_HERO_283p_t1e').trigger(source)
			if len([cd for cd in controller.field if cd.id=='BG20_HERO_283_Buddy']):
				Buff(controller.field[0], 'BG20_HERO_283p_t1e').trigger(source)
			if len([cd for cd in controller.field if cd.id=='BG20_HERO_283_Buddy_G']):
				Buff(controller.field[0], 'BG20_HERO_283p_t1e').trigger(source)
				Buff(controller.field[0], 'BG20_HERO_283p_t1e').trigger(source)
		ChangeHeroPower(controller, 'BG20_HERO_283p').trigger(source)
		pass
class BG20_HERO_283p_t1:# <12>[1453]
	""" Westfall
	&lt;b&gt;Passive.&lt;/b&gt; In 1 turn, give your left-most minion +2/+2. &lt;i&gt;(@ left!)&lt;/i&gt;"""
	### [Passive.] In 1 turn, give your left-most minion +2/+1. <i>(@ left!)</i> """
	events = BeginBar(CONTROLLER).on(SidequestCounter(SELF, 1, [BG20_HERO_283p_t1_Action()]))
	#
	pass
BG20_HERO_283p_t1e=buff(2,2)# new 25.6
#BG20_HERO_283p_t1e=buff(2,1)# new 24.2
#BG20_HERO_283p_t1e=buff(2,0)# 
""" Westfall,	+2 Attack. """
#class BG20_HERO_283p_t2_Choice(Choice):
#	def do(self, source, player, cards, option=None):
#		controller = player
#		super().do(source,player,cards)
#		choiceAction(controller)
#		ChangeHeroPower(controller, 'BG20_HERO_283p').trigger(source)
#		pass
#	def choose(self, card):
#		self.next_choice=None
#		super().choose
#		card.zone=Zone.HAND
#		self.player.choice=None
#		pass
class BG20_HERO_283p_t2_Action(GameAction):
	def do(self, source):
		controller = source.controller
		ManaThisTurn(controller,2).trigger(source)
		if len([cd for cd in controller.field if cd.id=='BG20_HERO_283_Buddy']):
			ManaThisTurn(controller,2).trigger(source)
		if len([cd for cd in controller.field if cd.id=='BG20_HERO_283_Buddy_G']):
			ManaThisTurn(controller,2).trigger(source)
			ManaThisTurn(controller,2).trigger(source)
		ChangeHeroPower(controller, 'BG20_HERO_283p').trigger(source)
		pass
class BG20_HERO_283p_t2:# <12>[1453]
	""" Ironforge
	&lt;b&gt;Passive&lt;/b&gt; In 2 turns, gain 2 Gold. &lt;i&gt;(@ left!)&lt;/i&gt;"""
	## [Passive.] In 3 turns,[Discover] a minion of your Tavern Tier. <i>(@ left!)</i> """
	events = BeginBar(CONTROLLER).on(SidequestCounter(SELF, 2, [\
		BG20_HERO_283p_t2_Action()
		##BG20_HERO_283p_t2_Choice(CONTROLLER, RandomBGAdmissible(tech_level=TIER(CONTROLLER))*3)
	]))
	#
	pass
class BG20_HERO_283p_t3_Choice(Choice):
	def do(self, source, player, cards, option=None):
		controller = player
		super().do(source,player,cards)
		choiceAction(controller)
		ChangeHeroPower(controller, 'BG20_HERO_283p').trigger(source)
		pass
	def choose(self, card):
		choice_counter=1
		if len([cd for cd in self.source.controller.field if cd.id=="BG20_HERO_283_Buddy"]):
			choice_counter+=1
		if len([cd for cd in self.source.controller.field if cd.id=="BG20_HERO_283_Buddy_G"]):
			choice_counter+=2
		self.source.sidequest_counter += 1
		if self.source.sidequest_counter>=choice_counter:
			self.next_choice=None
		else:
			tier=self.source.controller.tavern_tier
			self.next_choice=BG20_HERO_283p_t3_Choice(self.source.controller, RandomBGAdmissible(tech_level=tier)*3)
			self.next_choicea.trigger(self.source)
		super().choose
		card.zone=Zone.HAND
		self.player.choice=None
		pass

#class BG20_HERO_283p_t3_Action(GameAction):
#	def do(self, source):
#		controller=source.controller
#		ReduceTierUpCost(controller, 6).trigger(source)
#		ChangeHeroPower(controller, 'BG20_HERO_283p').trigger(source)
#		pass
class BG20_HERO_283p_t3:# <12>[1453]
	""" Eastern Plaguelands
	&lt;b&gt;Passive.&lt;/b&gt; In 3 turns, &lt;b&gt;Discover&lt;/b&gt; a minion of your Tavern Tier. &lt;i&gt;(@ left!)&lt;/i&gt;"""
	##[Passive.] In 5 turns, your next Tavern Tier upgrade costs (6) less. <i>(@ left!)</i> """
	events = BeginBar(CONTROLLER).on(SidequestCounter(SELF, 3, [
		BG20_HERO_283p_t3_Choice(CONTROLLER, RandomBGAdmissible(tech_level=TIER(CONTROLLER))*3)
		]))
	pass
######## BUDDY
class BG20_HERO_283_Buddy:# <12>[1453]
	""" Flight Trainer
	Your flightpaths trigger twice."""
	### At the end of your turn, progress your flight path by_1 turn. ### old one
	#
	pass
class BG20_HERO_283_Buddy_G:# <12>[1453]
	""" Flight Trainer
	Your flightpaths trigger three times."""
	### At the end of your turn, progress your flightpath by_2 turns. ### old one
	#
	pass



##George the Fallen #### OK ####
BG_Hero2+=['TB_BaconShop_HERO_15','TB_BaconShop_HP_010','TB_BaconShop_HERO_15_Buddy','TB_BaconShop_HERO_15_Buddy_e','TB_BaconShop_HERO_15_Buddy_G','TB_BaconShop_HERO_15_Buddy_G_e',]
BG_PoolSet_Hero2+=['TB_BaconShop_HERO_15']
BG_Hero2_Buddy['TB_BaconShop_HERO_15']='TB_BaconShop_HERO_15_Buddy'
BG_Hero2_Buddy_Gold['TB_BaconShop_HERO_15_Buddy']='TB_BaconShop_HERO_15_Buddy_G'
class TB_BaconShop_HERO_15:# <12>[1453]
	""" George the Fallen  """
class TB_BaconShop_HP_010:
	""" Boon of Light
	Give a minion [Divine Shield]."""
	## divine shield without buff
	requirements = {
		PlayReq.REQ_TARGET_TO_PLAY:0,
		PlayReq.REQ_FRIENDLY_TARGET:0,
		PlayReq.REQ_MINION_TARGET:0,
		}
	activate = GiveDivineShield(TARGET)
######## BUDDY
class TB_BaconShop_HERO_15_Buddy:# <12>[1453]
	""" Karl the Lost
	After you use your Hero Power, give your [Divine Shield] minions +2_Attack. """
	events = Activate(CONTROLLER).on(Buff(Activate.TARGET, 'TB_BaconShop_HERO_15_Buddy_e'))
	pass
TB_BaconShop_HERO_15_Buddy_e=buff(2,0)# <12>[1453]
""" Lost and Found,	+2 Attack. """
class TB_BaconShop_HERO_15_Buddy_G:# <12>[1453]
	""" Karl the Lost
	After you use your Hero Power, give your [Divine Shield] minions +4_Attack. """
	events = Activate(CONTROLLER).on(Buff(Activate.TARGET, 'TB_BaconShop_HERO_15_Buddy_G_e'))
	pass
TB_BaconShop_HERO_15_Buddy_G_e=buff(4,0)# <12>[1453]
""" Lost and Found,	+4 Attack. """




##Greybough  ### HP OK ###
BG_Hero2+=['TB_BaconShop_HERO_95','TB_BaconShop_HP_107','TB_BaconShop_HP_107e','TB_BaconShop_HERO_95_Buddy','TB_BaconShop_HERO_95_Buddy_e','TB_BaconShop_HERO_95_Buddy_G','TB_BaconShop_HERO_95_Buddy_G_e',]
BG_PoolSet_Hero2+=['TB_BaconShop_HERO_95']
BG_Hero2_Buddy['TB_BaconShop_HERO_95']='TB_BaconShop_HERO_95_Buddy'
BG_Hero2_Buddy_Gold['TB_BaconShop_HERO_95_Buddy']='TB_BaconShop_HERO_95_Buddy_G'
class TB_BaconShop_HERO_95:# <12>[1453]
	""" Greybough  """
class TB_BaconShop_HP_107_Action(TargetedAction):
	TARGET=ActionArg()
	def do(delf, source, target):
		controller = source.controller
		if controller.game.this_is_tavern:
			return
		Buff(target, 'TB_BaconShop_HP_107e').trigger(source)
class TB_BaconShop_HP_107:
	""" Sprout It Out!
	[Passive] Give +1/+2 and [Taunt] to minions you summon during combat."""
	events = Summon(CONTROLLER, FRIENDLY + MINION).on(TB_BaconShop_HP_107_Action(Summon.CARD))
TB_BaconShop_HP_107e=buff(1,2,taunt=True)
######## BUDDY
class TB_BaconShop_HERO_95_Buddy:# <12>[1453]
	""" Wandering Treant
	Whenever you summon a [Taunt] minion, give it +2/+2. """
	events = Summon(CONTROLLER, FRIENDLY + TAUNT).on(Buff(Summon.CARD, 'TB_BaconShop_HERO_95_Buddy_e'))
	pass
TB_BaconShop_HERO_95_Buddy_e=buff(2,2)# <12>[1453]
class TB_BaconShop_HERO_95_Buddy_G:# <12>[1453]
	""" Wandering Treant
	Whenever you summon a [Taunt] minion, give it +4/+4. """
	events = Summon(CONTROLLER, FRIENDLY + TAUNT).on(Buff(Summon.CARD, 'TB_BaconShop_HERO_95_Buddy_G_e'))
	pass
TB_BaconShop_HERO_95_Buddy_G_e=buff(4,4)# <12>[1453]




##Guff Runetotem  ### HP OK ###
BG_Hero2+=['BG20_HERO_242','BG20_HERO_242p','BG20_HERO_242pe','BG20_HERO_242_Buddy','BG20_HERO_242_Buddy_G',]
BG_PoolSet_Hero2+=['BG20_HERO_242']
BG_Hero2_Buddy['BG20_HERO_242']='BG20_HERO_242_Buddy'
BG_Hero2_Buddy_Gold['BG20_HERO_242_Buddy']='BG20_HERO_242_Buddy_G'
class BG20_HERO_242:# <2>[1453]
	""" Guff Runetotem """
class BG20_HERO_242p:# <2>[1453]
	""" Natural Balance
	Give a friendly minion of each Tavern Tier +2/+2. """
	def activate(self):
		controller = self.controller
		field = copy(controller.field)
		random.shuffle(field)
		tiers=[]
		cards=[]
		for card in field:
			if tiers==[] or not card.tech_level in tiers:
				tiers.append(card.tech_level)
				cards.append(card)
		for card in cards:
			Buff(card, 'BG20_HERO_242pe').trigger(self)
		pass
	pass
#BG20_HERO_242pe=buff(1,1)# <12>[1453] ## until 23.4.3
#BG20_HERO_242pe=buff(2,3)### until 24.0
BG20_HERO_242pe=buff(2,2)### 24.0.3
""" Guff's Buff,	+1/+1. """
######## BUDDY
class BG20_HERO_242_Buddy_Action(GameAction):
	def do(self, source):
		controller=source.controller
		game = controller.game
		bartender = game.bartender
		Rerole(controller).broadcast(source, EventListener.ON, controller)
		for i in range(len(bartender.field)):
			card=bartender.field[0]
			game.parent.ReturnCard(card)
		if controller.hero.power.id=='TB_BaconShop_HP_065t2':### アランナフラグ
			bartender.len_bobs_field=7
		for tier in range(1,controller.tavern_tier+1):
			card = game.parent.DealCard(bartender, tier, only_tier=True)
			if controller.hero.power.id=='TB_BaconShop_HP_101':### サイラスフラグ
				if random.choice([0,1]):
					card.darkmoon_ticket = True
		game.free_rerole = 0
		game.reroleCost=1
		if controller.hero.power.id=='TB_BaconShop_HP_054':## Millhouse flag
			game.reroleCost=2
		Rerole(controller).broadcast(source, EventListener.AFTER, controller)

class BG20_HERO_242_Buddy:
	""" Baby Kodo
	&lt;b&gt;Battlecry: Refresh&lt;/b&gt; Bob's Tavern with a minion of each Tavern Tier. """
	play = BG20_HERO_242_Buddy_Action()
	pass
class BG20_HERO_242_Buddy_G:
	""" Baby Kodo
	&lt;b&gt;Battlecry: Refresh&lt;/b&gt; Bob's Tavern with a minion of each Tavern Tier. """
	play = BG20_HERO_242_Buddy_Action()
	pass




##Heistbaron Togwaggle ### new 24.2  ## visually OK ###
BG_Hero2 += ['BG23_HERO_305','BG23_HERO_305p','BG23_HERO_305_Buddy','BG23_HERO_305_Buddy_G']	 
BG_PoolSet_Hero2.append('BG23_HERO_305') 
BG_Hero2_Buddy['BG23_HERO_305']='BG23_HERO_305_Buddy'
BG_Hero2_Buddy_Gold['BG23_HERO_305_Buddy']='BG23_HERO_305_Buddy_G'
#81#Heistbaron Togwaggle ## 24.0
class BG23_HERO_305:
	""" Heistbaron Togwaggle """
class BG23_HERO_305p_Action1(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		source.cost = max(0, source.cost-1)## or use cost_mod
		pass
class BG23_HERO_305p_Action2(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = target
		for card in controller.opponent.field:
			card.zone=Zone.SETASIDE
			card.controller=controller
			card.zone=Zone.HAND
		controller.opponent.field=[]
		pass
class BG23_HERO_305p:
	""" The Perfect Crime
	Steal all minions in Bob's Tavern. Each turn, your next Hero Power costs (1) less."""
	## cost 9 -> 10 in 24.2.2
	events = EndTurn(CONTROLLER).on(BG23_HERO_305p_Action1(SELF))
	activate = BG23_HERO_305p_Action2(CONTROLLER)
###### BUDDY ######
class BG23_HERO_305_Buddy_Action(GameAction):
	def do(self, source):
		controller=source.controller
		game = controller.game
		gamemaster = game.parent
		bartender = game.bartender
		Rerole(controller).broadcast(source, EventListener.ON, controller)
		for i in range(len(bartender.field)):
			card=bartender.field[0]
			game.parent.ReturnCard(card)
		if controller.hero.power.id=='TB_BaconShop_HP_065t2':### アランナフラグ
			bartender.len_bobs_field=7
		for theBar in gamemaster.BG_Bars:
			theHero = theBar.controller.hero
			if theHero.id!=controller.hero:
				theCards = []
				for cd in theBar.controeller.field:
					if cd.type==CardType.MINION:
						if theCards==[] or theCards[0].tech_level<cd.tech_level:
							theCards = [cd]
						elif theCards[0].tech_level==cd.tech_level:
							theCards.append(cd)
				if len(theCards):
					card = random.choice(theCards)
					cardID = card.id
					newcard = controller.opponent.card(cardID)
					newcard.zone=Zone.PLAY
		game.free_rerole = 0
		game.reroleCost=1
		if controller.hero.power.id=='TB_BaconShop_HP_054':## Millhouse flag
			game.reroleCost=2
		Rerole(controller).broadcast(source, EventListener.AFTER, controller)
class BG23_HERO_305_Buddy:
	""" Waxadred, the Drippy
	&lt;b&gt;Battlecry: Refresh&lt;/b&gt; Bob's Tavern with the highest Tier minion from each opponent's warband."""
	play = BG23_HERO_305_Buddy_Action()
class BG23_HERO_305_Buddy_G:
	""" Waxadred, the Drippy
	&lt;b&gt;Battlecry: Refresh&lt;/b&gt; Bob's Tavern with the highest Tier minion from each opponent's warband."""
	play = BG23_HERO_305_Buddy_Action()





##Illidan Stormrage  ### HP, maybe OK ###
BG_Hero2+=['TB_BaconShop_HERO_08','TB_BaconShop_HP_069','TB_BaconShop_HP_069e','TB_BaconShop_HERO_08_Buddy','TB_BaconShop_HERO_08_Buddy_e','TB_BaconShop_HERO_08_Buddy_G',]
BG_PoolSet_Hero2+=['TB_BaconShop_HERO_08']
BG_Hero2_Buddy['TB_BaconShop_HERO_08']='TB_BaconShop_HERO_08_Buddy'
BG_Hero2_Buddy_Gold['TB_BaconShop_HERO_08_Buddy']='TB_BaconShop_HERO_08_Buddy_G'
class TB_BaconShop_HERO_08:# <12>[1453]
	""" Illidan Stormrage  """
class TB_BaconShop_HP_069_Action(GameAction):
	def do(self, source):
		controller=source.controller
		field = controller.field
		if len(field)>0 and len(controller.opponent.field):
			left = field[0]
			right = field[-1]
			Buff(left, 'TB_BaconShop_HP_069e').trigger(source)
			BG_Attack(left, random.choice(controller.opponent.field)).trigger(source)
			if right!=left and len(controller.opponent.field):
				Buff(left, 'TB_BaconShop_HP_069e').trigger(source)
				BG_Attack(right, random.choice(controller.opponent.field)).trigger(source)
class TB_BaconShop_HP_069:
	""" Wingmen
	[Passive.] [Start of Combat:] Your left and right-most minions gain +2 Attack __and attack immediately. """
	events = BeginBattle(CONTROLLER).on(TB_BaconShop_HP_069_Action())
	pass
TB_BaconShop_HP_069e=buff(2,0)
######## BUDDY
class TB_BaconShop_HERO_08_Buddy:# <12>[1453]
	""" Eclipsion Illidari
	Your first minion that attacks has "[Immune]while Attacking" for one attack only. """
	events =[
		BeginBattle(CONTROLLER).on(Buff(FRIENDLY_MINIONS, 'TB_BaconShop_HERO_08_Buddy_e')),
		BG_Attack(CONTROLLER).on(RemoveBuff(FRIENDLY_MINIONS, 'TB_BaconShop_HERO_08_Buddy_e'))
		]
	pass
TB_BaconShop_HERO_08_Buddy_e=buff(immune_while_attacking = True)# <12>[1453]
class TB_BaconShop_HERO_08_Buddy_G:# <12>[1453]
	""" Eclipsion Illidari
	Your first two minions thatattack have "[Immune]while Attacking" for oneattack only. """
	events =[
		BeginBattle(CONTROLLER).on(Buff(FRIENDLY_MINIONS, 'TB_BaconShop_HERO_08_Buddy_e')),
		BG_Attack(CONTROLLER).on(SidequestCounter(SELF, 2, [RemoveBuff(FRIENDLY_MINIONS, 'TB_BaconShop_HERO_08_Buddy_e')]))
		]	
	pass




##Infinite Toki  ### OK ### BUDDY MAYBE ###
BG_Hero2+=['TB_BaconShop_HERO_28','TB_BaconShop_HP_028','TB_BaconShop_HERO_28_Buddy','TB_BaconShop_HERO_28_Buddy_G',]
BG_PoolSet_Hero2+=['TB_BaconShop_HERO_28']
BG_Hero2_Buddy['TB_BaconShop_HERO_28']='TB_BaconShop_HERO_28_Buddy'
BG_Hero2_Buddy_Gold['TB_BaconShop_HERO_28_Buddy']='TB_BaconShop_HERO_28_Buddy_G'
class TB_BaconShop_HERO_28:# <12>[1453]
	""" Infinite Toki  """
class TB_BaconShop_HP_028_Action(GameAction):
	def do(self, source):
		controller = source.controller
		bartender = controller.opponent
		Rerole(controller).trigger(controller)
		tier=controller.tavern_tier+1## 
		if tier==7:
			tier=6
		cardID = random.choice(controller.game.parent.BG_decks[tier])
		card = bartender.card(cardID)
		card.controller = bartender
		card.zone = Zone.PLAY
		controller.game.parent.BG_decks[tier].remove(cardID)
		## 24.6
		cardID = random.choice(controller.game.parent.BG_decks[tier])
		card = bartender.card(cardID)
		card.controller = bartender
		card.zone = Zone.PLAY
		controller.game.parent.BG_decks[tier].remove(cardID)
class TB_BaconShop_HP_028:
	"""  Temporal Tavern
	[Refresh] Bob's Tavern. Include a minion from a higher Tavern Tier."""
	activate = TB_BaconShop_HP_028_Action()
	pass
######## BUDDY
class TB_BaconShop_HERO_28_Buddy:# <12>[1453]
	""" Clockwork Assistant
	[Battlecry:] [Discover] a minion from a higher Tavern Tier. """
	play = Discover(CONTROLLER, RandomBGAdmissible(tech_level=(TIER(CONTROLLER)+1)))
	pass
class TB_BaconShop_HERO_28_Buddy_G:# <12>[1453]
	"""
	[Battlecry:] [Discover] two minions from a higher Tavern Tier."""
	play = DiscoverTwice(CONTROLLER, RandomBGAdmissible(tech_level=(TIER(CONTROLLER)+1))*3)
	pass


##Ini Stormcoil BG22_HERO_200 ## once banned, renew 25.6
BG_Hero2+=["BG22_HERO_200","BG22_HERO_200p","BG22_HERO_200_Buddy","BG22_HERO_200_Buddy_e","BG22_HERO_200_Buddy_G","BG22_HERO_200_Buddy_Ge"]
BG_PoolSet_Hero2+=['BG22_HERO_200']
BG_Hero2_Buddy['BG22_HERO_200']='BG22_HERO_200_Buddy'
BG_Hero2_Buddy_Gold['BG22_HERO_200_Buddy']='BG22_HERO_200_Buddy_G'
class BG22_HERO_200:
	""" Ini Stormcoil
	"""
class BG22_HERO_200p:
	""" MechGyver
	[x][Passive] After 12 friendly minions die, get a random Mech.@[x][Passive] After 12 friendly minions die, get a random Mech. &lt;i&gt;({0} left.)&lt;/i&gt;"""
	events = Death(FRIENDLY + MINION).after(SidequestCounter(SELF, 12, [Give(CONTROLLER, RandomBGMecha())]))
###### BUDDY ######
class BG22_HERO_200_Buddy:
	""" Sub Scrubber
	After you play a Mech, gain +2/+2. """
	events = BG_Play(FRIENDLY + MINION + MECH).after(Buff(SELF, "BG22_HERO_200_Buddy_e"))
BG22_HERO_200_Buddy_e=buff(2,2)
class BG22_HERO_200_Buddy_G:
	""" Sub Scrubber
	After you play a Mech, gain +4/+4."""
	events = BG_Play(FRIENDLY + MINION + MECH).after(Buff(SELF, "BG22_HERO_200_Buddy_Ge"))
BG22_HERO_200_Buddy_Ge=buff(4,4)



##Jandice Barov #### OK ####
BG_Hero2+=['TB_BaconShop_HERO_71','TB_BaconShop_HP_084','TB_BaconShop_HERO_71_Buddy','TB_BaconShop_HERO_71_Buddy_e','TB_BaconShop_HERO_71_Buddy_G',]
BG_PoolSet_Hero2+=['TB_BaconShop_HERO_71']
BG_Hero2_Buddy['TB_BaconShop_HERO_71']='TB_BaconShop_HERO_71_Buddy'
BG_Hero2_Buddy_Gold['TB_BaconShop_HERO_71_Buddy']='TB_BaconShop_HERO_71_Buddy_G'
class TB_BaconShop_HERO_71:# <12>[1453]
	""" Jandice Barov """
class TB_BaconShop_HP_084:
	""" Swap, Lock, &amp; Shop It
	Swap a friendly non-golden minion with a random one in Bob's Tavern."""
	requirements = {
		PlayReq.REQ_TARGET_TO_PLAY:0,
		PlayReq.REQ_FRIENDLY_TARGET:0,
		PlayReq.REQ_MINION_TARGET:0,
		}
	def activate(self):
		controller = self.controller
		bartender = controller.opponent
		target = self.target ## minion
		if bartender.field==[]:
			return 
		card = random.choice(bartender.field)
		target.zone=Zone.GRAVEYARD
		card.zone=Zone.GRAVEYARD
		target.controller = bartender
		for buff in target.buffs:
			buff.zone=Zone.REMOVEDFROMGAME
		card.controller = controller
		target.zone=Zone.PLAY
		card.zone=Zone.PLAY
		amount=0
		for card in controller.field:
			if card.id=='TB_BaconShop_HERO_71_Buddy':
				amount += 1
			if card.id=='TB_BaconShop_HERO_71_Buddy_G':
				amount += 2
		amount *= controller.tavern_tier
		Buff(target, 'TB_BaconShop_HERO_71_Buddy_e', atk=amount, max_health=amount).trigger(self.source)
	pass
######## BUDDY
class TB_BaconShop_HERO_71_Buddy:# <12>[1453]
	""" Jandice's Apprentice
	After you swap minions, give them stats equal to your Tavern Tier. """
	pass
class TB_BaconShop_HERO_71_Buddy_e:# <10>[1453]
	""" Spinning	Increased Stats. """
class TB_BaconShop_HERO_71_Buddy_G:# <12>[1453]
	""" Jandice's Apprentice
	After you swap minions,give them stats equal to your Tavern Tier twice. """
	pass



##Kael'thas Sunstrider  ### OK  24.0.3### BUDDY MAYBE ###
BG_Hero2+=['TB_BaconShop_HERO_60','TB_BaconShop_HP_066','TB_BaconShop_HP_066e','TB_BaconShop_HERO_60_Buddy','TB_BaconShop_HERO_60_Buddy_e','TB_BaconShop_HERO_60_Buddy_G','TB_BaconShop_HERO_60_Buddy_G_e',]
BG_PoolSet_Hero2+=['TB_BaconShop_HERO_60']
BG_Hero2_Buddy['TB_BaconShop_HERO_60']='TB_BaconShop_HERO_60_Buddy'
BG_Hero2_Buddy_Gold['TB_BaconShop_HERO_60_Buddy']='TB_BaconShop_HERO_60_Buddy_G'
class TB_BaconShop_HERO_60:# <12>[1453]
	""" Kael'thas Sunstrider """
class TB_BaconShop_HP_066_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		Buff(target, 'TB_BaconShop_HP_066e' ).trigger(source)
		for card in source.controller.field:
			if card.id=="TB_BaconShop_HERO_60_Buddy":
				for cd in source.controller.field+source.controller.hand:
					Buff(cd, "TB_BaconShop_HERO_60_Buddy_e").trigger(source)
			if card.id=="TB_BaconShop_HERO_60_Buddy_G":
				for cd in source.controller.field+source.controller.hand:
					Buff(cd, "TB_BaconShop_HERO_60_Buddy_G_e").trigger(source)
class TB_BaconShop_HP_066:
	""" Verdant Spheres
	[Passive]Every third minion you play gains +2/+2.""" #24.0.3
	## [Passive] Every third minion you buy gains +2/+2. until 24.0
	events = BG_Play(CONTROLLER, MINION).on(SidequestCounter(SELF, 3, [TB_BaconShop_HP_066_Action(Buy.CARD)]))
TB_BaconShop_HP_066e=buff(2,2)
######## BUDDY
class TB_BaconShop_HERO_60_Buddy:# <12>[1453]
	""" Crimson Hand Centurion
	After 'Verdant Spheres' triggers, give your hand and board +1/+1. """
	pass
TB_BaconShop_HERO_60_Buddy_e=buff(1,1)# <12>[1453]
class TB_BaconShop_HERO_60_Buddy_G:# <12>[1453]
	""" Crimson Hand Centurion
	After 'Verdant Spheres' triggers, give your hand and board +2/+2. """
	pass
TB_BaconShop_HERO_60_Buddy_G_e=buff(2,2)# <12>[1453]




##King Mukla  #### half OK  ####
BG_Hero2+=['TB_BaconShop_HERO_38','TB_BaconShop_HP_038','DMF_065t','DMF_065e','TB_BaconShop_HERO_38_Buddy','TB_BaconShop_HERO_38_Buddy_e','TB_BaconShop_HERO_38_Buddy_G','TB_BaconShop_HERO_38_Buddy_Ge',]
BG_PoolSet_Hero2+=['TB_BaconShop_HERO_38']
BG_Hero2_Buddy['TB_BaconShop_HERO_38']='TB_BaconShop_HERO_38_Buddy'
BG_Hero2_Buddy_Gold['TB_BaconShop_HERO_38_Buddy']='TB_BaconShop_HERO_38_Buddy_G'
class TB_BaconShop_HERO_38:# <12>[1453]
	""" King Mukla  """
class TB_BaconShop_HP_038_Action(TargetedAction):
	TARGET=ActionArg()
	COIN=ActionArg()
	def do(self, source, target, coin):
		gamemaster = source.controller.game.parent
		for bar in gamemaster.BG_Bars:
			player = bar.controller
			if player != source.controller:
				player.gifts.append(coin)
		pass
class TB_BaconShop_HP_038:
	""" Bananarama
	Get 2 Bananas. At the end of your turn, _give everyone else one."""
	activate = Give(CONTROLLER, random.choice(['DMF_065t', 'BGS_Treasures_000'])), Give(CONTROLLER, random.choice(['DMF_065t', 'BGS_Treasures_000'])), TB_BaconShop_HP_038_Action(CONTROLLER, 'DMF_065t')
	pass
TB_BaconShop_HP_038e=buff(1,1)## no use
class DMF_065t:### alternative TB_BaconShop_HP_038t
	""" Wild Banana
	Give a friendly minion +1/+1. """
	requirements = { PlayReq.REQ_TARGET_TO_PLAY:0,  PlayReq.REQ_MINION_TARGET:0,  PlayReq.REQ_FRIENDLY_TARGET:0 }
	play = ApplyBanana(TARGET, 'DMF_065e')
DMF_065e=buff(1,1)## 
######## BUDDY
class TB_BaconShop_HERO_38_Buddy:# <12>[1453]
	""" Crazy Monkey
	After you feed a minion a Banana, give it +1/+1."""
	events = ApplyBanana(FRIENDLY + MINION).after(Buff(ApplyBanana.TARGET, 'TB_BaconShop_HERO_38_Buddy_e'))
	pass
TB_BaconShop_HERO_38_Buddy_e=buff(1,1)# <12>[1453] ・・ｽo・・ｽi・・ｽi・・ｽ・瑚ｲｻ・ｿ・ｽ
""" Banana Peel,	+1/+1. """
class TB_BaconShop_HERO_38_Buddy_G:# <12>[1453]
	""" Crazy Monkey
	After you feed a minion a Banana, give it +2/+2."""
	events = ApplyBanana(FRIENDLY + MINION).after(Buff(ApplyBanana.TARGET, 'TB_BaconShop_HERO_38_Buddy_Ge'))
	pass
TB_BaconShop_HERO_38_Buddy_Ge=buff(2,2)# <12>[1453]



##Kurtrus Ashfallen  #### HP OK #### 
BG_Hero2+=['BG20_HERO_280','BG20_HERO_280e','BG20_HERO_280p','BG20_HERO_280pe','BG20_HERO_280p2','BG20_HERO_280p2e','BG20_HERO_280p2e2','BG20_HERO_280p3','BG20_HERO_280p3e2','BG20_HERO_280_Buddy','BG20_HERO_280_Buddye','BG20_HERO_280_Buddy_G','BG20_HERO_280_Buddye2',]
BG_PoolSet_Hero2+=['BG20_HERO_280']
BG_Hero2_Buddy['BG20_HERO_280']='BG20_HERO_280_Buddy'
BG_Hero2_Buddy_Gold['BG20_HERO_280_Buddy']='BG20_HERO_280_Buddy_G'
class BG20_HERO_280:# <14>[1453]
	""" Kurtrus Ashfallen """
class BG20_HERO_280e:# <12>[1453]
	""" Kurtrus Watcher """
class BG20_HERO_280p_Action1(TargetedAction):
	TARGET=ActionArg()#Buy.CARD
	def do(self, source, target):
		controller=source.controller
		source.sidequest_list0.append(target)
		source.script_data_num_1 -= 1
		if source.script_data_num_1<=0:
			for card in source.sidequest_list0:
				if card in source.controller.field or card in source.controller.hand:
					Buff(card, 'BG20_HERO_280pe').trigger(source)
			source.sidequest_list0=[]
			source.script_data_num_1 = 4
			ChangeHeroPower(controller, 'BG20_HERO_280p2').trigger(source)
class BG20_HERO_280p_Action0(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		target.sidequest_list0=[]
		target.script_data_num_1=3
		pass
class BG20_HERO_280p:# <14>[1453]
	""" Final Showdown
	[Passive]Buy 3 minions in 1 turn to give them +2/+2 and_progress this. <i>(@ left!)</i> """
	events = [
		Buy(CONTROLLER).on(BG20_HERO_280p_Action1(Buy.CARD)),
		OWN_TURN_END.on(BG20_HERO_280p_Action0(SELF))
	]
	pass
BG20_HERO_280pe=buff(2,2)# <12>[1453]
""" Showdown Preparation+2/+2. """
class BG20_HERO_280p_Action2(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		source.sidequest_list0.append(target)
		source.script_data_num_1 -= 1
		if source.script_data_num_1<=0:
			for card in source.controller.field:
				Buff(card, 'BG20_HERO_280p2e').trigger(source)
			for card in source.controller.hand:
				Buff(card, 'BG20_HERO_280p2e').trigger(source)
			source.sidequest_list0=[]
			source.script_data_num_1 = 5
			ChangeHeroPower(CONTROLLER, 'BG20_HERO_280p3').trigger(source)
class BG20_HERO_280p_Action02(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		target.sidequest_list0=[]
		target.script_data_num_1=4
		pass
class BG20_HERO_280p2:# <14>[1453]
	""" Gain Momentum
	[Passive.] Buy 4 minions in1 turn to give your hand and board +2/+2 and_progress this. <i>(@ left!)</i> """
	events = [
		Buy(CONTROLLER).on(BG20_HERO_280p_Action2(Buy.CARD)),
		OWN_TURN_END.on(BG20_HERO_280p_Action02(SELF))
	]
	pass
BG20_HERO_280p2e=buff(2,2)# <12>[1453]
""" Momentum,	+2/+2. """
class BG20_HERO_280p2e2:# <12>[1453]
	""" Marked for Showdown,	Will be buffed by Final Showdown. """
class BG20_HERO_280p_Action3(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		source.sidequest_list0.append(target)
		source.script_data_num_1 -= 1
		if source.script_data_num_1<=0:
			for card in source.controller.field:
				Buff(card, 'BG20_HERO_280p3e2').trigger(source)
			for card in source.controller.hand:
				Buff(card, 'BG20_HERO_280p3e2').trigger(source)
			source.sidequest_list0=[]
			source.script_data_num_1 = 5
class BG20_HERO_280p_Action03(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		target.sidequest_list0=[]
		target.script_data_num_1=5
		pass
class BG20_HERO_280p3:# <14>[1453]
	""" Close the Portal
	[Passive.] Buy 5 minions in1 turn to give ALL yourminions this game +2/+2__and complete this. <i>({0} left!)</i>@[Passive.] Buy 5 minions in1 turn to give ALL yourminions this game +2/+2.<i>(Complete!)</i> """
	events = [
		Buy(CONTROLLER).on(BG20_HERO_280p_Action3(Buy.CARD)),
		OWN_TURN_END.on(BG20_HERO_280p_Action03(SELF))
	]
	pass
BG20_HERO_280p3e2=buff(2,2)# <12>[1453]
""" Portal Closure,	+2/+2 """
######## BUDDY
class BG20_HERO_280_Buddy_Action(GameAction):
	def do(self, source):
		Buff()
class BG20_HERO_280_Buddy:# <12>[1453]
	""" Living Nightmare
	After you buy a minion, minions in Bob's Tavern have +2/+1 this turn."""
	##After you buy a minion, minions in Bob's Tavern have +1/+1 this turn. 
	events = [
		Buy(CONTROLLER).after(Buff(ENEMY_MINIONS, 'BG20_HERO_280_Buddye')),
		OWN_TURN_END.on(RemoveBuff(ENEMY_MINIONS, 'BG20_HERO_280_Buddye'))
	]
	pass
BG20_HERO_280_Buddye=buff(2,1)# <12>[1453]
class BG20_HERO_280_Buddy_G:# <12>[1453]
	""" Living Nightmare
	After you buy a minion, minions in Bob's Tavern have +4/+2 this turn. """
	##After you buy a minion,minions in Bob's Tavernhave +2/+2 this turn.
	events = [
		Buy(CONTROLLER).after(Buff(ENEMY_MINIONS, 'BG20_HERO_280_Buddye2')),
		OWN_TURN_END.on(RemoveBuff(ENEMY_MINIONS, 'BG20_HERO_280_Buddye2'))
	]
	pass
BG20_HERO_280_Buddye2=buff(4,2)# <12>[1453]






###############################


