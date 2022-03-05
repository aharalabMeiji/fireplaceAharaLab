from ..utils import *

#CardSet.DARKMOON_FAIRE_CardClass.DRUID=[
#'DMF_057','DMF_057e','DMF_057o','DMF_058','DMF_058e','DMF_058o',
#'DMF_059','DMF_060','DMF_061','DMF_061a','DMF_061b','DMF_061t','DMF_061t2',
#'DMF_075','DMF_075a','DMF_075a2','DMF_730','DMF_730e','DMF_730t',
#'DMF_732','DMF_733','DMF_734','DMF_734e',
#'YOP_025','YOP_025t','YOP_026','YOP_026e',]

class DMF_057:#OK <2>[1466]
	""" Lunar Eclipse
	Deal $3 damage to a minion. Your next spell this turn costs (2) less. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0}
	play = Hit(TARGET,3),  Buff(FRIENDLY_HAND + SPELL,'DMF_057e')
	pass
class DMF_057e:# <2>[1466]
	""" Lunar Empowerment
	The next spell you cast costs (2) less. """
	cost = lambda self, i: max(i-2,0)
	events =[
	   OWN_SPELL_PLAY.on(Destroy(SELF)),
	   OWN_TURN_END.on(Destroy(SELF)),
	   ]
	pass
class DMF_057o:# <2>[1466]#ONE_TURN_EFFECT
	""" Lunar Empowerment
	The next spell you cast this turn costs (2) less. """
	#
	pass

class PlayOnceMoreTime(TargetedAction):
	TARGET = ActionArg()
	CARD = ActionArg()
	OTHER = ActionArg()
	def do(self, source, target, card, other):
		log.info("Play Once more!")
		Battlecry(card,other).trigger(target)

class DMF_058:#OK <2>[1466]
	""" Solar Eclipse
	Your next spell this turn casts twice. """
	play = Buff(FRIENDLY_HERO,'DMF_058e')
	pass
class DMF_058e:# <2>[1466] #ONE_TURN_EFFECT
	""" Solar Empowerment
	Your next spell this turn casts twice. """
	events =[
	   OWN_SPELL_PLAY.on(
		   PlayOnceMoreTime(OWNER,Play.CARD,Play.TARGET),
		   Destroy(SELF)
		   ),
	   ]
	pass
class DMF_058o:# <2>[1466] #ONE_TURN_EFFECT
	""" Solar Empowerment
	Your next spell this turn casts twice. """
	#
	pass

class DMF_059:# <2>[1466]
	""" Fizzy Elemental
	[Rush][Taunt] """
	#####
	pass


class DMF_060_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		target._sidequest_counter_ = 0
		playList = target.controller.play_log
		for card in playList:
			if card.type == CardType.SPELL:
				target._sidequest_counter_ += 1
class DMF_060:##OK <2>[1466] #
	""" Umbral Owl
	[Rush]Costs (1) less for each spell you've cast this game. """
	class Deck:
		events = OWN_SPELL_PLAY.on(DMF_060_Action(SELF))
		pass
	class Hand:
		events = OWN_SPELL_PLAY.on(DMF_060_Action(SELF))
		pass
	cost_mod = -Attr(SELF,'_sidequest_counter_')
	pass

class DMF_061:#OK <2>[1466] #
#	""" Faire Arborist
#	[Choose One - ]Draw a card;or Summon a 2/2 Treant.[Corrupt:] Do both. """
	choose = ('DMF_061a','DMF_061b',)
	play = ChooseBoth(SELF) & (
		Draw(CONTROLLER),
		Summon(CONTROLLER,'DMF_061t2')
		)
	pass
class DMF_061a:# <2>[1466]
	""" Prune the Fruit
	Draw a card. """
	play = Draw(CONTROLLER)
	pass
class DMF_061b:# <2>[1466]
	""" Dig It Up
	Summon a 2/2 Treant. """
	play = Summon(CONTROLLER,'DMF_061t2')
	pass
class DMF_061t:# <2>[1466]
	""" Faire Arborist
	[Corrupted][Battlecry:] Summon a 2/2 Treant. Draw a card. """
	play = Draw(CONTROLLER), Summon(CONTROLLER,'DMF_061t2')
	pass
class DMF_061t2:# <2>[1466]
	""" Treant
	 """
	#
	pass

class DMF_075_Choice(GenericChoice):
    def choose(self, card):
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

class DMF_075: ###OK  <2>[1466]
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

class DMF_730:#OK <2>[1466]
	""" Moontouched Amulet
	Give your hero +4 Attack this turn. [Corrupt:] And gain 6 Armor. """
	play = Buff(FRIENDLY_HERO, 'DMF_730e')
	pass
DMF_730e=buff(atk=4)# <2>[1466] #_ONE_TURN_EFFECT
""" Moontouched Amulet
+4 Attack this turn. """

class DMF_730t:# <2>[1466]
	""" Moontouched Amulet
	[Corrupted]Give your hero +4 Attack this turn. Gain 6 Armor. """
	play = Buff(FRIENDLY_HERO, 'DMF_730e'), GainArmor(FRIENDLY_HERO,6)
	pass

class DMF_732:#OK <2>[1466]
	""" Cenarion Ward
	Gain 8 Armor.Summon a random8-Cost minion. """
	play = GainArmor(FRIENDLY_HERO, 8), Summon(CONTROLLER, RandomMinion(cost = 8))
	pass

class DMF_733:#OK <2>[1466]
	""" Kiri, Chosen of Elune
	[Battlecry:] Add a Solar Eclipse(DMF_058) and Lunar Eclipse(DMF_057) to your hand. """
	play = Give(CONTROLLER, 'DMF_058'), Give(CONTROLLER, 'DMF_057')
	pass

class DMF_734:# <2>[1466] #こっちは動く。
	""" Greybough
	[Taunt][Deathrattle:] Give a random friendly minion "[Deathrattle:]Summon Greybough." """
	deathrattle = Buff(RANDOM(FRIENDLY_MINIONS - SELF), 'DMF_734e')
	pass
class DMF_734e:#OK <3>[1466]#
	deathrattle = Summon(CONTROLLER, "DMF_734")
	tags = {GameTag.DEATHRATTLE: True}
	pass
class YOP_025:#OK <2>[1466]
	""" Dreaming Drake
	[Taunt][Corrupt:] Gain +2/+2. """
	#
	pass
class YOP_025t:# <2>[1466]
	""" Dreaming Drake
	[Corrupted][Taunt] """
	#
	pass

class YOP_026:# <2>[1466]
	""" Arbor Up
	Summon two 2/2 Treants. Give your minions +2/+1. """
	play = Summon(CONTROLLER, 'DMF_061t2') * 2, Buff(FRIENDLY_MINIONS, 'YOP_026e')
	pass

YOP_026e=buff(2,1)# <2>[1466]
""" Forest Guards
+2/+1. """

