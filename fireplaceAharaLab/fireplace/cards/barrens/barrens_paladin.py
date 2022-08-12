
from ..utils import *

Barrens_Paladin=[]

Barrens_Galloping_Savior=True  ###
Barrens_Soldiers_Caravan=True  ###
Barrens_Knight_of_Anointment=True  ###
Barrens_Sword_of_the_Fallen=True  ###
Barrens_Northwatch_Commander=True  ###
Barrens_Veteran_Warmedic=True  ###
Barrens_Cannonmaster_Smythe=True  ###
Barrens_Conviction_Rank_1=True  ###
Barrens_Invigorating_Sermon=True  ###
Barrens_Cariel_Roame=True  ###
Barrens_Seedcloud_Buckler=True  ###
Barrens_Judgment_of_Justice=True  ###
Barrens_Party_Up=True  ###

####################################################

if Barrens_Galloping_Savior:# 
	Barrens_Paladin+=['BAR_550']
	Barrens_Paladin+=['BAR_550t']
class BAR_550:# <5>[1525]
	""" Galloping Savior
	[Secret:] After youropponent plays threecards in a turn, summon a3/4 Steed with [Taunt]. """
	#
	pass

class BAR_550t:# <5>[1525]
	""" Holy Steed
	[Taunt] """
	#
	pass




if Barrens_Soldiers_Caravan:# 
	Barrens_Paladin+=['BAR_871']
class BAR_871:# <5>[1525]
	""" Soldier's Caravan
	At the start of your turn,summon two 1/1Silver Hand Recruits. """
	#
	pass




if Barrens_Knight_of_Anointment:# 
	Barrens_Paladin+=['BAR_873']
class BAR_873:# <5>[1525]
	""" Knight of Anointment
	[Battlecry:] Draw aHoly spell. """
	#
	pass




if Barrens_Sword_of_the_Fallen:# 
	Barrens_Paladin+=['BAR_875']
class BAR_875:# <5>[1525]
	""" Sword of the Fallen
	After your hero attacks,cast a [Secret] fromyour deck. """
	#
	pass




if Barrens_Northwatch_Commander:# 
	Barrens_Paladin+=['BAR_876']
class BAR_876:# <5>[1525]
	""" Northwatch Commander
	[Battlecry:] If you control a [Secret], draw a minion. """
	#
	pass




if Barrens_Veteran_Warmedic:# 
	Barrens_Paladin+=['BAR_878']
	Barrens_Paladin+=['BAR_878t']
class BAR_878:# <5>[1525]
	""" Veteran Warmedic
	After you cast a Holy spell,summon a 2/2 Medicwith [Lifesteal]. """
	#
	pass

class BAR_878t:# <5>[1525]
	""" Battlefield Medic
	[Lifesteal] """
	#
	pass




if Barrens_Cannonmaster_Smythe:# 
	Barrens_Paladin+=['BAR_879']
	Barrens_Paladin+=['BAR_879e']
	Barrens_Paladin+=['BAR_879t']
class BAR_879:# <5>[1525]
	""" Cannonmaster Smythe
	[Battlecry:] Transform your [Secrets] into 3/3 Soldiers. They transform back when they die. """
	#
	pass

class BAR_879e:# <5>[1525]
	""" Secrecy
	It's a secret...@{0} is inside! <i>(Only you can see this.)</i> """
	#
	pass

class BAR_879t:# <5>[1525]
	""" Northwatch Soldier
	[Deathrattle:] Transform back into a [Secret]. """
	#
	pass




if Barrens_Conviction_Rank_1:# 
	Barrens_Paladin+=['BAR_880']
	Barrens_Paladin+=['BAR_880e']
	Barrens_Paladin+=['BAR_880t']
	Barrens_Paladin+=['BAR_880t2']
class BAR_880:# <5>[1525]
	""" Conviction (Rank 1)
	Give a random friendlyminion +3 Attack.<i>(Upgrades when youhave 5 Mana.)</i> """
	#
	pass
class BAR_880e:# <5>[1525]
	""" Blessed
	+3 Attack. """
	#
	pass
class BAR_880t:# <5>[1525]
	""" Conviction (Rank 2)
	Give two random friendlyminions +3 Attack.<i>(Upgrades when youhave 10 Mana.)</i> """
	#
	pass
class BAR_880t2:# <5>[1525]
	""" Conviction (Rank 3)
	Give three random friendly minions +3_Attack. """
	#
	pass




if Barrens_Invigorating_Sermon:# 
	Barrens_Paladin+=['BAR_881']
	Barrens_Paladin+=['BAR_881e']
class BAR_881:# <5>[1525]
	""" Invigorating Sermon
	Give +1/+1 to all minions in your hand, deck, and battlefield. """
	#
	pass
class BAR_881e:# <5>[1525]
	""" Holy Might
	+1/+1 """
	#
	pass




if Barrens_Cariel_Roame:# 
	Barrens_Paladin+=['BAR_902']
	Barrens_Paladin+=['BAR_902e']
class BAR_902:# <5>[1525]
	""" Cariel Roame
	[Rush], [Divine Shield]Whenever this attacks,reduce the Cost of Holy______spells in your hand by (1).___ """
	#
	pass
class BAR_902e:# <5>[1525]
	""" Light's Strength
	Costs (1) less. """
	#
	pass




if Barrens_Seedcloud_Buckler:# 
	Barrens_Paladin+=['WC_032']
class WC_032:# <5>[1525]
	""" Seedcloud Buckler
	[Deathrattle:] Give your_minions [Divine Shield]. """
	#
	pass




if Barrens_Judgment_of_Justice:# 
	Barrens_Paladin+=['WC_033']
	Barrens_Paladin+=['WC_033e']
class WC_033:# <5>[1525]
	""" Judgment of Justice
	[Secret:] When an enemy minion attacks, set its Attack and Health to 1. """
	#
	pass
class WC_033e:# <5>[1525]
	""" Judged
	1/1. """
	#
	pass




if Barrens_Party_Up:# 
	Barrens_Paladin+=['WC_034']
class WC_034:# <5>[1525]
	""" Party Up!
	Summon five 2/2 Adventurers with random bonus effects. """
	#
	pass


