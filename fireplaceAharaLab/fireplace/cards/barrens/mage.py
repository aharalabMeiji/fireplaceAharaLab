from ..utils import *

#class BAR_064e:#<4> [1525] #BAR_064 is neutral
#    """ Touch of Arcane
#    You have [Spell Damage +2] for your next spell this turn. """
#    #
#    pass

#class BAR_064e2:#<4> [1525] #BAR_064 is neutral
#    """ Touch of Arcane
#    You have [Spell Damage +2] for your next spell this turn. """
#    #
#    pass

class BAR_305:#<4> [1525] ###
    """ Flurry (Rank 1)
    [Freeze] a random enemy minion. <i>(Upgrades when you have 5 Mana.)</i> """
    play = Freeze(RANDOM(ENEMY_MINIONS))
    pass

class BAR_305t:#<4> [1525] ###
    """ Flurry (Rank 2)
    [Freeze] two random enemy minions. <i>(Upgradeswhen you have 10 Mana.)</i> """
    play = Freeze(RANDOM(ENEMY_MINIONS)) * 2
    pass

class BAR_305t2:#<4> [1525] ###
    """ Flurry (Rank 3)
    [Freeze] three random enemy minions. """
    play = Freeze(RANDOM(ENEMY_MINIONS)) * 3
    pass

class BAR_541:#<4> [1525] ###
    """ Runed Orb
    Deal $2 damage. [Discover] a spell. """
    requirements = {PlayReq.REQ_TARGET_TO_PLAY:0}
    play = Hit(TARGET, 2),Discover(RandomSpell())
    pass

class GetManaIfSpell(TargetedAction):
    TARGET = ActionArg()
    AMOUNT = IntArg()
    def do(self, source, target, amount):
        if target.type == CardType.SPELL:
            source.controller.used_mana -= amount
            if source.controller.used_mana<0:
                source.controller.used_mana=0

class BAR_542:#<4> [1525] ###
    """ Refreshing Spring Water
    Draw 2 cards.Refresh 2 Mana Crystals for each spell drawn. """
    play = Draw(CONTROLLER).on(GetManaIfSpell(Draw.CARD, 2)), Draw(CONTROLLER).on(GetManaIfSpell(Draw.CARD, 2))
    pass

class BAR_544:#<4> [1525] ###
    """ Reckless Apprentice
    [Battlecry:] Fire your Hero Power at all enemies. """
    play = Activate(CONTROLLER, FRIENDLY_HERO_POWER, ENEMY_CHARACTERS)
    pass

class BAR_545:#<4> [1525] ## didn't start in your deck
    """ Arcane Luminary
    Cards that didn't start in your deck cost (2) less, but not less than (1). """
    events = Buff(FRIENDLY_HAND,'BAR_545e')
    pass

class BAR_545e:#<4> [1525]
    """ Conjured Reduction
    Costs (2) less (but not less than 1). """
    cost = 2
    pass

class BAR_546:#<4> [1525]
    """ Wildfire
    Increase the damage of your Hero Power by 1. """
    play = Buff(CONTROLLER, 'BAR_546e')
    pass

class BAR_546e:#<4> [1525]
    """ Flame On!
    Hero Power deals 1 more damage. """
    play = ChangeHeroPower(CONTROLLER, "HERO_05bp2")
    pass

class BAR_547:#<4> [1525]
    """ Mordresh Fire Eye
    [Battlecry:] If you've dealt 10damage with your Hero Power this game, deal 10 damageto all enemies.@ <i>({0} left!)</i>@ <i>(Ready!)</i> """
    #
    pass

class BAR_748:#<4> [1525]
    """ Varden Dawngrasp
    [Battlecry:] [Freeze] all enemyminions. If any are already[Frozen], deal 4 damageto them instead. """
    #
    pass

class BAR_812:#<4> [1525]
    """ Oasis Ally
    [Secret:] When a friendly minion is attacked, summon a 3/6 Water Elemental. """
    secret = Attack(ENEMY, FRIENDLY_MINIONS).on(Summon(CONTROLLER, 'CORE_CS2_033'))
    pass

class BAR_888:#<4> [1525]
    """ Rimetongue
    After you cast a Frost spell, summon a 1/1 Elemental that [[Freeze]s]. """
    events = OWN_SPELL_PLAY.on(Summon(CONTROLLER,'BAR_888t')*2)
    pass

class BAR_888t:#<4> [1525]
    """ Frosted Elemental
    [Freeze] any character damaged by this minion. """
    events = Attack(SELF, ALL_CHARACTERS).on(Freeze(Attack.DEFENDER))
    pass

class WC_041:#<4> [1525]
    """ Shattering Blast
    Destroy all [Frozen] minions. """
    play = Destroy(ALL_MINIONS + FROZEN)
    pass

class WC_805_Action(TargetedAction):
    TARGET=ActionArg()
    def do(self, source, target):#
        controller = source.controller
        Give(controller, target).trigger(source)
        if hasattr(target,'freeze'):
            Summon(controller,'BAR_888t').trigger(source)
            Summon(controller,'BAR_888t').trigger(source)


class WC_805:#<4> [1525] ###
    """ Frostweave Dungeoneer
    [Battlecry:] Draw a spell.If it's a Frost spell,summon two 1/1___Elementals that [Freeze]. """
    play = WC_805_Action(RANDOM(FRIENDLY_DECK + SPELL))
    pass

class WC_806:#<4> [1525] ### Costs (2)
    """ Floecaster
    Costs (2) less for each [Frozen] enemy. """
    cost_mod = - Count(ENEMY_CHARACTERS + FROZEN)
    pass
