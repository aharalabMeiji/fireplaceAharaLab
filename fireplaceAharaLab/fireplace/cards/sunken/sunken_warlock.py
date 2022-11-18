from ..utils import *

Sunken_Warlock=[]

Sunken_Herald_of_Shadows=True  ###
Sunken_Immolate=True  ###
Sunken_Commander_Ulthok=True  ###
Sunken_Azsharan_Scavenger=True  ###
Sunken_Voidgill=True  ###
Sunken_Bloodscent_Vilefin=True  ###
Sunken_Abyssal_Wave=True  ###
Sunken_Rock_Bottom=True  ###
Sunken_Sirakess_Cultist=True  ###
Sunken_Dragged_Below=True  ###
Sunken_Chum_Bucket=True  ###
Sunken_Zaqul=True  ###
Sunken_Gigafin=True  ###


if Sunken_Herald_of_Shadows:# 
	Sunken_Warlock+=['TID_717']
	Sunken_Warlock+=['TID_717e']
	Sunken_Warlock+=['TID_717e2']
	Sunken_Warlock+=['TID_717e2b']
	Sunken_Warlock+=['TID_717eb']
class TID_717_Action(TargetedAction):
	CONTROLLER=ActionArg()
	TARGET=ActionArg()
	def do(self, source, controller, target):
		if source.script_data_num_1>0:
			Buff(source, 'TID_717e2', max_health=2).trigger(source)
			if isinstance(target, list):
				target=target[0]
			Buff(target, 'TID_717e', max_health=-2).trigger(source)
		pass
class TID_717:# <9>[1658]
	""" Herald of Shadows
	[Battlecry:] If you've cast a Shadow spell while holding this, steal 2 Health from a minion. """
	class Hand:
		events = Play(CONTROLLER, SPELL + SHADOW).on(SetScriptDataNum1(SELF, 1))
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0}
	play = TID_717_Action(CONTROLLER, TARGET)
	pass
class TID_717e:# <9>[1658]
	""" Siphoned
	Reduced Health. """
	#
	pass
class TID_717e2:# <9>[1658]
	""" Shadow Siphon
	Increased Health. """
	#
	pass
class TID_717e2b:# <9>[1658]
	""" Siphoned
	Increased Health. """
	#
	pass
class TID_717eb:# <9>[1658]
	""" Siphoned
	Reduced Health. """
	#
	pass




if Sunken_Immolate:# 
	Sunken_Warlock+=['TID_718']
	Sunken_Warlock+=['TID_718e']
	Sunken_Warlock+=['TID_718e2']
class TID_718:# <9>[1658]
	""" Immolate
	Light every card in the opponent's hand on fire. In 3 turns, any still in hand are destroyed! """
	play = Buff(ENEMY_HAND, 'TID_718e2'),Buff(CONTROLLER, 'TID_718e')
	pass
class TID_718_Action(GameAction):
	def do(self, source):
		controller=source.controller
		for card in controller.opponent.hand:
			if 'TID_718e2' in [buff.id for buff in card.buffs]:
				Destroy(card).trigger(source)
		Deaths().trigger()
		pass
class TID_718e:# <9>[1658]
	""" Engulfed in Flame
	In 3 turns, destroy the opponent's cards that are on fire. """
	events = OWN_TURN_END.on(SidequestCounter(SELF, 3, [TID_718_Action()] ))
	pass
class TID_718e2:# <9>[1658]
	""" Engulfed in Flame
	This card is on fire! """
	#
	pass

if Sunken_Commander_Ulthok:# 
	Sunken_Warlock+=['TID_719']
	Sunken_Warlock+=['TID_719e']
class TID_719:# <9>[1658]
	""" Commander Ulthok
	[Battlecry:] Your opponent's cards cost Health instead of Mana next turn. """
	play = Buff(ENEMY_HAND, 'TID_719e')
	pass

class TID_719e:# <9>[1658]
	""" Blood Squeeze
	Your cards cost Health instead of Mana this turn. """
	def apply(self, target):
		target.cards_cost_health=True
		pass
	events = OWN_TURN_END.on(SetAttr(OWNER, 'cards_cost_health', False),Destroy(SELF))
	pass

if Sunken_Azsharan_Scavenger:# 
	Sunken_Warlock+=['TSC_039']
	Sunken_Warlock+=['TSC_039t']
	Sunken_Warlock+=['TSC_039te']
class TSC_039:# <9>[1658]
	""" Azsharan Scavenger
	[Battlecry:] Put a 'Sunken Scavenger' on the bottom of your deck. """
	play = ShuffleBottom(CONTROLLER, 'TSC_039t')
	pass
class TSC_039t:# <9>[1658]
	""" Sunken Scavenger
	[Battlecry:] Give your other Murlocs +1/+1 <i>(wherever they are)</i>. """
	def play(self):
		for card in self.controller.hand + self.controller.field + self.controller.deck:
			if card.type==CardType.MINION and card.race==Race.MURLOC:
				Buff(card, 'TSC_039te').trigger(self)
	pass
TSC_039te=buff(1,1)

if Sunken_Voidgill:# 
	Sunken_Warlock+=['TSC_614']
	Sunken_Warlock+=['TSC_614e']
class TSC_614:# <9>[1658]
	""" Voidgill
	[Deathrattle:] Give all Murlocs in your hand +1/+1. """
	deathrattle = Buff(FRIENDLY_HAND + MURLOC, 'TSC_614e')
	pass
TSC_614e=buff(1,1)

if Sunken_Bloodscent_Vilefin:# 
	Sunken_Warlock+=['TSC_753']
	Sunken_Warlock+=['TSC_753e']
class TSC_753_DredgeChoice(Choice):
	def choose(self, card):
		super().choose(card)
		if Config.LOGINFO:
			Config.log("DredgeChoice.choose","%s chooses %r"%(card.controller.name, card))
		controller = card.controller
		for c in controller.deck[:3]:
			if card.id==c.id:
				controller.deck.remove(c)
				controller.deck.append(c)
				if c.type==CardType.MINION and c.race==Race.MURLOC:
					Buff(c, 'TSC_753e').trigger(controller)
				break
		pass
class TSC_753_Dredge(TargetedAction):
	"""
	TARGET=ActionArg()#CONTROLLER
	"""
	TARGET=ActionArg()
	def do(self, source, target):
		bottom3ID=[card.id for card in target.deck[:3]]
		TSC_753_DredgeChoice(target, RandomID(*bottom3ID)*3).trigger(source)
	pass
class TSC_753:# <9>[1658]
	""" Bloodscent Vilefin
	[Battlecry:] [Dredge]. If it's a Murloc, change its Cost to_Health instead of Mana. """
	play = TSC_753_Dredge(CONTROLLER)
	pass
class TSC_753e:# <9>[1658]
	""" Fresh Scent
	Costs Health instead of Mana. """
	def apply(self, target):
		target.cards_cost_health=True
		pass
	#
	pass

if Sunken_Abyssal_Wave:# 
	Sunken_Warlock+=['TSC_924']
class TSC_924:# <9>[1658]
	""" Abyssal Wave
	Deal $4 damage to all minions. Give your opponent an Abyssal Curse(TSC_955t). """
	play = Hit(ENEMY_MINIONS, 4), Give(OPPONENT, 'TSC_955t')
	pass

if Sunken_Rock_Bottom:# 
	Sunken_Warlock+=['TSC_925']
	Sunken_Warlock+=['TSC_925t']
class TSC_925_DredgeChoice(Choice):
	def choose(self, card):
		super().choose(card)
		if Config.LOGINFO:
			Config.log("DredgeChoice.choose","%s chooses %r"%(card.controller.name, card))
		controller = card.controller
		for c in controller.deck[:3]:
			if card.id==c.id:
				controller.deck.remove(c)
				controller.deck.append(c)
				if c.type==CardType.MINION and c.race==Race.MURLOC:
					Summon(controller, 'TSC_925t').trigger(controller)
				break
		pass
class TSC_925_Dredge(TargetedAction):
	"""
	TARGET=ActionArg()#CONTROLLER
	"""
	TARGET=ActionArg()
	def do(self, source, target):
		bottom3ID=[card.id for card in target.deck[:3]]
		TSC_925_DredgeChoice(target, RandomID(*bottom3ID)*3).trigger(source)
	pass
class TSC_925:# <9>[1658]
	""" Rock Bottom
	Summon a 1/1Murloc, then [Dredge].If it's also a Murloc,summon one more. """
	play = Summon(CONTROLLER, 'TSC_925t'), TSC_925_Dredge(CONTROLLER)
	pass
class TSC_925t:# <9>[1658]
	""" Coldlight Lurker
	 """
	pass

if Sunken_Sirakess_Cultist:# 
	Sunken_Warlock+=['TSC_955']
	Sunken_Warlock+=['TSC_955t']
class TSC_955:# <9>[1658]
	""" Sira'kess Cultist
	[Battlecry:] Give your opponent an Abyssal Curse. """
	play = Give(OPPONENT, 'TSC_955t')
	pass

class TSC_955t_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=target
		amount = controller.abyssal_curse
		if 'TSC_959e' in [buff.id for buff in source.buffs]:
			Heal(controller.opponent.hero, amount).trigger(source)
		else:
			Hit(controller.hero, amount).trigger(source)
		controller.abyssal_curse+=1
		pass
class TSC_955t:# <9>[1658]
	""" Abyssal Curse
	At the start of your turn,take {0} damage. Each Curse is worse than the last.<i>({1} |4(turn,turns) remaining).</i> """
	events = [
		OWN_TURN_BEGIN.on(TSC_955t_Action(CONTROLLER) ),
		OWN_TURN_END.on(SidequestCounter(SELF, 2, [Destroy(SELF)]))
	]
	pass

if Sunken_Dragged_Below:# 
	Sunken_Warlock+=['TSC_956']
class TSC_956:# <9>[1658]
	""" Dragged Below
	Deal $4 damage to a minion.Give your opponent an Abyssal Curse. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = Hit(TARGET, 4), Give(OPPONENT, 'TSC_955t')#
	pass

if Sunken_Chum_Bucket:# 
	Sunken_Warlock+=['TSC_957']
	Sunken_Warlock+=['TSC_957e']
class TSC_957:# <9>[1658]
	""" Chum Bucket
	Give all Murlocs in your hand +1/+1. Repeat foreach Murloc you control. """
	def play(self):
		amount=len([card for card in self.controller.hand if card.type==CardType.MINION and card.race==Race.MURLOC])+1
		for card in self.controller.hand:
			if card.type==CardType.MINION and card.race==Race.MURLOC:
				Buff(card, 'TSC_957e', atk=amount, max_health=amount).trigger(self)
	pass
class TSC_957e:# <9>[1658]
	""" Empty Bucket 	+1/+1. """
	pass

if Sunken_Zaqul:# 
	Sunken_Warlock+=['TSC_959']
	Sunken_Warlock+=['TSC_959e']
	#Sunken_Warlock+=['TSC_959e2']
class TSC_959:# <9>[1658]
	""" Za'qul
	Your Abyssal Curses heal you for the damage they deal.[Battlecry:] Give your opponent an Abyssal Curse. """
	update = Refresh(ENEMY_HAND + ID('TSC_955t'), buff='TSC_959e')
	pass
class TSC_959e:# <9>[1658]
	""" Cursed
	Your Abyssal Curses(TSC_955t) heal you for the damage they deal. """
	pass
class TSC_959e2:# <9>[1658]
	""" Cursed
	Your Curses cost (2) more this game. """
	pass

if Sunken_Gigafin:# 
	Sunken_Warlock+=['TSC_962']
	Sunken_Warlock+=['TSC_962e']
	Sunken_Warlock+=['TSC_962e2']
	Sunken_Warlock+=['TSC_962t']
class TSC_962_Action1(TargetedAction):
	TARGET=ActionArg()
	CARDS=ActionArg()
	def do(self, source, target, cards):
		for card in cards:
			card.zone=Zone.SETASIDE
			target.sidequest_list0.append(card)
			EatsMinion(target, card, 1, 'TSC_962e2').trigger(source)
		pass
class TSC_962_Action2(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		for card in target.sidequest_list0:
			card.zone=Zone.SETASIDE
			card.zone=Zone.PLAY
		pass
class TSC_962:# <9>[1658]
	""" Gigafin
	[Colossal +1]. [Battlecry:]Devour all enemy minions.[Deathrattle:] Spit them back out. """
	play = Summon(CONTROLLER, 'TSC_962t'), TSC_962_Action1(SELF, ENEMY_MINIONS)
	deathrattle=TSC_962_Action2(SELF)
	pass
class TSC_962e:# <9>[1658]
	""" Swallowed Whole
	Storing a Minion. """
	#
	pass
class TSC_962e2:# <9>[1658]
	""" Bloated
	Gigafin has eaten all enemy minions! """
	#
	pass
class TSC_962_Action3(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		for card in target.field:
			if card.id=='TSC_962':
				card.sidequest_list0=[]
				break
		pass
class TSC_962t:# <9>[1658]
	""" Gigafin's Maw
	[Taunt][Deathrattle:] Permanently destroy all minions inside Gigafin. """
	deathrattle = TSC_962_Action3(CONTROLLER)
	pass

