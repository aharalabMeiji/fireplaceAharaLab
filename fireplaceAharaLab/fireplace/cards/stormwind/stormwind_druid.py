from ..utils import *

################################

StormWind_Druid=[]

StormWind_Druid_of_the_Reef=True## 24.0
StormWind_Moonlit_Guidance=True## 24.0
StormWind_Jerry_Rig_Carpenter=True## 24.0
StormWind_Oracle_of_Elune=True## 24.0
StormWind_Sow_the_Soil=True## 24.0
StormWind_Lost_in_the_Park=True## 24.0
StormWind_Best_in_Shell=True## 24.0
StormWind_Park_Panther=True## 24.0
StormWind_Kodo_Mount=True## 24.0
StormWind_Wickerclaw=True## 24.0
StormWind_Composting=True## 24.0
StormWind_Vibrant_Squirrel=True## 24.0
StormWind_Sheldras_Moontree=True## 24.0
StormWind_Elunes_Guidance=True## 24.0


if StormWind_Druid_of_the_Reef:# 
	StormWind_Druid+=['DED_001','DED_001a','DED_001at','DED_001b','DED_001bt','DED_001']
class DED_001:# <2>[1578] ###OK
	""" Druid of the Reef
	[Choose One - ]Transform into a 3/1 Shark with [Rush]; or a 1/3 Turtle with [Taunt]. """
	choose = ("DED_001a", "DED_001b")
	play = ChooseBoth(SELF) & (
		Summon(CONTROLLER, "DED_001c")
	)	
	pass
class DED_001a:# <2>[1578]
	""" Shark Form
	[Rush] """
	play = Morph(SELF, 'DED_001at')
	pass
class DED_001at:# <2>[1578]
	""" Druid of the Reef
	[Rush] """
	pass
class DED_001b:# <2>[1578]
	""" Sea Turtle Form
	[Taunt] """
	play = Morph(SELF, 'DED_001bt')
	pass
class DED_001bt:# <2>[1578]
	""" Druid of the Reef
	[Taunt] """
	#
class DED_001c:# <2>[1578]
	""" Druid of the Reef
	[Rush][Taunt] """
	#
	pass



if StormWind_Moonlit_Guidance:# 
	StormWind_Druid+=['DED_002']
class DED_002:# <2>[1578]####OK
	""" Moonlit Guidance
	[Discover] a copy of a card in your deck.If you play it this turn,draw the original. """
	play = Choice(CONTROLLER, RANDOM(FRIENDLY_DECK)*3).then(
		Give(CONTROLLER, Choice.CARD), Buff(Choice.CARD, 'DED_002e')
		)
	pass
class DED_002e:# <2>[1578]####OK
	""" Path of the Moon
	If played this turn, draw the original copy. """
	# do - shi yo -
	events = [
		Play(CONTROLLER, FRIENDLY+OWNER).on(Destroy(SELF), Give(CONTROLLER, ExactCopy(OWNER))),
		OWN_TURN_END.on(Destroy(SELF), Shuffle(CONTROLLER, ExactCopy(OWNER))),
		]
	pass


if StormWind_Jerry_Rig_Carpenter:# 
	StormWind_Druid+=['DED_003']
class DED_003:# <2>[1578]### it doesn't work for CORE_EX1_178 (Ancient of War)
	""" Jerry Rig Carpenter
	[Battlecry:] Draw a [Choose One] spell and split it. """
	def play(self):
		controller = self.controller
		choose_one_cards = []
		for card in controller.deck:
			if hasattr(card, 'has_choose_one') and card.has_choose_one and card.id != 'CORE_EX1_178':
				card_id = card.id
				# DED_001, SW_422, SCH_612, DMF_061, CORE_EX1_164, CORE_OG_047,CORE_EX1_160, CORE_EX1_573, CORE_EX1_165
				if card_id[:5]=='CORE_':
					card_id = card_id[5:]
				nameA = card_id + 'a'
				nameB = card_id + 'b'
				card.zone = Zone.GRAVEYARD
				Give(controller, nameA).trigger(controller)
				Give(controller, nameB).trigger(controller)
				break;
		pass
	pass




if StormWind_Oracle_of_Elune:# 
	StormWind_Druid+=['SW_419']
class SW_419:# <2>[1578] ###OK
	""" Oracle of Elune
	After you play a minion that costs (2) or less,summon a copy of it. """
	events = Play(CONTROLLER, MINION  + (COST<3)).on(Summon(CONTROLLER,ExactCopy(Play.CARD)))
	pass



if StormWind_Sow_the_Soil:# 
	StormWind_Druid+=['SW_422','SW_422a','SW_422b','SW_422e','SW_422t']
class SW_422:# <2>[1578] ###OK
	""" Sow the Soil
	[Choose One] - Give your minions +1 Attack; or_ Summon a 2/2 Treant. """
	choose = ("SW_422a", "SW_422b")
	play = ChooseBoth(SELF) & (
		Summon(CONTROLLER, 'SW_422t'), Buff(FRIENDLY_MINIONS, "SW_422e")
	)
	pass
class SW_422a:# <2>[1578]
	""" New Growth
	Summon a 2/2 Treant. """
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	play = Summon(CONTROLLER, 'SW_422t')
	pass
class SW_422b:# <2>[1578]
	""" Fertilizer
	Give your minions+1 Attack. """
	play = Buff(FRIENDLY_MINIONS, "SW_422e")
	pass
SW_422e=buff(atk=1)# <2>[1578]
""" Replanted
+1 Attack. """
class SW_422t:# <2>[1578]
	""" Treant
	 """
	#
	pass


if StormWind_Lost_in_the_Park:# 
	StormWind_Druid+=['SW_428','SW_428t','SW_428t2','SW_428t4','SW_428t4e']
class SW_428:# OK <2>[1578]
	""" Lost in the Park
	[Questline:] Gain 4 Attack with your hero. [Reward:] Gain 5 Armor. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Buff(FRIENDLY_HERO).on(
		SidequestLostInTheParkCounter(SELF, 4, [
			GainArmor(FRIENDLY_HERO,5),
			Summon(CONTROLLER,'SW_428t'), 
			Destroy(SELF)])
		)
	pass
class SW_428t:#OK <2>[1578]
	""" Defend the Squirrels
	[Questline:] Gain 5 Attack with your hero. [Reward:] Gain 5 Armor and draw a card. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Buff(FRIENDLY_HERO).on(
		SidequestLostInTheParkCounter(SELF, 5, [
			GainArmor(FRIENDLY_HERO,5),
			Summon(CONTROLLER,'SW_428t2'), 
			Draw(CONTROLLER),Destroy(SELF)
			])
		)
	pass
class SW_428t2:#OK  <2>[1578]
	""" Feral Friendsy
	[Questline:] Gain 6Attack with your hero.[Reward:] Guff the Tough. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Buff(FRIENDLY_HERO).on(
		SidequestLostInTheParkCounter(SELF, 6, [
			Give(CONTROLLER,'SW_428t4'), 
			Destroy(SELF)
			])
		)
	pass
class SW_428t4:#OK <2>[1578]
	""" Guff the Tough
	[Taunt]. [Battlecry:] Give your hero +8 Attack this turn.Gain 8 Armor. """
	play = Buff(FRIENDLY_HERO,'SW_428t4e'), GainArmor(FRIENDLY_HERO, 8)
	pass
SW_428t4e=buff(atk=8)# <2>[1578]##ONE_TURN_EFFECT
""" Guff's Buff
Your hero has Attack this turn. """
#



if StormWind_Best_in_Shell:# 
	StormWind_Druid+=['SW_429','SW_429t']
class SW_429:#OK <2>[1578]
	""" Best in Shell
	[Tradeable]Summon two 2/7_Turtles with [Taunt]. """
	play = Summon(CONTROLLER, 'SW_429t') * 2
	pass

class SW_429t:# <2>[1578]
	""" Goldshell Turtle
	[Taunt] """
	#
	pass




if StormWind_Park_Panther:# 
	StormWind_Druid+=['SW_431','SW_431e']
class SW_431:#OK <2>[1578]
	""" Park Panther
	[Rush]. Whenever this attacks, give your hero+3 Attack this turn. """
	events = Attack(SELF).on(Buff(FRIENDLY_HERO,'SW_431e'))
	pass

SW_431e=buff(atk=3)# <2>[1578] # ONE_TURN_EFFECT
""" Rawr!
+3 Attack this turn. """




if StormWind_Kodo_Mount:# 
	StormWind_Druid+=['SW_432','SW_432e','SW_432t']
class SW_432:#OK <2>[1578]
	""" Kodo Mount
	Give a minion +4/+2 and [Rush]. When it dies, summon a Kodo. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0}
	play = Buff(TARGET, 'SW_432e')
	pass

class SW_432e:# <2>[1578]
	""" On a Kodo
	+4/+2 and [Rush]. [Deathrattle:] Summon a Kodo. """
	tags = {GameTag.DEATHRATTLE:True, GameTag.RUSH:True}
	atk = lambda self,i: i+4
	max_health = lambda self,i: i+2
	deathrattle = Summon(CONTROLLER, 'SW_432t')
	pass

class SW_432t:# <2>[1578]
	""" Guff's Kodo
	[Rush] """
	#
	pass




if StormWind_Wickerclaw:# 
	StormWind_Druid+=['SW_436','SW_436e']
class SW_436:#OK <2>[1578]
	""" Wickerclaw
	After your hero gains Attack, this minion gains +2 Attack. """
	events = Buff(FRIENDLY_HERO).on(Buff(SELF, 'SW_436e'))
	pass

SW_436e=buff(atk=2)# <2>[1578]
""" Wicked Claws
+2 Attack. """




if StormWind_Composting:# 
	StormWind_Druid+=['SW_437','SW_437e']
class SW_437:#OK <2>[1578]
	""" Composting
	Give your minions"[Deathrattle:] Draw__a card." """
	play = Buff(FRIENDLY_MINIONS,'SW_437e')
	pass
class SW_437e:#<12>[1578]
	tags = {GameTag.DEATHRATTLE:True,}
	deathrattle = Draw(CONTROLLER)
	pass





if StormWind_Vibrant_Squirrel:# 
	StormWind_Druid+=['SW_439','SW_439t','SW_439t2']
class SW_439:# <2>[1578]
	""" Vibrant Squirrel
	[Deathrattle:] Shuffle 4 Acorns into your deck. When drawn,summon a 2/1 Squirrel. """
	deathrattle = Shuffle(CONTROLLER,'SW_439t')*4
	pass

class SW_439t:# <2>[1578] # CASTSWHENDRAWN
	""" Acorn
	[Casts When Drawn]Summon a 2/1 Squirrel. """
	play = Summon(CONTROLLER,'SW_439t2')
	pass

class SW_439t2:# <2>[1578]
	""" Satisfied Squirrel
	 """
	#
	pass


if StormWind_Sheldras_Moontree:# 
	StormWind_Druid+=['SW_447']
class SW_447:# <2>[1578]
	""" Sheldras Moontree
	[Battlecry:] The next 3spells you draw are[Cast When Drawn]. """
	#
	pass

if StormWind_Elunes_Guidance:# 
	StormWind_Druid+=['SW_447e','SW_447e','SW_447e2']
class SW_447:# <2>[1578]
	""" Sheldras Moontree
	[Battlecry:] The next 3 spells you draw are[Cast When Drawn]. """
	play = Buff(SELF, 'SW_447e')
	pass

class SW_447e_Action(TargetedAction):
	TARGET = ActionArg()
	CARD = CardArg()
	def do(self, source, target, card):
		controller = source.controller
		owner = source.owner
		amount = 3
		CastSpell(card).trigger(controller)
		Discard(card).trigger(controller)
		if Config.LOGINFO:
			print("Setting Counter on %r -> %i"%(target, (owner._sidequest_counter_+1)))
		owner._sidequest_counter_ += 1
		if owner._sidequest_counter_== amount:
			owner.buffs.remove(target)
			target.zone = Zone.GRAVEYARD
		pass
	pass

class SW_447e:# <2>[1578]
	""" Elune's Guidance
	Your next 3 spells are [Cast When Drawn]. """
	events = Draw(CONTROLLER,SPELL).on(SW_447e_Action(SELF, Draw.CARD))
	pass

class SW_447e2:# <2>[1578]
	""" Elune's Guidance 2
	Your next 3 spells are [Cast When Drawn]. """
	pass



###############################

