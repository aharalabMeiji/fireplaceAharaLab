from ..utils import *


class SW_320:#OK
    """ Rats of Extraordinary Size
    [x]Summon seven 1/1
Rats. Any that can't fit
on the battlefield go to
your hand with +4/+4. """
    #play = Summon(CONTROLLER,'SW_455t')
    play = (
        ((Count(FRIENDLY_MINIONS) < 8) & Summon(CONTROLLER,'SW_455t') | Give(CONTROLLER,'SW_455t').then(Buff(Give.CARD,'SW_320e'))),
        ((Count(FRIENDLY_MINIONS) < 8) & Summon(CONTROLLER,'SW_455t') | Give(CONTROLLER,'SW_455t').then(Buff(Give.CARD,'SW_320e'))),
        ((Count(FRIENDLY_MINIONS) < 8) & Summon(CONTROLLER,'SW_455t') | Give(CONTROLLER,'SW_455t').then(Buff(Give.CARD,'SW_320e'))),
        ((Count(FRIENDLY_MINIONS) < 8) & Summon(CONTROLLER,'SW_455t') | Give(CONTROLLER,'SW_455t').then(Buff(Give.CARD,'SW_320e'))),
        ((Count(FRIENDLY_MINIONS) < 8) & Summon(CONTROLLER,'SW_455t') | Give(CONTROLLER,'SW_455t').then(Buff(Give.CARD,'SW_320e'))),
        ((Count(FRIENDLY_MINIONS) < 8) & Summon(CONTROLLER,'SW_455t') | Give(CONTROLLER,'SW_455t').then(Buff(Give.CARD,'SW_320e'))),
        ((Count(FRIENDLY_MINIONS) < 8) & Summon(CONTROLLER,'SW_455t') | Give(CONTROLLER,'SW_455t').then(Buff(Give.CARD,'SW_320e')))
        )
    pass
SW_320e=buff(atk=4,health=4)


class SW_321:
    """ Aimed Shot
    Deal $3 damage. Your next Hero Power deals 2 more damage. """
    #
    pass

class SW_321e:
    """ Aiming
    Your next Hero Power deals 2 more damage. """
    #
    pass

class SW_322:
    """ Defend the Dwarven District
    [Questline:] Deal damage with 2 spells. [Reward:] Your Hero Power can target minions. """
    #
    pass

class SW_322t:
    """ Take the High Ground
    [Questline:] Deal damagewith 2 spells.[Reward:] Set the Cost ofyour Hero Power to (0). """
    #
    pass

class SW_322t2:
    """ Knock 'Em Down
    [Questline:] Dealdamage with 2 spells.[Reward:] Tavish,Master Marksman. """
    #
    pass

class SW_322t4:
    """ Tavish, Master Marksman
    [Battlecry:] For the rest ofthe game, spells you castrefresh your Hero Power. """
    #
    pass

class SW_323:
    """ The Rat King
    [Rush]. [Deathrattle:] Go[Dormant]. Revive after 5friendly minions die. """
    #
    pass

class SW_323e:
    """ Rat King's Slumber
    [Dormant]. Awaken after @ |4(friendly minion dies., friendly minions die.) """
    #
    pass

class SW_455:
    """ Rodent Nest
    [Deathrattle:] Summon five 1/1 Rats. """
    #
    pass

class SW_455t:
    """ Rat
     """
    #
    pass

class SW_457:
    """ Leatherworking Kit
    After three friendlyBeasts die, draw a Beastand give it +1/+1.Lose 1 Durability. """
    #
    pass

class SW_458:
    """ Ramming Mount
    Give a minion +2/+2and [Immune] whileattacking. When it dies,summon a Ram. """
    #
    pass

class SW_458e:
    """ On a Ram
    +2/+2 and [Immune] while attacking. [Deathrattle:] Summon a Ram. """
    #
    pass

class SW_458t:
    """ Tavish's Ram
    [Immune] while attacking. """
    #
    pass

class SW_459:
    """ Stormwind Piper
    After this minion attacks,give your Beasts +1/+1. """
    #
    pass

class SW_459e:
    """ Entranced
    +1/+1. """
    #
    pass

class SW_460:
    """ Devouring Swarm
    Choose an enemy minion.Your minions attack it,then return any that die to your hand. """
    #
    pass

class SW_463:
    """ Imported Tarantula
    [Tradeable] [Deathrattle:] Summon two1/1 Spiders with[Poisonous] and [Rush]. """
    #
    pass

class SW_463t:
    """ Invasive Spiderling
    [Poisonous][Rush] """
    #
    pass

