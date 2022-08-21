
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
	[Tradeable]After you [Trade] this,reduce the cost of a spellin your hand by (1). """
	#
	pass

class DED_004e:# <7>[1578]
	""" Blackwater Treasure
	Costs (1) less. """
	#
	pass




if StormWind_Parrrley:# 
	StormWind_Rogue+=['DED_005']
class DED_005:# <7>[1578]
	""" Parrrley
	Swap this for a card in your opponent's deck. """
	#
	pass




if StormWind_Edwin_Defias_Kingpin:# 
	StormWind_Rogue+=['DED_510']
	StormWind_Rogue+=['DED_510e']
	StormWind_Rogue+=['DED_510e2']
class DED_510:# <7>[1578]
	""" Edwin, Defias Kingpin
	[Battlecry:] Draw a card. If youplay it this turn, gain +2/+2and repeat this effect. """
	#
	pass

class DED_510e:# <7>[1578]
	""" Defias Supplies
	If played this turn, draw a card and give Edwin +2/+2. """
	#
	pass

class DED_510e2:# <7>[1578]
	""" King of the Brotherhood
	Increased stats. """
	#
	pass




if StormWind_Maestra_of_the_Masquerade:# 
	StormWind_Rogue+=['SW_050']
class SW_050:# <7>[1578]
	""" Maestra of the Masquerade
	You start the game as a different class until you play a Rogue card. """
	#
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
	play = Bounce(TARGET).on(Buff(Bounce.CARD, 'SW_052t4e'))
	pass

class SW_052t4e:# <7>[1578]
	""" Distracted
	Can't be played. """
	tags = {GameTag.CANT_PLAY:1}
	events = OWN_TURN_END.on(Destroy(SELF))
	pass

class SW_052t5:# <7>[1578]
	""" Spy-o-matic
	[Battlecry:] Look at 3 cards in your opponent's deck. Pick one to put on top. """
	
	pass

class SW_052t6:# <7>[1578]
	""" Noggen-Fog Generator
	Give a minion +2 Attack and [Stealth]. """
	#
	pass

class SW_052t6e:# <7>[1578]
	""" Noggen-Fog
	+2 Attack and [Stealth]. """
	#
	pass

class SW_052t7:# <7>[1578]
	""" Hidden Gyroblade
	[Deathrattle:] Throw this at a random enemy minion. """
	#
	pass

class SW_052t8_t:# <7>[1578]
	""" Undercover Mole
	[Stealth]. After this attacks,add a random card toyour hand <i>(from youropponent's class).</i> """
	#
	pass




if StormWind_Counterfeit_Blade:# 
	StormWind_Rogue+=['SW_310']
	StormWind_Rogue+=['SW_310e']
class SW_310:# <7>[1578]
	""" Counterfeit Blade
	[Battlecry:] Gain a randomfriendly [Deathrattle] that_triggered this game. """
	#
	pass

class SW_310e:# <7>[1578]
	""" Counterfeit Blade
	Copied [Deathrattle] from {0}. """
	#
	pass




if StormWind_Garrote:# 
	StormWind_Rogue+=['SW_311']
	StormWind_Rogue+=['SW_311t']
class SW_311:# <7>[1578]
	""" Garrote
	Deal $2 damage to theenemy hero. Shuffle 2Bleeds into your deck thatdeal $2 more when drawn. """
	#
	pass

class SW_311t:# <7>[1578]
	""" Bleed
	[Casts When Drawn]Deal $2 damage to the enemy hero. """
	#
	pass




if StormWind_Sketchy_Information:# 
	StormWind_Rogue+=['SW_405']
class SW_405:# <7>[1578]
	""" Sketchy Information
	Draw a [Deathrattle] cardthat costs (4) or less.Trigger its [Deathrattle.] """
	#
	pass




if StormWind_SI7_Informant:# 
	StormWind_Rogue+=['SW_411']
	StormWind_Rogue+=['SW_411e']
class SW_411:# <7>[1578]
	""" SI:7 Informant
	[Battlecry:] Gain +1/+1 for each other SI:7 card you've played this game. """
	#
	pass

class SW_411e:# <7>[1578]
	""" Well Informed
	+1/+1 """
	#
	pass




if StormWind_SI7_Extortion:# 
	StormWind_Rogue+=['SW_412']
class SW_412:# <7>[1578]
	""" SI:7 Extortion
	[Tradeable]Deal $3 damage to an undamaged character. """
	#
	pass




if StormWind_SI7_Operative:# 
	StormWind_Rogue+=['SW_413']
class SW_413:# <7>[1578]
	""" SI:7 Operative
	[Rush]After this attacks a minion, gain [Stealth]. """
	#
	pass




if StormWind_SI7_Assassin:# 
	StormWind_Rogue+=['SW_417']
class SW_417:# <7>[1578]
	""" SI:7 Assassin
	Costs (1) less for each SI:7card you've played this game.[Combo:] Destroy anenemy minion. """
	#
	pass




if StormWind_Loan_Shark:# 
	StormWind_Rogue+=['SW_434']
class SW_434:# <7>[1578]
	""" Loan Shark
	[Battlecry:] Give youropponent a Coin.__[Deathrattle:] You get two. """
	#
	pass


