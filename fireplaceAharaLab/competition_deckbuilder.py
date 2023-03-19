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


######### entries (samples) ############



	



	def deckCatMain(repeat=0):
		sourceClass=CardClass.DRUID
		sourceClassName='DRUID'
		Vector1=StandardVectorAgent("Vector1",StandardVectorAgent.StandardStep1\
			,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
			,myClass=sourceClass)
		

		DruidRandom={"name":"DruidRandom", "deck":[], "class":CardClass.DRUID}
		HunterRandom={"name":"HunterRandom", "deck":[], "class":CardClass.HUNTER}
		MageRandom={"name":"MageRandom", "deck":[], "class":CardClass.MAGE}
		PaladinRandom={"name":"PaladinRandom", "deck":[], "class":CardClass.PALADIN}
		PriestRandom={"name":"PriestRandom", "deck":[], "class":CardClass.PRIEST}
		RogueRandom={"name":"RogueRandom", "deck":[], "class":CardClass.ROGUE}
		ShamanRandom={"name":"ShamanRandom", "deck":[], "class":CardClass.SHAMAN}
		WarlockRandom={"name":"WarlockRandom", "deck":[], "class":CardClass.WARLOCK}
		WarriorRandom={"name":"WarriorRandom", "deck":[], "class":CardClass.WARRIOR}

		#targetClasses=[deckcatDruid0, deckcatHunter0, deckcatMage0, deckcatPaladin0, deckcatPriest0, deckcatRogue0, deckcatShaman0, deckcatWarlock0, deckcatWarrior0]
		targetClasses=[DruidRandom, HunterRandom, MageRandom, PaladinRandom, PriestRandom, RogueRandom, ShamanRandom, WarlockRandom, WarriorRandom]
		#targetClasses=[CardClass.SHAMAN]
		targetClassName='N100k5ALL-0-%d'%(repeat)
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
					,myClass=myCardClass["class"],
					mulliganStrategy=StandardVectorAgent.StandardMulligan)
				for repeat in range(matchN):
					winner , mydict_thisplay = play_one_game(Vector1, Vector2, deck1=myDeck, deck2=myCardClass["deck"], debugLog=True)
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
			positiveblockdic=len([key for key, value in blockdic if value>0])
			blockdicthreshold=0
			if positiveblockdic==0:
				blockdicthreshold=-25
			elif positiveblockdic<5:
				blockdicthreshold=-15

			for key, value in blockdic:
				if blocklinecount>=5 or value<blockdicthreshold:
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


	
