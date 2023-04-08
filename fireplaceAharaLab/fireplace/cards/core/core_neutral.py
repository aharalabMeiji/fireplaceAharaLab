from ..utils import *

Core_Neutral=[]

Ice_Rager=False##22.6
Toxicologist=False##22.6
Mistress_of_Mixtures=True## 23.6
Earthen_Ring_Farseer=False##22.6
River_Crocolisk=False##22.6
Raid_Leader=True##22.6## 23.6
Kobold_Geomancer=True##22.6## 23.6
Sen_jin_Shieldmasta=True##22.6## 23.6
Injured_Blademaster=False##22.6
Chillwind_Yeti=True##22.6## 23.6
Abusive_Sergeant=True##22.6## 23.6
Elven_Archer=True##22.6## 23.6
Ironbeak_Owl=True##22.6## 23.6
Stormwind_Champion=True##22.6## 23.6
Sunreaver_Spy=True##22.6## 23.6
Young_Priestess=False##22.6
Big_Game_Hunter=True##22.6## 23.6
Acolyte_of_Pain=True## 23.6
Argent_Squire=False##22.6
Worgen_Infiltrator=True##22.6## 23.6
Voodoo_Doctor=True##22.6## 23.6
Bloodmage_Thalnos=True##22.6## 23.6
King_Mukla=False##22.6
Jungle_Panther=True##22.6## 23.6
Stranglethorn_Tiger=True##22.6## 23.6
Twilight_Drake=True## 23.6
Dark_Iron_Dwarf=True##22.6## 23.6
Youthful_Brewmaster=True##22.6## 23.6
Crazed_Alchemist=True##22.6## 23.6
Acidic_Swamp_Ooze=True##22.6## 23.6
Mad_Bomber=True##22.6## 23.6
Defender_of_Argus=True##22.6## 23.6
Gadgetzan_Auctioneer=True##22.6## 23.6
Loot_Hoarder=True##22.6## 23.6
Coldlight_Seer=True##22.6## 23.6
Cairne_Bloodhoof=True##22.6## 23.6
Dire_Wolf_Alpha=True##22.6## 23.6
SI_7_Infiltrator=True##22.6## 23.6
Arcane_Devourer=True##22.6## 23.6
Barrens_Stablehand=False##22.6
Brightwing=False##22.6
High_Inquisitor_Whitemane=False##22.6
Baron_Geddon=True##22.6## 23.6
Azure_Drake=True## 23.6
Gurubashi_Berserker=False##22.6
Murloc_Tidehunter=True##22.6## 23.6
Murloc_Scout=True##22.6## 23.6
Murloc_Warleader=True## 23.6
Murloc_Tidecaller=True##22.6## 23.6
Faceless_Manipulator=True##22.6## 23.6
Sea_Giant=True## 23.6
Nerubian_Egg=True##22.6## 23.6
Baron_Rivendare=False##22.6
Mossy_Horror=True## 23.6
Lifedrinker=True## 23.6
ElveCogmastern_Archer=False##22.6
Spider_Tank=False##22.6
Explosive_Sheep=True##22.6## 23.6
Annoy_o_Tron=True##22.6## 23.6
Mini_Mage=False##22.6
Clockwork_Giant=False##22.6
Grim_Necromancer=True##22.6## 23.6
Cobalt_Scalebane=True## 23.6
Arcane_Anomaly=False##22.6
Reno_Jackson=True## 23.6
Gorillabot_A_3=True## 23.6
Sir_Finley_Mrrgglton=True## 23.6
Brann_Bronzebeard=True## 23.6
Elise_Starseeker=True## 23.6
Murloc_Tinyfin=True##22.6## 23.6
Lone_Champion=True##22.6## 23.6
Stoneskin_Basilisk=True##22.6
Sleepy_Dragon=True##22.6## 23.6
Plated_Beetle=True## 23.6
Zola_the_Gorgon=True## 23.6
Bloodsail_Raider=True##22.6## 23.6
Wild_Pyromancer=True## 23.6
Doomsayer=True## 23.6
Faerie_Dragon=True## 23.6
Violet_Teacher=True##22.6## 23.6
Southsea_Captain=True##22.6## 23.6
Flesheating_Ghoul=False##22.6
Beaming_Sidekick=True## 23.6
Vulpera_Scoundrel=True## 23.6 
Injured_Tolvir=True## 23.6
Stormwatcher=True##22.6## 23.6
Humongous_Razorleaf=True##22.6## 23.6
Primordial_Drake=True## 23.6
Tar_Creeper=True## 23.6
Escaped_Manasaber=True## 23.6
Fogsail_Freebooter=True##22.6## 23.6
Taelan_Fordring=True##22.6## 23.6
Overlord_Runthak=True##22.6## 23.6
Alexstrasza_the_Life_Binder=True##22.6## 23.6
Onyxia_the_Broodmother=True##22.6## 23.6
Ysera_the_Dreamer=True##22.6## 23.6
Malygos_the_Spellweaver=True##22.6## 23.6
Nozdormu_the_Eternal=True##22.6## 23.6
Deathwing_the_Destroyer=True##22.6## 23.6
Emerald_Skytalon=True##22.6## 23.6
Redgill_Razorjaw=True##22.6## 23.6


if Ice_Rager:
	Core_Neutral+=['CORE_AT_092']
class CORE_AT_092:# <12> 1637 #OK
	""" Ice Rager
	 """
	#
	pass



if Toxicologist:
	Core_Neutral+=['CORE_BOT_083','BOT_083e']
class CORE_BOT_083:# <12> 1637 #OK
	""" Toxicologist
	[Battlecry:] Give your weapon +1 Attack. """
	play = Buff(FRIENDLY+WEAPON,'BOT_083e')
	pass
BOT_083e=buff(atk=1)#<12> 1127


if Mistress_of_Mixtures:# 
	Core_Neutral+=['CORE_CFM_120']
class CORE_CFM_120:# <12>[1637] ## visually OK
	""" Mistress of Mixtures
	[Deathrattle:] Restore #4 Health to each hero. """
	deathrattle = Heal(ALL_HEROES, 4)
	pass


if Earthen_Ring_Farseer:
	Core_Neutral+=['CORE_CS2_117',]
class CORE_CS2_117:# <12> 1637 #OK
	""" Earthen Ring Farseer
	[Battlecry:] Restore #3_Health. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Heal(TARGET, 3)
	pass



if River_Crocolisk:
	Core_Neutral+=['CORE_CS2_120',]
class CORE_CS2_120:# <12> 1637 #OK
	""" River Crocolisk
	 """
	#
	pass



if Raid_Leader:
	Core_Neutral+=['CORE_CS2_122','CS2_122e']
class CORE_CS2_122:# <12> 1637 #OK
	""" Raid Leader
	Your other minions have +1 Attack. """
	update = Refresh(FRIENDLY_MINIONS - SELF, buff="CS2_122e")
	pass
CS2_122e = buff(1,0)# <12> 1635



if Kobold_Geomancer:
	Core_Neutral+=['CORE_CS2_142',]
class CORE_CS2_142:# <12> 1637 #OK
	""" Kobold_Geomancer
	[Spell Damage +1] """
	#
	pass


if Sen_jin_Shieldmasta:
	Core_Neutral+=['CORE_CS2_179',]
class CORE_CS2_179:# <12> 1637 #OK
	""" Sen'jin Shieldmasta
	[Taunt] """
	#
	pass



if Injured_Blademaster:
	Core_Neutral+=['CORE_CS2_181',]
class CORE_CS2_181:# <12> 1637 $OK
	""" Injured Blademaster
	[Battlecry:] Deal 4 damage to HIMSELF. """
	play = Hit(SELF, 4)
	pass



if Chillwind_Yeti:
	Core_Neutral+=['CORE_CS2_182',]
class CORE_CS2_182:# <12> 1637 #OK
	""" Chillwind_Yeti
	 """
	#
	pass



if Abusive_Sergeant:
	Core_Neutral+=['CORE_CS2_188','CS2_188o']
class CORE_CS2_188:# <12> 1637 #this turn OK
	""" Abusive Sergeant
	[Battlecry:] Give a minion +2_Attack this turn. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Buff(TARGET, "CS2_188o")
	pass
CS2_188o = buff(atk=2)# <12> 3
#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>



if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_CS2_189:# <12> 1637 #OK
	""" Elven_Archer
	[Battlecry:] Deal 1 damage. """
	requirements = {PlayReq.REQ_NONSELF_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Hit(TARGET, 1)
	pass




if Ironbeak_Owl:
	Core_Neutral+=['CORE_CS2_203']
class CORE_CS2_203:# <12> 1637 #OK
	""" Ironbeak_Owl
	[Battlecry:] [Silence] a_minion. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Silence(TARGET)
	pass




if Stormwind_Champion:
	Core_Neutral+=['CORE_CS2_222','CS2_222o']
class CORE_CS2_222:# <12> 1637 #OK
	""" Stormwind_Champion
	Your other minions have +1/+1. """
	update = Refresh(FRIENDLY_MINIONS - SELF, buff="CS2_222o")
	pass
CS2_222o = buff(+1, +1)# <12> 1635




if Sunreaver_Spy:
	Core_Neutral+=['CORE_DAL_086','DAL_086e']
class CORE_DAL_086:# <12> 1637 #OK
	""" Sunreaver_Spy
	[Battlecry:] If you control a [Secret], gain +1/+1. """
	play = Find(FRIENDLY_SECRETS) & Buff(SELF, "DAL_086e")
	pass
DAL_086e=buff(1,1)# <12> 1130




if Young_Priestess:
	Core_Neutral+=['CORE_EX1_004','EX1_004e']
class CORE_EX1_004:# <12> 1637  ## visually OK
	""" Young_Priestess
	At the end of your turn, give another random friendly minion +1 Health. """
	events = OWN_TURN_END.on(Buff(RANDOM_OTHER_FRIENDLY_MINION, "EX1_004e"))
	pass
EX1_004e = buff(health=1)# <12> 3




if Big_Game_Hunter:
	Core_Neutral+=['CORE_EX1_005']
class CORE_EX1_005:# <12> 1637 #OK
	""" Big_Game_Hunter
	[Battlecry:] Destroy a minion with 7 or more Attack. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0,
		PlayReq.REQ_TARGET_MIN_ATTACK: 7}
	play = Destroy(TARGET)
	pass


if Acolyte_of_Pain:# 
	Core_Neutral+=['CORE_EX1_007']
class CORE_EX1_007:# <12>[1637] ## visually OK
	""" Acolyte of Pain
	Whenever this minion takes damage, draw a_card. """
	events = SELF_DAMAGE.on(Draw(CONTROLLER))	
	pass


if Argent_Squire:
	Core_Neutral+=['CORE_EX1_008']
class CORE_EX1_008:# <12> 1637 #OK
	""" Argent_Squire
	[Divine Shield] """
	#
	pass




if Worgen_Infiltrator:
	Core_Neutral+=['CORE_EX1_010']
class CORE_EX1_010:# <12> 1637 #OK
	""" Worgen_Infiltrator
	[Stealth] """
	#
	pass




if Voodoo_Doctor:
	Core_Neutral+=['CORE_EX1_011']
class CORE_EX1_011:# <12> 1637 #OK
	""" Voodoo_Doctor
	[Battlecry:] Restore #2_Health. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Heal(TARGET, 2)
	pass




if Bloodmage_Thalnos:
	Core_Neutral+=['CORE_EX1_012']
class CORE_EX1_012:# <12> 1637 #OK
	""" Bloodmage_Thalnos
	[Spell Damage +1][Deathrattle:] Draw a card. """
	deathrattle = Draw(CONTROLLER)
	pass




if King_Mukla:
	Core_Neutral+=['CORE_EX1_014','EX1_014t','EX1_014te']
class CORE_EX1_014:# <12> 1637 #OK
	""" King_Mukla
	[Battlecry:] Give your opponent 2 Bananas. """
	play = Give(OPPONENT, "EX1_014t") * 2
	pass
class EX1_014t:# <12> 3 #OK
	"""Bananas
	Give a minion +1/+1. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "EX1_014te")
EX1_014te = buff(+1, +1)# <12> 3




if Jungle_Panther:
	Core_Neutral+=['CORE_EX1_017']
class CORE_EX1_017:# <12> 1637 #OK
	""" Jungle_Panther
	[Stealth] """
	#
	pass


if Stranglethorn_Tiger:
	Core_Neutral+=['CORE_EX1_028']
class CORE_EX1_028:# <12> 1637 #OK
	""" Stranglethorn_Tiger
	[Stealth] """
	#
	pass


if Twilight_Drake:# 
	Core_Neutral+=['CORE_EX1_043','EX1_043e']
class CORE_EX1_043:# <12>[1637] ## visually OK
	""" Twilight Drake
	[Battlecry:] Gain +1 Health for each card in your hand. """
	play = Buff(SELF, "EX1_043e") * Count(FRIENDLY_HAND)
EX1_043e = buff(health=1)


if Dark_Iron_Dwarf:
	Core_Neutral+=['CORE_EX1_046','EX1_046e']
class CORE_EX1_046:# <12> 1637 ## visually OK
	""" Dark_Iron_Dwarf
	[Battlecry:] Give a minion +2_Attack this turn. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0, 
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Buff(TARGET, "EX1_046e")#with one turn effect
	pass
EX1_046e = buff(atk=2)# <12> 3 #OK




if Youthful_Brewmaster:
	Core_Neutral+=['CORE_EX1_049']
class CORE_EX1_049:# <12> 1637 #OK
	""" Youthful_Brewmaster
	[Battlecry:] Return a friendly minion from the battlefield to your hand. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_NONSELF_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Bounce(TARGET)
	pass




if Crazed_Alchemist:### OK ###
	Core_Neutral+=['CORE_EX1_059','EX1_059e']
class CORE_EX1_059_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):
		if target!=None:
			amount=target.health-target.atk
			Buff(TARGET, "EX1_059e", atk=amount, max_health=-amount).trigger(source)
		pass
class CORE_EX1_059:# <12> 1637  #OK
	""" Crazed_Alchemist
	[Battlecry:] Swap the Attack and Health of a minion. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = CORE_EX1_059_Action(TARGET)
	pass
class EX1_059e:
	pass




if Acidic_Swamp_Ooze:
	Core_Neutral+=['CORE_EX1_066']
class CORE_EX1_066:# <12> 1637 #OK
	""" Acidic_Swamp_Ooze
	[Battlecry:] Destroy your opponent's weapon. """
	play = Destroy(ENEMY_WEAPON)
	pass




if Mad_Bomber:
	Core_Neutral+=['CORE_EX1_082']
class CORE_EX1_082:# <12> 1637 #OK
	""" Mad_Bomber
	[Battlecry:] Deal 3 damage randomly split between all other characters. """
	play = Hit(RANDOM_OTHER_CHARACTER, 1) * 3
	pass




if Defender_of_Argus:
	Core_Neutral+=['CORE_EX1_093','EX1_093e']
class CORE_EX1_093:# <12> 1637 #OK
	""" Defender_of_Argus
	[Battlecry:] Give adjacent minions +1/+1 and [Taunt]. """
	play = Buff(SELF_ADJACENT, "EX1_093e")
	pass
EX1_093e = buff(+1, +1, taunt=True)# <12> 3




if Gadgetzan_Auctioneer:
	Core_Neutral+=['CORE_EX1_095']
class CORE_EX1_095:# <12> 1637 #OK
	""" Gadgetzan_Auctioneer
	Whenever you cast a spell, draw a card. """
	events = OWN_SPELL_PLAY.on(Draw(CONTROLLER))
	pass




if Loot_Hoarder:
	Core_Neutral+=['CORE_EX1_096']
class CORE_EX1_096:# <12> 1637 #OK
	""" Loot_Hoarder
	[Deathrattle:] Draw a card. """
	deathrattle = Draw(CONTROLLER)
	pass




if Coldlight_Seer:
	Core_Neutral+=['CORE_EX1_103','EX1_103e']
class CORE_EX1_103:# <12> 1637 #OK
	""" Coldlight_Seer
	[Battlecry:] Give your other Murlocs +2 Health. """
	play = Buff(FRIENDLY_MINIONS + MURLOC - SELF, "EX1_103e")
	pass
EX1_103e = buff(health=2)# <12> 3




if Cairne_Bloodhoof:
	Core_Neutral+=['CORE_EX1_110','EX1_110t']
class CORE_EX1_110:# <12> 1637 #OK
	""" Cairne_Bloodhoof
	[Deathrattle:] Summon a 5/5 Baine Bloodhoof. """
	deathrattle = Summon(CONTROLLER, "EX1_110t")
	pass
class EX1_110t:# <12> 3
	"""  """




if Dire_Wolf_Alpha:
	Core_Neutral+=['CORE_EX1_162','EX1_162o']
class CORE_EX1_162:# <12> 1637 ## visually OK
	""" Dire_Wolf_Alpha
	Adjacent minions have +1_Attack. """
	update = Refresh(SELF_ADJACENT, buff="EX1_162o")
	pass
EX1_162o = buff(atk=1)# <12> 3




if SI_7_Infiltrator:
	Core_Neutral+=['CORE_EX1_186']
class CORE_EX1_186:# <12> 1637 ## visually OK
	""" SI:7_Infiltrator
	[Battlecry:] Destroy a random enemy [Secret]. """
	play = Destroy(RANDOM(ENEMY_SECRETS))
	pass




if Arcane_Devourer:
	Core_Neutral+=['CORE_EX1_187','EX1_187e']
class CORE_EX1_187:# <12> 1637 ## visually OK
	""" Arcane_Devourer
	Whenever you cast a spell, gain +2/+2. """
	events = OWN_SPELL_PLAY.on(Buff(SELF,'EX1_187e'))
	pass
EX1_187e=buff(atk=2,health=2)# <12> 3




if Barrens_Stablehand:
	Core_Neutral+=['CORE_EX1_188']
class CORE_EX1_188:# <12> 1637 ## visually OK
	""" Barrens_Stablehand
	[Battlecry:] Summon a random Beast. """
	play = Summon(CONTROLLER, RandomBeast())
	pass




if Brightwing:
	Core_Neutral+=['CORE_EX1_189']
class CORE_EX1_189:# <12> 1637 ## visually OK
	""" Brightwing
	[Battlecry:] Add a random [Legendary] minion to your_hand. """
	#play = Give(CONTROLLER,RANDOM(FRIENDLY_DECK + MINION + LEGENDARY))
	play = Give(CONTROLLER,RandomMinion(rarity=Rarity.LEGENDARY))
	pass





if High_Inquisitor_Whitemane:
	Core_Neutral+=['CORE_EX1_190']
class ResummonMinionDiedThisTurn(TargetedAction):
	TARGET = ActionArg()#controller
	def do(self, source, target):
		for _card in target.died_this_turn:
			Summon(target,_card).trigger(target)
class CORE_EX1_190:# <12> 1637 ## visually OK
	""" High_Inquisitor_Whitemane
	[Battlecry:] Summon all friendly minions that died this turn. """
	play = ResummonMinionDiedThisTurn(CONTROLLER)
	pass




if Baron_Geddon:
	Core_Neutral+=['CORE_EX1_249']
class CORE_EX1_249:# <12> 1637 ## visually OK
	""" Baron_Geddon
	At the end of your turn, deal 2 damage to ALL other characters. """
	events = OWN_TURN_END.on(Hit(ALL_CHARACTERS - SELF, 2))
	pass


if Azure_Drake:# 
	Core_Neutral+=['CORE_EX1_284']
class CORE_EX1_284:# <12>[1637] ## visually OK
	""" Azure Drake
	[Spell Damage +1][Battlecry:] Draw a card. """
	play = Draw(CONTROLLER)	
	pass


if Gurubashi_Berserker:
	Core_Neutral+=['CORE_EX1_399','EX1_399e']
class CORE_EX1_399:# <12> 1637 ## visually OK
	""" Gurubashi_Berserker
	Whenever this minion takes damage, gain +3_Attack. """
	events = SELF_DAMAGE.on(Buff(SELF, "EX1_399e"))
	pass
EX1_399e = buff(atk=3)# <12> 1635




if Murloc_Tidehunter:
	Core_Neutral+=['CORE_EX1_506']
class CORE_EX1_506:# <12> 1637 ## visually OK
	""" Murloc_Tidehunter
	[Battlecry:] Summon a 1/1_Murloc Scout. """
	play = Summon(CONTROLLER, "CORE_EX1_506a")
	pass
if Murloc_Scout:
	Core_Neutral+=['CORE_EX1_506a']
class CORE_EX1_506a:# <12> 1637
	""" Murloc_Scout
	 """
	#
	pass


if Murloc_Warleader:# 
	Core_Neutral+=['CORE_EX1_507','EX1_507e']
class CORE_EX1_507:# <12>[1637] ## visually OK
	""" Murloc Warleader
	Your other Murlocs have +2 Attack. """
	update = Refresh(FRIENDLY_MINIONS + MURLOC - SELF, buff="EX1_507e")
EX1_507e = buff(atk=2)

if Murloc_Tidecaller:
	Core_Neutral+=['CORE_EX1_509','EX1_509e']
class CORE_EX1_509:# <12> 1637 ## visually OK
	""" Murloc_Tidecaller
	Whenever you summon a Murloc, gain +1 Attack. """
	events = Summon(CONTROLLER, MURLOC).on(Buff(SELF, "EX1_509e"))
	pass
EX1_509e = buff(atk=1)# <12> 3




if Faceless_Manipulator:
	Core_Neutral+=['CORE_EX1_564']
class CORE_EX1_564:# <12> 1637 ## visually OK
	""" Faceless_Manipulator
	[Battlecry:] Choose a minion and become a copy of it. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_NONSELF_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Morph(SELF, ExactCopy(TARGET))
	pass


if Sea_Giant:# 
	Core_Neutral+=['CORE_EX1_586']
class CORE_EX1_586:# <12>[1637] ## visually OK
	""" Sea Giant
	Costs (1) less for each other minion on the battlefield. """
	cost_mod = -Count(ALL_MINIONS)
	pass


if Nerubian_Egg:
	Core_Neutral+=['CORE_FP1_007','FP1_007t']
class CORE_FP1_007:# <12> 1637 ## visually OK
	""" Nerubian_Egg
	[Deathrattle:] Summon a 4/4 Nerubian. """
	deathrattle = Summon(CONTROLLER, "FP1_007t")
	pass
class FP1_007t:# <12> 3
	""" Nerubian
	"""




if Baron_Rivendare:
	Core_Neutral+=['CORE_FP1_031']
class CORE_FP1_031:# <12> 1637  ## visually OK
	""" Baron_Rivendare
	Your minions trigger their [Deathrattles] twice. """
	update = Refresh(CONTROLLER, {GameTag.EXTRA_DEATHRATTLES: True})
	pass


if Mossy_Horror:# 
	Core_Neutral+=['CORE_GIL_124']
class CORE_GIL_124:# <12>[1637] ## visually OK
	""" Mossy Horror
	[Battlecry:] Destroy all other_minions with 2_or_less_Attack. """
	def play(self):
		controller = self.controller
		opponent = controller.opponent
		for card in controller.field:
			if card != self:
				if card.type==CardType.MINION and card.atk<=2:
					Destroy(card).trigger(self)
		for card in opponent.field:
			if card.type==CardType.MINION and card.atk<=2:
				Destroy(card).trigger(self)
		Deaths().trigger(self)
	pass


if Lifedrinker:# 
	Core_Neutral+=['CORE_GIL_622']
class CORE_GIL_622:# <12>[1637] ## visually OK
	""" Lifedrinker
	[Battlecry:] Deal 3 damage to the enemy hero. Restore #3 Health to your hero. """
	play = Hit(ENEMY_HERO, 3), Heal(FRIENDLY_HERO, 3)
	pass


if ElveCogmastern_Archer:
	Core_Neutral+=['CORE_GVG_013']
class CORE_GVG_013:# <12> 1637 ## visually OK
	""" Cogmaster
	Has +2 Attack while you have a Mech. """
	update = Find(FRIENDLY_MINIONS + MECH) & Refresh(SELF, {GameTag.ATK: +2})
	pass




if Spider_Tank:
	Core_Neutral+=['CORE_GVG_044']
class CORE_GVG_044:# <12> 1637 ## OK
	""" Spider_Tank
	"""
	#
	pass



if Explosive_Sheep:
	Core_Neutral+=['CORE_GVG_076']
class CORE_GVG_076:# <12> 1637 ## visually OK
	""" Explosive_Sheep
	[Deathrattle:] Deal 2 damage to all minions. """
	deathrattle = Hit(ALL_MINIONS, 2)
	pass




if Annoy_o_Tron:
	Core_Neutral+=['CORE_GVG_085']
class CORE_GVG_085:# <12> 1637 ## OK
	""" Annoy-o-Tron
	[Taunt][Divine Shield] """
	pass




if Mini_Mage:
	Core_Neutral+=['CORE_GVG_109']
class CORE_GVG_109:# <12> 1637 ## OK
	""" Mini-Mage
	[Stealth][Spell Damage +1] """
	pass




if Clockwork_Giant:
	Core_Neutral+=['CORE_GVG_121']
class CORE_GVG_121:# <12> 1637  ## visually OK
	""" Clockwork Giant
	Costs (1) less for each card in your opponent's hand. """
	cost_mod = -Count(ENEMY_HAND)
	pass




if Grim_Necromancer:
	Core_Neutral+=['CORE_ICC_026','ICC_026t']
class CORE_ICC_026:# <12> 1637 ## visually OK
	""" Grim Necromancer
	[Battlecry:] Summon two 1/1 Skeletons. """
	play = Summon(CONTROLLER, 'ICC_026t') * 2
	pass
class ICC_026t:# <12> 1001
	""" Skeleton """
	

if Cobalt_Scalebane:# 
	Core_Neutral+=['CORE_ICC_029','ICC_029e']
class CORE_ICC_029:# <12>[1637] ## visually OK
	""" Cobalt Scalebane
	At the end of your turn, give another random friendly minion +3 Attack. """
	events = OWN_TURN_END.on(Buff(RANDOM(FRIENDLY_MINIONS - SELF), 'ICC_029e'))
	pass
ICC_029e=buff(3,0)


if Arcane_Anomaly:
	Core_Neutral+=['CORE_KAR_036','KAR_036e']
class CORE_KAR_036:# <12> 1637 ## visually OK
	""" Arcane Anomaly
	After you cast a spell, give this minion +1 Health. """
	events = OWN_SPELL_PLAY.on(Buff(SELF, "KAR_036e"))
	pass
KAR_036e = buff(health=1)# <12> 23


if Reno_Jackson:# 
	Core_Neutral+=['CORE_LOE_011']
class CORE_LOE_011:# <12>[1637] ## visually OK
	""" Reno Jackson
	[Battlecry:] If your deck has no duplicates, fully heal your hero. """
	powered_up = -FindDuplicates(FRIENDLY_DECK)
	play = powered_up & FullHeal(FRIENDLY_HERO)	
	pass

if Gorillabot_A_3:# 
	Core_Neutral+=['CORE_LOE_039']
class CORE_LOE_039:# <12>[1637] ## visually OK
	""" Gorillabot A-3
	[Battlecry:] If you control another Mech, [Discover] a Mech. """
	powered_up = Find(FRIENDLY_MINIONS + MECH - SELF)
	play = powered_up & DISCOVER(RandomMech())
	pass

if Sir_Finley_Mrrgglton:# 
	Core_Neutral+=['CORE_LOE_076']
class CORE_LOE_076:# <12>[1637] ## OK
	""" Sir Finley Mrrgglton
	[[Battlecry:] Discover] a new basic Hero Power. """
	play = GenericChoiceChangeHeropower(CONTROLLER, RandomBasicHeroPower() * 3)
	pass

if Brann_Bronzebeard:# 
	Core_Neutral+=['CORE_LOE_077']
class CORE_LOE_077:# <12>[1637] ## visually OK
	""" Brann Bronzebeard
	Your [Battlecries] trigger twice. """
	update = Refresh(CONTROLLER, {enums.EXTRA_BATTLECRIES: True})
	pass

if Elise_Starseeker:# 
	Core_Neutral+=['CORE_LOE_079','LOE_019t','LOE_019t2']
class CORE_LOE_079:# <12>[1637] ## OK
	""" Elise Starseeker
	[Battlecry:] Shuffle the 'Map to the Golden Monkey'   into your deck. """
	requirements = {PlayReq.REQ_FRIENDLY_TARGET: 0, PlayReq.REQ_MINION_TARGET: 0}
	play = Shuffle(CONTROLLER, "LOE_019t")
	pass
class LOE_019t:
	"""Map to the Golden Monkey
	Shuffle the Golden Monkey into your deck. Draw a card. """
	play = Shuffle(CONTROLLER, "LOE_019t2"), Draw(CONTROLLER)
class LOE_019t2_Action(GameAction):
	def do(self, source):
		deck_amount=len(source.controller.deck)
		for card in reversed(source.controller.deck):
			card.zone==Zone.GRAVEYARD
		for count in range(deck_amount):
			newcard=get00(RandomLegendaryMinion().evaluate(source))
			newcard.zone=Zone.DECK
		hand_amount=len(source.controller.hand)
		for card in reversed(source.controller.hand):
			card.zone==Zone.GRAVEYARD
		for count in range(hand_amount):
			newcard=get00(RandomLegendaryMinion().evaluate(source))
			newcard.zone=Zone.HAND
		pass

class LOE_019t2:
	"""Golden Monkey
	[Taunt] [Battlecry:] Replace your hand and deck with [Legendary] minions. """
	play = LOE_019t2_Action()


if Murloc_Tinyfin:
	Core_Neutral+=['CORE_LOEA10_3']
class CORE_LOEA10_3:# <12> 1637 ## OK
	""" Murloc Tinyfin
	"""
	#
	pass





if Lone_Champion:
	Core_Neutral+=['CORE_LOOT_124']
class CORE_LOOT_124:###OK
	""" Lone Champion  
	[Battlecry:] If you control no other minions, gain [Taunt] and [Divine Shield]. """
	def play(self):
		controller = self.controller
		if len(controller.field)==1:
			self.taunt = True
			self.divine_shield = True
	pass




if Stoneskin_Basilisk:
	Core_Neutral+=['CORE_LOOT_125']
class CORE_LOOT_125:###OK
	""" Stoneskin Basilisk
	[Divine Shield]  [Poisonous]"""
	pass




if Sleepy_Dragon:
	Core_Neutral+=['CORE_LOOT_137']
class CORE_LOOT_137:###OK
	""" Sleepy Dragon
	[Taunt] """
	pass


if Plated_Beetle:# 
	Core_Neutral+=['CORE_LOOT_413']
class CORE_LOOT_413:# <12>[1637] ## visuall OK
	""" Plated Beetle
	[Deathrattle:] Gain 3 Armor. """
	deathrattle = GainArmor(FRIENDLY_HERO, 3)
	pass

if Zola_the_Gorgon:# 
	Core_Neutral+=['CORE_LOOT_516']
class CORE_LOOT_516:# <12>[1637] ## visuall OK
	""" Zola the Gorgon
	[Battlecry:] Choose a friendly minion. Add a Golden copy of it to your hand. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}	
	play = Give(CONTROLLER, ExactCopy(TARGET))
	pass



if Bloodsail_Raider:
	Core_Neutral+=['CORE_NEW1_018','NEW1_018e']
class CORE_NEW1_018_Action(TargetedAction):
	def do(self,source,target):
		player = target
		weapon = player.weapon
		Buff(source, 'NEW1_018e', atk = weapon.atk).trigger(source)

class CORE_NEW1_018:# <12> 1637 # visually OK
	""" Bloodsail Raider
	[Battlecry:] Gain Attack equal to the Attack of your weapon. """
	play = Find(FRIENDLY_WEAPON) & CORE_NEW1_018_Action(CONTROLLER)
	pass
class NEW1_018e:
	#=buff(atk=ATK(FRIENDLY_WEAPON)) # <12> 3 #
	pass


if Wild_Pyromancer:# 
	Core_Neutral+=['CORE_NEW1_020']
class CORE_NEW1_020:# <12>[1637] ## visually OK
	""" Wild Pyromancer
	After you cast a spell, deal 1 damage to ALL minions. """
	events = OWN_SPELL_PLAY.after(Hit(ALL_MINIONS, 1))
	pass

if Doomsayer:# 
	Core_Neutral+=['CORE_NEW1_021']
class CORE_NEW1_021:# <12>[1637]  ## visually OK
	""" Doomsayer
	At the start of your turn, destroy ALL minions. """
	events = OWN_TURN_BEGIN.on(Destroy(ALL_MINIONS))	
	pass

if Faerie_Dragon:# 
	Core_Neutral+=['CORE_NEW1_023']
class CORE_NEW1_023:# <12>[1637]  ## OK
	""" Faerie Dragon
	Can't be targeted by spells or Hero Powers. """
	#	<Tag enumID="311" name="CANT_BE_TARGETED_BY_SPELLS" type="Int" value="1"/>
	#	<Tag enumID="332" name="CANT_BE_TARGETED_BY_HERO_POWERS" type="Int" value="1"/>
	pass


if Violet_Teacher:
	Core_Neutral+=['CORE_NEW1_026','NEW1_026t']
class CORE_NEW1_026:# <12> 1637  ## visually OK
	""" Violet Teacher
	Whenever you cast a spell, summon a 1/1 Violet Apprentice. """
	events = OWN_SPELL_PLAY.on(Summon(CONTROLLER, "NEW1_026t"))
	pass

class NEW1_026t:# <12> 3
	pass




if Southsea_Captain:
	Core_Neutral+=['CORE_NEW1_027','NEW1_027e']
class CORE_NEW1_027:# <12> 1637  ## visually OK
	""" Southsea Captain
	Your other Pirates have +1/+1. """
	update = Refresh(FRIENDLY_MINIONS + PIRATE - SELF, buff="NEW1_027e")
	pass
NEW1_027e = buff(+1, +1)




if Flesheating_Ghoul:
	Core_Neutral+=['CORE_tt_004','tt_004o']
class CORE_tt_004:# <12> 1637 ## visually OK
	""" Flesheating Ghoul
	Whenever a minion dies, gain +1 Attack. """
	events = Death(MINION).on(Buff(SELF, "tt_004o"))
	pass
tt_004o=buff(atk=1)# <12> 3


if Beaming_Sidekick:# 
	Core_Neutral+=['CORE_ULD_191','ULD_191e']
class CORE_ULD_191:# <12>[1637]  ## visually OK
	""" Beaming Sidekick
	[Battlecry:] Give a friendly minion +2 Health. """
	play = Buff(RANDOM(FRIENDLY_MINIONS - SELF), "ULD_191e")
ULD_191e = buff(0,2)




if Vulpera_Scoundrel:# ### OK ###
	Core_Neutral+=['CORE_ULD_209','ULD_209t']
class CORE_ULD_209:# <12>[1637]  ## visually OK
	""" Vulpera Scoundrel
	[Battlecry]: [Discover] a spell or pick a mystery choice. """
	choose = ("CORE_ULD_209", "ULD_209t")
	play = Discover(CONTROLLER, RandomSpell())
class ULD_209t:
	"""Mystery Choice!
	Add a random spell to your hand.""" 
	play = Give(CONTROLLER, RandomSpell())




if Injured_Tolvir:# 
	Core_Neutral+=['CORE_ULD_271']
class CORE_ULD_271:# <12>[1637] ## visually OK
	""" Injured Tol'vir
	[Taunt][Battlecry:] Deal 3 damage to this minion. """
	play = Hit(SELF, 3)
	pass


if Stormwatcher:
	Core_Neutral+=['CORE_UNG_813']
class CORE_UNG_813:# <12> 1637 ## visually OK
	""" Stormwatcher
	[Windfury] """
	#
	pass




if Humongous_Razorleaf:
	Core_Neutral+=['CORE_UNG_844']
class CORE_UNG_844:# <12> 1637  ## visually OK
	""" Humongous Razorleaf
	Can't attack. """
	#
	pass

if Primordial_Drake:# 
	Core_Neutral+=['CORE_UNG_848']
class CORE_UNG_848:# <12>[1637] ## visually OK
	""" Primordial Drake
	[Taunt][Battlecry:] Deal 2 damageto all other minions. """
	play = Hit(ALL_MINIONS - SELF, 2) 
	pass

if Tar_Creeper:# 
	Core_Neutral+=['CORE_UNG_928']
class CORE_UNG_928:# <12>[1637] ## visually OK
	""" Tar Creeper
	[Taunt]Has +2 Attack during your opponent's turn. """
	events = OWN_TURN_END.on(Buff(SELF, 'UNG_928e'))
	pass
@custom_card
class WUNG_928e:
	tags = {
		GameTag.CARDNAME: "Tar Creeper",
		GameTag.CARDTYPE: CardType.ENCHANTMENT,
		GameTag.ATK: 2,
	}
	events = OWN_TURN_BEGIN.on(Destroy(SELF))

if Escaped_Manasaber:# 
	Core_Neutral+=['CORE_YOD_006']
class CORE_YOD_006:# <12>[1637] ## visually OK
	""" Escaped Manasaber
	[Stealth]Whenever this attacks,gain 1 Mana Crystal this turn only. """
	play = Attack(SELF,ALL_MINIONS).on(ManaThisTurn(CONTROLLER,1))
	pass


if Fogsail_Freebooter:
	Core_Neutral+=['CS3_022']
class CS3_022:# <12> 1637 #OK
	""" Fogsail Freebooter
	[Battlecry:] If you have a weapon equipped, deal_2_damage. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Find(FRIENDLY_WEAPON) & Hit(TARGET, 2)
	pass




if Taelan_Fordring:
	Core_Neutral+=['CS3_024']
class GiveHighestCostMinion(TargetedAction):
	def do(self, source, target):
		_highestCostCards=[]
		for _card in target.deck:
			if _card.type==CardType.MINION:
				if len(_highestCostCards)==0:
					_highestCostCards = [_card]
				elif _highestCostCards[0].cost < _card.cost:
					_highestCostCards = [_card]
				elif _highestCostCards[0].cost == _card.cost:
					_highestCostCards.append(_card)
		if len(_highestCostCards)>0:
			_card = random.choice(_highestCostCards)##
			_cost = _card.cost
			if Config.LOGINFO:
				print("Highest cost minion is %r (cost %d)"%(_card, _cost))
			Give(target,_card).trigger(source)
		else:
			if Config.LOGINFO:
				print("no minion is in the deck"%())
class CS3_024:# <12> 1637 #OK
	""" Taelan Fordring
	[[Taunt], Divine Shield][Deathrattle:] Draw your highest Cost minion. """
	deathrattle = GiveHighestCostMinion(CONTROLLER)
	pass




if Overlord_Runthak:
	Core_Neutral+=['CS3_025','CS3_025e']
class CS3_025:# <12> 1637 #OK
	""" Overlord Runthak
	[Rush]. Whenever this attacks, give +1/+1 to all minions in your hand. """
	events = Attack(SELF).on(Buff(FRIENDLY_HAND + MINION,'CS3_025e'))
	pass
CS3_025e=buff(atk=1,health=1)# <12> 1637
""" Rallying Cry
	+1/+1. """




if Alexstrasza_the_Life_Binder:
	Core_Neutral+=['CS3_031']
class CS3_031_Action(TargetedAction):
	def do(self,source,target):
		if target.controller==source.controller:
			Heal(target,8).trigger(source.controller)
		elif target.controller==source.controller.opponent:
			Hit(target,8).trigger(source.controller)
class CS3_031:# <12> 1637 #OK
	""" Alexstrasza the Life-Binder
	[Battlecry]: Choose a character. If it's friendly,restore 8 Health. 
	If it's an___enemy, deal 8 damage. """
	requirements = {PlayReq.REQ_HERO_OR_MINION_TARGET:0, PlayReq.REQ_TARGET_TO_PLAY:0}
	play = CS3_031_Action(TARGET)
	pass




if Onyxia_the_Broodmother:
	Core_Neutral+=['CS3_032','EX1_116t']
class CS3_032:# <12> 1637 #OK
	""" Onyxia the Broodmother
	At the end of each turn, fill_your board with 1/1_Whelps. """
	events = OWN_TURN_END.on(Summon(CONTROLLER,'EX1_116t') * 8)
	pass
class EX1_116t:# <12> 3
	""" Whelp """




if Ysera_the_Dreamer:
	Core_Neutral+=['CS3_033']
class CS3_033:# <12> 1637 #OK
	""" Ysera the Dreamer
	[Battlecry:] Add one of each Dream card to your hand. """
	play = Give(CONTROLLER,"DREAM_01"),\
		Give(CONTROLLER,"DREAM_02"),\
		Give(CONTROLLER,"DREAM_03"),\
		Give(CONTROLLER,"DREAM_04"),\
		Give(CONTROLLER,"DREAM_05")
	pass




if Malygos_the_Spellweaver:### OK ###
	Core_Neutral+=['CS3_034']
class CS3_034_Action(TargetedAction):
	PLAYER=ActionArg()
	def do(self, source, player):
		controller=player
		amount = 10-len(controller.hand)
		for repeat in range(amount):
			cards = [card for card in controller.deck if card.type==CardType.SPELL]
			if len(cards):
				if Config.LOGINFO:
					Config.log("CS3_034_Action.do","moves a spell card to hand.")
				card = random.choice(cards)
				card.zone=Zone.HAND
			else:
				if Config.LOGINFO:
					Config.log("CS3_034_Action.do","No spell card in the deck.")
				return
class CS3_034:# <12> 1637 #OK
	""" Malygos the Spellweaver
	[Battlecry:] Draw spells until your hand is full. """
	play = CS3_034_Action(CONTROLLER)
	pass




if Nozdormu_the_Eternal:
	Core_Neutral+=['CS3_035','CS3_035e']
class CS3_035:# <12> 1637 #OK
	""" Nozdormu the Eternal
	[Start of Game:] If this is in BOTH players' decks, turns_are only 15 seconds long. """
	#lol, no implementation
	pass
class CS3_035e:# <12> 1637 #OK
	""" Nozdormu Time
	Turns are 15 seconds long. """
	#
	pass




if Deathwing_the_Destroyer:
	Core_Neutral+=['CS3_036']
class CS3_036:# <12> 1637 #OK
	""" Deathwing the Destroyer
	[Battlecry:] Destroy all other minions. Discard a card for each destroyed. """
	play = Discard(RANDOM(FRIENDLY_HAND)) * Count(ALL_MINIONS - SELF), Destroy(ALL_MINIONS - SELF)
	pass




if Emerald_Skytalon:
	Core_Neutral+=['CS3_037']
class CS3_037:# <12> 1637 #OK
	""" Emerald Skytalon
	[Rush] """
	#
	pass




if Redgill_Razorjaw:
	Core_Neutral+=['CS3_038']
class CS3_038:# <12> 1637 #OK
	""" Redgill Razorjaw

	[Rush] """
	#
	pass

Core_Neutral+=['GAME_005']
class GAME_005:# <12> 1637 #OK
	""" The Coin
	Gain 1 Mana Crystal this turn only. """
	play = ManaThisTurn(CONTROLLER, 1)
	pass





