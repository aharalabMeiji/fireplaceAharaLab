from ..utils import *

Rev_DemonHunter=[]

Rev_Sightless_Magistrate=True##
Rev_All_Fel_Breaks_Loose=True##
Rev_Prosecutor_Meltranix=True##
Rev_Sinful_Brand=True##
Rev_Dispose_of_Evidence=True##
Rev_Relic_of_Dimensions=True##
Rev_Magnifying_Glaive=True#weapon
Rev_Kryxis_the_Voracious=True##
Rev_Bibliomite=True##
Rev_Artificer_Xymox=True##
Rev_Relic_Vault=True#location
Rev_Relic_of_Extinction=True##
Rev_Artificer_Xymox=True##
Rev_Relic_Vault=True##
Rev_Relic_of_Phantasms=True##


if Rev_Sightless_Magistrate:# 
	Rev_DemonHunter+=['MAW_008']
class MAW_008_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		if len(controller.hand)<5:
			amount=5-len(controller.hand)
			for repeat in range(amount):
				Draw(controller).trigger(source)
		if len(controller.opponent.hand)<5:
			amount=5-len(controller.opponent.hand)
			for repeat in range(amount):
				Draw(controller.opponent).trigger(source)
		pass
class MAW_008:# <14>[1691]
	""" Sightless Magistrate
	<b>Battlecry:</b> Both players draw until they have 5 cards. """
	play = MAW_008_Action(CONTROLLER)
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
class MAW_014_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		length=len(controller.opponent.hand)
		for i in range(length):
			if 0<i and i<length-1:
				Buff(controller.opponent.hand[i],'MAW_014e2').trigger(source)
		pass
class MAW_014:# <14>[1691]
	""" Prosecutor Mel'tranix
	<b>Battlecry:</b> Your opponent can only play their left-  and right-most cards on  their next turn. """
	play = MAW_014_Action(CONTROLLER)
	pass

	Rev_DemonHunter+=['MAW_014e2']
class MAW_014e2:# <14>[1691]
	""" Literally Unplayable
	You can only play the left and right-most cards in your hand. """
	#tags={GameTag.CANT_PLAY:1}
	def apply(self, target):
		target.cant_play=False
	events=BeginTurn(CONTROLLER).on(Destroy(SELF))
	pass





if Rev_Sinful_Brand:# 
	Rev_DemonHunter+=['REV_506']
	Rev_DemonHunter+=['REV_506e']
	#Rev_DemonHunter+=['REV_506e2']
class _Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		pass
class REV_506:# <14>[1691]
	""" Sinful Brand
	Brand an enemy minion. Whenever it takes damage, deal 2 damage to the enemy hero. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = Buff(TARGET, 'REV_506e')#
	pass
class REV_506e:# <14>[1691]
	""" Branded
	Whenever this takes damage, deal 2 damage to your hero. """
	events = Damage(OWNER).on(Hit(FRIENDLY_HERO, 2))
	pass
#class REV_506e2:# <14>[1691]
#	""" Branded
#	Costs (1) more. """
#	#
#	pass





if Rev_Dispose_of_Evidence:# 
	Rev_DemonHunter+=['REV_507']
class _Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		pass
class REV_507:# <14>[1691]
	""" Dispose of Evidence
	Give your hero +3 Attack this turn. Choose a card in your hand to shuffle into your deck. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	play = 	Buff(FRIENDLY_HERO, 'REV_507e'),Shuffle(CONTROLLER, TARGET)
	pass
	Rev_DemonHunter+=['REV_507e']
class REV_507e:# <14>[1691]
	""" Dispose of Evidence
	+3 Attack this turn. """
	tags={ GameTag.ATK:3 }
	events=BeginTurn(CONTROLLER).on(Destroy(SELF))
	#
	pass





if Rev_Relic_of_Dimensions:# 
	Rev_DemonHunter+=['REV_508']

	Rev_DemonHunter+=['REV_508e']
class REV_508_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		amount=controller.relic_improvision
		source.script_data_num_1=amount
		card1=Draw(controller).trigger(source)
		card1=card1[0]
		Buff(card1, 'REV_508e', cost = -amount)
		card2=Draw(controller).trigger(source)
		card2=card2[0]
		Buff(card2, 'REV_508e', cost = -amount)
		controller.relic_improvision+=1
		pass
class REV_508:# <14>[1691]
	""" Relic of Dimensions
	Draw two cards and reduce their Cost  by (@). Improve your future Relics. """
	def __init__(self):
		controller=self.controller
		self.script_data_num_1=controller.relic_improvision
	play = REV_508_Action(CONTROLLER)
	pass
class REV_508e:# <14>[1691]
	""" Dimensional
	Reduced Cost. """
	pass





if Rev_Magnifying_Glaive:# 
	Rev_DemonHunter+=['REV_509']
class REV_509_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		if len(controller.hand)<3:
			amount=3-len(controller.hand)
			for i in range(amount):
				Draw(controller).trigger(source)
		pass
class REV_509:# <14>[1691]
	""" Magnifying Glaive
	After your hero attacks, draw until you have 3 cards. """
	events = Attack(FRIENDLY_HERO, ENEMY).after(REV_509_Action(CONTROLLER))
	pass





if Rev_Kryxis_the_Voracious:# 
	Rev_DemonHunter+=['REV_510']
class REV_510:# <14>[1691]
	""" Kryxis the Voracious
	<b>Battlecry</b>: Discard your hand. <b>Deathrattle:</b> Draw 3 cards. """
	play = Discard(FRIENDLY_HAND)
	deathrattle = Draw(CONTROLLER), Draw(CONTROLLER), Draw(CONTROLLER)
	pass





if Rev_Bibliomite:# 
	Rev_DemonHunter+=['REV_511']
class REV_511_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		for hand in self.source.controller.hand:
			if hand.id==card.id:
				hand.zone=Zone.SETASIDE
				hand.zone=Zone.DECK
				self.source.controller.shuffle_deck()
				break
		pass
class REV_511_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		cards=[card.id for card in controller.hand]
		if len(cards)>3:
			cards=random.sample(cards, 3)
		REV_511_Choice(controller, RandomID(*cards)).trigger(source)
		pass
class REV_511:# <14>[1691]
	""" Bibliomite
	<b>Battlecry</b>: Choose a card  in your hand to shuffle  into your deck. """
	play = REV_511_Action(CONTROLLER)
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
class REV_834_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		if len(controller.opponent.field)>0:
			amount = controller.relic_improvision
			source.script_data_num_1 = amount
			Hit(random.choice(controller.opponent.field), amount).trigger(source)
			Hit(random.choice(controller.opponent.field), amount).trigger(source)
			controller.relic_improvision+=1
		pass
class REV_834:# <14>[1691]
	""" Relic of Extinction
	Deal $@ damage to a random enemy minion, twice. Improve your future Relics. """
	def __init__(self):
		controller=self.controller
		self.script_data_num_1=controller.relic_improvision
	play = REV_834_Action(CONTROLLER)
	pass





if Rev_Artificer_Xymox:# 
	Rev_DemonHunter+=['REV_937']

	Rev_DemonHunter+=['REV_937t']
class REV_937_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		CastSpell(card).trigger(self.source)
		pass
class REV_937:# <14>[1691]
	""" Artificer Xy'mox
	<b>Battlecry:</b> <b>Discover</b> and  cast a Relic. 
	<b>Infuse (@):</b>  Cast all three instead. """
	play = REV_937_Choice(CONTROLLER, RandomID('REV_508','REV_834','REV_943')*3)
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_937t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_937t', 1))
	#
	pass
class REV_937t_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		card = controller.card('REV_508')
		CastSpell(card).trigger(source)
		card = controller.card('REV_834')
		CastSpell(card).trigger(source)
		card = controller.card('REV_943')
		CastSpell(card).trigger(source)
		pass
class REV_937t:# <14>[1691]
	""" Artificer Xy'mox
	<b>Infused</b> <b>Battlecry:</b> Cast all three Relics. """
	play = REV_937t_Action(CONTROLLER)
	pass





if Rev_Relic_Vault:# ### OK ###
	Rev_DemonHunter+=['REV_942']
	Rev_DemonHunter+=['REV_942e']
class REV_942_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		for card in controller.hand:
			if getattr(card, 'relic', False):
				Buff(card, 'REV_942e').trigger(source)
		pass
class REV_942_Action2(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		for card in controller.hand:
			if getattr(card, 'relic', False):
				for buff in reversed(card.buffs):
					if buff.id=='REV_942e':
						card.spell_cast_twice=False
						card.buffs.remove(buff)
		pass
class REV_942:# <14>[1691]
	""" Relic Vault
	The next Relic you play this turn casts twice. """
	location = REV_942_Action(CONTROLLER)
	events = OWN_TURN_END.on(REV_942_Action2(CONTROLLER))
	pass
class REV_942e:# <14>[1691]
	""" Relic Empowerment
	Your Relics cast twice. """
	def apply(self, target):
		target.spell_cast_twice=True
	pass



if Rev_Relic_of_Phantasms:# ### OK ###
	Rev_DemonHunter+=['REV_943']
	Rev_DemonHunter+=['REV_943t']
class REV_943_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		amount = controller.relic_improvision
		source.script_data_num_1 = amount
		card1=Summon(controller, 'REV_943t').trigger(source)
		card1=card1[0][0]
		card1.atk=card1.data.tags[GameTag.ATK]=amount
		card1.max_health=card1.data.tags[GameTag.HEALTH]=amount
		card2=Summon(controller, 'REV_943t').trigger(source)
		card2=card2[0][0]
		card2.atk=card2.data.tags[GameTag.ATK]=amount
		card2.max_health=card2.data.tags[GameTag.HEALTH]=amount
		controller.relic_improvision+=1
		pass
class REV_943:# <14>[1691]
	""" Relic of Phantasms
	Summon two @/@ Spirits. Improve your future Relics. """
	def __init__(self):
		controller=self.controller
		self.script_data_num_1=controller.relic_improvision
	play = REV_943_Action(CONTROLLER)	#
	pass
class REV_943t:# <14>[1691]
	""" Fleeting Spirit
	 """
	#
	pass

