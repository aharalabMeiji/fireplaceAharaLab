from ..utils import *

#CardSet.DARKMOON_FAIRE_CardClass.DRUID=[
#'DMF_057','DMF_057e','DMF_057o','DMF_058','DMF_058e','DMF_058o',
#'DMF_059','DMF_060','DMF_061','DMF_061a','DMF_061b','DMF_061t','DMF_061t2',
#'DMF_075','DMF_075a','DMF_075a2','DMF_730','DMF_730e','DMF_730t',
#'DMF_732','DMF_733','DMF_734',
#'YOP_025','YOP_025t','YOP_026','YOP_026e',]

class DMF_057:# <2>[1466]
	""" Lunar Eclipse
	Deal $3 damage to a minion. Your next spell this turn costs (2) less. """
	#
	pass

class DMF_057e:# <2>[1466]
	""" Lunar Empowerment
	The next spell you cast costs (2) less. """
	#
	pass

class DMF_057o:# <2>[1466]
	""" Lunar Empowerment
	The next spell you cast this turn costs (2) less. """
	#
	pass

class DMF_058:# <2>[1466]
	""" Solar Eclipse
	Your next spell this turn casts twice. """
	#
	pass

class DMF_058e:# <2>[1466]
	""" Solar Empowerment
	Your next spell this turn casts twice. """
	#
	pass

class DMF_058o:# <2>[1466]
	""" Solar Empowerment
	Your next spell this turn casts twice. """
	#
	pass

class DMF_059:# <2>[1466]
	""" Fizzy Elemental
	[Rush][Taunt] """
	#
	pass

class DMF_060:# <2>[1466]
	""" Umbral Owl
	[Rush]Costs (1) less for each spellyou've cast this game. """
	#
	pass

class DMF_061:# <2>[1466]
#	""" Faire Arborist
#	[Choose One - ]Draw a card;or Summon a 2/2 Treant.[Corrupt:] Do both. """
#	choose = ("BT_136ta", "BT_136tb")
#	#choose = ('DMF_061a','DMF_061b',)
#	play = ChooseBoth(CONTROLLER) & (
#		Draw(CONTROLLER),
#		Summon(CONTROLLER,'DMF_061t2')
#		)
	pass

class DMF_061a:# <2>[1466]
	""" Prune the Fruit
	Draw a card. """
	play = Draw(CONTROLLER)
	pass

class DMF_061b:# <2>[1466]
	""" Dig It Up
	Summon a 2/2 Treant. """
	play = Summon(CONTROLLER,'DMF_061t2')
	pass

class DMF_061t:# <2>[1466]
	""" Faire Arborist
	[Corrupted][Battlecry:] Summon a 2/2 Treant. Draw a card. """
	play = Draw(CONTROLLER), Summon(CONTROLLER,'DMF_061t2')
	pass

class DMF_061t2:# <2>[1466]
	""" Treant
	 """
	#
	pass

class DMF_075:# <2>[1466]
	""" Guess the Weight
	Draw a card. Guess if your next card costs more or less to draw it. """
	#
	pass

class DMF_075a:# <2>[1466]
	""" More!
	Guess that the next card costs more. """
	#
	pass

class DMF_075a2:# <2>[1466]
	""" Less!
	Guess that the next card costs less. """
	#
	pass

class DMF_730:# <2>[1466]
	""" Moontouched Amulet
	Give your hero +4 Attack this turn. [Corrupt:] And gain 6 Armor. """
	#
	pass

class DMF_730e:# <2>[1466]
	""" Moontouched Amulet
	+4 Attack this turn. """
	#
	pass

class DMF_730t:# <2>[1466]
	""" Moontouched Amulet
	[Corrupted]Give your hero +4 Attack this turn. Gain 6 Armor. """
	#
	pass

class DMF_732:# <2>[1466]
	""" Cenarion Ward
	Gain 8 Armor.Summon a random8-Cost minion. """
	#
	pass

class DMF_733:# <2>[1466]
	""" Kiri, Chosen of Elune
	[Battlecry:] Add a Solar Eclipse and Lunar Eclipse to your hand. """
	#
	pass

class DMF_734:# <2>[1466]
	""" Greybough
	[Taunt][Deathrattle:] Give a randomfriendly minion "[Deathrattle:]Summon Greybough." """
	#
	pass

class Story_06_Broll:# <2>[1466]
	""" Broll Bearmantle
	[Spellburst:] Transform into a 3/6 Bear with [Rush].[Deathrattle:] Go [Dormant] for 2 turns. """
	#
	pass

class Story_06_BrollBear:# <2>[1466]
	""" Broll Bearmantle
	[Rush][Deathrattle:] Go [Dormant] for 2 turns. """
	#
	pass

class Story_06_BrollDormant:# <2>[1466]
	""" Broll Bearmantle
	[Dormant] """
	#
	pass

class YOP_025:# <2>[1466]
	""" Dreaming Drake
	[Taunt][Corrupt:] Gain +2/+2. """
	#
	pass

class YOP_025t:# <2>[1466]
	""" Dreaming Drake
	[Corrupted][Taunt] """
	#
	pass

class YOP_026:# <2>[1466]
	""" Arbor Up
	Summon two 2/2 Treants. Give your minions +2/+1. """
	#
	pass

class YOP_026e:# <2>[1466]
	""" Forest Guards
	+2/+1. """
	#
	pass

