
from ..utils import *

Sunken_Mage=[]

Sunken_Submerged_Spacerock=True  ###
Sunken_Polymorph_Jellyfish=True  ###
Sunken_Lady_Nazjar=True  ###
Sunken_Gaia_the_Techtonic=True  ###
Sunken_Mecha_Shark=True  ###
Sunken_Seafloor_Gateway=True  ###
Sunken_Mechanical_Marvel=True
Sunken_Volcanomancy=True  ###
Sunken_Commander_Sivara=True  ###
Sunken_Spitelash_Siren=True  ###
Sunken_Trench_Surveyor=True  ###
Sunken_Spellcoiler=True  ###
Sunken_Azsharan_Sweeper=True  ###
Sunken_Gifts_of_Azshara=True  ###



if Sunken_Submerged_Spacerock:# 
	Sunken_Mage+=['TID_707']
	Sunken_Mage+=['TID_707e']
class TID_707:# <4>[1658]
	""" Submerged Spacerock
	[Deathrattle:] Add two ArcaneMage spells to your hand.At the end of your turn,discard them. """
	#

class TID_707e:# <4>[1658]
	""" Submerged
	Discards at the end of your turn. """
	#
	pass




if Sunken_Polymorph_Jellyfish:# 
	Sunken_Mage+=['TID_708']
	Sunken_Mage+=['TID_708t']
class TID_708:# <4>[1658]
	""" Polymorph: Jellyfish
	Transform a minioninto a 4/1 Jellyfish with [Spell Damage +2]. """
	#

class TID_708t:# <4>[1658]
	""" Jellyfish
	[Spell Damage +2] """
	#
	pass




if Sunken_Lady_Nazjar:# 
	Sunken_Mage+=['TID_709']
	Sunken_Mage+=['TID_709e']
	Sunken_Mage+=['TID_709t']
	Sunken_Mage+=['TID_709t2']
	Sunken_Mage+=['TID_709t3']
class TID_709:# <4>[1658]
	""" Lady Naz'jar
	While in your hand, this___transforms after you cast a___Fire, Frost, or Arcane spell. """
	#

class TID_709e:# <4>[1658]
	""" Naz'jar's Gift
	Costs (1) less. """
	#

class TID_709t:# <4>[1658]
	""" Lady Naz'jar
	[Battlecry:] Reduce the Costof spells in your hand by (1). """
	#

class TID_709t2:# <4>[1658]
	""" Lady Naz'jar
	[Battlecry:] Deal 5 damageto an enemy minion and2 to adjacent minions. """
	#

class TID_709t3:# <4>[1658]
	""" Lady Naz'jar
	[Battlecry:] Gain 8 Armor. """
	#
	pass




if Sunken_Gaia_the_Techtonic:# 
	Sunken_Mage+=['TSC_029']
	Sunken_Mage+=['TSC_029t']
	Sunken_Mage+=['TSC_029t2']
class TSC_029:# <4>[1658]
	""" Gaia, the Techtonic
	[Colossal +2]After a friendly Mech attacks, deal 1 damage to all enemies. """
	play = (
		Summon(CONTROLLER, 'TSC_029t'),
		Summon(CONTROLLER, 'TSC_029t2')
		)
	events = Attack(FRIENDLY + MECH).after(Hit(ENEMY_CHARACTERS, 1))

class TSC_029t:# <4>[1658]
	""" Gaia's Drill
	[Rush] """
	pass
class TSC_029t2:# <4>[1658]
	""" Gaia's Drill
	[Rush] """
	pass




if Sunken_Mecha_Shark:# 
	Sunken_Mage+=['TSC_054']
class TSC_054:# <4>[1658]
	""" Mecha-Shark
	After you summon a Mech,deal 3 damage randomly_split among all enemies. """
	#
	pass




if Sunken_Seafloor_Gateway:# 
	Sunken_Mage+=['TSC_055']
	Sunken_Mage+=['TSC_055e']
class TSC_055:# <4>[1658]
	""" Seafloor Gateway
	Draw a Mech. Reduce the Cost of Mechs in your hand by (1). """
	#

class TSC_055e:# <4>[1658]
	""" Mechanical Marvel
	Costs (1) less. """
	#
	pass




if Sunken_Volcanomancy:# 
	Sunken_Mage+=['TSC_056']
	Sunken_Mage+=['TSC_056e']
class TSC_056:# <4>[1658]
	""" Volcanomancy
	Choose a minion. When it dies, deal 3 damage to all other minions. """
	#

class TSC_056e:# <4>[1658]
	""" Explosive
	When this dies, deal 3 damage to all other minions. """
	#
	pass




if Sunken_Commander_Sivara:# 
	Sunken_Mage+=['TSC_087']
class TSC_087:# <4>[1658]
	""" Commander Sivara
	[Battlecry:] If you've castthree spells while holdingthis, add those spells backto your hand.@ <i>({0} left!)</i>@ <i>(Ready!)</i> """
	#
	pass




if Sunken_Spitelash_Siren:# 
	Sunken_Mage+=['TSC_620']
class TSC_620:# <4>[1658]
	""" Spitelash Siren
	After you play a Naga,refresh two Mana Crystals.<i>(Then switch to spell!)</i>@After you cast a spell,refresh two Mana Crystals.<i>(Then switch to Naga!)</i> """
	#
	pass




if Sunken_Trench_Surveyor:# 
	Sunken_Mage+=['TSC_642']
class TSC_DredgeChoice(Choice):
	def choose(self, card):
		super().choose(card)
		if Config.LOGINFO:
			print("(DredgeChoice.choose)%s chooses %r"%(card.controller.name, card))
		controller = card.controller
		for c in controller.deck[:3]:
			if card.id==c.id:
				controller.deck.remove(c)
				controller.deck.append(c)
				if hasattr(c, 'race') and c.race==Race.MECHANICAL:
					Draw(controller, c).trigger(controller)
				break
		pass
class TSC_Dredge(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		bottom3ID=[card.id for card in target.deck[:3]]
		TSC_DredgeChoice(target, RandomID(*bottom3ID)*3).trigger(source)
	pass
class TSC_642:# <4>[1658]
	""" Trench Surveyor
	[Battlecry:] [Dredge].If it's a Mech, draw it. """
	play = TSC_Dredge(CONTROLLER)
	pass




if Sunken_Spellcoiler:# 
	Sunken_Mage+=['TSC_643']
class TSC_643:# <4>[1658]
	""" Spellcoiler
	[Battlecry:] If you've cast aspell while holding this,[Discover] a spell. """
	#
	pass




if Sunken_Azsharan_Sweeper:# 
	Sunken_Mage+=['TSC_776']
	Sunken_Mage+=['TSC_776t']
class TSC_776:# <4>[1658]
	""" Azsharan Sweeper
	[Battlecry:] Put a 'Sunken Sweeper' on the bottom of your deck. """
	#

class TSC_776t:# <4>[1658]
	""" Sunken Sweeper
	[Battlecry:] Add 3 random Mechs to your hand. """
	#
	pass




if Sunken_Gifts_of_Azshara:# 
	Sunken_Mage+=['TSC_948']
class TSC_948:# <4>[1658]
	""" Gifts of Azshara
	Draw a card. If you played a Naga while holding this, do it again. """
	#
	pass

