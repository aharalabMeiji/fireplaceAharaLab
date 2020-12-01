from .card import Spell
from hearthstone.enums import CardType, MultiClassGroup, PlayReq, PlayState, \
	Race, Rarity, Step, Zone

class Sidequest(Spell):
	sidequestCounter=0
	@property
	def events(self):
		ret = super().events
		if self.zone == Zone.SECRET:
			ret += self.data.scripts.secret
		return ret

	@property
	def exhausted(self):
		return self.zone == Zone.SECRET and self.controller.current_player

	@property
	def zone_position(self):
		if self.zone == Zone.SECRET:
			return self.controller.secrets.index(self) + 1
		return super().zone_position

	def _set_zone(self, value):
		if value == Zone.PLAY:
			# Move secrets to the SECRET Zone when played
			value = Zone.SECRET
		if self.zone == Zone.SECRET:
			self.controller.secrets.remove(self)
		if value == Zone.SECRET:
			self.controller.secrets.append(self)
		super()._set_zone(value)

	def is_summonable(self):
		# secrets are all unique
		if self.controller.secrets.contains(self):
			return False
		return super().is_summonable()

	def play(self, target=None, index=None, choose=None):
		self.controller.times_secret_played_this_game += 1
		return super().play(target, index, choose)
