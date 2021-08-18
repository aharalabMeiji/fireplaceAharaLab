from ..utils import *

class BAR_030:#OK
    """ Pack Kodo
    <b>Battlecry:</b> <b>Discover</b> a Beast, <b>Secret</b>, or weapon.
    """
    play = GenericChoice(CONTROLLER, [
    	RandomCollectible(race=Race.BEAST),
    	#RandomCollectible(type=CardType.SPELL),# secret
    	RandomCollectible(secret=True),# secret
    	RandomCollectible(type=CardType.WEAPON)
    ])
    pass

class BAR_031:#OK
    """ Sunscale Raptor
    <b>Frenzy:</b> Shuffle a Sunscale Raptor into your deck with permanent +2/+1.
    """
    events = Damage(SELF).on(Frenzy(SELF,Shuffle(CONTROLLER,PermanentBuff(Copy(SELF),2,1))))
    pass

class BAR_032:#OK
    """ Piercing Shot
    Deal $6 damage to a minion. Excess damage hits the enemy hero.
    """
    requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0}
    play = HitAndExcessToOther(TARGET,6,ENEMY_HERO)
    pass

class BAR_033:#OK
    """ Prospector's Caravan
    At the start of your turn, give all minions in your hand +1/+1.
    """
    events = OWN_TURN_BEGIN.on(Buff(FRIENDLY_HAND + MINION, "BAR_033e"))
    pass
BAR_033e=buff(atk=1,health=1)

class BAR_034:#OK
    """ Tame Beast (Rank 1)
    Summon a 2/2 Beast with <b>Rush</b>. <i>(Upgrades when you
have 5 Mana.)</i>    """
    play = Summon(CONTROLLER,"BAR_034t3")
    pass
class BAR_034t:
    """ Summon a 4/4 Beast with &lt;b&gt;Rush&lt;/b&gt;. &lt;i&gt;(Upgrades when you
have 10 Mana.)&lt;/i&gt;"""
    play = Summon(CONTROLLER,"BAR_034t4")
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


class BAR_035:#OK
    """ Kolkar Pack Runner
    [x]After you cast a spell,
summon a 1/1 Hyena
with <b>Rush</b>.
    """
    events = OWN_SPELL_PLAY.on(Summon(CONTROLLER,'BAR_035t'))
    pass
class BAR_035t:
    pass

class BAR_037:##############################################
    """ Warsong Wrangler
    [x]<b>Battlecry:</b> <b>Discover</b> a Beast from your deck. Give all copies of it +2/+1 <i>(wherever_they_are)</i>.
    """
    play = ChoiceAfter(CONTROLLER,RANDOM(FRIENDLY_DECK)*3,Buff(ChoiceAfter.CARDS,'BAR_037e'))
    #play = Choice(CONTROLLER, RANDOM(FRIENDLY_DECK+BEAST)*3).on(Give(CONTROLLER,Choice.CARD))
    #.on(Buff(ALL_CHARACTERS+ID(Attr(Choice.CARD,GameTag.ID)),'BAR_037e'))
    pass
BAR_037e=buff(atk=2,health=1)

class BAR_038:#'1 less' -> 'less than'
    """ Tavish Stormpike
    After a friendly Beast attacks, summon a Beast from your deck that costs (1) less.
    """
    events = Attack(FRIENDLY_MINIONS + BEAST).after(Summon(CONTROLLER, RANDOM(FRIENDLY_DECK+BEAST+(COST<Attr(Attack.ATTACKER,GameTag.COST)))))
    pass

class BAR_551:#OK
    """ Barak Kodobane
    [x]<b>Battlecry:</b> Draw a 1, 2,__and 3-Cost spell.
    """
    play = (
        Give(CONTROLLER,RANDOM(FRIENDLY_DECK+SPELL+(COST==1))),
        Give(CONTROLLER,RANDOM(FRIENDLY_DECK+SPELL+(COST==2))),
        Give(CONTROLLER,RANDOM(FRIENDLY_DECK+SPELL+(COST==3)))
        )
    pass

class BAR_801:#OK
    """ Wound Prey
    Deal $1 damage. Summon a 1/1 Hyena with <b>Rush</b>.
    """
    requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_HERO_OR_MINION_TARGET:0}
    play = (Hit(TARGET,1),Summon(CONTROLLER,'BAR_035t'))
    pass

class WC_007:#OK
    """ Serpentbloom
    Give a friendly
Beast <b>Poisonous</b>.
    """
    play = SetAttr(RANDOM(FRIENDLY_HAND+BEAST),'poisonous',True)
    pass

class WC_008:#OK
    """ Sin'dorei Scentfinder
    <b>Frenzy:</b> Summon four 1/1 Hyenas with <b>Rush</b>.
    """
    events = Damage(SELF).on(Frenzy(SELF,Summon(CONTROLLER,'BAR_035t')*4))
    pass

class WC_037:
    """ Venomstrike Bow
    <b>Poisonous</b>
    """
    #
    pass
