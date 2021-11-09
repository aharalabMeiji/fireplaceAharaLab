from ..utils import *

#stormwind updates

#Stormwind_Updates=[
#'DED_006','DED_006e2','DED_514e','DED_521','DED_523','DED_523e','DED_524','DED_525',
#'DED_007','DED_008',,'DED_009',,'DED_009e',
#'DED_515','DED_516','DED_517','DED_517t',
#'DED_001','DED_001a','DED_001at','DED_001b','DED_001bt','DED_001c','DED_002','DED_002e','DED_003',
#'DED_518','DED_519','DED_527','DED_527e',
#]

## neutral

class DED_006:# <12>[1578]
	""" Mr. Smite
	Your Pirates have [Charge]. """
	play = Buff(FIRNEDLY_MINIONS + PIRATE, 'DED_006e2')
	pass

DED_006e2 = buff(charge=True)# <12>[1578]
""" Charge
{0} grants [Charge]. """
#

class DED_514e:# <12>[1578]
	""" Copycat
	Add a copy of the next card your opponent plays to your hand. """
	#
	pass

class DED_521:# <12>[1578]
	""" Maddest Bomber
	[Battlecry:] Deal 12 damage randomly split among all other characters. """
	play = Hit(RANDOM(ALL_CHARACTERS),1) * 12
	pass

class DED_523:# <12>[1578]
	""" Golakka Glutton
	[Battlecry:] Destroy a Beast and gain +1/+1. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.BEAST}
	play = (Destroy(TARGET), Buff(SELF, 'DED_523e'))
	pass

DED_523e = buff(1,1)# <12>[1578]
""" Stuffed Belly
+1/+1. """
#

class DED_524:# <12>[1578]
	""" Multicaster
	[Battlecry:] Draw a card for each different spell school_you've cast this game. """
	#
	pass

class DED_525:# <12>[1578]
	""" Goliath, Sneed's Masterpiece
	[Battlecry:] Fire five rockets at enemy minions that deal 2 damage each. <i>(You pickthe targets!)</i> """
	#
	pass


## hunter

class DED_007:# <3>[1578]
	""" Defias Blastfisher
	[Battlecry:] Deal 2 damage to a random enemy. Repeat for each of your Beasts. """
	#
	pass

class DED_008:# <3>[1578]
	""" Monstrous Parrot
	[Battlecry:] Repeat the lastfriendly [Deathrattle]that triggered. """
	#
	pass

class DED_009:# <3>[1578]
	""" Doggie Biscuit
	[Tradeable]Give a minion +2/+3.After you [Trade] this, givea friendly minion [Rush]. """
	#
	pass

class DED_009e:# <3>[1578]
	""" Good Doggie!
	+2/+3. """
	#
	pass

## mage

class DED_515:# <4>[1578]
	""" Grey Sage Parrot
	[Battlecry:] Repeat the last spell you've cast that costs (5) or more. """
	#
	pass

class DED_516:# <4>[1578]
	""" Deepwater Evoker
	[Battlecry:] Draw a spell.Gain Armor equal toits Cost. """
	#
	pass

class DED_517:# <4>[1578]
	""" Arcane Overflow
	Deal $8 damage to anenemy minion. Summon a Remnant with stats equalto the excess damage. """
	#
	pass

class DED_517t:# <4>[1578]
	""" Arcane Remnant
	 """
	#
	pass

## druid

class DED_001:# <2>[1578]
	""" Druid of the Reef
	[Choose One - ]Transform into a 3/1 Shark with [Rush]; or a 1/3 Turtle with [Taunt]. """
	choose = ("DED_001a", "DED_001b")
	play = ChooseBoth(CONTROLLER) & (
		Summon(CONTROLLER, "DED_001c")
	)	

class DED_001a:# <2>[1578]
	""" Shark Form
	[Rush] """
	play = Buff(SELF, 'DED_001at')
	pass

DED_001at = buff(rush=True)# <2>[1578]
""" Druid of the Reef
[Rush] """

class DED_001b:# <2>[1578]
	""" Sea Turtle Form
	[Taunt] """
	play = Buff(SELF, 'DED_001bt')
	pass

DED_001bt = buff(taunt=True)# <2>[1578]
""" Druid of the Reef
[Taunt] """
#

class DED_001c:# <2>[1578]
	""" Druid of the Reef
	[Rush][Taunt] """
	#
	pass

class DED_002:# <2>[1578]
	""" Moonlit Guidance
	[Discover] a copy of a card in your deck.If you play it this turn,draw the original. """
	#
	pass

class DED_002e:# <2>[1578]
	""" Path of the Moon
	If played this turn, draw the original copy. """
	#
	pass

class DED_003:# <2>[1578]
	""" Jerry Rig Carpenter
	[Battlecry:] Draw a [Choose One] spell and split it. """
	#
	pass

## warrior

class DED_518:# <10>[1578]
	""" Man the Cannons
	Deal $3 damage to a minion and $1 damage to all other minions. """
	#
	pass

class DED_519:# <10>[1578]
	""" Defias Cannoneer
	After your hero attacks,deal 2 damage to arandom enemy twice. """
	#
	pass

class DED_527:# <10>[1578]
	""" Blacksmithing Hammer
	[Tradeable]After you [Trade] this,_gain +2 Durability. """
	#
	pass

class DED_527e:# <10>[1578]
	""" Blacksmithing
	+2 Durability. """
	#
	pass

