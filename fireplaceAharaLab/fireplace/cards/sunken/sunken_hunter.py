from ..utils import *

Sunken_Hunter=[]


Sunken_Ancient_Krakenbane=True  ###
Sunken_Shellshot=True  ###
Sunken_K9_0tron=True  ###
Sunken_Barbed_Nets=True  ###
Sunken_Harpoon_Gun=True  ###
Sunken_Twinbow_Terrorcoil=True  ###
Sunken_Conchs_Call=True  ###
Sunken_Raj_Nazjan=True  ###
Sunken_Emergency_Maneuvers=True  ###
Sunken_Azsharan_Saber=True  ###
Sunken_Urchin_Spines=True  ###
Sunken_Nagas_Pride=True  ###
Sunken_Hydralodon=True  ###



if Sunken_Ancient_Krakenbane:# 
	Sunken_Hunter+=['TID_074']
class TID_074:# <3>[1658]
	""" Ancient Krakenbane
	[Battlecry:] If you've cast three spells while holding this, deal 5 damage.@<i>({0} left!)</i>@<i>(Ready!)</i> """
	requirements={PlayReq.REQ_TARGET_IF_AVAILABLE:0,}
	class Hand:
		events = OWN_SPELL_PLAY.on(SidequestCounter(SELF, 3, SetScriptDataNum1(SELF, True)))
	play = ScriptDataNum1True(SELF) & Hit(TARGET, 5)
	pass




if Sunken_Shellshot:# 
	Sunken_Hunter+=['TID_075']
class TID_075:# <3>[1658]
	""" Shellshot
	Deal $3 damage to a random enemy minion. Repeat this with 1 less damage. """
	play = (
		Hit(RANDOM(ENEMY_MINIONS), 3),
		Find(ENEMY_MINIONS) & Hit(RANDOM(ENEMY_MINIONS), 2),
		Find(ENEMY_MINIONS) & Hit(RANDOM(ENEMY_MINIONS), 1),
	)
	pass




if Sunken_K9_0tron:#  ###OK
	Sunken_Hunter+=['TID_099']
class TID_099_DredgeChoice(Choice):
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
				if c.cost==1 and c.type==CardType.MINION:
					c.zone=Zone.SETASIDE
					Summon(controller,c).trigger(controller)
					#c.zone=Zone.PLAY# ???
				break
		pass
class TID_099_Dredge(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		bottom3ID=[card.id for card in target.deck[:3]]
		TID_099_DredgeChoice(target, RandomID(*bottom3ID)*3).trigger(source)
	pass
class TID_099:# <3>[1658]
	""" K9_0tron
	[Battlecry:] [Dredge].If it's a 1-Cost minion, summon it. """
	play = TID_099_Dredge(CONTROLLER)
	pass




if Sunken_Barbed_Nets:# 
	Sunken_Hunter+=['TSC_023']
class TSC_023:# <3>[1658]######################## difficult
	""" Barbed Nets
	Deal $2 damage to an enemy. If you played a Naga while holding this,choose a second target. """
	class Hand:
		events = Play(CONTROLLER, NAGA).on(SetScriptDataNum1(SELF, True))
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_ENEMY_TARGET:0, }
	play = ScriptDataNum1True(SELF) & Hit(TARGET, 4) | Hit(TARGET, 2)
	pass




if Sunken_Harpoon_Gun:# 
	Sunken_Hunter+=['TSC_070']
class TSC_070_DredgeChoice(Choice):
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
				if hasattr(c,'race') and c.race==Race.BEAST:
					c.cost-=3## c._cost-=3
				break
		pass
class TSC_070_Dredge(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		bottom3ID=[card.id for card in target.deck[:3]]
		TSC_070_DredgeChoice(target, RandomID(*bottom3ID)*3).trigger(source)
	pass
class TSC_070:# <3>[1658] weapon
	""" Harpoon Gun
	After your hero attacks, [Dredge]. If it's a Beast, reduce its Cost by (3). """
	events = Attack(FRIENDLY_HERO).after(TSC_070_Dredge(CONTROLLER))
	pass




if Sunken_Twinbow_Terrorcoil:# 
	Sunken_Hunter+=['TSC_071']
	Sunken_Hunter+=['TSC_071e']
	Sunken_Hunter+=['TSC_071e2']
class TSC_071:# <3>[1658]# 
	""" Twinbow Terrorcoil
	[Battlecry:] If you've cast a spell while holding this, your next spell casts twice. """
	class Hand:
		events = Play(CONTROLLER, SPELL).on(SetScriptDataNum1(SELF, True))
	play = ScriptDataNum1True(SELF) & Buff(CONTROLLER, 'TSC_071e')
class TSC_071e:# <3>[1658]
	""" Twinned
	Your next spell casts twice. """
	Tags= {GameTag.SPELLS_CAST_TWICE:True, }
	events = OWN_SPELL_PLAY.on(Destroy(SELF))
class TSC_071e2:# <3>[1658]
	""" Twinning
	Your next spell casts twice. """
	pass




if Sunken_Conchs_Call:# 
	Sunken_Hunter+=['TSC_072']
class TSC_072:# <3>[1658]
	""" Conch's Call
	Draw a Naga and a spell. """
	play = Give(CONTROLLER, RANDOM(FRIENDLY_DECK + NAGA)),Give(CONTROLLER, RANDOM(FRIENDLY_DECK + SPELL))
	pass




if Sunken_Raj_Nazjan:# 
	Sunken_Hunter+=['TSC_073']
class TSC_073:# <3>[1658]
	""" Raj Naz'jan
	After you cast a spell, deal damage equal to its Cost to the enemy Hero. """
	events = OWN_SPELL_PLAY.after(Hit(ENEMY_HERO, COST(Play.CARD)))
	pass




if Sunken_Emergency_Maneuvers:# 
	Sunken_Hunter+=['TSC_929']
	Sunken_Hunter+=['TSC_929t']
class TSC_929_Action(TargetedAction):
	TARGET=ActionArg()
	CARD=ActionArg()
	amount=IntArg()
	def do(self,source,target,card,amount):
		controller = target
		if isinstance(card,list):
			card=card[0]
		for i in range(amount):
			newcard = Summon(controller, card.id).trigger(source)
			newcard = newcard[0][0]
			newcard.dormant = 1
class TSC_929:# <3>[1658]
	""" Emergency Maneuvers
	[Secret:] When a friendly minion dies, summon a copy of it.It's [Dormant] for 1 turn. """
	secret = Death(FRIENDLY_MINIONS).on(TSC_929_Action(CONTROLLER, Death.TARGET, 1))

class TSC_929t:# <3>[1658]
	""" Improved Emergency Maneuvers
	[Secret:] When a friendly minion dies, summon two copies of it.They're [Dormant] for 1 turn. """
	secret = Death(FRIENDLY_MINIONS).on(TSC_929_Action(CONTROLLER, Death.TARGET, 2))
	pass




if Sunken_Azsharan_Saber:# 
	Sunken_Hunter+=['TSC_945']
	Sunken_Hunter+=['TSC_945t']
class TSC_945:# <3>[1658]
	""" Azsharan Saber
	[[Rush].] [Deathrattle:] Put a'Sunken Saber' on thebottom of your deck. """
	deathrattle = ShuffleBottom(CONTROLLER, 'TSC_945t')
class TSC_945t:# <3>[1658]
	""" Sunken Saber
	[[Rush].] [Deathrattle:] Summon a Beast from your deck. """
	deathrattle = Summon(CONTROLLER, RANDOM(FRIENDLY_DECK + BEAST))
	pass




if Sunken_Urchin_Spines:# 
	Sunken_Hunter+=['TSC_946']
	Sunken_Hunter+=['TSC_946e']
	Sunken_Hunter+=['TSC_946e2']
class TSC_946:# <3>[1658]
	""" Urchin Spines
	Your spells this turn are [Poisonous]. """ ## This means that damages by spell turns poinsonous.
	play = Buff(FRIENDLY_HAND + SPELL, 'TSC_946e')
class TSC_946e:# <3>[1658]
	""" Poisonous Urchin
	Your spells are [Poisonous]. """
	poisonous = True
	#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>
class TSC_946e2:# <3>[1658]
	pass




if Sunken_Nagas_Pride:# 
	Sunken_Hunter+=['TSC_947e']
	Sunken_Hunter+=['TSC_947']
	Sunken_Hunter+=['TSC_947t']
class TSC_947:# <3>[1658]
	""" Naga's Pride
	Summon two 2/2 Lionfish. If you played a Naga while holding this, give them +1/+1. """
	class Hand:
		events = Play(CONTROLLER, NAGA).on(SetScriptDataNum1(SELF, True))
	play = ScriptDataNum1True(SELF) & Summon(CONTROLLER,'TSC_947t').then(Buff(Summon.CARD,'TSC_947e')) | Summon(CONTROLLER,'TSC_947t')
TSC_947e=buff(1,1)
class TSC_947t:# <3>[1658]
	""" Lionfish
	 """
	pass




if Sunken_Hydralodon:# 
	Sunken_Hunter+=['TSC_950']
	Sunken_Hunter+=['TSC_950t']
	Sunken_Hunter+=['TSC_950t2']
class TSC_950:# <3>[1658]
	""" Hydralodon
	[Colossal +2][Battlecry:] Give your_Hydralodon Heads [Rush]. """
	play = (
		Summon(CONTROLLER, 'TSC_950t').then(Buff(Summon.CARD, 'TSC_950e2')),
		Summon(CONTROLLER, 'TSC_950t2').then(Buff(Summon.CARD, 'TSC_950e2'))
		)

class TSC_950t:# <3>[1658]
	""" Hydralodon Head
	[Deathrattle:] If you control Hydralodon, summon 2 Hydralodon Heads. """
	deathrattle = Find(FRIENDLY + ID('TSC_950')) & (
		Summon(CONTROLLER, 'TSC_950t'),
		Summon(CONTROLLER, 'TSC_950t2')
		)
@custom_card
class TSC_950e2:
	tags={
		GameTag.CARDNAME: "Doggie Biscuit",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.RUSH:True
		}

class TSC_950t2:# <3>[1658]
	""" Hydralodon Head
	[Deathrattle:] If you control Hydralodon, summon 2 Hydralodon Heads. """
	deathrattle = Find(FRIENDLY + ID('TSC_950')) & (
		Summon(CONTROLLER, 'TSC_950t'),
		Summon(CONTROLLER, 'TSC_950t2')
		)
	pass


