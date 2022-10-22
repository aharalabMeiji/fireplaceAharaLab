from ..utils import *

Rev_Neutral=[]

Rev_Soul_Seeker=True## new 24.4#
Rev_Afterlife_Attendant=True## new 24.4#
Rev_Tight_Lipped_Witness=True## new 24.4#
Rev_Sylvanas_the_Accused=True## new 24.4#
Rev_The_Jailer=True## new 24.4#
Rev_Bog_Beast=True#
Rev_Stoneborn_Accuser=True#
Rev_Red_Herring=True#
Rev_Masked_Reveler=True#
Rev_Crooked_Cook=True#
Rev_Insatiable_Devourer=True#
Rev_Prince_Renathal=True#
Rev_Famished_Fool=True#
Rev_Dinner_Performer=True#
Rev_Kaelthas_Sinstrider=True#
Rev_Murloc_Holmes=True ### difficult!#
Rev_Demolition_Renovator=True#
Rev_Theotar_the_Mad_Duke=True# ### OK ###
Rev_Sinrunner=True#
Rev_Maze_Guide=True#
Rev_Dredger_Staff=True#
Rev_Roosting_Gargoyle=True#
Rev_Party_Crasher=True#
Rev_Stoneborn_General=True#
Rev_Invitation_Courier=True#
Rev_Forensic_Duster=True#
Rev_Muck_Plumber=True#
Rev_Sinstone_Totem=True#
Rev_Anonymous_Informant=True#
Rev_Sinfueled_Golem=True#
Rev_Volatile_Skeleton=True#
Rev_Scuttlebutt_Ghoul=True#
Rev_Dispossessed_Soul=True#
Rev_Sire_Denathrius=True#
Rev_Creepy_Painting=True#
Rev_Sketchy_Stranger=True#
Rev_Steamcleaner=True#
Rev_Priest_of_the_Deceased=True#
Rev_Murlocula=True#
Rev_Ashen_Elemental=True#


if Rev_Soul_Seeker:# 
	Rev_Neutral+=['MAW_004']
class MAW_004_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=target
		opponent=controller.opponent
		deck_minion=[card for card in opponent.deck if card.type==CardType.MINION]
		if len(deck_minion)>0:
			mycard=source
			hiscard=random.choice(deck_minion)
			mycard.zone=Zone.SETASIDE
			hiscard.zone=Zone.SETASIDE
			mycard.controller=opponent
			hiscard.controller=controller
			mycard.zone=Zone.DECK
			Summon(controller, hiscard).trigger(source)
		pass
class MAW_004:# <12>[1691]
	""" Soul Seeker
	<b>Battlecry:</b> Swap this with a random minion from your opponent's deck. """
	play = MAW_004_Action(CONTROLLER)
	pass





if Rev_Afterlife_Attendant:# 
	Rev_Neutral+=['MAW_031']
	Rev_Neutral+=['MAW_031e']
class MAW_031_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		for buff in controller.buffs:
			if buff.id=='MAW_031e':
				controller.buffs.remove(buff)
				buff.discard()
				controller.infuse_in_deck=False
class MAW_031:# <12>[1691]
	""" Afterlife Attendant
	Your <b>Infuse</b> cards also <b>Infuse</b> while in your deck. """
	play=Buff(CONTROLLER, 'MAW_031e')
	events = Death(MINION + SELF).on(MAW_031_Action(CONTROLLER))
	pass

class MAW_031e:# <12>[1691]
	""" Afterlife
	Your <b>Infuse</b> cards also <b>Infuse</b> in your deck. """
	def apply(self, target):
		if hasattr(target, 'infuse_in_deck'):
			target.infuse_in_deck=True
	pass





if Rev_Tight_Lipped_Witness:# 
	Rev_Neutral+=['MAW_032']
class MAW_032_Action0(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		controller.cant_reveal_secret=True
		pass
class MAW_032_Action1(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		controller.cant_reveal_secret=False
		pass
class MAW_032:# <12>[1691]
	""" Tight-Lipped Witness
	<b>Secrets</b> can't be revealed. """
	play = MAW_032_Action0(CONTROLLER)
	events=Death(MINION + SELF).on(MAW_032_Action1(CONTROLLER))
	pass





if Rev_Sylvanas_the_Accused:# 
	Rev_Neutral+=['MAW_033']
	Rev_Neutral+=['MAW_033t']
class MAW_033:# <12>[1691]
	""" Sylvanas, the Accused
	<b>Battlecry:</b> Destroy an enemy minion. 
	<b>Infuse (@):</b> Take control of it instead. """
	#<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="7"/>
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = Destroy(TARGET)
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'MAW_033t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'MAW_033t',1))
	pass
class MAW_033t_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		assert target.type==CardType.MINION
		assert target.zone==Zone.PLAY
		target.zone=Zone.SETASIDE
		target.controller=source.controller
		target.zone=Zone.PLAY
		pass
class MAW_033t:# <12>[1691]
	""" Sylvanas, the Accused
	<b>Infused</b> <b>Battlecry:</b> Take control of an enemy minion. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = MAW_033t_Action(TARGET)
	#
	pass





if Rev_The_Jailer:# 
	Rev_Neutral+=['MAW_034']
	#Rev_Neutral+=['MAW_034e']
	#Rev_Neutral+=['MAW_034e2']
class MAW_034_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		for card in reversed(controller.deck):
			card.discard()
		for card in controller.field:
			card.cant_be_damaged=True
		pass
class MAW_034:# <12>[1691]
	""" The Jailer
	<b>Battlecry:</b> Destroy your  deck. For the rest of the game, your minions are <b>Immune</b>. """
	play = MAW_034_Action(CONTROLLER)
	pass
#class MAW_034e:# <12>[1691]
#	""" Mawsworn
#	Your minions are <b>Immune</b> """
#	#
#	pass
#class MAW_034e2:# <12>[1691]
#	""" Mawsworn
#	Can't die. """
#	#
#	pass




if Rev_Bog_Beast:# 
	Rev_Neutral+=['REV_012']
	Rev_Neutral+=['REV_012t']
class original_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=target
		pass
class REV_012:# <12>[1691]
	""" Bog Beast
	<b><b>Taunt</b></b>  <b>Deathrattle:</b> Summon a 2/4  Muckmare with <b>Taunt</b>. """
	deathrattle = Summon(CONTROLLER, 'REV_012t')
	pass
class REV_012t:# <12>[1691]
	""" Muckmare
	<b>Taunt</b> """
	#
	pass



if Rev_Stoneborn_Accuser:# ### OK ###
	Rev_Neutral+=['REV_013']
	Rev_Neutral+=['REV_013t']
class REV_013:# <12>[1691]
	""" Stoneborn Accuser
	<b>Infuse (@):</b> Gain "<b>Battlecry:</b> Deal 5 damage." """
	#<Tag enumID="2456" name="INFUSE" type="Int" value="1"/>
	#<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="5"/>
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_013t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_013t', 1))
	pass
class REV_013t:# <12>[1691]
	""" Stoneborn Accuser
	<b>Infused</b> <b>Battlecry:</b> Deal 5 damage. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = Hit(TARGET, 5)
	pass





if Rev_Red_Herring:# 
	Rev_Neutral+=['REV_014']
class REV_014_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		for card in controller.field:
			if card.id!='REV_014':
				card.stealthed=True
		pass
class REV_014:# <12>[1691]
	""" Red Herring
	<b>Taunt</b> Your non-Red Herring minions have <b>Stealth</b>. """
	play = REV_014_Action(CONTROLLER)
	pass





if Rev_Masked_Reveler:# 
	Rev_Neutral+=['REV_015']
	Rev_Neutral+=['REV_015t']
class REV_015_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		cardIDs = [card.id for card in controller.deck if card.type==CardType.MINION and card.id!='REV_015']
		if len(cardIDs)>2:
			cardIDs=random.sample(cardIDs, 2)
		for cardID in cardIDs:
			newcard=Summon(controller, cardID).trigger(source)
			newcard=newcard[0][0]
			Buff(newcard, 'REV_015t')
		pass
class REV_015:# <12>[1691]
	""" Masked Reveler
	<b>Rush</b> <b>Deathrattle:</b> Summon a 2/2 copy of another minion in your deck. """
	deathrattle = REV_015_Action(CONTROLLER)
	pass
class REV_015t:# <12>[1691] enchantment
	""" Masked 	2/2. """
	atk=lambda self,i:2
	max_health=lambda self,i:2
	pass





if Rev_Crooked_Cook:# 
	Rev_Neutral+=['REV_016']
	#Rev_Neutral+=['REV_016e']
class REV_016_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		if controller.opponent.hero.damage>=3:
			Draw(controller).trigger(source)
		pass
class REV_016:# <12>[1691]
	""" Crooked Cook
	At the end of your turn,  if you dealt 3 or more  damage to the enemy  hero, draw a card. """
	events = OWN_TURN_END.on(REV_016_Action(CONTROLLER))
	pass
#class REV_016e:# <12>[1691]
#	""" Suspicious Soup
#	<b>Poisonous</b> """
#	#
#	pass





if Rev_Insatiable_Devourer:# ### OK ###
	Rev_Neutral+=['REV_017']
	Rev_Neutral+=['REV_017e']
	Rev_Neutral+=['REV_017t']
class REV_017:# <12>[1691]
	""" Insatiable Devourer
	<b>Battlecry:</b> Devour an enemy  minion and gain its stats.  _
	<b>Infuse (@):</b> And its neighbors. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = EatsMinion(SELF, TARGET, 1, 'REV_017e')#
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_017t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_017t', 1))
	pass
class REV_017e:# <12>[1691]
	""" Satiated
	Increased Stats """
	#
	pass
class REV_017t_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=source.controller
		if target in controller.opponent.field:
			index = controller.opponent.field.index(target)
			if index<len(controller.opponent.field)-1:
				EatsMinion(source, controller.opponent.field[index+1], 1, 'REV_017e').trigger(source)
			EatsMinion(source, target, 1, 'REV_017e').trigger(source)
			if index>0:
				EatsMinion(source, controller.opponent.field[index-1], 1, 'REV_017e').trigger(source)
		pass
class REV_017t:# <12>[1691]
	""" Insatiable Devourer
	<b>Infused</b> <b>Battlecry:</b> Devour an enemy minion and its neighbors to gain their stats. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play=REV_017t_Action(TARGET)
	pass





if Rev_Prince_Renathal:# 
	Rev_Neutral+=['REV_018']
class REV_018:# <12>[1691]
	""" Prince Renathal
	Your deck size and starting Health are 40. """
	#
	pass





if Rev_Famished_Fool:# 
	Rev_Neutral+=['REV_019']
	Rev_Neutral+=['REV_019t']
class REV_019:# <12>[1691]
	""" Famished Fool
	<b>Battlecry:</b> Draw a card. 
	<b>Infuse (@):</b> Draw 3 instead. """
	play = Draw(CONTROLLER)
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_019t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_019t', 1))
	pass

class REV_019t:# <12>[1691]
	""" Famished Fool
	<b>Infused</b> <b>Battlecry:</b> Draw 3 cards. """
	play = Draw(CONTROLLER),Draw(CONTROLLER),Draw(CONTROLLER)
	pass





if Rev_Dinner_Performer:# 
	Rev_Neutral+=['REV_020']
class REV_020_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		cards = [card for card in controller.deck if card.type==CardType.MINION and card.cost<=controller.mana]
		if len(cards)>0:
			card = random.choice(cards)
			card.zone = Zone.HAND
		pass
class REV_020:# <12>[1691]
	""" Dinner Performer
	<b>Battlecry:</b> Summon a random minion from your deck that you can afford to play. """
	play = REV_020_Action(CONTROLLER)
	pass





if Rev_Kaelthas_Sinstrider:# 
	Rev_Neutral+=['REV_021']
	Rev_Neutral+=['REV_021e']
class REV_021_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		if len(controller.play_this_turn)%3==2:
			for card in controller.hand:
				Buff(card, 'REV_021e').trigger(source)
		pass
class REV_021:# <12>[1691]
	""" Kael'thas Sinstrider
	Every third minion you play each turn costs (0). """
	events = Play(CONTROLLER, MINION).on(REV_021_Action(CONTROLLER))
	pass
class REV_021e:# <12>[1691]
	""" Sinstrider 	Costs (0). """
	cost = lambda self, i: 0
	events = Play(CONTROLLER, MINION).on(Destroy(SELF))
	pass





if Rev_Murloc_Holmes:# ####  OK ###
	Rev_Neutral+=['REV_022']
def REV_022_Sub(opponent):
	if len(opponent.hand)==0:
		return []
	card = random.choice(opponent.hand)
	card_class = opponent.hero.data.card_class
	hand_id=[c.id for c in opponent.hand]
	for repeat in range(10):
		if card.type==CardType.MINION:
			card2 = RandomMinion(card_class=card_class).evaluate(opponent)
			card2 = card2[0]
			if hand_id in hand_id:
				continue
			else:
				return [card.id, card2.id]
		else:
			card2 = RandomSpell(card_class=card_class).evaluate(opponent)
			card2 = card2[0]
			if hand_id in hand_id:
				continue
			else:
				return [card.id, card2.id]
		pass
	return []
class REV_022_Choice(Choice):
	def choose(self, card):
		if card!=None:
			hand_id=[c.id for c in self.player.opponent.hand]
			if card.id in hand_id:
				Give(self.player, card.id).trigger(self.source)
		self.source._sidequest_counter_ += 1
		if self.source._sidequest_counter_>=3:
			self.next_choice=None
		else:
			cards=REV_022_Sub(self.player.opponent)
			if cards==[]:
				self.next_choice=None
			else:
				self.next_choice=REV_022_Choice(self.player, RandomID(*cards)*2)
				self.next_choice.trigger(self.source)
			pass
		super().choose(card)
class REV_022_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		opponent = controller.opponent
		cards=REV_022_Sub(opponent)
		if cards==[]:
			return
		else:
			choice=REV_022_Choice(controller, RandomID(*cards)*2)
			choice.trigger(source)
		pass
class REV_022:# <12>[1691]
	""" Murloc Holmes
	<b>Battlecry:</b> Solve 3 Clues about your opponent's cards  to get copies of them. """
	play = REV_022_Action(CONTROLLER)
	pass





if Rev_Demolition_Renovator:# 
	Rev_Neutral+=['REV_023']
class REV_023_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		cards = [card for card in controller.opponent.field if card.type==CardType.LOCATION]
		if len(cards)>0:
			card = random.choice(cards)
			Destroy(card).trigger(source)
		pass
class REV_023:# <12>[1691]
	""" Demolition Renovator
	<b>Battlecry:</b> Destroy  an enemy location. """
	play = REV_023_Action(CONTROLLER)
	pass





if Rev_Theotar_the_Mad_Duke:# ### OK ###
	Rev_Neutral+=['REV_238']
class REV_238_Choice(Choice):
	def choose(self, card):
		source = self.source
		controller = source.controller
		source._sidequest_counter_ += 1
		if source._sidequest_counter_==1:
			source.sidequest_list0=[card]
			self.next_choice = REV_238_Choice(controller, RandomID(*(source._sidequest_list2_))*3)
			self.next_choice.trigger(self.source)
			pass
		elif source._sidequest_counter_==2:
			source.sidequest_list0+=[card]
			self.next_choice = None
			## call back
			cards1=[card for card in controller.hand if card.id==source.sidequest_list0[0].id]
			if len(cards1)>0:
				card1=random.choice(cards1)
				cards2=[card for card in controller.opponent.hand if card.id==source.sidequest_list0[1].id]
				if len(cards2)>0:
					card2=random.choice(cards2)
					## swapping
					card1.zone=Zone.SETASIDE
					card2.zone=Zone.SETASIDE
					card1.controller=controller.opponent
					card2.controller=controller
					card1.zone=Zone.HAND
					card2.zone=Zone.HAND
		else:
			self.next_choice = None ## does not occur
		super().choose(card)
class REV_238_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		source._sidequest_list1_=[card.id for card in controller.hand]
		source._sidequest_list2_=[card.id for card in controller.opponent.hand]
		REV_238_Choice(controller, RandomID(*(source._sidequest_list1_))*3).trigger(source)
		pass
class REV_238:# <12>[1691]
	""" Theotar, the Mad Duke
	<b>Battlecry:</b> <b>Discover</b> a card in each player's hand and swap them. """
	play = REV_238_Action(CONTROLLER)
	pass





if Rev_Sinrunner:# 
	Rev_Neutral+=['REV_251']
class REV_251:# <12>[1691]
	""" Sinrunner
	<b>Deathrattle:</b> Destroy a random enemy minion. """
	deathrattle = Destroy(RANDOM(ENEMY_MINIONS))
	pass





if Rev_Maze_Guide:# 
	Rev_Neutral+=['REV_308']
class REV_308:# <12>[1691]
	""" Maze Guide
	<b>Battlecry</b>: Summon a random 2-Cost minion. """
	play = Summon(CONTROLLER, RandomMinion(cost=2))
	pass





if Rev_Dredger_Staff:# 
	Rev_Neutral+=['REV_338']
	Rev_Neutral+=['REV_338e']
class REV_338:# <12>[1691]
	""" Dredger Staff
	<b>Battlecry:</b> Give minions  in your hand +1 Health. """
	play = Buff(FRIENDLY_HAND, 'REV_338e')
	pass
REV_338e=buff(0,1)





if Rev_Roosting_Gargoyle:# 
	Rev_Neutral+=['REV_351']
	Rev_Neutral+=['REV_351e']
class REV_351:# <12>[1691]
	""" Roosting Gargoyle
	<b>Battlecry:</b> Give a friendly Beast +2 Attack. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE:Race.BEAST }	
	play = Buff(TARGET, 'REV_338e')
	pass
REV_351e=buff(2,0)





if Rev_Party_Crasher:# 
	Rev_Neutral+=['REV_370']
class REV_370_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=source.controller
		cards=[card for card in controller.hand if card.type==CardType.MINION]
		if len(cards)>0:
			card = random.choice(cards)
			Hit(target, card.atk).trigger(source)# throw
			card.discard()
		pass
class REV_370:# <12>[1691]
	""" Party Crasher
	<b>Battlecry:</b> Choose an enemy minion. Throw a random minion from your hand at it. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = REV_370_Action(TARGET)
	pass





if Rev_Stoneborn_General:# 
	Rev_Neutral+=['REV_375']
	Rev_Neutral+=['REV_375t']
class REV_375:# <12>[1691]
	""" Stoneborn General
	<b>Rush</b>  __<b>Deathrattle:</b> Summon an  ___8/8 Gravewing with <b>Rush</b>._ """
	deathrattle = Summon(CONTROLLER, 'REV_375t')
	pass
class REV_375t:# <12>[1691]
	""" Gravewing
	<b>Rush</b> """
	pass





if Rev_Invitation_Courier:# ### OK ###
	Rev_Neutral+=['REV_377']
class REV_377_Action(TargetedAction):
	CONTROLLER=ActionArg()
	CARD=ActionArg()
	def do(self, source, controller, card):
		if card.card_class != CardClass.NEUTRAL and card.card_class != controller.hero.card_class:
			if card not in source.sidequest_list0:
				newcard = controller.card(card.id)
				newcard.controller=controller
				newcard.zone=Zone.HAND
		pass
class REV_377:# <12>[1691]
	""" Invitation Courier
	After a card is added to your hand from another class, copy it. """
	events = [
		Draw(CONTROLLER).after(REV_377_Action(CONTROLLER, Draw.CARD)),
		Give(CONTROLLER).after(REV_377_Action(CONTROLLER, Give.CARD))
		]
	pass





if Rev_Forensic_Duster:# 
	Rev_Neutral+=['REV_378']
	Rev_Neutral+=['REV_378e']
	Rev_Neutral+=['REV_378e2']
class REV_378:# <12>[1691]
	""" Forensic Duster
	<b>Battlecry:</b> Your  opponent's minions  cost (1) more next turn. """
	play = Buff(CONTROLLER, 'REV_378e')
	pass
class REV_378e:# <12>[1691]
	""" Dusting
	Your minions cost (1) more this turn. """
	def apply(self, target):
		controller = target
		for card in controller.opponent.field:
			Buff(card, 'REV_378e2').trigger(self.source)
	pass
class REV_378e2:# <12>[1691]
	""" Discovered!
	Costs (1) more. """
	cost = lambda self, i : i+1
	events = EndTurn(CONTROLLER).on(Destroy(SELF))
	pass





#if Rev_Murloc_Holmes:# #not in service
#	Rev_Neutral+=['REV_770']
#	Rev_Neutral+=['REV_770hp']
#class REV_770:# <12>[1691]
#	""" Murloc Holmes	 """
#	#
#	pass
#class REV_770hp:# <12>[1691]
#	""" Accuse
#	<b>Hero Power</b> Make an accusation! """
#	#
#	pass





#if Rev_Investigate:# #not in service
#	Rev_Neutral+=['REV_771']
#class REV_771:# <12>[1691]
#	""" Investigate
#	Search for clues. """
#	#
#	pass





if Rev_Muck_Plumber:# 
	Rev_Neutral+=['REV_837']
	Rev_Neutral+=['REV_837e']
class REV_837:# <12>[1691]
	""" Muck Plumber
	ALL minions cost (2) more. """
	play = Buff(FRIENDLY_HAND, 'REV_837e'), Buff(ENEMY_HAND, 'REV_837e')
	pass
class REV_837e:# <12>[1691]
	""" Yuck!
	Costs (2) more. """
	cost = lambda self, i : i+2
	pass





if Rev_Sinstone_Totem:# 
	Rev_Neutral+=['REV_839']
	Rev_Neutral+=['REV_839e']
class original_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=target
		pass
class REV_839:# <12>[1691]
	""" Sinstone Totem
	At the end of your turn, gain +1 Health. """
	events = EndTurn(CONTROLLER).on(Buff(SELF, 'REV_839e'))
	pass
REV_839e=buff(0,1)





if Rev_Anonymous_Informant:# 
	Rev_Neutral+=['REV_841']
	Rev_Neutral+=['REV_841e','REV_841e2']
class original_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=target
		pass
class REV_841:# <12>[1691]
	""" Anonymous Informant
	<b>Battlecry:</b> The next <b>Secret</b> you play costs (0). """
	play = Buff(FRIENDLY_HAND + SECRET, 'REV_841e')
	pass

class REV_841e:# <12>[1691]
	""" Informed
	Your next Secret costs (0). """
	cost = lambda self, i : 0
	events = Play(CONTROLLER, SECRET).on(Destroy(SELF))
	pass
class REV_841e2:# <4>[1691]
	""" Informed
	Your next Secret costs (0). """
	#
	pass




if Rev_Sinfueled_Golem:# ### OK ###
	Rev_Neutral+=['REV_843']
	Rev_Neutral+=['REV_843e']
	Rev_Neutral+=['REV_843t']
class REV_843_Action(TargetedAction):
	TARGET=ActionArg()
	ENTITY=ActionArg()
	OPTION=IntArg()
	def do(self, source, target, entity, option):
		controller=target
		if option==1 and controller.infuse_in_deck==False:
			return
		source._sidequest_list1_.append(entity.atk)
		newcard=Infuse(controller, 'REV_843t').trigger(source)
		if isinstance(newcard, list):
			newcard = newcard[0]
		if newcard!=None:
			amount=sum(source._sidequest_list1_)
			Buff(newcard, 'REV_843e', atk=amount, max_health=amount).trigger(source)
		pass
class REV_843:# <12>[1691]
	""" Sinfueled Golem
	<b>Infuse (@):</b> Gain stats equal to the Attack of the minions that <b>Infused</b> this. """
	#<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="3"/>
	class Hand:
		events = Death(FRIENDLY+MINION).on(REV_843_Action(CONTROLLER, Death.ENTITY, 0))
	class Deck:
		events = Death(FRIENDLY+MINION).on(REV_843_Action(CONTROLLER, Death.ENTITY, 1))
	pass
class REV_843e:# <12>[1691]
	""" Animated
	Increased stats. """
	#
	pass
class REV_843t:# <12>[1691]
	""" Sinfueled Golem
	<b>Infused</b> """
	pass





if Rev_Volatile_Skeleton:# 
	Rev_Neutral+=['REV_845']
class REV_845:# <12>[1691]
	""" Volatile Skeleton
	<b>Deathrattle:</b> Deal 2 damage to a random enemy. """
	deathrattle = Hit(RANDOM(ENEMY_MINIONS), 2)
	pass





if Rev_Scuttlebutt_Ghoul:# 
	Rev_Neutral+=['REV_900']
class REV_900_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		if len(controller.secrets)>0:
			card = random.choice(controller.secrets)
			Give(controller, card.id).trigger(source)
		pass
class REV_900:# <12>[1691]
	""" Scuttlebutt Ghoul
	<b>Taunt</b> <b>Battlecry:</b> If you control a <b>Secret</b>, summon a copy of this. """
	play = REV_900_Action(CONTROLLER)
	pass





if Rev_Dispossessed_Soul:# 
	Rev_Neutral+=['REV_901']
class REV_901_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		cards=[card.id for card in controller.field if card.type==CardType.LOCATION]
		if len(cards)>0:
			Shuffle(controller, random.choice(cards)).trigger(source)
		pass
class REV_901:# <12>[1691]
	""" Dispossessed Soul
	<b>Battlecry:</b> If you control a location, <b>Discover</b> a copy of a card in your deck. """
	play = REV_901_Action(CONTROLLER)
	pass





if Rev_Sire_Denathrius:# 
	Rev_Neutral+=['REV_906']
	Rev_Neutral+=['REV_906t']
class REV_906:# <12>[1691]
	""" Sire Denathrius
	<b><b>Lifesteal</b>.</b> <b>Battlecry:</b> Deal 5 damage amongst enemies. 
	<b>Endlessly Infuse (1):</b> Deal 1 more. """
	#	<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="1"/>
	#	<Tag enumID="3" name="TAG_SCRIPT_DATA_NUM_2" type="Int" value="5"/>	#
	play = SplitHit(SELF, ENEMY_MINIONS, 5)
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_906t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_906t', 1))
	pass
class REV_906t_Infuse(TargetedAction):
	TARGET=ActionArg()
	INFUSED=ActionArg()
	def do(self, source, target, infused, infuse_in_deck=0):
		controller=target
		if infuse_in_deck==1 and controller.infuse_in_deck==False:
			return None
		source.script_data_num_1 -= 1
		if Config.LOGINFO:
			Config.log("Infuse.do","Infusing %d -> %d for %r"%(source.script_data_num_1+1, source.script_data_num_1, infused))
		if source.script_data_num_1<= 0:
			self.broadcast(source, EventListener.ON, target, infused)
			source.script_data_num_1=1
			source.script_data_num_2+=1
			self.broadcast(source, EventListener.AFTER, target, infused)
			return target
		return None
class REV_906t:# <12>[1691]
	""" Sire Denathrius
	<b>Lifesteal</b>. <b>Battlecry:</b> Deal {1} damage amongst enemies. <b>Endlessly Infuse ({0}):</b> Deal 1 more. """
	#	<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="1"/>
	#	<Tag enumID="3" name="TAG_SCRIPT_DATA_NUM_2" type="Int" value="6"/>
	#play = SplitHit(SELF, ENEMY_MINIONS, TAG_SCRIPT_DATA_NUM_2(CONTROLLER))
	def play(self):
		controller = self.controller
		amount = self.script_data_num_2
		SplitHit(controller, controller.opponent.field, amount).trigger(self)
	class Hand:
		events = Death(FRIENDLY+MINION).on(REV_906t_Infuse(CONTROLLER, 'REV_906t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(REV_906t_Infuse(CONTROLLER, 'REV_906t', 1))
	pass





if Rev_Creepy_Painting:# 
	Rev_Neutral+=['REV_916']
class REV_916:# <12>[1691]
	""" Creepy Painting
	After another minion dies, become a copy of it. """
	events = Death(FRIENDLY + MINION).on(Morph(SELF, Copy(Death.ENTITY)))
	pass





if Rev_Sketchy_Stranger:# 
	Rev_Neutral+=['REV_945']
class REV_945_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		cc = controller.hero.card_class
		ccs=[2,3,4,5,6,7,8,9,10,14]
		ccs.remove(cc)
		cc = random.choice(ccs)
		Discover(controller, RandomSecret(card_class=cc)).trigger(source)
		pass
class REV_945:# <12>[1691]
	""" Sketchy Stranger
	<b>Battlecry:</b> <b>Discover</b> a <b>Secret</b> from another class. """
	play =  REV_945_Action(CONTROLLER)
	pass





if Rev_Steamcleaner:# 
	Rev_Neutral+=['REV_946']
class REV_946_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		assert controller==source.controller, "controller"
		cards1=[card for card in controller.deck if card.id not in controller.starting_deck]
		if len(cards1)>0:
			for card in cards1:
				card.discard()
		cards2=[card for card in controller.opponent.deck if card.id not in controller.opponent.starting_deck]
		if len(cards2)>0:
			for card in cards2:
				card.discard()
		pass
class REV_946:# <12>[1691]
	""" Steamcleaner
	<b>Battlecry:</b> Destroy ALL cards in both players' decks that didn't start there. """
	play = REV_946_Action(CONTROLLER)
	pass





if Rev_Priest_of_the_Deceased:# 
	Rev_Neutral+=['REV_956']
	Rev_Neutral+=['REV_956t']
class REV_956:# <12>[1691]
	""" Priest of the Deceased
	<b>Taunt</b> <b>Infuse (@):</b> Gain +2/+2. """
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_956t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_956t', 1))
	pass
class REV_956t:# <12>[1691]
	""" Priest of the Deceased
	<b>Infused</b> <b>Taunt</b> """
	## this card has the stats +2/+2
	pass





if Rev_Murlocula:# 
	Rev_Neutral+=['REV_957']
	Rev_Neutral+=['REV_957t']
class REV_957:# <12>[1691]
	""" Murlocula
	<b>Lifesteal</b> 
	<b>Infuse (@):</b> This costs (0). """
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_957t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_957t', 1))
	pass
class REV_957t:# <12>[1691]
	""" Murlocula
	<b>Infused Lifesteal</b> """
	# The cost of this card is zero.
	pass

if Rev_Ashen_Elemental:# 
	Rev_Neutral+=['REV_960']
	Rev_Neutral+=['REV_960e']
class REV_960e_Action(TargetedAction):
	CARD = ActionArg()
	def do(self, source, card):
		Hit(card, 2).trigger(source)
		pass
class REV_960:# <12>[1691]
	""" Ashen Elemental
	<b>Battlecry:</b> Whenever your opponent draws a card next turn, they take 2 damage. """
	play = Buff(CONTROLLER, 'REV_960e')
	pass
class REV_960e:# <12>[1691]
	""" Ashy
	Whenever your opponent draws a card next turn, they take 2 damage. """
	events = [
		Draw(OPPONENT).on(REV_960e_Action(Draw.CARD)),
		BeginTurn(CONTROLLER).on(Destroy(SELF))
	]
	pass

