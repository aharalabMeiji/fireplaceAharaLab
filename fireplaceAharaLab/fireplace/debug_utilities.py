from hearthstone.enums import CardSet, CardClass, SpellSchool, GameTag, CardType
from hearthstone import cardxml
from .cards.cardlist import All

def printClasses():
	from hearthstone import cardxml
	myCardSet=CardSet.THE_SUNKEN_CITY#STORMWIND#ALTERAC_VALLEY#THE_SUNKEN_CITY#REVENDRETH#VANILLA
	myCardClass=CardClass.WARLOCK##DEMONHUNTER,DRUID,HUNTER,MAGE,NEUTRAL,PALADIN,PRIEST,ROGUE,SHAMAN,WARLOCK,WARRIOR
	setText={
		CardSet.VANILLA:'Classic_',
		CardSet.THE_BARRENS:'Barrens_',
		CardSet.STORMWIND:'StormWind_',
		CardSet.ALTERAC_VALLEY:'Alterac_',
		CardSet.THE_SUNKEN_CITY:'Sunken_',
		CardSet.REVENDRETH:'Revendreth_',
		}
	classText={
		CardClass.DEMONHUNTER:'DemonHunter',
		CardClass.DRUID:'Druid',
		CardClass.HUNTER:'Hunter',
		CardClass.MAGE:'Mage',
		CardClass.NEUTRAL:'Neutral',
		CardClass.PALADIN:'Paladin',
		CardClass.PRIEST:'Priest',
		CardClass.ROGUE:'Rogue',
		CardClass.SHAMAN:'Shaman',
		CardClass.WARLOCK:'Warlock',
		CardClass.WARRIOR:'Warrior',
		}
	mySetText=setText[myCardSet]
	myClassText=classText[myCardClass]
	mySetClass=mySetText+myClassText
	filename=mySetClass.lower()
	f = open("%s.py"%filename, 'w')
	f.write('from ..utils import *\n')
	f.write('\n')
	f.write ("%s=[]\n\n"%(mySetClass))
	db, xml = cardxml.load(locale='enUS')
	keyID='XXX_000'
	for _id in db.keys():
		_card = db[_id]
		if _card.card_set== myCardSet and _card.card_class == myCardClass: 
			if not keyID in _card.id:
				f.write("%s%s=True\n"%(mySetText,_card.name.replace(' ','_').replace('-','_').replace("'",'').replace(':','').replace('!','').replace('=','')))
				keyID=_card.id
		pass
	pass
	f.write('\n'%())
	f.write('\n'%())
	keyID='XXX_000'
	for _id in db.keys():
		_card = db[_id]
		if _card.card_set== myCardSet and _card.card_class == myCardClass: 
			if not keyID in _card.id:
				f.write('if %s%s:# \n'%(mySetText,_card.name.replace(' ','_').replace('-','_').replace("'",'').replace(':','').replace('!','').replace('=','')))
				keyID=_card.id		
			f.write("\t%s+=['%s']\n"%(mySetClass, _card.id))
			f.write('class %s:# <%d>[%d]\n'%(_card.id, _card.card_class, _card.card_set))
			f.write('\t""" %s\n'%(_card.name))
			f.write('\t%s """\n'%(_card.description.replace('\n',' ').replace('[x]','').replace('<b>','[').replace('</b>',']')))
			f.write('\t#\n'%())
			f.write('\tpass\n'%())
			f.write('\n'%())
		pass
	f.close()
	f = open("t_%s.py"%filename, 'w')
	f.write('from .simulate_game import Preset_Play,PresetGame\n')
	f.write('from fireplace.actions import Hit, Summon, Give\n')
	f.write('from hearthstone.enums import CardClass, Zone, CardType, Rarity\n\n')
	f.write ("def %s():\n\n"%(filename))
	db, xml = cardxml.load(locale='enUS')
	keyID='XXX_000'
	for _id in db.keys():
		_card = db[_id]
		if _card.card_set== myCardSet and _card.card_class == myCardClass: 
			if not keyID in _card.id:
				f.write("\t#PresetGame(pp_%s)##\n"%(_card.id))
				keyID=_card.id
		pass
	pass
	f.write('\tpass\n'%())	
	f.write('\n'%())
	f.write('\n'%())
	keyID='XXX_000'
	for _id in db.keys():
		_card = db[_id]
		if _card.card_set== myCardSet and _card.card_class == myCardClass: 
			if not keyID in _card.id:
				keyID=_card.id		
				f.write('##########%s##########\n\n'%(_card.id))
				f.write('class pp_%s(Preset_Play):\n'%(_card.id))
				f.write('\t""" %s\n'%(_card.name))
				f.write('\t%s """\n'%(_card.description.replace('\n',' ').replace('[x]','').replace  ('<b>','[').replace('</b>',']')))
				f.write('\tclass1=%s\n'%(myCardClass))
				f.write('\tclass2=%s\n'%(myCardClass))
				f.write('\tdef preset_deck(self):\n')
				f.write('\t\tself.con1=self.exchange_card("%s", self.controller)\n'%(_card.id))
				f.write('\t\tself.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)\n'%())
				f.write('\t\tself.con4=self.con4[0][0]\n'%())
				f.write('\t\tself.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)\n'%())
				f.write('\t\tself.opp1=self.opp1[0][0]\n'%())
				f.write('\t\tsuper().preset_deck()\n'%())
				f.write('\t\tpass\n'%())
				f.write('\tdef preset_play(self):\n'%())
				f.write('\t\tsuper().preset_play()\n'%())
				f.write('\t\t### con\n'%())
				f.write('\t\tself.play_card(self.con1)\n'%())
				f.write('\t\tself.change_turn()\n'%())
				f.write('\t\t### opp\n'%())
				f.write('\t\tself.change_turn()\n'%())
				f.write('\t\tpass\n'%())
				f.write('\tdef result_inspection(self):\n'%())
				f.write('\t\tsuper().result_inspection()\n'%())
				f.write('\t\tfor card in self.controller.hand:\n'%())
				f.write('\t\t\tself.print_stats("hand", card)\n'%())
				f.write('\tpass\n\n'%())
				f.write('\n'%())
		pass
	f.close()
	pass

def printMissedCards():
	from importlib import import_module
	CARD_SETS=['core','hero_dream','aoo','scholo','darkmoon','barrens','stormwind','faceHunter','clownDruid','bigWarrior',]
	for cardIDlist in All:
		for id in cardIDlist:
			#card = cardxml.CardXML(id)
			ok=False
			for cardset in CARD_SETS:
				module = import_module("fireplace.cards.%s" % (cardset))
				if hasattr(module, id):
					ok=True
					break
			if not ok:
				print("%s"%(id))
		pass
	pass

def printCards():
	CARD_SETS=['core','hero_dream','aoo','scholo','darkmoon','barrens','stormwind','faceHunter','clownDruid','bigWarrior',]
	myCardSchool=SpellSchool.NATURE
	myCardSet=CardSet.STORMWIND
	myCardClass=CardClass.NEUTRAL
	print('#%s_%s='%(myCardSet,myCardClass),end='[')#
	db, xml = cardxml.load(locale='enUS')
	for cardIDlist in All:
		for id in cardIDlist:
			card = db[id]
			tag = card.tags.get(GameTag.CARDRACE)
			if card.tags.get(GameTag.CARDTYPE)==CardType.MINION and card.tags.get(GameTag.TAUNT,0)!=0: #tag == Race.ELEMENTAL:#card.card_set== myCardSet and card.card_class == myCardClass: 
				print("'%s'"%(card.id), end=",")
			pass
		pass
	pass
	print(']')

def print_deck():
	from tkinter import filedialog
	from hearthstone import cardxml
	db, xml = cardxml.load(locale='jaJP')
	typ = [('textfile','*.txt')] 
	dir = 'D:\\'
	fle = filedialog.askopenfilename(filetypes = typ, initialdir = dir) 
	try:
		f = open(fle, 'r')
		datalist = f.readlines()
		print("[",end='')
		for line in datalist:
			if len(line)>10:
				number = line[2:4]
				if number == '1x':
					name = line[9:-1]
					for id in db.keys():
						card = db[id]
						if card.name == name: 
							print("'%s'"%(card.id), end=",")
							break
						pass
					pass
				elif number == '2x':
					name = line[9:-1]
					for id in db.keys():
						card = db[id]
						if card.name == name: 
							print("'%s'"%(card.id), end=",")
							print("'%s'"%(card.id), end=",")
							break
						pass
					pass
				pass
		f.close()
		print("]")
	except FileNotFoundError:
		pass


