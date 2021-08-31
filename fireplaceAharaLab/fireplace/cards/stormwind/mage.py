from ..utils import *



class SW_001:#<4>[1578]###########################################
    """ Celestial Ink Set
    After you spend 5 Mana on spells, reduce the cost of a spell in your hand by (5).Lose 1 Durability. """
    event = OWN_SPELL_PLAY.on(SidequestManaCounter(SELF,Play.CARD,5,[Buff(FRIENDLY_HAND + SPELL,'SW_001e'), Hit(SELF,1)]))
    pass
SW_001e = buff(cost=-5)#<12> [1578]
SW_001e2 = buff(cost=-5)#<12> [1578]

#class SW_059e:#<4>[1578]
#    """ Engineered
#    Cost reduced. """
#    #
#    pass

class SW_107:#<4>[1578]###OK
    """ Fire Sale
    [Tradeable]Deal $3 damage to all minions. """
    play = Hit(ENEMY_MINIONS,3)
    pass

class SW_108:#<4>[1578]###OK
    """ First Flame
    Deal $2 damage to a minion. Add a Second Flame to your hand. """
    requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0}
    play = Hit(TARGET,2), Give(CONTROLLER, 'SW_108t')
    pass

class SW_108t:#<4>[1578]###OK
    """ Second Flame
    Deal $2 damage to a minion. """
    requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0}
    play = Hit(TARGET, 2)
    pass

class SW_109:#<4>[1578]#####################
    """ Clumsy Courier
    [Battlecry:] Cast the highest Cost spell from your hand. """
    #play = Summon(HighestCostSpell)
    pass

class SW_110:#<4>[1578] ####
    """ Ignite
    Deal $@ damage. Shuffle an Ignite into your deck that deals one more damage. """
    reqirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0}
    #play = Hit(TARGET, 2), Shuffle(CONTROLLER,'SW_110').then(Buff(atk=1))
    
    pass

class SW_111:#<4>[1578] ####
    """ Sanctum Chandler
    After you cast a Fire spell, draw a spell. """
    events = Play(CONTROLLER, SPELL + FIRE).on(Give(CONTROLLER, RANDOM(FRIENDLY + SPELL)))
    pass

class SW_112:#<4>[1578] ###
    """ Prestor's Pyromancer
    [Battlecry:] Your next Fire spell has [SpellDamage +2]. """
    play = Buff(FRIENDLY_HAND + FIRE,'SW_112e')
    pass

class SW_112e:#<4>[1578]
    """ Burning Hot!
    Your next Fire spell has [Spell Damage +2]. """
    spellpower = lambda self, i : i + 2
    events = Play(CONTROLLER, SPELL + FIRE).on(Destroy(SELF))
    pass

class SW_112e2:#<4>[1578]
    """ Burning Hot!
    Your next Fire spell has [Spell Damage +2]. """
    #
    pass

class CountFireSpellThis3Turns(TargetedAction):
    TARGET = ActionArg()
    TARGETEDACTION = ActionArg()
    def do(self, source, target, targetedaction):
        pass

class SW_113:#<4>[1578]
    """ Grand Magus Antonidas
    [Battlecry:] If you've cast a Fire spell on each of your last three turns, cast 3 Fireballs at___random enemies.@ <i>(@/3)</i> """
    play = CountFireSpellThis3Turns(CONTROLLER).on(Play(CONTROLLER, 'CORE_CS2_029', RANDOM_ENEMY_CHARACTER))
    pass

class SidequestFireFrostArcane(TargetedAction):############
    TARGET = ActionArg()
    CARD = CardArg()
    TARGETEDACTION = ActionArg()
    def do(self,source,target,card,targetedaction):
        pass
class SW_450:#<4>[1578]#######################
    """ Sorcerer's Gambit
    [Questline:] Cast a Fire, Frost, and Arcane spell. [Reward: ]Draw a spell. """
    events = OWN_SPELL_PLAY.on(SidequestFireFrostArcane(CONTROLLER,Play.CARD,[Give(CONTROLLER,RANDOM(SPELL)), Summon(CONTROLLER,'SW_450t')]))
    pass

class SW_450t:#<4>[1578]
    """ Stall for Time
    [Questline:] Cast a Fire, Frost, and Arcane spell. [Reward:] [Discover] one. """
    events = OWN_SPELL_PLAY.on(SidequestFireFrostArcane(CONTROLLER,Play.CARD,[DISCOVER(RANDOM(SPELL)), Summon(CONTROLLER,'SW_450t2')]))
    pass

class SW_450t2:#<4>[1578]
    """ Reach the Portal Room
    [Questline:] Cast a Fire,Frost, and Arcane spell.[Reward:] ArcanistDawngrasp. """
    events = OWN_SPELL_PLAY.on(SidequestFireFrostArcane(CONTROLLER,Play.CARD,[Give( CONTROLLER,'SW_450t4')]))
    pass

class SW_450t4:#<4>[1578]######
    """ Arcanist Dawngrasp
    [Battlecry:] For the rest of the game, you have [Spell Damage +3]. """
    #play = EternalBuff(CONTROLLER,'SW_450t4e')
    pass

class SW_450t4e:#<4>[1578]
    """ Power of Dawngrasp
    [Spell Damage +3] """
    spellpower = +3
    pass

class SW_462:#<4>[1578]###OK
    """ Hot Streak
    Your next Fire spell this turn costs (2) less. """
    play = Buff(FRIENDLY_HAND + SPELL + FIRE, 'SW_462e')
    pass

class SW_462e:#<4>[1578] ####
    """ Hot Streak
    The next Fire spell you play costs (2) less. """
    cost = lambda self, i: max(i-2,0) 
    events = [
        Play(CONTROLLER, SPELL+FIRE).on(Destroy(SELF)),
        OWN_TURN_END.on(Destroy(SELF)),
        ]
    pass

