from ..utils import *

Alterac_Mage=[]

Alterac_Shivering_Sorceress=True  ###
Alterac_Amplified_Snowflurry=True  ###
Alterac_Arcane_Brilliance=True  ###
Alterac_Magister_Dawngrasp=True  ###
Alterac_Siphon_Mana=True  ###
Alterac_Mass_Polymorph=True  ###
Alterac_Build_a_Snowman=True  ###
Alterac_Rune_of_the_Archmage=True  ###
Alterac_Balinda_Stonehearth=True  ###
Alterac_Iceblood_Tower=True  ###
Alterac_Deep_Breath=True  ###
Alterac_Haleh,_Matron_Protectorate=True  ###
Alterac_Drakefire_Amulet=True  ###

################################


if Alterac_Shivering_Sorceress:# 
	Alterac_Mage+=['AV_114']
	Alterac_Mage+=['AV_114e']
class AV_114_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		highestcost=[]
		for card in target.hand:
			if len(highestcost)==0:
				highestcost = [card]
			elif highestcost[0].cost < card.cost:
				highestcost = [card]
			elif highestcost[0].cost == card.cost:
				highestcost.append(card)
		for card in highestcost:
			target.game.trigger(target, [Buff(card, 'AV_114e')], event_args=None)
		pass
	pass
class AV_114:
	""" Shivering Sorceress (1/2/2)
	Battlecry: Reduce the Cost of the highest Cost spell in your hand by (1).
	"""
	play = AV_114_Action(CONTROLLER)
	pass
AV_114e=buff(cost=-1)




if Alterac_Amplified_Snowflurry:# 
	Alterac_Mage+=['AV_115']
	Alterac_Mage+=['AV_115e5']
class AV_115:
	""" Amplified Snowflurry (2/2/3)
	Battlecry: Your next Hero Power costs (0) and Freezes the target.
	"""
	play = Buff(CONTROLLER, 'AV_115e5')
	pass
class AV_115e5:
	update = Refresh(FRIENDLY_HERO_POWER, {GameTag.COST:SET(0)})
	events = Activate(CONTROLLER, HERO_POWER).on(Freeze(Activate.TARGET), Destroy(SELF))




if Alterac_Arcane_Brilliance:# 
	Alterac_Mage+=['AV_116']
class AV_116_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		cardlist = []
		for card in target.deck:
			if card.cost >6:
				cardlist.append(card)
		if len(cardlist)>0:
			card = random.choice(cardlist)
			target.game.trigger(target, [Give(target, card)],	event_args=None)
			pass
		pass
	pass
class AV_116:
	""" Arcane Brilliance (4) Arcane
	Add a copy of a 7, 8, 9, and 10-Cost spell in your deck to your hand.
	"""
	play = AV_116_Action(CONTROLLER)
	pass




if Alterac_Magister_Dawngrasp:# 
	Alterac_Mage+=['AV_200']
	Alterac_Mage+=['AV_200p2']
class AV_200:
	""" Magister Dawngrasp (8/*/5) Hero
	Battlecry: Recast a spell from each spell school you've cast this game.
	"""
	def play(self):
		for school in [SpellSchool.ARCANE, SpellSchool.NATURE, SpellSchool.FEL, SpellSchool.FIRE, SpellSchool.FROST, SpellSchool.HOLY, SpellSchool.SHADOW]:
			cards = []
			for log in self.controller.play_log:
				if log.type==CardType.SPELL and log.spell_school==school:
					cards.append(log)
			if cards != []:
				card = random.choice(cards)
				CastSpell(card).trigger(self.controller)
			pass
		pass
		#ChangeHero(self).trigger(controller)
	pass
class AV_200p2:
	""" >Arcane Burst (Hero power)
	[x]<b>Hero Power</b> Deal $@ damage. 
	<b>Honorable Kill:</b> Gain +2 damage."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, }
	activate = HitScriptDataNum1(SELF, TARGET)
	honorable_kill = AddScriptDataNum1(SELF, 2)
	pass




if Alterac_Siphon_Mana:# 
	Alterac_Mage+=['AV_212']
	Alterac_Mage+=['AV_212e']
class AV_212:
	""" Siphon Mana (2) Arcane
	Deal 2 damage. Honorable Kill: Reduce the Cost of spells in your hand by (1).
	"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0  }
	play = Hit(TARGET, 2)
	honorable_kill = Buff(FRIENDLY_HAND, 'AV_212e')
	pass
AV_212e=buff(cost=-1)




if Alterac_Mass_Polymorph:# 
	Alterac_Mage+=['AV_218','AV_218t']
class AV_218:
	""" Mass Polymorph (7) Arcane
	Transform all minions into 1/1 Sheep."""
	play = Morph(ALL_MINIONS, 'AV_218t')
	pass
class AV_218t:
	"""  sheep """
	pass




if Alterac_Build_a_Snowman:# 
	Alterac_Mage+=['AV_282']
	Alterac_Mage+=['AV_282t']
	Alterac_Mage+=['AV_282t2']
	Alterac_Mage+=['AV_282t3']
	Alterac_Mage+=['AV_282t4']
	Alterac_Mage+=['AV_282t5']
class AV_282:
	""" Build a Snowman (3) Frost
	Summon a 3/3 Snowman that Freezes.  Add 'Build a Snowbrute' to your hand.
	"""
	play = Summon(CONTROLLER, 'AV_282t'), Give(CONTROLLER, 'AV_282t2')
	pass
class AV_282t:
	""" Snowman (3/3/3) Elemental
	Freeze any character damaged by this minion
	"""
	events = Attack(SELF, ENEMY_CHARACTERS).on(Freeze(Attack.DEFENDER))
	pass
class AV_282t2:
	""" Build a Snowbrute (6) Frost
	Summon a 6/6 Snowbrute that Freezes.  Add 'Build a Snowgre' to your hand.
	"""
	play = Summon(CONTROLLER, 'AV_282t3'), Give(CONTROLLER, 'AV_282t4')
	pass
class AV_282t3:
	""" Snowbrute (6/6/6) Elemental
	Freeze any character damaged by this minion.
	"""
	events = Attack(SELF, ENEMY_CHARACTERS).on(Freeze(Attack.DEFENDER))
	pass
class AV_282t4:
	""" Build a Snowgre (9) Frost
	Summon a 9/9 Sbiwgre tgat Freezes.
	"""
	play = Summon(CONTROLLER, 'AV_282t5')
	pass
class AV_282t5:
	""" Snowgre (9/9/9) Elemental
	Freeze any character damaged by this minion.
	"""
	events = Attack(SELF, ENEMY_CHARACTERS).on(Freeze(Attack.DEFENDER))
	pass




if Alterac_Rune_of_the_Archmage:# 
	Alterac_Mage+=['AV_283']
class AV_283_Action(TargetedAction):#
	TARGET = ActionArg()
	def do(self, source, target):
		controller = target
		count = 0
		while True:	
			card = RandomSpell(card_class=CardClass.MAGE).evaluate(source)[0]
			if card.cost + count <= 20:
				count += card.cost
				target = None
				if card.requires_target() and card.targets!=None and card.targets!=[]:
					target = random.choice(card.targets)
				controller.game.trigger(controller, [Play(card,target,None,None)],event_args=None)
			else:
				break
			pass
		pass
	pass
class AV_283:
	""" Rune of the Archmage (9)
	Cast 20 Mana worth of Mage spells at enemies.
	"""
	play = AV_283_Action(CONTROLLER)
	pass




if Alterac_Balinda_Stonehearth:# 
	Alterac_Mage+=['AV_284']
	#Alterac_Mage+=['AV_284e']
	#Alterac_Mage+=['AV_284e2']
class AV_284:
	""" Balinda Stonehearth (6/5/5)
	Battlecry: Draw 2 spells. Swap their Costs with this minion's stats."""
	def play(self):
		card1=Give(CONTROLLER, RANDOM(FRIENDLY_DECK + SPELL)).trigger(self.controller)
		card1cost=5
		if card1!=[] and card1[0]!=[]:
			card1cost = card1[0][0].cost
			card1[0][0].cost = self.atk# =5
			self.atk=card1cost
		card2=Give(CONTROLLER, RANDOM(FRIENDLY_DECK + SPELL)).trigger(self.controller)
		card2cost=5
		if card2!=[] and card2[0]!=[]:
			card2cost = card2[0][0].cost
			card2[0][0].cost = self.max_health# =5
			self.max_health=card2cost
		pass
	pass
#AV_284e=buff(cost=SET(5))
#AV_284e2=buff(atk=SET(1),health=SET(1))




if Alterac_Iceblood_Tower:# 
	Alterac_Mage+=['AV_290']
class AV_290:
	""" Iceblood Tower (10) lasts 3 turns
	At the end of your turn, cast another spell from your deck. Lasts 3 turns.	"""
	tags={GameTag.SIDEQUEST:True, }
	events=[
		OWN_TURN_END.on(CastSpell(RANDOM(FRIENDLY_DECK + SPELL))),
		OWN_TURN_BEGIN.on(SidequestCounter(SELF, 3, [Destroy(SELF)])),
		]
	pass




if Alterac_Deep_Breath:# 
	Alterac_Mage+=['ONY_006']
class ONY_006:# <4>[1626]
	""" Deep Breath
	Deal $@ damage to aminion and its neighbors.<i>(Improved by number of_other spells in your hand.)</i> """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	def play(self):
		target=self.target
		controller=self.controller
		amount=1
		for card in controller.hand:
			if card.type==CardType.SPELL:
				amount+=1
		self.script_data_text_0=amount# カード記載のため
		targets=[target]
		#instead of TARGET_ADJACENT
		opp_field = controller.opponent.field
		for i in range(len(opp_field)):
			if opp_field[i]==target:
				if i>0:
					targets.append(opp_field[i-1])
				if i<len(opp_field)-1:
					targets.append(opp_field[i+1])
				break;
		for card in targets:
			Hit(card, amount).trigger(controller)
	pass




if Alterac_Haleh,_Matron_Protectorate:# 
	Alterac_Mage+=['ONY_007']
class ONY_007:# <4>[1626]
	""" Haleh, Matron Protectorate
	After you cast a spell, deal 4 damage randomly split among all enemies. """
	events = OWN_SPELL_PLAY.on(Hit(RANDOM_ENEMY_CHARACTER,1) * 4)
	pass




if Alterac_Drakefire_Amulet:# 
	Alterac_Mage+=['ONY_029']
class ONY_029_Choice(Choice):
	def choose(self, card):
		self.source._sidequest_counter_ += 1
		if self.source._sidequest_counter_>=2:
			self.next_choice=None
		else:
			self.next_choice=self
		super().choose(card)
		card.zone = Zone.PLAY
		cards = self._args[1]
		if isinstance(cards, LazyValue):
			self.cards = cards.evaluate(self.source)
class ONY_029:# <4>[1626]
	""" Drakefire Amulet
	[Tradeable][Discover] 2 Dragons. Summon them. """
	play = 	ONY_029_Choice(CONTROLLER, RandomMinion(race=Race.DRAGON)*3)
	pass




###################################################

