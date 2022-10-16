from ..utils import *

Rev_Mage=[]

Rev_Objection=True
Rev_Life_Sentence=True
Rev_Contract_Conjurer=True
Rev_Suspicious_Alchemist=False### difficult
Rev_Solid_Alibi=True
Rev_Cold_Case=True
Rev_Chatty_Bartender=True
Rev_KelThuzad_the_Inevitable=True
Rev_Orion_Mansion_Manager=True
Rev_Vengeful_Visage=True
Rev_Frozen_Touch=True
Rev_Nightcloak_Sanctum=True
Rev_Deathborne=True


if Rev_Objection:# ### 
	Rev_Mage+=['MAW_006']
class MAW_006:# <4>[1691]
	""" Objection!
	<b>Secret:</b> When your opponent plays a _minion, <b>Counter</b> it. """
	secret = Play(OPPONENT, MINION).after(Counter(Play.CARD))
	pass




if Rev_Life_Sentence:# ### 
	Rev_Mage+=['MAW_013']
class MAW_013:# <4>[1691]
	""" Life Sentence
	Remove a minion from the game. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = Destroy(TARGET)
	pass




if Rev_Contract_Conjurer:# ### 
	Rev_Mage+=['MAW_101']
class MAW_101:# <4>[1691]
	""" Contract Conjurer
	Costs (3) less for each <b>Secret</b> you control. """
	cost_mod = - Count(FRIENDLY_SECRETS) * 3
	pass




if Rev_Suspicious_Alchemist:# ### 
	Rev_Mage+=['REV_000']
	Rev_Mage+=['REV_000e']
class REV_000_Choice(Choice):
	def do(self, source, player, cards, option=None):
		self.source.sidequest_list0=[[card.id for card in cards]]
		super().do(source, player, cards, option)
	def choose(self, card):
		self.next_choice=None
		self.source.sidequest_list0.append(card.id)
		super().choose(card)
class REV_000:# <4>[1691]
	""" Suspicious Alchemist
	<b>Battlecry:</b> <b>Discover</b> a spell. If your opponent guesses your choice, they get a copy. """
	def play(self):
		source=self
		controller=self.controller
		opponent=controller.opponent
		choice=REV_000_Choice(controller, RandomSpell()*3)
		choice.trigger(source)
		buff=Buff(opponent, 'REV_000e')
		buff.trigger(source)
		enchant=buff.BUFF.evaluate(source)
		enchant.sidequest_list0=[self.sidequest_list0[0],self.sidequest_list0[1]]
		pass
	pass
class REV_000e_Choice(Choice):
	def choose(self, card):
		source = self.source
		answer=source.sidequest_list0[1]
		if card.id==answer:
			card.zone=Zone.SETASIDE
			card.controller=source.controller
			card.zone=Zone.HAND
		pass
class REV_000e_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		REV_000e_Choice(controller, RandomID(*(source.sidequest_list0[0]))*3).trigger(source)
	pass
class REV_000e:# <4>[1691]
	""" A Mystery!
	At the start of your turn, guess what card your opponent chose to get a copy of it. """
	events = BeginTurn(CONTROLLER).on(REV_000e_Action(CONTROLLER))
	pass




if Rev_Solid_Alibi:# 
	Rev_Mage+=['REV_504']
class REV_504:# <4>[1691]
	""" Solid Alibi
	Until your next turn, your hero can only take 1 damage at a time. """
	play = Buff(FRIENDLY_HERO, 'REV_504e'), SetAttr(FRIENDLY_HERO, 'take_only_one_damage', True)
	pass
	Rev_Mage+=['REV_504e']
class REV_504e:# <4>[1691]
	""" Solid Alibi
	Your hero only takes 1 damage at a time until the start of your next turn. """
	events = BeginTurn(CONTROLLER).on(SetAttr(FRIENDLY_HERO, 'take_only_one_damage', False), Destroy(SELF))
	pass




if Rev_Cold_Case:# ### 
	Rev_Mage+=['REV_505']
class REV_505:# <4>[1691]
	""" Cold Case
	Summon two 2/2 Volatile Skeletons. Gain 4 Armor. """
	play = Summon(CONTROLLER, 'REV_845'), Summon(CONTROLLER, 'REV_845'), GainArmor(FRIENDLY_HERO)
	pass




if Rev_Chatty_Bartender:# ### 
	Rev_Mage+=['REV_513']
class REV_513_Action(TargetedAction):
	CONTROLLER=ActionArg()
	def do(self, source, controller):
		if len(controller.secrets)>0:
			for card in controller.opponent.characters:
				Hit(card, 2).trigger(source)
		pass
class REV_513:# <4>[1691]
	""" Chatty Bartender
	At the end of your turn, if you control a <b>Secret</b>, deal 2 damage to all enemies. """
	events = OWN_TURN_END.on(REV_513_Action(CONTROLLER))
	pass




if Rev_KelThuzad_the_Inevitable:# ### 
	Rev_Mage+=['REV_514']
class REV_514:# <4>[1691]
	""" Kel'Thuzad, the Inevitable
	<b>Battlecry:</b> Resurrect your  Volatile Skeletons. Any that  can't fit on the battlefield  instantly explode! @<i>(@)</i> """
	def play(self):
		source = self
		controller = self.controller
		amount = len([card for card in controller.death_log if card.id=='REV_845'])
		amount1 = 7-len(controller.field)
		amount2=amount-amount1
		for repeat in range(amount1):
			Summon(controller, 'REV_845').trigger(source)
		for repeat in range(amount2):
			target = random.choice(controller.opponent.characters)
			Hit(target, 2)
	pass




if Rev_Orion_Mansion_Manager:# 
	Rev_Mage+=['REV_515']
	Rev_Mage+=['REV_515e']
class REV_515_Action(TargetedAction):
	CONTROLLER=ActionArg()
	CARD=CardArg()
	def do(self, source, controller,card):
		while True:
			newcard = RandomSecret(card_class=CardClass.MAGE).evaluate(source)
			newcard = newcard[0]
			if newcard.id!=card.id:
				break
		Buff(newcard, 'REV_515e').trigger(source)
		pass
class REV_515:# <4>[1691]
	""" Orion, Mansion Manager
	After a friendly <b>Secret</b> is revealed, cast a different Mage <b>Secret</b> and gain +2/+2. """
	events =Reveal(FRIENDLY + SECRET).after(REV_515_Action(CONTROLLER, Reveal.TARGET))
	pass
REV_515e=buff(2,2)




if Rev_Vengeful_Visage:# ### 
	Rev_Mage+=['REV_516']
class REV_516_Action(TargetedAction):
	CONTROLLER=ActionArg()
	ATTACKER=ActionArg()
	def do(self, source, controller, attacker):
		card = Summon(controller, attacker.id).trigger(source)
		card=card[0][0]
		Attack(card, controller.opponent.hero).trigger(source)
		pass
class REV_516:# <4>[1691]
	""" Vengeful Visage
	<b>Secret:</b> After an enemy minion attacks your hero, summon a copy of it to attack the enemy hero. """
	secret = Attack(ENEMY+MINION, FRIENDLY_HERO).after(Reveal(SELF), REV_516_Action(CONTROLLER, Attack.ATTACKER))
	pass




if Rev_Frozen_Touch:# ### 
	Rev_Mage+=['REV_601']
	Rev_Mage+=['REV_601t']
class REV_601:# <4>[1691]
	""" Frozen Touch
	Deal $3 damage. 
	<b>Infuse (@):</b> Add a Frozen Touch to your hand. """
	class Hand:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_601t'))
	class Deck:
		events = Death(FRIENDLY+MINION).on(Infuse(CONTROLLER, 'REV_601t', 1))
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = Hit(TARGET, 3)#
	pass

class REV_601t:# <4>[1691]
	""" Frozen Touch
	<b>Infused</b> Deal $3 damage.  Add a Frozen Touch  to your hand. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = Hit(TARGET, 3), Give(CONTROLLER, 'REV_601')#
	#
	pass



if Rev_Nightcloak_Sanctum:# ### location ###
	Rev_Mage+=['REV_602']
class REV_602:# <4>[1691]
	""" Nightcloak Sanctum
	<b>Freeze</b> a minion. Summon a 2/2 Volatile Skeleton(REV_845). """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }	
	location = Freeze(TARGET), Summon(CONTROLLER, 'REV_845')
	pass



#if Rev_KelThuzad_the_Inevitable:# 
#	Rev_Mage+=['REV_786']
#class REV_786:# <4>[1691]
#	""" Kel'Thuzad, the Inevitable
#	{0} {1} {2} {3} """
#	#
#	pass
#
#if Rev_Nightcloak_Sanctum:# 
#	Rev_Mage+=['REV_796']
#class REV_796:# <4>[1691]
#	""" Nightcloak Sanctum
#	{0} {1} """
#	#
#	pass

if Rev_Deathborne:# 
	Rev_Mage+=['REV_840']
class REV_840:# <4>[1691]
	""" Deathborne
	Deal $2 damage to all minions. Summon a 2/2 Volatile Skeleton  for each killed. """
	def play(self):
		source = self
		controller = self.controller
		for card in controller.opponent.characters:
			Hit(card, 2).trigger(source)
		controller.game.process_deaths()
		amount = len(controller.opponent.death_this_turn)
		for repeat in amount:
			Summon(controller, 'REV_845').trigger(source)
	pass



