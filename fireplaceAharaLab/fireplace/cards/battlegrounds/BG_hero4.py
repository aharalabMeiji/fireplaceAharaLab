from ..utils import *

BG_Hero4=[
#53#Rakanishu
'TB_BaconShop_HERO_75','TB_BaconShop_HP_085','TB_BaconShop_HP_085e','TB_BaconShop_HERO_75_Buddy','TB_BaconShop_HERO_75_Buddy_G',
#54#Reno Jackson
'TB_BaconShop_HERO_41','TB_BaconShop_HERO_41_Buddy','TB_BaconShop_HERO_41_Buddy_G','TB_BaconShop_HP_046',
#55#Rokara
'BG20_HERO_100','BG20_HERO_100_Buddy','BG20_HERO_100_Buddy_e','BG20_HERO_100_Buddy_G','BG20_HERO_100_Buddy_Ge','BG20_HERO_100p','BG20_HERO_100p_e2',
#56#Scabbs Cutterbutter
'BG21_HERO_010','BG21_HERO_010_Buddy','BG21_HERO_010_Buddy_G','BG21_HERO_010p',
#57#Shudderwock
'TB_BaconShop_HERO_23','TB_BaconShop_HERO_23_Buddy','TB_BaconShop_HERO_23_Buddy_e','TB_BaconShop_HERO_23_Buddy_G','TB_BaconShop_HERO_23_Buddy_Ge','TB_BaconShop_HP_022','TB_BaconShop_HP_022e','TB_BaconShop_HP_022t','TB_BaconShop_HP_022t_G',
#58#Silas Darkmoon
'TB_BaconShop_HERO_90','TB_BaconShop_HERO_90_Buddy','TB_BaconShop_HERO_90_Buddy_G','TB_BaconShop_HP_101','TB_BaconShop_HP_101e','TB_BaconShop_HP_101t2'
#59#Sindragosa
#60#Sir Finley Mrrgglton
#61#Skycap'n Kragg
#62#Sneed
#63#Tamsin Roame
#64#Tavish Stormpike
#65#Tess Greymane
#66#The Curator
#67#The Great Akazamzarak
#68#The Lich King
#69#The Rat King
]


BG_PoolSet_Hero4=[
	'TB_BaconShop_HERO_75',
	'TB_BaconShop_HERO_41',
	'BG20_HERO_100',
	'BG21_HERO_010',
	'TB_BaconShop_HERO_23',
	'TB_BaconShop_HERO_90',
	]
BG_Hero4_Buddy={
	'TB_BaconShop_HERO_75':'TB_BaconShop_HERO_75_Buddy',
	'TB_BaconShop_HERO_41':'TB_BaconShop_HERO_41_Buddy',
	'BG20_HERO_100':'BG20_HERO_100_Buddy',
	'BG21_HERO_010':'BG21_HERO_010_Buddy',
	'TB_BaconShop_HERO_23':'TB_BaconShop_HERO_23_Buddy',
	'TB_BaconShop_HERO_90':'TB_BaconShop_HERO_90_Buddy',
	}
BG_Hero4_Buddy_Gold={
	'TB_BaconShop_HERO_75_Buddy':'TB_BaconShop_HERO_75_Buddy_G',
	'TB_BaconShop_HERO_41_Buddy':'TB_BaconShop_HERO_41_Buddy_G',
	'BG20_HERO_100_Buddy':'BG20_HERO_100_Buddy_G',
	'BG21_HERO_010_Buddy':'BG21_HERO_010_Buddy_G',
	'TB_BaconShop_HERO_23_Buddy':'TB_BaconShop_HERO_23_Buddy_G',
	'TB_BaconShop_HP_022t':'TB_BaconShop_HP_022t_G',
	'TB_BaconShop_HERO_90_Buddy':'TB_BaconShop_HERO_90_Buddy_G',

	}

######## source #################################################################

#53#Rakanishu # armor 5
class TB_BaconShop_HERO_75:# <12>[1453]
	""" Rakanishu """
	pass
class TB_BaconShop_HP_085:
	"""  """
class TB_BaconShop_HP_085e:
	"""  """
class TB_BaconShop_HERO_75_Buddy:# <12>[1453]
	""" Lantern Tender
	At the end of your turn,give a random friendlyminion stats equal toyour Tavern Tier. """
	pass
class TB_BaconShop_HERO_75_Buddy_G:# <12>[1453]
	""" Lantern Tender
	At the end of your turn,give a random friendlyminion stats equal to yourTavern Tier twice. """
	pass






#Reno Jackson # armor 6
class TB_BaconShop_HERO_41:# <12>[1453]
	""" Reno Jackson """
	pass
class TB_BaconShop_HERO_41_Buddy:# <12>[1453]
	""" Sr. Tomb Diver
	[Deathrattle:] Make your right-most minion Golden. """
	pass
class TB_BaconShop_HERO_41_Buddy_G:# <12>[1453]
	""" Sr. Tomb Diver
	[Deathrattle:] Make your tworight-most minions Golden. """
	pass
class TB_BaconShop_HP_046:
	"""  """
	pass







#Rokara # armor 5
class BG20_HERO_100:# <10>[1453]
	""" Rokara
	 """
	pass
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
class BG20_HERO_100p:# <10>[1453]
	""" Glory of Combat
	&lt;b&gt;Passive.&lt;/b&gt; After a friendly minion kills an enemy, give it +1 Attack permanently. """
	events =  Attack(FRIENDLY_MINIONS, ENEMY_CHARACTERS).on(Buff(Attack.ATTACKER, 'BG20_HERO_100p_e2'))
	pass
BG20_HERO_100p_e2=buff(1,0)



#Scabbs Cutterbutter
#### 010 ####
class BG21_HERO_010:# <7>[1453]
	""" Scabbs Cutterbutter	 """
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
class BG21_HERO_010p:# <7>[1453]
	""" I Spy
	[Discover] a plain copy of a minion from your next opponent's warband. """
	#play = GenericChoice(CONTROLLER, RANDOM(NEXT_OPPONENT) * 3)
	pass



#Shudderwock # armor 3
class TB_BaconShop_HERO_23:# <12>[1453]
	""" Shudderwock """
	pass
class TB_BaconShop_HERO_23_Buddy:# <12>[1453]
	""" Muckslinger
	After you play a minion,add a [Battlecry] minionto Bob's Tavern.Give it +2/+2. """
	pass
class TB_BaconShop_HERO_23_Buddy_e:# <12>[1453]
	""" Mucked Up
	+2/+2. """
	pass
class TB_BaconShop_HERO_23_Buddy_G:# <12>[1453]
	""" Muckslinger
	After you play a minion,add a [Battlecry] minionto Bob's Tavern.Give it +4/+4. """
	pass
class TB_BaconShop_HERO_23_Buddy_Ge:# <12>[1453]
	""" Mucked Up
	+4/+4. """
	pass

class TB_BaconShop_HP_022:
	""" """
	pass
class TB_BaconShop_HP_022e:
	pass
class TB_BaconShop_HP_022t:
	pass
class TB_BaconShop_HP_022t_G:
	pass



#Silas Darkmoon # # armor 6
class TB_BaconShop_HERO_90:# <12>[1453]
	""" Silas Darkmoon """
	pass
class TB_BaconShop_HERO_90_Buddy:# <12>[1453]
	""" Burth
	After you buy a minion witha Darkmoon Ticket, gain1_Gold this turn only. """
	pass
class TB_BaconShop_HERO_90_Buddy_G:# <12>[1453]
	""" Burth
	After you buy a minion witha Darkmoon Ticket, gain2_Gold this turn only. """
	pass
class TB_BaconShop_HP_101:
	"""  """
class TB_BaconShop_HP_101e:
	"""  """
class TB_BaconShop_HP_101t2:
	"""  """
,




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
class TB_BaconShop_HERO_40:# <12>[1453]
	""" Sir Finley Mrrgglton
	 """
	#
	pass

class TB_BaconShop_HERO_40_SKIN_A:# <12>[1453]
	""" Finley of the Kyrian
	 """
	#
	pass

class TB_BaconShop_HERO_40_SKIN_B:# <12>[1453]
	""" Fintastic Finley
	 """
	#
	pass

class TB_BaconShop_HERO_40_SKIN_C:# <12>[1453]
	""" Finley & Metzen
	 """
	#
	pass




#Skycap'n Kragg
class TB_BaconShop_HERO_68:# <12>[1453]
	""" Skycap'n Kragg
	 """
	#
	pass

class TB_BaconShop_HERO_68_SKIN_A:# <12>[1453]
	""" Undercap'n Kragg
	 """
	#
	pass





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
class TB_BaconShop_HERO_50:# <12>[1453]
	""" Tess Greymane
	 """
	#
	pass

class TB_BaconShop_HERO_50_Buddy:# <12>[1453]
	""" Hunter of Old
	At the start of your turn,add your last opponent's Buddy to your hand. """
	#
	pass

class TB_BaconShop_HERO_50_Buddy_G:# <12>[1453]
	""" Hunter of Old
	At the start of your turn, add 2 of your last opponent's Buddy to your hand. """
	#
	pass

class TB_BaconShop_HERO_50_SKIN_A:# <12>[1453]
	""" Venthyr Tess
	 """
	#
	pass

class TB_BaconShop_HERO_50_SKIN_B:# <12>[1453]
	""" Tess, Stormpike Assassin
	 """
	#
	pass

class TB_BaconShop_HERO_50_SKIN_C:# <12>[1453]
	""" Riddling Tempest Tess
	 """
	#
	pass





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


