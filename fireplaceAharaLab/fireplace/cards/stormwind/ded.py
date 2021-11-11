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
	play = Hit(RANDOM(ALL_CHARACTERS),1) * 12
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

class DED_524:# <12>[1578]
	""" Multicaster
	[Battlecry:] Draw a card for each different spell school_you've cast this game. """
	def play(self):
		play_log = self.controller.play_log
		school_count=[0] * 6
		for card in play_log:
			if card.type == CardType.SPELL:
				if card.spell_school == CardSchool.ARCANE:
					school_count[0] = 1
				if card.spell_school == CardSchool.FIRE:
					school_count[1] = 1
				if card.spell_school == CardSchool.FROST:
					school_count[2] = 1
				if card.spell_school == CardSchool.NATURE:
					school_count[3] = 1
				if card.spell_school == CardSchool.HOLY:
					school_count[4] = 1
				if card.spell_school == CardSchool.SHADOW:
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

class DED_007:# <3>[1578]
	""" Defias Blastfisher
	[Battlecry:] Deal 2 damage to a random enemy. Repeat for each of your Beasts. """
	play = Hit(RANDOM(ENEMY_MINIONS),2), Hit(RANDOM(ENEMY_MINIONS),2) * Count(FRIENDLY_MINIONS + BEAST)
	pass

class DED_008:# <3>[1578]
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
			deathrattle.trigger(self.controller)
		pass
	pass

class DED_009:# <3>[1578]
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

class DED_515:# <4>[1578]
	""" Grey Sage Parrot
	[Battlecry:] Repeat the last spell you've cast that costs (5) or more. """
	def play(self):
		controller = self.controller
		play_log = controller.play_log
		spell_target = None
		spell_action = None
		for card in play_log:
			if card.type == CardType.SPELL and card.cost>=5:
				if card.require_target():
					spell_target = random.choice(card.targets)
				spell_action = Play(card, spell_target, None, None)
		if spell_action != None:
			spell_action.trigger(controller)
		pass
	pass

class DED_516:# <4>[1578]
	""" Deepwater Evoker
	[Battlecry:] Draw a spell. Gain Armor equal to its Cost. """
	play = Give(CONTROLLER, RANDOM(FRIENDLY_DECK + SPELL)).on(GainArmor(FRIENDLY_HERO, COST(Give.CARD)))
	pass

class DED_517:# <4>[1578]
	""" Arcane Overflow
	Deal $8 damage to an enemy minion. Summon a Remnant with stats equal to the excess damage. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0}
	def play(self):
		target = self.target
		excess = 8-target.health
		Hit(target, target.health).trigger(self.controller)
		new_card = Summon(self.controller, 'DED_517t').trigger(self.controller)
		if isinstance(new_card,list) and len(new_card)>0:
			new_card - new_card[0]
		if isinstance(new_card,list) and len(new_card)>0:
			new_card - new_card[0]
		assert isinstance(new_card, Card)
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

class DED_001:# <2>[1578]
	""" Druid of the Reef
	[Choose One - ]Transform into a 3/1 Shark with [Rush]; or a 1/3 Turtle with [Taunt]. """
	choose = ("DED_001a", "DED_001b")
	play = ChooseBoth(CONTROLLER) & (
		Summon(CONTROLLER, "DED_001c")
	)	

class DED_001a:# <2>[1578]
	""" Shark Form
	[Rush] """
	play = Buff(SELF, 'DED_001at')
	pass

DED_001at = buff(rush=True)# <2>[1578]
""" Druid of the Reef
[Rush] """

class DED_001b:# <2>[1578]
	""" Sea Turtle Form
	[Taunt] """
	play = Buff(SELF, 'DED_001bt')
	pass

DED_001bt = buff(taunt=True)# <2>[1578]
""" Druid of the Reef
[Taunt] """
#

class DED_001c:# <2>[1578]
	""" Druid of the Reef
	[Rush][Taunt] """
	#
	pass

class DED_002:# <2>[1578]###########################################
	""" Moonlit Guidance
	[Discover] a copy of a card in your deck.If you play it this turn,draw the original. """
	play = Choice(CONTROLLER, RANDOM(FRIENDLY_DECK))
	play.callback = [Give(CONTROLLER, ExactCopy(Choice.CARD)).then( Buff(Give.CARD, 'DED_002e'))]
	pass

class DED_002e:# <2>[1578]##########################################
	""" Path of the Moon
	If played this turn, draw the original copy. """
	# do - shi yo -
	pass

class DED_003:# <2>[1578]###########################################
	""" Jerry Rig Carpenter
	[Battlecry:] Draw a [Choose One] spell and split it. """
	play = Give(CONTROLLER, RandomMinion(has_choose_one=True))#not be splitted
	pass

## warrior

class DED_518:# <10>[1578]
	""" Man the Cannons
	Deal $3 damage to a minion and $1 damage to all other minions. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0}
	play = Hit(TARGET,3), Hit(ALL_MINIONS - TARGET, 1)
	#
	pass

class DED_519:# <10>[1578]
	""" Defias Cannoneer
	After your hero attacks,deal 2 damage to a random enemy twice. """
	events = Attack(FRIENDLY_HERO).after(Hit(RANDOM(ENEMY_MINIONS),2) * 2)
	pass

class DED_527:# <10>[1578]
	""" Blacksmithing Hammer
	[Tradeable]After you [Trade] this,_gain +2 Durability. """
	# weapon 
	#trade = Buff(SELF, 'DED_527e')
	pass

DED_527e = buff(0,2)# <10>[1578]
""" Blacksmithing
+2 Durability. """

