from fireplace import cards
from fireplace.game import Game
from fireplace.card import Card
from fireplace.actions import *
from fireplace.player import Player
import random
from hearthstone.enums import Zone, State, Race


from .BG_agent import BG_HumanAgent,BG_NecoAgent,BG_RandomAgent
from .BG_bar import BG_Bar
from .BG_battle import BG_Battle
from .BG_enums import MovePlay

from fireplace.config import Config

BobsFieldSize={1:3, 2:4, 3:4, 4:5, 5:5, 6:6}

BG_Exclude_Hero=[
	'TB_BaconShop_HERO_56',#2 dragon ban
	'BG22_HERO_001',#6 X
	'TB_BaconShop_HERO_29',#7 X
	'TB_BaconShop_HERO_64',#8 X
	'TB_BaconShop_HERO_67',#9 X
	'TB_BaconShop_HERO_78',#11 X elemental ban
	'BG21_HERO_020',#12 X
	'BG20_HERO_103',#14 X
	'TB_BaconShop_HERO_52',#15 X
	'TB_BaconShop_HERO_43',#16 X

	'BG22_HERO_002',#17 X
	'TB_BaconShop_HERO_01',#18 X
	'TB_BaconShop_HERO_42',#19 X
	'TB_BaconShop_HERO_74',#20 X
	'TB_BaconShop_HERO_55',#21 X Murloc ban
	'TB_BaconShop_HERO_02',#22 X
	'BG20_HERO_283',#23 X
	'TB_BaconShop_HERO_15',#24 X
	'TB_BaconShop_HERO_95',#25 X
	'BG20_HERO_242',#26 X
	'TB_BaconShop_HERO_08',#27 X
	'TB_BaconShop_HERO_28',#28 X
	'TB_BaconShop_HERO_71',#29 X
	'TB_BaconShop_HERO_60',#30 X
	'TB_BaconShop_HERO_38',#31 X
	'BG20_HERO_280',#32 X
	'TB_BaconShop_HERO_25',#33 X
	'TB_BaconShop_HERO_72',#34 X
	
	'TB_BaconShop_HERO_37',#35 demon ban
	'BG20_HERO_202',#38 X
	'TB_BaconShop_HERO_17',#40 mech ban
	'TB_BaconShop_HERO_70',#41 X 
	'BG20_HERO_301',#42 X
	'TB_BaconShop_HERO_93',#43 X
	'TB_BaconShop_HERO_57',#44 X
	'BG22_HERO_305',#45 X
	'BG20_HERO_102',#46 X
	'TB_BaconShop_HERO_18',#47 X
	'TB_BaconShop_HERO_34',#48 X pirate ban
	'TB_BaconShop_HERO_39',#49 X
	'TB_BaconShop_HERO_14',#50 X
	'TB_BaconShop_HERO_11',#51 X

	'TB_BaconShop_HERO_23',#56 XX

	'TB_BaconShop_HERO_94',#69 XX
	'TB_BaconShop_HERO_53',#77 dragon ban
	]

class BG_main:
	def __init__(self):
		#使用カードの初期化
		cards.db.BG_initialize()
		#エージェントのリスト
		if Config.HUMAN_PLAY:
			self.Agents=[
			BG_HumanAgent("Human1"),
			BG_NecoAgent("Neco2"),
			BG_NecoAgent("Random3"),
			BG_NecoAgent("Random4")
			]
		else:
			self.Agents=[
			BG_NecoAgent("Neco1"),
			BG_NecoAgent("Neco2"),
			BG_NecoAgent("Random3"),
			BG_NecoAgent("Random4")
			]
		# ヒーローセット
		self.Heroes = cards.battlegrounds.BG_hero1.BG_PoolSet_Hero1
		self.Heroes += cards.battlegrounds.BG_hero2.BG_PoolSet_Hero2
		self.Heroes += cards.battlegrounds.BG_hero3.BG_PoolSet_Hero3
		self.Heroes += cards.battlegrounds.BG_hero4.BG_PoolSet_Hero4
		self.Heroes += cards.battlegrounds.BG_hero5.BG_PoolSet_Hero5
		# デッキを作る新しいゲームの始まり。
		self.BG_decks=[[],[],[],[],[],[],[]]
		if Config.RANDOM_RACE:
			# BAN される raceはここで除外
			if Config.PATCH23_2_2:
				self.BG_races = races = ['naga',] + random.sample(['beast','demon','dragon','elemental','mecha','murloc', 'pirate','quilboar'],4)
			else:
				self.BG_races = races = random.sample(['beast','demon','dragon','elemental','mecha','murloc','pirate','quilboar'],5)
		else:
			# 特定の種族のみを指定(config.py内で指定)
			self.BG_races = races=Config.RACE_CHOICE
		for i in range(6):
			if i<5:
				rep=8
			else:
				rep=4
			for repeat in range(rep):	
				self.BG_decks[i+1] += cards.battlegrounds.BG_minion.BG_PoolSet_Minion[i]
				if 'beast' in races:
					self.BG_decks[i+1] += cards.battlegrounds.BG_minion_beast.BG_PoolSet_Beast[i]
				if 'demon' in races:
					self.BG_decks[i+1] += cards.battlegrounds.BG_minion_demon.BG_PoolSet_Demon[i]
				if 'dragon' in races:
					self.BG_decks[i+1] += cards.battlegrounds.BG_minion_dragon.BG_PoolSet_Dragon[i]
				if 'elemental' in races:
					self.BG_decks[i+1] += cards.battlegrounds.BG_minion_elemental.BG_PoolSet_Elemental[i]
				if 'mecha' in races:
					self.BG_decks[i+1] += cards.battlegrounds.BG_minion_mecha.BG_PoolSet_Mecha[i]
				if 'murloc' in races:
					self.BG_decks[i+1] += cards.battlegrounds.BG_minion_murloc.BG_PoolSet_Murloc[i]
				if 'naga' in races:
					self.BG_decks[i+1] += cards.battlegrounds.BG_minion_naga.BG_PoolSet_Naga[i]
				if 'pirate' in races:
					self.BG_decks[i+1] += cards.battlegrounds.BG_minion_pirate.BG_PoolSet_Pirate[i]
				if 'quilboar' in races:
					self.BG_decks[i+1] += cards.battlegrounds.BG_minion_quilboar.BG_PoolSet_Quilboar[i]
		self.BG_Bars=[]
		self.BG_Gold=cards.battlegrounds.BG_minion.BG_Minon_Gold
		self.BG_Gold.update(cards.battlegrounds.BG_minion_beast.BG_Beast_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_minion_demon.BG_Demon_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_minion_dragon.BG_Dragon_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_minion_elemental.BG_Elemental_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_minion_mecha.BG_Mecha_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_minion_naga.BG_Naga_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_minion_murloc.BG_Murloc_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_minion_pirate.BG_Pirate_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_minion_quilboar.BG_Quilboar_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_hero1.BG_Hero1_Buddy_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_hero2.BG_Hero2_Buddy_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_hero3.BG_Hero3_Buddy_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_hero4.BG_Hero4_Buddy_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_hero5.BG_Hero5_Buddy_Gold)

		self.BG_Hero_Buddy=cards.battlegrounds.BG_hero1.BG_Hero1_Buddy
		self.BG_Hero_Buddy.update(cards.battlegrounds.BG_hero2.BG_Hero2_Buddy)
		self.BG_Hero_Buddy.update(cards.battlegrounds.BG_hero3.BG_Hero3_Buddy)
		self.BG_Hero_Buddy.update(cards.battlegrounds.BG_hero4.BG_Hero4_Buddy)
		self.BG_Hero_Buddy.update(cards.battlegrounds.BG_hero5.BG_Hero5_Buddy)
		self.prevMatches=[[0,1],[2,3]]# previous combination
		self.matches=[[0,1],[2,3]]
	pass

	def BG_main(self):
		# each agent chooses heroes 
		for agent in self.Agents:
			if Config.LOGINFO:
				print ("==== %s 's bar building ===="% agent)
			if agent.name=='Human1':
				theHeroes = [self.Heroes[Config.HERO_1],self.Heroes[Config.HERO_2]]
			else:
				theHeroes = random.sample(self.Heroes, 2)
			self.Heroes.remove(theHeroes[0])
			self.Heroes.remove(theHeroes[1])
			theHero = agent.heroChoiceStrategy(theHeroes)
			#heroCard=Card(theHero)
			thePlayer = Player(agent.name, self.BG_decks[1], theHero)#
			# building a Tavern
			bar = BG_Bar(thePlayer)
			bar.BG_setup()
			bar.player1 = bar.current_player = bar.controller
			bar.player1.buddy_gauge = 0
			bar.player2 = bar.bartender
			bar.turn=1
			bar.parent = self
			bar.player1.parent_agent = agent
			bar.player1.choiceStrategy = agent.choiceStrategy
			self.BG_Bars.append(bar)
			########## FOR DEBUGGIN! Default dealing a specific card
			if Config.CARD_PRESET:
				if agent.name=='Human1':
					if Config.CARD_PRESET1!= '':
						card = bar.controller.card(Config.CARD_PRESET1)
						card.zone = Zone.HAND
					if Config.CARD_PRESET2!= '':
						card = bar.controller.card(Config.CARD_PRESET2)
						card.zone = Zone.HAND
			##########
			if bar.player1.hero.power.id=='TB_BaconShop_HP_054': #Millhouse flag
				bar.player1.tavern_tierup_cost += 1
				bar.reroleCost=2
				bar.minionCost=2
			BeginGame(bar.controller).trigger(bar.controller)
			if Config.LOGINFO:
				print ("==== %s 's bar done ===="% agent)
			pass
		self.prevMatches=[[0,1],[2,3]]# previous combination
		# Start game
		while True:	
			### randomize the combinations(now fixed)
			self.matches=[[0,1],[2,3]]#
			#in tha final, battles lengtha will be 4 
			battles = [None,None]
			### Agent moves start
			for bar in self.BG_Bars:
				controller = bar.controller
				print ("==== %s 's thinkng ===="% controller)
				controller.game = bar
				bartender = bar.bartender
				bar.current_player=controller
				agent = controller.parent_agent
				assert agent
				#if Aranna-flag, 
				if controller.hero.power.id!='TB_BaconShop_HP_065t2':
					bartender.len_bobs_field=BobsFieldSize[controller.tavern_tier]
				else:
					bartender.len_bobs_field=7
				controller.max_mana = min(10,bar.turn+2)
				controller.used_mana = 0
				if controller.hero.power.id=='TB_BaconShop_HP_008':
					controller.used_mana = -controller.sells_in_this_turn
				controller.sells_in_this_turn=0
				### deal cards to tavern
				frozencard=0
				for card in reversed(bartender.field):
					if Config.LOGINFO:
						print("(BG_MainBG_Main)field card %s is removed."%(card))
					if not card.frozen and not card.dormant>0:
						self.ReturnCard(card)
					else:
						card.frozen=False
						frozencard += 1
				for repeat in range(bartender.len_bobs_field-frozencard):
					card = self.DealCard(bartender, controller.tavern_tier)
					if controller.hero.power.id=='TB_BaconShop_HP_101':### Silas-flag
						if random.choice([0,1]):
							card.darkmoon_ticket = True
				#start bob's tavern
				BeginBar(controller, bar.turn).trigger(controller)
				if controller.hero.power:
					controller.hero.power.activations_this_turn = 0
				controller.spentmoney_in_this_turn=0
				controller.once_per_turn=0
				# in this timing, some choice may occer.
				choiceAction(controller)
				while True:
					##### get a list of all moves
					candidates = GetMoveCandidates(bar, controller, bartender)
					##### each agent choose a move
					choice = agent.moveStrategy(bar, candidates, controller, bartender)
					if choice.move==MovePlay.TURNEND:#### if the move is 'turnend' then turn to the battle
						bar.no_drawing_at_turn_begin=True
						for card in controller.field:
							card.gem_applied_thisturn=False
						EndTurn(controller).trigger(controller)
						break
					else: ###execute the move here
						choice.execute()
						choiceAction(controller)
					pass
			### end of move turn of agent 
			#self.manager.step(self.next_step, Step.MAIN_NEXT)

			### 対戦
			i=0
			battles[i] = BG_Battle([self.BG_Bars[self.matches[i][0]],self.BG_Bars[self.matches[i][1]]])
			battleplayer0 = self.BG_Bars[self.matches[i][0]].controller
			battleplayer1 = self.BG_Bars[self.matches[i][1]].controller
			battles[i].parent = self
			#for  player in [battleplayer0, battleplayer1]:
			### begin the battle
			damage0, damage1, battleplayer0.buddy_gauge, battleplayer1.buddy_gauge  = battles[i].battle()
			### after the battle
			for  player in [battleplayer0, battleplayer1]:
				### バディーゲージが100を超えたらバディーカードを発行する。
				if player.buddy_gauge>=100 and player.got_buddy==0:
					player.got_buddy=1
					buddy = self.BG_Hero_Buddy[player.hero.id]
					Give(player, buddy).trigger(player)
				### バディーゲージが200を超えたらバディーカードを2枚発行する。
				if player.buddy_gauge>=300 and player.got_buddy==1:
					player.got_buddy=2
					buddy = self.BG_Hero_Buddy[player.hero.id]
					Give(player, buddy).trigger(player)
					Give(player, buddy).trigger(player)
					gold_card_id = player.game.BG_find_triple()## トリプルを判定
					if gold_card_id:
						player.game.BG_deal_gold(gold_card_id)
			### if agent got a gem card while the battle, we carry it to the bar
			if damage0>0:
				hero0 = battleplayer0.hero
				if hero0.armor>0:# armorも加味する
					if hero0.armor >= damage0:
						hero0.armor -= damage0
					else:
						hero0.damage += (damage0 - hero0.armor)
						hero0.armor=0
				else:
					hero0.damage += damage0#
				print_hero_stats(battleplayer0.hero, battleplayer1.hero)
				if hero0.health<=0:
					#Hero をケルスザード'TB_KTRAF_H_1'に交代して続行する。
					#ケルスザードは酒場のムーブを行わない。
					return
			if damage1>0:
				hero1 = battleplayer1.hero
				if hero1.armor>0:# armorも加味する
					if hero1.armor >= damage1:
						hero1.armor -= damage1
					else:
						hero1.damage += (damage1 - hero1.armor)
						hero1.armor=0
				else:
					hero1.damage += damage1#
				print_hero_stats(battleplayer0.hero, battleplayer1.hero)
				if hero1.health<=0:
					#Hero をケルスザード'TB_KTRAF_H_1'に交代する。
					return
			pass
			#次のターンへ
			for bar in self.BG_Bars:
				controller = bar.controller
				# グレードアップコストを減らす。
				controller.tavern_tierup_cost = max(0, controller.tavern_tierup_cost-1) 
				#ターン更新に伴うコインの補充。
				#bar.turn += 1
				controller.used_mana = 0 
				controller.prev_field=[]
				for card in controller.field:
					controller.prev_field.append(card.id)
				pass

		# 無限ループ終わり
		# main おわり
		pass

	def DealCard(self, bartender, tier):
		dk=[]
		for i in range(1,tier+1):
			dk += self.BG_decks[i]
		cardID = random.choice(dk)
		card = bartender.card(cardID)
		if card.race==Race.ELEMENTAL:## 
			if bartender.opponent.nomi_powered_up>0: ### Nomi, Kitchen Nightmare
				Buff(card, 'BGS_104pe').trigger(bartender)
				buff = card.buffs[-1]
				buff.atk=bartender.opponent.nomi_powered_up
				buff.max_health=bartender.opponent.nomi_powered_up
			if bartender.opponent.lightspawn_powered_up>0: ### Dazzling Lightspawn
				Buff(card, 'BG21_020pe').trigger(bartender)
				buff = card.buffs[-1]
				buff.atk=bartender.opponent.lightspawn_powered_up
				buff.max_health=bartender.opponent.lightspawn_powered_up
		self.BG_decks[card.tech_level].remove(cardID)
		card.controller = bartender# maybe deletable
		card.zone = Zone.PLAY
		return card
	def ReturnCard(self, card):
		# if the card is not a buddy
		if not hasattr(card, 'buddy'):
			self.BG_decks[card.tech_level].append(card.id)
		else:
			test=0
		card.zone=Zone.GRAVEYARD
		card.controller.field.remove(card)
		pass

	def last_warband(self, controller):
		my_bar = controller.game
		# assert my_bar.parent == self
		last_matches = self.prevMatches
		for match in range(len(last_matches)):
			the_match = last_matches[match]
			if my_bar == self.BG_Bars[the_match[0]]:
				last_opponent_bar = self.BG_Bars[the_match[1]]
				break
			elif my_bar == self.BG_Bars[the_match[1]]:
				last_opponent_bar = self.BG_Bars[the_match[0]]
				break
		else:
			something_is_wrong=1
		return last_opponent_bar.controller.prev_field

	def next_warband(self, controller):
		my_bar = controller.game
		# assert my_bar.parent == self
		next_matches = self.matches
		for match in range(len(next_matches)):
			the_match = next_matches[match]
			if my_bar == self.BG_Bars[the_match[0]]:
				next_opponent_bar = self.BG_Bars[the_match[1]]
				break
			elif my_bar == gamemaster.self.BG_Bars[the_match[1]]:
				next_opponent_bar = self.BG_Bars[the_match[0]]
				break
		else:
			something_is_wrong=1
		return next_opponent_bar.controller.prev_field

	#class 終わり
	pass

def print_hero_stats(hero0, hero1):
	print("<< %s (%s)<< health=%d+%d"%(hero0, hero0.controller, hero0.health, hero0.armor))
	print("<< %s (%s)<< health=%d+%d"%(hero1, hero1.controller, hero1.health, hero1.armor))
	pass

def choiceAction(player):
	while True:
		if player.choice == None:
			return
		else:
			if player.choiceStrategy==None:
				if len(player.choice.cards)==0:
					choice = None
				else:
					choice = random.choice(player.choice.cards)
			else:
				choice = player.choiceStrategy(player,player.choice.cards)
			if Config.LOGINFO:
				print("%r Chooses a card %r from %r" % (player, choice, player.choice.cards))
			#myChoiceStr = str(choice)
			if 'RandomCardPicker' in str(choice):
				myCardID =  random.choice(choice.find_cards())
				Give(player,myCardID).trigger(player)
				player.choice = None
			else :
				if choice == None:
					player.choice=None##return
				else:
					player.choice.choose(choice)

class Move(object):
	def __init__(self, game, target, move, param0=-1, param1=-1, param2=-1):
		self.game=game
		self.controller = game.controller
		self.bartender = game.bartender
		self.target = target
		self.move = move
		self.param0 = param0
		self.param1 = param1
		self.param2 = param2
		pass
	def __str__(self):
		if self.move==MovePlay.PLAY:
			if self.param1==-1:
				return "%s を場に出す（位置：%d）"%(self.target, self.param0)
			else :
				return "%s を場に出す（位置：%d）（ターゲット：%s）"%(self.target, self.param0,
										self.controller.field[self.param1])
		elif self.move==MovePlay.ORDER:
			return "%s の場所を動かす（位置：%d）"%(self.target, self.param0)
		elif self.move==MovePlay.BUY:# 
			return "%s を雇用する"%(self.target)
		elif self.move==MovePlay.SELL:# 
			return "%s を売る"%(self.target)
		elif self.move==MovePlay.POWER:# 
			if self.target != None:
				return "%s （ヒーローパワー）を発動する（コスト%d）"%(self.target, self.controller.hero.power.cost)
			else:
				return "（ヒーローパワー）を発動する（コスト%d）"%(self.controller.hero.power.cost)
		elif self.move==MovePlay.TIERUP:#
			return "グレードを上げる（コスト%d）"%(self.controller.tavern_tierup_cost)
		elif self.move==MovePlay.REROLE:# 
			return "リロールする（コスト%d）"%(self.game.reroleCost)
		elif self.move==MovePlay.FREEZE:# 
			return "凍結する"
		elif self.move==MovePlay.TURNEND:# 
			return "ターンを終了する"
		else:
			return "%s %s %d"%(self.target, self.move, self.param0)

	def execute(self):
		if self.move==MovePlay.PLAY:# move a card from hand to field
			self.play(self.target, position=self.param0, targetpos=self.param1)
			pass
		elif self.move==MovePlay.ORDER:# change the order of field cards 
			self.changeOrder(self.target, self.param0)
			pass
		elif self.move==MovePlay.BUY:# move a card from opponent field to hand
			self.buy(self.target)
			pass
		elif self.move==MovePlay.SELL:# move a card from field to opponent
			self.sell(self.target)
			pass
		elif self.move==MovePlay.POWER:# move a card from field to opponent
			self.power(self.target)
			pass
		elif self.move==MovePlay.TIERUP:#push a button of grade-up
			self.tierup()
			pass
		elif self.move==MovePlay.REROLE:# refresh opponent field by pool set
			self.rerole()
			pass
		elif self.move==MovePlay.FREEZE:# fix opponent field 
			self.freeze()
			pass
		else:
			pass
		pass

	def play(self, card, position=-1, targetpos=-1):
		if card!=None and card.id=='TB_BaconShop_Triples_01':## カードを発見
			pass
		# play a spell card (blood gem, banana, coin, spellcraft)
		if card!=None and card.type==CardType.SPELL:
			if card.requires_target() and targetpos>=0 and self.controller.field[targetpos] in card.targets:
				card.target = self.controller.field[targetpos]
			BG_Play(card, card.target, None, None).trigger(self.controller)
		# play a minion card
		if card!=None and card.cant_play!=True and card.type==CardType.MINION and len(self.controller.field)<7:
			if position<0:
				position += len(self.controller.field)
			card._summon_index = position
			if card.requires_target() and targetpos>=0 and self.controller.field[targetpos] in card.targets:
				card.target = self.controller.field[targetpos]
			BG_Play(card, card.target, position, None).trigger(self.controller)
	def changeOrder(self, card, p0):
		num = len(self.controller.field)
		field = self.controller.field
		tmp = card
		for p in range(num):
			if field[p]==card:
				break
		if p>p0:
			for offset in range(p-p0):
				q=p-offset
				field[q]=field[q-1]
			field[p0]=tmp
		elif p<p0:
			for offset in range(p0-p):
				q=p+offset
				field[q]=field[q+1]
			field[p0]=tmp
		pass

	def buy(self, card):
		Buy(self.controller, card).trigger(self.controller)

	def sell(self, card):
		Sell(self.controller, card).trigger(self.controller)

	def power(self, target):
		controller = self.controller
		heropower = self.controller.hero.power
		if heropower.is_usable() and heropower.cost <= controller.mana:
			if heropower.requires_target() and target in heropower.targets:
				heropower.use(target=target)
			else:
				heropower.use()
		pass

	def tierup(self):
		UpgradeTier(self.controller).trigger(self.controller)
		pass

	def rerole(self):## TargetedActionへ振り替える。
		Rerole(self.controller).trigger(self.controller)
		pass

	def freeze(self):
		allfrozen=True
		for c in self.bartender.field:
			if not c.frozen:
				allfrozen=False
		if allfrozen:
			for c in self.bartender.field:
				c.frozen=False
		else:
			for c in self.bartender.field:
				c.frozen=True
		pass

	def turnend(self):
		pass

	def turnbegin(self):
		pass

def GetMoveCandidates(bar, controller, bartender):
	ret = []
	#TURNEND=9
	ret.append(Move(bar, None, MovePlay.TURNEND, 0))
	#BUY=3
	if controller.mana>=bar.minionCost:
		for card in bartender.field:
			ret.append(Move(bar, card, MovePlay.BUY))
	#PLAY=1
	for card in controller.hand:
		if card.type==CardType.MINION:
			if len(controller.field)<7:
				if not card.cant_play:
					for pos in range(len(controller.field)+1):
						if card.requires_target():
							for target in card.targets:
								targetpos=controller.field.index(target)
								ret.append(Move(bar, card, MovePlay.PLAY, param0=pos, param1=targetpos))
						else:
							ret.append(Move(bar, card, MovePlay.PLAY, param0=pos))
		else: ## card.type==CardType.SPELL
			if not card.cant_play:
				if card.requires_target():
					for target in card.targets:
						targetpos=controller.field.index(target)
						ret.append(Move(bar, card, MovePlay.PLAY, param0=0, param1=targetpos))
				else:
					ret.append(Move(bar, card, MovePlay.PLAY, param0=0))
	#ORDER=2
	#for pos0 in range(len(controller.field)):
	#	card = controller.field[pos0]
	#	for pos in range(len(controller.field)):
	#		if pos != pos0:
	#			ret.append(Move(bar, card, MovePlay.ORDER, param0=pos))
	#SELL=4
	for card in controller.field:
		ret.append(Move(bar, card, MovePlay.SELL))
	#POWER=5
	if not controller.hero.power.cant_play and controller.hero.power.is_usable() and controller.hero.power.cost <= controller.mana:
		if controller.hero.power.requires_target() and len(controller.hero.power.targets)>0:
			for target in controller.hero.power.targets:
				ret.append(Move(bar, target, MovePlay.POWER))
		else:
			ret.append(Move(bar, None, MovePlay.POWER))
	#TIERUP=6
	if controller.tavern_tier<=5 and controller.mana>=controller.tavern_tierup_cost:
		ret.append(Move(bar, None, MovePlay.TIERUP))
	#REROLE=7
	if controller.mana>=bar.reroleCost:
		ret.append(Move(bar, None, MovePlay.REROLE, 0))
	#FREEZE=8
	ret.append(Move(bar, None, MovePlay.FREEZE, 0))
	return ret




