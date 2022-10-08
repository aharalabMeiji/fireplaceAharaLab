from ..utils import *

Rev_Hunter=[]

Rev_Shadehound=True
Rev_Motion_Denied=True
Rev_Defense_Attorney_Nathanos=True
Rev_Frenzied_Fangs=True
Rev_Stonebound_Gargon=True
Rev_Huntsman_Altimor=True
Rev_Batty_Guest=True
Rev_Spirit_Poacher=True
Rev_Wild_Spirits=True
Rev_Castle_Kennels=True
Rev_Aralon=True
Rev_Stag_Charge=True
Rev_Collateral_Damage=True
Rev_Aralon=True
Rev_Castle_Kennels=True


if Rev_Shadehound:# 
	Rev_Hunter+=['MAW_009']
	Rev_Hunter+=['MAW_009e']
	Rev_Hunter+=['MAW_009t']
class MAW_009:# <3>[1691]
	""" Shadehound
	Whenever this attacks, give your other Beasts +2/+2. 
	<b>Infuse (@ Beasts):</b> Gain <b>Rush</b>. """
	# @ = script_data_num_1 = 3
	events = Attack(SELF, ENEMY).after(Buff(FRIENDLY_MINIONS + BEAST, 'MAW_009e'))#
	class Hand:
		events = Death(FRIENDLY+MINION + BEAST).on(Infuse(CONTROLLER, 'MAW_009t'))
	class Deck:
		events = Death(FRIENDLY+MINION + BEAST).on(Infuse(CONTROLLER, 'MAW_009t', 1))
	pass
MAW_009e=buff(2,2)
class MAW_009t:# <3>[1691]
	""" Shadehound
	<b>Infused</b> <b>Rush</b>. Whenever this attacks, give your other Beasts +2/+2. """
	events = Attack(SELF, ENEMY).after(Buff(FRIENDLY_MINIONS + BEAST, 'MAW_009e'))#
	pass




if Rev_Motion_Denied:# 
	Rev_Hunter+=['MAW_010']
	Rev_Hunter+=['MAW_010t']
class c_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		pass
class MAW_010:# <3>[1691]
	""" Motion Denied
	<b>Secret:</b> After your opponent plays three cards in a turn, deal $6 damage to the enemy hero. """
	secret = 
	pass

class MAW_010t:# <3>[1691]
	""" Improved Motion Denied
	<b>Secret:</b> After your opponent plays three cards in a turn, deal $9 damage to the enemy hero. """
	#
	pass




if Rev_Defense_Attorney_Nathanos:# 
	Rev_Hunter+=['MAW_011']
class c_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		pass
class MAW_011:# <3>[1691]
	""" Defense Attorney Nathanos
	<b>Battlecry:</b> <b>Discover</b> a friendly <b>Deathrattle</b> minion that died this game. Trigger and gain its <b>Deathrattle</b>. """
	#
	pass

	Rev_Hunter+=['MAW_011e']
class MAW_011e:# <3>[1691]
	""" Defending Death
	Copied <b>Deathrattle</b> from {0}. """
	#
	pass




if Rev_Frenzied_Fangs:# 
	Rev_Hunter+=['REV_350']
	Rev_Hunter+=['REV_350e']
	Rev_Hunter+=['REV_350t']
	Rev_Hunter+=['REV_350t2']
class c_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		pass
class REV_350:# <3>[1691]
	""" Frenzied Fangs
	Summon two 2/1 Bats. <b>Infuse (@):</b> Give them +1/+2. """
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_350t2'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_350t2', 1))
	#
	pass

class REV_350e:# <3>[1691]
	""" Bloodthirsty
	+1/+2. """
	#
	pass

class REV_350t:# <3>[1691]
	""" Thirsty Bat
	 """
	#
	pass

class REV_350t2:# <3>[1691]
	""" Frenzied Fangs
	<b>Infused</b> Summon two 2/1 Bats. Give them +1/+2. """
	#
	pass




if Rev_Stonebound_Gargon:# 
	Rev_Hunter+=['REV_352']
	Rev_Hunter+=['REV_352t']
class REV_352:# <3>[1691]
	""" Stonebound Gargon
	<b>Rush</b> <b>Infuse (@):</b> Also damages the minions next to __whomever this attacks. """
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_352t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_352t', 1))
	pass

class REV_352t:# <3>[1691]
	""" Stonebound Gargon
	<b>Infused</b> <b>Rush</b>. Also damages the minions next to __whomever this attacks. """
	#
	pass





if Rev_Huntsman_Altimor:# 
	Rev_Hunter+=['REV_353']
	Rev_Hunter+=['REV_353t']
	Rev_Hunter+=['REV_353t2']
	Rev_Hunter+=['REV_353t3']
	Rev_Hunter+=['REV_353t4']
	Rev_Hunter+=['REV_353t4e']
	Rev_Hunter+=['REV_353t5']
class REV_353:# <3>[1691]
	""" Huntsman Altimor
	<b>Battlecry:</b> Summon a Gargon Companion. 
	<b>Infuse ({0}):</b> Summon another. _
	<b>Infuse ({1}):</b> And another! """
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_353t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_353t', 1))
	pass
class REV_353t:# <3>[1691]
	""" Huntsman Altimor
	<b>Infused</b> <b>Battlecry:</b> Summon 2  Gargon Companions.  _______
	<b>Infuse (@):</b> Summon all 3!___ """
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_353t2'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_353t2', 1))
	#
	pass

class REV_353t2:# <3>[1691]
	""" Huntsman Altimor
	<b>Infused</b> <b>Battlecry:</b> Summon all 3 Gargon Companions. """
	play=Summon(CONTROLLER, 'REV_353t3'),Summon(CONTROLLER, 'REV_353t4'),Summon(CONTROLLER, 'REV_353t5')
	pass

class REV_353t3:# <3>[1691] Gargon Companions
	""" Hecutis
	<b>Taunt</b> """
	#
	pass

class REV_353t4:# <3>[1691] Gargon Companions
	""" Barghast
	Your other minions have +1 Attack. """
	#
	pass

class REV_353t4e:# <3>[1691]
	""" Bone from the Stone
	Barghast is granting this minion +1 Attack. """
	#
	pass

class REV_353t5:# <3>[1691] Gargon Companions
	""" Margore
	<b>Charge</b> """
	#
	pass




if Rev_Batty_Guest:# 
	Rev_Hunter+=['REV_356']
class REV_356:# <3>[1691]
	""" Batty Guest
	<b>Deathrattle:</b> Summon a 2/1 Bat. """
	#
	pass




if Rev_Spirit_Poacher:# 
	Rev_Hunter+=['REV_360']
class c_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		pass
class REV_360:# <3>[1691]
	""" Spirit Poacher
	<b>Battlecry:</b> Summon a random <b>Dormant</b> Wildseed. """
	#
	pass

	Rev_Hunter+=['REV_360t']
class REV_360t:# <3>[1691]
	""" Fox Spirit Wildseed
	<b>Dormant</b> for 1 turn. <b>Rush</b> """
	#
	pass

	Rev_Hunter+=['REV_360t1']
class REV_360t1:# <3>[1691]
	""" Bear Spirit Wildseed
	<b>Dormant</b> for 2 turns. <b>Taunt</b> """
	#
	pass

	Rev_Hunter+=['REV_360t1e']
class REV_360t1e:# <3>[1691]
	""" Mature Wildseed
	<b>Dormant</b>. Awaken in @ |4(turn, turns). """
	#
	pass

	Rev_Hunter+=['REV_360t2']
class REV_360t2:# <3>[1691]
	""" Stag Spirit Wildseed
	<b>Dormant</b> for 3 turns.  When this awakens, equip a 3/2 Greatbow. """
	#
	pass

	Rev_Hunter+=['REV_360t2e']
class REV_360t2e:# <3>[1691]
	""" Elder Wildseed
	<b>Dormant</b>. Awaken in @ |4(turn, turns). """
	#
	pass

	Rev_Hunter+=['REV_360t4']
class REV_360t4:# <3>[1691]
	""" Stagpoint Wildbow
	 """
	#
	pass

	Rev_Hunter+=['REV_360te']
class REV_360te:# <3>[1691]
	""" Young Wildseed
	<b>Dormant</b>. Awaken in @ |4(turn, turns). """
	#
	pass




if Rev_Wild_Spirits:# 
	Rev_Hunter+=['REV_361']
class c_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		pass
class REV_361:# <3>[1691]
	""" Wild Spirits
	Summon two different  <b>Dormant</b> Wildseeds.  Make your Wildseeds  awaken 1 turn sooner. """
	#
	pass




if Rev_Castle_Kennels:# ### location ###
	Rev_Hunter+=['REV_362']
	Rev_Hunter+=['REV_362e']
	Rev_Hunter+=['REV_362e2']
class REV_362_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = source.controller
		Buff(target, 'REV_362e').trigger(source)
		if target.race==Race.BEAST:
			target.rush=True
		pass
class REV_362:# <3>[1691]
	""" Castle Kennels
	Give a friendly minion  +2 Attack. If it's a  Beast, give it <b>Rush</b>. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	location = REV_362_Action(TARGET)#
	pass
REV_362e=buff(2,0)
#class REV_362e2:# <3>[1691]
#	""" Resistant
#	<b>Immune</b> this turn. """
#	#
#	pass




if Rev_Aralon:# 
	Rev_Hunter+=['REV_363']
class c_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		pass
class REV_363:# <3>[1691]
	""" Ara'lon
	<b>Battlecry:</b> Summon one of each <b>Dormant</b> Wildseed. """
	#
	pass




if Rev_Stag_Charge:# 
	Rev_Hunter+=['REV_364']
class c_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		pass
class REV_364:# <3>[1691]
	""" Stag Charge
	Deal $3 damage. Summon a random <b>Dormant</b> Wildseed. """
	#
	pass




if Rev_Collateral_Damage:# 
	Rev_Hunter+=['REV_369']
class c_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		pass
class REV_369:# <3>[1691]
	""" Collateral Damage
	Deal $6 damage to three  random enemy minions.  Excess damage hits  the enemy hero. """
	#
	pass




#if Rev_Aralon:# 
#	Rev_Hunter+=['REV_780']
#class REV_780:# <3>[1691]
#	""" Ara'lon
#	{0} {1} {2} {3} """
#	#
#	pass

#if Rev_Castle_Kennels:# 
#	Rev_Hunter+=['REV_790']
#class REV_790:# <3>[1691]
#	""" Castle Kennels
#	{0} {1} """
#	#
#	pass

