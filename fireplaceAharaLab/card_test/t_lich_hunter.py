from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give, PutOnTop, Buff
from hearthstone.enums import CardClass, Zone, CardType, SpellSchool

def lich_hunter():

	#PresetGame(pp_RLK_804)##OK
	#PresetGame(pp_RLK_817)##OK
	#PresetGame(pp_RLK_818)##OK
	#PresetGame(pp_RLK_819)##OK
	#PresetGame(pp_RLK_820)##OK
	#PresetGame(pp_RLK_821)##OK
	#PresetGame(pp_RLK_825)##OK
	#PresetGame(pp_RLK_826)##OK
	#PresetGame(pp_RLK_827)##OK
	#PresetGame(pp_RLK_828)##OK

	pass


##########RLK_804##########

class pp_RLK_804(Preset_Play):
	""" Conjured Arrow
	Deal $2 damage to a minion. <b>Manathirst (6):</b> Draw that many cards. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_804", self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.controller.max_mana=6
		self.amount=len(self.controller.hand)
		self.play_card(self.con1, target=self.opp1)
		self.assertion("self.opp1.damage==2")
		self.actions=[action['class'] for action in self.controller._targetedaction_log]
		self.assertion("len(self.controller.hand)==self.amount-1+2")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_817##########

class pp_RLK_817(Preset_Play):
	""" Arcane Quiver
	<b>Discover</b> a spell from your deck. If it's Arcane, give it <b>Spell Damage +1</b>. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_817", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.amount=len(self.controller.hand)
		self.choose_action()
		self.assertion("len(self.controller.hand)==self.amount+1")
		self.con2=self.controller.hand[-1]
		self.assertion("self.con2.type==CardType.SPELL")
		if self.con2.spell_school==SpellSchool.ARCANE:
			self.assertion("self.controller.spellpower_by_spell==1")
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_818##########

class pp_RLK_818(Preset_Play):
	""" Ricochet Shot
	Deal $1 damage to three random enemies. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_818", self.controller)
		self.opp1=(Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent))[0][0]
		self.opp2=(Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent))[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.actions=[action['class'] for action in self.controller._targetedaction_log]
		self.assertion("len(self.actions)>=3")
		self.assertion("self.opp1.damage+self.opp2.damage+self.opponent.hero.damage==3")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_819##########

class pp_RLK_819(Preset_Play):
	""" Eversong Portal (spell:4)
	Summon $1 4/4 |4(Lynx, Lynxes) with <b>Rush</b> <i>(improved by <b>Spell Damage</b>)</i>. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_819", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.assertion("len(self.controller.field)==1")
		self.assertion("self.controller.field[0].id=='RLK_819t'")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_819a(Preset_Play):
	""" Eversong Portal (spell:4)
	Summon $1 4/4 |4(Lynx, Lynxes) with <b>Rush</b> <i>(improved by <b>Spell Damage</b>)</i>. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_819", self.controller)
		self.con2=self.exchange_card("CS3_001", self.controller)#spell damage 2
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con2)
		self.play_card(self.con1)
		self.assertion("len(self.controller.field)==3")
		self.assertion("self.controller.field[0].id=='RLK_819t'")
		self.assertion("self.controller.field[2].id=='RLK_819t'")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_820##########

class pp_RLK_820(Preset_Play):
	""" Halduron Brightwing
	<b>Battlecry:</b> Give all Arcane spells in your deck <b>Spell Damage +1</b>. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_820", self.controller)
		self.con2=(PutOnTop(self.controller, self.card_choice("arcane")).trigger(self.controller))[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.assertion("self.con2.spellpower_by_spell==1")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_821##########

class pp_RLK_821(Preset_Play):
	""" Scourge Tamer
	<b>Battlecry:</b> Craft a custom Zombeast. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_821", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.choose_action()
		for card in self.controller.hand:
			if card.id=='ICC_828t':
				self.con2=card
				break
		if self.con2.sidequest_list0[0]=='TSC_069':
			self.play_card(self.con2, target=self.con4)
		else:
			self.play_card(self.con2)
		self.choose_action()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("field", card)
			if card.id=='ICC_828t':
				print("*** rush : %s"%(card.rush))
				print("*** poisonous : %s"%(card.poisonous))
				print("*** windfury : %s"%(card.windfury))
				print("*** taunt : %s"%(card.taunt))
				print("*** lifesteal : %s"%(card.lifesteal))
				print("*** divine_shield : %s"%(card.divine_shield))
				print("*** stealthed : %s"%(card.stealthed))
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_825##########

class pp_RLK_825(Preset_Play):
	""" Shockspitter
	<b>Battlecry:</b> Deal @ damage. <i>(Improved by your hero attacks this game!)</i> """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_825", self.controller)
		self.con2=self.exchange_card(self.card_choice("weapon"), self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con2)
		self.attack_card(self.controller.hero, self.opp1)
		self.change_turn()
		### opp
		self.change_turn()
		### con
		self.play_card(self.con1)
		self.assertion("self.opponent.hero.damage==2")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_826##########

class pp_RLK_826(Preset_Play):
	""" Silvermoon Farstrider
	<b>Battlecry:</b> Give all Arcane spells in your hand <b>Spell Damage +1</b>. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_826", self.controller)
		self.con2=self.exchange_card(self.card_choice("arcane"), self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.assertion("self.con2.spellpower_by_spell==1")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_827##########

class pp_RLK_827(Preset_Play):
	""" Keeneye Spotter (minion:3/3/4)
	Whenever your hero attacks a minion, set its Health to 1. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_827", self.controller)
		self.con2=self.exchange_card(self.card_choice("weapon"), self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH9")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con2)
		self.play_card(self.con1)
		self.attack_card(self.controller.hero, self.opp1)
		self.actions=[action for action in self.controller._targetedaction_log if isinstance(action['class'], Buff)]
		self.assertion("len(self.actions)>0")
		self.action = self.actions[0]
		self.assertion("self.action['target'].id==self.opp1.id")
		self.assertion("self.action['target_args'][0].id=='RLK_827e'")
		self.assertion("self.opp1.dead==True")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_828##########

class pp_RLK_828(Preset_Play):
	""" Hope of Quel'Thalas
	After your hero attacks, give your minions +1/+1 <i>(wherever they are).</i> """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_828", self.controller)
		self.con2=self.exchange_card(self.card_choice("weapon"), self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con2)
		self.play_card(self.con1)
		self.attack_card(self.controller.hero, self.opp1)
		self.assertion("len(self.con4.buffs)==1")
		self.assertion("self.con4.atk==self.con4.data.atk+1")
		self.assertion("self.con4.max_health==self.con4.data.health+1")
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


