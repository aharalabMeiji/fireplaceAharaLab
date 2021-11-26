from ..utils import *

class ALT_NEU1:
	""" Blood Guard (5/4/7)
	Whenever this minion takes damage, give your minions +1 Attack. """
	events = Attack(ALL_CHARACTERS,SELF).on(Buff(FRIENDLY_MINIONS,'ALT_NEU1e'))
	pass
ALT_NEU1 = buff(1,0)

class ALT_NEU2:##############
	""" Bunker Sergeant (3/2/4)
	[Battlecry]: If your opponent has 2 or more minions, deal 1 damage to all enemy minions."""
	pass

class ALT_NEU3:
	""" Direwolf Commander (3/2/5)
	[Honorable Kill]: Summon a 2/2 Wolf with Stealth """
	events = Predamage().on(HonorableKill(Predamage.TARGET, Predamage.AMOUNT, [Summon(CONTROLLER,'ALT_NEU3t')]))
	pass
class ALT_NEU3t:
	""" wolf """
	pass

class ALT_NEU4:
	""" Frantic Hippogryph (5/3/7)
	[Rush]. [Honorable Kill]: Gain [Windfury]. """
	events = Predamage().on(HonorableKill(Predamage.TARGET, Predamage.AMOUNT, [Buff(SELF,'ALT_NEU4e')]))
	pass
ALT_NEU4e = buff(windfury=True)

class ALT_NEU5:
	""" Frostwolf Warmaster (4/3/5)
	Costs (1) less for each card you've played this turn."""
	play = Buff(FRIENDLY_HAND,'ALT_NEU5e')
	pass
class ALT_NEU5e:
	cost = lambda self, i: max(i-1,0)
	events = OWN_TURN_END.on(Destroy(SELF))

class ALT_NEU6:
	""" Gankster (2/4/2)
	[Stealth] After your opponents plays a minion, attack it"""
	events = Play(OPPONENT, MINION).after(RegularAttack(SELF, Play.CARD))
	pass

class ALT_NEU_7:
	""" Herald of Lokholar (4/3/5)
	[Battlecry]: Draw a Frost spell."""
	play = Give(CONTROLLER, RANDOM(FRIENDLY + SPELL))
	pass

class ALT_NEU_8:
	"""Humongous Owl(7/8/4)
	Deathrattle: Deal 8 damage to a random enemy."""
	deathrattle = Hit(RANDOM(ENEMY_MINIONS), 8)
	pass

class ALT_NEU_9:
	""" Ice Revenant (4/4/5)
	Whenever you cast a Frost spell, gain +2/+2. """
	events = Play(CONTROLLER, SPELL+FROST).on(Buff(SELF,'ALT_NEU_9e'))
	pass
ALT_NEU_9e=buff(2,2)

class ALT_NEU_10:
	""" Icehoof Protector (6/2/10)
	[Taunt] [Freeze] any character damaged by this minion."""
	events = Attack(SELF, ALL_CHARACTERS).on(Buff(Attack.TARGET,'ALT_NEU_10e'))
	pass
ALT_NEU_10e=buff(frost=True)

class ALT_NEU_11:
	""" Irondeep Trogg (1/1/2)
	After your opponent casts a spell, summon a copy of this."""
	events = Play(OPPONENT, SPELL).on(Summon(CONTROLLER,ExactCopy(SELF)))
	pass

class ALT_NEU_12:
	""" Kobold Taskmaster (3/2/4)
	[Battlecry]: Add 2 Armor Scraps to your hand that give +2 Health to a minion."""
	Play = Give(CONTROLLER, 'ALT_NEU_12t') * 2
	pass

class ALT_NEU_13:##################
	""" Korrak the Bloodrager (4/3/5)
	Deathrattle: If this wasn't Honorably Killed, resummon Korrak."""
	pass

class ALT_NEU_14:
	""" Legionnaire (6/9/3)
	Deathrattle: Give all minions in your hand +2/+2. """
	deathrattle = Buff(FRIENDLY_HAND + MINION, 'ALT_NEU_14e')
	pass
ALT_NEU_14e = buff(2,2)

class ALT_NEU_15:
	""" Piggyback Imp (3/1/1) deamon
	Deathrattle: Summon a 4/1 Imp. """
	deathrattle = Summon(CONTROLLER,'ALT_NEU_15t')
	pass
class ALT_NEU_15t:
	""" 4/1 imp """
	pass

class ALT_NEU_16:
	""" Reflecto Engineer (3/2/4)
	[Battlecry]: Swap the Attack and Health of all minions in both players' hands."""
	def play(self):
		game = self.game
		cardlist = game.hands
		for card in cardlist:
			health = card.health
			atk = card.atk
			card.atk =health
			card.max_health = atk
			card.damage=0
	pass

class ALT_NEU_17:
	""" Ram Commander (2/2/2)
	[Battlecry]: Add two 1/1 Rams with Rush to your hand."""
	pass

class ALT_NEU_18:
	""" Snowblind Harpy (3/3/4)
	[Battlecry]: If you're holding a Frost spell, gain 5 Armor."""
	pass

class ALT_NEU_19:
	""" Stormpike Marshal (4/2/6)
	[Taunt] If you took 5 or more damage on your opponent's turn, this costs (1)."""
	pass

class ALT_NEU_20:
	""" Stormpike Quartermaster (2/2/2)
	After you cast a spell, give a random minion in your hand +1/+1."""
	pass

class ALT_NEU_21:
	""" Tower Sergeant (4/4/4)
	[Battlecry]: If you control at least 2 other minions, gain +2/+2."""
	pass

class ALT_NEU_22:
	""" Troll Centurion (8/8/8)
	[Rush]. [Honorable Kill]: Deal 8 damage to the enemy hero."""
	pass

class ALT_NEU_23:
	""" Sneaky Scout (2/3/2)
	[Stealth] [Honorable Kill]: Your next Hero Power costs (0). """
	pass

class ALT_NEU_24:
	""" Corporal ( 2/2/3)
	Honorable Kill: Give your other minions Divine Shield."""
	pass

class ALT_NEU_25:
	""" Frozen Mammoth (4/6/7)
	This is [Frozen] until you cast a Fire spell."""
	pass

class ALT_NEU_26:
	""" Popsicooler (3/3/3) Mech
	[Deathrattle]: [Freeze] two random enemy minions."""
	pass

class ALT_NEU_27:
	""" Lokholar the Ice Lord (10/8/8) Elemental
	[Rush], [Windfury] Costs (5) less if you have 15 Health or less. """
	pass

class ALT_NEU_28:
	""" Grimtotem Bounty Hunter (3/4/2)
	[Battlecry]: Destroy an enemy [Legendary] minion."""
	pass

class ALT_NEU_29:
	""" Spammy Arcanist (5/3/4)
	[Battlecry]: Deal 1 damage to all other minions. If any die, repeat this."""
	def play(self):
		while True:	
			list = self.game.fields
			cont=False
			for card in list:
				if card != self:
					Hit(card,1).trigger(self)
					if card.health==0:
						cont = True
			if not cont:
				return
		pass
	pass

class ALT_NEU_30:
	""" Ivus, the Forest Lord(1/1/1)
	[Battlecry]: Spend the rest of your Mana and gain +2/+2, [Rush], [Divine Shield], or [Taunt] at random for each."""
	def play(self):
		controller = self.controller
		rest_mana = controller.mana
		choices = random.sample(['rush','shield','taunt','2/2','2/2','2/2','2/2','2/2','2/2','2/2'],rest_mana)
		for choice in choices:
			if choice == 'rush':
				Buff(SELF,'ALT_NEU_30e1')
			elif choice == 'shield':
				Buff(SELF,'ALT_NEU_30e2')
			elif choice == 'taunt':
				Buff(SELF,'ALT_NEU_30e3')
			else:
				Buff(SELF,'ALT_NEU_30e4')
		pass
	pass
ALT_NEU_30e1=buff(rush=True)
ALT_NEU_30e2=buff(divine_shield=True)
ALT_NEU_30e3=buff(taunt=True)
ALT_NEU_30e4=buff(2,2)

class ALT_NEU_31:
	"""Abominable Lieutenant (8/3/5)
	At the end of your turn, eat a random enemy minion and gain its stats. """
	pass

class ALT_NEU_32:
	"""Knight-Captain (5/3/3)
	[Battlecry]: Deal 3 damage. [Honorable Kill]: Gain +3/+3."""
	requirements = {PlayReq.REQ_TARGET_TO_PLY:0, }
	play = Hit(TARGET, 3)
	events = Predamage().on(HonorableKill(Predamage.TARGET, predamage.AMOUNT, [Buff(SELF, 'ALT_NEU_32e')]))
	pass
ALT_NEU_32e=buff(3,3)

class ALT_NEU_33:
	"""Gnome Private (1/1/3)
	[Honorable Kill]: Gain +2 Attack. """
	events = Predamage(ENEMY_MINIONS).on(HonorableKill(Predamage.TARGET, Predamage.AMOUNT, [Buff(SELF,'ALT_NEU33e')]))
	pass
ALT_NEU33e=buff(2,0)

class ALT_NEU_34:
	"""Vanndar Stormpike (4/4/4)
	[Battlecry]: If this costs less than every minion in your deck, reduce their Cost by (3)."""
	def play(self):
		controller = self.controller
		go = True
		for card in controller.deck:
			if card.type == CardType.MINION and card.cost <= self.cost:
				go = False
				break
		if go:
			for card in controller.deck:
				if card.type == CardType.MINION:
					Buff(card,'ALT_NEU_34e').trigger(self)
		pass
	pass
ALT_NEU_34e = buff(cost=-3)

class ALT_NEU_35:
	"""Drek'Thar (4/4/4)
	[Battlecry]: If this costs more than every minion in your deck, summon 2 of them. """
	pass
	def play(self):
		controller = self.controller
		go = True
		choices = []
		for card in controller.deck:
			if card.type == CardType.MINION:
				choices.append(card)
				if card.cost >= self.cost:
					go = False
					break
		if go:
			choices = random.sample(choices,2)
			for card in choices:
				Summon(self.controller, card).trigger(self)
		pass
	pass





