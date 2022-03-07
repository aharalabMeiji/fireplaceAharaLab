from ..utils import *

#stormwind updates

#Stormwind_Updates=[
#'DED_006','DED_006e2','DED_514e','DED_521','DED_523','DED_523e','DED_524','DED_525',
#'DED_007','DED_008',,'DED_009',,'DED_009e',
#'DED_515','DED_516','DED_517','DED_517t',
#'DED_001','DED_001a','DED_001at','DED_001b','DED_001bt','DED_001c','DED_002','DED_002e','DED_003',
#'DED_518','DED_519','DED_527','DED_527e',
#]

## neutral

class DED_006:# <12>[1578] ###OK
	""" Mr. Smite
	Your Pirates have [Charge]. """
	play = Buff(FRIENDLY_MINIONS + PIRATE, 'DED_006e2')
	pass

DED_006e2 = buff(charge=True)# <12>[1578]
""" Charge
{0} grants [Charge]. """
#

class DED_514e:# <12>[1578] -> <6>[1578]
	""" Copycat
	Add a copy of the next card your opponent plays to your hand. """
	#
	pass

class DED_521:# <12>[1578] ####OK
	""" Maddest Bomber
	[Battlecry:] Deal 12 damage randomly split among all other characters. """
	play = Hit(RANDOM(ALL_CHARACTERS - SELF),1) * 12
	pass

class DED_523:# <12>[1578] ###OK
	""" Golakka Glutton
	[Battlecry:] Destroy a Beast and gain +1/+1. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.BEAST}
	play = (Destroy(TARGET), Buff(SELF, 'DED_523e'))
	pass

DED_523e = buff(1,1)# <12>[1578]
""" Stuffed Belly
+1/+1. """
#

class DED_524:# <12>[1578]###OK
	""" Multicaster
	[Battlecry:] Draw a card for each different spell school_you've cast this game. """
	def play(self):
		play_log = self.controller.play_log
		school_count=[0] * 6
		for card in play_log:
			if card.type == CardType.SPELL:
				if card.spell_school == SpellSchool.ARCANE:
					school_count[0] = 1
				if card.spell_school == SpellSchool.FIRE:
					school_count[1] = 1
				if card.spell_school == SpellSchool.FROST:
					school_count[2] = 1
				if card.spell_school == SpellSchool.NATURE:
					school_count[3] = 1
				if card.spell_school == SpellSchool.HOLY:
					school_count[4] = 1
				if card.spell_school == SpellSchool.SHADOW:
					school_count[5] = 1
			pass
		pass
		count = sum(school_count)
		for i in range(count):
			Draw(self.controller).trigger(self.controller)
	pass

class DED_525Choice(Choice):
	def choose(self, card):
		self.source._sidequest_counter_ += 1
		if self.source._sidequest_counter_>=5:
			self.next_choice=None
		else:
			self.next_choice=self
		self.callback = [Hit(card, 2)]
		super().choose(card)
		self.cards = self.player.opponent.field


class DED_525:# <12>[1578] #### maybe success
	""" Goliath, Sneed's Masterpiece
	[Battlecry:] Fire five rockets at enemy minions that deal 2 damage each. <i>(You pick the targets!)</i> """
	play = DED_525Choice(CONTROLLER, ENEMY_MINIONS)
	#play = GenericChoiceFromEnemyMinions(CONTROLLER, [Hit(GenericChoiceFromEnemyMinions.CARD, 2)]) * 5
	pass


## hunter

class DED_007:# <3>[1578] ###OK
	""" Defias Blastfisher
	[Battlecry:] Deal 2 damage to a random enemy. Repeat for each of your Beasts. """
	play = Hit(RANDOM(ENEMY_CHARACTERS),2), Hit(RANDOM(ENEMY_CHARACTERS),2) * Count(FRIENDLY_MINIONS + BEAST)
	pass

class DED_008:# <3>[1578] ###OK
	""" Monstrous Parrot
	[Battlecry:] Repeat the last friendly [Deathrattle] that triggered. """
	def play(self):
		death_log = self.controller.death_log
		deathrattle = None
		for card in death_log:
			if card.has_deathrattle:
				deathrattle = card.deathrattles[-1]
				if isinstance(deathrattle,(list, tuple)):
					deathrattle = deathrattle[0]
		if deathrattle != None:
			deathrattle.trigger(self)
		pass
	pass

class DED_009:# <3>[1578] ###OK
	""" Doggie Biscuit
	[Tradeable]Give a minion +2/+3.After you [Trade] this, give a friendly minion [Rush]. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0}
	play = Buff(TARGET, 'DED_009e')
	#trade = Buff(RANDOM(FRIENDLY_MINION),'DED_001at')-> game.trade_card()
	pass

DED_009e = buff(2,3)# <3>[1578]
""" Good Doggie!
+2/+3. """

## mage

class DED_515:# <4>[1578] ###OK
	""" Grey Sage Parrot
	[Battlecry:] Repeat the last spell you've cast that costs (5) or more. """
	def play(self):
		controller = self.controller
		play_log = controller.play_log
		spell_target = None
		spell_action = None
		for card in play_log:
			if card.type == CardType.SPELL and card.cost>=5:
				if card.requires_target():
					spell_target = random.choice(card.targets)
				spell_action = Battlecry(card, spell_target)
		if spell_action != None:
			spell_action.trigger(controller)
		pass
	pass

class DED_516:# <4>[1578] ###OK
	""" Deepwater Evoker
	[Battlecry:] Draw a spell. Gain Armor equal to its Cost. """
	def play(self):
		new_card = Give(self.controller, RandomSpell()).trigger(self.controller)
		new_card_cost = new_card[0][0].cost
		GainArmor(self.controller.hero, new_card_cost).trigger(self.controller)
	pass

class DED_517:# <4>[1578] ###OK
	""" Arcane Overflow
	Deal $8 damage to an enemy minion. Summon a Remnant with stats equal to the excess damage. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0}
	def play(self):
		target = self.target
		excess = 8 + self.controller.spellpower - target.health
		Hit(target, target.health).trigger(self.controller)
		new_card = Summon(self.controller, 'DED_517t').trigger(self.controller)
		if isinstance(new_card,list) and len(new_card)>0:
			new_card = new_card[0]
		if isinstance(new_card,list) and len(new_card)>0:
			new_card = new_card[0]
		#assert isinstance(new_card, Card)
		if excess>0:
			new_card.atk = excess
			new_card.max_health = excess 
	pass

class DED_517t:# <4>[1578]
	""" Arcane Remnant
	 """
	#
	pass

## druid

class DED_001:# <2>[1578] ###OK
	""" Druid of the Reef
	[Choose One - ]Transform into a 3/1 Shark with [Rush]; or a 1/3 Turtle with [Taunt]. """
	choose = ("DED_001a", "DED_001b")
	play = ChooseBoth(SELF) & (
		Summon(CONTROLLER, "DED_001c")
	)	

class DED_001a:# <2>[1578]
	""" Shark Form
	[Rush] """
	play = Morph(SELF, 'DED_001at')
	pass

class DED_001at:# <2>[1578]
	""" Druid of the Reef
	[Rush] """
	pass

class DED_001b:# <2>[1578]
	""" Sea Turtle Form
	[Taunt] """
	play = Morph(SELF, 'DED_001bt')
	pass

class DED_001bt:# <2>[1578]
	""" Druid of the Reef
	[Taunt] """
	#

class DED_001c:# <2>[1578]
	""" Druid of the Reef
	[Rush][Taunt] """
	#
	pass

class DED_002:# <2>[1578]####OK
	""" Moonlit Guidance
	[Discover] a copy of a card in your deck.If you play it this turn,draw the original. """
	play = Choice(CONTROLLER, RANDOM(FRIENDLY_DECK)*3).then(
		Give(CONTROLLER, Choice.CARD), Buff(Choice.CARD, 'DED_002e')
		)
	pass

class DED_002e:# <2>[1578]####OK
	""" Path of the Moon
	If played this turn, draw the original copy. """
	# do - shi yo -
	events = [
		Play(CONTROLLER, FRIENDLY+OWNER).on(Destroy(SELF), Give(CONTROLLER, ExactCopy(OWNER))),
		OWN_TURN_END.on(Destroy(SELF), Shuffle(CONTROLLER, ExactCopy(OWNER))),
		]
	pass


class DED_003:# <2>[1578]### it doesn't work for CORE_EX1_178 (Ancient of War)
	""" Jerry Rig Carpenter
	[Battlecry:] Draw a [Choose One] spell and split it. """
	def play(self):
		controller = self.controller
		choose_one_cards = []
		for card in controller.deck:
			if hasattr(card, 'has_choose_one') and card.has_choose_one and card.id != 'CORE_EX1_178':
				card_id = card.id
				# DED_001, SW_422, SCH_612, DMF_061, CORE_EX1_164, CORE_OG_047,CORE_EX1_160, CORE_EX1_573, CORE_EX1_165
				if card_id[:5]=='CORE_':
					card_id = card_id[5:]
				nameA = card_id + 'a'
				nameB = card_id + 'b'
				card.zone = Zone.GRAVEYARD
				Give(controller, nameA).trigger(controller)
				Give(controller, nameB).trigger(controller)
				break;
		pass
	pass

## warrior

class DED_518:# <10>[1578] ###OK
	""" Man the Cannons
	Deal $3 damage to a minion and $1 damage to all other minions. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0}
	play = Hit(TARGET,3), Hit(ALL_MINIONS - TARGET, 1)
	#
	pass

class DED_519:# <10>[1578] ###OK
	""" Defias Cannoneer
	After your hero attacks,deal 2 damage to a random enemy twice. """
	events = Attack(FRIENDLY_HERO).on(Hit(RANDOM(ENEMY_CHARACTERS),2) * 2)
	pass

class DED_527:# <10>[1578] ###OK
	""" Blacksmithing Hammer
	[Tradeable]After you [Trade] this, _gain +2 Durability. """
	# weapon 
	#trade = Buff(SELF, 'DED_527e')
	pass

DED_527e = buff(0,2)# <10>[1578]
""" Blacksmithing
+2 Durability. """

