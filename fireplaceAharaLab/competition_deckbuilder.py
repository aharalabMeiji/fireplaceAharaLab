from hearthstone.enums import CardClass
from fireplace.debug_utilities import parseDeck
from agent_Standard import StandardVectorAgent
from utils import play_one_game

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



class CompetitionDeckbuilding:


	def deckCatMain(repeat=0):
		sourceClass=CardClass.DRUID
		sourceClassName='DRUID'
		Vector1=StandardVectorAgent("Vector1",StandardVectorAgent.StandardStep1\
			,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
			,myClass=sourceClass)
		targetClasses=[CardClass.DRUID,CardClass.HUNTER,CardClass.MAGE,CardClass.PALADIN,CardClass.PRIEST,CardClass.ROGUE,CardClass.SHAMAN,CardClass.WARLOCK,CardClass.WARRIOR]
		#targetClasses=[CardClass.SHAMAN]
		targetClassName='N100k5ALL%d'%(repeat)
		lenTarget=len(targetClasses)
		poolfilename="classic_pool_en.csv"
		matchN=100
		myDeck=[
			]
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
		for stepcount in range(20):
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
		
			if processend==True:
				myDeckTexts=[]		
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
				df = open(deckfilename, 'w')
				for text in myDeckTexts:
					df.write("%s"%(text))
				df.close()
				return


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
				if blocklinecount>=5 or value<0:
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
				df.write("%s"%(text))
			df.close()
		pass


	######### entries (samples) ############


	deckcatDruid0={"name":"deckcatDruid0","deck":[## Wins: 819 / 900 = 0.910000 (4)
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
	deckcatDruid25={"name":"deckcatDruid25","deck":[
		## Wins: 157 / 225 = 0.697778 (5)
		## "VAN_EX1_283","VAN_EX1_283",#(0)VAN_EX1_283,Frost Elemental,Neutral,Rarity.COMMON,6,5,5,<b>Battlecry:</b> <b>Freeze</b> a_character.
		## "VAN_EX1_571","VAN_EX1_571",#(0)VAN_EX1_571,Force of Nature,Druid,Rarity.EPIC,6,0,0,Summon three 2/2 Treants with<b>Charge</b> that die at the end of the turn.
		## "VAN_EX1_178","VAN_EX1_178",#(0)VAN_EX1_178,Ancient of War,Druid,Rarity.EPIC,7,5,5,<b>Choose One -</b>+5 Attack; or +5 Health and <b>Taunt</b>.
		## "VAN_EX1_298",#(0)VAN_EX1_298,Ragnaros the Firelord,Neutral,Rarity.LEGENDARY,8,8,8,Can't attack. At the end of your turn deal 8 damage to a random enemy.
		## "VAN_EX1_032","VAN_EX1_032",#(1)VAN_EX1_032,Sunwalker,Neutral,Rarity.RARE,6,4,5,<b>Taunt</b><b>Divine Shield</b>
		"VAN_EX1_097","VAN_EX1_097",#(1)VAN_EX1_097,Abomination,Neutral,Rarity.RARE,5,4,4,<b>Taunt</b>. <b>Deathrattle:</b> Deal 2damage to ALL characters.
		## "VAN_NEW1_016","VAN_NEW1_016",#(1)VAN_NEW1_016,Captain's Parrot,Neutral,Rarity.EPIC,2,1,1,<b>Battlecry:</b> Draw a Pirate from your deck.
		"VAN_EX1_049","VAN_EX1_049",#(1)VAN_EX1_049,Youthful Brewmaster,Neutral,Rarity.COMMON,2,3,2,<b>Battlecry:</b> Return a friendly minion from the battlefield to your hand.
		"VAN_EX1_062",#(2)VAN_EX1_062,Old Murk-Eye,Neutral,Rarity.LEGENDARY,4,2,4,<b>Charge</b>. Has +1 Attack for each other Murloc on the battlefield.
		"VAN_EX1_155","VAN_EX1_155",#(2)VAN_EX1_155,Mark of Nature,Druid,Rarity.COMMON,3,0,0,<b>Choose One -</b> Give a minion +4 Attack; or +4 Health and <b>Taunt</b>.
		"VAN_EX1_085","VAN_EX1_085",#(2)VAN_EX1_085,Mind Control Tech,Neutral,Rarity.RARE,3,3,3,[x]<b>Battlecry:</b> If your opponenthas 4 or more minions take control of one at random.
		"VAN_EX1_076","VAN_EX1_076",#(2)VAN_EX1_076,Pint-Sized Summoner,Neutral,Rarity.RARE,2,2,2,The first minion you play each turn costs (1) less.
		"VAN_EX1_507","VAN_EX1_507",#(3)VAN_EX1_507,Murloc Warleader,Neutral,Rarity.EPIC,3,3,3,ALL other murlocs have +2/+1.
		"VAN_CS2_005","VAN_CS2_005",#(3)VAN_CS2_005,Claw,Druid,Rarity.FREE,1,0,0,Give your hero +2_Attack this turn. Gain 2 Armor.
		"VAN_NEW1_019","VAN_NEW1_019",#(3)VAN_NEW1_019,Knife Juggler,Neutral,Rarity.RARE,2,3,2,[x]After you summon aminion deal 1 damageto a random enemy.
		"VAN_EX1_096","VAN_EX1_096",#(3)VAN_EX1_096,Loot Hoarder,Neutral,Rarity.COMMON,2,2,1,<b>Deathrattle:</b> Draw a card.
		## "VAN_CS2_147","VAN_CS2_147",#(4)VAN_CS2_147,Gnomish Inventor,Neutral,Rarity.FREE,4,2,4,<b>Battlecry:</b> Draw a card.
		"VAN_EX1_095","VAN_EX1_095",#(4)VAN_EX1_095,Gadgetzan Auctioneer,Neutral,Rarity.RARE,5,4,4,Whenever you cast a spell draw a card.
		"VAN_NEW1_023","VAN_NEW1_023",#(4)VAN_NEW1_023,Faerie Dragon,Neutral,Rarity.COMMON,2,3,2,Can't be targeted by spells or Hero Powers.
		"VAN_NEW1_037","VAN_NEW1_037",#(4)VAN_NEW1_037,Master Swordsmith,Neutral,Rarity.RARE,2,1,3,At the end of your turn give another random friendly minion +1 Attack.
		"VAN_CS2_120","VAN_CS2_120",#(5)VAN_CS2_120,River Crocolisk,Neutral,Rarity.FREE,2,2,3,
		"VAN_EX1_045","VAN_EX1_045",#(5)VAN_EX1_045,Ancient Watcher,Neutral,Rarity.RARE,2,4,5,Can't attack.
		"VAN_EX1_556",#(5)VAN_EX1_556,Harvest Golem,Neutral,Rarity.COMMON,3,2,3,<b>Deathrattle:</b> Summon a 2/1 Damaged Golem.
		],"class":CardClass.DRUID}
	deckcatDruid50={"name":"deckcatDruid50","deck":[
		## Wins: 403 / 450 = 0.895556 (3)
		"VAN_CS2_009","VAN_CS2_009",#(0)VAN_CS2_009,Mark of the Wild,Druid,Rarity.FREE,2,0,0,Give a minion <b>Taunt</b> and +2/+2.<i>(+2 Attack/+2 Health)</i>
		"VAN_CS2_122","VAN_CS2_122",#(0)VAN_CS2_122,Raid Leader,Neutral,Rarity.FREE,3,2,2,Your other minions have +1 Attack.
		"VAN_EX1_058","VAN_EX1_058",#(0)VAN_EX1_058,Sunfury Protector,Neutral,Rarity.RARE,2,2,3,<b>Battlecry:</b> Give adjacent minions <b>Taunt</b>.
		## "VAN_PRO_001",#(0)VAN_PRO_001,Elite Tauren Chieftain,Neutral,Rarity.LEGENDARY,5,5,5,<b>Battlecry:</b> Give both players the power to ROCK! (with a Power Chord card)
		"VAN_EX1_103","VAN_EX1_103",#(1)VAN_EX1_103,Coldlight Seer,Neutral,Rarity.RARE,3,2,3,<b>Battlecry:</b> Give ALL other Murlocs +2 Health.
		"VAN_EX1_165","VAN_EX1_165",#(1)VAN_EX1_165,Druid of the Claw,Druid,Rarity.COMMON,5,4,4,<b>Choose One -</b> <b>Charge</b>; or +2 Health and <b>Taunt</b>.
		"VAN_EX1_508","VAN_EX1_508",#(1)VAN_EX1_508,Grimscale Oracle,Neutral,Rarity.FREE,1,1,1,ALL other Murlocs have +1 Attack.
		"VAN_CS2_231","VAN_CS2_231",#(1)VAN_CS2_231,Wisp,Neutral,Rarity.COMMON,0,1,1,
		"VAN_EX1_010","VAN_EX1_010",#(2)VAN_EX1_010,Worgen Infiltrator,Neutral,Rarity.COMMON,1,2,1,<b>Stealth</b>
		"VAN_EX1_507","VAN_EX1_507",#(2)VAN_EX1_507,Murloc Warleader,Neutral,Rarity.EPIC,3,3,3,ALL other murlocs have +2/+1.
		"VAN_EX1_029","VAN_EX1_029",#(2)VAN_EX1_029,Leper Gnome,Neutral,Rarity.COMMON,1,2,1,<b>Deathrattle:</b> Deal 2 damage to the enemy_hero.
		"VAN_CS2_142","VAN_CS2_142",#(2)VAN_CS2_142,Kobold Geomancer,Neutral,Rarity.FREE,2,2,2,<b>Spell Damage +1</b>
		"VAN_CS2_169","VAN_CS2_169",#(3)VAN_CS2_169,Young Dragonhawk,Neutral,Rarity.COMMON,1,1,1,<b>Windfury</b>
		"VAN_NEW1_037","VAN_NEW1_037",#(3)VAN_NEW1_037,Master Swordsmith,Neutral,Rarity.RARE,2,1,3,At the end of your turn give another random friendly minion +1 Attack.
		"VAN_CS2_197","VAN_CS2_197",#(3)VAN_CS2_197,Ogre Magi,Neutral,Rarity.FREE,4,4,4,<b>Spell Damage +1</b>
		"VAN_CS2_141","VAN_CS2_141",#(3)VAN_CS2_141,Ironforge Rifleman,Neutral,Rarity.FREE,3,2,2,<b>Battlecry:</b> Deal 1 damage.
		],"class":CardClass.DRUID}
	deckcatDruid100={"name":"deckcatDruid100","deck":[
		## Wins: 740 / 900 = 0.822222 (4)
		## "VAN_EX1_396","VAN_EX1_396",#(0)VAN_EX1_396,Mogu'shan Warden,Neutral,Rarity.COMMON,4,1,7,<b>Taunt</b>
		"VAN_CS2_012","VAN_CS2_012",#(0)VAN_CS2_012,Swipe,Druid,Rarity.FREE,4,0,0,Deal $4 damage to an enemy and $1 damage to all other enemies.
		"VAN_NEW1_019","VAN_NEW1_019",#(0)VAN_NEW1_019,Knife Juggler,Neutral,Rarity.RARE,2,3,2,[x]After you summon aminion deal 1 damageto a random enemy.
		## "VAN_EX1_154","VAN_EX1_154",#(0)VAN_EX1_154,Wrath,Druid,Rarity.COMMON,2,0,0,<b>Choose One -</b>Deal $3 damage to a minion; or $1 damageand draw a card.
		"VAN_EX1_093","VAN_EX1_093",#(1)VAN_EX1_093,Defender of Argus,Neutral,Rarity.RARE,4,2,3,<b>Battlecry:</b> Give adjacent minions +1/+1 and <b>Taunt</b>.
		"VAN_EX1_165","VAN_EX1_165",#(1)VAN_EX1_165,Druid of the Claw,Druid,Rarity.COMMON,5,4,4,<b>Choose One -</b> <b>Charge</b>; or +2 Health and <b>Taunt</b>.
		## "VAN_EX1_116",#(1)VAN_EX1_116,Leeroy Jenkins,Neutral,Rarity.LEGENDARY,4,6,2,<b>Charge</b>. <b>Battlecry:</b> Summon two 1/1 Whelps for your opponent.
		## "VAN_NEW1_008","VAN_NEW1_008",#(1)VAN_NEW1_008,Ancient of Lore,Druid,Rarity.EPIC,7,5,5,<b>Choose One -</b> Draw 2 cards; or Restore #5 Health.
		"VAN_CS2_120","VAN_CS2_120",#(2)VAN_CS2_120,River Crocolisk,Neutral,Rarity.FREE,2,2,3,
		"VAN_EX1_393","VAN_EX1_393",#(2)VAN_EX1_393,Amani Berserker,Neutral,Rarity.COMMON,2,2,3,<b>Enrage:</b> +3 Attack
		"VAN_EX1_178","VAN_EX1_178",#(2)VAN_EX1_178,Ancient of War,Druid,Rarity.EPIC,7,5,5,<b>Choose One -</b>+5 Attack; or +5 Health and <b>Taunt</b>.
		"VAN_CS2_169","VAN_CS2_169",#(2)VAN_CS2_169,Young Dragonhawk,Neutral,Rarity.COMMON,1,1,1,<b>Windfury</b>
		"VAN_CS2_181","VAN_CS2_181",#(3)VAN_CS2_181,Injured Blademaster,Neutral,Rarity.RARE,3,4,7,<b>Battlecry:</b> Deal 4 damage to HIMSELF.
		"VAN_CS2_009","VAN_CS2_009",#(3)VAN_CS2_009,Mark of the Wild,Druid,Rarity.FREE,2,0,0,Give a minion <b>Taunt</b> and +2/+2.<i>(+2 Attack/+2 Health)</i>
		"VAN_CS2_008","VAN_CS2_008",#(3)VAN_CS2_008,Moonfire,Druid,Rarity.FREE,0,0,0,Deal $1 damage.
		"VAN_EX1_009","VAN_EX1_009",#(3)VAN_EX1_009,Angry Chicken,Neutral,Rarity.RARE,1,1,1,<b>Enrage:</b> +5 Attack.
		"VAN_EX1_006","VAN_EX1_006",#(4)VAN_EX1_006,Alarm-o-Bot,Neutral,Rarity.RARE,3,0,3,[x]At the start of your turnswap this minion with a   random one in your hand.
		"VAN_EX1_025","VAN_EX1_025",#(4)VAN_EX1_025,Dragonling Mechanic,Neutral,Rarity.FREE,4,2,4,<b>Battlecry:</b> Summon a 2/1 Mechanical Dragonling.
		"VAN_CS2_155","VAN_CS2_155",#(4)VAN_CS2_155,Archmage,Neutral,Rarity.FREE,6,4,7,<b>Spell Damage +1</b>
		],"class":CardClass.DRUID}
	deckcatDruid200={"name":"deckcatDruid200","deck":[##Wins: 1628 / 1800 = 0.904444 (4)
		"VAN_CS2_009","VAN_CS2_009",#(0)VAN_CS2_009,Mark of the Wild,Druid,Rarity.FREE,2,0,0,Give a minion <b>Taunt</b> and +2/+2.<i>(+2 Attack/+2 Health)</i>
		"VAN_EX1_166","VAN_EX1_166",#(0)VAN_EX1_166,Keeper of the Grove,Druid,Rarity.RARE,4,2,4,<b>Choose One -</b> Deal_2_damage; or <b>Silence</b> a minion.
		"VAN_EX1_509","VAN_EX1_509",#(0)VAN_EX1_509,Murloc Tidecaller,Neutral,Rarity.RARE,1,1,2,Whenever a Murloc is summoned gain +1 Attack.
		"VAN_EX1_390","VAN_EX1_390",#(0)VAN_EX1_390,Tauren Warrior,Neutral,Rarity.COMMON,3,2,3,<b>Taunt</b>. <b>Enrage:</b> +3 Attack
		"VAN_EX1_066","VAN_EX1_066",#(1)VAN_EX1_066,Acidic Swamp Ooze,Neutral,Rarity.FREE,2,3,2,<b>Battlecry:</b> Destroy your opponent's weapon.
		"VAN_CS2_187","VAN_CS2_187",#(1)VAN_CS2_187,Booty Bay Bodyguard,Neutral,Rarity.FREE,5,5,4,<b>Taunt</b>
		"VAN_CS2_013","VAN_CS2_013",#(1)VAN_CS2_013,Wild Growth,Druid,Rarity.FREE,2,0,0,Gain an empty Mana Crystal.
		"VAN_CS2_146","VAN_CS2_146",#(1)VAN_CS2_146,Southsea Deckhand,Neutral,Rarity.COMMON,1,2,1,Has <b>Charge</b> while you have a weapon equipped.
		"VAN_CS2_169","VAN_CS2_169",#(2)VAN_CS2_169,Young Dragonhawk,Neutral,Rarity.COMMON,1,1,1,<b>Windfury</b>
		"VAN_CS2_005","VAN_CS2_005",#(2)VAN_CS2_005,Claw,Druid,Rarity.FREE,1,0,0,Give your hero +2_Attack this turn. Gain 2 Armor.
		"VAN_CS2_012","VAN_CS2_012",#(2)VAN_CS2_012,Swipe,Druid,Rarity.FREE,4,0,0,Deal $4 damage to an enemy and $1 damage to all other enemies.
		"VAN_CS2_231","VAN_CS2_231",#(2)VAN_CS2_231,Wisp,Neutral,Rarity.COMMON,0,1,1,
		"VAN_NEW1_029",#(3)VAN_NEW1_029,Millhouse Manastorm,Neutral,Rarity.LEGENDARY,2,4,4,<b>Battlecry:</b> Enemy spells cost (0) next turn.
		"VAN_EX1_082","VAN_EX1_082",#(3)VAN_EX1_082,Mad Bomber,Neutral,Rarity.COMMON,2,3,2,<b>Battlecry:</b> Deal 3 damage randomly split between all other characters.
		"VAN_EX1_506","VAN_EX1_506",#(3)VAN_EX1_506,Murloc Tidehunter,Neutral,Rarity.FREE,2,2,1,<b>Battlecry:</b> Summon a 1/1_Murloc Scout.
		"VAN_EX1_014",#(3)VAN_EX1_014,King Mukla,Neutral,Rarity.LEGENDARY,3,5,5,<b>Battlecry:</b> Give your opponent 2 Bananas.
		],"class":CardClass.DRUID}
	#classicDruid ## this is a sample
	#classicTier1Druid = {"name":"classicTier1Druid",#win : 699/1000
	#	"deck":parseDeck("AAEDAZICArehBNuhBA7ZlQTblQTclQSvlgSwlgTdlgT6oATpoQTwoQTxoQTzoQSTogS9owTFqgQA"),
	#	"class":CardClass.DRUID}



	#deckCatHunter ## this is a sample
	deckcatHunter0={"name":"deckCatHunter0",### 908/1000
		"deck":[
		"VAN_CS2_162","VAN_CS2_162",#VAN_CS2_162#,Lord of the Arena,Neutral,Rarity.FREE,6,6,5,<b>Taunt</b>
		"VAN_EX1_032","VAN_EX1_032",#VAN_EX1_032#,Sunwalker, Neutral,Rarity.RARE,6,4,5,<b>Taunt</b><b>Divine Shield</b>
		"VAN_EX1_050","VAN_EX1_050",#VAN_EX1_050#,Coldlight Oracle, Neutral,Rarity.RARE,3,2,2,<b>Battlecry:</b> Each player draws 2 cards.
		"VAN_CS2_226","VAN_CS2_226",#VAN_CS2_226#,Frostwolf Warlord, Neutral,Rarity.FREE,5,4,4,<b>Battlecry:</b> Gain +1/+1 for each other friendly minion on the battlefield.
		"VAN_DS1_184","VAN_DS1_184",#VAN_DS1_184#,Tracking, Hunter,Rarity.FREE,1,0,0,Look at the top 3 cards of your deck. Draw one and discard the others.
		"VAN_EX1_533","VAN_EX1_533",#VAN_EX1_533,Misdirection, Hunter,Rarity.RARE,2,0,0,<b>Secret:</b> When an enemy attacks your hero instead it attacks another random character.
		"VAN_EX1_537","VAN_EX1_537",#VAN_EX1_537,Explosive Shot, Hunter,Rarity.RARE,5,0,0,Deal $5 damage to a minion and $2 damage to adjacent ones.
		"VAN_CS2_187","VAN_CS2_187",#VAN_CS2_187,Booty Bay Bodyguard, Neutral,Rarity.FREE,5,5,4,<b>Taunt</b>
		"VAN_CS2_179","VAN_CS2_179",#VAN_CS2_179,Sen'jin Shieldmasta, Neutral,Rarity.FREE,4,3,5,<b>Taunt</b>
		"VAN_CS2_125","VAN_CS2_125",#VAN_CS2_125,Ironfur Grizzly, Neutral,Rarity.FREE,3,3,3,<b>Taunt</b>
		"VAN_CS2_203","VAN_CS2_203",#VAN_CS2_203,Ironbeak Owl, Neutral,Rarity.COMMON,2,2,1,<b>Battlecry:</b> <b>Silence</b> a_minion.
		"VAN_EX1_049","VAN_EX1_049",#VAN_EX1_049,Youthful Brewmaster, Neutral,Rarity.COMMON,2,3,2,<b>Battlecry:</b> Return a friendly minion from the battlefield to your hand.
		"VAN_EX1_539","VAN_EX1_539",#VAN_EX1_539,Kill Command, Hunter,Rarity.FREE,3,0,0,Deal $3 damage. If you control a Beast deal$5 damage instead.
		"VAN_EX1_080","VAN_EX1_080",#VAN_EX1_080,Secretkeeper, Neutral,Rarity.RARE,1,1,2,Whenever a <b>Secret</b> is played gain +1/+1.
		"VAN_CS2_181","VAN_CS2_181",#VAN_CS2_181,Injured Blademaster,Neutral,Rarity.RARE,3,4,7,<b>Battlecry:</b> Deal 4 damage to HIMSELF.
		],"class":CardClass.HUNTER }
	deckcatHunter100={"name":"deckcatHunter","deck":[## Wins: 742 / 900 = 0.824444 (3)
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
	deckcatMage={"name":"deckcatMage","deck":[## Wins: 739 / 900 = 0.821111 (3)
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
	deckcatPaladin={"name":"deckcatPaladin","deck":[## Wins: 640 / 900 = 0.711111 (3)
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
	deckcatPriest={"name":"deckcatPriest","deck":[## Wins: 681 / 900 = 0.756667 (4)
		"VAN_CS2_117","VAN_CS2_117",#(0)VAN_CS2_117,Earthen Ring Farseer,Neutral,Rarity.COMMON,3,3,3,<b>Battlecry:</b> Restore #3_Health.
		"VAN_CS2_231","VAN_CS2_231",#(0)VAN_CS2_231,Wisp,Neutral,Rarity.COMMON,0,1,1,
		"VAN_EX1_062",#(0)VAN_EX1_062,Old Murk-Eye,Neutral,Rarity.LEGENDARY,4,2,4,<b>Charge</b>. Has +1 Attack for each other Murloc on the battlefield.
		"VAN_EX1_032","VAN_EX1_032",#(0)VAN_EX1_032,Sunwalker,Neutral,Rarity.RARE,6,4,5,<b>Taunt</b><b>Divine Shield</b>
		"VAN_CS2_127","VAN_CS2_127",#(1)VAN_CS2_127,Silverback Patriarch,Neutral,Rarity.FREE,3,1,4,<b>Taunt</b>
		"VAN_EX1_593","VAN_EX1_593",#(1)VAN_EX1_593,Nightblade,Neutral,Rarity.FREE,5,4,4,<b>Battlecry: </b>Deal 3 damage to the enemy hero.
		"VAN_tt_004","VAN_tt_004",#(1)VAN_tt_004,Flesheating Ghoul,Neutral,Rarity.COMMON,3,2,3,Whenever a minion dies gain +1 Attack.
		"VAN_CS1_042","VAN_CS1_042",#(1)VAN_CS1_042,Goldshire Footman,Neutral,Rarity.FREE,1,1,2,<b>Taunt</b>
		"VAN_EX1_046","VAN_EX1_046",#(2)VAN_EX1_046,Dark Iron Dwarf,Neutral,Rarity.COMMON,4,4,4,<b>Battlecry:</b> Give a minion +2_Attack this turn.
		"VAN_EX1_011","VAN_EX1_011",#(2)VAN_EX1_011,Voodoo Doctor,Neutral,Rarity.FREE,1,2,1,<b>Battlecry:</b> Restore #2_Health.
		"VAN_EX1_028","VAN_EX1_028",#(2)VAN_EX1_028,Stranglethorn Tiger,Neutral,Rarity.COMMON,5,5,5,<b>Stealth</b>
		"VAN_CS2_146","VAN_CS2_146",#(2)VAN_CS2_146,Southsea Deckhand,Neutral,Rarity.COMMON,1,2,1,Has <b>Charge</b> while you have a weapon equipped.
		"VAN_EX1_170","VAN_EX1_170",#(3)VAN_EX1_170,Emperor Cobra,Neutral,Rarity.RARE,3,2,3,Destroy any minion damaged by this minion.
		"VAN_EX1_048","VAN_EX1_048",#(3)VAN_EX1_048,Spellbreaker,Neutral,Rarity.COMMON,4,4,3,<b>Battlecry:</b> <b>Silence</b> a_minion.
		"VAN_EX1_116",#(3)VAN_EX1_116,Leeroy Jenkins,Neutral,Rarity.LEGENDARY,4,6,2,<b>Charge</b>. <b>Battlecry:</b> Summon two 1/1 Whelps for your opponent.
		"VAN_EX1_102","VAN_EX1_102",#(3)VAN_EX1_102,Demolisher,Neutral,Rarity.RARE,3,1,4,At the start of your turn deal 2 damage to a random enemy.
		], "class":CardClass.PRIEST}
	deckcatRogue={"name":"deckcatRogue","deck":[##Wins: 765 / 900 = 0.850000 (5)
		## "VAN_NEW1_005","VAN_NEW1_005",#(0)VAN_NEW1_005,Kidnapper,Rogue,Rarity.EPIC,6,5,3,<b>Combo:</b> Return a minion to_its owner's hand.
		"VAN_CS2_080","VAN_CS2_080",#(1)VAN_CS2_080,Assassin's Blade,Rogue,Rarity.FREE,5,3,0,
		"VAN_EX1_097","VAN_EX1_097",#(1)VAN_EX1_097,Abomination,Neutral,Rarity.RARE,5,4,4,<b>Taunt</b>. <b>Deathrattle:</b> Deal 2damage to ALL characters.
		## "VAN_PRO_001",#(1)VAN_PRO_001,Elite Tauren Chieftain,Neutral,Rarity.LEGENDARY,5,5,5,<b>Battlecry:</b> Give both players the power to ROCK! (with a Power Chord card)
		## "VAN_CS2_077","VAN_CS2_077",#(2)VAN_CS2_077,Sprint,Rogue,Rarity.FREE,7,0,0,Draw 4 cards.
		"VAN_EX1_507","VAN_EX1_507",#(2)VAN_EX1_507,Murloc Warleader,Neutral,Rarity.EPIC,3,3,3,ALL other murlocs have +2/+1.
		"VAN_NEW1_027","VAN_NEW1_027",#(2)VAN_NEW1_027,Southsea Captain,Neutral,Rarity.EPIC,3,3,3,Your other Pirates have +1/+1.
		## "VAN_EX1_561",#(2)VAN_EX1_561,Alexstrasza,Neutral,Rarity.LEGENDARY,9,8,8,<b>Battlecry:</b> Set a hero's remaining Health to 15.
		"VAN_EX1_522","VAN_EX1_522",#(3)VAN_EX1_522,Patient Assassin,Rogue,Rarity.EPIC,2,1,1,<b>Stealth</b>. Destroy any minion damaged by this minion.
		"VAN_CS2_121","VAN_CS2_121",#(3)VAN_CS2_121,Frostwolf Grunt,Neutral,Rarity.FREE,2,2,2,<b>Taunt</b>
		"VAN_CS2_073","VAN_CS2_073",#(3)VAN_CS2_073,Cold Blood,Rogue,Rarity.COMMON,1,0,0,Give a minion +2 Attack. <b>Combo:</b> +4 Attack instead.
		"VAN_NEW1_029",#(3)VAN_NEW1_029,Millhouse Manastorm,Neutral,Rarity.LEGENDARY,2,4,4,<b>Battlecry:</b> Enemy spells cost (0) next turn.
		"VAN_CS2_173","VAN_CS2_173",#(4)VAN_CS2_173,Bluegill Warrior,Neutral,Rarity.FREE,2,2,1,<b>Charge</b>
		"VAN_EX1_124","VAN_EX1_124",#(4)VAN_EX1_124,Eviscerate,Rogue,Rarity.COMMON,2,0,0,Deal $2 damage. <b>Combo:</b> Deal $4 damage instead.
		"VAN_NEW1_022","VAN_NEW1_022",#(4)VAN_NEW1_022,Dread Corsair,Neutral,Rarity.COMMON,4,3,3,<b>Taunt</b>Costs (1) less per Attack of_your weapon.
		"VAN_EX1_021","VAN_EX1_021",#(4)VAN_EX1_021,Thrallmar Farseer,Neutral,Rarity.COMMON,3,2,3,<b>Windfury</b>
		"VAN_EX1_029","VAN_EX1_029",#(5)VAN_EX1_029,Leper Gnome,Neutral,Rarity.COMMON,1,2,1,<b>Deathrattle:</b> Deal 2 damage to the enemy_hero.
		"VAN_EX1_080","VAN_EX1_080",#(5)VAN_EX1_080,Secretkeeper,Neutral,Rarity.RARE,1,1,2,Whenever a <b>Secret</b> is played gain +1/+1.
		"VAN_EX1_412","VAN_EX1_412",#(5)VAN_EX1_412,Raging Worgen,Neutral,Rarity.COMMON,3,3,3,<b>Enrage:</b> <b>Windfury</b> and +1 Attack
		"VAN_EX1_019",#(5)VAN_EX1_019,Shattered Sun Cleric,Neutral,Rarity.FREE,3,3,2,<b>Battlecry:</b> Give a friendly minion +1/+1.
		], "class":CardClass.ROGUE}



	deckcatShaman100={"name":"deckcatShaman100","deck":[## Wins: 462 / 540 = 0.855556 (7)
		## "VAN_EX1_561",#(0)VAN_EX1_561,Alexstrasza,Neutral,Rarity.LEGENDARY,9,8,8,<b>Battlecry:</b> Set a hero's remaining Health to 15.
		## "VAN_NEW1_030",#(1)VAN_NEW1_030,Deathwing,Neutral,Rarity.LEGENDARY,10,12,12,<b>Battlecry:</b> Destroy all other minions and discard your_hand.
		## "VAN_EX1_560",#(2)VAN_EX1_560,Nozdormu,Neutral,Rarity.LEGENDARY,9,8,8,Players only have 15 seconds to take their_turns.
		"VAN_EX1_509","VAN_EX1_509",#(3)VAN_EX1_509,Murloc Tidecaller,Neutral,Rarity.RARE,1,1,2,Whenever a Murloc is summoned gain +1 Attack.
		"VAN_CS2_179","VAN_CS2_179",#(3)VAN_CS2_179,Sen'jin Shieldmasta,Neutral,Rarity.FREE,4,3,5,<b>Taunt</b>
		"VAN_EX1_244","VAN_EX1_244",#(3)VAN_EX1_244,Totemic Might,Shaman,Rarity.FREE,0,0,0,Give your Totems +2_Health.
		## "VAN_DS1_055","VAN_DS1_055",#(3)VAN_DS1_055,Darkscale Healer,Neutral,Rarity.FREE,5,4,5,<b>Battlecry:</b> Restore #2 Health to all friendly characters.
		"VAN_EX1_097","VAN_EX1_097",#(4)VAN_EX1_097,Abomination,Neutral,Rarity.RARE,5,4,4,<b>Taunt</b>. <b>Deathrattle:</b> Deal 2damage to ALL characters.
		"VAN_CS2_162","VAN_CS2_162",#(4)VAN_CS2_162,Lord of the Arena,Neutral,Rarity.FREE,6,6,5,<b>Taunt</b>
		"VAN_CS2_187","VAN_CS2_187",#(4)VAN_CS2_187,Booty Bay Bodyguard,Neutral,Rarity.FREE,5,5,4,<b>Taunt</b>
		"VAN_CS2_196","VAN_CS2_196",#(4)VAN_CS2_196,Razorfen Hunter,Neutral,Rarity.FREE,3,2,3,<b>Battlecry:</b> Summon a 1/1_Boar.
		"VAN_EX1_250","VAN_EX1_250",#(5)VAN_EX1_250,Earth Elemental,Shaman,Rarity.EPIC,5,7,8,<b>Taunt</b>. <b><b>Overload</b>:</b> (3)
		"VAN_EX1_616","VAN_EX1_616",#(5)VAN_EX1_616,Mana Wraith,Neutral,Rarity.RARE,2,2,2,ALL minions cost (1) more.
		"VAN_CS2_203","VAN_CS2_203",#(5)VAN_CS2_203,Ironbeak Owl,Neutral,Rarity.COMMON,2,2,1,<b>Battlecry:</b> <b>Silence</b> a_minion.
		"VAN_NEW1_021","VAN_NEW1_021",#(5)VAN_NEW1_021,Doomsayer,Neutral,Rarity.EPIC,2,0,7,At the start of your turn destroy ALL minions.
		"VAN_EX1_009","VAN_EX1_009",#(6)VAN_EX1_009,Angry Chicken,Neutral,Rarity.RARE,1,1,1,<b>Enrage:</b> +5 Attack.
		"VAN_CS2_117","VAN_CS2_117",#(6)VAN_CS2_117,Earthen Ring Farseer,Neutral,Rarity.COMMON,3,3,3,<b>Battlecry:</b> Restore #3_Health.
		"VAN_tt_004","VAN_tt_004",#(6)VAN_tt_004,Flesheating Ghoul,Neutral,Rarity.COMMON,3,2,3,Whenever a minion dies gain +1 Attack.
		"VAN_EX1_005","VAN_EX1_005",#(6)VAN_EX1_005,Big Game Hunter,Neutral,Rarity.EPIC,3,4,2,<b>Battlecry:</b> Destroy a minion with 7 or more Attack.
		], "class":CardClass.SHAMAN}
	deckcatShaman25={"name":"deckcatShaman25","deck":[## Wins: 186 / 225 = 0.826667 (4)
		"VAN_CS2_046","VAN_CS2_046",#(0)VAN_CS2_046,Bloodlust,Shaman,Rarity.FREE,5,0,0,Give your minions +3_Attack this turn.
		## "VAN_EX1_059","VAN_EX1_059",#(0)VAN_EX1_059,Crazed Alchemist,Neutral,Rarity.RARE,2,2,2,<b>Battlecry:</b> Swap the Attack and Health of a minion.
		"VAN_CS1_069","VAN_CS1_069",#(0)VAN_CS1_069,Fen Creeper,Neutral,Rarity.COMMON,5,3,6,<b>Taunt</b>
		"VAN_EX1_046","VAN_EX1_046",#(0)VAN_EX1_046,Dark Iron Dwarf,Neutral,Rarity.COMMON,4,4,4,<b>Battlecry:</b> Give a minion +2_Attack this turn.
		"VAN_CS2_187","VAN_CS2_187",#(1)VAN_CS2_187,Booty Bay Bodyguard,Neutral,Rarity.FREE,5,5,4,<b>Taunt</b>
		"VAN_EX1_010","VAN_EX1_010",#(1)VAN_EX1_010,Worgen Infiltrator,Neutral,Rarity.COMMON,1,2,1,<b>Stealth</b>
		## "VAN_EX1_002",#(1)VAN_EX1_002,The Black Knight,Neutral,Rarity.LEGENDARY,6,4,5,<b>Battlecry:</b> Destroy an enemy minion with <b>Taunt</b>.
		## "VAN_PRO_001",#(1)VAN_PRO_001,Elite Tauren Chieftain,Neutral,Rarity.LEGENDARY,5,5,5,<b>Battlecry:</b> Give both players the power to ROCK! (with a Power Chord card)
		"VAN_CS2_162","VAN_CS2_162",#(2)VAN_CS2_162,Lord of the Arena,Neutral,Rarity.FREE,6,6,5,<b>Taunt</b>
		"VAN_EX1_008","VAN_EX1_008",#(2)VAN_EX1_008,Argent Squire,Neutral,Rarity.COMMON,1,1,1,<b>Divine Shield</b>
		"VAN_EX1_590","VAN_EX1_590",#(2)VAN_EX1_590,Blood Knight,Neutral,Rarity.EPIC,3,3,3,<b>Battlecry:</b> All minions lose <b>Divine Shield</b>. Gain +3/+3 for each Shield lost.
		"VAN_CS2_037","VAN_CS2_037",#(2)VAN_CS2_037,Frost Shock,Shaman,Rarity.FREE,1,0,0,Deal $1 damage to an enemy character and <b>Freeze</b> it.
		"VAN_EX1_586","VAN_EX1_586",#(3)VAN_EX1_586,Sea Giant,Neutral,Rarity.EPIC,10,8,8,Costs (1) less for each other minion on the battlefield.
		"VAN_EX1_082","VAN_EX1_082",#(3)VAN_EX1_082,Mad Bomber,Neutral,Rarity.COMMON,2,3,2,<b>Battlecry:</b> Deal 3 damage randomly split between all other characters.
		"VAN_EX1_080","VAN_EX1_080",#(3)VAN_EX1_080,Secretkeeper,Neutral,Rarity.RARE,1,1,2,Whenever a <b>Secret</b> is played gain +1/+1.
		"VAN_NEW1_021","VAN_NEW1_021",#(3)VAN_NEW1_021,Doomsayer,Neutral,Rarity.EPIC,2,0,7,At the start of your turn destroy ALL minions.
		"VAN_EX1_058","VAN_EX1_058",#(4)VAN_EX1_058,Sunfury Protector,Neutral,Rarity.RARE,2,2,3,<b>Battlecry:</b> Give adjacent minions <b>Taunt</b>.
		"VAN_CS2_188","VAN_CS2_188",#(4)VAN_CS2_188,Abusive Sergeant,Neutral,Rarity.COMMON,1,2,1,<b>Battlecry:</b> Give a minion +2_Attack this turn.
		], "class":CardClass.SHAMAN}
	deckcatShaman50={"name":"deckcatShaman50","deck":[## Wins: 365 / 450 = 0.811111 (4)
		"VAN_CS2_125","VAN_CS2_125",#(0)VAN_CS2_125,Ironfur Grizzly,Neutral,Rarity.FREE,3,3,3,<b>Taunt</b>
		"VAN_EX1_259","VAN_EX1_259",#(0)VAN_EX1_259,Lightning Storm,Shaman,Rarity.RARE,3,0,0,Deal $2-$3 damage to all enemy minions. <b>Overload:</b> (2)
		"VAN_EX1_058","VAN_EX1_058",#(0)VAN_EX1_058,Sunfury Protector,Neutral,Rarity.RARE,2,2,3,<b>Battlecry:</b> Give adjacent minions <b>Taunt</b>.
		## "VAN_NEW1_021","VAN_NEW1_021",#(0)VAN_NEW1_021,Doomsayer,Neutral,Rarity.EPIC,2,0,7,At the start of your turn destroy ALL minions.
		## "VAN_CS2_201","VAN_CS2_201",#(1)VAN_CS2_201,Core Hound,Neutral,Rarity.FREE,7,9,5,
		"VAN_EX1_243","VAN_EX1_243",#(1)VAN_EX1_243,Dust Devil,Shaman,Rarity.COMMON,1,3,1,<b>Windfury</b>. <b>Overload:</b> (2)
		"VAN_EX1_508","VAN_EX1_508",#(1)VAN_EX1_508,Grimscale Oracle,Neutral,Rarity.FREE,1,1,1,ALL other Murlocs have +1 Attack.
		"VAN_EX1_080","VAN_EX1_080",#(1)VAN_EX1_080,Secretkeeper,Neutral,Rarity.RARE,1,1,2,Whenever a <b>Secret</b> is played gain +1/+1.
		"VAN_EX1_244","VAN_EX1_244",#(2)VAN_EX1_244,Totemic Might,Shaman,Rarity.FREE,0,0,0,Give your Totems +2_Health.
		"VAN_NEW1_016","VAN_NEW1_016",#(2)VAN_NEW1_016,Captain's Parrot,Neutral,Rarity.EPIC,2,1,1,<b>Battlecry:</b> Draw a Pirate from your deck.
		"VAN_CS2_041","VAN_CS2_041",#(2)VAN_CS2_041,Ancestral Healing,Shaman,Rarity.FREE,0,0,0,Restore a minionto full Health andgive it <b>Taunt</b>.
		"VAN_NEW1_027","VAN_NEW1_027",#(2)VAN_NEW1_027,Southsea Captain,Neutral,Rarity.EPIC,3,3,3,Your other Pirates have +1/+1.
		"VAN_CS1_042","VAN_CS1_042",#(3)VAN_CS1_042,Goldshire Footman,Neutral,Rarity.FREE,1,1,2,<b>Taunt</b>
		"VAN_NEW1_022","VAN_NEW1_022",#(3)VAN_NEW1_022,Dread Corsair,Neutral,Rarity.COMMON,4,3,3,<b>Taunt</b>Costs (1) less per Attack of_your weapon.
		"VAN_EX1_055","VAN_EX1_055",#(3)VAN_EX1_055,Mana Addict,Neutral,Rarity.RARE,2,1,3,Whenever you cast a spell gain +2 Attack this turn.
		"VAN_EX1_021","VAN_EX1_021",#(3)VAN_EX1_021,Thrallmar Farseer,Neutral,Rarity.COMMON,3,2,3,<b>Windfury</b>
		"VAN_EX1_004","VAN_EX1_004",#(4)VAN_EX1_004,Young Priestess,Neutral,Rarity.RARE,1,2,1,At the end of your turn give another random friendly minion +1 Health.
		], "class":CardClass.SHAMAN}
	deckcatShaman200={"name":"deckcatShaman200","deck":[## Wins: 1652 / 1800 = 0.917778 (3)
		"VAN_NEW1_023","VAN_NEW1_023",#(0)VAN_NEW1_023,Faerie Dragon,Neutral,Rarity.COMMON,2,3,2,Can't be targeted by spells or Hero Powers.
		"VAN_EX1_509","VAN_EX1_509",#(0)VAN_EX1_509,Murloc Tidecaller,Neutral,Rarity.RARE,1,1,2,Whenever a Murloc is summoned gain +1 Attack.
		"VAN_EX1_009","VAN_EX1_009",#(0)VAN_EX1_009,Angry Chicken,Neutral,Rarity.RARE,1,1,1,<b>Enrage:</b> +5 Attack.
		"VAN_EX1_096","VAN_EX1_096",#(0)VAN_EX1_096,Loot Hoarder,Neutral,Rarity.COMMON,2,2,1,<b>Deathrattle:</b> Draw a card.
		"VAN_EX1_062",#(1)VAN_EX1_062,Old Murk-Eye,Neutral,Rarity.LEGENDARY,4,2,4,<b>Charge</b>. Has +1 Attack for each other Murloc on the battlefield.
		"VAN_EX1_028","VAN_EX1_028",#(1)VAN_EX1_028,Stranglethorn Tiger,Neutral,Rarity.COMMON,5,5,5,<b>Stealth</b>
		"VAN_CS2_120","VAN_CS2_120",#(1)VAN_CS2_120,River Crocolisk,Neutral,Rarity.FREE,2,2,3,
		"VAN_CS2_189","VAN_CS2_189",#(1)VAN_CS2_189,Elven Archer,Neutral,Rarity.FREE,1,1,1,<b>Battlecry:</b> Deal 1 damage.
		"VAN_EX1_507","VAN_EX1_507",#(2)VAN_EX1_507,Murloc Warleader,Neutral,Rarity.EPIC,3,3,3,ALL other murlocs have +2/+1.
		"VAN_CS2_142","VAN_CS2_142",#(2)VAN_CS2_142,Kobold Geomancer,Neutral,Rarity.FREE,2,2,2,<b>Spell Damage +1</b>
		"VAN_CS2_045","VAN_CS2_045",#(2)VAN_CS2_045,Rockbiter Weapon,Shaman,Rarity.FREE,1,0,0,Give a friendly character +3 Attack this turn.
		"VAN_EX1_590","VAN_EX1_590",#(2)VAN_EX1_590,Blood Knight,Neutral,Rarity.EPIC,3,3,3,<b>Battlecry:</b> All minions lose <b>Divine Shield</b>. Gain +3/+3 for each Shield lost.
		"VAN_CS2_041","VAN_CS2_041",#(3)VAN_CS2_041,Ancestral Healing,Shaman,Rarity.FREE,0,0,0,Restore a minionto full Health andgive it <b>Taunt</b>.
		"VAN_EX1_080","VAN_EX1_080",#(3)VAN_EX1_080,Secretkeeper,Neutral,Rarity.RARE,1,1,2,Whenever a <b>Secret</b> is played gain +1/+1.
		"VAN_CS2_171","VAN_CS2_171",#(3)VAN_CS2_171,Stonetusk Boar,Neutral,Rarity.FREE,1,1,1,<b>Charge</b>
		"VAN_EX1_014",#(3)VAN_EX1_014,King Mukla,Neutral,Rarity.LEGENDARY,3,5,5,<b>Battlecry:</b> Give your opponent 2 Bananas.
		], "class":CardClass.SHAMAN}

	deckcatWarlock={"name":"deckcatWarlock","deck":[## Wins: 469 / 540 = 0.868519 (5)
		"VAN_EX1_309","VAN_EX1_309",#(0)VAN_EX1_309,Siphon Soul,Warlock,Rarity.RARE,6,0,0,Destroy a minion. Restore #3 Health to_your hero.
		"VAN_EX1_301","VAN_EX1_301",#(1)VAN_EX1_301,Felguard,Warlock,Rarity.RARE,3,3,5,<b>Taunt</b><b>Battlecry:</b> Destroy one of your Mana Crystals.
		## "VAN_PRO_001",#(1)VAN_PRO_001,Elite Tauren Chieftain,Neutral,Rarity.LEGENDARY,5,5,5,<b>Battlecry:</b> Give both players the power to ROCK! (with a Power Chord card)
		"VAN_EX1_093","VAN_EX1_093",#(2)VAN_EX1_093,Defender of Argus,Neutral,Rarity.RARE,4,2,3,<b>Battlecry:</b> Give adjacent minions +1/+1 and <b>Taunt</b>.
		## "VAN_NEW1_029",#(2)VAN_NEW1_029,Millhouse Manastorm,Neutral,Rarity.LEGENDARY,2,4,4,<b>Battlecry:</b> Enemy spells cost (0) next turn.
		"VAN_NEW1_019","VAN_NEW1_019",#(2)VAN_NEW1_019,Knife Juggler,Neutral,Rarity.RARE,2,3,2,[x]After you summon aminion deal 1 damageto a random enemy.
		"VAN_CS2_231","VAN_CS2_231",#(2)VAN_CS2_231,Wisp,Neutral,Rarity.COMMON,0,1,1,
		"VAN_EX1_319","VAN_EX1_319",#(3)VAN_EX1_319,Flame Imp,Warlock,Rarity.COMMON,1,3,2,<b>Battlecry:</b> Deal 3 damage to your hero.
		"VAN_EX1_032","VAN_EX1_032",#(3)VAN_EX1_032,Sunwalker,Neutral,Rarity.RARE,6,4,5,<b>Taunt</b><b>Divine Shield</b>
		"VAN_EX1_390","VAN_EX1_390",#(3)VAN_EX1_390,Tauren Warrior,Neutral,Rarity.COMMON,3,2,3,<b>Taunt</b>. <b>Enrage:</b> +3 Attack
		"VAN_EX1_048","VAN_EX1_048",#(3)VAN_EX1_048,Spellbreaker,Neutral,Rarity.COMMON,4,4,3,<b>Battlecry:</b> <b>Silence</b> a_minion.
		"VAN_EX1_306","VAN_EX1_306",#(4)VAN_EX1_306,Felstalker,Warlock,Rarity.FREE,2,4,3,<b>Battlecry:</b> Discard a random card.
		"VAN_EX1_019","VAN_EX1_019",#(4)VAN_EX1_019,Shattered Sun Cleric,Neutral,Rarity.FREE,3,3,2,<b>Battlecry:</b> Give a friendly minion +1/+1.
		"VAN_NEW1_023","VAN_NEW1_023",#(4)VAN_NEW1_023,Faerie Dragon,Neutral,Rarity.COMMON,2,3,2,Can't be targeted by spells or Hero Powers.
		"VAN_CS2_125","VAN_CS2_125",#(4)VAN_CS2_125,Ironfur Grizzly,Neutral,Rarity.FREE,3,3,3,<b>Taunt</b>
		"VAN_NEW1_025","VAN_NEW1_025",#(5)VAN_NEW1_025,Bloodsail Corsair,Neutral,Rarity.RARE,1,1,2,[x]<b>Battlecry:</b> Remove1 Durability from youropponent's weapon.
		"VAN_EX1_616","VAN_EX1_616",#(5)VAN_EX1_616,Mana Wraith,Neutral,Rarity.RARE,2,2,2,ALL minions cost (1) more.
		"VAN_NEW1_026","VAN_NEW1_026",#(5)VAN_NEW1_026,Violet Teacher,Neutral,Rarity.RARE,4,3,5,Whenever you cast a spell summon a 1/1 Violet Apprentice.
		], "class":CardClass.WARLOCK}
	deckcatWarrior={"name":"deckcatWarrior","deck":[## Wins: 459 / 540 = 0.850000 (4)
		## "VAN_EX1_284","VAN_EX1_284",#(0)VAN_EX1_284,Azure Drake,Neutral,Rarity.RARE,5,4,4,<b>Spell Damage +1</b><b>Battlecry:</b> Draw a card.
		"VAN_EX1_050","VAN_EX1_050",#(0)VAN_EX1_050,Coldlight Oracle,Neutral,Rarity.RARE,3,2,2,<b>Battlecry:</b> Each player draws 2 cards.
		## "VAN_EX1_583","VAN_EX1_583",#(0)VAN_EX1_583,Priestess of Elune,Neutral,Rarity.COMMON,6,5,4,<b>Battlecry:</b> Restore #4 Health to your hero.
		## "VAN_NEW1_041","VAN_NEW1_041",#(0)VAN_NEW1_041,Stampeding Kodo,Neutral,Rarity.RARE,5,3,5,<b>Battlecry:</b> Destroy a random enemy minion with 2 or less Attack.
		"VAN_EX1_004","VAN_EX1_004",#(1)VAN_EX1_004,Young Priestess,Neutral,Rarity.RARE,1,2,1,At the end of your turn give another random friendly minion +1 Health.
		"VAN_CS2_187","VAN_CS2_187",#(1)VAN_CS2_187,Booty Bay Bodyguard,Neutral,Rarity.FREE,5,5,4,<b>Taunt</b>
		"VAN_EX1_564","VAN_EX1_564",#(1)VAN_EX1_564,Faceless Manipulator,Neutral,Rarity.EPIC,5,3,3,<b>Battlecry:</b> Choose a minion and become a copy of it.
		"VAN_CS2_114","VAN_CS2_114",#(1)VAN_CS2_114,Cleave,Warrior,Rarity.FREE,2,0,0,[x]Deal $2 damage totwo random enemyminions.
		"VAN_EX1_062",#(2)VAN_EX1_062,Old Murk-Eye,Neutral,Rarity.LEGENDARY,4,2,4,<b>Charge</b>. Has +1 Attack for each other Murloc on the battlefield.
		"VAN_EX1_509","VAN_EX1_509",#(2)VAN_EX1_509,Murloc Tidecaller,Neutral,Rarity.RARE,1,1,2,Whenever a Murloc is summoned gain +1 Attack.
		"VAN_EX1_059","VAN_EX1_059",#(2)VAN_EX1_059,Crazed Alchemist,Neutral,Rarity.RARE,2,2,2,<b>Battlecry:</b> Swap the Attack and Health of a minion.
		"VAN_EX1_590","VAN_EX1_590",#(2)VAN_EX1_590,Blood Knight,Neutral,Rarity.EPIC,3,3,3,<b>Battlecry:</b> All minions lose <b>Divine Shield</b>. Gain +3/+3 for each Shield lost.
		"VAN_EX1_010","VAN_EX1_010",#(3)VAN_EX1_010,Worgen Infiltrator,Neutral,Rarity.COMMON,1,2,1,<b>Stealth</b>
		"VAN_EX1_507","VAN_EX1_507",#(3)VAN_EX1_507,Murloc Warleader,Neutral,Rarity.EPIC,3,3,3,ALL other murlocs have +2/+1.
		"VAN_NEW1_016","VAN_NEW1_016",#(3)VAN_NEW1_016,Captain's Parrot,Neutral,Rarity.EPIC,2,1,1,<b>Battlecry:</b> Draw a Pirate from your deck.
		"VAN_EX1_606","VAN_EX1_606",#(3)VAN_EX1_606,Shield Block,Warrior,Rarity.FREE,3,0,0,Gain 5 Armor.Draw a card.
		"VAN_CS1_042","VAN_CS1_042",#(4)VAN_CS1_042,Goldshire Footman,Neutral,Rarity.FREE,1,1,2,<b>Taunt</b>
		"VAN_EX1_019","VAN_EX1_019",#(4)VAN_EX1_019,Shattered Sun Cleric,Neutral,Rarity.FREE,3,3,2,<b>Battlecry:</b> Give a friendly minion +1/+1.
		"VAN_CS2_104",#(4)VAN_CS2_104,Rampage,Warrior,Rarity.COMMON,2,0,0,Give a damaged minion +3/+3.
		], "class":CardClass.WARRIOR}


	


