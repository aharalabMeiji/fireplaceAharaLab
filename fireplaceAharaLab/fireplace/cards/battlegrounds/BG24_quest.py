from ..utils import *

BG24_Quest=[]

BG24_Quest_Track_the_Footprints=True
BG24_Quest_Assemble_a_Lineup=True
BG24_Quest_Unmask_the_Culprit=True
BG24_Quest_Find_the_Murder_Weapon=True
BG24_Quest_Reenact_the_Murder=True
BG24_Quest_Sort_It_All_Out=True
BG24_Quest_Follow_the_Money=True
BG24_Quest_Unlikely_Duo=True
BG24_Quest_Balance_the_Scales=True
BG24_Quest_Cry_for_Help=True
BG24_Quest_Invite_the_Guests=True
BG24_Quest_Dust_for_Prints=True
BG24_Quest_Witness_Protection=False## banned 24.2.1
BG24_Quest_Exhume_the_Bones=True
BG24_Quest_Close_the_Case=True
BG24_Quest_An_Investigation=True
BG24_Quest_Discover_Quest__Reward_DNT=True


if BG24_Quest_Track_the_Footprints:# 
	BG24_Quest+=['BG24_Quest_112']
class BG24_Quest_112:# [2466]=1, [2580]=1, 
	""" Track the Footprints
	[Quest:] Have Bob's Tavern [Refreshed] {0} times. """
	#{0}=script_data_text_0=10
	events = Rerole(CONTROLLER).on(QuestCounter(SELF))
	pass

if BG24_Quest_Assemble_a_Lineup:# 
	BG24_Quest+=['BG24_Quest_114']
class BG24_Quest_114:# [2466]=1, [2643]=80, [2644]=90, [2646]=90, 
	""" Assemble a Lineup
	[Quest:] Summon {0} minions. """
	#{0}=14
	events = Summon(CONTROLLER).on(QuestCounter(SELF))
	pass

if BG24_Quest_Unmask_the_Culprit:# 
	BG24_Quest+=['BG24_Quest_120']
class BG24_Quest_120:# [2466]=1, [2580]=1, [2674]=2, 
	""" Unmask the Culprit
	[Quest:] Lose or tie {0} combats. """
	#{0}=3
	events = [
		TieGame(CONTROLLER).on(QuestCounter(SELF)),
		LoseGame(CONTROLLER).on(QuestCounter(SELF))
	]
	pass

if BG24_Quest_Find_the_Murder_Weapon:# 
	BG24_Quest+=['BG24_Quest_123']
class BG24_Quest_123_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self, source, target, buff):
		if buff.id in [bf.id for bf in target.buffs]:
			if buff.atk>0 or buff.max_health>0:
				QuestCounter(source).trigger(source)
		pass
class BG24_Quest_123:# [2466]=1, [2580]=1, 
	""" Find the Murder Weapon
	[Quest:] Increase a friendly minion's stats {0} times. """
	#{0}=15
	events = Buff(FRIENDLY_MINIONS).on(BG24_Quest_123_Action(Buff.TARGET, Buff.BUFF))
	pass

if BG24_Quest_Reenact_the_Murder:# 
	BG24_Quest+=['BG24_Quest_124']
class BG24_Quest_124:# [2466]=1, [2643]=80, [2644]=80, [2646]=90, 
	""" Reenact the Murder
	[Quest:] Have {0} friendly minions die. """
	#{0}=18
	events = Death(FRIENDLY_MINIONS).on(QuestCounter(SELF))
	pass

if BG24_Quest_Sort_It_All_Out:# 
	BG24_Quest+=['BG24_Quest_125']
class BG24_Quest_125:# [2466]=1, [2580]=1, [2642]=88, [2653]=300, [2674]=2, 
	""" Sort It All Out
	[Quest:] Order your minions from lowest to highest Attack for {0} combats. """

	#{0}=4
	pass

if BG24_Quest_Follow_the_Money:# 
	BG24_Quest+=['BG24_Quest_126']
class BG24_Quest_126:# [2466]=1, 
	""" Follow the Money
	[Quest:] Spend {0} Gold. """
	#{0}=25
	pass

if BG24_Quest_Unlikely_Duo:# 
	BG24_Quest+=['BG24_Quest_151']
class BG24_Quest_151:# [2466]=1, [2496]=1, 
	""" Unlikely Duo
	[Quest:] Play {0} {2} or {3}. """
	#{0}=5, {2}{3}:�푰
	pass

if BG24_Quest_Balance_the_Scales:# ????????????????
	BG24_Quest+=['BG24_Quest_152']
class BG24_Quest_152:# 
	""" Balance the Scales
	[Quest:] Control at least 2 Naga, 2 Murlocs, and 2 Dragons. """
	#
	pass

if BG24_Quest_Cry_for_Help:# 
	BG24_Quest+=['BG24_Quest_311']
class BG24_Quest_311:# [2466]=1, [2642]=92, [2647]=80, 
	""" Cry for Help
	[Quest:] Play {0} [Battlecry] minions. """
	#{0}=6
	pass

if BG24_Quest_Invite_the_Guests:# 
	BG24_Quest+=['BG24_Quest_313']
class BG24_Quest_313:# [2466]=1, 
	""" Invite the Guests
	[Quest:] Buy {0} minions. """
	#{0}=7
	pass

if BG24_Quest_Dust_for_Prints:# 
	BG24_Quest+=['BG24_Quest_314']
class BG24_Quest_314:# [2466]=1, [2650]=70, [2651]=70, 
	""" Dust for Prints
	[Quest:] Add {0} cards to your hand. """
	#{0}=15
	pass

if BG24_Quest_Witness_Protection:#  ## banned 24.2.1
	BG24_Quest+=['BG24_Quest_318']
class BG24_Quest_318:# [2466]=1, 
	""" Witness Protection
	[Quest:] Have a friendly [Taunt] minion attacked {0} times. """
	#{0}=8 <Tag enumID="535" name="QUEST_PROGRESS_TOTAL" type="Int" value="8"/>
	pass

if BG24_Quest_Exhume_the_Bones:# 
	BG24_Quest+=['BG24_Quest_320']
class BG24_Quest_320:# [2466]=1, [2580]=1, [2643]=80, [2644]=90, [2646]=90, 
	""" Exhume the Bones
	[Quest:] Trigger {0} friendly [Deathrattles]. """
	#{0}=6 <Tag enumID="535" name="QUEST_PROGRESS_TOTAL" type="Int" value="6"/>
	pass

if BG24_Quest_Close_the_Case:# ???????????
	BG24_Quest+=['BG24_Quest_328']
class BG24_Quest_328:# 
	""" Close the Case
	[Quest:] Win the game. """
	#
	pass

if BG24_Quest_An_Investigation:# ***********
	BG24_Quest+=['BG24_Quest_Bob']
class BG24_Quest_Bob:# [2732]=1, 
	""" An Investigation!
	In @ |4(turn, turns), [Discover] a [Quest]! """
	#
	pass

if BG24_Quest_Discover_Quest__Reward_DNT:# 
	BG24_Quest+=['BG24_QuestsPlayerEnch_t']
class BG24_QuestsPlayerEnch_t:# 
	""" Discover Quest + Reward [DNT]
	[Discover] a Quest and Reward pair. [DNT] """
	#
	pass

