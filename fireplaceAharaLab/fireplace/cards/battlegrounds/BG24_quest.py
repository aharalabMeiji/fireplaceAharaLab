from ..utils import *
from .BG24_reward import BG24_Reward_130_Action1, BG24_Reward_134_Action1

BG24_Quest=[]
BG24_Quest_Pool=[]

BG24_Quest_Track_the_Footprints=True
BG24_Quest_Assemble_a_Lineup=True
BG24_Quest_Unmask_the_Culprit=True
BG24_Quest_Find_the_Murder_Weapon=True
BG24_Quest_Reenact_the_Murder=True
BG24_Quest_Sort_It_All_Out=True
BG24_Quest_Follow_the_Money=True
BG24_Quest_Unlikely_Duo=True
BG24_Quest_Balance_the_Scales=False #not in service
BG24_Quest_Cry_for_Help=True
BG24_Quest_Invite_the_Guests=True
BG24_Quest_Dust_for_Prints=True
BG24_Quest_Witness_Protection=False## banned 24.2.1
BG24_Quest_Exhume_the_Bones=True
BG24_Quest_Close_the_Case=False #not in service
BG24_Quest_An_Investigation=True
BG24_Quest_Discover_Quest__Reward_DNT=False #not in service
BG24_Quest_Hire_an_Investigator=True # new 24.6 ### OK ###
BG24_Quest_Crack_the_Case=True #new 24.6 ### OK ###



if BG24_Quest_Track_the_Footprints:# ### OK ###
	BG24_Quest+=['BG24_Quest_112']
	BG24_Quest_Pool+=['BG24_Quest_112']
class BG24_Quest_112:# [2466]=1, [2580]=1, 
	""" Track the Footprints
	[Quest:] Have Bob's Tavern [Refreshed] {0} times. """
	#{0}=script_data_text_0=10 -> 9 24.2.2
	events = Rerole(CONTROLLER).on(QuestCounter(SELF))
	#<Tag enumID="535" name="QUEST_PROGRESS_TOTAL" type="Int" value="9"/>
	pass

if BG24_Quest_Assemble_a_Lineup:# ### OK ###
	BG24_Quest+=['BG24_Quest_114']
	BG24_Quest_Pool+=['BG24_Quest_114']
class BG24_Quest_114:# [2466]=1, [2643]=80, [2644]=90, [2646]=90, 
	""" Assemble a Lineup
	[Quest:] Summon {0} minions. """
	#{0}=14
	events = Summon(CONTROLLER).on(QuestCounter(SELF))
	pass

if BG24_Quest_Unmask_the_Culprit:# ### if lose, OK ###
	BG24_Quest+=['BG24_Quest_120']
	BG24_Quest_Pool+=['BG24_Quest_120']
class BG24_Quest_120:# [2466]=1, [2580]=1, [2674]=2, 
	""" Unmask the Culprit
	[Quest:] Lose or tie {0} combats. """
	#{0}=3
	events = [
		TieGame(CONTROLLER).on(QuestCounter(SELF)),
		LoseGame(CONTROLLER).on(QuestCounter(SELF))
	]
	pass

if BG24_Quest_Find_the_Murder_Weapon:# ### OK ###
	BG24_Quest+=['BG24_Quest_123']
	BG24_Quest_Pool+=['BG24_Quest_123']
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
	#{0}=15 -> 14 (new 24.6)
	events = Buff(FRIENDLY_MINIONS).after(BG24_Quest_123_Action(Buff.TARGET, Buff.BUFF))
	pass

if BG24_Quest_Reenact_the_Murder:# ### OK ###
	BG24_Quest+=['BG24_Quest_124']
	BG24_Quest_Pool+=['BG24_Quest_124']
class BG24_Quest_124:# [2466]=1, [2643]=80, [2644]=80, [2646]=90, 
	""" Reenact the Murder
	[Quest:] Have {0} friendly minions die. """
	#{0}=18->19 (24.2.2)
	events = Death(FRIENDLY + MINION).on(QuestCounter(SELF))
	pass

if BG24_Quest_Sort_It_All_Out:# 
	BG24_Quest+=['BG24_Quest_125']
	BG24_Quest_Pool+=['BG24_Quest_125']
class BG24_Quest_125_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = target.controller
		amount = len(controller.field)
		for i in range(amount-1):
			if controller.field[i].atk > controller.field[i+1].atk:
				return
		QuestCounter(target).trigger(source)
		pass
class BG24_Quest_125:# [2466]=1, [2580]=1, [2642]=88, [2653]=300, [2674]=2, 
	""" Sort It All Out
	[Quest:] Order your minions from lowest to highest Attack for {0} combats. """
	#{0}=4
	events = BeginBattle(CONTROLLER).on(BG24_Quest_125_Action(SELF))
	pass

if BG24_Quest_Follow_the_Money:# ### looks OK ###
	BG24_Quest+=['BG24_Quest_126']
	BG24_Quest_Pool+=['BG24_Quest_126']
class BG24_Quest_126_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target, amount):
		pass
class BG24_Quest_126:# [2466]=1, 
	""" Follow the Money
	[Quest:] Spend {0} Gold. """
	#{0}=30
	## 30->33 (24.2.2)
	events = [
		Buy(CONTROLLER).on(QuestCounter(SELF, 3)),
		Activate(CONTROLLER).on(QuestCounter(SELF, COST(FRIENDLY_HERO_POWER)))
	]
	pass

if BG24_Quest_Unlikely_Duo:# ### OK ###
	BG24_Quest+=['BG24_Quest_151']
	BG24_Quest_Pool+=['BG24_Quest_151']
def BG24_Quest_151_Initialize(source):
	if source.id=='BG24_Quest_151':
		source.sidequest_list0=[race for race in random_picker.BG_races if race != Race.INVALID]
		source.sidequest_list0=random.sample(source.sidequest_list0, 2)
		names={Race.BEAST:'獣', Race.DEMON:'悪魔', Race.DRAGON:'ドラゴン', Race.ELEMENTAL:'エレメンタル', 
		Race.MECHANICAL:'メカ', Race.MURLOC:'マーロック', Race.PIRATE:'海賊', Race.NAGA:'ナーガ', Race.QUILBOAR:'キルボア', Race.UNDEAD:'アンデッド',Race.ALL:'すべて'}
		source.script_data_text_2=names[source.sidequest_list0[0]]
		source.script_data_text_3=names[source.sidequest_list0[1]]
	pass
class BG24_Quest_151_Action2(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		names={Race.BEAST:'獣', Race.DEMON:'悪魔', Race.DRAGON:'ドラゴン', Race.ELEMENTAL:'エレメンタル', 
		Race.MECHANICAL:'メカ', Race.MURLOC:'マーロック', Race.PIRATE:'海賊', Race.NAGA:'ナーガ', 
		Race.QUILBOAR:'キルボア', Race.UNDEAD:'アンデッド', Race.INVALID:'なし', Race.ALL:'すべて'}		
		if source.sidequest_list0==[]:
			source.sidequest_list0=[race for race in random_picker.BG_races if race != Race.INVALID]
			source.sidequest_list0=random.sample(source.sidequest_list0, 2)
		if isinstance(target,list):
			target=target[0]
		if target!=[]:
			if target.type==CardType.MINION and names[target.race] == source.script_data_text_2:
				QuestCounter(source).trigger(source)
			if target.type==CardType.MINION and names[target.race] == source.script_data_text_3:
				QuestCounter(source).trigger(source)
		pass
class BG24_Quest_151:# [2466]=1, [2496]=1, 
	""" Unlikely Duo
	[Quest:] Play {0} {2} or {3}. """
	#{0}=5, {2}{3}:種族
	events = BG_Play(CONTROLLER, FRIENDLY + MINION).on(BG24_Quest_151_Action2(Play.CARD))
	pass

if BG24_Quest_Balance_the_Scales:# ### not in service
	BG24_Quest+=['BG24_Quest_152']
	BG24_Quest_Pool+=['BG24_Quest_152']
class BG24_Quest_152:# 
	""" Balance the Scales
	[Quest:] Control at least 2 Naga, 2 Murlocs, and 2 Dragons. """
	#
	pass

if BG24_Quest_Cry_for_Help:# ### visually OK ###
	BG24_Quest+=['BG24_Quest_311']
	BG24_Quest_Pool+=['BG24_Quest_311']
class BG24_Quest_311:# 
	""" Cry for Help
	[Quest:] Play {0} [Battlecry] minions. """
	# [2466]=1, [2642]=92, [2647]=80, 
	# 	#{0}=6
	events = BG_Play(CONTROLLER, FRIENDLY+BATTLECRY).on(QuestCounter(SELF))
	pass




if BG24_Quest_Invite_the_Guests:# ### visually OK ###
	BG24_Quest+=['BG24_Quest_313']
	BG24_Quest_Pool+=['BG24_Quest_313']
class BG24_Quest_313:# [2466]=1, 
	""" Invite the Guests
	[Quest:] Buy {0} minions. """
	#{0}=7
	events = Buy(CONTROLLER).on(QuestCounter(SELF))
	pass




if BG24_Quest_Dust_for_Prints:# 
	BG24_Quest+=['BG24_Quest_314']
	BG24_Quest_Pool+=['BG24_Quest_314']
class BG24_Quest_314:# [2466]=1, [2650]=70, [2651]=70, 
	""" Dust for Prints
	[Quest:] Add {0} cards to your hand. """
	#{0}=15
	events = [
		Draw(CONTROLLER).on(QuestCounter(SELF)),
		Give(CONTROLLER).on(QuestCounter(SELF))
		]
	pass

if BG24_Quest_Witness_Protection:#  ## banned 24.2.1
	BG24_Quest+=['BG24_Quest_318']
	BG24_Quest_Pool+=['BG24_Quest_318']
class BG24_Quest_318:# [2466]=1, 
	""" Witness Protection
	[Quest:] Have a friendly [Taunt] minion attacked {0} times. """
	#{0}=8 <Tag enumID="535" name="QUEST_PROGRESS_TOTAL" type="Int" value="8"/>
	events = Attack(ENEMY, FRIENDLY + MINION + TAUNT).on(QuestCounter(SELF))
	pass




if BG24_Quest_Exhume_the_Bones:# ### OK ###
	BG24_Quest+=['BG24_Quest_320']
	BG24_Quest_Pool+=['BG24_Quest_320']
class BG24_Quest_320:# [2466]=1, [2580]=1, [2643]=80, [2644]=90, [2646]=90, 
	""" Exhume the Bones
	[Quest:] Trigger {0} friendly [Deathrattles]. """
	#{0}=6 <Tag enumID="535" name="QUEST_PROGRESS_TOTAL" type="Int" value="6"/>
	events = Deathrattle(FRIENDLY + MINION).on(QuestCounter(SELF))
	pass




if BG24_Quest_Close_the_Case:# ? not in service
	BG24_Quest+=['BG24_Quest_328']
	BG24_Quest_Pool+=['BG24_Quest_328']
class BG24_Quest_328:# 
	""" Close the Case
	[Quest:] Win the game. """
	#
	pass




if BG24_Quest_Hire_an_Investigator:# ### OK ###
	BG24_Quest+=['BG24_Quest_351']
	BG24_Quest_Pool+=['BG24_Quest_351']
class BG24_Quest_351_Action(GameAction):
	def do(self, source):
		controller = source.controller
		amount=controller.mana
		if amount>0:
			QuestCounter(source).trigger(source)
class BG24_Quest_351:# 
	""" Hire an Investigator
	[Quest:] End your turn with unspent Gold {0} times. """
	#{0}=3 -> 2 (24.6.2)
	events = OWN_TURN_END.on(BG24_Quest_351_Action())
	pass




if BG24_Quest_Crack_the_Case:### OK ###
	BG24_Quest+=['BG24_Quest_352']
	BG24_Quest_Pool+=['BG24_Quest_352']
class BG24_Quest_352:#
	""" Crack the Case
	[Quest:] Have friendly minions attack {0} times."""
	## {0}=11
	#<Tag enumID="535" name="QUEST_PROGRESS_TOTAL" type="Int" value="11"/>
	events = BG_Attack(FRIENDLY + MINION).on(QuestCounter(SELF))


from .BG24_reward import BG24_Reward_Pool
if BG24_Quest_An_Investigation:# ### OK ### no weight for the parameter of quests
	BG24_Quest+=['BG24_Quest_Bob']
class BG24_Quest_Bob_Choice(Choice):
	def do(self, source, player, cards, option=None):
		super().do(source, player, cards, option=None)
		for card in cards:
			card.script_data_text_0=str(card.quest_progress_total)
			if card.id=='BG24_Quest_151':
				BG24_Quest_151_Initialize(card)
			if card.id==Config.QUEST_PRESET and Config.REWARD_PRESET!='':
				rewardID=Config.REWARD_PRESET
			else:
				rewardID = random.choice(BG24_Reward_Pool)
			reward = player.card(rewardID)## zone=SETASIDE
			if reward.id=='BG24_Reward_130':
				BG24_Reward_130_Action1(player, reward)
			if reward.id=='BG24_Reward_134':
				BG24_Reward_134_Action1(reward)
			card.sidequest_list0=[reward]
			## change the parameter in the card
			##130=reward.data.get(2467,0)
			#card.quest_progress_total= int(card.quest_progress_total*130/100)
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		CastSecret(card).trigger(self.source)
	pass
class BG24_Quest_Bob_Action(GameAction):
	TARGET=ActionArg()
	def do(self, source):
		## may need to check if target is the controller
		controller=source.controller
		if Config.QUEST_PRESET=='':
			quests=BG24_Quest_Pool
			if len(quests)>3:
				quests=random.sample(quests,3)
		else:
			quests=[Config.QUEST_PRESET]+random.sample(BG24_Quest_Pool,2)
		BG24_Quest_Bob_Choice(CONTROLLER, RandomID(*quests)*3).trigger(source)
		choiceAction(controller)
		Destroy(source).trigger(source)
		pass
class BG24_Quest_Bob:# [2732]=1, 
	""" An Investigation!
	In @ |4(turn, turns), [Discover] a [Quest]! """
	events = BeginBar(CONTROLLER).on(SidequestCounter(SELF, 4, [BG24_Quest_Bob_Action()]))
	pass

if BG24_Quest_Discover_Quest__Reward_DNT:# 
	BG24_Quest+=['BG24_QuestsPlayerEnch_t']
class BG24_QuestsPlayerEnch_t:# 
	""" Discover Quest + Reward [DNT]
	[Discover] a Quest and Reward pair. [DNT] """
	#
	pass

