
from ..utils import *

Barrens_DemonHunter=[]

Barrens_Sigil_of_Flame=True  ###
Barrens_Razorboar=True  ###
Barrens_Razorfen_Beastmaster=True  ###
Barrens_Vile_Call=True  ###
Barrens_Vengeful_Spirit=True  ###
Barrens_Death_Speaker_Blackthorn=True  ###
Barrens_Tuskpiercer=True  ###
Barrens_Kurtrus_Ashfallen=True  ###
Barrens_Sigil_of_Silence=True  ###
Barrens_Fury_Rank_1=True  ###
Barrens_Sigil_of_Summoning=True  ###
Barrens_Taintheart_Tormenter=True  ###
Barrens_Felrattler=True  ###

##################################################

if Barrens_Sigil_of_Flame:# 
	Barrens_DemonHunter+=['BAR_306']
class BAR_306:# <14>[1525]
	""" Sigil of Flame
	At the start of your next turn, deal $3 damageto all minions. """
	#
	pass




if Barrens_Razorboar:# 
	Barrens_DemonHunter+=['BAR_325']
class BAR_325:# <14>[1525]
	""" Razorboar
	[Deathrattle:] Summon a [Deathrattle] minion that costs (3) or less from your hand. """
	#
	pass




if Barrens_Razorfen_Beastmaster:# 
	Barrens_DemonHunter+=['BAR_326']
class BAR_326:# <14>[1525]
	""" Razorfen Beastmaster
	[Deathrattle:] Summon a [Deathrattle] minion that costs (4) or less from your hand. """
	#
	pass




if Barrens_Vile_Call:# 
	Barrens_DemonHunter+=['BAR_327']
	Barrens_DemonHunter+=['BAR_327t']
class BAR_327:# <14>[1525]
	""" Vile Call
	Summon two 2/2 Demons with [Lifesteal]. """
	#
	pass

class BAR_327t:# <14>[1525]
	""" Ravenous Vilefiend
	[Lifesteal] """
	#
	pass




if Barrens_Vengeful_Spirit:# 
	Barrens_DemonHunter+=['BAR_328']
class BAR_328:# <14>[1525]
	""" Vengeful Spirit
	[Outcast:] Draw 2 [Deathrattle] minions. """
	#
	pass




if Barrens_Death_Speaker_Blackthorn:# 
	Barrens_DemonHunter+=['BAR_329']
class BAR_329:# <14>[1525]
	""" Death Speaker Blackthorn
	[Battlecry:] Summon 3 [Deathrattle] minions that cost (5) or less from your deck. """
	#
	pass




if Barrens_Tuskpiercer:# 
	Barrens_DemonHunter+=['BAR_330']
class BAR_330:# <14>[1525]
	""" Tuskpiercer
	[Deathrattle:] Draw a[Deathrattle] minion. """
	#
	pass




if Barrens_Kurtrus_Ashfallen:# 
	Barrens_DemonHunter+=['BAR_333']
class BAR_333:# <14>[1525]
	""" Kurtrus Ashfallen
	[Battlecry:] Attack the left andright-most enemy minions.[Outcast:] [Immune] this turn. """
	#
	pass




if Barrens_Sigil_of_Silence:# 
	Barrens_DemonHunter+=['BAR_705']
class BAR_705:# <14>[1525]
	""" Sigil of Silence
	At the start of yournext turn, [Silence] allenemy minions. """
	#
	pass




if Barrens_Fury_Rank_1:# 
	Barrens_DemonHunter+=['BAR_891']
	Barrens_DemonHunter+=['BAR_891e']
	Barrens_DemonHunter+=['BAR_891e2']
	Barrens_DemonHunter+=['BAR_891e3']
	Barrens_DemonHunter+=['BAR_891t']
	Barrens_DemonHunter+=['BAR_891t2']
class BAR_891:# <14>[1525]
	""" Fury (Rank 1)
	Give your hero +2 Attack this turn. <i>(Upgrades when you have 5 Mana.)</i> """
	#
	pass

class BAR_891e:# <14>[1525]
	""" Fury
	+2 Attack this turn. """
	#
	pass

class BAR_891e2:# <14>[1525]
	""" Fury
	+3 Attack this turn. """
	#
	pass

class BAR_891e3:# <14>[1525]
	""" Fury
	+4 Attack this turn. """
	#
	pass

class BAR_891t:# <14>[1525]
	""" Fury (Rank 2)
	Give your hero +3 Attackthis turn. <i>(Upgrades whenyou have 10 Mana.)</i> """
	#
	pass

class BAR_891t2:# <14>[1525]
	""" Fury (Rank 3)
	Give your hero +4_Attack this turn. """
	#
	pass



if Barrens_Sigil_of_Summoning:# 
	Barrens_DemonHunter+=['WC_003']
	Barrens_DemonHunter+=['WC_003t']
class WC_003:# <14>[1525]
	""" Sigil of Summoning
	At the start of your next turn, summon two 2/2 Demons with [Taunt]. """
	#
	pass

class WC_003t:# <14>[1525]
	""" Wailing Demon
	[Taunt] """
	#
	pass




if Barrens_Taintheart_Tormenter:# 
	Barrens_DemonHunter+=['WC_040']
class WC_040:# <14>[1525]
	""" Taintheart Tormenter
	[Taunt]Your opponent's spells cost (2) more. """
	#
	pass




if Barrens_Felrattler:# 
	Barrens_DemonHunter+=['WC_701']
class WC_701:# <14>[1525]
	""" Felrattler
	[Rush][Deathrattle:] Deal 1 damageto all enemy minions. """
	#
	pass

