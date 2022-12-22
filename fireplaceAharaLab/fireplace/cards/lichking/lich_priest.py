from ..utils import *

Lich_Priest=[]

Lich_Animate_Dead=True
Lich_Bonecaller=True
Lich_Crystalsmith_Cultist=True
Lich_Shadow_Word_Undeath=True
Lich_Sister_Svalna=True
Lich_Haunting_Nightmare=True
Lich_Undying_Allies=True
Lich_Grave_Digging=True
Lich_High_Cultist_Basaleph=True
Lich_Mind_Eater=True


if Lich_Animate_Dead:# 
	Lich_Priest+=['RLK_812']
class RLK_812_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		cards=[card.id for card in controller.death_log if card.type==CardType.MINION and card.cost<=3 ]
		if len(cards):
			card=random.choice(cards)
			Summon(controller, card).trigger(source)
		pass
class RLK_812:# <6>[1776]
	""" Animate Dead (spell:1)
	Resurrect a friendly minion that costs (3) or less. """
	play = RLK_812_Action()
	pass

if Lich_Bonecaller:# 
	Lich_Priest+=['RLK_813']
class RLK_813_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		cards=[card.id for card in controller.death_log if card.type==CardType.MINION and card.race==Race.UNDEAD ]
		if len(cards):
			card=random.choice(cards)
			Summon(controller, card).trigger(source)
		pass
class RLK_813:# <6>[1776]
	""" Bonecaller (minion:4/2/4)
	<b>Taunt</b> <b>Deathrattle</b>: Resurrect a friendly Undead that died this game. """
	play = RLK_813_Action()
	pass

if Lich_Crystalsmith_Cultist:# 
	Lich_Priest+=['RLK_814']
	Lich_Priest+=['RLK_814e']
class RLK_814:# <6>[1776]
	""" Crystalsmith Cultist (minion:1/1/2)
	<b>Battlecry:</b> If you're holding a Shadow spell, gain +1/+1. """
	play = Find(FRIENDLY_HAND + SPELL + SHADOW) & Buff(SELF, 'RLK_814e')
	pass
RLK_814e=buff(1,1)
""" Shadow Flow (0)	+1/+1 """

if Lich_Shadow_Word_Undeath:# 
	Lich_Priest+=['RLK_815']
class RLK_815_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		cards=[card.id for card in controller.death_after_last_turn if card.type==CardType.MINION and card.race==Race.UNDEAD ]
		if len(cards):
			Hit(ENEMY_CHARACTERS, 2).trigger(source)
		pass
class RLK_815:# <6>[1776]
	""" Shadow Word: Undeath (spell:5)
	Deal $2 damage to all enemies. If a friendly Undead died after your last turn, deal $2 more. """
	play = Hit(ENEMY_CHARACTERS, 2), RLK_815_Action()
	pass

if Lich_Sister_Svalna:# 
	Lich_Priest+=['RLK_816']
	Lich_Priest+=['RLK_816t3']
class RLK_816:# <6>[1776]
	""" Sister Svalna (minion:6/6/6)
	<b>Battlecry:</b> <i>Permanently</i> add a Vision of Darkness(RLK_816t3) to your hand. """
	play = Give(CONTROLLER, 'RLK_816t3')
	pass
class RLK_816t3:# <6>[1776]
	""" Vision of Darkness (spell:3)
	<b>Discover</b> a Shadow spell. <i>(This stays in your hand.)</i> """
	play = Discover(CONTROLLER, RandomSpell()), Give(CONTROLLER, 'RLK_816')
	pass

if Lich_Haunting_Nightmare:# 
	Lich_Priest+=['RLK_822']
	Lich_Priest+=['RLK_822e']
	Lich_Priest+=['RLK_822e2']
	Lich_Priest+=['RLK_822t']
class RLK_822:# <6>[1776]
	""" Haunting Nightmare (minion:3/3/3)
	<b>Deathrattle:</b> Haunt a card in your hand. When you play it, summon a 3/3 Soldier. """
	deathrattle = Buff(RANDOM(FRIENDLY_HAND, 'RLK_822e'))
	pass
class RLK_822e:# <6>[1776]
	""" Cold Sweat (0)
	 """
	events = Play(CONTROLLER, OWNER).on(Summon(CONTROLLER, 'RLK_822t'), Destroy(SELF))
	pass
class RLK_822e2:# <6>[1776]
	""" Night Terror (0)
	Summons a 3/3 Soldier """
	pass
class RLK_822t:# <6>[1776]
	""" Haunted Soldier (minion:3/3/3)
	 """
	pass

if Lich_Undying_Allies:# 
	Lich_Priest+=['RLK_823']
	Lich_Priest+=['RLK_823e']
class RLK_823:# <6>[1776]
	""" Undying Allies (spell:0)
	After you play an Undead this turn, give it <b>Reborn</b>. """
	play = Buff(CONTROLLER, 'RLK_823e')
	pass

class RLK_823e_Action(TargetedAction):# 
	def do(self, source, target):# 
		controller=source.controller
		target.reborn=True
		pass
class RLK_823e:# <6>[1776]
	""" Grave Calling (0)
	After you play an Undead this turn, give it <b>Reborn</b>. """
	events = [
		Play(CONTROLLER, FRIENDLY + UNDEAD).after(RLK_823e_Action(Play.CARD))
	]
	#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>
	pass

if Lich_Grave_Digging:# 
	Lich_Priest+=['RLK_829']
class RLK_829_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		card1 = get00(Draw(controller).trigger(source))
		card2 = get00(Draw(controller).trigger(source))
		cards=[card.id for card in controller.death_after_last_turn if card.type==CardType.MINION and card.race==Race.UNDEAD ]
		if len(cards):
			card1._cost=1
			card2._cost=1
		pass
class RLK_829:# <6>[1776]
	""" Grave Digging (spell:4)
	Draw 2 cards. Costs (1) if a friendly Undead died after your last turn. """
	play = RLK_829_Action()
	pass

if Lich_High_Cultist_Basaleph:# 
	Lich_Priest+=['RLK_832']
class RLK_832_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		cards=[card.id for card in controller.death_after_last_turn if card.type==CardType.MINION and card.race==Race.UNDEAD ]
		if len(cards):
			for card in cards:
				Summon(controller, card).trigger(source)
		pass
class RLK_832:# <6>[1776]
	""" High Cultist Basaleph (minion:5/3/5)
	<b>Battlecry:</b> Resurrect all friendly Undead that died after your last turn. """
	play = RLK_832_Action()
	pass

if Lich_Mind_Eater:# 
	Lich_Priest+=['RLK_845']
class RLK_845_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		if len(controller.opponent.deck):
			card = random.choice(controller.opponent.deck)
			Give(controller, card.id).trigger(source)
		pass
class RLK_845:# <6>[1776]
	""" Mind Eater (minion:2/3/2)
	<b>Deathrattle:</b> Add a copy of a card in your opponent's deck to your hand. """
	deathrattle = RLK_845_Action()
	pass

