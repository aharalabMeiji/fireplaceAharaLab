from ..utils import *

##### paladin-shadows,,,10,,,,,


class DAL_141:#OK
	"""Desperate Measures,,1,-,-,Spell,Rare,-,Secret,Twinspell
	<b>Twinspell</b>
	Cast a random Paladin <b>Secret</b>."""
	play = Summon(CONTROLLER,RandomSpell(secret=True, card_class=CardClass.PALADIN)), Give(CONTROLLER, "DAL_141ts")
class DAL_141ts:
	play = Summon(CONTROLLER,RandomSpell(secret=True, card_class=CardClass.PALADIN))

class DAL_570:#OK
	"""Never Surrender!,,1,-,-,Spell,Common,-,Secret
	<b>Secret:</b> When your opponent casts a spell, give your minions +2_Health."""
	secret = Play(OPPONENT, SPELL).on(Reveal(SELF),Buff(FRIENDLY_MINIONS, "DAL_570e"))
DAL_570e = buff(0,2)
class DAL_568:#OK
	"""Lightforged Blessing,,2,-,-,Spell,Common,-,Lifesteal,Twinspell
	<b>Twinspell</b>
	Give a friendly minion <b>Lifesteal</b>."""
	requirements = {PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_TO_PLAY:0}
	play = SetTag(TARGET, (GameTag.LIFESTEAL,)), Give(CONTROLLER, "DAL_568ts")
class DAL_568ts:
	requirements = {PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_TARGET_TO_PLAY:0}
	play = SetTag(TARGET, (GameTag.LIFESTEAL,))

class DAL_571:#OK
	"""Mysterious Blade,,2,2,0,Weapon,Rare,-,Battlecry,Secret
	<b>Battlecry:</b> If you control a
	<b>Secret</b>, gain +1 Attack."""
	powered_up = Find(FRIENDLY + SECRET)
	play = powered_up & Buff(SELF,"DAL_571e")
DAL_571e = buff(atk=1)

class DAL_146:#OK
	"""Bronze Herald,,3,3,2,Minion,Common,Dragon,Deathrattle
	<b>Deathrattle:</b> Add two 4/4 Dragons to your hand."""
	deathrattle = Give(CONTROLLER, "DAL_146t")*2
class DAL_146t:
	""" Bronze Dragon"""
	pass

#LOWEST_COST = lambda sel: (
#	RANDOM(sel + (AttrValue(GameTag.COST) == OpAttr(sel, GameTag.COST, min)))
#)
class DAL_727:#OK
	"""Call to Adventure,,3,-,-,Spell,Rare,-,-
	Draw the lowest Cost minion from your deck. Give it +2/+2."""
	play = Give(CONTROLLER, RANDOM(FRIENDLY_DECK + (AttrValue(GameTag.COST) == OpAttr(FRIENDLY_DECK, GameTag.COST, min)))).then(Buff(Give.CARD  ,"DAL_727e"))
DAL_727e = buff(2,2)

class DAL_573:#baybe OK
	"""Commander Rhyssa,,3,4,3,Minion,Legendary,-,Secret
	Your <b>Secrets</b> trigger twice."""
	############## implemented in fireplace.card.Secret

class DAL_147:#OK
	"""Dragon Speaker,,5,3,5,Minion,Epic,-,Battlecry
	<b>Battlecry:</b> Give all Dragons in your hand +3/+3."""
	play = Buff(FRIENDLY_HAND + DRAGON, "DAL_147e")
DAL_147e = buff(3,3)

class DAL_731:#OK
	"""Duel!,,5,-,-,Spell,Epic,-,-
	Summon a minion from each player's deck.
	They fight!"""
	play = DAL731Duel(RANDOM(FRIENDLY_DECK+MINION), RANDOM(ENEMY_DECK+MINION))

class DAL_581:#OK
	"""Nozari,,10,4,12,Minion,Legendary,Dragon,Battlecry
	<b>Battlecry:</b> Restore both heroes to full Health."""
	play = FullHeal(FRIENDLY_HERO), FullHeal(ENEMY_HERO)
