from fireplace.game import Game
from fireplace.player import Player
from hearthstone.enums import State, Zone

class BG_Bar(Game):
	def __init__(self, player):
		self.bartender = Player('Bartender', player.starting_deck, 'TB_BaconShopBob')
		self.controller = player
		#self.controller.starting_hero.game=self
		players = (self.bartender, player)
		super().__init__(players)
		self.reroleCost=1
		self.parent=None

	pass

	def BG_setup(self):
		self.log("Setting up game %r", self)
		self.state = State.RUNNING
		#self.step = Step.BEGIN_DRAW
		self.zone = Zone.PLAY
		self.players[0].opponent = self.players[1]
		self.players[1].opponent = self.players[0]
		for player in self.players:
			player.zone = Zone.PLAY
			self.manager.new_entity(player)

		first, second = self.controller, self.bartender
		self.player1 = first
		self.player1.first_player = True
		self.player2 = second
		self.player2.first_player = False

		for player in self.players:
			player.summon(player.starting_hero)
			#player.playstate = PlayState.PLAYING
		self.manager.start_game()


