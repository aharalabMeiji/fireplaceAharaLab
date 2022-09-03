
from ..utils import *

StormWind_Priest=[]

StormWind_Amulet_of_Undying=True  ###
StormWind_Defias_Leper=True  ###
StormWind_Copycat=True  ###
StormWind_Shadowcloth_Needle=True  ###
StormWind_Seek_Guidance=True  ###
StormWind_Call_of_the_Grave=True  ###
StormWind_Shard_of_the_Naaru=True  ###
StormWind_Void_Shard=True  ###
StormWind_Elekk_Mount=True  ###
StormWind_Twilight_Deceptor=True  ###
StormWind_Psyfiend=True  ###
StormWind_Voidtouched_Attendant=True  ###
StormWind_Darkbishop_Benedictus=True  ###


##################################


if StormWind_Amulet_of_Undying:# 
	StormWind_Priest+=['DED_512']
class DED_512:# <6>[1578]
	""" Amulet of Undying
	[Tradeable]Resurrect @ friendly[Deathrattle] |4(minion, minions).<i>(Upgrades when [Traded]!)</i> """
	def play(self):
		cards=[card for card in self.controller.graveyard if card.type==CardType.MINION and card.has_deathrattle==True]
		amount = min(len(cards), self.script_data_num_1+1)
		cards = random.sample(cards, amount)
		for card in cards:
			Summon(self.controller, card.id).trigger(self)
	class Hand:
		events = Trade(CONTROLLER).after(AddScriptDataNum1(SELF, 1))
	pass




if StormWind_Defias_Leper:# 
	StormWind_Priest+=['DED_513']
class DED_513:# <6>[1578]
	""" Defias Leper  (2/3/2)
	[Battlecry:] If you're holdinga Shadow spell, deal2 damage. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }	
	play = Find(FRIENDLY_HAND + SHADOW) & Hit(TARGET, 2)
	#
	pass




if StormWind_Copycat:# 
	StormWind_Priest+=['DED_514','DED_514e']
class DED_514:# <6>[1578]
	""" Copycat 
	[Battlecry:] Add a copy of the next card your opponent plays to your hand. """
	play = Buff(CONTROLLER, 'DED_514e')
	pass
class DED_514e:
	events = Play(OPPONENT).after(
		Give(CONTROLLER, Copy(Play.CARD)),
		Destroy(SELF)
		)
	pass



if StormWind_Shadowcloth_Needle:# 
	StormWind_Priest+=['SW_012']
class SW_012:# <6>[1578]
	""" Shadowcloth Needle
	After you cast a Shadowspell, deal 1 damageto all enemies.Lose 1 Durability. """
	events = Play(CONTROLLER, SHADOW).after(
		Hit(ENEMY_CHARACTERS, 1),
		Hit(FRIENDLY_WEAPON, 1)
		)
	pass




if StormWind_Seek_Guidance:# 
	StormWind_Priest+=['SW_433']
	StormWind_Priest+=['SW_433t']
	StormWind_Priest+=['SW_433t2']
	StormWind_Priest+=['SW_433t3']
	StormWind_Priest+=['SW_433t3a']
class SW_433_Quest1(TargetedAction):
	CARD=ActionArg()
	def do(self, source, card):
		if isinstance(card,list):
			card = card[0]
		self.record = [None,None,None]
		if card.cost in [2,3,4]:
			if self.record[card.cost-2]==None:
				self.record[card.cost-2]=card
		if self.record[0]!=None and self.record[1]!=None and self.record[2]!=None: 
			Discover(CONTROLLER, RANDOM(FRIENDLY_DECK)*3).trigger(source)
			Summon(source.controller, 'SW_433t').trigger(source)
			Destroy(source).trigger(source)
class SW_433:# <6>[1578]
	""" Seek Guidance
	[Questline:] Play a 2, 3,and 4-Cost card.[Reward:] [Discover] a cardfrom your deck. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}
	events = Play(CONTROLLER).on(SW_433_Quest1(Play.CARD))
	pass
class SW_433_Quest2(TargetedAction):
	CARD=ActionArg()
	def do(self, source, card):
		if isinstance(card,list):
			card = card[0]
		self.record = [None,None]
		if card.cost in [5,6]:
			if self.record[card.cost-5]==None:
				self.record[card.cost-5]=card
		if self.record[0]!=None and self.record[1]!=None: 
			Discover(CONTROLLER, RANDOM(FRIENDLY_DECK)*3).trigger(source)
			Summon(source.controller, 'SW_433t2').trigger(source)
			Destroy(source).trigger(source)
class SW_433t:# <6>[1578]
	""" Discover the Void Shard
	[Questline:] Play a 5and 6-Cost card.[Reward:] [Discover] a card from your deck. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}	#
	events = Play(CONTROLLER).on(SW_433_Quest2(Play.CARD))
	pass
class SW_433_Quest3(TargetedAction):
	CARD=ActionArg()
	def do(self, source, card):
		if isinstance(card,list):
			card = card[0]
		self.record = [None,None]
		if card.cost in [7,8]:
			if self.record[card.cost-7]==None:
				self.record[card.cost-7]=card
		if self.record[0]!=None and self.record[1]!=None: 
			Give(CONTROLLER, 'SW_433t3').trigger(source)
			Destroy(source).trigger(source)
class SW_433t2:# <6>[1578]
	""" Illuminate the Void
	[Questline:] Play a 7and 8-Cost card.[Reward:] Xyrella,the Sanctified. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}	#
	events = Play(CONTROLLER).on(SW_433_Quest3(Play.CARD))
	pass
class SW_433t3:# <6>[1578]
	""" Xyrella, the Sanctified
	[Taunt][Battlecry:] Shuffle the Purified Shard into your deck. """
	play = Shuffle(CONTROLLER, 'SW_433t3a')
	pass
class SW_433t3a:# <6>[1578]
	""" Purified Shard
	Destroy the enemy hero. """
	play=Hit(ENEMY_HERO,10000)#Destroy(ENEMY_HERO)
	pass




if StormWind_Call_of_the_Grave:# 
	StormWind_Priest+=['SW_440']
class SW_440_Choice(Choice):
	def choose(self, card):
		super().choose(card)
		self.next_choice=None
		if Config.LOGINFO:
			print("(GenericChoice.choose)%s chooses %r"%(card.controller.name, card))
		for _card in self.cards:
			if _card is card:
				if len(self.player.hand) < self.player.max_hand_size:
					new_card = self.player.card(_card.id)# make a new copy
					new_card.zone = Zone.HAND
					if new_card.cost <= new_card.controller.mana:
						actions = new_card.deathrattles
						for action in actions:
							if isinstance(action, Action):
								action.trigger(new_card.controller)
							else:
								action[0].trigger(self.source)

class SW_440:# <6>[1578]
	""" Call of the Grave
	[Discover] a [Deathrattle] minion. If you have enough Mana to play it, trigger its [Deathrattle]. """
	play = SW_440_Choice(CONTROLLER, RandomDeathrattle()*3)
	pass




if StormWind_Shard_of_the_Naaru:# 
	StormWind_Priest+=['SW_441']
class SW_441:# <6>[1578]
	""" Shard of the Naaru
	[Tradeable][Silence] all enemy minions. """
	play = Silence(ENEMY_MINIONS)
	pass




if StormWind_Void_Shard:# 
	StormWind_Priest+=['SW_442']
class SW_442:# <6>[1578]
	""" Void Shard
	[Lifesteal]Deal $4 damage. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0}
	play = Hit(TARGET, 4)
	#<Tag enumID="685" name="LIFESTEAL" type="Int" value="1"/>
	pass




if StormWind_Elekk_Mount:# 
	StormWind_Priest+=['SW_443']
	StormWind_Priest+=['SW_443e']
	StormWind_Priest+=['SW_443t']
class SW_443:# <6>[1578]
	""" Elekk Mount
	Give a minion +4/+7 and [Taunt]. When it dies, summon an Elekk. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0}	
	play = Buff(TARGET, 'SW_443e')
	pass
class SW_443e:# <6>[1578]
	""" On an Elekk
	+4/+7 and [Taunt]. [Deathrattle:] Summon an Elekk. """
	tags = {
		GameTag.ATK:4,
		GameTag.HEALTH:7,
		GameTag.TAUNT:True
		}
	deathrattle = Summon(CONTROLLER, 'SW_443t')
	pass
class SW_443t:# <6>[1578]
	""" Xyrella's Elekk
	[Taunt] """
	#
	pass




if StormWind_Twilight_Deceptor:# 
	StormWind_Priest+=['SW_444']
class SW_444:# <6>[1578]
	""" Twilight Deceptor
	[Battlecry:] If any hero took damage this turn, draw a Shadow spell. """
	def play(self):
		controller = self.controller
		actions = [action for action in controller._targetedaction_log if\
			isinstance(action['class'],Hit) and action['target'].type==CardType.HERO and action['target_args'][0]>0 and action['turn']==controller.game.turn]
		if len(actions)>0:
			cards = [card for card in controller.deck if card.type==CardType.SPELL and card.spell_school==SpellSchool.SHADOW]
			if len(cards)>0:
				Give(controller, random.choice(cards)).trigger(self)
	pass




if StormWind_Psyfiend:# 
	StormWind_Priest+=['SW_445']
class SW_445:# <6>[1578]
	""" Psyfiend
	After you cast a Shadow spell, deal 2 damage to each hero. """
	events = Play(CONTROLLER, SHADOW).after(Hit(ALL_HEROES, 2))
	pass




if StormWind_Voidtouched_Attendant:# 
	StormWind_Priest+=['SW_446']
	StormWind_Priest+=['SW_446e']
class SW_446:# <6>[1578]
	""" Voidtouched Attendant
	Both heroes take one extra damage from all sources. """
	play = SetAttr(ALL_HEROES, 'get_extra_damage', 1)
	pass
class SW_446e:# <6>[1578]
	""" Voidtouched
	Both heroes take one extra damage from all sources. """
	#
	pass




if StormWind_Darkbishop_Benedictus:# 
	StormWind_Priest+=['SW_448']
class SW_448_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		cards = [card for card in target.deck if card.type==CardType.SPELL and card.spell_school!=SpellSchool.SHADOW]
		if len(cards)==0:
			Morph(source, 'CORE_EX1_625')

class SW_448:# <6>[1578]
	""" Darkbishop Benedictus
	[Start of Game:] If the spells in your deck are all Shadow, enter Shadowform(CORE_EX1_625). """
	class Hand:
		events = BeginGame(CONTROLLER).on(SW_448_Action(CONTROLLER))
	class Deck:
		events = BeginGame(CONTROLLER).on(SW_448_Action(CONTROLLER))
	pass

#####################################
