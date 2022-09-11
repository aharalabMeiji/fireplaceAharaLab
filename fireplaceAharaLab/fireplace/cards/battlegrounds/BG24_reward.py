from ..utils import *

BG24_Reward=[]

BG24_Reward_Snicker_Snacks=True
BG24_Reward_Stolen_Gold=True
BG24_Reward_Evil_Twin=True
BG24_Reward_Ritual_Dagger=True
BG24_Reward_Theotars_Parasol=True
BG24_Reward_Exquisite_Conch=True
BG24_Reward_The_Smoking_Gun=True
BG24_Reward_Mirror_Shield=True
BG24_Reward_Secret_Sinstone=True
BG24_Reward_Ghastly_Mask=True
BG24_Reward_Red_Hand=True
BG24_Reward_The_Friends_Along_the_Way=True
BG24_Reward_Yogg_tastic_Tasties=True
BG24_Reward_Tiny_Henchmen=True
BG24_Reward_Victims_Specter=True
BG24_Reward_A_Good_Time=True
BG24_Reward_Avatar_of_the_Coin=True
BG24_Reward_Anima_Bribe=True
BG24_Reward_Cooked_Book=True
BG24_Reward_Teal_Tiger_Sapphire=True
BG24_Reward_Devils_in_the_Details=True
BG24_Reward_Partner_in_Crime=True
BG24_Reward_Another_Hidden_Body=False## banned 24.2.1
BG24_Reward_Staff_of_Origination=True
BG24_Reward_Wondrous_Wisdomball=True
BG24_Reward_To_The_Moon_Almost=True
BG24_Reward_Alter_Ego=True
BG24_Reward_9_Lives=True
BG24_Reward_Menagerie_Mayhem=True
BG24_Reward_Pilfered_Lamps=True
BG24_Reward_Totemic_Tavern=True
BG24_Reward_Purified_Shard=True
BG24_Reward_Un_Murloc_Your_Potential=True


if BG24_Reward_Snicker_Snacks:# 
	BG24_Reward+=['BG24_Reward_107']
class BG24_Reward_107_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		controller = target
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
	events = OWN_TURN_END.on(BG24_Reward_107_Action(CONTROLLER))
	#<Tag enumID="201" name="FACTION" type="Int" value="3"/>
	pass

if BG24_Reward_Stolen_Gold:# 
	BG24_Reward+=['BG24_Reward_109']
class BG24_Reward_109:# [1500]=1, [2467]=80, [2641]=1, [2643]=90, [2646]=90, [2727]=1,
	# [1500]=1, [2467]=140, [2641]=1, [2643]=90, [2645]=90, [2646]=90, [2727]=1,(24.2.2 harder)
	""" Stolen Gold
	[Start of Combat:] Make your left and right- most minions Golden. """
	#
	pass

if BG24_Reward_Evil_Twin:# 
	BG24_Reward+=['BG24_Reward_111']
class BG24_Reward_111:# [1500]=1, [2467]=150, [2641]=1, [2647]=120, [2727]=1, 
	""" Evil Twin
	[Start of Combat:] Summon a copy of your highest-Health minion. """
	#
	pass

if BG24_Reward_Ritual_Dagger:# 
	BG24_Reward+=['BG24_Reward_113']
class BG24_Reward_113:# [2467]=80, [2641]=1, 
	""" Ritual Dagger
	After a friendly [Deathrattle] minion dies, give it +4/+4 permanently. """
	#
	pass

	BG24_Reward+=['BG24_Reward_113_ALT']
class BG24_Reward_113_ALT:# [2467]=70, [2643]=90, [2646]=90, 
	""" Ritual Dagger
	Your first [Deathrattle] each combat triggers an extra time. """
	#
	pass

	BG24_Reward+=['BG24_Reward_113e']
class BG24_Reward_113e:# [1927]=1, 
	""" "Noble" Sacrifice
	+4/+4 """
	#
	pass

if BG24_Reward_Theotars_Parasol:# 
	BG24_Reward+=['BG24_Reward_115']
class BG24_Reward_115:# [2467]=70, [2641]=1, 
	""" Theotar's Parasol
	At the end of your turn, give your right-most minion [Stealth] until next turn and +8 Health. """
	#
	pass

	BG24_Reward+=['BG24_Reward_115e']
class BG24_Reward_115e:# 
	""" Shaded
	+8 Health. """
	#
	pass

	BG24_Reward+=['BG24_Reward_115e2']
class BG24_Reward_115e2:# [2594]=1, 
	""" Shady
	[Stealth] until next turn. """
	#
	pass

if BG24_Reward_Exquisite_Conch:# 
	BG24_Reward+=['BG24_Reward_123']
class BG24_Reward_123:# [2467]=80, [2647]=50, 
	""" Exquisite Conch
	Your first [Battlecry] each turn triggers 2 extra times. """
	#
	pass

if BG24_Reward_The_Smoking_Gun:# 
	BG24_Reward+=['BG24_Reward_125']
	BG24_Reward+=['BG24_Reward_125e']
class BG24_Reward_125:# [2467]=110, [2641]=1, [2643]=70, [2646]=80, 
	# [2467]=150, [2641]=1, [2643]=70, [2646]=80, (harder to obtain it)
	""" The Smoking Gun
	Your minions have +5 Attack. """
	#
	pass

class BG24_Reward_125e:# 
	""" Armed and Still Smoking
	+5 Attack. """
	#
	pass

if BG24_Reward_Mirror_Shield:# 
	BG24_Reward+=['BG24_Reward_128']
class BG24_Reward_128:# [2467]=75, [2641]=1, 
	# [2467]=130, [2641]=1, [2647]=85 (harder to obatain it)
	""" Mirror Shield
	After each [Refresh], give a minion in Bob's Tavern +4/+4 and [Divine Shield]. """
	#
	pass

	BG24_Reward+=['BG24_Reward_128e']
class BG24_Reward_128e:# 
	""" Mirror Shield
	+4/+4 and [Divine Shield]. """
	#
	pass

if BG24_Reward_Secret_Sinstone:# 
	BG24_Reward+=['BG24_Reward_129']
class BG24_Reward_129:# [2467]=130, [2641]=1, 
	""" Secret Sinstone
	After you [Discover] a card, get an extra copy of it. """
	#
	pass

if BG24_Reward_Ghastly_Mask:# 
	BG24_Reward+=['BG24_Reward_130']
class BG24_Reward_130:# [2467]=230, [2641]=1, [2673]=59707, [2677]=1, 
	""" Ghastly Mask
	Add '{0}' to your hand. Your end of turn effects trigger twice. """
	#
	pass

if BG24_Reward_Red_Hand:# 
	BG24_Reward+=['BG24_Reward_131']
class BG24_Reward_131:# [2467]=110, [2641]=1
	# -> [2467]=90, [2641]=1 (24.2.2, easier to obtain)
	""" Red Hand
	At the start of your turn, give a minion in your hand +12/+12. """
	#
	pass

	BG24_Reward+=['BG24_Reward_131e']
class BG24_Reward_131e:# 
	""" Caught Red Handed
	+12/+12 """
	#
	pass

if BG24_Reward_The_Friends_Along_the_Way:# 
	BG24_Reward+=['BG24_Reward_134']
class BG24_Reward_134:# [2467]=140, [2571]=1, [2641]=1, 
	""" The Friends Along the Way
	At the start of your turn, get 2 random {0}. """
	#
	pass

if BG24_Reward_Yogg_tastic_Tasties:# 
	BG24_Reward+=['BG24_Reward_135']
class BG24_Reward_135:# [2467]=150, [2641]=1, [2653]=300, 
	""" Yogg-tastic Tasties
	At the start of your turn, spin the Wheel of Yogg-Saron. """
	#
	pass

if BG24_Reward_Tiny_Henchmen:# 
	BG24_Reward+=['BG24_Reward_136']
class BG24_Reward_136:# [2467]=100, [2641]=1, 
	""" Tiny Henchmen
	At the end of your turn, give +2/+2 to 3 friendly minions of Tier 3 or lower. """
	#
	pass

	BG24_Reward+=['BG24_Reward_136e']
	# 2/2->3/3 (24.2.2)
BG24_Reward_136e=buff(3,3)# 

if BG24_Reward_Victims_Specter:# 
	BG24_Reward+=['BG24_Reward_138']
class BG24_Reward_138:# [2467]=80, [2641]=1, 
	""" Victim's Specter
	 After each combat, get a plain copy of the last friendly minion that died. """
	#
	pass

if BG24_Reward_A_Good_Time:# 
	BG24_Reward+=['BG24_Reward_210']
class BG24_Reward_210:# [2467]=150, 
	""" A Good Time
	You have unlimited Gold but only 15 second turns. """
	#
	pass

if BG24_Reward_Avatar_of_the_Coin:# 
	BG24_Reward+=['BG24_Reward_211']
class BG24_Reward_211:# [2467]=51, 
	""" Avatar of the Coin
	Combat is replaced with a coin flip. """
	#
	pass

if BG24_Reward_Anima_Bribe:# 
	BG24_Reward+=['BG24_Reward_305']
class BG24_Reward_305:# [2467]=190, [2641]=1, [2649]=80, 
	""" Anima Bribe
	After you sell a minion, give its stats to a minion in Bob's Tavern. """
	#
	pass

	BG24_Reward+=['BG24_Reward_305e']
class BG24_Reward_305e:# 
	""" Anima Bribed
	Increased stats. """
	#
	pass

if BG24_Reward_Cooked_Book:# 
	BG24_Reward+=['BG24_Reward_306']
class BG24_Reward_306:# [2467]=150, [2641]=1, 
	""" Cooked Book
	After you buy a minion, give it +@/+@ and upgrade this. """
	#
	pass

	BG24_Reward+=['BG24_Reward_306e']
class BG24_Reward_306e:# 
	""" Cooked
	Increased stats. """
	#
	pass

if BG24_Reward_Teal_Tiger_Sapphire:# 
	BG24_Reward+=['BG24_Reward_308']
class BG24_Reward_308:# [2467]=140, [2641]=1, [2644]=60, 
	# ->  [2467]=100, [2641]=1, [2644]=70, (24.2.2) 
	""" Teal Tiger Sapphire
	Minions in Bob's Tavern have +1/+1 for each time it was [Refreshed] this turn. """
	#
	pass

	BG24_Reward+=['BG24_Reward_308e']
class BG24_Reward_308e:# 
	""" Tiger Spirit
	Increased stats. """
	#
	pass

if BG24_Reward_Devils_in_the_Details:# 
	BG24_Reward+=['BG24_Reward_309']
class BG24_Reward_309:# [2467]=110, [2641]=1, 
	""" Devils in the Details
	At the end of your turn, Your left and right-most minions consume a minion in Bob's Tavern. """
	#
	pass

	BG24_Reward+=['BG24_Reward_309e']
class BG24_Reward_309e:# 
	""" Satisfied. For Now...
	Consumed the stats of minion. """
	#
	pass

if BG24_Reward_Partner_in_Crime:# 
	BG24_Reward+=['BG24_Reward_310']
class BG24_Reward_310:# [2467]=100, [2653]=10000, 
	""" Partner in Crime
	Get your Golden Buddy. """
	#
	pass

if BG24_Reward_Another_Hidden_Body:# banned 24.2.1
	BG24_Reward+=['BG24_Reward_311']
class BG24_Reward_311:# [2467]=70, [2581]=1, [2641]=1, 
	""" Another Hidden Body
	[Discover] a minion of your Tavern Tier. <i>(Can be earned endlessly!)</i> """
	#
	pass

if BG24_Reward_Staff_of_Origination:# 
	BG24_Reward+=['BG24_Reward_312']
class BG24_Reward_312:# [1500]=1, [2467]=275, [2641]=1, [2653]=300, [2727]=1, 
	""" Staff of Origination
	[Start of Combat:] Give your minions +15/+15. """
	#
	pass

	BG24_Reward+=['BG24_Reward_312e']
#+15/+15 -> +12/+12 (24.2.2)
BG24_Reward_312e=buff(12,12)# 

if BG24_Reward_Wondrous_Wisdomball:# 
	BG24_Reward+=['BG24_Reward_313']
class BG24_Reward_313:# [2467]=160, [2641]=1, [2653]=300, 
	""" Wondrous Wisdomball
	Occasionally gives helpful [Refreshes]. """
	#
	pass

	BG24_Reward+=['BG24_Reward_313e']
class BG24_Reward_313e:# 
	""" Wisdom and Wonder
	Increased stats. """
	#
	pass

if BG24_Reward_To_The_Moon_Almost:# 
	BG24_Reward+=['BG24_Reward_320']
class BG24_Reward_320:# [2467]=130, 
	""" To The Moon... Almost
	Skip to Tavern Tier 5. You can't upgrade to Tavern Tier 6. """
	#
	pass

if BG24_Reward_Alter_Ego:# 
	BG24_Reward+=['BG24_Reward_321']
class BG24_Reward_321:# [2467]=120, [2641]=1, 
	""" Alter Ego
	Even Tier minions in Bob's Tavern have +6/+6. <i>(Swaps to Odd next turn!)</i> """
	#
	pass

	BG24_Reward+=['BG24_Reward_321e']
## +6/+6 -> +7/+7 (24.2.2)
BG24_Reward_321e=buff(7,7)# 

	BG24_Reward+=['BG24_Reward_321t']
class BG24_Reward_321t:# 
	""" Alter Ego
	Odd Tier minions in Bob's Tavern have +6/+6. <i>(Swaps to Even next turn!)</i> """
	#
	pass

if BG24_Reward_9_Lives:# 
	BG24_Reward+=['BG24_Reward_323']
class BG24_Reward_323:# [2467]=99, 
	""" 9 Lives
	Set your Health to 1. Add 8 'Iceblocks' to your hand. """
	#
	pass

if BG24_Reward_Menagerie_Mayhem:# 
	BG24_Reward+=['BG24_Reward_331']
class BG24_Reward_331:# [2467]=150, [2641]=1, 
	""" Menagerie Mayhem
	At the end of your turn, give your minions +1 Attack for each friendly minion type. """
	#
	pass

	BG24_Reward+=['BG24_Reward_331e']
class BG24_Reward_331e:# 
	""" Mischievous Mayhem
	Increased Attack. """
	#
	pass

if BG24_Reward_Pilfered_Lamps:# 
	BG24_Reward+=['BG24_Reward_350']
class BG24_Reward_350:# [2467]=250, [2641]=1, [2653]=300, 
	""" Pilfered Lamps
	You only need 2 copies of a minion to make it Golden. """
	#
	pass

if BG24_Reward_Totemic_Tavern:# 
	BG24_Reward+=['BG24_Reward_351']
class BG24_Reward_351:# [2467]=30, 
	""" Totemic Tavern
	The Totem minion type is added to Bob's Tavern. """
	#
	pass

if BG24_Reward_Purified_Shard:# 
	BG24_Reward+=['BG24_Reward_352']
class BG24_Reward_352:# [2467]=999, 
	""" Purified Shard
	Win the game. """
	#
	pass

if BG24_Reward_Un_Murloc_Your_Potential:# 
	BG24_Reward+=['BG24_Reward_535']
class BG24_Reward_535:# [2467]=80, 
	""" Un-Murloc Your Potential
	Transform your hero into a Murloc. """
	#
	pass

