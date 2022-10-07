from ast import Pass
from ..utils import *

Rev_Druid=[]

Rev_Dew_Process=True
Rev_Attorney_at_Maw=True
Rev_Incarceration=True
Rev_Natural_Causes=True
Rev_Death_Blossom_Whomper=True
Rev_Nightshade_Bud=True
Rev_Planted_Evidence=True
Rev_Topior_the_Shrubbagazzor=True
Rev_Widowbloom_Seedsman=True
Rev_Sesselie_of_the_Fae_Court=True
Rev_Hedge_Maze=True### location ###
Rev_Plot_of_Sin=True
Rev_Convoke_the_Spirits=True
Rev_Sesselie_of_the_Fae_Court=False ## not in service
Rev_Hedge_Maze=False ## not in service


if Rev_Dew_Process:# 
	Rev_Druid+=['MAW_024']
	Rev_Druid+=['MAW_024e2']
	#Rev_Druid+=['MAW_024e3']
class REV__Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		pass
class MAW_024:# <2>[1691]
	""" Dew Process
	For the rest of the game, players draw an extra card at the start of their turn. """
	play = Buff(CONTROLLER, 'MAW_024e2')
	pass
class MAW_024e2:# <2>[1691]
	""" Maw Rules
	Player draws an extra card at the start of their turn. """
	def apply(self, target):
		target.draw_extra_card=True
	pass
#class MAW_024e3:# <2>[1691]
#	""" Maw Rules
#	Draw an extra card at the start of your turn. """
#	#
#	pass





if Rev_Attorney_at_Maw:# 
	Rev_Druid+=['MAW_025']
	Rev_Druid+=['MAW_025a']
	Rev_Druid+=['MAW_025b']
	Rev_Druid+=['MAW_025e']
class REV__Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		pass
class MAW_025:# <2>[1691]
	""" Attorney-at-Maw
	<b>Choose One -</b> <b>Silence</b> a minion; or Give a minion <b>Immune</b> this turn. """
	choose = ('MAW_025a', 'MAW_025b')
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0}	
	play = ChooseBoth(CONTROLLER) & (Silence(RANDOM(ENEMY_MINIONS)), Buff(TARGET, 'MAW_025e'))
	pass
class MAW_025a:# <2>[1691]
	""" Guilty!
	<b>Silence</b> a minion. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }	#
	play = Silence(TARGET)
	pass

class MAW_025b:# <2>[1691]
	""" Innocent!
	Give a minion <b>Immune</b> this turn. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }	#
	play = Buff(TARGET, 'MAW_025e')
	pass

class MAW_025e:# <2>[1691]
	""" Proven Innocent
	<b>Immune</b> this turn. """
	tags = { GameTag.CANT_BE_DAMAGED:1 }
	events = OWN_TURN_END.on(Destroy(SELF))
	pass





if Rev_Incarceration:# 
	Rev_Druid+=['MAW_026']
	Rev_Druid+=['MAW_026e']
	#Rev_Druid+=['MAW_026e2']
class REV__Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		pass
class MAW_026:# <2>[1691]
	""" Incarceration
	Choose a minion. It goes <b>Dormant</b> for 3 turns. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0,}	#
	play = Buff(TARGET, 'MAW_026e')
	pass
class MAW_026e:# <2>[1691]
	""" Doing Time
	<b>Dormant</b>. Awaken in @ |4(turn, turns). """
	def apply(self, target):
		target.dormant = 3
	pass
#class MAW_026e2:# <2>[1691]
#	""" Doing Time
#	 """
#	#
#	pass





if Rev_Natural_Causes:# 
	Rev_Druid+=['REV_307']
	#Rev_Druid+=['REV_336t2']#Treant
class REV__Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		pass
class REV_307:# <2>[1691]
	""" Natural Causes
	Deal $2 damage. Summon a 2/2 Treant. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = Hit(TARGET, 2), Summon(CONTROLLER, 'REV_336t2')#
	pass





if Rev_Death_Blossom_Whomper:# 
	Rev_Druid+=['REV_310']
class REV_310_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		cards=[card for card in controller.deck if card.deathrattles!=[]]
		if len(cards)>0:
			card = random.choice(cards)
			card.zone=Zone.SETASIDE
			card.zone=Zone.HAND
			for action in card.deathrattles:
				source.deathrattles.append(action)
			source.data.tags[GameTag.DEATHRATTLE]=1
			source.has_deathrattle=True
		pass
class REV_310:# <2>[1691]
	""" Death Blossom Whomper
	<b>Battlecry:</b> Draw a <b>Deathrattle</b> minion and gain its <b>Deathrattle.</b> """
	play = REV_310_Action(CONTROLLER)
	pass

	Rev_Druid+=['REV_310e']
#class REV_310e:# <2>[1691]
#	""" Whomping
#	Copied <b>Deathrattle</b> from {0}. """
#	#
#	pass





if Rev_Nightshade_Bud:# 
	Rev_Druid+=['REV_311']
	Rev_Druid+=['REV_311t']
	Rev_Druid+=['REV_311t2']
class REV_311:# <2>[1691]
	""" Nightshade Bud
	<b>Choose One - </b><b>Discover</b> a minion from your deck to summon; or a spell to cast. """
	choose=("REV_311t","REV_311t2")
	#
	pass
class REV_311t_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		CastSpell(card).trigger(self.source)
		pass
class REV_311t:# <2>[1691]
	""" Sunlight Blossom
	<b>Discover</b> a spell from your deck to cast. """
	play = REV_311t_Choice(CONTROLLER, RANDOM(FRIENDLY_DECK + SPELL)*3)
	pass
class REV_311t2_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		Summon(self.controller, card).trigger(self.source)
		pass
class REV_311t2:# <2>[1691]
	""" Moonlight Blossom
	<b>Discover</b> a minion from your deck to summon. """
	play = REV_311t2_Choice(CONTROLLER, RANDOM(FRIENDLY_DECK + MINION)*3)
	pass





if Rev_Planted_Evidence:# 
	Rev_Druid+=['REV_313']
	Rev_Druid+=['REV_313e']
class REV_313_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		Buff(card, 'REV_313e').trigger(self.source)
		pass
class REV_313:# <2>[1691]
	""" Planted Evidence
	<b>Discover</b> a spell. It costs (2) less this turn. """
	play = REV_313_Choice(CONTROLLER, RandomSpell()*3)
	pass
class REV_313e:# <2>[1691]
	""" Ripe Spell
	Costs (2) less this turn. """
	cost = lambda self,i: max(i-2, 0)
	events = OWN_TURN_END.on(Destroy(SELF))## maybe this doesnt work
	pass





if Rev_Topior_the_Shrubbagazzor:# 
	Rev_Druid+=['REV_314']
	Rev_Druid+=['REV_314e']
	Rev_Druid+=['REV_314t']
class REV__Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		pass
class REV_314:# <2>[1691]
	""" Topior the Shrubbagazzor
	<b>Battlecry:</b> For the rest of the game, after you cast a Nature spell, summon a 3/3 Whelp with <b>Rush</b>. """
	play = Buff(CONTROLLER, 'REV_314e')
	pass
class REV_314e:# <2>[1691]
	""" Winter Queen's Blessing
	For the rest of the game, after you play a Nature spell summon a 3/3 Dragon. """
	events = Play(CONTROLLER, SPELL + NATURE).on(Summon(CONTROLLER, 'REV_314t')) 
	pass
class REV_314t:# <2>[1691]
	""" Whelpagazzor
	<b>Rush</b> """
	#
	pass





if Rev_Widowbloom_Seedsman:# 
	Rev_Druid+=['REV_318']
class REV__Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		pass
class REV_318:# <2>[1691]
	""" Widowbloom Seedsman
	<b>Battlecry:</b> Draw a Nature spell. Gain an empty Mana Crystal. """
	#
	pass

	Rev_Druid+=['REV_318e']
class REV_318e:# <2>[1691]
	""" Cycle of Life
	Play the card to gain an empty Mana Crystal. """
	#
	pass

	Rev_Druid+=['REV_318e2']
class REV_318e2:# <2>[1691]
	""" Play This Game Enchantment
	 """
	#
	pass





if Rev_Sesselie_of_the_Fae_Court:# 
	Rev_Druid+=['REV_319']
	Rev_Druid+=['REV_319e']
class REV_319_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		card=Draw(controller).trigger(source)
		card=card[0]
		Buff(card, 'REV_319e').trigger(source)
		pass
class REV_319:# <2>[1691]
	""" Sesselie of the Fae Court
	<b>Taunt</b> <b>Deathrattle</b>: Draw a minion. Reduce its Cost by (8). """
	deathrattle = REV_319_Action(CONTROLLER)
	pass
class REV_319e:# <2>[1691]
	""" Sesselie's Blessing
	Costs (8) less. """
	cost = lambda self, i:max(0,i-8)
	pass





if Rev_Hedge_Maze:# ### location ###
	Rev_Druid+=['REV_333']
class REV_333_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		if len(target.deathrattles)>0:
			for action in target.deathrattles:
				action.trigger(source)
		pass
class REV_333:# <2>[1691]
	""" Hedge Maze
	Trigger a friendly minion's <b>Deathrattle</b>. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_DEATHRATTLE:0 }	
	location = REV_333_Action(TARGET)
	pass





if Rev_Plot_of_Sin:# 
	Rev_Druid+=['REV_336']
	Rev_Druid+=['REV_336t2']
	Rev_Druid+=['REV_336t3']
	Rev_Druid+=['REV_336t4']
class REV_336:# <2>[1691]
	""" Plot of Sin
	Summon two 2/2  Treants. 
	<b>Infuse (@):</b> Two  5/5 Ancients instead. """
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_336t4'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_336t4', 1))
	#
	pass
class REV_336t2:# <2>[1691]
	""" Treant
	 """
	#
	pass

class REV_336t3:# <2>[1691]
	""" Ancient
	 """
	#
	pass

class REV_336t4:# <2>[1691]
	""" Plot of Sin
	<b>Infused</b> Summon two 5/5 Ancients. """
	#
	pass





if Rev_Convoke_the_Spirits:# 
	Rev_Druid+=['REV_365']
class REV__Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		pass
class REV_365:# <2>[1691]
	""" Convoke the Spirits
	Cast 8 random Druid spells <i>(targets chosen randomly)</i>. """
	#
	pass





#if Rev_Sesselie_of_the_Fae_Court:# 
#	Rev_Druid+=['REV_782']
#class REV_782:# <2>[1691]
#	""" Sesselie of the Fae Court
#	{0} {1} {2} {3} """
#	#
#	pass

#if Rev_Hedge_Maze:# 
#	Rev_Druid+=['REV_792']
#class REV_792:# <2>[1691]
#	""" Hedge Maze
#	{0} {1} """
#	#
#	pass

