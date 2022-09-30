from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def rev_mage():

	#PresetGame(pp_MAW_006)##
	#PresetGame(pp_MAW_013)##
	#PresetGame(pp_MAW_101)##
	#PresetGame(pp_REV_000)##
	#PresetGame(pp_REV_504)##
	#PresetGame(pp_REV_505)##
	#PresetGame(pp_REV_513)##
	#PresetGame(pp_REV_514)##
	#PresetGame(pp_REV_515)##
	#PresetGame(pp_REV_516)##
	#PresetGame(pp_REV_601)##
	#PresetGame(pp_REV_602)##
	#PresetGame(pp_REV_786)##
	#PresetGame(pp_REV_796)##
	#PresetGame(pp_REV_840)##
	#PresetGame(pp_REV_841e2)##
	pass


##########MAW_006##########

class pp_MAW_006(Preset_Play):
	""" Objection!
	<b>Secret:</b> When your opponent plays a _minion, <b>Counter</b> it. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_006", self.controller)
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
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########MAW_013##########

class pp_MAW_013(Preset_Play):
	""" Life Sentence
	Remove a minion from the game. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_013", self.controller)
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
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########MAW_101##########

class pp_MAW_101(Preset_Play):
	""" Contract Conjurer
	Costs (3) less for each <b>Secret</b> you control. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("MAW_101", self.controller)
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
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########REV_000##########

class pp_REV_000(Preset_Play):
	""" Suspicious Alchemist
	<b>Battlecry:</b> <b>Discover</b> a spell. If your opponent guesses your choice, they get a copy. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_000", self.controller)
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
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########REV_504##########

class pp_REV_504(Preset_Play):
	""" Solid Alibi
	Until your next turn, your hero can only take 1 damage at a time. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_504", self.controller)
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
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########REV_505##########

class pp_REV_505(Preset_Play):
	""" Cold Case
	Summon two 2/2 Volatile Skeletons. Gain 4 Armor. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_505", self.controller)
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
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########REV_513##########

class pp_REV_513(Preset_Play):
	""" Chatty Bartender
	At the end of your turn, if you control a <b>Secret</b>, deal 2 damage to all enemies. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_513", self.controller)
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
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########REV_514##########

class pp_REV_514(Preset_Play):
	""" Kel'Thuzad, the Inevitable
	<b>Battlecry:</b> Resurrect your  Volatile Skeletons. Any that  can't fit on the battlefield  instantly explode! @<i>(@)</i> """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_514", self.controller)
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
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########REV_515##########

class pp_REV_515(Preset_Play):
	""" Orion, Mansion Manager
	After a friendly <b>Secret</b> is revealed, cast a different Mage <b>Secret</b> and gain +2/+2. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_515", self.controller)
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
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########REV_516##########

class pp_REV_516(Preset_Play):
	""" Vengeful Visage
	<b>Secret:</b> After an enemy minion attacks your hero, summon a copy of it to attack the enemy hero. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_516", self.controller)
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
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########REV_601##########

class pp_REV_601(Preset_Play):
	""" Frozen Touch
	Deal $3 damage. <b>Infuse (@):</b> Add a Frozen Touch to your hand. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_601", self.controller)
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
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########REV_602##########

class pp_REV_602(Preset_Play):
	""" Nightcloak Sanctum
	<b>Freeze</b> a minion. Summon a 2/2 Volatile Skeleton. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_602", self.controller)
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
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########REV_786##########

class pp_REV_786(Preset_Play):
	""" Kel'Thuzad, the Inevitable
	{0} {1} {2} {3} """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_786", self.controller)
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
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########REV_796##########

class pp_REV_796(Preset_Play):
	""" Nightcloak Sanctum
	{0} {1} """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_796", self.controller)
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
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########REV_840##########

class pp_REV_840(Preset_Play):
	""" Deathborne
	Deal $2 damage to all minions. Summon a 2/2 Volatile Skeleton  for each killed. """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_840", self.controller)
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
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########REV_841e2##########

class pp_REV_841e2(Preset_Play):
	""" Informed
	Your next Secret costs (0). """
	class1=CardClass.MAGE
	class2=CardClass.MAGE
	def preset_deck(self):
		self.con1=self.exchange_card("REV_841e2", self.controller)
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
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


