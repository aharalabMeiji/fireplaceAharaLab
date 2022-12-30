from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give, Draw
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def lich_priest():

	#PresetGame(pp_RLK_812)##OK
	#PresetGame(pp_RLK_812a)##OK
	#PresetGame(pp_RLK_813)##OK
	#PresetGame(pp_RLK_814)##OK
	#PresetGame(pp_RLK_815)##OK
	#PresetGame(pp_RLK_816)##OK
	#PresetGame(pp_RLK_816a)##OK
	#PresetGame(pp_RLK_822)##OK
	#PresetGame(pp_RLK_823)##OK
	#PresetGame(pp_RLK_829)##OK
	#PresetGame(pp_RLK_832)##OK
	#PresetGame(pp_RLK_845)##OK
	pass


##########RLK_812##########

class pp_RLK_812(Preset_Play):
	""" Animate Dead
	Resurrect a friendly minion that costs (3) or less. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_812", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionC3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		Hit(self.con4, 10).trigger(self.controller)
		self.play_card(self.con1)
		self.assertion("self.con4.id in [card.id for card in self.controller.field]")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_812a(Preset_Play):
	""" Animate Dead
	Resurrect a friendly minion that costs (3) or less. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_812", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionC4")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		Hit(self.con4, 10).trigger(self.controller)
		self.play_card(self.con1)
		self.assertion("not self.con4.id in [card.id for card in self.controller.field]")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_813##########

class pp_RLK_813(Preset_Play):
	""" Bonecaller
	<b>Taunt</b> <b>Deathrattle</b>: Resurrect a friendly Undead that died this game. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_813", self.controller)
		self.con4=Summon(self.controller, self.card_choice("undead")).trigger(self.controller)
		self.con4=self.con4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		Hit(self.con4, 10).trigger(self.controller)
		self.play_card(self.con1)
		self.change_turn()
		### opp
		Hit(self.con1, 10).trigger(self.opponent)
		self.assertion("self.con4.id in [card.id for card in self.controller.field]")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_814##########

class pp_RLK_814(Preset_Play):
	""" Crystalsmith Cultist
	<b>Battlecry:</b> If you're holding a Shadow spell, gain +1/+1. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_814", self.controller)
		self.con2=self.exchange_card(self.card_choice("shadow"), self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.assertion("'RLK_814e' in [card.id for card in self.con1.buffs]")
		self.assertion("self.con1.atk==self.con1.data.atk+1")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_815##########

class pp_RLK_815(Preset_Play):
	""" Shadow Word: Undeath
	Deal $2 damage to all enemies. If a friendly Undead died after your last turn, deal $2 more. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_815", self.controller)
		self.con4=Summon(self.controller, self.card_choice("undead")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH5")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.assertion("self.opp1.damage==2")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_815a(Preset_Play):
	""" Shadow Word: Undeath
	Deal $2 damage to all enemies. If a friendly Undead died after your last turn, deal $2 more. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_815", self.controller)
		self.con4=Summon(self.controller, self.card_choice("undead")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH5")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.change_turn()
		### opp
		Hit(self.con4, 10).trigger(self.opponent)
		self.change_turn()
		### con
		self.play_card(self.con1)
		self.assertion("self.opp1.damage==4")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_816##########

class pp_RLK_816(Preset_Play):
	""" Sister Svalna
	<b>Battlecry:</b> <i>Permanently</i> add a Vision of Darkness to your hand. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_816", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.assertion("'RLK_816t3' in [card.id for card in self.controller.hand]")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_816a(Preset_Play):
	""" Sister Svalna
	<b>Battlecry:</b> <i>Permanently</i> add a Vision of Darkness to your hand. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_816t3", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.choose_action()
		self.assertion("'RLK_816t3' in [card.id for card in self.controller.hand]")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_822##########

class pp_RLK_822(Preset_Play):
	""" Haunting Nightmare
	<b>Deathrattle:</b> Haunt a card in your hand. When you play it, summon a 3/3 Soldier. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_822", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		Hit(self.con1, 10).trigger(self.controller)
		for card in self.controller.hand:
			if 'RLK_822e' in [bf.id for bf in card.buffs]:
				self.con2=card
		self.assertion("self.con2!=None")
		self.play_card(self.con2)
		self.assertion("'RLK_822t' in [card.id for card in self.controller.field]")
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_823##########

class pp_RLK_823(Preset_Play):
	""" Undying Allies
	After you play an Undead this turn, give it <b>Reborn</b>. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_823", self.controller)
		self.con2=self.exchange_card(self.card_choice("undead"), self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.play_card(self.con2)
		self.assertion("self.con2.reborn==True")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_829##########

class pp_RLK_829(Preset_Play):
	""" Grave Digging
	Draw 2 cards. Costs (1) if a friendly Undead died after your last turn. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_829", self.controller)
		self.con4=Summon(self.controller, self.card_choice("undead")).trigger(self.controller)
		self.con4=self.con4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.change_turn()
		### opp
		Hit(self.con4, 10).trigger(self.opponent)
		self.change_turn()
		### con
		self.play_card(self.con1)
		self.cards=[action for action in self.controller._targetedaction_log if isinstance(action['class'], Draw)==True and action['turn']==3]
		self.assertion("len(self.cards)==3")
		self.assertion("self.controller.hand[-2].cost==1")
		self.assertion("self.controller.hand[-1].cost==1")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_832##########

class pp_RLK_832(Preset_Play):
	""" High Cultist Basaleph
	<b>Battlecry:</b> Resurrect all friendly Undead that died after your last turn. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_832", self.controller)
		self.con4=(Summon(self.controller, self.card_choice("undead")).trigger(self.controller))[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.change_turn()
		### opp
		Hit(self.con4, 10).trigger(self.opponent)
		self.change_turn()
		### con
		self.play_card(self.con1)
		self.assertion("self.con4.id in [card.id for card in self.controller.field]")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_845##########

class pp_RLK_845(Preset_Play):
	""" Mind Eater
	<b>Deathrattle:</b> Add a copy of a card in your opponent's deck to your hand. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_845", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.amount=len(self.controller.hand)
		Hit(self.con1, 10).trigger(self.controller)
		self.assertion("len(self.controller.hand)==self.amount+1")
		self.con2=self.controller.hand[-1]
		self.assertion("self.con2.id in [card.id for card in self.opponent.deck]")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


