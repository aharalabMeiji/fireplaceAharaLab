from ..utils import *

Core_Neutral=[]

Ice_Rager=True
Toxicologist=True
Earthen_Ring_Farseer=True
River_Crocolisk=True
Raid_Leader=True
Kobold_Geomancer=True
Sen_jin_Shieldmasta=True
Injured_Blademaster=True
Chillwind_Yeti=True
Abusive_Sergeant=True
Elven_Archer=True
Ironbeak_Owl=True
Stormwind_Champion=True
Sunreaver_Spy=True
Young_Priestess=True
Big_Game_Hunter=True
Argent_Squire=True
Worgen_Infiltrator=True
Voodoo_Doctor=True
Bloodmage_Thalnos=True
King_Mukla=True
Jungle_Panther=True


Fogsail_Freebooter=True
Taelan_Fordring=True
Overlord_Runthak=True
Alexstrasza_the_Life_Binder=True
Onyxia_the_Broodmother=True
Ysera_the_Dreamer=True
Malygos_the_Spellweaver=True
Nozdormu_the_Eternal=True
Deathwing_the_Destroyer=True
Emerald_Skytalon=True
Redgill_Razorjaw=True


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
	update = BuffOnce(FRIENDLY_MINIONS - SELF, "CS2_122e")
	pass
CS2_122e = buff(atk=1)# <12> 1635



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
class CORE_EX1_004:# <12> 1637 
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



#############################################
if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_028:# <12> 1637 #OK
	""" Stranglethorn Tiger
	[Stealth] """
	#
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_046:# <12> 1637
	""" Dark Iron Dwarf
	[Battlecry:] Give a minion +2_Attack this turn. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0, 
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Buff(TARGET, "EX1_046e")#with one turn effect
	pass
EX1_046e = buff(atk=2)# <12> 3 #OK




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_049:# <12> 1637 #OK
	""" Youthful Brewmaster
	[Battlecry:] Return a friendly minion from the battlefield to your hand. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_NONSELF_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Bounce(TARGET)
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_059:# <12> 1637  #OK
	""" Crazed Alchemist
	[Battlecry:] Swap the Attack and Health of a minion. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Buff(TARGET, "EX1_059e")
	pass
EX1_059e = AttackHealthSwapBuff()# <12> 3




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_066:# <12> 1637 #OK
	""" Acidic Swamp Ooze
	[Battlecry:] Destroy your opponent's weapon. """
	play = Destroy(ENEMY_WEAPON)
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_082:# <12> 1637 #OK
	""" Mad Bomber
	[Battlecry:] Deal 3 damage randomly split between all other characters. """
	play = Hit(RANDOM_OTHER_CHARACTER, 1) * 3
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_093:# <12> 1637 #OK
	""" Defender of Argus
	[Battlecry:] Give adjacent minions +1/+1 and [Taunt]. """
	play = Buff(SELF_ADJACENT, "EX1_093e")
	pass
EX1_093e = buff(+1, +1, taunt=True)# <12> 3




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_095:# <12> 1637 #OK
	""" Gadgetzan Auctioneer
	Whenever you cast a spell, draw a card. """
	events = OWN_SPELL_PLAY.on(Draw(CONTROLLER))
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_096:# <12> 1637 #OK
	""" Loot Hoarder
	[Deathrattle:] Draw a card. """
	deathrattle = Draw(CONTROLLER)
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_103:# <12> 1637 #OK
	""" Coldlight Seer
	[Battlecry:] Give your other Murlocs +2 Health. """
	play = Buff(FRIENDLY_MINIONS + MURLOC - SELF, "EX1_103e")
	pass
EX1_103e = buff(health=2)# <12> 3




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_110:# <12> 1637 #OK
	""" Cairne Bloodhoof
	[Deathrattle:] Summon a 5/5 Baine Bloodhoof. """
	deathrattle = Summon(CONTROLLER, "EX1_110t")
	pass
class EX1_110t:# <12> 3
	"""  """




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_162:# <12> 1637
	""" Dire Wolf Alpha
	Adjacent minions have +1_Attack. """
	update = Refresh(SELF_ADJACENT, buff="EX1_162o")
	pass
EX1_162o = buff(atk=1)# <12> 3




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_186:# <12> 1637
	""" SI:7 Infiltrator
	[Battlecry:] Destroy a random enemy [Secret]. """
	play = Destroy(RANDOM(ENEMY_SECRETS))
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_187:# <12> 1637
	""" Arcane Devourer
	Whenever you cast a spell, gain +2/+2. """
	events = OWN_SPELL_PLAY.on(Buff(SELF,'EX1_187e'))
	pass
EX1_187e=buff(atk=2,health=2)# <12> 3




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_188:# <12> 1637
	""" Barrens Stablehand
	[Battlecry:] Summon a random Beast. """
	play = Summon(CONTROLLER, RANDOM(BEAST))
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_189:# <12> 1637
	""" Brightwing
	[Battlecry:] Add a random [Legendary] minion to your_hand. """
	#play = Give(CONTROLLER,RANDOM(FRIENDLY_DECK + MINION + LEGENDARY))
	play = Give(CONTROLLER,RandomMinion(rarity=Rarity.LEGENDARY))
	pass

class ResummonMinionDiedThisTurn(TargetedAction):
	TARGET = ActionArg()#controller
	def do(self, source, target):
		for _card in target.died_this_turn:
			Summon(target,_card).trigger(target)




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_190:# <12> 1637
	""" High Inquisitor Whitemane
	[Battlecry:] Summon all friendly minions that died this turn. """
	play = ResummonMinionDiedThisTurn(CONTROLLER)
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_249:# <12> 1637
	""" Baron Geddon
	At the end of your turn, deal 2 damage to ALL other characters. """
	events = OWN_TURN_END.on(Hit(ALL_CHARACTERS - SELF, 2))
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_399:# <12> 1637
	""" Gurubashi Berserker
	Whenever this minion takes damage, gain +3_Attack. """
	events = SELF_DAMAGE.on(Buff(SELF, "EX1_399e"))
	pass
EX1_399e = buff(atk=3)# <12> 1635




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_506:# <12> 1637
	""" Murloc Tidehunter
	[Battlecry:] Summon a 1/1_Murloc Scout. """
	play = Summon(CONTROLLER, "CORE_EX1_506a")
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_506a:# <12> 1637
	""" Murloc Scout
	 """
	#
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_509:# <12> 1637
	""" Murloc Tidecaller
	Whenever you summon a Murloc, gain +1 Attack. """
	events = Summon(ALL_PLAYERS, MURLOC).on(Buff(SELF, "EX1_509e"))
	pass
EX1_509e = buff(atk=1)# <12> 3




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_EX1_564:# <12> 1637
	""" Faceless Manipulator
	[Battlecry:] Choose a minion and become a copy of it. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_NONSELF_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Morph(SELF, ExactCopy(TARGET))
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_FP1_007:# <12> 1637
	""" Nerubian Egg
	[Deathrattle:] Summon a 4/4 Nerubian. """
	deathrattle = Summon(CONTROLLER, "FP1_007t")
	pass
class FP1_007t:# <12> 3
	""" Nerubian
	"""




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_FP1_031:# <12> 1637
	""" Baron Rivendare
	Your minions trigger their [Deathrattles] twice. """
	update = Refresh(CONTROLLER, {GameTag.EXTRA_DEATHRATTLES: True})
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_GVG_013:# <12> 1637
	""" Cogmaster
	Has +2 Attack while you have a Mech. """
	update = Find(FRIENDLY_MINIONS + MECH) & Refresh(SELF, {GameTag.ATK: +2})
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_GVG_044:# <12> 1637
	""" Spider Tank
	"""
	#
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_GVG_076:# <12> 1637
	""" Explosive Sheep
	[Deathrattle:] Deal 2 damage to all minions. """
	deathrattle = Hit(ALL_MINIONS, 2)
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_GVG_085:# <12> 1637
	""" Annoy-o-Tron
	[Taunt][Divine Shield] """
	#
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_GVG_109:# <12> 1637
	""" Mini-Mage
	[Stealth][Spell Damage +1] """
	#
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_GVG_121:# <12> 1637
	""" Clockwork Giant
	Costs (1) less for each card in your opponent's hand. """
	cost_mod = -Count(ENEMY_HAND)
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_ICC_026:# <12> 1637
	""" Grim Necromancer
	[Battlecry:] Summon two 1/1 Skeletons. """
	play = Summon(CONTROLLER, 'ICC_026t') * 2
	pass
class ICC_026t:# <12> 1001
	""" Skeleton """
	



if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_KAR_036:# <12> 1637
	""" Arcane Anomaly
	After you cast a spell, give this minion +1 Health. """
	events = OWN_SPELL_PLAY.on(Buff(SELF, "KAR_036e"))
	pass
KAR_036e = buff(health=1)# <12> 23




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_LOEA10_3:# <12> 1637
	""" Murloc Tinyfin
	"""
	#
	pass





if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_LOOT_124:###OK
	""" Lone Champion  
	<b>Battlecry:</b> If you control no other minions, gain <b>Taunt</b> and <b>Divine Shield</b>. """
	def play(self):
		controller = self.controller
		if len(controller.field)==1:
			self.taunt = True
			self.divine_shield = True
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_LOOT_125:###OK
	""" Stoneskin Basilisk
	<b>Divine Shield</b>  <b>Poisonous</b>"""
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_LOOT_137:###OK
	""" Sleepy Dragon
	<b>Taunt</b> """
	pass





if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_NEW1_018_Action(TargetedAction):
	def do(self,source,target):
		player = target
		weapon = player.weapon
		source.atk += weapon.atk

class CORE_NEW1_018:# <12> 1637 #OK
	""" Bloodsail Raider
	[Battlecry:] Gain Attack equal to the Attack of your weapon. """
	play = Find(FRIENDLY_WEAPON) & CORE_NEW1_018_Action(CONTROLLER)
	pass
class NEW1_018e:
	#=buff(atk=ATK(FRIENDLY_WEAPON)) # <12> 3 #
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_NEW1_026:# <12> 1637
	""" Violet Teacher
	Whenever you cast a spell, summon a 1/1 Violet Apprentice. """
	events = OWN_SPELL_PLAY.on(Summon(CONTROLLER, "NEW1_026t"))
	pass

class NEW1_026t:# <12> 3
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_NEW1_027:# <12> 1637
	""" Southsea Captain
	Your other Pirates have +1/+1. """
	update = Refresh(FRIENDLY_MINIONS + PIRATE - SELF, buff="NEW1_027e")
	pass
NEW1_027e = buff(+1, +1)




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_tt_004:# <12> 1637
	""" Flesheating Ghoul
	Whenever a minion dies, gain +1 Attack. """
	events = Death(MINION).on(Buff(SELF, "tt_004o"))
	pass
tt_004o=buff(atk=1)# <12> 3




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_UNG_813:# <12> 1637
	""" Stormwatcher
	[Windfury] """
	#
	pass




if Elven_Archer:
	Core_Neutral+=['CORE_CS2_189']
class CORE_UNG_844:# <12> 1637
	""" Humongous Razorleaf
	Can't attack. """
	#
	pass



############################
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
			log.info("Highest cost minion is %r (cost %d)"%(_card, _cost))
			Give(target,_card).trigger(source)
		else:
			log.info("no minion is in the deck"%())
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




if Malygos_the_Spellweaver:
	Core_Neutral+=['CS3_034']
class CS3_034:# <12> 1637 #OK
	""" Malygos the Spellweaver
	[Battlecry:] Draw spells until your hand is full. """
	play = Give(CONTROLLER,RANDOM(FRIENDLY_DECK + SPELL)) * 10
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

class GAME_005:# <12> 1637 #OK
	""" The Coin
	Gain 1 Mana Crystal this turn only. """
	play = ManaThisTurn(CONTROLLER, 1)
	pass





