from ..utils import *

Rev_Warlock=[]

Rev_Imp_oster=True
Rev_Arson_Accusation=True
Rev_Habeas_Corpses=True
Rev_Suffocating_Shadows=True
Rev_Tome_Tampering=True
Rev_Flustered_Librarian=True
Rev_Mischievous_Imp=True
Rev_Impending_Catastrophe=True
Rev_Vile_Library=True
Rev_Shadow_Waltz=True
Rev_Lady_Darkvein=True
Rev_Shadowborn=True
Rev_Imp_King_Rafaam=True
Rev_Vile_Library=True
Rev_Imp_King_Rafaam=True


if Rev_Imp_oster:# 
	Rev_Warlock+=['MAW_000']
class MAW_000:# <9>[1691]
	""" Imp-oster
	<b>Battlecry:</b> Choose a friendly Imp. Transform into a copy of it. """
	#
	pass

if Rev_Arson_Accusation:# 
	Rev_Warlock+=['MAW_001']
class MAW_001:# <9>[1691]
	""" Arson Accusation
	Choose a minion. Destroy it after your hero takes damage. """
	#
	pass

	Rev_Warlock+=['MAW_001e']
class MAW_001e:# <9>[1691]
	""" Arson Trial
	When your hero takes damage, destroy the accused. """
	#
	pass

	Rev_Warlock+=['MAW_001e2']
class MAW_001e2:# <9>[1691]
	""" Accused of Arson
	When the accuser takes damage, this minion dies. """
	#
	pass

if Rev_Habeas_Corpses:# 
	Rev_Warlock+=['MAW_002']
class MAW_002:# <9>[1691]
	""" Habeas Corpses
	<b>Discover</b> a friendly minion to resurrect and give it <b>Rush</b>. It dies at the end of turn. """
	#
	pass

	Rev_Warlock+=['MAW_002e']
class MAW_002e:# <9>[1691]
	""" Habeas Corpse
	Dies at the end of turn. """
	#
	pass

if Rev_Suffocating_Shadows:# 
	Rev_Warlock+=['REV_239']
class REV_239:# <9>[1691]
	""" Suffocating Shadows
	When you play or  discard this, destroy a  random enemy minion. """
	#
	pass

	Rev_Warlock+=['REV_239e']
class REV_239e:# <9>[1691]
	""" Suffocation
	Costs (3) less. """
	#
	pass

if Rev_Tome_Tampering:# 
	Rev_Warlock+=['REV_240']
class REV_240:# <9>[1691]
	""" Tome Tampering
	Shuffle 1-Cost  copies of cards in your  hand into your deck,  then discard your hand. """
	#
	pass

	Rev_Warlock+=['REV_240e']
class REV_240e:# <9>[1691]
	""" Cost Curse
	Costs (1). """
	#
	pass

if Rev_Flustered_Librarian:# 
	Rev_Warlock+=['REV_242']
class REV_242:# <9>[1691]
	""" Flustered Librarian
	Has +1 Attack for each Imp you control. """
	#
	pass

if Rev_Mischievous_Imp:# 
	Rev_Warlock+=['REV_244']
class REV_244:# <9>[1691]
	""" Mischievous Imp
	<b>Battlecry:</b> Summon a copy of this. <b>Infuse (@):</b> Summon two copies instead. """
	#
	pass

	Rev_Warlock+=['REV_244t']
class REV_244t:# <9>[1691]
	""" Mischievous Imp
	<b>Infused Battlecry:</b> Summon two  copies of this. """
	#
	pass

if Rev_Impending_Catastrophe:# 
	Rev_Warlock+=['REV_245']
class REV_245:# <9>[1691]
	""" Impending Catastrophe
	Draw a card. Repeat for each Imp you control. """
	#
	pass

if Rev_Vile_Library:# 
	Rev_Warlock+=['REV_371']
class REV_371:# <9>[1691]
	""" Vile Library
	Give a friendly minion +1/+1 for each Imp you control. """
	#
	pass

	Rev_Warlock+=['REV_371e']
class REV_371e:# <9>[1691]
	""" Imp Power
	+1/+1. """
	#
	pass

if Rev_Shadow_Waltz:# 
	Rev_Warlock+=['REV_372']
class REV_372:# <9>[1691]
	""" Shadow Waltz
	Summon a 3/5 Shadow with <b>Taunt</b>. If a minion died this turn, summon another. """
	#
	pass

	Rev_Warlock+=['REV_372t']
class REV_372t:# <9>[1691]
	""" Twirling Shadow
	<b>Taunt</b> """
	#
	pass

if Rev_Lady_Darkvein:# 
	Rev_Warlock+=['REV_373']
class REV_373:# <9>[1691]
	""" Lady Darkvein
	<b>Battlecry:</b> Summon two 2/1 Shades. Each gains a <b>Deathrattle</b> to cast your  last Shadow spell. """
	#
	pass

	Rev_Warlock+=['REV_373e']
class REV_373e:# <9>[1691]
	""" Dark Bidding
	Spell: {0} is inside! """
	#
	pass

	Rev_Warlock+=['REV_373t']
class REV_373t:# <9>[1691]
	""" Shadow Manifestation
	 """
	#
	pass

if Rev_Shadowborn:# 
	Rev_Warlock+=['REV_374']
class REV_374:# <9>[1691]
	""" Shadowborn
	<b>Deathrattle:</b> Reduce the Cost of the highest Cost Shadow spell in your hand by (3). """
	#
	pass

	Rev_Warlock+=['REV_374e']
class REV_374e:# <9>[1691]
	""" In Shadow
	Costs (3) less. """
	#
	pass

if Rev_Imp_King_Rafaam:# 
	Rev_Warlock+=['REV_789']
class REV_789:# <9>[1691]
	""" Imp King Rafaam
	{0} {1} {2} {3} """
	#
	pass

if Rev_Vile_Library:# 
	Rev_Warlock+=['REV_799']
class REV_799:# <9>[1691]
	""" Vile Library
	{0} {1} """
	#
	pass

if Rev_Imp_King_Rafaam:# 
	Rev_Warlock+=['REV_835']
class REV_835:# <9>[1691]
	""" Imp King Rafaam
	<b>Battlecry:</b> Resurrect four friendly Imps. <b>Infuse (@):</b> Give your Imps +2/+2. """
	#
	pass

	Rev_Warlock+=['REV_835e']
class REV_835e:# <9>[1691]
	""" Impfused Anima
	+2/+2. """
	#
	pass

	Rev_Warlock+=['REV_835t']
class REV_835t:# <9>[1691]
	""" Imp King Rafaam
	<b>Infused.</b> <b>Battlecry:</b> Summon four friendly Imps that died this game. __Give your Imps +2/+2. """
	#
	pass

