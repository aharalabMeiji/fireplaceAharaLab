from ..utils import *

Classic_DemonHunter=[]

Classic_DemonHunter+=['HERO_10','VAN_HERO_10bp']
class HERO_10:#
	""" Illidan Stormrage  """
	pass
class VAN_HERO_10bp:# <14>[1646]
	""" Demon Claws
	[Hero Power]+1 Attack this turn. """
	activate = buff(FRIENDLY_HERO, 'VAN_HERO_10bpe')
	pass

Classic_DemonHunter+=['VAN_HERO_10bp2']
class VAN_HERO_10bp2:# <14>[1646]
	""" Demon's Bite
	[Hero Power]+2 Attack this turn. """
	activate = buff(FRIENDLY_HERO, 'VAN_HERO_10pe2')
	pass

Classic_DemonHunter+=['VAN_HERO_10bpe']
class VAN_HERO_10bpe:# <14>[1646]
	""" Demon Claws
	Your hero has +1 Attack this turn. """
	tags = {GameTag.ATK: 1,}
	#
	pass

Classic_DemonHunter+=['VAN_HERO_10pe2']
class VAN_HERO_10pe2:# <14>[1646]
	""" Demon's Bite
	Your hero has +2 Attack this turn. """
	tags = {GameTag.ATK: 2,}
	#
	pass



