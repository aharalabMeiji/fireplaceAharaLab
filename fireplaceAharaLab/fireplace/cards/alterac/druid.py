from ..utils import *

class ALT_DRU_1:#70249
	""" Heart of the Wild (3)
	Give a minion +2/+2, then give your Beasts +1/+1."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0}
	play = Buff(TARGET, 'ALT_DRU_1e'), Buff(FRIENDLY_MINIONS + BEAST, 'ALT_DRU_1e2')
	pass
ALT_DRU_1e=buff(2,2)
ALT_DRU_1e2=buff(1,1)

class ALT_DRU_2:
	""" Pride Seeker (3/2/4)
	[Battlecry]: Your next [Choose One] card costs (2) less."""
	play = Buff(CONTROLLER, 'ALT_DRU_2e')
	pass
class ALT_DRU_2e:
	update = Refresh(FRIENDLY_HAND + CHOOSE_ONE, "ALT_DRU_2e")
	events = play(CONTROLLER, FRIENDLY + CHOOSE_ONE).then(Destroy(SELF))
ALT_DRU_2e=buff(cost=-2)

class ALT_DRU_3:
	""" Wing Commander Mulverick (4/2/5)
	[Rush]. Your minions have "Honorable Kill: Summon a 2/2 Wyvern with Rush." """
	play = Buff(FRIENDLY_MINIONS, 'ALT_DRU_3e')
	pass
class ALT_DRU_3e:
	#tags = {GameTag.HONORABLE_KILL: True}
	#honorable_kill = Summon(CONTROLLER, 'ALT_DRU_3t')
	pass
class ALT_DRU_3t:
	""" Strike Wyvern
	Rush """
	pass

class ALT_DRU_4:
	""" Clawfury Adept (2/2/3) beast
	[Battlecry]: Give all other friendly characters +1 Attack this turn. """
	play = Buff(FRIENDLY_CHARACTERS, 'ALT_DRU_4e')
	pass
class ALT_DRU_4e:
	atk = lambda self, i: i+1
	events = OWN_TURN_END.on(Destroy(SELF))

class ALT_DRU_5:###########################
	""" Pathmaker (3/3/4) 
	Battlecry: Cast the other choice from the last [Choose One] spell you've cast.  """
	#
	pass

class DrawLowestCost(TargetedAction):
	TARGET = ActionArg()
	def do(self,source, target):
		controller = target
		deck = controller.deck
		lowest = None
		for card in deck:
			if lowest == None:
				lowest = [card]
			elif lowest[0].cost > card.cost:
				lowest = [card]
			elif lewest[0].cost == card.cost:
				lowest.append(card)
		card = random.choice(lowest)
		controller.game.trigger(controller, [Give(controller,card)],event_args=None)
	pass
class DrawHighestCost(TargetedAction):
	TARGET = ActionArg()
	def do(self,source, target):
		controller = target
		deck = controller.deck
		lowest = None
		for card in deck:
			if lowest == None:
				lowest = [card]
			elif lowest[0].cost < card.cost:
				lowest = [card]
			elif lewest[0].cost == card.cost:
				lowest.append(card)
		card = random.choice(lowest)
		controller.game.trigger(controller, [Give(controller,card)],event_args=None)
	pass
class ALT_DRU_6:
	""" Capture Coldtooth Mine (2)
	[Choose One] - Draw your lowest Cost card; or Draw your highest Cost card. """
	choose = ("ALT_DRU_6a", "ALT_DRU_6b")
	play = ChooseBoth(CONTROLLER) & (DrawLowestCost(CONTROLLER), DrawLowestCost(CONTROLLER))
	pass
class ALT_DRU_6a: ## More Supplies
	play = DrawLowestCost(CONTROLLER)
	pass
class ALT_DRU_6b: ## More Resources
	play = DrawLowestCost(CONTROLLER)
	pass

class ALT_DRU_7:#
	""" Frostwolf Kennels (3) Lasts
	At the end of your turn, summon a 2/2 Wolf with Stealth. Lasts 3 turns. """
	tags={GameTag.SIDEQUEST:True, }
	events = [
		OWN_TURN_END.on(Summon(CONTROLLER, 'ALT_DRU_7t')),
		OWN_TURN_BEGIN.on(SidequestCounter(SELF, 3, [Destroy(SELF)])),
		]		
	pass
class ALT_DRU_7t:
	""" Frostwolf Cub (2/2/2) """
	pass

class ALT_DRU_8_Count(LazyNum):
	"""
	Lazily count the matches in a selector
	"""
	def __init__(self, selector):
		super().__init__()
		self.selector = selector

	def __repr__(self):
		return "%s(%r)" % (self.__class__.__name__, self.selector)

	def evaluate(self, source):
		###change this part(What is 'source'?)
		return self.num(len(self.get_entities(source)))

class ALT_DRU_8: ##################   this game
	""" Frostsaber Matriarch (7/4/5) beast
	[Taunt]. Costs (1) less for each Beast you've summoned this game. """
	cost_mod = -ALT_DRU_8_Count(CONTROLLER)
	pass

class ALT_DRU_9:
	""" Dire Frostwolf (4/4/4) beast
	[Stealth] [Deathrattle]: Summon a 2/2 Wolf with Stealth. """
	deathrattle = Summon(CONTROLLER, 'ALT_DRU_7t')
	pass

class ALT_DRU_10:#################
	""" Wildheart Guff ( 5/*/5) Hero
	Battlecry: Set your maximum Mana to 20. Gain a Mana Crystal. Draw a card."""
	def play(self):
		controller = self.controller
		difference = 20 - controller.max_mana
		controller.max_resources = 20
		controller.max_mana += difference
		controller.used_mana += (difference-1)
		Draw(controller).trigger(controller)
	pass


