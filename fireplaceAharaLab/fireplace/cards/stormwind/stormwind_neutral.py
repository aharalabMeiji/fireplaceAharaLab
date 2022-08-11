from ..utils import *
#from .logging import log


from ..utils import *

Stormwind_Neutral=[]

Stormwind_Mr_Smite=True  ####OK
Stormwind_Maddest_Bomber=True  ####OK
Stormwind_Golakka_Glutton=True  ####OK
Stormwind_Multicaster=True  ####OK
Stormwind_Goliath_Sneeds_Masterpiece=True  ####OK
Stormwind_Stubborn_Suspect=True  ####OK
Stormwind_Two_Faced_Investor=True  ####OK
Stormwind_Auctioneer_Jaxon=True  ####OK
Stormwind_Stormwind_Guard=True  ####OK
Stormwind_Impatient_Shopkeep=True  ####OK
Stormwind_Spice_Bread_Baker=True  ####OK
Stormwind_Package_Runner=True  ####OK
Stormwind_Deeprun_Engineer=True  ####OK
Stormwind_Florist=True  ####OK
Stormwind_Guild_Trader=True  ####OK
Stormwind_Goldshire_Gnoll=True  ####OK
Stormwind_Battleground_Battlemaster=True  ####OK
Stormwind_Northshire_Farmer=True  ####OK
Stormwind_Pandaren_Importer=True  ####OK
Stormwind_Royal_Librarian=True  ####OK
Stormwind_Stockades_Guard=True  ####OK
Stormwind_Moarg_Forgefiend=True  ####OK
Stormwind_Enthusiastic_Banker=True  ####OK
Stormwind_Mailbox_Dancer=True  ####OK
Stormwind_Lions_Guard=True  ####OK
Stormwind_Rustrot_Viper=True  ####OK
Stormwind_Cheesemonger=True  ####OK
Stormwind_Nobleman=True  ####OK
Stormwind_Elwynn_Boar=True  ####OK
Stormwind_City_Architect=True  ####OK
Stormwind_Stockades_Prisoner=True  ####OK
Stormwind_Lady_Prestor=True  ####OK
Stormwind_Flightmaster_Dungar=True  ####OK
Stormwind_Cornelius_Roame=True  ####OK
Stormwind_Varian_King_of_Stormwind=True  ####OK
Stormwind_Encumbered_Pack_Mule=True  ####OK
Stormwind_Traveling_Merchant=True  ####OK
Stormwind_Peasant=True  ####OK
Stormwind_Entrapped_Sorceress=True  ####OK
Stormwind_SI7_Skulker=True  ####OK



########################




if Stormwind_Mr_Smite:# 
	Stormwind_Neutral+=['DED_006']
	Stormwind_Neutral+=['DED_006e2']
class DED_006:# <12>[1578] ###OK
	""" Mr. Smite
	Your Pirates have [Charge]. """
	play = Buff(FRIENDLY_MINIONS + PIRATE, 'DED_006e2')
	pass

DED_006e2 = buff(charge=True)# <12>[1578]
""" Charge
{0} grants [Charge]. """





if Stormwind_Maddest_Bomber:# 
	Stormwind_Neutral+=['DED_521']
class DED_521:# <12>[1578] ####OK
	""" Maddest Bomber
	[Battlecry:] Deal 12 damage randomly split among all other characters. """
	play = Hit(RANDOM(ALL_CHARACTERS - SELF),1) * 12
	pass




if Stormwind_Golakka_Glutton:# 
	Stormwind_Neutral+=['DED_523']
class DED_523:# <12>[1578] ###OK
	""" Golakka Glutton
	[Battlecry:] Destroy a Beast and gain +1/+1. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.BEAST}
	play = (Destroy(TARGET), Buff(SELF, 'DED_523e'))
	pass

DED_523e = buff(1,1)# <12>[1578]
""" Stuffed Belly +1/+1. """




if Stormwind_Multicaster:# 
	Stormwind_Neutral+=['DED_524']
class DED_524:# <12>[1578]###OK
	""" Multicaster
	[Battlecry:] Draw a card for each different spell school_you've cast this game. """
	def play(self):
		play_log = self.controller.play_log
		school_count=[0] * 6
		for card in play_log:
			if card.type == CardType.SPELL:
				if card.spell_school == SpellSchool.ARCANE:
					school_count[0] = 1
				if card.spell_school == SpellSchool.FIRE:
					school_count[1] = 1
				if card.spell_school == SpellSchool.FROST:
					school_count[2] = 1
				if card.spell_school == SpellSchool.NATURE:
					school_count[3] = 1
				if card.spell_school == SpellSchool.HOLY:
					school_count[4] = 1
				if card.spell_school == SpellSchool.SHADOW:
					school_count[5] = 1
			pass
		pass
		count = sum(school_count)
		for i in range(count):
			Draw(self.controller).trigger(self.controller)
	pass





if Stormwind_Goliath_Sneeds_Masterpiece:# 
	Stormwind_Neutral+=['DED_525']
class DED_525Choice(Choice):
	def choose(self, card):
		self.source._sidequest_counter_ += 1
		if self.source._sidequest_counter_>=5:
			self.next_choice=None
		else:
			self.next_choice=self
		self.callback = [Hit(card, 2)]
		super().choose(card)
		self.cards = self.player.opponent.field
class DED_525:# <12>[1578] #### maybe success
	""" Goliath, Sneed's Masterpiece
	[Battlecry:] Fire five rockets at enemy minions that deal 2 damage each. <i>(You pick the targets!)</i> """
	play = DED_525Choice(CONTROLLER, ENEMY_MINIONS)
	#play = GenericChoiceFromEnemyMinions(CONTROLLER, [Hit(GenericChoiceFromEnemyMinions.CARD, 2)]) * 5
	pass






if Stormwind_Stubborn_Suspect:# 
	Stormwind_Neutral+=['SW_006']
class SW_006:#OK
	""" Stubborn Suspect
	<b>Deathrattle:</b> Summon a random 3-Cost minion. """
	deathrattle = Summon(CONTROLLER, RANDOM(MINION+(COST==3)))
	pass



if Stormwind_Two_Faced_Investor:# 
	Stormwind_Neutral+=['SW_036']
	Stormwind_Neutral+=['SW_036e']
	Stormwind_Neutral+=['SW_036e2']
class SW_036:#OK
	""" Two-Faced Investor
	[x]At the end of your turn,reduce the Cost of a cardin your hand by (1). <i>(50%chance to increase.)</i> """
	events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_HAND),random.choice(['SW_036e','SW_036e2'])))##
	#events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_HAND),RandomID('SW_036e','SW_036e2')))##
	pass
SW_036e=buff(cost=-1)
SW_036e2=buff(cost=1)





if Stormwind_Auctioneer_Jaxon:# 
	Stormwind_Neutral+=['SW_045']
class SW_045:#OK
	""" Auctioneer Jaxon
	[x]Whenever you <b>Trade</b>,<b>Discover</b> a card from your_deck to draw instead. """
	pass



if Stormwind_Stormwind_Guard:# 
	Stormwind_Neutral+=['SW_054']
	Stormwind_Neutral+=['SW_054e']
class SW_054:#OK
	""" Stormwind Guard
	<b>Taunt</b><b>Battlecry:</b> Give adjacent minions +1/+1. """
	update = BuffOnce(SELF_ADJACENT,'SW_054e')
	#play = Buff(SELF_ADJACENT,'SW_054e')
	pass
SW_054e=buff(atk=1,health=1)


if Stormwind_Impatient_Shopkeep:# 
	Stormwind_Neutral+=['SW_055']
class SW_055:#OK
	""" Impatient Shopkeep
	<b>Tradeable</b><b>Rush</b> """
	pass




if Stormwind_Spice_Bread_Baker:# 
	Stormwind_Neutral+=['SW_056']
class SW_056:#OK
	""" Spice Bread Baker
	<b>Battlecry:</b> Restore Health to your hero equal to your hand size. """
	play = Heal(FRIENDLY_HERO, Count(FRIENDLY_HAND))
	pass




if Stormwind_Package_Runner:# 
	Stormwind_Neutral+=['SW_057']
class SW_057:#OK
	""" Package Runner
	Can only attack if you have at least 8 cards in hand. """
	update = (Count(FRIENDLY_HAND)<8) & Refresh(SELF, {GameTag.CANT_ATTACK:True}) | Refresh(SELF,{GameTag.CANT_ATTACK:False}) 
	pass




if Stormwind_Deeprun_Engineer:# 
	Stormwind_Neutral+=['SW_059','SW_059e']
class SW_059:####OK
	""" Deeprun Engineer
	<b>Battlecry:</b> <b>Discover</b> a Mech. It costs (1) less. """
	play = GenericChoiceBuff(CONTROLLER, RandomMech()*3) # cost 1 less
	pass
SW_059e=buff(cost=-1)#<4>[1578]




if Stormwind_Florist:# 
	Stormwind_Neutral+=['SW_060']
	Stormwind_Neutral+=['SW_060t']
class SW_060:#OK
	""" Florist
	[x]At then end of your turn, reduce the cost of a Nature spell in your hand by (1). """
	events = OWN_TURN_END.on(Buff(FRIENDLY_HAND+NATURE,'SW_060t'))
	pass
SW_060t=buff(cost=-1)




if Stormwind_Guild_Trader:# 
	Stormwind_Neutral+=['SW_061']
class SW_061:#OK
	""" Guild Trader
	<b>Tradeable</b><b>Spell Damage +2</b> """
	#
	pass




if Stormwind_Goldshire_Gnoll:# 
	Stormwind_Neutral+=['SW_062']
class SW_062:#OK
	""" Goldshire Gnoll
	[x]<b>Rush</b>Costs (1) less for each__other card in your hand. """
	update = Refresh(FRIENDLY_HAND - SELF, {GameTag.COST:-1})
	pass




if Stormwind_Battleground_Battlemaster:# 
	Stormwind_Neutral+=['SW_063']
	#Stormwind_Neutral+=['SW_063e']
class SW_063:#OK
	""" Battleground Battlemaster
	Adjacent minions have <b>Windfury</b>. """
	update = Refresh(SELF_ADJACENT,{GameTag.WINDFURY:True})
	pass
#SW_63e=buff({GameTag.WINDFURY:True})




if Stormwind_Northshire_Farmer:# 
	Stormwind_Neutral+=['SW_064']
class SW_064:#OK
	""" Northshire Farmer
	<b>Battlecry:</b> Choose a friendly Beast. Shuffle three 3/3 copies_into_your_deck. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE: Race.BEAST}
	play= ShuffleBuff(CONTROLLER, Copy(TARGET),'SW_064e')*3
	pass
SW_064e=buff(atk=3,health=3)




if Stormwind_Pandaren_Importer:# 
	Stormwind_Neutral+=['SW_065']
class SW_065:###OK
	""" Pandaren Importer
	[x]<b>Battlecry:</b> <b>Discover</b> a spell that didn't start in your deck. """
	play=GenericChoice(CONTROLLER,RANDOM(SPELL-FRIENDLY_DECK)*3)
	pass




if Stormwind_Royal_Librarian:# 
	Stormwind_Neutral+=['SW_066']
class SW_066:##動作はしているが、silencedがそもそも動いていない気がする。
	""" Royal Librarian
	[x]<b>Tradeable</b><b>Battlecry:</b> <b>Silence</b>a minion. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0}
	play = SetTag(TARGET,{GameTag.SILENCED:True})
	pass




if Stormwind_Stockades_Guard:# 
	Stormwind_Neutral+=['SW_067']
class SW_067:#OK
	""" Stockades Guard
	[x]<b>Battlecry:</b> Give a friendly minion <b>Taunt</b>. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_FRIENDLY_TARGET:0, PlayReq.REQ_MINION_TARGET:0}
	play = SetTag(TARGET,{GameTag.TAUNT:True})
	pass




if Stormwind_Moarg_Forgefiend:# 
	Stormwind_Neutral+=['SW_068']
class SW_068:#OK bigWarrior
	""" Mo'arg Forgefiend
	<b>Taunt</b><b>Deathrattle:</b> Gain 8 Armor. """
	deathrattle = GainArmor(FRIENDLY_HERO,8)
#	pass




if Stormwind_Enthusiastic_Banker:# 
	Stormwind_Neutral+=['SW_069','SW_069e']
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




if Stormwind_Mailbox_Dancer:# 
	Stormwind_Neutral+=['SW_070']
class SW_070:#OK
	""" Mailbox Dancer
	[x]<b>Battlecry:</b> Add a Coin to your hand. <b>Deathrattle:</b> Give your opponent one. """
	play = Give(CONTROLLER, 'GAME_005')
	deathrattle = Give(OPPONENT, 'GAME_005')
	pass



if Stormwind_Lions_Guard:# 
	Stormwind_Neutral+=['SW_071']
	Stormwind_Neutral+=['SW_071e']
class SW_071:#OK
	""" Lion's Guard
	[x]<b>Battlecry:</b> If you have 15 or less Health, gain +2/+4 and <b>Taunt</b>. """
	def play(self):
		if self.controller.hero.health <= 15:
			yield Buff(SELF,'SW_071e')
SW_071e=buff(atk=2,health=4,taunt=True)




if Stormwind_Rustrot_Viper:# 
	Stormwind_Neutral+=['SW_072']
class SW_072:#OK
	""" Rustrot Viper
	[x]<b>Tradeable</b><b>Battlecry:</b> Destroy your opponent's weapon. """
	play = Destroy(ENEMY_WEAPON)
	pass




if Stormwind_Cheesemonger:# 
	Stormwind_Neutral+=['SW_073']
class SW_073:#OK
	""" Cheesemonger
	[x]Whenever your opponent casts a spell, add a random spell with the same Cost to your hand. """
	events = Play(OPPONENT, SPELL).on(Give(CONTROLLER, RandomSpell(cost=Attr(Play.CARD,GameTag.COST))))
	pass




if Stormwind_Nobleman:# 
	Stormwind_Neutral+=['SW_074']
class SW_074:#OK
	""" Nobleman
	<b>Battlecry:</b> Create a Golden copy of a random card in your hand. """
	play = Give(CONTROLLER,Copy(RANDOM(FRIENDLY_HAND)))#gold?
	pass




if Stormwind_Elwynn_Boar:# 
	Stormwind_Neutral+=['SW_075','SW_075t']
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




if Stormwind_City_Architect:# 
	Stormwind_Neutral+=['SW_076','SW_076t']
class SW_076:#OK
	""" City Architect
	[x]<b>Battlecry:</b> Summon two 0/5 Castle Walls with <b>Taunt</b>. """
	play = Summon(CONTROLLER, 'SW_076t')*2
	pass
class SW_076t:
	pass




if Stormwind_Stockades_Prisoner:# 
	Stormwind_Neutral+=['SW_077','SW_077e']
class SW_077:#OK
	""" Stockades Prisoner
	[x]Starts <b>Dormant</b>. After you play 3 cards, this awakens. """ 
	dormant = -1 #infinite dormant
	events = Play(CONTROLLER).on(SidequestCounter(SELF,3,[SetAttr(SELF, 'dormant',0), Awaken(SELF)]))
	#play = Buff(SELF, "SW_077e")
	pass
class SW_077e:
	pass





if Stormwind_Lady_Prestor:# 
	Stormwind_Neutral+=['SW_078','SW_078e','SW_078e2']
class SW_078:#OK
	""" Lady Prestor
	[x]<b>Battlecry:</b> Transform minions in your deck into random Dragons. <i>(They keep their
__original stats and Cost.)</I> """
	play = SW_078_Morph(FRIENDLY_DECK,RandomDragon())
	pass
SW_078e=buff(0,0)
SW_078e2=buff(0,0)




if Stormwind_Flightmaster_Dungar:# 
	Stormwind_Neutral+=['SW_079']
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
				if Config.LOGINFO:
					print("%r has dormant %d with awaken %r"%(main_card, main_card.dormant, main_card.get_actions("awaken")))
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
				if Config.LOGINFO:
					print("%r has dormant %d with awaken %r"%(main_card, main_card.dormant, main_card.get_actions("awaken")))
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
				if Config.LOGINFO:
					print("%r has dormant %d with awaken %r"%(main_card, main_card.dormant, main_card.get_actions("awaken")))
				break
		controller.hand[-1].zone = Zone.GRAVEYARD
SW_079t3e=buff(0,0)





if Stormwind_Cornelius_Roame:# 
	Stormwind_Neutral+=['SW_080']
class SW_080:#OK
	""" Cornelius Roame
	[x]At the start and end
_of each player's turn,
draw a card. """
	events = [OWN_TURN_END.on(Draw(CONTROLLER)), OWN_TURN_BEGIN.on(Draw(OPPONENT))]
	pass




if Stormwind_Varian_King_of_Stormwind:# 
	Stormwind_Neutral+=['SW_081']
class SW_081:#OK
	""" Varian, King of Stormwind
	[x]<b>Battlecry:</b> Draw a <b>Rush</b> minion to gain <b>Rush</b>. Repeat for <b>Taunt</b> and <b>Divine Shield</b>. """
	play = [
		Find(FRIENDLY_DECK + RUSH) & Give(CONTROLLER,RANDOM(FRIENDLY_DECK + RUSH)).then(SetAttr(SELF,'rush', True)),
		Find(FRIENDLY_DECK + TAUNT) & Give(CONTROLLER,RANDOM(FRIENDLY_DECK + TAUNT)).then(SetAttr(SELF,'taunt', True)),
		Find(FRIENDLY_DECK + DIVINE_SHIELD) & Give(CONTROLLER,RANDOM(FRIENDLY_DECK + DIVINE_SHIELD)).then(SetAttr(SELF,'divine_shield', True)),
		]
	pass







if Stormwind_Encumbered_Pack_Mule:# 
	Stormwind_Neutral+=['SW_306']
class SW_306:#OK
	# CASTSWHENDRAWN タグなし
	#description が無限ループを含んでいるが・・・・GiveとDrawを区別して解決。
	""" Encumbered Pack Mule
	[x]<b>Taunt</b> When you draw this, add a _copy of it to your hand. """
	#
	pass




if Stormwind_Traveling_Merchant:# 
	Stormwind_Neutral+=['SW_307','SW_307e']
class SW_307:#OK
	""" Traveling Merchant
	[x]<b>Tradeable</b><b>Battlecry:</b> Gain +1/+1 for each other friendly _minion you control. """
	play = Buff(SELF,'SW_307e') * Count(FRIENDLY_MINIONS - SELF)
	pass
SW_307e=buff(atk=1,health=1)



if Stormwind_Peasant:# 
	Stormwind_Neutral+=['SW_319']
class SW_319:#OK
	""" Peasant
	At the start of your turn, draw a card. """
	events = OWN_TURN_BEGIN.on(Draw(CONTROLLER))
	pass





if Stormwind_Entrapped_Sorceress:# 
	Stormwind_Neutral+=['SW_400']
class SW_400:#OK
	""" Entrapped Sorceress
	[x]<b>Battlecry:</b> If you control a _<b>Quest</b>, <b>Discover</b> a spell. """
	powered_up = Find(FRIENDLY + EnumSelector(GameTag.SIDEQUEST))
	play = powered_up & Discover(CONTROLLER, RandomSpell())
	pass




if Stormwind_SI7_Skulker:# 
	Stormwind_Neutral+=['SW_418']
class SW_418:#OK
	""" SI:7 Skulker
	[x]<b>Stealth</b><b>Battlecry:</b> The next card _you draw costs (1) less. """
	play = Buff(CONTROLLER,'SW_418e')
	pass
class SW_418e:
	events = Draw(CONTROLLER).on(Buff(Draw.CARD,'SW_418e2'),Destroy(SELF))
	pass
SW_418e2=buff(cost=-1)





