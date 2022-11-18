from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity, CardClass
import random

def sunken_paladin():

	#PresetGame(pp_TID_077)##
	#PresetGame(pp_TID_098)##
	#PresetGame(pp_TID_949)##
	#PresetGame(pp_TSC_030)##
	#PresetGame(pp_TSC_059)##OKOK
	#PresetGame(pp_TSC_060)##OKOK
	#PresetGame(pp_TSC_061x)##OK OK
	#PresetGame(pp_TSC_061y)##OK  OK
	#PresetGame(pp_TSC_074)## OKOK
	#PresetGame(pp_TSC_076)##
	#PresetGame(pp_TSC_079)##
	#PresetGame(pp_TSC_083)##
	#PresetGame(pp_TSC_644)##
	#PresetGame(pp_TSC_952)##
	pass

##########TID_077##########

class pp_TID_077(Preset_Play):
	""" Lightray
	[Taunt]Costs (1) less for each Paladin card you've played this game. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TID_077", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########TID_098##########

class pp_TID_098(Preset_Play):
	""" Myrmidon
	After you cast a spell on this minion, draw a card. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TID_098", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########TID_949##########

class pp_TID_949(Preset_Play):
	""" Front Lines
	Summon a minionfrom each player's deck.Repeat until either sideof the battlefield is full. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TID_949", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########TSC_030##########

class pp_TSC_030(Preset_Play):
	""" The Leviathan
	[Colossal +1][Rush], [Divine Shield]After this attacks,[Dredge]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_030", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########TSC_059##########

class pp_TSC_059(Preset_Play):
	""" Bubblebot
	[Battlecry:] Give your otherMechs [Divine Shield]and [Taunt]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_059", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("mech")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		assert self.mark4.divine_shield==False, "divine_shield"		
		assert self.mark4.taunt==False, "taunt"		
		self.play_card(self.mark1, target=self.mark4)
		assert self.mark4.divine_shield==True, "divine_shield"		
		assert self.mark4.taunt==True, "taunt"		
		self.change_turn()
		assert self.mark4.divine_shield==True, "divine_shield"		
		### opp
		Hit(self.mark4, 5).trigger(self.opponent)
		assert self.mark4.divine_shield==False, "divine_shield"		
		self.change_turn()
		assert self.mark4.divine_shield==False, "divine_shield"		
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########TSC_060##########

class pp_TSC_060(Preset_Play):
	""" Shimmering Sunfish
	[Battlecry:] If you're holding a Holy Spell, gain [Taunt] and [Divine Shield]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_060", self.controller)
		self.mark2=self.exchange_card("holy", self.controller)
		#self.mark4=Summon(self.controller, self.card_choice("holy")).trigger(self.controller)
		#self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		assert self.mark1.taunt==False, "taunt"
		assert self.mark1.divine_shield==False, "divine_shield"
		self.play_card(self.mark1)
		assert self.mark1.taunt==True, "taunt"
		assert self.mark1.divine_shield==True, "divine_shield"
		self.change_turn()
		### opp
		assert self.mark1.divine_shield==True, "divine_shield"
		Hit(self.mark1, 5).trigger(self.opponent)
		assert self.mark1.divine_shield==False, "divine_shield"
		assert ''
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########TSC_061##########

class pp_TSC_061x(Preset_Play):
	""" The Garden's Grace (cost:10)
	Give a minion +5/+5 and[Divine Shield]. Costs (1) lessfor each Mana you've spenton Holy spells this game. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_061", self.controller)
		self.mark2=self.exchange_card("holy", self.controller)
		self.mark3=self.exchange_card("holy", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		if self.mark2.requires_target():
			target = random.choice(self.mark2.targets)
		else:
			target=None
		self.play_card(self.mark2, target=target)
		self.change_turn()
		### opp
		self.change_turn()
		### con
		if self.mark3.requires_target():
			target = random.choice(self.mark3.targets)
		else:
			target=None
		self.play_card(self.mark3, target=target)
		print("10-%d-%d=%d"%(self.mark2.cost,self.mark3.cost,self.mark1.cost))
		assert 10-self.mark2.cost-self.mark3.cost==self.mark1.cost, "cost"
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_TSC_061y(Preset_Play):
	""" The Garden's Grace
	Give a minion +5/+5 and[Divine Shield]. Costs (1) lessfor each Mana you've spenton Holy spells this game. """
	class1=CardClass.PALADIN
	class2=CardClass.PALADIN

	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_061", self.controller)
		self.mark2=self.exchange_card("holy", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		if self.mark2.requires_target():
			target = random.choice(self.mark2.targets)
		else:
			target=None
		self.play_card(self.mark2, target=target)
		self.change_turn()
		### opp
		self.change_turn()
		### con
		self.play_card(self.mark1, target=self.mark4)
		assert 'TSC_061e' in [buff.id for buff in self.mark4.buffs], "buff"
		assert self.mark4.divine_shield==True, "shield"
		self.change_turn()
		### opp
		Hit(self.mark4, 5).trigger(self.opponent)
		assert self.mark4.divine_shield==False, "shield"
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########TSC_074##########

class pp_TSC_074(Preset_Play):
	""" Kotori Lightblade
	After you cast a Holy spell on this, cast it again on__another friendly minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_074", self.controller)
		self.mark2=self.exchange_card("CORE_AT_055", self.controller)##<CORE_AT_055: 'uŠÔ‰ñ•œ'>
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		### con
		self.GOON = (self.mark1 in self.mark2.targets)
		self.play_card(self.mark2, target=self.mark1)
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########TSC_076##########

class pp_TSC_076(Preset_Play):
	""" Immortalized in Stone
	Summon a 1/2, 2/4 and 4/8 Elemental with [Taunt]. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_076", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########TSC_079##########

class pp_TSC_079(Preset_Play):
	""" Radar Detector
	Scan the bottom 5 cardsof your deck. Draw anyMechs found this way,then shuffle your deck. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_079", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########TSC_083##########

class pp_TSC_083(Preset_Play):
	""" Seafloor Savior
	[Battlecry:] [Dredge].If it's a minion, give itthis minion's Attackand Health. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_083", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########TSC_644##########

class pp_TSC_644(Preset_Play):
	""" Azsharan Mooncatcher
	[Divine Shield]. [Battlecry:] Puta 'Sunken Mooncatcher' onthe bottom of your deck. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_644", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########TSC_952##########

class pp_TSC_952(Preset_Play):
	""" Holy Maki Roll
	Restore #2 Health. Repeatable this turn. """
	def preset_deck(self):
		self.mark1=self.exchange_card("TSC_952", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


