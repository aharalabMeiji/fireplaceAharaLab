from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give, Draw, Discard, CastSpell
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def lich_warrior():

	PresetGame(pp_RLK_600)##OK
	PresetGame(pp_RLK_601)##OK
	PresetGame(pp_RLK_602)##OK
	PresetGame(pp_RLK_603)##OK
	PresetGame(pp_RLK_604)##OK
	PresetGame(pp_RLK_604a)##OK
	PresetGame(pp_RLK_605)##OK
	PresetGame(pp_RLK_607)##OK
	PresetGame(pp_RLK_608)##OK
	PresetGame(pp_RLK_609)##OK
	PresetGame(pp_RLK_960)##OK
	pass


##########RLK_600##########

class pp_RLK_600(Preset_Play):
	""" Sunfire Smithing
	Equip a 4/2 Sword. Give a random minion in your hand +4/+2. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_600", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.assertion("self.controller.weapon.id=='RLK_600t'")
		self.assertion("self.controller.weapon.durability==2")
		self.cards=[card for card in self.controller.hand if card.type==CardType.MINION and len(card.buffs)>0 and card.buffs[-1].id=='RLK_600e']
		self.assertion("len(self.cards)==1")
		self.assertion("self.cards[0].atk==self.cards[0].data.atk+4")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_601##########

class pp_RLK_601(Preset_Play):
	""" Last Stand
	Draw a <b>Taunt</b> minion. Double its stats. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_601", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.actions=[action for action in self.controller._targetedaction_log if isinstance(action['class'], Give)]
		self.assertion("len(self.actions)>0")
		self.last_draw=self.actions[-1]['target_args'][0][0]
		self.assertion("self.last_draw.taunt==True")
		self.assertion("self.last_draw.buffs[-1].id=='RLK_601e'")
		self.assertion("self.last_draw.atk==self.last_draw.data.atk*2")
		self.assertion("self.last_draw.max_health==self.last_draw.data.health*2")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_602##########

class pp_RLK_602(Preset_Play):
	""" Silverfury Stalwart
	<b><b>Taunt</b>, Rush</b> Can't be targeted by spells or Hero Powers. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_602", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.assertion("self.con1.cant_be_targeted_by_hero_powers==True")
		self.assertion("self.con1.cant_be_targeted_by_spells==True")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_603##########

class pp_RLK_603(Preset_Play):
	""" Light of the Phoenix
	Draw 2 cards. Costs (1) less for each damaged friendly character. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_603", self.controller)
		self.con4=self.summon_card(self.controller, "minionH5")
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.hit_card(self.con4, amount=2)# make it damaged
		self.play_card(self.con1)
		self.assertion("len(self.controller.hand)>2")
		self.con2=self.controller.hand[-2]
		self.con3=self.controller.hand[-1]
		self.assertion("self.con2.cost==self.con2.data.cost-1")
		self.assertion("self.con3.cost==self.con3.data.cost-1")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_604##########

class pp_RLK_604(Preset_Play):
	""" Thori'belore
	<b>Rush</b>. <b>Deathrattle:</b> Go <b>Dormant</b>. Cast a Fire spell to revive Thori'belore! <i>(Revives 2 times.)</i> """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_604", self.controller)
		self.con2=self.exchange_card("fire", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.hit_card(self.con1)## deathrattle is triggered
		self.cards=[card for card in self.controller.field if card.id=='RLK_604t']
		self.assertion("len(self.cards)==1")
		self.assertion("self.cards[0].dormant!=0")
		self.play_card(self.con2) ### fire spell
		self.cards=[card for card in self.controller.field if card.id=='RLK_604a']
		self.assertion("len(self.cards)==1")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_604a(Preset_Play):
	""" Thori'belore
	<b>Rush</b>. <b>Deathrattle:</b> Go <b>Dormant</b>. Cast a Fire spell to revive Thori'belore! <i>(Revives 2 times.)</i> """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.summon_card(self.controller, "RLK_604a")
		self.con2=self.exchange_card("fire", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.hit_card(self.con1)## deathrattle is triggered
		self.cards=[card for card in self.controller.field if card.id=='RLK_604t2']
		self.assertion("len(self.cards)==1")
		self.assertion("self.cards[0].dormant!=0")
		self.play_card(self.con2) ### fire spell
		self.cards=[card for card in self.controller.field if card.id=='RLK_604b']
		self.assertion("len(self.cards)==1")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_605##########

class pp_RLK_605(Preset_Play):
	""" Blazing Power
	Give a minion +1/+1. Repeat for each damaged friendly character. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_605", self.controller)
		self.con2=self.summon_card(self.controller, "minionH5")
		self.con3=self.summon_card(self.controller, "minionH2")
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.hit_card(self.con2, amount=2)
		self.play_card(self.con1, target=self.con3)
		self.assertion("self.con3.atk==self.con3.data.atk+2")
		self.assertion("self.con3.max_health==self.con3.data.health+2")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_607##########

class pp_RLK_607(Preset_Play):
	""" Disruptive Spellbreaker
	At the end of your turn, your opponent discards a spell. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_607", self.controller)
		self.opp1=self.exchange_card("spell", self.opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		self.actions=[action for action in self.controller._targetedaction_log if isinstance(action['class'], Discard)]
		self.assertion("len(self.actions)>0")
		self.opp2=self.actions[-1]['target']
		self.assertion("self.opp2.controller==self.opponent")
		self.assertion("self.opp2.type==CardType.SPELL")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_608##########

class pp_RLK_608(Preset_Play):
	""" Asvedon, the Grandshield
	<b>Battlecry:</b> Cast a copy of the last spell your opponent played. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_608", self.controller)
		self.opp1=self.exchange_card("spell", self.opponent)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.change_turn()
		### opp
		self.play_card(self.opp1)
		self.change_turn()
		### con
		self.play_card(self.con1)
		self.actions=[action for action in self.controller._targetedaction_log if isinstance(action['class'], CastSpell)]
		self.assertion("len(self.actions)>0")
		self.con2=self.actions[-1]['target']
		self.assertion("self.con2.id==self.opp1.id")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_609##########

class pp_RLK_609(Preset_Play):
	""" Sunfury Champion
	After you cast a Fire spell, deal 1 damage to all minions. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_609", self.controller)
		self.con2=self.exchange_card("fire", self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.play_card(self.con2)
		self.assertion("self.opp1.damage==1")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_960##########

class pp_RLK_960(Preset_Play):
	""" Embers of Strength
	Summon two 1/2 Guards with <b>Taunt</b>. <b>Manathirst (6):</b> Give them +1/+2. """
	class1=CardClass.WARRIOR
	class2=CardClass.WARRIOR
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_960", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.controller.max_mana=6
		self.play_card(self.con1)
		self.cards=[card for card in self.controller.field if card.id=='RLK_960t']
		self.assertion("len(self.cards)==2")
		self.con2=self.cards[0]
		self.con3=self.cards[1]
		self.assertion("len(self.con2.buffs)>0")
		self.assertion("self.con2.buffs[0].id=='RLK_960e'")
		self.assertion("self.con2.atk==self.con2.data.atk+1")
		self.assertion("self.con2.max_health==self.con2.data.health+2")
		self.assertion("self.con3.buffs[0].id=='RLK_960e'")
		self.assertion("self.con3.atk==self.con2.data.atk+1")
		self.assertion("self.con3.max_health==self.con2.data.health+2")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


