from imp import source_from_cache
from ..utils import *

Rev_Priest=[]

Rev_Clear_Conscience=True
Rev_Incriminating_Psychic=True
Rev_Theft_Accusation=True
Rev_Suspicious_Usher=True
Rev_The_Harvester_of_Envy=True
Rev_Mysterious_Visitor=True
Rev_Partner_in_Crime=True
Rev_Boon_of_the_Ascended=True
Rev_The_Light_It_Burns=True
Rev_Pelagos=True
Rev_Clean_the_Scene=True
Rev_Identity_Theft=True
Rev_Cathedral_of_Atonement=True


if Rev_Clear_Conscience:# 
	Rev_Priest+=['MAW_021']
	Rev_Priest+=['MAW_021e']
	Rev_Priest+=['MAW_021e2']
class MAW_021:# <6>[1691]
	""" Clear Conscience
	Give a friendly minion +2/+3 and "Only you can target this with spells and Hero Powers." """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	play = Buff(TARGET, 'MAW_021e'),Buff(FRIENDLY_MINIONS - TARGET, 'MAW_021e2')
	pass
MAW_021e=buff(2,3)
class MAW_021e2:# <6>[1691]
	""" In the Clear
	Can't be targeted by spells or Hero Powers. """
	#<Tag enumID="311" name="CANT_BE_TARGETED_BY_SPELLS" type="Int" value="1"/>
	#<Tag enumID="332" name="CANT_BE_TARGETED_BY_HERO_POWERS" type="Int" value="1"/>	#
	pass



if Rev_Incriminating_Psychic:# 
	Rev_Priest+=['MAW_022']
class MAW_022_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		if len(controller.opponent.hand)>0:
			card = random.choice(controller.opponent.hand)
			card = Give(controller, card.id).trigger(source)
			if isinstance(card, list):
				card = card[0]
			if isinstance(card, list):
				card = card[0]
			card.copied_from_opponent = True
		pass
class MAW_022:# <6>[1691]
	""" Incriminating Psychic
	<b>Taunt</b>  <b>Deathrattle:</b> Copy a  random card from your opponent's hand. """
	deathrattle = MAW_022_Action(CONTROLLER)#
	pass




if Rev_Theft_Accusation:# 
	Rev_Priest+=['MAW_023']
	Rev_Priest+=['MAW_023e']
class MAW_023:# <6>[1691]
	""" Theft Accusation
	Choose a minion. Destroy it after you play a card copied from the opponent. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	play = Buff(TARGET, 'MAW_023e')
	pass
class MAW_023_Action(TargetedAction):
	CONTROLLER=ActionArg()
	CARD=CardArg()
	def do(self, source, controller, card):
		if getattr(card, 'copied_from_opponent', False):
			Destroy(source.owner).trigger(source.owner)
		pass
class MAW_023e:# <6>[1691]
	""" Theft Trial
	When you play a card copied from your opponent, destroy the accused. """
	events = Play(CONTROLLER).after(MAW_023_Action(CONTROLLER, Play.CARD))
	pass
#	Rev_Priest+=['MAW_023e2']
#class MAW_023e2:# <6>[1691]
#	""" Accused of Theft
#	When the accuser plays a card copied from their enemy, this minion dies. """
#	#
#	pass




if Rev_Suspicious_Usher:# 
	Rev_Priest+=['REV_002', 'REV_000e']
class REV_002_Choice(Choice):
	def do(self, source, player, cards, option=None):
		source.sidequest_list0=[[card.id for card in cards]]
		super().do(source, player, cards, option)
	def choose(self, card):
		self.next_choice=None
		self.source.sidequest_list0.append(card.id)
		super().choose(card)
		buff=Buff(self.player.opponent, 'REV_000e')
		buff.trigger(self.player.opponent)
		buff.buff.sidequest_list0=[self.source.sidequest_list0[0],self.source.sidequest_list0[1]]
class REV_002:# <4>[1691]
	""" Suspicious Usher
	<b>Battlecry:</b> <b>Discover</b> a <b>Legendary</b> minion. If your opponent guesses your __choice, they get a copy. """	
	def play(self):
		source=self
		controller=self.controller
		opponent=controller.opponent
		choice=REV_002_Choice(controller, RandomLegendaryMinion()*3)
		choice.trigger(source)
		pass
	pass




if Rev_The_Harvester_of_Envy:# 
	Rev_Priest+=['REV_011']
class REV_011_Action(TargetedAction):
	CONTROLLER=ActionArg()
	CARD=CardArg()
	def do(self, source, controller, card):
		if getattr(card, 'copied_from_opponent', False):
			for target in controller.opponent.hand:
				if target.id==card.id:
					target.zone=Zone.SETASIDE
					target.controller=controller
					target.zone=Zone.HAND
					target.copied_from_opponent=True
		pass
class REV_011:# <6>[1691]
	""" The Harvester of Envy
	After you play a card copied from the opponent, steal the original. """
	events = Play(CONTROLLER).after(REV_011_Action(CONTROLLER, Play.CARD))
	pass
#	Rev_Priest+=['REV_011e']
#class REV_011e:# <6>[1691]
#	""" Copied From Opponent
#	 """
#	#
#	pass




if Rev_Mysterious_Visitor:# 
	Rev_Priest+=['REV_246']
	Rev_Priest+=['REV_246e2']
class REV_246:# <6>[1691]
	""" Mysterious Visitor
	<b>Battlecry:</b> Reduce the Cost of cards copied from your opponent by (2). """
	def play(self):
		controller=self.controller
		source=self
		for card in controller.hand:
			if getattr(card, 'copied_from_opponent', False):
				Buff(card, 'REV_246e2').trigger(source)
	pass
class REV_246e2:# <6>[1691]
	""" Mind Read
	Costs (2) less. """
	cost = lambda self, i:max(0,i-2)
	pass




if Rev_Partner_in_Crime:# 
	Rev_Priest+=['REV_247']
	Rev_Priest+=['REV_247e']
class REV_247:# <6>[1691]
	""" Partner in Crime
	<b>Battlecry:</b> Summon a  copy of this minion at  the end of your turn. """
	play = Buff(SELF, 'REV_247e')#
	pass
class REV_247e:# <6>[1691]
	""" Alibi
	At the end of your turn, summon a copy of this. """
	events = OWN_TURN_END.on(Summon(CONTROLLER, Copy(OWNER)))
	pass




if Rev_Boon_of_the_Ascended:# 
	Rev_Priest+=['REV_248']
	Rev_Priest+=['REV_248e']
	Rev_Priest+=['REV_248t']
class REV_248_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		Buff(source.target,'REV_248e').trigger(source)
		card=Summon(controller, 'REV_248t').trigger(source)
		if card[0]==[]:
			return
		card=card[0][0]
		card.atk=source.target.atk
		card.max_health=source.target.max_health
		pass
class REV_248:# <6>[1691]
	""" Boon of the Ascended
	Give a minion +2 Health. Summon a Kyrian with its stats and <b>Taunt</b>. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }#
	play = REV_248_Action(CONTROLLER)
	pass
REV_248e=buff(0,2)
class REV_248t:# <6>[1691]
	""" Ascended Kyrian (1/1/1)
	<b>Taunt</b> """
	#
	pass




if Rev_The_Light_It_Burns:# 
	Rev_Priest+=['REV_249']
class REV_249:# <6>[1691]
	""" The Light! It Burns!
	Deal damage to a minion  equal to its Attack. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }	#
	play = Hit(TARGET, ATK(TARGET))
	pass




if Rev_Pelagos:# 
	Rev_Priest+=['REV_250']
	Rev_Priest+=['REV_250e1']
class REV_250_Action(TargetedAction):
	CONTROLLER=ActionArg()
	CARD=CardArg()
	def do(self, source, controller, card):
		atk=card.atk
		health=card.max_health 
		if atk<health:
			Buff(card, 'REV_250e1', atk=health-atk).trigger(source)
		if atk>health:
			Buff(card, 'REV_250e1', max_health=atk-health).trigger(source)
		pass
class REV_250:# <6>[1691]
	""" Pelagos
	After you cast a spell  on a friendly minion, set  its Attack and Health to  the higher of the two. """
	events = Play(CONTROLLER, SPELL, FRIENDLY + MINION).after(REV_250_Action(CONTROLLER, Play.TARGET))
	pass
class REV_250e1:# <6>[1691]
	""" Pelagos' Blessing
	Stats set to the higher value. """
	#
	pass

#	Rev_Priest+=['REV_250e2']
#class REV_250e2:# <6>[1691]
#	""" Pelagos' Blessing
#	Stats set to the higher value. """
#	#
#	pass




if Rev_Clean_the_Scene:# 
	Rev_Priest+=['REV_252']
	Rev_Priest+=['REV_252t']
class REV_252:# <6>[1691]
	""" Clean the Scene
	Destroy all minions with 3 or less Attack. <b>Infuse (@):</b> 6 or less. """
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_252t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_252t', 1))
	def play(self):#
		source=self
		controller=self.controller
		for card in reversed(controller.field):
			if card.atk<=3:
				card.discard()
		opponent=controller.opponent
		for card in reversed(opponent.field):
			if card.atk<=3:
				card.discard()
	pass

class REV_252t:# <6>[1691]
	""" Clean the Scene
	<b>Infused</b> Destroy all minions with  6 or less Attack. """
	def play(self):#
		source=self
		controller=self.controller
		for card in reversed(controller.field):
			if card.atk<=6:
				card.discard()
		opponent=controller.opponent
		for card in reversed(opponent.field):
			if card.atk<=6:
				card.discard()
	pass

if Rev_Identity_Theft:# 
	Rev_Priest+=['REV_253']
class REV_253_Choice(Choice):
	def choose(self, card):
		controller=self.source.controller
		self.source._sidequest_counter_+=1
		if self.source._sidequest_counter_==1:
			cards = [card.id for card in controller.opponent.deck]
			cards = random.sample(cards, 3)
			choice=REV_253_Choice(controller, RandomID(*cards)*3)
			choice.trigger(self.source)
			self.next_choice=choice
			super().choose(card)
		if self.source._sidequest_counter_==2:
			self.next_choice=None
			super().choose(card)
		pass
class REV_253_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		cards = [card.id for card in controller.opponent.hand]
		if len(cards)>3:
			cards = random.sample(cards, 3)
		REV_253_Choice(controller, RandomID(*cards)*3).trigger(source)
		pass
class REV_253:# <6>[1691]
	""" Identity Theft
	<b>Discover</b> a copy of a card from your opponent's hand and deck. """
	play = REV_253_Action(CONTROLLER)
	pass




if Rev_Cathedral_of_Atonement:# 
	Rev_Priest+=['REV_290']
	Rev_Priest+=['REV_290e']
class REV_290:# <6>[1691]
	""" Cathedral of Atonement
	Give a minion +2/+1 and draw a card. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }	#
	location = Buff(TARGET, 'REV_290e'), Draw(CONTROLLER)
	pass
REV_290e=buff(2,1)

#if Rev_Pelagos:# 
#	Rev_Priest+=['REV_781']
#class REV_781:# <6>[1691]
#	""" Pelagos
#	{0} {1} {2} {3} """
#	#
#	pass

#if Rev_Cathedral_of_Atonement:# 
#	Rev_Priest+=['REV_791']
#class REV_791:# <6>[1691]
#	""" Cathedral of Atonement
#	{0} {1} """
#	#
#	pass

