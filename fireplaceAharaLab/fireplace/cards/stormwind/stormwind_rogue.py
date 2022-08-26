
from ..utils import *

StormWind_Rogue=[]

StormWind_Blackwater_Cutlass=True  ###
StormWind_Parrrley=True  ###
StormWind_Edwin_Defias_Kingpin=True  ###
StormWind_Maestra_of_the_Masquerade=True  ###
StormWind_Find_the_Imposter=True  ###
StormWind_Counterfeit_Blade=True  ###
StormWind_Garrote=True  ###
StormWind_Sketchy_Information=True  ###
StormWind_SI7_Informant=True  ###
StormWind_SI7_Extortion=True  ###
StormWind_SI7_Operative=True  ###
StormWind_SI7_Assassin=True  ###
StormWind_Loan_Shark=True  ###

###########################################





if StormWind_Blackwater_Cutlass:# 
	StormWind_Rogue+=['DED_004']
	StormWind_Rogue+=['DED_004e']
class DED_004:# <7>[1578]
	""" Blackwater Cutlass
	[Tradeable]After you [Trade] this,reduce the cost of a spell in your hand by (1). """
	events = Trade(CONTROLLER, SELF).after(Buff(FRIENDLY_HAND + SPELL, 'DED_004e'))
	pass

class DED_004e:# <7>[1578]
	""" Blackwater Treasure		Costs (1) less. """
	cost = lambda self, i: max(i-1,0)
	pass




if StormWind_Parrrley:# 
	StormWind_Rogue+=['DED_005']
class DED_005:# <7>[1578]
	""" Parrrley
	Swap this for a card in your opponent's deck. """
	def play(self):
		controller = self.controller
		if controller.opponent.deck!=[]:
			card = random.choice(controller.opponent.deck)
			index=controller.opponent.deck.index(card)
			controller.opponent.deck.remove(card)
			card.controller=controller
			card.zone=Zone.HAND
			controller.opponent.deck.insert(index, self)
			self.controller = controller.opponent
			self.zone=Zone.DECK
		pass
	pass




if StormWind_Edwin_Defias_Kingpin:# 
	StormWind_Rogue+=['DED_510']
	StormWind_Rogue+=['DED_510e']
	StormWind_Rogue+=['DED_510e2']
class DED_510:# <7>[1578]
	""" Edwin, Defias Kingpin
	[Battlecry:] Draw a card. If you play it this turn, gain +2/+2 and repeat this effect. """
	play = Draw(CONTROLLER).on(Buff(Draw.CARD, 'DED_510e'))
	pass

class DED_510e:# <7>[1578]
	""" Defias Supplies
	If played this turn, draw a card and give Edwin +2/+2. """
	events=[
		Play(CONTROLLER, OWNER)on(Buff(FRIENDLY_MINIONS+ID('DED_510'), 'DED_510e2'), Draw(CONTROLLER).on(Buff(Draw.CARD, 'DED_510e')))
		OWN_TURN_END.on(Destroy(SELF))
		]
	pass
DED_510e2=buff(2,2)# <7>[1578]




if StormWind_Maestra_of_the_Masquerade:# 
	StormWind_Rogue+=['SW_050']
class SW_050_Action1(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=target
		classes = [CardClass.DEMONHUNTER, CardClass.DRUID, CardClass.HUNTER, CardClass.MAGE, CardClass.PALADIN, CardClass.PRIEST, CardClass.ROGUE, CardClass.SHAMAN, CardClass.WARLOCK, CardClass.WARRIOR,]
		myclass=controller.hero.data.card_class
		classes.remove(myclass)
		temporaryClass = random.choice(classes)
		temporaryHeroID=temporaryClass.default_hero
		controller.summon(temporaryHeroID)
		pass
class SW_050_Action2(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = target
		originalClass = controller.hero.data.card_class
		originalHeroID=originalClass.default_hero
		controller.summon(originalHeroID)
		pass
class SW_050:# <7>[1578]
	""" Maestra of the Masquerade
	You start the game as a different class until you play a Rogue card. """
	class Hand:
		events=[
			BeginGame(CONTROLLER).on(SW_050_Action1(CONTROLLER)),
			Play(CONTROLLER, ROGUE).SW_050_Action2(CONTROLLER)]
	class Deck:
		events=[
			BeginGame(CONTROLLER).on(SW_050_Action1(CONTROLLER)),
			Play(CONTROLLER, ROGUE).SW_050_Action2(CONTROLLER)]
	events = Play(CONTROLLER, ROGUE).SW_050_Action2(CONTROLLER)## exceptional case

	pass




if StormWind_Find_the_Imposter:# 
	StormWind_Rogue+=['SW_052']
	StormWind_Rogue+=['SW_052t']
	StormWind_Rogue+=['SW_052t2']
	StormWind_Rogue+=['SW_052t3']
	StormWind_Rogue+=['SW_052t4']
	StormWind_Rogue+=['SW_052t4e']
	StormWind_Rogue+=['SW_052t5']
	StormWind_Rogue+=['SW_052t6']
	StormWind_Rogue+=['SW_052t6e']
	StormWind_Rogue+=['SW_052t7']
	StormWind_Rogue+=['SW_052t8_t']
class SW_052_Quest1(TargetedAction):
	CARD=ActionArg()
	def do(self, source, card):
		if isinstance(card, list):
			card = card[0]
		if card.SI7_minion:
			source._sidequest_counter_ += 1
			if source._sidequest_counter_==2:
				card = random.choice(['SW_052t5','SW_052t4','SW_052t7','SW_052t8_t','SW_052t6'])
				Give(source.controller, card).trigger(source)
				Summon(source.controller, 'SW_052t')
				Destroy(source).trigger(source)
class SW_052:# <7>[1578]
	""" Find the Imposter
	[Questline:] Play 2 SI:7 cards.[Reward:] Add a Spy Gizmo to your hand. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}	#
	events = Play(CONTROLLER).on(SW_052_Quest1(Play.CARD))
	pass
class SW_052_Quest2(TargetedAction):
	CARD=ActionArg()
	def do(self, source, card):
		if isinstance(card, list):
			card = card[0]
		if card.SI7_minion:
			source._sidequest_counter_ += 1
			if source._sidequest_counter_==2:
				card = random.choice(['SW_052t5','SW_052t4','SW_052t7','SW_052t8_t','SW_052t6'])
				Give(source.controller, card).trigger(source)
				Summon(source.controller, 'SW_052t2')
				Destroy(source).trigger(source)
class SW_052t:# <7>[1578]
	""" Learn the Truth
	[Questline:] Play 2SI:7 cards.[Reward:] Add a Spy Gizmo to your hand. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}	#
	events = Play(CONTROLLER).on(SW_052_Quest2(Play.CARD))
	pass
class SW_052_Quest3(TargetedAction):
	CARD=ActionArg()
	def do(self, source, card):
		if isinstance(card, list):
			card = card[0]
		if card.SI7_minion:
			source._sidequest_counter_ += 1
			if source._sidequest_counter_==2:
				card = random.choice(['SW_052t5','SW_052t4','SW_052t7','SW_052t8_t','SW_052t6'])
				Summon(source.controller, 'SW_052t3').trigger(source)
				Destroy(source).trigger(source)
class SW_052t2:# <7>[1578]
	""" Marked a Traitor
	[Questline:] Play 2SI:7 cards.[Reward:] Spymaster Scabbs. """
	tags={GameTag.SIDEQUEST:True, GameTag.QUESTLINE:True}	#
	events = Play(CONTROLLER).on(SW_052_Quest3(Play.CARD))
	pass
class SW_052t3:# <7>[1578]
	""" Spymaster Scabbs
	[Battlecry:] Add one ofeach Spy Gizmo to your hand. """
	def play(self):
		card = random.choice(['SW_052t5','SW_052t4','SW_052t7','SW_052t8_t','SW_052t6'])
		Give(self.controller, 'SW_052t3').trigger(self)
	pass

class SW_052t4:# <7>[1578]
	""" Fizzflash Distractor
	Return an enemy minion to its owner's hand.They can't play it next turn. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = Bounce(TARGET).on(Buff(Bounce.TARGET, 'SW_052t4e'))
	pass

class SW_052t4e:# <7>[1578]
	""" Distracted
	Can't be played. """
	tags = {GameTag.CANT_PLAY:1}
	events = OWN_TURN_END.on(Destroy(SELF))
	pass


class SW_052t5_Choice(Choice):
	def choose(self, card):
		super().choose(card)
		for cd in self.source.controller.opponent.deck:
			if cd.id==card.id:
				cd.zone=Zone.GRAVEYARD## discard
				break
		card.zone=Zone.DECK
		# card.controller.deck.append(card)
class SW_052t5:# <7>[1578]
	""" Spy-o-matic
	[Battlecry:] Look at 3 cards in your opponent's deck. Pick one to put on top. """
	def play(self):
		cards=[card.id for card in self.controller.opponent.deck]
		SW_052t5_Choice(self.controller, RandomID(cards)*3).trigger(self)
	pass

class SW_052t6:# <7>[1578]
	""" Noggen-Fog Generator
	Give a minion +2 Attack and [Stealth]. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0}
	play = Buff(TARGET, 'SW_052t6e')#
	pass

class SW_052t6e:# <7>[1578]
	""" Noggen-Fog +2 Attack and [Stealth]. """
	tags ={GameTag.ATK:2, GameTag.STEALTH:True}
	pass

class SW_052t7:# <7>[1578]
	""" Hidden Gyroblade
	[Deathrattle:] Throw this at a random enemy minion. """
	deathrattle = Hit(RANDOM(ENEMY_MINIONS), 3)
	pass

class SW_052t8_t:# <7>[1578]
	""" Undercover Mole
	[Stealth]. After this attacks,add a random card toyour hand <i>(from youropponent's class).</i> """
	events = Attack(SELF).after(Give(CONTROLLER, RandomCollectible(card_class=CARDCLASS(OPPONENT))))
	pass




if StormWind_Counterfeit_Blade:# ### OK 
	StormWind_Rogue+=['SW_310']
	StormWind_Rogue+=['SW_310e']
class SW_310:# <7>[1578]
	""" Counterfeit Blade
	[Battlecry:] Gain a random friendly [Deathrattle] that_triggered this game. """
	def play(self):
		actions=[action for action in self.controller._targetedaction_log if\
			isinstance(action['class'], Deathrattle) ]
		if len(actions)>0:
			action = random.choice(actions)
			new_deathrattles = action['target'].deathrattles
			ret = new_deathrattles[0]
			self.has_deathrattle=True
			self.data.tags[GameTag.DEATHRATTLE]=True
			self.data.scripts.deathrattle=tuple(ret)
			print("Copy [deathrattle] %s->%s"%(action['target'], self))
	pass

class SW_310e:# <7>[1578]
	""" Counterfeit Blade
	Copied [Deathrattle] from {0}. """
	tags = {GameTag.DEATHRATTLE:True}
	pass




if StormWind_Garrote:# ### OK
	StormWind_Rogue+=['SW_311']
	StormWind_Rogue+=['SW_311t']
class SW_311:# <7>[1578]
	""" Garrote
	Deal $2 damage to the enemy hero. Shuffle 2 Bleeds into your deck that deal $2 more when drawn. """
	play = Hit(ENEMY_HERO, 2), Shuffle(CONTROLLER, 'SW_311t') * 2
	pass

class SW_311t:# <7>[1578]
	""" Bleed
	[Casts When Drawn]Deal $2 damage to the enemy hero. """
	#<Tag enumID="1077" name="CASTSWHENDRAWN" type="Int" value="1"/>
	play = Hit(ENEMY_HERO, 2)
	pass




if StormWind_Sketchy_Information:# 
	StormWind_Rogue+=['SW_405']
class SW_405:# <7>[1578] spell(3)
	""" Sketchy Information
	Draw a [Deathrattle] card that costs (4) or less.Trigger its [Deathrattle.] """
	def play(self):
		newcard = Give(self.controller, RandomDeathrattle(cost=[1,2,3,4])).trigger(self)
		newcard=newcard[0][0]
		action = newcard.deathrattles[0]
		action.trigger(self)
	pass




if StormWind_SI7_Informant:# 
	StormWind_Rogue+=['SW_411']
	StormWind_Rogue+=['SW_411e']
class SW_411:# <7>[1578]
	""" SI:7 Informant
	[Battlecry:] Gain +1/+1 for each other SI:7 card you've played this game. """
	def play(self):
		cards = [card for card in self.controller.play_log if card.SI7_minion==True]
		Buff(self, 'SW_411e', atk=len(cards), max_health=len(cards))
	pass
class SW_411e:# <7>[1578]
	""" Well Informed 	+1/+1 """
	pass




if StormWind_SI7_Extortion:# 
	StormWind_Rogue+=['SW_412']
class SW_412:# <7>[1578]
	""" SI:7 Extortion
	[Tradeable]Deal $3 damage to an undamaged character. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0, PlayReq.REQ_UNDAMAGED_TARGET: 0}
	play = Hit(TARGET, 3)
	#
	pass




if StormWind_SI7_Operative:# 
	StormWind_Rogue+=['SW_413']
class SW_413:# <7>[1578]
	""" SI:7 Operative
	[Rush]After this attacks a minion, gain [Stealth]. """
	events = Attack(SELF, ENEMY_MINIONS).after(SetAttr(SELF, 'stealth', True))
	pass




if StormWind_SI7_Assassin:# 
	StormWind_Rogue+=['SW_417']
class SW_417:# <7>[1578]
	""" SI:7 Assassin
	Costs (1) less for each SI:7card you've played this game.[Combo:] Destroy anenemy minion. """
	cost_mod = -Count((FRIENDLY_MINIONS | FRIENDLY_KILLED) + SI7_MINION)
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	combo = Destroy(TARGET)
	pass




if StormWind_Loan_Shark:# 
	StormWind_Rogue+=['SW_434']
class SW_434:# <7>[1578]
	""" Loan Shark
	[Battlecry:] Give youropponent a Coin.__[Deathrattle:] You get two. """
	play = Give(OPPONENT, 'GAME_005')
	deathrattle = Give(CONTROLLER, 'GAME_005') * 2
	pass


