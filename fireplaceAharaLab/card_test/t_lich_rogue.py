from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def lich_rogue():

	PresetGame(pp_RLK_216)##OK
	PresetGame(pp_RLK_217)##OK
	PresetGame(pp_RLK_529)##OK
	PresetGame(pp_RLK_567)##OK
	PresetGame(pp_RLK_568)##OK
	PresetGame(pp_RLK_569)##OK
	PresetGame(pp_RLK_570)##OK
	PresetGame(pp_RLK_571)##OK
	PresetGame(pp_RLK_572)##OK
	PresetGame(pp_RLK_573)##OK
	PresetGame(pp_RLK_573a)##OK
	pass


##########RLK_216##########

class pp_RLK_216(Preset_Play):
	""" Rotten Rodent
	<b>Battlecry:</b> Reduce the Cost of all <b>Deathrattle</b> cards in your deck by (1). """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_216", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		for card in self.controller.deck:
			self.card = card
			if card.type==CardType.MINION and card.has_deathrattle:
				self.assertion("self.card.cost==self.card.data.cost-1#%r"%(self.card))
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.deck:
			self.print_stats("deck", card)
	pass


##########RLK_217##########

class pp_RLK_217(Preset_Play):
	""" Scourge Illusionist
	<b>Deathrattle:</b> Add a 4/4 copy of another <b>Deathrattle</b> minion in your deck to your hand. It costs (4) less. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_217", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.amount=len(self.controller.hand)
		Hit(self.con1, 10).trigger(self.controller)
		self.assertion("len(self.controller.hand)==self.amount+1")
		self.con2 = self.controller.hand[-1]
		self.assertion("self.con2.has_deathrattle==True")
		self.assertion("self.con2.atk==4")
		self.assertion("self.con2.max_health==4")
		self.assertion("self.con2.cost==max(self.con2.data.cost-4,0)")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_529##########

class pp_RLK_529(Preset_Play):
	""" Noxious Infiltrator
	<b>Poisonous</b> <b>Battlecry:</b> If a friendly Undead died after your last turn, deal 1 damage to a minion. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_529", self.controller)
		self.con2=self.exchange_card(self.card_choice("undead"), self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con2)
		self.change_turn()
		### opp
		Hit(self.con2, 10).trigger(self.opponent)
		self.change_turn()
		### con
		self.play_card(self.con1)
		self.assertion("self.opp1.dead==True")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_567##########

class pp_RLK_567(Preset_Play):
	""" Shadow of Demise (spell:0)
	Each time you cast a spell, transform this into a copy of it. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_567", self.controller)
		self.con2=self.exchange_card(self.card_choice("spell"), self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con2)
		self.assertion("not 'RLK_567' in [card.id for card in self.controller.hand]")
		self.assertion("self.con2.id in [card.id for card in self.controller.hand]")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_568##########

class pp_RLK_568(Preset_Play):
	""" Concoctor
	<b>Battlecry:</b> Add a random Concoction to your hand. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_568", self.controller)
		self.con2=self.exchange_card("RLK_568", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.assertion("len([card for card in self.controller.hand if getattr(card, 'concoction')])>0")
		self.play_card(self.con2)
		self.assertion("len([card for card in self.controller.hand if 'RLK_570' in card.id])>0")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_569##########

class pp_RLK_569(Preset_Play):
	""" Potion Belt
	<b>Discover</b> 2 Concoctions. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_569", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.choose_action()
		cards=[self.controller.hand.index(card) for card in self.controller.hand if 'RLK_570' in card.id]
		self.assertion("len([card for card in self.controller.hand if 'RLK_570' in card.id])>0")
		self.con2=self.controller.hand[cards[0]]
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_570##########

class pp_RLK_570(Preset_Play):
	""" Ghoulish Alchemist
	<b>Battlecry</b>: Your next Concoction costs (0). """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_570", self.controller)
		self.con2=self.exchange_card("RLK_569", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con2)
		self.choose_action()
		self.play_card(self.con1)
		cards=[self.controller.hand.index(card) for card in self.controller.hand if 'RLK_570' in card.id]
		self.con2=self.controller.hand[cards[0]]
		self.assertion("self.con2.cost==0")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_571##########

class pp_RLK_571(Preset_Play):
	""" Vile Apothecary
	At the end of your turn, add a random Concoction to your hand. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_571", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		cards=[card for card in self.controller.hand if 'RLK_570' in card.id]
		self.assertion("len([card for card in self.controller.hand if 'RLK_570' in card.id])>0")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_572##########

class pp_RLK_572(Preset_Play):
	""" Potionmaster Putricide
	After a minion dies, add a Concoction to your hand. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_572", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		Hit(self.con4, 10).trigger(self.controller)
		cards=[card for card in self.controller.hand if 'RLK_570' in card.id]
		self.assertion("len([card for card in self.controller.hand if 'RLK_570' in card.id])>0")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_573##########

class pp_RLK_573(Preset_Play):
	""" Ghostly Strike
	Deal $1 damage. <b>Combo:</b> Draw a card. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_573", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.assertion("self.opponent.hero.damage==1")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_573a(Preset_Play):
	""" Ghostly Strike
	Deal $1 damage. <b>Combo:</b> Draw a card. """
	class1=CardClass.ROGUE
	class2=CardClass.ROGUE
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_573", self.controller)
		self.con2=self.exchange_card("RLK_572", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con2)
		self.amount=len(self.controller.hand)
		self.play_card(self.con1)
		self.assertion("len(self.controller.hand)==self.amount")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


