from ..utils import *

Rev_Rogue=[]

Rev_Perjury=True
Rev_Murder_Accusation=True
Rev_Scribbling_Stenographer=True
Rev_Sinstone_Graveyard=True
Rev_Double_Cross=True
Rev_Private_Eye=True
Rev_Sticky_Situation=True
Rev_Kidnap=True
Rev_Halkias=True
Rev_Door_of_Shadows=True
Rev_Serrated_Bone_Spike=True
Rev_Necrolord_Draka=True
Rev_Ghastly_Gravedigger=True


if Rev_Perjury:# ###
	Rev_Rogue+=['MAW_018']
class MAW_018_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		CastSecret(card).trigger(self)
class MAW_018:# <7>[1691]
	""" Perjury
	<b>Secret:</b> When your turn starts, <b>Discover</b> and cast a <b>Secret</b> from another class. """
	secret = BeginTurn(CONTROLLER).on(
		Reveal(SELF),
		MAW_018_Choice(CONTROLLER, RandomSecret(card_class=CLASSES_EXCEPT_ROGUE))
		)
	pass

if Rev_Murder_Accusation:# ###
	Rev_Rogue+=['MAW_019']
	Rev_Rogue+=['MAW_019e']
class MAW_019:# <7>[1691]
	""" Murder Accusation
	Choose a minion. Destroy it after another enemy minion dies. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }	#
	play = Buff(TARGET, 'MAW_019e')
	pass
class MAW_019e:# <7>[1691]
	""" Murder Trial
	When another enemy minion dies, destroy the accused. """
	events = Death(FRIENDLY + MINION - SELF).after(Destroy(OWNER))
	pass
#	Rev_Rogue+=['MAW_019e2']
#class MAW_019e2:# <7>[1691]
#	""" Accused of Murder
#	When an enemy minion of the accuser dies, this minion dies. """
#	#
#	pass

if Rev_Scribbling_Stenographer:# ###
	Rev_Rogue+=['MAW_020']
class MAW_020_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		source.cost_mod=-len(controller.play_this_turn)
		pass
class MAW_020:# <7>[1691]
	""" Scribbling Stenographer
	<b>Rush</b>. Costs (1) less for each card you've played this turn. """
	class Hand:
		events = Play(CONTROLLER).on(MAW_020_Action(CONTROLLER))
	pass




if Rev_Sinstone_Graveyard:# ### location ###
	Rev_Rogue+=['REV_750']
	Rev_Rogue+=['REV_750t2']
class REV_750_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		amount = len(controller.play_this_turn)
		card = Summon(controller,'REV_750t2').trigger(source)
		card = card[0][0]
		card.atk+=amount
		card.max_health+=amount
		pass
class REV_750:# <7>[1691]
	""" Sinstone Graveyard
	Summon a @/@ <b>Stealthed</b> Ghost. <i>(Has +1/+1 for each other card you played this turn!)</i> """
	location = REV_750_Action(CONTROLLER)
	pass
class REV_750t2:# <7>[1691]
	""" Haunted Conscience
	<b>Stealth</b> """
	#
	pass




#if Rev_Necrolord_Draka:# 
#	Rev_Rogue+=['REV_785']
#class REV_785:# <7>[1691]
#	""" Necrolord Draka
#	{0} {1} {2} {3} """
#	#
#	pass
#if Rev_Sinstone_Graveyard:# 
#	Rev_Rogue+=['REV_795']
#class REV_795:# <7>[1691]
#	""" Sinstone Graveyard
#	{0} {1} """
#	#
#	pass




if Rev_Double_Cross:# ###
	Rev_Rogue+=['REV_825']
class REV_825:# <7>[1691]
	""" Double Cross
	<b>Secret:</b> When your opponent spends all their Mana, draw two cards. """
	secret = SpendMana(OPPONENT, MANA(OPPONENT)).after(Reveal(SELF, Draw(CONTROLLER), Draw(CONTROLLER)))
	pass




if Rev_Private_Eye:# 
	Rev_Rogue+=['REV_826']
class REV_826:# <7>[1691]
	""" Private Eye
	<b>Battlecry:</b> Cast a <b>Secret</b> from your deck. _<b>Combo:</b> Cast 2 instead. """
	play = CastSecret(RANDOM(FRIENDLY_DECK+SECRET))
	combo = (CastSecret(RANDOM(FRIENDLY_DECK+SECRET)), CastSecret(RANDOM(FRIENDLY_DECK+SECRET)))
	pass




if Rev_Sticky_Situation:# ###
	Rev_Rogue+=['REV_827']
	Rev_Rogue+=['REV_827t']
class REV_827:# <7>[1691]
	""" Sticky Situation
	<b>Secret:</b> After your opponent casts a spell, summon a 3/4 Spider with <b>Stealth</b>. """
	secret = Play(OPPONENT, SPELL).after(Reveal(SELF), Summon(CONTROLLER, 'REV_827t'))
	pass
class REV_827t:# <7>[1691]
	""" Tomb Crawler
	<b>Stealth</b> """
	#
	pass




if Rev_Kidnap:# ###
	Rev_Rogue+=['REV_828']
	Rev_Rogue+=['REV_828e']
	Rev_Rogue+=['REV_828t']
class REV_828_Action(TargetedAction):
	CONTROLLER=ActionArg()
	CARD=CardArg()
	def do(self, source, controller, card):
		newcard=Summon(controller, 'REV_828t').trigger(source)
		newcard=newcard[0][0]
		newcard.script_data_num_1=card.id
		card.discard()
		pass
class REV_828:# <7>[1691]
	""" Kidnap
	<b>Secret:</b> After your opponent plays a minion, stuff it in a 0/4 Sack. """
	secret = Play(OPPONENT, MINION).after(Reveal(SELF), REV_828_Action(CONTROLLER, Play.CARD))
	pass

class REV_828e:# <7>[1691]
	""" Kidnapper's Sack
	{0} is inside the sack! """
	#
	pass
class REV_828t_Action(TargetedAction):
	CONTROLLER=ActionArg()
	CARD=CardArg()
	def do(self, source, controller, card):
		Give(controller, source.script_data_num_1).trigger(source)
class REV_828t:# <7>[1691]
	""" Kidnapper's Sack
	<b>Deathrattle:</b> Return your opponent's kidnapped minion to their hand. """
	deathrattle = REV_828t_Action(CONTROLLER)
	pass




if Rev_Halkias:# ###
	Rev_Rogue+=['REV_829']
	Rev_Rogue+=['REV_829e']
class REV_829_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		if len(controller.secrets)>0:
			secret=random.choice(controller.secrets)
			Buff(secret, 'REV_829e').trigger(source)
		pass
class REV_829:# <7>[1691]
	""" Halkias
	<b>Stealth</b>. <b>Deathrattle:</b> Store Halkias's soul inside of a friendly <b>Secret</b>. It resummons Halkias when triggered. """
	deathrattle = REV_829_Action(CONTROLLER)
	pass
class REV_829e:# <7>[1691]
	""" Shard of Halkias
	Contains Halkias' soul. """
	events = Reveal(OWNER).on(Summon(CONTROLLER, 'REV_829'))
	pass




if Rev_Door_of_Shadows:# ###
	Rev_Rogue+=['REV_938']
	Rev_Rogue+=['REV_938t']
	Rev_Rogue+=['REV_938te']
class REV_938:# <7>[1691]
	""" Door of Shadows
	Draw a spell. <b>Infuse (@):</b> Add a temporary copy of it to your hand. """
	play = Give(CONTROLLER, RANDOM(FRIENDLY_DECK + SPELL))
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_938t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_938t', 1))
	pass

class REV_938t:# <7>[1691]
	""" Door of Shadows
	<b>Infused</b> Draw a spell. Add a temporary copy of it to your hand. """
	def play(self):
		controller=self.controller
		source=self
		cards=[card for card in controller.deck]
		if len(cards)>0:
			card=random.choice(cards)
			newcard=controller.card(card.id)
			newcard.zone=Zone.HAND
			Buff(newcard,'REV_938te').trigger(source)
	pass

class REV_938te:# <7>[1691]
	""" Shadowstalking
	Discard this at the end of your turn. """
	events = OWN_TURN_END.on(Destroy(OWNER))
	pass




if Rev_Serrated_Bone_Spike:# ###
	Rev_Rogue+=['REV_939']
	Rev_Rogue+=['REV_939e']
class REV_939:# <7>[1691]
	""" Serrated Bone Spike
	Deal $3 damage to a  minion. If it dies, your  next card this turn  costs (2) less. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }	
	def play(self):
		controller=self.controller
		source=self
		if self.target.health<=3:
			for hand in controller.hand:
				Buff(hand, 'REV_939e').trigger(source)
		Hit(self.target, 3).trigger(source)
	pass
class REV_939e:# <7>[1691]
	""" Serrated
	The next card you play this turn costs (2) less. """
	cost=lambda self,i:max(0,i-2)
	tags = {GameTag.TAG_ONE_TURN_EFFECT:1 }
	events = Play(CONTROLLER, FRIENDLY).on(Destroy(SELF))
	pass
#	Rev_Rogue+=['REV_939e2']
#class REV_939e2:# <7>[1691]
#	""" Serrated
#	Your next card this turn costs (2) less. """
#	#
#	pass




if Rev_Necrolord_Draka:# ###
	Rev_Rogue+=['REV_940']
class REV_940:# <7>[1691]
	""" Necrolord Draka
	<b>Battlecry:</b> Equip a @/3 Dagger.  <i>(+1 Attack for each other  card you played this turn!)</i> """
	def play(self):
		controller=self.controller
		source=self
		amount = len(controller.play_this_turn)
		card=Summon(controller, 'REV_940t').trigger(source)
		card=card[0][0]
		card.atk += amount
	pass
	Rev_Rogue+=['REV_940t']
class REV_940t:# <7>[1691]
	""" Maldraxxus Dagger
	 """
	#
	pass




if Rev_Ghastly_Gravedigger:# ###
	Rev_Rogue+=['REV_959']
class REV_959:# <7>[1691]
	""" Ghastly Gravedigger
	<b>Battlecry:</b> If you control a <b>Secret</b>, choose a card in your opponent's hand to _shuffle into their deck. """
	def play(self):
		source=self
		controller=self.controller
		if len(controller.opponent.hand)>0:
			card=random.choice(controller.opponent.hand)
			card.zone=Zone.SETASIDE
			card.zone=Zone.DECK
			controller.opponent.deck.shuffle()
	pass

