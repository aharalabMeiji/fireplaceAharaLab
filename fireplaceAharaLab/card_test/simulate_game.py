from hearthstone.enums import CardClass,BlockType, CardType ,PlayState, State, Race, SpellSchool
from fireplace.game import Game
from fireplace.card import Card, PlayableCard
from fireplace.actions import *
from fireplace.utils import random_draft
from fireplace.player import Player
import random
from agent_Standard import *
from utils import postAction


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
		pass
	def preset_deck(self):
		#self.print_hand(self.player)
		#self.print_hand(self.player.opponent)
		#print ("")
		#print ("")
		#print ("")
		#print ("")
		Config.LOGINFO_LOG=[]
		pass
	def preset_play(self):
		pass
	def result_inspection(self):
		#self.print_hand(self.player)
		#self.print_hand(self.player.opponent)
		pass
	def change_turn(self, player=None):
		if player==None:
			player=self.current
		game = player.game
		if player.choice!=None:
			postAction(player)
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
		if _card=='arcane':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.spell_school == SpellSchool.ARCANE: 
						choices.append(_id)
			_card=random.choice(choices)		
		if _card=='armor':
			_card=random.choice(['SW_030','SW_094',])
		if _card=='attackspell':
			_card=random.choice(['SCH_348','SCH_604','BAR_801','BAR_032'])
		if _card=='beast':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.race == Race.BEAST: 
						choices.append(_id)
			_card=random.choice(choices)
		if _card=='chooseone':
			_card=random.choice(['CORE_EX1_178','CORE_EX1_165','CORE_EX1_573','CORE_EX1_160','CORE_OG_047','CORE_EX1_164','DMF_061',])
		if _card=='corrupt':
			_card=random.choice(['DMF_124','DMF_082','DMF_073'])
		if _card=='deathrattle':
			_card=random.choice(['SW_070','CORE_FP1_007','CORE_EX1_012'])
		if _card=='dragon':
			_card=random.choice(['CORE_EX1_189','CORE_LOOT_137','CS3_031','CS3_032','CS3_033','CS3_034','CS3_035','CS3_036','EX1_116t','CORE_AT_008','BT_726',\
					   'SCH_162t','SCH_230','SCH_232','SCH_711','YOP_034','YOP_025','YOP_025t','DMF_528','DREAM_03',])
		if _card=='elemental':
			_card=random.choice(['CORE_AT_092','CORE_EX1_187','CORE_EX1_249','CORE_KAR_036','CORE_UNG_813','CORE_CS2_033','BT_155','BT_155t','BT_735','SCH_143',\
						'SCH_245','DMF_044','DMF_062','DMF_190','YOP_021','DMF_100','DMF_100t','DMF_101','DMF_059','BAR_042','BAR_854','BAR_545','SW_111',])
		if _card=='fire':
			_card=random.choice(['CORE_EX1_610','CORE_CS2_029','CORE_CS2_032','SCH_348','DMF_104','BAR_546','SW_107','SW_108','SW_108t','SW_110','SW_462','CORE_EX1_610',])
		if _card=='frost':
			_card=random.choice(['CORE_EX1_611','CORE_EX1_275','CORE_EX1_289','CORE_GIL_801','BT_072','SCH_509','BAR_305','BAR_305t','BAR_305t2','BAR_812','WC_041',])
		if _card=='mech':
			_card=random.choice(['CORE_GVG_085','CORE_GVG_076','CORE_GVG_044'])
		if _card=='minionH4':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.type == CardType.MINION and hasattr(_card,'health') and _card.health==4: 
						choices.append(_id)
			_card=random.choice(choices)
		if _card=='minionA4':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.type == CardType.MINION and _card.atk==4: 
						choices.append(_id)
			_card=random.choice(choices)
		if _card=='minionH5':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.type == CardType.MINION and hasattr(_card,'health') and _card.health==5: 
						choices.append(_id)
			_card=random.choice(choices)
		if _card=='minionA5':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.type == CardType.MINION and _card.atk==5: 
						choices.append(_id)
			_card=random.choice(choices)
		if _card=='minionH6':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.type == CardType.MINION and hasattr(_card,'health') and _card.health==6: 
						choices.append(_id)
			_card=random.choice(choices)
		if _card=='minionA6':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.type == CardType.MINION and _card.atk==6: 
						choices.append(_id)
			_card=random.choice(choices)
		if _card=='murloc':
			_card=random.choice(['BAR_063','BAR_062','WC_030'])
		if _card=='nature':
			_card=random.choice(['CORE_BOT_420','CORE_CS2_009','CORE_CS2_013','CORE_EX1_158','CORE_EX1_164','EX1_164a','EX1_164b','CORE_EX1_169','CORE_EX1_571',\
						'BT_128','BT_129','BT_130','BT_132','SCH_333','SCH_427','SCH_612','YOP_015','DMF_058','DMF_732','YOP_026','BAR_533','BAR_536','BAR_549',\
						'SW_422','SW_437','DREAM_02','DREAM_04','CORE_EX1_169',])
		if _card=='noTaunt':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.type == CardType.MINION and _card.taunt==False: 
						choices.append(_id)
			_card=random.choice(choices)
		if _card=='pirate':
			_card=random.choice(['CS3_022','CORE_NEW1_018','BAR_081'])
		if _card=='rush':
			_card=random.choice(['YOP_031'])
		if _card=='secret':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.type == CardType.SPELL and _card.secret: 
						choices.append(_id)
			_card=random.choice(choices)
		if _card=='spell':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.type == CardType.SPELL: 
						choices.append(_id)
			_card=random.choice(choices)
		if _card=='spellC4':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.type == CardType.SPELL and _card.cost==4: 
						choices.append(_id)
			_card=random.choice(choices)
		if _card=='spellpower':
			_card=random.choice(['CORE_CS2_142','CORE_EX1_012','CORE_GVG_109','CS3_001','BT_008t','BT_028','SCH_245','SCH_310','YOP_021','SW_061','CS2_052',])
		if _card=='taunt':
			choices=[]
			for cardIDlist in All:
				for _id in cardIDlist:
					_card = cards.db[_id]
					if _card.type == CardType.MINION and _card.taunt: 
						choices.append(_id)
			_card=random.choice(choices)
		if _card=='totem':
			_card=random.choice(['CORE_EX1_575','SCH_537','SCH_612t','CS2_050','CS2_051','CS2_052','NEW1_009'])
		if _card=='vanilla':
			_card=random.choice(['EX1_554t','EX1_534t','CORE_AT_092','CORE_CS2_120','CORE_CS2_182','CORE_GVG_044','ICC_026t','EX1_110t','FP1_007t',
	'EX1_116t','NEW1_026t','EX1_158t','EX1_160t','EX1_tk9','CORE_KAR_300','CORE_CS2_106','BT_159t','BT_160t','BT_721t',
	'BT_726t','BT_728t','BT_163t','BT_135t','SCH_145','SCH_162t','SCH_224t','SCH_340t','SCH_617t','SCH_612t','DMF_100t',
	'DMF_104t','DMF_061t2','BAR_076t','BAR_077t','BAR_721t2','SW_455t','SW_422t','SW_439t2','DED_517t',
	'DREAM_03','SCH_337t',])####
		if _card=='vanillaH1' or _card=='minionH1':
			_card=random.choice(['EX1_554t','CORE_EX1_506a','ICC_026t','CORE_LOEA10_3','EX1_116t','NEW1_026t','BT_159t','BT_160t','BT_721t','BT_728t','SCH_145','SCH_162t','SCH_224t','SCH_617t','SW_455t','SW_439t2','skele21','DED_517t','CS2_050',])
		if _card=='vanillaH2' or _card=='minionH2':
			_card=random.choice(['EX1_534t','CORE_AT_092','EX1_158t','EX1_160t','EX1_tk9','CORE_KAR_300','BT_135t','SCH_612t','DMF_100t','DMF_061t2','BAR_076t','SW_422t',])
		if _card=='vanillaH3' or _card=='minionH3':
			_card=random.choice(['CORE_CS2_120','DMF_086e','SCH_337t',])
		if _card=='vanillaA3':
			_card=random.choice(['CORE_GVG_044','EX1_160t','BT_726t','BT_163t','BAR_721t2','SCH_337t',])
		if _card=='minionH7':
			_card=random.choice(['CORE_CS2_181','CORE_CS2_222','CORE_EX1_190','CORE_EX1_249','CORE_FP1_031','CORE_AT_008','SCH_709','SCH_709t','SCH_710','DMF_002','DMF_068','BAR_021','BAR_027','BAR_721t2','BAR_538t','WC_006','SW_078','SW_081','SW_322t4','SW_450t4','SW_429t','SW_028t5','SW_024',])
		if _card=='minionH8':
			_card=random.choice(['CORE_EX1_543','CORE_EX1_187','CORE_EX1_399','CORE_GVG_121','CORE_UNG_813','CORE_UNG_844','CS3_031','CS3_032','CS3_035','CORE_EX1_573','BT_720','BT_138','SCH_711','SCH_717','SCH_400','DMF_080t','DMF_104t','BAR_071','BAR_072t','BAR_547','SW_068','SW_428t4','DED_521','DED_525','AV_132','AV_141t','SCH_337','SW_068',])
		if _card=='minionA7':
			_card=random.choice(['CORE_EX1_543','CORE_CS2_222','CORE_EX1_249','CORE_GVG_121','CS3_031','CS3_032','CS3_035','CS3_036','BT_155','BT_155t','BT_728t','BT_734','BT_735','BT_850','BT_028t','BT_133','BT_136t','BT_136tt','BT_136tt2','BT_136tt3','BT_123t','SCH_711','DMF_004','DMF_080t','DMF_188','YOP_034','DMF_085','DMF_104t','DMF_059','BAR_079_m3','BAR_547','BAR_538','SW_068','SW_081','SW_322t4','SW_450t4','SW_428t4','SW_028t5','DED_521','DED_525','AV_130','AV_132','AV_141t','AV_704','DREAM_03','SW_024','SW_068','SCH_621',])
		if _card=='weapon':
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
			print ("%s(%s): %r(%s): %d/%d (%s) <- %d/%d"%(
				cat, card.controller, card, card.id, card.atk, card.health, 
				card.zone,
				card.data.atk, card.data.health),end=" ")
		elif hasattr(card,'atk') and hasattr(card,'durability'):
			print ("%s(%s): %r: %d/%d (%s) <- %d/%d"%(
				card, card.controller, card, card.atk, card.durability, 
				card.zone,
				card.data.atk, card.data.durability),end=" ")
		else: 
			print ("%s(%s): %r: cost:%d"%(
				cat, card.controller, card, card.cost),end=" ")
		if old_cost:
			print("(cost:%d<-%d)"%(card.cost, card.data.cost),end="")
		if show_buff and len(card.buffs):
			for buff in card.buffs:
				print("[%r]" % buff,end="")
		if show_race:
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
	def cast_spell(self, card, player):
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
	def activate_heropower(self, player, target=None):
		player.hero.power.use(target=target)
		pass


def PresetGame(pp, testNr=1):
	from fireplace import cards
	cards.db.initialize()
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
			if self.contains_buff(self.mark1, 'DED_523e'):
				print ("OK : contains_buff(mark3, 'DED_523e')")
			else:
				print ("NG")
		elif self.testNr == 1:
			if not self.contains_buff(self.mark1, 'DED_523e'):
				print ("OK : not contains_buff(mark3, 'DED_523e')")
			else:
				print ("NG")

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
