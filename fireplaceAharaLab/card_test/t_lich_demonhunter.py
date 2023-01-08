from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give, Destroy
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def lich_demonhunter():

	#PresetGame(pp_RLK_206)##OK
	#PresetGame(pp_RLK_207)##OK
	#PresetGame(pp_RLK_208)##OK
	#PresetGame(pp_RLK_208a)##OK
	#PresetGame(pp_RLK_209)##OK
	#PresetGame(pp_RLK_210)##OK
	#PresetGame(pp_RLK_211)##OK
	#PresetGame(pp_RLK_211a)##OK
	#PresetGame(pp_RLK_212)##OK
	#PresetGame(pp_RLK_212a)##OK
	#PresetGame(pp_RLK_213)##OK
	#PresetGame(pp_RLK_214)##OK
	#PresetGame(pp_RLK_215)##OK
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
		self.opp1=Summon(self.opponent, self.card_choice("minionH6")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		for card in reversed(self.controller.deck):
			if card.type==CardType.MINION:
				Destroy(card).trigger(self.controller)
		self.play_card(self.con1, target=self.opp1)
		self.assertion("self.opp1.damage==4")
		self.cards = [card for card in self.controller.field if card.id=='BT_036t']
		self.assertion("len(self.cards)==4")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_208a(Preset_Play):
	""" Fel'dorei Warband
	Deal $4 damage. If your deck has no minions, summon four 1/1 Illidari with <b>Rush</b>. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_208", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH6")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		#for card in reversed(self.controller.deck):
		#	if card.type==CardType.MINION:
		#		Destroy(card).trigger(self.controller)
		self.play_card(self.con1, target=self.opp1)
		self.assertion("self.opp1.damage==4")
		self.cards = [card for card in self.controller.field if card.id=='BT_036t']
		self.assertion("len(self.cards)==0")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_209##########

class pp_RLK_209(Preset_Play):
	""" Unleash Fel (spell:1)
	Deal $1 damage to all enemies. <b>Manathirst_(4):</b> With <b>Lifesteal</b>. """
	## manathirst 4 -> 6 (25.0.4)
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_209", self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		Hit(self.controller.hero, 10)
		self.play_card(self.con1)
		self.assertion("self.opp1.damage==1")
		self.assertion("self.opponent.hero.damage==1")
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_209a(Preset_Play):
	""" Unleash Fel (spell:1)
	Deal $1 damage to all enemies. <b>Manathirst_(4):</b> With <b>Lifesteal</b>. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_209", self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		Hit(self.controller.hero, 10)
		self.controller.max_mana=6
		self.play_card(self.con1)
		self.assertion("self.opp1.damage==1")
		self.assertion("self.opponent.hero.damage==1")
		self.assertion("self.controller.damage==10-2")
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
		self.con2=self.exchange_card("RLK_207", self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.lenhand=len(self.controller.hand)
		self.play_card(self.con2)
		self.assertion("len(self.controller.hand)==self.lenhand")
		self.con3=self.controller.hand[-1]
		self.assertion("getattr(self.con3, 'outcast_card')==1")
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
		for card in reversed(self.controller.deck):
			if card.type==CardType.MINION:
				Destroy(card).trigger(self.controller)
		self.play_card(self.con1)
		self.RLK_211t_count=len([card for card in self.controller.field if card.id=='RLK_211t'])
		self.assertion("self.RLK_211t_count==3")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_211a(Preset_Play):
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
		#for card in reversed(self.controller.deck):
		#	if card.type==CardType.MINION:
		#		Destroy(card).trigger(self.controller)
		self.play_card(self.con1)
		self.RLK_211t_count=len([card for card in self.controller.field if card.id=='RLK_211t'])
		self.assertion("self.RLK_211t_count==2")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_212##########

class pp_RLK_212(Preset_Play):
	""" Brutal Annihilan (minion:9/9/9)
	<b>Taunt</b>, <b>Rush</b> After this minion survives damage, deal that amount to the enemy hero. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_212", self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionA3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		#self.attack_card(self.opp1, self.con1)
		Hit(self.con1, 4).trigger(self.controller)
		self.assertion("self.opponent.hero.damage==4")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_212a(Preset_Play):
	""" Brutal Annihilan (minion:9/9/9)
	<b>Taunt</b>, <b>Rush</b> After this minion survives damage, deal that amount to the enemy hero. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_212", self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionA3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		Hit(self.con1, 10).trigger(self.controller)
		self.assertion("self.opponent.hero.damage==0")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_213##########

class pp_RLK_213(Preset_Play):
	""" Vengeful Walloper (minion:7/5/5)
	<b>Rush</b>. Costs (1) less for each <b>Outcast</b> card you've played this game. """
	class1=CardClass.DEMONHUNTER
	class2=CardClass.DEMONHUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_213", self.controller)
		self.con2=self.exchange_card("RLK_207", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con2)
		self.assertion("self.con1.cost==self.con1.data.cost-1")
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
		#self.con1=self.exchange_card("RLK_214", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		#self.play_card(self.con1)
		self.cards = [card for card in self.controller.deck if card.id=='RLK_214t']
		self.assertion("len(self.cards)>0") 
		self.con2=self.cards[0]
		self.assertion("len(self.con2.entourage)==3")
		self.con2.zone=Zone.HAND
		self.amount=len(self.controller.hand)
		self.play_card(self.con2)
		self.choose_action()
		self.assertion("len(self.controller.hand)==self.amount")
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
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.amount=len(self.controller.hand)		
		self.play_card(self.con1)
		self.assertion("len(self.controller.hand)==self.amount")
		self.con2=self.controller.hand[-1]
		self.assertion("self.con2.cost==self.con2.data.cost-2")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass

#############################################################


