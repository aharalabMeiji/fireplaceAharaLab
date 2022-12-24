from ..utils import *

Lich_Hunter=[]

Lich_Conjured_Arrow=True
Lich_Arcane_Quiver=True
Lich_Ricochet_Shot=True
Lich_Eversong_Portal=True
Lich_Halduron_Brightwing=True
Lich_Scourge_Tamer=True
Lich_Shockspitter=True### Resurrect ICC_828t
Lich_Silvermoon_Farstrider=True
Lich_Keeneye_Spotter=True
Lich_Hope_of_QuelThalas=True


if Lich_Conjured_Arrow:# 
	Lich_Hunter+=['RLK_804']
class RLK_804:# <3>[1776]
	""" Conjured Arrow (spell:2)
	Deal $2 damage to a minion. <b>Manathirst (6):</b> Draw that many cards. """
	requirements = REQUIRE_ENEMY_MINION_TARGET
	play = Manathirst(6, [Hit(TARGET, 2)], [Draw(CONTROLLER), Draw(CONTROLLER)])
	pass

if Lich_Arcane_Quiver:# 
	Lich_Hunter+=['RLK_817']
class RLK_817_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		card.zone=Zone.HAND
		if getattr(card, 'spell_school', None)==SpellSchool.ARCANE:
			card.spellpower_by_spell+=1
class RLK_817_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		cards=[card for card in controller.deck if card.type==CardType.SPELL]
		if len(cards)>4:
			cards=random.sample(cards,3)
		cardsID=[card.id for card in cards]
		for card in reversed(cards):
			card.discard()
		RLK_817_Choice(controller, RandomID(*cardsID)).trigger(source)
		pass
class RLK_817:# <3>[1776]
	""" Arcane Quiver (spell:2)
	<b>Discover</b> a spell from your deck. If it's Arcane, give it <b>Spell Damage +1</b>. """
	play = RLK_817_Action()
	pass

if Lich_Ricochet_Shot:# 
	Lich_Hunter+=['RLK_818']
class RLK_818_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		for count in range(3):
			card=random.choice(controller.opponent.characters)
			Hit(card, 1).trigger(source)
		pass
class RLK_818:# <3>[1776]
	""" Ricochet Shot (spell:1)
	Deal $1 damage to three random enemies. """
	play = RLK_818_Action()
	pass

if Lich_Eversong_Portal:# 
	Lich_Hunter+=['RLK_819']
	Lich_Hunter+=['RLK_819t']
class RLK_819_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		amount = 1+controller.spellpower
		for count in range(amount):
			Summon(controller, 'RLK_819t').trigger(source)
		pass
class RLK_819:# <3>[1776]
	""" Eversong Portal (spell:4)
	Summon $1 4/4 |4(Lynx, Lynxes) with <b>Rush</b> <i>(improved by <b>Spell Damage</b>)</i>. """
	play = RLK_819_Action()
	pass
class RLK_819t:# <3>[1776]
	""" Eversong Lynx (minion:4/4/4)
	<b>Rush</b> """
	pass

if Lich_Halduron_Brightwing:# 
	Lich_Hunter+=['RLK_820']
class RLK_820_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		for card in controller.deck:
			if card.type==CardType.SPELL and getattr(card, 'spell_school',None)==SpellSchool.ARCANE:
				controller.spellpower_adjustment += 1
			pass
		pass
class RLK_820:# <3>[1776]
	""" Halduron Brightwing (minion:3/3/4)
	<b>Battlecry:</b> Give all Arcane spells in your deck <b>Spell Damage +1</b>. """
	play = RLK_820_Action()
	pass

if Lich_Scourge_Tamer:### OK ###
	# Resurrect ICC_828t. using ICC828t2~ICC_828t7, TSC_069, BAR_030, TID_710
	Lich_Hunter+=['RLK_821','ICC_828t','ICC_828t2','ICC_828t3','ICC_828t4','ICC_828t5','ICC_828t6','ICC_828t7']
	Lich_Hunter+=['TSC_069','BAR_030','TID_710','TID_710e']
	## TID_710e, 
class RLK_821_Choice2(Choice):# 
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		source=self.source
		newcard=self.player.card("ICC_828t")
		newcard.cost=source.sidequest_list1[0]+card.cost
		newcard.atk=source.sidequest_list1[1]+card.atk
		newcard.max_health=source.sidequest_list1[2]+card.max_health
		if card.id=='ICC_828t2':#Stubborn Gastropod
			newcard.taunt=True
			newcard.poisonous=True
		elif card.id=='ICC_828t3':#Giant Wasp
			newcard.stealthed=True
			newcard.poisonous=True
		elif card.id=='ICC_828t4':#Stoneskin Basilisk
			newcard.divine_shield=True
			newcard.poisonous=True
		elif card.id=='ICC_828t5':#Hunting Mastiff
			#newcard.echo=True
			newcard.rush=True
		elif card.id=='ICC_828t6':#Vilebrood Skitterer
			newcard.poisonous=True
			newcard.rush=True
		elif card.id=='ICC_828t7':#Vicious Scalehide
			newcard.lifesteal=True
			newcard.rush=True
		card0=source.sidequest_list0[0]
		newcard.sidequest_list0=[card0]
		if card0=='TSC_069':#
			newcard.requirements = REQUIRE_FRIEND_MINION_TARGET
		else:
			newcard.requirements = {}
		newcard.zone=Zone.HAND
		pass
class RLK_821_Choice1(Choice):# 
	def choose(self, card):
		source=self.source
		source.sidequest_list0=[card.id]
		source.sidequest_list1=[card.cost, card.atk, card.max_health]
		cards=['ICC_828t2','ICC_828t3','ICC_828t4','ICC_828t5','ICC_828t6','ICC_828t7']
		newchoice=RLK_821_Choice2(self.player, RandomID(*cards)*3)
		newchoice.trigger(self.source)
		self.next_choice=newchoice
		super().choose(card)
		pass
class RLK_821_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		source.sidequest_list0=[]
		cards=['TSC_069','BAR_030','TID_710','TID_710e']
		RLK_821_Choice1(controller, RandomID(*cards)*3).trigger(source)
		pass
class RLK_821:# <3>[1776]
	""" Scourge Tamer (minion:2/2/2)
	<b>Battlecry:</b> Craft a custom Zombeast. """
	play = RLK_821_Action()
	pass
class ICC_828t_Action(TargetedAction):
	def do(self, source, target):
		controller=source.controller
		if source.sidequest_list0[0]=='TSC_069':#
			if target and target.type==CardType.MINION:
				Discover(controller, RandomMinion(race=target.race)).trigger(source)
		elif source.sidequest_list0[0]=='BAR_030':#
			card1=get00(RandomCollectible(race=Race.BEAST).evaluate(source))
			card2=get00(RandomCollectible(secret=True).evaluate(source))
			card3=get00(RandomCollectible(type=CardType.WEAPON).evaluate(source))
			play = Discover(controller, RandomID(card1.id, card2.id, card3.id)).trigger(source)
		elif source.sidequest_list0[0]=='TID_710':#
			controller=source.controller
			for card in controller.deck:
				if card.has_battlecry:
					Buff(card, 'TID_710e').trigger(source)
		pass
	pass
class ICC_828t:
	play = ICC_828t_Action(TARGET)
#TID_710e=buff(1,1)

if Lich_Shockspitter:# 
	Lich_Hunter+=['RLK_825']
class RLK_825_Action(TargetedAction):# 
	def do(self, source, target):# 
		controller=source.controller
		Hit(target, source.script_data_num_1).trigger(source)
		pass
class RLK_825_Action2(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		source.script_data_num_1+=1
class RLK_825:# <3>[1776]
	""" Shockspitter (minion:2/2/2)
	<b>Battlecry:</b> Deal @ damage. <i>(Improved by your hero attacks this game!)</i> """
	#<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="1"/>
	requirements = REQUIRE_FRIEND_MINION_TARGET
	play = RLK_825_Action(TARGET)
	class Hand:
		events = Attack(FRIENDLY_HERO).after(RLK_825_Action2())
	pass

if Lich_Silvermoon_Farstrider:# 
	Lich_Hunter+=['RLK_826','RLK_826e']
class RLK_826_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		for card in controller.hand:
			if card.type==CardType.SPELL and card.spell_school==SpellSchool.ARCANE:
				controller.spellpower_adjustment+=1
		pass
class RLK_826:# <3>[1776]
	""" Silvermoon Farstrider (minion:2/2/3)
	<b>Battlecry:</b> Give all Arcane spells in your hand <b>Spell Damage +1</b>. """
	play = RLK_826_Action()
	pass
class RLK_826e:# <12>[1776]
	""" Silvermoon Farstrider Spellpower
	<b>Spell Damage +1</b>. """
	#	
	pass

if Lich_Keeneye_Spotter:# 
	Lich_Hunter+=['RLK_827']
	Lich_Hunter+=['RLK_827e']
class RLK_827:# <3>[1776]
	""" Keeneye Spotter (minion:3/3/4)
	Whenever your hero attacks a minion, set its Health to 1. """
	events = Attack(FRIENDLY_HERO, MINION).on(Buff(Attack.DEFENDER, 'RLK_827e'))
	pass
class RLK_827e:# <3>[1776]
	""" Hunter's Mark (0)
	This minion has 1 Health. """
	max_health=SET(1)
	pass

if Lich_Hope_of_QuelThalas:# 
	Lich_Hunter+=['RLK_828']
	Lich_Hunter+=['RLK_828e']
class RLK_828_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_828:# <3>[1776]
	""" Hope of Quel'Thalas (6)
	After your hero attacks, give your minions +1/+1 <i>(wherever they are).</i> """
	events = Attack(FRIENDLY_HERO).after(Buff(FRIENDLY_MINIONS, 'RLK_828e'))
	pass
RLK_828e=buff(1,1)

