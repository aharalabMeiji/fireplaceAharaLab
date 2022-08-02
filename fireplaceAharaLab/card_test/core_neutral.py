from .simulate_game import Preset_Play,PresetGame
from hearthstone.enums import Zone,CardType, Rarity,CardClass

from fireplace.cards.core.core_neutral import * 
from fireplace.actions import *

def core_neutral():
	#if core_neutral.Ice_Rager:##22.6
	#if core_neutral.Toxicologist=False##22.6
	if Mistress_of_Mixtures:## 23.6
		PresetGame(pp_CORE_CFM_120)
	#Earthen_Ring_Farseer=False##22.6
	#River_Crocolisk=False##22.6
	if Raid_Leader:##22.6## 23.6
		PresetGame(pp_CORE_CS2_122)
	if Kobold_Geomancer:##22.6## 23.6
		PresetGame(pp_CORE_CS2_142)
	#Sen_jin_Shieldmasta=True##22.6## 23.6
	#Injured_Blademaster=False##22.6
	#Chillwind_Yeti=True##22.6## 23.6
	#Abusive_Sergeant=True##22.6## 23.6
	#Elven_Archer=True##22.6## 23.6
	#Ironbeak_Owl=True##22.6## 23.6
	#Stormwind_Champion=True##22.6## 23.6
	#Sunreaver_Spy=True##22.6## 23.6
	#Young_Priestess=False##22.6
	#Big_Game_Hunter=True##22.6## 23.6
	#Acolyte_of_Pain=True## 23.6
	#Argent_Squire=False##22.6
	#Worgen_Infiltrator=True##22.6## 23.6
	#Voodoo_Doctor=True##22.6## 23.6
	#Bloodmage_Thalnos=True##22.6## 23.6
	#King_Mukla=False##22.6
	#Jungle_Panther=True##22.6## 23.6
	#Stranglethorn_Tiger=True##22.6## 23.6
	#Twilight_Drake=True## 23.6
	#Dark_Iron_Dwarf=True##22.6## 23.6
	#Youthful_Brewmaster=True##22.6## 23.6
	#Crazed_Alchemist=True##22.6## 23.6
	#Acidic_Swamp_Ooze=True##22.6## 23.6
	#Mad_Bomber=True##22.6## 23.6
	#Defender_of_Argus=True##22.6## 23.6
	#Gadgetzan_Auctioneer=True##22.6## 23.6
	#Loot_Hoarder=True##22.6## 23.6
	#Coldlight_Seer=True##22.6## 23.6
	#Cairne_Bloodhoof=True##22.6## 23.6
	#Dire_Wolf_Alpha=True##22.6## 23.6
	#SI_7_Infiltrator=True##22.6## 23.6
	#Arcane_Devourer=True##22.6## 23.6
	#Barrens_Stablehand=False##22.6
	#Brightwing=False##22.6
	#High_Inquisitor_Whitemane=False##22.6
	#Baron_Geddon=True##22.6## 23.6
	#Azure_Drake=True## 23.6
	#Gurubashi_Berserker=False##22.6
	#Murloc_Tidehunter=True##22.6## 23.6
	#Murloc_Scout=True##22.6## 23.6
	#Murloc_Warleader=True## 23.6
	#Murloc_Tidecaller=True##22.6## 23.6
	#Faceless_Manipulator=True##22.6## 23.6
	#Sea_Giant=True## 23.6
	#Nerubian_Egg=True##22.6## 23.6
	#Baron_Rivendare=False##22.6
	#Mossy_Horror=True## 23.6
	#Lifedrinker=True## 23.6
	#ElveCogmastern_Archer=False##22.6
	#Spider_Tank=False##22.6
	#Explosive_Sheep=True##22.6## 23.6
	#Annoy_o_Tron=True##22.6## 23.6
	#Mini_Mage=False##22.6
	#Clockwork_Giant=False##22.6
	#Grim_Necromancer=True##22.6## 23.6
	#Cobalt_Scalebane=True## 23.6
	#Arcane_Anomaly=False##22.6
	#Reno_Jackson=True## 23.6
	#Gorillabot_A_3=True## 23.6
	#Sir_Finley_Mrrgglton=True## 23.6
	#Brann_Bronzebeard=True## 23.6
	#Elise_Starseeker=True## 23.6
	#Murloc_Tinyfin=True##22.6## 23.6
	#Lone_Champion=True##22.6## 23.6
	#Stoneskin_Basilisk=True##22.6
	#Sleepy_Dragon=True##22.6## 23.6
	#Plated_Beetle=True## 23.6
	#Zola_the_Gorgon=True## 23.6
	#Bloodsail_Raider=True##22.6## 23.6
	#Wild_Pyromancer=True## 23.6
	#Doomsayer=True## 23.6
	#Faerie_Dragon=True## 23.6
	#Violet_Teacher=True##22.6## 23.6
	#Southsea_Captain=True##22.6## 23.6
	#Flesheating_Ghoul=False##22.6
	#Beaming_Sidekick=True## 23.6
	#Vulpera_Scoundrel=True## 23.6
	#Injured_Tolvir=True## 23.6
	#Stormwatcher=True##22.6## 23.6
	#Humongous_Razorleaf=True##22.6## 23.6
	#Primordial_Drake=True## 23.6
	#Tar_Creeper=True## 23.6
	#Escaped_Manasaber=True## 23.6
	#Fogsail_Freebooter=True##22.6## 23.6
	#Taelan_Fordring=True##22.6## 23.6
	#Overlord_Runthak=True##22.6## 23.6
	#Alexstrasza_the_Life_Binder=True##22.6## 23.6
	#Onyxia_the_Broodmother=True##22.6## 23.6
	#Ysera_the_Dreamer=True##22.6## 23.6
	#Malygos_the_Spellweaver=True##22.6## 23.6
	#Nozdormu_the_Eternal=True##22.6## 23.6
	#Deathwing_the_Destroyer=True##22.6## 23.6
	#Emerald_Skytalon=True##22.6## 23.6
	#Redgill_Razorjaw=True##22.6## 23.6
	#PresetGame(pp_CORE_EX1_189)#OK
	pass

##################################

class pp_CORE_CFM_120(Preset_Play):# <12>[1637]
	""" Mistress of Mixtures
	[Deathrattle:] Restore #4 Health to each hero. """
	class1=CardClass.HUNTER
	class2=CardClass.PRIEST
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CFM_120',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		Hit(opponent.hero, 5).trigger(controller)
		assert opponent.hero.health==30-5, "stop"
		Hit(controller.hero, 6).trigger(opponent)
		assert controller.hero.health==30-6, "stop"
		self.play_card(self.mark1, controller)
		Hit(self.mark1, 10).trigger(opponent)
		controller.game.process_deaths()
		assert self.mark1.zone == Zone.GRAVEYARD, "stop"
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		opponent = controller.opponent
		assert controller.hero.health==30-6+4, "stop"
		assert opponent.hero.health==30-5+4, "stop"
		print("CORE_CFM_120 OK")
		pass
	pass

###########

class pp_CORE_CS2_122(Preset_Play):# <12> 1637 #OK
	""" Raid Leader
	Your other minions have +1 Attack. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_122',controller)#
		self.mark3=self.exchange_card('minionA5',opponent)#
		super().preset_deck()
		self.mark2=controller.hand[0]
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark2, controller)
		self.play_card(self.mark1, controller)
		assert len(self.mark2.buffs)>0, "with buff"
		assert self.mark2.buffs[0].id=='CS2_122e',"with buff"
		assert self.mark2.atk == self.mark2.data.atk + 1, "buffed"
		self.change_turn(controller)
		self.play_card(self.mark3, opponent)
		self.change_turn(opponent)
		self.change_turn(controller)
		self.attack_card(self.mark3, self.mark1,opponent)
		assert self.mark1.zone==Zone.GRAVEYARD, "dead"
		assert self.mark2.buffs==[], "refresh aura buff"
		assert self.mark2.atk == self.mark2.data.atk, "no buff"
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.opponent.hero
		print("CORE_CS2_122 OK")
		pass

	########

class pp_CORE_CS2_142(Preset_Play):# <12> 1637 #OK
	""" Kobold_Geomancer
	[Spell Damage +1] """
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_CS2_142',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		assert controller.spellpower==0, "default spellpower"
		##########controller
		self.play_card(self.mark1, controller)
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark3, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.opponent.hero
		assert controller.spellpower==1, "modified spellpower"
		pass


	##########
class pp_CORE_EX1_189(Preset_Play):# <6>[1637]
	""" Brightwing
	[Battlecry:] Add a random [Legendary] minion to your_hand. """
	class1=CardClass.PRIEST
	class2=CardClass.PRIEST
	def preset_deck(self):
		controller=self.player
		opponent = controller.opponent
		self.mark1=self.exchange_card('CORE_EX1_189',controller)#
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		controller = self.player
		opponent = controller.opponent
		game = controller.game
		##########controller
		self.play_card(self.mark1, controller)
		#self.change_turn(controller)
		##########opponent
		#self.play_card(self.mark3, opponent)#
		#self.change_turn(opponent)
		pass
	def result_inspection(self):
		super().result_inspection()
		controller = self.player
		hero = controller.opponent.hero
		for card in controller.hand:
			self.print_stats ("controller.hand", card)
		pass

##################################

