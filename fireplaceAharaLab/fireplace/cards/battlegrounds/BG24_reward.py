from ..utils import *
import collections

BG24_Reward=[]
BG24_Reward_Pool=[]

BG24_Reward_Snicker_Snacks=True ### OK ### 
BG24_Reward_Stolen_Gold=True### OK ###
BG24_Reward_Evil_Twin=True#### OK ###
BG24_Reward_Ritual_Dagger=True  #### OK ###
BG24_Reward_Theotars_Parasol=True ## banned ## renew 24.6 ### OK ###
#BG24_Reward_Exquisite_Conch=False # not in service
BG24_Reward_The_Smoking_Gun=True### OK ###
BG24_Reward_Mirror_Shield=True#### OK ###
BG24_Reward_Secret_Sinstone=True#### OK ###
BG24_Reward_Ghastly_Mask=True#### OK ###
BG24_Reward_Red_Hand=True#### OK ###
BG24_Reward_The_Friends_Along_the_Way=True #
BG24_Reward_Yogg_tastic_Tasties=True# ### OK ###
BG24_Reward_Tiny_Henchmen=True #### OK ###
BG24_Reward_Victims_Specter=True#### OK ###
#BG24_Reward_A_Good_Time=False# not in service
#BG24_Reward_Avatar_of_the_Coin=False# not in service
BG24_Reward_Anima_Bribe=False ## banned 24.6
BG24_Reward_Cooked_Book=True### OK ###
BG24_Reward_Teal_Tiger_Sapphire=True#### OK ###
BG24_Reward_Devils_in_the_Details=True#### OK ###
#BG24_Reward_Partner_in_Crime=False# not in service
BG24_Reward_Another_Hidden_Body=True## banned 24.2.1 # renew ### OK ###
BG24_Reward_Staff_of_Origination=True#### OK ###
BG24_Reward_Wondrous_Wisdomball=True# #### OK ###
#BG24_Reward_To_The_Moon_Almost=False# not in service
BG24_Reward_Alter_Ego=True #### OK ###
#BG24_Reward_9_Lives=False ### not in service
BG24_Reward_Menagerie_Mayhem=True #### OK ###
BG24_Reward_Pilfered_Lamps=True ### OK ###
#BG24_Reward_Totemic_Tavern=False ### not in service
#BG24_Reward_Purified_Shard=False ### not in service
#BG24_Reward_Un_Murloc_Your_Potential=False ### not in service
BG24_Reward_Hidden_Treasure_Vault=True # new 24.6### OK ###
BG24_Reward_Essence_of_Zerus=True # new 24.6 ### OK ###
BG24_Reward_Ethereal_Evidence=True # new 24.6  ### OK ###
BG24_Reward_Volatile_Venom=True # new 24.6 ### OK ###
BG24_Reward_Blood_Goblet=True # new 24.6#### OK ###
BG24_Reward_Sinfall_Medallion=True # new 24.6  ### OK ###
BG24_Enhance_a_matic=True # new 25.0 ### OK ###
BG24_Reward_Kidnap_Sack=True # new 24.6.2 ### OK ###
BG24_Reward_The_Golden_Hammer=True # new 24.6.2  ### OK ###


if BG24_Reward_Snicker_Snacks:# ### OK ###
	BG24_Reward+=['BG24_Reward_107']
	BG24_Reward_Pool+=['BG24_Reward_107']
class BG24_Reward_107_Action(GameAction):
	def do(self, source):
		controller = source.controller
		cards = [card for card in controller.field if card.has_battlecry==True]
		if len(cards)>2:
			cards = random.sample(cards, 2)
		for card in cards:
			PlayBattlecry(card).trigger(source)
		pass
class BG24_Reward_107:# [2467]=140, [2641]=1, [2647]=50, 
	# -> [2467]=120, [2641]=1, [2647]=60 (24.2.2) (easy to obtain)
	""" Snicker Snacks
	At the end of your turn, 2 friendly minions trigger their [Battlecries]. """
	events = OWN_TURN_END.on(BG24_Reward_107_Action())
	#<Tag enumID="201" name="FACTION" type="Int" value="3"/>
	pass




if BG24_Reward_Stolen_Gold:# ### OK ###
	BG24_Reward+=['BG24_Reward_109']
	BG24_Reward_Pool+=['BG24_Reward_109']
class BG24_Reward_109_Action(GameAction):
	def do(self, source):
		controller=source.controller
		if len(controller.field)>0:
			card1 = controller.field[0]
			controller.game.BG_morph_gold(card1)
			if len(controller.field)>1:
				card2 = controller.field[-1]
				controller.game.BG_morph_gold(card2)
		pass
class BG24_Reward_109:# [1500]=1, [2467]=80, [2641]=1, [2643]=90, [2646]=90, [2727]=1,
	# [1500]=1, [2467]=140, [2641]=1, [2643]=90, [2645]=90, [2646]=90, [2727]=1,(24.2.2 harder)
	# [2467]=160 (24.6 harder)
	""" Stolen Gold
	[Start of Combat:] Make your left and right- most minions Golden. """
	events = BeginBattle(CONTROLLER).on(BG24_Reward_109_Action())
	pass



if BG24_Reward_Evil_Twin:# ### OK ###
	BG24_Reward+=['BG24_Reward_111']
	BG24_Reward_Pool+=['BG24_Reward_111']
class BG24_Reward_111_Action(GameAction):
	def do(self, source):
		controller=source.controller
		if len(controller.field)<7:
			high=[]
			for card in controller.field:
				if high==[] or high[0].health<card.health:
					high=[card]
				elif high[0].health==card.health:
					high.append(card)
			if len(high):
				card = random.choice(high)
				ret = exactCopy(card, source)
				ret.zone=Zone.PLAY
class BG24_Reward_111:# [1500]=1, [2467]=150, [2641]=1, [2647]=120, [2727]=1, 
	""" Evil Twin
	[Start of Combat:] Summon a copy of your highest-Health minion. """
	events = BeginBattle(CONTROLLER).on(BG24_Reward_111_Action())
	pass




if BG24_Reward_Ritual_Dagger:# ### OK ###
	BG24_Reward+=['BG24_Reward_113']
	#BG24_Reward+=['BG24_Reward_113_ALT']
	BG24_Reward+=['BG24_Reward_113e']
	BG24_Reward_Pool+=['BG24_Reward_113']
class BG24_Reward_113:# [2467]=80, [2641]=1, 
	""" Ritual Dagger
	After a friendly [Deathrattle] minion dies, give it +4/+4 permanently. """
	events = Death(FRIENDLY + DEATHRATTLE).on(BuffPermanently(Death.ENTITY, 'BG24_Reward_113e'))
	pass
class BG24_Reward_113_ALT:# [2467]=70, [2643]=90, [2646]=90, 
	""" Ritual Dagger
	Your first [Deathrattle] each combat triggers an extra time. """
	pass
BG24_Reward_113e=buff(4,4)




if BG24_Reward_Theotars_Parasol:# ### OK ### renew 24.6
	BG24_Reward+=['BG24_Reward_115']
	BG24_Reward+=['BG24_Reward_115e']
	BG24_Reward+=['BG24_Reward_115e2']
	BG24_Reward_Pool+=['BG24_Reward_115']
class BG24_Reward_115_Action(GameAction):
	def do(self, source):
		controller=source.controller
		if len(controller.field)>0:
			card = controller.field[-1]
			BuffPermanently(card, 'BG24_Reward_115e').trigger(source)
			Buff(card, 'BG24_Reward_115e2').trigger(source)
		pass
class BG24_Reward_115:# [2467]=70, [2641]=1, 
	""" Theotar's Parasol
	At the end of your turn, give your right-most minion [Stealth] until next turn and +8 Health. """
	events = BeginBattle(CONTROLLER).on(BG24_Reward_115_Action())
	pass
BG24_Reward_115e=buff(0,8)
class BG24_Reward_115e2:# [2594]=1, 
	""" Shady
	[Stealth] until next turn. """
	def apply(self, target):
		target.stealthed=True
	pass

#if BG24_Reward_Exquisite_Conch:# not in service
#	BG24_Reward+=['BG24_Reward_123']
#	BG24_Reward_Pool+=['BG24_Reward_123']
#class BG24_Reward_123:# [2467]=80, [2647]=50, ### not in service
#	""" Exquisite Conch
#	Your first [Battlecry] each turn triggers 2 extra times. """
#	#
#	pass

if BG24_Reward_The_Smoking_Gun:# ### OK ###
	BG24_Reward+=['BG24_Reward_125']
	BG24_Reward+=['BG24_Reward_125e']
	BG24_Reward_Pool+=['BG24_Reward_125']
class BG24_Reward_125:# [2467]=110, [2641]=1, [2643]=70, [2646]=80, 
	# [2467]=150, [2641]=1, [2643]=70, [2646]=80, (harder to obtain it)
	""" The Smoking Gun
	Your minions have +4 Attack. """ ## new 24.4.3
	##Your minions have +5 Attack. """
	update = Refresh(FRIENDLY_MINIONS , buff='BG24_Reward_125e')
	pass
BG24_Reward_125e=buff(4,0)# new 24.4.3
##BG24_Reward_125e=buff(5,0)# 




if BG24_Reward_Mirror_Shield:# ### OK ###
	BG24_Reward+=['BG24_Reward_128']
	BG24_Reward+=['BG24_Reward_128e']
	BG24_Reward_Pool+=['BG24_Reward_128']
class BG24_Reward_128:# [2467]=75, [2641]=1, 
	# [2467]=130, [2641]=1, [2647]=85 (harder to obatain it)
	""" Mirror Shield
	After each [Refresh], give a minion in Bob's Tavern +4/+4 and [Divine Shield]. """
	events = Rerole(CONTROLLER).after(Buff(RANDOM(ENEMY_MINIONS), 'BG24_Reward_128e'))
	pass
class BG24_Reward_128e:#
	""" Mirror Shield
	+4/+4 and [Divine Shield]. """
	tags = {
		GameTag.ATK:4,
		GameTag.HEALTH:4
		}
	def apply(self, target):
		target.divine_shield=True
	pass




if BG24_Reward_Secret_Sinstone:# ### OK ###
	BG24_Reward+=['BG24_Reward_129']
	BG24_Reward_Pool+=['BG24_Reward_129']
class BG24_Reward_129_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		#controller = source.controller
		if hasattr(target, 'type') and target.type==CardType.MINION:
			card = exactCopy(target, source)
			card.zone=Zone.HAND
		pass
class BG24_Reward_129:# [2467]=130, [2641]=1, 
	""" Secret Sinstone
	After you [Discover] a card, get an extra copy of it. """
	events = Choice(CONTROLLER).after(BG24_Reward_129_Action(Choice.CARD))
	pass

if BG24_Reward_Ghastly_Mask:#### OK ###
	BG24_Reward+=['BG24_Reward_130']
	BG24_Reward_Pool+=['BG24_Reward_130']
def BG24_Reward_130_Action1(player, reward):
	reward_card = RandomBGAdmissible(tech_level=random.choice([5,6])).evaluate(player)## [5,6]
	reward.script_data_text_0=reward_card[0]
class BG24_Reward_130_Action2(GameAction):
	def do(self, source):
		controller=source.controller
		controller.game.turn_end_effects_twice=True
		if source.script_data_text_0!=[] and source.script_data_text_0!='':
			Give(controller, source.script_data_text_0).trigger(controller)
			source.script_data_text_0=[]
		pass
class BG24_Reward_130:# [2467]=230, [2641]=1, [2673]=59707, [2677]=1, 
	""" Ghastly Mask
	Add '{0}' to your hand. Your end of turn effects trigger twice. """
	events = BeginBar(CONTROLLER).on(BG24_Reward_130_Action2())
	pass




if BG24_Reward_Red_Hand:# ### OK ###
	BG24_Reward+=['BG24_Reward_131']
	BG24_Reward+=['BG24_Reward_131e']
	BG24_Reward_Pool+=['BG24_Reward_131']
class BG24_Reward_131:# [2467]=110, [2641]=1
	# -> [2467]=90, [2641]=1 (24.2.2, easier to obtain)
	""" Red Hand
	At the start of your turn, give a minion in your hand +12/+12. """
	events = BeginBar(CONTROLLER).on(Buff(RANDOM(FRIENDLY_HAND), 'BG24_Reward_131e'))
	pass
BG24_Reward_131e=buff(12,12)




if BG24_Reward_The_Friends_Along_the_Way:# ## OK ###
	BG24_Reward+=['BG24_Reward_134']
	BG24_Reward_Pool+=['BG24_Reward_134']
def BG24_Reward_134_Action1(source):
	source.script_data_num_1=random.choice(random_picker.BG_races)
	pass
class BG24_Reward_134_Action2(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=source.controller
		tier = controller.tavern_tier
		if target!=None and hasattr(target, 'this_is_questreward') and target.script_data_num_1!=None:
			Give(controller, RandomBGMinion(race=target.script_data_num_1,tech_level_less=tier)).trigger(source)
			Give(controller, RandomBGMinion(race=target.script_data_num_1,tech_level_less=tier)).trigger(source)
		pass
class BG24_Reward_134:# [2467]=140, [2571]=1, [2641]=1, 
	""" The Friends Along the Way
	At the start of your turn, get 2 random {0}. """
	#{0} = Race.SOMETHING
	events = BeginBar(CONTROLLER).on(BG24_Reward_134_Action2(SELF))
	pass




if BG24_Reward_Yogg_tastic_Tasties:###  ### OK ###
	BG24_Reward+=['BG24_Reward_135']
	BG24_Reward_Pool+=['BG24_Reward_135']
class BG24_Reward_135_Action(GameAction):
	def do(self, source):
		controller=source.controller
		#cards=['TB_BaconShop_HERO_35_Buddy_t2',
		#   'TB_BaconShop_HERO_35_Buddy_t3',
		#   'TB_BaconShop_HERO_35_Buddy_t4',
		#   'TB_BaconShop_HERO_35_Buddy_t5',
		#   'TB_BaconShop_HERO_35_Buddy_t6',
		#   'TB_BaconShop_HERO_35_Buddy_t7']
		## 19% for each, 5% for t6
		point = random.choice(range(100))
		if point<19:
			card='TB_BaconShop_HERO_35_Buddy_t2'
		elif point<38:
			card='TB_BaconShop_HERO_35_Buddy_t3'
		elif point<57:
			card='TB_BaconShop_HERO_35_Buddy_t4'
		elif point<76:
			card='TB_BaconShop_HERO_35_Buddy_t5'
		elif point<95:
			card='TB_BaconShop_HERO_35_Buddy_t7'
		else:
			card='TB_BaconShop_HERO_35_Buddy_t6'
		Give(controller, card).trigger(source)
		pass
class BG24_Reward_135:# [2467]=150, [2641]=1, [2653]=300,  
	""" Yogg-tastic Tasties
	At the start of your turn, spin the Wheel of Yogg-Saron. """
	#### see TB_BaconShop_HERO_35_Buddy
	events = BeginBar(CONTROLLER).on(BG24_Reward_135_Action())
	pass




if BG24_Reward_Tiny_Henchmen:# ### OK ###
	BG24_Reward+=['BG24_Reward_136']
	BG24_Reward+=['BG24_Reward_136e']
	BG24_Reward_Pool+=['BG24_Reward_136']
class BG24_Reward_136_Action(GameAction):
	def do(self, source):
		controller=source.controller
		cards=[card for card in controller.field if card.tech_level<=3]
		if len(cards)>3:
			cards=random.sample(cards, 3)
		for card in cards:
			Buff(card, 'BG24_Reward_136e').trigger(source)
		pass
class BG24_Reward_136:# [2467]=100, [2641]=1, 
	""" Tiny Henchmen
	At the end of your turn, give +2/+2 to 3 friendly minions of Tier 3 or lower. """
	events = OWN_TURN_END.on(BG24_Reward_136_Action())
	pass
# 2/2->3/3 (24.2.2)
BG24_Reward_136e=buff(3,3)# 




if BG24_Reward_Victims_Specter:#### OK ### 
	BG24_Reward+=['BG24_Reward_138']
	BG24_Reward_Pool+=['BG24_Reward_138']
class BG24_Reward_138_Action(GameAction):
	def do(self, source):
		controller=source.controller
		if len(controller.death_log)>0:
			card = controller.death_log[-1]
			Give(controller.deepcopy_original, card.id).trigger(source)
		pass
class BG24_Reward_138:# [2467]=80, [2641]=1, 
	""" Victim's Specter
	 After each combat, get a plain copy of the last friendly minion that died. """
	events = EndBattle(CONTROLLER).on(BG24_Reward_138_Action())
	pass

#if BG24_Reward_A_Good_Time:# #### not in service
#	BG24_Reward+=['BG24_Reward_210']
#	BG24_Reward_Pool+=['BG24_Reward_210']
#class BG24_Reward_210:# [2467]=150, ### not in service
#	""" A Good Time
#	You have unlimited Gold but only 15 second turns. """
#	#
#	pass

#if BG24_Reward_Avatar_of_the_Coin:#  ## not in service
#	BG24_Reward+=['BG24_Reward_211']
#	BG24_Reward_Pool+=['BG24_Reward_211']
#class BG24_Reward_211:# [2467]=51, ### not in service
#	""" Avatar of the Coin
#	Combat is replaced with a coin flip. """
#	#
#	pass

if BG24_Reward_Anima_Bribe:# ### OK ### banned 24.6
	BG24_Reward+=['BG24_Reward_305']
	BG24_Reward+=['BG24_Reward_305e']
	BG24_Reward_Pool+=['BG24_Reward_305']
class BG24_Reward_305:# [2467]=190, [2641]=1, [2649]=80, 
	""" Anima Bribe
	After you sell a minion, give its stats to a minion in Bob's Tavern. """
	events = Sell(CONTROLLER).after(Buff(RANDOM(ENEMY_MINIONS), 'BG24_Reward_305e', atk=ATK(Sell.CARD), max_health=MAX_HEALTH(Sell.CARD)))
	pass
class BG24_Reward_305e:# 
	""" Anima Bribed	Increased stats. """
	pass




if BG24_Reward_Cooked_Book:# ### OK ###
	BG24_Reward+=['BG24_Reward_306']
	BG24_Reward+=['BG24_Reward_306e']
	BG24_Reward_Pool+=['BG24_Reward_306']
def BG24_Reward_306_Action(source):
	source.script_data_num_1 = 1
class BG24_Reward_306_Action(TargetedAction):
	#TARGET=ActionArg()
	CARD=ActionArg()
	def do(self, source, card):
		#controller=target
		Buff(card, 'BG24_Reward_306e', atk=source.script_data_num_1, max_health=source.script_data_num_1).trigger(source)
		source.script_data_num_1 += 1
		pass
class BG24_Reward_306:# [2467]=150, [2641]=1, 
	""" Cooked Book
	After you buy a minion, give it +@/+@ and upgrade this. """
	events = Buy(CONTROLLER).on(BG24_Reward_306_Action(Buy.CARD))
	pass
class BG24_Reward_306e:# 
	""" Cooked 	Increased stats. """
	pass




if BG24_Reward_Teal_Tiger_Sapphire:# ### OK ###　20221112 OK 
	BG24_Reward+=['BG24_Reward_308']
	BG24_Reward+=['BG24_Reward_308e']
	BG24_Reward_Pool+=['BG24_Reward_308']
class BG24_Reward_308_Action(GameAction):
	def do(self, source):
		controller=source.controller
		bartender=controller.opponent
		tavern=bartender.field
		if isinstance(source.script_data_num_1, int)==False:
			source.script_data_num_1=0
		source.script_data_num_1+=1
		amount = source.script_data_num_1
		for card in tavern:
			Buff(card, 'BG24_Reward_308e', atk=amount, max_health=amount).trigger(source)
		pass
class BG24_Reward_308_Action2(GameAction):
	def do(self, source):
		controller=source.controller
		bartender=controller.opponent
		tavern=bartender.field
		source.script_data_num_1=1
		amount=source.script_data_num_1
		for card in tavern:
			for bf in card.buffs:
				if bf.id=='BG24_Reward_308e':
					card.buffs.remove(bf)
			Buff(card, 'BG24_Reward_308e', atk=amount, max_health=amount).trigger(source)
		pass
class BG24_Reward_308:# [2467]=140, [2641]=1, [2644]=60, 
	# ->  [2467]=100, [2641]=1, [2644]=70, (24.2.2) 
	""" Teal Tiger Sapphire
	Minions in Bob's Tavern have +1/+1 for each time it was [Refreshed] this turn. """
	events = [
		Rerole(CONTROLLER).after(BG24_Reward_308_Action()),
		BeginBar(CONTROLLER).on(BG24_Reward_308_Action2())
	]
	pass
class BG24_Reward_308e:
	pass




if BG24_Reward_Devils_in_the_Details:# ### OK ###
	BG24_Reward+=['BG24_Reward_309']
	BG24_Reward+=['BG24_Reward_309e']
	BG24_Reward_Pool+=['BG24_Reward_309']
class BG24_Reward_309_Action(GameAction):
	def do(self, source):
		controller=source.controller
		if len(controller.field)>0:
			if len(controller.opponent.field)>0:
				card = random.choice(controller.opponent.field)
				EatsMinion(controller.field[0],card,1,'BG24_Reward_309e').trigger(source)
			if len(controller.field)>1:
				if len(controller.opponent.field)>0:
					card = random.choice(controller.opponent.field)
					EatsMinion(controller.field[-1],card,1,'BG24_Reward_309e').trigger(source)
class BG24_Reward_309:# [2467]=110, [2641]=1, 
	""" Devils in the Details
	At the end of your turn, Your left and right-most minions consume a minion in Bob's Tavern. """
	events = OWN_TURN_END.on(BG24_Reward_309_Action())
	pass
class BG24_Reward_309e:# 
	""" Satisfied. For Now...Consumed the stats of minion. """
	pass

#if BG24_Reward_Partner_in_Crime:# not in service
#	BG24_Reward+=['BG24_Reward_310']
#	BG24_Reward_Pool+=['BG24_Reward_310']
#class BG24_Reward_310:# [2467]=100, [2653]=10000, ### not in service
#	""" Partner in Crime
#	Get your Golden Buddy. """
#	#
#	pass

if BG24_Reward_Another_Hidden_Body:# banned 24.2.1
	BG24_Reward+=['BG24_Reward_311']
	BG24_Reward_Pool+=['BG24_Reward_311']
class BG24_Reward_311:# [2467]=70, [2581]=1, [2641]=1, 
	""" Another Hidden Body
	[Discover] a minion of your Tavern Tier. <i>(Can be earned endlessly!)</i> """
	pass




if BG24_Reward_Staff_of_Origination:# ### OK ###
	BG24_Reward+=['BG24_Reward_312']
	BG24_Reward+=['BG24_Reward_312e']
	BG24_Reward_Pool+=['BG24_Reward_312']
class BG24_Reward_312:# [1500]=1, [2467]=275, [2641]=1, [2653]=300, [2727]=1, 
	""" Staff of Origination
	[Start of Combat:] Give your minions +12/+12. """
	events = BeginBattle(CONTROLLER).on(Buff(FRIENDLY_MINIONS, 'BG24_Reward_312e'))
	pass
#+15/+15 -> +12/+12 (24.2.2)
BG24_Reward_312e=buff(12,12)# 




if BG24_Reward_Wondrous_Wisdomball:# ### OK ###
	BG24_Reward+=['BG24_Reward_313']
	BG24_Reward+=['BG24_Reward_313e']
	BG24_Reward_Pool+=['BG24_Reward_313']
class BG24_Reward_313_Action(GameAction):
	def do(self, source):
		controller=source.controller
		if random.choice([0,1]):
			choice=random.choice(range(9))
			if choice==0:### OK ###
				#10．酒場のミニオン全てがグレード６ミニオンとなる		
				amount=len(controller.opponent.field)
				for card in reversed(controller.opponent.field):
					card.discard()
				for repeat in range(amount):
					Summon(controller.opponent, RandomBGAdmissible(tech_level=6).evaluate(controller.opponent)).trigger(controller.opponent)
				pass
			elif choice==1:### OK ###
				#１．酒場のミニオン1体がゴールデンとなる
				if len(controller.opponent.field):
					card = random.choice(controller.opponent.field)
					controller.game.BG_morph_gold(card)
				pass
			elif choice==2:
				#２．酒場のミニオン2体が自陣のミニオンとなる
				if len(controller.opponent.field)>=2:
					controller.opponent.field[-1].discard()
					controller.opponent.field[-1].discard()
					if len(controller.field):
						card=random.choice(controller.field)
						Summon(controller.opponent, card.id).trigger(controller.opponent)
						card=random.choice(controller.field)
						Summon(controller.opponent, card.id).trigger(controller.opponent)
				pass
			elif choice==3:### OK ###
				#３．酒場のミニオン全てが自陣で最も多い種族のミニオンとなる
				if len(controller.field):
					races=[card.race for card in controller.field]
					race=collections.Counter(races).most_common()[0][0]
					amount=len(controller.opponent.field)	
					for card in reversed(controller.opponent.field):
						card.discard()
					for repeat in range(amount):
						Summon(controller.opponent, RandomBGAdmissible(race=race)).trigger(controller.opponent)
				pass
			elif choice==4:### OK ###
				#４．酒場のミニオン全てが自陣のミラーとなる#
				if len(controller.field):	
					for card in reversed(controller.opponent.field):
						card.discard()
					for card in controller.field:
						Summon(controller.opponent, card.id).trigger(controller.opponent)
				pass
			elif choice==5:### OK ###
				#５．酒場のミニオン全てが同じミニオンとなる
				minion_id=controller.opponent.field[0].id
				for card in reversed(controller.opponent.field):
					card.discard()
				for repeat in range(7):
					Summon(controller.opponent, minion_id).trigger(controller.opponent)
				pass
			elif choice==6:### OK ###
				#６．酒場のミニオン全てが厳選中立ミニオン(ザップ、バロン、献身、トンネル爆破、ブラン、15/15/、taunt)となる
				amount=len(controller.opponent.field)
				cards=['BGS_022','BG_FP1_031','BG_OG_221','BG_DAL_775','BG_LOE_077','BG23_190','BG_AT_069']
				for card in reversed(controller.opponent.field):
					card.discard()
				for repeat in range(amount):
					Summon(controller.opponent, random.choice(cards)).trigger(controller.opponent)
				pass
			#elif choice==7:
			#	#７．酒場のミニオン全てがレジェンドミニオンとなる
			#	pass
			elif choice==7:### OK ###
				#８．酒場のミニオン全てに聖なる盾を付与する
				for card in controller.opponent.field:
					SetDivineShield(card, True).trigger(source)
				pass
			elif choice==8:### OK ###
				#９．酒場のミニオン全てに酒場のグレードと同じだけ+X/+X付与する
				amount = controller.tavern_tier
				for card in controller.opponent.field:
					Buff(card, 'BG24_Reward_313e', atk=amount, max_health=amount).trigger(source)
				pass
		pass
class BG24_Reward_313:# [2467]=160, [2641]=1, [2653]=300, 
	""" Wondrous Wisdomball
	Occasionally gives helpful [Refreshes]. """
	events = Rerole(CONTROLLER).after(BG24_Reward_313_Action())
	pass
class BG24_Reward_313e:# 
	""" Wisdom and Wonder
	Increased stats. """
	#
	pass

#if BG24_Reward_To_The_Moon_Almost:# not in service
#	BG24_Reward+=['BG24_Reward_320']
#	BG24_Reward_Pool+=['BG24_Reward_320']
#class BG24_Reward_320:# [2467]=130, ### not in service
#	""" To The Moon... Almost
#	Skip to Tavern Tier 5. You can't upgrade to Tavern Tier 6. """
#	#
#	pass

if BG24_Reward_Alter_Ego:# ### OK ###
	BG24_Reward+=['BG24_Reward_321']
	BG24_Reward+=['BG24_Reward_321t']
	BG24_Reward+=['BG24_Reward_321e']
	BG24_Reward_Pool+=['BG24_Reward_321']
class BG24_Reward_321_Action0(TargetedAction):
	TARGET=ActionArg()
	CARDID=ActionArg()
	def do(self, source, target, cardid):
		controller=target
		newcard=Give(controller, cardid).trigger(source)
		if newcard[0]!=[]:
			newcard=newcard[0][0]
			CastSecret(newcard).trigger(source)
		source.destroy()
		pass
class BG24_Reward_321_Action1(TargetedAction):
	TARGET=ActionArg()
	AMOUNT=IntArg()
	BUFF=ActionArg()
	def do(self, source, target, amount, buff):
		if target.game.this_is_tavern:
			for card in target.opponent.field:
				if card.type==CardType.MINION and card.tech_level%2==amount:
					Buff(card, buff).trigger(source)
		pass
class BG24_Reward_321:# [2467]=120, [2641]=1, 
	""" Alter Ego
	Even Tier minions in Bob's Tavern have +6/+6. <i>(Swaps to Odd next turn!)</i> """
	events = [
		BeginBar(CONTROLLER).on(BG24_Reward_321_Action1(CONTROLLER,1,'BG24_Reward_321e')),
		Rerole(CONTROLLER).on(BG24_Reward_321_Action1(CONTROLLER,1,'BG24_Reward_321e')),
		OWN_TURN_END.on(BG24_Reward_321_Action0(CONTROLLER,'BG24_Reward_321t'))
	]
	pass
## +6/+6 -> +7/+7 (24.2.2)
BG24_Reward_321e=buff(7,7)# 
class BG24_Reward_321t:# 
	""" Alter Ego
	Odd Tier minions in Bob's Tavern have +6/+6. <i>(Swaps to Even next turn!)</i> """
	events = [
		BeginBar(CONTROLLER).on(BG24_Reward_321_Action1(CONTROLLER,0,'BG24_Reward_321e')),
		Rerole(CONTROLLER).on(BG24_Reward_321_Action1(CONTROLLER,0,'BG24_Reward_321e')),
		OWN_TURN_END.on(BG24_Reward_321_Action0(CONTROLLER,'BG24_Reward_321'))
	]
	pass



#if BG24_Reward_9_Lives:# ### not in service
#	BG24_Reward+=['BG24_Reward_323']
#	BG24_Reward_Pool+=['BG24_Reward_323']
#class BG24_Reward_323:# [2467]=99, 
#	""" 9 Lives
#	Set your Health to 1. Add 8 'Iceblocks' to your hand. """
#	#
#	pass

if BG24_Reward_Menagerie_Mayhem:# 
	BG24_Reward+=['BG24_Reward_331']
	BG24_Reward+=['BG24_Reward_331e']
	BG24_Reward_Pool+=['BG24_Reward_331']
class BG24_Reward_331_Action(GameAction):
	def do(self, source):
		controller=source.controller
		targets=[]
		for race in random_picker.BG_races:
			if race!=Race.INVALID:
				cards = [card for card in controller.field if card.race==race]
				if len(cards)>0:
					targets.append(random.choice(cards))
		for card in targets:
			Buff(card, 'BG24_Reward_331e').trigger(source)
		pass
class BG24_Reward_331:# [2467]=150, [2641]=1, 
	""" Menagerie Mayhem
	At the end of your turn, give your minions +1 Attack for each friendly minion type. """
	events = OWN_TURN_END.on(BG24_Reward_331_Action())
	pass
BG24_Reward_331e=buff(1,0)


if BG24_Reward_Pilfered_Lamps:# ### OK ####
	BG24_Reward+=['BG24_Reward_350']
	BG24_Reward_Pool+=['BG24_Reward_350']
class BG24_Reward_350:# [2467]=250, [2641]=1, [2653]=300, 
	""" Pilfered Lamps
	You only need 2 copies of a minion to make it Golden. """
	# See BG_bar.py
	pass

#if BG24_Reward_Totemic_Tavern:# XXXX### not in service
#	BG24_Reward+=['BG24_Reward_351']
#	BG24_Reward_Pool+=['BG24_Reward_351']
#class BG24_Reward_351:# [2467]=30, 
#	""" Totemic Tavern
#	The Totem minion type is added to Bob's Tavern. """
#	#
#	pass

#if BG24_Reward_Purified_Shard:# ?????### not in service
#	BG24_Reward+=['BG24_Reward_352']
#	BG24_Reward_Pool+=['BG24_Reward_352']
#class BG24_Reward_352:# [2467]=999, 
#	""" Purified Shard
#	Win the game. """
#	#
#	pass

#if BG24_Reward_Un_Murloc_Your_Potential:#??### not in service
#	BG24_Reward+=['BG24_Reward_535']
#	BG24_Reward_Pool+=['BG24_Reward_535']
#class BG24_Reward_535:# [2467]=80, 
#	""" Un-Murloc Your Potential
#	Transform your hero into a Murloc. """
#	#
#	pass


if BG24_Reward_Hidden_Treasure_Vault:### OK ###
	BG24_Reward+=['BG24_Reward_361']
	BG24_Reward_Pool+=['BG24_Reward_361']
class BG24_Reward_361_Action(GameAction):
	def do(self, source):
		controller=source.controller
		amount = source.script_data_num_1
		for repeat in range(amount):
			Give(controller, 'GAME_005').trigger(source)
		source.script_data_num_1 += 1
		pass
class BG24_Reward_361:# , 
	"""Hidden Treasure Vault(BG24_Reward_361)
	At the start of your turn, gain @ Gold. &lt;i&gt;(Upgrades each turn!)&lt;/i&gt;"""
	#<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="1"/>
	events = [
		BeginBar(CONTROLLER).on(BG24_Reward_361_Action())
		]
	pass




if BG24_Reward_Essence_of_Zerus:### OK ###
	BG24_Reward+=['BG24_Reward_362']
	BG24_Reward_Pool+=['BG24_Reward_362']
class BG24_Reward_362:# , 
	"""Essence of Zerus BG24_Reward_362 
	At the end of your turn, get a 'Shifter Zerus' which transforms into random minions."""
	events = OWN_TURN_END.on(Give(CONTROLLER, 'BGS_029'))
	pass




if BG24_Reward_Ethereal_Evidence:### OK ###
	BG24_Reward+=['BG24_Reward_363','BG24_Reward_363e']
	BG24_Reward_Pool+=['BG24_Reward_363']
class BG24_Reward_363_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		Buff(card, 'BG24_Reward_363e').trigger(self.player)
		card.zone=Zone.HAND
		CastSecret(card).trigger(self.player)
		if getattr(self.source, 'this_is_enchantment', False):
			self.source.owner.discard()
		elif getattr(self.source, 'this_is_questreward', False):
			self.source.discard()
		else:
			self.source.discard()
		pass
class BG24_Reward_363_Action(GameAction):
	def do(self, source):
		if len(BG24_Reward_Pool)>=2:
			cards=random.sample(BG24_Reward_Pool, 2)
			BG24_Reward_363_Choice(source.controller, RandomID(*cards)*2).trigger(source)
		pass
class BG24_Reward_363:# , 
	"""Ethereal Evidence(BG24_Reward_363)
	At the start of every turn, choose from 2 new Rewards."""
	events = BeginBar(CONTROLLER).on(BG24_Reward_363_Action())
	pass
class BG24_Reward_363e:
	events = BeginBar(CONTROLLER).on(BG24_Reward_363_Action())
	pass




if BG24_Reward_Volatile_Venom:### OK ###
	BG24_Reward+=['BG24_Reward_364', 'BG24_Reward_364e']
	BG24_Reward_Pool+=['BG24_Reward_364']
class BG24_Reward_364:# 
	"""Volatile Venom(BG24_Reward_364)
	Your minions have +8/+8. After they attack, they die. Horribly."""
	events = BeginBattle(CONTROLLER).on(Buff(FRIENDLY_MINIONS, 'BG24_Reward_364e'))
	pass
class BG24_Reward_364e:
	""" Volatile """
	#tags = {GameTag.ATK:8, GameTag.HEALTH:8, }
	tags = {GameTag.ATK:7, GameTag.HEALTH:7, } ## 24.6.2
	events = Attack(OWNER, ENEMY).after(Destroy(OWNER))
	pass



if BG24_Reward_Blood_Goblet:### OK ###
	BG24_Reward+=['BG24_Reward_708','BG24_Reward_708_e']
	BG24_Reward_Pool+=['BG24_Reward_708']
class BG24_Reward_708_Action(GameAction):
	def do(self, source):
		controller=source.controller
		if len(controller.field):
			amount=controller.hero.damage
			card=controller.field[-1]
			Buff(card, 'BG24_Reward_708_e', atk=amount).trigger(source)
		pass
class BG24_Reward_708:# , 
	"""Blood Goblet BG24_Reward_708 
	At the end of your turn, give your right-most minion Attack equal to your missing Health."""
	events = OWN_TURN_END.on(BG24_Reward_708_Action())
	pass
class BG24_Reward_708_e:
	""" """
	pass


#
if BG24_Reward_Sinfall_Medallion:### OK ###
	BG24_Reward+=['BG24_Reward_712','BG24_Reward_712e']
	BG24_Reward_Pool+=['BG24_Reward_712']
class BG24_Reward_712_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller=source.controller
		cards = [card for card in controller.field if card.type==CardType.MINION and card != target and card.tech_level==target.tech_level]
		if len(cards):
			if len(cards)>2:
				cards=random.sample(cards, 2)
			for card in cards:
				Buff(card, 'BG24_Reward_712e').trigger(source)
		pass
class BG24_Reward_712:# , 
	"""Sinfall Medallion(BG24_Reward_712)
	After you play a minion, give 2 other friendly minions of its Tavern Tier +2/+2."""
	events = BG_Play(CONTROLLER, MINION).after(BG24_Reward_712_Action(BG_Play.CARD))
	pass
BG24_Reward_712e=buff(2,2)


if BG24_Enhance_a_matic:
	BG24_Reward+=['BG24_Reward_715','BG24_Reward_715e','BG24_Reward_715e2','BG24_Reward_715e3','BG24_Reward_715e4','BG24_Reward_715t','BG24_Reward_715t2','BG24_Reward_715t3','BG24_Reward_715t4']
	BG24_Reward_Pool+=['BG24_Reward_715']
class BG24_Reward_715_Action(GameAction):
	def do(self, source):
		card = random.choice(['BG24_Reward_715t','BG24_Reward_715t2','BG24_Reward_715t3','BG24_Reward_715t4'])
		Give(CONTROLLER, card).trigger(source)
class BG24_Reward_715:#
	""" >Enhance-a-matic
	At the start of your turn, get an Enhanced Part that gives +5/+5 and a random bonus."""
	events = BeginBar(CONTROLLER).on(BG24_Reward_715_Action())
	pass
class BG24_Reward_715t:
	""" Mega Horn
	Give a minion +5/+5 and [Taunt]. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }	
	play=Buff(TARGET, 'BG24_Reward_715e')
BG24_Reward_715e=buff(5, 5, taunt=True)
class BG24_Reward_715t2:
	""" Blazing Blades
	Give a minion +5/+5 and [Windfury]."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }	
	play=Buff(TARGET, 'BG24_Reward_715e2')
class BG24_Reward_715e2:
	def apply(self, target):
		target.windfury=1
	tags={GameTag.ATK:5, GameTag.HEALTH:5, } 
class BG24_Reward_715t3:
	""" Bunker Plating
	Give a minion +5/+5 and [Divine Shield]. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }	
	play=Buff(TARGET, 'BG24_Reward_715e3')
class BG24_Reward_715e3:
	tags={GameTag.ATK:5, GameTag.HEALTH:5, GameTag.DIVINE_SHIELD:1 } 
class BG24_Reward_715t4:
	""" BG24_Reward_715t4
	Give a minion +5/+5 and [Reborn]. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }	
	play=Buff(TARGET, 'BG24_Reward_715e4')
BG24_Reward_715e4=buff(5, 5, reborn=True)




#
if BG24_Reward_Kidnap_Sack:### OK ###
	BG24_Reward+=['BG24_Reward_718','BG24_Reward_718t']
	BG24_Reward_Pool+=['BG24_Reward_718']
class BG24_Reward_718:# , 
	"""Kidnap Sack(BG24_Reward_718)
	[Spellcraft:] Choose a non-golden minion. Add it to your hand."""
	play = Spellcraft(CONTROLLER,'BG24_Reward_718t')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG24_Reward_718t'))
	tags={2359:'BG24_Reward_718t'}	
	pass
class BG24_Reward_718t_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		target.zone=Zone.HAND
		pass
class BG24_Reward_718t:## spell craft card
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, 1003:0,}
	## 1003:# REQ_NONGOLDEN_TARGET# 
	play = BG24_Reward_718t_Action(TARGET)
	class Hand:
		events = EndTurn(CONTROLLER).on(Destroy(SELF))




if BG24_Reward_The_Golden_Hammer:### OK #####
	BG24_Reward+=['BG24_Reward_719','BG24_Reward_719t','BG24_Reward_719te']
	BG24_Reward_Pool+=['BG24_Reward_719']
class BG24_Reward_719:# , 
	"""The Golden Hammer(BG24_Reward_719)
	[Spellcraft:] Make a friendly minion Golden until next turn."""
	play = Spellcraft(CONTROLLER,'BG24_Reward_719t')
	events = BeginBar(CONTROLLER).on(Spellcraft(CONTROLLER,'BG24_Reward_719t'))
	tags={2359:'BG24_Reward_719t'}		
	pass
class BG24_Reward_719t_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		assert target.controller.game.this_is_tavern, "bar"
		gold_id=target.controller.game.parent.BG_Gold[target.id]
		newcard=target.controller.card(gold_id)
		newcard.zone=Zone.PLAY
		Buff(newcard, 'BG24_Reward_719te').trigger(source)
		target.discard()
		pass
class BG24_Reward_719t:
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0, 1003:0,}	
	play = BG24_Reward_719t_Action(TARGET)
	class Hand:
		events = EndTurn(CONTROLLER).on(Destroy(SELF))
class BG24_Reward_719te_Action(GameAction):
	def do(self, source):
		player=source.controller
		target=source.owner
		cards = [cardId for cardId in player.game.parent.BG_Gold.keys() if player.game.parent.BG_Gold[cardId]==target.id]
		if len(cards):
			newcard=player.card(cards[0])
			newcard.zone=Zone.PLAY
		target.discard()
		Destroy_spellcraft(source)
		pass
class BG24_Reward_719te:
	events = BeginBar(CONTROLLER).on(BG24_Reward_719te_Action())

