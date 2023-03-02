#!/usr/bin/env python
from base64 import b16decode
from binascii import a2b_base64
from pickle import TRUE
from re import A
import sys
from hearthstone.enums import *
from utils import *
from agent_Standard import *
from fireplace import cards
from fireplace.debug_utilities import printClasses, printClasses_BG24, parse, parseDeck, printPool
from fireplace.config import Config

sys.path.append("..")

#
#		main()
#
def main():
	if Config.HEARTHSTONE==1:
		cards.db.initialize()
	else:
		cards.db.classic_initialize()
	#manual input(if you don't specify a class, it will be a hunter)
	Human1=HumanAgent("Human1",HumanAgent.HumanInput,myClass=CardClass.DRUID,
		choiceStrategy=HumanAgent.HumanInputChoice)
		# ,mulliganStrategy=HumanAgent.HumanInputMulligan)
	Human2=HumanAgent("Human2",HumanAgent.HumanInput,myClass=CardClass.WARRIOR)
	# random agent
	Random1=StandardAgent("Random1",StandardAgent.StandardRandom, myClass=CardClass.DEMONHUNTER) 
	Random2=StandardAgent("Random2",StandardAgent.StandardRandom, myClass=CardClass.DRUID) 

	#ベクトルプレーヤー。意外と強い。このプレーヤーとサシで勝負して勝てるくらいが一応の目安。
	Vector1=StandardVectorAgent("Vector1",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.PALADIN)
		#,mulliganStrategy=StandardVectorAgent.StandardMulligan) 
	Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.PRIEST)
		#,mulliganStrategy=StandardVectorAgent.StandardMulligan) 
	##DEMONHUNTER,DRUID,HUNTER,MAGE,NEUTRAL,PALADIN,PRIEST,ROGUE,SHAMAN,WARLOCK,WARRIOR.UNDEAD


	####################################################################

	#competition #3 stage

	######### entries (samples) ############

	#deckCatHunter ## this is a sample
	deckCatHunter0={
		"deck":[
		"VAN_CS2_162", "VAN_CS2_162", "VAN_EX1_032", "VAN_EX1_032", "VAN_EX1_050", "VAN_EX1_050", "VAN_CS2_226", "VAN_CS2_226", "VAN_DS1_184", "VAN_DS1_184",
		"VAN_EX1_533", "VAN_EX1_533", "VAN_EX1_537", "VAN_EX1_537", "VAN_CS2_187", "VAN_CS2_187", "VAN_CS2_179", "VAN_CS2_179", "VAN_CS2_125", "VAN_CS2_125",
		"VAN_CS2_203", "VAN_CS2_203", "VAN_EX1_049", "VAN_EX1_049", "VAN_EX1_539", "VAN_EX1_539", "VAN_EX1_080", "VAN_EX1_080", "VAN_CS2_181", "VAN_CS2_181",],
		"class":CardClass.HUNTER}

	deckcatDruid={
		"deck":[## Wins: 819 / 900 = 0.910000 (4)
		"VAN_EX1_509","VAN_EX1_509",#(0)VAN_EX1_509,Murloc Tidecaller,Neutral,Rarity.RARE,1,1,2,Whenever a Murloc is summoned gain +1 Attack.
		"VAN_CS2_179","VAN_CS2_179",#(0)VAN_CS2_179,Sen'jin Shieldmasta,Neutral,Rarity.FREE,4,3,5,<b>Taunt</b>
		"VAN_NEW1_019","VAN_NEW1_019",#(0)VAN_NEW1_019,Knife Juggler,Neutral,Rarity.RARE,2,3,2,[x]After you summon aminion deal 1 damageto a random enemy.
		"VAN_EX1_048","VAN_EX1_048",#(0)VAN_EX1_048,Spellbreaker,Neutral,Rarity.COMMON,4,4,3,<b>Battlecry:</b> <b>Silence</b> a_minion.
		"VAN_CS2_009","VAN_CS2_009",#(1)VAN_CS2_009,Mark of the Wild,Druid,Rarity.FREE,2,0,0,Give a minion <b>Taunt</b> and +2/+2.<i>(+2 Attack/+2 Health)</i>
		"VAN_EX1_011","VAN_EX1_011",#(1)VAN_EX1_011,Voodoo Doctor,Neutral,Rarity.FREE,1,2,1,<b>Battlecry:</b> Restore #2_Health.
		"VAN_EX1_062",#(1)VAN_EX1_062,Old Murk-Eye,Neutral,Rarity.LEGENDARY,4,2,4,<b>Charge</b>. Has +1 Attack for each other Murloc on the battlefield.
		"VAN_EX1_405","VAN_EX1_405",#(1)VAN_EX1_405,Shieldbearer,Neutral,Rarity.COMMON,1,0,4,<b>Taunt</b>
		"VAN_NEW1_029",#(2)VAN_NEW1_029,Millhouse Manastorm,Neutral,Rarity.LEGENDARY,2,4,4,<b>Battlecry:</b> Enemy spells cost (0) next turn.
		"VAN_CS2_203","VAN_CS2_203",#(2)VAN_CS2_203,Ironbeak Owl,Neutral,Rarity.COMMON,2,2,1,<b>Battlecry:</b> <b>Silence</b> a_minion.
		"VAN_CS2_012","VAN_CS2_012",#(2)VAN_CS2_012,Swipe,Druid,Rarity.FREE,4,0,0,Deal $4 damage to an enemy and $1 damage to all other enemies.
		"VAN_CS2_125","VAN_CS2_125",#(2)VAN_CS2_125,Ironfur Grizzly,Neutral,Rarity.FREE,3,3,3,<b>Taunt</b>
		"VAN_CS2_142","VAN_CS2_142",#(3)VAN_CS2_142,Kobold Geomancer,Neutral,Rarity.FREE,2,2,2,<b>Spell Damage +1</b>
		"VAN_EX1_029","VAN_EX1_029",#(3)VAN_EX1_029,Leper Gnome,Neutral,Rarity.COMMON,1,2,1,<b>Deathrattle:</b> Deal 2 damage to the enemy_hero.
		"VAN_CS2_141","VAN_CS2_141",#(3)VAN_CS2_141,Ironforge Rifleman,Neutral,Rarity.FREE,3,2,2,<b>Battlecry:</b> Deal 1 damage.
		"VAN_EX1_066","VAN_EX1_066",#(3)VAN_EX1_066,Acidic Swamp Ooze,Neutral,Rarity.FREE,2,3,2,<b>Battlecry:</b> Destroy your opponent's weapon.
		],"class":CardClass.DRUID}
	deckcatHunter={"deck":[## Wins: 742 / 900 = 0.824444 (3)
		"VAN_EX1_533","VAN_EX1_533",#(0)VAN_EX1_533,Misdirection,Hunter,Rarity.RARE,2,0,0,<b>Secret:</b> When an enemy attacks your hero instead it attacks another random character.
		"VAN_NEW1_031","VAN_NEW1_031",#(0)VAN_NEW1_031,Animal Companion,Hunter,Rarity.FREE,3,0,0,Summon a random Beast Companion.
		"VAN_NEW1_029",#(0)VAN_NEW1_029,Millhouse Manastorm,Neutral,Rarity.LEGENDARY,2,4,4,<b>Battlecry:</b> Enemy spells cost (0) next turn.
		"VAN_DS1_070","VAN_DS1_070",#(0)VAN_DS1_070,Houndmaster,Hunter,Rarity.FREE,4,4,3,<b>Battlecry:</b> Give a friendly Beast +2/+2 and <b>Taunt</b>.
		"VAN_NEW1_019","VAN_NEW1_019",#(1)VAN_NEW1_019,Knife Juggler,Neutral,Rarity.RARE,2,3,2,[x]After you summon aminion deal 1 damageto a random enemy.
		"VAN_EX1_001","VAN_EX1_001",#(1)VAN_EX1_001,Lightwarden,Neutral,Rarity.RARE,1,1,2,Whenever a character is healed gain +2 Attack.
		"VAN_EX1_017","VAN_EX1_017",#(1)VAN_EX1_017,Jungle Panther,Neutral,Rarity.COMMON,3,4,2,<b>Stealth</b>
		"VAN_EX1_010","VAN_EX1_010",#(1)VAN_EX1_010,Worgen Infiltrator,Neutral,Rarity.COMMON,1,2,1,<b>Stealth</b>
		"VAN_CS2_084","VAN_CS2_084",#(2)VAN_CS2_084,Hunter's Mark,Hunter,Rarity.FREE,0,0,0,Change a minion's Health to 1.
		"VAN_NEW1_037","VAN_NEW1_037",#(2)VAN_NEW1_037,Master Swordsmith,Neutral,Rarity.RARE,2,1,3,At the end of your turn give another random friendly minion +1 Attack.
		"VAN_DS1_175","VAN_DS1_175",#(2)VAN_DS1_175,Timber Wolf,Hunter,Rarity.FREE,1,1,1,Your other Beasts have +1_Attack.
		"VAN_EX1_609","VAN_EX1_609",#(2)VAN_EX1_609,Snipe,Hunter,Rarity.COMMON,2,0,0,<b>Secret:</b> After your opponent plays a minion deal $4 damage to it.
		"VAN_NEW1_016","VAN_NEW1_016",#(3)VAN_NEW1_016,Captain's Parrot,Neutral,Rarity.EPIC,2,1,1,<b>Battlecry:</b> Draw a Pirate from your deck.
		"VAN_EX1_076","VAN_EX1_076",#(3)VAN_EX1_076,Pint-Sized Summoner,Neutral,Rarity.RARE,2,2,2,The first minion you play each turn costs (1) less.
		"VAN_EX1_059","VAN_EX1_059",#(3)VAN_EX1_059,Crazed Alchemist,Neutral,Rarity.RARE,2,2,2,<b>Battlecry:</b> Swap the Attack and Health of a minion.
		"VAN_NEW1_020",#(3)VAN_NEW1_020,Wild Pyromancer,Neutral,Rarity.RARE,2,3,2,After you cast a spell deal 1 damage to ALL minions.
		],"class":CardClass.HUNTER}
	deckcatMage={"deck":[## Wins: 739 / 900 = 0.821111 (3)
		"VAN_EX1_066","VAN_EX1_066",#(0)VAN_EX1_066,Acidic Swamp Ooze,Neutral,Rarity.FREE,2,3,2,<b>Battlecry:</b> Destroy your opponent's weapon.
		"VAN_EX1_507","VAN_EX1_507",#(0)VAN_EX1_507,Murloc Warleader,Neutral,Rarity.EPIC,3,3,3,ALL other murlocs have +2/+1.
		"VAN_EX1_062",#(0)VAN_EX1_062,Old Murk-Eye,Neutral,Rarity.LEGENDARY,4,2,4,<b>Charge</b>. Has +1 Attack for each other Murloc on the battlefield.
		"VAN_NEW1_012","VAN_NEW1_012",#(0)VAN_NEW1_012,Mana Wyrm,Mage,Rarity.COMMON,1,1,3,Whenever you cast a spell gain +1 Attack.
		"VAN_NEW1_025","VAN_NEW1_025",#(1)VAN_NEW1_025,Bloodsail Corsair,Neutral,Rarity.RARE,1,1,2,[x]<b>Battlecry:</b> Remove1 Durability from youropponent's weapon.
		"VAN_EX1_045","VAN_EX1_045",#(1)VAN_EX1_045,Ancient Watcher,Neutral,Rarity.RARE,2,4,5,Can't attack.
		"VAN_EX1_015","VAN_EX1_015",#(1)VAN_EX1_015,Novice Engineer,Neutral,Rarity.FREE,2,1,1,<b>Battlecry:</b> Draw a card.
		"VAN_NEW1_027","VAN_NEW1_027",#(1)VAN_NEW1_027,Southsea Captain,Neutral,Rarity.EPIC,3,3,3,Your other Pirates have +1/+1.
		"VAN_EX1_277","VAN_EX1_277",#(2)VAN_EX1_277,Arcane Missiles,Mage,Rarity.FREE,1,0,0,Deal $3 damage randomly split among all enemy characters.
		"VAN_EX1_080","VAN_EX1_080",#(2)VAN_EX1_080,Secretkeeper,Neutral,Rarity.RARE,1,1,2,Whenever a <b>Secret</b> is played gain +1/+1.
		"VAN_EX1_029","VAN_EX1_029",#(2)VAN_EX1_029,Leper Gnome,Neutral,Rarity.COMMON,1,2,1,<b>Deathrattle:</b> Deal 2 damage to the enemy_hero.
		"VAN_EX1_556","VAN_EX1_556",#(2)VAN_EX1_556,Harvest Golem,Neutral,Rarity.COMMON,3,2,3,<b>Deathrattle:</b> Summon a 2/1 Damaged Golem.
		"VAN_CS2_189","VAN_CS2_189",#(3)VAN_CS2_189,Elven Archer,Neutral,Rarity.FREE,1,1,1,<b>Battlecry:</b> Deal 1 damage.
		"VAN_NEW1_017","VAN_NEW1_017",#(3)VAN_NEW1_017,Hungry Crab,Neutral,Rarity.EPIC,1,1,2,<b>Battlecry:</b> Destroy a Murloc and gain +2/+2.
		"VAN_EX1_275","VAN_EX1_275",#(3)VAN_EX1_275,Cone of Cold,Mage,Rarity.COMMON,4,0,0,<b>Freeze</b> a minion and the minions next to it and deal $1 damage to them.
		"VAN_CS2_031",#(3)VAN_CS2_031,Ice Lance,Mage,Rarity.COMMON,1,0,0,<b>Freeze</b> a character. If it was already <b>Frozen</b> deal $4 damage instead.
		], "class":CardClass.MAGE}
	deckcatPaladin={"deck":[## Wins: 640 / 900 = 0.711111 (3)
		"VAN_CS2_187","VAN_CS2_187",#(0)VAN_CS2_187,Booty Bay Bodyguard,Neutral,Rarity.FREE,5,5,4,<b>Taunt</b>
		"VAN_CS2_092","VAN_CS2_092",#(0)VAN_CS2_092,Blessing of Kings,Paladin,Rarity.FREE,4,0,0,Give a minion +4/+4. <i>(+4 Attack/+4 Health)</i>
		"VAN_CS2_097","VAN_CS2_097",#(0)VAN_CS2_097,Truesilver Champion,Paladin,Rarity.FREE,4,4,0,Whenever your hero attacks restore #2_Health to it.
		"VAN_EX1_132","VAN_EX1_132",#(0)VAN_EX1_132,Eye for an Eye,Paladin,Rarity.COMMON,1,0,0,<b>Secret:</b> When your hero takes damage deal_that much damage to the enemy hero.
		"VAN_EX1_032","VAN_EX1_032",#(1)VAN_EX1_032,Sunwalker,Neutral,Rarity.RARE,6,4,5,<b>Taunt</b><b>Divine Shield</b>
		"VAN_EX1_365","VAN_EX1_365",#(1)VAN_EX1_365,Holy Wrath,Paladin,Rarity.RARE,5,0,0,Draw a card and deal_damage equal to_its Cost.
		"VAN_NEW1_023","VAN_NEW1_023",#(1)VAN_NEW1_023,Faerie Dragon,Neutral,Rarity.COMMON,2,3,2,Can't be targeted by spells or Hero Powers.
		"VAN_NEW1_027","VAN_NEW1_027",#(1)VAN_NEW1_027,Southsea Captain,Neutral,Rarity.EPIC,3,3,3,Your other Pirates have +1/+1.
		"VAN_EX1_507","VAN_EX1_507",#(2)VAN_EX1_507,Murloc Warleader,Neutral,Rarity.EPIC,3,3,3,ALL other murlocs have +2/+1.
		"VAN_CS2_146","VAN_CS2_146",#(2)VAN_CS2_146,Southsea Deckhand,Neutral,Rarity.COMMON,1,2,1,Has <b>Charge</b> while you have a weapon equipped.
		"VAN_EX1_616","VAN_EX1_616",#(2)VAN_EX1_616,Mana Wraith,Neutral,Rarity.RARE,2,2,2,ALL minions cost (1) more.
		"VAN_EX1_049","VAN_EX1_049",#(2)VAN_EX1_049,Youthful Brewmaster,Neutral,Rarity.COMMON,2,3,2,<b>Battlecry:</b> Return a friendly minion from the battlefield to your hand.
		"VAN_NEW1_018","VAN_NEW1_018",#(3)VAN_NEW1_018,Bloodsail Raider,Neutral,Rarity.COMMON,2,2,3,<b>Battlecry:</b> Gain Attack equal to the Attackof your weapon.
		"VAN_NEW1_026","VAN_NEW1_026",#(3)VAN_NEW1_026,Violet Teacher,Neutral,Rarity.RARE,4,3,5,Whenever you cast a spell summon a 1/1 Violet Apprentice.
		"VAN_EX1_025","VAN_EX1_025",#(3)VAN_EX1_025,Dragonling Mechanic,Neutral,Rarity.FREE,4,2,4,<b>Battlecry:</b> Summon a 2/1 Mechanical Dragonling.
		"VAN_EX1_170","VAN_EX1_170",#(3)VAN_EX1_170,Emperor Cobra,Neutral,Rarity.RARE,3,2,3,Destroy any minion damaged by this minion.
		], "class":CardClass.PALADIN}
	#frozenMidrangeMage ## this is a sample
	frozenMidrangeMage = {
		"deck":parseDeck("AAEDAf0ECJiiBMSqBNGjBLehBNuhBLWhBM2jBN+VBAvolQTilQS7ogSyoQTDowTVoQTQoQTZlgSTogS5oQSwlgQA"),
		"class":CardClass.MAGE}

	competition_round=1

	########## qualifying ##############

	if competition_round==0:
		theDeck=deckcatHunter
		Vector1=StandardVectorAgent("Vector1",StandardVectorAgent.StandardStep1\
			,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
			,myClass=theDeck["class"])

		myclasses = [CardClass.DRUID,CardClass.HUNTER,CardClass.MAGE,CardClass.PALADIN,CardClass.PRIEST,CardClass.ROGUE,CardClass.SHAMAN,CardClass.WARLOCK,CardClass.WARRIOR]
		win=0
		lose=0
		for myclass in myclasses:
			Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
				,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
				,myClass=myclass)	
			a,b,c = play_set_of_games(Vector1, Vector2, deck1=theDeck["deck"], deck2=[], gameNumber=10, debugLog=True)		
			win+=a
			lose+=b
		print("#### result ####")
		print("win : %d, lose : %d"%(win,lose))
		print("################")
		input()
		pass


	########## final #############

	if competition_round==1:
		theDeck1=deckcatMage
		theDeck2=deckcatPaladin

		Vector1=StandardVectorAgent("Vector1",StandardVectorAgent.StandardStep1\
			,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
			,myClass=theDeck1["class"])
		Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
			,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
			,myClass=theDeck2["class"])	
		#空デッキを指定すると、ランダムデッキが構築される
		a,b,c = play_set_of_games(Vector1, Vector2, deck1=theDeck1["deck"], deck2=theDeck2["deck"], gameNumber=100, debugLog=True)
		print("#### result ####")
		print("Player1 wins : %d, player2 wins : %d"%(a,b))
		print("################")
		input()
	
	######### goto deckCat #############

	#deckCatMain()

	####################################################################

### deckCat ###
class deckCatCard:
	def __init__(self):
		self.id=''
		self.e_name="name"
		self.card_class='CardClass.NEUTRAL'
		self.rarity='Rarity.FREE'
		self.cost=1
		self.atk=0
		self.max_health=0
		self.description=""
		self.max_number=2
		pass

class deckCatBlock:
	def __init__(self):
		self.cardId=''
		self.card=None
		self.pickupStep=-1
		self.active=True
		self.number=2
		pass

def deckCatMain():
	sourceClass=CardClass.SHAMAN
	sourceClassName='SHAMAN'
	Vector1=StandardVectorAgent("Vector1",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=sourceClass)
	targetClasses=[CardClass.DRUID,CardClass.HUNTER,CardClass.MAGE,CardClass.PALADIN,CardClass.PRIEST,CardClass.ROGUE,CardClass.SHAMAN,CardClass.WARLOCK,CardClass.WARRIOR]
	targetClassName='ALL'
	lenTarget=len(targetClasses)
	poolfilename="classic_pool_en.csv"
	matchN=60
	myDeck=[]
	myDeckTexts = []
	myDeckBlocks = []
	myDeckWinrate = []
	mydict ={}
	mydict['XXXX']=0
	pf = open(poolfilename, 'r')
	datalist = pf.readlines()
	pf.close()
	poolcardlist = []
	for line in datalist:
		terms = line.split(',')
		newcard = deckCatCard()
		newcard.id=terms[0]
		newcard.e_name=terms[1]
		newcard.card_class=terms[2]
		newcard.rarity=terms[3]
		newcard.cost=int(terms[4])
		newcard.atk=int(terms[5])
		newcard.max_health=int(terms[6])
		newcard.description=terms[7]
		if newcard.rarity=="Rarity.LEGENDARY":
			newcard.max_number=1
		poolcardlist.append(newcard)
		pass

	stepcount=0

	processend=False

	myDeckTexts.append("\t\t## deckCat-%s-%s"%(sourceClassName,targetClassName))
	for stepcount in range(10):
		cardsfilename="deckCatblockdic-%s-%s_%d.csv"%(sourceClassName,targetClassName,stepcount)
		deckfilename="deckCat-%s-%s_%d.txt"%(sourceClassName,targetClassName,stepcount)
		win_count=0
		mydict ={}
		mydict['XXXX']=0		
		for myCardClass in targetClasses:
			Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
				,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
				,myClass=myCardClass)
			for repeat in range(matchN):
				winner , mydict_thisplay = play_one_game(Vector1, Vector2, deck1=myDeck, deck2=[], debugLog=True)
				if winner=='Vector1':
					win_count += 1
					for key in mydict_thisplay:
						if key in mydict.keys():
							mydict[key] = mydict[key]+1
						else:
							mydict[key] = 1
				else:
					for key in mydict_thisplay:
						if key in mydict.keys():
							mydict[key] = mydict[key]-1
						else:
							mydict[key] = -1
		myDeckWinrate.append([win_count, matchN*lenTarget, stepcount])
		
		blockdic = sorted(mydict.items(), key=lambda x:x[1], reverse=True)
		cf = open(cardsfilename, 'w')
		for key,value in blockdic:
			cf.write(key+','+str(value)+"\n")
		cf.close()

		for block in myDeckBlocks:
			block.active=False
		blocklinecount=0
		blockcardcount=0
		for key, value in blockdic:
			if blocklinecount>=4 or value<0:
				break
			thisblock = [block for block in myDeckBlocks if block.cardId==key] 
			if len(thisblock)>0:
				thisblock[0].active=True
				blockcardcount += thisblock[0].number
				if blockcardcount>= 30:
					print("End point 2")
					processend=True
					break
			else:
				thisblockcard=[card for card in poolcardlist if card.id==key]
				if len(thisblockcard)==0:
					continue
				thisblock = deckCatBlock()
				thisblock.cardId = key
				thisblock.card = thisblockcard[0]
				thisblock.pickupStep=stepcount
				thisblock.active=True
				thisblock.number=thisblock.card.max_number
				myDeckBlocks.append(thisblock)
				blocklinecount += 1
				blockcardcount += thisblock.number
				if blockcardcount> 30:
					thisblock.number=blockcardcount-30
					print("End point 3")
					processend=True
					break
				if blockcardcount==30:
					print("End point 4")
					processend=True
					break
		myDeckTexts=[]		
		myDeck=[]
		for winrate in myDeckWinrate:
			myDeckTexts.append("\t\t## Wins: %d / %d = %f (%d)\n"%(winrate[0], winrate[1], 1.0*winrate[0]/winrate[1], winrate[2]))
		for block in myDeckBlocks:
			blockText="\t\t"
			if block.active==False:
				blockText+="## "
			if block.number==2:
				blockText+='"%s","%s",'%(block.cardId,block.cardId)
			else:
				blockText+='"%s",'%(block.cardId)
			blockText+=('#(%d)%s,%s,%s,%s,%d,%d,%d,%s'%(
					block.pickupStep,
					block.card.id,
					block.card.e_name,
					block.card.card_class,
					block.card.rarity,
					block.card.cost,
					block.card.atk,
					block.card.max_health,
					block.card.description
					))
			myDeckTexts.append(blockText)
			if block.active==True:
				myDeck.append(block.cardId)
				if block.number==2:
					myDeck.append(block.cardId)

		df = open(deckfilename, 'w')
		for text in myDeckTexts:
			df.write("\t\t%s"%(text))
		df.close()
		if processend==True:
			break
	pass

### #3

from card_test.simulate_game import card_test

def battleground_main():
	from fireplace.battlegrounds.BG_utils import  BG_main
	for repeat in range(5):
		BG=BG_main()
		BG.BG_main()


### #6

def simulation_main():
	cards.db.initialize()
	playerA_class=getattr(CardClass, Config.PLAYERA_CLASS)
	playerB_class=getattr(CardClass, Config.PLAYERB_CLASS)
	Vector1=StandardVectorAgent("Vector1",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=playerA_class)
	Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=playerB_class)
	a,b,c = play_set_of_games(Vector1, Vector2, deck1=[], deck2=[], gameNumber=Config.SIMULATION_NUMBER, debugLog=True)

### #7

def simulation_classic_main():
	cards.db.classic_initialize()
	playerA_class=getattr(CardClass, Config.PLAYERA_CLASS)
	playerB_class=getattr(CardClass, Config.PLAYERB_CLASS)
	Vector1=StandardVectorAgent("Vector1",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=playerA_class)
	Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=playerB_class)
	a,b,c = play_set_of_games(Vector1, Vector2, deck1=[], deck2=[], gameNumber=Config.SIMULATION_NUMBER, debugLog=True)

### #8

def simulation_bigDeck_classic_main():
	cclass={'faceHunter':CardClass.HUNTER, 'bigWarrior':CardClass.WARRIOR, 'clownDruid':CardClass.DRUID }
	cards.db.classic_initialize()
	playerA_class=cclass[Config.PLAYERA_DECK]
	playerB_class=cclass[Config.PLAYERB_DECK]
	Vector1=StandardVectorAgent("Vector1",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=playerA_class)
	Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=playerB_class)
	playerA_deck=getattr(BigDeck,Config.PLAYERA_DECK, [])
	playerB_deck=getattr(BigDeck,Config.PLAYERB_DECK, [])
	a,b,c = play_set_of_games(Vector1, Vector2, deck1=playerA_deck, deck2=playerB_deck, gameNumber=Config.SIMULATION_BIGDECK_NUMBER, debugLog=True)

if __name__ == "__main__":
	if Config.HEARTHSTONE==1 or Config.HEARTHSTONE==2:
		main()
	elif Config.HEARTHSTONE==3:
		battleground_main()
	elif Config.HEARTHSTONE==4:
		card_test()
	elif Config.HEARTHSTONE==5:
		#printPool()
		printClasses()
	elif Config.HEARTHSTONE==6:
		simulation_main()
	elif Config.HEARTHSTONE==7:
		simulation_classic_main()
	elif Config.HEARTHSTONE==8:
		simulation_bigDeck_classic_main()
	elif Config.HEARTHSTONE==10:
		parse()
		#parseDeck("AAECAZICAA+t7AOz7APs9QP09gOsgASwgASHnwThpASIsgSuwASozgSB1ASe1ATW3gTd7QQA")
	
