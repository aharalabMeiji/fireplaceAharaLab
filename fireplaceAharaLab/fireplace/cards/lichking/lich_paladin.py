from pickle import TRUE
from ..utils import *

Lich_Paladin=[]

Lich_Timewarden=True
Lich_Daring_Drake=True
Lich_Flight_of_the_Bronze=True
Lich_For_QuelThalas=True
Lich_Anachronos=False#  difficult
Lich_Sanguine_Soldier=True
Lich_Seal_of_Blood=True
Lich_Feast_and_Famine=True
Lich_Blood_Matriarch_Liadrin=True
Lich_Blood_Crusader=True



if Lich_Timewarden:# 
	Lich_Paladin+=['RLK_527']
	Lich_Paladin+=['RLK_527e2']
class RLK_527:# <5>[1776]
	""" Timewarden (minion:4/3/5)
	<b>Battlecry:</b> Until the end of your next turn, Dragons you summon gain <b>Taunt</b> and <b>Divine Shield</b>. """
	play = Buff(FRIENDLY_MINIONS + DRAGON, 'RLK_527e2')
	pass
class RLK_527e2_Action(TargetedAction):# 
	def do(self, source, target):# 
		target.divine_shield=False
		target.taunt=False
		pass
class RLK_527e2:# <5>[1776]
	""" From the Future (0)
	Has <b>Divine Shield</b> and <b>Taunt</b>. """
	def apply(self, target):
		target.divine_shield=True
		target.taunt=True
		pass
	events = OWN_TURN_BEGIN.on(RLK_527e2_Action(OWNER), Destroy(SELF))

if Lich_Daring_Drake:# 
	Lich_Paladin+=['RLK_916']
	Lich_Paladin+=['RLK_916e']
class RLK_916:# <5>[1776]
	""" Daring Drake (minion:4/4/4)
	<b>Rush</b> <b>Battlecry:</b> If you're holding a Dragon, gain +1/+1. """
	play = Find(FRIENDLY_MINIONS + DRAGON) & Buff(SELF, 'RLK_916e')
	pass
RLK_916e=buff(1,1)


if Lich_Flight_of_the_Bronze:# 
	Lich_Paladin+=['RLK_917']
	Lich_Paladin+=['RLK_917t']
class RLK_917:# <5>[1776]
	""" Flight of the Bronze (spell:1)
	<b>Discover</b> a Dragon. <b>Manathirst (7):</b> Summon a 5/5 Drake with <b>Taunt</b>. """
	play = Manathirst(7, [Summon(CONTROLLER, 'RLK_917t')], []), Discover(CONTROLLER, RandomDragon())
	pass
class RLK_917t:# <5>[1776]
	""" Bronze Defender (minion:5/5/5)
	<b>Taunt</b> """
	#
	pass

if Lich_For_QuelThalas:# 
	Lich_Paladin+=['RLK_918']
	Lich_Paladin+=['RLK_918e']
	Lich_Paladin+=['RLK_918e2']
class RLK_918:# <5>[1776]
	""" For Quel'Thalas! (spell:2)
	Give a friendly minion +3 Attack. Give your hero +2 Attack this turn. """
	play = Buff(TARGET, 'RLK_918e'), Buff(FRIENDLY_HERO, 'RLK_918e2')
	pass
RLK_918e=buff(3,0)
RLK_918e2=buff(2,0)


if Lich_Anachronos:# 
	Lich_Paladin+=['RLK_919']
	Lich_Paladin+=['RLK_919e']
class RLK_919_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_919:# <5>[1776]
	""" Anachronos (minion:7/8/8)
	<b>Battlecry:</b> Send all other minions 2 turns into the future. """
	#
	pass
class RLK_919e_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_919e:# <5>[1776]
	""" Time Travel (0)
	Sending a minion 2 turns into the future. """
	#
	pass

if Lich_Sanguine_Soldier:# 
	Lich_Paladin+=['RLK_921']
class RLK_921:# <5>[1776]
	""" Sanguine Soldier (minion:1/2/1)
	<b>Divine Shield</b>  <b>Battlecry:</b> Deal 2 damage to your hero. """
	play = Hit(FRIENDLY_HERO, 2)
	pass

if Lich_Seal_of_Blood:# 
	Lich_Paladin+=['RLK_922']
	Lich_Paladin+=['RLK_922e']
class RLK_922:# <5>[1776]
	""" Seal of Blood (spell:3)
	Give a minion +3/+3 and <b>Divine Shield</b>. Deal $3 damage to your hero. """
	requirements = REQUIRE_FRIEND_MINION_TARGET
	play = Buff(TARGET, 'RLK_922e'), Hit(FRIENDLY_HERO, 2)
	pass
RLK_922e=buff(divine_shield=True)


if Lich_Feast_and_Famine:# 
	Lich_Paladin+=['RLK_923']
	Lich_Paladin+=['RLK_923e1']
	Lich_Paladin+=['RLK_923e3']
class RLK_923:# <5>[1776]
	""" Feast and Famine (spell:1)
	Give your hero +3 Attack this turn. <b>Manathirst (4):</b> And <b>Lifesteal</b>. """
	play = Buff(FRIENDLY_HERO, 'RLK_923e1'), Manathirst(4, [Buff(FRIENDLY_HERO, 'RLK_923e3')], [])
	pass
RLK_923e1=buff(3,0)#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>
RLK_923e3=buff(lifesteal=True)#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>



if Lich_Blood_Matriarch_Liadrin:# 
	Lich_Paladin+=['RLK_924']
	Lich_Paladin+=['RLK_924e']
class RLK_924_Action(TargetedAction):# 
	def do(self, source, target):# 
		controller=source.controller
		if target.atk < source.atk:
			Buff(target, 'RLK_924e').trigger(source)
		pass
class RLK_924:# <5>[1776]
	""" Blood Matriarch Liadrin (minion:2/3/2)
	After you summon a minion with less Attack than this, give it <b>Divine Shield</b> and <b>Rush</b>. """
	events = Summon(CONTROLLER, MINION).after(RLK_924_Action(Summon.CARD))
	pass
RLK_924e=buff(rush=True, divine_shield=True)


if Lich_Blood_Crusader:# 
	Lich_Paladin+=['RLK_927']
	Lich_Paladin+=['RLK_927e']
class RLK_927:# <5>[1776]
	""" Blood Crusader (minion:6/5/5)
	<b>Battlecry:</b> Your next Paladin minion this turn costs  Health instead of Mana. """
	play = Buff(FRIENDLY_HAND+PALADIN, 'RLK_927e')
	pass
class RLK_927e:# <5>[1776]
	""" Crusade (0)
	Costs Health instead of Mana. """
	#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>
	def apply(self, target):
		target.card_costs_health = True
	pass



