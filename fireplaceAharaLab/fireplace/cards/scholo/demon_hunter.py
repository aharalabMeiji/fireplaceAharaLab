from ..utils import *

class SCH_700:
	""" Spirit Jailer
	<b>Battlecry:</b> Shuffle 2 Soul Fragments into your deck."""
	play = Shuffle(CONTROLLER,"SCH_307t")*2 
	pass

class SCH_307t:
	""" Soul Fragment
	<b>Casts When Drawn</b>
	Restore #2 Health to your hero.""" 
	play = Heal(FRIENDLY_HERO,2)
