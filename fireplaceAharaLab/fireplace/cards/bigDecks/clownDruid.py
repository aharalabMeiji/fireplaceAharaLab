from ..utils import *

clownDruid = []
#'AV_205'
#'BT_130','BT_130',
#'BAR_042','BAR_042',
#'BAR_535',
#'CORE_CS2_013','CORE_CS2_013',
#'CORE_EX1_169','CORE_EX1_169',
#'DMF_075','DMF_075',
#'DMF_078','DMF_078',
#'DMF_163','DMF_163',
#'SCH_311','SCH_311',
#'SCH_333','SCH_333',
#'SCH_427','SCH_427',
#'SCH_605','SCH_605',
#'SCH_609','SCH_609',
#'SCH_610','SCH_610',
#'SCH_616','SCH_616',




#class AV_205:##
#	""" Wildheart Guff ( 5/*/5) Hero
#	Battlecry: Set your maximum Mana to 20. Gain a Mana Crystal. Draw a card."""
#	def play(self):
#		controller = self.controller
#		GainArmor(self, self.armor)
#		controller.max_resources = 20
#		Draw(controller).trigger(controller)
#		#controller.summon('AV_205p')## Hero power いらないらしい。
#	pass
#class AV_205a:
#	""" Ice Blossom
#	Gain a Mana Crystal."""
#	play = GainMana(CONTROLLER, 1)
#	pass
#class AV_205p:
#	""" Nurture (hero power)
#	[Hero Power][Choose One -] Draw a card;or Gain a Mana Crystal."""
#	choose=('AV_205a', 'AV_205pb')
#	play = ChooseBoth(SELF) & (GainMana(CONTROLLER, 1), Draw(CONTROLLER))
#	pass
#class AV_205pb:
#	""" Valley Root
#	Draw a card."""
#	play = Draw(CONTROLLER)
#	pass



class BT_130: #OK
	"""Overgrowth
	Gain two empty Mana Crystals."""
	play = GainEmptyMana(CONTROLLER, 2)
	pass



#class BAR_042_Action(TargetedAction): 
#	def do(self, source, target):
#		_highestCostCards=[]
#		for _card in target.deck:
#			if _card.type==CardType.SPELL:
#				if len(_highestCostCards)==0:
#					_highestCostCards = [_card]
#				elif _highestCostCards[0].cost < _card.cost:
#					_highestCostCards = [_card]
#				elif _highestCostCards[0].cost == _card.cost:
#					_highestCostCards.append(_card)
#		if len(_highestCostCards)>0:
#			_card = random.choice(_highestCostCards)
#			_cost = _card.cost
#			if Config.LOGINFO:
#				print("Highest cost spell is %r (cost %d)"%(_card, _cost))
#			Give(target,_card).then(Summon(CONTROLLER,RANDOM(MINION+(COST==Attr(Give.CARD,GameTag.COST))))).trigger(source)
#		else:
#			if Config.LOGINFO:
#				print("no spell is in the deck"%())
#class BAR_042:###OK barrens-neutral
#	"""Primordial Protector
#	Battlecry: Draw your highest Cost spell. 
#	Summon a random minion with the same Cost."""
#	play = BAR_042_Action(CONTROLLER)
#	pass




class BAR_535:##OK <-barrens.druid
	"""Thickhide Kodo
	Taunt: Deathrattle: Gain 5 Armor."""
	deathrattle = GainArmor(FRIENDLY_HERO,5)
	pass




#class CORE_CS2_013: # copied from classic #OK
#	"""Wild Growth
#	Gain an empty Mana Crystal."""
#	play = GainEmptyMana(CONTROLLER, 1)
#	pass

#class CS2_013t:
#	play = Draw(CONTROLLER)




#class CORE_EX1_169: #OK core-druid
#	"""Innervate
#	Gain 1 Mana Crystal this turn only."""
#	play = ManaThisTurn(CONTROLLER, 1)
#	pass



class DMF_075_Choice(GenericChoice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		controller = self.player
		choiceCard = controller.hand[-1]
		choiceCardId = choiceCard.id
		choiceCard.zone = Zone.GRAVEYARD
		if len(controller.hand)<controller.max_hand_size:
			moreCard = Draw(controller,1).trigger(controller)
			if moreCard[0] != []:
				moreCard = moreCard[0][0]
				drawnCard = controller.hand[-2]# first drawn card
				if choiceCardId == 'DMF_075a':
					if drawnCard.cost < moreCard.cost:
						pass
					else:
						moreCard.zone = Zone.GRAVEYARD
					return
				elif choiceCardId == 'DMF_075a2':
					if drawnCard.cost > moreCard.cost:
						pass
					else:
						moreCard.zone = Zone.GRAVEYARD
					return
class DMF_075: ###OK  Darkmoon_Druid
	"""Guess the Weight
	Draw a card. Guess if your next card costs more or less to draw it."""
	entourage = ['DMF_075a','DMF_075a2']
	def play(self):
		controller = self.controller
		new_card=Draw(CONTROLLER,1).trigger(controller)
		if len(new_card[0])>0:
			new_card=new_card[0][0]
			self.choiceText=" %s(%d)より :"%(new_card.data.name, new_card.cost)
			DMF_075_Choice(CONTROLLER,RandomEntourage()*2).trigger(self)
	pass
class DMF_075a:
	pass
class DMF_075a2:
	pass



class DMF_078: #-> darkmoon.neutral
	"""Strongman
	Taunt Corrupt: This costs (0)."""
	pass
DMF_078e=buff(cost=0)
class DMF_078t:###OK
	"""Strongman"""
	##[Corrupted] [Taunt]
	pass




class DMF_163: # -> darkmoon.neutral
	"""Carnival Clown
	Taunt: Battlecry: Summon 2 copies of this. Corrupt: Fill your board with copies."""
	pass
class DMF_163t:
	pass




class SCH_311: #scholo-neutral
	"""Animated Broomstick
	Rush Battlecry: Give your other minions Rush."""
	update = Refresh(FRIENDLY_MINIONS - SELF, {GameTag.RUSH: 1})
	pass



class SCH_333:###OK Scholo_Druid
	"""Nature Studies
	Discover a spell. Your next one costs (1) less."""
	play = Discover(CONTROLLER, RandomSpell(card_class=FRIENDLY_CLASS)).then(Buff(FRIENDLY_HAND+SPELL,'SCH_333e'))
	pass
class SCH_333e:
	"""Nature Studies
		Your next spell costs (1) less."""
	cost = lambda self, i: max(i-1,0)
	events = OWN_SPELL_PLAY.on(Destroy(SELF))
	pass




class SCH_427: #OK scholo-neutral
	"""Lightning Bloom
	Gain 2 Mana Crystals this turn only. Overload: (2)"""
	play = ManaThisTurn(CONTROLLER, 2)
	pass




class SCH_605:#-> scholo.neutral 
	"""Lake Thresher
	Also damages the minions next to whomever this attacks."""
	events = Attack(SELF, ENEMY_MINIONS).on(Hit(ADJACENT(Attack.DEFENDER), ATK(SELF)))
	pass





class SCH_609:###OK scholo-druid
	"""Survival of the Fittest
	Give +4/+4 to all minions in your hand, deck, and battlefield."""
	def play(self):
		controller = self.controller
		for _card in (controller.hand + controller.deck + controller.field):
			if _card.type == CardType.MINION:
				Buff(_card,'SCH_609e').trigger(self)
		pass
	pass
SCH_609e=buff(atk=4,health=4)



class SCH_610:###OK -> scholo_hunter
	"""Guardian Animals
	Summon two Beasts that cost (5) or less from your deck. Give them Rush."""
	play = (
		Summon(CONTROLLER, RANDOM(FRIENDLY_DECK+BEAST+(COST<6))).then(SetTag(Summon.CARD, (GameTag.RUSH,))),
		Summon(CONTROLLER, RANDOM(FRIENDLY_DECK+BEAST+(COST<6))).then(SetTag(Summon.CARD, (GameTag.RUSH,)))
		) 
	pass




class SCH_616:###OK  scholo-druid
	"""Twilight Runner
	Stealth: Whenever this attacks, draw 2 cards."""
	events = Attack(SELF).on(Draw(CONTROLLER)*2)
	pass


#############################################


