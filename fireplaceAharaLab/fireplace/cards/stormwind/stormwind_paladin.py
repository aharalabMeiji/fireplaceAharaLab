
from ..utils import *

StormWind_Paladin=[]

StormWind_Wealth_Redistributor=True  ### 
StormWind_Sunwing_Squawker=True  ### 
StormWind_Righteous_Defense=True  ### 
StormWind_City_Tax=True  ### 
StormWind_Highlord_Fordragon=True  ### 
StormWind_Prismatic_Jewel_Kit=True  ### 
StormWind_Blessed_Goods=True  ### 
StormWind_First_Blade_of_Wrynn=True  ### 
StormWind_Rise_to_the_Occasion=True  ### 
StormWind_Lightbringers_Hammer=True  ### 
StormWind_Alliance_Bannerman=True  ### 
StormWind_Noble_Mount=True  ### 
StormWind_Catacomb_Guard=True  ### 





if StormWind_Wealth_Redistributor:# 
	StormWind_Paladin+=['DED_500']
	StormWind_Paladin+=['DED_500e']
class DED_500:# <5>[1578]
	""" Wealth Redistributor
	[Taunt]. [Battlecry:] Swap theAttack of the highest andlowest Attack minion. """
	#
	pass




if StormWind_Sunwing_Squawker:# 
	StormWind_Paladin+=['DED_501']
class DED_501:# <5>[1578]
	""" Sunwing Squawker
	[Battlecry:] Repeat the lastspell you've cast on a__friendly minion on this. """
	#
	pass




if StormWind_Righteous_Defense:# 
	StormWind_Paladin+=['DED_502']
	StormWind_Paladin+=['DED_502e']
	StormWind_Paladin+=['DED_502e2']
class DED_502:# <5>[1578]
	""" Righteous Defense
	Set a minion's Attack and Health to 1. Give the stats it lost to a minion in your hand. """
	#
	pass




if StormWind_City_Tax:# 
	StormWind_Paladin+=['SW_046']
class SW_046:# <5>[1578]
	""" City Tax
	[Tradeable][Lifesteal]. Deal $1 damageto all enemy minions. """
	#
	pass




if StormWind_Highlord_Fordragon:# 
	StormWind_Paladin+=['SW_047']
class SW_047:# <5>[1578]
	""" Highlord Fordragon
	[Divine Shield]After a friendly minion loses[Divine Shield], give a minion__in your hand +5/+5. """
	#
	pass




if StormWind_Prismatic_Jewel_Kit:# 
	StormWind_Paladin+=['SW_048']
class SW_048:# <5>[1578]
	""" Prismatic Jewel Kit
	After a friendly minion loses[Divine Shield], give minionsin your hand  +1/+1.Lose 1 Durability. """
	#
	pass




if StormWind_Blessed_Goods:# 
	StormWind_Paladin+=['SW_049']
class SW_049:# <5>[1578]
	""" Blessed Goods
	[Discover] a [Secret], weapon, or [Divine Shield] minion. """
	#
	pass




if StormWind_First_Blade_of_Wrynn:# 
	StormWind_Paladin+=['SW_305']
class SW_305:# <5>[1578]
	""" First Blade of Wrynn
	[Divine Shield][Battlecry:] Gain [Rush] if thishas at least 4 Attack. """
	#
	pass




if StormWind_Rise_to_the_Occasion:# 
	StormWind_Paladin+=['SW_313','CS2_091']
	#StormWind_Paladin+=['SW_313e1']
	StormWind_Paladin+=['SW_313t']
	StormWind_Paladin+=['SW_313t2']
	StormWind_Paladin+=['SW_313t4']
	StormWind_Paladin+=['SW_313t4e']
class SW_313_Questline(TargetedAction):
	TARGET=ActionArg()
	AMOUNT=IntArg()
	TARGETEDACTION=ActionArg()
	def do(self, source, target, amount, targetedaction):
		if not target.id in source.sidequest_list0:
			if target.cost==1:
				source.sidequest_list0.append(target.id)
				if len(source.sidequest_list0)>=3:
					for action in targetedaction:
						action.trigger(source)
					Destroy(source).trigger(source)
		pass
	pass
class SW_313:# <5>[1578]
	""" Rise to the Occasion
	[Questline:] Play 3 different 1-Cost cards.[Reward:] Equip a 1/4 Light's Justice. """
	# Light's Justice  VAN_CS2_091 CS2_091 weapon
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}	
	events = Play(CONTROLLER).on(SW_313_Questline(Play.CARD, 3, [
		Summon(CONTROLLER, 'CS2_091'), 
		Summon(CONTROLLER, 'SW_313t')
		]))
	pass
#class SW_313e1:# <5>[1578]
#	""" Costs (1) less """
#	pass
class CS2_091:
	""" Light's Justice """
	pass
class SW_313t:# <5>[1578]
	""" Pave the Way
	&lt;b&gt;Questline: &lt;/b&gt; Play 3 different 1-Cost cards. &lt;b&gt;Reward:&lt;/b&gt; Upgrade your Hero Power."""
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}	
	events = Play(CONTROLLER).on(SW_313_Questline(Play.CARD, 3, [
		ChangeHeroPower(CONTROLLER, 'HERO_04bp2'),
		Summon(CONTROLLER, 'SW_313t2'), 
		]))
	pass
class SW_313t2:# <5>[1578]
	""" Avenge the Fallen
	&lt;b&gt;Questline:&lt;/b&gt; Play 3 different 1-Cost cards. &lt;b&gt;Reward:&lt;/b&gt; Lightborn Cariel."""
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}	
	events = Play(CONTROLLER).on(SW_313_Questline(Play.CARD, 3, [
		Give(CONTROLLER, 'SW_313t4') 
		]))
	pass

class SW_313t4:# <5>[1578]
	""" Lightborn Cariel
	&lt;b&gt;Battlecry:&lt;/b&gt; For the rest of the game, your Silver Hand Recruits have +2/+2."""
	pass

class SW_313t4e:# <5>[1578]
	tags={GameTag.ATL:2, GameTag.HEALTH:2}
	pass




if StormWind_Lightbringers_Hammer:# 
	StormWind_Paladin+=['SW_314']
class SW_314:# <5>[1578]
	""" Lightbringer's Hammer
	[Lifesteal]Can't attack heroes. """
	#
	pass




if StormWind_Alliance_Bannerman:# 
	StormWind_Paladin+=['SW_315']
class SW_315:# <5>[1578]
	""" Alliance Bannerman
	[Battlecry:] Draw a minion.Give minions in yourhand +1/+1. """
	#
	pass




if StormWind_Noble_Mount:# 
	StormWind_Paladin+=['SW_316']
	StormWind_Paladin+=['SW_316t']
class SW_316:# <5>[1578]
	""" Noble Mount
	Give a minion +1/+1and [Divine Shield].When it dies, summona Warhorse. """
	#
	pass

class SW_316t:# <5>[1578]
	pass




if StormWind_Catacomb_Guard:# 
	StormWind_Paladin+=['SW_317']
class SW_317:# <5>[1578]
	""" Catacomb Guard
	[Lifesteal][Battlecry:] Deal damageequal to this minion's Attackto an enemy minion. """
	#
	pass


