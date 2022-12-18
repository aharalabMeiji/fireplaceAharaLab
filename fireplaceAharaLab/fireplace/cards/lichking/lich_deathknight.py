from ..utils import *

Lich_DeathKnight=[]


Lich_Soulbreaker=True
Lich_Corpse_Explosion=True
Lich_Vampiric_Blood=True
Lich_Necrotic_Mortician=True
Lich_Meat_Grinder=True
Lich_Acolyte_of_Death=True
Lich_Blightfang=True
Lich_Boneguard_Commander=True
Lich_Alexandros_Mograine=True
Lich_Soulstealer=True


if Lich_Soulbreaker:# 
	Lich_DeathKnight+=['RLK_012']
class RLK_012_Action(TargetedAction):# 
	def do(self, source, target):#
		#source.game.process_deaths()
		if target.dead:
			AddCorpse(CONTROLLER, 2).trigger(source)
		pass
class RLK_012:# <1>[1776]
	""" Soulbreaker (3)
	After your hero attacks and kills a minion, gain 2 <b>Corpses</b>. """
	events = Attack(FRIENDLY_HERO).after(RLK_012_Action(Attack.DEFENDER))
	pass

#class RLK_025e_Action(GameAction):# 
#	def do(self, source):# 
#		pass
#class RLK_025e:# <1>[1776]
#	""" Glacial Advance (0)
#	The next spell you cast this turn costs (2) less. """
#	#
#	pass

#class RLK_025o_Action(GameAction):# 
#	def do(self, source):# 
#		pass
#class RLK_025o:# <1>[1776]
#	""" Glacial Advance (0)
#	The next spell you cast this turn costs (2) less. """
#	#
#	pass

if Lich_Corpse_Explosion:# 
	Lich_DeathKnight+=['RLK_035']
class RLK_035_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		if controller.corpse>=1:
			SpendCorpse(controller, 1).trigger(source)
			for repeat in range(10):
				for card in controller.field+controller.opponent.field:
					Hit(card, 1).trigger(source)
				if len([card for card in controller.field+controller.opponent.field if card.dead==True])>0:
					controller.game.process_deaths()
					break
				controller.game.process_deaths()
		pass
class RLK_035:# <1>[1776]
	""" Corpse Explosion (spell:5)
	Detonate a <b>Corpse</b> to deal $1 damage to all minions. If any are still alive, repeat this. """
	play = RLK_035_Action()
	pass

if Lich_Vampiric_Blood:# 
	Lich_DeathKnight+=['RLK_051']
class RLK_051_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		Heal(controller.hero, 5).trigger(source)
		if controller.corpse>=3:
			SpendCorpse(controller, 3).trigger(source)
			Heal(controller.hero, 5).trigger(source)
			Draw(controller).trigger(source)
		pass
class RLK_051:# <1>[1776]
	""" Vampiric Blood (spell:2)
	Give your hero +5 Health. Spend 3 <b>Corpses</b> to gain 5 more and draw a card. """
	play = RLK_051_Action()
	pass

#class RLK_066e_Action(GameAction):# 
#	def do(self, source):# 
#		pass
#class RLK_066e:# <1>[1776]
#	""" Winter's Gift (0)
#	Increased Health. """
#	#
#	pass

#class RLK_085e_Action(GameAction):# 
#	def do(self, source):# 
#		pass
#class RLK_085e:# <1>[1776]
#	""" Bonestorm (0)
#	+2/+2. """
#	#
#	pass

if Lich_Necrotic_Mortician:# 
	Lich_DeathKnight+=['RLK_116']
class RLK_116_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		cards=[card for card in controller.death_after_last_turn if card.type==CardType.MINION and card.race==Race.UNDEAD]
		if len(cards)>0:
			Discover(controller, RandomUnholyRune()).trigger(source)
		pass
class RLK_116:# <1>[1776]
	""" Necrotic Mortician (minion:2/2/3)
	<b>Battlecry:</b> If a friendly Undead died after your last turn, <b>Discover</b> an Unholy Rune card. """
	play = RLK_116_Action()
	pass

if Lich_Meat_Grinder:# 
	Lich_DeathKnight+=['RLK_120']
class RLK_120_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		if len(controller.deck):
			card=random.choice(controller.deck)
			card.discard()#card.zone=Zone.GRAVEYARD
			AddCorpse(controller, 3).trigger(source)
		pass
class RLK_120:# <1>[1776]
	""" Meat Grinder (minion:3/3/4)
	<b>Battlecry:</b> Shred a random minion in your deck to gain 3 <b>Corpses.</b> """
	play = RLK_120_Action()
	pass

if Lich_Acolyte_of_Death:# 
	Lich_DeathKnight+=['RLK_121']
class RLK_121_Action(GameAction):# 
	def do(self, source):# 
		pass
class RLK_121:# <1>[1776]
	""" Acolyte of Death (minion:3/3/4)
	After a friendly Undead dies, draw a card. """
	events = Death(FRIENDLY + MINION + UNDEAD).after(Draw(CONTROLLER))
	pass

if Lich_Blightfang:# 
	Lich_DeathKnight+=['RLK_225']
	Lich_DeathKnight+=['RLK_225e']
class RLK_225_Action(GameAction):# 
	def do(self, source):# 
		pass
class RLK_225:# <1>[1776]
	""" Blightfang (minion:3/3/3)
	<b>Battlecry:</b> Infect all enemy minions. When they die, you summon a 2/2 Zombie with <b>Taunt</b>. """
	play = Buff(ENEMY_MINIONS, 'RLK_225e')
	pass
class RLK_225e:# <1>[1776]
	""" Plagued (0)
	<b>Deathrattle:</b> Summon a 2/2 Zombie with <b>Taunt</b> for your opponent. """
	tags={GameTag.DEATHRATTLE:True, }
	deathrattle = Summon(OPPONENT, 'RLK_118t3')
	pass

if Lich_Boneguard_Commander:# 
	Lich_DeathKnight+=['RLK_506','RLK_061t']
class RLK_506_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		amount=min(6,controller.corpse)
		if amount+len(controller.field)>7:
			amount=7-len(controller.field)
		SpendCorpse(controller, amount).trigger(source)
		for count in range(amount):
			Summon(controller, 'RLK_061t').trigger(source)
		pass
class RLK_506:# <1>[1776]
	""" Boneguard Commander (minion:8/8/8)
	<b>Taunt</b> <b>Battlecry:</b> Raise up to 6 <b>Corpses</b> as 1/2 Risen Footmen(RLK_061t) with <b>Taunt</b>. """
	play = RLK_506_Action()
	pass
class RLK_061t:
	""" Risen Footmen
	&lt;b&gt;Taunt&lt;/b&gt; &lt;i&gt;Doesn't leave a &lt;b&gt;Corpse&lt;/b&gt;.&lt;/i&gt;"""
	# this is not collectible.
	# implementation in class Death.


if Lich_Alexandros_Mograine:# 
	Lich_DeathKnight+=['RLK_706']
	Lich_DeathKnight+=['RLK_706e3']
class RLK_706:# <1>[1776]
	""" Alexandros Mograine (minion:7/7/7)
	<b>Battlecry:</b> For the rest of the game, deal 3 damage to your opponent at the end of your turns. """
	play = Buff(CONTROLLER, 'RLK_706e3')
	pass
class RLK_706e3:# <1>[1776]
	""" Mograine's Migraine (0)
	For the rest of the game, deal 3 damage to your opponent at the end of your turns. """
	events = OWN_TURN_END.on(Hit(RANDOM(ENEMY_CHARACTERS), 3))
	pass

#class RLK_707e_Action(GameAction):# 
#	def do(self, source):# 
#		pass
#class RLK_707e:# <1>[1776]
#	""" Grave Mark (0)
#	+1 Attack. """
#	#
#	pass

#class RLK_707e2_Action(GameAction):# 
#	def do(self, source):# 
#		pass
#class RLK_707e2:# <1>[1776]
#	""" Grave Force (0)
#	+3 Attack. """
#	#
#	pass

#class RLK_715e_Action(GameAction):# 
#	def do(self, source):# 
#		pass
#class RLK_715e:# <1>[1776]
#	""" Runeforged (0)
#	Costs (1) less. """
#	#
#	pass

if Lich_Soulstealer:# 
	Lich_DeathKnight+=['RLK_741']
class RLK_741_Action(GameAction):# 
	def do(self, source):# 
		pass
class RLK_741:# <1>[1776]
	""" Soulstealer (minion:8/5/5)
	<b>Battlecry:</b> Destroy all other minions. Gain 1 <b>Corpse</b> for each enemy destroyed. """
	play = AddCorpse(CONTROLLER, Count(ENEMY_MINIONS)) ,Destroy(ALL_MINIONS-SELF)
	pass

#class RLK_753e_Action(GameAction):# 
#	def do(self, source):# 
#		pass
#class RLK_753e:# <1>[1776]
#	""" Dug Up (0)
#	+1/+2. """
#	#
#	pass

#class RLK_958e_Action(GameAction):# 
#	def do(self, source):# 
#		pass
#class RLK_958e:# <1>[1776]
#	""" Thrown a Bone (0)
#	+2 Attack. """
#	#
#	pass

