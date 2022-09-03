from ..utils import *
import copy



########################################

Core_Warlock=[]
Core_Tiny_Knight_of_Evil=True
Core_Imp_Gang_Boss=True
Core_Abyssal_Enforcer=True
Core_Hellfire=True
Core_Voidwalker=True
Core_Mortal_Coil=True
Core_Void_Terror=True
Core_Siphon_Soul=True
Core_Twisting_Nether=True
Core_Flame_Imp=True
Core_Lord_Jaraxxus=True
Core_Fiendish_Circle=True
Core_Drain_Soul=True
Core_Darkshire_Librarian=True
Core_High_Priestess_Jeklik=True##  check
Core_Lakkari_Felhound=True
Core_Felsoul_Jailer=True



if Core_Tiny_Knight_of_Evil:# 
	Core_Warlock+=['CORE_AT_021']
class CORE_AT_021:# <9>[1637] ##23.6 ## OK 
	""" Tiny Knight of Evil
	Whenever you discard a card, gain +1/+1. """
	events = Discard(FRIENDLY_MINIONS).on(Buff(SELF, "AT_021e"))
	pass
AT_021e = buff(+1, +1)

if Core_Imp_Gang_Boss:# 
	Core_Warlock+=['CORE_BRM_006','BRM_006t']
class CORE_BRM_006:# <9>[1637] ##23.6 ## visually OK
	""" Imp Gang Boss
	Whenever this minion takes damage, summon a 1/1 Imp. """
	events = SELF_DAMAGE.on(Summon(CONTROLLER, "BRM_006t"))
	pass
class BRM_006t:
	pass

if Core_Abyssal_Enforcer:# 
	Core_Warlock+=['CORE_CFM_751']
class CORE_CFM_751:# <9>[1637] ##23.6 ##visually OK
	""" Abyssal Enforcer
	[Battlecry:] Deal 3 damage to all other characters. """
	play = Hit(ALL_CHARACTERS - SELF, 3)
	pass

if Core_Hellfire:# 
	Core_Warlock+=['CORE_CS2_062']
class CORE_CS2_062:# <9>[1637] ##23.6  ## OK 
	""" Hellfire
	Deal $3 damage to ALL_characters. """
	play = Hit(ALL_CHARACTERS, 3)
	pass

class CORE_CS2_064:# <9>[1637] ##22.6  ## OK 
	""" Dread Infernal
	[Battlecry:] Deal 1 damage to ALL other characters. """
	play = Hit(ALL_CHARACTERS - SELF, 1)
	pass

if Core_Voidwalker:# 
	Core_Warlock+=['CORE_CS2_065']
class CORE_CS2_065:# <9>[1637] ##23.6 ##OK
	""" Voidwalker
	[Taunt] """
	pass

if Core_Mortal_Coil:# 
	Core_Warlock+=['CORE_EX1_302']
class CORE_EX1_302:# <9>[1637] ##23.6  ## OK 
	""" Mortal Coil
	Deal $1 damage to a minion. If that kills it, draw a card. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 1), Dead(TARGET) & Draw(CONTROLLER)
	pass

if Core_Void_Terror:# 
	Core_Warlock+=['CORE_EX1_304','EX1_304e']
class CORE_EX1_304:# <9>[1637] ##23.6 ## OK 
	""" Void Terror
	[Battlecry:] Destroy bothadjacent minions and gain their Attack and Health. """
	play = (
		Buff(SELF, "EX1_304e", atk=ATK(SELF_ADJACENT), max_health=CURRENT_HEALTH(SELF_ADJACENT)),
		Destroy(SELF_ADJACENT)
	)
	pass
class EX1_304e:
	pass

if Core_Siphon_Soul:# 
	Core_Warlock+=['CORE_EX1_309']
class CORE_EX1_309:# <9>[1637] ##23.6 ## OK 
	""" Siphon Soul
	Destroy a minion. Restore #3 Health to_your hero. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Destroy(TARGET), Heal(FRIENDLY_HERO, 3)
	pass

if Core_Twisting_Nether:# 
	Core_Warlock+=['CORE_EX1_312']
class CORE_EX1_312:# <9>[1637] ##23.6 ## OK 
	""" Twisting Nether
	Destroy all minions. """
	play = Destroy(ALL_MINIONS)
	pass

if Core_Flame_Imp:# 
	Core_Warlock+=['CORE_EX1_319']
class CORE_EX1_319:# <9>[1637] ##23.6 ## OK 
	""" Flame Imp
	[Battlecry:] Deal 3 damage to your hero. """
	play = Hit(FRIENDLY_HERO, 3)
	pass

if Core_Lord_Jaraxxus:# 
	Core_Warlock+=['CORE_EX1_323']
class CORE_EX1_323:# <9>[1637] ##23.6 ## OK 
	""" Lord Jaraxxus
	[Battlecry:] Equip a 3/8 Blood Fury. """
	play = (
		Summon(CONTROLLER, "EX1_323h").then(Morph(SELF, Summon.CARD)),
		Summon(CONTROLLER, "EX1_323w")
	)
	pass
class EX1_323h: ## Hero (9/*/5) ##22.6
	""" Lord Jaraxxus
	"""
	pass
class EX1_tk33: ## heropower  ##22.6
	"""INFERNO!"""
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	activate = Summon(CONTROLLER, "EX1_tk34")
class EX1_tk34: ##(6/6/6)
	""" Infernal """
	## vanilla 
class EX1_323w: ## weapon (3/3/8)
	""" Blood Fury
	"""
	pass


if Core_Fiendish_Circle:# 
	Core_Warlock+=['CORE_GIL_191']
	Core_Warlock+=['CORE_GIL_191t']
class CORE_GIL_191:# <9>[1637] ##23.6 ## OK 
	""" Fiendish Circle
	Summon four 1/1 Imps. """
	play = Summon(CONTROLLER, 'CORE_GIL_191t') * 4
	pass
class CORE_GIL_191t:# <9>[1637] ##22.6
	""" Imp
	"""




if Core_Drain_Soul:# 
	Core_Warlock+=['CORE_ICC_055']
class CORE_ICC_055:# <9>[1637] ##23.6 ## OK 
	""" Drain Soul
	[Lifesteal]Deal $3 damageto a minion. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 3)
	pass

if Core_Darkshire_Librarian:# 
	Core_Warlock+=['CORE_OG_109']
class CORE_OG_109:# <9>[1637] ##23.6 ###visually OK
	""" Darkshire Librarian
	[Battlecry:]Discard a random card. [Deathrattle:]Draw a card. """
	play = Discard(RANDOM(FRIENDLY_HAND))
	deathrattle = Draw(CONTROLLER)
	pass

class CORE_OG_241:# <9>[1637] (1/1/1) ##22.6  ## OK 
	""" Possessed Villager
	[Deathrattle:] Summon a 1/1 Shadowbeast. """
	deathrattle = Summon(CONTROLLER, "OG_241a")	#
	pass
class OG_241a:# minion (1/1/1)
	""" Shadowbeast """
	pass

if Core_High_Priestess_Jeklik:# 
	Core_Warlock+=['CORE_TRL_252']
class CORE_TRL_252:# <9>[1637] ##23.6 #################need check###########
	""" High Priestess Jeklik
	[Taunt], [Lifesteal]When you discard this,add 2 copies of it to your hand. """
	#[挑発]、[生命奪取]このカードを破棄した時そのコピー2枚を自分の手札に追加する。
	events = Discard(SELF).on(Give(CONTROLLER, Copy(SELF))*2)
	pass

if Core_Lakkari_Felhound:# 
	Core_Warlock+=['CORE_UNG_833']
class CORE_UNG_833:# <9>[1637] ##23.6 ## OK 
	""" Lakkari Felhound
	[Taunt][Battlecry:] Discard your two lowest-Cost cards. """
	def play(self):
		controller = self.controller
		hand = controller.hand
		lowest = None
		next_lowest=None
		for card in hand:
			if lowest==None:
				lowest=card
			elif lowest.cost>=card.cost:
				next_lowest=lowest
				lowest=card
			else:
				if next_lowest==None:
					next_lowest=card
				elif next_lowest.cost>=card.cost:
					next_lowest=card
		if lowest:
			Discard(lowest).trigger(self)
		if next_lowest:
			Discard(next_lowest).trigger(self)
		pass
	pass


class CS3_002:# <9>[1637] ##22.6 ## OK 
	""" Ritual of Doom
	Destroy a friendly minion. If you had 5 or more, summon a 5/5 Demon. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0 }
	def play(self):
		minion_count=len(self.controller.field)
		Destroy(self.target).trigger(self)
		if minion_count>=5:
			Summon(self.controller, 'CS3_002t').trigger(self)
	pass
class CS3_002t:# <9>[1637] ##23.6
	""" Demonic Tyrant
	 """
	pass

if Core_Felsoul_Jailer:# 
	Core_Warlock+=['CS3_003']
class CS3_003Play(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		source.sidequest_list0=target.id
		Discard(target).trigger(source)
		pass
class CS3_003Deathrattle(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		Summon(source.controller.opponent, source.sidequest_list0).trigger(source)
		pass
class CS3_003:# <9>[1637] ##23.6  ## OK 
	""" Felsoul Jailer
	[Battlecry:] Your opponentdiscards a minion.[Deathrattle:] Return it. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = CS3_003Play(TARGET)
	deathrattle = CS3_003Deathrattle(TARGET)
	pass

class CS3_021:# <9>[1637] (7/4/10) ##22.6  ## OK 
	""" Enslaved Fel Lord
	[Taunt]. Also damages the minions next to whomever this attacks. """
	events = Attack(SELF, ENEMY_MINIONS).on(Hit(ADJACENT(ENEMY_MINIONS+Attack.DEFENDER), ATK(SELF)))
	pass

#######################################
