from ..utils import *

class SCH_700:
	""" Spirit Jailer
	&lt;b&gt;Battlecry:&lt;/b&gt; Shuffle 2 Soul Fragments into your deck."""
	play = Shuffle(CONTROLLER,"SCH_307t")*2 
	pass

class SCH_307t:
	""" Soul Fragment
	&lt;b&gt;Casts When Drawn&lt;/b&gt;
	Restore #2 Health to your hero.""" 
	play = Heal(FRIENDLY_HERO,2)
