from ..utils import *

BG_Hero5=[
	'TB_BaconShop_HERO_94','TB_BaconShop_HP_106','TB_BaconShop_HERO_94_Buddy','TB_BaconShop_HERO_94_Buddy_G',#69#Tickatus
	'TB_BaconShop_HERO_10','TB_BaconShop_HP_008','TB_BaconShop_HP_008a','TB_BaconShop_HERO_10_Buddy','TB_BaconShop_HERO_10_Buddye','TB_BaconShop_HERO_10_Buddy_G',#70#Trade Prince Gallywix
	'BG22_HERO_003','BG22_HERO_003p','BG22_HERO_003pe','BG22_HERO_003pe2','BG22_HERO_003pe3','BG22_HERO_003_Buddy','BG22_HERO_003_Buddy_e','BG22_HERO_003_Buddy_G','BG22_HERO_003_Buddy_Ge',#71#Vanndar Stormpike
	'BG22_HERO_004','BG22_HERO_004p','BG22_HERO_004_Buddy','BG22_HERO_004_Buddy_e2','BG22_HERO_004_Buddy_G',#72#Varden Dawngrasp
	'BG20_HERO_201','BG20_HERO_201e','BG20_HERO_201e2','BG20_HERO_201e3','BG20_HERO_201p','BG20_HERO_201p2','BG20_HERO_201p2e','BG20_HERO_201p3e','BG20_HERO_201_Buddy','BG20_HERO_201_Buddy_e','BG20_HERO_201_Buddy_e2','BG20_HERO_201_Buddy_G',#73#Vol'jin
	'BG20_HERO_101','BG20_HERO_101p','BG20_HERO_101pe2','BG20_HERO_101_Buddy','BG20_HERO_101_Buddy_e','BG20_HERO_101_Buddy_G','BG20_HERO_101_Buddy_Ge',#74#Xyrella
	'TB_BaconShop_HERO_92','TB_BaconShop_HP_103','TB_BaconShop_HERO_92_Buddy','TB_BaconShop_HERO_92_Buddy_e','TB_BaconShop_HERO_92_Buddy_G','TB_BaconShop_HERO_92_Buddy_G_e',#75#Y'Shaarj
	'TB_BaconShop_HERO_35','TB_BaconShop_HP_039','TB_BaconShop_HP_039e','TB_BaconShop_HERO_35_Buddy','TB_BaconShop_HERO_35_Buddy_t1','TB_BaconShop_HERO_35_Buddy_t1e','TB_BaconShop_HERO_35_Buddy_t2','TB_BaconShop_HERO_35_Buddy_t3','TB_BaconShop_HERO_35_Buddy_t3e','TB_BaconShop_HERO_35_Buddy_t3f','TB_BaconShop_HERO_35_Buddy_t4','TB_BaconShop_HERO_35_Buddy_t5','TB_BaconShop_HERO_35_Buddy_t6','TB_BaconShop_HERO_35_Buddy_t6e','TB_BaconShop_HERO_35_Buddy_t6t','TB_BaconShop_HERO_35_Buddy_G',#76#Yogg-Saron, Hope's End
	'TB_BaconShop_HERO_53','TB_BaconShop_HP_062','TB_BaconShop_HERO_53_Buddy','TB_BaconShop_HERO_53_Buddy_e','TB_BaconShop_HERO_53_Buddy_G',#77#Ysera
	'TB_BaconShop_HERO_91','TB_BaconShop_HP_102','TB_BaconShop_HERO_91_Buddy','TB_BaconShop_HERO_91_Buddy_G',#78#Zephrys, the Great
	]


BG_PoolSet_Hero5=[
	'TB_BaconShop_HERO_94',
	'TB_BaconShop_HERO_10',
	'BG22_HERO_003',	
	'BG22_HERO_004',
	'BG20_HERO_201',
	'BG20_HERO_101',
	'TB_BaconShop_HERO_92',
	'TB_BaconShop_HERO_35',
	'TB_BaconShop_HERO_53',
	'TB_BaconShop_HERO_91',
	]
BG_Hero5_Buddy={
	'TB_BaconShop_HERO_94':'TB_BaconShop_HERO_94_Buddy',
	'TB_BaconShop_HERO_10':'TB_BaconShop_HERO_10_Buddy',
	'BG22_HERO_003':'BG22_HERO_003_Buddy',
	'BG22_HERO_004':'BG22_HERO_004_Buddy',
	'BG20_HERO_201':'BG20_HERO_201_Buddy',
	'BG20_HERO_101':'BG20_HERO_101_Buddy',
	'TB_BaconShop_HERO_92':'TB_BaconShop_HERO_92_Buddy',
	'TB_BaconShop_HERO_35':'TB_BaconShop_HERO_35_Buddy',
	'TB_BaconShop_HERO_53':'TB_BaconShop_HERO_53_Buddy',
	'TB_BaconShop_HERO_91':'TB_BaconShop_HERO_91_Buddy',
	}
BG_Hero5_Buddy_Gold={
	'TB_BaconShop_HERO_94_Buddy':'TB_BaconShop_HERO_94_Buddy_G',
	'TB_BaconShop_HERO_10_Buddy':'TB_BaconShop_HERO_10_Buddy_G',
	'BG22_HERO_003_Buddy':'BG22_HERO_003_Buddy_G',
	'BG22_HERO_004_Buddy':'BG22_HERO_004_Buddy_G',
	'BG20_HERO_201_Buddy':'BG20_HERO_201_Buddy_G',
	'BG20_HERO_101_Buddy':'BG20_HERO_101_Buddy_G',
	'TB_BaconShop_HERO_92_Buddy':'TB_BaconShop_HERO_92_Buddy_G',
	'TB_BaconShop_HERO_35_Buddy':'TB_BaconShop_HERO_35_Buddy_G',
	'TB_BaconShop_HERO_53_Buddy':'TB_BaconShop_HERO_53_Buddy_G',
	'TB_BaconShop_HERO_91_Buddy':'TB_BaconShop_HERO_91_Buddy_G',
	}

######## source #################################################################




#69#Tickatus   ### HP OK ###
class TB_BaconShop_HERO_94:# <12>[1453]
	""" Tickatus """
class TB_BaconShop_HP_106:
	""" Prize Wall 
	&lt;b&gt;Passive&lt;/b&gt; Every 4 turns, &lt;b&gt;Discover&lt;/b&gt; a Darkmoon Prize. &lt;i&gt;(@ |4(turn, turns) left!)&lt;/i&gt;"""
	entourage = [
	'BGS_Treasures_000','BGS_Treasures_001','BGS_Treasures_003',
	'BGS_Treasures_004','BGS_Treasures_006','BGS_Treasures_007',
	'BGS_Treasures_009','BGS_Treasures_010','BGS_Treasures_011',
	'BGS_Treasures_012','BGS_Treasures_013','BGS_Treasures_014','BGS_Treasures_015',
	'BGS_Treasures_016','BGS_Treasures_018','BGS_Treasures_019',
	'BGS_Treasures_020','BGS_Treasures_022','BGS_Treasures_023',
	'BGS_Treasures_025','BGS_Treasures_026',
	'BGS_Treasures_028','BGS_Treasures_029','BGS_Treasures_030',
	'BGS_Treasures_032','BGS_Treasures_033','BGS_Treasures_034',
	'BGS_Treasures_036','BGS_Treasures_037',
	]
	events = BeginBar(CONTROLLER).on(SidequestCounter(SELF, 4, [Discover(CONTROLLER, RandomEntourage())]))
	pass
## darkmoon prize -> BGS_Treasures_000 ~ BGS_Treasures_037
class TB_BaconShop_HERO_94_Buddy:# <12>[1453]
	""" Ticket Collector
	[Battlecry:] [Discover] aDarkmoon Prize fromthe next Prize turn. """
	#
	pass
class TB_BaconShop_HERO_94_Buddy_G:# <12>[1453]
	""" Ticket Collector
	[Battlecry:] [Discover] 2Darkmoon Prizes fromthe next Prize turn. """
	#
	pass





#70#Trade Prince Gallywix  ### HP OK ###
class TB_BaconShop_HERO_10:# <12>[1453]
	""" Trade Prince Gallywix """
class TB_BaconShop_HP_008:
	""" 
	&lt;b&gt;Passive&lt;/b&gt; After you sell a minion, get 1 extra Gold next turn. &lt;i&gt;(Can exceed 10.)&lt;/i&gt;"""
	### proceed in BG_main
	pass
class TB_BaconShop_HP_008a:
	""" """
class TB_BaconShop_HERO_10_Buddy:# <12>[1453]
	""" Bilgewater Mogul
	[Battlecry:] Give a minion +1/+1 for each Gold spent this turn. """
	#
	pass
class TB_BaconShop_HERO_10_Buddye:# <12>[1453]
	""" Brutal Luxury
	Increased stats. """
	#
	pass
class TB_BaconShop_HERO_10_Buddy_G:# <12>[1453]
	""" Bilgewater Mogul
	[Battlecry:] Give a minion +2/+2 for each Gold spent this turn. """
	#
	pass




#71#Vanndar Stormpike   ## HP OK ##
class BG22_HERO_003:# <12>[1453]
	""" Vanndar Stormpike """
class BG22_HERO_003p:# <12>[1453]
	""" Lead the Stormpikes
	Choose a friendly minion.It copies the Health of your highest Health minion for next combat only. """
	requirements = { PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0, 1001:2 }
	activate = Buff(TARGET,'BG22_HERO_003pe3' )
	pass
class BG22_HERO_003pe:# <12>[1453]
	""" Stormpike Strength
	Copied highest Health. """
	events = EndBattle(CONTROLLER).on(Destroy(SELF))
	pass
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
		Buff(target, 'BG22_HERO_003pe').trigger(source)
		buff = target.buffs[-1]
		buff.max_health = highest_health - target.max_health
class BG22_HERO_003pe3:# <12>[1453]
	""" Modified Health Next Combat Only
	Health is increased or decreased for next combat only. """
	events = [
		EndTurn(CONTROLLER).on(BG22_HERO_003p_Action(OWNER)),
		EndBattle(CONTROLLER).on(Destroy(SELF))
		]
	pass
class BG22_HERO_003_Buddy:# <12>[1453]
	""" Stormpike Lieutenant
	[Avenge (2):] Give your minions +1 Health permanently. """
	#
	pass
class BG22_HERO_003_Buddy_e:# <12>[1453]
	""" Lieutenant's Leadership
	+1 Health. """
	#
	pass
class BG22_HERO_003_Buddy_G:# <12>[1453]
	""" Stormpike Lieutenant
	[Avenge (2):] Give your minions +2 Health permanently. """
	#
	pass
class BG22_HERO_003_Buddy_Ge:# <12>[1453]
	""" Lieutenant's Leadership
	+2 Health. """
	#
	pass


#72#Varden Dawngrasp ## HP OK ##
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
class BG22_HERO_004p:# <12>[1453]
	""" Twice as Nice
	[Passive.] After Bob's Tavern is [Refreshed],copy and [Freeze] one of his minions. """
	events = Rerole(CONTROLLER).after(BG22_HERO_004p_Action(HIGHEST_TIER(ENEMY_MINIONS)))
	pass
class BG22_HERO_004_Buddy:# <12>[1453]
	""" Varden's Aquarrior
	'Twice as Nice' also gives the copy stats equal to your Tavern Tier. """
	#
	pass
class BG22_HERO_004_Buddy_e2:# <12>[1453]
	""" Frosted
	Increased stats. """
	#
	pass
class BG22_HERO_004_Buddy_G:# <12>[1453]
	""" Varden's Aquarrior
	'Twice as Nice' also givesthe copy stats equal toyour Tavern Tier twice. """
	#
	pass





#73#Vol'jin   ### HP OK ###
class ChooseTwice(Choice):
	card1=None
	card2=None
	def choose(self, card):
		self.source._sidequest_counter_ += 1
		if self.source._sidequest_counter_>=2:
			self.next_choice=None
		else:
			self.next_choice=self
		super().choose(card)
		if self.source._sidequest_counter_==1:
			self.card1=card
			#self.cards = self._args[1]
			self.cards = self.source.controller.field
		else:
			self.card2=card
			buff1 = self.source.controller.card('BG20_HERO_201e')
			buff2 = self.source.controller.card('BG20_HERO_201e2')
			buff1.tags[GameTag.ATK]=self.card2.atk-self.card1.atk
			buff1.tags[GameTag.HEALTH]=self.card2.max_health-self.card1.max_health
			buff2.tags[GameTag.ATK]=self.card1.atk-self.card2.atk
			buff2.tags[GameTag.HEALTH]=self.card1.max_health-self.card2.max_health
			buff1.apply(self.card1)
			buff2.apply(self.card2)
			if Config.LOGINFO:
				print("(ChooseTwice.choose)Swaping stats between %s and %s"%(self.card1, self.card2))
class BG20_HERO_201:# <12>[1453]
	""" Vol'jin  """
class BG20_HERO_201e:# <12>[1453]
	""" Modified Attack,	Attack is increased or decreased. """
	pass
class BG20_HERO_201e2:# <12>[1453]
	""" Modified Health,	Health is increased or decreased. """
	pass
class BG20_HERO_201e3:# <12>[1453]
	""" Stats Set	 """
	pass
class BG20_HERO_201p:# <12>[1453]
	""" Spirit Swap
	Choose two minions. Swap their stats. """
	requirements = {1001:2}
	activate = ChooseTwice(CONTROLLER, FRIENDLY_MINIONS)
	pass
class BG20_HERO_201p2:# <12>[1453]
	""" Spirit Swap
	Choose a minion. Swap its stats with {0}. """
	#
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
class BG20_HERO_201_Buddy:# <12>[1453]
	""" Master Gadrin
	At the end of your turn,the minion to the leftof this copies this minion's Attack. """
	#
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
class BG20_HERO_201_Buddy_G:# <12>[1453]
	""" Master Gadrin
	At the end of your turn,adjacent minions copythis minion's Attack. """
	#
	pass



#74#Xyrella  ### HP OK ###
class BG20_HERO_101:# <12>[1453]
	""" Xyrella """
class BG20_HERO_101p_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = source.controller
		controller.opponent.field.remove(target)
		target.controller=controller
		target.zone=Zone.HAND
		target.frozen=False
		buff=controller.card('BG20_HERO_101pe2')
		buff.apply(target)
class BG20_HERO_101p:
	""" See the Light
	Choose a minion in Bob's Tavern to add to your hand. Set its stats to 2."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_ENEMY_TARGET:0,PlayReq.REQ_MINION_TARGET:0,}
	activate = BG20_HERO_101p_Action(TARGET)
class BG20_HERO_101pe2:
	max_health = SET(2)
	atk = SET(2)
class BG20_HERO_101_Buddy_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self,source,target,buff):
		if isinstance(target,PlayableCard):
			if target.health==target.atk:
				Buff(source,buff).trigger(source)
class BG20_HERO_101_Buddy:#
	""" Baby Elekk
	After you play a minion with Attack equal to its Health, gain +2/+2. """
	events = BG_Play(CONTROLLER, FRIENDLY + MINION).on(BG20_HERO_101_Buddy_Action(Play.CARD, 'BG20_HERO_101_Buddy_e'))
	pass
BG20_HERO_101_Buddy_e=buff(2,2)
class BG20_HERO_101_Buddy_G:
	""" 
	After you play a minion with Attack equal to its Health, gain +4/+4.""" 
	events = BG_Play(CONTROLLER, FRIENDLY + MINION).on(BG20_HERO_101_Buddy_Action(Play.CARD, 'BG20_HERO_101_Buddy_Ge'))
	pass
BG20_HERO_101_Buddy_Ge=buff(4,4)



#75#Y'Shaarj
class TB_BaconShop_HERO_92:# <12>[1453]
	""" Y'Shaarj """
class TB_BaconShop_HP_103:
	"""  Embrace Your Rage
	&lt;b&gt;Start of Combat:&lt;/b&gt; Summon a minion from your Tavern Tier. Add a copy to your hand."""
	pass
class TB_BaconShop_HERO_92_Buddy:# <12>[1453]
	""" Baby Y'Shaarj
	Whenever you summon a minion of your current Tavern Tier, give it +4/+4. """
	#
	pass
class TB_BaconShop_HERO_92_Buddy_e:# <12>[1453]
	""" Rage Unbound
	+4/+4. """
	#
	pass
class TB_BaconShop_HERO_92_Buddy_G:# <12>[1453]
	""" Baby Y'Shaarj
	Whenever you summon a minion of your current Tavern Tier, give it +8/+8. """
	#
	pass
class TB_BaconShop_HERO_92_Buddy_G_e:# <12>[1453]
	""" Rage Unbound
	+8/+8. """
	#
	pass





#76#Yogg-Saron, Hope's End # armor 0
class TB_BaconShop_HERO_35:# <12>[1453]
	""" Yogg-Saron, Hope's End """
class TB_BaconShop_HP_039:
	""" """
	pass
TB_BaconShop_HP_039e=buff(1,1)
class TB_BaconShop_HERO_35_Buddy:
	""" """
	pass
class TB_BaconShop_HERO_35_Buddy_t1:# <12>[1453]
	""" Mysterybox
	For the rest of the game,your Hero Power triggersan extra time when used. """
	#
	pass
class TB_BaconShop_HERO_35_Buddy_t1e:# <12>[1453]
	""" Mysterybox
	Your Hero Power triggers an extra time. """
	#
	pass
class TB_BaconShop_HERO_35_Buddy_t2:# <12>[1453]
	""" Hand of Fate
	Add 3 random Darkmoon Prizes to your hand. """
	#
	pass
class TB_BaconShop_HERO_35_Buddy_t3:# <12>[1453]
	""" Curse of Flesh
	Give your minions +3/+3, then randomly shuffle their stats. """
	#
	pass
class TB_BaconShop_HERO_35_Buddy_t3e:# <12>[1453]
	""" Fleshy
	+3/+3 """
	#
	pass
class TB_BaconShop_HERO_35_Buddy_t3f:# <12>[1453]
	""" Curse of Fleshed
	Stats shuffled with other minions. """
	#
	pass
class TB_BaconShop_HERO_35_Buddy_t4:# <12>[1453]
	""" Mindflayer Goggles
	Steal all minions in Bob's Tavern, then [Refresh] it. """
	#
	pass
class TB_BaconShop_HERO_35_Buddy_t5:# <12>[1453]
	""" Devouring Hunger
	Consume Bob's Tavern and give thestats to your minions.Then [Refresh] it. """
	#
	pass
class TB_BaconShop_HERO_35_Buddy_t6:# <12>[1453]
	""" Rod of Roasting
	Cast 'Pyrobuff' randomly to give minions +4/+4 until one hits your bartender or hero. """
	#
	pass
class TB_BaconShop_HERO_35_Buddy_t6e:# <12>[1453]
	""" Pyrobuffed
	+4/+4 """
	#
	pass
class TB_BaconShop_HERO_35_Buddy_t6t:# <12>[1453]
	""" Pyrobuff
	Give a minion +4/+4. """
	#
	pass
class TB_BaconShop_HERO_35_Buddy_G:
	""" """
	pass






#77#Ysera
class TB_BaconShop_HERO_53:# <12>[1453]
	""" Ysera """
class TB_BaconShop_HP_062:
	"""  """
	pass
class TB_BaconShop_HERO_53_Buddy:
	""" """
	pass
class TB_BaconShop_HERO_53_Buddy_e:# <12>[1453]
	""" Pleasant Dream
	Stats increased by Valithria. """
	#
	pass
class TB_BaconShop_HERO_53_Buddy_G:
	""" """
	pass




#78#Zephrys, the Great
class TB_BaconShop_HERO_91:# <12>[1453]
	""" Zephrys, the Great """
class TB_BaconShop_HP_102:
	"""  """
	pass
class TB_BaconShop_HERO_91_Buddy:
	"""  """
	pass
class TB_BaconShop_HERO_91_Buddy_G:
	"""  """
	pass


#79#



####################################################################################

