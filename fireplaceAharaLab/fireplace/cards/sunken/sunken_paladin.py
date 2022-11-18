from ..utils import *

Sunken_Paladin=[]

Sunken_Lightray=True
Sunken_Myrmidon=True
Sunken_Front_Lines=True
Sunken_The_Leviathan=True
Sunken_Bubblebot=True
Sunken_Shimmering_Sunfish=True
Sunken_The_Gardens_Grace=True
Sunken_Kotori_Lightblade=True
Sunken_Immortalized_in_Stone=True
Sunken_Radar_Detector=True
Sunken_Seafloor_Savior=True
Sunken_Azsharan_Mooncatcher=True
Sunken_Holy_Maki_Roll=True



if Sunken_Lightray:# 
	Sunken_Paladin+=['TID_077']
class TID_077_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		cards = [card for card in target.play_log if card.type==CardType.MINION and card.card_class==CardClass.PALADIN]
		if len(cards)>0:
			source.cost = max(source.cost-len(cards),0)
class TID_077:# <5>[1658]
	""" Lightray
	[Taunt]Costs (1) less for each Paladin card you've played this game. """
	class Hand:
		events = Play(CONTROLLER).on(TID_077_Action(CONTROLLER))
	pass

if Sunken_Myrmidon:# 
	Sunken_Paladin+=['TID_098']
class TID_098:# <5>[1658]
	""" Myrmidon
	After you cast a spell on this minion, draw a card. """
	events = Play(CONTROLLER, SPELL, SELF).after(Draw(CONTROLLER))
	pass

if Sunken_Front_Lines:# 
	Sunken_Paladin+=['TID_949']
class TID_949:# <5>[1658]
	""" Front Lines
	Summon a minion from each player's deck.Repeat until either side of the battlefield is full. """
	def play(self):
		while True:
			cards1 = [card for card in self.controller.deck if card.type==CardType.MINION]
			cards2 = [card for card in self.controller.opponent.deck if card.type==CardType.MINION]
			if len(cards1)>0 and len(cards2)>0:
				if len(self.controller.field)<7 and len(self.controller.opponent.field)<7:
					card1 = random.choice(cards1)
					card2 = random.choice(cards2)
					card1.zone=Zone.SETASIDE
					card1.zone=Zone.PLAY
					card2.zone=Zone.SETASIDE
					card2.zone=Zone.PLAY
				else:
					break
			else:
				break
	pass

if Sunken_The_Leviathan:# ### OK
	Sunken_Paladin+=['TSC_030']
	Sunken_Paladin+=['TSC_030t2']
class TSC_030:# <5>[1658]
	""" The Leviathan
	[Colossal +1][Rush], [Divine Shield]After this attacks,[Dredge]. """
	play = Summon(CONTROLLER, 'TSC_030t2')
	events = Attack(SELF).after(Dredge(CONTROLLER))
	pass
class TSC_030t2:# <5>[1658]
	""" The Leviathan's Claw
	[Rush], [Divine Shield]After this attacks,draw a card. """
	events = Attack(SELF).after(Draw(CONTROLLER))
	pass

if Sunken_Bubblebot:# ### OK
	Sunken_Paladin+=['TSC_059']
class TSC_059:# <5>[1658]
	""" Bubblebot
	[Battlecry:] Give your other Mechs [Divine Shield]and [Taunt]. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_TARGET_WITH_RACE:Race.MECHANICAL, }
	def play(self):
		if self.target:
			self.target.divine_shield=True
			self.target.taunt=True
	pass

if Sunken_Shimmering_Sunfish:# 
	Sunken_Paladin+=['TSC_060']
class TSC_060:# <5>[1658]
	""" Shimmering Sunfish
	[Battlecry:] If you're holding a Holy Spell, gain [Taunt] and [Divine Shield]. """
	play = Find((FRIENDLY_HAND + SPELL) + HOLY) & (SetDivineShield(SELF), SetAttr(SELF, 'taunt', True))
	pass

if Sunken_The_Gardens_Grace:#  ### OK
	Sunken_Paladin+=['TSC_061']
	Sunken_Paladin+=['TSC_061e']
class TSC_061_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		newcost = target.data.cost
		for card in target.controller.play_log:
			if card.type==CardType.SPELL and card.spell_school==SpellSchool.HOLY:
				newcost -= card.cost
		newcost = max(newcost, 0)
		target.cost = newcost
class TSC_061:# <5>[1658]
	""" The Garden's Grace
	Give a minion +5/+5 and [Divine Shield]. Costs (1) less for each Mana you've spent on Holy spells this game. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0}	
	play = Buff(TARGET, 'TSC_061e2'), Buff(TARGET, 'TSC_061e')
	class Hand:
		update = TSC_061_Action(SELF)
	pass

class TSC_061e:
	def apply(self, target):
		target.divine_shield=True
@custom_card
class TSC_061e2:# <5>[1658]
	tags={
		GameTag.CARDNAME:"+",
		GameTag.CARDTYPE:CardType.ENCHANTMENT,
		GameTag.ATK:5,
		GameTag.HEALTH:5,
	}

if Sunken_Kotori_Lightblade:# ### OK
	Sunken_Paladin+=['TSC_074']
class TSC_074_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		newtargets=[card for card in source.controller.field if card != source]
		if newtargets!=[]:
			newcard=Give(source.controller, target.id).trigger(source)
			if newcard[0]==[]:
				return
			newcard=newcard[0][0]
			newtarget=random.choice(newtargets)
			newcard.target = newtarget
			Battlecry(newcard,newtarget).trigger(source)
			Destroy(newcard).trigger(source)

class TSC_074:# <5>[1658]
	""" Kotori Lightblade
	After you cast a Holy spell on this, cast it again on__another friendly minion. """
	events = Play(CONTROLLER, SPELL + HOLY, SELF).after(TSC_074_Action(Play.CARD))
	pass

if Sunken_Immortalized_in_Stone:# 
	Sunken_Paladin+=['TSC_076']
	Sunken_Paladin+=['TSC_076t']
	Sunken_Paladin+=['TSC_076t2']
	Sunken_Paladin+=['TSC_076t3']
class TSC_076:# <5>[1658]
	""" Immortalized in Stone
	Summon a 1/2, 2/4 and 4/8 Elemental with [Taunt]. """
	play = Summon(CONTROLLER, 'TSC_076t'), Summon(CONTROLLER, 'TSC_076t2'), Summon(CONTROLLER, 'TSC_076t3')
	pass
class TSC_076t:# <5>[1658]
	""" Worn Statue
	[Taunt] """
	#
	pass
class TSC_076t2:# <5>[1658]
	""" Living Statue
	[Taunt] """
	#
	pass
class TSC_076t3:# <5>[1658]
	""" Pristine Statue
	[Taunt] """
	#
	pass

if Sunken_Radar_Detector:# 
	Sunken_Paladin+=['TSC_079']
class TSC_079:# <5>[1658]
	""" Radar Detector
	Scan the bottom 5 cards of your deck. Draw anyMechs found this way,then shuffle your deck. """
	#
	pass

if Sunken_Seafloor_Savior:# 
	Sunken_Paladin+=['TSC_083','TSC_083e']
class TSC_083_DredgeChoice(Choice):
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
				if c.type==CardType.MINION:
					Buff(c, 'TSC_083e', atk=2, max_health=2)
				break
		pass

class TSC_083_Dredge(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		bottom3ID=[card.id for card in target.deck[:3]]
		TSC_083_DredgeChoice(target, RandomID(*bottom3ID)*3).trigger(source)
	pass
class TSC_083:# <5>[1658]
	""" Seafloor Savior (2/2/2)
	[Battlecry:] [Dredge].If it's a minion, give it this minion's Attack and Health. """
	play = TSC_083_Dredge(CONTROLLER)
	pass
class TSC_083e:
	pass

if Sunken_Azsharan_Mooncatcher:# 
	Sunken_Paladin+=['TSC_644']
	Sunken_Paladin+=['TSC_644t']
class TSC_644:# <5>[1658]
	""" Azsharan Mooncatcher
	[Divine Shield]. [Battlecry:] Put a 'Sunken Mooncatcher' on the bottom of your deck. """
	play = ShuffleBottom(CONTROLLER, 'TSC_644t')
	pass

class TSC_644t:# <5>[1658]
	""" Sunken Mooncatcher
	[Divine Shield]. [Battlecry:] Summon a copy of this. """
	play = Summon(CONTROLLER, ExactCopy(SELF))
	pass



if Sunken_Holy_Maki_Roll:# 
	Sunken_Paladin+=['TSC_952']
class TSC_952_Action1(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		Heal(FRIENDLY_HERO, 2).trigger(source)
		newcard=Give(source.controller, 'TSC_952').trigger(source)
		if newcard[0]==[]:
			return
		newcard=newcard[0][0]
		newcard.repeatable=True
		pass
class TSC_952_Action2(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		if target.repeatable:
			Destroy(target).trigger(source)
		pass
class TSC_952:# <5>[1658]
	""" Holy Maki Roll
	Restore #2 Health. Repeatable this turn. """
	play = TSC_952_Action1(SELF)
	class Hand:
		events = OWN_TURN_END.on(TSC_952_Action2(SELF))
	pass

