from ..utils import *

Sunken_Shaman=[]

Sunken_Tidelost_Burrower=True  ###
Sunken_Clownfish=True  ###
Sunken_Command_of_Neptulon=True  ###
Sunken_Wrathspine_Enchanter=True  ###
Sunken_Schooling=True  ###
Sunken_Piranha_Poacher=True  ###
Sunken_Radiance_of_Azshara=True  ###
Sunken_Scalding_Geyser=True  ###
Sunken_Glugg_the_Gulper=True  ###
Sunken_Coral_Keeper=True  ###
Sunken_Azsharan_Scroll=True  ###
Sunken_Anchored_Totem=True  ###
Sunken_Bioluminescence=True  ###

if Sunken_Tidelost_Burrower:# 
	Sunken_Shaman+=['TID_003']
	Sunken_Shaman+=['TID_003e2']
class TID_003_DredgeChoice(Choice):
	def choose(self, card):
		super().choose(card)
		if Config.LOGINFO:
			Config.log("DredgeChoice.choose","%s chooses %r"%(card.controller.name, card))
		controller = card.controller
		for c in controller.deck[:3]:
			if card.id==c.id:
				controller.deck.remove(c)
				controller.deck.append(c)
				if c.type==CardType.MINION and c.race==Race.MURLOC:
					newcard=Summon(controller, c.id).trigger(controller)
					newcard=newcard[0][0]
					Buff(newcard, 'TID_003e2').trigger(controller)
				break
		pass
class TID_003_Dredge(TargetedAction):
	"""
	TARGET=ActionArg()#CONTROLLER
	"""
	TARGET=ActionArg()
	def do(self, source, target):
		bottom3ID=[card.id for card in target.deck[:3]]
		TID_003_DredgeChoice(target, RandomID(*bottom3ID)*3).trigger(source)
	pass
class TID_003:# <8>[1658]
	""" Tidelost Burrower
	[Battlecry:] [Dredge].If it's a Murloc, summon a 2/2 copy of it. """
	play = TID_003_Dredge(CONTROLLER)
	pass
class TID_003e2:# <8>[1658]
	""" Revealed 	2/2. """
	atk = lambda self,i:2
	max_health = lambda self,i:2
	pass

if Sunken_Clownfish:# 
	Sunken_Shaman+=['TID_004']
	#Sunken_Shaman+=['TID_004e']
	Sunken_Shaman+=['TID_004e2']
class TID_004:# <8>[1658]
	""" Clownfish
	[Battlecry:] Your next two Murlocs cost (2) less. """
	play = Buff(FRIENDLY_HAND, 'TID_004e2')
	pass
class TID_004e:# <8>[1658]
	""" Clownfish Car
	Your next two Murlocs cost (2) less. """
	#
	pass
class TID_004e2:# <8>[1658]
	""" Clownin' Around
	Costs (2) less. """
	cost = lambda self,i: max(i-2,0)
	events = Play(CONTROLLER, MURLOC).on(SidequestCounter(SELF, 2, [Destroy(SELF)]))
	pass

if Sunken_Command_of_Neptulon:# 
	Sunken_Shaman+=['TID_005']
	Sunken_Shaman+=['TID_005t']
class TID_005:# <8>[1658]
	""" Command of Neptulon
	Summon two 5/4 Elementals(TID_005t) with [Rush].[Overload:] (1) """
	#<Tag enumID="215" name="OVERLOAD" type="Int" value="1"/>
	play = Summon(CONTROLLER, 'TID_005t'), Summon(CONTROLLER, 'TID_005t')
	pass
class TID_005t:# <8>[1658]
	""" Water Revenant
	[Rush] """
	pass

if Sunken_Wrathspine_Enchanter:# 
	Sunken_Shaman+=['TSC_630']
class TSC_630:# <8>[1658]
	""" Wrathspine Enchanter
	[Battlecry:] Cast a copy of a Fire, Frost, and Nature spell in your hand <i>(targets chosen randomly).</i> """
	def play(self):
		cards=[card for card in self.controller.hand if card.type==CardType.SPELL and card.spell_school==SpellSchool.FIRE]
		if len(cards)>0:
			card=random.choice(cards)
			CastSpell(card.id).trigger(self)
		cards=[card for card in self.controller.hand if card.type==CardType.SPELL and card.spell_school==SpellSchool.FROST]
		if len(cards)>0:
			card=random.choice(cards)
			CastSpell(card.id).trigger(self)
		cards=[card for card in self.controller.hand if card.type==CardType.SPELL and card.spell_school==SpellSchool.NATURE]
		if len(cards)>0:
			card=random.choice(cards)
			CastSpell(card.id).trigger(self)
	pass

if Sunken_Schooling:# 
	Sunken_Shaman+=['TSC_631']
class TSC_631:# <8>[1658]
	""" Schooling
	Add three 1/1 Piranha Swarmers(TSC_638) to your hand. """
	play = Give(CONTROLLER, 'TSC_638') * 3
	pass

if Sunken_Piranha_Poacher:# 
	Sunken_Shaman+=['TSC_633']
class TSC_633:# <8>[1658]
	""" Piranha Poacher
	At the end of your turn,add a 1/1 Piranha Swarmer(TSC_638) to your hand. """
	events = OWN_TURN_END.on(Give(CONTROLLER, 'TSC_638'))
	pass

if Sunken_Radiance_of_Azshara:# 
	Sunken_Shaman+=['TSC_635']
	Sunken_Shaman+=['TSC_635e']
class TSC_635:# <8>[1658]
	""" Radiance of Azshara
	[Fire Spell Damage +2]Your Nature spells cost (1)less. After you cast a Frostspell, gain 3 Armor. """
	#<Tag enumID="1946" name="SPELLPOWER_FIRE" type="Int" value="1"/> ## mistake
	tags = {GameTag.SPELLPOWER_FIRE: 2, }
	play = Buff(FRIENDLY_HAND + NATURE, 'TSC_635e')
	events = Play(CONTROLLER, FROST).after(GainArmor(FRIENDLY_HERO, 3))
	pass
class TSC_635e:# <8>[1658]
	""" Kaldorei Strength
	Costs (1) less. """
	cost = lambda self, i: max(i-1,0)
	pass

if Sunken_Scalding_Geyser:# 
	Sunken_Shaman+=['TSC_637']
class TSC_637:# <8>[1658]
	""" Scalding Geyser
	Deal $2 damage.[Dredge]. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = Hit(TARGET, 2), Dredge(CONTROLLER)
	pass

if Sunken_Glugg_the_Gulper:# 
	Sunken_Shaman+=['TSC_639']
	Sunken_Shaman+=['TSC_639e']
	Sunken_Shaman+=['TSC_639e2']
	Sunken_Shaman+=['TSC_639t']
	Sunken_Shaman+=['TSC_639t2']
	Sunken_Shaman+=['TSC_639t3']
class TSC_639_Action(TargetedAction):
	TARGET=ActionArg()
	CARD=ActionArg()
	def do(self, source, target, card):
		Buff(target, 'TSC_639e', atk = card.atk, max_health=card.max_health).trigger(source)
		pass
class TSC_639:# <8>[1658]
	""" Glugg the Gulper
	[Colossal +3] After a friendly minion dies,gain its original stats. """
	play = Summon(CONTROLLER, 'TSC_639t'), Summon(CONTROLLER, 'TSC_639t2'), Summon(CONTROLLER, 'TSC_639t3')
	events = Death(FRIENDLY_MINIONS).after(TSC_639_Action(SELF, Death.TARGET))
	pass
class TSC_639e:# <8>[1658]
	""" Gulped
	Increased stats. """
	#
	pass
class TSC_639e2:# <8>[1658]
	""" Gulped
	Increased stats. """
	#
	pass
class TSC_639t:# <8>[1658]
	""" Glugg's Tail 	[Taunt] """
class TSC_639t2:# <8>[1658]
	""" Glugg's Tail 	[Taunt] """
class TSC_639t3:# <8>[1658]
	""" Glugg's Tail 	[Taunt] """


if Sunken_Coral_Keeper:# 
	Sunken_Shaman+=['TSC_648']
	Sunken_Shaman+=['TSC_648t']
class TSC_648:# <8>[1658]
	""" Coral Keeper
	[Battlecry:] Summon a 3/3 Elemental(TSC_648t) for each spell school you've cast this game. """
	def play(self):
		cards=[]
		schools=[]
		for card in self.controller.play_log:
			if card.type==CardType.SPELL and not card.spell_school in schools:
				cards.append(card)
				schools.append(card.spell_school)
		for repeat in range(len(cards)+1):
			Summon(self.controller, 'TSC_648t').trigger(self)
	pass
class TSC_648t:# <8>[1658]
	""" Coral Elemental 	 """
	pass

if Sunken_Azsharan_Scroll:# 
	Sunken_Shaman+=['TSC_772']
	Sunken_Shaman+=['TSC_772t']
class TSC_772:# <8>[1658]
	""" Azsharan Scroll
	[Discover] a Fire, Frost or Nature spell. Put a 'Sunken Scroll'(TSC_772t) on the bottom of your deck. """
	def play(self):
		card1 = (RandomSpell(spell_school=SpellSchool.FIRE).evaluate(self))[0]
		card2 = (RandomSpell(spell_school=SpellSchool.FROST).evaluate(self))[0]
		card3 = (RandomSpell(spell_school=SpellSchool.NATURE).evaluate(self))[0]
		cards=(card1, card2, card3)
		ShuffleBottom(CONTROLLER, 'TSC_772t').trigger(self)
		Discover(CONTROLLER, RandomID(*cards)).trigger(self)
	pass
class TSC_772t:# <8>[1658]
	""" Sunken Scroll
	Add a Fire, Frost, and Nature spell from your class to your hand. """
	#
	pass

if Sunken_Anchored_Totem:# 
	Sunken_Shaman+=['TSC_922']
	Sunken_Shaman+=['TSC_922e']
class TSC_922:# <8>[1658]
	""" Anchored Totem
	After you summon a 1-Cost minion, give it +2/+1. """
	events = Summon(CONTROLLER, MINION + (COST == 1)).on(Buff(Summon.CARD, 'TSC_922e'))
	pass
TSC_922e=buff(2,1)

if Sunken_Bioluminescence:# 
	Sunken_Shaman+=['TSC_923']
	Sunken_Shaman+=['TSC_923e']
class TSC_923:# <8>[1658]
	""" Bioluminescence
	Give your minions [Spell Damage +1]. """
	play = Buff(FRIENDLY_MINIONS, 'TSC_923e')
	#
	pass
class TSC_923e:# <8>[1658]
	""" Bioluminescent
	[Spell Damage +1]. """
	apply = SetAttr(OWNER, 'spellpower', 1) 
	pass

