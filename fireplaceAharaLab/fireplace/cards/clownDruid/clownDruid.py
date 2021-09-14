from ..utils import *

class CORE_EX1_169:
    """Innervate
    Gain 1 Mana Crystal this turn only."""
    play = ManaThisTurn(CONTROLLER, 1)
    pass

class SCH_427:
    """Lightning Bloom
    Gain 2 Mana Crystals this turn only. Overload: (2)"""
    play = ManaThisTurn(CONTROLLER, 2)
    pass

# class SCH_311:
#     """Animated Broomstick
#     Rush Battlecry: Give your other minions Rush."""
    
#     pass

class SCH_333_Choice(GenericChoice):
	def choose(self, card):
		super().choose(card)
		controller = self.player
		for handcard in controller.hand:
		    if handcard.type==CardType.SPELL:
		        Buff(handcard,'SCH_333e').trigger(controller)
		pass

class SCH_333:
    """Nature Studies
    Discover a spell. Your next one costs (1) less."""
    play = SCH_333_Choice(CONTROLLER, RandomSpell*3)
    pass

class SCH_333e:
    """Nature Studies
        Your next spell costs (1) less."""
    cost = lambda self, i: max(i-1,0)
    events = OWN_SPELL_PLAY.on(Destroy(SELF))
    pass

class DMF_075: #????
    """Guess the Weight
    Draw a card. Guess if your next card costs more or less to draw it."""
    # play = Draw(CONTROLLER,1).then(choose.())
    pass


class CORE_CS2_013: # copied from classic
    """Wild Growth
    Gain an empty Mana Crystal."""
    play = (
		AT_MAX_MANA(CONTROLLER) &
		Give(CONTROLLER, "CS2_013t") |
		GainEmptyMana(CONTROLLER, 1)
	)
    pass

class CS2_013t:
	play = Draw(CONTROLLER)

class BT_130:
    """Overgrowth
    Gain two empty Mana Crystals."""
    play = (
		AT_MAX_MANA(CONTROLLER) &
		Give(CONTROLLER, "CS2_013t") |
		GainEmptyMana(CONTROLLER, 2)
	)
    pass

class BAR_535:
    """Thickhide Kodo
    Taunt Deathrattle: Gain 5 Armor."""
    deathrattle = GainArmor(FRIENDLY_HERO,5)
    
    pass

# class SCH_605:
#     """Lake Thresher
#     Also damages the minions next to whomever this attacks."""
    
#     pass

class SCH_616:
    """Twilight Runner
    Stealth Whenever this attacks, draw 2 cards."""
    events = Attack(SELF).on(Draw(CONTROLLER)*2)
    pass

# class DMF_078:
#     """Strongman
#     Taunt Corrupt: This costs (0)."""
    
#     pass

class SCH_610:
    """Guardian Animals
    Summon two Beasts that cost (5) or less from your deck. Give them Rush."""
    play = Summon(CONTROLLER, RANDOM(FRIENDLY_DECK+BEAST+(COST<5))).then(SetTag(Summon.CARD, (GameTag.RUSH,))) * 2
    pass

class BAR_042_Action(TargetedAction):
	def do(self, source, target):
		_highestCostCards=[]
		for _card in target.deck:
			if _card.type==CardType.SPELL:
				if len(_highestCostCards)==0:
					_highestCostCards = [_card]
				elif _highestCostCards[0].cost < _card.cost:
					_highestCostCards = [_card]
				elif _highestCostCards[0].cost == _card.cost:
					_highestCostCards.append(_card)
		if len(_highestCostCards)>0:
			_card = random.choice(_highestCostCards)
			_cost = _card.cost
			log.info("Highest cost spell is %r (cost %d)"%(_card, _cost))
			Give(target,_card).then(Summon(CONTROLLER,RANDOM(MINION+(COST==Attr(Give.CARD,GameTag.COST))))).trigger(source)
		else:
			log.info("no spell is in the deck"%())

class BAR_042:
    """Primordial Protector
    Battlecry: Draw your highest Cost spell. Summon a random minion with the same Cost."""
    play = BAR_042_Action(CONTROLLER)
    
    pass

# class DMF_163:
#     """Carnival Clown
#     Taunt Battlecry: Summon 2 copies of this. Corrupt: Fill your board with copies."""
    
#     pass

class SCH_609:
    """Survival of the Fittest
    Give +4/+4 to all minions in your hand, deck, and battlefield."""
    def play(self):
        for _card in self.controller.cards:
            if _card.type == CardType.MINION:
                Buff(_card,'SCH_609e').tigger(self.controller)
        pass

    pass
SCH_609e=buff(atk=4,health=4)

# class DMF_188:
#     """Y'Shaarj, the Defiler
#     Battlecry: Add a copy of each Corrupted card you've played this game to your hand. They cost (0) this turn."""
    
#     pass

