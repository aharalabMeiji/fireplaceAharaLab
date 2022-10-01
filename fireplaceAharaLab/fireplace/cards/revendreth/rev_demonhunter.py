from ..utils import *

Rev_DemonHunter=[]

Rev_Sightless_Magistrate=True
Rev_All_Fel_Breaks_Loose=True
Rev_Prosecutor_Meltranix=True
Rev_Sinful_Brand=True
Rev_Dispose_of_Evidence=True
Rev_Relic_of_Dimensions=True
Rev_Magnifying_Glaive=True
Rev_Kryxis_the_Voracious=True
Rev_Bibliomite=True
Rev_Artificer_Xymox=True
Rev_Relic_Vault=True
Rev_Relic_of_Extinction=True
Rev_Artificer_Xymox=True
Rev_Relic_Vault=True
Rev_Relic_of_Phantasms=True


if Rev_Sightless_Magistrate:# 
	Rev_DemonHunter+=['MAW_008']
class MAW_008:# <14>[1691]
	""" Sightless Magistrate
	<b>Battlecry:</b> Both players draw until they have 5 cards. """
	#
	pass




if Rev_All_Fel_Breaks_Loose:# 
	Rev_DemonHunter+=['MAW_012']
	Rev_DemonHunter+=['MAW_012t']
class MAW_012_Action(TargetedAction):
	CONTROLLER=ActionArg()
	AMOUNT=ActionArg()
	def do(self, source, controller, amount):
		killed_demon=[card for card in controller.death_log if card.type==CardType.MINION and card.race==Race.DEMON]
		if len(killed_demon)>0:
			if len(killed_demon)>amount:
				killed_demon=random.sample(killed_demon,amount)
			for card in killed_demon:
				Summon(controller, card.id).trigger(source)
		pass
class MAW_012:# <14>[1691]
	""" All Fel Breaks Loose
	Summon a friendly Demon that died this game. 
	<b>Infuse (@ Demons):</b> Summon three instead. """
	play = MAW_012_Action(CONTROLLER, 1)
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'MAW_012t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'MAW_012t', 1))
	pass
class MAW_012t:# <14>[1691]
	""" All Fel Breaks Loose
	<b>Infused</b> Summon three friendly Demons that died this game. """
	play = MAW_012_Action(CONTROLLER, 3)
	pass




if Rev_Prosecutor_Meltranix:# 
	Rev_DemonHunter+=['MAW_014']
class MAW_014:# <14>[1691]
	""" Prosecutor Mel'tranix
	<b>Battlecry:</b> Your opponent can only play their left-  and right-most cards on  their next turn. """
	#
	pass

	Rev_DemonHunter+=['MAW_014e2']
class MAW_014e2:# <14>[1691]
	""" Literally Unplayable
	You can only play the left and right-most cards in your hand. """
	#
	pass

if Rev_Sinful_Brand:# 
	Rev_DemonHunter+=['REV_506']
class REV_506:# <14>[1691]
	""" Sinful Brand
	Brand an enemy minion. Whenever it takes damage, deal 2 damage to the enemy hero. """
	#
	pass

	Rev_DemonHunter+=['REV_506e']
class REV_506e:# <14>[1691]
	""" Branded
	Whenever this takes damage, deal 2 damage to your hero. """
	#
	pass

	Rev_DemonHunter+=['REV_506e2']
class REV_506e2:# <14>[1691]
	""" Branded
	Costs (1) more. """
	#
	pass

if Rev_Dispose_of_Evidence:# 
	Rev_DemonHunter+=['REV_507']
class REV_507:# <14>[1691]
	""" Dispose of Evidence
	Give your hero +3 Attack this turn. Choose a card in your hand to shuffle into your deck. """
	#
	pass

	Rev_DemonHunter+=['REV_507e']
class REV_507e:# <14>[1691]
	""" Dispose of Evidence
	+3 Attack this turn. """
	#
	pass

if Rev_Relic_of_Dimensions:# 
	Rev_DemonHunter+=['REV_508']
class REV_508:# <14>[1691]
	""" Relic of Dimensions
	Draw two cards  and reduce their Cost  by (@). Improve your  future Relics. """
	#
	pass

	Rev_DemonHunter+=['REV_508e']
class REV_508e:# <14>[1691]
	""" Dimensional
	Reduced Cost. """
	#
	pass

if Rev_Magnifying_Glaive:# 
	Rev_DemonHunter+=['REV_509']
class REV_509:# <14>[1691]
	""" Magnifying Glaive
	After your hero attacks, draw until you have 3 cards. """
	#
	pass

if Rev_Kryxis_the_Voracious:# 
	Rev_DemonHunter+=['REV_510']
class REV_510:# <14>[1691]
	""" Kryxis the Voracious
	<b>Battlecry</b>: Discard your hand. <b>Deathrattle:</b> Draw 3 cards. """
	#
	pass

if Rev_Bibliomite:# 
	Rev_DemonHunter+=['REV_511']
class REV_511:# <14>[1691]
	""" Bibliomite
	<b>Battlecry</b>: Choose a card  in your hand to shuffle  into your deck. """
	#
	pass

#if Rev_Artificer_Xymox:# 
#	Rev_DemonHunter+=['REV_787']
#class REV_787:# <14>[1691]
#	""" Artificer Xy'mox
#	{0} {1} {2} {3} """
#	#
#	pass

#if Rev_Relic_Vault:# 
#	Rev_DemonHunter+=['REV_797']
#class REV_797:# <14>[1691]
#	""" Relic Vault
#	{0} {1} """
#	#
#	pass

if Rev_Relic_of_Extinction:# 
	Rev_DemonHunter+=['REV_834']
class REV_834:# <14>[1691]
	""" Relic of Extinction
	Deal $@ damage to a random enemy minion, twice. Improve your future Relics. """
	#
	pass

if Rev_Artificer_Xymox:# 
	Rev_DemonHunter+=['REV_937']
class REV_937:# <14>[1691]
	""" Artificer Xy'mox
	<b>Battlecry:</b> <b>Discover</b> and  cast a Relic. 
	<b>Infuse (@):</b>  Cast all three instead. """
	entourage=['REV_508','REV_797','REV_834','REV_942','REV_943']
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_937t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_937t', 1))
	#
	pass

	Rev_DemonHunter+=['REV_937t']
class REV_937t:# <14>[1691]
	""" Artificer Xy'mox
	<b>Infused</b> <b>Battlecry:</b> Cast all three Relics. """
	#
	pass

if Rev_Relic_Vault:# 
	Rev_DemonHunter+=['REV_942']
class REV_942:# <14>[1691]
	""" Relic Vault
	The next Relic you play this turn casts twice. """
	#
	pass

	Rev_DemonHunter+=['REV_942e']
class REV_942e:# <14>[1691]
	""" Relic Empowerment
	Your Relics cast twice. """
	#
	pass

if Rev_Relic_of_Phantasms:# 
	Rev_DemonHunter+=['REV_943']
class REV_943:# <14>[1691]
	""" Relic of Phantasms
	Summon two @/@ Spirits. Improve your future Relics. """
	#
	pass

	Rev_DemonHunter+=['REV_943t']
class REV_943t:# <14>[1691]
	""" Fleeting Spirit
	 """
	#
	pass

