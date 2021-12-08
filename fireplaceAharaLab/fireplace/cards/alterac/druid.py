from ..utils import *


#Alteric_Druid=['AV_205','AV_210','AV_210e','AV_211','AV_211t','AV_291','AV_292','AV_292e','AV_292e2','AV_293','AV_293e','AV_294','AV_294e','AV_293t','AV_295','AV_295a','AV_295b','AV_296','AV_296e','AV_296e2','AV_360',   ]

class AV_205:#################
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

class AV_210:###########################
	""" Pathmaker (3/3/4) 
	Battlecry: Cast the other choice from the last [Choose One] spell you've cast.  """
	#
	pass
class AV_210e:
	""" Path Tracker
	Tracking Sub-Spell. """
	pass

class AV_211:
	""" Dire Frostwolf (4/4/4) beast
	[Stealth] [Deathrattle]: Summon a 2/2 Wolf with Stealth. """
	deathrattle = Summon(CONTROLLER, 'AV_211t')
	pass
class AV_211t:
	""" Frostwolf Cub (2/2/2) """
	pass

class AV_291_Count(LazyNum):
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
class AV_291: ##################   this game
	""" Frostsaber Matriarch (7/4/5) beast
	[Taunt]. Costs (1) less for each Beast you've summoned this game. """
	cost_mod = -AV_291_Count(CONTROLLER)
	pass

class AV_292:#70249
	""" Heart of the Wild (3)
	Give a minion +2/+2, then give your Beasts +1/+1."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0}
	play = Buff(TARGET, 'ALT_DRU_1e'), Buff(FRIENDLY_MINIONS + BEAST, 'ALT_DRU_1e2')
	pass
AV_292e=buff(2,2)
AV_292e2=buff(1,1)

class AV_293:
	""" Wing Commander Mulverick (4/2/5)
	[Rush]. Your minions have "Honorable Kill: Summon a 2/2 Wyvern with Rush." """
	play = Buff(FRIENDLY_MINIONS, 'AV_293e')
	pass
class AV_293e:
	#tags = {GameTag.HONORABLE_KILL: True}
	#honorable_kill = Summon(CONTROLLER, 'AV_293t')
	pass
class AV_293t:
	""" Strike Wyvern
	Rush """
	pass

class AV_294:
	""" Clawfury Adept (2/2/3) beast
	[Battlecry]: Give all other friendly characters +1 Attack this turn. """
	play = Buff(FRIENDLY_CHARACTERS, 'AV_294e')
	pass
class AV_294e:
	atk = lambda self, i: i+1
	events = OWN_TURN_END.on(Destroy(SELF))

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
class AV_295:
	""" Capture Coldtooth Mine (2)
	[Choose One] - Draw your lowest Cost card; or Draw your highest Cost card. """
	choose = ("AV_295a", "AV_295b")
	play = ChooseBoth(CONTROLLER) & (DrawLowestCost(CONTROLLER), DrawLowestCost(CONTROLLER))
	pass
class AV_295a: ## More Supplies
	play = DrawLowestCost(CONTROLLER)
	pass
class AV_295b: ## More Resources
	play = DrawLowestCost(CONTROLLER)
	pass

class AV_296:
	""" Pride Seeker (3/2/4)
	[Battlecry]: Your next [Choose One] card costs (2) less."""
	play = Buff(CONTROLLER, 'AV_296e')
	pass
class AV_296e:
	update = Refresh(FRIENDLY_HAND + CHOOSE_ONE, "AV_296e2")
	events = Play(CONTROLLER, FRIENDLY + CHOOSE_ONE).then(Destroy(SELF))
AV_296e2=buff(cost=-2)

class AV_360:#
	""" Frostwolf Kennels (3) Lasts
	At the end of your turn, summon a 2/2 Wolf with Stealth. Lasts 3 turns. """
	tags={GameTag.SIDEQUEST:True, }
	events = [
		OWN_TURN_END.on(Summon(CONTROLLER, 'AV_211t')),
		OWN_TURN_BEGIN.on(SidequestCounter(SELF, 3, [Destroy(SELF)])),
		]		
	pass


