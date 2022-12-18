from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def lich_paladin():

	#PresetGame(pp_RLK_527)##
	#PresetGame(pp_RLK_916)##
	#PresetGame(pp_RLK_917)##
	#PresetGame(pp_RLK_918)##
	#PresetGame(pp_RLK_919)##
	#PresetGame(pp_RLK_921)##
	#PresetGame(pp_RLK_922)##
	#PresetGame(pp_RLK_923)##
	#PresetGame(pp_RLK_924)##
	#PresetGame(pp_RLK_927)##
	#PresetGame(pp_RLK_Prologue_Anasterian_003t)##
	#PresetGame(pp_RLK_Prologue_Arthas_001hp)##
	#PresetGame(pp_RLK_Prologue_Arthas_001p)##
	#PresetGame(pp_RLK_Prologue_Gavinrad_002t)##
	#PresetGame(pp_RLK_Prologue_Lightbringer_003e)##
	#PresetGame(pp_RLK_Prologue_Lightbringer_003w)##
	#PresetGame(pp_RLK_Prologue_Uther_002hb)##
	#PresetGame(pp_RLK_Prologue_Uther_002p)##
	pass


##########RLK_527##########

class pp_RLK_527(Preset_Play):
	""" Timewarden
	<b>Battlecry:</b> Until the end of your next turn, Dragons you summon gain <b>Taunt</b> and <b>Divine Shield</b>. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_527", self.controller)
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


##########RLK_916##########

class pp_RLK_916(Preset_Play):
	""" Daring Drake
	<b>Rush</b> <b>Battlecry:</b> If you're holding a Dragon, gain +1/+1. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_916", self.controller)
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


##########RLK_917##########

class pp_RLK_917(Preset_Play):
	""" Flight of the Bronze
	<b>Discover</b> a Dragon. <b>Manathirst (7):</b> Summon a 5/5 Drake with <b>Taunt</b>. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_917", self.controller)
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


##########RLK_918##########

class pp_RLK_918(Preset_Play):
	""" For Quel'Thalas!
	Give a friendly minion +3 Attack. Give your hero +2 Attack this turn. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_918", self.controller)
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


##########RLK_919##########

class pp_RLK_919(Preset_Play):
	""" Anachronos
	<b>Battlecry:</b> Send all other minions 2 turns into the future. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_919", self.controller)
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


##########RLK_921##########

class pp_RLK_921(Preset_Play):
	""" Sanguine Soldier
	<b>Divine Shield</b>  <b>Battlecry:</b> Deal 2 damage to your hero. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_921", self.controller)
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


##########RLK_922##########

class pp_RLK_922(Preset_Play):
	""" Seal of Blood
	Give a minion +3/+3 and <b>Divine Shield</b>. Deal $3 damage to your hero. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_922", self.controller)
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


##########RLK_923##########

class pp_RLK_923(Preset_Play):
	""" Feast and Famine
	Give your hero +3 Attack this turn. <b>Manathirst (4):</b> And <b>Lifesteal</b>. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_923", self.controller)
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


##########RLK_924##########

class pp_RLK_924(Preset_Play):
	""" Blood Matriarch Liadrin
	After you summon a minion with less Attack than this, give it <b>Divine Shield</b> and <b>Rush</b>. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_924", self.controller)
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


##########RLK_927##########

class pp_RLK_927(Preset_Play):
	""" Blood Crusader
	<b>Battlecry:</b> Your next Paladin minion this turn costs  Health instead of Mana. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_927", self.controller)
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


##########RLK_Prologue_Anasterian_003t##########

class pp_RLK_Prologue_Anasterian_003t(Preset_Play):
	""" Anasterian Sunstrider
	<b>Rush</b>. Also damages the minions next to whomever he attacks. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_Anasterian_003t", self.controller)
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


##########RLK_Prologue_Arthas_001hp##########

class pp_RLK_Prologue_Arthas_001hp(Preset_Play):
	""" Arthas
	 """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_Arthas_001hp", self.controller)
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


##########RLK_Prologue_Arthas_001p##########

class pp_RLK_Prologue_Arthas_001p(Preset_Play):
	""" Reinforce
	<b>Hero Power</b> Summon a 1/1 Silver  Hand Recruit. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_Arthas_001p", self.controller)
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


##########RLK_Prologue_Gavinrad_002t##########

class pp_RLK_Prologue_Gavinrad_002t(Preset_Play):
	""" Gavinrad the Dire
	Your Silver Hand Recruits have +1/+1. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_Gavinrad_002t", self.controller)
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


##########RLK_Prologue_Lightbringer_003e##########

class pp_RLK_Prologue_Lightbringer_003e(Preset_Play):
	""" Blessed by Lightbringer
	<b>Divine Shield</b>. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_Lightbringer_003e", self.controller)
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


##########RLK_Prologue_Lightbringer_003w##########

class pp_RLK_Prologue_Lightbringer_003w(Preset_Play):
	""" Hammer of the Lightbringer
	 """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_Lightbringer_003w", self.controller)
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


##########RLK_Prologue_Uther_002hb##########

class pp_RLK_Prologue_Uther_002hb(Preset_Play):
	""" Uther Lightbringer
	 """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_Uther_002hb", self.controller)
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


##########RLK_Prologue_Uther_002p##########

class pp_RLK_Prologue_Uther_002p(Preset_Play):
	""" Equip Lightbringer
	<b>Hero Power</b> Equip a 3/4 Lightbringer. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_Prologue_Uther_002p", self.controller)
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


