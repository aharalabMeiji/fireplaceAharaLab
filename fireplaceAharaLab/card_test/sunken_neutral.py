from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity
from fireplace.actions import Hit, Summon

def sunken_neutral():
	#PresetGame(pp_TID_710)#
	PresetGame(pp_TID_711)#
	pass

################TID_710##################

class pp_TID_710(Preset_Play):
	""" Snapdragon
	[Battlecry:] Give all[Battlecry] minions in your deck +1/+1. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TID_710',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.deck:
			if card.has_battlecry:
				assert card.buffs[0].id=='TID_710e', "buff"
			else:
				assert card.buffs==[], "buffs"
			self.print_stats("deck", card, show_buff=True)
		pass

################TID_711##################

class pp_TID_711(Preset_Play):
	""" Ozumat
	[Colossal +6] [Deathrattle:] For each of Ozumat's Tentacles, destroy   a random enemy minion. """
	def preset_deck(self):
		controller=self.player
		opponent=controller.opponent
		self.mark1=self.exchange_card('TID_711',controller)#
		Summon(opponent, self.card_choice('minionH4')).trigger(opponent)
		Summon(opponent, self.card_choice('minionH4')).trigger(opponent)
		Summon(opponent, self.card_choice('minionH4')).trigger(opponent)
		Summon(opponent, self.card_choice('minionH4')).trigger(opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		opponent = self.player.opponent
		for card in opponent.field:
			self.print_stats("opp. field", card)
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		Hit(self.mark1, 10).trigger(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		opponent = self.player.opponent
		for card in opponent.field:
			self.print_stats("opp. field", card)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################XXXX##################

class pp_XXXX(Preset_Play):
	""" T
	M"""
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('XXXX',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass


##################################1
