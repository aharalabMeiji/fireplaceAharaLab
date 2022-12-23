from telnetlib import GA
from ..utils import *

Lich_Shaman=[]

Lich_Rotgill=True
Lich_Blightblood_Berserker=True
Lich_Unliving_Champion=True
Lich_Prescience=True
Lich_Harkener_of_Dread=True
Lich_Deathweaver_Aura=True
Lich_Shadow_Suffusion=True
Lich_From_De_Other_Side=True
Lich_Scourge_Troll=True
Lich_Overlord_Drakuru=True


if Lich_Rotgill:# 
	Lich_Shaman+=['RLK_550']
	Lich_Shaman+=['RLK_550e']
	Lich_Shaman+=['RLK_550e2']
class RLK_550:# <8>[1776]
	""" Rotgill (minion:5/3/6)
	<b>Battlecry:</b> Give your other minions "<b>Deathrattle:</b> Give __your minions +1/+1." """
	play = Buff(FRIENDLY_MINIONS - SELF, 'RLK_550e')
	pass
class RLK_550e:# <8>[1776]
	""" Deathwatch (0)
	<b>Deathrattle:</b> Give your minions +1/+1. """
	tags = {GameTag.DEATHRATTLE:True, }
	deathrattle = Buff(FRIENDLY_MINIONS, 'RLK_550e2')
	pass
RLK_550e2=buff(1,1)
""" Deathsight (0)	+1/+1. """


if Lich_Blightblood_Berserker:# 
	Lich_Shaman+=['RLK_551']
class RLK_551_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_551:# <8>[1776]
	""" Blightblood Berserker (minion:8/3/8)
	<b>Taunt</b>, <b>Lifesteal</b>, <b>Reborn</b> <b>Deathrattle:</b> Deal 3 damage to a random enemy. """
	deathrattle = Hit(RANDOM(ENEMY_CHARACTERS), 3)
	pass


if Lich_Unliving_Champion:# 
	Lich_Shaman+=['RLK_552']
class RLK_552_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		cards = [card for card in controller.death_after_last_turn if card.type==CardType.MINION and card.race==Race.UNDEAD]
		if len(cards):
			Summon(controller, 'RLK_909t').trigger(source)
		pass
class RLK_552:# <8>[1776]
	""" Unliving Champion (minion:3/3/2)
	<b>Battlecry:</b> If a friendly Undead died after your last turn, summon two 3/2 Zombies(RLK_909t). """
	play = RLK_552_Action()
	pass


if Lich_Prescience:# 
	Lich_Shaman+=['RLK_553']
	Lich_Shaman+=['RLK_553t']
class RLK_553_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		card1=get00(Draw(controller).trigger(source))
		card2=get00(Draw(controller).trigger(source))
		if card1.cost>=5:
			Summon(controller, 'RLK_553t').trigger(source)
		if card2.cost>=5:
			Summon(controller, 'RLK_553t').trigger(source)
		pass
class RLK_553:# <8>[1776]
	""" Prescience (spell:4)
	Draw 2 minions. For each that costs (5) or more, summon a_ 2/3 Spirit(RLK_553t) with <b>Taunt</b>. """
	play = RLK_553_Action()
	pass
class RLK_553t:# <8>[1776]
	""" Ghastly Apparition (minion:2/2/3)
	<b>Taunt</b> """
	#
	pass

if Lich_Harkener_of_Dread:# 
	Lich_Shaman+=['RLK_554']
	Lich_Shaman+=['RLK_554t']
class RLK_554:# <8>[1776]
	""" Harkener of Dread (minion:5/2/2)
	<b>Taunt</b> <b>Deathrattle:</b> Summon a 6/6 Undead with <b>Taunt</b>. """
	deathrattle = Summon(CONTROLLER, 'RLK_554t')
	pass
class RLK_554t:# <8>[1776]
	""" Drakkari Specter (minion:6/6/6)
	<b>Taunt</b> """
	pass


if Lich_Deathweaver_Aura:# 
	Lich_Shaman+=['RLK_909']
	Lich_Shaman+=['RLK_909e']
	Lich_Shaman+=['RLK_909t']
class RLK_909_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_909:# <8>[1776]
	""" Deathweaver Aura (spell:2)
	Give a minion "<b>Deathrattle:</b> Summon two 3/2 Zombies." <b>Overload:</b> (1) """
	#<Tag enumID="215" name="OVERLOAD" type="Int" value="1"/>
	requirements = REQUIRE_FRIEND_MINION_TARGET
	play = Buff(TARGET, 'RLK_909e')
	pass
class RLK_909e:# <8>[1776]
	""" Voodoo Be With You (0)
	<b>Deathrattle:</b> Summon two 3/2 Zombies. """
	tags = {GameTag.DEATHRATTLE:True, }
	deathrattle = Summon(CONTROLLER, 'RLK_909t'), Summon(CONTROLLER, 'RLK_909t')
	pass
class RLK_909t:# <8>[1776]
	""" Drakkari Zombie (minion:2/3/2)
	 """
	pass


if Lich_Shadow_Suffusion:# 
	Lich_Shaman+=['RLK_910']
class RLK_910_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_910:# <8>[1776]
	""" Shadow Suffusion (spell:3)
	Give your minions "<b>Deathrattle:</b> Deal 3 damage to a random enemy." """
	#
	pass

	Lich_Shaman+=['RLK_910e']
class RLK_910e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_910e:# <8>[1776]
	""" Mojo Missile (0)
	<b>Deathrattle:</b> Deal 3 damage to a random enemy. """
	#
	pass

if Lich_From_De_Other_Side:# 
	Lich_Shaman+=['RLK_911']
class RLK_911_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_911:# <8>[1776]
	""" From De Other Side (spell:10)
	Summon a copy of each minion in your hand. They attack random enemy minions, then die. """
	#
	pass

if Lich_Scourge_Troll:# 
	Lich_Shaman+=['RLK_912']
class RLK_912_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_912:# <8>[1776]
	""" Scourge Troll (minion:1/1/3)
	<b>Deathrattles</b> given to this minion trigger twice. """
	#
	pass

if Lich_Overlord_Drakuru:# 
	Lich_Shaman+=['RLK_913']
class RLK_913_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_913:# <8>[1776]
	""" Overlord Drakuru (minion:9/6/8)
	<b>Rush</b>, <b>Windfury</b> After this attacks and kills a minion, resurrect it on your side. """
	#
	pass

