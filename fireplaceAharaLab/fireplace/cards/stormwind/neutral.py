from ..utils import *

class SW_006:
    """ Stubborn Suspect
    <b>Deathrattle:</b> Summon a random 3-Cost minion. """
    deathrattle = Summon(CONTROLLER, RANDOM(MINION+(COST==3)))
    pass

class SW_036:
    """ Two-Faced Investor
    [x]At the end of your turn,
reduce the Cost of a card
in your hand by (1). <i>(50%
chance to increase.)</i> """
    events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_HAND),random.choice(['SW_036e','SW_036e2'])))
    pass

SW_036e=buff(cost=1)
SW_036e2=buff(cost=-1)

class SW_045:
    """ Auctioneer Jaxon
    [x]Whenever you <b>Trade</b>,<b>Discover</b> a card from your_deck to draw instead. """
    #trade_option=1#GameTag.DISCOVER=415
    pass

class SW_054:
    """ Stormwind Guard
    <b>Taunt</b><b>Battlecry:</b> Give adjacent minions +1/+1. """
    play = Buff(FRIENDLY_MINIONS+ADJACENT,'SW_054e')
    pass
SW_054e=buff(atk=1,health=1)

class SW_055:
    """ Impatient Shopkeep
    <b>Tradeable</b><b>Rush</b> """
    #
    pass

class SW_056:
    """ Spice Bread Baker
    <b>Battlecry:</b> Restore Health to your hero equal to your hand size. """
    #
    pass

class SW_057:
    """ Package Runner
    Can only attack if you have at least 8 cards in hand. """
    #
    pass

class SW_059:
    """ Deeprun Engineer
    <b>Battlecry:</b> <b>Discover</b> a Mech. It costs (1) less. """
    #
    pass

class SW_060:
    """ Florist
    [x]At then end of your turn,
reduce the cost of a Nature
spell in your hand by (1). """
    #
    pass

class SW_061:
    """ Guild Trader
    <b>Tradeable</b>
<b>Spell Damage +2</b> """
    #
    pass

class SW_062:
    """ Goldshire Gnoll
    [x]<b>Rush</b>
Costs (1) less for each
__other card in your hand. """
    #
    pass

class SW_063:
    """ Battleground Battlemaster
    Adjacent minions
have <b>Windfury</b>. """
    #
    pass

class SW_064:
    """ Northshire Farmer
    <b>Battlecry:</b> Choose a friendly Beast. Shuffle three 3/3 copies_into_your_deck. """
    #
    pass

class SW_065:
    """ Pandaren Importer
    [x]<b>Battlecry:</b> <b>Discover</b> a
spell that didn't start
in your deck. """
    #
    pass

class SW_066:
    """ Royal Librarian
    [x]<b>Tradeable</b>
<b>Battlecry:</b> <b>Silence</b>
a minion. """
    #
    pass

class SW_067:
    """ Stockades Guard
    [x]<b>Battlecry:</b> Give a
friendly minion <b>Taunt</b>. """
    #
    pass

class SW_068:
    """ Mo'arg Forgefiend
    <b>Taunt</b>
<b>Deathrattle:</b> Gain 8 Armor. """
    #
    pass

class SW_069:
    """ Enthusiastic Banker
    [x]At the end of your turn,
store a card from your deck.
<b>Deathrattle:</b> Add the stored
cards to your hand. """
    #
    pass

class SW_070:
    """ Mailbox Dancer
    [x]<b>Battlecry:</b> Add a Coin
to your hand.
<b>Deathrattle:</b> Give your
opponent one. """
    #
    pass

class SW_071:
    """ Lion's Guard
    [x]<b>Battlecry:</b> If you have 15
or less Health, gain
+2/+4 and <b>Taunt</b>. """
    #
    pass

class SW_072:
    """ Rustrot Viper
    [x]<b>Tradeable</b>
<b>Battlecry:</b> Destroy your
opponent's weapon. """
    #
    pass

class SW_073:
    """ Cheesemonger
    [x]Whenever your opponent
casts a spell, add a random
spell with the same Cost
to your hand. """
    #
    pass

class SW_074:
    """ Nobleman
    <b>Battlecry:</b> Create a Golden copy of a random card in your hand. """
    #
    pass

class SW_075:
    """ Elwynn Boar
    [x]<b>Deathrattle:</b> If you had 7
Elwynn Boars die this game,
equip a 15/3 Sword of a
___Thousand Truths.@ <i>(@/7)</i> """
    #
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

