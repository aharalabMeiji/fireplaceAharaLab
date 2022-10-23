from ..utils import *

Rev_Paladin=[]

Rev_Jury_Duty=True
Rev_Order_in_the_Court=True
Rev_Class_Action_Lawyer=True
Rev_Promotion=True
Rev_Muckborn_Servant=True
Rev_Service_Bell=True## OK ##
Rev_Divine_Toll=True
Rev_The_Countess=True
Rev_Sinful_Sous_Chef=True
Rev_Stewart_the_Steward=True
Rev_Buffet_Biggun=True
Rev_Elitist_Snob=True
Rev_Great_Hall=True


if Rev_Jury_Duty:# 
	Rev_Paladin+=['MAW_015']
	Rev_Paladin+=['MAW_015e']
	#Rev_Paladin+=['CS2_101t'] ##hero.py
class MAW_015:# <5>[1691]
	""" Jury Duty
	Summon two Silver Hand Recruits. Give your Silver Hand Recruits +1/+1. """
	def play(self):
		controller=self.controller
		source=self
		Summon(controller, 'CS2_101t').trigger(source)
		Summon(controller, 'CS2_101t').trigger(source)
		for card in controller.field:
			if card.id=='CS2_101t':
				Buff(card, 'MAW_015e').trigger(source)
	pass
MAW_015e=buff(1,1)




if Rev_Order_in_the_Court:# 
	Rev_Paladin+=['MAW_016']
class MAW_016:# <5>[1691]
	""" Order in the Court
	Reorder your deck from highest Cost to lowest Cost. Draw a card. """
	def play(self):
		if Config.LOGINFO:
			print("Reorder deck from the highest Cost card.")
		self.controller.deck.sort(key=lambda x:x.cost)
		Draw(self.controller).trigger(self)
		pass
	pass




if Rev_Class_Action_Lawyer:# 
	Rev_Paladin+=['MAW_017']
	Rev_Paladin+=['MAW_017e']
class MAW_017:# <5>[1691]
	""" Class Action Lawyer
	<b>Battlecry:</b> If your deck has no Neutral cards, set _a minion's stats to 1/1. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	def play(self):
		controller=self.controller
		cards=[card for card in controller.deck if card.card_class==CardClass.NEUTRAL]
		if len(cards)==0:
			Buff(self.target, 'MAW_017e')
	pass
MAW_017e=buff(1,1)



#if Rev_Stewart_the_Steward:# 
#	Rev_Paladin+=['REV_784']
#class REV_784:# <5>[1691]
#	""" Stewart the Steward
#	{0} {1} {2} {3} """
#	#
#	pass

#if Rev_Great_Hall:# 
#	Rev_Paladin+=['REV_794']
#class REV_794:# <5>[1691]
#	""" Great Hall
#	{0} {1} """
#	#
#	pass

if Rev_Promotion:# 
	Rev_Paladin+=['REV_842']
	Rev_Paladin+=['REV_842e']
class REV_842:# <5>[1691]
	""" Promotion
	Give a Silver Hand Recruit +3/+3 and <b>Taunt</b>. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, 
				 PlayReq.REQ_FRIENDLY_TARGET:0, 1003:'CS2_101t'}## 1003=REQ_TARGET_ID
	play = Buff(TARGET,'REV_842e')
	pass
REV_842e=buff(3,3,taunt=True)
#	Rev_Paladin+=['REV_842e2']
#class REV_842e2:# <5>[1691]
#	""" Under New Leadership
#	+2 Attack. """
#	#
#	pass




if Rev_Muckborn_Servant:# 
	Rev_Paladin+=['REV_947']
class REV_947:# <5>[1691]
	""" Muckborn Servant
	<b>Taunt</b> <b>Battlecry:</b> <b>Discover</b> a Paladin card. """
	play = Discover(CONTROLLER, RandomCollectible(card_class=CardClass.PALADIN))
	pass




if Rev_Service_Bell:# ### OK ###
	Rev_Paladin+=['REV_948']
class REV_948_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		for deckcard in self.player.deck:
			if deckcard.id==card.id:
				Give(self.player, deckcard).trigger(self.source)
		super().choose(card)
class REV_948_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		card_class = controller.hero.card_class
		cards=[card.id for card in controller.deck if card.card_class==card_class]
		if len(cards)>0:
			REV_948_Choice(controller, RandomID(*cards)*3).trigger(source)
		pass

class REV_948:# <5>[1691]
	""" Service Bell
	<b>Discover</b> a Class card from your deck and draw all copies of it. """
	play = REV_948_Action(CONTROLLER)
	pass




if Rev_Divine_Toll:# 
	Rev_Paladin+=['REV_950']
	Rev_Paladin+=['REV_950e']
class REV_950:# <5>[1691]
	""" Divine Toll
	Shoot 5 rays at random minions. They give friendly minions +2/+2, and deal $2 damage to enemy minions. """
	def play(self):
		controller=self.controller
		source=self
		cards=random.sample(controller.field + controller.opponent.field , 5)
		for card in cards:
			if card.controller==controller:
				Buff(card, 'REV_950e').trigger(source)
			else:
				Hit(card, 2).trigger(source)
	pass
REV_950e=buff(2,2)




if Rev_The_Countess:# 
	Rev_Paladin+=['REV_951']
	Rev_Paladin+=['REV_951e']
	Rev_Paladin+=['REV_951t']
class REV_951:# <5>[1691]
	""" The Countess
	<b>Battlecry:</b> If your deck  has no Neutral cards, add  3 <b>Legendary </b>Invitations  to your hand. """
	def play(self):
		controller=self.controller
		cards=[card for card in controller.deck if card.type==CardType.NEUTRAL]
		if len(cards)==0:
			Give(controller, 'REV_951t')
	pass
class REV_951e:# <5>[1691]
	""" Guest of Honor
	Costs (0). """
	cost=lambda self, i:0#
	pass
class REV_951t_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		Buff(card, 'REV_951e').trigger(self.source)
		super().choose(card)
	pass
class REV_951t:# <5>[1691]
	""" Legendary Invitation
	<b>Discover</b> a <b>Legendary</b> minion from another class. It costs (0). """
	play = REV_951t_Choice(CONTROLLER, RandomLegendaryMinion(card_class=CLASSES_EXCEPT_PALADIN))
	pass




if Rev_Sinful_Sous_Chef:# 
	Rev_Paladin+=['REV_952']
class REV_952:# <5>[1691]
	""" Sinful Sous Chef
	<b>Deathrattle:</b> Add 2 Silver Hand Recruits to your hand. """
	deathrattle = Give(CONTROLLER, 'CS2_101t'), Give(CONTROLLER, 'CS2_101t')
	pass




if Rev_Stewart_the_Steward:# 
	Rev_Paladin+=['REV_955']
	Rev_Paladin+=['REV_955e']
	Rev_Paladin+=['REV_955e2']
class REV_955:# <5>[1691]
	""" Stewart the Steward
	<b>Deathrattle:</b> Give the next Silver Hand Recruit you summon +3/+3 and this <b>Deathrattle</b>. """
	deathrattle = Buff(CONTROLLER, 'REV_955e')
	pass
class REV_955e:# <5>[1691]
	""" Open Position
	Your next Silver Hand Recruit carries on Stewart's legacy. """
	events = Summon(FRIENDLY + ID('CS2_101t')).after(Buff(Summon.CARD,'REV_955e2'), RemoveBuff(CONTROLLER, 'REV_955e'))
	pass
class REV_955e2:# <5>[1691]
	""" Stewart's Legacy
	+3/+3. <b>Deathrattle:</b> Your next Silver Hand Recruit has this enchant. """
	tags = {GameTag.ATK:3, GameTag.HEALTH:3, GameTag.DEATHRATTLE:1 }
	deathrattle = Buff(CONTROLLER, 'REV_955e')
	pass




if Rev_Buffet_Biggun:# 
	Rev_Paladin+=['REV_958']
	Rev_Paladin+=['REV_958e']
	Rev_Paladin+=['REV_958t']
class REV_958:# <5>[1691]
	""" Buffet Biggun
	<b>Battlecry:</b> Summon two Silver  Hand Recruits. <b>Infuse (@):</b>  Give them +2 Attack  and <b>Divine Shield</b>. """
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_958t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_958t', 1))
	play = Summon(CONTROLLER, 'CS2_101t'), Summon(CONTROLLER, 'CS2_101t')
	pass
REV_958e=buff(2,0)
class REV_958t:# <5>[1691]
	""" Buffet Biggun
	<b>Infused.</b> <b>Battlecry:</b> Summon two Silver Hand Recruits. Give them +2 Attack and <b>Divine Shield</b>. """
	def play(self):#
		controller=self.controller
		source=self
		card=Summon(controller, 'CS2_101t').trigger(source)
		card=card[0][0]
		Buff(card, 'REV_958e').trigger(source)
		card.divine_shield=True
		card2=Summon(controller, 'CS2_101t').trigger(source)
		card2=card2[0][0]
		Buff(card2, 'REV_958e').trigger(source)
		card2.divine_shield=True
	pass

if Rev_Elitist_Snob:# 
	Rev_Paladin+=['REV_961']
class REV_961:# <5>[1691]
	""" Elitist Snob
	<b>Battlecry:</b> For each Paladin card in your hand, randomly  gain <b>Divine Shield</b>, <b>Lifesteal</b>,  <b>Rush</b>, or <b>Taunt</b>. """
	def play(self):
		controller=self.controller
		source=self
		amount=len([card for card in controller.hand if card.card_class==CardClass.PALADIN])
		buffs=['divine_shield','lifesteal','rush','taunt']
		if amount<4:
			buffs=random.sample(buffs, amount)
		for b in buffs:
			if b=='divine_shield':
				self.divine_shield=True
			if b=='lifesteal':
				self.lifesteal=True
			if b=='rush':
				self.rush=True
			if b=='divine_shield':
				self.taunt=True
	pass

if Rev_Great_Hall:# 
	Rev_Paladin+=['REV_983']
	Rev_Paladin+=['REV_983e']
class REV_983:# <5>[1691]
	""" Great Hall
	Set a minion's Attack and Health to 3. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	location = Buff(TARGET, 'REV_983e')
	pass
class REV_983e:# <5>[1691]
	""" Good Food
	Stats changed to 3/3. """
	atk=lambda self,i: 3
	max_health=lambda self,i: 3
	pass

