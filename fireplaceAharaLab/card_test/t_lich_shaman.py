from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give, RegularAttack, Destroy
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def lich_shaman():

	PresetGame(pp_RLK_550)##OK
	PresetGame(pp_RLK_551)##OK
	PresetGame(pp_RLK_552)##OK
	PresetGame(pp_RLK_553)##OK
	PresetGame(pp_RLK_554)##OK
	PresetGame(pp_RLK_909)##OK
	PresetGame(pp_RLK_910)##OK
	PresetGame(pp_RLK_911)##OK
	PresetGame(pp_RLK_912)##OK
	PresetGame(pp_RLK_913)##OK
	pass


##########RLK_550##########

class pp_RLK_550(Preset_Play):
	""" Rotgill
	<b>Battlecry:</b> Give your other minions "<b>Deathrattle:</b> Give __your minions +1/+1." """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_550", self.controller)
		self.con3=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con3=self.con3[0][0]
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.assertion("len(self.con3.buffs)>0")
		self.assertion("self.con3.buffs[0].id=='RLK_550e'")
		self.change_turn()
		### opp
		self.hit_card(self.con3)
		self.assertion("len(self.con4.buffs)>0")
		self.assertion("'RLK_550e2' in [card.id for card in self.con4.buffs]")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_551##########

class pp_RLK_551(Preset_Play):
	""" Blightblood Berserker
	<b>Taunt</b>, <b>Lifesteal</b>, <b>Reborn</b> <b>Deathrattle:</b> Deal 3 damage to a random enemy. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_551", self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionH5")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		Hit(self.controller.hero, 10).trigger(self.controller)
		self.play_card(self.con1)
		Hit(self.con1, 10).trigger(self.controller)
		self.assert1=(self.opp1.damage==3)
		self.assert2=(self.opponent.hero.damage==3)
		self.assertion("self.assert1 or self.assert2")
		self.assertion("self.controller.hero.damage==10-3")
		self.assertion("'RLK_551' in [card.id for card in self.controller.field]")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_552##########

class pp_RLK_552(Preset_Play):
	""" Unliving Champion
	<b>Battlecry:</b> If a friendly Undead died after your last turn, summon two 3/2 Zombies. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_552", self.controller)
		self.con4=self.summon_card(self.controller, "undead" )
		self.opp1=self.summon_card(self.opponent, "minionH3")
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.change_turn()
		### opp
		self.hit_card(self.con4)
		self.change_turn()
		### con
		self.play_card(self.con1)
		self.assertion("len([card.id for card in self.controller.field if card.id=='RLK_909t'])==2")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_553##########

class pp_RLK_553(Preset_Play):
	""" Prescience
	Draw 2 minions. For each that costs (5) or more, summon a_ 2/3 Spirit with <b>Taunt</b>. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_553", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.con2=self.controller.hand[-2]
		self.con3=self.controller.hand[-1]
		self.count=0
		if self.con2.cost>=5:
			self.count+=1
		if self.con3.cost>=5:
			self.count+=1
		self.assertion("len([card for card in self.controller.field if card.id=='RLK_553t'])==self.count")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_554##########

class pp_RLK_554(Preset_Play):
	""" Harkener of Dread
	<b>Taunt</b> <b>Deathrattle:</b> Summon a 6/6 Undead with <b>Taunt</b>. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_554", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		self.hit_card(self.con1)
		self.assertion("'RLK_554t' in [card.id for card in self.controller.field]")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_909##########

class pp_RLK_909(Preset_Play):
	""" Deathweaver Aura
	Give a minion "<b>Deathrattle:</b> Summon two 3/2 Zombies." <b>Overload:</b> (1) """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_909", self.controller)
		self.con4=self.summon_card(self.controller, "minionH3")
		self.opp1=self.summon_card(self.opponent, "minionH3")
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1, target=self.con4)
		self.change_turn()
		### opp
		self.hit_card(self.con4)
		self.assertion("'RLK_909t' in [card.id for card in self.controller.field]")
		self.assertion("self.controller.overloaded==1")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_910##########

class pp_RLK_910(Preset_Play):
	""" Shadow Suffusion
	Give your minions "<b>Deathrattle:</b> Deal 3 damage to a random enemy." """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_910", self.controller)
		self.con3=self.summon_card(self.controller, "minionH2")
		self.con4=self.summon_card(self.controller, "minionH3")
		self.opp1=self.summon_card(self.opponent, "minionH5")
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.assertion("'RLK_910e' in [card.id for card in self.con3.buffs]")
		self.assertion("'RLK_910e' in [card.id for card in self.con4.buffs]")
		self.change_turn()
		### opp
		if self.opp1.divine_shield==True:
			Hit(self.opp1, 1).trigger(self.opponent)
		self.hit_card(self.con3)
		self.assertion("self.opp1.damage==3 or self.opponent.hero.damage==3")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_911##########

class pp_RLK_911(Preset_Play):
	""" From De Other Side
	Summon a copy of each minion in your hand. They attack random enemy minions, then die. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_911", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.con2=self.controller.hand[0]
		self.con3=self.controller.hand[1]
		self.play_card(self.con1)
		self.actions=[action for action in self.controller._targetedaction_log if action['source'].type==CardType.SPELL and action['source'].id=='RLK_911']
		if self.con2.type==CardType.MINION:
			self.list_summon=[action for action in self.actions if isinstance(action['class'], Summon) and action['target_args'][0][0].id==self.con2.id]
			self.assertion("len(self.list_summon)>0")
			self.list_attack=[action for action in self.actions if isinstance(action['class'], RegularAttack) and action['target'].id==self.con2.id]
			self.assertion("len(self.list_attack)>0")
			self.list_destroy=[action for action in self.actions if isinstance(action['class'], Destroy) and action['target'].id==self.con2.id]
			self.assertion("len(self.list_destroy)>0")
		if self.con3.type==CardType.MINION:
			self.list_summon=[action for action in self.actions if isinstance(action['class'], Summon) and action['target_args'][0][0].id==self.con3.id]
			self.assertion("len(self.list_summon)>0")
			self.list_attack=[action for action in self.actions if isinstance(action['class'], RegularAttack) and action['target'].id==self.con3.id]
			self.assertion("len(self.list_attack)>0")
			self.list_destroy=[action for action in self.actions if isinstance(action['class'], Destroy) and action['target'].id==self.con3.id]
			self.assertion("len(self.list_destroy)>0")

		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_912##########

class pp_RLK_912(Preset_Play):
	""" Scourge Troll
	<b>Deathrattles</b> given to this minion trigger twice. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_912", self.controller)
		self.con2=self.exchange_card("RLK_550", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.play_card(self.con2)# buff to con1
		self.hit_card(self.con1)
		self.cards=[card.id for card in self.con2.buffs if card.id=='RLK_550e2']
		self.assertion("len(self.cards)==2")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_913##########

class pp_RLK_913(Preset_Play):
	""" Overlord Drakuru
	<b>Rush</b>, <b>Windfury</b> After this attacks and kills a minion, resurrect it on your side. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.summon_card(self.controller, "RLK_913")
		self.opp1=self.summon_card(self.opponent, "minionH1")
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		if self.opp1.divine_shield:
			Hit(self.opp1,1).trigger(self.controller)
		self.attack_card(self.con1, self.opp1)
		self.cards=[card.id for card in self.controller.field if card.id==self.opp1.id]
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


