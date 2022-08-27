#!/usr/bin/env python
import sys
from hearthstone.enums import *
from utils import *
from agent_Standard import *
from fireplace import cards
from fireplace.logging import log
from fireplace.config import Config

sys.path.append("..")

#
#		main()
#
def main():
	cards.db.initialize()
	#manual input(if you don't specify a class, it will be a hunter)
	Human1=HumanAgent("Human1",HumanAgent.HumanInput,myClass=CardClass.DRUID,
		choiceStrategy=HumanAgent.HumanInputChoice)
		# ,mulliganStrategy=HumanAgent.HumanInputMulligan)
	Human2=HumanAgent("Human2",HumanAgent.HumanInput,myClass=CardClass.WARRIOR)
	# random agent
	Random1=StandardAgent("Random1",StandardAgent.StandardRandom, myClass=CardClass.MAGE) 
	Random2=StandardAgent("Random2",StandardAgent.StandardRandom, myClass=CardClass.HUNTER) 

	#ベクトルプレーヤー。意外と強い。このプレーヤーとサシで勝負して勝てるくらいが一応の目安。
	Vector1=StandardVectorAgent("Vector1",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.PALADIN)
		#,mulliganStrategy=StandardVectorAgent.StandardMulligan) 
	Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.PRIEST)
		#,mulliganStrategy=StandardVectorAgent.StandardMulligan) 

	# Maya : モンテカルロによる読み切り
	#from agent_Maya import MayaAgent
	#Maya=MayaAgent("Maya",MayaAgent.Maya_MCTS,myClass=CardClass.MAGE)

	# Miyaryo
	# winner of the 1st competition of the fixed deck
	#from agent_Miyaryo import MiyaryoAgent
	#Miyaryo=MiyaryoAgent("Miyaryo",MiyaryoAgent.MiyaryoAI,myClass=CardClass.WARRIOR)

	# Takasho001
	#from agent_takasho001 import takasho001Agent
	#takasho001=takasho001Agent("Takasho",takasho001Agent.takashoAI)

	# 言葉で戦略を組み立てるエージェント by Ahara
	#from agent_word_strategy import WordStrategyAgent
	#WordStrategy = WordStrategyAgent("WS", WordStrategyAgent.agent_word_strategy\
	#	,myOption=[WS.ミニョンで敵ヒーローの体力を削る, WS.呪文を使えるなら呪文, WS.ランダムにプレー]\
	#	,myClass=CardClass.PRIEST)

	#from agent_Test import TestHumanAgent
	#TestHuman=TestHumanAgent("TestHuman",TestHumanAgent.HumanInput,myClass=CardClass.DRUID,choiceStrategy=TestHumanAgent.HumanInputChoice)

	#HunterCat : faceHunter専用のエージェント
	#from agent_HunterCat import HunterCatAgent
	#HunterCat=HunterCatAgent("HunterCat", HunterCatAgent.HunterCatAI)

	####################################################################

	#ゲームプレイ(きまったゲーム数を対戦し、勝ち数を数える)
	#from utils import BigDeck
	##BigDeck.faceHunter, BigDeck.clownDruid, BigDeck.bigWarrior
	a,b,c = play_set_of_games(Vector1, Vector2, deck1=[], deck2=[], gameNumber=10, debugLog=True)
	#a,b,c = play_set_of_games(Human1, Human2, deck1=[], deck2=[],gameNumber=1, debugLog=True,)# P1MAXMANA=10, P2MAXMANA=10)
	#デッキを固定しての総当たり戦
	#デッキ種類は関数内で設定
	#レーティングを表示する。
	#from competition import play_round_robin_competition
	#play_round_robin_competition([Random,Vector,AngryCat,HunterCat],matchNumber=1)

	#特定の2枚のカードのシナジーを調べる(idea by Maya)
	#from card_pair import investigate_card_pair, find_card_pair
	#investigate_card_pair()
	#シナジーのあるカードの組を漠然と探す
	#find_card_pair(1)
	#print("test_branch_yamadamaya")
	pass

def printClasses():
	from hearthstone import cardxml
	myCardSet=CardSet.STORMWIND#STORMWIND#ALTERAC_VALLEY#THE_SUNKEN_CITY#REVENDRETH#VANILLA
	myCardClass=CardClass.WARLOCK##DEMONHUNTER,DRUID,HUNTER,MAGE,NEUTRAL,PALADIN,PRIEST,ROGUE,SHAMAN,WARLOCK,WARRIOR
	setText={
		CardSet.VANILLA:'Classic_',
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
	f.write('from hearthstone.enums import Zone, CardType, Rarity\n\n')
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
	#from hearthstone import cardxml
	from importlib import import_module
	from fireplace.cards.cardlist import All
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
	from hearthstone import cardxml
	from fireplace.cards.cardlist import All
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
	typ = [('テキストファイル','*.txt')] 
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

def card_test():
	from card_test.stormwind_rogue import stormwind_rogue
	stormwind_rogue()
	pass

def battleground_main():
	from fireplace.battlegrounds.BG_utils import  BG_main
	BG=BG_main()
	BG.BG_main()

if __name__ == "__main__":
	if Config.HEARTHSTONE:
		main()
	elif Config.BATTLEGROUNDS:
		battleground_main()
	elif Config.CARDTEST:
		card_test()
	elif Config.CARDCLASS:
		printClasses()
	
