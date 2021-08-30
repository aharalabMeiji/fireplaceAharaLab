from ..utils import *

class DREAM_01:# <11> 3 
	""" Laughing Sister
	Can't be targeted by spells or Hero Powers.
		<Tag enumID="311" name="CANT_BE_TARGETED_BY_SPELLS" type="Int" value="1"/>
		<Tag enumID="332" name="CANT_BE_TARGETED_BY_HERO_POWERS" type="Int" value="1"/>
	"""
	pass

class DREAM_02:# <11> 3 
	"""Ysera Awakens
	Deal $5 damage to all minions except Ysera.
	"""
	play = Hit(ALL_MINIONS - ID("EX1_572"), 5)
	pass

class DREAM_03:# <11> 3 
	""" Emerald Drake
	vanilla
	"""
	pass

class DREAM_04:# <11> 3 
	""" Dream
	Return an enemy minion to your opponent's hand.
	"""
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0, PlayReq.REQ_ENEMY_TARGET:0}
	play = Bounce(TARGET)
	pass

class DREAM_05: # <11> 3 
	""" Nightmare
	Give a minion +4/+4. At the start of your next turn, destroy it.
	"""
	requirements={		
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0
		}
	play = (Buff(TARGET,"DREAM_05e"), Buff(TARGET,"WC_035e2"))
	
	pass

class DREAM_05e:#=buff(atk=4, health=4) # <12> 3
	events = OWN_TURN_BEGIN.on(Destroy(OWNER), Destroy(SELF))
WC_035e2=buff(atk=4,health=4)#借りてきた


