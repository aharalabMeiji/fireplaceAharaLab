from ..utils import *

##### paladin-shadows,,,10,,,,,


class DAL_:
	"""Desperate Measures,,1,-,-,Spell,Rare,-,Secret,Twinspell
	&lt;b&gt;Twinspell&lt;/b&gt;
	Cast a random Paladin &lt;b&gt;Secret&lt;/b&gt;."""
	play = CastSpell(RANDOM(SECRET + PALADIN))
class DAL_570:
	"""Never Surrender!,,1,-,-,Spell,Common,-,Secret
	&lt;b&gt;Secret:&lt;/b&gt; When your opponent casts a spell, give your minions +2_Health."""
	secret = Play(OPPONENT, SPELL).on(Buff(FRIENDLY_MINIONS, "DAL_570e"))
DAL_570e = buff(0,2)
class DAL_568:
	"""Lightforged Blessing,,2,-,-,Spell,Common,-,Lifesteal,Twinspell
	&lt;b&gt;Twinspell&lt;/b&gt;
	Give a friendly minion &lt;b&gt;Lifesteal&lt;/b&gt;."""
	requirements = {PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_TO_PLAY:0}
	play = SetTag(TARGET, (GameTag.LIFESTEAL,)), Give(CONTROLLER, "DAL_568ts")
class DAL_568ts:
	requirements = {PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_TO_PLAY:0}
	play = SetTag(TARGET, (GameTag.LIFESTEAL,))

class DAL_571:
	"""Mysterious Blade,,2,2,0,Weapon,Rare,-,Battlecry,Secret
	&lt;b&gt;Battlecry:&lt;/b&gt; If you control a
	&lt;b&gt;Secret&lt;/b&gt;, gain +1 Attack."""
	powered_up = Find(FRIENDLY_CHARACTERS + SECRET)
	play = powered_up & Buff(SELF,"DAL_571e")
DAL_571e = buff(1,0)
class DAL_146:
	"""Bronze Herald,,3,3,2,Minion,Common,Dragon,Deathrattle
	&lt;b&gt;Deathrattle:&lt;/b&gt; Add two 4/4 Dragons to your hand."""
	deathrattle = Give(CONTROLLER, "DAL_146t")
class DAL_146t:
	""" Bronze Dragon"""
	pass

#LOWEST_COST = lambda sel: (
#	RANDOM(sel + (AttrValue(GameTag.COST) == OpAttr(sel, GameTag.COST, min)))
#)
class DAL_727:
	"""Call to Adventure,,3,-,-,Spell,Rare,-,-
	Draw the lowest Cost minion from your deck. Give it +2/+2."""
	play = ForceDraw(CONTROLLER, Buff( RANDOM(FRIENDLY_DECK + (AttrValue(GameTag.COST) == OpAttr(FRIENDLY_DECK, GameTag.COST, min))) ,"DAL_727e"))
DAL_727e = buff(2,2)

class DAL_573:################################
	"""Commander Rhyssa,,3,4,3,Minion,Legendary,-,Secret
	Your &lt;b&gt;Secrets&lt;/b&gt; trigger twice."""
	############## no such tag?

class DAL_147:
	"""Dragon Speaker,,5,3,5,Minion,Epic,-,Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Give all Dragons in your hand +3/+3."""
	play = Buff(FRIENDLY_HAND + DRAGON, "DAL_147e")
DAL_147e = buff(3,3)

class DAL_731:############################# how they fight?
	"""Duel!,,5,-,-,Spell,Epic,-,-
	Summon a minion from each player's deck.
	They fight!"""
	play = Summon(CONTROLLER,RANDOM(FRIENDLY_DECK+MINION)), Summon(OPPONENT,RANDOM(ENEMY_DECK+MINION))

class DAL_581:
	"""Nozari,,10,4,12,Minion,Legendary,Dragon,Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Restore both heroes to full Health."""
	play = FullHeal(FRIENDLY_HERO), FullHeal(ENEMY_HERO)
