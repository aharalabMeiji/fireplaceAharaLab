from ..utils import *

class SW_006:#OK
    """ Stubborn Suspect
    <b>Deathrattle:</b> Summon a random 3-Cost minion. """
    deathrattle = Summon(CONTROLLER, RANDOM(MINION+(COST==3)))
    pass

class SW_036:#OK
    """ Two-Faced Investor
    [x]At the end of your turn,
reduce the Cost of a card
in your hand by (1). <i>(50%
chance to increase.)</i> """
    events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_HAND),random.choice(['SW_036e','SW_036e2'])))
    pass

SW_036e=buff(cost=-1)
SW_036e2=buff(cost=1)

class SW_045:#OK
    """ Auctioneer Jaxon
    [x]Whenever you <b>Trade</b>,<b>Discover</b> a card from your_deck to draw instead. """
    pass

class SW_054:#OK
    """ Stormwind Guard
    <b>Taunt</b><b>Battlecry:</b> Give adjacent minions +1/+1. """
    update = BuffOnce(SELF_ADJACENT,'SW_054e')
    #play = Buff(SELF_ADJACENT,'SW_054e')
    pass
SW_054e=buff(atk=1,health=1)

class SW_055:#OK
    """ Impatient Shopkeep
    <b>Tradeable</b><b>Rush</b> """
    #
    pass

class SW_056:#OK
    """ Spice Bread Baker
    <b>Battlecry:</b> Restore Health to your hero equal to your hand size. """
    play = Heal(FRIENDLY_HERO, Count(FRIENDLY_HAND))
    pass

class SW_057:#OK
    """ Package Runner
    Can only attack if you have at least 8 cards in hand. """
    update = (Count(FRIENDLY_HAND)<8) & Refresh(SELF, {GameTag.CANT_ATTACK:True}) | Refresh(SELF,{GameTag.CANT_ATTACK:False}) 
    pass

class SW_059:
    """ Deeprun Engineer
    <b>Battlecry:</b> <b>Discover</b> a Mech. It costs (1) less. """
    play = SW_059Action(CONTROLLER, RandomMech()) # cost 1 less
    pass
SW_059e=buff(cost=-1)

class SW_060:#OK
    """ Florist
    [x]At then end of your turn,
reduce the cost of a Nature
spell in your hand by (1). """
    events = OWN_TURN_END.on(Buff(FRIENDLY_HAND+NATURE,'SW_060t'))
    pass
SW_060t=buff(cost=-1)

class SW_061:#OK
    """ Guild Trader
    <b>Tradeable</b><b>Spell Damage +2</b> """
    #
    pass

class SW_062:#OK
    """ Goldshire Gnoll
    [x]<b>Rush</b>Costs (1) less for each__other card in your hand. """
    update = Refresh(FRIENDLY_HAND - SELF, {GameTag.COST:-1})
    pass

class SW_063:
    """ Battleground Battlemaster
    Adjacent minions have <b>Windfury</b>. """
    update = Refresh(FRIENDLY_MINIONS+ADJACENT,'SW_063e')
    pass
SW_63e=buff({GameTag.WINDFURY:True})

class SW_064:
    """ Northshire Farmer
    <b>Battlecry:</b> Choose a friendly Beast. Shuffle three 3/3 copies_into_your_deck. """
    requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.BEAST}
    play= Shuffle(CONTROLLER, Buff(Copy(TARGET),'SW_64e'))*3
    pass
SW_064e=buff(atk=3,health=3)
class SW_065:
    """ Pandaren Importer
    [x]<b>Battlecry:</b> <b>Discover</b> a spell that didn't start in your deck. """
    play=GenericChoice(CONTROLLER,RANDOM(SPELL-FRIENDLY_DECK)*3)
    pass

class SW_066:
    """ Royal Librarian
    [x]<b>Tradeable</b><b>Battlecry:</b> <b>Silence</b>a minion. """
    requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0}
    play = Buff(TARGET,{GameTag.SILENCE:True})
    pass

class SW_067:
    """ Stockades Guard
    [x]<b>Battlecry:</b> Give a friendly minion <b>Taunt</b>. """
    requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0}
    play = Buff(TARGET,{GameTag.TAUNT:True})
    pass

class SW_068:
    """ Mo'arg Forgefiend
    <b>Taunt</b><b>Deathrattle:</b> Gain 8 Armor. """
    deathrattle = GainArmor(CONTROLLER,8)
    pass

class SW_069:
    """ Enthusiastic Banker
    [x]At the end of your turn, store a card from your deck. <b>Deathrattle:</b> Add the stored cards to your hand. """
    events = OWN_TURN_END.on(Morph('SW_069e', ID(RANDOM(FRIENDLY_DECK))))
    deathrattle = Give(CONTROLLER,'SW_069e')
    pass
class SW_069e:
    """ Safety Deposit """
    pass

class SW_070:
    """ Mailbox Dancer
    [x]<b>Battlecry:</b> Add a Coin to your hand. <b>Deathrattle:</b> Give your opponent one. """
    play = Give(CONTROLLER, 'GAME_005e')
    deathrattle = Give(OPPONENT, 'GAME_005e')
    pass

class SW_071:
    """ Lion's Guard
    [x]<b>Battlecry:</b> If you have 15 or less Health, gain +2/+4 and <b>Taunt</b>. """
    #play = (HEALTH(FRIENDLY_HERO)<=15).on(Buff())
    pass
SW_071e=buff(atk=2,health=4,taunt=True)

class SW_072:
    """ Rustrot Viper
    [x]<b>Tradeable</b><b>Battlecry:</b> Destroy your opponent's weapon. """
    play = Destroy(ENEMY_WEAPON)
    pass

class SW_073:
    """ Cheesemonger
    [x]Whenever your opponent casts a spell, add a random spell with the same Cost to your hand. """
    events = Play(OPPONENT, SPELL).on(Give(CONTROLLER, RandomSpell(cost=Attr(Play.CARD,GameTag.COST))))
    pass

class SW_074:
    """ Nobleman
    <b>Battlecry:</b> Create a Golden copy of a random card in your hand. """
    play = Give(CONTROLLER,RANDOM(FRIENDLY_HAND))#gold?
    pass

class SW_075:
    """ Elwynn Boar
    [x]<b>Deathrattle:</b> If you had 7
Elwynn Boars die this game,
equip a 15/3 Sword of a
___Thousand Truths.@ <i>(@/7)</i> """
    # if we use LazyNum, we are able to make in much more general way.
    deathrattle = CountDeathAction(CONTROLLER,['SW_075'], 7, Summon(CONTROLLER,'SW_075t'))
    pass
class SW_075t: ##
    """ [x]After your hero attacks,destroy your opponent's Mana Crystals."""
    events = Attack(FRIENDLY_HERO).on(GainMana(OPPONENT,-10))
    pass

class SW_076:
    """ City Architect
    [x]<b>Battlecry:</b> Summon two
0/5 Castle Walls
with <b>Taunt</b>. """
    #
    pass

class SW_077:
    """ Stockades Prisoner
    [x]Starts <b>Dormant</b>.
After you play 3 cards,
this awakens. """
    #
    pass

class SW_078:
    """ Lady Prestor
    [x]<b>Battlecry:</b> Transform minions
in your deck into random
Dragons. <i>(They keep their
__original stats and Cost.)</I> """
    #
    pass

class SW_079:
    """ Flightmaster Dungar
    [x]<b>Battlecry:</b> Choose a
flightpath and go <b>Dormant.
</b> Awaken with a bonus
__when you complete it! """
    #
    pass

class SW_080:
    """ Cornelius Roame
    [x]At the start and end
_of each player's turn,
draw a card. """
    #
    pass

class SW_081:
    """ Varian, King of Stormwind
    [x]<b>Battlecry:</b> Draw a <b>Rush</b>
minion to gain <b>Rush</b>.
Repeat for <b>Taunt</b> and
<b>Divine Shield</b>. """
    #
    pass

class SW_306:
    """ Encumbered Pack Mule
    [x]<b>Taunt</b>
When you draw this, add a
_copy of it to your hand. """
    #
    pass

class SW_307:
    """ Traveling Merchant
    [x]<b>Tradeable</b>
<b>Battlecry:</b> Gain +1/+1
for each other friendly
_minion you control. """
    #
    pass

class SW_319:
    """ Peasant
    At the start of your turn, draw a card. """
    #
    pass

class SW_400:
    """ Entrapped Sorceress
    [x]<b>Battlecry:</b> If you control a
_<b>Quest</b>, <b>Discover</b> a spell. """
    #
    pass

class SW_418:
    """ SI:7 Skulker
    [x]<b>Stealth</b>
<b>Battlecry:</b> The next card
__you draw costs (1) less. """
    #
    pass

