from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def lich_demonhunter():

	#PresetGame(pp_RLK_206)##OK
	#PresetGame(pp_RLK_207)##OK
	PresetGame(pp_RLK_208)##
	PresetGame(pp_RLK_209)##
	PresetGame(pp_RLK_210)##
	PresetGame(pp_RLK_211)##
	PresetGame(pp_RLK_212)##
	PresetGame(pp_RLK_213)##
	PresetGame(pp_RLK_214)##
	PresetGame(pp_RLK_215)##
	pass


##########RLK_206##########

class pp_RLK_206(Preset_Play):
	""" Mark of Scorn
	Draw a card. If it's not a minion, deal $3 damage to the lowest Health enemy. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_206", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH4")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		self.opp2=Summon(self.opponent, self.card_choice("minionH5")).trigger(self.opponent)
		self.opp2=self.opp2[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.lenhand=len(self.controller.hand)
		self.play_card(self.con1)
		self.assertion("self.lenhand==len(self.controller.hand)")
		self.con2=self.controller.hand[-1]
		if self.con2.type!=CardType.MINION:
			self.assertion("self.opp1.damage==3")
			self.assertion("self.opp2.damage==0")
		else:
			self.assertion("self.opp1.damage==0")
			self.assertion("self.opp2.damage==0")
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_207##########

class pp_RLK_207(Preset_Play):
	""" Fierce Outsider
	<b>Rush</b> <b>Outcast:</b> Your next <b>Outcast</b> card costs (1) less. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_207", self.controller)##outcast
		self.con2=self.exchange_card("CORE_BT_480", self.controller)
		self.con3=self.exchange_card("CORE_BT_480", self.controller)##outcast
		index=self.controller.hand.index(self.con1)
		self.controller.hand[0],self.controller.hand[index]=self.controller.hand[index],self.controller.hand[0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.assertion("len(self.con2.buffs)>0")
		self.assertion("self.con2.cost==self.con2.data.cost-1")
		self.assertion("len(self.con3.buffs)>0")
		self.assertion("self.con3.cost==self.con3.data.cost-1")
		self.play_card(self.con3)
		self.assertion("len(self.con2.buffs)==0")
		self.assertion("self.con2.cost==self.con2.data.cost")
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_208##########

class pp_RLK_208(Preset_Play):
	""" Fel'dorei Warband
	Deal $4 damage. If your deck has no minions, summon four 1/1 Illidari with <b>Rush</b>. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_208", self.controller)
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


##########RLK_209##########

class pp_RLK_209(Preset_Play):
	""" Unleash Fel
	Deal $1 damage to all enemies. <b>Manathirst_(4):</b> With <b>Lifesteal</b>. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_209", self.controller)
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


##########RLK_210##########

class pp_RLK_210(Preset_Play):
	""" Wretched Exile
	After you play an <b>Outcast</b> card, add a random <b>Outcast</b> card to your hand. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_210", self.controller)
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


##########RLK_211##########

class pp_RLK_211(Preset_Play):
	""" Deal with a Devil
	Summon two 3/3 Felfiends with <b>Lifesteal</b>. If your deck has no minions, summon another. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_211", self.controller)
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


##########RLK_212##########

class pp_RLK_212(Preset_Play):
	""" Brutal Annihilan
	<b>Taunt</b>, <b>Rush</b> After this minion survives damage, deal that amount to the enemy hero. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_212", self.controller)
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


##########RLK_213##########

class pp_RLK_213(Preset_Play):
	""" Vengeful Walloper
	<b>Rush</b>. Costs (1) less for each <b>Outcast</b> card you've played this game. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_213", self.controller)
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


##########RLK_214##########

class pp_RLK_214(Preset_Play):
	""" Souleater's Scythe
	<b>Start of Game:</b> Consume 3 different minions in your deck. Leave behind Souls that <b>Discover</b> them. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_214", self.controller)
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


##########RLK_215##########

class pp_RLK_215(Preset_Play):
	""" Felerin, the Forgotten
	<b>Battlecry:</b> Add a random <b>Outcast</b> card to the left and right sides of your hand. They cost (2) less. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_215", self.controller)
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

#############################################################


