from ..utils import *


class SW_023:
    """Provoke
    Tradeable Choose a friendly minion. Enemy minions attack it."""
    requirements = {PlayReq.REQ_MINION_TARGET: 0,
                    PlayReq.REQ_TARGET_TO_PLAY: 0, PlayReq.REQ_FRIENDLY_TARGET: 0}
    play =
    pass


class SCH_237:
    """Athletic Studies
    Discover a Rush minion. Your next one costs (1) less."""
    play = DISCOVER(RandomMinion(rush=True)).then(
        Buff(CONTROLLER, "SCH_237e")
    )
    pass


class SCH_237e:
    """Athletic Studies
        Your next [Rush] minion costs (1) less."""
    update = Refresh(IN_HAND + FRIENDLY + MINION +
                     RUSH, {GameTag.COST: -1})
    events = Play(CONTROLLER, RUSH).on(Destroy(SELF))
    pass


class CORE_EX1_410:
    """Shield Slam
    Deal 1 damage to a minion for each Armor you have."""
    requirements = {PlayReq.REQ_MINION_TARGET: 0,
                    PlayReq.REQ_TARGET_TO_PLAY: 0}
    play = Hit(TARGET, ARMOR(FRIENDLY_HERO))
    pass


class BT_124:
    """Corsair Cache
    Draw a weapon. Give it +1 Durability."""
    play = ForceDraw(RANDOM(FRIENDLY_DECK + WEAPON)).then(
        Buff(ForceDraw.TARGET, "BT_124e"))
    pass


BT_124e = buff(health=1)


class DMF_522:
    """Minefield
    Deal 5 damage randomly split among all minions."""
    play = Hit(RANDOM_MINION, 1) * 5
    pass


class BT_117:
    """Bladestorm
    Deal 1 damage to all minions. Repeat until one dies."""

    def play(self):
        before = ALL_MINIONS
        for i in range(30):
            if ALL_MINIONS == before:
                Hit(ALL_MINIONS, 1)
        pass
    pass


class SW_094:
    """Heavy Plate
    Tradeable Gain 8 Armor."""
    play = GainArmor(FRIENDLY_HERO, 8)
    pass


class BT_781:
    """Bulwark of Azzinoth
    Whenever your hero would take damage, this loses 1 Durability instead.
    """
    update = Refresh(FRIENDLY_HERO, {GameTag.HEAVILY_ARMORED: True})
    events = Attack(ALL_CHARACTERS, FRIENDLY_HERO).on(
        Buff(SELF, buff(health=-1)))
    # BuffじゃなくてHit??
    pass


class BAR_845:
    """Rancor
    Deal 2 damage to all minions. Gain 2 Armor for each destroyed."""
    # 生の苦悩、ケルスザード校長らへんが参考になりそうだがわからん
    pass


class BAR_844:
    """Outrider's Axe
    After your hero attacks and kills a minion, draw a card."""
    events = Attack(FRIENDLY_HERO, ALL_MINIONS).after(
        Dead(ALL_MINIONS + Attack.DEFENDER) & Draw(CONTROLLER))
    pass


class YOP_005:
    """Barricade
    Summon a 2/4 Guard with Taunt. If it's your only minion, summon another."""

    def play(self):
        Summon(CONTROLLER, "YOP_005t")
        if Count(ALL_MINIONS) == 1:
            Summon(CONTROLLER, "YOP_005t")
    pass


class YOP_005t:
    """Race Guard
    Taunt"""
    pass


class CORE_EX1_407:
    """Brawl
    Destroy all minions except one. (chosen randomly)"""
    requirements = {PlayReq.REQ_MINIMUM_TOTAL_MINIONS: 2}
    play = (
        Find(ALL_MINIONS + ALWAYS_WINS_BRAWLS) &
        Destroy(ALL_MINIONS - RANDOM(ALL_MINIONS + ALWAYS_WINS_BRAWLS)) |
        Destroy(ALL_MINIONS - RANDOM_MINION)
    )
    pass


class SW_021:
    """Cowardly Grunt
    Deathrattle: Summon a minion from your deck."""
    deathrattle = Summon(CONTROLLER, RANDOM(FRIENDLY_DECK+MINION))
    pass


class SCH_533:
    """Commencement
    Summon a minion from your deck. Give it Taunt and Divine Shield."""
    play = Summon(CONTROLLER, RANDOM(FRIENDLY_DECK+MINION)
                  ).then(SetTag(Summon.CARD, (GameTag.DIVINE_SHIELD, GameTag.TAUNT)))

    pass


class SW_024:
    """Lothar
    At the end of your turn, attack a random enemy minion. If it dies, gain +3/+3."""
    events = OWN_TURN_END.on(Attack(SELF, RANDOM_ENEMY_MINION).after(
        Dead(Attack.DEFENDER) & Buff(SELF, "SW_024e")))
    pass


SW_024e = buff(atk=3, health=3)


class SCH_337_Troublemaker:
    def do(self, source, target):
        Summon(CONTROLLER, "SCH_337t").then(Attack(Summon.CARD,RANDOM_ENEMY_CHARACTER)) * 2
        pass


class SCH_337:
    """Troublemaker
    At the end of your turn, summon two 3/3 Ruffians that attack random enemies."""
    events = OWN_TURN_END.on(SCH_337_Troublemaker)
    pass


class SW_068:
    """Mo'arg Forgefiend
    Taunt Deathrattle: Gain 8 Armor."""
    deathrattle = GainArmor(FRIENDLY_HERO, 8)
    pass


class SCH_621:
    """Rattlegore
    Deathrattle: Resummon this with -1/-1."""
    deathrattle = 
    #https://wiki.denfaminicogamer.jp/hearthstone/ラトルゴア_Rattlegore 
    # のメモに要注意
    pass
