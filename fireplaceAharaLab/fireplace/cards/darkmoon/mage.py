from ..utils import *

class DMF_100:# <4>[1466] ###OK
    """ Confection Cyclone
    [Battlecry:] Add two 1/2 Sugar Elementals to your_hand. """
    play = Give(CONTROLLER, 'DMF_100t') * 2
    pass

class DMF_100t:# <4>[1466]
    """ Sugar Elemental
     """
    #
    pass

class DMF_101:# <4>[1466] ##OK
    """ Firework Elemental
    [Battlecry:] Deal 3 damageto a minion. [Corrupt:]Deal 12 instead. """
    requirements = { PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
    play = Hit(TARGET, 3)
    pass

class DMF_101t:# <4>[1466] ###OK
    """ Firework Elemental
    [Corrupted][Battlecry:] Deal 12 damage to a minion. """
    play = Hit(TARGET, 12)
    pass

class DMF_102:# <4>[1466] ##OK remark that 'play + after'
    """ Game Master
    The first [Secret] you play each turn costs (1). """
    play = Buff(FRIENDLY_HAND + SECRET,'DMF_102e')
    events = OWN_TURN_BEGIN.on(Buff(FRIENDLY_HAND + SECRET,'DMF_102e'))
    pass
class DMF_102e:#<12>[1466]
    cost = SET(1)
    events = Play(CONTROLLER,SECRET).after(Destroy(SELF))


class DMF_103:# <4>[1466] ###OK
    """ Mask of C'Thun
    Deal $10 damage randomly split among all enemies. """
    play = Hit(RANDOM_ENEMY_CHARACTER,1) * 10
    pass

class CountElementalLastTurnAndAction(TargetedAction):
    TARGET = ActionArg()#self
    ACTION = ActionArg()
    def do(self, source, target, actions) :
        _thisPlayer = target.controller
        _playLogList = _thisPlayer.play_log_of_last_turn
        _count = 0
        for _card in _playLogList:
            if _card.race == Race.ELEMENTAL:
                _count += 1
        if not isinstance(actions,list):
            actions = [actions]
        for _repeat in range(_count):
            for _action in actions:
                _action.trigger(source)

class DMF_104:# <4>[1466] ##OK
    """ Grand Finale
    Summon an 8/8 Elemental. Repeat for each Elemental you played last turn. """
    play = Summon(CONTROLLER,'DMF_104t'), CountElementalLastTurnAndAction(SELF, [Summon(CONTROLLER,'DMF_104t')])
    pass

class DMF_104t:# <4>[1466]
    """ Exploding Sparkler
     """
    #
    pass

class DMF_105:# <4>[1466]###OK
    """ Ring Toss
    [Discover] a [Secret] and cast it. [Corrupt:] [Discover] 2 instead. """
    play = GenericChoicePlayBackToDeck(CONTROLLER, RANDOM(SECRET)*3)
    pass

class DMF_105t:# <4>[1466]###OK:  2回チョイスできるようにした
    """ Ring Toss
    [Corrupted][Discover] 2 [Secrets] and cast them. """
    play = GenericChoicePlayBackToDeck(CONTROLLER, RANDOM(SECRET)*3), GenericChoicePlayBackToDeck(CONTROLLER, RANDOM(SECRET)*3)
    pass

class DMF_106:# <4>[1466]###OK
    """ Occult Conjurer
    [Battlecry:] If you control a [Secret], summon a copy of_this. """
    play = Find(FRIENDLY_SECRETS) & Summon(CONTROLLER,ExactCopy(SELF))
    pass

class NoDamageThisTurn(TargetedAction):
    TARGET = ActionArg()
    TARGETEDACTION = ActionArg()
    def do(self, source, target, targetedaction):
        entities = source.controller.get_damage_log_of_this_turn
        if len(entities) == 0:
            for myAction in targetedaction:
                myAction.trigger(source)

class DMF_107:# <4>[1466] ##OK
    """ Rigged Faire Game
    [Secret:] If you didn't take any damage during your opponent's turn, draw 3 cards. """
    secret = EndTurn(OPPONENT).on( NoDamageThisTurn(CONTROLLER, [Reveal(SELF),Draw(CONTROLLER),Draw(CONTROLLER),Draw(CONTROLLER)]))
    pass


class DMF_108:# <4>[1466] ##OK
    """ Deck of Lunacy
    Transform spells in your deck into ones that cost (3) more. <i>(They keep their original Cost.)</i> """
    play = DMF_108_Morph(FRIENDLY_DECK + SPELL,RandomSpell(cost=[3,4,5,6,7,8,9,10]))
    pass
#class DMF_108e:# <12>[1466]
#    cost = SET(COST(OWNER))

class CountTriggeredSecret(TargetedAction):
    TARGET = ActionArg()
    def do(self, source, target):# controller
        playLog = target.play_log
        count = 0
        for log in playLog:
            if hasattr(log,'secret') and log.secret:
                count += 1
        return count

class DMF_109:# <4>[1466] ###OK
    """ Sayge, Seer of Darkmoon
    [Battlecry:] Draw @ |4(card, cards).<i>(Upgraded for each friendly [Secret] that has triggered this game!)</i> """
    play = Draw(CONTROLLER), Draw(CONTROLLER) * CountTriggeredSecret(CONTROLLER)
    pass

class YOP_019:# <4>[1466] ###
    """ Conjure Mana Biscuit
    Add a Biscuit to your hand that refreshes 2 Mana Crystals. """
    play = Summon(CONTROLLER,'YOP_019t')
    pass

class YOP_019t:# <4>[1466] ###
    """ Mana Biscuit
    Refresh 2 Mana Crystals. """
    play = RefreshMana(CONTROLLER)
    #
    pass

class YOP_020:# <4>[1466] ###
    """ Glacier Racer
    [Spellburst]: Deal 3 damage to all [Frozen] enemies. """
    play = OWN_SPELL_PLAY.on(Hit(ENEMY_CHARACTERS,3))
    pass



