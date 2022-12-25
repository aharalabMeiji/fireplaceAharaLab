from ..utils import *

Lich_Warrior=[]

Lich_Sunfire_Smithing=True
Lich_Last_Stand=True
Lich_Silverfury_Stalwart=True
Lich_Light_of_the_Phoenix=True
Lich_Thoribelore=True
Lich_Blazing_Power=True
Lich_Disruptive_Spellbreaker=True
Lich_Asvedon_the_Grandshield=True
Lich_Sunfury_Champion=True
Lich_Embers_of_Strength=True


if Lich_Sunfire_Smithing:# 
	Lich_Warrior+=['RLK_600']
	Lich_Warrior+=['RLK_600e']
	Lich_Warrior+=['RLK_600t']
class RLK_600:# <10>[1776]
	""" Sunfire Smithing (spell:4)
	Equip a 4/2 Sword. Give a random minion in your hand +4/+2. """
	play = Summon(CONTROLLER, 'RLK_600t'), Buff(RANDOM(FRIENDLY_HAND), 'RLK_600e')
	pass
RLK_600e=buff(4,2)
class RLK_600t:# <10>[1776]
	""" Flamberge (weapon: 4/4/0)
	 """
	#
	pass

if Lich_Last_Stand:# 
	Lich_Warrior+=['RLK_601']
	Lich_Warrior+=['RLK_601e']
class RLK_601_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		cards = [card for card in controller.deck if card.type==CardType.MINION and card.taunt==True]
		if len(cards):
			card = random.choice(cards)
			card.zone=Zone.HAND
			atk=card.atk
			hth=card.max_health
			Buff(card, 'RLK_601e', atk=atk, max_health=hth).trigger(source)
		pass
class RLK_601:# <10>[1776]
	""" Last Stand (spell:4)
	Draw a <b>Taunt</b> minion. Double its stats. """
	play = RLK_601_Action()
	pass
class RLK_601e:# <10>[1776]
	""" Stalwart Stand (0)
	Stats Doubled. """
	pass

if Lich_Silverfury_Stalwart:# 
	Lich_Warrior+=['RLK_602']
class RLK_602:# <10>[1776]
	""" Silverfury Stalwart (minion:6/4/8)
	<b><b>Taunt</b>, Rush</b> Can't be targeted by spells or Hero Powers. """
	tags={GameTag.CANT_BE_TARGETED_BY_HERO_POWERS:0, GameTag.CANT_BE_TARGETED_BY_SPELLS:0 }
	pass

if Lich_Light_of_the_Phoenix:# 
	Lich_Warrior+=['RLK_603']
class RLK_603_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		card1=get00(Draw(controller).trigger(source))
		card2=get00(Draw(controller).trigger(source))
		amount=len([card for card in controller.field if card.type==CardType.MINION and card.damage>0])
		card1._cost=max(card1._cost-amount, 0)
		card2._cost=max(card2._cost-amount, 0)
		pass
class RLK_603:# <10>[1776]
	""" Light of the Phoenix (spell:4)
	Draw 2 cards. Costs (1) less for each damaged friendly character. """
	play = RLK_603_Action()
	pass

if Lich_Thoribelore:# 
	Lich_Warrior+=['RLK_604']
	Lich_Warrior+=['RLK_604a']
	Lich_Warrior+=['RLK_604b']
	Lich_Warrior+=['RLK_604t']
	Lich_Warrior+=['RLK_604t2']
class RLK_604:# <10>[1776]
	""" Thori'belore (minion:4/4/4)
	<b>Rush</b>. <b>Deathrattle:</b> Go <b>Dormant</b>. Cast a Fire spell to revive Thori'belore! <i>(Revives 2 times.)</i> """
	deathrattle = Summon(CONTROLLER, 'RLK_604t')
	pass
class RLK_604a:# <10>[1776]
	""" Thori'belore (minion:4/4/4)
	<b>Rush</b>. <b>Deathrattle:</b> Go <b>Dormant</b>. Cast a Fire spell to revive Thori'belore! <i>(Revives once.)</i> """
	deathrattle = Summon(CONTROLLER, 'RLK_604t2')
	pass
class RLK_604b:# <10>[1776]
	""" Thori'belore (minion:4/4/4)
	<b>Rush</b> """
	pass
class RLK_604t:# <10>[1776]
	""" Phoenix Egg (minion:21/0/1)
	<b>Dormant</b> Cast a Fire spell to revive Thori'belore! """
	dormant = -1
	events = Play(CONTROLLER, SPELL + FIRE).on(Morph(SELF, 'RLK_604a'))
	pass
class RLK_604t2:# <10>[1776]
	""" Phoenix Egg (minion:21/0/1)
	<b>Dormant</b> Cast a Fire spell to revive Thori'belore! """
	dormant = -1
	events = Play(CONTROLLER, SPELL + FIRE).on(Morph(SELF, 'RLK_604b'))
	pass

if Lich_Blazing_Power:# 
	Lich_Warrior+=['RLK_605']
	Lich_Warrior+=['RLK_605e']
class RLK_605:# <10>[1776]
	""" Blazing Power (spell:2)
	Give a minion +1/+1. Repeat for each damaged friendly character. """
	requirements = REQUIRE_FRIEND_MINION_TARGET
	play = Buff(TARGET, 'RLK_605e') * Count(FRIENDLY + MINION + DAMAGED)
	pass
RLK_605e=buff(1,1)

if Lich_Disruptive_Spellbreaker:# 
	Lich_Warrior+=['RLK_607']
	Lich_Warrior+=['RLK_607e']
class RLK_607:# <10>[1776]
	""" Disruptive Spellbreaker (minion:5/4/5)
	At the end of your turn, your opponent discards a spell. """
	events = OWN_TURN_END.on(Destroy(RANDOM(ENEMY_HAND + SPELL)))
	pass
class RLK_607e:# <10>[1776]
	""" Broken Spell (0)
	Storing {0}. """
	pass

if Lich_Asvedon_the_Grandshield:# 
	Lich_Warrior+=['RLK_608']
class RLK_608_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		cards=[card.id for card in controller.opponent.play_log if card.type==CardType.SPELL]
		if len(cards):
			newcard=controller.card(cards[-1])
			CastSpell(newcard).trigger(source)
		pass
class RLK_608:# <10>[1776]
	""" Asvedon, the Grandshield (minion:3/3/3)
	<b>Battlecry:</b> Cast a copy of the last spell your opponent played. """
	play = RLK_608_Action()
	pass

if Lich_Sunfury_Champion:# 
	Lich_Warrior+=['RLK_609']
class RLK_609:# <10>[1776]
	""" Sunfury Champion (minion:1/1/3)
	After you cast a Fire spell, deal 1 damage to all minions. """
	events = Play(CONTROLLER, SPELL + FIRE).after(Hit(ALL_MINIONS, 1))
	pass

if Lich_Embers_of_Strength:# 
	Lich_Warrior+=['RLK_960']
	Lich_Warrior+=['RLK_960e']
	Lich_Warrior+=['RLK_960t']
class RLK_960_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		newcard=get00(Summon(controller, 'RLK_960t').trigger(source))
		Buff(newcard, 'RLK_960e').trigger(source)
		pass
class RLK_960:# <10>[1776]
	""" Embers of Strength (spell:2)
	Summon two 1/2 Guards with <b>Taunt</b>. <b>Manathirst (6):</b> Give them +1/+2. """
	play = Manathirst(6, [Summon(CONTROLLER, 'RLK_960t')], [RLK_960_Action()])
	pass
RLK_960e=buff(1,2)
""" Empowered Embers (0)	+1/+2. """
class RLK_960t:# <10>[1776]
	""" Emberbound Guard (minion:1/1/2)
	<b>Taunt</b> """
	pass

