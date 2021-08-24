from ..utils import *

class DMF_100:
    """ Confection Cyclone
    [Battlecry:] Add two 1/2 Sugar Elementals to your_hand. """
    play = Give(CONTROLLER, 'DMF_100t') * 2
    pass

class DMF_100t:
    """ Sugar Elemental
     """
    #
    pass

class DMF_101:
    """ Firework Elemental
    [Battlecry:] Deal 3 damageto a minion. [Corrupt:]Deal 12 instead. """
    requirements = { PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
    play = Hit(TARGET, 3)
    pass

class DMF_101t:
    """ Firework Elemental
    [Corrupted][Battlecry:] Deal 12 damage to a minion. """
    play = Hit(TARGET, 12)
    pass

class DMF_102:
    """ Game Master
    The first [Secret] you play each turn costs (1). """
    #
    pass

class DMF_103:
    """ Mask of C'Thun
    Deal $10 damage randomly split among all enemies. """
    #
    pass

class DMF_104:
    """ Grand Finale
    Summon an 8/8 Elemental. Repeat for each Elemental you played last turn. """
    #
    pass

class DMF_104t:
    """ Exploding Sparkler
     """
    #
    pass

class DMF_105:
    """ Ring Toss
    [Discover] a [Secret] and cast it. [Corrupt:] [Discover] 2 instead. """
    #
    pass

class DMF_105t:
    """ Ring Toss
    [Corrupted][Discover] 2 [Secrets] and cast them. """
    #
    pass

class DMF_106:
    """ Occult Conjurer
    [Battlecry:] If you control a [Secret], summon a copy of_this. """
    #
    pass

class DMF_107:
    """ Rigged Faire Game
    [Secret:] If you didn't take any damage during your opponent's turn, draw 3 cards. """
    #
    pass

class DMF_108:
    """ Deck of Lunacy
    Transform spells in your deck into ones that cost (3) more. <i>(They keep their original Cost.)</i> """
    #
    pass

class DMF_109:
    """ Sayge, Seer of Darkmoon
    [Battlecry:] Draw @ |4(card, cards).<i>(Upgraded for eachfriendly [Secret] that hastriggered this game!)</i> """
    #
    pass

class YOP_019:
    """ Conjure Mana Biscuit
    Add a Biscuit to your hand that refreshes 2 Mana Crystals. """
    #
    pass

class YOP_019t:
    """ Mana Biscuit
    Refresh 2 Mana Crystals. """
    #
    pass

class YOP_020:
    """ Glacier Racer
    [Spellburst]: Deal 3 damage to all [Frozen] enemies. """
    #
    pass
