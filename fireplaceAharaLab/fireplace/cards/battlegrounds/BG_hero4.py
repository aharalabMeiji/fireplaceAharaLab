from ..utils import *

BG_Hero4=[
#Rakanishu
#Reno Jackson
'BG20_HERO_100','BG20_HERO_100p','BG20_HERO_100p_e2','BG20_HERO_100_Buddy','BG20_HERO_100_Buddy_e','BG20_HERO_100_Buddy_G','BG20_HERO_100_Buddy_Ge',
#Rokara
#Scabbs Cutterbutter
#Shudderwock
#Silas Darkmoon
#Sindragosa
#Sir Finley Mrrgglton
#Skycap'n Kragg
#Sneed
#Tamsin Roame
#BG22_HERO_000#Tavish Stormpike
#Tess Greymane
#The Curator
#The Great Akazamzarak
#The Lich King
#The Rat King
#Tickatus
#Trade Prince Gallywix
#BG22_HERO_003#Vanndar Stormpike
#BG22_HERO_004#Varden Dawngrasp
'BG20_HERO_201','BG20_HERO_201e','BG20_HERO_201e2','BG20_HERO_201e3','BG20_HERO_201p','BG20_HERO_201p2','BG20_HERO_201p2e','BG20_HERO_201p3e','BG20_HERO_201_Buddy','BG20_HERO_201_Buddy_e','BG20_HERO_201_Buddy_e2','BG20_HERO_201_Buddy_G',
#Vol'jin
'BG20_HERO_101','BG20_HERO_101p','BG20_HERO_101pe2','BG20_HERO_101_Buddy','BG20_HERO_101_Buddy_e','BG20_HERO_101_Buddy_G','BG20_HERO_101_Buddy_Ge',
#Xyrella
#Y'Shaarj
#Yogg-Saron, Hope's End
#Ysera
#Zephrys, the Great
]
######## source #################################################################

#Rakanishu # armor 5

#Reno Jackson # armor 6

#Rokara # armor 5
class BG20_HERO_100:# <10>[1453]
	""" Rokara
	 """
	pass
class BG20_HERO_100p:# <10>[1453]
	""" Glory of Combat
	&lt;b&gt;Passive.&lt;/b&gt; After a friendly minion kills an enemy, give it +1 Attack permanently. """
	events =  Attack(FRIENDLY_MINIONS, ENEMY_CHARACTERS).on(Buff(Attack.ATTACKER, 'BG20_HERO_100p_e2'))
	pass
BG20_HERO_100p_e2=buff(1,0)
class BG20_HERO_100_Buddy:# <12>[1453]
	""" Icesnarl the Mighty
	After a friendly minionkills an enemy, gain+1 Health permanently. """
	events = Attack(FRIENDLY_MINIONS, ENEMY_CHARACTERS).on(Buff(SELF, 'BG20_HERO_100_Buddy_e'))
	pass
BG20_HERO_100_Buddy_e=buff(0,1)# <12>[1453]
class BG20_HERO_100_Buddy_G:# <12>[1453]
	""" Icesnarl the Mighty
	After a friendly minionkills an enemy, gain+2 Health permanently. """
	events = Attack(FRIENDLY_MINIONS, ENEMY_CHARACTERS).on(Buff(SELF, 'BG20_HERO_100_Buddy_Ge'))
	pass
BG20_HERO_100_Buddy_Ge=buff(0,2)# <12>[1453]


#Scabbs Cutterbutter
#### 010 ####
class BG21_HERO_010:# <7>[1453]
	""" Scabbs Cutterbutter
	 """
	pass
class BG21_HERO_010p:# <7>[1453]
	""" I Spy
	[Discover] a plain copy of a minion from your next opponent's warband. """
	#play = GenericChoice(CONTROLLER, RANDOM(NEXT_OPPONENT) * 3)
	pass
class BG21_HERO_010_Buddy:# <12>[1453]
	""" Warden Thelwater
	At the start of your turn, add your next opponent's Buddy to your hand. """
	#events = OWN_TURN_BEGIN.on(Give(CONTROLLER, ID(NEXT_OPPONENT_BUDDY)))
	pass
class BG21_HERO_010_Buddy_G:# <12>[1453]
	""" Warden Thelwater
	At the start of your turn, add 2 of your next opponent's Buddy to your hand. """
	#events = OWN_TURN_BEGIN.on(Give(CONTROLLER, ID(NEXT_OPPONENT_BUDDY))*2)
	pass

#Shudderwock # armor 3
class TB_BaconShop_HERO_23:# <12>[1453]
	""" Shudderwock
	 """
	#
	pass

class TB_BaconShop_HERO_23_Buddy:# <12>[1453]
	""" Muckslinger
	After you play a minion,add a [Battlecry] minionto Bob's Tavern.Give it +2/+2. """
	#
	pass

class TB_BaconShop_HERO_23_Buddy_e:# <12>[1453]
	""" Mucked Up
	+2/+2. """
	#
	pass

class TB_BaconShop_HERO_23_Buddy_G:# <12>[1453]
	""" Muckslinger
	After you play a minion,add a [Battlecry] minionto Bob's Tavern.Give it +4/+4. """
	#
	pass

class TB_BaconShop_HERO_23_Buddy_Ge:# <12>[1453]
	""" Mucked Up
	+4/+4. """
	#
	pass

class TB_BaconShop_HERO_23_SKIN_A:# <12>[1453]
	""" Gentleman Shudderwock
	 """
	#
	pass


#Silas Darkmoon # # armor 6

#Sindragosa
class TB_BaconShop_HERO_27:# <12>[1453]
	""" Sindragosa
	 """
	#
	pass

class TB_BaconShop_HERO_27_Buddy:# <12>[1453]
	""" Thawed Champion
	At the end of your turn, adda random [Frozen] minionfrom Bob's Tavernto your hand. """
	#
	pass

class TB_BaconShop_HERO_27_Buddy_G:# <12>[1453]
	""" Thawed Champion
	At the end of your turn, add2 random [Frozen] minionsfrom Bob's Tavernto your hand. """
	#
	pass

class TB_BaconShop_HERO_27_SKIN_A:# <12>[1453]
	""" Sindragosa the Blue
	 """
	#
	pass


#Sir Finley Mrrgglton ## armor 3

#Skycap'n Kragg

#Sneed
class BG21_HERO_030:# <10>[1453]
	""" Sneed
	 """
	#
	pass
class BG21_HERO_030p:# <12>[1453]
	""" Sneed's Replicator
	Give a friendly minion:"[Deathrattle]: Summon a random minion of the same Tavern Tier." """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0,}
	play = Buff(TARGET,'BG21_HERO_030pe')
	pass
class BG21_HERO_030pe:# <12>[1453]
	""" Replicate
	[Deathrattle]: Summon a random minion of the same Tavern Tier. """
	pass
class BG21_HERO_030_Buddy:# <12>[1453]
	""" Piloted Whirl-O-Tron
	[Battlecry:] Copy a friendly minion's [Deathrattles]. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0,}
	play = Buff(SELF, 'BG21_HERO_030_Buddy_e') 
	pass
class BG21_HERO_030_Buddy_e:# <12>[1453]
	""" Whirling
	Copied [Deathrattles] from {0}. """
	tags={GameTag.DEATHRATTLE:True}
	deathrattle = Deathrattle(TARGET)
	pass
class BG21_HERO_030_Buddy_G:# <12>[1453]
	""" Piloted Whirl-O-Tron
	[Battlecry:] Copy a friendly minion's [Deathrattles] twice. """
	play = Buff(SELF, 'BG21_HERO_030_Buddy_e') * 2
	pass


#Tamsin Roame
#### 20 282 ####
class BG20_HERO_282:# <9>[1453]
	""" Tamsin Roame
	 """
	#
	pass

class BG20_HERO_282_Buddy:# <12>[1453]
	""" Monstrosity
	After a friendly minion dies, gain its Attack. """
	#
	pass

class BG20_HERO_282_Buddy_G:# <12>[1453]
	""" Monstrosity
	After a friendly minion dies, gain its Attack twice. """
	#
	pass

class BG20_HERO_282_Buddye:# <12>[1453]
	""" Consumed
	Increased Attack. """
	#
	pass

class BG20_HERO_282p:# <9>[1453]
	""" Fragrant Phylactery
	[Start of Combat:]Destroy your lowest Healthminion. Give its stats_to four friendly minions. """
	#
	pass

class BG20_HERO_282pe:# <12>[1453]
	""" Fragrant
	Increased stats. """
	#
	pass

#BG22_HERO_000#Tavish Stormpike
###Tavish Stormpike
class BG22_HERO_000:# <12>[1453]
	""" Tavish Stormpike
	 """
	#
	pass
class BG22_HERO_000p:
	"""
	"""
class BG22_HERO_000_Buddy:# <12>[1453]
	""" Crabby
	After your Hero Power fires,give adjacent minions stats__equal to the damage dealt._ """
	#
	pass

class BG22_HERO_000_Buddy_G:# <12>[1453]
	""" Crabby
	After your Hero Power fires, give adjacent minions stats equal to twice the damage dealt. """
	#
	pass
class BG22_HERO_000:# <12>[1453]
	""" Tavish Stormpike
	 """
	#
	pass

class BG22_HERO_000_Buddy_e:# <12>[1453]
	""" Crabby
	Increased stats. """
	#
	pass

class BG22_HERO_000p:# <12>[1453]
	""" Deadeye
	Take aim![Start of Combat]: Deal@ damage to your target.<i>(Upgrades each turn!)</i> """
	#
	pass

class BG22_HERO_000p_t1:# <12>[1453]
	""" Aim Left!
	[PassiveStart of Combat]: Deal@ damage to the left-most enemy minion. """
	#
	pass

class BG22_HERO_000p_t2:# <12>[1453]
	""" Aim Low!
	[PassiveStart of Combat]: Deal@ damage to the lowestHealth enemy minion. """
	#
	pass

class BG22_HERO_000p_t3:# <12>[1453]
	""" Aim High!
	[PassiveStart of Combat]: Deal@ damage to the highestHealth enemy minion. """
	#
	pass

class BG22_HERO_000p_t4:# <12>[1453]
	""" Aim Right!
	[PassiveStart of Combat]: Deal@ damage to the right-most enemy minion. """
	#
	pass

#Tess Greymane

#The Curator
class TB_BaconShop_HERO_33:# <12>[1453]
	""" The Curator
	 """
	#
	pass

class TB_BaconShop_HERO_33_Buddy_e:# <12>[1453]
	""" Amalfam
	Increased stats. """
	#
	pass

class TB_BaconShop_HERO_33_SKIN_A:# <12>[1453]
	""" Cuddly Curator
	 """
	#
	pass

#The Great Akazamzarak
class TB_BaconShop_HERO_21:# <12>[1453]
	""" The Great Akazamzarak
	 """
	#
	pass

class TB_BaconShop_HERO_21_Buddy:# <12>[1453]
	""" Street Magician
	[Deathrattle:] Put a random [Secret] into the battlefield. """
	#
	pass

class TB_BaconShop_HERO_21_Buddy_G:# <12>[1453]
	""" Street Magician
	[Deathrattle:] Put 2 random[Secrets] into the battlefield. """
	#
	pass

class TB_BaconShop_HERO_21_SKIN_A:# <12>[1453]
	""" Crashin' Thrashin' Akazamzarak
	 """
	#
	pass


#The Lich King
class TB_BaconShop_HERO_22:# <12>[1453]
	""" The Lich King
	 """
	#
	pass

class TB_BaconShop_HERO_22_SKIN_A:# <12>[1453]
	""" Grill King Bolvar
	 """
	#
	pass

class TB_BaconShop_HERO_22_SKIN_B:# <12>[1453]
	""" Invincible Lich King
	 """
	#
	pass

class TB_BaconShop_HERO_22_SKIN_C:# <12>[1453]
	""" Lü Bu Arthas
	 """
	#
	pass


#The Rat King ## armor 6
class TB_BaconShop_HERO_12:# <12>[1453]
	""" The Rat King
	 """
	#
	pass

class TB_BaconShop_HERO_12_Buddy:# <12>[1453]
	""" Pigeon Lord
	Your [Refreshes] cost (0)while Bob's Tavern doesn'thave the minion type ofyour Hero Power. """
	#
	pass

class TB_BaconShop_HERO_12_Buddy_G:# <12>[1453]
	""" Pigeon Lord
	Your [Refreshes] cost (0)while Bob's Tavern doesn'thave the minion type ofyour Hero Power. """
	#
	pass

class TB_BaconShop_HERO_12_SKIN_A:# <12>[1453]
	""" The Martial Rat
	 """
	#
	pass


#Tickatus

#Trade Prince Gallywix
class TB_BaconShop_HERO_10:# <12>[1453]
	""" Trade Prince Gallywix
	 """
	#
	pass

class TB_BaconShop_HERO_10_Buddy:# <12>[1453]
	""" Bilgewater Mogul
	[Battlecry:] Give a minion +1/+1 for each Gold spent this turn. """
	#
	pass

class TB_BaconShop_HERO_10_Buddy_G:# <12>[1453]
	""" Bilgewater Mogul
	[Battlecry:] Give a minion +2/+2 for each Gold spent this turn. """
	#
	pass

class TB_BaconShop_HERO_10_Buddye:# <12>[1453]
	""" Brutal Luxury
	Increased stats. """
	#
	pass

class TB_BaconShop_HERO_10_SKIN_A:# <12>[1453]
	""" Moneyhogger Gallywix
	 """
	#
	pass

class TB_BaconShop_HERO_10_SKIN_B:# <12>[1453]
	""" Dong Zhuo Gallywix
	 """
	#
	pass

#BG22_HERO_003#Vanndar Stormpike
###Vanndar Stormpike
class BG22_HERO_003:# <12>[1453]
	""" Vanndar Stormpike
	 """
	#
	pass
class BG22_HERO_003_Buddy:# <12>[1453]
	""" Stormpike Lieutenant
	[Avenge (2):] Give your minions +1 Health permanently. """
	#
	pass

class BG22_HERO_003_Buddy_G:# <12>[1453]
	""" Stormpike Lieutenant
	[Avenge (2):] Give your minions +2 Health permanently. """
	#
	pass
class BG22_HERO_003:# <12>[1453]
	""" Vanndar Stormpike
	 """
	#
	pass

class BG22_HERO_003_Buddy:# <12>[1453]
	""" Stormpike Lieutenant
	[Avenge (2):] Give your minions +1 Health permanently. """
	#
	pass

class BG22_HERO_003_Buddy_e:# <12>[1453]
	""" Lieutenant's Leadership
	+1 Health. """
	#
	pass

class BG22_HERO_003_Buddy_G:# <12>[1453]
	""" Stormpike Lieutenant
	[Avenge (2):] Give your minions +2 Health permanently. """
	#
	pass

class BG22_HERO_003_Buddy_Ge:# <12>[1453]
	""" Lieutenant's Leadership
	+2 Health. """
	#
	pass

class BG22_HERO_003p:# <12>[1453]
	""" Lead the Stormpikes
	Choose a friendly minion.It copies the Health of yourhighest Health minion fornext combat only. """
	#
	pass

class BG22_HERO_003pe:# <12>[1453]
	""" Stormpike Strength
	Copied highest Health. """
	#
	pass

class BG22_HERO_003pe2:# <12>[1453]
	""" Health Set Next Combat Only
	 """
	#
	pass

class BG22_HERO_003pe3:# <12>[1453]
	""" Modified Health Next Combat Only
	Health is increased or decreased for next combat only. """
	#
	pass

#BG22_HERO_004#Varden Dawngrasp
###Varden Dawngrasp
class BG22_HERO_004:# <4>[1453]
	""" Varden Dawngrasp
	 """
	#
	pass
class BG22_HERO_004_Buddy:# <12>[1453]
	""" Varden's Aquarrior
	'Twice as Nice' also gives the copy stats equal to your Tavern Tier. """
	#
	pass

class BG22_HERO_004_Buddy_G:# <12>[1453]
	""" Varden's Aquarrior
	'Twice as Nice' also givesthe copy stats equal toyour Tavern Tier twice. """
	#
	pass
class BG22_HERO_004:# <4>[1453]
	""" Varden Dawngrasp
	 """
	#
	pass

class BG22_HERO_004_Buddy_e2:# <12>[1453]
	""" Frosted
	Increased stats. """
	#
	pass

class BG22_HERO_004p:# <12>[1453]
	""" Twice as Nice
	[Passive.] After Bob'sTavern is [Refreshed],copy and [Freeze] oneof his minions. """
	#
	pass



#Vol'jin
class BG20_HERO_201:# <12>[1453]
	""" Vol'jin
	 """
	#
	pass
class BG20_HERO_201e:# <12>[1453]
	""" Modified Attack
	Attack is increased or decreased. """
	#
	pass
class BG20_HERO_201e2:# <12>[1453]
	""" Modified Health
	Health is increased or decreased. """
	#
	pass
class BG20_HERO_201e3:# <12>[1453]
	""" Stats Set
	 """
	#
	pass
class BG20_HERO_201p:# <12>[1453]
	""" Spirit Swap
	Choose two minions. Swap their stats. """
	#
	pass
class BG20_HERO_201p2:# <12>[1453]
	""" Spirit Swap
	Choose a minion. Swap its stats with {0}. """
	#
	pass
class BG20_HERO_201p2e:# <12>[1453]
	""" Spirit Swapped
	Stats swapped with another minion. """
	#
	pass
class BG20_HERO_201p3e:# <12>[1453]
	""" Marked for Swap
	Stats can be swapped. """
	#
	pass
class BG20_HERO_201_Buddy:# <12>[1453]
	""" Master Gadrin
	At the end of your turn,the minion to the leftof this copies thisminion's Attack. """
	#
	pass
class BG20_HERO_201_Buddy_e:# <12>[1453]
	""" Blessed Hands
	Copied Gadrin's Attack. """
	#
	pass
class BG20_HERO_201_Buddy_e2:# <12>[1453]
	""" Attack Set
	 """
	#
	pass
class BG20_HERO_201_Buddy_G:# <12>[1453]
	""" Master Gadrin
	At the end of your turn,adjacent minions copythis minion's Attack. """
	#
	pass

#Xyrella
class BG20_HERO_101:# <12>[1453]
	""" Xyrella
	 """
	pass
class BG20_HERO_101p:
	""" See the Light
	Choose a minion in Bob's Tavern to add to your hand. Set its stats to 2."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_ENEMY_TARGET:0,PlayReq.REQ_MINION_TARGET:0,}
	activate = Buy(CONTROLLER, TARGET).on(Buff(Buy.CARD,'BG20_HERO_101pe2'))
class BG20_HERO_101pe2:
	max_health = lambda self, i : 2
	atk = lambda self, i : 2
class BG20_HERO_101_Buddy_Action(TargetedAction):
	TARGET=ActionArg()
	BUFF=ActionArg()
	def do(self,source,target,buff):
		if isinstance(target,PlayableCard):
			if target.health==target.atk:
				Buff(source,buff).trigger(source)
class BG20_HERO_101_Buddy:#
	""" Baby Elekk
	After you play a minion with Attack equal to its Health, gain +2/+2. """
	events = BG_Play(CONTROLLER, FRIENDLY + MINION).on(BG20_HERO_101_Buddy_Action(Play.CARD, 'BG20_HERO_101_Buddy_e'))
	pass
BG20_HERO_101_Buddy_e=buff(2,2)
class BG20_HERO_101_Buddy_G:
	""" 
	After you play a minion with Attack equal to its Health, gain +4/+4.""" 
	events = BG_Play(CONTROLLER, FRIENDLY + MINION).on(BG20_HERO_101_Buddy_Action(Play.CARD, 'BG20_HERO_101_Buddy_Ge'))
	pass
BG20_HERO_101_Buddy_Ge=buff(4,4)

#Y'Shaarj

#Yogg-Saron, Hope's End # armor 0

#Ysera

#Zephrys, the Great



####################################################################################

