from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def lich_deathknight():

	PresetGame(pp_RLK_012)##
	PresetGame(pp_RLK_035)##
	PresetGame(pp_RLK_035a)##
	PresetGame(pp_RLK_035b)##
	PresetGame(pp_RLK_035c)##
	PresetGame(pp_RLK_051)##
	PresetGame(pp_RLK_051a)##
	PresetGame(pp_RLK_116)##
	PresetGame(pp_RLK_116a)##
	PresetGame(pp_RLK_120)##
	PresetGame(pp_RLK_121)##
	PresetGame(pp_RLK_121a)##
	PresetGame(pp_RLK_225)##
	PresetGame(pp_RLK_506)##
	PresetGame(pp_RLK_706)##
	PresetGame(pp_RLK_741)##
	pass


##########RLK_012##########

class pp_RLK_012(Preset_Play):
	""" Soulbreaker
	After your hero attacks and kills a minion, gain 2 <b>Corpses</b>. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_012", self.controller)
		self.con4=Summon(self.controller, self.card_choice("weapon")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH1")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.play_card(self.con4)
		self.attack_card(self.controller.hero, self.opp1)
		self.assertion("self.opp1.dead==True")
		self.assertion("self.controller.corpse==2")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_035##########

class pp_RLK_035(Preset_Play):
	""" Corpse Explosion
	Detonate a <b>Corpse</b> to deal $1 damage to all minions. If any are still alive, repeat this. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_035", self.controller)
		self.opp1=(Summon(self.opponent, self.card_choice("minionH4")).trigger(self.opponent))[0][0]
		self.opp2=(Summon(self.opponent, self.card_choice("minionH1")).trigger(self.opponent))[0][0]
		self.opp3=(Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent))[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.controller.corpse=1
		self.play_card(self.con1)
		self.assertion("self.opp1.health==3")
		self.assertion("self.opp2.dead==True")
		self.assertion("self.opp3.health==2")
		self.assertion("self.controller.corpse==0")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_035a(Preset_Play):
	""" Corpse Explosion
	Detonate a <b>Corpse</b> to deal $1 damage to all minions. If any are still alive, repeat this. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_035", self.controller)
		self.opp1=(Summon(self.opponent, self.card_choice("minionH4")).trigger(self.opponent))[0][0]
		self.opp2=(Summon(self.opponent, self.card_choice("minionH1")).trigger(self.opponent))[0][0]
		self.opp3=(Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent))[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.controller.corpse=2
		self.play_card(self.con1)
		self.assertion("self.opp1.health==3")
		self.assertion("self.opp2.dead==True")
		self.assertion("self.opp3.health==2")
		self.assertion("self.controller.corpse==1")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_035b(Preset_Play):
	""" Corpse Explosion
	Detonate a <b>Corpse</b> to deal $1 damage to all minions. If any are still alive, repeat this. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_035", self.controller)
		self.opp1=(Summon(self.opponent, self.card_choice("minionH4")).trigger(self.opponent))[0][0]
		self.opp2=(Summon(self.opponent, self.card_choice("minionH2")).trigger(self.opponent))[0][0]
		self.opp3=(Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent))[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.controller.corpse=1
		self.play_card(self.con1)
		self.assertion("self.opp1.health==3")
		self.assertion("self.opp2.health==1")
		self.assertion("self.opp3.health==2")
		self.assertion("self.controller.corpse==0")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_035c(Preset_Play):
	""" Corpse Explosion
	Detonate a <b>Corpse</b> to deal $1 damage to all minions. If any are still alive, repeat this. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_035", self.controller)
		self.opp1=(Summon(self.opponent, self.card_choice("minionH4")).trigger(self.opponent))[0][0]
		self.opp2=(Summon(self.opponent, self.card_choice("minionH1")).trigger(self.opponent))[0][0]
		self.opp3=(Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent))[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.controller.corpse=2
		self.play_card(self.con1)
		self.assertion("self.opp1.health==2")
		self.assertion("self.opp2.dead==True")
		self.assertion("self.opp3.health==1")
		self.assertion("self.controller.corpse==0")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_051##########

class pp_RLK_051(Preset_Play):
	""" Vampiric Blood
	Give your hero +5 Health. Spend 3 <b>Corpses</b> to gain 5 more and draw a card. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_051", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		Hit(self.controller.hero, 15).trigger(self.controller)
		self.controller.corpse=4
		self.play_card(self.con1)
		self.assertion("self.controller.corpse==1")
		self.assertion("self.controller.hero.damage==5")
		self.assertion("len(self.controller.hand)==4")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_051a(Preset_Play):
	""" Vampiric Blood
	Give your hero +5 Health. Spend 3 <b>Corpses</b> to gain 5 more and draw a card. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_051", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		Hit(self.controller.hero, 15).trigger(self.controller)
		self.controller.corpse=2
		self.play_card(self.con1)
		self.assertion("self.controller.corpse==4")
		self.assertion("self.controller.hero.damage==10")
		self.assertion("len(self.controller.hand)==3")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_116##########

class pp_RLK_116(Preset_Play):
	""" Necrotic Mortician
	<b>Battlecry:</b> If a friendly Undead died after your last turn, <b>Discover</b> an Unholy Rune card. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_116", self.controller)
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
		self.choose_action()
		self.assertion("len(self.controller.hand)==5")
		self.con2=self.controller.hand[3]
		self.assertion("self.con2.cost_unholy>0")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_116a(Preset_Play):
	""" Necrotic Mortician
	<b>Battlecry:</b> If a friendly Undead died after your last turn, <b>Discover</b> an Unholy Rune card. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_116", self.controller)
		self.con4=Summon(self.controller, self.card_choice("undead")).trigger(self.controller)
		self.con4=self.con4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.change_turn()
		### opp
		#Hit(self.con4, 10).trigger(self.opponent)
		self.change_turn()
		### con
		self.play_card(self.con1)
		self.choose_action()
		self.assertion("len(self.controller.hand)==4")
		self.con2=self.controller.hand[3]
		self.assertion("getattr(self.con2, 'cost_unholy', 0)==0")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_120##########

class pp_RLK_120(Preset_Play):
	""" Meat Grinder
	<b>Battlecry:</b> Shred a random minion in your deck to gain 3 <b>Corpses.</b> """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_120", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.lendeck1=len([card for card in self.controller.deck if card.type==CardType.MINION])
		self.play_card(self.con1)
		self.assertion("self.controller.corpse==3")
		self.lendeck2=len([card for card in self.controller.deck if card.type==CardType.MINION])
		self.assertion("self.lendeck1-1==self.lendeck2")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_121##########

class pp_RLK_121(Preset_Play):
	""" Acolyte of Death
	After a friendly Undead dies, draw a card. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_121", self.controller)
		self.con4=Summon(self.controller, self.card_choice("undead")).trigger(self.controller)
		self.con4=self.con4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		Hit(self.con4, 10).trigger(self.controller)
		self.assertion("self.controller.hand==4")
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_121a(Preset_Play):
	""" Acolyte of Death
	After a friendly Undead dies, draw a card. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_121", self.controller)
		self.con4=Summon(self.controller, self.card_choice("undead")).trigger(self.controller)
		self.con4=self.con4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		Hit(self.con4, 10).trigger(self.opponent)
		self.assertion("self.controller.hand==4")
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_225##########

class pp_RLK_225(Preset_Play):
	""" Blightfang
	<b>Battlecry:</b> Infect all enemy minions. When they die, you summon a 2/2 Zombie with <b>Taunt</b>. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_225", self.controller)
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
		self.assertion("len(self.opp1.buffs)==1")
		self.assertion("self.opp1.buffs[0].id=='RLK_225e'")
		Hit(self.opp1, 10).trigger(self.controller)
		self.assertion("len(self.controller.field)==2")
		self.assertion("self.controller.field[1].id=='RLK_118t3'")
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_506##########

class pp_RLK_506(Preset_Play):
	""" Boneguard Commander
	<b>Taunt</b> <b>Battlecry:</b> Raise up to 6 <b>Corpses</b> as 1/2 Risen Footmen with <b>Taunt</b>. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_506", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.controller.corpse=3
		self.play_card(self.con1)
		self.assertion("len(self.controller.field)==4")
		self.assertion("self.controller.field[1].id=='RLK_061t'")
		self.assertion("self.controller.field[2].id=='RLK_061t'")
		self.assertion("self.controller.field[3].id=='RLK_061t'")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_506a(Preset_Play):
	""" Boneguard Commander
	<b>Taunt</b> <b>Battlecry:</b> Raise up to 6 <b>Corpses</b> as 1/2 Risen Footmen with <b>Taunt</b>. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_506", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.controller.corpse=8
		self.play_card(self.con1)
		self.assertion("len(self.controller.field)==7")
		self.assertion("self.controller.field[1].id=='RLK_061t'")
		self.assertion("self.controller.field[3].id=='RLK_061t'")
		self.assertion("self.controller.field[6].id=='RLK_061t'")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_706##########

class pp_RLK_706(Preset_Play):
	""" Alexandros Mograine
	<b>Battlecry:</b> For the rest of the game, deal 3 damage to your opponent at the end of your turns. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_706", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		self.assertion("len(self.controller.buffs)==1")
		self.assertion("self.opponent.hero.damage==3")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_741##########

class pp_RLK_741(Preset_Play):
	""" Soulstealer
	<b>Battlecry:</b> Destroy all other minions. Gain 1 <b>Corpse</b> for each enemy destroyed. """
	class1=CardClass.DEATHKNIGHT
	class2=CardClass.DEATHKNIGHT
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_741", self.controller)
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
		self.assertion("self.con4.dead==True")
		self.assertion("self.opp1.dead==True")
		self.assertion("self.controller.corpse==2")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass



