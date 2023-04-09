from fireplace import cards
from fireplace.card import Card
from fireplace.config import Config
from fireplace.player import Player
from fireplace.utils import modify_description
from fireplace.dsl.selector import TARGET
#from fireplace.cards.battlegrounds import BG_hero1
import random
from hearthstone.enums import Zone,State, CardClass, CardType, GameTag, Race
from .BG_enums import MovePlay

class BG_Agent(object):
	""" class of agent for battlegrounds
	PLZ ingerit this class to build a new agent. """
	def __init__(self, myName: str, myOption: list, rating ,E = 0, heroChoiceStrategy=None, moveStrategy = None, choiceStrategy=None):
		self.name = myName
		self.option = myOption
		self.rating = rating = 1000
		self.E = E 
		self.heroChoiceStrategy = heroChoiceStrategy
		self.moveStrategy = moveStrategy
		self.choiceStrategy = choiceStrategy
		self.tavern_tierup_cost=5# -> player
		self.player = Player(myName, None, None)
		pass

	def __str__(self):
		return self.name

class BG_RandomAgent(BG_Agent):
	def __init__(self, myName: str, myOption = [], rating =1000 ):
		super().__init__(myName, myOption, rating, \
			heroChoiceStrategy=self.RandomHeroChoice, \
			moveStrategy=self.RandomMoveChoice )
		pass
	
	def RandomHeroChoice(self, heroes):
		return random.choice(heroes)

	def RandomMoveChoice(self, bar, candidates, controller, bartender):
		return random.choice(candidates)

class BG_NecoAgent(BG_Agent):
	def __init__(self, myName, myOption = [], rating =1000 ):
		super().__init__(myName, myOption, rating, \
			heroChoiceStrategy=self.NecoHeroChoice, \
			moveStrategy=self.NecoMoveChoice,
			choiceStrategy=self.NecoDiscoveryChoice)
		pass
	def getStats(self, card):
		if card.type==CardType.MINION:
			return card.atk+card.max_health
		else:
			return 10
	def NecoMoveChoice(self, bar, candidates, controller, bartender):
		if len(candidates)>0:
			choices=[]
			tier = controller.tavern_tier
			gold = controller.mana
			if (tier,gold) in [(1,4),(2,7),(3,9),(4,10),(5,10)]:
				for move in candidates:
					if move.move==MovePlay.TIERUP:
						return move
			if gold>=3:
				max_stats=0
				for move in candidates:
					if move.move==MovePlay.BUY:
						card = move.target
						if choices==[]:
							choices=[move]
							max_stats=self.getStats(move.target)
						elif self.getStats(card)>max_stats:
							choices=[move]
							max_stats=self.getStats(move.target)
						elif self.getStats(card)==max_stats:
							choices.append(move)
				if len(choices)>0:
					return random.choice(choices)
			if len(controller.field)<7 and len(controller.hand)>0:
				max_stats=0
				choices=[]
				for move in candidates:
					if move.move==MovePlay.PLAY:
						card = move.target
						if choices==[]:
							choices=[move]
							max_stats=self.getStats(move.target)
						elif self.getStats(card)>max_stats:
							choices=[move]
							max_stats=self.getStats(move.target)
						elif self.getStats(card)==max_stats:
							choices.append(move)
				if len(choices)>0:
					return random.choice(choices)
			if len(controller.field)==7 and len(controller.hand)>0:
				max_stats=999
				min_minion=None
				for card in controller.field:
					if max_stats>self.getStats(card):
						min_minion=card
						max_stats=self.getStats(card)
				for move in candidates:
					if move.move==MovePlay.BUY:
						card = move.target
						if self.getStats(card)>max_stats:
							choices=[move]
							max_stats=self.getStats(move.target)
						elif self.getStats(card)==max_stats:
							choices.append(move)
				if len(choices)>0:
					for choice in candidates:
						if choice.target==card and choice.move==MovePlay.SELL:
							return choice
			for choice in candidates:
				if choice.move==MovePlay.TURNEND:
					return choice
		return None

	def NecoHeroChoice(self, heroes):
		return random.choice(heroes)
	def NecoDiscoveryChoice(self, controller, choices):
		return random.choice(choices)


class BG_HumanAgent(BG_Agent):
	def __init__(self, myName, myOption = [], rating =1000 ):
		super().__init__(myName, myOption, rating, \
			heroChoiceStrategy=self.HumanHeroChoice, \
			moveStrategy = self.HumanMoveChoice,
			choiceStrategy = self.HumanDiscoveryChoice	   )
		pass
	def HumanMoveChoice(self, bar, candidates, controller, bartender):
		self.printBar(bar, controller, bartender)
		self.inputCandidates=[]
		self.moveDict={}
		count=0
		for move in candidates:
			if move.move==MovePlay.TURNEND:
				self.printMove(count, move)
				self.inputCandidates.append(count)
				self.moveDict[count]=move
		count=10
		for move in candidates:
			if move.move==MovePlay.BUY:
				self.printMove(count, move)
				self.inputCandidates.append(count)
				self.moveDict[count]=move
				count += 1
			if move.move==MovePlay.BUY_BUDDY:
				self.printMove(count, move)
				self.inputCandidates.append(count)
				self.moveDict[count]=move
		count=20
		for move in candidates:
			if move.move==MovePlay.SELL:
				self.printMove(count, move)
				self.inputCandidates.append(count)
				self.moveDict[count]=move
				count += 1
		count=30
		for move in candidates:
			if move.move==MovePlay.POWER:
				self.printMove(count, move)
				self.inputCandidates.append(count)
				self.moveDict[count]=move
				count += 1
		count=4
		for move in candidates:
			if move.move==MovePlay.TIERUP:
				self.printMove(count, move)
				self.inputCandidates.append(count)
				self.moveDict[count]=move
		count=5
		for move in candidates:
			if move.move==MovePlay.REROLE:
				self.printMove(count, move)
				self.inputCandidates.append(count)
				self.moveDict[count]=move
		count=6
		for move in candidates:
			if move.move==MovePlay.FREEZE:
				self.printMove(count, move)
				self.inputCandidates.append(count)
				self.moveDict[count]=move
		count=70
		for move in candidates:
			if move.move==MovePlay.PLAY:
				self.printMove(count, move)
				self.inputCandidates.append(count)
				self.moveDict[count]=move
				count += 1
		while True:
			try :
				print("choose from moves ->",end='')
				inputNum = int(input())
				if inputNum in self.inputCandidates:
					return self.moveDict[inputNum]
			except ValueError :
				pass
		pass
	def HumanHeroChoice(self, heroes):
		count=0
		for card in heroes:
			self.printHero(count, card)
			count += 1
		while True:
			try :
				print("->",end='')
				inputNum = int(input())
				if inputNum>=0 and inputNum<len(heroes):
					return heroes[inputNum]
			except ValueError :
				pass
	def printHero(self, count, cardID):
		card = cards.db[cardID]
		hpID=card.hero_power
		hp=cards.db[hpID]
		print("[%d] %s "%(count, card.name))
		print("HeroPower:%s"%(modify_description(hp,hp.description)))
		## before 23.2 (with buddy)
		if Config.BUDDY_SYSTEM or Config.NEW_BUDDY_SYSTEM:
			buddy_fid=card.tags.get(GameTag.BACON_COMPANION_ID, -1)
			buddy_card=[c for c in cards.db.values() if c.tags.get(9090, None)==buddy_fid]
			if len(buddy_card):
				buddy=buddy_card[0]
				print("Buddy:%s"%(modify_description(buddy,buddy.description)))
		pass
	def printMove(self, count, move):
		print("[%d] %s"%(count, move))
		pass

	raceName={
		Race.INVALID:'neutral',
		Race.MURLOC:'murloc',
		Race.DEMON:'demon',
		Race.MECHANICAL:'mechanical',
		Race.ELEMENTAL:'elemental',
		Race.BEAST:'beast',
		Race.PIRATE:'pirate',
		Race.DRAGON:'dragon',
		Race.ALL:'all',
		Race.QUILBOAR:'quilboar',
		Race.NAGA:'naga',
		Race.UNDEAD:'undead'
	}
	def printBar(self, bar, controller, bartender):
		print("----------------------------------------------")
		races = controller.game.parent.BG_races
		print("種族 : ", end="")
		for race in races:
			print("[%s]"%(race),end=' ')
		print("")
		gamemaster=bar.parent
		statstable=[]
		for b in gamemaster.BG_Bars:
			player = b.controller
			hero = player.hero
			heropower = hero.power
			herohealth = hero.health+hero.armor
			playertier = player.tavern_tier
			statstable.append([100-herohealth, herohealth, playertier, "(%s)[%s]%s"%(hero,player,modify_description(heropower,heropower.data.description))])
		statstable.sort( key=lambda b: b[0])
		for b in statstable:
			print("%d (*%d) %s"%(b[1],b[2],b[3]))
		print("----------------------------------------------")
		if controller.tavern_tier<6:
			print("グレード[%d], グレードアップコスト[%d], リロールコスト[%d], ゴールド[%d/%d] ターン[%d]"%(controller.tavern_tier, controller.tavern_tierup_cost, bar.reroleCost, controller.mana, controller.max_mana, bar.turn))
		else:
			print("グレード[%d], リロールコスト[%d], ゴールド[%d/%d] ターン[%d]"%(controller.tavern_tier, bar.reroleCost, controller.mana, controller.max_mana, bar.turn))
		print("ヒーロー：%s(%d + %d)"%(controller.hero, controller.hero.health, controller.hero.armor))
		if controller.hero.power.cant_play:
			print("パワー ：%s(unplayable) : %s"%(controller.hero.power, modify_description(controller.hero.power,controller.hero.power.data.description)))
		else:
			print("パワー ：%s(cost %d) : %s"%(controller.hero.power, controller.hero.power.cost, modify_description(controller.hero.power,controller.hero.power.data.description)))
		if controller.hero.power.id=='TB_BaconShop_HP_101':
			print ("ダークムーンチケット (%d/3)"%(controller.hero.power.sidequest_counter))
		if Config.BUDDY_SYSTEM: 
			buddy = controller.buddy_gauge
			if buddy>100:
				buddy = (buddy-100)*0.5
		elif Config.NEW_BUDDY_SYSTEM:
			if controller.got_buddy<2:
				print("バディ ：%s(%d) : %s"%(cards.db[controller.buddy_id].name, controller.buddy_gauge, modify_description(cards.db[controller.buddy_id], cards.db[controller.buddy_id].description)))
		print("----------------------------------------------")
		for card in bartender.field:
			print("Bar:(*%d)[%s]%s" %(card.tech_level, self.raceName[card.race], self.card_stats(card)))
		print("----------------------------------------------")
		for card in controller.field:
			print("Field : %s"%(self.card_stats(card)))
		for card in controller.secrets:
			print("Secret: %s"%(self.card_stats(card)))
		for card in controller.quests:
			print("Quest: %s"%(self.card_stats(card)))
		for card in controller.rewards:
			print("Reward: %s"%(self.card_stats(card)))
		print("----------------------------------------------")
		for card in controller.hand:
			print("Hand  : %s"%(self.card_stats(card)))
		print("----------------------------------------------")
		pass
	def HumanDiscoveryChoice(self, controller, choices):
		#return random.choice(choices)
		print("----------------------------------------------")
		count=0
		for choice in choices:
			#if choice.type!=CardType.HERO_POWER and  choice.requires_target() and len(choice.targets)>0:
			#	for target in choice.targets:
			#		self.printChoice(count, choice, target)
			#		count += 1
			#else:
			self.printChoice(count, choice)
			count += 1
		print("----------------------------------------------")
		while True:
			try :
				print("choose from choices ->",end='')
				inputNum = int(input())
				if inputNum>=0 and inputNum<len(choices):
					return choices[inputNum]
			except ValueError :
				pass
		pass
	def printChoice(self, count, choice, target=None):
		if hasattr(choice, 'quest') and len(choice.sidequest_list0)>0:
			print ("[%d] %s : [ %s ]"%(count, self.card_stats(choice), self.card_stats(choice.sidequest_list0[0])))
		elif target:
			print ("[%d] %s (target: %s) : %s"%(count, choice, target, choice.data.description.replace('\n','_')))
		else :
			print ("[%d] %s : %s"%(count, choice, choice.data.description.replace('\n','_')))
			count += 1
		pass

	def card_stats(self, card):
		ret = ' %s'%(card)
		if card.type == CardType.MINION:
			ret += '(%d/%d)'%(card.atk,card.health)
			if card.dormant:
				ret += "(dormant %d)"%(card.dormant)
			if card.BG_cost>0:
				ret += "(cost %d)"%(card.BG_cost)
			if card.cant_play:
				ret += "(can't play)"
			if card.frozen:
				ret += "(frozen)"
			if card.taunt:
				ret += "(taunt)"
			if card.divine_shield:
				ret += "(divine_shield)"
			if card.windfury>0:
				ret += "(windfury)"
			if card.reborn:
				ret += "(reborn)"
			if card.has_deathrattle:
				ret += "(deathrattle)"
			if card.darkmoon_ticket:
				ret += "(darkmoon ticket)"
		else:
			ret+=':'
		ret += modify_description(card, card.data.description)
		return ret

