from fireplace import cards
from fireplace.actions import BeginBar, BeginGame, BG_Play, Buff, Buy, CastSecret, EndTurn, EventListener, Give, LoseGame, Rerole, Sell, TieGame, UpgradeTier, WinGame
#from fireplace.card import Card
from fireplace.cards.utils import get00
from fireplace.config import Config
from fireplace.player import Player
from fireplace.dsl import random_picker
#from fireplace.game import Game
import random
from hearthstone.enums import Zone, CardType, Race, GameTag

from .BG_agent import BG_HumanAgent,BG_NecoAgent,BG_RandomAgent
from .BG_bar import BG_Bar
from .BG_battle import BG_Battle
from .BG_enums import MovePlay


BobsFieldSize={1:3, 2:4, 3:4, 4:5, 5:5, 6:6}


class BG_main:
	def __init__(self):
		# initializing pool set
		cards.db.BG_initialize()
		# list of agents
		if Config.PLAYER1_HUMAN:
			self.Agents=[
			BG_HumanAgent("Human1"),
			BG_NecoAgent("Neco2"),
			BG_NecoAgent("Random3"),
			BG_NecoAgent("Random4")
			]
		else:
			self.Agents=[
			BG_NecoAgent("Human1"),
			BG_NecoAgent("Neco2"),
			BG_NecoAgent("Random3"),
			BG_NecoAgent("Random4")
			]
		# list of heroes
		self.Heroes = cards.battlegrounds.BG_hero1.BG_PoolSet_Hero1
		self.Heroes += cards.battlegrounds.BG_hero2.BG_PoolSet_Hero2
		self.Heroes += cards.battlegrounds.BG_hero3.BG_PoolSet_Hero3
		self.Heroes += cards.battlegrounds.BG_hero4.BG_PoolSet_Hero4
		self.Heroes += cards.battlegrounds.BG_hero5.BG_PoolSet_Hero5
		#for hero in BG_Exclude_Hero:
		#	self.Heroes.remove(hero)
		# begining the deck
		self.BG_decks=[[],[],[],[],[],[],[]]
		if Config.RANDOM_RACE:
			# sample races randomly
			self.BG_races = races = random.sample(['beast','demon','dragon','elemental','mecha','murloc','naga','pirate','quilboar','undead'],5)## add naga 23.2.2 ## add undead 25.2.2
		else:
			# or specific race set. 
			self.BG_races = races=Config.RACE_CHOICE
		random_picker.BG_races=[]
		random_picker.BG_races.append(Race.INVALID)
		if 'beast' in self.BG_races:
			random_picker.BG_races.append(Race.BEAST)
		if 'demon' in self.BG_races:
			random_picker.BG_races.append(Race.DEMON)
		if 'dragon' in self.BG_races:
			random_picker.BG_races.append(Race.DRAGON)
		if 'elemental' in self.BG_races:
			random_picker.BG_races.append(Race.ELEMENTAL)
		if 'mecha' in self.BG_races:
			random_picker.BG_races.append(Race.MECHANICAL)
		if 'murloc' in self.BG_races:
			random_picker.BG_races.append(Race.MURLOC)
		if 'naga' in self.BG_races:
			random_picker.BG_races.append(Race.NAGA)
		if 'pirate' in self.BG_races:
			random_picker.BG_races.append(Race.PIRATE)
		if 'quilboar' in self.BG_races:
			random_picker.BG_races.append(Race.QUILBOAR)
		if 'undead' in self.BG_races:## new 25.2.2
			random_picker.BG_races.append(Race.UNDEAD)## new 25.2.2
		for i in range(6):
			if i<5:
				rep=8
			else:
				rep=4
			for repeat in range(rep):	
				self.BG_decks[i+1] += cards.battlegrounds.BG_minion.BG_PoolSet_Minion[i+1]
				if 'beast' in races:
					self.BG_decks[i+1] += cards.battlegrounds.BG_minion_beast.BG_PoolSet_Beast[i+1]
				if 'demon' in races:
					self.BG_decks[i+1] += cards.battlegrounds.BG_minion_demon.BG_PoolSet_Demon[i+1]
				if 'dragon' in races:
					self.BG_decks[i+1] += cards.battlegrounds.BG_minion_dragon.BG_PoolSet_Dragon[i+1]
				if 'elemental' in races:
					self.BG_decks[i+1] += cards.battlegrounds.BG_minion_elemental.BG_PoolSet_Elemental[i+1]
				if 'mecha' in races:
					self.BG_decks[i+1] += cards.battlegrounds.BG_minion_mecha.BG_PoolSet_Mecha[i+1]
				if 'murloc' in races:
					self.BG_decks[i+1] += cards.battlegrounds.BG_minion_murloc.BG_PoolSet_Murloc[i+1]
				if 'naga' in races:
					self.BG_decks[i+1] += cards.battlegrounds.BG_minion_naga.BG_PoolSet_Naga[i+1]
				if 'pirate' in races:
					self.BG_decks[i+1] += cards.battlegrounds.BG_minion_pirate.BG_PoolSet_Pirate[i+1]
				if 'quilboar' in races:
					self.BG_decks[i+1] += cards.battlegrounds.BG_minion_quilboar.BG_PoolSet_Quilboar[i+1]
				if 'undead' in races:## new 25.2.2
					self.BG_decks[i+1] += cards.battlegrounds.BG_minion_undead.BG_PoolSet_Undead[i+1]## new 25.2.2
		if not 'dragon' in self.BG_races and 'TB_BaconShop_HERO_56' in self.Heroes:
			self.Heroes.remove('TB_BaconShop_HERO_56')#2 dragon ban
		if not 'elemental' in self.BG_races and 'TB_BaconShop_HERO_78' in self.Heroes:
			self.Heroes.remove('TB_BaconShop_HERO_78')#11 elemental ban
		if not 'murloc' in self.BG_races and 'TB_BaconShop_HERO_55' in self.Heroes:
			self.Heroes.remove('TB_BaconShop_HERO_55')#21 Murloc ban
		if not 'demon' in self.BG_races and 'TB_BaconShop_HERO_37' in self.Heroes:
			self.Heroes.remove('TB_BaconShop_HERO_37')#35 demon ban
		if not 'mecha' in self.BG_races and 'TB_BaconShop_HERO_17' in self.Heroes:
			self.Heroes.remove('TB_BaconShop_HERO_17')#40 mech ban
		if not 'pirate' in self.BG_races and 'TB_BaconShop_HERO_18' in self.Heroes:
			self.Heroes.remove('TB_BaconShop_HERO_18')#48 pirate ban
		if not 'dragon' in self.BG_races and 'TB_BaconShop_HERO_53' in self.Heroes:
			self.Heroes.remove('TB_BaconShop_HERO_53')#77 dragon ban
		if not 'naga' in self.BG_races and 'BG23_HERO_304' in self.Heroes:
			self.Heroes.remove('BG23_HERO_304')#80#Lady Vashj

		self.BG_Bars=[]
		self.BG_Gold=cards.battlegrounds.BG_minion.BG_Minion_Gold
		self.BG_Gold.update(cards.battlegrounds.BG_minion_beast.BG_Beast_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_minion_demon.BG_Demon_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_minion_dragon.BG_Dragon_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_minion_elemental.BG_Elemental_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_minion_mecha.BG_Mecha_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_minion_naga.BG_Naga_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_minion_murloc.BG_Murloc_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_minion_pirate.BG_Pirate_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_minion_quilboar.BG_Quilboar_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_minion_undead.BG_Undead_Gold)## new 25.2.2
		self.BG_Gold.update(cards.battlegrounds.BG_hero1.BG_Hero1_Buddy_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_hero2.BG_Hero2_Buddy_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_hero3.BG_Hero3_Buddy_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_hero4.BG_Hero4_Buddy_Gold)
		self.BG_Gold.update(cards.battlegrounds.BG_hero5.BG_Hero5_Buddy_Gold)

		if Config.BUDDY_SYSTEM or Config.NEW_BUDDY_SYSTEM:
			self.BG_Hero_Buddy=cards.battlegrounds.BG_hero1.BG_Hero1_Buddy
			self.BG_Hero_Buddy.update(cards.battlegrounds.BG_hero2.BG_Hero2_Buddy)
			self.BG_Hero_Buddy.update(cards.battlegrounds.BG_hero3.BG_Hero3_Buddy)
			self.BG_Hero_Buddy.update(cards.battlegrounds.BG_hero4.BG_Hero4_Buddy)
			self.BG_Hero_Buddy.update(cards.battlegrounds.BG_hero5.BG_Hero5_Buddy)
		self.size = 4
		self.prevMatches=[[0,1],[2,3]]# previous combination
		self.matches=[[0,1],[2,3]]
		self.BG_darkmoon_tickets=cards.battlegrounds.BG_DarkmoonTicket
		self.darkmoon_ticket_by_4=False# 24.2 (until 24.0, random.choice([True,False]))
		self.winners=[] # for Load Barov TB_BaconShop_HERO_72
		self.drawers=[] # for TB_BaconShop_HP_081
		self.warbandDeceased=[] # for Bigglesworth TB_BaconShop_HERO_70
	pass
	def __str__(self):
		return "BG_gamemaster"
	def BG_main(self):
		# each agent chooses heroes 
		for agent in self.Agents:
			if Config.LOGINFO:
				print ("==== %s 's bar building ===="% agent)
			if agent.name=='Human1':
				theHeroes = []
				if Config.HERO_1 in self.Heroes:
					theHeroes.append(Config.HERO_1)
					self.Heroes.remove(theHeroes[0])
				if Config.HERO_2 in self.Heroes:
					theHeroes.append(Config.HERO_2)
					self.Heroes.remove(theHeroes[1])
				theHeroes += random.sample(self.Heroes, 4-len(theHeroes))
			else:
				theHeroes = random.sample(self.Heroes, 4)
			for hero in theHeroes:
				if hero in self.Heroes:
					self.Heroes.remove(hero)
			if Config.HERO_1!='':
				theHero = theHeroes[0]
			else:
				theHero = agent.heroChoiceStrategy(theHeroes)
			#heroCard=Card(theHero)
			## create a player
			thePlayer = Player(agent.name, self.BG_decks[1], theHero)#
			# building a Tavern
			bar = BG_Bar(thePlayer)
			bar.BG_setup()
			bar.player1 = bar.current_player = bar.controller
			if Config.NEW_BUDDY_SYSTEM:
				buddy_fid=bar.player1.hero.tags.get(GameTag.BACON_COMPANION_ID, -1)
				buddy_card=[c for c in cards.db.values() if c.tags.get(9090, None)==buddy_fid]
				assert len(buddy_card)>0

				bar.player1.buddy_id = buddy_card[0].id
				bar.player1.buddy_taver_tier = buddy_card[0].tags[GameTag.TECH_LEVEL]
				bar.player1.buddy_gauge=bar.player1.buddy_taver_tier*2+9
				bar.player1.got_buddy = 0
			bar.player2 = bar.bartender
			bar.turn=1
			bar.parent = self
			bar.player1.parent_agent = agent
			bar.player1.choiceStrategy = agent.choiceStrategy
			self.BG_Bars.append(bar)
			########## FOR DEBUGGIN! Default dealing a specific card
			if agent.name=='Human1':
				if Config.CARD_PRESET1!= '':
					card = bar.controller.card(Config.CARD_PRESET1)
					card.zone = Zone.HAND
				if Config.CARD_PRESET2!= '':
					card = bar.controller.card(Config.CARD_PRESET2)
					card.zone = Zone.HAND
				if Config.REWARD_PRESET_FIRST>0 and Config.REWARD_PRESET!='':
					card = bar.controller.card(Config.REWARD_PRESET)
					#if card.id=='BG24_Reward_130':
					#	card.script_data_num_1=random.choice(random_picker.BG_races)
					CastSecret(card).trigger(bar.controller)
			##########
			if bar.player1.hero.power.id=='TB_BaconShop_HP_054': #Millhouse flag
				bar.player1.tavern_tierup_cost += 1
				bar.reroleCost=2
				bar.minionCost=2
			BeginGame(bar.controller).trigger(bar.controller)
			################### 24.2 battlegrounds quest=reward
			if Config.QUEST_REWARD:
				secret = bar.player1.card('BG24_Quest_Bob')
				CastSecret(secret).trigger(bar.player1)
			if Config.LOGINFO:
				print ("==== %s 's bar was built ===="% agent)
			pass
		self.prevMatches=[[0,1],[2,3]]# previous combination
		# Start game
		while True:	
			### randomize the combinations
			draw_list = [[i for i in range(self.size)] for j in range(self.size)]
			count_alive = 0
			for i in range(self.size):
				if self.BG_Bars[i].hero_is_alive:
					count_alive+=1
			latest_killed=-1
			latest_killed_rank=9#number more than 8
			if count_alive%2==1: #odd case
				for i in range(self.size):
					b=self.BG_Bars[i]
					r=b.local_rank
					if not b.hero_is_alive and r<latest_killed_rank:
						latest_killed_rank = r
						latest_killed = i
			for i in range(self.size):
				b=self.BG_Bars[i]
				if not b.hero_is_alive and i!=latest_killed:
					for j in range(self.size):
						if i in draw_list[j]:
							draw_list[j].remove(i)
					draw_list[i]=[]
			for i in range(self.size):
				if i in draw_list[i]:
					draw_list[i].remove(i)
			if count_alive>2:
				for match in self.matches:##previous matches
					if match[1] in draw_list[match[0]]:
						draw_list[match[0]].remove(match[1])
					if match[0] in draw_list[match[1]]:
						draw_list[match[1]].remove(match[0])
			self.matches=[]#
			for i in range(self.size):
				if draw_list[i]==[]:
					continue
				j=random.choice(draw_list[i])
				self.matches.append([i,j])
				draw_list[i]=[]
				draw_list[j]=[]
				for ii in range(self.size):
					if i in draw_list[ii]:
						draw_list[ii].remove(i)
					if j in draw_list[ii]:
						draw_list[ii].remove(j)
			print("Next battle draw:::::::::::::::::::::::::")
			for match in self.matches:
				print("%s(%s)"%(self.BG_Bars[match[0]].controller.hero, self.BG_Bars[match[0]].controller), end=":")
				print("%s(%s)"%(self.BG_Bars[match[1]].controller.hero, self.BG_Bars[match[1]].controller))
			#in tha final, battles length will be 4 
			battles = [None for i in range(int(self.size/2))]
			### Agent moves start
			for bar in self.BG_Bars:
				for card in bar.controller.gifts:
					Give(bar.controller, card).trigger(bar.controller)
				bar.controller.gifts=[]
			for bar in self.BG_Bars:
				if bar.hero_is_alive:
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
					controller.total_used_mana_this_turn = 0
					if controller.hero.power.id=='TB_BaconShop_HP_008':
						controller.used_mana = -controller.sells_in_this_turn
					controller.sells_in_this_turn=0
					### deal cards to tavern
					frozencard=0
					for card in reversed(bartender.field):
						if Config.LOGINFO:
							Config.log("BG_MainBG_Main","field card %s is removed."%(card))
						if not card.frozen and not card.dormant>0:
							card.discard()
						else:
							card.frozen=False
							frozencard += 1
					bar.process_deaths()### do we need?
					if bartender.len_bobs_field-frozencard+bartender.extra_len_bobs_field>0:
						for repeat in range(bartender.len_bobs_field-frozencard+bartender.extra_len_bobs_field):
							card = self.DealCard(bartender, controller.tavern_tier)
							if controller.hero.power.id=='TB_BaconShop_HP_101':### Silas-flag
								if random.choice([0,1]):
									card.darkmoon_ticket = True
						Rerole(controller).broadcast(controller, EventListener.AFTER, controller)
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
						if Config.ALL_PLAYERS_LOGINFO:
							print("(%s) %s"%(controller, choice))
						if choice.move==MovePlay.TURNEND:#### if the move is 'turnend' then turn to the battle
							bar.no_drawing_at_turn_begin=True
							for card in controller.field:
								card.gem_applied_thisturn=False
							EndTurn(controller).trigger(controller)## EndBar
							break
						else: ###execute the move here
							choice.execute()
							choiceAction(controller)
						pass
			### end of move turn of agent 
			#self.manager.step(self.next_step, Step.MAIN_NEXT)

			### 対戦
			self.winners=[]
			self.drawers=[]
			for i in range(len(self.matches)):
				self.BG_Bars[self.matches[i][0]].countcards()
				self.BG_Bars[self.matches[i][1]].countcards()
				battles[i] = BG_Battle([self.BG_Bars[self.matches[i][0]],self.BG_Bars[self.matches[i][1]]])
				battleplayer0 = self.BG_Bars[self.matches[i][0]].controller
				battleplayer1 = self.BG_Bars[self.matches[i][1]].controller
				battles[i].parent = self
				#for  player in [battleplayer0, battleplayer1]:
				### begin the battle
				damage0, damage1, battleplayer0.buddy_gauge, battleplayer1.buddy_gauge  = battles[i].battle()
				### after the battle
				self.BG_Bars[self.matches[i][0]].identifycards()
				self.BG_Bars[self.matches[i][1]].identifycards()
				## buddy mechanism, before 23.1
				if Config.BUDDY_SYSTEM:
					for  player in [battleplayer0, battleplayer1]:
						### if buddy gauge turn into the limit, 
						if player.buddy_gauge>=100 and player.got_buddy==0:
							player.got_buddy=1
							buddy = self.BG_Hero_Buddy[player.hero.id]
							Give(player, buddy).trigger(player)
						### if buddy gauge turn into the second limit, 
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
					self.winners.append(battleplayer1.hero.id)
					LoseGame(battleplayer0).trigger(battleplayer0)	
					WinGame(battleplayer1).trigger(battleplayer1)	
					hero0 = battleplayer0.hero
					if hero0.armor>0:# add armor to health
						if hero0.armor >= damage0:
							hero0.armor -= damage0
						else:
							hero0.damage += (damage0 - hero0.armor)
							hero0.armor=0
					else:
						hero0.damage += damage0#
					print_hero_stats(battleplayer0.hero, battleplayer1.hero)
					if hero0.health<=0:
						hero0.max_health=0
						hero0.game.hero_is_alive=False
						# if dead hero, morph it to Kelse
						winner = self.refresh_ranks()
						self.warbandDeceased.append(battleplayer0.field)
						if winner:
							print("Winner is %s(%s)"%(winner.controller.hero, winner.controller))
							return
				if damage1>0:
					self.winners.append(battleplayer0.hero.id)
					WinGame(battleplayer0).trigger(battleplayer0)	
					LoseGame(battleplayer1).trigger(battleplayer1)	
					hero1 = battleplayer1.hero
					if hero1.armor>0:# armor
						if hero1.armor >= damage1:
							hero1.armor -= damage1
						else:
							hero1.damage += (damage1 - hero1.armor)
							hero1.armor=0
					else:
						hero1.damage += damage1#
					print_hero_stats(battleplayer0.hero, battleplayer1.hero)
					if hero1.health<=0:
						hero1.max_health=0
						hero1.game.hero_is_alive=False
						# if dead hero, morph it to Kelse
						winner = self.refresh_ranks()
						self.warbandDeceased.append(battleplayer1.field)
						if winner:
							print("Winner is %s(%s)"%(winner.controller.hero, winner.controller))
							return
				if damage0==0 and damage1==0:
					self.drawers.append(battleplayer0.hero.id)
					self.drawers.append(battleplayer1.hero.id)
					TieGame(battleplayer0).trigger(battleplayer0)	
					TieGame(battleplayer1).trigger(battleplayer1)	
					pass
			## end of battle
			# next turn at tavern
			for bar in self.BG_Bars:
				bar.identifycards()
				controller = bar.controller
				# decrease tier-up cost
				controller.tavern_tierup_cost = max(0, controller.tavern_tierup_cost-1-controller.extra_tavern_tierup_reduce_cost) 
				# fill coins 
				#bar.turn += 1
				controller.used_mana = 0 
				controller.total_used_mana_this_turn = 0 
				controller.prev_field=[]
				for card in controller.field:
					controller.prev_field.append(card.id)
				pass
			self.prevMatches=[]
			for match in self.matches:
				self.prevMatches.append(match)
		# end of infinite loop
		# end of main
		pass

	def DealCard(self, bartender, tier, only_tier=False):
		dk=[]
		if only_tier:
			dk += self.BG_decks[tier]
		else:
			for i in range(1,tier+1):
				dk += self.BG_decks[i]
		cardID = random.choice(dk)
		card = bartender.card(cardID)
		if card.race==Race.ELEMENTAL:## 
			if bartender.opponent.nomi_powered_up>0: ### Nomi, Kitchen Nightmare
				Buff(card, 'BGS_104pe',
					atk=bartender.opponent.nomi_powered_up,
					max_health=bartender.opponent.nomi_powered_up
					).trigger(bartender)
			if bartender.opponent.lightspawn_powered_up>0: ### Dazzling Lightspawn
				Buff(card, 'BG21_020pe',
					atk=bartender.opponent.lightspawn_powered_up,
					max_health=bartender.opponent.lightspawn_powered_up
					).trigger(bartender)
			for buff in bartender.opponent.buffs:
				if buff.id == 'BGS_Treasures_013pe':  #(Good stuff, a darkmoon ticket)
					Buff(card, 'BGS_Treasures_013e1')
		if card.id=='BG25_008':
			if bartender.opponent.eternal_knight_powered_up>0: ### Eternal_Knight
				Buff(card, 'BG25_008pe',
					atk=bartender.opponent.eternal_knight_powered_up,
					max_health=bartender.opponent.eternal_knight_powered_up
					).trigger(bartender)		
		elif card.id=='BG25_008_G':
			if bartender.opponent.eternal_knight_powered_up>0: ### Eternal_Knight(gold)
				Buff(card, 'BG25_008pe',
					atk=bartender.opponent.eternal_knight_powered_up*2,
					max_health=bartender.opponent.eternal_knight_powered_up*2
					).trigger(bartender)	
		if bartender.opponent.felemental_powered_up>0:
			Buff(card, 'BG25_041e',
				atk=bartender.opponent.felemental_powered_up,
				max_health=bartender.opponent.felemental_powered_up
				).trigger(bartender)
		if bartender.opponent.stormpike_powered_up>0:
			Buff(card, 'BG22_HERO_003_Buddy_e',
				max_health=bartender.opponent.stormpike_powered_up
				).trigger(bartender)
		if cardID in self.BG_decks[card.tech_level]:
			self.BG_decks[card.tech_level].remove(cardID)
		else:
			print("cardID=%s, card.tech_level=%d"%(cardID, card.tech_level))
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
			elif my_bar == self.BG_Bars[the_match[1]]:
				next_opponent_bar = self.BG_Bars[the_match[0]]
				break
		else:
			something_is_wrong=1
		return next_opponent_bar.controller.prev_field

	def refresh_ranks(self):
		""" refresh the rank table of heroes.
		if the winner is deteremined, return the hero. else return None
		"""
		statstable=[]
		for b in self.BG_Bars:
			player = b.controller
			hero = player.hero
			herohealth = hero.health+hero.armor
			if herohealth<=0:
				herohealth=0
			local_rank=b.local_rank
			statstable.append([100-herohealth, local_rank, b])
		statstable.sort( key=lambda x: x[1])
		statstable.sort( key=lambda x: x[0])
		alive_count=0
		rank=1
		for x in statstable:
			x[2].local_rank=rank
			rank+=1
			if x[2].hero_is_alive:
				alive_count+=1
		if alive_count==1:
			for x in statstable:
				if x[2].local_rank==1:
					return x[2]
			else:
				print("No one wins.")
				return statstable[0][2]
		else:
			return None

	# end of class 	
	# pass

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
				Config.log("BG_utils.choiceAction","%r Chooses a card %r from %r" % (player, choice, player.choice.cards))
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
		elif self.move==MovePlay.BUY_BUDDY:# 
			return "バディ %s を雇用する"%(cards.db[self.target].name)
		elif self.move==MovePlay.SELL:# 
			return "%s を売る"%(self.target)
		elif self.move==MovePlay.POWER:# 
			if self.target != None:
				return "ヒーローパワー （対象：%s）を発動する（コスト%d）"%(self.target, self.controller.hero.power.cost)
			else:
				return "ヒーローパワーを発動する（コスト%d）"%(self.controller.hero.power.cost)
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
		elif self.move==MovePlay.BUY_BUDDY:# move a card from opponent field to hand
			self.buy_buddy(self.target)
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
		if card!=None and card.id=='TB_BaconShop_Triples_01':## discover a card
			pass
		if card.BG_cost>0:
			if Config.LOGINFO:
				Config.log("BG_utils.Move.play","This card(%s) need coins to play."%(card))
			if card.BG_cost>self.controller.mana:
				return
			else:
				self.controller.used_mana += card.BG_cost
				self.controller.total_used_mana_this_turn += card.BG_cost
				card.BG_cost=0
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

	def buy_buddy(self, card):
		if self.controller.got_buddy==0:
			self.controller.used_mana += self.controller.buddy_gauge
			self.controller.total_used_mana_this_turn += self.controller.buddy_gauge
			newcard=Give(self.controller, card).trigger(self.controller)
			newcard=get00(newcard)
			self.controller.buddy_gauge=newcard.tech_level*2+11
			self.controller.got_buddy=1
		elif self.controller.got_buddy==1:
			self.controller.used_mana += self.controller.buddy_gauge
			self.controller.total_used_mana_this_turn += self.controller.buddy_gauge
			Give(self.controller, card).trigger(self.controller)
			Give(self.controller, card).trigger(self.controller)
			gold_card_id = self.controller.game.BG_find_triple()## judge a triple
			if gold_card_id:
				self.controller.game.BG_deal_gold(gold_card_id) ## deal a gold card
			self.controller.got_buddy=2
			self.controller.buddy_gauge=0
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

	def rerole(self):##
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
	#BUY_BUDDY=11
	if controller.mana>=controller.buddy_gauge and controller.got_buddy<2:
		ret.append(Move(bar, controller.buddy_id, MovePlay.BUY_BUDDY))
	#PLAY=1
	for card in controller.hand:
		if card.type==CardType.MINION:
			if len(controller.field)<7:
				if not card.cant_play and card.BG_cost<=controller.mana:
					for pos in range(len(controller.field)+1):
						if card.requires_target():
							for target in card.targets:
								if target in controller.field:
									targetpos=controller.field.index(target)
								else:
									targetpos=0
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

def getRacesInCards(cards):
	for card in cards:
		count=[]
		tech_level=card.tech_level
		if card.id in cards.battlegrounds.BG_minion_beast.BG_PoolSet_Beast[tech_level]:
			if not Race.BEAST in count:
				count.append[Race.BEAST]
		if card.id in cards.battlegrounds.BG_minion_demon.BG_PoolSet_Demon[tech_level]:
			if not Race.DEMON in count:
				count.append[Race.DEMON]
		if card.id in cards.battlegrounds.BG_minion_dragon.BG_PoolSet_Dragon[tech_level]:
			if not Race.DRAGON in count:
				count.append[Race.DRAGON]
		if card.id in cards.battlegrounds.BG_minion_elemental.BG_PoolSet_Elemental[tech_level]:
			if not Race.ELEMENTAL in count:
				count.append[Race.ELEMENTAL]
		if card.id in cards.battlegrounds.BG_minion_mecha.BG_PoolSet_Mecha[tech_level]:
			if not Race.MECHANICAL in count:
				count.append[Race.MECHANICAL]
		if card.id in cards.battlegrounds.BG_minion_murloc.BG_PoolSet_Murloc[tech_level]:
			if not Race.MURLOC in count:
				count.append[Race.MURLOC]
		if card.id in cards.battlegrounds.BG_minion_naga.BG_PoolSet_Naga[tech_level]:
			if not Race.NAGA in count:
				count.append[Race.NAGA]
		if card.id in cards.battlegrounds.BG_minion_pirate.BG_PoolSet_Pirate[tech_level]:
			if not Race.PIRATE in count:
				count.append[Race.PIRATE]
		if card.id in cards.battlegrounds.BG_minion_quilboar.BG_PoolSet_Quilboar[tech_level]:
			if not Race.QUILBOAR in count:
				count.append[Race.QUILBOAR]
		if card.id in cards.battlegrounds.BG_minion_undead.BG_PoolSet_Undead[tech_level]:
			if not Race.UNDEAD in count:
				count.append[Race.UNDEAD]
	return count



