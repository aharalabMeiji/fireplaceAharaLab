from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity, PlayReq
from fireplace.actions import Hit, Summon

def sunken_neutral():
	#PresetGame(pp_TID_710)#OK
	#PresetGame(pp_TID_711)#OK
	#PresetGame(pp_TID_712x)#OK
	#PresetGame(pp_TID_712y)#OK
	#PresetGame(pp_TID_713x)#OK
	#PresetGame(pp_TID_713y)#OK
	#PresetGame(pp_TID_744)#OK
	#PresetGame(pp_TSC_017x)#OK
	#PresetGame(pp_TSC_017y)#OK
	#PresetGame(pp_TSC_020)#OK
	#PresetGame(pp_TSC_032x)#OK
	#PresetGame(pp_TSC_032y)#OK
	#PresetGame(pp_TSC_034)#OK
	#PresetGame(pp_TSC_052)#giving up
	PresetGame(pp_TSC_064)#OK
	PresetGame(pp_TSC_067)#
	PresetGame(pp_TSC_069)#
	PresetGame(pp_TSC_638)#
	PresetGame(pp_TSC_641)#
	PresetGame(pp_TSC_641ta)#
	PresetGame(pp_TSC_641tb)#
	PresetGame(pp_TSC_641tc)#
	PresetGame(pp_TSC_641td)#
	PresetGame(pp_TSC_645)#
	PresetGame(pp_TSC_646)#
	PresetGame(pp_TSC_649)#
	PresetGame(pp_TSC_823)#
	PresetGame(pp_TSC_826)#
	PresetGame(pp_TSC_827)#
	#PresetGame(pp_TSC_829)#OK
	#PresetGame(pp_TSC_908)#OK
	#PresetGame(pp_TSC_909)#OK
	#PresetGame(pp_TSC_911)#OK
	#PresetGame(pp_TSC_919)#OK
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

################TSC_002##################

class pp_TSC_002(Preset_Play):
	""" Pufferfist
	After your hero attacks, deal 1 damage to all enemies. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_002',controller)#
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

################TSC_007##################

class pp_TSC_007(Preset_Play):
	""" Gangplank Diver
	[Dormant] for 1 turn.[Rush]. [Immune] while attacking. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_007',controller)#
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

################TSC_013##################

class pp_TSC_013(Preset_Play):
	""" Slimescale Diver
	[Dormant] for 1 turn.[Rush], [Poisonous] """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_013',controller)#
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

################TSC_017##################

class pp_TSC_017x(Preset_Play):
	""" Baba Naga
	[Battlecry:] If you've cast a spell while holding this, deal 3 damage. """
	def preset_deck(self):
		controller=self.player
		opponent=controller.opponent
		self.mark1=self.exchange_card('TSC_017',controller)#
		self.mark2=self.exchange_card('minionH4',opponent)#
		self.mark3=self.exchange_card('spellC3',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark3)
		self.change_turn()
		### opp
		self.play_card(self.mark2)
		self.change_turn()
		### con
		self.play_card(self.mark1, target=self.mark2)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		self.print_stats("opp mark2", self.mark2)
		assert self.mark2.health==self.mark2.data.health-3, "health"
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass
class pp_TSC_017y(Preset_Play):
	""" Baba Naga
	[Battlecry:] If you've cast a spell while holding this, deal 3 damage. """
	def preset_deck(self):
		controller=self.player
		opponent=controller.opponent
		self.mark1=self.exchange_card('TSC_017',controller)#
		self.mark2=self.exchange_card('minionH4',opponent)#
		self.mark3=self.exchange_card('spellC3',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		#self.play_card(self.mark3)
		self.change_turn()
		### opp
		self.play_card(self.mark2)
		self.change_turn()
		### con
		self.play_card(self.mark1, target=self.mark2)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		self.print_stats("opp mark2", self.mark2)
		assert self.mark2.health==self.mark2.data.health, "health"
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################TSC_020##################

class pp_TSC_020(Preset_Play):
	""" Barbaric Sorceress
	[Taunt]. [Battlecry:] Swap the Cost of a random spell in each player's hand. """
	def preset_deck(self):
		controller=self.player
		opponent=controller.opponent
		self.mark1=self.exchange_card('TSC_020',controller)#
		self.mark2=self.exchange_card('spellC3',controller)#
		self.mark3=self.exchange_card('spellC5',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent=controller.opponent
		### con
		for card in controller.hand: 
			if card.type==CardType.SPELL:
				self.print_stats("con hand", card, old_cost=True)
		for card in opponent.hand: 
			if card.type==CardType.SPELL:
				self.print_stats("opp hand", card, old_cost=True)
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent=controller.opponent
		for card in controller.hand: 
			if card.type==CardType.SPELL:
				self.print_stats("con hand", card, old_cost=True)
		for card in opponent.hand: 
			if card.type==CardType.SPELL:
				self.print_stats("opp hand", card, old_cost=True)
		pass

################TSC_032##################

class pp_TSC_032x(Preset_Play):
	""" Blademaster Okani
	[Battlecry:] [Secretly] choose to [Counter] the next minion or spell your opponent plays while this is alive. """
	def preset_deck(self):
		controller=self.player
		opponent=controller.opponent
		self.mark1=self.exchange_card('TSC_032',controller)#
		self.mark2=self.exchange_card('minionH3',opponent)#
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
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.opponent.hand:
			self.print_stats("opponent.hand", card, old_cost=True)
		pass
class pp_TSC_032y(Preset_Play):
	""" Blademaster Okani
	[Battlecry:] [Secretly] choose to [Counter] the next minion or spell your opponent plays while this is alive. """
	def preset_deck(self):
		controller=self.player
		opponent=controller.opponent
		self.mark1=self.exchange_card('TSC_032',controller)#
		self.mark2=self.exchange_card('spellC3',opponent)#
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
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.opponent.hand:
			self.print_stats("opponent.hand", card, old_cost=True)
		pass

################TSC_034##################

class pp_TSC_034(Preset_Play):
	""" Gorloc Ravager
	[Battlecry:] Draw 3 Murlocs. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_034',controller)#
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

################TSC_052##################

class pp_TSC_052(Preset_Play):
	""" School Teacher
	[Battlecry:] Add a 1/1 Nagaling to your hand. [Discover] a spell that costs (3) or less to teach it. """
	def preset_deck(self):
		controller=self.player
		opponent=controller.opponent
		self.mark1=self.exchange_card('TSC_052',controller)#
		self.mark3=(Summon(opponent, self.card_choice('minionH4')).trigger(opponent))[0][0]
		super().preset_deck()
		pass
	def preset_play(self):

		import random
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		for card in controller.hand:
			#self.print_stats("controller.hand", card, old_cost=True)
			if card.id=='TSC_052t':
				self.mark2=card
				break
		self.play_card(self.mark2, target=self.mark3)
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		pass

################TSC_053##################

class pp_TSC_053(Preset_Play):
	""" Rainbow Glowscale
	[Spell Damage +1] """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_053',controller)#
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

################TSC_064##################

class pp_TSC_064(Preset_Play):
	""" Slithering Deathscale
	[Battlecry:] If you've cast three spells while holding this, deal 3 damage to all enemies.@ <i>({0} left!)</i>@ <i>(Ready!)</i> """
	def preset_deck(self):
		from fireplace.actions import Give
		controller=self.player
		opponent=controller.opponent
		self.mark2=self.exchange_card('spellC2',controller)#
		self.mark3=self.exchange_card('spellC2',controller)#
		self.mark4=self.exchange_card('spellC2',controller)#
		self.mark1=(Give(controller,'TSC_064').trigger(controller))[0][0]#
		self.mark5=self.exchange_card('minionH3',opponent)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark2)
		self.play_card(self.mark3)
		self.play_card(self.mark4)
		self.change_turn()
		### opp
		self.play_card(self.mark5)
		self.change_turn()
		### con
		self.play_card(self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################TSC_065##################

class pp_TSC_065(Preset_Play):
	""" Helmet Hermit
	Can't attack. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_065',controller)#
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

################TSC_067##################

class pp_TSC_067(Preset_Play):
	""" Ambassador Faelin
	[Battlecry:] Put 3 [Colossal] minions on the bottom of your deck. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_067',controller)#
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

################TSC_069##################

class pp_TSC_069(Preset_Play):
	""" Amalgam of the Deep
	[Battlecry:] Choose a friendly minion. [Discover] a minionof the same minion type. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_069',controller)#
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

################TSC_632##################

class pp_TSC_632(Preset_Play):
	""" Click-Clocker
	[Divine Shield]. [Battlecry:]Give a random Mech inyour hand +1/+1. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_632',controller)#
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

################TSC_638##################

class pp_TSC_638(Preset_Play):
	""" Piranha Swarmer
	[Rush]After you summon a PiranhaSwarmer, gain +1 Attack. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_638',controller)#
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

################TSC_640##################

class pp_TSC_640(Preset_Play):
	""" Reefwalker
	[Battlecry and Deathrattle:] Summon a 1/1 Piranha Swarmer. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_640',controller)#
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

################TSC_641##################

class pp_TSC_641(Preset_Play):
	""" Queen Azshara
	[Battlecry:] If you've cast three spells while holding this, choose an Ancient Relic.@ <i>({0} left!)</i>@ <i>(Ready!)</i> """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_641',controller)#
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
class pp_TSC_641ta(Preset_Play):
	""" Queen Azshara
	[Battlecry:] If you've cast three spells while holding this, choose an Ancient Relic.@ <i>({0} left!)</i>@ <i>(Ready!)</i> """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_641ta',controller)#
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
class pp_TSC_641tb(Preset_Play):
	""" Queen Azshara
	[Battlecry:] If you've cast three spells while holding this, choose an Ancient Relic.@ <i>({0} left!)</i>@ <i>(Ready!)</i> """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_641tb',controller)#
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
class pp_TSC_641tc(Preset_Play):
	""" Queen Azshara
	[Battlecry:] If you've cast three spells while holding this, choose an Ancient Relic.@ <i>({0} left!)</i>@ <i>(Ready!)</i> """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_641tc',controller)#
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
class pp_TSC_641td(Preset_Play):
	""" Queen Azshara
	[Battlecry:] If you've cast three spells while holding this, choose an Ancient Relic.@ <i>({0} left!)</i>@ <i>(Ready!)</i> """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_641td',controller)#
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

################TSC_645##################

class pp_TSC_645(Preset_Play):
	""" Mothership
	[Rush][Deathrattle:] Summon two random Mechs that cost (3) or less. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_645',controller)#
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

################TSC_646##################

class pp_TSC_646(Preset_Play):
	""" Seascout Operator
	[Battlecry:] If you control a Mech, summon two 2/1 Mechafish. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_646',controller)#
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

################TSC_647##################

class pp_TSC_647(Preset_Play):
	""" Pelican Diver
	[Dormant] for 1 turn.[Rush] """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_647',controller)#
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

################TSC_649##################

class pp_TSC_649(Preset_Play):
	""" Ini Stormcoil
	[Battlecry:] Choose a friendlyMech. Summon a copy of itwith [Rush], [Windfury], and[Divine Shield]. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_649',controller)#
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

################TSC_823##################

class pp_TSC_823(Preset_Play):
	""" Murkwater Scribe
	[Battlecry:] The next spell you play costs (1) less. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_823',controller)#
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

################TSC_826##################

class pp_TSC_826(Preset_Play):
	""" Crushclaw Enforcer
	[Battlecry:] If you've cast a spell while holding this, draw a Naga. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_826',controller)#
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

################TSC_827##################

class pp_TSC_827(Preset_Play):
	""" Vicious Slitherspear
	After you cast a spell,gain +1 Attack untilyour next turn. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_827',controller)#
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

################TSC_829##################

class pp_TSC_829(Preset_Play):
	""" Naga Giant
	Costs (1) less for each Mana you've spent on spells this game. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_829',controller)#
		self.mark2=self.exchange_card('spellC2',controller)#
		self.mark3=self.exchange_card('spellC3',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.print_stats("mark1", self.mark1,old_cost=True)
		self.play_card(self.mark2)
		self.print_stats("mark1", self.mark1,old_cost=True)
		self.play_card(self.mark3)
		self.print_stats("mark1", self.mark1,old_cost=True)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.hand:
			self.print_stats("controller.hand", card, old_cost=True)
		pass

################TSC_908##################

class pp_TSC_908(Preset_Play):
	""" Sir Finley, Sea Guide
	[Battlecry:] Swap yourhand with the bottom of your deck. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_908',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		for card in controller.deck[:4]:
			self.print_stats("deck(bottom)", card)
		for card in controller.hand:
			self.print_stats("hand", card)
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.deck[:4]:
			self.print_stats("deck(bottom)", card)
		for card in controller.hand:
			self.print_stats("hand", card)
		pass

################TSC_909##################

class pp_TSC_909(Preset_Play):
	""" Tuskarrrr Trawler
	[Battlecry:] [Dredge]. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_909',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		for card in controller.deck[:3]:
			self.print_stats("deck(bottom)", card)
		for card in controller.deck[-3:]:
			self.print_stats("deck(top)", card)
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.deck[:3]:
			self.print_stats("deck(bottom)", card)
		for card in controller.deck[-3:]:
			self.print_stats("deck(top)", card)
		print("Check the phenomenon visually.")
		pass

################TSC_911##################

class pp_TSC_911(Preset_Play):
	""" Excavation Specialist
	[Battlecry:] [Dredge].Reduce its Cost by (1). """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_911',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		for card in controller.deck[:3]:
			self.print_stats("deck(bottom)", card)
		for card in controller.deck[-3:]:
			self.print_stats("deck(top)", card)
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.deck[:3]:
			self.print_stats("deck(bottom)", card)
		for card in controller.deck[-3:]:
			self.print_stats("deck(top)", card, old_cost=True)
		print("Check the phenomenon visually.")
		pass

################TSC_919##################

class pp_TSC_919(Preset_Play):
	""" Azsharan Sentinel
	[Taunt]. [Deathrattle:] Put a'Sunken Sentinel' on the bottom of your deck. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_919',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		Hit(self.mark1, 10).trigger(self.player.opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		for card in controller.deck:
			self.print_stats("controller.deck", card)
		assert controller.deck[0].id=='TSC_919t', "deck"
		pass

################TSC_926##################

class pp_TSC_926(Preset_Play):
	""" Smothering Starfish
	[Battlecry:] [Silence] ALL other minions. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_926',controller)#
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

################TSC_928##################

class pp_TSC_928(Preset_Play):
	""" Security Automaton
	After you summon a Mech, gain +1/+1. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_928',controller)#
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

################TSC_935##################

class pp_TSC_935(Preset_Play):
	""" Selfish Shellfish
	[Deathrattle:] Your opponent draws 2 cards. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_935',controller)#
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

################TSC_938##################

class pp_TSC_938(Preset_Play):
	""" Treasure Guard
	[Taunt][Deathrattle:] Draw a card. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_938',controller)#
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

################TSC_960##################

class pp_TSC_960(Preset_Play):
	""" Twin-fin Fin Twin
	[Rush]. [Battlecry:] Summon a copy of this. """
	def preset_deck(self):
		controller=self.player
		self.mark1=self.exchange_card('TSC_960',controller)#
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
