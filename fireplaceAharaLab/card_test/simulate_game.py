from hearthstone.enums import CardClass, BlockType, CardType ,PlayState, State, Race, SpellSchool
from fireplace.game import Game
from fireplace.card import Card, PlayableCard
from fireplace.actions import *
from fireplace.utils import random_draft
from fireplace.player import Player
from fireplace.config import Config
import random
from agent_Standard import *
from utils import postAction


def card_test():
	if Config.CARD_TEST_SET=='VANILLA':
		if Config.CARD_TEST_CLASS=='NEUTRAL':
			from card_test.t_classic_neutral import classic_neutral
			classic_neutral()
	elif Config.CARD_TEST_SET=='CORE':
		if Config.CARD_TEST_CLASS=='NEUTRAL':
			from card_test.core_neutral import core_neutral
			core_neutral()
	elif Config.CARD_TEST_SET=='ALTERAC_VALLEY':
		if Config.CARD_TEST_CLASS=='DRUID':
			from card_test.alterac_druid import alterac_druid
			alterac_druid()
		elif Config.CARD_TEST_CLASS=='HUNTER':
			from card_test.alterac_hunter import alterac_hunter
			alterac_hunter()
		elif Config.CARD_TEST_CLASS=='NEUTRAL':
			from card_test.alterac_neutral import alterac_neutral
			alterac_neutral()
		elif Config.CARD_TEST_CLASS=='ROGUE':
			from card_test.alterac_rogue import alterac_rogue
			alterac_rogue()
	elif Config.CARD_TEST_SET=='THE_BARRENS':
		if Config.CARD_TEST_CLASS=='ROGUE':
			from card_test.barrens_rogue import barrens_rogue
			barrens_rogue()
	elif Config.CARD_TEST_SET=='THE_SUNKEN_CITY':
		if Config.CARD_TEST_CLASS=='PRIEST':
			from card_test.sunken_priest import sunken_priest
			sunken_priest()
		elif Config.CARD_TEST_CLASS=='SHAMAN':
			from card_test.sunken_shaman import sunken_shaman
			sunken_shaman()
		elif Config.CARD_TEST_CLASS=='WARLOCK':
			from card_test.sunken_warlock import sunken_warlock
			sunken_warlock()
		pass
	elif Config.CARD_TEST_SET=='STORMWIND':
		if Config.CARD_TEST_CLASS=='DRUID':
			from card_test.stormwind_druid import stormwind_druid
			stormwind_druid()
		elif Config.CARD_TEST_CLASS=='WARLOCK':
			from card_test.stormwind_warlock import stormwind_warlock
			stormwind_warlock()
	elif Config.CARD_TEST_SET=='REVENDRETH':
		if Config.CARD_TEST_CLASS=='NEUTRAL':
			from card_test.t_rev_neutral import rev_neutral
			rev_neutral()
	pass


class DummyAgent(Agent):
	def __init__(self, myName: str, myFunction, myOption = [], myClass: CardClass = CardClass.HUNTER, rating =1000 ):
		super().__init__(myName, myFunction, myOption, myClass, rating )
		pass

	def DummyAI(self, thisgame, option=[], gameLog=[], debugLog=False):
		player = thisgame.current_player
		loopCount=0
		##########
		#new_game = deepcopy_game(thisgame, player, 0)
		#candidate1 = getCandidates(thisgame)
		#candidate2 = getCandidates(new_game)
		#compaireCandidates(candidate1, candidate2)
		##########
		while loopCount<20:
			##########
			#debug_board(new_game,thisgame)#
			##########
			loopCount+=1
			myCandidate = getCandidates(thisgame)
			if len(myCandidate)>0:
				myChoice = random.choice(myCandidate)
				##########
				#executeAction(new_game, myChoice, debugLog=debugLog)
				#postAction(new_game.current_player)
				##########
				exc = executeAction(thisgame, myChoice, debugLog=debugLog)
				postAction(player)
				if exc==ExceptionPlay.GAMEOVER:
					##########
					#debug_board(new_game,thisgame)#
					##########
					return ExceptionPlay.GAMEOVER
				else:
					continue
			return ExceptionPlay.VALID

class Preset_Play:
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def __init__(self, player):
		self.mark1 = None
		self.mark2 = None
		self.mark3 = None
		self.mark4 = None
		self.mark5 = None
		self.mark6 = None
		self.player = player
		self.game = player.game
		self.testNr = 0
		self.current=player
		self.controller=player
		self.opponent=player.opponent
		pass
	def preset_deck(self):
		#self.print_hand(self.player)
		#self.print_hand(self.player.opponent)
		#print ("")
		#print ("")
		#print ("")
		#print ("")
		pass
	def preset_play(self):
		pass
	def result_inspection(self):
		#self.print_hand(self.player)
		#self.print_hand(self.player.opponent)
		pass
	def choose_action(self):
		if self.current.choice!=None:
			return postAction(self.current)
		return None
		pass
	def change_turn(self, player=None):
		if player==None:
			player=self.current
		game = player.game
		if self.current.choice!=None:
			postAction(self.current)
		game.end_turn()
		self.current = player.opponent
		pass
	def execute(self, testNr = 0):
		self.testNr = testNr
		self.preset_deck()
		self.preset_play()
		#print ("")
		#print ("")
		#print ("")
		print ("####### results: %s  (%d)#######"%(self.__class__.__name__, self.testNr))
		self.result_inspection()
		print ("####### end    : %s  (%d)#######"%(self.__class__.__name__, self.testNr))

	def card_choice(self, _card):
		#from hearthstone import cardxml
		from fireplace.cards.cardlist import All
		from fireplace import cards
		#db, xml = cardxml.load(locale='enUS')
		### minion
		if _card[:-1]=='minionH':
			amount=int(_card[-1])
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.type == CardType.MINION and getattr(_card,'health',0)==amount and getattr(_card, 'collectible',0)==True: 
						choices.append(_id)
			_card=random.choice(choices)
		elif _card[:-1]=='minionA':
			amount=int(_card[-1])
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.type == CardType.MINION and _card.atk==amount: 
						choices.append(_id)
			_card=random.choice(choices)
		### spell
		elif _card=='spell':# except secret cards
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.type == CardType.SPELL and _card.secret==False: 
						choices.append(_id)
			_card=random.choice(choices)
		elif _card[:-1]=='spellC':# except secret cards
			amount=int(_card[-1:])
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.type == CardType.SPELL and _card.secret==False and _card.cost==amount: 
						choices.append(_id)
			_card=random.choice(choices)
		## race
		elif _card=='beast':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.race == Race.BEAST: 
						choices.append(_id)
			_card=random.choice(choices)
		elif _card=='dragon':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.race == Race.DRAGON: 
						choices.append(_id)
			_card=random.choice(choices)
		elif _card=='elemental':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.race == Race.ELEMENTAL: 
						choices.append(_id)
			_card=random.choice(choices)
		elif _card=='mech' or _card=='mecha':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.race == Race.MECHANICAL: 
						choices.append(_id)
			_card=random.choice(choices)
		elif _card=='murloc':
			_card=random.choice(['BAR_063','BAR_062','WC_030'])
		elif _card=='naga':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.race == Race.NAGA: 
						choices.append(_id)
			_card=random.choice(choices)
		elif _card=='pirate':
			_card=random.choice(['CS3_022','CORE_NEW1_018','BAR_081'])
		elif _card=='totem':
			_card=random.choice(['CORE_EX1_575','SCH_537','SCH_612t','CS2_050','CS2_051','CS2_052','NEW1_009'])
		### spell school
		elif _card=='arcane':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.spell_school == SpellSchool.ARCANE: 
						choices.append(_id)
			_card=random.choice(choices)		
		elif _card=='fire':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.spell_school == SpellSchool.FIRE: 
						choices.append(_id)
			_card=random.choice(choices)		
		elif _card=='frost':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.spell_school == SpellSchool.FROST: 
						choices.append(_id)
			_card=random.choice(choices)		
		elif _card=='holy':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.spell_school == SpellSchool.HOLY: 
						choices.append(_id)
			_card=random.choice(choices)
		elif _card=='nature':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.spell_school == SpellSchool.NATURE: 
						choices.append(_id)
			_card=random.choice(choices)
		elif _card=='shadow':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.spell_school == SpellSchool.SHADOW: 
						choices.append(_id)
			_card=random.choice(choices)
		### HOLY, FEL
		### etc

		elif _card=='armor':
			_card=random.choice(['SW_030','SW_094',])
		elif _card=='attackspell':
			_card=random.choice(['SCH_348','SCH_604','BAR_801','BAR_032'])
		elif _card=='battlecry':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if hasattr(_card, 'battlecry') and _card.battlecry: 
						choices.append(_id)
			_card=random.choice(choices)
		elif _card=='chooseone':
			_card=random.choice(['CORE_EX1_178','CORE_EX1_165','CORE_EX1_573','CORE_EX1_160','CORE_OG_047','CORE_EX1_164','DMF_061',])
		elif _card=='corrupt':
			_card=random.choice(['DMF_124','DMF_082','DMF_073'])
		elif _card=='deathrattle':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.type == CardType.MINION and _card.deathrattle==True: 
						choices.append(_id)
			_card=random.choice(choices)
		elif _card=='noTaunt':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.type == CardType.MINION and _card.taunt==False: 
						choices.append(_id)
			_card=random.choice(choices)
		elif _card=='rush':
			_card=random.choice(['YOP_031'])
		elif _card=='secret':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.type == CardType.SPELL and _card.secret: 
						choices.append(_id)
			_card=random.choice(choices)
		elif _card=='SI7':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.type == CardType.MINION and _card.tags.get(1678): 
						choices.append(_id)
					if _card.id=='SW_411' or _card.id=='SW_413':
						assert _card.tags.get(1678)==1, '_card.SI7_minion'
			_card=random.choice(choices)
		elif _card=='spellpower':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.type == CardType.MINION and hasattr(_card, 'spellpower') and _card.spellpower: 
						choices.append(_id)
			_card=random.choice(choices)
		elif _card=='taunt':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.type == CardType.MINION and _card.taunt: 
						choices.append(_id)
			_card=random.choice(choices)
		elif _card=='tradable':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.tradeable: 
						choices.append(_id)
			_card=random.choice(choices)
		elif _card=='vanilla':
			_card=random.choice(['EX1_554t','EX1_534t','CORE_AT_092','CORE_CS2_120','CORE_CS2_182','CORE_GVG_044','ICC_026t','EX1_110t','FP1_007t',
	'EX1_116t','NEW1_026t','EX1_158t','EX1_160t','EX1_tk9','CORE_KAR_300','CORE_CS2_106','BT_159t','BT_160t','BT_721t',
	'BT_726t','BT_728t','BT_163t','BT_135t','SCH_145','SCH_162t','SCH_224t','SCH_340t','SCH_617t','SCH_612t','DMF_100t',
	'DMF_104t','DMF_061t2','BAR_076t','BAR_077t','BAR_721t2','SW_455t','SW_422t','SW_439t2','DED_517t',
	'DREAM_03','SCH_337t',])####
		elif _card=='vanillaH1':
			_card=random.choice(['EX1_554t','CORE_EX1_506a','ICC_026t','CORE_LOEA10_3','EX1_116t','NEW1_026t','BT_159t','BT_160t','BT_721t','BT_728t','SCH_145','SCH_162t','SCH_224t','SCH_617t','SW_455t','SW_439t2','skele21','DED_517t','CS2_050',])
		elif _card=='vanillaH2':
			_card=random.choice(['EX1_534t','CORE_AT_092','EX1_158t','EX1_160t','EX1_tk9','CORE_KAR_300','BT_135t','SCH_612t','DMF_100t','DMF_061t2','BAR_076t','SW_422t',])
		elif _card=='vanillaH3':
			_card=random.choice(['CORE_CS2_120','DMF_086e','SCH_337t',])
		elif _card=='vanillaA3':
			_card=random.choice(['CORE_GVG_044','EX1_160t','BT_726t','BT_163t','BAR_721t2','SCH_337t',])
		elif _card=='weapon':
			_card=random.choice(['WC_037','DMF_088','DMF_521t'])
		return _card

	def exchange_card(self, card, player, health=0):
		_card = self.card_choice(card)
		Discard(self.player.hand[0]).trigger(player)
		new_card = Give(player,_card).trigger(player)
		return new_card[0][0]
	def append_deck_shuffle(self, card, player):
		_card = self.card_choice(card)
		new_card=Shuffle(player, _card).trigger(player)
		return new_card[0][0]
		pass
	def print_hand(self, player):
		print ("##### %s HAND ####"%(player.name))
		for card in player.hand:
			print("%s "%(card))
		print ("##### %s FIELD ####"%(player.name))
		for card in player.field:
			print("%s "%(card))
		print ("##### %s END ####"%(player.name))
		pass
	def print_stats(self, cat, card, show_buff=False, old_cost=False, show_race=False):
		""" print stats of card
		show_buff: showing all buffs
		old_cost: showing chainge of the cost
		sgiw_race: showing the race of the card
		"""
		if hasattr(card,'atk') and hasattr(card,'health'):
			print ("%s(%s) %r %d/%d (%s) <- %d/%d"%(
				cat, card.controller, card, card.atk, card.health, 
				card.zone,
				card.data.atk, card.data.health),end=" ")
		elif hasattr(card,'atk') and hasattr(card,'durability'):
			print ("%s(%s) %r %d/%d (%s) <- %d/%d"%(
				cat, card.controller, card, card.atk, card.durability, 
				card.zone,
				card.data.atk, card.data.durability),end=" ")
		else: 
			print ("%s(%s) %r cost:%d"%(
				cat, card.controller, card, card.cost),end=" ")
		if old_cost:
			print("(cost:%d<-%d)"%(card.cost, card.data.cost),end="")
		if show_buff and len(card.buffs):
			for buff in card.buffs:
				print("[%r]" % buff,end="")
		if show_race and hasattr(card,'race'):
			print("(race=%r)"%(card.race),end="")
		print("")
		pass
	def play_card(self, card,  player=None, target = None, choose = None):
		if player==None:
			player=card.controller
		if isinstance(card,PlayableCard):
			if choose != None and target!=None and target in choose.targets:
				pass
			else:
				if target!=None and not target in card.targets:
					target=None
				if choose != None and not choose in card.choose_cards:
					choose = None
				pass
			Play(card, target, None, choose).trigger(player)
		pass
	def attack_card(self, card,  target, player=None):
		if player==None:
			player=card.controller
		if isinstance(card,PlayableCard) and isinstance(target, PlayableCard):
			if card.can_attack(target):
				card.attack(target)
		pass
	def cast_spell(self, card, player=None):
		if player==None:
			player=card.controller
		if card.type==CardType.SPELL:
			CastSpell(card).trigger(player)
		pass
	def contains_buff(self, card, buffID):
		for buff in card.buffs:
			if buff.id == buffID:
				return True
		return False
	def card_in_field(self, player, cardID):
		for card in player.field:
			if card.id==cardID:
				return True
		return False
	def activate_heropower(self, player=None, target=None):
		if player==None:
			player=self.player
		player.hero.power.use(target=target)
		pass
	def trade_card(self, card, player=None):
		if player==None:
			player=card.controller
		if card.can_trade()==(True, 0):
			card.trade()
		pass
	def play_location(self, card, player=None, target=None):
		if player==None:
			player=card.controller
		card.location(target=target)
		pass


def PresetGame(pp, testNr=1):
	from fireplace import cards
	if Config.CARD_TEST_SET!='VANILLA':	
		cards.db.initialize()
	else:
		cards.db.classic_initialize()
	for test in range(testNr):
		class1=pp.class1
		class2=pp.class2
		Dummy1=DummyAgent("Dummy1",DummyAgent.DummyAI,myClass=class1)
		Dummy2=DummyAgent("Dummy2",DummyAgent.DummyAI,myClass=class2)
		deck1 = random_draft(Dummy1.myClass,[])#random deck wrt its class
		deck2 = random_draft(Dummy2.myClass,[])#random deck wrt its class
		player1 = Player(Dummy1.name, deck1, Dummy1.myClass.default_hero)
		player2 = Player(Dummy2.name, deck2, Dummy2.myClass.default_hero)
		game = Game(players=(player1, player2))
		# Configurations
		player1._start_hand_size=3## this line must be before 'start()'
		player2._start_hand_size=3## 
		player1.max_mana=9## this line must be before 'start()'
		player2.max_mana=9##
		game.start()
		player1.hero.max_health = 30## this line must be below 'start()'
		player2.hero.max_health = 30## 
		cards_to_mulligan=[]
		player1.choice.choose(*cards_to_mulligan)
		player2.choice.choose(*cards_to_mulligan)
		player1._targetedaction_log=[]
		player2._targetedaction_log=[]
		pp(game.current_player).execute(test)
	pass

class pp_DED_006(Preset_Play):# <12>[1578] 
	""" Mr. Smite
	Your Pirates have [Charge]. """
	def preset_deck(self):
		self.mark1=self.exchange_card('DED_006',self.player)
		self.mark2=self.exchange_card('pirate',self.player)
		self.mark3=self.exchange_card('vanilla',self.player)
		#PutOnTop(player1,'').trigger(player1)#specific card into deck
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		player = self.player
		opponent = player.opponent
		game = player.game
		self.play_card(self.mark2, player)
		self.play_card(self.mark3, player)
		game.end_turn()
		postAction(player)
		game.end_turn()
		postAction(opponent)
		self.play_card(self.mark1, player)
		pass
	def result_inspection(self):
		super().result_inspection()
		if not self.contains_buff(self.mark1, 'DED_006e2'):
			print("not contains_buff(mark1, 'DED_006e2')")
		else:
			print("OK")
		if not self.contains_buff(self.mark2, 'DED_006e2'):
			print("not contains_buff(mark2. 'DED_006e2')")
		else:
			print("OK")
		if self.contains_buff(self.mark3, 'DED_006e2'):
			print("contains_buff(mark3, 'DED_006e2')")
		else:
			print("OK")
		pass

class pp_DED_521(Preset_Play):# <12>[1578] 
	""" Name
	description. """
	def preset_deck(self):
		self.mark1=self.exchange_card('DED_521',self.player)
		self.mark2=self.exchange_card('vanilla',self.player)
		self.mark3=self.exchange_card('vanilla',self.player.opponent)
		self.mark4=self.exchange_card('vanilla',self.player.opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		player = self.player
		opponent = player.opponent
		game = player.game
		self.play_card(self.mark2, player)
		game.end_turn()
		postAction(player)
		self.play_card(self.mark3, opponent)
		self.play_card(self.mark4, opponent)
		game.end_turn()
		postAction(opponent)
		self.play_card(self.mark1, player)
		pass
	def result_inspection(self):
		super().result_inspection()
		count=0
		for action in self.player.targetedaction_log:
			if action['class'].__class__.__name__ == 'Hit':
				print("target = %s"%( action['target']))
				print("amount = %s"%( action['class']._args[1]))
				count += 1
		if count==12:
			print("OK")
		else: 
			print("NO: times of Hit is not 12.")
		pass

class pp_DED_523(Preset_Play):
	""" Golakka Glutton
	[Battlecry:] Destroy a Beast and gain +1/+1. """
	def preset_deck(self):
		self.mark1=self.exchange_card('DED_523',self.player)
		self.mark2=self.exchange_card('vanilla',self.player)
		self.mark3=self.exchange_card('beast',self.player.opponent)
		self.mark4=self.exchange_card('dragon',self.player.opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		player = self.player
		opponent = player.opponent
		game = player.game
		self.play_card(self.mark2, player)
		game.end_turn()
		postAction(player)
		self.play_card(self.mark3, opponent)
		self.play_card(self.mark4, opponent)
		game.end_turn()
		postAction(opponent)
		if self.testNr == 0:
			self.play_card(self.mark1, player, target=self.mark3)
		elif self.testNr == 1:
			self.play_card(self.mark1, player, target=self.mark4)
	def result_inspection(self):
		super().result_inspection()
		if self.testNr == 0:
			assert self.contains_buff(self.mark1, 'DED_523e')==True,'buff'
			print ("OK : contains_buff(mark1, 'DED_523e')")
		elif self.testNr == 1:
			assert self.contains_buff(self.mark1, 'DED_523e')==False, 'buff'
			print ("OK : not contains_buff(mark1, 'DED_523e')")

class pp_DED_524(Preset_Play):
	""" Multicaster
	[Battlecry:] Draw a card for each different spell school_you've cast this game. """
	def preset_deck(self):
		self.mark1=self.exchange_card('DED_524',self.player)
		if self.testNr==0:
			self.mark2=self.exchange_card('arcane',self.player)
			self.mark3=self.exchange_card('vanilla',self.player)
		if self.testNr==1:
			self.mark2=self.exchange_card('arcane',self.player)
			self.mark3=self.exchange_card('nature',self.player)
		if self.testNr==2:
			self.mark2=self.exchange_card('fire',self.player)
			self.mark3=self.exchange_card('frost',self.player)
		#self.mark4=self.exchange_card('spell',self.player)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		player = self.player
		opponent = player.opponent
		game = player.game
		self.play_card(self.mark2, player)
		self.play_card(self.mark3, player)
		if player.choice!=None:
			player.choice=None#somotimes it comes here
		game.end_turn()
		postAction(player)
		if opponent.choice!=None:
			opponent.choice=None#somotimes it comes here
		game.end_turn()
		postAction(opponent)
		self.play_card(self.mark1, player)
	def result_inspection(self):
		super().result_inspection()
		count=0
		for action in self.player.targetedaction_log:
			if action['class'].__class__.__name__ == 'Draw':
				source = action['source']
				if isinstance(source, Player):
					print("name = %s"%( source.name))
					count += 1
		if self.testNr==0:
			if count==2:
				print("OK")
		if self.testNr==1:
			if count==3:
				print("OK")
		if self.testNr==2:
			if count==3:
				print("OK")

#from .darkmoon_druid import SimulateGames_Darkmoon_Druid
#from .alterac_neutral import SimulateGames_Alterac_Neutral
#def SimulateGames():
#	SimulateGames_Alterac_Neutral()
#
#	pass
