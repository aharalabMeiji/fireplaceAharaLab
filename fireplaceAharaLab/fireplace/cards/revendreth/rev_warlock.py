from ..utils import *

Rev_Warlock=[]

Rev_Imp_oster=True
Rev_Arson_Accusation=True
Rev_Habeas_Corpses=True
Rev_Suffocating_Shadows=True
Rev_Tome_Tampering=True
Rev_Flustered_Librarian=True
Rev_Mischievous_Imp=True
Rev_Impending_Catastrophe=True
Rev_Vile_Library=True
Rev_Shadow_Waltz=True
Rev_Lady_Darkvein=True
Rev_Shadowborn=True
Rev_Imp_King_Rafaam=True


if Rev_Imp_oster:# ###
	Rev_Warlock+=['MAW_000']
class MAW_000:# <9>[1691]
	""" Imp-oster
	<b>Battlecry:</b> Choose a friendly Imp. Transform into a copy of it. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, 1005:0 }
	#req == 1005:## PlayReq.REQ_TARGET_IMP:
	def play(self):
		Morph(self, self.target.id).trigger(self)
	pass




if Rev_Arson_Accusation:# ###
	Rev_Warlock+=['MAW_001']
	Rev_Warlock+=['MAW_001e']
class MAW_001:# <9>[1691]
	""" Arson Accusation
	Choose a minion. Destroy it after your hero takes damage. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = Buff(TARGET, 'MAW_001e')	
	pass
class MAW_001e:# <9>[1691]
	""" Arson Trial
	When your hero takes damage, destroy the accused. """
	events = Hit(FRIENDLY_HERO).after(Destroy(OWNER))
	pass
#	Rev_Warlock+=['MAW_001e2']
#class MAW_001e2:# <9>[1691]
#	""" Accused of Arson
#	When the accuser takes damage, this minion dies. """
#	#
#	pass




if Rev_Habeas_Corpses:# ###
	Rev_Warlock+=['MAW_002']
	Rev_Warlock+=['MAW_002e']
class MAW_002_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		card.rush=True
		card.zone=Zone.PLAY#ressurect
class MAW_002:# <9>[1691]
	""" Habeas Corpses
	<b>Discover</b> a friendly minion to resurrect and give it <b>Rush</b>. It dies at the end of turn. """
	def play(self):
		controller=self.controller
		cards=[card.id for card in controller.death_log]
		MAW_002_Choice(controller, RandomID(*cards)*3).trigger(self)
	pass
class MAW_002e:# <9>[1691]
	""" Habeas Corpse
	Dies at the end of turn. """
	events = OWN_TURN_END.on(Destroy(OWNER))
	pass




if Rev_Suffocating_Shadows:# ###
	Rev_Warlock+=['REV_239']
class REV_239:# <9>[1691]
	""" Suffocating Shadows
	When you play or  discard this, destroy a  random enemy minion. """
	play = Destroy(RANDOM(ENEMY_MINIONS))
	events = Destroy(SELF).on(Destroy(RANDOM(ENEMY_MINIONS)))
	pass

#	Rev_Warlock+=['REV_239e']
#class REV_239e:# <9>[1691]
#	""" Suffocation
#	Costs (3) less. """
#	#
#	pass




if Rev_Tome_Tampering:# ###
	Rev_Warlock+=['REV_240']
	Rev_Warlock+=['REV_240e']
class REV_240:# <9>[1691]
	""" Tome Tampering
	Shuffle 1-Cost  copies of cards in your  hand into your deck,  then discard your hand. """
	def play(self):
		controller=self.controller
		for card in reversed(controller.hand):
			Buff(card,'REV_240e').trigger(self)
			card.zone=Zone.SETASIDE
			card.zone=Zone.DECK
		random.shuffle(controller.deck)
	pass
class REV_240e:# <9>[1691]
	""" Cost Curse
	Costs (1). """
	cost = lambda self, i: 1
	pass




if Rev_Flustered_Librarian:# 
	Rev_Warlock+=['REV_242']
class REV_242:# <9>[1691]
	""" Flustered Librarian (maybe an aura-buff?)
	Has +1 Attack for each Imp you control. """
	def play(self):
		controller=self.controller
		amount = len([card for card in controller.field if getattr(card, 'imp', 0)])
		self.atk += amount
	pass




if Rev_Mischievous_Imp:# ###
	Rev_Warlock+=['REV_244']
	Rev_Warlock+=['REV_244t']
class REV_244:# <9>[1691]
	""" Mischievous Imp
	<b>Battlecry:</b> Summon a copy of this. <b>Infuse (@):</b> Summon two copies instead. """
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_244t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_244t', 1))
	play = Summon(CONTROLLER, Copy(SELF))
	pass

class REV_244t:# <9>[1691]
	""" Mischievous Imp
	<b>Infused Battlecry:</b> Summon two  copies of this. """
	play = Summon(CONTROLLER, Copy(SELF)), Summon(CONTROLLER, Copy(SELF))
	pass




if Rev_Impending_Catastrophe:# ###
	Rev_Warlock+=['REV_245']
class REV_245:# <9>[1691]
	""" Impending Catastrophe
	Draw a card. Repeat for each Imp you control. """
	def play(self):
		controller=self.controller
		amount = len([card for card in controller.field if getattr(card, 'imp', 0)])
		for repeat in range(amount+1):
			Draw(controller).trigger(self)
	pass




if Rev_Vile_Library:# ###
	Rev_Warlock+=['REV_371']
	Rev_Warlock+=['REV_371e']
class REV_371_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		amount = len([card for card in controller.field if getattr(card, 'imp', 0)])
		if amount>0:
			Buff(self.target, 'REV_371e', atk=amount, max_health=amount).triger(source)
		pass
class REV_371:# <9>[1691]
	""" Vile Library
	Give a friendly minion +1/+1 for each Imp you control. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	location = REV_371_Action(CONTROLLER)
	pass
class REV_371e:
	pass




if Rev_Shadow_Waltz:# ###
	Rev_Warlock+=['REV_372']
	Rev_Warlock+=['REV_372t']
class REV_372:# <9>[1691]
	""" Shadow Waltz
	Summon a 3/5 Shadow with <b>Taunt</b>. If a minion died this turn, summon another. """
	def play(self):
		controller=self.controller
		Summon(controller, 'REV_372t').trigger(self)
		if len(controller.death_this_turn)>0:
			Summon(controller, 'REV_372t').trigger(self)
	pass
class REV_372t:# <9>[1691]
	""" Twirling Shadow
	<b>Taunt</b> """
	#
	pass




if Rev_Lady_Darkvein:# 
	Rev_Warlock+=['REV_373']
	Rev_Warlock+=['REV_373e']
	Rev_Warlock+=['REV_373t']
class REV_373:# <9>[1691]
	""" Lady Darkvein
	<b>Battlecry:</b> Summon two 2/1 Shades. Each gains a <b>Deathrattle</b> to cast your  last Shadow spell. """
	def play(self):
		controller=self.controller
		for repeat in range(2):
			shade = Summon(controller, 'REV_373t').trigger(self)
			shade=shade[0][0]
			shadows=[card for card in controller.play_log if card.type==CardType.SPELL and card.spell_school==SpellSchool.SHADOW]
			if len(shadows)>0:
				lastshadow=shadows[-1]
				buff=Buff(shade,'REV_373e')
				buff.script_data_0=lastshadow.id
	pass
class REV_373t_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		buff=source.script_data_text_0
		card=controller.card(buff)
		CastSpell(card).trigger(source)
	pass
class REV_373e:# <9>[1691]
	""" Dark Bidding
	Spell: {0} is inside! """
	tags={GameTag.DEATHRATTLE:1, }
	deathrattle=REV_373t_Action(CONTROLLER)
	pass
class REV_373t:# <9>[1691]
	""" Shadow Manifestation
	 """
	#
	pass




if Rev_Shadowborn:# 
	Rev_Warlock+=['REV_374']
	Rev_Warlock+=['REV_374e']
class REV_374:# <9>[1691]
	""" Shadowborn
	<b>Deathrattle:</b> Reduce the Cost of the highest Cost Shadow spell in your hand by (3). """
	def play(self):
		controller=self.controller
		high=[]
		for card in controller.hand:
			if card.type==CardType.SPELL and card.spell_school==SpellSchool.SHADOW:
				if high==[] or high[0].cost<card.cost:
					high=[card]
				elif high[0].cost==card.cost:
					high.append(card)
		if len(high)>0:
			Buff(random.choice(high), 'REV_374e').trigger(self)
	#
	pass
class REV_374e:# <9>[1691]
	""" In Shadow
	Costs (3) less. """
	cost=lambda self, i:max(0, i-3)#
	pass

#if Rev_Imp_King_Rafaam:# 
#	Rev_Warlock+=['REV_789']
#class REV_789:# <9>[1691]
#	""" Imp King Rafaam
#	{0} {1} {2} {3} """
#	#
#	pass

#if Rev_Vile_Library:# 
#	Rev_Warlock+=['REV_799']
#class REV_799:# <9>[1691]
#	""" Vile Library
#	{0} {1} """
#	#
#	pass

if Rev_Imp_King_Rafaam:# 
	Rev_Warlock+=['REV_835']
	Rev_Warlock+=['REV_835e']
	Rev_Warlock+=['REV_835t']
class REV_835:# <9>[1691]
	""" Imp King Rafaam
	<b>Battlecry:</b> Resurrect four friendly Imps. <b>Infuse (@):</b> Give your Imps +2/+2. """
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_835t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_835t', 1))
	def play(self):
		controller=self.controller
		source=self
		cards=[card for card in controller.death_log if getattr(card,'imp',0)]
		if len(cards)>4:
			cards=random.sample(cards)
		for card in cards:
			Summon(controller, card.id).trigger(source)
REV_835e=buff(2,2)
class REV_835t:# <9>[1691]
	""" Imp King Rafaam
	<b>Infused.</b> <b>Battlecry:</b> Summon four friendly Imps that died this game. __Give your Imps +2/+2. """
	def play(self):
		controller=self.controller
		source=self
		cards=[card for card in controller.death_log if getattr(card,'imp',0)]
		if len(cards)>4:
			cards=random.sample(cards)
		for card in cards:
			newcard=Summon(controller, card.id).trigger(source)
			newcard=newcard[0][0]
			Buff(newcard,'REV_835e').trigger(source)
	pass

