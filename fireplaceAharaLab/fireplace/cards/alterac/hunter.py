from ..utils import *

Alterac_Hunter=['AV_113','AV_113p','AV_113t1','AV_113t2','AV_113t2e','AV_113t3','AV_113t3t2','AV_113t7','AV_113t8','AV_113t9','AV_113t9e','AV_147','AV_147e','AV_224','AV_226','AV_226e','AV_244','AV_244e','AV_333','AV_334','AV_334e','AV_335','AV_335e','AV_336','AV_336e','AV_337','AV_337t',
	]
class AV_113_Choice(Choice):
	def choose(self, card):
		self.source._sidequest_counter_ += 1
		if self.source._sidequest_counter_>=2:
			self.next_choice=None
		else:
			self.next_choice=self
		super().choose(card)
		card.zone = Zone.SECRET
		cards = self._args[1]
		if isinstance(cards, LazyValue):
			self.cards = cards.evaluate(self.source)

class AV_113:
	"""Beaststalker Tavish (6/*/5) Hero
	Battlecry: Discover and cast 2 Improved Secrets."""
	entourage=['AV_113t1','AV_113t2','AV_113t3','AV_113t7','AV_113t8','AV_113t9',]
	play = AV_113_Choice(CONTROLLER, RandomEntourage()*3)
	pass
class AV_113p:
	""" Summon Pet (3) (hero power)
	&lt;b&gt;Hero Power&lt;/b&gt;Summon an Animal Companion. """
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	entourage = ["NEW1_032", "NEW1_033", "NEW1_034"]
	activate = Summon(CONTROLLER, RandomEntourage())	
	pass
class AV_113t1:
	""" Improved Explosive Trap
	&lt;b&gt;Secret:&lt;/b&gt; When your hero is attacked, deal $3 damage to all enemies. """
	secret = Attack(ENEMY_CHARACTERS, FRIENDLY_HERO).on(
		Reveal(SELF), Hit(ENEMY_CHARACTERS, 3))	
	pass
class AV_113t2:
	""" Improved Freezing Trap
	&lt;b&gt;Secret:&lt;/b&gt; When an enemy minion attacks, return it to its owner's hand. It costs (4) more. """
	secret = Attack(ENEMY_MINIONS).on(
		Reveal(SELF),
		Bounce(Attack.ATTACKER),
		Buff(Attack.ATTACKER, "AV_113t2e")
	)	
	pass
class AV_113t2e:# 3 3
	events = REMOVED_IN_PLAY
	tags = {GameTag.COST: +4}
class AV_113t3:
	""" Improved Snake Trap
	&lt;b&gt;Secret:&lt;/b&gt; When one of your minions is attacked, summon three 2/2 Snakes. """
	secret = Attack(ALL_MINIONS, FRIENDLY_MINIONS).on(FULL_BOARD | (
		Reveal(SELF), Summon(CONTROLLER, "AV_113t3t2") * 3
	))
	pass
class AV_113t3t2:
	"""Snake
	"""
	pass
class AV_113t7_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		Reveal(source).trigger(source)
		if isinstance(target, list):
			target = target[0]
		card00 = Summon(source.controller, ExactCopy(FuncSelector(lambda entities, source: [target]))).trigger(source)
		card = card00[0][0]
		Buff(card,"BT_203e" ).trigger(source)
		card00 = Summon(source.controller, ExactCopy(FuncSelector(lambda entities, source: [target]))).trigger(source)
		card = card00[0][0]
		Buff(card,"BT_203e" ).trigger(source)

class AV_113t7:
	"""Improved Pack Tactics
	&lt;b&gt;Secret:&lt;/b&gt; When a friendly minion is attacked, summon two 3/3 copies. """
	secret = Attack(CHARACTER, FRIENDLY_MINIONS).on(AV_113t7_Action(Attack.DEFENDER))
	pass
#class BT_203e: ## AOO_Hunter
#	atk = SET(3)
#	max_health = SET(3)

class AV_113t8_Action(TargetedAction):
	TARGET = ActionArg()
	TARGETACTION = ActionArg()
	def do(self, source, target, targetaction):
		if len(target.field)==2:
			log.info("AV_113t8_action warks!!!")
			for _action in targetaction:
				_action.trigger(source)

class AV_113t8:
	""" Improved Open the Cages
	[x]&lt;b&gt;Secret:&lt;/b&gt; When your turn starts, if you control two minions, summon two Animal Companions."""
	secret = EndTurn(OPPONENT).on(AV_113t8_Action(CONTROLLER,[
		Reveal(SELF), 
		Summon(CONTROLLER,random.choice(['NEW1_032','NEW1_033','NEW1_034'])),  
		Summon(CONTROLLER,random.choice(['NEW1_032','NEW1_033','NEW1_034'])),
		]))##
	pass
class AV_113t9:
	""" Improved Ice Trap
	&lt;b&gt;Secret:&lt;/b&gt; When your opponent casts a spell, return it to their hand instead. It costs (2) more. """
	secret = Play(OPPONENT, SPELL).on(
		Reveal(SELF),
		Bounce(Play.CARD),
		Buff(Play.CARD,'AV_113t9e')
		)
	pass
AV_113t9e=buff(cost=2)

class AV_147:
	""" Dun Baldar Bunker (2) Lasts
	At the end of your turn, draw a Secret and set its Cost to (1). Lasts 3 turns."""
	tags={GameTag.SIDEQUEST:True, }
	events = [
		OWN_TURN_END.on(Give(CONTROLLER, RandomSpell(secret=True)).then(Buff(Give.CARD,'AV_147e'))),
		OWN_TURN_BEGIN.on(SidequestCounter(SELF, 3, [Destroy(SELF)])),
		]	
	pass
class AV_147e:
	cost=SET(1)
	pass

class AV_224:##
	""" Spring the Trap (4)
	Deal 3 damage to a minion and cast a Secret from your deck. Honorable Kill: Cast 2."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0,}
	play = Hit(TARGET, 3),CastSecret(RANDOM(FRIENDLY_DECK + SECRET)) # Play?
	honorable_kill = CastSecret(RANDOM(FRIENDLY_DECK + SECRET))
	pass

class AV_226:
	""" Ice Trap (2) frost
	Secret: When your opponent casts a spell, return it to their hand instead. It costs (1) more."""
	secret = Play(OPPONENT, SPELL).on(
		Reveal(SELF),
		Bounce(Play.CARD),
		Buff(Play.CARD,'AV_226e')
		)
	pass
AV_226e=buff(cost=1)

class AV_244:
	""" Bloodseeker (2/2/2) weapon
	Honorable Kill: Gain +1/+1."""
	honorable_kill = Buff(SELF, 'AV_244e')
	pass
AV_244e=buff(1,1)

class AV_333: ##
	""" Revive Pet (3) nature
	Discover a friendly Beast that died this game. Summon it. """
	play = GenericChoicePlay(CONTROLLER, RANDOM(FRIENDLY_KILLED + BEAST)*3)# not GenericChoiceBattlecry
	pass

class AV_334:
	""" Stormpike Battle Ram (4/4/3) beast
	Rush Deathrattle: Your next Beast costs (2) less."""
	deathrattle = Buff(FRIENDLY_HAND + BEAST, 'AV_334e')
	pass
class AV_334e:
	cost = lambda self, i : max(0,i-2)
	events = Play(CONTROLLER, MINION + BEAST).on(Destroy(SELF))
	pass

class AV_335:
	""" Ram Tamer (3/4/3)
	Battlecry: If you control a Secret, gain +1/+1 and Stealth."""
	play = Find(FRIENDLY_SECRETS) & Buff(SELF, 'AV_335e')
	pass
AV_335e=buff(atk=1,health=1,stealth=True)

class AV_336: ################################ need the latter half
	""" Wing Commander Ichman (9/5/4)
	[Battlecry]: Summon a Beast from your deck and give it [Rush]. If it kills a minion this turn, repeat."""
	play = Summon(CONTROLLER, RANDOM(FRIENDLY_DECK + BEAST)).then(
		SetAttr(Summon.CARD, 'rush', True),
		Buff(Summon.CARD, 'AV_336e')
		)
	pass
class AV_336_Action(TargetedAction):
	ATTACKER=ActionArg()
	DEFENDER=ActionArg()
	TARGETEDACTION=ActionArg()
	def do(self, source, attacker, defender, targetedaction):
		if hasattr(attacker, 'atk') and hasattr(defender,'health'):
			if attacker.atk>=defender.health:
				targetedaction.trigger(source)

class AV_336e:
	next_action = Summon(CONTROLLER, RANDOM(FRIENDLY_DECK + BEAST)).then(SetAttr(Summon.CARD, 'rush', True), Buff(Summon.CARD, 'AV_336e'))
	events =[
		Attack(OWNER, ENEMY_MINIONS).on(AV_336_Action(Attack.ATTACKER, Attack.DEFENDER, next_action)),
		OWN_TURN_END.on(Destroy(SELF))
		]
	pass

class AV_337:
	""" Mountain Bear (7/5/6) beast
	[Taunt] [Deathrattle]: Summon two 2/4 Cubs with [Taunt]."""
	deathrattle = Summon(CONTROLLER, 'AV_337t') * 2
	pass
class AV_337t:
	"""  """
	pass


class ONY_008:# <3>[1626]
	""" Furious Howl
	Draw a card.Repeat until you have at least 3 cards. """
	#
	pass

class ONY_009:# <3>[1626]
	""" Pet Collector
	[Battlecry:] Summon a Beast from your deck that costs (5) or less. """
	#
	pass

class ONY_010:# <3>[1626]
	""" Dragonbane Shot
	Deal $2 damage.[Honorable Kill:] Add a Dragonbane Shotto your hand. """
	#
	pass

class ONY_010e:# <3>[1626]
	""" Drakeshot
	Costs (1) less. """
	#
	pass