from ..utils import *

class AV_101:
	""" Herald of Lokholar (4/3/5)
	[Battlecry]: Draw a Frost spell."""
	play = Give(CONTROLLER, RANDOM(FRIENDLY + SPELL))
	pass

class AV_112:
	""" Snowblind Harpy (3/3/4)
	[Battlecry]: If you're holding a Frost spell, gain 5 Armor."""
	play = Find(FRIENDLY_HAND + FROST) & GainArmor(FRIENDLY_HERO,5)
	pass

class AV_122:
	""" Corporal ( 2/2/3)
	Honorable Kill: Give your other minions Divine Shield."""
	honorable_kill = Buff(FRIENDLY_MINIONS - SELF, 'AV_122')###########
	pass
ALT_NEU_24e=buff(divine_shield=True)############

class AV_123:
	""" Sneaky Scout (2/3/2)
	[Stealth] [Honorable Kill]: Your next Hero Power costs (0). """
	honorable_kill = Buff(FRIENDLY_HERO_POWER, 'AV_123e')
	pass
class AV_123e:
	cost = SET(0)
	pass

class AV_124:####OK
	""" Direwolf Commander (3/2/5)
	[Honorable Kill]: Summon a 2/2 Wolf with Stealth """
	honorable_kill = Summon(CONTROLLER,'AV_211t')
	pass
class AV_211t:##重複を除く
	""" wolf """
	pass

class AV_125:
	""" Tower Sergeant (4/4/4)
	[Battlecry]: If you control at least 2 other minions, gain +2/+2."""
	powered_up = Count(FRIENDLY_MINIONS - SELF) >= 2
	play = powered_up & Buff(SELF,'AV_125e')
	pass
AV_125e=buff(2,2)

class AV_126:###OK
	""" Bunker Sergeant (3/2/4)
	[Battlecry]: If your opponent has 2 or more minions, deal 1 damage to all enemy minions."""
	play = (Count(ENEMY_MINIONS)>=2) & Hit(ENEMY_MINIONS, 1)
	pass

class AV_127:
	""" Ice Revenant (4/4/5)
	Whenever you cast a Frost spell, gain +2/+2. """
	events = Play(CONTROLLER, SPELL + FROST).on(Buff(SELF,'AV_127e'))
	pass
AV_127e=buff(2,2)

class AV_129:####OK # [1626]<12>
	""" Blood Guard (5/4/7)
	Whenever this minion takes damage, give your minions +1 Attack. """
	events = Attack(ALL_CHARACTERS,SELF).on(Buff(FRIENDLY_MINIONS,'AV_129e'))
	pass
AV_129e = buff(1,0)

class AV_130:
	""" Legionnaire (6/9/3)
	Deathrattle: Give all minions in your hand +2/+2. """
	deathrattle = Buff(FRIENDLY_HAND + MINION, 'AV_130e')
	pass
AV_130e = buff(2,2)

class CountPlayedThisTurn(LazyNum):
	def evaluate(self, source):
		controller = source
		game =controller.game
		turn = game.turn
		count=0
		for card in controller._play_log:
			if card[1] == turn:
				count+=1
		return self.num(count)

class AV_132:
	""" Troll Centurion (8/8/8)
	[Rush]. [Honorable Kill]: Deal 8 damage to the enemy hero."""
	honorable_kill = Hit(ENEMY_HERO, 8)
	pass

class AV_133:
	""" Icehoof Protector (6/2/10)
	[Taunt] [Freeze] any character damaged by this minion."""
	events = Attack(SELF, ALL_CHARACTERS).on(SetTag(Attack.DEFENDER,(GameTag.FREEZE,)))
	pass

class AV_134:
	""" Frostwolf Warmaster (4/3/5)
	Costs (1) less for each card you've played this turn."""
	cost_mod = -CountPlayedThisTurn(CONTROLLER)
	pass

class AV_135:#################################
	""" Stormpike Marshal (4/2/6)
	[Taunt] If you took 5 or more damage on your opponent's turn, this costs (1)."""
	class Hand:
		events = Damage(FRIENDLY_MINIONS).on(SidequestCounter(CONTROLLER, 5, [SetTag(SELF, (GameTag.COST,))]))
	pass

class AV_136:#######################
	""" Kobold Taskmaster (3/2/4)
	[Battlecry]: Add 2 Armor Scraps to your hand that give +2 Health to a minion."""
	play = Give(CONTROLLER, 'AV_136t') * 2
	pass
AV_136e=buff(0,2)
class AV_136t:
	pass

class AV_137:
	""" Irondeep Trogg (1/1/2)
	After your opponent casts a spell, summon a copy of this."""
	events = Play(OPPONENT, SPELL).on(Summon(CONTROLLER,ExactCopy(SELF)))
	pass

class AV_143_Find(Evaluator):
	"""
	Evaluates to True if \a selector has a match.
	"""
	def __init__(self, selector, count=1):
		super().__init__()
		self.selector = selector

	def check(self, source):
		card = self.selector.eval(source.game.allcards, source) ### Korrak card
		return card[0].honorably_killed

class AV_143:#
	""" Korrak the Bloodrager (4/3/5)
	Deathrattle: If this wasn't Honorably Killed, resummon Korrak."""
	deathrattle = AV_143_Find(SELF) & Summon(CONTROLLER, 'AV_143')
	pass

class AV_215:####OK
	""" Frantic Hippogryph (5/3/7)
	[Rush]. [Honorable Kill]: Gain [Windfury]. """
	honorable_kill = SetTag(SELF, (GameTag.WINDFURY,))
	pass

class AV_219:
	""" Ram Commander (2/2/2)
	[Battlecry]: Add two 1/1 Rams with Rush to your hand."""
	play = Give(CONTROLLER, 'AV_219t') * 2
	pass
class AV_219t:
	""" Ram with Rush (1/1)"""
	pass

class AV_238:
	""" Gankster (2/4/2)
	[Stealth] After your opponents plays a minion, attack it"""
	events = Play(OPPONENT, MINION).after(RegularAttack(SELF, Play.CARD))
	pass

class AV_256:
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

class AV_309:
	""" Piggyback Imp (3/1/1) deamon
	Deathrattle: Summon a 4/1 Imp. """
	deathrattle = Summon(CONTROLLER,'AV_309t')
	pass
class AV_309t:
	""" 4/1 imp """
	pass

class AV_401:
	""" Stormpike Quartermaster (2/2/2)
	After you cast a spell, give a random minion in your hand +1/+1."""
	events = OWN_SPELL_PLAY.on(Buff(RANDOM(FRIENDLY_MINIONS),'AV_401e'))
	pass
AV_401e=buff(1,1)

class AV_704:
	"""Humongous Owl(7/8/4)
	Deathrattle: Deal 8 damage to a random enemy."""
	deathrattle = Hit(RANDOM(ENEMY_MINIONS), 8)
	pass

##########################

class AV_128:
	""" Frozen Mammoth (4/6/7)
	This is [Frozen] until you cast a Fire spell."""
	events = Play(CONTROLLER, SPELL + FIRE).on(Buff(SELF,'AV_128e'))
	pass
AV_128e=buff(freeze=False)

class AV_102:
	""" Popsicooler (3/3/3) Mech
	[Deathrattle]: [Freeze] two random enemy minions."""
	deathrattle = SetTag(RANDOM_ENEMY_MINION, (GameTag.FREEZE,)) * 2#
	pass

class AV_141t:
	""" Lokholar the Ice Lord (10/8/8) Elemental
	[Rush], [Windfury] Costs (5) less if you have 15 Health or less. """
	powered_up = CURRENT_HEALTH(FRIENDLY_HERO) <= 15
	update = powered_up & Buff(SELF, 'ALT_NEU_27e')##############
	pass
ALT_NEU_27e=buff(cost=-5)###################

class AV_138:
	""" Grimtotem Bounty Hunter (3/4/2)
	[Battlecry]: Destroy an enemy [Legendary] minion."""
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0 }
	def play(self):
		if self.target != None and self.target.rarity==Rarity.LEGENDARY:
			self.controller.game.trigger(self.controller, [Destroy(self.target)], action_args=None)
	pass

class AV_222:
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

class AV_142t:
	""" Ivus, the Forest Lord(1/1/1)
	[Battlecry]: Spend the rest of your Mana and gain +2/+2, [Rush], [Divine Shield], or [Taunt] at random for each."""
	def play(self):
		controller = self.controller
		rest_mana = controller.mana
		choices = random.sample(['rush','shield','taunt','2/2','2/2','2/2','2/2','2/2','2/2','2/2'],rest_mana)
		for choice in choices:
			if choice == 'rush':
				Buff(SELF,'AV_142e2')
			elif choice == 'shield':
				Buff(SELF,'AV_142e3')
			elif choice == 'taunt':
				Buff(SELF,'AV_142e4')
			else:
				Buff(SELF,'AV_142e')
		pass
	pass
AV_142e2=buff(rush=True)
AV_142e3=buff(divine_shield=True)
AV_142e4=buff(taunt=True)
AV_142e=buff(2,2)

class AV_139:
	"""Abominable Lieutenant (8/3/5)
	At the end of your turn, eat a random enemy minion and gain its stats. """
	events = OWN_TURN_END.on(EatsCard(SELF, RANDOM_ENEMY_MINION))
	pass

class AV_131:
	"""Knight-Captain (5/3/3)
	[Battlecry]: Deal 3 damage. [Honorable Kill]: Gain +3/+3."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, }
	play = Hit(TARGET, 3)
	honorable_kill = Buff(SELF, 'AV_131e')
	pass
AV_131e=buff(3,3)

class AV_121:
	"""Gnome Private (1/1/3)
	[Honorable Kill]: Gain +2 Attack. """
	honorable_kill = Buff(SELF,'AV_121e')
	pass
AV_121e=buff(2,0)

class AV_223:
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
					Buff(card,'AV_223e').trigger(self)
		pass
	pass
AV_223e = buff(cost=-3)

class AV_100:
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




