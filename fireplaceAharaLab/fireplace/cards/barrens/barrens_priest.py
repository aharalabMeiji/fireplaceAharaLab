
from ..utils import *

Barrens_Priest=[]

Barrens_Void_Flayer=True  ###
Barrens_Power_Word_Fortitude=True  ###
Barrens_Desperate_Prayer=True  ###
Barrens_Lightshower_Elemental=True  ###
Barrens_Devouring_Plague=True  ###
Barrens_Soothsayers_Caravan=True  ###
Barrens_Priest_of_Anshe=True  ###
Barrens_Suns_Strength=True
Barrens_Condemn_Rank_1=True  ###
Barrens_Serena_Bloodfeather=True  ###
Barrens_Xyrella=True  ###
Barrens_Devout_Dungeoneer=True  ###
Barrens_Against_All_Odds=True  ###
Barrens_Cleric_of_Anshe=True  ###

#################################################

if Barrens_Void_Flayer:# 
	Barrens_Priest+=['BAR_307']
class BAR_307:# <6>[1525]
	""" Void Flayer
	[Battlecry:] For each spellin your hand, deal 1damage to a randomenemy minion. """
	#
	pass




if Barrens_Power_Word_Fortitude:# 
	Barrens_Priest+=['BAR_308']
class BAR_308:# <6>[1525]
	""" Power Word: Fortitude
	Give a minion +3/+5. Costs (1) less for each spell in your hand. """
	#
	pass




if Barrens_Desperate_Prayer:# 
	Barrens_Priest+=['BAR_309']
class BAR_309:# <6>[1525]
	""" Desperate Prayer
	Restore #5 Health to each hero. """
	#
	pass




if Barrens_Lightshower_Elemental:# 
	Barrens_Priest+=['BAR_310']
class BAR_310:# <6>[1525]
	""" Lightshower Elemental
	[Taunt][Deathrattle:] Restore #8 Healthto all friendly characters. """
	#
	pass




if Barrens_Devouring_Plague:# 
	Barrens_Priest+=['BAR_311']
class BAR_311:# <6>[1525]
	""" Devouring Plague
	[Lifesteal]. Deal $4 damagerandomly split amongall enemy minions. """
	#
	pass




if Barrens_Soothsayers_Caravan:# 
	Barrens_Priest+=['BAR_312']
class BAR_312:# <6>[1525]
	""" Soothsayer's Caravan
	At the start of your turn, copy a spell from your opponent's deck to your hand. """
	#
	pass




if Barrens_Priest_of_Anshe:# 
	Barrens_Priest+=['BAR_313']
	Barrens_Priest+=['BAR_313e']
class BAR_313:# <6>[1525]
	""" Priest of An'she
	[Taunt]. [Battlecry:] If you've restored Health this turn, gain +3/+3. """
	#
	pass
class BAR_313e:# <6>[1525]
	""" Sun's Strength
	+3/+3. """
	#
	pass




if Barrens_Condemn_Rank_1:# 
	Barrens_Priest+=['BAR_314']
	Barrens_Priest+=['BAR_314t']
	Barrens_Priest+=['BAR_314t2']
class BAR_314:# <6>[1525]
	""" Condemn (Rank 1)
	Deal $1 damage toall enemy minions.<i>(Upgrades when youhave 5 Mana.)</i> """
	#
	pass
class BAR_314t:# <6>[1525]
	""" Condemn (Rank 2)
	Deal $2 damage toall enemy minions.<i>(Upgrades when youhave 10 Mana.)</i> """
	#
	pass
class BAR_314t2:# <6>[1525]
	""" Condemn (Rank 3)
	Deal $3 damage to all enemy minions. """
	#
	pass




if Barrens_Serena_Bloodfeather:# 
	Barrens_Priest+=['BAR_315']
class BAR_315:# <6>[1525]
	""" Serena Bloodfeather
	[Battlecry:] Choose an enemy minion. Steal Attack and Health from it until this has more. """
	#
	pass




if Barrens_Xyrella:# 
	Barrens_Priest+=['BAR_735']
class BAR_735:# <6>[1525]
	""" Xyrella
	[Battlecry:] If you've restored Health this turn, deal that much damage to all enemy minions. """
	#
	pass




if Barrens_Devout_Dungeoneer:# 
	Barrens_Priest+=['WC_013']
class WC_013:# <6>[1525]
	""" Devout Dungeoneer
	[Battlecry:] Draw a spell.If it's a Holy spell,reduce its Cost by (2). """
	#
	pass




if Barrens_Against_All_Odds:# 
	Barrens_Priest+=['WC_014']
class WC_014:# <6>[1525]
	""" Against All Odds
	Destroy ALLodd-Attack minions. """
	#
	pass




if Barrens_Cleric_of_Anshe:# 
	Barrens_Priest+=['WC_803']
class WC_803:# <6>[1525]
	""" Cleric of An'she
	[Battlecry:] If you've restored Health this turn, [Discover] a spell from your deck. """
	#
	pass


######################################################