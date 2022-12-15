from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give, Shuffle
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def lich_neutral():
	#PresetGame(pp_RLK_029)## OK
	#PresetGame(pp_RLK_070)## OK
	#PresetGame(pp_RLK_104)## OK
	#PresetGame(pp_RLK_113)##OK
	#PresetGame(pp_RLK_117)##OK
	#PresetGame(pp_RLK_119)##OK
	#PresetGame(pp_RLK_123)##OK
	#PresetGame(pp_RLK_218)##OK
	#PresetGame(pp_RLK_219)## OK 
	#PresetGame(pp_RLK_219b)## OK 
	#PresetGame(pp_RLK_220)##OK
	#PresetGame(pp_RLK_221a)## OK
	#PresetGame(pp_RLK_221b)## OK
	#PresetGame(pp_RLK_222)## OK
	#PresetGame(pp_RLK_222b)## OK
	#PresetGame(pp_RLK_222c)## OK
	#PresetGame(pp_RLK_518)## OK
	#PresetGame(pp_RLK_590)## OK
	#PresetGame(pp_RLK_591)##  OK
	#PresetGame(pp_RLK_592)##OK
	#PresetGame(pp_RLK_593)##OK
	#PresetGame(pp_RLK_653)##OK
	#PresetGame(pp_RLK_677)##OK
	#PresetGame(pp_RLK_824)##OK
	#PresetGame(pp_RLK_830)##OK
	#PresetGame(pp_RLK_831)##OK
	#PresetGame(pp_RLK_833)##OK
	#PresetGame(pp_RLK_834)##OK
	#PresetGame(pp_RLK_867)##OK
	#PresetGame(pp_RLK_900)##OK
	#PresetGame(pp_RLK_914)##OK
	#PresetGame(pp_RLK_915)##OK
	#PresetGame(pp_RLK_926)##OK
	#PresetGame(pp_RLK_950)##OK
	#PresetGame(pp_RLK_951)##OK
	#PresetGame(pp_RLK_952)##OK
	#PresetGame(pp_RLK_955)##OK
	#PresetGame(pp_RLK_957)##OK
	#PresetGame(pp_RLK_970)##OK
	pass



##########RLK_029##########

class pp_RLK_029(Preset_Play):
	""" Shatterskin Gargoyle
	<b>Taunt</b> <b>Deathrattle:</b> Deal 4 damage to a random enemy. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_029", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH5")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		Hit(self.con1, 10).trigger(self.opponent)
		self.asserting(self.opponent.hero.damage==4 or self.opp1.damage==4,"self.opponent.hero.damage==4 or self.opp1.damage==4")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.opponent.field:
			self.print_stats("opponent.field", card)
	pass


##########RLK_070##########

class pp_RLK_070(Preset_Play):
	""" Infected Peasant
	<b>Deathrattle:</b> Summon a 2/2 Undead Peasant. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_070", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		Hit(self.con1, 10).trigger(self.opponent)
		self.asserting(self.controller.field[0].id=='RLK_070t',"self.controller.field[0].id=='RLK_070t'")
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("controller.field", card)
	pass


##########RLK_104##########

class pp_RLK_104(Preset_Play):
	""" Street Sweeper
	<b>Battlecry:</b> Deal 2 damage to all other minions. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_104", self.controller)
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
		self.asserting(self.con4.damage==2,'self.con4.damage==2')
		self.asserting(self.opp1.damage==2,'self.opp1.damage==2')
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_113##########

class pp_RLK_113(Preset_Play):
	""" Brittleskin Zombie
	<b>Deathrattle:</b> If it's your opponent's turn, deal 3 damage to them. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_113", self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionH5")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		Hit(self.con1, 10).trigger(self.opponent)
		self.asserting(self.opp1.damage==3,"self.opp1.damage==3")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_117##########

class pp_RLK_117(Preset_Play):
	""" Incorporeal Corporal
	After this minion attacks, destroy it. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_117", self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionH8")).trigger(self.opponent)
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
		### con
		self.attack_card(self.con1,self.opp1)#atk=5
		self.controller.game.process_deaths()
		self.asserting(self.con1.zone==Zone.GRAVEYARD,"self.con1.zone==Zone.GRAVEYARD")
		pass
	def result_inspection(self):
		super().result_inspection()
	pass


##########RLK_119##########

class pp_RLK_119(Preset_Play):
	""" Drakkari Embalmer
	<b>Battlecry:</b> Give a friendly Undead <b>Reborn</b>. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_119", self.controller)
		self.con4=Summon(self.controller, self.card_choice("undead")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con4)
		self.play_card(self.con1, target=self.con4)
		self.asserting(self.con4.reborn==True,"self.con4.reborn==True")
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
	pass


##########RLK_123##########

class pp_RLK_123(Preset_Play):
	""" Bone Flinger
	<b>Battlecry:</b> If a friendly Undead died after your last turn, deal 2 damage. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_123", self.controller)
		self.con4=Summon(self.controller, self.card_choice("undead")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con4)
		self.change_turn()
		### opp
		Hit(self.con4, 10).trigger(self.opponent)
		self.change_turn()
		### con
		self.play_card(self.con1)
		self.assertion("self.opp1.damage==2 or self.opponent.hero.damage==2")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_218##########

class pp_RLK_218(Preset_Play):
	""" Silvermoon Arcanist
	<b>Spell Damage +2</b> <b>Battlecry:</b> Your spells can't target heroes this turn. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_218", self.controller)
		self.con2=self.exchange_card("CORE_BRM_013", self.controller)
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
		self.assertion("self.opponent.hero.cant_be_targeted_by_spells==True")
		#self.assertion("is_valid_target(self.con2, self.opponent.hero)")
		self.play_card(self.con2, target=self.opponent.hero)# spelldamage=3+2
		self.assertion("self.opponent.hero.damage==5")
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_219##########

class pp_RLK_219(Preset_Play):
	""" Sunfury Clergy (cost:3)
	<b>Battlecry:</b> Restore 3 Health to all friendly characters. <b>Manathirst (6):</b> Restore 6 Health instead. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_219", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH8")).trigger(self.controller)
		self.con4=self.con4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		Hit(self.con4, 6).trigger(self.opponent)
		self.play_card(self.con1, target=self.con4)
		self.asserting(self.con4.health==8-6+3,'self.con4.health==8-6+3') 
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("field", card)
	pass
class pp_RLK_219b(Preset_Play):
	""" Sunfury Clergy (cost:3)
	<b>Battlecry:</b> Restore 3 Health to all friendly characters. <b>Manathirst (6):</b> Restore 6 Health instead. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_219", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH8")).trigger(self.controller)
		self.con4=self.con4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		Hit(self.con4, 6).trigger(self.opponent)
		self.controller.max_mana=6
		self.play_card(self.con1, target=self.con4)
		self.asserting(self.con4.health==8-6+6,'self.con4.health==8-6+6') 
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("field", card)
	pass


##########RLK_220##########

class pp_RLK_220(Preset_Play):
	""" Tenacious San'layn (5/4/6)
	<b>Lifesteal</b> Whenever this attacks, deal 2 damage to the enemy hero. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_220", self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionH7")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		Hit(self.controller.hero, 10).trigger(self.opponent)
		self.change_turn()
		### con
		self.attack_card(self.con1, self.opp1)
		self.assertion("self.controller.hero.damage==10-4-2")
		self.assertion("self.opponent.hero.damage==2")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_221##########

class pp_RLK_221a(Preset_Play):
	""" Crystal Broker
	<b>Manathirst (5):</b> Summon a random 3-Cost minion. <b>Manathirst (10):</b> Summon an 8-Cost minion instead. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_221", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.controller.max_mana=5
		self.play_card(self.con1)
		self.asserting(self.controller.field[-1].cost==3,"self.controller.field[-1].cost==3")
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_221b(Preset_Play):
	""" Crystal Broker
	<b>Manathirst (5):</b> Summon a random 3-Cost minion. <b>Manathirst (10):</b> Summon an 8-Cost minion instead. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_221", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.controller.max_mana=10
		self.play_card(self.con1)
		self.asserting(self.controller.field[-1].cost==8,"self.controller.field[-1].cost==8")
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_222##########

class pp_RLK_222(Preset_Play):
	""" Astalor Bloodsworn
	<b>Battlecry:</b> Add Astalor, the Protector to your hand. <b>Manathirst (@):</b> Deal 2 damage. """
	#<Tag enumID="2498" name="MANATHIRST" type="Int" value="4"/>
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_222", self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.controller.max_mana=4
		self.play_card(self.con1)
		### opp
		self.print_stats("self.opp1", self.opp1)
		self.print_stats("self.opponent.hero", self.opponent.hero)
		self.assertion("self.opp1.damage==2 or self.opponent.hero.damage==2")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_222b(Preset_Play):
	""" Astalor, the Protector
	<b>Battlecry:</b> Add Astalor, the Flamebringer to your hand. <b>Manathirst (@):</b> Gain 5 Armor. """
	#<Tag enumID="2498" name="MANATHIRST" type="Int" value="7"/>
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_222t1", self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.controller.max_mana=7
		self.play_card(self.con1)
		### opp
		self.assertion("self.controller.hero.armor==5")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass
class pp_RLK_222c(Preset_Play):
	""" Astalor, the Flamebringer
	<b>Battlecry:</b> Deal 8 damage randomly split between all enemies. <b>Manathirst (10):</b> Deal 8 more. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_222t2", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.controller.max_mana=10
		self.play_card(self.con1)
		### opp
		self.assertion("self.opponent.hero.damage==8+8")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_518##########

class pp_RLK_518(Preset_Play):
	""" Silvermoon Sentinel
	<b>Taunt</b> <b>Manathirst (@):</b> Gain +2/+2 and <b>Divine Shield</b>. """
	#<Tag enumID="2498" name="MANATHIRST" type="Int" value="8"/>	
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_518", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.controller.max_mana=8
		self.play_card(self.con1)
		self.assertion("self.con1.atk==self.con1.data.atk+2")
		self.assertion("self.con1.divine_shield==True")
		### opp
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("field", card, show_buff=True)
	pass


##########RLK_590##########

class pp_RLK_590(Preset_Play):
	""" The Sunwell
	Fill your hand with random spells. Costs (1) less for each other card in your hand. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_590", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card, old_cost=True)
	pass


##########RLK_591##########

class pp_RLK_591(Preset_Play):
	""" Bonelord Frostwhisper
	<b>Deathrattle:</b> For the rest of the game, your first card each turn costs (0). You die in 3 turns. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_591", self.controller)
		self.con2=self.exchange_card("minionA3", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		Hit(self.con1, 10).trigger(self.controller)
		self.costs=[card.cost for card in self.controller.hand]
		self.assertion("len([c for c in self.costs if c!=0])==0")
		self.play_card(self.con2)
		self.costs=[card.cost for card in self.controller.hand]
		self.assertion("len([c for c in self.costs if c==0])==0")
		self.change_turn()		
		### opp
		self.change_turn()		
		### con
		self.change_turn()		
		### opp
		self.change_turn()		
		### con
		self.change_turn()
		self.assertion("self.controller.hero.alive==False")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_592##########

class pp_RLK_592(Preset_Play):
	""" Invincible
	<b>Reborn</b> <b>Battlecry and Deathrattle:</b> Give a random friendly Undead +5/+5 and <b>Taunt</b>. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_592", self.controller)
		self.con4=Summon(self.controller, self.card_choice("undead")).trigger(self.controller)
		self.con4=self.con4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.assertion("self.con4.atk==self.con4.data.atk+5")
		self.assertion("self.con4.taunt==True")
		Hit(self.con1, 10).trigger(self.opponent)
		self.assertion("self.con1.health==1")
		self.assertion("self.con4.atk==self.con4.data.atk+10")
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_593##########
import random

class pp_RLK_593(Preset_Play):
	""" Lor'themar Theron
	<b>Battlecry:</b> Double the stats of all minions in your deck. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_593", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.con2=random.choice([card for card in self.controller.deck if card.type==CardType.MINION])
		self.assertion("self.con2.atk==self.con2.data.atk*2")
		self.assertion("self.con2.max_health==self.con2.data.health*2")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.deck:
			self.print_stats("deck", card, show_buff=True)
	pass


##########RLK_653##########

class pp_RLK_653(Preset_Play):
	""" Infectious Ghoul
	<b>Deathrattle:</b> Give a random friendly minion "<b>Deathrattle:</b> Summon an Infectious Ghoul." """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_653", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con4)
		self.play_card(self.con1)
		Hit(self.con1, 10).trigger(self.controller)
		self.assertion("self.con4.has_deathrattle")
		self.assertion("self.con4.buffs[0].id=='RLK_653e'")
		Hit(self.con4, 10).trigger(self.opponent)
		self.assertion("'RLK_653' in [card.id for card in self.controller.field]")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("field", card)
	pass


##########RLK_677##########

class pp_RLK_677(Preset_Play):
	""" Sanctum Spellbender
	Whenever your opponent targets another minion with a spell, redirect it to this. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_677", self.controller)#
		self.opp1=self.exchange_card("CORE_BRM_013", self.opponent)#
		self.con4=(Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller))[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.change_turn()
		### opp
		self.play_card(self.opp1, target=self.con4)
		self.assertion("self.con4.damage==0")
		self.assertion("self.con1.damage>0")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("field", card)
	pass


##########RLK_824##########

class pp_RLK_824(Preset_Play):
	""" Arms Dealer
	After you summon an Undead, give it +1 Attack. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_824", self.controller)
		self.con2=self.exchange_card("undead", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.play_card(self.con2)
		self.assertion("self.con2.atk==self.con2.data.atk+1")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("field", card)
	pass




##########RLK_830##########

class pp_RLK_830(Preset_Play):
	""" Flesh Behemoth
	<b>Taunt</b> <b>Deathrattle:</b> Draw another Undead and summon a copy of it. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_830", self.controller)
		Shuffle(self.controller, self.card_choice("undead"))
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		Hit(self.con1, 10).trigger(self.controller)
		self.con2=self.controller.field[0]
		self.assertion("self.con2.race==Race.UNDEAD")
		self.assertion("self.con2.id in [card.id for card in self.controller.hand]")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_831##########

class pp_RLK_831(Preset_Play):
	""" Plaguespreader
	<b>Deathrattle:</b> Transform a random minion in your opponent's hand into a Plaguespreader. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_831", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		Hit(self.con1, 10).trigger(self.controller)
		self.assertion("'RLK_831' in [card.id for card in self.opponent.hand]")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.opponent.hand:
			self.print_stats("opponent.hand", card)
	pass


##########RLK_833##########

class pp_RLK_833(Preset_Play):
	""" Foul Egg
	<b>Deathrattle:</b> Summon a 3/3 Undead Chicken. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_833", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		Hit(self.con1, 10).trigger(self.controller)
		self.assertion("'RLK_833t' in [card.id for card in self.controller.field]")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("field", card)
	pass


##########RLK_834##########

class pp_RLK_834(Preset_Play):
	""" Nerubian Vizier
	<b>Battlecry:</b> <b>Discover</b> a spell. If a friendly Undead died after your last turn, it costs (2) less. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_834", self.controller)
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
		self.con2=self.controller.hand[-1]
		self.assertion("self.con2.cost==max(0,self.con2.data.cost-2)")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card, old_cost=True)
	pass


##########RLK_867##########

class pp_RLK_867(Preset_Play):
	""" Vrykul Necrolyte
	<b>Battlecry:</b> Give a friendly minion "<b>Deathrattle:</b> Summon a 2/2 Zombie with <b>Rush</b>." """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_867", self.controller)
		self.con4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.con4=self.con4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1, target=self.con4)
		self.assertion("self.con4.has_deathrattle")
		self.assertion("self.con4.buffs[0].id=='RLK_867e'")
		Hit(self.con4, 10).trigger(self.controller)
		self.assertion("'RLK_018t' in [card.id for card in self.controller.field]")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_900##########

class pp_RLK_900(Preset_Play):
	""" Scourge Rager
	<b>Reborn</b> <b>Battlecry:</b> Die. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_900", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		## die and reborn
		self.cards = [card for card in self.controller.field if card.id==self.con1.id]
		self.assertion("len(self.cards)==1")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("field", card)
	pass


##########RLK_914##########

class pp_RLK_914(Preset_Play):
	""" Umbral Geist
	<b>Deathrattle:</b> Add a random Shadow spell to your hand. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_914", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		Hit(self.con1, 10).trigger(self.controller)
		self.con2=self.controller.hand[-1]#new card
		self.assertion("self.con2.type==CardType.SPELL")
		self.assertion("self.con2.spell_school==SpellSchool.SHADOW")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_915##########

class pp_RLK_915(Preset_Play):
	""" Amber Whelp
	<b>Battlecry:</b> If you're holding a Dragon, deal 3 damage. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_915", self.controller)
		self.con4=Summon(self.controller, self.card_choice("dragon")).trigger(self.controller)
		self.con4=self.con4[0][0]
		self.opp1=Summon(self.opponent, self.card_choice("minionH4")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.assertion("self.opp1.damage==3 or self.opponent.hero.damage==3")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_926##########

class pp_RLK_926(Preset_Play):
	""" Bloodied Knight
	At the end of your turn, deal 2 damage to your hero. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_926", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.assertion("self.controller.hero.damage==0")
		self.change_turn()
		self.assertion("self.controller.hero.damage==2")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_950##########

class pp_RLK_950(Preset_Play):
	""" Translocation Instructor
	<b>Battlecry:</b> Choose an enemy minion. Swap it with a random one in their deck. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_950", self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1, target=self.opp1)
		self.assertion("self.opp1.zone==Zone.DECK")
		self.assertion("len(self.opponent.field)==1")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_951##########

class pp_RLK_951(Preset_Play):
	""" Coroner
	<b>Battlecry:</b> <b>Freeze</b> an enemy minion. <b>Manathirst (6):</b> <b>Silence</b> it first. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_951", self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionH3")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.controller.max_mana=6
		self.play_card(self.con1, target=self.opp1)
		self.assertion("self.opp1.silenced==True")
		self.assertion("self.opp1.frozen==True")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.opponent.field:
			self.print_stats("opponent.field", card)
	pass


##########RLK_952##########

class pp_RLK_952(Preset_Play):
	""" Enchanter
	Enemy minions take double damage during your turn. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_952", self.controller)
		self.opp1=Summon(self.opponent, self.card_choice("minionH5")).trigger(self.opponent)
		self.opp1=self.opp1[0][0]
		self.opp2=Summon(self.opponent, self.card_choice("minionH5")).trigger(self.opponent)
		self.opp2=self.opp2[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		Hit(self.opp1, 1).trigger(self.con1)
		self.assertion("self.opp1.damage==2")
		self.change_turn()
		### opp
		Hit(self.opp2, 1).trigger(self.con1)
		self.assertion("self.opp2.damage==1")
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_955##########

class pp_RLK_955(Preset_Play):
	""" Silvermoon Armorer
	<b>Rush</b> <b>Manathirst (@):</b> Gain +2/+2. """
	#<Tag enumID="2498" name="MANATHIRST" type="Int" value="7"/>	
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_955", self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.controller.max_mana=7
		self.play_card(self.con1)
		self.assertion("self.con1.buffs!=[]")
		self.assertion("self.con1.buffs[0].id=='RLK_955e'")
		self.assertion("self.con1.max_health==self.con1.data.health+2")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.field:
			self.print_stats("field", card)
	pass


##########RLK_957##########

class pp_RLK_957(Preset_Play):
	""" Banshee
	<b>Deathrattle:</b> Give a random friendly Undead +2/+1. """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_957", self.controller)
		self.con4=Summon(self.controller, self.card_choice("undead")).trigger(self.controller)
		self.con4=self.con4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		Hit(self.con1, 10).trigger(self.opponent)
		self.assertion("self.con4.buffs!=[]")
		self.assertion("self.con4.buffs[0].id=='RLK_957e'")
		self.assertion("self.con4.max_health==self.con4.data.health+1")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########RLK_970##########

class pp_RLK_970(Preset_Play):
	""" Hawkstrider Rancher
	After you play a minion, give it +1/+1 and "<b>Deathrattle:</b> Summon a 1/1 Hawkstrider." """
	class1=CardClass.HUNTER
	class2=CardClass.HUNTER
	def preset_deck(self):
		self.con1=self.exchange_card("RLK_970", self.controller)
		self.con2=self.exchange_card(self.card_choice("minionH3"), self.controller)
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.con1)
		self.play_card(self.con2)
		self.assertion("self.con2.buffs[0].id=='RLK_970e'")
		self.assertion("self.con2.has_deathrattle==True")
		self.assertion("self.con2.atk==self.con2.data.atk+1")
		Hit(self.con2, 10).trigger(self.opponent)
		self.assertion("self.controller.field[-1].id=='RLK_970t'")
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


