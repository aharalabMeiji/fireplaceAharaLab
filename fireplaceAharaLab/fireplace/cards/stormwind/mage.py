from ..utils import *



class SW_001:#<4>[1578]###OK
	""" Celestial Ink Set
	After you spend 5 Mana on spells, reduce the cost of a spell in your hand by (5).Lose 1 Durability. """
	events = OWN_SPELL_PLAY.on(SidequestManaCounter(SELF,Play.CARD,5,[Buff(FRIENDLY_HAND + SPELL,'SW_001e'), Hit(SELF,1)]))
	pass
SW_001e = buff(cost=-5)#<12> [1578]
SW_001e2 = buff(cost=-5)#<12> [1578]

#class SW_059e:#<4>[1578]
#	""" Engineered
#	Cost reduced. """
#	#
#	pass

class SW_107:#<4>[1578]###OK
	""" Fire Sale
	[Tradeable]Deal $3 damage to all minions. """
	play = Hit(ALL_MINIONS,3)
	pass

class SW_108:#<4>[1578]###OK
	""" First Flame
	Deal $2 damage to a minion. Add a Second Flame to your hand. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0}
	play = Hit(TARGET,2), Give(CONTROLLER, 'SW_108t')
	pass

class SW_108t:#<4>[1578]###OK
	""" Second Flame
	Deal $2 damage to a minion. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0}
	play = Hit(TARGET, 2)
	pass

class PlayHighestCostSpell(TargetedAction):
	TARGET = ActionArg()# controller
	def do(self, source, target):
		maxCost=-1
		maxCostSpells=[]
		for card in target.hand:
			if card.id!='SW_109' and card.type == CardType.SPELL and not card.requires_target():
				if card.cost>maxCost:
					maxCost = card.cost
					maxCostSpells=[card]
				elif card.cost==maxCost:
					maxCostSpells.append(card)
		if len(maxCostSpells)>0:
			Summon(target,random.choice(maxCostSpells)).trigger(source)#Summonすることにより、マナを消費しない。##

class SW_109:#<4>[1578]##OK
	""" Clumsy Courier
	[Battlecry:] Cast the highest Cost spell from your hand. """
	play = PlayHighestCostSpell(CONTROLLER)
	pass



class SW_110_Action(TargetedAction):
	"""
	Shuffle and buff card targets into player target's deck.
	"""
	TARGET = ActionArg()#player
	CARD = CardArg()
	def do(self, source, target, cards):
		log.info("%r shuffles into %s's deck", cards, target)
		if not isinstance(cards, list):
			cards = [cards]
		for card in cards:
			card.script_data_num_1 += 1#
			if card.controller != target:
				card.zone = Zone.SETASIDE
				card.controller = target
			if len(target.deck) >= target.max_deck_size:
				log.info("Shuffle(%r) fails because %r's deck is full", card, target)
				continue
			card.zone = Zone.DECK
			target.shuffle_deck()
class SW_110:#<4>[1578] ###OK
	""" Ignite
	Deal $@ damage. Shuffle an Ignite into your deck that deals one more damage. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0}
	play = HitScriptDataNum1(SELF, TARGET), SW_110_Action(CONTROLLER,'SW_110')
	
	pass

class SW_111:#<4>[1578] ###OK
	""" Sanctum Chandler
	After you cast a Fire spell, draw a spell. """
	events = Play(CONTROLLER, SPELL + FIRE).on(Give(CONTROLLER, RANDOM(FRIENDLY_DECK + SPELL)))
	pass

class SW_112:#<4>[1578] ####OK
	""" Prestor's Pyromancer
	[Battlecry:] Your next Fire spell has [SpellDamage +2]. """
	play = SetAttr(SELF,'spellpower_fire',2)
	events = Play(CONTROLLER, SPELL + FIRE).after(SetAttr(SELF,'spellpower_fire',0))
	pass

class SW_112e:#<4>[1578]
	""" Burning Hot!
	Your next Fire spell has [Spell Damage +2]. """
	#update = Refresh(FRIENDLY_HAND, {GameTag.SPELLPOWER: 2})
	
	pass

class SW_112e2:#<4>[1578]
	""" Burning Hot!
	Your next Fire spell has [Spell Damage +2]. """
	#
	pass

class SW_113_Action(TargetedAction):
	TARGET = ActionArg()#controller
	TARGETEDACTION = ActionArg()
	def do(self, source, target, targetedaction):
		playList = target._play_log
		flag1=flag2=flag3=0
		for _log in playList:
			card = _log.card
			turn = _log.turn
			if card.type == CardType.SPELL and card.spell_school == SpellSchool.FIRE:
				if turn == source.game.turn - 2:
					flag1 = 1
				elif turn == source.game.turn - 4:
					flag2 = 1
				elif turn == source.game.turn - 6:
					flag3 = 1
		if flag1==1 and flag2==1 and flag3==1:
			for action in targetedaction:
				action.trigger(source)

class SW_113_Hand_Event(TargetedAction):
	TARGET = ActionArg()#controller
	def do(self, source, target):
		playList = target._play_log
		flag1=flag2=flag3=0
		for _log in playList:
			card = _log.card
			turn = _log.turn
			if card.type == CardType.SPELL and card.spell_school == SpellSchool.FIRE:
				if turn == source.game.turn:
					flag1 = 1
				elif turn == source.game.turn - 2:
					flag2 = 1
				elif turn == source.game.turn - 4:
					flag3 = 1
		if flag1==1 and flag2==0:
			source.script_data_num_1 = 1
		if flag1==1 and flag2==1 and flag3==0:
			source.script_data_num_1 = 2
		if flag1==1 and flag2==1 and flag3==1:
			source.script_data_num_1 = 3

class SW_113:#<4>[1578] ### not perfect but yes (fireball -> deal 6 damage)
	""" Grand Magus Antonidas
	[Battlecry:] If you've cast a Fire spell on each of your last three turns, cast 3 Fireballs at___random enemies.@ <i>(@/3)</i> """
	play = SW_113_Action(CONTROLLER, \
						 [Hit(RANDOM_ENEMY_CHARACTER,6),# insted of a fireball
						  Hit(RANDOM_ENEMY_CHARACTER,6),
						  Hit(RANDOM_ENEMY_CHARACTER,6)]
						 )
	class Hand:
		events = OWN_TURN_END.on(SW_113_Hand_Event(CONTROLLER))
	pass

class SidequestFireFrostArcane(TargetedAction):############
	TARGET = ActionArg()#controller
	CARD = CardArg()
	TARGETEDACTION = ActionArg()
	def do(self,source,target,card,targetedaction):
		if card.spell_school == SpellSchool.FIRE:
			source._sidequest_list1_.append(card)
		elif card.spell_school == SpellSchool.FROST:
			source._sidequest_list2_.append(card)
		elif card.spell_school == SpellSchool.ARCANE:
			source._sidequest_list3_.append(card)
		source._sidequest_counter_ = 0
		if len(source._sidequest_list1_)>0:
			source._sidequest_counter_ += 1
		if len(source._sidequest_list2_)>0:
			source._sidequest_counter_ += 1
		if len(source._sidequest_list3_)>0:
			source._sidequest_counter_ += 1
		if source._sidequest_counter_==3:
			for action in targetedaction:
				action.trigger(source)
		pass
class SW_450:#<4>[1578]###OK
	""" Sorcerer's Gambit
	[Questline:] Cast a Fire, Frost, and Arcane spell. [Reward: ]Draw a spell. """
	events = OWN_SPELL_PLAY.on(SidequestFireFrostArcane(CONTROLLER,Play.CARD,[Give(CONTROLLER,RANDOM(FRIENDLY_DECK + SPELL)), Summon(CONTROLLER,'SW_450t'),Destroy(SELF)]))
	pass

class SW_450t:#<4>[1578]##OK
	""" Stall for Time
	[Questline:] Cast a Fire, Frost, and Arcane spell. [Reward:] [Discover] one. """
	events = OWN_SPELL_PLAY.on(SidequestFireFrostArcane(CONTROLLER,Play.CARD,[\
		Discover(CONTROLLER,RandomSpell()), \
		Summon(CONTROLLER,'SW_450t2'),Destroy(SELF)]))
	pass

class SW_450t2:#<4>[1578]###OK
	""" Reach the Portal Room
	[Questline:] Cast a Fire,Frost, and Arcane spell.[Reward:] ArcanistDawngrasp. """
	events = OWN_SPELL_PLAY.on(SidequestFireFrostArcane(CONTROLLER,Play.CARD,[Give( CONTROLLER,'SW_450t4'),Destroy(SELF)]))
	pass

class SW_450t4:#<4>[1578]#################
	""" Arcanist Dawngrasp
	[Battlecry:] For the rest of the game, you have [Spell Damage +3]. """
	play = SetAttr(CONTROLLER,'spellpower_option',3)
	pass

class SW_450t4e:#<4>[1578]
	""" Power of Dawngrasp
	[Spell Damage +3] """
	spellpower = +3
	pass

class SW_462:#<4>[1578]###OK
	""" Hot Streak
	Your next Fire spell this turn costs (2) less. """
	play = Buff(FRIENDLY_HAND + SPELL + FIRE, 'SW_462e')
	pass

class SW_462e:#<4>[1578] ####
	""" Hot Streak
	The next Fire spell you play costs (2) less. """
	cost = lambda self, i: max(i-2,0) 
	events = [
		Play(CONTROLLER, SPELL+FIRE).on(Destroy(SELF)),
		OWN_TURN_END.on(Destroy(SELF)),
		]
	pass

