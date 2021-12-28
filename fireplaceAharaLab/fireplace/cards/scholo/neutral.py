from ..utils import *

# 未実装
#'SCH_158e2','SCH_301e','SCH_305d',
#'SCH_519e','SCH_539e','SCH_622e',

class SCH_142:#done
	""" Voracious Reader (rare) """
	#At the end of your turn, draw until you have 3 cards.
	events = OWN_TURN_END.on(DrawUntil(CONTROLLER,3))#
	pass

class SCH_143:#done
	""" Divine Rager"""
	#Divine Shield
	pass

class SCH_145:#done
	""" Desk Imp"""
	#Vanilla
	pass

class SCH_146:#done
	""" Robes of Protection (Rare)"""
	#Your minions have &quot;Can't be targeted by spells or Hero Powers.&quot;
	play = Buff(CONTROLLER, "SCH_146e")
	pass
class SCH_146e:################# cannot be verified
	"""Protected"""
	#Can't be targeted by spells or Hero Powers.
	update = Refresh(FRIENDLY_MINIONS, {GameTag.CANT_BE_TARGETED_BY_HERO_POWERS: 1}), Refresh(FRIENDLY_MINIONS, {GameTag.CANT_BE_TARGETED_BY_SPELLS: 1}) 
	pass

class SCH_157:#done
	""" Enchanted Cauldron (Epic)"""
	#Spellburst: Cast a random spell of the same Cost.(3)
	play = Play(CONTROLLER, SPELL).on(CastSpell(RandomSpell(cost=Attr(Play.CARD, GameTag.COST))))
	pass

class SCH_160:#done
	""" Wandmaker"""
	#Battlecry: Add a 1-Cost spell from your class(HUNTER) to_your hand.
	play = Give(CONTROLLER, RandomSpell(cost=1, card_class=FRIENDLY_CLASS))
	pass

class SCH_162:##OK
	""" Vectus"""
	#Battlecry: Summon two 1/1 Whelps. Each gains a Deathrattle from your minions that died this game.
	#雄叫び:1/1のチビドラゴンを2体召喚する。
	#それらはこの対戦で死亡した味方のミニオンの断末魔を1つずつ獲得する。
	def play(self):
		controller = self.controller
		death_log = controller.death_log
		deathrattle_log=[]
		for card in death_log:
			if len(card.deathrattles)>0:
				deathrattle_log.append(card)
		if len(deathrattle_log)==0:
			return 
		minion1 = Summon(controller, "SCH_162t").trigger(controller)
		if minion1[0] != []:
			minion1 = minion1[0][0]
			Buff(minion1, 'SCH_162e').trigger(controller)
			buff1 = minion1.buffs[0]
			death = random.choice(deathrattle_log)
			buff1.additional_deathrattles.append(death.deathrattles[0])
			log.info ('%s gains deathrattle (%s)'%(minion1, minion1.deathrattles[0]))
			if len(deathrattle_log)>=2:
				deathrattle_log.remove(death)
			pass
		minion2 = Summon(controller, "SCH_162t").trigger(controller)
		if minion2[0] != []:
			minion2 = minion2[0][0]
			Buff(minion2, 'SCH_162e').trigger(controller)
			buff2 = minion2.buffs[0]
			death = random.choice(deathrattle_log)
			buff2.additional_deathrattles.append(death.deathrattles[0])
			log.info ('%s gains deathrattle (%s)'%(minion2, minion2.deathrattles[0]))
			pass
	pass
class SCH_162e:
	# Experimental Plague
	# Copied Deathrattle from {0}
	tags = {GameTag.DEATHRATTLE : True} 
	#deathrattle = 
class SCH_162t:
	# Plagued Hatchling
	# Vanilla
	pass

class SCH_199:###how we execute 'battlecry'?####
	""" Transfer Student (Epic)"""
	#This has different effects based on which game board you're on.
	def play(self):
		yield Morph(self, self.controller.game.__stage_choice__)
		pass
class SCH_199t:
	"""Stormwind,　Standard
	#Divine Shield"""  
	pass
class SCH_199t2:#OK
	""" Orgrimmar, Standard
	#<b>Battlecry:</b> Deal 2 damage."""
	requirements = {PlayReq.REQ_ENEMY_TARGET: 0,
			PlayReq.REQ_TARGET_IF_AVAILABLE: 0,}
	play = Hit(TARGET,2)
	pass
class SCH_199t3:#OK
	"""Pandaria, Standard#
	#<b>Battlecry:</b> Give a friendly minion +1/+2."""
	requirements = {PlayReq.REQ_FRIENDLY_TARGET: 0,
				 PlayReq.REQ_MINION_TARGET:0,
			PlayReq.REQ_TARGET_IF_AVAILABLE: 0,}
	play = Buff(TARGET,"SCH_199t3e")
	pass
SCH_199t3e=buff(1,2)
#Mark of the Pandaren
class SCH_199t4:#OK
	"""Stranglethorn, Standard
	#<b>Stealth</b> <b>Poisonous</b>"""
	pass
class SCH_199t19:#OK
	"""Rise of Shadows, Standard
	#<b>Battlecry:</b> Add a <b>Lackey</b> to_your hand."""
	entourage = ["CFM_066", "DAL_613", "DAL_614", "DAL_615", "DAL_739",\
	   "DAL_741", "DRG_052" ,"ULD_616"]
	play = Draw(CONTROLLER, RandomEntourage())
	pass
class SCH_199t20:#OK
	"""Saviors of Uldum,　Standard
	#Reborn"""
	pass
class SCH_199t21:#OK
	""" Descent of Dragons Standard
	#<b>Battlecry:</b> <b>Discover</b> a Dragon."""
	play = DISCOVER(RandomDragon())
	pass
class SCH_199t22:#OK
	"""Ashes of Outland, Standard
	##<b>Dormant</b> for 2 turns. When this awakens, deal 3 damage to two random enemy minions."""
	dormant = 2
	awaken = Hit(RANDOM_ENEMY_MINION * 2, 3)
	pass
class SCH_199t23:
	"""Scholomance Academy, Standard
	<b>Battlecry:</b> Add a Dual Class card to your hand.
	 dual class card <=> hasattr(self, "multi_class_group")==True"""
	#play = ForceDraw(RANDOM_MULTI_CLASS_GROUP)
	pass
class SCH_199t25:#OK
	""""Saviors of Uldum, Standard
	#<b>Battlecry:</b> Add an <b>Uldum</b> Plague spell to your hand."""
	pass
class SCH_199t26:################################################### no checked
	"""Madness at the Darkmoon Faire, Standard
	#<b>Corrupt:</b> Gain +2/+2."""
	play = Buff(CONTROLLER, "SCH_199t26t")
	pass
SCH_199t26t = buff(2,2)

class SCH_224:#OK
	# <b>Spellburst:</b> If the spell destroys any minions, summon them.
	""" Headmaster Kel'Thuzad (Legendary)"""
	play = Buff(CONTROLLER,"SCH_224e3")
	pass
class SCH_224e3:#OK
	#Kel'thuzad's Call
	events = OWN_SPELL_PLAY.after(
		Dead(ALL_MINIONS + Play.CARD) & (# Dead -> return bool
			Summon(CONTROLLER, "SCH_224t"),
			Destroy(SELF)
		)
	)
	pass
class SCH_224t:
	#Mr. Bigglesworth
	#Vanilla
	pass

class SCH_230:#OK
	""" Onyx Magescribe"""
	# <b>Spellburst:</b> Add 2 random spells from your class to_your hand.
	play = OWN_SPELL_PLAY.on(
		ForceDraw(RandomSpell(card_class=FRIENDLY_CLASS)) * 2
	)
	#spellburst = ForceDraw(RandomSpell(card_class=FRIENDLY_CLASS)) * 2,
	pass

class SCH_231:#OK
	"""Intrepid Initiate """
    #<b>Spellburst:</b> Gain +2_Attack.
	play = OWN_SPELL_PLAY.on(Buff(SELF, "SCH_231e"))#
	#spellburst = Buff(SELF, "SCH_231e")
	pass
SCH_231e = buff(2,0)

class SCH_232:#OK
	""" Crimson Hothead"""
	#<b>Spellburst:</b> Gain +1 Attack and <b>Taunt</b>.
	play = OWN_SPELL_PLAY.on(Buff(SELF, "SCH_232e"))#
	pass
SCH_232e = buff(1, 0, taunt=True)

class SCH_245:#OK
	""" Steward of Scrolls"""
	#<b>Spell Damage +1</b><b>Battlecry:</b> <b>Discover</b> a spell.
	play = DISCOVER(RandomSpell())
	# 'spellpower=1' has already coded.
	pass

class SCH_248:#OK
	""" Pen Flinger"""
	# <b>Battlecry:</b> Deal 1 damage. <b>Spellburst:</b> Return this to_your hand.
	requirements = {PlayReq.REQ_ENEMY_TARGET: 0,
			PlayReq.REQ_TARGET_IF_AVAILABLE: 0,}
	play = Hit(TARGET, 1), OWN_SPELL_PLAY.on(Bounce(SELF))
	pass

class SCH_259_Choice(Choice):
	def choose(self, card):
		super().choose(card)
		log.info("%s chooses %r"%(card.controller.name, card))
		cardID = card.id
		if cardID == 'SCH_259t':
			if len(self.source.controller.hand)>0:
				new_card = self.source.controller.hand[-1]#すでに配られてしまっている
				new_card.zone = Zone.DECK#デッキに戻す。
			controller = self.source.controller
			controller.deck.insert(0,new_card)
			del controller.deck[-1]
			controller.draw()
			pass
		else:
			pass
		Hit(self.source, 1).trigger(self.player)  # 
		pass
class SCH_259_Action(TargetedAction):
	ACTION = ActionArg()
	def do(self, source, target):
		controller = target
		new_card_id = controller.deck[-1].id
		source.entourage = [new_card_id, 'SCH_259t']
		SCH_259_Choice(CONTROLLER, RandomEntourage()*2).trigger(source)

class SCH_259:####OK
	""" Sphere of Sapience (legendary)"""
	#At the start of your turn, look at your top card. You can put it on the bottom _and lose 1 Durability.
	entourage=['SCH_259t']
	events = OWN_TURN_BEGIN.on(SCH_259_Action(CONTROLLER))
	pass
class SCH_259t:
	"""	A New Fate """
	#Draw a different card.
	pass


class SCH_283:#OK
	""" Manafeeder Panthara"""
	#<b>Battlecry:</b> If you've used your Hero Power this turn, draw a card.
	#play = HERO_POWER_USED & ForceDraw(FRIENDLY) 
	def play(self):
		if self.controller.hero.power.is_usable()==False:
			yield  Draw(CONTROLLER)
	pass

class SCH_311:#OK
	""" Animated Broomstick"""
	#<b>Rush</b> <b>Battlecry:</b> Give your other minions <b>Rush</b>.
	#update = Refresh(FRIENDLY_MINIONS - SELF, {GameTag.RUSH: 1})
	play = Buff(FRIENDLY_MINIONS - SELF, 'EX1_084e')
	pass

class SCH_312:#OK
	""" Tour Guide"""
	#	<b>Battlecry:</b> Your next Hero Power costs (0).
	play = Buff(CONTROLLER, "SCH_312e")
class SCH_312e:
	update = Refresh(FRIENDLY_HERO_POWER, {GameTag.COST: SET(0)})
	events = Activate(CONTROLLER, HERO_POWER).on(Destroy(SELF))

class SCH_313:#done
	""" Wretched Tutor"""
	#<b>Spellburst:</b> Deal 2 damage to all other minions.
	play = OWN_SPELL_PLAY.on(Hit(ALL_MINIONS-SELF,2))
	pass

class SCH_428:#done
	""" Lorekeeper Polkelt (Legendary)"""
	#[x]<b>Battlecry:</b> Reorder your deck from the highest Cost card to the lowest Cost card. 
	def play(self):
		log.info("Reorder deck from the highest Cost card.")
		self.controller.deck.sort(key=lambda x:x.cost)
		pass
	pass

class SCH_530:#done
	""" Sorcerous Substitute"""
	#<b>Battlecry:</b> If you have <b>Spell Damage</b>, summon a copy of this.
	#play = Find(FRIENDLY_HAND + MINION + SPELLPOWER) & Summon(CONTROLLER, ExactCopy(RANDOM(FRIENDLY_HAND + MINION + SPELLPOWER)))
	import random 
	def play(self):
		find = []
		for card in self.controller.hand:
			if card.type==CardType.MINION and card.spellpower>0:
				find.append(card)
		if len(find)>0:
			yield Summon(CONTROLLER, random.choice(find).id)##
	pass

class SCH_605:#OK
	""" Lake Thresher"""
	#Also damages the minions next to whomever this attacks.
	events = Attack(SELF, ENEMY_MINIONS).on(Hit(ADJACENT(ENEMY_MINIONS+Attack.DEFENDER), ATK(SELF)))
	pass

class SCH_707:#done
	""" Fishy Flyer"""
	#<b>Rush</b>. <b>Deathrattle:</b> Add a_4/3 Ghost with <b>Rush</b> to_your hand.
	deathrattle = Give(CONTROLLER,"SCH_707t")
	pass
class SCH_707t:
	"""Spectral Flyer"""
	# Rush
	pass

class SCH_708:#done
	""" Sneaky Delinquent"""
	#<b>Stealth</b>. <b>Deathrattle:</b> Add a 3/1 Ghost with <b>Stealth</b> to your hand.
	deathrattle = Give(CONTROLLER,"SCH_708t")
	pass
class SCH_708t:
	"""Spectral Delinquent"""
	#Stealth

class SCH_709:#done
	""" Smug Senior"""
	#<b>Taunt</b>. <b>Deathrattle:</b> Add a_5/7 Ghost with <b>Taunt</b> to_your hand.
	deathrattle = Give(CONTROLLER,"SCH_709t")
	pass
class SCH_709t:
	"""Spectral Senior"""
	#Taunt
	pass

class SCH_710:#done
	""" Ogremancer"""
	#[x]Whenever your opponent casts a spell, summon a 2/2 Skeleton with <b>Taunt</b>.
	events = Play(ENEMY,SPELL).on(Summon(CONTROLLER,"SCH_710t"))
	pass
class SCH_710t:
	"""Risen Skeleton"""
	#Taunt
	pass

class SCH_711:#OK
	""" Plagued Protodrake"""
	#<b>Deathrattle:</b> Summon a random 7-Cost minion.
	deathrattle = Summon(CONTROLLER, RandomMinion(cost=7))
	pass

class SCH_713:#OK
	""" Cult Neophyte (Rare)"""
	#<b>Battlecry:</b> Your opponent's spells cost (1) more next_turn.
	play = OWN_TURN_END.on( Buff(CONTROLLER, "SCH_713e"))
	pass
class SCH_713e:
	update = Refresh(ENEMY_HAND + SPELL, buff="SCH_713e2")
	#Spoiled!
SCH_713e2 = buff(cost=1)
	#Spoiling

class SCH_714:# maybe OK!!
	""" Educated Elekk (epic)"""
	#[x]Whenever a spell is played, this minion remembers it.
	#<b>Deathrattle:</b> Shuffle the spells into your deck.
	events = OWN_SPELL_PLAY.on(EducatedElekkMemory(SELF, Play.CARD))
	deathrattle = EducatedElekkDeathrattle(SELF)
	pass
SCH_714e = buff(cost=-1)
	#"""Educated"""
	#Remembering spell
	#pass

class SCH_717:##complete
	""" Keymaster Alabaster"""
	#[x]Whenever your opponent _draws a card, add a copy to_ _your hand that costs (1).
	events = Draw(OPPONENT).on(
		#Give(CONTROLLER, Buff(Copy(Draw.CARD), {GameTag.COST:SET(1)}),
		Give(CONTROLLER, CopyCostA(Draw.CARD,1))
	)
	pass

#class SCH_235: ## mage
#class SCH_270:#,'SCH_270e','SCH_270e2',# mage
#class SCH_273:##mage
#class SCH_350:##mage
#class SCH_300e, SCH_300e2 ## hunter
#class SCH_351:##'SCH_351a','SCH_351b','SCH_351e','SCH_351e2' ##mage
#class SCH_352:# SCH_352e ## mage
#class SCH_509: ## mage
#class SCH_537:##mage

class SCH_182_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		source.atk += target.cost
		source.max_health += target.cost
		pass

class SCH_182:###OK
	""" Speaker Gidra
	[x]&lt;b&gt;&lt;b&gt;Rush&lt;/b&gt;, Windfury&lt;/b&gt;
&lt;b&gt;&lt;b&gt;Spellburst&lt;/b&gt;:&lt;/b&gt; Gain Attack
and Health equal to
the spell's Cost.""" 
	play = OWN_SPELL_PLAY.on(SCH_182_Action(Play.CARD))
	pass
class SCH_182e:
	pass

class SCH_425:###OK
	""" Doctor Krastinov
	&lt;b&gt;Rush&lt;/b&gt;
	Whenever this attacks, give your weapon +1/+1. """ 
	events = Attack(SELF).on(Buff(FRIENDLY_WEAPON,'SCH_425e'))
	pass
SCH_425e = buff(1,1)##<10>[1443]

class SCH_521:###OK
	""" Coerce
	Destroy a damaged minion. &lt;b&gt;Combo:&lt;/b&gt; Destroy any minion. """ 
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0}
	def play(self):
		if self.target.damage>0:
			yield Destroy(TARGET)
		pass
	combo = Destroy(TARGET)
	pass

class SCH_522:###OK
	"""  Steeldancer
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; Summon a random
minion with Cost equal to
your weapon's Attack. """ 
	def play(self):
		if self.controller.weapon:
			cost = self.controller.weapon.atk
			picker = RandomMinion(cost = cost)
			yield Summon(CONTROLLER, picker)
		pass
	pass


class SCH_623:###OK
	""" Cutting Class
	[x]Draw 2 cards.
Costs (1) less per Attack
of your weapon. """ 
	def play(self):
		controller = self.controller
		if controller.weapon:
			cost = controller.weapon.atk
		else:
			cost = 0
		card1 = Draw(controller).trigger(controller)
		if card1[0] != []:
			card1 = card1[0][0]
			card1.cost -= cost
		card2 = Draw(controller).trigger(controller)
		if card2[0] != []:
			card2 = card2[0][0]
			card2.cost -= cost
		pass
	pass

