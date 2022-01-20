from ..utils import *
import copy

#Core_Warlock=[
#	"CORE_AT_021","AT_021e","CORE_CS2_062","CORE_CS2_064","CORE_EX1_302","CORE_EX1_304","EX1_304e","CORE_EX1_309","CORE_EX1_312","CORE_EX1_319","CORE_EX1_323","EX1_323h","EX1_tk33","EX1_tk34","EX1_323w","CORE_GIL_191","CORE_GIL_191t","CORE_ICC_055","CORE_OG_241","OG_241a","CORE_UNG_833","CS3_002","CS3_002t","CS3_003","CS3_021"
#	]

class CORE_AT_021:# <9>[1637]
	""" Tiny Knight of Evil
	Whenever you discard a card, gain +1/+1. """
	#
	events = Discard(FRIENDLY_MINIONS).on(Buff(SELF, "AT_021e"))
	pass
AT_021e = buff(+1, +1)

class CORE_CS2_062:# <9>[1637]
	""" Hellfire
	Deal $3 damage to ALL_characters. """
	play = Hit(ALL_CHARACTERS, 3)
	pass

class CORE_CS2_064:# <9>[1637]
	""" Dread Infernal
	[Battlecry:] Deal 1 damage to ALL other characters. """
	play = Hit(ALL_CHARACTERS - SELF, 1)
	pass

class CORE_EX1_302:# <9>[1637]
	""" Mortal Coil
	Deal $1 damage to a minion. If that kills it, draw a card. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 1), Dead(TARGET) & Draw(CONTROLLER)
	pass

class CORE_EX1_304:# <9>[1637]
	""" Void Terror
	[Battlecry:] Destroy both adjacent minions and gain their Attack and Health. """
	play = (
		Buff(SELF, "EX1_304e", atk=ATK(SELF_ADJACENT), max_health=CURRENT_HEALTH(SELF_ADJACENT)),
		Destroy(SELF_ADJACENT)
	)
	pass

class CORE_EX1_309:# <9>[1637]
	""" Siphon Soul
	Destroy a minion. Restore #3 Health to_your hero. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Destroy(TARGET), Heal(FRIENDLY_HERO, 3)
	pass

class CORE_EX1_312:# <9>[1637]
	""" Twisting Nether
	Destroy all minions. """
	play = Destroy(ALL_MINIONS)
	pass

class CORE_EX1_319:# <9>[1637]
	""" Flame Imp
	[Battlecry:] Deal 3 damage to your hero. """
	play = Hit(FRIENDLY_HERO, 3)
	pass

class CORE_EX1_323:# <9>[1637]
	""" Lord Jaraxxus
	[Battlecry:] Equip a 3/8 Blood Fury. """
	play = (
		Summon(CONTROLLER, "EX1_323h").then(Morph(SELF, Summon.CARD)),
		Summon(CONTROLLER, "EX1_323w")
	)
	pass
class EX1_323h: ## Hero (9/*/5)
	""" Lord Jaraxxus
	"""
	pass
class EX1_tk33: ## heropower
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

class CORE_GIL_191:# <9>[1637] #
	""" Fiendish Circle
	Summon four 1/1 Imps. """
	play = Summon(CONTROLLER, 'CORE_GIL_191t') * 4
	pass

class CORE_GIL_191t:# <9>[1637]
	""" Imp
	"""
	#
	pass

class CORE_ICC_055:# <9>[1637]
	""" Drain Soul
	[Lifesteal]Deal $3 damage to a minion. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 3)
	pass

class CORE_OG_241:# <9>[1637] (1/1/1)
	""" Possessed Villager
	[Deathrattle:] Summon a 1/1 Shadowbeast. """
	deathrattle = Summon(CONTROLLER, "OG_241a")	#
	pass
class OG_241a:# minion (1/1/1)
	""" Shadowbeast """
	pass

class CORE_UNG_833:# <9>[1637]
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

class CS3_002:# <9>[1637]
	""" Ritual of Doom
	Destroy a friendly minion. If you had 5 or more, summon a 5/5 Demon. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0 }
	def play(self):
		minion_count=len(self.controller.field)
		Destroy(self.target).trigger(self)
		if minion_count>=5:
			Summon(self.controller, 'CS3_002t').trigger(self)
	pass

class CS3_002t:# <9>[1637]
	""" Demonic Tyrant
	vanilla  """
	#
	pass

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
class CS3_003:# <9>[1637]
	""" Felsoul Jailer
	[Battlecry:] Your opponent discards a minion.[Deathrattle:] Return it. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = CS3_003Play(TARGET)
	deathrattle = CS3_003Deathrattle(TARGET)
	pass

class CS3_021:# <9>[1637] (7/4/10)
	""" Enslaved Fel Lord
	[Taunt]. Also damages the minions next to whomever this attacks. """
	events = Attack(SELF, ENEMY_MINIONS).on(Hit(ADJACENT(ENEMY_MINIONS+Attack.DEFENDER), ATK(SELF)))
	pass

