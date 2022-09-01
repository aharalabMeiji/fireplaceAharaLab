from ..utils import *

Sunken_Rogue=[]

Sunken_Shattershambler=True  ###
Sunken_Inkveil_Ambusher=True  ###
Sunken_Jackpot=True  ###
Sunken_Cutlass_Courier=True  ###
Sunken_Swordfish=True  ###
Sunken_Azsharan_Vessel=True  ###
Sunken_Gone_Fishin=True  ###
Sunken_Blood_in_the_Water=True  ###
Sunken_Bootstrap_Sunkeneer=True  ###
Sunken_Pirate_Admiral_Hooktusk=True  ###
Sunken_Swiftscale_Trickster=True  ###
Sunken_Crabatoa=True  ###
Sunken_Filletfighter=True  ###


if Sunken_Shattershambler:# 
	Sunken_Rogue+=['TID_078','TID_078e','TID_078e2',]
class TID_078:# <7>[1658]
	""" Shattershambler
	[Battlecry:] Your next [Deathrattle] minion costs (1) less, but immediately dies when played. """
	play = Buff(FRIENDLY_HAND + DEATHRATTLE, 'TID_078e'),Buff(FRIENDLY_HAND + DEATHRATTLE, 'TID_078e2')
	pass
class TID_078e:
	events = [
		Play(CONTROLLER, OWNER).after(Destroy(OWNER)),
		Play(CONTROLLER, MINION+DEATHRATTLE).after(Destroy(SELF))
	]
	pass
class TID_078e2:
	cost = lambda self, i:max(i-1,0)
	events = Play(CONTROLLER, MINION+DEATHRATTLE).after(Destroy(SELF))
	pass



if Sunken_Inkveil_Ambusher:# 
	Sunken_Rogue+=['TID_080']
	Sunken_Rogue+=['TID_080e2']
class TID_080:# <7>[1658]
	""" Inkveil Ambusher
	[Stealth]Has +3 Attack and [Immune] while attacking. """
	#<Tag enumID="373" name="IMMUNE_WHILE_ATTACKING" type="Int" value="1"/>
	update = Attacking(SELF,ENEMY) & Refresh(SELF, buff='TID_080e2')# Attacking(CONTROLLER)??
	pass
TID_080e2=buff(3,0)




if Sunken_Jackpot:# 
	Sunken_Rogue+=['TID_931']
class TID_931:# <7>[1658]
	""" Jackpot!
	Add two random spells from other classes that cost (5) or more to your hand. """
	play = Give(CONTROLLER, RandomSpell(card_class=CLASSES_EXCEPT_ROGUE, cost=[5,6,7,8,9])) * 2
	pass




if Sunken_Cutlass_Courier:# 
	Sunken_Rogue+=['TSC_085']
class TSC_085:# <7>[1658]
	""" Cutlass Courier
	After your hero attacks, draw a Pirate. """
	events = Attack(FRIENDLY_HERO).after(Give(CONTROLLER, RANDOM(FRIENDLY_DECK + PIRATE)))
	pass




if Sunken_Swordfish:# 
	Sunken_Rogue+=['TSC_086']

	Sunken_Rogue+=['TSC_086e']
class TSC_086_DredgeChoice(Choice):
	def choose(self, card):
		super().choose(card)
		if Config.LOGINFO:
			Config.log("DredgeChoice.choose","%s chooses %r"%(card.controller.name, card))
		controller = card.controller
		for c in controller.deck[:3]:
			if card.id==c.id:
				controller.deck.remove(c)
				controller.deck.append(c)
				if c.type==CardType.MINION and c.race==Race.PIRATE:
					Buff(c, 'TSC_086e').trigger(self.option)
					Buff(self.option, 'TSC_086e').trigger(self.option)
				break
		pass
class TSC_086_Dredge(TargetedAction):
	"""
	TARGET=ActionArg()#CONTROLLER
	"""
	TARGET=ActionArg()
	def do(self, source, target):
		bottom3ID=[card.id for card in target.deck[:3]]
		TSC_086_DredgeChoice(target, RandomID(*bottom3ID)*3, source).trigger(source)
	pass
class TSC_086:# <7>[1658]
	""" Swordfish
	[Battlecry:] [Dredge].If it's a Pirate, give this weapon and the Pirate +2 Attack. """
	play = 	TSC_086_Dredge(CONTROLLER)
	pass
TSC_086e=buff(2,0)

if Sunken_Azsharan_Vessel:# 
	Sunken_Rogue+=['TSC_912']
	Sunken_Rogue+=['TSC_912t']
	Sunken_Rogue+=['TSC_912t2']
	Sunken_Rogue+=['TSC_912t3']
class TSC_912:# <7>[1658]
	""" Azsharan Vessel
	Summon two 3/3 Pirates(TSC_912t2) with [Stealth]. Put a 'Sunken Vessel' on the bottom of your deck. """
	play = Summon(CONTROLLER, 'TSC_912t2'), ShuffleBottom(CONTROLLER, 'TSC_912t')
	pass
class TSC_912t:# <7>[1658]
	""" Sunken Vessel
	[Casts When Drawn]Summon two 3/3 Pirates(TSC_912t3) with [Stealth]. """
	tags = {GameTag.CASTSWHENDRAWN: 1}
	play = Summon(CONTROLLER, 'TSC_912t3')
	pass
class TSC_912t2:# <7>[1658]
	""" Sunken Pirate
	[Stealth] """
	#
	pass
class TSC_912t3:# <7>[1658]
	""" Azsharan Pirate
	[Stealth] """
	#
	pass




if Sunken_Gone_Fishin:# 
	Sunken_Rogue+=['TSC_916']
class TSC_916:# <7>[1658]
	""" Gone Fishin'
	[Dredge].[Combo:] Draw a card. """
	play = Dredge(CONTROLLER)
	combo = Draw(CONTROLLER)
	pass




if Sunken_Blood_in_the_Water:# 
	Sunken_Rogue+=['TSC_932']
	Sunken_Rogue+=['TSC_932t']
class TSC_932:# <7>[1658]
	""" Blood in the Water
	Deal $3 damage to an enemy. Summon a 5/5 Shark with [Rush]. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = Hit(TARGET, 3), Summon(CONTROLLER, 'TSC_932t')#
	pass
class TSC_932t:# <7>[1658]
	""" Tiger Shark
	[Rush] """
	#
	pass




if Sunken_Bootstrap_Sunkeneer:# 
	Sunken_Rogue+=['TSC_933']
class TSC_933:# <7>[1658]
	""" Bootstrap Sunkeneer
	[Combo:] Put an enemy minion on the bottom of_your opponent's deck. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	Combo = ShuffleBottom(OPPONENT, Copy(TARGET)), Destroy(TARGET)
	pass




if Sunken_Pirate_Admiral_Hooktusk:# 
	Sunken_Rogue+=['TSC_934']
	Sunken_Rogue+=['TSC_934t']
	Sunken_Rogue+=['TSC_934t2']
	Sunken_Rogue+=['TSC_934t3']
class TSC_934:# <7>[1658]
	""" Pirate Admiral Hooktusk
	[Battlecry:] If you've summoned 8 other Pirates this game, plunder the enemy!@ <i>({0} left!)</i>@ <i>(Ready!)</i> """
	entourage = ['TSC_934t','TSC_934t2','TSC_934t3']
	def play(self):
		cards=[card for card in self.controller.summon_log if card.race==Race.PIRATE]
		if len(cards)>=8:
			Discover(self.controller, RandomEntourage()).trigger()
	pass
class TSC_934t:# <7>[1658]
	""" Take their Supplies!
	Take 5 cards from your opponent's deck. """
	play = Give(CONTROLLER, RANDOM(ENEMY_DECK)) * 5
	pass
class TSC_934t2:# <7>[1658]
	""" Take their Gold!
	Take 2 cards from your opponent's hand. """
	play = Give(CONTROLLER, RANDOM(ENEMY_HAND)) * 2
	pass
class TSC_934t3:# <7>[1658]
	""" Take their Ship!
	Take control of your opponent's highest Attack minion. """
	def play(self):
		high=[]
		for card in self.controller.opponent.field:
			if high==[] or high[0].atk<card.atk:
				high=[card]
			elif high[0].atk==card.atk:
				high.append(card)
		if len(high)>0:
			card = random.choice(high)
			card.zone=Zone.SETASIDE
			card.controller = self.controller
			card.zone=Zone.Field
		pass
	pass





if Sunken_Swiftscale_Trickster:# 
	Sunken_Rogue+=['TSC_936']
	Sunken_Rogue+=['TSC_936e']
class TSC_936:# <7>[1658]
	""" Swiftscale Trickster
	[Battlecry:] Your next spell this turn costs (0). """
	play = Buff(FRIENDLY_HAND + SPELL)
	pass
class TSC_936e:# <7>[1658]
	""" Fooled the Audience
	Your next spell this turn costs (0). """
	cost = lambda self, i:0
	events = Play(CONTROLLER, SPELL).on(Destroy(SELF))
	pass




if Sunken_Crabatoa:# 
	Sunken_Rogue+=['TSC_937']
	Sunken_Rogue+=['TSC_937e']
	Sunken_Rogue+=['TSC_937t']
	Sunken_Rogue+=['TSC_937t2']
	Sunken_Rogue+=['TSC_937t3']
class TSC_937:# <7>[1658]
	""" Crabatoa
	[Colossal +2]Your Crabatoa Claws have +2 Attack. """
	play = Summon(CONTROLLER,'TSC_937t'), Summon(CONTROLLER,'TSC_937t3')
	update = Refresh(FRIENDLY_MINIONS + ID('TSC_937t2'), buff='TSC_937e')
	pass
TSC_937e=buff(2,0)
class TSC_937t:# <7>[1658]
	""" Crabatoa's Claw
	[Rush][Deathrattle:]  Equip a 2/1 Claw. """
	deathrattle = Summon(CONTROLLER, 'TSC_937t2')
	pass
class TSC_937t2:# <7>[1658]
	""" Crabatoa Claw
	 """
	pass
class TSC_937t3:# <7>[1658]
	""" Crabatoa's Claw
	[Rush][Deathrattle:]  Equip a 2/1 Claw. """
	deathrattle = Summon(CONTROLLER, 'TSC_937t2')
	pass




if Sunken_Filletfighter:# 
	Sunken_Rogue+=['TSC_963']
class TSC_963:# <7>[1658]
	""" Filletfighter
	[Battlecry:] Deal 1 damage. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_HERO_OR_MINION_TARGET:0}
	play = Hit(TARGET, 1)
	pass



