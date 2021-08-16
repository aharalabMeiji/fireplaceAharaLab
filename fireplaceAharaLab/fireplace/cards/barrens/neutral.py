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

class BAR_:
	"""
	Mankrik
	3
	3
	4
	Minion
	Legendary
	Battlecry
	"""
	#
	pass

class BAR_:
	"""
	Mor'shan Watch Post
	3
	3
	4
	Minion
	Rare
	-
	"""
	#
	pass

class BAR_:
	"""
	Ratchet Privateer
	3
	4
	3
	Minion - Pirate
	Common
	Battlecry
	"""
	#
	pass

class BAR_:
	"""
	Sunwell Initiate
	3
	3
	4
	Minion
	Common
	Divine Shield, Frenzy
	"""
	#
	pass

class BAR_:
	"""
	Venomous Scorpid
	3
	1
	3
	Minion - Beast
	Common
	Battlecry, Discover, Poisonous
	"""
	#
	pass

class BAR_:
	"""
	Blademaster Samuro
	4
	1
	6
	Minion
	Legendary
	Frenzy, Rush
	"""
	#
	pass

class BAR_:
	"""
	Crossroads Watch Post
	4
	4
	6
	Minion
	Epic
	-
	"""
	#
	pass

class BAR_:
	"""
	Darkspear Berserker
	4
	5
	7
	Minion
	Common
	Deathrattle
	"""
	#
	pass

class BAR_:
	"""
	Gruntled Patron
	4
	3
	3
	Minion
	Common
	Frenzy
	"""
	#
	pass

class BAR_:
	"""
	Injured Marauder
	4
	5
	10
	Minion
	Common
	Battlecry, Taunt
	"""
	#
	pass

class BAR_:
	"""
	Kazakus, Golem Shaper
	4
	3
	3
	Minion
	Legendary
	Battlecry
	"""
	#
	pass

class BAR_:
	"""
	Southsea Scoundrel
	4
	5
	5
	Minion - Pirate
	Epic
	Battlecry, Discover
	"""
	#
	pass

class BAR_:
	"""
	Spirit Healer
	4
	3
	6
	Minion
	Epic
	-
	"""
	#
	pass

class BAR_:
	"""
	Barrens Blacksmith
	5
	3
	5
	Minion
	Epic
	Frenzy
	"""
	#
	pass

class BAR_:
	"""
	Burning Blade Acolyte
	5
	1
	1
	Minion
	Rare
	Deathrattle, Taunt
	"""
	#
	pass

class BAR_:
	"""
	Gold Road Grunt
	5
	3
	7
	Minion
	Common
	Frenzy, Taunt
	"""
	#
	pass

class BAR_:
	"""
	Razormane Raider
	5
	5
	6
	Minion - Quilboar
	Common
	Frenzy
	"""
	#
	pass

class BAR_:
	"""
	Shadow Hunter Vol'jin
	5
	3
	6
	Minion
	Legendary
	Battlecry
	"""
	#
	pass

class BAR_:
	"""
	Taurajo Brave
	6
	4
	8
	Minion
	Rare
	Frenzy
	"""
	#
	pass

class BAR_:
	"""
	Kargal Battlescar
	7
	5
	5
	Minion
	Legendary
	Battlecry
	"""
	#
	pass

class BAR_:
	"""
	Mutanus the Devourer
	7
	4
	4
	Minion - Murloc
	Legendary
	Battlecry
	"""
	#
	pass

class BAR_:
	"""
	Selfless Sidekick
	7
	6
	6
	Minion
	Common
	Battlecry
	"""
	#
	pass

class BAR_:
	"""
	Primordial Protector
	8
	6
	6
	Minion - Elemental
	Epic
	Battlecry
	"""
	#
	pass


	