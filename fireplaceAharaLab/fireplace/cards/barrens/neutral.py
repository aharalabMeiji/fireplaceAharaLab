from ..utils import *

class BAR_854:#Perfait
	"""Kindling Elemental
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; The next  Elemental you play costs (1) less.
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

class BAR_074:#OK
	"""
	Far Watch Post

	[x]Can't attack. After your opponent draws a card, it ___costs (1) more &lt;i&gt;(up to 10)&lt;/i&gt;.__
	"""
	update = Refresh(SELF, {GameTag.CANT_ATTACK: True})
	events = Draw(OPPONENT).on(Buff(Draw.CARD,"BAR_074e"))
	pass

BAR_074e = buff(cost=1)
# Spotted!"""

class BAR_745:#OK
	"""
	Hecklefang Hyena
	&lt;b&gt;Battlecry:&lt;/b&gt; Deal 3 damage to your hero.
	"""
	play = Hit(FRIENDLY_HERO,3)
	pass

class BAR_062:#OK
	"""
	Lushwater Murcenary
	&lt;b&gt;Battlecry:&lt;/b&gt; If you control a Murloc, gain +1/+1.
	"""
	play = Find(FRIENDLY_MINIONS + MURLOC - SELF) & Buff(SELF, "BAR_062e")
	pass
BAR_062e = buff(atk=1,health=1)

class BAR_063:
	"""
	Lushwater Scout
	After you summon a Murloc, give it +1 Attack and &lt;b&gt;Rush&lt;/b&gt;.
	"""
	events = Summon(CONTROLLER,MURLOC).on(Buff(Summon.CARD,"BAR_063e"))
	pass
BAR_063e=buff(atk=1, rush=True)

class BAR_024:#OK
	"""
	Oasis Thrasher
	&lt;b&gt;Frenzy:&lt;/b&gt; Deal 3 damage to the enemy Hero.
	"""
	events = Damage(SELF).on(Frenzy(SELF,Hit(ENEMY_HERO,3)))
	pass

class BAR_022:#OK
	"""
	Peon
	[x]&lt;b&gt;Frenzy:&lt;/b&gt; Add a random spell from your class to your hand.
	"""
	events = Damage(SELF).on(Frenzy(SELF,Give(CONTROLLER,RandomSpell(card_class=FRIENDLY_CLASS))))
	pass

class BAR_064:#maybe OK
	"""
	Talented Arcanist
	&lt;b&gt;Battlecry:&lt;/b&gt; Your next spell_this turn has &lt;b&gt;Spell_Damage +2&lt;/b&gt;.
	"""
	play = Buff(CONTROLLER, "BAR_064e")
	events = [OWN_SPELL_PLAY.after( Destroy(FRIENDLY + ID("BAR_854e"))),TURN_END.on( Destroy(FRIENDLY + ID("BAR_854e")))]
	pass
class BAR_064e:
	update = Refresh(FRIENDLY_HAND + MINION, {GameTag.SPELLPOWER: 2})

class BAR_743:#確認不能
	"""
	[x]&lt;b&gt;Taunt&lt;/b&gt; &lt;b&gt;Battlecry:&lt;/b&gt; If you're holding a Nature spell, gain +2 Health.
	"""
	play = Find(FRIENDLY_HAND+SPELL+NATURE) & Heal(FRIENDLY_HERO,2)
	pass

class WC_035:#OK
	"""
	Archdruid Naralex
	[x]&lt;b&gt;Dormant&lt;/b&gt; for 2 turns. While &lt;b&gt;Dormant&lt;/b&gt;, 
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
	Your &lt;b&gt;Deathrattle&lt;/b&gt; cards cost (1) less.
	"""
	play = Buff(FRIENDLY_HAND+DEATHRATTLE,"BAR_082e")
	pass
BAR_082e=buff(cost=-1)

class BAR_890:
	"""
	Crossroads Gossiper
	After a friendly &lt;b&gt;Secret&lt;/b&gt; is revealed, gain +2/+2.
	"""
	events = Reveal(FRIENDLY_SECRETS).on(Buff(SELF, "BAR_890e"))
	pass
BAR_890e=buff(atk=2,health=2)

class BAR_026:
	"""
	Death's Head Cultist
	&lt;b&gt;Taunt&lt;/b&gt; &lt;b&gt;Deathrattle:&lt;/b&gt; Restore 4 Health to your hero.
	"""
	deathrattle = Heal(FRIENDLY_HERO,4)
	pass

class WC_027:
	"""
	Devouring Ectoplasm
	[x]&lt;b&gt;Deathrattle:&lt;/b&gt; Summon a 2/2 Adventurer with_a random bonus effect.
	"""
	deathrattle = WC_027_Devouring_Ectoplasm(CONTROLLER)
	pass

class BAR_060:
	"""
	Hog Rancher
	&lt;b&gt;Battlecry:&lt;/b&gt; Summon a 2/1 Hog with &lt;b&gt;Rush&lt;/b&gt;.
	"""
	play = Summon(CONTROLLER, "BAR_060t")
	pass
class BAR_060t:
	""" Hog """
	pass

class BAR_430:#OK
	"""
	Horde Operative
	&lt;b&gt;Battlecry:&lt;/b&gt; Copy your opponent's &lt;b&gt;Secrets&lt;/b&gt; and put them into play.
	"""
	play = Summon(CONTROLLER,Copy(ENEMY_SECRETS))
	pass

class BAR_721:
	"""
	Mankrik
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; Help Mankrik find his wife! She was last seen somewhere in your deck.
	"""
	#
	pass

class BAR_076:
	"""
	Mor'shan Watch Post
	[x]Can't attack. After your
opponent plays a minion,
_summon a 2/2 Grunt.
	"""
	#
	pass

class BAR_061:
	"""
	Ratchet Privateer
	&lt;b&gt;Battlecry:&lt;/b&gt; Give your weapon +1 Attack.
	"""
	#
	pass

class BAR_025:
	"""
	Sunwell Initiate
	&lt;b&gt;Frenzy:&lt;/b&gt; Gain &lt;b&gt;Divine Shield&lt;/b&gt;.
	"""
	#
	pass

class BAR_065:
	"""
	Venomous Scorpid
	&lt;b&gt;Poisonous&lt;/b&gt;
&lt;b&gt;Battlecry:&lt;/b&gt; &lt;b&gt;Discover&lt;/b&gt; a spell.
	"""
	#
	pass

class BAR_078:
	"""
	Blademaster Samuro
	[x]&lt;b&gt;Rush&lt;/b&gt;
&lt;b&gt;Frenzy:&lt;/b&gt; Deal damage equal
to this minion's Attack
_to all enemy minions.
	"""
	#
	pass

class BAR_075:
	"""
	Crossroads Watch Post
	[x]Can't attack. Whenever your
opponent casts a spell, give
your minions +1/+1.
	"""
	#
	pass

class BAR_027:
	"""
	Darkspear Berserker
	&lt;b&gt;Deathrattle:&lt;/b&gt; Deal 5 damage to your hero.
	"""
	#
	pass

class BAR_070:
	"""
	Gruntled Patron
	>&lt;b&gt;Frenzy:&lt;/b&gt; Summon another Gruntled Patron.
	"""
	#
	pass

class BAR_069:
	"""
	Injured Marauder
	&lt;b&gt;Taunt&lt;/b&gt;
&lt;b&gt;Battlecry:&lt;/b&gt; Deal 6 damage to this minion.
	"""
	#
	pass

class BAR_079:
	"""
	Kazakus, Golem Shaper
	&lt;b&gt;Battlecry:&lt;/b&gt; If your deck has no 4-Cost cards, build a custom Golem.
	"""
	#
	pass

class BAR_081:
	"""
	Southsea Scoundrel
	&lt;b&gt;Battlecry:&lt;/b&gt; &lt;b&gt;Discover&lt;/b&gt; a card in your opponent's deck. They draw theirs as well.
	"""
	#
	pass

class BAR_744:
	"""
	Spirit Healer
	After you cast a Holy spell, give a random friendly minion +2 Health.
	-
	"""
	#
	pass

class BAR_073:
	"""
	Barrens Blacksmith
	&lt;b&gt;Frenzy:&lt;/b&gt; Give your other minions +2/+2.
	"""
	#
	pass

class BAR_072:
	"""
	Burning Blade Acolyte
	&lt;b&gt;Deathrattle:&lt;/b&gt; Summon a 5/8 Demonspawn
with &lt;b&gt;Taunt&lt;/b&gt;.
	"""
	#
	pass

class BAR_021:
	"""
	Gold Road Grunt
	[x]&lt;b&gt;Taunt&lt;/b&gt;
&lt;b&gt;Frenzy:&lt;/b&gt; Gain Armor equal
to the damage taken.
	"""
	#
	pass

class BAR_020:
	"""
	Razormane Raider
	&lt;b&gt;Frenzy:&lt;/b&gt; Attack a
random enemy.
	"""
	#
	pass

class BAR_080:
	"""
	Shadow Hunter Vol'jin
	&lt;b&gt;Battlecry:&lt;/b&gt; Choose a minion. Swap it with a random one in its owner's hand.
	"""
	#
	pass

class BAR_071:
	"""
	Taurajo Brave
	&lt;b&gt;Frenzy:&lt;/b&gt; Destroy a random enemy minion.
	"""
	#
	pass

class BAR_077:
	"""
	Kargal Battlescar
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; Summon a
5/5 Lookout for each
Watch Post you've
__summoned this game.
	"""
	#
	pass

class WC_030:
	"""
	Mutanus the Devourer
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; Eat a minion in
your opponent's hand.
Gain its stats.
	"""
	#
	pass

class WC_029:
	"""
	Selfless Sidekick
	&lt;b&gt;Battlecry:&lt;/b&gt; Equip a random weapon from your deck.
	"""
	#
	pass

class BAR_042:
	"""
	Primordial Protector
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; Draw your
highest Cost spell.
Summon a random minion
with the same Cost.
	"""
	#
	pass


	