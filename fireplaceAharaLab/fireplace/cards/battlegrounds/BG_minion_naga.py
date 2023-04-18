from fireplace.card import THE_COIN
from ..utils import *


BG_Mini_Myrmidon=True##(1)
BG_Shell_Collector=True##(1)

BG_Snail_Cavalry=True##(2)
BG_Deep_Sea_Angler=True## (2)
BG_Lava_Lurker=True## (2)

BG_Stormscale_Siren=False## (3) BANNED!
BG_Pashmar_the_Vengeful=True## (3)
BG_Warden_of_Old=True## (3)
BG_Shoal_Commander=True## (3)

BG_Eelbound_Archer=True## (4)
BG_Waverider=True## (4)
BG_Eventide_Brute=True## (4)
#BG_Pufferquil=True(4/2/6): quilboar

BG_Critter_Wrangler=True##(5)
BG_Glowscale=True## (5)
BG_Corrupted_Myrmidon=True## (5)

BG_Tidemistress_Athissa=True## (6)
BG25__Greta_Gold_Gun=True# 6/2/9 naga/pirate ## new 25.2.2

BG_Minion_Naga=[]

BG_PoolSet_Naga=[[],[],[],[],[],[],[]]

BG_Naga_Gold={}


## Mini-Myrmidon(1)  ## OK ##
if BG_Mini_Myrmidon:
	BG_Minion_Naga+=['BG23_000','BG23_000e','BG23_000t','BG23_000_G','BG23_000_Ge','BG23_000_Gt', ]#
	BG_PoolSet_Naga[1].append('BG23_000')
	BG_Naga_Gold['BG23_000']='BG23_000_G'
class BG23_000:# <12>[1453]
	""" Mini-Myrmidon(1)
	[Spellcraft:] Give a minion +2 Attack until next turn. """
	play = Spellcraft(CONTROLLER,'BG23_000t')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG23_000t'))
	tags={2359:'BG23_000t'}
	pass
class BG23_000t:
	""" Mini-Trident
	Give a minion +2_Attack until next turn."""
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0}
	play = SpellcraftSpell(TARGET, 'BG23_000e')
	tags = {GameTag.TECH_LEVEL:1}
	class Hand:
		events = EndTurn(CONTROLLER).on(Destroy(SELF))
class BG23_000e:
	tags={GameTag.ATK:2, }
	events = BeginBar(CONTROLLER).on(Destroy_spellcraft(SELF))
class BG23_000_G:# <12>[1453]
	""" Mini-Myrmidon
	[Spellcraft:] Give a minion +4 Attack until next turn. """
	play = Spellcraft(CONTROLLER,'BG23_000_Gt')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG23_000_Gt'))
	tags={2359:'BG23_000_Gt'}
	pass
class BG23_000_Ge:
	tags={GameTag.ATK:4,}
	events = BeginBar(CONTROLLER).on(Destroy_spellcraft(SELF))
class BG23_000_Gt:
	""" """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0}
	play = SpellcraftSpell(TARGET, 'BG23_000_Ge')
	class Hand:
		events = EndTurn(CONTROLLER).on(Destroy(SELF))




## Shell Collector(1) ## OK ##
if BG_Shell_Collector:
	BG_Minion_Naga+=['BG23_002','BG23_002_G', ]#
	BG_PoolSet_Naga[1].append('BG23_002')
	BG_Naga_Gold['BG23_002']='BG23_002_G'
class BG23_002:# <12>[1453]
	""" Shell Collector(1)
	[Battlecry:] Add a Gold Coin to your hand. """
	play = Give(CONTROLLER, THE_COIN)
	pass
class BG23_002_G:# <12>[1453]
	""" Shell Collector
	[Battlecry:] Add 2 Gold Coinsto your hand. """
	play = Give(CONTROLLER, THE_COIN)*2
	pass




## Snail Cavalry(2)   ## OK ##
if BG_Snail_Cavalry:
	BG_Minion_Naga+=['BG23_001','BG23_001e','BG23_001_G','BG23_001_Ge', ]#
	BG_PoolSet_Naga[2].append('BG23_001')
	BG_Naga_Gold['BG23_001']='BG23_001_G'
class BG23_001_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self,source,target, buff):
		controller = source.controller
		if controller.once_per_turn==0:
			Buff(target, buff).trigger(source)
			controller.once_per_turn=1
class BG23_001:# <12>[1453]
	""" Snail Cavalry(2)
	[Once per Turn:]After you cast a spell,gain +2_Health. """
	events = BG_Play(CONTROLLER, SPELL).on(BG23_001_Action(SELF, 'BG23_001e'))
	pass
BG23_001e=buff(0,2)
class BG23_001_G:# <12>[1453]
	""" Snail Cavalry
	[Once per Turn:]After you cast a spell,gain +4_Health. """
	events = BG_Play(CONTROLLER, SPELL).on(BG23_001_Action(SELF, 'BG23_001_Ge'))
	pass
BG23_001_Ge=buff(0,4)



## Deep-Sea Angler (2) ### OK ###
if BG_Deep_Sea_Angler:
	BG_Minion_Naga+=['BG23_004','BG23_004e','BG23_004t','BG23_004_G','BG23_004_Ge','BG23_004_Gt', ]#
	BG_PoolSet_Naga[2].append('BG23_004')
	BG_Naga_Gold['BG23_004']='BG23_004_G'
class BG23_004:# <12>[1453]
	""" Deep-Sea Angler (2)
	[Spellcraft:] Give a minion+3 Health and [Taunt]until next turn. """
	play=Spellcraft(CONTROLLER,'BG23_004t')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG23_004t'))
	tags={2359:'BG23_004t'}
	pass
class BG23_004e:
	tags={GameTag.HEALTH:3, GameTag.TAUNT:True}
	events = BeginBar(CONTROLLER).on(Destroy_spellcraft(SELF))	
	pass
class BG23_004t:
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0}
	play = SpellcraftSpell(TARGET, 'BG23_004e'), 
	tags = {GameTag.TECH_LEVEL:2}
	class Hand:
		events = EndTurn(CONTROLLER).on(Destroy(SELF))
	pass
class BG23_004_G:# <12>[1453]
	""" Deep-Sea Angler
	[Spellcraft:] Give a minion+6 Health and [Taunt]until next turn. """
	play=Spellcraft(CONTROLLER,'BG23_004_Gt')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG23_004_Gt'))
	tags={2359:'BG23_004_Gt'}
	pass
class BG23_004_Ge:
	tags={GameTag.HEALTH:6, GameTag.TAUNT:True}
	events = BeginBar(CONTROLLER).on(Destroy_spellcraft(SELF))	
	pass
class BG23_004_Gt:
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0}
	play = SpellcraftSpell(TARGET, 'BG23_004_Ge')	
	class Hand:
		events = EndTurn(CONTROLLER).on(Destroy(SELF))	
	pass


## Lava Lurker (2)  ### OK ###
if BG_Lava_Lurker:#(2/2/5)
	BG_Minion_Naga+=['BG23_009','BG23_009_G', ]#
	BG_PoolSet_Naga[2].append('BG23_009')
	BG_Naga_Gold['BG23_009']='BG23_009_G'
class BG23_009_Action(TargetedAction):
	BUFF=ActionArg()
	AMOUNT=IntArg()
	def do(self, source, buff, amount):
		if hasattr(buff.source,'spellcraft_spellcard') or  buff.data.tags.get(2594)==1:
			if source.script_data_num_1<amount:
				buff.permanent_buff = True
				source.script_data_num_1+=1
class BG23_009_Action2(GameAction):
	def do(self, source):
		source.script_data_num_1=0
class BG23_009:# <12>[1453]
	""" Lava Lurker (2)
	The first [Spellcraft] spellcast on this each turn is permanent. """
	## Only in this case, Buff.on activates for spellcraft spellcasts. 
	events = [
		SpellcraftSpell(SELF).on(BG23_009_Action(SpellcraftSpell.SPELLCARD, 1)),
		BeginBar(CONTROLLER).on(BG23_009_Action2())
	]
	pass
class BG23_009_G:# <12>[1453]
	""" Lava Lurker
	The first 2 [Spellcraft] spellscast on this each turnare permanent. """
	events = [
		SpellcraftSpell(SELF).on(BG23_009_Action(SpellcraftSpell.SPELLCARD, 2)),
		BeginBar(CONTROLLER).on(BG23_009_Action2())
	]
	pass



## Stormscale Siren (3)  ### OK ### ### BANNED ###
if BG_Stormscale_Siren:
	BG_Minion_Naga+=['BG23_005','BG23_005_G', ]#
	BG_PoolSet_Naga[3].append('BG23_005')
	BG_Naga_Gold['BG23_005']='BG23_005_G'
class BG23_005_Action(TargetedAction): ## 
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		controller =source.controller
		for card in target.field:
			if hasattr(card, "spellcraft") and card.spellcraft:
				spellcraft_spellid = card.id+'t'## cheet to get spell card id
				for repeat in range(amount):
					spellcard = controller.card(spellcraft_spellid)
					BG_Play(spellcard, card, None, None).trigger(controller)
class BG23_005:# <12>[1453]
	""" Stormscale Siren (3)
	At the end of your turn,your [Spellcraft] minions cast their spells on themselves. """
	events = OWN_TURN_END.on(BG23_005_Action(CONTROLLER, 1))
	pass
class BG23_005_G:# <12>[1453]
	""" Stormscale Siren
	At the end of your turn,your [Spellcraft] minionscast their spells_on themselves twice. """
	events = OWN_TURN_END.on(BG23_005_Action(CONTROLLER, 2))
	pass



## Pashmar the Vengeful (3) ### OK ###
if BG_Pashmar_the_Vengeful:
	BG_Minion_Naga+=['BG23_014','BG23_014_G', ]#
	BG_PoolSet_Naga[3].append('BG23_014')
	BG_Naga_Gold['BG23_014']='BG23_014_G'
class BG23_014_Action(GameAction):
	"""
	Give player targets card \a id. (battleground)
	"""
	def do(self, source):
		#CONTROLLER, RandomBGSpellcraft(tech_level_less=TIER(CONTROLLER))
		original = source.controller.deepcopy_original#controller
		if original:
			cards=RandomBGSpellcraft(tech_level_less=source.controller.tavern_tier).evaluate(source.controller)
			if not hasattr(cards, "__iter__"):
				cards = [cards]			
			for card in cards:
				if isinstance(card.spellcraft, str):
					Give(original, card.spellcraft).trigger(source)
				else:
					pass
		pass
class BG23_014:# <12>[1453]
	""" Pashmar the Vengeful (3)
	[Avenge (3):] Get a [Spellcraft] spell of your Tier or lower. """
	events = Death(FRIENDLY+MINION).on(Avenge(SELF, 3, [BG23_014_Action()]))
	pass
class BG23_014_G_Action(GameAction):
	"""
	Give player targets card \a id. (battleground)
	"""
	def do(self, source):
		#CONTROLLER, RandomBGSpellcraft(tech_level_less=TIER(CONTROLLER))
		original = source.controller.deepcopy_original#controller
		if original:
			cards=RandomBGSpellcraft(tech_level_less=source.controller.tavern_tier).evaluate(source.controller)
			if not hasattr(cards, "__iter__"):
				cards = [cards]			
			for card in cards:
				Give(original, card.spellcraft).trigger(source)
			cards=RandomBGSpellcraft(tech_level_less=source.controller.tavern_tier).evaluate(source.controller)
			if not hasattr(cards, "__iter__"):
				cards = [cards]			
			for card in cards:
				Give(original, card.spellcraft).trigger(source)
		pass
class BG23_014_G:# <12>[1453]
	""" Pashmar the Vengeful
	[Avenge (3):] Get 2[Spellcraft] spells of your Tier or lower. """
	events = Death(FRIENDLY+MINION).on(Avenge(SELF, 3, [BG23_014_G_Action()]*2))
	pass




## Warden of Old (3) ### OK ###
if BG_Warden_of_Old:
	BG_Minion_Naga+=['BGS_200','TB_BaconUps_256', ]#
	BG_PoolSet_Naga[3].append('BGS_200')
	BG_Naga_Gold['BGS_200']='TB_BaconUps_256'
class BGS_200_Action(TargetedAction):
	"""
	Give player targets card \a id. (battleground)
	"""
	TARGET = ActionArg()
	CARD = CardArg()
	def do(self, source, target, cards):
		original = target.deepcopy_original
		if original:
			if not hasattr(cards, "__iter__"):
				cards = [cards]			
			for card in cards:
				Give(original, card).trigger(source)
		pass
class BGS_200:# <12>[1453]
	""" Warden of Old (3)
	[Deathrattle:] Add a Gold Coin to your hand. """
	deathrattle = BGS_200_Action(CONTROLLER, THE_COIN)
	pass
class TB_BaconUps_256:# <12>[1453]
	""" Warden of Old
	[Deathrattle:] Add 2 Gold Coins to your hand. """
	deathrattle = BGS_200_Action(CONTROLLER, THE_COIN)*2
	pass



### Shoal Commander (3)
if BG_Shoal_Commander:
	BG_Minion_Naga+=['BG23_011','BG23_011e','BG23_011t','BG23_011_G','BG23_011_Ge','BG23_011_Gt', ]#
	BG_PoolSet_Naga[3].append('BG23_011')
	BG_Naga_Gold['BG23_011']='BG23_011_G'
class BG23_011:# <12>[1453]  ### OK ###
	""" Shoal Commander (3)
	[Spellcraft:] Give a minion +1/+1 for each friendly Naga until next turn. """
	play=Spellcraft(CONTROLLER,'BG23_011t')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG23_011t'))
	tags={2359:'BG23_011t'}
	pass
class BG23_011e:
	tags={GameTag.ATK:1, GameTag.HEALTH:1}
	events = BeginBar(CONTROLLER).on(Destroy_spellcraft(SELF))
	pass
class BG23_011t:
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0}
	play = SpellcraftSpell(TARGET, 'BG23_011e') * Count(FRIENDLY_MINIONS + NAGA)		
	tags = {GameTag.TECH_LEVEL:3}
	class Hand:
		events = EndTurn(CONTROLLER).on(Destroy(SELF))	
	pass
class BG23_011_G:# <12>[1453]
	""" Shoal Commander
	[Spellcraft:] Give a minion+2/+2 for each friendlyNaga until next turn. """
	play=Spellcraft(CONTROLLER,'BG23_011_Gt')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG23_011_Gt'))
	tags={2359:'BG23_011_Gt'}
	pass
class BG23_011_Ge:
	tags={GameTag.ATK:2, GameTag.HEALTH:2}
	events = BeginBar(CONTROLLER).on(Destroy_spellcraft(SELF))
	pass
class BG23_011_Gt:
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0}
	play = SpellcraftSpell(TARGET, 'BG23_011_Ge') * Count(FRIENDLY_MINIONS + NAGA)	
	class Hand:
		events = EndTurn(CONTROLLER).on(Destroy(SELF))	
	pass




#Eelbound Archer (4) ### OK ###
if BG_Eelbound_Archer:
	BG_Minion_Naga+=['BG23_006','BG23_006e','BG23_006t','BG23_006_G','BG23_006_Ge','BG23_006_Gt', ]#
	BG_PoolSet_Naga[4].append('BG23_006')
	BG_Naga_Gold['BG23_006']='BG23_006_G'
class BG23_006:# <12>[1453]
	""" Eelbound Archer (4)
	[Spellcraft:] Give a minion +8_Attack until next turn. """
	play=Spellcraft(CONTROLLER,'BG23_006t')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG23_006t'))
	tags={2359:'BG23_006t'}
	pass
class BG23_006e:
	tags = {GameTag.ATK:8}
	events = BeginBar(CONTROLLER).on(Destroy_spellcraft(SELF))	
	pass
class BG23_006t:
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0}
	play = SpellcraftSpell(TARGET, 'BG23_006e')	
	tags = {GameTag.TECH_LEVEL:4}
	class Hand:
		events = EndTurn(CONTROLLER).on(Destroy(SELF))
	pass
class BG23_006_G:# <12>[1453]
	""" Eelbound Archer
	[Spellcraft:] Give a minion+16_Attack until next turn. """
	play=Spellcraft(CONTROLLER,'BG23_006_Gt')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG23_006_Gt'))
	tags={2359:'BG23_006_Gt'}
	pass
class BG23_006_Ge:
	tags = {GameTag.ATK:16}
	events = BeginBar(CONTROLLER).on(Destroy_spellcraft(SELF))	
	pass
class BG23_006_Gt:
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0}
	play = SpellcraftSpell(TARGET, 'BG23_006_Ge')	
	class Hand:
		events = EndTurn(CONTROLLER).on(Destroy(SELF))
	pass



## Waverider (4) ### OK ### too hard to manage windfury buff
if BG_Waverider:
	BG_Minion_Naga+=['BG23_007','BG23_007e','BG23_007t','BG23_007_G','BG23_007_Ge','BG23_007_Gt', ]#
	BG_PoolSet_Naga[4].append('BG23_007')
	BG_Naga_Gold['BG23_007']='BG23_007_G'
class BG23_007:# <12>[1453]
	""" Waverider (4)
	[Spellcraft:] Give a minion+2/+2 and [Windfury] until next turn. """
	play=Spellcraft(CONTROLLER,'BG23_007t')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG23_007t'))
	tags={2359:'BG23_007t'}
	pass
class BG23_007e:
	def apply(self, target):
		target.windfury=1
	tags={GameTag.ATK:2, GameTag.HEALTH:2, } ## 23.4.3
	events = BeginBar(CONTROLLER).on(SetAttr(OWNER,'windfury',0), Destroy_spellcraft(SELF))	
	pass
class BG23_007t:
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0}
	play = SpellcraftSpell(TARGET, 'BG23_007e')	
	tags = {GameTag.TECH_LEVEL:4}
	class Hand:
		events = EndTurn(CONTROLLER).on(Destroy(SELF))
	pass
class BG23_007_G:# <12>[1453]
	""" Waverider
	[Spellcraft:] Give a minion+4/+4 and [Windfury]until next turn. """
	play=Spellcraft(CONTROLLER,'BG23_007_Gt')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG23_007_Gt'))
	tags={2359:'BG23_007_Gt'}
	pass
class BG23_007_Ge:
	def apply(self, target):
		target.windfury=1
	tags={GameTag.ATK:4, GameTag.HEALTH:4, } ## 23.4.3
	events = BeginBar(CONTROLLER).on(SetAttr(OWNER,'windfury',0), Destroy_spellcraft(SELF))	
	pass
class BG23_007_Gt:
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0}
	play = SpellcraftSpell(TARGET, 'BG23_007_Ge')	
	class Hand:
		events = EndTurn(CONTROLLER).on(Destroy(SELF))
	pass




## Eventide Brute (4)  ### OK ##
if BG_Eventide_Brute:
	BG_Minion_Naga+=['BG23_010','BG23_010e','BG23_010_G','BG23_010_Ge', ]#
	BG_PoolSet_Naga[4].append('BG23_010')
	BG_Naga_Gold['BG23_010']='BG23_010_G'
class BG23_010:# <12>[1453]
	""" Eventide Brute (4)
	After you cast a spell,gain +1/+1. """
	events = BG_Play(CONTROLLER, SPELL).on(Buff(SELF,'BG23_010e'))
	pass
BG23_010e=buff(1,1)
class BG23_010_G:# <12>[1453]
	""" Eventide Brute
	After you cast a spell,gain +2/+2. """
	events = BG_Play(CONTROLLER, SPELL).on(Buff(SELF,'BG23_010_Ge'))
	pass
BG23_010_Ge=buff(2,2)
	

from .BG_minion_quilboar import BG25__Pufferquil
if BG25__Pufferquil:# 4/2/6, quilbour/naga
	BG_Minion_Naga+=['BG25_039','BG25_039_G','BG25_039_Ge','BG25_039e']
	BG_PoolSet_Naga[4].append('BG25_039')
	BG_Naga_Gold['BG25_039']='BG25_039_G'

########### tavern tierr 5

## Critter Wrangler(5)  ### OK ###
if BG_Critter_Wrangler:
	BG_Minion_Naga+=['BG23_003','BG23_003e','BG23_003_G','BG23_003_Ge', ]#
	BG_PoolSet_Naga[5].append('BG23_003')
	BG_Naga_Gold['BG23_003']='BG23_003_G'
class BG23_003_Action(TargetedAction):
	TARGET=ActionArg()
	CARD=CardArg()
	OTHER=CardArg()
	BUFF=ActionArg()
	def do(self, source, target, card, other, buff):
		controller = target
		spell_card = card
		spell_target = other
		if hasattr(spell_card,'spellcraft_spellcard'):
			Buff(spell_target, buff).trigger(source)
		pass
	pass
class BG23_003:# <12>[1453]
	""" Critter Wrangler(5)
	After you cast a [Spellcraft] spell on a minion,give it +2/+2. """
	events = BG_Play(CONTROLLER, SPELL).on(BG23_003_Action(CONTROLLER, BG_Play.CARD, BG_Play.TARGET, 'BG23_003e'))
	pass
BG23_003e=buff(2,2) ## 23.4.3
class BG23_003_G:# <12>[1453]
	""" Critter Wrangler
	After you cast a [Spellcraft] spell on a minion,give it +4/+4. """
	events = BG_Play(CONTROLLER, SPELL).on(BG23_003_Action(CONTROLLER, BG_Play.CARD, BG_Play.TARGET, 'BG23_003_Ge'))
	pass
BG23_003_Ge=buff(4,4) ## 23.4.3


## Glowscale (5)  ### OK ###
if BG_Glowscale:
	BG_Minion_Naga+=['BG23_008','BG23_008e','BG23_008t','BG23_008_G','BG23_008_Ge','BG23_008_Gt', ]#
	BG_PoolSet_Naga[5].append('BG23_008')
	BG_Naga_Gold['BG23_008']='BG23_008_G'
class BG23_008:# <12>[1453]
	""" Glowscale (5)
	[Taunt][Spellcraft:] Give a minion [Divine Shield] until next turn. """
	play=Spellcraft(CONTROLLER,'BG23_008t')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG23_008t'))
	tags={2359:'BG23_008t'}
	pass
class BG23_008e:
	def apply(self,target):
		target.divine_shield=True	
		pass
	events = BeginBar(CONTROLLER).on(SetAttr(OWNER,'divine_shield',False), Destroy_spellcraft(SELF))
	pass
class BG23_008t:
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0}
	play = SpellcraftSpell(TARGET, 'BG23_008e')	
	tags = {GameTag.TECH_LEVEL:5}
	class Hand:
		events = EndTurn(CONTROLLER).on(Destroy(SELF))
	pass
class BG23_008_G:# <12>[1453]
	""" Glowscale
	[Taunt][Spellcraft:] Give a minion [Divine Shield] until next turn. """
	play=Spellcraft(CONTROLLER,'BG23_008_Gt')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG23_008_Gt'))
	tags={2359:'BG23_008_Gt'}
	pass
class BG23_008_Ge:
	def apply(self,target):
		target.divine_shield=True	
		pass
	events = BeginBar(CONTROLLER).on(SetAttr(OWNER,'divine_shield',False), Destroy_spellcraft(SELF))
	pass
class BG23_008_Gt:
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0}
	play = SpellcraftSpell(TARGET, 'BG23_008_Ge')	
	class Hand:
		events = EndTurn(CONTROLLER).on(Destroy(SELF))
	pass


#Corrupted Myrmidon (5) ### OK ###
if BG_Corrupted_Myrmidon:
	BG_Minion_Naga+=['BG23_012','BG23_012e','BG23_012_G','BG23_012_Ge', ]#
	BG_PoolSet_Naga[5].append('BG23_012')
	BG_Naga_Gold['BG23_012']='BG23_012_G'
class BG23_012_Buff(TargetedAction):
	TARGET = ActionArg()
	BUFF = ActionArg()
	AMOUNT = ActionArg()
	def do(self, source, target, buff, amount):
		Buff(target, buff).trigger(source)
		buff = target.buffs[-1]
		atk_buff  = target.atk*amount
		health_buff  = target.max_health*amount
		buff.tags[GameTag.ATK] = atk_buff
		buff.tags[GameTag.HEALTH] = health_buff
class BG23_012:# <12>[1453]
	""" Corrupted Myrmidon (5)
	[Start of Combat:] Double this minion's stats. """
	events = BeginBattle(CONTROLLER).on(BG23_012_Buff(SELF, 'BG23_012e', 1))
	pass
class BG23_012e:
	events = BeginBar(CONTROLLER).on(Destroy(SELF))
	pass
class BG23_012_G:# <12>[1453]
	""" Corrupted Myrmidon
	[Start of Combat:] Triple this minion's stats. """
	events = BeginBattle(CONTROLLER).on(BG23_012_Buff(SELF, 'BG23_012_Ge', 2))
	pass
class BG23_012_Ge:
	events = BeginBar(CONTROLLER).on(Destroy(SELF))
	pass



##Tidemistress Athissa (6)  アジッサ  ### OK ###
if BG_Tidemistress_Athissa:
	BG_Minion_Naga+=['BG23_013','BG23_013e','BG23_013_G','BG23_013_Ge', ]#
BG_PoolSet_Naga[6].append('BG23_013')
BG_Naga_Gold['BG23_013']='BG23_013_G'
class BG23_013_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self,source,target, buff):
		controller = target
		nagas=[]
		for card in controller.field:
			#if card.race==Race.NAGA:
			if race_identity(card, Race.NAGA):
				nagas.append(card)
		if len(nagas)>3:
			nagas=random.sample(nagas,3)
		for card in nagas:
			Buff(card, buff).trigger(source)
class BG23_013:# <12>[1453]
	""" Tidemistress Athissa (6)
	After you cast a spell, give three friendly Naga +1/+1. """
	events = BG_Play(CONTROLLER, SPELL).on(BG23_013_Action(CONTROLLER, 'BG23_013e'))
	pass
BG23_013e=buff(1,1)
class BG23_013_G:# <12>[1453]
	""" Tidemistress Athissa
	After you cast a spell, give three friendly Naga +2/+2. """
	events = BG_Play(CONTROLLER, SPELL).on(BG23_013_Action(CONTROLLER, 'BG23_013_Ge'))
	pass
BG23_013_Ge=buff(2,2)


if BG25__Greta_Gold_Gun:# 6/2/9 naga/pirate ## new 25.2.2#########################################
	BG_Minion_Naga+=['BG25_044','BG25_044_G','BG25_044e2','BG25_044t']
	BG_PoolSet_Naga[6].append('BG25_044')
	BG_Naga_Gold['BG25_044']='BG25_044_G'
class BG25_044:# (minion)
	""" Greta Gold-Gun
	<b>Spellcraft:</b> Make a different friendly Pirate or Naga Golden until next turn. """
	play = Spellcraft(CONTROLLER,'BG25_044t')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG25_044t'))
	tags={2359:'BG25_044t'}	
	pass
class BG25_044_G:# (minion)
	""" Greta Gold-Gun
	<b>Spellcraft:</b> Make a different friendly Pirate or Naga Golden until next turn. """
	play = Spellcraft(CONTROLLER,'BG25_044t')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG25_044t'))
	tags={2359:'BG25_044t'}	
	pass
class BG25_044e2_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		original_card = target.gold_original
		if original_card!=None:
			target.zone=Zone.GRAVEYARD
			original_card.zone=Zone.PLAY
class BG25_044e2:# (enchantment)
	""" Gold-Gunned
	Golden until next turn. """
	def apply(self, target):
		target.controller.game.BG_morph_gold(target)
		target.buffs.append(self)
	events = BeginBar(CONTROLLER).on(BG25_044e2_Action(OWNER))
	pass
class BG25_044t:# (spell)
	""" Gold-Gun
	Make a friendly Pirate or Naga Golden until next turn <i>(except Greta Gold-Gun)</i>. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0,
			   PlayReq.REQ_TARGET_WITH_RACE:2392}## Race.NAGA or Race.PIRATE
	play = SpellcraftSpell(TARGET, 'BG25_044e2')
	tags = {GameTag.TECH_LEVEL:6}
	pass

############################


