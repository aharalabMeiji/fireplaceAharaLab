from ..utils import *

#class BAR_064e:#<4> [1525] #BAR_064 is neutral
#	""" Touch of Arcane
#	You have [Spell Damage +2] for your next spell this turn. """
#	#
#	pass

#class BAR_064e2:#<4> [1525] #BAR_064 is neutral
#	""" Touch of Arcane
#	You have [Spell Damage +2] for your next spell this turn. """
#	#
#	pass

class BAR_305:#<4> [1525] ##OK
	""" Flurry (Rank 1)
	[Freeze] a random enemy minion. <i>(Upgrades when you have 5 Mana.)</i> """
	play = Freeze(RANDOM(ENEMY_MINIONS - FROZEN))
	pass

class BAR_305t:#<4> [1525] ##OK 
	""" Flurry (Rank 2)
	[Freeze] two random enemy minions. <i>(Upgradeswhen you have 10 Mana.)</i> """
	play = Freeze(RANDOM(ENEMY_MINIONS - FROZEN)) * 2
	pass

class BAR_305t2:#<4> [1525] ##OK
	""" Flurry (Rank 3)
	[Freeze] three random enemy minions. """
	play = Freeze(RANDOM(ENEMY_MINIONS - FROZEN)) * 3
	pass

class BAR_541:#<4> [1525] #OK
	""" Runed Orb
	Deal $2 damage. [Discover] a spell. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0}
	play = Hit(TARGET, 2),DISCOVER(RandomSpell())
	pass

class GetManaIfSpell(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	def do(self, source, target, amount):
		if target.type == CardType.SPELL:
			source.controller.used_mana -= amount
			log.info("Refresh %d Mana for %r"%(amount, source.controller))
			if source.controller.used_mana<0:
				source.controller.used_mana=0

class BAR_542:#<4> [1525] ##OK # if you use 'on' you may fail.
	""" Refreshing Spring Water
	Draw 2 cards.Refresh 2 Mana Crystals for each spell drawn. """
	play = Draw(CONTROLLER).then(GetManaIfSpell(Draw.CARD, 2)), Draw(CONTROLLER).then(GetManaIfSpell(Draw.CARD, 2))
	pass

class BAR_544_Action(TargetedAction):#fake heropower
	def do(self,source,target):
		controller = target
		targetList=controller.opponent.field
		targetList.append(controller.opponent.hero)
		heropower = controller.hero.power
		for tgt in targetList:
			heropower.target=tgt
			actions = heropower.get_actions("activate")
			source.game.action_start(BlockType.PLAY, heropower, 0, tgt)
			source.game.main_power(heropower, actions, tgt)
			source.game.action_end(BlockType.PLAY, heropower)

class BAR_544:#<4> [1525] ##OK
	""" Reckless Apprentice
	[Battlecry:] Fire your Hero Power at all enemies. """
	play = BAR_544_Action(CONTROLLER)
	pass

class BAR_545_Action(TargetedAction):
	TARGET = ActionArg()
	CARDS = ActionArg()
	BUFF = ActionArg()
	def do(self, source, target, cards, buff):
		player = source.controller
		for card in cards:
			if not card.id in player.starting_deck:
				Buff(card,buff).trigger(source)


class BAR_545:#<4> [1525] ##OK
	""" Arcane Luminary
	Cards that didn't start in your deck cost (2) less, but not less than (1). """
	play = BAR_545_Action(CONTROLLER, FRIENDLY_HAND,'BAR_545e')
	pass

class BAR_545e:#<4> [1525]
	""" Conjured Reduction
	Costs (2) less (but not less than 1). """
	cost = lambda self, i: max(i-2, 1)
	pass

class BAR_546:#<4> [1525] ##OK
	""" Wildfire
	Increase the damage of your Hero Power by 1. """
	play = ChangeHeroPower(CONTROLLER, 'HERO_08bp2')
	pass

class BAR_546e:#<4> [1525] #ヒロパにバフがつけられるのか？
	""" Flame On!
	Hero Power deals 1 more damage. """
	atk = 1
	pass

class BAR_547_Action(TargetedAction):
	TARGET = ActionArg()
	AMOUNT = IntArg()
	TARGETEDACTION = ActionArg()
	def do(self, source, target, amount, targetedaction):
		ActivateList = target._activate_log
		count=0
		for case in ActivateList:
			count += case.amount
		if count >= amount:
			targetedaction.trigger(source)
		pass
class BAR_547_Hand_Event(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		ActivateList = target._activate_log
		count=0
		for case in ActivateList:
			count += case.amount
		source.script_data_num_1 = count+1
		source.script_data_text_0 = str(9 - count)
		pass
class BAR_547:#<4> [1525] ##OK
	""" Mordresh Fire Eye
	[Battlecry:] If you've dealt 10 damage with your Hero Power this game, deal 10 damage to all enemies.@ <i>({0} left!)</i>@ <i>(Ready!)</i> """
	play = BAR_547_Action(CONTROLLER,10,Hit(ENEMY_CHARACTERS,10))
	class Hand:
		events = Activate(CONTROLLER, HERO_POWER).on(BAR_547_Hand_Event(CONTROLLER))
	pass


class BAR_748:#<4> [1525] ##OK
	""" Varden Dawngrasp
	[Battlecry:] [Freeze] all enemy minions. If any are already[Frozen], deal 4 damage to them instead. """
	play = FreezeOrHit(ENEMY_MINIONS, 4)
	pass

class BAR_812:#<4> [1525] ##OK
	""" Oasis Ally
	[Secret:] When a friendly minion is attacked, summon a 3/6 Water Elemental. """
	secret = Attack(ENEMY, FRIENDLY_MINIONS).on(Summon(CONTROLLER, 'CORE_CS2_033'))
	pass

class IsFrostSpell(TargetedAction):
	TARGET=ActionArg()
	TARGETEDACTION = ActionArg()
	def do(self, source, target, targetedaction):
		if target.data.referenced_tags.get(GameTag.FREEZE) or target.data.tags.get(GameTag.FREEZE):
			targetedaction.trigger(source)
		pass

class BAR_888:#<4> [1525] ###OK.
	""" Rimetongue
	After you cast a Frost spell, summon a 1/1 Elemental that [[Freeze]s]. """
	events = OWN_SPELL_PLAY.on(IsFrostSpell(Play.CARD,Summon(CONTROLLER,'BAR_888t')))
	pass

class BAR_888t:#<4> [1525] ##OK
	""" Frosted Elemental
	[Freeze] any character damaged by this minion. """
	events = Attack(SELF, ALL_CHARACTERS).on(Freeze(Attack.DEFENDER))
	pass

class WC_041:#<4> [1525] ###OK
	""" Shattering Blast
	Destroy all [Frozen] minions. """
	play = Destroy(ALL_MINIONS + FROZEN)
	pass

class WC_805_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):#
		controller = source.controller
		Give(controller, target).trigger(source)
		if target.data.referenced_tags.get(GameTag.FREEZE) or target.data.tags.get(GameTag.FREEZE):
			Summon(controller,'BAR_888t').trigger(source)
			Summon(controller,'BAR_888t').trigger(source)


class WC_805:#<4> [1525] ###OK
	""" Frostweave Dungeoneer
	[Battlecry:] Draw a spell.If it's a Frost spell,summon two 1/1___Elementals that [Freeze]. """
	play = WC_805_Action(RANDOM(FRIENDLY_DECK + SPELL))
	pass

class WC_806:#<4> [1525] ##OK
	""" Floecaster
	Costs (2) less for each [Frozen] enemy. """
	cost_mod = - Count(ENEMY_CHARACTERS+ FROZEN) * 2
	pass
