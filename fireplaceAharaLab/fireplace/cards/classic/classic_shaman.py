from ..utils import *

Classic_Shaman=[]

Classic_Frost_Shock=True
Classic_Ancestral_Spirit=True
Classic_Windfury=True
Classic_Ancestral_Healing=True
Classic_Fire_Elemental=True
Classic_Rockbiter_Weapon=True
Classic_Bloodlust=True
Classic_Searing_Totem=True
Classic_Stoneclaw_Totem=True
Classic_Wrath_of_Air_Totem=True
Classic_Far_Sight=True
Classic_Lightning_Bolt=True
Classic_Lava_Burst=True
Classic_Dust_Devil=True
Classic_Totemic_Might=True
Classic_Earth_Shock=True
Classic_Hex=True
Classic_Stormforged_Axe=True
Classic_Feral_Spirit=True
Classic_Earth_Elemental=True
Classic_Forked_Lightning=True
Classic_Unbound_Elemental=True
Classic_Lightning_Storm=True
Classic_Flametongue_Totem=True
Classic_Doomhammer=True
Classic_Mana_Tide_Totem=True
Classic_Windspeaker=True
Classic_Spirit_Wolf=True
Classic_Totemic_Call=False ## HP
Classic_Healing_Totem=True
Classic_AlAkir_the_Windlord=True


if Classic_Frost_Shock:# ### OK ###
	Classic_Shaman+=['VAN_CS2_037']
class VAN_CS2_037:# <8>[1646]
	""" Frost Shock
	Deal $1 damage to an enemy character and [Freeze] it. """
	requirements = {PlayReq.REQ_ENEMY_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 1), Freeze(TARGET)
	pass

if Classic_Ancestral_Spirit:# checking
	Classic_Shaman+=['VAN_CS2_038','CS2_038e']
class VAN_CS2_038:# <8>[1646]
	""" Ancestral Spirit
	Choose a minion. When that minion is destroyed, return it to the battlefield. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "CS2_038e")
	pass
class CS2_038e:
	deathrattle = Summon(CONTROLLER, Copy(SELF))
	tags = {GameTag.DEATHRATTLE: True}

if Classic_Windfury:# ### OK ###
	Classic_Shaman+=['VAN_CS2_039']
class VAN_CS2_039:# <8>[1646]
	""" Windfury
	Give a minion [Windfury]. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = GiveWindfury(TARGET - WINDFURY)
	pass

if Classic_Ancestral_Healing:# ### OK ###
	Classic_Shaman+=['VAN_CS2_041','CS2_041e']
class VAN_CS2_041:# <8>[1646]
	""" Ancestral Healing
	Restore a minion to full Health and give it [Taunt]. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = FullHeal(TARGET), Buff(TARGET, "CS2_041e")
	pass
CS2_041e = buff(taunt=True)

if Classic_Fire_Elemental:# ### OK ###
	Classic_Shaman+=['VAN_CS2_042']
class VAN_CS2_042:# <8>[1646]
	""" Fire Elemental
	[Battlecry:] Deal 3 damage. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Hit(TARGET, 3)
	pass

if Classic_Rockbiter_Weapon:# ### OK ###
	Classic_Shaman+=['VAN_CS2_045','CS2_045e']
class VAN_CS2_045:# <8>[1646]
	""" Rockbiter Weapon
	Give a friendly character +3 Attack this turn. """
	requirements = {PlayReq.REQ_FRIENDLY_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "CS2_045e")
	pass
CS2_045e = buff(atk=3)#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>

if Classic_Bloodlust:# ### OK ###
	Classic_Shaman+=['VAN_CS2_046','CS2_046e']
class VAN_CS2_046:# <8>[1646]
	""" Bloodlust
	Give your minions +3_Attack this turn. """
	play = Buff(FRIENDLY_MINIONS, "CS2_046e")
	pass
CS2_046e = buff(atk=3)#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>

if Classic_Searing_Totem:# ### OK ###
	Classic_Shaman+=['VAN_CS2_050']
class VAN_CS2_050:# <8>[1646]
	""" Searing Totem
	 """
	#
	pass

if Classic_Stoneclaw_Totem:# ### OK ###
	Classic_Shaman+=['VAN_CS2_051']
class VAN_CS2_051:# <8>[1646]
	""" Stoneclaw Totem
	[Taunt] """
	#
	pass

if Classic_Wrath_of_Air_Totem:# ### OK ###
	Classic_Shaman+=['VAN_CS2_052']
class VAN_CS2_052:# <8>[1646]
	""" Wrath of Air Totem
	[Spell Damage +1] """
	#
	pass

if Classic_Far_Sight:# checking
	Classic_Shaman+=['VAN_CS2_053','CS2_053e']
class VAN_CS2_053_Action(GameAction):
	def do(self, source):
		card = Draw(source.controller).trigger(source)
		card=get00(card)
		Buff(card, 'CS2_053e').trigger(source)
		pass
class VAN_CS2_053:# <8>[1646]
	""" Far Sight
	Draw a card. That card costs (3) less. """
	play = VAN_CS2_053_Action()#Draw(CONTROLLER).then(Buff(Draw.CARD, "CS2_053e"))
	pass
CS2_053e = buff(cost=-3)

if Classic_Lightning_Bolt:# ### OK ###
	Classic_Shaman+=['VAN_EX1_238']
class VAN_EX1_238:# <8>[1646]
	""" Lightning Bolt
	Deal $3 damage. [Overload:] (1) """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 3)
	#<Tag enumID="215" name="OVERLOAD" type="Int" value="1"/>
	pass

if Classic_Lava_Burst:# ### OK ###
	Classic_Shaman+=['VAN_EX1_241']
class VAN_EX1_241:# <8>[1646]
	""" Lava Burst
	Deal $5 damage. [Overload:] (2) """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 5)
	pass

if Classic_Dust_Devil:# ### OK ###
	Classic_Shaman+=['VAN_EX1_243']
class VAN_EX1_243:# <8>[1646]
	""" Dust Devil
	[Windfury]. [Overload:] (2) """
	#
	pass

if Classic_Totemic_Might:# ### OK ###
	Classic_Shaman+=['VAN_EX1_244','EX1_244e']
class VAN_EX1_244:# <8>[1646]
	""" Totemic Might
	Give your Totems +2_Health. """
	play = Buff(FRIENDLY_MINIONS + TOTEM, "EX1_244e")
	pass
EX1_244e = buff(health=2)

if Classic_Earth_Shock:# ### OK ###
	Classic_Shaman+=['VAN_EX1_245']
class VAN_EX1_245:# <8>[1646] ##
	""" Earth Shock
	[Silence] a minion, then deal $1 damage to it. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Silence(TARGET), Hit(TARGET, 1)
	pass

if Classic_Hex:# ### OK ###
	Classic_Shaman+=['VAN_EX1_246','hexfrog']
class VAN_EX1_246:# <8>[1646]
	""" Hex
	Transform a minion into a 0/1 Frog with [Taunt]. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Morph(TARGET, "hexfrog")
	pass
class hexfrog:### OK ###
	""" Frog
	[Taunt] """

if Classic_Stormforged_Axe:# ### OK ###
	Classic_Shaman+=['VAN_EX1_247']
class VAN_EX1_247:# <8>[1646]
	""" Stormforged Axe
	[Overload:] (1) """
	#
	pass

if Classic_Feral_Spirit:# ### OK ###
	Classic_Shaman+=['VAN_EX1_248']
class VAN_EX1_248:# <8>[1646]
	""" Feral Spirit
	Summon two 2/3 Spirit Wolves with [Taunt]. [Overload:] (2) """
	requirements = {PlayReq.REQ_NUM_MINION_SLOTS: 1}
	play = Summon(CONTROLLER, "VAN_EX1_tk11") * 2
	pass

if Classic_Spirit_Wolf:# ### OK ###
	Classic_Shaman+=['VAN_EX1_tk11']
class VAN_EX1_tk11:# <8>[1646]
	""" Spirit Wolf
	[Taunt] """
	#
	pass

if Classic_Earth_Elemental:# ### OK ###
	Classic_Shaman+=['VAN_EX1_250']
class VAN_EX1_250:# <8>[1646]
	""" Earth Elemental
	[Taunt]. [[Overload]:] (3) """
	#
	pass

if Classic_Forked_Lightning:# checking
	Classic_Shaman+=['VAN_EX1_251']
class VAN_EX1_251_Action(GameAction):
	def do(self, source):
		cards=[card for card in source.controller.opponent.field if card.type==CardType.MINION]
		if len(cards):
			if len(cards)>2:
				cards=random.sample(cards, 2)
			for card in cards:
				Hit(card, 2).trigger(source)
		pass
class VAN_EX1_251:# <8>[1646]
	""" Forked Lightning
	Deal $2 damage to 2_random enemy minions. [Overload:] (2) """
	requirements = {PlayReq.REQ_MINIMUM_ENEMY_MINIONS: 1}
	play = VAN_EX1_251_Action()#Hit(RANDOM_ENEMY_MINION * 2, 2)
	pass

if Classic_Unbound_Elemental:# ### OK ###
	Classic_Shaman+=['VAN_EX1_258','EX1_258e']
class VAN_EX1_258:# <8>[1646]
	""" Unbound Elemental
	Whenever you play a card_with [Overload], gain_+1/+1. """
	events = Play(CONTROLLER, OVERLOAD).on(Buff(SELF, "EX1_258e"))
	pass
EX1_258e = buff(+1, +1)


if Classic_Lightning_Storm:# ### OK ###
	Classic_Shaman+=['VAN_EX1_259']
class VAN_EX1_259:# <8>[1646]
	""" Lightning Storm
	Deal $2-$3 damage to all enemy minions. [Overload:] (2) """
	play = Hit(ENEMY_MINIONS, RandomNumber(2, 3))
	pass

if Classic_Flametongue_Totem:# ### OK ###
	Classic_Shaman+=['VAN_EX1_565','EX1_565o']
class VAN_EX1_565:# <8>[1646]
	""" Flametongue Totem
	Adjacent minions have +2_Attack. """
	update = Refresh(SELF_ADJACENT, buff="EX1_565o")
	pass
EX1_565o = buff(atk=2)

if Classic_Doomhammer:# ### OK ###
	Classic_Shaman+=['VAN_EX1_567']
class VAN_EX1_567:# <8>[1646]
	""" Doomhammer
	[Windfury, Overload:] (2) """
	#
	pass

if Classic_Mana_Tide_Totem:# ### OK ###
	Classic_Shaman+=['VAN_EX1_575']
class VAN_EX1_575:# <8>[1646]
	""" Mana Tide Totem
	At the end of your turn, draw a card. """
	events = OWN_TURN_END.on(Draw(CONTROLLER))
	pass

if Classic_Windspeaker:# ### OK ###
	Classic_Shaman+=['VAN_EX1_587']
class VAN_EX1_587:# <8>[1646]
	""" Windspeaker
	[Battlecry:] Give a friendly minion [Windfury]. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = GiveWindfury(TARGET - WINDFURY)
	pass

if Classic_Totemic_Call:# 
	Classic_Shaman+=['VAN_HERO_02bp']
	Classic_Shaman+=['VAN_HERO_02bp2']
	Classic_Shaman+=['VAN_HERO_02e2']
class VAN_HERO_02bp:# <8>[1646]
	""" Totemic Call
	[Hero Power]Summon a random Totem. """
	#
	pass
class VAN_HERO_02bp2:# <8>[1646]
	""" Totemic Slam
	[Hero Power]Summon a Totem of your choice. """
	#
	pass
class VAN_HERO_02e2:# <8>[1646]
	""" Strength of Earth
	+1 Attack. """
	#
	pass

if Classic_Healing_Totem:# ### OK ###
	Classic_Shaman+=['VAN_NEW1_009']
class VAN_NEW1_009:# <8>[1646]
	""" Healing Totem
	At the end of your turn, restore #1 Health to all friendly minions. """
	events = OWN_TURN_END.on(Heal(FRIENDLY_MINIONS, 1))
	pass

if Classic_AlAkir_the_Windlord:# ### OK ###
	Classic_Shaman+=['VAN_NEW1_010']
class VAN_NEW1_010:# <8>[1646]
	""" Al'Akir the Windlord
	[Charge, Divine Shield, Taunt, Windfury] """
	#
	pass

