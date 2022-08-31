from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import CardClass, Zone, CardType, Rarity

def sunken_shaman():

	#PresetGame(pp_AIBot_ShamanTrainee_008_hb)##
	#PresetGame(pp_Story_11_Bioluminescente)##
	#PresetGame(pp_Story_11_Errgl_009hb)##
	#PresetGame(pp_Story_11_FireElemental)##
	#PresetGame(pp_Story_11_FlamewreathedFaceless)##
	#PresetGame(pp_Story_11_Hurricane_005hb)##
	#PresetGame(pp_Story_11_Hurricane_005p)##
	#PresetGame(pp_Story_11_PriestessMemory)##
	#PresetGame(pp_Story_11_RadianceofAzshara)##
	#PresetGame(pp_Story_11_ScaldingPuzzle)##
	#PresetGame(pp_Story_11_Sundering_011hb)##
	#PresetGame(pp_Story_11_Sundering_011p)##
	#PresetGame(pp_Story_11_Vortex)##
	#PresetGame(pp_TID_003)##
	#PresetGame(pp_TID_004)##
	#PresetGame(pp_TID_005)##
	#PresetGame(pp_TSC_630)##
	#PresetGame(pp_TSC_631)##
	#PresetGame(pp_TSC_633)##
	#PresetGame(pp_TSC_635)##
	#PresetGame(pp_TSC_637)##
	#PresetGame(pp_TSC_639)##
	#PresetGame(pp_TSC_648)##
	#PresetGame(pp_TSC_772)##
	#PresetGame(pp_TSC_922)##
	#PresetGame(pp_TSC_923)##
	pass


##########AIBot_ShamanTrainee_008_hb##########

class pp_AIBot_ShamanTrainee_008_hb(Preset_Play):
	""" Shaman Trainee
	 """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("AIBot_ShamanTrainee_008_hb", self.controller)
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


##########Story_11_Bioluminescente##########

class pp_Story_11_Bioluminescente(Preset_Play):
	""" Bioluminescent
	[Spell Damage +1]. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_Bioluminescente", self.controller)
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


##########Story_11_Errgl_009hb##########

class pp_Story_11_Errgl_009hb(Preset_Play):
	""" Cousin Errgl
	<i>Though an infrequent and rather disruptive visitor, Errgl is always welcome at the Mrrgglton household.</i> """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_Errgl_009hb", self.controller)
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


##########Story_11_FireElemental##########

class pp_Story_11_FireElemental(Preset_Play):
	""" Fire Elemental
	Whenever your opponent plays a card, deal 4 damage to the enemy hero. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_FireElemental", self.controller)
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


##########Story_11_FlamewreathedFaceless##########

class pp_Story_11_FlamewreathedFaceless(Preset_Play):
	""" Flamewreathed Faceless
	[[Taunt] Deathrattle:] Give the opposing player 3 Mana Crystals. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_FlamewreathedFaceless", self.controller)
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


##########Story_11_Hurricane_005hb##########

class pp_Story_11_Hurricane_005hb(Preset_Play):
	""" Hurricane Elemental
	<i>The elements themselves seem to have turned against you as they rage across the open sea...</i> """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_Hurricane_005hb", self.controller)
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


##########Story_11_Hurricane_005p##########

class pp_Story_11_Hurricane_005p(Preset_Play):
	""" Squall
	[Hero Power] Deal @ damage to a random enemy. <i>(increases each use)</i> """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_Hurricane_005p", self.controller)
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


##########Story_11_PriestessMemory##########

class pp_Story_11_PriestessMemory(Preset_Play):
	""" Priestess' Memory
	Add a Holy spell to your hand. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_PriestessMemory", self.controller)
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


##########Story_11_RadianceofAzshara##########

class pp_Story_11_RadianceofAzshara(Preset_Play):
	""" Radiance of Azshara
	Can't be targeted by spells. At the end of your turn, deal 1  damage to all enemy minions. [Deathrattle:] Advance fight. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_RadianceofAzshara", self.controller)
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


##########Story_11_ScaldingPuzzle##########

class pp_Story_11_ScaldingPuzzle(Preset_Play):
	""" Scalding Geyser
	Deal $2 damage. [Dredge]. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_ScaldingPuzzle", self.controller)
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


##########Story_11_Sundering_011hb##########

class pp_Story_11_Sundering_011hb(Preset_Play):
	""" The Sundering
	 """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_Sundering_011hb", self.controller)
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


##########Story_11_Sundering_011p##########

class pp_Story_11_Sundering_011p(Preset_Play):
	""" Calamitous Flood
	[Hero Power] Deal @ damage to all enemy minions. For each    that dies, gain 1 damage. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_Sundering_011p", self.controller)
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


##########Story_11_Vortex##########

class pp_Story_11_Vortex(Preset_Play):
	""" Vortex
	Deal $3 damage to a random enemy minion. If it dies, recast this. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("Story_11_Vortex", self.controller)
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


##########TID_003##########

class pp_TID_003(Preset_Play):
	""" Tidelost Burrower
	[Battlecry:] [Dredge]. If it's a Murloc, summon a 2/2 copy of it. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("TID_003", self.controller)
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


##########TID_004##########

class pp_TID_004(Preset_Play):
	""" Clownfish
	[Battlecry:] Your next two Murlocs cost (2) less. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("TID_004", self.controller)
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


##########TID_005##########

class pp_TID_005(Preset_Play):
	""" Command of Neptulon
	Summon two 5/4 Elementals with [Rush]. [Overload:] (1) """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("TID_005", self.controller)
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


##########TSC_630##########

class pp_TSC_630(Preset_Play):
	""" Wrathspine Enchanter
	[Battlecry:] Cast a copy of a Fire, Frost, and Nature spell in your hand <i>(targets chosen randomly).</i> """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_630", self.controller)
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


##########TSC_631##########

class pp_TSC_631(Preset_Play):
	""" Schooling
	Add three 1/1 Piranha Swarmers to your hand. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_631", self.controller)
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


##########TSC_633##########

class pp_TSC_633(Preset_Play):
	""" Piranha Poacher
	At the end of your turn, add a 1/1 Piranha Swarmer to your hand. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_633", self.controller)
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


##########TSC_635##########

class pp_TSC_635(Preset_Play):
	""" Radiance of Azshara
	[Fire Spell Damage +2] Your Nature spells cost (1) less. After you cast a Frost spell, gain 3 Armor. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_635", self.controller)
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


##########TSC_637##########

class pp_TSC_637(Preset_Play):
	""" Scalding Geyser
	Deal $2 damage. [Dredge]. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_637", self.controller)
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


##########TSC_639##########

class pp_TSC_639(Preset_Play):
	""" Glugg the Gulper
	[Colossal +3]  After a friendly minion dies, gain its original stats. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_639", self.controller)
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


##########TSC_648##########

class pp_TSC_648(Preset_Play):
	""" Coral Keeper
	[Battlecry:] Summon a 3/3 Elemental for each spell school you've cast this game. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_648", self.controller)
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


##########TSC_772##########

class pp_TSC_772(Preset_Play):
	""" Azsharan Scroll
	[Discover] a Fire, Frost or Nature spell. Put a 'Sunken Scroll' on the bottom of your deck. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_772", self.controller)
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


##########TSC_922##########

class pp_TSC_922(Preset_Play):
	""" Anchored Totem
	After you summon a 1-Cost minion, give it +2/+1. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_922", self.controller)
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


##########TSC_923##########

class pp_TSC_923(Preset_Play):
	""" Bioluminescence
	Give your minions [Spell Damage +1]. """
	class1=CardClass.SHAMAN
	class2=CardClass.SHAMAN
	def preset_deck(self):
		self.con1=self.exchange_card("TSC_923", self.controller)
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


