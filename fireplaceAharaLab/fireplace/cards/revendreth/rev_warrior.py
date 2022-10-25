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
Rev_Crazed_Wretch=True
Rev_Conquerors_Banner=True
Rev_Imbued_Axe=True
Rev_Decimator_Olgra=True
Rev_Sanguine_Depths=True


if Rev_Call_to_the_Stand:# ###
	Rev_Warrior+=['MAW_027']
class MAW_027:# <10>[1691]
	""" Call to the Stand (spell)
	Your opponent summons a random minion from their hand. """
	play = Summon(OPPONENT, RANDOM(ENEMY_HAND))
	pass




if Rev_Mawsworn_Bailiff:# 
	Rev_Warrior+=['MAW_028']
	Rev_Warrior+=['MAW_028e2']
class MAW_028:# <10>[1691]
	""" Mawsworn Bailiff
	<b><b>Taunt</b>.</b> <b>Battlecry:</b> If you have 4 or more Armor, gain +4/+4. """
	def play(self):
		if self.controller.hero.armor>=4:
			Buff(self, 'MAW_028e2').trigger(self)
	pass
MAW_028e2=buff(4,4)




if Rev_Weapons_Expert:# ###
	Rev_Warrior+=['MAW_029']
	Rev_Warrior+=['MAW_029e2']
class MAW_029:# <10>[1691]
	""" Weapons Expert
	<b>Battlecry:</b> If you have a weapon equipped, give it +1/+1. Otherwise, draw a weapon. """
	def play(self):
		controller=self.controller
		if controller.weapon!=None:
			Buff(self, 'MAW_029e2').trigger(self)
		else:
			cards=[card for card in controller.deck if card.type==CardType.WEAPON]
			if len(cards)>0:
				Give(controller,random.choice(cards)).trigger(self)
	pass
MAW_029e2=buff(1,1)




if Rev_Suspicious_Pirate:# ### OK ###
	Rev_Warrior+=['REV_006']
	#Rev_Warrior+=['REV_000e']
class REV_006_Choice(Choice):
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

class REV_006:# <10>[1691]
	""" Suspicious Pirate
	<b>Battlecry:</b> <b>Discover</b> a weapon. If your opponent guesses your choice, they get a copy. """
	def play(self):
		source=self
		controller=self.controller
		opponent=controller.opponent
		choice=REV_006_Choice(controller, RandomWeapon()*3)
		choice.trigger(source)
		pass
	pass





if Rev_Remornia_Living_Blade:# ###
	Rev_Warrior+=['REV_316']
	Rev_Warrior+=['REV_316t']
class REV_316_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		newcard=Summon(controller, 'REV_316t').trigger(source)
		if newcard[0]==[]:
			return
		newcard=newcard[0][0]
		newcard.damage=source.damage
		for buff in source.buffs:
			buff.apply(newcard)
		source.discard()
		pass
class REV_316:# <10>[1691]
	""" Remornia, Living Blade
	<b>Rush</b> After this attacks, equip it. """
	events = Attack(SELF).after(REV_316_Action(CONTROLLER))
	pass
#	Rev_Warrior+=['REV_316e']
#class REV_316e:# <10>[1691]
#	""" Remornia's Will
#	Has the stats of Remornia. """
#	#
#	pass
class REV_316t_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		newcard=Summon(controller, 'REV_316').trigger(source)
		if newcard[0]!=[]:
			newcard=newcard[0][0]
			newcard.damage=source.damage
			for buff in source.buffs:
				buff.apply(newcard)
		source.discard()
		pass
class REV_316t:# <10>[1691]
	""" Remornia, Living Blade
	After your hero attacks, return this to the battlefield. """
	events = Attack(FRIENDLY_HERO).after(REV_316t_Action(CONTROLLER))
	pass




if Rev_Anima_Extractor:# ###
	Rev_Warrior+=['REV_332']
	Rev_Warrior+=['REV_332e']
class REV_332:# <10>[1691]
	""" Anima Extractor
	Whenever a friendly minion takes damage, give a random minion in your hand +1/+1. """
	events = Damage(FRIENDLY+MINION).on(Buff(RANDOM(FRIENDLY_HAND+MINION),'REV_332e'))
	pass
REV_332e=buff(1,1)




if Rev_Burden_of_Pride:# ###
	Rev_Warrior+=['REV_334']
	Rev_Warrior+=['REV_334e']
	Rev_Warrior+=['REV_334t']
class REV_334:# <10>[1691]
	""" Burden of Pride
	Summon three 1/3 Jailers with <b>Taunt</b>. If you have 20 or less Health, give them +1/+1. """
	def play(self):
		controller=self.controller
		card1 = Summon(controller,'REV_334t').trigger(self)
		card2 = Summon(controller,'REV_334t').trigger(self)
		card3 = Summon(controller,'REV_334t').trigger(self)
		if sum([card.health for card in controller.field])<=20:
			if card1[0]!=[]:
				Buff(card1[0][0], 'REV_334e').trigger(self)
			if card2[0]!=[]:
				Buff(card2[0][0], 'REV_334e').trigger(self)
			if card3[0]!=[]:
				Buff(card3[0][0], 'REV_334e').trigger(self)
	pass
REV_334e=buff(1,1)
class REV_334t:# <10>[1691]
	""" Sanguine Jailer
	<b>Taunt</b> """
	#
	pass




if Rev_Riot:# ###
	Rev_Warrior+=['REV_337']
	Rev_Warrior+=['REV_337e']
class REV_337:# <10>[1691]
	""" Riot!
	Your minions can't be  reduced below 1 Health  this turn. They each attack  a random enemy minion. """
	play = Buff(FRIENDLY_MINIONS, 'REV_337e'), RegularAttack(FRIENDLY+MINION, RANDOM(ENEMY_MINIONS))
	pass

class REV_337e:# <10>[1691]
	""" Riot!
	Can't be reduced below 1 Health this turn. """
	tags = {GameTag.HEALTH_MINIMUM:1}
	#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>
	pass

#	Rev_Warrior+=['REV_337e2']
#class REV_337e2:# <10>[1691]
#	""" Riot!
#	Your minions can't be reduced below 1 Health this turn. """
#	#
#	pass

#if Rev_Decimator_Olgra:# 
#	Rev_Warrior+=['REV_783']
#class REV_783:# <10>[1691]
#	""" Decimator Olgra
#	{0} {1} {2} {3} """
#	#
#	pass

#if Rev_Sanguine_Depths:# 
#	Rev_Warrior+=['REV_793']
#class REV_793:# <10>[1691]
#	""" Sanguine Depths
#	{0} {1} """
#	#
#	pass




if Rev_Crazed_Wretch:# ###
	Rev_Warrior+=['REV_930']
	Rev_Warrior+=['REV_930e']
class REV_930:# <10>[1691]
	""" Crazed Wretch
	Has +2 Attack and <b>Charge</b> while damaged. """
	update = Refresh(SELF + DAMAGED, buff='REV_930e')
	pass
class REV_930e:# <10>[1691]
	""" Angry
	<b>Charge</b>. """
	tags = {GameTag.CHARGE:1, GameTag.ATK:2, }	
	pass




if Rev_Conquerors_Banner:# ###
	Rev_Warrior+=['REV_931']
class REV_931:# <10>[1691]
	""" Conqueror's Banner
	Reveal a card from each player's deck, three times. Draw any of yours that cost more. """
	def play(self):
		controller=self.controller
		opponent=controller.opponent
		for repeat in range(3):
			card1=random.choice(controller.deck)
			card2=random.choice(opponent.deck)
			if card1.cost>card2.cost:
				Give(controller, card1).trigger(self)
	pass

if Rev_Imbued_Axe:# ###
	Rev_Warrior+=['REV_933']
	Rev_Warrior+=['REV_933e']
	Rev_Warrior+=['REV_933e2']
	Rev_Warrior+=['REV_933t']
class REV_933:# <10>[1691]
	""" Imbued Axe
	After your hero attacks, give your damaged minions +1/+2. <b>Infuse (@):</b> +2/+2 instead. """
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_933t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_933t', 1))
	events = Attack(FRIENDLY_HERO).after(Buff(FRIENDLY_MINIONS + DAMAGED, 'REV_933e'))
	pass
REV_933e=buff(1,2)
REV_933e2=buff(2,2)
class REV_933t:# <10>[1691]
	""" Imbued Axe
	<b>Infused</b> After your hero attacks, give your damaged minions +2/+2. """
	events = Attack(FRIENDLY_HERO).after(Buff(FRIENDLY_MINIONS + DAMAGED, 'REV_933e2'))
	pass




if Rev_Decimator_Olgra:# ###
	Rev_Warrior+=['REV_934']
	Rev_Warrior+=['REV_934e']
class REV_934:# <10>[1691]
	""" Decimator Olgra
	<b>Battlecry:</b> Gain +1/+1 for each damaged minion, _then attack all enemies. """
	play = Buff(FRIENDLY_MINIONS + DAMAGED, 'REV_934e'), RegularAttack(FRIENDLY+MINION+DAMAGED, RANDOM(ENEMY_MINIONS))
	pass
REV_934e=buff(1,1)




if Rev_Sanguine_Depths:# 
	Rev_Warrior+=['REV_990']
	Rev_Warrior+=['REV_990e']
class REV_990:# <10>[1691]
	""" Sanguine Depths
	Deal 1 damage to a  minion and give it  +2 Attack. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0 }	#
	play = Hit(TARGET, 1), Buff(TARGET, 'REV_990e')
	pass
REV_990e=buff(2,0)

