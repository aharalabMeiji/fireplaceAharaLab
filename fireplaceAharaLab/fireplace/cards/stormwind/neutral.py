from ..utils import *
#from .logging import log

#SW_003e
#SW_034e
#SW_039t3_te
#SW_039te
#SW_043e
#SW_047e
#SW_048e
#SW_050e
#SW_063e
#SW_086e
#SW_087e
#SW_087e2
#SW_093e
#SW_313t4ee
#SW_315e
#SW_316e
#SW_322e
#SW_322e2
#SW_322e3

#Stormwind_Neutral=['SW_700','SW_701','SW_702','SW_710','SW_710t0','SW_710t1','SW_710t2','SW_710t3','SW_710t4','SW_710t5','SW_710t6','SW_710t7','SW_710t8','SW_710t9','SW_711','SW_712','SW_COIN1','SW_COIN2',]

class SW_006:#OK
	""" Stubborn Suspect
	<b>Deathrattle:</b> Summon a random 3-Cost minion. """
	deathrattle = Summon(CONTROLLER, RANDOM(MINION+(COST==3)))
	pass

class SW_036:#OK
	""" Two-Faced Investor
	[x]At the end of your turn,
reduce the Cost of a card
in your hand by (1). <i>(50%
chance to increase.)</i> """
	events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_HAND),random.choice(['SW_036e','SW_036e2'])))##
	pass

SW_036e=buff(cost=-1)
SW_036e2=buff(cost=1)

class SW_045:#OK
	""" Auctioneer Jaxon
	[x]Whenever you <b>Trade</b>,<b>Discover</b> a card from your_deck to draw instead. """
	pass

class SW_054:#OK
	""" Stormwind Guard
	<b>Taunt</b><b>Battlecry:</b> Give adjacent minions +1/+1. """
	update = BuffOnce(SELF_ADJACENT,'SW_054e')
	#play = Buff(SELF_ADJACENT,'SW_054e')
	pass
SW_054e=buff(atk=1,health=1)

class SW_055:#OK
	""" Impatient Shopkeep
	<b>Tradeable</b><b>Rush</b> """
	#
	pass

class SW_056:#OK
	""" Spice Bread Baker
	<b>Battlecry:</b> Restore Health to your hero equal to your hand size. """
	play = Heal(FRIENDLY_HERO, Count(FRIENDLY_HAND))
	pass

class SW_057:#OK
	""" Package Runner
	Can only attack if you have at least 8 cards in hand. """
	update = (Count(FRIENDLY_HAND)<8) & Refresh(SELF, {GameTag.CANT_ATTACK:True}) | Refresh(SELF,{GameTag.CANT_ATTACK:False}) 
	pass

class SW_059:####OK
	""" Deeprun Engineer
	<b>Battlecry:</b> <b>Discover</b> a Mech. It costs (1) less. """
	play = GenericChoiceBuff(CONTROLLER, RandomMech()*3) # cost 1 less
	pass
SW_059e=buff(cost=-1)#<4>[1578]

class SW_060:#OK
	""" Florist
	[x]At then end of your turn, reduce the cost of a Nature spell in your hand by (1). """
	events = OWN_TURN_END.on(Buff(FRIENDLY_HAND+NATURE,'SW_060t'))
	pass
SW_060t=buff(cost=-1)

class SW_061:#OK
	""" Guild Trader
	<b>Tradeable</b><b>Spell Damage +2</b> """
	#
	pass

class SW_062:#OK
	""" Goldshire Gnoll
	[x]<b>Rush</b>Costs (1) less for each__other card in your hand. """
	update = Refresh(FRIENDLY_HAND - SELF, {GameTag.COST:-1})
	pass

class SW_063:#OK
	""" Battleground Battlemaster
	Adjacent minions have <b>Windfury</b>. """
	update = Refresh(SELF_ADJACENT,{GameTag.WINDFURY:True})
	pass
#SW_63e=buff({GameTag.WINDFURY:True})

class SW_064:#OK
	""" Northshire Farmer
	<b>Battlecry:</b> Choose a friendly Beast. Shuffle three 3/3 copies_into_your_deck. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.BEAST}
	play= ShuffleBuff(CONTROLLER, Copy(TARGET),'SW_064e')*3
	pass
SW_064e=buff(atk=3,health=3)

class SW_065:###OK
	""" Pandaren Importer
	[x]<b>Battlecry:</b> <b>Discover</b> a spell that didn't start in your deck. """
	play=GenericChoice(CONTROLLER,RANDOM(SPELL-FRIENDLY_DECK)*3)
	pass

class SW_066:##動作はしているが、silencedがそもそも動いていない気がする。
	""" Royal Librarian
	[x]<b>Tradeable</b><b>Battlecry:</b> <b>Silence</b>a minion. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0}
	play = SetTag(TARGET,{GameTag.SILENCED:True})
	pass

class SW_067:#OK
	""" Stockades Guard
	[x]<b>Battlecry:</b> Give a friendly minion <b>Taunt</b>. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0}
	play = SetTag(TARGET,{GameTag.TAUNT:True})
	pass

#class SW_068:#OK bigWarrior
#	""" Mo'arg Forgefiend
#	<b>Taunt</b><b>Deathrattle:</b> Gain 8 Armor. """
#	deathrattle = GainArmor(FRIENDLY_HERO,8)
#	pass

class Deposite_Payment(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		if target==[]:
			return
		if isinstance(target,list):
			target = target[0]
		target.zone = Zone.SETASIDE
		source.sidequest_list0.append(target)
		pass
	pass

class Deposite_Withdrawal(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		cards = source.sidequest_list0
		for card in cards:
			Give(target, card.id).trigger(source)
		pass
	pass

class SW_069:#OK
	""" Enthusiastic Banker
	[x]At the end of your turn, store a card from your deck. <b>Deathrattle:</b> Add the stored cards to your hand. """
	events = OWN_TURN_END.on(Deposite_Payment(RANDOM(FRIENDLY_DECK)))
	deathrattle = Deposite_Withdrawal(CONTROLLER)
	pass
class SW_069e:
	""" Safety Deposit """
	pass

class SW_070:#OK
	""" Mailbox Dancer
	[x]<b>Battlecry:</b> Add a Coin to your hand. <b>Deathrattle:</b> Give your opponent one. """
	play = Give(CONTROLLER, 'GAME_005')
	deathrattle = Give(OPPONENT, 'GAME_005')
	pass

class SW_071:#OK
	""" Lion's Guard
	[x]<b>Battlecry:</b> If you have 15 or less Health, gain +2/+4 and <b>Taunt</b>. """
	def play(self):
		if self.controller.hero.health <= 15:
			yield Buff(SELF,'SW_071e')

SW_071e=buff(atk=2,health=4,taunt=True)

class SW_072:#OK
	""" Rustrot Viper
	[x]<b>Tradeable</b><b>Battlecry:</b> Destroy your opponent's weapon. """
	play = Destroy(ENEMY_WEAPON)
	pass

class SW_073:#OK
	""" Cheesemonger
	[x]Whenever your opponent casts a spell, add a random spell with the same Cost to your hand. """
	events = Play(OPPONENT, SPELL).on(Give(CONTROLLER, RandomSpell(cost=Attr(Play.CARD,GameTag.COST))))
	pass

class SW_074:#OK
	""" Nobleman
	<b>Battlecry:</b> Create a Golden copy of a random card in your hand. """
	play = Give(CONTROLLER,Copy(RANDOM(FRIENDLY_HAND)))#gold?
	pass

class SW_075:#OK
	""" Elwynn Boar
	[x]<b>Deathrattle:</b> If you had 7 Elwynn Boars die this game, equip a 15/3 Sword of a ___Thousand Truths.@ <i>(@/7)</i> """
	# if we use LazyNum, we are able to make in much more general way.
	deathrattle = CountDeathAction(CONTROLLER,['SW_075'], 7, Summon(CONTROLLER,'SW_075t'))
	pass
class SW_075t: #OK
	""" [x]After your hero attacks,destroy your opponent's Mana Crystals."""
	events = Attack(FRIENDLY_HERO).on(GainMana(OPPONENT,-10))
	pass

class SW_076:#OK
	""" City Architect
	[x]<b>Battlecry:</b> Summon two 0/5 Castle Walls with <b>Taunt</b>. """
	play = Summon(CONTROLLER, 'SW_076t')*2
	pass
class SW_076t:
	pass

class SW_077:#OK
	""" Stockades Prisoner
	[x]Starts <b>Dormant</b>. After you play 3 cards, this awakens. """ 
	dormant = -1 #infinite dormant
	events = Play(CONTROLLER).on(SidequestCounter(SELF,3,[SetAttr(SELF, 'dormant',0), Awaken(SELF)]))
	#play = Buff(SELF, "SW_077e")
	pass
class SW_077e:
	pass

class SW_078:#OK
	""" Lady Prestor
	[x]<b>Battlecry:</b> Transform minions in your deck into random Dragons. <i>(They keep their
__original stats and Cost.)</I> """
	play = SW_078_Morph(FRIENDLY_DECK,RandomDragon())
	pass
SW_078e=buff(0,0)
SW_078e2=buff(0,0)

class SW_079:###OK
	""" Flightmaster Dungar
	[x]<b>Battlecry:</b> Choose a flightpath and go <b>Dormant.</b> Awaken with a bonus __when you complete it! """
	entourage = ['SW_079t', 'SW_079t2', 'SW_079t3']
	play = GenericChoiceBattlecry(CONTROLLER,RandomEntourage()*3)
	pass
SW_079e4=buff(0,0)
SW_079e5=buff(0,0)
SW_079e6=buff(0,0)
class SW_079t:##OK
	""" >[x]In 1 turn, summon a 2/2 Adventurer with _a random bonus effect. """
	def play(self):
		controller = self.controller
		for main_card in controller.field:
			if main_card.id == 'SW_079':
				main_card.dormant = 1
				setattr(main_card.data.scripts, 'awaken', (SummonAdventurerWithBonus(CONTROLLER),))
				log.info("%r has dormant %d with awaken %r"%(main_card, main_card.dormant, main_card.get_actions("awaken")))
				break;
		controller.hand[-1].zone = Zone.GRAVEYARD
SW_079te=buff(0,0)
class SW_079t2:###OK
	""" Ironforge
	In 3 turns, restore 10 Health to your hero. """
	def play(self):
		controller = self.controller
		for main_card in controller.field:
			if main_card.id == 'SW_079':
				main_card.dormant = 3
				setattr(main_card.data.scripts, 'awaken', (Heal(FRIENDLY_HERO,10),))
				log.info("%r has dormant %d with awaken %r"%(main_card, main_card.dormant, main_card.get_actions("awaken")))
				break
		controller.hand[-1].zone = Zone.GRAVEYARD
SW_079t2e=buff(0,0)
class SW_079t3:###OK
	""" Eastern Plaguelands
	In 5 turns, deal 12 damage randomly split among enemies."""
	def play(self):
		controller = self.controller
		for main_card in controller.field:
			if main_card.id == 'SW_079':
				main_card.dormant = 5
				setattr(main_card.data.scripts, 'awaken', (Hit(RANDOM(ENEMY_CHARACTERS),1) * 12,))
				log.info("%r has dormant %d with awaken %r"%(main_card, main_card.dormant, main_card.get_actions("awaken")))
				break
		controller.hand[-1].zone = Zone.GRAVEYARD
SW_079t3e=buff(0,0)

class SW_080:#OK
	""" Cornelius Roame
	[x]At the start and end
_of each player's turn,
draw a card. """
	events = [OWN_TURN_END.on(Draw(CONTROLLER)), OWN_TURN_BEGIN.on(Draw(OPPONENT))]
	pass

class SW_081:#OK
	""" Varian, King of Stormwind
	[x]<b>Battlecry:</b> Draw a <b>Rush</b> minion to gain <b>Rush</b>. Repeat for <b>Taunt</b> and <b>Divine Shield</b>. """
	play = [
		Find(FRIENDLY_DECK + RUSH) & Give(CONTROLLER,RANDOM(FRIENDLY_DECK + RUSH)).then(SetAttr(SELF,'rush', True)),
		Find(FRIENDLY_DECK + TAUNT) & Give(CONTROLLER,RANDOM(FRIENDLY_DECK + TAUNT)).then(SetAttr(SELF,'taunt', True)),
		Find(FRIENDLY_DECK + DIVINE_SHIELD) & Give(CONTROLLER,RANDOM(FRIENDLY_DECK + DIVINE_SHIELD)).then(SetAttr(SELF,'divine_shield', True)),
		]
	pass

class SW_306:#OK
	# CASTSWHENDRAWN タグなし
	#description が無限ループを含んでいるが・・・・GiveとDrawを区別して解決。
	""" Encumbered Pack Mule
	[x]<b>Taunt</b> When you draw this, add a _copy of it to your hand. """
	#
	pass

class SW_307:#OK
	""" Traveling Merchant
	[x]<b>Tradeable</b><b>Battlecry:</b> Gain +1/+1 for each other friendly _minion you control. """
	play = Buff(SELF,'SW_307e') * Count(FRIENDLY_MINIONS - SELF)
	pass
SW_307e=buff(atk=1,health=1)

class SW_319:#OK
	""" Peasant
	At the start of your turn, draw a card. """
	events = OWN_TURN_BEGIN.on(Draw(CONTROLLER))
	pass

class SW_400:#OK
	""" Entrapped Sorceress
	[x]<b>Battlecry:</b> If you control a _<b>Quest</b>, <b>Discover</b> a spell. """
	powered_up = Find(FRIENDLY + EnumSelector(GameTag.SIDEQUEST))
	play = powered_up & Discover(CONTROLLER, RandomSpell())
	pass

class SW_418:#OK
	""" SI:7 Skulker
	[x]<b>Stealth</b><b>Battlecry:</b> The next card _you draw costs (1) less. """
	play = Buff(CONTROLLER,'SW_418e')
	pass
class SW_418e:
	events = Draw(CONTROLLER).on(Buff(Draw.CARD,'SW_418e2'),Destroy(SELF))
	pass
SW_418e2=buff(cost=-1)
