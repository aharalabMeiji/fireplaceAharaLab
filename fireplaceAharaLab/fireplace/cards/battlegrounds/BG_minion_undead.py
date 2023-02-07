from ..utils import *



BG25__Risen_Rider=True#1 undead ## new 25.2.2
BG25__Rot_Hide_Gnoll=True#1 undead ## new 25.2.2

BG25__Eternal_Knight=True#2 undead ## new 25.2.2
BG25__Nerubian_Deathswarmer=True#2 undead ## new 25.2.2
BG25__Scarlet_Skull=True#2 undead ## new 25.2.2
BG25__Corpse_Refiner=True# 2/2/3 undead/pirate ## new 25.2.2 

BG25__Ghoul_of_the_Feast=True # 3 undead ## new 25.2.2
BG25__Jelly_Belly=True#3 undead ## new 25.2.2
BG25__Lich_Doctor=True#3 undead ## new 25.2.2

BG25__Anubarak_Nerubian_King=True#4 undead ## new 25.2.2
BG25__Handless_Forsaken=True#4 undead ## new 25.2.2
BG25__Possessive_Banshee=True#4 undead ## new 25.2.2

BG25__Hungering_Abomination=True#5 undead ## new 25.2.2
BG24__Sinrunner_Blanchy=True#5 undead/beast ## new 25.2.2
BG25__Soulsplitter=True#5 undead ## new 25.2.2

BG25__Colossus_of_the_Sun=True #6 undead ## new 25.2.2
BG25__Eternal_Summoner=True#6 undead ## new 25.2.2
BG25__Sister_Deathwhisper=True#6 undead ## new 25.2.2

BG_Minion_Undead = []
BG_PoolSet_Undead=[ [],[],[],[],[],[],[]]
BG_Undead_Gold={}


#Risen Rider 1/2/1/Undead	Reborn, Taunt ## OK ## new 25.2.2 
if BG25__Risen_Rider:# 
	BG_Minion_Undead+=['BG25_001']
	BG_Minion_Undead+=['BG25_001_G']
	BG_PoolSet_Undead[1]+=['BG25_001']
	BG_Undead_Gold['BG25_001']='BG25_001_G'
class BG25_001:# (minion)
	""" Risen Rider
	<b>Taunt</b> <b>Reborn</b> """
	pass
class BG25_001_G:# (minion)
	""" Risen Rider
	<b>Taunt</b> <b>Reborn</b> """
	pass



#Rot Hide Gnoll 1/1/4/Undead	- ## new 25.2.2
if BG25__Rot_Hide_Gnoll:# 
	BG_Minion_Undead+=['BG25_013','BG25_013_G']
	BG_PoolSet_Undead[1]+=['BG25_013']
	BG_Undead_Gold['BG25_013']='BG25_013_G'
class BG25_013_Action(GameAction):
	def do(self, source):
		if source.controller.game.this_is_battle:
			source.atk +=1
class BG25_013:# (minion)
	""" Rot Hide Gnoll
	Has +1 Attack for each friendly minion that died this combat. """
	events = Death(FRIENDLY+MINION).on(BG25_013_Action())
	pass
class BG25_013_G_Action(GameAction):
	def do(self, source):
		if source.controller.game.this_is_battle:
			source.atk +=2
class BG25_013_G:# (minion)
	""" Rot Hide Gnoll
	Has +2 Attack for each friendly minion that died this combat. """
	events = Death(FRIENDLY+MINION).on(BG25_013_G_Action())
	pass


from .BG_minion_mecha import BG_Micro_Mummy
if BG_Micro_Mummy:
	##BG_Minion_Undead+=['BG_ULD_217', 'ULD_217e','TB_BaconUps_250','TB_BaconUps_250e',]## no need
	BG_PoolSet_Undead[1].append('BG_ULD_217')
	BG_Undead_Gold['BG_ULD_217']='TB_BaconUps_250'


######## tavern tier 2

#Eternal Knight 2/3/1/Undead	- ## 60% OK  ##new 25.2.2
if BG25__Eternal_Knight:# 
	BG_Minion_Undead+=['BG25_008','BG25_008_e','BG25_008_G','BG25_008pe']
	BG_PoolSet_Undead[2]+=['BG25_008']
	BG_Undead_Gold['BG25_008']='BG25_008_G'
class BG25_008_Action(GameAction):
	def do(self, source):
		if source.controller.game.this_is_battle:
			source.controller.eternal_knight_powered_up += 1
			source.controller.deepcopy_original.eternal_knight_powered_up += 1
			#refresh cards
		elif source.controller.game.this_is_tavern:
			amount = source.controller.eternal_knight_powered_up
			for card in source.controller.hand + source.controller.field + source.controller.opponent.field:
				if card.id=='BG25_008':
					buffs=[bf for bf in card.buffs if bf.id=='BG25_008_e']
					if len(buffs)==0:
						Buff(card, 'BG25_008_e', atk=amount, max_health=amount).trigger(source)
					else: 
						buffs[0].atk=amount
						buffs[0].max_health=amount
class BG25_008:# (minion)
	""" Eternal Knight
	Has +1/+1 for each friendly Eternal Knight that died this __game <i>(wherever this is)</i>. """
	events = [ Death(SELF).after(BG25_008_Action()),## while battle
		Rerole(CONTROLLER).after(BG25_008_Action()),
		Buy(CONTROLLER, SELF).after(BG25_008_Action()),
		Play(CONTROLLER, SELF).after(BG25_008_Action()),
		BeginTurn(CONTROLLER).after(BG25_008_Action())
		]
class BG25_008_e:# (enchantment)
	""" Eternal Legion
	+@/+@. """
	pass
class BG25_008_G_Action(GameAction):
	def do(self, source):
		if source.controller.game.this_is_battle:
			source.controller.eternal_knight_powered_up += 1
			source.controller.deepcopy_original.eternal_knight_powered_up += 1
			#refresh cards
		elif source.controller.game.this_is_tavern:
			amount = source.controller.eternal_knight_powered_up
			for card in source.controller.hand + source.controller.field + source.controller.opponent.field:
				if card.id=='BG25_008':
					buffs=[bf for bf in card.buffs if bf.id=='BG25_008_e']
					if len(buffs)==0:
						Buff(card, 'BG25_008_e', atk=amount*2, max_health=amount*2).trigger(source)
					else: 
						buffs[0].atk=amount*2
						buffs[0].max_health=amount*2
class BG25_008_G:# (minion)
	""" Eternal Knight
	Has +2/+2 for each friendly Eternal Knight that died this __game <i>(wherever this is)</i>. """
	events = [ Death(SELF).after(BG25_008_G_Action()),## while battle
		Rerole(CONTROLLER).after(BG25_008_G_Action()),
		Buy(CONTROLLER, SELF).after(BG25_008_G_Action()),
		Play(CONTROLLER, SELF).after(BG25_008_G_Action()),
		BeginTurn(CONTROLLER).after(BG25_008_G_Action())
		]	
	pass
class BG25_008pe:# (enchantment)
	""" Eternal Knight Player Enchant
	Counts the number of Eternal Knights that died. """
	pass



#Nerubian Deathswarmer 2/1/3/Undead	Battlecry  ## new 25.2.2
if BG25__Nerubian_Deathswarmer:# 
	BG_Minion_Undead+=['BG25_011','BG25_011_G','BG25_011e2','BG25_011pe']
	BG_PoolSet_Undead[2]+=['BG25_011']
	BG_Undead_Gold['BG25_011']='BG25_011_G'
class BG25_011_Action(GameAction):
	def do(self, source):
		source.controller.nerubian_deathswarmer_powered_up += 1
		## rewrite BG25_011pe for all card in field and opponent.field and hand
		for card in source.controller.field+source.controller.hand+source.controller.opponent.field:
			cards=[bf for bf in card.buffs if bf.id=='BG25_011e2']
			if cards!=[]:
				cards[0].atk=source.controller.nerubian_deathswarmer_powered_up
			else:
				Buff(card, 'BG25_011e2', atk=1).trigger(source)
class BG25_011:# (minion)
	""" Nerubian Deathswarmer
	<b>Battlecry:</b> Give your Undead +1 Attack for the rest of the game <i>(wherever they are)</i>. """
	play = BG25_011_Action()
	pass
class BG25_011_G_Action(GameAction):
	def do(self, source):
		source.controller.nerubian_deathswarmer_powered_up += 2
		## rewrite BG25_011pe for all card in field and opponent.field and hand
		for card in source.controller.field+source.controller.hand+source.controller.opponent.field:
			cards=[bf for bf in card.buffs if bf.id=='BG25_011e2']
			if cards!=[]:
				cards[0].atk=source.controller.nerubian_deathswarmer_powered_up
			else:
				Buff(card, 'BG25_011e2', atk=2).trigger(source)
class BG25_011_G:# (minion)
	""" Nerubian Deathswarmer
	<b>Battlecry:</b> Give your Undead +2 Attack for the rest of the game <i>(wherever they are)</i>. """
	play = BG25_011_G_Action()
	pass
class BG25_011e2:# (enchantment)
	""" Undead Army
	+@ Attack """
	#
	pass
class BG25_011pe:# (enchantment)
	""" Undead Bonus Attack Player Enchant [DNT]
	Give Attack to Undead. """
	#
	pass



#Scarlet Skull 2/1/2/Undead	Deathrattle, Reborn ## new 25.2.2 ## OK ##
if BG25__Scarlet_Skull:# 
	BG_Minion_Undead+=['BG25_022','BG25_022_G','BG25_022_Ge','BG25_022e']
	BG_PoolSet_Undead[2]+=['BG25_022']
	BG_Undead_Gold['BG25_022']='BG25_022_G'
class BG25_022_Action(GameAction):
	def do(self, source):
		if source.controller.game.this_is_battle:
			#cards = [card for card in source.controller.field if card.race==Race.UNDEAD]
			cards = [card for card in source.controller.field if race_identity(card,Race.UNDEAD) and card!=source]
			if len(cards):
				Buff(random.choice(cards), 'BG25_022e').trigger(source)
class BG25_022:# (minion)############
	""" Scarlet Skull
	<b>Reborn</b> <b>Deathrattle:</b> Give a friendly Undead +1/+2. """
	deathrattle = BG25_022_Action()
	pass
BG25_022e=buff(1,2)
class BG25_022_G_Action(GameAction):
	def do(self, source):
		if source.controller.game.this_is_battle:
			#cards = [card for card in source.controller.field if card.race==Race.UNDEAD]
			cards = [card for card in source.controller.field if race_identity(card,Race.UNDEAD) and card!=source]
			if len(cards):
				Buff(random.choice(cards), 'BG25_022_Ge').trigger(source)
class BG25_022_G:# (minion)
	""" Scarlet Skull
	<b>Reborn</b> <b>Deathrattle:</b> Give a friendly Undead +2/+4. """
	deathrattle = BG25_022_G_Action()
	pass
BG25_022_Ge=buff(2,4)



if BG25__Corpse_Refiner:# 2/2/3 undead/pirate ## new 25.2.2
	BG_Minion_Undead+=['BG25_033','BG25_033_G']
	BG_PoolSet_Undead[2]+=['BG25_033']
	BG_Undead_Gold['BG25_033']='BG25_033_G'
class BG25_033_Action(GameAction):
	def do(self, source):
		amount = getattr(source,'gambler_sell_price',0)
		amount +=1
		SetAttr(source, 'gambler_sell_price', amount).trigger(source)
		source.script_data_text_0=str(amount)
class BG25_033:# (minion)
	""" Corpse Refiner
	<b>Avenge (4):</b> This minion sells for 1 more Gold.@<b>Avenge (4):</b> This minion sells for 1 more Gold. __<i>(Sells for {0} extra Gold!)</i> """
	## tag 1587 gambler_sell_price
	tags={1587:1}
	Death(FRIENDLY + MINION).on(Avenge(SELF, 4, [BG25_033_Action()]))
	pass
class BG25_033_G_Action(GameAction):
	def do(self, source):
		amount = getattr(source,'gambler_sell_price',0)
		amount +=2
		SetAttr(source, 'gambler_sell_price', amount).trigger(source)
		source.script_data_text_0=str(amount)
class BG25_033_G:# (minion)
	""" Corpse Refiner
	<b>Avenge (4):</b> This minion sells for 2 more Gold.@<b>Avenge (4):</b> This minion sells for 2 more Gold. __<i>(Sells for {0} extra Gold!)</i> """
	tags={1587:1}
	Death(FRIENDLY + MINION).on(Avenge(SELF, 4, [BG25_033_G_Action()]))
	pass


###### tavern tier 3



#Ghoul of the Feast 3/2/4/Undead	Avenge (X) ## new 25.2.2
if BG25__Ghoul_of_the_Feast:# 
	BG_Minion_Undead+=['BG25_002']
	BG_Minion_Undead+=['BG25_002e']
	BG_Minion_Undead+=['BG25_002_G']
	BG_Minion_Undead+=['BG25_002_Ge']
	BG_PoolSet_Undead[3]+=['BG25_002']
	BG_Undead_Gold['BG25_002']='BG25_002_G'
class BG25_002_Action(GameAction):
	def do(self, source):
		if source.controller.game.this_is_battle:
			races=[]
			cards=[]
			for card in source.controller.field:
				if card.race in races:
					index=races.index(card.race)
					cards[index].append(card)
				else:
					races.append(card.race)
					cards.append([card])
			for cds in cards:
				Buff(random.choice(cds), 'BG25_002e').trigger(source)
class BG25_002:# (minion)
	""" Ghoul of the Feast
	<b>Avenge (1):</b> Give a friendly minion of each minion type +3 Attack. """
	events = Death(FRIENDLY + MINION - SELF).on(Avenge(SELF, 1, [BG25_002_Action()]))
	pass
BG25_002e=buff(3,0)
class BG25_002_G_Action(GameAction):
	def do(self, source):
		if source.controller.game.this_is_battle:
			races=[]
			cards=[]
			for card in source.controller.field:
				if card.race in races:
					index=races.index(card.race)
					cards[index].append(card)
				else:
					races.append(card.race)
					cards.append([card])
			for cds in cards:
				Buff(random.choice(cds), 'BG25_002_Ge').trigger(source)
class BG25_002_G:# (minion)
	""" Ghoul of the Feast
	<b>Avenge (1):</b> Give a friendly minion of each minion type +6 Attack. """
	events = Death(FRIENDLY + MINION - SELF).on(Avenge(SELF, 1, [BG25_002_G_Action()]))
	pass
BG25_002_Ge=buff(6,0)



#Jelly Belly 3/3/5/Undead	Reborn ## new 25.2.2
if BG25__Jelly_Belly:# 
	BG_Minion_Undead+=['BG25_005']
	BG_Minion_Undead+=['BG25_005_G']
	BG_Minion_Undead+=['BG25_005_Ge']
	BG_Minion_Undead+=['BG25_005e']
	BG_PoolSet_Undead[3]+=['BG25_005']
	BG_Undead_Gold['BG25_005']='BG25_005_G'
class BG25_005:# (minion)
	""" Jelly Belly
	After a friendly minion is <b>Reborn</b>, gain +3/+3. """
	events = Reborn(FRIENDLY + MINION - SELF).after(Buff(Reborn.TARGET, 'BG25_005e'))
	pass
BG25_005e=buff(3,3)
class BG25_005_G:# (minion)
	""" Jelly Belly
	After a friendly minion is <b>Reborn</b>, gain +6/+6. """
	events = Reborn(FRIENDLY + MINION - SELF).after(Buff(Reborn.TARGET, 'BG25_005_Ge'))
	pass
BG25_005_Ge=buff(6,6)



#Lich Doctor 3/3/2/Undead	Taunt ## new 25.2.2
if BG25__Lich_Doctor:# 
	BG_Minion_Undead+=['BG25_006']
	BG_Minion_Undead+=['BG25_006_G']
	BG_Minion_Undead+=['BG25_006_Ge']
	BG_Minion_Undead+=['BG25_006e']
	BG_PoolSet_Undead[3]+=['BG25_006']
	BG_Undead_Gold['BG25_006']='BG25_006_G'
class BG25_006_Action(GameAction):
	def do(self, source):
		for card in source.controller.field:
			if getattr(card, 'killed_in_former_battle', False):
				Buff(card, 'BG25_006e').trigger(source)
		pass
class BG25_006:# (minion)
	""" Lich Doctor
	<b>Taunt</b>. At the start of your turn, give your minions that _died last combat +1/+1. """
	events = BeginBar(CONTROLLER).on(BG25_006_Action())
	pass
BG25_006e=buff(1,1)
class BG25_006_G_Action(GameAction):
	def do(self, source):
		for card in source.controller.field:
			if getattr(card, 'killed_in_former_battle', False):
				Buff(card, 'BG25_006e').trigger(source)
		pass
class BG25_006_G:# (minion)
	""" Lich Doctor
	<b>Taunt</b>. At the start of your turn, give your minions that _died last combat +2/+2. """
	events = BeginBar(CONTROLLER).on(BG25_006_G_Action())
	pass
BG25_006_Ge=buff(2,2)



##### tavern tier 4

#Anub'arak, Nerubian King 4/4/3/Undead	Deathrattle ## new 25.2.2#############################
if BG25__Anubarak_Nerubian_King:# 
	BG_Minion_Undead+=['BG25_007','BG25_007_G']
	BG_PoolSet_Undead[4]+=['BG25_007']
	BG_Undead_Gold['BG25_007']='BG25_007_G'
class BG25_007_Action(GameAction):
	def do(self, source):
		## cards in battle
		controller=source.controller
		for card in controller.field:
			if race_identity(card,Race.UNDEAD):
				card.atk+=2
		## cards in bar
		controller=getattr(controller, 'deepcopy_original',None)
		if controller:
			for card in controller.field+controller.hand:
				if race_identity(card,Race.UNDEAD):
					card.atk+=2
			for card in controller.opponent.field: ## bartender's cards
				if race_identity(card,Race.UNDEAD):
					card.atk+=2
		pass
class BG25_007:# (minion)
	""" Anub'arak, Nerubian King
	<b>Deathrattle:</b> Your Undead have +2 Attack for the rest of the game <i>(wherever they are)</i>. """
	deathrattle = BG25_007_Action()
	pass
class BG25_007_G_Action(GameAction):
	def do(self, source):
		## cards in battle
		controller=source.controller
		for card in controller.field:
			if race_identity(card,Race.UNDEAD):
				card.atk+=4
		## cards in bar
		controller=getattr(controller, 'deepcopy_original',None)
		if controller:
			for card in controller.field+controller.hand:
				if race_identity(card,Race.UNDEAD):
					card.atk+=4
			for card in controller.opponent.field: ## bartender's cards
				if race_identity(card,Race.UNDEAD):
					card.atk+=4
		pass
class BG25_007_G:# (minion)
	""" Anub'arak, Nerubian King
	<b>Deathrattle:</b> Your Undead have +4 Attack for the rest of the game <i>(wherever they are)</i>. """
	deathrattle = BG25_007_G_Action()
	pass


#Handless Forsaken 4/2/3/Undead	Deathrattle, Reborn ## new 25.2.2
if BG25__Handless_Forsaken:# 
	BG_Minion_Undead+=['BG25_010','BG25_010t','BG25_010_G','BG25_010_Gt']
	BG_PoolSet_Undead[4]+=['BG25_010']
	BG_Undead_Gold['BG25_010']='BG25_010_G'
	BG_Undead_Gold['BG25_010t']='BG25_010_Gt'
class BG25_010:# (minion)
	""" Handless Forsaken
	<b>Deathrattle:</b> Summon a 2/2 Hand with <b>Reborn</b>. """
	deathrattle = Summon(CONTROLLER, 'BG25_010t')
	pass
class BG25_010t:# (minion)
	""" Helping Hand
	<b>Reborn</b> """
	pass
class BG25_010_G:# (minion)
	""" Handless Forsaken
	<b>Deathrattle:</b> Summon a 4/4 Hand with <b>Reborn</b>. """
	deathrattle = Summon(CONTROLLER, 'BG25_010_Gt')
	pass
class BG25_010_Gt:# (minion)
	""" Helping Hand
	<b>Reborn</b> """
	pass



#Possessive Banshee 4/2/7/Undead	Battlecry ## new 25.2.2
if BG25__Possessive_Banshee:# 
	BG_Minion_Undead+=['BG25_004']
	BG_Minion_Undead+=['BG25_004e']
	BG_Minion_Undead+=['BG25_004_G']
	BG_Minion_Undead+=['BG25_004_Ge']
	BG_PoolSet_Undead[4]+=['BG25_004']
	BG_Undead_Gold['BG25_004']='BG25_004_G'
class BG25_004:# (minion)###### TARGET_IF_AVAILABLE??
	""" Possessive Banshee
	<b>Battlecry:</b> Give an Undead +2/+7. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE:Race.UNDEAD}
	play = Buff(TARGET, 'BG25_004e')
	pass
BG25_004e=buff(2,7)
class BG25_004_G:# (minion)
	""" Possessive Banshee
	<b>Battlecry:</b> Give an Undead +4/+14. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_WITH_RACE:Race.UNDEAD}
	play = Buff(TARGET, 'BG25_004_Ge')
	pass
BG25_004_Ge=buff(4,14)




###### tavern tier 5

#Hungering Abomination 5/3/4/Undead	Avenge (X) ## new 25.2.2
if BG25__Hungering_Abomination:# 
	BG_Minion_Undead+=['BG25_014']
	BG_Minion_Undead+=['BG25_014e']
	BG_Minion_Undead+=['BG25_014_G']
	BG_Minion_Undead+=['BG25_014_Ge']
	BG_PoolSet_Undead[5]+=['BG25_014']
	BG_Undead_Gold['BG25_014']='BG25_014_G'
class BG25_014:# (minion)
	""" Hungering Abomination
	<b>Avenge (1):</b> Gain +1/+1 permanently. """
	events = Death(FRIENDLY + MINION).on(Avenge(SELF, 1, [BuffPermanently(SELF, 'BG25_014e')]))
	pass
BG25_014e=buff(1,1)
class BG25_014_G:# (minion)
	""" Hungering Abomination
	<b>Avenge (1):</b> Gain +2/+2 permanently. """
	events = Death(FRIENDLY + MINION).on(Avenge(SELF, 1, [BuffPermanently(SELF, 'BG25_014_Ge')]))
	pass
BG25_014_Ge=buff(2,2)


#Sinrunner Blanchy 5/3/3/Beast, Undead	Reborn ## new 25.2.2
#BG24_005
if BG24__Sinrunner_Blanchy:
	BG_Minion_Undead += ['BG24_005','BG24_005_G']
	BG_PoolSet_Undead[5]+=['BG24_005']
	BG_Undead_Gold['BG24_005']='BG24_005_G'
class BG24_005:
	""" Sinrunner Branky (5/4/4)
	[Reborn]. This is [Reborn] with full Health and enchantments. """
	##< when reborn, effects and max_health will be preserved.>
	pass
class BG24_005_G:
	""" KIGA-reshimono
	[Reborn]. This is [Reborn] with full Health and enchantments."""
	pass



#Soulsplitter 5/5/2/Undead	Reborn, Start of Combat ## new 25.2.2
if BG25__Soulsplitter:# 
	BG_Minion_Undead+=['BG25_023']
	BG_Minion_Undead+=['BG25_023e']
	BG_Minion_Undead+=['BG25_023_G']
	BG_PoolSet_Undead[5]+=['BG25_023']
	BG_Undead_Gold['BG25_023']='BG25_023_G'
class BG25_023_Action(GameAction):
	def do(self, source):
		cards=[card for card in source.controller.field if race_identity(card,Race.UNDEAD)]
		if len(cards):
			Buff(random.choice(cards), 'BG25_023e').trigger(source)
		pass
class BG25_023:# (minion)
	""" Soulsplitter
	<b>Reborn</b> <b>Start of Combat:</b> Give a ___friendly Undead <b>Reborn</b>. """
	events = BeginBattle(CONTROLLER).on(BG25_023_Action())
	pass
BG25_023e=buff(reborn=True)
class BG25_023_G_Action(GameAction):
	def do(self, source):
		#cards=[card for card in source.controller.field if card.Race==Race.UNDEAD]
		cards=[card for card in source.controller.field if race_identity(card,Race.UNDEAD)]
		if len(cards)>2:
			cards = random.sample(cards, 2)
		for card in cards:
			Buff(card, 'BG25_023e').trigger(source)
		pass
class BG25_023_G:# (minion)
	""" Soulsplitter
	<b>Reborn</b> <b>Start of Combat:</b> Give 2 ___friendly Undead <b>Reborn</b>. """
	events = BeginBattle(CONTROLLER).on(BG25_023_G_Action())
	pass



###### tavern tier 6

#Colossus of the Sun 6/6/6/Undead	Divine Shield, Reborn ## new 25.2.2
if BG25__Colossus_of_the_Sun:# 
	BG_Minion_Undead+=['BG25_050','BG25_050_G']
	BG_PoolSet_Undead[6]+=['BG25_050']
	BG_Undead_Gold['BG25_050']='BG25_050_G'
class BG25_050:# (minion)
	""" Colossus of the Sun
	<b>Divine Shield</b> <b>Reborn</b> """
	pass
class BG25_050_G:# (minion)
	""" Colossus of the Sun
	<b>Divine Shield</b> <b>Reborn</b> """
	pass


#Eternal Summoner 6/6/1/Undead	Deathrattle, Reborn ## new 25.2.2
if BG25__Eternal_Summoner:# 
	BG_Minion_Undead+=['BG25_009']
	BG_Minion_Undead+=['BG25_009_G']
	BG_PoolSet_Undead[6]+=['BG25_009']
	BG_Undead_Gold['BG25_009']='BG25_009_G'
class BG25_009:# (minion)
	""" Eternal Summoner
	<b>Deathrattle:</b> Summon 2 Eternal Knights(BG25_008). """
	deathrattle = Summon(CONTROLLER, 'BG25_008')*2
	pass
class BG25_009_G:# (minion)
	""" Eternal Summoner
	<b>Deathrattle:</b> Summon 4 Eternal Knights. """
	deathrattle = Summon(CONTROLLER, 'BG25_008')*4
	pass


#Sister Deathwhisper 6/4/9/Undead	Reborn ## new 25.2.2
if BG25__Sister_Deathwhisper:# 
	BG_Minion_Undead+=['BG25_020','BG25_020e','BG25_020_G','BG25_020_Ge']
	BG_PoolSet_Undead[6]+=['BG25_020']
	BG_Undead_Gold['BG25_020']='BG25_020_G'
class BG25_020:# (minion)
	""" Sister Deathwhisper
	After a friendly minion is <b>Reborn</b>, give your Undead +1/+3 permanently. """
	events = Reborn(FRIENDLY + MINION).after(BuffPermanently(FRIENDLY + MINION + UNDEAD, 'BG25_020e'))
	pass
BG25_020e=buff(1,3)
class BG25_020_G:# (minion)
	""" Sister Deathwhisper
	After a friendly minion is <b>Reborn</b>, give your Undead +2/+6  permanently. """
	events = Reborn(FRIENDLY + MINION).after(BuffPermanently(FRIENDLY + MINION + UNDEAD, 'BG25_020_Ge'))
	pass
BG25_020_Ge=buff(2,6)



#################################