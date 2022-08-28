from ..utils import *

Sunken_Druid=[]

Sunken_Spirit_of_the_Tides=True  ###
Sunken_Moonbeam=True  ###
Sunken_Herald_of_Nature=True  ###
Sunken_Colaque=True  ###
Sunken_Flipper_Friends=True  ###
Sunken_Seaweed_Strike=True  ###
Sunken_Green_Thumb_Gardener=True  ###
Sunken_Bottomfeeder=True  ###
Sunken_Aquatic_Form=True  ###
Sunken_Miracle_Growth=True  ###
Sunken_Dozing_Kelpkeeper=True  ###
Sunken_Hedra_the_Heretic=True  ###
Sunken_Azsharan_Gardens=True  ###




if Sunken_Spirit_of_the_Tides:# 
	Sunken_Druid+=['TID_000']
	Sunken_Druid+=['TID_000e']
class TID_000_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		controller = source.controller
		if controller.mana>0:
			Buff(target, buff).trigger(source)
			pass
class TID_000:# <2>[1658]
	""" Spirit of the Tides
	If you have any unspentMana at the end of_your turn, gain +1/+2. """
	events = OWN_TURN_END.on(TID_000_Action(SELF,'TID_000e'))
	pass
TID_000e=buff(1,2)




if Sunken_Moonbeam:# 
	Sunken_Druid+=['TID_001']
class TID_001:# <2>[1658]
	""" Moonbeam
	Deal $1 damage to an enemy, twice. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_ENEMY_TARGET:0,}
	play = Hit(TARGET, 1)
	pass




if Sunken_Herald_of_Nature:# 
	Sunken_Druid+=['TID_002']
	Sunken_Druid+=['TID_002e']
class TID_002:# <2>[1658]
	""" Herald of Nature
	[Battlecry:] If you've cast a Nature spell while holding this, give your other minions +1/+2. """
	class Hand:
		events = Play(CONTROLLER, SPELL + NATURE).on(SetScriptDataNum1(SELF, True))
	play = ScriptDataNum1True(SELF) & Buff(FRIENDLY_MINIONS - SELF, 'TID_002e')
	pass
TID_002e=buff(1,2)




if Sunken_Colaque:# 
	Sunken_Druid+=['TSC_026']
	Sunken_Druid+=['TSC_026t']
class TSC_026:# <2>[1658]
	""" Colaque
	[Colossal +1] [Immune] while you control Colaque's Shell. """
	play=Summon(CONTROLLER, 'TSC_026t')
	update = Find(FRIENDLY + ID('TSC_026t')) & Refresh(CONTROLLER, {GameTag.IMMUNE: True, })
	pass

class TSC_026t:# <2>[1658]
	""" Colaque's Shell
	[Taunt][Deathrattle:] Gain 8 Armor. """
	deathrattle = GainArmor(FRIENDLY_HERO, 8)
	pass




if Sunken_Flipper_Friends:# 
	Sunken_Druid+=['TSC_650']
	Sunken_Druid+=['TSC_650a']
	Sunken_Druid+=['TSC_650d']
	Sunken_Druid+=['TSC_650t']
	Sunken_Druid+=['TSC_650t4']
class TSC_650:# <2>[1658]
	""" Flipper Friends
	[Choose One] - Summon a 6/6 Orca with [Taunt]; or six 1/1 Otters with [Rush]. """
	choose=('TSC_650a','TSC_650d')
	play = ChooseBoth(CONTROLLER) & (Summon(CONTROLLER, 'TSC_650t'), Summon(CONTROLLER, 'TSC_650t4')*6)
class TSC_650a:# <2>[1658]
	""" Order the Orca
	Summon a 6/6 Orca with [Taunt]. """
	play=Summon(CONTROLLER, 'TSC_650t')
class TSC_650d:# <2>[1658]
	""" Romp of Otters
	Summon six 1/1 Otters with [Rush]. """
	play = Summon(CONTROLLER, 'TSC_650t4')*6

class TSC_650t:# <2>[1658]
	""" Orca
	[Taunt] """
class TSC_650t4:# <2>[1658]
	""" Otter
	[Rush] """
	pass




if Sunken_Seaweed_Strike:# 
	Sunken_Druid+=['TSC_651']
	Sunken_Druid+=['TSC_651e']
class TSC_651:# <2>[1658]
	""" Seaweed Strike
	Deal $4 damage to a minion.If you played a Naga while holding this, also give your hero +4 Attack this turn. """
	class Hand:
		events = Play(CONTROLLER, NAGA).on(SetScriptDataNum1(SELF, True))
	requirements = { PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0,}
	play = Hit(TARGET, 4), ScriptDataNum1True(SELF) & Buff(FRIENDLY_HERO, 'TSC_651e')
TSC_651e=buff(4,0)
#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>




if Sunken_Green_Thumb_Gardener:# 
	Sunken_Druid+=['TSC_652']
class TSC_652:# <2>[1658]
	""" Green-Thumb Gardener
	[Battlecry:] Refresh empty Mana Crystals equal to the Cost of the most expensive spell in your hand. """
	def play(self):
		amount=0
		for card in self.controller.hand:
			if card.type==CardType.SPELL and card.cost>amount:
				amount = card.cost
		if amount>0:
			actions=GainEmptyMana(CONTROLLER, amount)
			for action in actions:
				action.trigger(self)
	pass




if Sunken_Bottomfeeder:# 
	Sunken_Druid+=['TSC_653']
class TSC_653:# <2>[1658]
	""" Bottomfeeder
	[Deathrattle:] Add a Bottomfeeder to the bottom of your deck with permanent +2/+2. """
	deathrattle = ShuffleBottom(CONTROLLER, 'TSC_653').then(Buff(ShuffleBottom.CARD, 'TSC_653e'))
	pass
@custom_card
class TSC_653e:
	tags = {
		GameTag.CARDNAME: "Miracle Growth enchantment",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.ATK:2,
		GameTag.HEALTH:2
	}



if Sunken_Aquatic_Form:# 
	Sunken_Druid+=['TSC_654']
class TSC_654_DredgeChoice(Choice):
	def choose(self, card):
		super().choose(card)
		self.next_choice=None
		if Config.LOGINFO:
			print("(DredgeChoice.choose)%s chooses %r"%(card.controller.name, card))
		controller = card.controller
		for c in controller.deck[:3]:
			if card.id==c.id:
				controller.deck.remove(c)
				controller.deck.append(c)
				if controller.mana >= c.cost:
					c.zone=Zone.HAND# draw it
				break
		pass
class TSC_654_Dredge(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		bottom3ID=[card.id for card in target.deck[:3]]
		TSC_654_DredgeChoice(target, RandomID(*bottom3ID)*3).trigger(source)
	pass
class TSC_654:# <2>[1658]
	""" Aquatic Form
	[Dredge]. If you have the Mana to play the card this turn, draw it. """
	play = TSC_654_Dredge(CONTROLLER)
	pass




if Sunken_Miracle_Growth:# 
	Sunken_Druid+=['TSC_656']
	Sunken_Druid+=['TSC_656t']
class TSC_656:# <2>[1658]
	""" Miracle Growth
	Draw 3 cards.Summon a Plant with[Taunt] and stats equal to your hand size. """
	def play(self):
		Draw(self.controller).trigger(self)
		Draw(self.controller).trigger(self)
		Draw(self.controller).trigger(self)
		amount = len(self.controller.hand)
		newcard = Summon(self.controller, 'TSC_656t').trigger(self)
		newcard=newcard[0][0]
		Buff(newcard, 'TSC_656e', atk=amount-1, max_health=amount-1).trigger(self)
class TSC_656t:# <2>[1658]
	""" Kelp Creeper 	[Taunt] """
@custom_card
class TSC_656e:
	tags = {
		GameTag.CARDNAME: "Miracle Growth enchantment",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
	}




if Sunken_Dozing_Kelpkeeper:# 
	Sunken_Druid+=['TSC_657']
	#Sunken_Druid+=['TSC_657e']
class TSC_657:# <2>[1658]
	""" Dozing Kelpkeeper
	[Rush]. Starts [Dormant].After you've cast 5 Mana_worth of spells, awaken. """
	dormant = -1 #infinite dormant
	events = OWN_SPELL_PLAY.on(SidequestManaCounter(SELF,Play.CARD,5,
		[SetAttr(SELF, 'dormant',0), Awaken(SELF) ]))
#class TSC_657e:# <2>[1658]
#	""" Aquatic Slumber	[Dormant]. Awaken after you cast @ Mana worth of spells. """




if Sunken_Hedra_the_Heretic:# ### OK 
	Sunken_Druid+=['TSC_658']
class TSC_658_Action1(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		if isinstance(target, list):
			target = target[0]
		source.sidequest_list0.append(target.cost)
		pass
class TSC_658_Action2(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		for cost in source.sidequest_list0:
			Summon(target , RandomMinion(cost=cost)).trigger(source)
		pass
class TSC_658:# <2>[1658]
	""" Hedra the Heretic
	[Battlecry:] For each spell you've cast while holding this, summon a minion of that spell's Cost. """
	class Hand:
		events = OWN_SPELL_PLAY.on(TSC_658_Action1(Play.CARD))
	play = TSC_658_Action2(CONTROLLER)
	pass




if Sunken_Azsharan_Gardens:# 
	Sunken_Druid+=['TSC_927']
	Sunken_Druid+=['TSC_927e']
	Sunken_Druid+=['TSC_927t']
class TSC_927:# <2>[1658]
	""" Azsharan Gardens
	Give all minions in your hand +1/+1. Put a 'Sunken Gardens' on the bottom of your deck. """
	play = Buff(FRIENDLY_HAND+MINION, 'TSC_927e'), ShuffleBottom(CONTROLLER, 'TSC_927t')
TSC_927e=buff(1,1)
class TSC_927t:# <2>[1658]
	""" Sunken Gardens """

