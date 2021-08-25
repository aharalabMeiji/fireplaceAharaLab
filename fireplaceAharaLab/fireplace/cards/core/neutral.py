class CORE_AT_092:# 12 1637
    """ Ice Rager
     """
    #
    pass

class CORE_BOT_083:# 12 1637
    """ Toxicologist
    [Battlecry:] Give your weapon +1 Attack. """
    #
    pass

class CORE_CS2_117:# 12 1637
    """ Earthen Ring Farseer
    [Battlecry:] Restore #3_Health. """
    requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
    play = Heal(TARGET, 3)
    pass

class CORE_CS2_120:# 12 1637
    """ River Crocolisk
     """
    #
    pass

class CORE_CS2_122:# 12 1637
    """ Raid Leader
    Your other minions have +1 Attack. """
    update = Refresh(FRIENDLY_MINIONS - SELF, buff="CS2_122e")
    pass
CS2_122e = buff(atk=1)

class CORE_CS2_142:# 12 1637
    """ Kobold Geomancer
    [Spell Damage +1] """
    #
    pass

class CORE_CS2_179:# 12 1637
    """ Sen'jin Shieldmasta
    [Taunt] """
    #
    pass

class CORE_CS2_181:# 12 1637
    """ Injured Blademaster
    [Battlecry:] Deal 4 damage to HIMSELF. """
    play = Hit(SELF, 4)
    pass

class CORE_CS2_182:# 12 1637
    """ Chillwind Yeti
     """
    #
    pass

class CORE_CS2_188:# 12 1637
    """ Abusive Sergeant
    [Battlecry:] Give a minion +2_Attack this turn. """
    requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
    play = Buff(TARGET, "CS2_188o")
    pass
CS2_188o = buff(atk=2)

class CORE_CS2_189:# 12 1637
    """ Elven Archer
    [Battlecry:] Deal 1 damage. """
    requirements = {PlayReq.REQ_NONSELF_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
    play = Hit(TARGET, 1)
    pass

class CORE_CS2_203:# 12 1637
    """ Ironbeak Owl
    [Battlecry:] [Silence] a_minion. """
    requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
    play = Silence(TARGET)
    pass

class CORE_CS2_222:# 12 1637
    """ Stormwind Champion
    Your other minions have +1/+1. """
    update = Refresh(FRIENDLY_MINIONS - SELF, buff="CS2_222o")
    pass
CS2_222o = buff(+1, +1)

class CORE_DAL_086:# 12 1637
    """ Sunreaver Spy
    [Battlecry:] If you control a [Secret], gain +1/+1. """
    play = Find(FRIENDLY_SECRETS) & Buff(SELF, "DAL_086e")
    pass
DAL_086e=buff(1,1)

class CORE_EX1_004:# 12 1637
    """ Young Priestess
    At the end of your turn, give another random friendly minion +1 Health. """
    events = OWN_TURN_END.on(Buff(RANDOM_OTHER_FRIENDLY_MINION, "EX1_004e"))
    pass
EX1_004e = buff(health=1)

class CORE_EX1_005:# 12 1637
    """ Big Game Hunter
    [Battlecry:] Destroy a minion with 7 or more Attack. """
    requirements = {
        PlayReq.REQ_MINION_TARGET: 0,
        PlayReq.REQ_TARGET_IF_AVAILABLE: 0,
        PlayReq.REQ_TARGET_MIN_ATTACK: 7}
    play = Destroy(TARGET)
    pass

class CORE_EX1_008:# 12 1637
    """ Argent Squire
    [Divine Shield] """
    #
    pass

class CORE_EX1_010:# 12 1637
    """ Worgen Infiltrator
    [Stealth] """
    #
    pass

class CORE_EX1_011:# 12 1637
    """ Voodoo Doctor
    [Battlecry:] Restore #2_Health. """
    requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
    play = Heal(TARGET, 2)
    pass

class CORE_EX1_012:# 12 1637
    """ Bloodmage Thalnos
    [Spell Damage +1][Deathrattle:] Draw a card. """
    deathrattle = Draw(CONTROLLER)
    pass

class CORE_EX1_014:# 12 1637
    """ King Mukla
    [Battlecry:] Give your opponent 2 Bananas. """
    play = Give(OPPONENT, "EX1_014t") * 2
    pass
class EX1_014t:
	"""Bananas"""
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "EX1_014te")
EX1_014te = buff(+1, +1)

class CORE_EX1_017:# 12 1637
    """ Jungle Panther
    [Stealth] """
    #
    pass

class CORE_EX1_028:# 12 1637
    """ Stranglethorn Tiger
    [Stealth] """
    #
    pass

class CORE_EX1_046:# 12 1637
    """ Dark Iron Dwarf
    [Battlecry:] Give a minion +2_Attack this turn. """
    requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
    play = Buff(TARGET, "EX1_046e")
    pass
EX1_046e = buff(atk=2)

class CORE_EX1_049:# 12 1637
    """ Youthful Brewmaster
    [Battlecry:] Return a friendly minion from the battlefield to your hand. """
    requirements = {
        PlayReq.REQ_FRIENDLY_TARGET: 0,
        PlayReq.REQ_MINION_TARGET: 0,
        PlayReq.REQ_NONSELF_TARGET: 0,
        PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
    play = Bounce(TARGET)
    pass

class CORE_EX1_059:# 12 1637
    """ Crazed Alchemist
    [Battlecry:] Swap the Attack and Health of a minion. """
    requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
    play = Buff(TARGET, "EX1_059e")
    pass
EX1_059e = AttackHealthSwapBuff()

class CORE_EX1_066:# 12 1637
    """ Acidic Swamp Ooze
    [Battlecry:] Destroy your opponent's weapon. """
    play = Destroy(ENEMY_WEAPON)
    pass

class CORE_EX1_082:# 12 1637
    """ Mad Bomber
    [Battlecry:] Deal 3 damage randomly split between all other characters. """
    play = Hit(RANDOM_OTHER_CHARACTER, 1) * 3
    pass

class CORE_EX1_093:# 12 1637
    """ Defender of Argus
    [Battlecry:] Give adjacent minions +1/+1 and [Taunt]. """
    play = Buff(SELF_ADJACENT, "EX1_093e")
    pass
EX1_093e = buff(+1, +1, taunt=True)

class CORE_EX1_095:# 12 1637
    """ Gadgetzan Auctioneer
    Whenever you cast a spell, draw a card. """
    events = OWN_SPELL_PLAY.on(Draw(CONTROLLER))
    pass

class CORE_EX1_096:# 12 1637
    """ Loot Hoarder
    [Deathrattle:] Draw a card. """
    deathrattle = Draw(CONTROLLER)
    pass

class CORE_EX1_103:# 12 1637
    """ Coldlight Seer
    [Battlecry:] Give your other Murlocs +2 Health. """
    play = Buff(FRIENDLY_MINIONS + MURLOC - SELF, "EX1_103e")
    pass
EX1_103e = buff(health=2)

class CORE_EX1_110:# 12 1637
    """ Cairne Bloodhoof
    [Deathrattle:] Summon a 5/5 Baine Bloodhoof. """
    deathrattle = Summon(CONTROLLER, "EX1_110t")
    pass
class EX1_110t:
    """  """

class CORE_EX1_162:# 12 1637
    """ Dire Wolf Alpha
    Adjacent minions have +1_Attack. """
    update = Refresh(SELF_ADJACENT, buff="EX1_162o")
    pass
EX1_162o = buff(atk=1)

class CORE_EX1_186:# 12 1637
    """ SI:7 Infiltrator
    [Battlecry:] Destroy a random enemy [Secret]. """
    #
    pass

class CORE_EX1_187:# 12 1637
    """ Arcane Devourer
    Whenever you cast a spell, gain +2/+2. """
    #
    pass

class CORE_EX1_188:# 12 1637
    """ Barrens Stablehand
    [Battlecry:] Summon a random Beast. """
    #
    pass

class CORE_EX1_189:# 12 1637
    """ Brightwing
    [Battlecry:] Add a random [Legendary] minion to your_hand. """
    #
    pass

class CORE_EX1_190:# 12 1637
    """ High Inquisitor Whitemane
    [Battlecry:] Summon all friendly minions that died_this turn. """
    #
    pass

class CORE_EX1_249:# 12 1637
    """ Baron Geddon
    At the end of your turn, deal 2 damage to ALL other characters. """
    events = OWN_TURN_END.on(Hit(ALL_CHARACTERS - SELF, 2))
    pass

class CORE_EX1_399:# 12 1637
    """ Gurubashi Berserker
    Whenever this minion takes damage, gain +3_Attack. """
    events = SELF_DAMAGE.on(Buff(SELF, "EX1_399e"))
    pass
EX1_399e = buff(atk=3)

class CORE_EX1_506:# 12 1637
    """ Murloc Tidehunter
    [Battlecry:] Summon a 1/1_Murloc Scout. """
    play = Summon(CONTROLLER, "EX1_506a")
    pass

class CORE_EX1_506a:# 12 1637
    """ Murloc Scout
     """
    #
    pass

class CORE_EX1_509:# 12 1637
    """ Murloc Tidecaller
    Whenever you summon a Murloc, gain +1 Attack. """
    events = Summon(ALL_PLAYERS, MURLOC).on(Buff(SELF, "EX1_509e"))
    pass
EX1_509e = buff(atk=1)

class CORE_EX1_564:# 12 1637
    """ Faceless Manipulator
    [Battlecry:] Choose a minion and become a copy of it. """
    requirements = {
        PlayReq.REQ_MINION_TARGET: 0,
        PlayReq.REQ_NONSELF_TARGET: 0,
        PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
    play = Morph(SELF, ExactCopy(TARGET))
    #
    pass

class CORE_FP1_007:# 12 1637
    """ Nerubian Egg
    [Deathrattle:] Summon a 4/4 Nerubian. """
    deathrattle = Summon(CONTROLLER, "FP1_007t")
    pass

class CORE_FP1_031:# 12 1637
    """ Baron Rivendare
    Your minions trigger their [Deathrattles] twice. """
    update = Refresh(CONTROLLER, {GameTag.EXTRA_DEATHRATTLES: True})
    pass

class CORE_GVG_013:# 12 1637
    """ Cogmaster
    Has +2 Attack while you have a Mech. """
    update = Find(FRIENDLY_MINIONS + MECH) & Refresh(SELF, {GameTag.ATK: +2})
    pass

class CORE_GVG_044:# 12 1637
    """ Spider Tank
     """
    #
    pass

class CORE_GVG_076:# 12 1637
    """ Explosive Sheep
    [Deathrattle:] Deal 2 damage to all minions. """
    deathrattle = Hit(ALL_MINIONS, 2)
    pass

class CORE_GVG_085:# 12 1637
    """ Annoy-o-Tron
    [Taunt][Divine Shield] """
    #
    pass

class CORE_GVG_109:# 12 1637
    """ Mini-Mage
    [Stealth][Spell Damage +1] """
    #
    pass

class CORE_GVG_121:# 12 1637
    """ Clockwork Giant
    Costs (1) less for each card in your opponent's hand. """
    cost_mod = -Count(ENEMY_HAND)
    pass

class CORE_ICC_026:# 12 1637
    """ Grim Necromancer
    [Battlecry:] Summon two 1/1 Skeletons. """
    #
    pass

class CORE_KAR_036:# 12 1637
    """ Arcane Anomaly
    After you cast a spell, give this minion +1 Health. """
    events = OWN_SPELL_PLAY.on(Buff(SELF, "KAR_036e"))
    pass
KAR_036e = buff(health=1)

class CORE_LOEA10_3:# 12 1637
    """ Murloc Tinyfin
     """
    #
    pass

class CORE_NEW1_018:# 12 1637
    """ Bloodsail Raider
    [Battlecry:] Gain Attack equal to the Attackof your weapon. """
    play = Find(FRIENDLY_WEAPON) & Buff(SELF, "NEW1_018e", atk=ATK(FRIENDLY_WEAPON))
    pass

class CORE_NEW1_026:# 12 1637
    """ Violet Teacher
    Whenever you cast a spell, summon a 1/1 Violet Apprentice. """
    events = OWN_SPELL_PLAY.on(Summon(CONTROLLER, "NEW1_026t"))
    pass

class CORE_NEW1_027:# 12 1637
    """ Southsea Captain
    Your other Pirates have +1/+1. """
    update = Refresh(FRIENDLY_MINIONS + PIRATE - SELF, buff="NEW1_027e")
    pass
NEW1_027e = buff(+1, +1)

class CORE_tt_004:# 12 1637
    """ Flesheating Ghoul
    Whenever a minion dies, gain +1 Attack. """
    #
    pass

class CORE_UNG_813:# 12 1637
    """ Stormwatcher
    [Windfury] """
    #
    pass

class CORE_UNG_844:# 12 1637
    """ Humongous Razorleaf
    Can't attack. """
    #
    pass

class CS3_022:# 12 1637
    """ Fogsail Freebooter
    [Battlecry:] If you have a weapon equipped, deal_2_damage. """
    #
    pass

class CS3_024:# 12 1637
    """ Taelan Fordring
    [[Taunt], Divine Shield][Deathrattle:] Draw yourhighest Cost minion. """
    #
    pass

class CS3_025:# 12 1637
    """ Overlord Runthak
    [Rush]. Whenever thisattacks, give +1/+1 to allminions in your hand. """
    #
    pass

class CS3_025e:# 12 1637
    """ Rallying Cry
    +1/+1. """
    #
    pass

class CS3_031:# 12 1637
    """ Alexstrasza the Life-Binder
    [Battlecry]: Choose acharacter. If it's friendly,restore 8 Health. If it's an___enemy, deal 8 damage. """
    #
    pass

class CS3_032:# 12 1637
    """ Onyxia the Broodmother
    At the end of each turn, fill_your board with 1/1_Whelps. """
    #
    pass

class CS3_033:# 12 1637
    """ Ysera the Dreamer
    [Battlecry:] Add one of each Dream card to your hand. """
    #
    pass

class CS3_034:# 12 1637
    """ Malygos the Spellweaver
    [Battlecry:] Draw spells until your hand is full. """
    #
    pass

class CS3_035:# 12 1637
    """ Nozdormu the Eternal
    [Start of Game:] If this is inBOTH players' decks, turns_are only 15 seconds long. """
    #
    pass

class CS3_035e:# 12 1637
    """ Nozdormu Time
    Turns are 15 seconds long. """
    #
    pass

class CS3_036:# 12 1637
    """ Deathwing the Destroyer
    [Battlecry:] Destroy all other minions. Discard a card for each destroyed. """
    #
    pass

class CS3_037:# 12 1637
    """ Emerald Skytalon
    [Rush] """
    #
    pass

class CS3_038:# 12 1637
    """ Redgill Razorjaw

    [Rush] """
    #
    pass

class GAME_005:# 12 1637
    """ The Coin
    Gain 1 Mana Crystal this turn only. """
    #
    pass

class Story_09_DireWolfAlphaPuzzle:# 12 1637
    """ Dire Wolf Alpha
    Adjacent minions have +1_Attack. """
    #
    pass

class Story_09_StormwatcherPuzzle:# 12 1637
    """ Stormwatcher
    [Windfury] """
    #
    pass