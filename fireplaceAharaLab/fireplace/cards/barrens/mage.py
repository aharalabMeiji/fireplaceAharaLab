from ..utils import *

class BAR_064e:
    """ Touch of Arcane
    You have [Spell Damage +2] for your next spell this turn. """
    #
    pass

class BAR_064e2:
    """ Touch of Arcane
    You have [Spell Damage +2] for your next spell this turn. """
    #
    pass

class BAR_305:
    """ Flurry (Rank 1)
    [Freeze] a random enemy minion. <i>(Upgrades when you have 5 Mana.)</i> """
    #
    pass

class BAR_305t:
    """ Flurry (Rank 2)
    [Freeze] two random enemy minions. <i>(Upgradeswhen you have 10 Mana.)</i> """
    #
    pass

class BAR_305t2:
    """ Flurry (Rank 3)
    [Freeze] three random enemy minions. """
    #
    pass

class BAR_541:
    """ Runed Orb
    Deal $2 damage. [Discover] a spell. """
    #
    pass

class BAR_542:
    """ Refreshing Spring Water
    Draw 2 cards.Refresh 2 Mana Crystals for each spell drawn. """
    #
    pass

class BAR_544:
    """ Reckless Apprentice
    [Battlecry:] Fire your Hero Power at all enemies. """
    #
    pass

class BAR_545:
    """ Arcane Luminary
    Cards that didn't start in your deck cost (2) less, but not less than (1). """
    #
    pass

class BAR_545e:
    """ Conjured Reduction
    Costs (2) less (but not less than 1). """
    #
    pass

class BAR_546:
    """ Wildfire
    Increase the damage of your Hero Power by 1. """
    play = Buff(CONTROLLER, 'BAR_546e')
    pass

class BAR_546e:
    """ Flame On!
    Hero Power deals 1 more damage. """
    play = ChangeHeroPower(CONTROLLER, "HERO_05bp2")
    pass

class BAR_547:
    """ Mordresh Fire Eye
    [Battlecry:] If you've dealt 10damage with your Hero Power this game, deal 10 damageto all enemies.@ <i>({0} left!)</i>@ <i>(Ready!)</i> """
    #
    pass

class BAR_748:
    """ Varden Dawngrasp
    [Battlecry:] [Freeze] all enemyminions. If any are already[Frozen], deal 4 damageto them instead. """
    #
    pass

class BAR_812:
    """ Oasis Ally
    [Secret:] When afriendly minion isattacked, summon a3/6 Water Elemental. """
    #
    pass

class BAR_888:
    """ Rimetongue
    After you cast a Frost spell, summon a 1/1 Elemental that [[Freeze]s]. """
    #
    pass

class BAR_888t:
    """ Frosted Elemental
    [Freeze] any character damaged by this minion. """
    #
    pass

class WC_041:
    """ Shattering Blast
    Destroy all [Frozen] minions. """
    #
    pass

class WC_805:
    """ Frostweave Dungeoneer
    [Battlecry:] Draw a spell.If it's a Frost spell,summon two 1/1___Elementals that [Freeze]. """
    #
    pass

class WC_806:
    """ Floecaster
    Costs (2) less for each [Frozen] enemy. """
    #
    pass
