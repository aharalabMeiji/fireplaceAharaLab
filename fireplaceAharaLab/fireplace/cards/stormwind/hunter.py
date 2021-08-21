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


class SW_321:#?#?#?#?#?#?#?#?#?#?#?#?
    """ Aimed Shot
    Deal $3 damage. Your next Hero Power deals 2 more damage. """
    #
    pass
class SW_321e:
    """ Your next Hero Power deals 2 more damage. """
    pass

class SW_322:
    """ Defend the Dwarven District
    <b>Questline:</b> Deal damage with 2 spells. <b>Reward:</b> Your Hero Power can target minions. """
    #
    pass

class SW_323:
    """ The Rat King
    [x]<b>Rush</b>. <b>Deathrattle:</b> Go
<b>Dormant</b>. Revive after 5
friendly minions die. """
    #
    pass

class SW_455:
    """ Rodent Nest
    <b>Deathrattle:</b> Summon five 1/1 Rats. """
    #
    pass

class SW_457:
    """ Leatherworking Kit
    [x]After three friendly
Beasts die, draw a Beast
and give it +1/+1.
Lose 1 Durability. """
    #
    pass

class SW_458:
    """ Ramming Mount
    [x]Give a minion +2/+2
and <b>Immune</b> while
attacking. When it dies,
summon a Ram. """
    #
    pass

class SW_459:
    """ Stormwind Piper
    After this minion attacks,
give your Beasts +1/+1. """
    #
    pass

class SW_460:
    """ Devouring Swarm
    [x]Choose an enemy minion.
Your minions attack it,
then return any that die
 to your hand. """
    #
    pass

class SW_463:
    """ Imported Tarantula
    [x]<b>Tradeable</b>
 <b>Deathrattle:</b> Summon two
1/1 Spiders with
<b>Poisonous</b> and <b>Rush</b>. """
    #
    pass