from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def lich_druid():

	#PresetGame(pp_RLK_650)##OK
	#PresetGame(pp_RLK_651)##OK
	#PresetGame(pp_RLK_652)##OK
	#PresetGame(pp_RLK_654)##OK
	#PresetGame(pp_RLK_654a)##OK
	PresetGame(pp_RLK_655)##
	#PresetGame(pp_RLK_656)##OK
	#PresetGame(pp_RLK_657)##OK
	#PresetGame(pp_RLK_658)##OK
	#PresetGame(pp_RLK_659)##OK
	#PresetGame(pp_RLK_956)##OK
	pass


##########RLK_650##########

class pp_RLK_650(Preset_Play):
	""" Lingering Zombie
	<b>Deathrattle:</b> Summon a 1/1 Disarmed Zombie with "<b>Deathrattle:</b> Summon a 1/1 Zombie." """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_650", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		Hit(self.con1, 10).trigger(self.controller)
		self.field=[card.id for card in self.controller.field]
		self.assertion("'RLK_650t' in self.field")
		for card in self.controller.field:
			if card.id=='RLK_650t':
				self.con2=card
				break
		Hit(self.con2, 10).trigger(self.opponent)
		self.field=[card.id for card in self.controller.field]
		self.assertion("'RLK_650t2' in self.field")
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_651##########

class pp_RLK_651(Preset_Play):
	""" Crypt Keeper(minion:8/4/6)
	<b>Taunt</b>. Costs (1) less for each Armor you have. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_651", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.controller.hero.armor=5
		self.assertion("self.con1.cost==self.con1.data.cost-5")

		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_652##########

class pp_RLK_652(Preset_Play):
	""" Unending Swarm(spell:6)
	Resurrect all friendly minions that cost (2) or less. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_652", self.controller)
		self.con3=(Summon(self.controller, self.card_choice("minionC4")).trigger(self.controller))[0][0]
		self.con4=(Summon(self.controller, self.card_choice("minionC2")).trigger(self.controller))[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		Hit(self.con3, 10).trigger(self.controller)
		Hit(self.con4, 10).trigger(self.controller)
		self.play_card(self.con1)
		self.assertion("len(self.controller.field)==1")
		self.assertion("self.controller.field[0].id==self.con4.id")
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_654##########

class pp_RLK_654(Preset_Play):
	""" Beetlemancy
	<b>Choose One</b> - Gain 12 Armor; or Summon two 3/3 Beetles with <b>Taunt</b>. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_654", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1, choose=self.con1.choose_cards[0])
		self.assertion("self.controller.hero.armor==12")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_654a(Preset_Play):
	""" Beetlemancy
	<b>Choose One</b> - Gain 12 Armor; or Summon two 3/3 Beetles with <b>Taunt</b>. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_654", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1, choose=self.con1.choose_cards[1])
		self.assertion("len(self.controller.field)==2")
		self.assertion("self.controller.field[0].id=='RLK_654t'")
		self.assertion("self.controller.field[1].id=='RLK_654t'")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_655##########

class pp_RLK_655(Preset_Play):
	""" Wither
	Choose a minion. Each friendly Undead steals 1 Attack and Health from it. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_655", self.controller)
		self.con3=(Summon(self.controller, self.card_choice("undead")).trigger(self.controller))[0][0]
		self.con4=(Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller))[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1, target=self.con4)
		self.assertion("self.con3.atk==self.con3.data.atk+1")
		self.assertion("self.con4.atk==self.con4.data.atk-1")
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_656##########

class pp_RLK_656(Preset_Play):
	""" Chitinous Plating
	Gain 4 Armor. At the start of your next turn, gain 4 more. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_656", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.assertion("self.controller.hero.armor==4")
		self.change_turn()
		self.assertion("self.controller.hero.armor==4")
		### opp
		self.change_turn()
		self.assertion("self.controller.hero.armor==8")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_657##########

class pp_RLK_657(Preset_Play):
	""" Underking
	<b>Rush</b> <b>Battlecry and Deathrattle:</b> Gain 6 Armor. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_657", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.assertion("self.controller.hero.armor==6")
		Hit(self.con1, 10).trigger(self.controller)
		self.assertion("self.controller.hero.armor==12")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_658##########

class pp_RLK_658(Preset_Play):
	""" Elder Nadox(minion:5/5/4)
	<b>Battlecry:</b> Destroy a friendly Undead. Your minions gain its Attack. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_658", self.controller)
		self.con3=Summon(self.controller, self.card_choice("minionH4")).trigger(self.controller)
		self.con3=self.con3[0][0]
		self.con4=Summon(self.controller, self.card_choice("undead")).trigger(self.controller)
		self.con4=self.con4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1, target=self.con4)
		self.amount=self.con4.atk
		self.assertion("self.con3.atk==self.con3.data.atk+self.amount")
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_659##########

class pp_RLK_659(Preset_Play):
	""" Anub'Rekhan
	<b>Battlecry:</b> Gain 8 Armor. This turn, your minions cost Armor instead of Mana. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_659", self.controller)
		self.con2=self.exchange_card(self.card_choice("minionC3"), self.controller)	
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.assertion("self.controller.hero.armor==8")
		self.amount=self.controller.mana
		self.play_card(self.con2)
		self.assertion("self.controller.mana==self.amount")
		self.assertion("self.controller.hero.armor==8-3")

		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_956##########

class pp_RLK_956(Preset_Play):
	""" Nerubian Flyer
	<b>Battlecry:</b> If a friendly Undead died after your last turn, summon a 2/2 Nerubian. """
	class1=CardClass.DRUID
	class2=CardClass.DRUID
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_956", self.controller)
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
		self.cards=[card.id for card in self.controller.field]
		self.assertion("'RLK_956t' in self.cards")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


