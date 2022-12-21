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
		cards = [card.id for card in controller.death_log if card.type==CardType.MINION and card.race==Race.UNDEAD]
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
	events = [
		Discard(SELF).on(Summon(CONTROLLER, 'RLK_532'))
	]
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
			RLK_533_Choice(controller, RandomID(*cards)).trigger()
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
	events = [
		Play(CONTROLLER, SELF).on(SplitHit(CONTROLLER, ENEMY_CHARACTERS, 6)),
		Discard(SELF).on(SplitHit(CONTROLLER, ENEMY_CHARACTERS, 6))
		]
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
class RLK_536_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller

		pass
class RLK_536:# <9>[1776]
	""" Shallow Grave (spell:2)
	Trigger a friendly minion's <b>Deathrattle</b>, then destroy it. """
	#
	pass

if Lich_Twisted_Tether:# 
	Lich_Warlock+=['RLK_537']
class RLK_537_Action(TargetedAction):# 
	def do(self, source, target):# 
		controller=source.controller
		atk=target.atk
		hth=target.max_health
		Destroy(target).trigger(source)

		pass
class RLK_537:# <9>[1776]
	""" Twisted Tether (spell:4)
	Destroy a minion. Give its stats to a random Undead in your hand. """
	requirements = REQUIRE_ENEMY_MINION_TARGET
	play = RLK_537_Action(TARGET)
	#
	pass

	Lich_Warlock+=['RLK_537e']
class RLK_537e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_537e:# <9>[1776]
	""" Twisted Tether (0)
	Increased stats. """
	#
	pass

if Lich_Devourer_of_Souls:# 
	Lich_Warlock+=['RLK_538']
class RLK_538_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_538:# <9>[1776]
	""" Devourer of Souls (minion:1/1/3)
	After a friendly minion dies, gain its <b>Deathrattle</b>. """
	#
	pass

	Lich_Warlock+=['RLK_538e']
class RLK_538e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_538e:# <9>[1776]
	""" Devoured Soul (0)
	Copied <b>Deathrattle</b> from {0}. """
	#
	pass

if Lich_DarKhan_Drathir:# 
	Lich_Warlock+=['RLK_539']
class RLK_539_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_539:# <9>[1776]
	""" Dar'Khan Drathir (minion:8/6/6)
	<b>Lifesteal</b> At the end of your turn, deal 6 damage to the enemy hero. """
	#
	pass

if Lich_Amorphous_Slime:# 
	Lich_Warlock+=['RLK_540']
class RLK_540_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_540:# <9>[1776]
	""" Amorphous Slime (minion:5/5/3)
	<b>Battlecry:</b> Discard a random Undead. <b>Deathrattle:</b> Summon a copy of it. """
	#
	pass

	Lich_Warlock+=['RLK_540e']
class RLK_540e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_540e:# <9>[1776]
	""" Morphing (0)
	Discarded {0}. """
	#
	pass

