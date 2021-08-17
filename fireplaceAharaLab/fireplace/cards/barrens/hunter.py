from ..utils import *

class BAR_030:
    """ Pack Kodo
    <b>Battlecry:</b> <b>Discover</b> a Beast, <b>Secret</b>, or weapon.
    """
    play = GenericChoice(CONTROLLER, [
    	RandomCollectible(race=Race.BEAST),
    	RandomCollectible(secret=True),
    	RandomCollectible(type=CardType.WEAPON)
    ])
    pass

class BAR_031:
    """ Sunscale Raptor
    <b>Frenzy:</b> Shuffle a Sunscale Raptor into your deck with permanent +2/+1.
    """
    events = Damage(SELF).on(Frenzy(SELF,Shuffle(CONTROLLER,PermanentBuff(ID("BAR_031"),2,1))))
    pass

class BAR_032:
    """ Piercing Shot
    Deal $6 damage to a minion. Excess damage hits the enemy hero.
    """
    requirements={PlayReq.REQ_MINION_TARGET:0}
    play = HitAndExcessToOther(TARGET,6,ENEMY_HERO)
    pass

class BAR_033:
    """ Prospector's Caravan
    At the start of your turn, give all minions in your hand +1/+1.
    """
    events = OWN_TURN_BEGIN.on(Buff(FRIENDLY_HAND + MINION, "BAR_033e"))
    pass
BAR_033e=buff(atk=1,health=1)

class BAR_034:##################################################
    """ Tame Beast (Rank 1)
    Summon a 2/2 Beast with <b>Rush</b>. <i>(Upgrades when you
have 5 Mana.)</i>
    """
    events = ( 
        Play(CONTROLLER,SELF).on(Summon(CONTROLLER,"BAR_034t3")),
        HaveMana(CONTROLLER,5).on(Give(CONTROLLER,"BAR_034t"),Discard(self))
        )
    pass
class BAR_034t:
    """ Summon a 4/4 Beast with &lt;b&gt;Rush&lt;/b&gt;. &lt;i&gt;(Upgrades when you
have 10 Mana.)&lt;/i&gt;"""
    events = ( 
        Play(CONTROLLER,SELF).on(Summon(CONTROLLER,"BAR_034t4")),
        HaveMana(CONTROLLER,10).on(Give(CONTROLLER,"BAR_034t2"),Discard(self))
        )
    pass
class BAR_034t2:
    """ Summon a 6/6 Beast with &lt;b&gt;Rush&lt;/b&gt;."""
    play = Summon(CONTROLLER,"BAR_034t5")
    pass
class BAR_034t3:
    pass
class BAR_034t4:
    pass
class BAR_034t5:
    pass


class BAR_035:
    """ Kolkar Pack Runner
    [x]After you cast a spell,
summon a 1/1 Hyena
with <b>Rush</b>.
    """
    #
    pass

class BAR_037:
    """ Warsong Wrangler
    [x]<b>Battlecry:</b> <b>Discover</b> a
Beast from your deck. Give
all copies of it +2/+1 
<i>(wherever_they_are)</i>.
    """
    #
    pass

class BAR_038:
    """ Tavish Stormpike
    After a friendly Beast attacks, summon a Beast from your deck that costs (1) less.
    """
    #
    pass

class BAR_551:
    """ Barak Kodobane
    [x]<b>Battlecry:</b> Draw a 1, 2,
__and 3-Cost spell.
    """
    #
    pass

class BAR_801:
    """ Wound Prey
    Deal $1 damage. Summon a 1/1 Hyena with <b>Rush</b>.
    """
    #
    pass

class WC_007:
    """ Serpentbloom
    Give a friendly
Beast <b>Poisonous</b>.
    """
    #
    pass

class WC_008:
    """ Sin'dorei Scentfinder
    <b>Frenzy:</b> Summon four 1/1 Hyenas with <b>Rush</b>.
    """
    #
    pass

class WC_037:
    """ Venomstrike Bow
    <b>Poisonous</b>
    """
    #
    pass
