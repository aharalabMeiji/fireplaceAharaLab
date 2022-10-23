from ..utils import *

Alterac_Druid=[]

Alterac_Wildheart_Guff=True  ###
Alterac_Pathmaker=True  ###
Alterac_Dire_Frostwolf=True  ###
Alterac_Frostsaber_Matriarch=True  ###
Alterac_Heart_of_the_Wild=True  ###
Alterac_Wing_Commander_Mulverick=True  ###
Alterac_Clawfury_Adept=True  ###
Alterac_Capture_Coldtooth_Mine=True  ###
Alterac_Pride_Seeker=True  ###
Alterac_Frostwolf_Kennels=True  ###
Alterac_Boomkin=True  ###
Alterac_Raid_Negotiator=True  ###
Alterac_Scale_of_Onyxia=True  ###

##########################################

if Alterac_Wildheart_Guff:# 
	Alterac_Druid+=['AV_205']
	Alterac_Druid+=['AV_205a']
	Alterac_Druid+=['AV_205p']
	Alterac_Druid+=['AV_205pb']
class AV_205:##
	""" Wildheart Guff ( 5/*/5) Hero
	Battlecry: Set your maximum Mana to 20. Gain a Mana Crystal. Draw a card."""
	def play(self):
		controller = self.controller
		GainArmor(self, self.armor)
		controller.max_resources = 20
		Draw(controller).trigger(controller)
		#controller.summon('AV_205p')## Hero power いらないらしい。
	pass
class AV_205a:
	""" Ice Blossom
	Gain a Mana Crystal."""
	play = GainMana(CONTROLLER, 1)
	pass
class AV_205p:
	""" Nurture (hero power)
	[Hero Power][Choose One -] Draw a card;or Gain a Mana Crystal."""
	choose=('AV_205a', 'AV_205pb')
	play = ChooseBoth(SELF) & (GainMana(CONTROLLER, 1), Draw(CONTROLLER))
	pass
class AV_205pb:
	""" Valley Root
	Draw a card."""
	play = Draw(CONTROLLER)
	pass




if Alterac_Pathmaker:# wait checkin
	Alterac_Druid+=['AV_210']
	Alterac_Druid+=['AV_210e']
class AV_210_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		answer=controller.last_choose_one
		if answer!=[]:
			card = answer[0]
			card2 = answer[1]
			choice = card.choose_cards
			if len(choice)>=2:
				if card2.id==choice[0].id:
					card = choice[1]
					CastSpell(card).trigger(source)
				else:
					card = choice[0]
					CastSpell(card).trigger(source)
		pass
class AV_210:##
	""" Pathmaker (3/3/4) 
	Battlecry: Cast the other choice from the last [Choose One] spell you've cast.  """
	play = AV_210_Action(CONTROLLER)
	pass
class AV_210e:
	""" Path Tracker
	Tracking Sub-Spell. """
	pass




if Alterac_Dire_Frostwolf:# 
	Alterac_Druid+=['AV_211','AV_211t']
class AV_211:
	""" Dire Frostwolf (4/4/4) beast
	[Stealth] [Deathrattle]: Summon a 2/2 Wolf with Stealth. """
	deathrattle = Summon(CONTROLLER, 'AV_211t')
	pass
class AV_211t:
	""" Frostwolf Cub (2/2/2) """
	pass



if Alterac_Frostsaber_Matriarch:# 
	Alterac_Druid+=['AV_291']
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
		controller = source.controller
		cardlist = controller.summon_log
		count = 0
		for card in cardlist:
			if hasattr(card, 'race') and card.race==Race.BEAST:
				count += 1
		if Config.LOGINFO:
			print("%s costs %d less "%(source, count))
		return self.num(count)
class AV_291: #
	""" Frostsaber Matriarch (7/4/5) beast
	[Taunt]. Costs (1) less for each Beast you've summoned this game. """
	cost_mod = -AV_291_Count(SELF)
	pass




if Alterac_Heart_of_the_Wild:# 
	Alterac_Druid+=['AV_292']
	Alterac_Druid+=['AV_292e']
	Alterac_Druid+=['AV_292e2']
class AV_292:#70249
	""" Heart of the Wild (3)
	Give a minion +2/+2, then give your Beasts +1/+1."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0}
	play = Buff(TARGET, 'AV_292e'), Buff(FRIENDLY_MINIONS + BEAST, 'AV_292e2')
	pass
AV_292e=buff(2,2)
AV_292e2=buff(1,1)




if Alterac_Wing_Commander_Mulverick:# 
	Alterac_Druid+=['AV_293']
	Alterac_Druid+=['AV_293e']
	Alterac_Druid+=['AV_293t']
class AV_293:
	""" Wing Commander Mulverick (4/2/5)
	[Rush]. Your minions have "Honorable Kill: Summon a 2/2 Wyvern with Rush." """
	play = Buff(FRIENDLY_MINIONS, 'AV_293e')
	pass
class AV_293e:
	#tags = {GameTag.HONORABLEKILL: True} #exists
	honorable_kill = Summon(CONTROLLER, 'AV_293t')
	pass
class AV_293t:
	""" Strike Wyvern
	Rush """
	pass




if Alterac_Clawfury_Adept:# 
	Alterac_Druid+=['AV_294']
	Alterac_Druid+=['AV_294e']
class AV_294:
	""" Clawfury Adept (2/2/3) beast
	[Battlecry]: Give all other friendly characters +1 Attack this turn. """
	play = Buff(FRIENDLY_CHARACTERS - SELF, 'AV_294e')
	pass
class AV_294e:#ONE_TURN_EFFECT
	tags = {GameTag.ATK:1,}
	events = OWN_TURN_END.on(Destroy(SELF))




if Alterac_Capture_Coldtooth_Mine:# 
	Alterac_Druid+=['AV_295']
	Alterac_Druid+=['AV_295a']
	Alterac_Druid+=['AV_295b']
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
			elif lowest[0].cost == card.cost:
				lowest.append(card)
		if lowest!=None and len(lowest)>0:
			card = random.choice(lowest)
			controller.game.trigger(controller, [Give(controller,card)],event_args=None)
	pass
class DrawHighestCost(TargetedAction):
	TARGET = ActionArg()
	def do(self,source, target):
		controller = target
		deck = controller.deck
		highest = None
		for card in deck:
			if highest == None:
				highest = [card]
			elif highest[0].cost < card.cost:
				highest = [card]
			elif highest[0].cost == card.cost:
				highest.append(card)
		if highest!=None and len(highest)>0:
			card = random.choice(highest)
			controller.game.trigger(controller, [Give(controller,card)],event_args=None)
	pass
class AV_295:
	""" Capture Coldtooth Mine (2)
	[Choose One] - Draw your lowest Cost card; or Draw your highest Cost card. """
	choose = ("AV_295a", "AV_295b")
	play = ChooseBoth(SELF) & (DrawLowestCost(CONTROLLER), DrawHighestCost(CONTROLLER))
	pass
class AV_295a: ## More Supplies
	play = DrawLowestCost(CONTROLLER)
	pass
class AV_295b: ## More Resources
	play = DrawHighestCost(CONTROLLER)
	pass




if Alterac_Pride_Seeker:# 
	Alterac_Druid+=['AV_296']
	Alterac_Druid+=['AV_296e']
	Alterac_Druid+=['AV_296e2']
class AV_296:
	""" Pride Seeker (3/2/4)
	[Battlecry]: Your next [Choose One] card costs (2) less."""
	play = Buff(CONTROLLER, 'AV_296e')
	pass
class AV_296e:
	update = Refresh(FRIENDLY_HAND + CHOOSE_ONE, buff= "AV_296e2")
	events = Play(CONTROLLER, FRIENDLY + CHOOSE_ONE).on(Destroy(SELF))
AV_296e2=buff(cost=-2)




if Alterac_Frostwolf_Kennels:# 
	Alterac_Druid+=['AV_360']
class AV_360:#
	""" Frostwolf Kennels (3) Lasts
	At the end of your turn, summon a 2/2 Wolf with Stealth. Lasts 3 turns. """
	tags={GameTag.SIDEQUEST:True, }
	events = [
		OWN_TURN_END.on(Summon(CONTROLLER, 'AV_211t')),
		OWN_TURN_BEGIN.on(SidequestCounter(SELF, 3, [Destroy(SELF)])),
		]		
	pass




if Alterac_Boomkin:# 
	Alterac_Druid+=['ONY_018']
	Alterac_Druid+=['ONY_018t']
	Alterac_Druid+=['ONY_018t2']
class ONY_018:# <2>[1626]
	""" Boomkin
	[Choose One - ]Restore8 Health to your hero; or Deal 4 damage. """
	choose=('ONY_018t','ONY_018t2')
	play = ChooseBoth(SELF) & (Heal(FRIENDLY_HERO, 8), Hit(FRIENDLY_HERO, 4))
	pass

class ONY_018t:# <2>[1626]
	""" Eyes of the Moon
	Restore 8 Health to your hero. """
	play = Heal(FRIENDLY_HERO, 8)
	pass

class ONY_018t2:# <2>[1626]
	""" Heart of the Sun
	Deal 4 damage. """
	play = Hit(FRIENDLY_HERO, 4)
	pass




if Alterac_Raid_Negotiator:# 
	Alterac_Druid+=['ONY_019']
	Alterac_Druid+=['ONY_019e']
class ONY_019_Discover(GenericChoice):##
	def choose(self, card):
		super().choose(card)
		new_card = self.source.controller.hand[-1]
		Buff(new_card,'ONY_019e').trigger(self.source.controller)
		pass

class ONY_019:# <2>[1626]
	""" Raid Negotiator
	[Battlecry:] [Discover] a [Choose One] card. It has both effects combined. """
	play = ONY_019_Discover(CONTROLLER, RandomCollectible(has_choose_one=True)*3)
	pass

class ONY_019e:
	#update = Refresh(OWNER, {GameTag.CHOOSE_BOTH:True})
	#play = SetTag(OWNER, (GameTag.CHOOSE_BOTH,))
	def apply(self, target):
		self.owner.choose_both=True
		pass
	events = Play(CONTROLLER, OWNER).after(Destroy(SELF))
#ONY_019e=buff(choose_both=True)# <2>[1626]
""" Decisive
Your next [Choose One] card is combined. """




if Alterac_Scale_of_Onyxia:# 
	Alterac_Druid+=['ONY_021']
class ONY_021:# <2>[1626]
	""" Scale of Onyxia
	Fill your board with 2/1 Whelps with [Rush]. """
	play = Summon(CONTROLLER, 'ONY_001t') * 7
	pass

##################################