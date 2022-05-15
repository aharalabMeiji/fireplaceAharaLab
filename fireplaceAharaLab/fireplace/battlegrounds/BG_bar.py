from fireplace.game import Game
from fireplace.player import Player
from hearthstone.enums import State, Zone, CardType
from fireplace.config import Config
import random

class BG_Bar(Game):
	def __init__(self, player):
		self.bartender = Player('Bartender', player.starting_deck, 'TB_BaconShopBob')
		self.controller = player
		#self.controller.starting_hero.game=self
		players = (self.bartender, player)
		super().__init__(players)
		self.reroleCost=1
		self.free_rerole=0
		self.parent=None
	pass

	def BG_setup(self):
		if Config.LOGINFO:
			("(BG.Bar.BG_setup)Setting up game %r", self)
		self.state = State.RUNNING
		#self.step = Step.BEGIN_DRAW
		self.zone = Zone.PLAY
		self.players[0].opponent = self.players[1]
		self.players[1].opponent = self.players[0]
		for player in self.players:
			player.zone = Zone.PLAY
			self.manager.new_entity(player)
		#print("S", end=':')
		first, second = self.controller, self.bartender
		self.player1 = first
		self.player1.first_player = True
		self.player2 = second
		self.player2.first_player = False
		#print("S", end=':')

		for player in self.players:
			#print("S(%s)(%s)"%(player,player.starting_hero), end=':')
			player.summon(player.starting_hero)
			#print("S", end=':')
			armor_grade = player.hero.data.tags.get(1723)
			if armor_grade != 1 and armor_grade != None:
				player.hero.armor = random.randint(armor_grade, armor_grade+3)
			#player.playstate = PlayState.PLAYING
		self.manager.start_game()
		pass

	def BG_find_double(self):
		## in any way, we find one double
		# except spell cards(coins, golds, bananas)
		characters=[]
		for card in self.controller.field:
			characters.append(card.id)
		for card in self.controller.hand:
			if card.type==CardType.MINION:
				characters.append(card.id)
		for id in characters:
			count=0
			for jd in characters:
				if id==jd:
					count+=1
					if count>=2:
						return id
				pass
			pass
		return None


	def BG_find_triple(self):
		## in any way, we find one triple
		# except spell cards(coins, golds, bananas)
		characters=[]
		for card in self.controller.field:
			characters.append(card.id)
		for card in self.controller.hand:
			if card.type==CardType.MINION:
				characters.append(card.id)
		for id in characters:
			count=0
			for jd in characters:
				if id==jd:
					count+=1
					if count>=3:
						return id
				pass
			pass
		return None
		pass

	def BG_deal_gold(self, id):
		if not id:
			return
		gold_id = self.parent.BG_Gold[id] ## to find a buf
		#gold_id = self.parent.BG_Gold.get(id, 0)
		if not gold_id:
			return
		buffs = []
		for card in self.controller.field + self.controller.hand:
			if card.id==id:
				buffs += card.buffs
				decks = self.parent.BG_decks
				gr = card.tech_level-1
				#decks[gr].append(card.id) #no need to back to deck
				card.zone=Zone.GRAVEYARD
		newcard = self.controller.card(gold_id)
		for buff in buffs:## inferit all buffs
			buff.apply(newcard)
		print("Gold card!!! by %s"%(self.controller))
		newcard.zone = Zone.HAND # do we need this line?
		return newcard

	def BG_morph_gold(self, card):
		if not card:
			return
		controller = card.controller
		index = controller.field.index(card)
		if not card in controller.field:
			return
		gold_id = self.parent.BG_Gold[card.id]
		if not gold_id:
			return
		buffs=[]
		for buff in card.buffs:## inferit buffs
			buffs.append(buff)
		card.zone=Zone.GRAVEYARD
		newcard = controller.card(gold_id)
		for buff in buffs:## inferit buffs
			buff.apply(newcard)
		newcard._summon_index=index
		newcard.zone = Zone.PLAY #something wrong? 
		return newcard
