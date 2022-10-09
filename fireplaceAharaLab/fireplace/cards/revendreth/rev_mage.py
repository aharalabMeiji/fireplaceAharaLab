from ..utils import *

Rev_Mage=[]

Rev_Objection=True
Rev_Life_Sentence=True
Rev_Contract_Conjurer=True
Rev_Suspicious_Alchemist=True
Rev_Solid_Alibi=True
Rev_Cold_Case=True
Rev_Chatty_Bartender=True
Rev_KelThuzad_the_Inevitable=True
Rev_Orion_Mansion_Manager=True
Rev_Vengeful_Visage=True
Rev_Frozen_Touch=True
Rev_Nightcloak_Sanctum=True
Rev_KelThuzad_the_Inevitable=True
Rev_Nightcloak_Sanctum=True
Rev_Deathborne=True
Rev_Informed=True


if Rev_Objection:# 
	Rev_Mage+=['MAW_006']
class MAW_006:# <4>[1691]
	""" Objection!
	<b>Secret:</b> When your opponent plays a _minion, <b>Counter</b> it. """
	secret = Play(OPPONENT, MINION).after(Counter(Play.CARD))
	pass




if Rev_Life_Sentence:# 
	Rev_Mage+=['MAW_013']
class MAW_013:# <4>[1691]
	""" Life Sentence
	Remove a minion from the game. """
	#
	pass

if Rev_Contract_Conjurer:# 
	Rev_Mage+=['MAW_101']
class MAW_101:# <4>[1691]
	""" Contract Conjurer
	Costs (3) less for each <b>Secret</b> you control. """
	#
	pass

if Rev_Suspicious_Alchemist:# 
	Rev_Mage+=['REV_000']
class REV_000:# <4>[1691]
	""" Suspicious Alchemist
	<b>Battlecry:</b> <b>Discover</b> a spell. If your opponent guesses your choice, they get a copy. """
	#
	pass

	Rev_Mage+=['REV_000e']
class REV_000e:# <4>[1691]
	""" A Mystery!
	At the start of your turn, guess what card your opponent chose to get a copy of it. """
	#
	pass

if Rev_Solid_Alibi:# 
	Rev_Mage+=['REV_504']
class REV_504:# <4>[1691]
	""" Solid Alibi
	Until your next turn, your hero can only take 1 damage at a time. """
	#
	pass

	Rev_Mage+=['REV_504e']
class REV_504e:# <4>[1691]
	""" Solid Alibi
	Your hero only takes 1 damage at a time until the start of your next turn. """
	#
	pass

if Rev_Cold_Case:# 
	Rev_Mage+=['REV_505']
class REV_505:# <4>[1691]
	""" Cold Case
	Summon two 2/2 Volatile Skeletons. Gain 4 Armor. """
	#
	pass

if Rev_Chatty_Bartender:# 
	Rev_Mage+=['REV_513']
class REV_513:# <4>[1691]
	""" Chatty Bartender
	At the end of your turn, if you control a <b>Secret</b>, deal 2 damage to all enemies. """
	#
	pass

if Rev_KelThuzad_the_Inevitable:# 
	Rev_Mage+=['REV_514']
class REV_514:# <4>[1691]
	""" Kel'Thuzad, the Inevitable
	<b>Battlecry:</b> Resurrect your  Volatile Skeletons. Any that  can't fit on the battlefield  instantly explode! @<i>(@)</i> """
	#
	pass

if Rev_Orion_Mansion_Manager:# 
	Rev_Mage+=['REV_515']
	Rev_Mage+=['REV_515e']
class REV_515:# <4>[1691]
	""" Orion, Mansion Manager
	After a friendly <b>Secret</b> is revealed, cast a different Mage <b>Secret</b> and gain +2/+2. """
	#
	pass
class REV_515e:# <12>[1691]
	""" Cosmic Power
	+2/+2. """
	#
	pass

if Rev_Vengeful_Visage:# 
	Rev_Mage+=['REV_516']
class REV_516:# <4>[1691]
	""" Vengeful Visage
	<b>Secret:</b> After an enemy minion attacks your hero, summon a copy of it to attack the enemy hero. """
	#
	pass

if Rev_Frozen_Touch:# 
	Rev_Mage+=['REV_601']
	Rev_Mage+=['REV_601t']
class REV_601:# <4>[1691]
	""" Frozen Touch
	Deal $3 damage. <b>Infuse (@):</b> Add a Frozen Touch to your hand. """
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_601t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_601t', 1))
	#
	pass

class REV_601t:# <4>[1691]
	""" Frozen Touch
	<b>Infused</b> Deal $3 damage.  Add a Frozen Touch  to your hand. """
	#
	pass

if Rev_Nightcloak_Sanctum:# 
	Rev_Mage+=['REV_602']
class REV_602:# <4>[1691]
	""" Nightcloak Sanctum
	<b>Freeze</b> a minion. Summon a 2/2 Volatile Skeleton. """
	#
	pass

if Rev_KelThuzad_the_Inevitable:# 
	Rev_Mage+=['REV_786']
class REV_786:# <4>[1691]
	""" Kel'Thuzad, the Inevitable
	{0} {1} {2} {3} """
	#
	pass

if Rev_Nightcloak_Sanctum:# 
	Rev_Mage+=['REV_796']
class REV_796:# <4>[1691]
	""" Nightcloak Sanctum
	{0} {1} """
	#
	pass

if Rev_Deathborne:# 
	Rev_Mage+=['REV_840']
class REV_840:# <4>[1691]
	""" Deathborne
	Deal $2 damage to all minions. Summon a 2/2 Volatile Skeleton  for each killed. """
	#
	pass

if Rev_Informed:# 
	Rev_Mage+=['REV_841e2']
class REV_841e2:# <4>[1691]
	""" Informed
	Your next Secret costs (0). """
	#
	pass

