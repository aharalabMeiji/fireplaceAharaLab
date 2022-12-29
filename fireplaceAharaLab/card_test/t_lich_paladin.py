from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def lich_paladin():

	#PresetGame(pp_RLK_527)##OK
	#PresetGame(pp_RLK_916)##OK
	#PresetGame(pp_RLK_917)##OK
	#PresetGame(pp_RLK_918)##OK
	#PresetGame(pp_RLK_919)## pending
	#PresetGame(pp_RLK_921)##OK
	#PresetGame(pp_RLK_922)##OK
	#PresetGame(pp_RLK_923)##OK
	#PresetGame(pp_RLK_924)##OK
	#PresetGame(pp_RLK_927)##OK

	pass


##########RLK_527##########

class pp_RLK_527(Preset_Play):
	""" Timewarden
	<b>Battlecry:</b> Until the end of your next turn, Dragons you summon gain <b>Taunt</b> and <b>Divine Shield</b>. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_527", self.controller)
		self.con2=self.exchange_card(self.card_choice("dragon"), self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.play_card(self.con2)
		self.assertion("'RLK_527e2' in [card.id for card in self.con2.buffs]")
		self.assertion("self.con2.taunt==True")
		self.assertion("self.con2.divine_shield==True")
		self.change_turn()
		### opp
		self.change_turn()
		self.assertion("self.con2.taunt!=True")
		self.assertion("self.con2.divine_shield!=True")
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
		self.con4=Summon(self.controller, self.card_choice("dragon")).trigger(self.controller)
		self.con4=self.con4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.assertion("len(self.con1.buffs)>0")
		self.assertion("'RLK_916e' in [card.id for card in self.con1.buffs]")
		self.assertion("self.con1.atk==self.con1.data.atk+1")
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

		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.lenhand=len(self.controller.hand)
		self.play_card(self.con1)
		self.choose_action()
		self.assertion("len(self.controller.hand)==self.lenhand")
		self.con2=self.controller.hand[-1]
		self.assertion("self.con2.race==Race.DRAGON")
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_917a(Preset_Play):
	""" Flight of the Bronze(spell:1)
	<b>Discover</b> a Dragon. <b>Manathirst (7):</b> Summon a 5/5 Drake with <b>Taunt</b>. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_917", self.controller)

		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.lenhand=len(self.controller.hand)
		self.controller.max_mana=7
		self.play_card(self.con1)
		self.choose_action()
		self.assertion("len(self.controller.hand)==self.lenhand")
		self.con2=self.controller.hand[-1]
		self.assertion("self.con2.race==Race.DRAGON")
		self.assertion("len(self.controller.field)==1")
		self.assertion("self.controller.field[0].id=='RLK_917t'")
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
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1, target=self.con4)
		self.assertion("len(self.con4.buffs)>0")
		self.assertion("'RLK_918e' in [card.id for card in self.con4.buffs]")
		self.assertion("self.con4.atk==self.con4.data.atk+3")
		self.assertion("len(self.controller.hero.buffs)>0")
		self.assertion("'RLK_918e2' in [card.id for card in self.controller.hero.buffs]")
		self.assertion("self.controller.hero.atk==2")
		self.change_turn()
		### opp
		self.change_turn()
		self.assertion("len(self.controller.hero.buffs)==0")
		self.assertion("self.controller.hero.atk==0")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_919##########

class pp_RLK_919(Preset_Play):### pending
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
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.assertion("self.con1.divine_shield==True")
		self.assertion("self.controller.hero.damage==2")
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
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1, target=self.con4)
		self.assertion("len(self.con4.buffs)>0")
		self.assertion("self.con4.buffs[0].id=='RLK_922e'")
		self.assertion("self.con4.atk==self.con4.data.atk+3")
		self.assertion("self.con4.divine_shield==True")
		self.assertion("self.controller.hero.damage==2")
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
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.controller.max_mana=4
		self.play_card(self.con1)
		self.assertion("len(self.controller.hero.buffs)>0")
		self.assertion("'RLK_923e1' in [card.id for card in self.controller.hero.buffs]")
		self.assertion("'RLK_923e3' in [card.id for card in self.controller.hero.buffs]")
		self.assertion("self.controller.hero.atk==3")
		self.assertion("self.controller.hero.lifesteal==True")
		self.change_turn()
		self.assertion("not 'RLK_923e1' in [card.id for card in self.controller.hero.buffs]")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_924##########

class pp_RLK_924(Preset_Play):
	""" Blood Matriarch Liadrin (minion:2/3/2)
	After you summon a minion with less Attack than this, give it <b>Divine Shield</b> and <b>Rush</b>. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_924", self.controller)
		self.con4=self.exchange_card(self.card_choice("minionA2"), self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.play_card(self.con4)
		self.assertion("len(self.con4.buffs)>0")
		self.assertion("'RLK_924e' in [card.id for card in self.con4.buffs]")
		self.assertion("self.con4.divine_shield==True")
		self.assertion("self.con4.rush==True")
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
		self.con2=self.exchange_card("RLK_918", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.amount=self.con2.cost
		self.this_mana=self.controller.mana
		self.this_hero_health=self.controller.hero.health
		self.play_card(self.con2)
		self.assertion("self.controller.mana==self.this_mana")
		self.assertion("self.controller.hero.health==self.this_hero_health-self.amount")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass



