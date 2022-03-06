from ..utils import *

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
		else:
			pass
			#print("Nothing happens at playing AV_100")
		pass
	pass

class AV_101:
	""" Herald of Lokholar (4/3/5)
	[Battlecry]: Draw a Frost spell."""
	play = Give(CONTROLLER, RANDOM(FRIENDLY_DECK + SPELL + FROST))
	pass

class AV_102:
	""" Popsicooler (3/3/3) Mech
	[Deathrattle]: [Freeze] two random enemy minions."""
	deathrattle = Freeze(RANDOM(ENEMY_MINIONS - FROZEN)) * 2#
	pass

class AV_112:
	""" Snowblind Harpy (3/3/4)
	[Battlecry]: If you're holding a Frost spell, gain 5 Armor."""
	play = Find(FRIENDLY_HAND + FROST) & GainArmor(FRIENDLY_HERO,5)
	pass

class AV_121:
	"""Gnome Private (1/1/3)
	[Honorable Kill]: Gain +2 Attack. """
	honorable_kill = Buff(SELF,'AV_121e')
	pass
AV_121e=buff(2,0)

class AV_122:
	""" Corporal ( 2/2/3)
	Honorable Kill: Give your other minions Divine Shield."""
	honorable_kill = SetAttr(FRIENDLY_MINIONS - SELF, 'divine_shield', 1)#
	pass

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

class AV_131:
	"""Knight-Captain (5/3/3)
	[Battlecry]: Deal 3 damage. [Honorable Kill]: Gain +3/+3."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, }
	play = Hit(TARGET, 3)
	honorable_kill = Buff(SELF, 'AV_131e')
	pass
AV_131e=buff(3,3)

class HitWithoutHonorableKill(TargetedAction):
	"""
	Hit character targets by \a amount.
	"""
	TARGET = ActionArg()
	AMOUNT = ActionArg()

	def do(self, source, target, amount):
		amount = source.get_damage(amount, target)
		if amount:
			return source.game.queue_actions(source, [Predamage(target, amount)])[0][0]
		return 0
class AV_132:
	""" Troll Centurion (8/8/8)
	[Rush]. [Honorable Kill]: Deal 8 damage to the enemy hero."""
	honorable_kill = HitWithoutHonorableKill(ENEMY_HERO, 8)
	pass

class AV_133:
	""" Icehoof Protector (6/2/10)
	[Taunt] [Freeze] any character damaged by this minion."""
	events = Attack(SELF, ALL_CHARACTERS).on(Freeze(Attack.DEFENDER))
	pass

class CountPlayedThisTurn(LazyNum):
	def __init__(self, selector):
		super().__init__()
		self.selector = selector
	def evaluate(self, source):
		controller = source.controller
		game =controller.game
		turn = game.turn
		count=0
		for card in controller._play_log:
			if card.turn == turn:
				count+=1
		return self.num(count)

class AV_134:
	""" Frostwolf Warmaster (4/3/5)
	Costs (1) less for each card you've played this turn."""
	cost_mod = -CountPlayedThisTurn(CONTROLLER)
	pass

class AV_135_AmountCounter(TargetedAction):
	"""	"""
	TARGET = ActionArg()# sidequest card
	AMOUNT = IntArg() #current damage
	AMOUNTGOAL = IntArg() #max of damage
	TARGETACTION = ActionArg()# sidequest action
	def do(self, source, target, amount, amountgoal, targetaction):
		if source.controller.game.current_player == source.controller.opponent:
			target._sidequest_counter_ += amount
			log.info("Setting Counter on %r -> %i, %r", target, (source._sidequest_counter_), targetaction)
		if target._sidequest_counter_>= amountgoal:
			target._sidequest_counter_ = 0
			if targetaction!=None:
				if not isinstance(targetaction,list):
					targetaction = [targetaction]
				for action in targetaction:
					if isinstance(action, TargetedAction):
						action.trigger(source)

class AV_135:#
	""" Stormpike Marshal (4/2/6)
	[Taunt] If you took 5 or more damage on your opponent's turn, this costs (1)."""
	class Hand:
		events = Damage(FRIENDLY_MINIONS).on(AV_135_AmountCounter(SELF, Damage.AMOUNT, 5, [SetCost(SELF,1)]))
	pass

class AV_136:#
	""" Kobold Taskmaster (3/2/4)
	[Battlecry]: Add 2 Armor Scraps to your hand that give +2 Health to a minion."""
	play = Give(CONTROLLER, 'AV_136t') * 2
	pass
AV_136e=buff(0,2)
class AV_136t:
	""" Armor Scrap 
	Give a minion +2 Health. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0}
	play = Buff(TARGET, 'AV_136e')
	pass

class AV_137:
	""" Irondeep Trogg (1/1/2)
	After your opponent casts a spell, summon a copy of this."""
	events = Play(OPPONENT, SPELL).on(Summon(CONTROLLER,ExactCopy(SELF)))
	pass

class AV_138:
	""" Grimtotem Bounty Hunter (3/4/2)
	[Battlecry]: Destroy an enemy [Legendary] minion."""
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0 }
	def play(self):
		if self.target != None and self.target.rarity==Rarity.LEGENDARY:
			self.controller.game.trigger(self.controller, [Destroy(self.target)], event_args=None)
	pass

class AV_139:
	"""Abominable Lieutenant (8/3/5)
	At the end of your turn, eat a random enemy minion and gain its stats. """
	events = OWN_TURN_END.on(EatsCard(SELF, RANDOM_ENEMY_MINION))
	pass

class AV_141t:
	""" Lokholar the Ice Lord (10/8/8) Elemental
	[Rush], [Windfury] Costs (5) less if you have 15 Health or less. """
	powered_up = CURRENT_HEALTH(FRIENDLY_HERO) <= 15
	cost_mod  = powered_up & -5
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
				Buff(self,'AV_142e2').trigger(controller)
			elif choice == 'shield':
				Buff(self,'AV_142e3').trigger(controller)
			elif choice == 'taunt':
				Buff(self,'AV_142e4').trigger(controller)
			else:
				Buff(self,'AV_142e').trigger(controller)
		pass
	pass
AV_142e2=buff(rush=True)
AV_142e3=buff(divine_shield=True)
AV_142e4=buff(taunt=True)
AV_142e=buff(2,2)

class AV_143_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source,target):
		controller = target.controller
		if not target.honorably_killed:
			Summon(controller, 'AV_143').trigger(controller)

class AV_143:#
	""" Korrak the Bloodrager (4/3/5)
	Deathrattle: If this wasn't Honorably Killed, resummon Korrak."""
	deathrattle = AV_143_Action(SELF)
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

class AV_222:
	""" Spammy Arcanist (5/3/4)
	[Battlecry]: Deal 1 damage to all other minions. If any die, repeat this."""
	def play(self):
		while True:	
			list = self.controller.field + self.controller.opponent.field
			cont=False
			for card in list:
				if card != self:
					if card.health==1:
						cont = True
					Hit(card,1).trigger(self.controller)##これだけでは死亡処理が行われない。
			Deaths().trigger(self.controller)#死亡処理
			if not cont:
				return
		pass
	pass

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

class AV_238:
	""" Gankster (2/4/2)
	[Stealth] After your opponents plays a minion, attack it"""
	events = Play(OPPONENT, MINION).after(Hit(Play.CARD, ATK(SELF)), Hit(SELF, ATK(Play.CARD)))
	pass

class AV_256:
	""" Reflecto Engineer (3/2/4)
	[Battlecry]: Swap the Attack and Health of all minions in both players' hands."""
	def play(self):
		game = self.game
		cardlist = game.hands
		for card in cardlist:
			if card.type==CardType.MINION:
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
	events = Play(CONTROLLER,SPELL).on(Buff(RANDOM(FRIENDLY_HAND - SPELL),'AV_401e'))
	pass
AV_401e=buff(1,1)

class AV_704:
	"""Humongous Owl(7/8/4)
	Deathrattle: Deal 8 damage to a random enemy."""
	deathrattle = Hit(RANDOM(ENEMY_MINIONS), 8)
	pass


##### Onyxian

class ONY_001:# <12>[1626]
	""" Onyxian Warder
	[Battlecry:] If you're holdinga Dragon, summon two2/1 Whelps with [Rush]. """
	powered_up = Find(FRIENDLY_HAND + DRAGON)
	play = powered_up & (Summon(CONTROLLER, 'ONY_001t'), Summon(CONTROLLER, 'ONY_001t'))
	pass

class ONY_001t:# <12>[1626]
	""" Onyxian Whelp
	[Rush] """
	pass

class ONY_002_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		log.info("now ONY_002_Action")
		unspent_mana = (target.controller.mana>0)
		if unspent_mana:
			Buff(target,'ONY_002e').trigger(target)
		pass

class ONY_002:# <12>[1626]
	""" Gear Grubber
	[Taunt]. If you end your turn with any unspent mana, reduce this card's Cost by (1). """
	class Hand:
		events = OWN_TURN_END.on(ONY_002_Action(SELF))
	pass

ONY_002e=buff(cost=-1)
""" More Loot!
Reduced Cost. """

class ONY_003:# <12>[1626]
	""" Whelp Bonker
	[Frenzy and Honorable Kill:] Draw a card. """
	events = Damage(SELF).on(Frenzy(SELF,Draw(CONTROLLER)))
	#tags = {GameTag.HONORABLEKILL: True} #exists
	honorable_kill = Draw(CONTROLLER)
	pass

class ONY_004:# <12>[1626]
	""" Raid Boss Onyxia
	[Rush]. [Immune] while you control a Whelp.[Battlecry:] Summon six_2/1 Whelps with [Rush]. """
	update = Find(FRIENDLY_MINIONS + ID('ONY_001t')) & Refresh(SELF, {GameTag.IMMUNE:True}) |  Refresh(SELF, {GameTag.IMMUNE:False})
	play = Summon(CONTROLLER, 'ONY_001t') * 6
	pass

class ONY_005_Action(TargetedAction):# <12>[1626]
	TARGET=ActionArg()
	## discover new cards 5 times.(new cards are fed in two.)
	def do(self, source,target):
		controller = target
		powered_up=True
		for card in controller.deck:
			if card.type == CardType.MINION and card.card_class != Race.DRAGON:
				powered_up=False
		if powered_up:
			new_deckA=['ONY_005ta1','ONY_005ta2','ONY_005ta3','ONY_005ta4','ONY_005ta5','ONY_005ta6','ONY_005ta7','ONY_005ta8','ONY_005ta9','ONY_005ta10','ONY_005ta11','ONY_005ta12','ONY_005ta13',]
			new_deckB=[]
			new_deckC=[]
			new_deck = random.choice[new_deckA, new_deckB, new_deckC]
			for card in controller.deck:
				Destroy(card).trigger(self)
			for card in new_deck:
				Shuffle(controller, new_deck).trigger(self)
			pass
class ONY_005:# <12>[1626]
	""" Kazakusan
	[Battlecry:] If all minions in your deck are Dragons,craft a custom deck of Treasures. """
	play = ONY_005_Action(CONTROLLER)
	pass

class ONY_005ta1:# <12>[1626]
	""" Necrotic Poison
	Destroy a minion. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Destroy(TARGET)#
	pass

class ONY_005ta10:# <12>[1626]
	""" Spyglass
	Put a copy of a random card in your opponent's hand into yours. It costs (3) less. """
	play = Give(CONTROLLER, ExactCopy(RANDOM(ENEMY_HAND))).then(Buff(Give.CARD, 'ONY_005ta10e'))
	pass
@custom_card
class ONY_005ta10e:
	tags = {
		GameTag.CARDNAME: "Spyglass",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.COST: -3,
	}
	events = REMOVED_IN_PLAY

class ONY_005ta11:# <12>[1626]
	""" Clockwork Assistant
	Has +1/+1 for each spell you've cast this game. """
	#AV_401eを拝借？
	def play(self):
		spell_count=0
		for card_log in self.controller.play_log:
			if card_log.card.type==CardType.SPELL:
				spell_count+=1
		for repeat in range(spell_count):
			Buff(source, 'ONY_005ta11e').trigger(self)
		pass
@custom_card
class ONY_005ta11e:
	tags = {
		GameTag.CARDNAME: "Clockwork Assistant",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.ATK: +1,
		GameTag.HEALTH: +1,
	}

class ONY_005ta12:# <12>[1626]
	""" Grimmer Patron
	At the end of your turn, summon a copy of this minion. """
	events = OWN_TURN_END.on(Summon, ExactCopy(SELF))
	pass

class ONY_005ta13:# <12>[1626]##################################
	""" Puzzle Box
	Transform all minions into random ones that cost (3) more. """
	def play(self):
		for card in self.controller.field + self.controller.opponent.field:
			cost = card.cost+3
			new_card = RandomMinion(cost=cost)
			yield Destroy(card)#????????????
			yield Summon(CONTROLLER, new_card)
		pass
	pass

class ONY_005ta2:# <12>[1626]
	""" Mutating Injection
	Give a minion +4/+4 and [Taunt]. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "ONY_005ta2e")#
	pass
ONY_005ta2e=buff(+4, +4, taunt=True)# <12>[1626]
""" Mutating Injection
+4/+4 and [Taunt]. """

class ONY_005ta3:# <12>[1626]
	""" The Exorcisor
	[Silence] any minion attacked by this weapon. """
	events = Attack(FRIENDLY_HERO, ENEMY_MINIONS).on(SetTag(Attack.DEFENDER,{GameTag.SILENCED:True}))
	pass

class ONY_005ta4:# <12>[1626]
	""" Pure Cold
	Deal $8 damage to the enemy hero, and [Freeze] it. """
	play = Hit(ENEMY_HERO, 8), Freeze(ENEMY_HERO)#
	pass

class ONY_005ta5:# <12>[1626]
	""" Bubba
	[Battlecry]: Summon six 1/1 Bloodhounds with[Rush] to attack an enemy minion. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }
	play = Summon(CONTROLLER, 'ONY_005ta5t').then(RegularAttack(Summon.CARD, TARGET)) * 6
	pass

class ONY_005ta5t:# <12>[1626]
	""" Bloodhound
	[Rush] """
	pass

class ONY_005ta6:# <12>[1626]
	""" Holy Book
	[Silence] and destroy a minion. Summon a 10/10 copy of it. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0,}
	play = (Silence(TARGET), Destroy(TARGET),Summon(CONTROLLER, ExactCopy(TARGET)))
	pass

class ONY_005ta7:# <12>[1626]
	""" Crusty the Crustacean
	[Battlecry:] Destroy a minion.Gain its Attack and Health. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, }
	play = (Destroy(TARGET), GainAttackHealth(SELF, ATK(TARGET), MAX_HEALTH(TARGET)))
	pass

class ONY_005ta7e:# <12>[1626] # dont know how to use this.
	""" Om Nom Nom
	Increased stats. """
	pass

class ONY_005ta8:# <12>[1626]
	""" Looming Presence
	Draw 2 cards. Gain 4 Armor. """
	play = Draw(CONTROLLER) * 2, GainArmor(FRIENDLY_HERO, 4)#
	pass

class ONY_005ta9:# <12>[1626]
	""" Beastly Beauty
	[Rush]After this attacks a minion and survives, transform this into an 8/8. """
	events = Attack(SELF).after(-Dead(SELF) & Morph(SELF, 'ONY_005ta9t'))
	pass

class ONY_005ta9t:# <12>[1626]
	""" Beautiful Beast
	 """
	pass

class ONY_005tb1:# <12>[1626]
	""" Hyperblaster
	[Poisonous].Your hero is [Immune] while attacking. """
	play = Buff(FRIENDLY_HERO, 'ONY_005tb1e')#
	pass
ONY_005tb1e=buff(immune_while_attacking = True)# <12>[1626]
""" Hyperblaster Enchantment
[Immune] while attacking. """

## no class ONY_005tb10,class ONY_005tb11 (but class ONY_005tb610)

class ONY_005tb12:# <12>[1626]
	""" Dr. Boom's Boombox
	Summon 7 'Boom Bots'. """
	play = Summon(CONTROLLER, 'GVG_110t') * 7#
	pass
class GVG_110t:
	"""Boom Bot
	&lt;b&gt;Deathrattle:&lt;/b&gt; Deal 1-4 damage to a random enemy."""
	deathrattle = Hit(RANDOM_ENEMY_CHARACTER, RandomNumber(1, 2, 3, 4))

class ONY_005tb13:# <12>[1626]
	""" Wax Rager　(3/5/1)
	[Deathrattle:] Resummon this minion. """
	deathrattel = Summon(CONTROLLER, Copy(SELF))#なんだこりゃ。
	pass

class ONY_005tb14:# <12>[1626]
	""" Vampiric Fangs
	Destroy a minion. Restore its Health to your hero. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0,} #
	play = Destroy(TARGET), Heal(FRIENDLY_HERO, CURRENT_HEALTH(TARGET))
	pass

class ONY_005tb2:# <12>[1626]
	""" Gnomish Army Knife
	Give a minion [Rush],[Windfury], [Divine Shield],[Lifesteal], [Poisonous],[Taunt], and [Stealth]. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0,} #
	play = Buff(TARGET, 'ONY_005tb2e')
	#
	pass

ONY_005tb2e=buff(rush=True, windfury=True, divine_shield=True, lifesteal=True, taunt=True, stealth=True)
# <12>[1626]
""" Tooled Up!
Granted [Rush],[Windfury], [Divine Shield],[Lifesteal], [Poisonous],[Taunt], and [Stealth]. """

class ONY_005tb3:# <12>[1626]
	""" LOCUUUUSTS!!!
	[Twinspell]Choose an enemy.Fill your board with 2/2 Locusts that attack it. """
	requirements = { PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_ENEMY_TARGET:0, PlayReq.REQ_MINION_TARGET:0}
	play = Summon(CONTROLLER, 'ONY_005tb3t2').then(RegularAttack(Summon.CARD, TARGET)),\
		Summon(CONTROLLER, 'ONY_005tb3t2').then(RegularAttack(Summon.CARD, TARGET)),\
		Summon(CONTROLLER, 'ONY_005tb3t2').then(RegularAttack(Summon.CARD, TARGET)),\
		Summon(CONTROLLER, 'ONY_005tb3t2').then(RegularAttack(Summon.CARD, TARGET)),\
		Summon(CONTROLLER, 'ONY_005tb3t2').then(RegularAttack(Summon.CARD, TARGET)),\
		Summon(CONTROLLER, 'ONY_005tb3t2').then(RegularAttack(Summon.CARD, TARGET)),\
		Summon(CONTROLLER, 'ONY_005tb3t2').then(RegularAttack(Summon.CARD, TARGET)),\
		Give(CONTROLLER,'ONY_005tb3t')
	pass

class ONY_005tb3t:# <12>[1626]
	""" LOCUUUUSTS!!!
	Choose an enemy.Fill your board with 2/2 Locusts that attack it. """
	play = Summon(CONTROLLER, 'ONY_005tb3t2').then(RegularAttack(Summon.CARD, TARGET)),\
		Summon(CONTROLLER, 'ONY_005tb3t2').then(RegularAttack(Summon.CARD, TARGET)),\
		Summon(CONTROLLER, 'ONY_005tb3t2').then(RegularAttack(Summon.CARD, TARGET)),\
		Summon(CONTROLLER, 'ONY_005tb3t2').then(RegularAttack(Summon.CARD, TARGET)),\
		Summon(CONTROLLER, 'ONY_005tb3t2').then(RegularAttack(Summon.CARD, TARGET)),\
		Summon(CONTROLLER, 'ONY_005tb3t2').then(RegularAttack(Summon.CARD, TARGET)),\
		Summon(CONTROLLER, 'ONY_005tb3t2').then(RegularAttack(Summon.CARD, TARGET))
	pass

class ONY_005tb3t2:# <12>[1626]
	""" Giant Locust
	vanilla """
	pass

class ONY_005tb4:# <12>[1626]
	""" Wand of Disintegration
	[Silence] and destroy all enemy minions. """
	play = Silence(ENEMY_MINIONS),Destroy(ENEMY_MINIONS)
	pass

class ONY_005tb5:# <12>[1626]
	""" Staff of Scales
	Summon three 1/1 Snakes with [Rush], [Poisonous] and [Reborn]. """
	play=Summon(CONTROLLER,'ONY_005tb5t')*3#
	pass

class ONY_005tb5t:# <12>[1626]
	""" Ancient Snake
	[Rush][Poisonous][Reborn] """
	#
	pass

class ONY_005tb6:# <12>[1626]
	""" Phaoris' Blade
	[Windfury].After your hero attacks and kills a minion, this gains +2/+1. """
	events = Attack(SELF, ENEMY_MINIONS).after(Dead(ALL_MINIONS + Attack.DEFENDER) &Buff(SELF, 'ONY_005tb6e'))
	pass

class ONY_005tb610:# <12>[1626]#???????? maybe class ONY_005tb10
	""" Zephrys's Lamp
	Wish for the perfect card. 
	[x]「勝利のカード」の願いを叶える。 = ULD_003"""
	#def play(self):
	#	entourage=['CS2_046','CS2_011']##Bloodlust, Savage Roar
	#	if self.controller.opponent.hero.health<10:
	#		entourage=['BT_512','CORE_CS2_029','EX1_241','EX1_308']#Inner Demon, Fireball, Lava Burst, Soulfire
	#	else:
	#		for card in self.controller.opponent.field:
	#			if card.taunt == True and card.max_health-card.damage>2:
	#				entourage=['EX1_626','EX1_303','EX1_332']#Mass Dispel, Shadowflame, Silence
	#				break
	#	card = random.choice(entourage)
	#	Give(self.controller, card).trigger(self.controller)
	pass

ONY_005tb6e=buff(2,1)# <12>[1626]
""" Phaoris' Fury
Increased stats. """

class ONY_005tb7:# <12>[1626]
	""" Canopic Jars
	Give your minions "[Deathrattle:] Summon a random [Legendary] minion." """
	#
	pass

class ONY_005tb7e:# <12>[1626]
	""" Canopic Jars
	[Deathrattle:] Summon a random [Legendary] minion. """
	tags={GameTag.DEATHRATTLE: True}
	deathrattle = Summon(RandomMinion(rarity=Rarity.LEGENDARY))
	pass

class ONY_005tb8:# <12>[1626]
	""" Ancient Reflections
	Choose a minion.Fill your board with 1/1 copies of it. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0}
	play = Summon(CONTROLLER, Copy(TARGET)).then(Summon.CARD,'ONY_005tb8e')
	pass

class ONY_005tb8e:# <12>[1626]
	""" Titan Hologram
	1/1. """
	atk=SET(1)
	max_health=SET(1)
	pass

class ONY_005tb9:# <12>[1626]
	""" Banana Split
	Give a friendly minion +2/+2. Summon two copies of it. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0}
	play = Buff(TARGET, 'ONY_005tb9e').then(Summon(CONTROLLER,ExactCopy(Buff.TARGET)) * 2)
	pass

ONY_005tb9e=buff(2,2)# <12>[1626]
""" Glowing Green
+2/+2. """

class ONY_005tc1:# <12>[1626]
	""" Embers of Ragnaros
	Shoot three fireballs at random enemies that deal $8 damage each. """
	play = Hit(RANDOM_ENEMY_CHARACTER,8) * 3
	pass

class ONY_005tc2:# <12>[1626]#################
	""" Book of the Dead
	Deal $7 damage to all enemies. Costs (1) less for each minion that's died this game. """
	#### whose cost?
	#play = Hit(ENEMY_CHARACTERS,7), 
	pass

class ONY_005tc3:# <12>[1626]######################
	""" Annoy-o Horn
	Fill your board with annoying minions. """
	annoying=['CORE_GVG_085','BOT_911',]
	pass

class ONY_005tc4:# <12>[1626]
	""" Flex-plosion
	Blow up half your opponent's stuff. """
	#
	pass

class ONY_005tc5:# <12>[1626]
	""" Blade of Quel'Delar
	 """
	#
	pass

class ONY_005tc6:# <12>[1626]
	""" Hilt of Quel'Delar
	Give a minion +3/+3. """
	#
	pass

class ONY_005tc7:# <12>[1626]
	""" Quel'Delar
	After your hero attacks, deal 4 damage to all_enemies. """
	#
	pass

class ONY_005tc7t:# <12>[1626]
	""" Forging Quel'Delar
	 """
	#
	pass

class ONY_025e:# <12>[1626]
	""" Incensed
	+2/+1 and [Rush]. """
	#
	pass



