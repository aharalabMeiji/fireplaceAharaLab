from ..utils import *

Lich_DemonHunter=[]

Lich_Mark_of_Scorn=True
Lich_Fierce_Outsider=True
Lich_Feldorei_Warband=True
Lich_Unleash_Fel=True
Lich_Wretched_Exile=True
Lich_Deal_with_a_Devil=True
Lich_Brutal_Annihilan=True
Lich_Vengeful_Walloper=True
Lich_Souleaters_Scythe=True
Lich_Felerin_the_Forgotten=True


if Lich_Mark_of_Scorn:# 
	Lich_DemonHunter+=['RLK_206']
class RLK_206_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		card=get00(Draw(controller).trigger(source))
		if card.type!=CardType.MINION and len(controller.opponent.field):
			low=[]
			for ocard in controller.opponent.field:
				if ocard.type==CardType.MINION:
					if low==[] or low[0].max_health>ocard.max_health:
						low=[ocard]
					if low[0].max_health==ocard.max_health:
						low.append(ocard)
			Hit(random.choice(low), 3).trigger(source)
		pass
class RLK_206:# <14>[1776]
	""" Mark of Scorn (spell:2)
	Draw a card. If it's not a minion, deal $3 damage to the lowest Health enemy. """
	play = RLK_206_Action()
	pass

if Lich_Fierce_Outsider:# 
	Lich_DemonHunter+=['RLK_207']
	Lich_DemonHunter+=['RLK_207e']
class RLK_207_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		cards = [card for card in controller.hand if card.type==CardType.MINION and getattr(card, 'outcast_card',0)==1]
		for card in cards:
			Buff(card, 'RLK_207e').trigger(source)
		pass
class RLK_207:# <14>[1776]
	""" Fierce Outsider (minion:1/2/1)
	<b>Rush</b> <b>Outcast:</b> Your next <b>Outcast</b> card costs (1) less. """
	#<Tag enumID="1333" name="OUTCAST" type="Int" value="1"/>
	outcast = RLK_207_Action()
	pass
class RLK_207e_Action(TargetedAction):# 
	def do(self, source, target):# 
		controller=source.controller
		if getattr(target, 'outcast_card',0)==1:
			source.remove()
class RLK_207e:# <14>[1776]
	""" Introverted (0)
	Your next <b>Outcast</b> card costs (1) less. """
	cost = lambda self, i: max(0,i-1)
	class Hand:
		events = Play(CONTROLLER, FRIENDLY + MINION).on(RLK_207e_Action(Play.CARD))
	pass

if Lich_Feldorei_Warband:# 
	Lich_DemonHunter+=['RLK_208', 'BT_036t']
class RLK_208_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		cards = [card for card in controller.deck if card.type==CardType.MINION]
		if len(cards)==0:
			Summon(controller, 'BT_036t').trigger(source)
			Summon(controller, 'BT_036t').trigger(source)
			Summon(controller, 'BT_036t').trigger(source)
			Summon(controller, 'BT_036t').trigger(source)
		pass
class RLK_208:# <14>[1776]
	""" Fel'dorei Warband (spell:4)
	Deal $4 damage. If your deck has no minions, summon four 1/1 Illidari with <b>Rush</b>. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = Hit(TARGET, 4), RLK_208_Action()
	pass

if Lich_Unleash_Fel:# 
	Lich_DemonHunter+=['RLK_209']
class RLK_209_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		tmp=source.lifesteal
		source.lifesteal=True
		for card in controller.opponent.characters:
			Hit(card, 1).trigger(source)
		source.lifesteal=tmp
		pass
class RLK_209:# <14>[1776]
	""" Unleash Fel (spell:1)
	Deal $1 damage to all enemies. <b>Manathirst_(4):</b> With <b>Lifesteal</b>. """
	### manathirst 4 -> 6 (25.0.4)
	play = Manathirst(6, [RLK_209_Action()], [Hit(ENEMY_CHARACTERS, 1)]) 
	pass

if Lich_Wretched_Exile:# 
	Lich_DemonHunter+=['RLK_210']
class RLK_210_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_210:# <14>[1776]
	""" Wretched Exile (minion:2/2/3)
	After you play an <b>Outcast</b> card, add a random <b>Outcast</b> card to your hand. """
	events = Play(CONTROLLER, OUTCAST).after(Give(CONTROLLER, RandomCollectible(outcast=True)))
	pass

if Lich_Deal_with_a_Devil:# 
	Lich_DemonHunter+=['RLK_211']
	Lich_DemonHunter+=['RLK_211t']
class RLK_211_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		amount=2
		if len([card for card in controller.deck if card.type==CardType.MINION])==0:
			amount+=1
		for count in range(amount):
			Summon(controller,'RLK_211t').trigger(source)
		pass
class RLK_211:# <14>[1776]
	""" Deal with a Devil (spell:5)
	Summon two 3/3 Felfiends with <b>Lifesteal</b>. If your deck has no minions, summon another. """
	play = RLK_211_Action()
	pass
class RLK_211t:# <14>[1776]
	""" Felfiend (minion:3/3/3)
	<b>Lifesteal</b> """
	pass

if Lich_Brutal_Annihilan:# 
	Lich_DemonHunter+=['RLK_212']
class RLK_212_Action(TargetedAction):# 
	TARGET=ActionArg()
	AMOUNT=IntArg()
	def do(self, source, target, amount):# 
		controller=source.controller
		if source.alive:
			Hit(controller.opponent.hero, amount).trigger(source)
		pass
class RLK_212:# <14>[1776]
	""" Brutal Annihilan (minion:9/9/9)
	<b>Taunt</b>, <b>Rush</b> After this minion survives damage, deal that amount to the enemy hero. """
	events = Damage(SELF).on(RLK_212_Action(Damage.TARGET, Damage.AMOUNT))
	pass

if Lich_Vengeful_Walloper:# 
	Lich_DemonHunter+=['RLK_213']
class RLK_213_Count(LazyNum):# 
	def __init__(self, selector):
		super().__init__()
		self.selector = selector
	def evaluate(self, source):
		controller=source.controller
		amount = len(controller.outcast_play_log)
		return self.num(-amount)
class RLK_213:# <14>[1776]
	""" Vengeful Walloper (minion:7/5/5)
	<b>Rush</b>. Costs (1) less for each <b>Outcast</b> card you've played this game. """
	cost_mod = RLK_213_Count(CONTROLLER)
	pass

if Lich_Souleaters_Scythe:# 
	Lich_DemonHunter+=['RLK_214']
	Lich_DemonHunter+=['RLK_214t']
#class RLK_214_Begingame_Action(GameAction):# 
#	def do(self, source):# 
#		controller=source.controller
#		for cd in reversed(controller.deck):
#			if cd.id=='RLK_214':
#				cd.zone==Zone.SETASIDE
#				cd.zone==Zone.GRAVEYARD
#		card = controller.card("RLK_214t")
#		minions=[cd for cd in controller.deck if cd.type==CardType.MINION]
#		if len(minions)>3:
#			minions=random.sample(minions, 3)
#		card.sidequest_list0=[cd.id for cd in minions]
#		card.zone=Zone.DECK
#		for cd in reversed(minions):
#			cd.zone==Zone.SETASIDE
#			cd.zone==Zone.GRAVEYARD
#		pass
class RLK_214:# <14>[1776]
	""" Souleater's Scythe (4)
	<b>Start of Game:</b> Consume 3 different minions in your deck. Leave behind Souls that <b>Discover</b> them. """
	## See utils.play_one_game
	pass
class RLK_214t_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		card.zone=Zone.HAND
		pass
class RLK_214t_Action(GameAction):
	def do(self, source):
		controller=source.controller
		if isinstance(source.sidequest_list0[0], str):
			the_list=source.sidequest_list0
		elif isinstance(source.sidequest_list0[0], list):
			the_list=source.sidequest_list0[0]
		else:
			the_list=['RLK_220', 'CORE_NEW1_027', 'RLK_221']
		RLK_214t_Choice(controller, RandomID(*the_list)).trigger(source)
		pass
class RLK_214t:# <14>[1776]
	""" Bound Soul (spell:1)
	<b>Discover</b> a minion consumed by Souleater's Scythe. """
	play = RLK_214t_Action()
	pass

if Lich_Felerin_the_Forgotten:# 
	Lich_DemonHunter+=['RLK_215']
class RLK_215_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		card = get00(RandomOutcast().evaluate(source))
		card.controller=controller
		card.zone=Zone.HAND
		card._cost=max(0, card._cost-2)
		pass
class RLK_215:# <14>[1776]
	""" Felerin, the Forgotten (minion:4/3/3)
	<b>Battlecry:</b> Add a random <b>Outcast</b> card to the left and right sides of your hand. They cost (2) less. """
	play = RLK_215_Action()
	pass


