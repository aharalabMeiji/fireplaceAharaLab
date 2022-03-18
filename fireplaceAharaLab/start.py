#!/usr/bin/env python
import sys
from hearthstone.enums import *
from agent_HappyCat import HappyCat
from utils import *
from agent_Standard import *
from fireplace import cards
from fireplace.logging import log

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
		,myClass=CardClass.DRUID)
		#,mulliganStrategy=StandardVectorAgent.StandardMulligan) 
	Vector2=StandardVectorAgent("Vector2",StandardVectorAgent.StandardStep1\
		,myOption=[3,1,4,1,5,9,2,6,5,3,5,8,9,7,9,3,2,3,8,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8]\
		,myClass=CardClass.MAGE)
		#,mulliganStrategy=StandardVectorAgent.StandardMulligan) 

	#HappyCatAgent
	from agent_HappyCat import HappyCatAgent
	HappyCat = HappyCatAgent("HappyCat", HappyCatAgent.HappyCatAI)

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
	a,b,c = play_set_of_games(Vector1, HappyCat, deck1=[], deck2=[], gameNumber=1, debugLog=True)
	#a,b,c = play_set_of_games(Human1, Human2, deck1=[], deck2=[],gameNumber=1, debugLog=True,)# P1MAXMANA=10, P2MAXMANA=10)
	#デッキを固定しての総当たり戦
	#デッキ種類は関数内で設定
	#レーティングを表示する。
	from competition import play_round_robin_competition
	#play_round_robin_competition([Random,Vector,AngryCat,HunterCat],matchNumber=1)
	#play_round_robin_competition([Random1,Vector1,Vector2],matchNumber=1)

	#特定の2枚のカードのシナジーを調べる(idea by Maya)
	#from card_pair import investigate_card_pair, find_card_pair
	#investigate_card_pair()
	#シナジーのあるカードの組を漠然と探す
	#find_card_pair(1)
	#print("test_branch_yamadamaya")
	pass

def printClasses():
	from hearthstone import cardxml
	print('')
	print('from ..utils import *')
	print('')
	myCardSet=CardSet.STORMWIND
	myCardClass=CardClass.NEUTRAL
	print('#%s_%s='%(myCardSet,myCardClass),end='[')#
	db, xml = cardxml.load(locale='enUS')
	for _id in db.keys():
		_card = db[_id]
		if _card.card_set== myCardSet and _card.card_class == myCardClass: 
			print("'%s'"%(_card.id), end=",")
		pass
	pass
	print(']')
	for _id in db.keys():
		_card = db[_id]
		if _card.card_set== myCardSet and _card.card_class == myCardClass: 
			print('class %s:# <%d>[%d]'%(_card.id, _card.card_class, _card.card_set))
			print('\t""" %s'%(_card.name))
			print('\t%s """'%(_card.description.replace('\n','').replace('[x]','').replace('<b>','[').replace('</b>',']')))
			print('\t#'%())
			print('\tpass'%())
			print(''%())
		pass
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

if __name__ == "__main__":
	#from card_test.scholo_mage import SimulateGames_Scholo_Mage
	#SimulateGames_Scholo_Mage()
	main()
