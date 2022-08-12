from ..utils import *



from ..utils import *

Alterac_Hunter=[]

Alterac_Beaststalker_Tavish=True  ###
Alterac_Dun_Baldar_Bunker=True  ###
Alterac_Spring_the_Trap=True  ###
Alterac_Ice_Trap=True  ###
Alterac_Bloodseeker=True  ###
Alterac_Revive_Pet=True  ###
Alterac_Stormpike_Battle_Ram=True  ###
Alterac_Ram_Tamer=True  ###
Alterac_Wing_Commander_Ichman=False  ###difficult
Alterac_Mountain_Bear=True  ###
Alterac_Furious_Howl=True  ###
Alterac_Pet_Collector=True  ###
Alterac_Dragonbane_Shot=True  ###


if Alterac_Beaststalker_Tavish:# 
	Alterac_Hunter+=['AV_113']
	Alterac_Hunter+=['AV_113p']
	Alterac_Hunter+=['AV_113t1']
	Alterac_Hunter+=['AV_113t2']
	Alterac_Hunter+=['AV_113t2e']
	Alterac_Hunter+=['AV_113t3']
	Alterac_Hunter+=['AV_113t3t2']
	Alterac_Hunter+=['AV_113t7']
	Alterac_Hunter+=['AV_113t8']
	Alterac_Hunter+=['AV_113t9']
	Alterac_Hunter+=['AV_113t9e']
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
	<b>Hero Power</b>Summon an Animal Companion. """
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	entourage = ["NEW1_032", "NEW1_033", "NEW1_034"]
	activate = Summon(CONTROLLER, RandomEntourage())	
	pass
class AV_113t1:
	""" Improved Explosive Trap
	<b>Secret:</b> When your hero is attacked, deal $3 damage to all enemies. """
	secret = Attack(ENEMY_CHARACTERS, FRIENDLY_HERO).on(
		Reveal(SELF), Hit(ENEMY_CHARACTERS, 3))	
	pass
class AV_113t2:
	""" Improved Freezing Trap
	<b>Secret:</b> When an enemy minion attacks, return it to its owner's hand. It costs (4) more. """
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
	<b>Secret:</b> When one of your minions is attacked, summon three 2/2 Snakes. """
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
	<b>Secret:</b> When a friendly minion is attacked, summon two 3/3 copies. """
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
			if Config.LOGINFO:
				print("AV_113t8_action warks!!!")
			for _action in targetaction:
				_action.trigger(source)

class AV_113t8:
	""" Improved Open the Cages
	[x]<b>Secret:</b> When your turn starts, if you control two minions, summon two Animal Companions."""
	secret = EndTurn(OPPONENT).on(AV_113t8_Action(CONTROLLER,[
		Reveal(SELF), 
		Summon(CONTROLLER,random.choice(['NEW1_032','NEW1_033','NEW1_034'])),  
		Summon(CONTROLLER,random.choice(['NEW1_032','NEW1_033','NEW1_034'])),
		]))##
	pass
class AV_113t9:
	""" Improved Ice Trap
	<b>Secret:</b> When your opponent casts a spell, return it to their hand instead. It costs (2) more. """
	secret = Play(OPPONENT, SPELL).on(
		Reveal(SELF),
		Bounce(Play.CARD),
		Buff(Play.CARD,'AV_113t9e')
		)
	pass
AV_113t9e=buff(cost=2)




if Alterac_Dun_Baldar_Bunker:# 
	Alterac_Hunter+=['AV_147']
	Alterac_Hunter+=['AV_147e']
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




if Alterac_Spring_the_Trap:# 
	Alterac_Hunter+=['AV_224']
class AV_224:##
	""" Spring the Trap (4)
	Deal 3 damage to a minion and cast a Secret from your deck. Honorable Kill: Cast 2."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0,}
	play = Hit(TARGET, 3),CastSecret(RANDOM(FRIENDLY_DECK + SECRET)) # Play?
	honorable_kill = CastSecret(RANDOM(FRIENDLY_DECK + SECRET))
	pass




if Alterac_Ice_Trap:# 
	Alterac_Hunter+=['AV_226']
	Alterac_Hunter+=['AV_226e']
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




if Alterac_Bloodseeker:# 
	Alterac_Hunter+=['AV_244']
	Alterac_Hunter+=['AV_244e']
class AV_244:
	""" Bloodseeker (2/2/2) weapon
	Honorable Kill: Gain +1/+1."""
	honorable_kill = Buff(SELF, 'AV_244e')
	pass
AV_244e=buff(1,1)




if Alterac_Revive_Pet:# 
	Alterac_Hunter+=['AV_333']
class AV_333: ##
	""" Revive Pet (3) nature
	Discover a friendly Beast that died this game. Summon it. """
	play = GenericChoicePlay(CONTROLLER, RANDOM(FRIENDLY_KILLED + BEAST)*3)# not GenericChoiceBattlecry
	pass




if Alterac_Stormpike_Battle_Ram:# 
	Alterac_Hunter+=['AV_334']
	Alterac_Hunter+=['AV_334e']
	#Alterac_Hunter+=['AV_334e2']
class AV_334:
	""" Stormpike Battle Ram (4/4/3) beast
	Rush Deathrattle: Your next Beast costs (2) less."""
	deathrattle = Buff(FRIENDLY_HAND + BEAST, 'AV_334e')
	pass
class AV_334e:
	#cost = lambda self, i : max(0,i-2)
	tags = {GameTag.COST:-2,}
	events = Play(CONTROLLER, MINION + BEAST).on(Destroy(SELF))
	pass




if Alterac_Ram_Tamer:# 
	Alterac_Hunter+=['AV_335']
	Alterac_Hunter+=['AV_335e']
class AV_335:
	""" Ram Tamer (3/4/3)
	Battlecry: If you control a Secret, gain +1/+1 and Stealth."""
	play = Find(FRIENDLY_SECRETS) & Buff(SELF, 'AV_335e')
	pass
AV_335e=buff(atk=1,health=1,stealth=True)




if Alterac_Wing_Commander_Ichman:# 
	Alterac_Hunter+=['AV_336']
	Alterac_Hunter+=['AV_336e']
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




if Alterac_Mountain_Bear:# 
	Alterac_Hunter+=['AV_337']
	Alterac_Hunter+=['AV_337t']
class AV_337:
	""" Mountain Bear (7/5/6) beast
	[Taunt] [Deathrattle]: Summon two 2/4 Cubs with [Taunt]."""
	deathrattle = Summon(CONTROLLER, 'AV_337t') * 2
	pass
class AV_337t:
	"""  """
	pass




if Alterac_Furious_Howl:# 
	Alterac_Hunter+=['ONY_008']
class ONY_008:# <3>[1626]
	""" Furious Howl
	Draw a card.Repeat until you have at least 3 cards. """
	def play(self):
		Draw(self.controller).trigger(self.controller)
		while True:
			if len(self.controller.hand)>3:
				break;
			Draw(self.controller).trigger(self.controller)
			pass
	pass




if Alterac_Pet_Collector:# 
	Alterac_Hunter+=['ONY_009']
class ONY_009:# <3>[1626]
	""" Pet Collector
	[Battlecry:] Summon a Beast from your deck that costs (5) or less. """
	def play(self):
		cards = []
		for card in self.controller.deck:
			if card.type==CardType.MINION and card.race==Race.BEAST and card.cost<=5:
				cards.append(card)
		if len(cards)>0:
			Summon(self.controller, random.choice(cards)).trigger(self.controller)
		pass
	pass



if Alterac_Dragonbane_Shot:# 
	Alterac_Hunter+=['ONY_010']
	Alterac_Hunter+=['ONY_010e']
class ONY_010:# <3>[1626]
	""" Dragonbane Shot
	Deal $2 damage.[Honorable Kill:] Add a Dragonbane Shot to your hand. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, }
	play = Hit(TARGET, 2)
	honorable_kill = Give(CONTROLLER, 'ONY_010')	
	pass

ONY_010e=buff(cost=-1)# <3>[1626] ##???
""" Drakeshot
Costs (1) less. """



###############################################
