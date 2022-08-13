from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity
from fireplace.actions import Hit, Summon

def sunken_neutral():
	#PresetGame(pp_TID_710)#OK
	#PresetGame(pp_TID_711)#OK
	#PresetGame(pp_TID_712x)#OK
	#PresetGame(pp_TID_712y)#OK
	#PresetGame(pp_TID_713x)#OK
	#PresetGame(pp_TID_713y)#OK
	PresetGame(pp_TID_744)#OK
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

################TID_712##################

class pp_TID_712x(Preset_Play):
	""" Neptulon the Tidehunter
	[Colossal +2], [Rush], [Windfury]Whenever Neptulon attacks,if you control any Hands,they attack instead. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TID_712',controller)#
		opponent=controller.opponent
		self.mark2=(Summon(opponent, self.card_choice('minionH3')).trigger(opponent))[0][0]
		for card in controller.hand:
			self.print_stats("controller.hand", card)
		for card in opponent.field:
			self.print_stats("opponent.field", card)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		for card in self.player.hand:
			self.print_stats("controller.field", card)
		self.change_turn()
		### opp
		self.change_turn()
		### con
		self.attack_card(self.mark1, self.mark2)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		print("Check the followings")
		print("TID_712t and TID_712t2 attack the target. ")
		print("TID_712 itself does not attack anything.")
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass
class pp_TID_712y(Preset_Play):
	""" Neptulon the Tidehunter
	[Colossal +2], [Rush], [Windfury]Whenever Neptulon attacks,if you control any Hands,they attack instead. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TID_712',controller)#
		opponent=controller.opponent
		self.mark2=(Summon(opponent, self.card_choice('minionH6')).trigger(opponent))[0][0]
		for card in controller.hand:
			self.print_stats("controller.hand", card)
		for card in opponent.field:
			self.print_stats("opponent.field", card)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		for card in self.player.hand:
			self.print_stats("controller.field", card)
		self.change_turn()
		### opp
		self.change_turn()
		### con
		self.attack_card(self.mark1, self.mark2)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		print("Check the followings")
		print("TID_712t and TID_712t2 attack the target. ")
		print("TID_712 itself does not attack anything.")
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################TID_713##################

class pp_TID_713x(Preset_Play):
	""" Bubbler
	After this minion takes exactly one damage, destroy it. <i>(Pop!)</i> """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TID_713',controller)#
		opponent=controller.opponent
		self.mark2=self.exchange_card('minionA1',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.play_card(self.mark2)
		self.change_turn()
		### con
		self.change_turn()
		### opp
		self.attack_card(self.mark2, self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		assert self.mark1.zone==Zone.GRAVEYARD, "dead"
		for card in controller.field:
			self.print_stats("controller.field", card, old_cost=True)
		pass
class pp_TID_713y(Preset_Play):
	""" Bubbler
	After this minion takes exactly one damage, destroy it. <i>(Pop!)</i> """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TID_713',controller)#
		opponent=controller.opponent
		self.mark2=self.exchange_card('minionA2',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.play_card(self.mark2)
		self.change_turn()
		### con
		self.change_turn()
		### opp
		self.attack_card(self.mark2, self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		assert self.mark1.zone!=Zone.GRAVEYARD, "not dead"
		for card in controller.field:
			self.print_stats("controller.field", card, old_cost=True)
		pass

################TID_744##################

class pp_TID_744(Preset_Play):
	""" Coilfang Constrictor
	[Battlecry:] Look at 3 cards in your opponent's hand and choose one. It can't be played next turn. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TID_744',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		opponent=self.player.opponent
		for card in opponent.hand:
			self.print_stats("opponent.hand", card)
			print("----> card.cant_play=%s"%(card.cant_play))
			if card.cant_play:
				self.play_card(card)
		self.change_turn()
		### con
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent=self.player.opponent
		for card in opponent.hand:
			self.print_stats("opponent.hand", card)
			print("----> card.cant_play=%s"%(card.cant_play))
		pass

################TSC_001##################

class pp_TSC_001(Preset_Play):
	""" Naval Mine
	[Deathrattle:] Deal 4 damage to the enemy hero. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_001',controller)#
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
