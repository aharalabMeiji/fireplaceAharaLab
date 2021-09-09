from hearthstone.enums import *
from hearthstone import cardxml
#from fireplace import cards

testFile = [
'### ピエロドルイド',
'# Class: Druid',
'# Format: Standard',
'# Year of the Gryphon',
'#',
'# 2x (0) Innervate',
'# 2x (0) Lightning Bloom',
'# 2x (1) Animated Broomstick',
'# 2x (1) Nature Studies',
'# 2x (2) Guess the Weight',
'# 2x (3) Wild Growth',
'# 2x (4) Overgrowth',
'# 1x (4) Thickhide Kodo',
'# 2x (5) Lake Thresher',
'# 2x (5) Twilight Runner',
'# 2x (7) Strongman',
'# 2x (8) Guardian Animals',
'# 2x (8) Primordial Protector',
'# 2x (9) Carnival Clown',
'# 2x (10) Survival of the Fittest',
"# 1x (10) Y'Shaarj, the Defiler",
'# ',
'AAECAe2/BAL83gO17AMO6LoDlc0Dm84DutADvNADk9ED3tED8NQD/tsD0eED5uED3uwDiZ8Erp8EAA==',
'# ',
'# To use this deck, copy it to your clipboard and create a new deck in Hearthstone',
	]

def match(id):
	number = ['0','1','2','3','4','5','6','7','8','9']
	head = ['COR','BT_','SCH','DMF','YOP','BAR','WC_','SW_',]
	a1=id[-3]
	a2=id[-2]
	a3=id[-1]
	b=id[:3]
	if not a1 in number:
		return False
	if not a2 in number:
		return False
	if not a3 in number:
		return False
	if b in head:
		return True
	return False

def readFile():
	output = ""
	db, xml = cardxml.load(locale="enUS")
	for line in testFile:
		if line[:3]=="###":
			deckName = line[4:]
			output = deckName+"=["
		elif line[:8]=="# Class:":
			deckClass = line[9:]
			output = output + "#" + deckClass + "\n"
		elif line[:4] == "# 1x":
			if line[8]==" ":
				cardName=line[9:]
			else: #line[9]==" ":
				cardName=line[10:]
			for id in db.keys():
				card = db[id]
				if card.name == cardName and match(id):
					output += ("'"+card.id+"',")
		elif line[:4] == "# 2x":
			if line[8]==" ":
				cardName=line[9:]
			else: #line[9]==" ":
				cardName=line[10:]
			for id in db.keys():
				card = db[id]
				if card.name == cardName and match(id):
					output = output + "'"+id+"','"+id+"',"
					break
	output = output + "]"
	print ("%s"%output)
	return output

	
#def printClasses():
#	print('')
#	print('from ..utils import *')
#	print('')
#	_cardList = []
#	for _id in cards.db.keys():
#		_card = cards.db[_id]
#		if _card.card_set== CardSet.CORE:
#			if _card.card_class == CardClass.DEMONHUNTER: 
#				_cardList.append(_card.id)
#				print('class %s:# <%d>[%d]'%(_card.id, _card.card_class, _card.card_set))
#				print('    """ %s'%(_card.name))
#				print('    %s """'%(_card.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
#				print('    #'%())
#				print('    pass'%())
#				print(''%())

#def printListOfCards():
#	print('Stormwind_Mage=',end='[')#   Neutral   Hunter   Mage
#	for _id in cards.db.keys():
#		_card = cards.db[_id]
#		if _card.card_set== CardSet.HERO_SKINS:
#		#	if _card.card_class == CardClass.MAGE: 
#				print("'%s'"%(_card.id), end=",")
#	print(']')

def deckCode():
	#printClasses()
	#printListOfCards()
	readFile()
	pass

ピエロドルイド=[#Druid
'CORE_EX1_169','CORE_EX1_169','SCH_427','SCH_427','SCH_311','SCH_311',
'SCH_333','SCH_333','DMF_075','DMF_075','CORE_CS2_013','CORE_CS2_013',
'BT_130','BT_130','BAR_535','SCH_605','SCH_605','SCH_616',
'SCH_616','DMF_078','DMF_078','SCH_610','SCH_610','BAR_042',
'BAR_042','DMF_163','DMF_163','SCH_609','SCH_609','DMF_188',]



