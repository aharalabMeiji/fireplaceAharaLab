from ..utils import *

####### neutral in dragon #######

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
	<b>Battlecry:</b> Choose a friendly Dragon. Add a copy of it to_your hand."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0, PlayReq.REQ_TARGET_WITH_RACE: Race.DRAGON}
	play = Give(CONTROLLER, Copy(TARGET)) 

class DRG_066:#OK
	"""Evasive Chimaera	Common
	<b>Poisonous</b>
	Can't be targeted by spells or Hero Powers."""
	update = Refresh(SELF, {GameTag.CANT_BE_TARGETED_BY_HERO_POWERS: True}), Refresh(SELF, {GameTag.CANT_BE_TARGETED_BY_SPELLS: True}) 

class DRG_401:#OK
	"""Grizzled Wizard	Epic
	<b>Battlecry:</b> Swap Hero Powers with your opponent until your next turn."""
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
	<b>Deathrattle:</b> Give a Dragon in your hand +2/+2."""
	deathrattle = Buff(RANDOM(FRIENDLY + IN_HAND + DRAGON),"DRG_049e")
DRG_049e = buff(2,2)

class DRG_092:#OK
	"""Transmogrifier	Epic
	Whenever you draw a card, transform it into a random <b>Legendary</b> minion."""
	events = Draw(CONTROLLER).on(Morph(Draw.CARD, RANDOM(LEGENDARY)))

class DRG_062:#OK
	"""Wyrmrest Purifier	Epic
	[x]<b>Battlecry:</b> Transform all
	Neutral cards in your deck
	into random cards from
	your class."""
	play = Morph(IN_DECK+FRIENDLY+EnumSelector(CardClass.NEUTRAL),RandomCard(card_class=Attr(FRIENDLY_HERO, GameTag.CLASS)))

#### 10 ####

class DRG_403:#OK
	"""Blowtorch Saboteur	Epic
	<b>Battlecry:</b> Your opponent's next Hero Power costs (3)."""
	play = Buff(CONTROLLER,"DRG_403e")
class DRG_403e:
	update = Refresh(ENEMY_HERO_POWER, {GameTag.COST:SET(3)})
	events = Activate(OPPONENT, HERO_POWER).on(Destroy(SELF))

class DRG_088:#OK
	"""Dread Raven	Epic
	Has +3 Attack for each other Dread Raven you_control."""
	play = Buff(SELF, "DRG_088e") * Count(FRIENDLY_MINIONS + ID("DRG_088") - SELF)
DRG_088e = buff(3,0)
"""Conspiracy of Ravens	Epic
Has +3 Attack for each other Dread Raven you_control."""

class DRG_060:#OK
	"""Fire Hawk	Common
	<b>Battlecry:</b> Gain +1 Attack for each card in your opponent's hand."""
	play = Buff(SELF, "DRG_060e") * Count(ENEMY_HAND)
DRG_060e = buff(1,0)

class DRG_059:#OK
	"""Goboglide Tech	Common
	<b>Battlecry:</b> If you control a_Mech, gain +1/+1 and_<b>Rush</b>."""
	play = Find(FRIENDLY_MINIONS + MECH) & Buff(SELF,"DRG_059e")
DRG_059e=buff(1,1,rush=True)

class DRG_068:#OK
	"""Living Dragonbreath	Common
	Your minions can't be_<b>Frozen</b>."""
	update = Refresh(FRIENDLY_MINIONS, {GameTag.CANT_BE_FROZEN: True})# 

class DRG_081:#OK
	"""Scalerider	Common
	<b>Battlecry:</b> If you're holding a Dragon, deal 2 damage."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}	
	play = HOLDING_DRAGON | Hit(TARGET, 2) 

class DRG_071:#OK
	"""Bad Luck Albatross	Rare
	<b>Deathrattle:</b> Shuffle two 1/1 Albatross into your opponent's deck."""
	deathrattle = Shuffle(OPPONENT, "DRG_071t") * 2
class DRG_071t:
	pass

class DRG_050:########################### Galakrond pass
	"""Devoted Maniac	Common
	<b>Rush</b>
	<b>Battlecry:</b> <b>Invoke</b> Galakrond."""
	#play = InvokeGarakrond(CONTROLLER)

class DRG_063:#OK
	"""Dragonmaw Poacher	Rare
	<b>Battlecry:</b> If your opponent controls a Dragon, gain +4/+4 and <b>Rush</b>."""
	play = Find(ENEMY_MINIONS + DRAGON) & Buff(SELF, "DRG_063e")
DRG_063e = buff(4,4,rush=True)
""" Poaching """
	

class DRG_073:#OK
	"""Evasive Feywing	Common
	Can't be targeted by spells or Hero Powers."""
	update = Refresh(SELF, {GameTag.CANT_BE_TARGETED_BY_HERO_POWERS: True}), Refresh(SELF, {GameTag.CANT_BE_TARGETED_BY_SPELLS: True})

####20 ####

class DRG_257:#OK
	"""Frizz Kindleroost	Legendary
	<b>Battlecry:</b> Reduce the Cost of Dragons in your deck by_(2)."""
	play = Buff(FRIENDLY_DECK + DRAGON, "DRG_257e3")
DRG_257e3 = buff(cost=-2)

class DRG_065:#OK
	"""Hippogryph	Common
	<b>Rush</b>
	<b>Taunt</b>"""

class DRG_055:#OK
	"""Hoard Pillager	Rare
	<b>Battlecry:</b> Equip one of your destroyed weapons."""
	play = Summon(CONTROLLER, Copy(RANDOM(FRIENDLY + KILLED + WEAPON)))

class DRG_067:#OK
	"""Troll Batrider	Common
	<b>Battlecry:</b> Deal 3 damage to a random enemy minion."""
	play = Hit(RANDOM(ENEMY_MINIONS), 3)

class DRG_058:#OK
	"""Wing Commander	Common
	Has +2 Attack for each Dragon in your hand."""
	play = Buff(SELF, "DRG_058e") * Count(FRIENDLY_HAND + DRAGON)
DRG_058e = buff(2,0)
"""Commanding"""

class DRG_064:#OK
	"""Zul'Drak Ritualist	Rare
	[x]<b>Taunt</b>
	 <b>Battlecry:</b> Summon three
	random 1-Cost minions
	for your opponent."""
	play = Summon(OPPONENT, RandomMinion(cost=3))*3

class DRG_054:#OK
	"""Big Ol' Whelp	Common
	<b>Battlecry:</b> Draw a card."""
	play = Draw(CONTROLLER)

class DRG_086:#OK :  omit discovering
	"""Chromatic Egg	Epic
	[x]<b>Battlecry:</b> Secretly <b>Discover</b>
	a Dragon to hatch into.
	<b>Deathrattle:</b> Hatch!"""
	play = HoldinHatch(CONTROLLER, RandomDragon())
	deathrattle = OpenHatch(CONTROLLER )
class DRG_086e:
	""" What's in the Egg?"""
	pass

class DRG_075:#OK
	"""Cobalt Spellkin	Rare
	<b>Battlecry:</b> Add two 1-Cost spells from your class to_your hand."""
	play = Give(CONTROLLER, RandomSpell(cost=1,card_class=Attr(FRIENDLY_HERO, GameTag.CLASS)))*2

class DRG_076:#OK
	"""Faceless Corruptor	Rare
	[x]<b>Rush</b>. <b>Battlecry:</b> Transform
	one of your minions into
	a copy of this."""
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Morph(TARGET, ExactCopy(SELF))

#### 30 ####

class DRG_082:#OK
	"""Kobold Stickyfinger	Epic
	<b>Battlecry:</b> Steal your opponent's weapon."""
	play = Steal(ENEMY_WEAPON, CONTROLLER)

class DRG_069:#OK
	"""Platebreaker	Common
	<b>Battlecry:</b> Destroy your opponent's Armor."""
	play = DestroyArmor(OPPONENT)

class DRG_242:###########################################Galakrond
	"""Shield of Galakrond	Common
	<b>Taunt</b>
	<b>Battlecry:</b> <b>Invoke</b> Galakrond."""
	#play = InvokeGarakrond(CONTROLLER)

class DRG_072:#OK
	"""Skyfin	Epic
	<b>Battlecry:</b> If you're holding a Dragon, summon 2 random Murlocs."""
	play = HOLDING_DRAGON & Summon(CONTROLLER,RandomMurloc())*2

class DRG_084:#OK
	"""Tentacled Menace	Epic
	<b>Battlecry:</b> Each player draws a card. Swap their_Costs."""
	play = TentacledMenace(CONTROLLER,OPPONENT)

class DRG_074:#OK
	"""Camouflaged Dirigible	Common
	<b>Battlecry:</b> Give your other Mechs <b>Stealth</b> until your_next turn."""
	play = Buff(FRIENDLY_MINIONS + MECH - SELF, "DRG_074e")
class DRG_074e:
	tags = {GameTag.STEALTH: True}
	events = OWN_TURN_BEGIN.on(Unstealth(OWNER), Destroy(SELF))

class DRG_079:#OK
	"""Evasive Wyrm	Common
	<b>Divine Shield</b>, <b>Rush</b>
	Can't be targeted by spells or Hero Powers."""
	update = Refresh(SELF, {GameTag.CANT_BE_TARGETED_BY_HERO_POWERS: True}), Refresh(SELF, {GameTag.CANT_BE_TARGETED_BY_SPELLS: True})

class DRG_061:#OK
	"""Gyrocopter	Common
	<b>Rush</b>
	<b>Windfury</b>"""

class DRG_099:##################################Galakrond
	"""Kronx Dragonhoof	Legendary
	[x]<b>Battlecry:</b> Draw Galakrond.
	If you're already Galakrond,
	unleash a Devastation."""  # change hero to "DRGA_BOSS_24h"?
	#powered_up = Find(EnumSelector("DRGA_BOSS_24h"))
	#play = -powered_up & Give(CONTROLLER, "DRGA_BOSS_24h")#, powered_up & RefreshHeroPower(CONTROLLER, "DRGA_BOSS_28p")

class DRG_077:#OK
	"""Utgarde Grapplesniper	Rare
	<b>Battlecry:</b> Both players draw a card. If it's a Dragon, summon it."""
	def play(self):
		target = self.controller
		draw1 = Draw(target)
		cards1 = draw1.trigger(self)
		card1 = cards1[0][0]
		if card1.type == CardType.MINION and card1.race == Race.DRAGON:
			Summon(target, card1).trigger(self)
		other = target.opponent
		draw2 = Draw(other)
		cards2 = draw2.trigger(self)
		card2 = cards2[0][0]
		if card2.type == CardType.MINION and card2.race == Race.DRAGON:
			Summon(other, card2).trigger(self)		

#### 40 ####

class DRG_310:#OK
	"""Evasive Drakonid	Common
	<b>Taunt</b>
	Can't be targeted by spells or Hero Powers."""
	update = Refresh(SELF, {GameTag.CANT_BE_TARGETED_BY_HERO_POWERS: True}), Refresh(SELF, {GameTag.CANT_BE_TARGETED_BY_SPELLS: True})

class DRG_091:#OK
	"""Shu'ma	Legendary
	At the end of your turn,
	fill your board with 1/1_Tentacles."""
	play = OWN_TURN_END.on(Summon(CONTROLLER,"DRG_091t") * 7)
class DRG_091t:
	""" Tentacles"""
	#vanilla

class DRG_213:#OK
	"""Twin Tyrant	Common
	<b>Battlecry:</b> Deal 4 damage to two random enemy minions."""
	play = Hit(RANDOM(ENEMY_MINIONS),4) * 2

class DRG_089:#OK
	"""Dragonqueen Alexstrasza	Legendary
	[x]<b>Battlecry:</b> If your deck has
	no duplicates, add 2 other
	random Dragons to your
	hand. They cost (1)."""
	powered_up = -FindDuplicates(FRIENDLY_DECK)
	play = powered_up & Give(CONTROLLER, RandomDragon()).then(Buff(Give.CARD, "DRG_089e")), powered_up & Give(CONTROLLER, RandomDragon()).then(Buff(Give.CARD, "DRG_089e"))
class DRG_089e:
	"""A Queen's Discount"""
	cost=SET(1)

class DRG_402:#OK
	"""Sathrovarr	Legendary
	<b>Battlecry:</b> Choose a friendly minion. Add a copy of it to_your hand, deck, and battlefield."""
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play= Give(CONTROLLER, Copy(TARGET)),Shuffle(CONTROLLER,Copy(TARGET)), Summon(CONTROLLER,Copy(TARGET))

