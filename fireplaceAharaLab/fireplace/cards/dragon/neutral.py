from ..utils import *

####### newtral in dragon #######

class DRG_239:#OK
	"""Blazing Battlemage	Common
	Weaponized an ancient technique once used to slice cold butter."""

class DRG_078:#OK
	"""Depth Charge	Rare
	At the start of your turn, deal 5 damage to ALL_minions."""
	events = OWN_TURN_BEGIN.on(Hit(ALL_MINIONS,5))

class DRG_057:#OK
	"""Hot Air Balloon	Common
	At the start of your turn, gain +1 Health."""
	events = OWN_TURN_BEGIN.on(Heal(SELF,1))

class DRG_070:#OK
	"""Dragon Breeder	Rare
	&lt;b&gt;Battlecry:&lt;/b&gt; Choose a friendly Dragon. Add a copy of it to_your hand."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0, PlayReq.REQ_TARGET_WITH_RACE: Race.DRAGON}
	play = Give(CONTROLLER, Copy(TARGET)) 

class DRG_066:#OK
	"""Evasive Chimaera	Common
	&lt;b&gt;Poisonous&lt;/b&gt;
	Can't be targeted by spells or Hero Powers."""
	update = Refresh(SELF, {GameTag.CANT_BE_TARGETED_BY_HERO_POWERS: 1}), Refresh(SELF, {GameTag.CANT_BE_TARGETED_BY_SPELLS: 1}) 

class DRG_401:#OK
	"""Grizzled Wizard	Epic
	&lt;b&gt;Battlecry:&lt;/b&gt; Swap Hero Powers with your opponent until your next turn."""
	play = SwapController(FRIENDLY_HERO_POWER, ENEMY_HERO_POWER)
	events = OWN_TURN_BEGIN.on(SwapController(FRIENDLY_HERO_POWER, ENEMY_HERO_POWER))

class DRG_056:#OK
	"""Parachute Brigand	Common
	[x]After you play a Pirate,
	summon this minion
	from your hand."""
	play = Play(CONTROLLER, PIRATE).after(Summon(CONTROLLER,Copy(Play.CARD)))

class DRG_049:#OK
	"""Tasty Flyfish	Common
	&lt;b&gt;Deathrattle:&lt;/b&gt; Give a Dragon in your hand +2/+2."""
	deathrattle = Buff(RANDOM(FRIENDLY + IN_HAND + DRAGON),"DRG_049e")
DRG_049e = buff(2,2)

class DRG_092:#OK
	"""Transmogrifier	Epic
	Whenever you draw a card, transform it into a random &lt;b&gt;Legendary&lt;/b&gt; minion."""
	events = Draw(CONTROLLER).on(Morph(Draw.CARD, RANDOM(LEGENDARY)))

class DRG_062:#OK
	"""Wyrmrest Purifier	Epic
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; Transform all
	Neutral cards in your deck
	into random cards from
	your class."""
	play = Morph(IN_DECK+EnumSelector(CardClass.NEUTRAL),RandomCard(card_class=Attr(FRIENDLY_HERO, GameTag.CLASS)))

class DRG_403:################################################################
	"""Blowtorch Saboteur	Epic
	&lt;b&gt;Battlecry:&lt;/b&gt; Your opponent's next Hero Power costs (3)."""
	play = Buff(ENEMY_HERO_POWER,"DRG_403e")
class DRG_403e:
	update  = Refresh(OWNER, {GameTag.COST:SET(3)})
	events = Activate(OPPONENT, ENEMY_HERO_POWER).after(Destroy(SELF))

class DRG_088:#OK
	"""Dread Raven	Epic
	Has +3 Attack for each other Dread Raven you_control."""
	play = Buff(SELF, "DRG_088e") * Count(FRIENDLY_MINIONS + ID("DRG_088") - SELF)
DRG_088e = buff(3,0)
"""Conspiracy of Ravens	Epic
Has +3 Attack for each other Dread Raven you_control."""

class DRG_060:
	"""Fire Hawk	Common
	&lt;b&gt;Battlecry:&lt;/b&gt; Gain +1 Attack for each card in your opponent's hand."""
	play = Buff(SELF, "DRG_060e") * Count(ENEMY_HAND)
DRG_060e = buff(1,0)

class DRG_059:
	"""Goboglide Tech	Common
	&lt;b&gt;Battlecry:&lt;/b&gt; If you control a_Mech, gain +1/+1 and_&lt;b&gt;Rush&lt;/b&gt;."""
	play = Find(FRIENDLY_MINIONS + MECH) & Buff(SELF,"DRG_059e")
DRG_059e=buff(1,1,rush=True)

class DRG_068:
	"""Living Dragonbreath	Common
	Your minions can't be_&lt;b&gt;Frozen&lt;/b&gt;."""
	update = Refresh(SELF, {GameTag.CANT_BE_FROZEN: 1})# 

class DRG_081:
	"""Scalerider	Common
	&lt;b&gt;Battlecry:&lt;/b&gt; If you're holding a Dragon, deal 2 damage."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}	
	play = HOLDING_DRAGON | Hit(TARGET, 2) 

class DRG_071:
	"""Bad Luck Albatross	Rare
	&lt;b&gt;Deathrattle:&lt;/b&gt; Shuffle two 1/1 Albatross into your opponent's deck."""
	deathrattle = Shuffle(OPPONENT, "DRG_071t") * 2
class DRG_071t:
	pass

class DRG_050:
	"""Devoted Maniac	Common
	&lt;b&gt;Rush&lt;/b&gt;
	&lt;b&gt;Battlecry:&lt;/b&gt; &lt;b&gt;Invoke&lt;/b&gt; Galakrond."""
	#play = InvokeGarakrond(CONTROLLER)

class DRG_063:
	"""Dragonmaw Poacher	Rare
	&lt;b&gt;Battlecry:&lt;/b&gt; If your opponent controls a Dragon, gain +4/+4 and &lt;b&gt;Rush&lt;/b&gt;."""
	play = Find(OPPONENT, DRAGON) & Give(CONTROLLER, "DRG_063e")
class DRG_063e:
	""" Poaching """
	#vanilla

class DRG_073:
	"""Evasive Feywing	Common
	Can't be targeted by spells or Hero Powers."""
	update = Refresh(SELF, {GameTag.CANT_BE_TARGETED_BY_HERO_POWERS: 1}), Refresh(SELF, {GameTag.CANT_BE_TARGETED_BY_SPELLS: 1})

class DRG_257:
	"""Frizz Kindleroost	Legendary
	&lt;b&gt;Battlecry:&lt;/b&gt; Reduce the Cost of Dragons in your deck by_(2)."""
	play = Buff(IN_DECK + DRAGON, "DRG_257e")
DRG_257e = buff(cost=-2)

class DRG_065:
	"""Hippogryph	Common
	&lt;b&gt;Rush&lt;/b&gt;
	&lt;b&gt;Taunt&lt;/b&gt;"""

class DRG_055:
	"""Hoard Pillager	Rare
	&lt;b&gt;Battlecry:&lt;/b&gt; Equip one of your destroyed weapons."""
	play = Play(CONTROLLER, RANDOM(FRIENDLY_WEAPON+KILLED))

class DRG_067:
	"""Troll Batrider	Common
	&lt;b&gt;Battlecry:&lt;/b&gt; Deal 3 damage to a random enemy minion."""
	play = Hit(RANDOM(ENEMY_MINIONS), 3)

class DRG_058:
	"""Wing Commander	Common
	Has +2 Attack for each Dragon in your hand."""
	update = Refresh(FRIENDLY_HAND+DRAGON, "DRG_058e")
DRG_058e = buff(2,0)

class DRG_064:
	"""Zul'Drak Ritualist	Rare
	[x]&lt;b&gt;Taunt&lt;/b&gt;
	 &lt;b&gt;Battlecry:&lt;/b&gt; Summon three
	random 1-Cost minions
	for your opponent."""
	play = Summon(OPPONENT, RandomMinion(cost=3))*3

class DRG_054:
	"""Big Ol' Whelp	Common
	&lt;b&gt;Battlecry:&lt;/b&gt; Draw a card."""
	play = Draw(CONTROLLER)

class DRG_086:
	"""Chromatic Egg	Epic
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; Secretly &lt;b&gt;Discover&lt;/b&gt;
	a Dragon to hatch into.
	&lt;b&gt;Deathrattle:&lt;/b&gt; Hatch!"""
	play = HoldinHatch(CONTROLLER, Discover(CONTROLLER, DRAGON))
	deathrattle = OpenHatch(CONTROLLER )

class DRG_086e:
	""" What's in the Egg?"""
	pass

class DRG_075:
	"""Cobalt Spellkin	Rare
	&lt;b&gt;Battlecry:&lt;/b&gt; Add two 1-Cost spells from your class to_your hand."""
	play = Give(CONTROLLER, RandomSpell(cost=1,card_class=Attr(FRIENDLY_HERO, GameTag.CLASS)))*2

class DRG_076:
	"""Faceless Corruptor	Rare
	[x]&lt;b&gt;Rush&lt;/b&gt;. &lt;b&gt;Battlecry:&lt;/b&gt; Transform
	one of your minions into
	a copy of this."""
	reqirements = {PlayReq.REQ_FRIENDLY_TARGET: 0}
	play = Morph(TARGET, ExactCopy(SELF))

class DRG_082:
	"""Kobold Stickyfinger	Epic
	&lt;b&gt;Battlecry:&lt;/b&gt; Steal your opponent's weapon."""
	play = Steal(ENEMY_WEAPON, CONTROLLER)

class DRG_069:
	"""Platebreaker	Common
	&lt;b&gt;Battlecry:&lt;/b&gt; Destroy your opponent's Armor."""
	play = DestroyArmor(OPPONENT)

class DRG_242:
	"""Shield of Galakrond	Common
	&lt;b&gt;Taunt&lt;/b&gt;
	&lt;b&gt;Battlecry:&lt;/b&gt; &lt;b&gt;Invoke&lt;/b&gt; Galakrond."""
	#play = InvokeGarakrond(CONTROLLER)

class DRG_072:
	"""Skyfin	Epic
	&lt;b&gt;Battlecry:&lt;/b&gt; If you're holding a Dragon, summon 2 random Murlocs."""
	play = HOLDING_DRAGON & Summon(CONTROLLER,RandomMurloc())*2

class DRG_084:
	"""Tentacled Menace	Epic
	&lt;b&gt;Battlecry:&lt;/b&gt; Each player draws a card. Swap their_Costs."""
	play = TentacledMenace(CONTROLLER,OPPONENT)

class DRG_074:
	"""Camouflaged Dirigible	Common
	&lt;b&gt;Battlecry:&lt;/b&gt; Give your other Mechs &lt;b&gt;Stealth&lt;/b&gt; until your_next turn."""
	play = Buff(CONTROLLER, "DRG_074e")
class DRG_074e:
	play = Stealth(FRIENDLY_MINIONS+MECH)  
	events = OWN_TURN_BEGIN.on(Destroy(SELF))

class DRG_079:
	"""Evasive Wyrm	Common
	&lt;b&gt;Divine Shield&lt;/b&gt;, &lt;b&gt;Rush&lt;/b&gt;
	Can't be targeted by spells or Hero Powers."""
	update = Refresh(SELF, {GameTag.CANT_BE_TARGETED_BY_HERO_POWERS: 1}), Refresh(SELF, {GameTag.CANT_BE_TARGETED_BY_SPELLS: 1})


class DRG_061:
	"""Gyrocopter	Common
	&lt;b&gt;Rush&lt;/b&gt;
	&lt;b&gt;Windfury&lt;/b&gt;"""

class DRG_099:##################################
	"""Kronx Dragonhoof	Legendary
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; Draw Galakrond.
	If you're already Galakrond,
	unleash a Devastation."""  # change hero to "DRGA_BOSS_24h"?


class DRG_077:
	"""Utgarde Grapplesniper	Rare
	&lt;b&gt;Battlecry:&lt;/b&gt; Both players draw a card. If it's a Dragon, summon it."""
	play = UtgardeGrapplesniper(CONTROLLER,OPPONENT)

class DRG_310:
	"""Evasive Drakonid	Common
	&lt;b&gt;Taunt&lt;/b&gt;
	Can't be targeted by spells or Hero Powers."""
	update = Refresh(SELF, {GameTag.CANT_BE_TARGETED_BY_HERO_POWERS: 1})

class DRG_091:
	"""Shu'ma	Legendary
	At the end of your turn,
	fill your board with 1/1_Tentacles."""
	play = Summon(CONTROLLER,"DRG_091t") * 7
class DRG_091t:
	""" Tentacles"""
	#vanilla

class DRG_213:
	"""Twin Tyrant	Common
	&lt;b&gt;Battlecry:&lt;/b&gt; Deal 4 damage to two random enemy minions."""
	play = Hit(RANDOM(ENEMY_MINIONS),4) * 2

class DRG_089:
	"""Dragonqueen Alexstrasza	Legendary
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; If your deck has
	no duplicates, add 2 other
	random Dragons to your
	hand. They cost (1)."""
	powered_up = -FindDuplicates(FRIENDLY_DECK)
	play = powered_up & Buff(CONTROLLER, "DRG_089e")
class DRG_089e:
	"""A Queen's Discount"""
	play = Give(CONTROLLER, RANDOM(DRAGON)).on(Refresh(Give.CARD, {GameTag.COST: 1})),Give(CONTROLLER, RANDOM(DRAGON)).on(Refresh(Give.CARD, {GameTag.COST: 1}))

class DRG_402:
	"""Sathrovarr	Legendary
	&lt;b&gt;Battlecry:&lt;/b&gt; Choose a friendly minion. Add a copy of it to_your hand, deck, and battlefield."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY}
	play= Give(CONTROLLER, Copy(TARGET)),Shuffle(CONTROLLER,Copy(TARGET)), Summon(CONTROLLER,Copy(TARGET))

