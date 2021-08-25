from ..utils import *


class DMF_083:#OK
    """ Dancing Cobra
    [Corrupt:] Gain [Poisonous]. """
    pass

class DMF_083t:
    """ Dancing Cobra
    [Corrupted][Poisonous] """
    #
    pass

class DMF_084_Action(TargetedAction):
    TARGET=ActionArg()
    def do(self, source, target):
        _player = target
        _minionList=_player.__myDeathLog__
        _count =0
        for _card in _minionList:
            if _card.deathrattles != None and _count<3:
                Summon(_player, Copy(ID(_card))).trigger(_player)
                _count += 1

class DMF_084:
    """ Jewel of N'Zoth
    Summon three friendly [Deathrattle] minions that died this game. """
    play = DMF_084_Action(CONTROLLER)
    pass

class DMF_085:
    """ Darkmoon Tonk
    [Deathrattle:] Fire four missiles at random enemies that deal 2 damage each. """
    deathrattle = Hit(RANDOM(ENEMY_CHARACTERS),2) * 4
    pass

class DMF_086:
    """ Petting Zoo
    Summon a 3/3 Strider. Repeat for each [Secret] you control. """
    play = Summon(CONTROLLER,'DMF_086e'), Summon(CONTROLLER,'DMF_086e') * Count(FRIENDLY_SECRETS)
    pass

class DMF_086e:
    """ Darkmoon Strider
     """
    #
    pass

class DMF_087_Action(TargetedAction):
    CONTROLLER=ActionArg()
    DEFENDER=ActionArg()
    def do(self,source,controller,defender):
        excess = source.atk - defender.health
        if excess > 0:
            Hit(controller.opponent.hero, excess).trigger(controller)

class DMF_087:
    """ Trampling Rhino
    [Rush]. After this attacks and kills a minion, excess damage hits the enemy hero. """
    events = Attack(SELF,ENEMY_MINIONS).on(DMF_087_Action(CONTROLLER,Attack.DEFENDER))
    pass

class DMF_088:
    """ Rinling's Rifle
    After your hero attacks, [Discover] a [Secret] and cast it. """
    events = Attack(FRIENDLY_HERO).on(GenericChoicePlay(CONTROLLER, RANDOM(SECRET)*3))
    pass

class DMF_089:
    """ Maxima Blastenheimer
    [Battlecry:] Summon a minion from your deck. It attacks the enemy hero, then dies. """
    play = Summon(CONTROLLER,RANDOM(FRIENDLY_DECK + MINION)).then(Attack(Summon.CARD,ENEMY_HERO), Destroy(Summon.CARD))
    pass

class DMF_090:
    """ Don't Feed the Animals
    Give all Beasts in your hand +1/+1.[Corrupt:] Give them +2/+2 instead. """
    play = Buff(FRIENDLY_HAND + BEAST,'DMF_090e2')
    pass

class DMF_090e:
    """ Well Fed
    +2/+2. """
    #
    pass

class DMF_090e2:
    """ Well Fed
    +1/+1. """
    #
    pass

class DMF_090t:
    """ Don't Feed the Animals
    [Corrupted]Give all Beasts in your hand +2/+2. """
    play = Buff(FRIENDLY_HAND + BEAST,'DMF_090e')
    pass

class DMF_122:
    """ Mystery Winner
    [Battlecry:] [Discover] a [Secret.] """
    play = GenericChoice(CONTROLLER, RANDOM(SECRET)*3)
    pass

class DMF_123:############# control two minions
    """ Open the Cages
    [Secret:] When your turn starts, if you control two minions, summon an Animal Companion. """
    secret = OWN_TURN_BEGIN.on(Reveal(SELF), Summon(CONTROLLER,'NEW1_031'))
    pass

class DMF_734e:
    """ Greybud
    [Deathrattle:] Summon Greybough. """
    deathrattle = Summon(CONTROLLER,'DMF_734')
    pass

class YOP_027:
    """ Bola Shot
    Deal $1 damage to a minion and $2 damage to its neighbors. """
    requirements = { PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0}
    play = Hit(TARGET, 1), Hit(TARGET_ADJACENT,2)
    pass

class YOP_028:
    """ Saddlemaster
    After you play a Beast, add_a random Beast to_your hand. """
    events = Play(CONTROLLER, BEAST).on(Give(CONTROLLER,RANDOM(BEAST)))
    pass
