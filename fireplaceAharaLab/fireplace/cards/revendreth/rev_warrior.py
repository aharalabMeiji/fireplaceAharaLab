from ..utils import *

Rev_Warrior=[]

Rev_Call_to_the_Stand=True
Rev_Mawsworn_Bailiff=True
Rev_Weapons_Expert=True
Rev_Suspicious_Pirate=True
Rev_Remornia_Living_Blade=True
Rev_Anima_Extractor=True
Rev_Burden_of_Pride=True
Rev_Riot=True
Rev_Decimator_Olgra=True
Rev_Sanguine_Depths=True
Rev_Crazed_Wretch=True
Rev_Conquerors_Banner=True
Rev_Imbued_Axe=True
Rev_Decimator_Olgra=True
Rev_Sanguine_Depths=True


if Rev_Call_to_the_Stand:# 
	Rev_Warrior+=['MAW_027']
class MAW_027:# <10>[1691]
	""" Call to the Stand
	Your opponent summons a random minion from their hand. """
	#
	pass

if Rev_Mawsworn_Bailiff:# 
	Rev_Warrior+=['MAW_028']
class MAW_028:# <10>[1691]
	""" Mawsworn Bailiff
	<b><b>Taunt</b>.</b> <b>Battlecry:</b> If you have 4 or more Armor, gain +4/+4. """
	#
	pass

	Rev_Warrior+=['MAW_028e2']
class MAW_028e2:# <10>[1691]
	""" This Man Is Charged!
	+4/+4. """
	#
	pass

if Rev_Weapons_Expert:# 
	Rev_Warrior+=['MAW_029']
class MAW_029:# <10>[1691]
	""" Weapons Expert
	<b>Battlecry:</b> If you have a weapon equipped, give it +1/+1. Otherwise, draw a weapon. """
	#
	pass

	Rev_Warrior+=['MAW_029e2']
class MAW_029e2:# <10>[1691]
	""" Sharpened
	+1/+1. """
	#
	pass

if Rev_Suspicious_Pirate:# 
	Rev_Warrior+=['REV_006']
class REV_006:# <10>[1691]
	""" Suspicious Pirate
	<b>Battlecry:</b> <b>Discover</b> a weapon. If your opponent guesses your choice, they get a copy. """
	#
	pass

if Rev_Remornia_Living_Blade:# 
	Rev_Warrior+=['REV_316']
class REV_316:# <10>[1691]
	""" Remornia, Living Blade
	<b>Rush</b> After this attacks, equip it. """
	#
	pass

	Rev_Warrior+=['REV_316e']
class REV_316e:# <10>[1691]
	""" Remornia's Will
	Has the stats of Remornia. """
	#
	pass

	Rev_Warrior+=['REV_316t']
class REV_316t:# <10>[1691]
	""" Remornia, Living Blade
	After your hero attacks, return this to the battlefield. """
	#
	pass

if Rev_Anima_Extractor:# 
	Rev_Warrior+=['REV_332']
class REV_332:# <10>[1691]
	""" Anima Extractor
	Whenever a friendly minion takes damage, give a random minion in your hand +1/+1. """
	#
	pass

	Rev_Warrior+=['REV_332e']
class REV_332e:# <10>[1691]
	""" Extracted
	+1/+1. """
	#
	pass

if Rev_Burden_of_Pride:# 
	Rev_Warrior+=['REV_334']
class REV_334:# <10>[1691]
	""" Burden of Pride
	Summon three 1/3 Jailers with <b>Taunt</b>. If you have 20 or less Health, give them +1/+1. """
	#
	pass

	Rev_Warrior+=['REV_334e']
class REV_334e:# <10>[1691]
	""" Empowered
	+1/+1. """
	#
	pass

	Rev_Warrior+=['REV_334t']
class REV_334t:# <10>[1691]
	""" Sanguine Jailer
	<b>Taunt</b> """
	#
	pass

if Rev_Riot:# 
	Rev_Warrior+=['REV_337']
class REV_337:# <10>[1691]
	""" Riot!
	Your minions can't be  reduced below 1 Health  this turn. They each attack  a random enemy minion. """
	#
	pass

	Rev_Warrior+=['REV_337e']
class REV_337e:# <10>[1691]
	""" Riot!
	Can't be reduced below 1 Health this turn. """
	#
	pass

	Rev_Warrior+=['REV_337e2']
class REV_337e2:# <10>[1691]
	""" Riot!
	Your minions can't be reduced below 1 Health this turn. """
	#
	pass

if Rev_Decimator_Olgra:# 
	Rev_Warrior+=['REV_783']
class REV_783:# <10>[1691]
	""" Decimator Olgra
	{0} {1} {2} {3} """
	#
	pass

if Rev_Sanguine_Depths:# 
	Rev_Warrior+=['REV_793']
class REV_793:# <10>[1691]
	""" Sanguine Depths
	{0} {1} """
	#
	pass

if Rev_Crazed_Wretch:# 
	Rev_Warrior+=['REV_930']
class REV_930:# <10>[1691]
	""" Crazed Wretch
	Has +2 Attack and <b>Charge</b> while damaged. """
	#
	pass

	Rev_Warrior+=['REV_930e']
class REV_930e:# <10>[1691]
	""" Angry
	<b>Charge</b>. """
	#
	pass

if Rev_Conquerors_Banner:# 
	Rev_Warrior+=['REV_931']
class REV_931:# <10>[1691]
	""" Conqueror's Banner
	Reveal a card from each player's deck, three times. Draw any of yours that cost more. """
	#
	pass

if Rev_Imbued_Axe:# 
	Rev_Warrior+=['REV_933']
	Rev_Warrior+=['REV_933e']
	Rev_Warrior+=['REV_933e2']
class REV_933:# <10>[1691]
	""" Imbued Axe
	After your hero attacks, give your damaged minions +1/+2. <b>Infuse (@):</b> +2/+2 instead. """
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_933t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_933t', 1))
	#
	pass
class REV_933e:# <10>[1691]
	""" Thirst for Blood
	+1/+2. """
	#
	pass
class REV_933e2:# <10>[1691]
	""" Thirst for Blood
	+2/+2. """
	#
	pass

	Rev_Warrior+=['REV_933t']
class REV_933t:# <10>[1691]
	""" Imbued Axe
	<b>Infused</b> After your hero attacks, give your damaged minions +2/+2. """
	#
	pass

if Rev_Decimator_Olgra:# 
	Rev_Warrior+=['REV_934']
class REV_934:# <10>[1691]
	""" Decimator Olgra
	<b>Battlecry:</b> Gain +1/+1 for each damaged minion, _then attack all enemies. """
	#
	pass

	Rev_Warrior+=['REV_934e']
class REV_934e:# <10>[1691]
	""" Bloodthirsty
	Increased stats. """
	#
	pass

if Rev_Sanguine_Depths:# 
	Rev_Warrior+=['REV_990']
class REV_990:# <10>[1691]
	""" Sanguine Depths
	Deal 1 damage to a  minion and give it  +2 Attack. """
	#
	pass

	Rev_Warrior+=['REV_990e']
class REV_990e:# <10>[1691]
	""" Sinfall Boon
	+2 Attack. """
	#
	pass

