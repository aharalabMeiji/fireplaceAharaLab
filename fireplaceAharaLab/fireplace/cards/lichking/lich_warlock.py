from ..utils import *

Lich_Warlock=[]

Lich_Infantry_Reanimator=True
Lich_Walking_Dead=True
Lich_Scourge_Supplies=True
Lich_Soul_Barrage=True
Lich_Savage_Ymirjar=True
Lich_Shallow_Grave=True
Lich_Twisted_Tether=True
Lich_Devourer_of_Souls=True
Lich_DarKhan_Drathir=True
Lich_Amorphous_Slime=True


if Lich_Infantry_Reanimator:# 
	Lich_Warlock+=['RLK_531']
class RLK_531_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		cards = [card.id for card in controller.death_log if card.MINION_RACE(Race.UNDEAD)]
		if len(cards):
			newcard=get00(Summon(controller, random.choice(cards)).trigger(source))
			newcard.reborn=True
		pass
class RLK_531:# <9>[1776]
	""" Infantry Reanimator (minion:6/4/4)
	<b>Battlecry:</b> Resurrect a friendly Undead. Give it <b>Reborn</b>. """
	play = RLK_531_Action()
	pass

if Lich_Walking_Dead:# 
	Lich_Warlock+=['RLK_532']
class RLK_532:# <9>[1776]
	""" Walking Dead (minion:3/2/5)
	<b>Taunt</b> If you discard this minion, summon it. """
	class Hand:
		events = Discard(SELF).on(Summon(CONTROLLER, 'RLK_532'))
	pass

if Lich_Scourge_Supplies:# 
	Lich_Warlock+=['RLK_533']
class RLK_533_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		Draw(CONTROLLER).trigger(self.source)
		Draw(CONTROLLER).trigger(self.source)
		Draw(CONTROLLER).trigger(self.source)
		for cd in self.player.hand:
			if cd.id==card.id:
				Discard(cd).trigger(self.source)
class RLK_533_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		if len(controller.deck)>=3 and len(controller.hand)<=7:
			cards=[card.id for card in controller.deck[-3:]]
			RLK_533_Choice(controller, RandomID(*cards)).trigger(source)
		pass
class RLK_533:# <9>[1776]
	""" Scourge Supplies (spell:3)
	Draw 3 cards. Choose one to discard. """
	play = RLK_533_Action()
	pass

if Lich_Soul_Barrage:# 
	Lich_Warlock+=['RLK_534']
class RLK_534:# <9>[1776]
	""" Soul Barrage (spell:5)
	When you play or discard this, deal $6 damage randomly split among all enemies. """
	play = SplitHit(CONTROLLER, ENEMY_CHARACTERS, 6)
	events =Discard(SELF).on(SplitHit(CONTROLLER, ENEMY_CHARACTERS, 6))
	pass

if Lich_Savage_Ymirjar:# 
	Lich_Warlock+=['RLK_535']
class RLK_535:# <9>[1776]
	""" Savage Ymirjar (minion:5/7/7)
	<b>Rush</b> <b>Battlecry:</b> Discard 2 cards. """
	play = Discard(RANDOM(FRIENDLY_HAND)), Discard(RANDOM(FRIENDLY_HAND))
	pass

if Lich_Shallow_Grave:# 
	Lich_Warlock+=['RLK_536']
class RLK_536:# <9>[1776]
	""" Shallow Grave (spell:2)
	Trigger a friendly minion's <b>Deathrattle</b>, then destroy it. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_DEATHRATTLE:0 }
	play = Destroy(TARGET)
	pass

if Lich_Twisted_Tether:# 
	Lich_Warlock+=['RLK_537']
	Lich_Warlock+=['RLK_537e']
class RLK_537_Action(TargetedAction):# 
	def do(self, source, target):# 
		controller=source.controller
		atk=target.atk
		hth=target.max_health
		Destroy(target).trigger(source)
		cards=[card for card in controller.hand if card.MINION_RACE(Race.UNDEAD)]
		if len(cards):
			card = random.choice(cards)
			Buff(card, 'RLK_537e', atk=atk, max_health=hth).trigger(source)
		pass
class RLK_537:# <9>[1776]
	""" Twisted Tether (spell:4)
	Destroy a minion. Give its stats to a random Undead in your hand. """
	requirements = REQUIRE_ENEMY_MINION_TARGET
	play = RLK_537_Action(TARGET)
	pass
class RLK_537e:# <9>[1776]
	""" Twisted Tether (0)
	Increased stats. """
	pass

if Lich_Devourer_of_Souls:# 
	Lich_Warlock+=['RLK_538']
	Lich_Warlock+=['RLK_538e']
class RLK_538_Action(TargetedAction):# 
	def do(self, source, target):# 
		controller=source.controller
		controller.sidequest_list0=target.deathrattles
		pass
class RLK_538:# <9>[1776]
	""" Devourer of Souls (minion:1/1/3)
	After a friendly minion dies, gain its <b>Deathrattle</b>. """
	events = Death(FRIENDLY + MINION).after(RLK_538_Action(Death.ENTITY))
	pass
class RLK_538e_Action(GameAction):# 
	def do(self, source):# 
		owner=self.owner
		actions= owner.sidequest_list0
		for action in actions:
			action.trigger(owner)
		pass
class RLK_538e:# <9>[1776]
	""" Devoured Soul (0)
	Copied <b>Deathrattle</b> from {0}. """
	tags={GameTag.DEATHRATTLE:1, }
	deathrattle = RLK_538e_Action()
	pass

if Lich_DarKhan_Drathir:# 
	Lich_Warlock+=['RLK_539']
class RLK_539:# <9>[1776]
	""" Dar'Khan Drathir (minion:8/6/6)
	<b>Lifesteal</b> At the end of your turn, deal 6 damage to the enemy hero. """
	events = OWN_TURN_END.on(Hit(ENEMY_HERO, 6))
	pass

if Lich_Amorphous_Slime:# 
	Lich_Warlock+=['RLK_540']
	Lich_Warlock+=['RLK_540e']
class RLK_540_Action1(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		cards=[card for card in controller.hand if card.MINION_RACE(Race.UNDEAD)]
		if len(cards):
			card=random.choice(cards)
			source.sidequest_list0=[card]
			Discard(card).trigger(source)
		pass
class RLK_540_Action2(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		if len(source.sidequest_list0):
			card=source.sidequest_list0[0]
			Summon(controller, card.id).trigger(source)
		pass
class RLK_540:# <9>[1776]
	""" Amorphous Slime (minion:5/5/3)
	<b>Battlecry:</b> Discard a random Undead. <b>Deathrattle:</b> Summon a copy of it. """
	play = RLK_540_Action1()
	deathrattle = RLK_540_Action2()
	pass
class RLK_540e:# <9>[1776]
	""" Morphing (0)
	Discarded {0}. """
	#
	pass

