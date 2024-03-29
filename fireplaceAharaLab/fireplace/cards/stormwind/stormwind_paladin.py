
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





if StormWind_Wealth_Redistributor:# ### OK ###
	StormWind_Paladin+=['DED_500']
	StormWind_Paladin+=['DED_500e']
class DED_500:# <5>[1578]
	""" Wealth Redistributor
	[Taunt]. [Battlecry:] Swap the Attack of the highest and lowest Attack minion. """
	def play(self):
		lowest = []
		highest = []
		for card in self.controller.field:
			if lowest==[] or lowest[0].atk>card.atk:
				lowest=[card]
			elif lowest[0].atk==card.atk:
				lowest.append(card)
			if highest==[] or highest[0].atk<card.atk:
				highest=[card]
			elif highest[0].atk==card.atk:
				highest.append(card)
		if lowest!=[] and highest!=[]:
			lowest=random.choice(lowest)
			highest=random.choice(highest)
			if lowest.atk!=highest.atk:
				diff=highest.atk-lowest.atk
				Buff(lowest,'DED_500e', atk=diff).trigger(self)
				Buff(highest,'DED_500e2', atk=-diff).trigger(self)
	pass
class DED_500e:
	pass
@custom_card
class DED_500e2:
	tags={
		GameTag.CARDNAME:"Wealth Redistributor",
		GameTag.CARDTYPE:CardType.ENCHANTMENT,}
	pass



if StormWind_Sunwing_Squawker:# 
	StormWind_Paladin+=['DED_501']
class DED_501:# <5>[1578] OK
	""" Sunwing Squawker
	[Battlecry:] Repeat the last spell you've cast on a__friendly minion on this. """
	def play(self):	
		actions = [action for action in self.controller._targetedaction_log if isinstance(action['class'], Battlecry) and action['target'].controller==self.controller and action['source'].type==CardType.SPELL]
		if len(actions)>0:
			action=actions[-1]
			newcard = Give(self.controller, action['source'].id).trigger(self)
			if newcard[0]!=[]:
				newcard=newcard[0][0]
				Battlecry(newcard, self).trigger(self)
				newcard.zone=Zone.GRAVEYARD
	pass




if StormWind_Righteous_Defense:# 
	StormWind_Paladin+=['DED_502']
	StormWind_Paladin+=['DED_502e']
	StormWind_Paladin+=['DED_502e2']
class DED_502_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		atk=target.atk
		hlt=target.health
		Buff(target, 'DED_502e', atk=1-atk, max_health=1-hlt).trigger(source)
		if len(source.controller.hand)>0:
			card = random.choice(source.controller.hand)
			Buff(card, 'DED_502e2', atk=atk-1, max_health=hlt-1).trigger(source)
		pass

class DED_502:# <5>[1578]
	""" Righteous Defense
	Set a minion's Attack and Health to 1. Give the stats it lost to a minion in your hand. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0,PlayReq.REQ_TARGET_TO_PLAY: 0}
	play=DED_502_Action(TARGET)
	pass
class DED_502e:
	pass
class DED_502e2:
	pass



if StormWind_City_Tax:# 
	StormWind_Paladin+=['SW_046']
class SW_046:# <5>[1578]
	""" City Tax
	[Tradeable][Lifesteal]. Deal $1 damage to all enemy minions. """
	play = Hit(ENEMY_MINIONS, 1)
	pass




if StormWind_Highlord_Fordragon:# 
	StormWind_Paladin+=['SW_047','SW_047e']
class SW_047:# <5>[1578]
	""" Highlord Fordragon
	[Divine Shield]After a friendly minion loses[Divine Shield], give a minion__in your hand +5/+5. """
	events = LoseDivineShield(FRIENDLY_MINIONS).after(Buff(RANDOM(FRIENDLY_MINIONS), 'SW_047e'))
	pass
SW_047e=buff(5,5)



if StormWind_Prismatic_Jewel_Kit:# 
	StormWind_Paladin+=['SW_048']
class SW_048:# <5>[1578]
	""" Prismatic Jewel Kit
	After a friendly minion loses[Divine Shield], give minions in your hand  +1/+1. Lose 1 Durability. """
	events = LoseDivineShield(FRIENDLY_MINIONS).after(Buff(FRIENDLY_HAND + MINION, 'SW_047e'), Predamage(SELF,1))
	pass
SW_048e=buff(1,1)



if StormWind_Blessed_Goods:# ### OK ###
	StormWind_Paladin+=['SW_049']
class SW_049:# <5>[1578]
	""" Blessed Goods
	[Discover] a [Secret], weapon, or [Divine Shield] minion. """
	def play(self):
		secrets = RandomSpell(secret=True).evaluate(self)
		weapons = RandomWeapon().evaluate(self)
		shield_minions = RandomMinion(divine_shield=True).evaluate(self)
		self.entourage = [secrets[0].id, weapons[0].id, shield_minions[0].id]
		Discover(self.controller, RandomEntourage()).trigger(self)
	pass




if StormWind_First_Blade_of_Wrynn:# 
	StormWind_Paladin+=['SW_305']
class SW_305:# <5>[1578]
	""" First Blade of Wrynn (4/3/5)
	[Divine Shield][Battlecry:] Gain [Rush] if this has at least 4 Attack. """
	play = (ATK(SELF)>3) & SetTag(SELF, {GameTag.RUSH:True, })
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
	[Questline: ] Play 3 different 1-Cost cards. [Reward:] Upgrade your Hero Power."""
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}	
	events = Play(CONTROLLER).on(SW_313_Questline(Play.CARD, 3, [
		ChangeHeroPower(CONTROLLER, 'HERO_04bp2'),
		Summon(CONTROLLER, 'SW_313t2'), 
		]))
	pass
class SW_313t2:# <5>[1578]
	""" Avenge the Fallen
	[Questline:] Play 3 different 1-Cost cards. [Reward:] Lightborn Cariel."""
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}	
	events = Play(CONTROLLER).on(SW_313_Questline(Play.CARD, 3, [
		Give(CONTROLLER, 'SW_313t4') 
		]))
	pass

class SW_313t4:# <5>[1578]
	""" Lightborn Cariel
	[Battlecry:] For the rest of the game, your Silver Hand Recruits have +2/+2."""
	play = Buff(CONTROLLER, 'SW_313t4e')
	pass

class SW_313t4e:# <5>[1578]
	events = Summon(CONTROLLER, MINION+ID('CS2_101t')).on(Summon.CARD, 'SW_313t4e2')
	pass
@custom_card
class SW_313t4e2:# <5>[1578]
	tags={
		GameTag.CARDNAME:"Lightborn Cariel",
		GameTag.CARDTYPE:CardType.ENCHANTMENT,
		GameTag.ATK:2, GameTag.HEALTH:2
		}
	pass




if StormWind_Lightbringers_Hammer:# 
	StormWind_Paladin+=['SW_314']
class SW_314:# <5>[1578]
	""" Lightbringer's Hammer
	[Lifesteal]Can't attack heroes. """
	tags = {GameTag.CANNOT_ATTACK_HEROES:True, }
	pass




if StormWind_Alliance_Bannerman:# 
	StormWind_Paladin+=['SW_315','SW_315e']
class SW_315:# <5>[1578]
	""" Alliance Bannerman
	[Battlecry:] Draw a minion.Give minions in yourhand +1/+1. """
	play = Give(CONTROLLER, RANDOM(FRIENDLY_DECK+MINION)), Buff(FRIENDLY_HAND + MINION, 'SW_315e')
	pass
class SW_315e:
	tags={
		GameTag.ATK:1, GameTag.HEALTH:1		
		}


if StormWind_Noble_Mount:# first half OK
	StormWind_Paladin+=['SW_316','SW_316e']
	StormWind_Paladin+=['SW_316t']
class SW_316:# <5>[1578]
	""" Noble Mount
	Give a minion +1/+1and [Divine Shield].When it dies, summon a Warhorse. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0}
	play = Buff(TARGET, 'SW_316e'), GiveDivineShield(TARGET), 
	pass
class SW_316e:
	tags={
		GameTag.ATK:1, 
		GameTag.HEALTH:1		
		}
	events = Death(OWNER).on(Summon(CONTROLLER, 'SW_316t'))
	pass
class SW_316t:# <5>[1578]
	pass




if StormWind_Catacomb_Guard:# 
	StormWind_Paladin+=['SW_317']
class SW_317:# <5>[1578]
	""" Catacomb Guard
	[Lifesteal][Battlecry:] Deal damage equal to this minion's Attack to an enemy minion. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0}	
	play = Hit(TARGET, ATK(SELF))
	pass


