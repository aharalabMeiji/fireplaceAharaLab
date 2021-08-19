from ..utils import *

class BAR_854:#Perfait
	"""Kindling Elemental
	[x]<b>Battlecry:</b> The next  Elemental you play costs (1) less.
	"""
	play = Buff(CONTROLLER, "BAR_854e")
	events = Play(CONTROLLER,ELEMENTAL).on( Destroy(FRIENDLY + ID("BAR_854e")))
	pass

class BAR_854e:
	update = Refresh(FRIENDLY_HAND +ELEMENTAL, {GameTag.COST: -1})
	#+ EnumSelector(Race.ELEMENTAL)
	pass 

class WC_028:#OK
	"""
	Meeting Stone
	[x]At the end of your turn, add a 2/2 Adventurer with a random bonus effect to your hand.
	"""
	events = OWN_TURN_END.on(WC_028_Meeting_Stone(CONTROLLER))
	pass

class BAR_074:#OK　　up to 10 がまだ
	"""
	Far Watch Post

	[x]Can't attack. After your opponent draws a card, it ___costs (1) more <i>(up to 10)</i>.__
	"""
	update = Refresh(SELF, {GameTag.CANT_ATTACK: True})
	events = Draw(OPPONENT).on(Buff(Draw.CARD,"BAR_074e"))
	pass

BAR_074e = buff(cost=1)
# Spotted!"""

class BAR_745:#OK
	"""
	Hecklefang Hyena
	<b>Battlecry:</b> Deal 3 damage to your hero.
	"""
	play = Hit(FRIENDLY_HERO,3)
	pass

class BAR_062:#OK
	"""
	Lushwater Murcenary
	<b>Battlecry:</b> If you control a Murloc, gain +1/+1.
	"""
	play = Find(FRIENDLY_MINIONS + MURLOC - SELF) & Buff(SELF, "BAR_062e")
	pass
BAR_062e = buff(atk=1,health=1)

class BAR_063:#OK
	"""
	Lushwater Scout
	After you summon a Murloc, give it +1 Attack and <b>Rush</b>.
	"""
	events = Summon(CONTROLLER,MURLOC).on(Buff(Summon.CARD,"BAR_063e"))
	pass
BAR_063e=buff(atk=1, rush=True)

class BAR_024:#OK
	"""
	Oasis Thrasher
	<b>Frenzy:</b> Deal 3 damage to the enemy Hero.
	"""
	events = Damage(SELF).on(Frenzy(SELF,Hit(ENEMY_HERO,3)))
	pass

class BAR_022:#OK
	"""
	Peon
	[x]<b>Frenzy:</b> Add a random spell from your class to your hand.
	"""
	events = Damage(SELF).on(Frenzy(SELF,Give(CONTROLLER,RandomSpell(card_class=FRIENDLY_CLASS))))
	pass

class BAR_064:#maybe OK「一夜漬け」では効果を見られない。
	"""
	Talented Arcanist
	<b>Battlecry:</b> Your next spell_this turn has <b>Spell_Damage +2</b>.
	"""
	play = Buff(CONTROLLER, "BAR_064e")
	events = [ OWN_SPELL_PLAY.on( Destroy(FRIENDLY + ID("BAR_064e"))),
		   OWN_TURN_END.on( Destroy(FRIENDLY + ID("BAR_064e")))
		   ]
	pass
class BAR_064e:
	update = Refresh(FRIENDLY_HAND, {GameTag.SPELLPOWER: 2})
	#{GameTag.SPELLPOWER: 2})

class BAR_743:#OK 
	#******NATUREはドルイド、シャーマンの特性****たとえば自然学の予習(SCH_333)**
	"""
	[x]<b>Taunt</b> <b>Battlecry:</b> If you're holding a Nature spell, gain +2 Health.
	"""
	play = Find(FRIENDLY_HAND+SPELL+NATURE) & Buff(SELF,'BAR_743e')
	pass
BAR_743e=buff(health=2)

class WC_035:#OK
	"""
	Archdruid Naralex
	[x]<b>Dormant</b> for 2 turns. While <b>Dormant</b>, 
	add a Dream card to your hand __at the end of your turn.
	"""

	play = Buff(CONTROLLER,"WC_035e")
	dormant = 2
	awaken = Destroy(FRIENDLY + ID("WC_035e"))
	pass

class WC_035e:
	events = OWN_TURN_END.on(WC_035_Archdruid_Naralex(CONTROLLER))
	pass


class BAR_082:#OK
	"""
	Barrens Trapper
	Your <b>Deathrattle</b> cards cost (1) less.
	"""
	play = Buff(FRIENDLY_HAND+DEATHRATTLE,"BAR_082e")
	pass
BAR_082e=buff(cost=-1)

class BAR_890:#OK
	"""
	Crossroads Gossiper
	After a friendly <b>Secret</b> is revealed, gain +2/+2.
	"""
	events = Reveal(FRIENDLY_SECRETS).on(Buff(SELF, "BAR_890e"))
	pass
BAR_890e=buff(atk=2,health=2)

class BAR_026:#OK
	"""
	Death's Head Cultist
	<b>Taunt</b> <b>Deathrattle:</b> Restore 4 Health to your hero.
	"""
	deathrattle = Heal(FRIENDLY_HERO,4)
	pass

class WC_027:#OK
	"""
	Devouring Ectoplasm
	[x]<b>Deathrattle:</b> Summon a 2/2 Adventurer with_a random bonus effect.
	"""
	deathrattle = WC_027_Devouring_Ectoplasm(CONTROLLER)
	pass

class BAR_060:#OK
	"""
	Hog Rancher
	<b>Battlecry:</b> Summon a 2/1 Hog with <b>Rush</b>.
	"""
	play = Summon(CONTROLLER, "BAR_060t")
	pass
class BAR_060t:
	""" Hog """
	pass

class BAR_430:#OK
	"""
	Horde Operative
	<b>Battlecry:</b> Copy your opponent's <b>Secrets</b> and put them into play.
	"""
	play = Summon(CONTROLLER,Copy(ENEMY_SECRETS))
	pass

class BAR_721:#OK
	"""
	Mankrik
	[x]<b>Battlecry:</b> Help Mankrik find his wife! She was last seen somewhere in your deck.
	"""
	play = Give(CONTROLLER,"BAR_721t"),
	pass
class BAR_721t:#OK
	"""Olgra, Mankrik's Wife
	[x]<b>Casts When Drawn</b>	Summon a 3/7 Mankrik,		who immediately attacks		the enemy hero.
		<Tag enumID="1077" name="CASTSWHENDRAWN" type="Int" value="1"/>
	"""
	play = Summon(CONTROLLER,'BAR_721t2'),Attack(FRIENDLY_MINIONS+ID('BAR_721t2'),ENEMY_HERO)
	pass
class BAR_721t2:
	"""Mankrik, Consumed by Hatred
	vanilla
	"""
	pass

class BAR_076:#OK
	"""
	Mor'shan Watch Post
	[x]Can't attack. After your opponent plays a minion, _summon a 2/2 Grunt.
<Tag enumID="227" name="CANT_ATTACK" type="Int" value="1"/>
	"""
	events = Play(OPPONENT,MINION).on(Summon(CONTROLLER,"BAR_076t"))
	pass
class BAR_076t:
	"""Watchful Grunt
	vanilla
	"""
	pass

class BAR_061:#OK
	"""
	Ratchet Privateer
	<b>Battlecry:</b> Give your weapon +1 Attack.
	"""
	play = Find(FRIENDLY_WEAPON) & Buff(FRIENDLY_WEAPON, "BAR_061e")
	pass
BAR_061e=buff(atk=1)

class BAR_025:#OK
	"""
	Sunwell Initiate
	<b>Frenzy:</b> Gain <b>Divine Shield</b>.
	"""
	events = SELF_DAMAGE.on(Frenzy(SELF,SetTag(SELF, (GameTag.DIVINE_SHIELD,))))
	pass

class BAR_065:#OK
	"""
	Venomous Scorpid
	<b>Poisonous</b>
	<b>Battlecry:</b> <b>Discover</b> a spell.
	"""
	play = Discover(CONTROLLER, RandomSpell())
	pass

class BAR_078:#OK
	"""
	Blademaster Samuro
	[x]<b>Rush</b> <b>Frenzy:</b> Deal damage equal to this minion's Attack _to all enemy minions.
	"""
	events = SELF_DAMAGE.on(Frenzy(SELF,Hit(ENEMY_MINIONS,Attr(SELF, GameTag.ATK))))
	pass

class BAR_075:#OK (2回やれば2つつく。)
	"""
	Crossroads Watch Post
	[x]Can't attack. Whenever your opponent casts a spell, give your minions +1/+1.
<Tag enumID="227" name="CANT_ATTACK" type="Int" value="1"/>
	"""
	events = Play(OPPONENT,SPELL).on(Buff(FRIENDLY_MINIONS,"BAR_075e")) 
	pass
BAR_075e=buff(atk=1,health=1)

class BAR_027:#OK
	"""
	Darkspear Berserker
	<b>Deathrattle:</b> Deal 5 damage to your hero.
	"""
	deathrattle = Hit(FRIENDLY_HERO,5)
	pass

class BAR_070:#OK
	"""
	Gruntled Patron
	><b>Frenzy:</b> Summon another Gruntled Patron.
	"""
	events = SELF_DAMAGE.on(Frenzy(SELF,Summon(CONTROLLER,Copy(SELF))))
	pass

class BAR_069:#OK
	"""
	Injured Marauder
	<b>Taunt</b> <b>Battlecry:</b> Deal 6 damage to this minion.
	"""
	play = Hit(SELF,6)
	pass

class BAR_079:####################### possible but huge
	"""
	Kazakus, Golem Shaper
	<b>Battlecry:</b> If your deck has no 4-Cost cards, build a custom Golem.
	First, choose one of 'cost 1, cost 5, cost 10'
	Next, choose one of 'rush, taunt, divine shield, life steal,  stealth, poisonous'

	"""
	#self.firstChoice = ["BAR_079_m1","BAR_079_m2","BAR_079_m3"]# first choice
	#self.secondChoice = ["BAR_079t4","BAR_079t5","BAR_079t6","BAR_079t7","BAR_079t8","BAR_079t9"]# first choice
	entourage = ["BAR_079t10","BAR_079t11","BAR_079t14","BAR_079t13","BAR_079t15","BAR_079t12",
		"BAR_079t10b","BAR_079t11","BAR_079t14b","BAR_079t13b","BAR_079t15b","BAR_079t12b",
		"BAR_079t10c","BAR_079t11","BAR_079t14c","BAR_079t13c","BAR_079t15c","BAR_079t12c",]
	powered_up = -Find(FRIENDLY_DECK + (COST==4))
	play = powered_up & BAR_079_Kazakus_Golem_Shaper(CONTROLLER,["BAR_079_m1","BAR_079_m2","BAR_079_m3"])
	pass

class BAR_079_m1:
    """ Lesser Golem
    {0}
{1} """
    #
    pass

class BAR_079_m2:
    """ Greater Golem
    {0}
{1} """
    #
    pass

class BAR_079_m3:
    """ Superior Golem
    {0}
{1} """
    #
    pass

class BAR_079t4:
    """ Swifthistle
    <b>Rush</b> """
    #
    pass

class BAR_079t5:
    """ Earthroot
    <b>Taunt</b> """
    #
    pass

class BAR_079t6:
    """ Sungrass
    <b>Divine Shield</b> """
    #
    pass

class BAR_079t7:
    """ Liferoot
    <b>Lifesteal</b> """
    #
    pass

class BAR_079t8:
    """ Fadeleaf
    <b>Stealth</b> """
    #
    pass

class BAR_079t9:
    """ Grave Moss
    <b>Poisonous</b> """
    #
    pass

class BAR_079t10:
    """ Wildvine
    <b>Battlecry:</b> Give your other minions +1/+1. """
    play = Buff(FRIENDLY_MINIONS,"BAR_079t10e")
    pass
BAR_079t10e=buff(1,1)

class BAR_079t10b:
    """ Wildvine
    <b>Battlecry:</b> Give your other minions +2/+2. """
    play = Buff(FRIENDLY_MINIONS,"BAR_079t10be")
    pass
BAR_079t10be=buff(2,2)

class BAR_079t10c:
    """ Wildvine
    <b>Battlecry:</b> Give your other minions +4/+4. """
    play = Buff(FRIENDLY_MINIONS,"BAR_079t10ce")
    pass
BAR_079t10ce=buff(4,4)

class BAR_079t11:
    """ Gromsblood
    <b>Battlecry:</b> Summon a copy of this. """
    play = Summon(CONTROLLER, Copy(SELF))   
    pass

class BAR_079t12:
    """ Icecap
    <b>Battlecry:</b> <b>Freeze</b> a random enemy minion. """
    play = Freeze(RANDOM_ENEMY_MINION)
    pass

class BAR_079t12b:
    """ Icecap
    <b>Battlecry:</b> <b>Freeze</b> two random enemy minions. """
    play = Freeze(RANDOM_ENEMY_MINION)*2
    pass

class BAR_079t12c:
    """ Icecap
    <b>Battlecry:</b> <b>Freeze</b> all enemy minions. """
    play = Freeze(ENEMY_MINIONS)
    pass

class BAR_079t13:
    """ Firebloom
    <b>Battlecry:</b> Deal 3 damage to a random enemy minion. """
    play = Hit(CONTROLLER,RANDOM_ENEMY_MINION)
    pass

class BAR_079t13b:
    """ Firebloom
    <b>Battlecry:</b> Deal 3 damage to two random enemy minions. """
    play = Hit(CONTROLLER,RANDOM_ENEMY_MINION)*2
    pass

class BAR_079t13c:
    """ Firebloom
    <b>Battlecry:</b> Deal 3 damage to all enemy minions. """
    play = Hit(CONTROLLER,ENEMY_MINIONS)
    pass

class BAR_079t14:
    """ Mageroyal
    <b>Spell Damage +1</b>. """
    #
    pass

class BAR_079t14b:
    """ Mageroyal
    <b>Spell Damage +2</b>. """
    #
    pass

class BAR_079t14c:
    """ Mageroyal
    <b>Spell Damage +4</b>. """
    #
    pass

class BAR_079t15:
    """ Kingsblood
    <b>Battlecry:</b> Draw a card. """
    play = Draw(CONTROLLER)
    pass

class BAR_079t15b:
    """ Kingsblood
    <b>Battlecry:</b> Draw 2 cards. """
    play = Draw(CONTROLLER)*2
    pass

class BAR_079t15c:
    """ Kingsblood
    <b>Battlecry:</b> Draw 4 cards. """
    play = Draw(CONTROLLER)*4
    pass

class BAR_081:#OK
	"""
	Southsea Scoundrel
	<b>Battlecry:</b> <b>Discover</b> a card in your opponent's deck. They draw theirs as well.
	"""
	play = BAR_081_Southsea_Scoundrel(CONTROLLER,RANDOM(ENEMY_DECK)*3)
	pass

class BAR_744:#OK
	"""
	Spirit Healer
	After you cast a Holy spell, give a random friendly minion +2 Health.
	-
	"""
	events = Play(CONTROLLER, SPELL+HOLY).on(Buff(RANDOM_FRIENDLY_MINION,"BAR_744e"))
	pass
BAR_744e=buff(health=2)

class BAR_073:#OK
	"""
	Barrens Blacksmith
	<b>Frenzy:</b> Give your other minions +2/+2.
	"""
	events = SELF_DAMAGE.on(Frenzy(SELF,Buff(FRIENDLY_MINIONS - SELF,"BAR_073e")))
	pass
BAR_073e=buff(atk=2,health=2)

class BAR_072:#OK
	"""
	Burning Blade Acolyte
	<b>Deathrattle:</b> Summon a 5/8 Demonspawn with <b>Taunt</b>.
	"""
	deathrattle = Summon(CONTROLLER, "BAR_072t")
	pass
class BAR_072t:
	""" Demonspawn
	"""
	pass

class BAR_021:#OK
	"""
	Gold Road Grunt
	[x]<b>Taunt</b> <b>Frenzy:</b> Gain Armor equal to the damage taken.
	"""
	events = Damage(SELF).on(Frenzy(SELF,GainArmor(FRIENDLY_HERO,Damage.AMOUNT)))
	pass

class BAR_020:#OK
	"""
	Razormane Raider
	<b>Frenzy:</b> Attack a random enemy.
	"""
	events = Damage(SELF).on(Frenzy(SELF,Attack(SELF,RANDOM_ENEMY_CHARACTER)))
	pass

class BAR_080:#OK
	"""
	Shadow Hunter Vol'jin
	<b>Battlecry:</b> Choose a minion. Swap it with a random one in its owner's hand.
	"""
	requirements = { PlayReq.REQ_MINION_TARGET: 0,	PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = SwapMinionAndHand(TARGET, RANDOM(FRIENDLY_HAND))
	pass

class BAR_071:#OK
	"""
	Taurajo Brave
	<b>Frenzy:</b> Destroy a random enemy minion.
	"""
	events = Damage(SELF).on(Frenzy(SELF,Destroy(RANDOM(ENEMY_MINIONS))))
	pass

class BAR_077:#OK
	"""
	Kargal Battlescar
	[x]<b>Battlecry:</b> Summon a 5/5 Lookout for each Watch Post you've __summoned this game.
	"""
	play = Summon(CONTROLLER,"BAR_077t") * CountSummon(SELF,["BAR_074","BAR_075","BAR_076"])
	pass
class BAR_077t:
	""" Lookout """

class WC_030:#OK
	"""
	Mutanus the Devourer
	[x]<b>Battlecry:</b> Eat a minion in your opponent's hand. Gain its stats.
	"""
	play = EatsCard(SELF, RANDOM(ENEMY_HAND + MINION))
	pass
WC_030e=buff()

class WC_029:#OK
	"""
	Selfless Sidekick
	<b>Battlecry:</b> Equip a random weapon from your deck.
	"""
	play = Summon(CONTROLLER, RANDOM(FRIENDLY_DECK+WEAPON))
	pass

class BAR_042:#OK
	"""
	Primordial Protector
	[x]<b>Battlecry:</b> Draw your highest Cost spell. Summon a random minion with the same Cost.
	"""
	play = BAR_042_Action(CONTROLLER) 
	pass

