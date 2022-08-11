from ..utils import *

#CardSet.SCHOLOMANCE_CardClass.DEMONHUNTER=['SCH_252','SCH_253','SCH_253t','SCH_276','SCH_279','SCH_354','SCH_354e','SCH_354e2','SCH_354e2a','SCH_354e2b','SCH_354ea','SCH_354eb','SCH_355','SCH_356','SCH_357','SCH_357e','SCH_357t','SCH_422','SCH_538','SCH_600','SCH_600t1','SCH_600t2','SCH_600t3','SCH_603','SCH_618','SCH_702e','SCH_704','SCH_704e','SCH_705','SCH_705t',]

class SCH_700:#<9>[1443]WARLOCK
	""" Spirit Jailer
	<b>Battlecry:</b> Shuffle 2 Soul Fragments into your deck."""
	play = Shuffle(CONTROLLER,"SCH_307t")*2 
	pass

class SCH_307t:# <9>[1443]WARLOCK
	""" Soul Fragment
	<b>Casts When Drawn</b>
	Restore #2 Health to your hero.""" 
	play = Heal(FRIENDLY_HERO,2)

	
class SCH_252:# <14>[1443]
	""" Marrowslicer
	[Battlecry:] Shuffle 2 Soul Fragments into your deck. """
	#
	pass

class SCH_253:# <14>[1443]
	""" Cycle of Hatred
	Deal $3 damage to all minions. Summon a 3/3 Spirit for every minion killed. """
	#
	pass

class SCH_253t:# <14>[1443]
	""" Spirit of Vengeance
	 """
	#
	pass

class SCH_276:# <14>[1443]
	""" Magehunter
	[Rush]Whenever this attacks a minion, [Silence] it. """
	#
	pass

class SCH_279:# <14>[1443]
	""" Trueaim Crescent
	After your Hero attacks a minion, your minions attack it too. """
	#
	pass

class SCH_354:# <14>[1443]
	""" Ancient Void Hound
	At the end of your turn,steal 1 Attack and Healthfrom all enemy minions. """
	#
	pass

class SCH_354e:# <14>[1443]
	""" Siphoned
	Reduced Attack and Health. """
	#
	pass

class SCH_354e2:# <14>[1443]
	""" Void Siphon
	Increased Attack and Health. """
	#
	pass

class SCH_354e2a:# <14>[1443]
	""" Void Siphon
	Increased Attack. """
	#
	pass

class SCH_354e2b:# <14>[1443]
	""" Void Siphon
	Increased Health. """
	#
	pass

class SCH_354ea:# <14>[1443]
	""" Siphoned
	Reduced Attack. """
	#
	pass

class SCH_354eb:# <14>[1443]
	""" Siphoned
	Reduced Health. """
	#
	pass

class SCH_355:# <14>[1443]
	""" Shardshatter Mystic
	[Battlecry:] Destroy a Soul Fragment in your deck to deal 3 damage to all other minions. """
	#
	pass

class SCH_356:# <14>[1443]
	""" Glide
	Shuffle your hand intoyour deck. Draw 4 cards.[Outcast:] Your opponentdoes the same. """
	#
	pass

class SCH_357:# <14>[1443]
	""" Fel Guardians
	Summon three 1/2 Demons with [Taunt]. Costs (1) less whenever a_friendly minion dies. """
	#
	pass

class SCH_357e:# <14>[1443]
	""" Soul Infused
	Costs less. """
	#
	pass

class SCH_357t:# <14>[1443]
	""" Soulfed Felhound
	[Taunt] """
	#
	pass

class SCH_422:# <14>[1443]
	""" Double Jump
	Draw an [Outcast] card from your deck. """
	#
	pass

#class SCH_538:# <14>[1443]-> scholo_hunter
#	""" Ace Hunter Kreen
#	Your other characters are [Immune] while attacking. """
#	#
#	pass

class SCH_600:# <14>[1443]
	""" Demon Companion
	Summon a random Demon Companion. """
	#
	pass

class SCH_600t1:# <14>[1443]
	""" Reffuh
	[Charge] """
	#
	pass

class SCH_600t2:# <14>[1443]
	""" Shima
	[Taunt] """
	#
	pass

class SCH_600t3:# <14>[1443]
	""" Kolek
	Your other minions have +1 Attack. """
	#
	pass

class SCH_603:# <14>[1443]
	""" Star Student Stelina
	[Outcast:] Look at 3 cardsin your opponent's hand.Shuffle one of theminto their deck. """
	#
	pass

class SCH_618:# <14>[1443]
	""" Blood Herald
	Whenever a friendly minion dies while this is in your hand, gain +1/+1. """
	#
	pass

class SCH_702e:# <14>[1443]
	""" Felosophically Inclined
	+1/+1 """
	#
	pass

class SCH_704:# <14>[1443]
	""" Soulshard Lapidary
	[Battlecry:] Destroy a SoulFragment in your deck togive your hero +5 Attackthis turn. """
	#
	pass

class SCH_704e:# <14>[1443]
	""" Soul Rage
	+5 Attack this turn. """
	#
	pass

class SCH_705:# <14>[1443]
	""" Vilefiend Trainer
	[Outcast:] Summon two 1/1_Demons. """
	#
	pass

class SCH_705t:# <14>[1443]
	""" Snarling Vilefiend
	 """
	#
	pass

