from .simulate_game import Preset_Play,PresetGame
from fireplace.actions import Hit, Summon, Give
from hearthstone.enums import Zone, CardType, Rarity

def stormwind_paladin():

	#PresetGame(pp_DED_500)##  OKOK
	#PresetGame(pp_DED_501)##OKOK
	#PresetGame(pp_DED_502)##
	#PresetGame(pp_SW_046)##
	#PresetGame(pp_SW_047)##
	#PresetGame(pp_SW_048)##
	#PresetGame(pp_SW_049)##OK
	#PresetGame(pp_SW_305)##
	#PresetGame(pp_SW_313)##
	#PresetGame(pp_SW_314)##
	#PresetGame(pp_SW_315)##
	#PresetGame(pp_SW_316)##
	#PresetGame(pp_SW_317)##
	pass



##########DED_500##########

class pp_DED_500(Preset_Play):
	""" Wealth Redistributor
	[Taunt]. [Battlecry:] Swap theAttack of the highest andlowest Attack minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_500", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionA1")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		self.mark5=Summon(self.controller, self.card_choice("minionA3")).trigger(self.controller)
		self.mark5=self.mark5[0][0]
		self.mark6=Summon(self.controller, self.card_choice("minionA5")).trigger(self.controller)
		self.mark6=self.mark6[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark1)
		#self.change_turn()
		### opp
		#self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		assert self.mark4.atk==5, "atk"
		assert self.mark5.atk==3, "atk"
		assert self.mark6.atk==1, "atk"
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########DED_501##########

class pp_DED_501(Preset_Play):
	""" Sunwing Squawker
	[Battlecry:] Repeat the last spell you've cast on a__friendly minion on this. """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_501", self.controller)
		self.mark2=self.exchange_card("SW_316", self.controller)
		self.mark4=Summon(self.controller, self.card_choice("minionH3")).trigger(self.controller)
		self.mark4=self.mark4[0][0]
		super().preset_deck()
		pass
	def preset_play(self):
		super().preset_play()
		### con
		self.play_card(self.mark2, target=self.mark4)
		self.play_card(self.mark1)
		self.change_turn()
		### opp
		self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		print("mark1 got +1/+1 (SW_316e) and divine_shield ")
		#assert self.mark1.atk==self.mark1.data.atk+1, "atk"
		#assert self.mark1.health==self.mark1.data.health+1, "health"
		assert 'SW_316e' in [buff.id for buff in self.mark1.buffs], "buff"
		assert self.mark1.divine_shield==True, "shield"
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########DED_502##########

class pp_DED_502(Preset_Play):
	""" Righteous Defense
	Set a minion's Attack and Health to 1. Give the stats it lost to a minion in your hand. """
	def preset_deck(self):
		self.mark1=self.exchange_card("DED_502", self.controller)
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


##########SW_046##########

class pp_SW_046(Preset_Play):
	""" City Tax
	[Tradeable][Lifesteal]. Deal $1 damageto all enemy minions. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_046", self.controller)
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


##########SW_047##########

class pp_SW_047(Preset_Play):
	""" Highlord Fordragon
	[Divine Shield]After a friendly minion loses[Divine Shield], give a minion__in your hand +5/+5. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_047", self.controller)
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


##########SW_048##########

class pp_SW_048(Preset_Play):
	""" Prismatic Jewel Kit
	After a friendly minion loses[Divine Shield], give minionsin your hand  +1/+1.Lose 1 Durability. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_048", self.controller)
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


##########SW_049##########

class pp_SW_049(Preset_Play):
	""" Blessed Goods
	[Discover] a [Secret], weapon, or [Divine Shield] minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_049", self.controller)
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
		#self.change_turn()
		pass
	def result_inspection(self):
		super().result_inspection()
		for card in self.controller.hand:
			self.print_stats("hand", card)
	pass


##########SW_305##########

class pp_SW_305(Preset_Play):
	""" First Blade of Wrynn
	[Divine Shield][Battlecry:] Gain [Rush] if thishas at least 4 Attack. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_305", self.controller)
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


##########SW_313##########

class pp_SW_313(Preset_Play):
	""" Rise to the Occasion
	[Questline:] Play 3 different 1-Cost cards.[Reward:] Equip a 1/4 Light's Justice. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_313", self.controller)
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


##########SW_314##########

class pp_SW_314(Preset_Play):
	""" Lightbringer's Hammer
	[Lifesteal]Can't attack heroes. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_314", self.controller)
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


##########SW_315##########

class pp_SW_315(Preset_Play):
	""" Alliance Bannerman
	[Battlecry:] Draw a minion.Give minions in yourhand +1/+1. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_315", self.controller)
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


##########SW_316##########

class pp_SW_316(Preset_Play):
	""" Noble Mount
	Give a minion +1/+1and [Divine Shield].When it dies, summona Warhorse. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_316", self.controller)
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


##########SW_317##########

class pp_SW_317(Preset_Play):
	""" Catacomb Guard
	[Lifesteal][Battlecry:] Deal damageequal to this minion's Attackto an enemy minion. """
	def preset_deck(self):
		self.mark1=self.exchange_card("SW_317", self.controller)
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


