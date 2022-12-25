from ..utils import *

Alterac_Shaman=[]

Alterac_Glaciate=True
Alterac_Snowball_Fight=True
Alterac_Cheaty_Snobold=True
Alterac_Snowfall_Guardian=True
Alterac_Bearon_Glashear=True
Alterac_Brukan_of_the_Elements=True
Alterac_Frostbite=True
Alterac_Sleetbreaker=True
Alterac_Windchill=True
Alterac_Wildpaw_Cavern=True
Alterac_Dont_Stand_in_the_Fire=True
Alterac_Spirit_Mount=True
Alterac_Bracing_Cold=True


if Alterac_Glaciate:# 
	Alterac_Shaman+=['AV_107']
class AV_107_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		controller = card.controller
		newcard=Summon(controller, card).trigger(controller)
		if newcard[0]==[]:
			return
		newcard=newcard[0][0]
		Freeze(newcard).trigger(controller)
		pass
	pass
class AV_107:# <8>[1626]
	""" Glaciate
	[Discover] an 8-Cost minion. Summon and [Freeze] it. """
	play = AV_107_Choice(CONTROLLER, RandomMinion(cost=8))
	pass




if Alterac_Snowball_Fight:# ### OK ###
	Alterac_Shaman+=['AV_250']
class AV_250_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		Hit(card, 1).trigger(self.source)
	pass
class AV_250_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		Hit(target, 1).trigger(source)
		target.frozen=True
		if target.health>1:#if it survives
			cards=[card.id for card in source.controller.opponent.field]
			amount=len(cards)
			if amount>0:
				AV_250_Choice(source.controller, RandomID(*cards)*amount).trigger(source)
		pass
	pass
class AV_250:# <8>[1626]
	""" Snowball Fight!
	Deal $1 damage to a minion and [Freeze] it. If it survives, repeat this on another minion! """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = AV_250_Action(TARGET)
	pass




if Alterac_Cheaty_Snobold:# 
	Alterac_Shaman+=['AV_251']
class AV_251:# <8>[1626]
	""" Cheaty Snobold
	After an enemy is [Frozen], deal 3 damage to it. """
	events = Freeze(ENEMY_CHARACTERS).after(Hit(Freeze.TARGET, 3))
	pass

if Alterac_Snowfall_Guardian:# 
	Alterac_Shaman+=['AV_255']
	#Alterac_Shaman+=['AV_255e']
class AV_255:# <8>[1626]
	""" Snowfall Guardian
	[Battlecry:] [Freeze] all other minions. """
	play = Freeze(ALL_MINIONS - SELF)
	pass
class AV_255e:# <8>[1626]
	""" Chilled 	Increased stats. """
	pass

if Alterac_Bearon_Glashear:# 
	Alterac_Shaman+=['AV_257']
	Alterac_Shaman+=['AV_257t']
class AV_257:# <8>[1626]
	""" Bearon Gla'shear
	[Battlecry:] For each Frost spell you've cast this game, summon a 3/4 Elemental(AV_257t) that [Freezes].@ <i>(@)</i> """
	def play(self):
		cards = [card for card in self.controller.play_log if card.SPELL_SCHOOL(SpellSchool.FROST)]
		if len(cards)>0:
			for repeat in range(len(cards)):
				Summon(self.controller, 'AV_257t').trigger(self)
	pass
class AV_257t:# <8>[1626]
	""" Frozen Stagguard
	[Freeze] any character damaged by this minion. """
	events = Attack(SELF).after(Freeze(Attack.DEFENDER))
	pass

if Alterac_Brukan_of_the_Elements:# 
	Alterac_Shaman+=['AV_258']
	Alterac_Shaman+=['AV_258p']
	Alterac_Shaman+=['AV_258p2']
	Alterac_Shaman+=['AV_258pt']
	Alterac_Shaman+=['AV_258pt3']
	Alterac_Shaman+=['AV_258pt4']
	Alterac_Shaman+=['AV_258pt7']
	Alterac_Shaman+=['AV_258t']
	Alterac_Shaman+=['AV_258t2']
	Alterac_Shaman+=['AV_258t3']
	Alterac_Shaman+=['AV_258t4']
	Alterac_Shaman+=['AV_258t6']
class AV_258_Choice1(Choice):
	def choose(self,card):
		super().choose(card)
		cards = ['AV_258t','AV_258t2','AV_258t3','AV_258t4']
		cards.remove(card.id)
		cards = tuple(cards)
		self.next_choice = AV_258_Choice2(CONTROLLER, RandomID(*cards))
		Give(self.controller, card).trigger(card.controller)
class AV_258_Choice2(Choice):
	def choose(self,card):
		super().choose(card)
		self.next_choice=None
		Give(self.controller, card).trigger(card.controller)
class AV_258:# <8>[1626] ### hero
	""" Bru'kan of the Elements
	[Battlecry:] Call upon the power of two Elements! """
	play = AV_258_Choice1(CONTROLLER, RandomID('AV_258t','AV_258t2','AV_258t3','AV_258t4')*4)
	pass
class AV_258p:# <8>[1626]
	""" Elemental Mastery
	[Hero Power] Call upon a different Element every turn! """
	pass
class AV_258p2:# <8>[1626]
	""" Water Invocation
	[Hero Power] Restore #6 Health to all friendly characters. Swaps each turn. """
	activate = Heal(FRIENDLY_MINIONS, 6)
	events = OWN_TURN_END.on(ChangeHeroPower(CONTROLLER, 'AV_258pt7'))
	pass

class AV_258pt:# <8>[1626]
	""" Earth Invocation
	[Hero Power] Summon two 2/3 Elementals(AV_258t6) with [Taunt]. Swaps each turn. """
	activate = Summon(CONTROLLER, 'AV_258t6')*2
	events = OWN_TURN_END.on(ChangeHeroPower(CONTROLLER, 'AV_258pt7'))
	pass
class AV_258pt3:# <8>[1626]
	""" Fire Invocation
	[Hero Power] Deal $6 damage to the enemy hero. Swaps each turn. """
	activate = Hit(ENEMY_HERO, 6)
	events = OWN_TURN_END.on(ChangeHeroPower(CONTROLLER, 'AV_258pt7'))
	pass

class AV_258pt4:# <8>[1626]
	""" Lightning Invocation
	[Hero Power] Deal $2 damage to all enemy minions. Swaps each turn. """
	activate = Hit(ENEMY_MINIONS, 2)
	events = OWN_TURN_END.on(ChangeHeroPower(CONTROLLER, 'AV_258pt7'))
	pass
class AV_258pt7_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = target
		card = random.choice(['AV_258pt','AV_258p2','AV_258pt3','AV_258pt4'])
		ChangeHeroPower(controller, card).trigger(source)
		pass
class AV_258pt7:# <8>[1626]
	""" Command the Elements
	[Hero Power] Call upon a different Element every turn! """
	events = OWN_TURN_BEGIN.on(AV_258pt7_Action(CONTROLLER))
	pass
class AV_258t:# <8>[1626]
	""" Earth Invocation
	Summon two 2/3 Elementals(AV_258t6) with [Taunt]. """
	play = Summon(CONTROLLER, 'AV_258t6')*2
	pass
class AV_258t2:# <8>[1626]
	""" Water Invocation
	Restore 6 Health to all friendly characters. """
	play = Heal(FRIENDLY_MINIONS, 6)
	pass
class AV_258t3:# <8>[1626]
	""" Fire Invocation
	Deal 6 damage to the enemy hero. """
	play = Hit(ENEMY_HERO, 6)
	pass
class AV_258t4:# <8>[1626]
	""" Lightning Invocation
	Deal 2 damage to all enemy minions. """
	play = Hit(ENEMY_MINIONS, 2)
	pass
class AV_258t6:# <8>[1626]
	""" Earthen Guardian
	[Taunt] """
	#
	pass

if Alterac_Frostbite:# 
	Alterac_Shaman+=['AV_259','AV_259e','AV_259e2']
class AV_259:# <8>[1626]
	""" Frostbite
	Deal $3 damage. [Honorable Kill:] Your opponent's next spell costs (2) more. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }	
	play = Hit(TARGET, 3)
	honorable_kill=Buff(ENEMY_HAND + SPELL, 'AV_259e')
	pass
class AV_259e:
	cost = lambda self, i:i+2
	events = Play(ENEMY, SPELL).after(Destroy(SELF))

if Alterac_Sleetbreaker:# 
	Alterac_Shaman+=['AV_260']
class AV_260:# <8>[1626]
	""" Sleetbreaker
	[Battlecry:] Add a Windchill(AV_266) to your hand. """
	play = Give(CONTROLLER, 'AV_266')
	pass

if Alterac_Windchill:# 
	Alterac_Shaman+=['AV_266']
class AV_266:# <8>[1626]
	""" Windchill
	[Freeze] a minion. Draw a card. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }	
	Play = Freeze(TARGET), Draw(CONTROLLER)
	pass

if Alterac_Wildpaw_Cavern:# 
	Alterac_Shaman+=['AV_268']
class AV_268:# <8>[1626]
	""" Wildpaw Cavern
	At the end of your turn, summon a 3/4 Elemental(AV_257t) that [Freezes]. Lasts 3 turns. """
	events=[
		OWN_TURN_END.on(Summon(CONTROLLER, 'AV_257t')),
		OWN_TURN_BEGIN.on(SidequestCounter(SELF, 3, [Destroy(SELF)]))
		]
	pass

if Alterac_Dont_Stand_in_the_Fire:# 
	Alterac_Shaman+=['ONY_011']
class ONY_011:# <8>[1626]
	""" Don't Stand in the Fire!
	Deal $10 damage randomly split among all enemy minions. [Overload:] (1) """
	play = SplitHit(SELF, ENEMY_MINIONS, 10)
	pass

if Alterac_Spirit_Mount:# 
	Alterac_Shaman+=['ONY_012']
	Alterac_Shaman+=['ONY_012e']
	Alterac_Shaman+=['ONY_012t']
class ONY_012:# <8>[1626]
	""" Spirit Mount
	Give a minion +1/+2 and [Spell Damage +1]. When it dies, summon a Spirit Raptor(ONY_012t). """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	play = Buff(TARGET, 'ONY_012e')	
	pass
class ONY_012e:# <8>[1626]
	""" With Da Spirits
	+1/+2 and [Spell Damage +1]. [Deathrattle:] Summon a Spirit Raptor(ONY_012t). """
	tags={
		GameTag.ATK:1,
		GameTag.HEALTH:2,
		GameTag.SPELLPOWER:1,
		GameTag.DEATHRATTLE:1	
		}
	deathrattle = Summon(CONTROLLER, 'ONY_012t')
	pass
class ONY_012t:# <8>[1626]
	""" Bru'kan's Raptor 	[Spell Damage +1] """
	pass

if Alterac_Bracing_Cold:# 
	Alterac_Shaman+=['ONY_013']
	Alterac_Shaman+=['ONY_013e']
class ONY_013:# <8>[1626]
	""" Bracing Cold
	Restore #5 Health to your hero. Reduce the Cost of a random spell in your hand by (2). """
	play = Heal(FRIENDLY_HERO, 5), Buff(RANDOM(FRIENDLY_HAND + SPELL), 'ONY_013e')
	pass
class ONY_013e:# <8>[1626]
	""" Shivers 	Costs (2) less. """
	cost = lambda self, i: max(i-2,0)
	pass

