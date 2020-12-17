from ..utils import *

####### paladin in dragon  10 cards #######


class DRG_008:
	"""Righteous Cause		1	-	-	Spell	Rare	-	Sidequest
	&lt;b&gt;Sidequest:&lt;/b&gt; Summon 5 minions.
	&lt;b&gt;Reward:&lt;/b&gt; Give your minions +1/+1."""
	events = Play(CONTROLLER, FRIENDLY_HAND + MINION).on(SidequestCounter(SELF, 5, Buff(FRIENDLY_MINIONS, "DRG_008e")))
DRG_008e = buff(1,1)
class DRG_233:
	"""Sand Breath		1	-	-	Spell	Common	-	Divine Shield
	[x]Give a minion +1/+2.
	Give it &lt;b&gt;Divine Shield&lt;/b&gt; if
	you're holding a Dragon."""
	play = Buff(TARGET, "DRG_233e"), HOLDING_DRAGON & SetTag(TARGET, (GameTag.DIVINE_SHIELD, ))
DRG_233e =buff(1,2)
class DRG_258:################################################
	"""Sanctuary		2	-	-	Spell	Epic	-	Sidequest
	[x]&lt;b&gt;Sidequest:&lt;/b&gt; Take no
	damage for a turn.
	&lt;b&gt;Reward:&lt;/b&gt; Summon a 3/6
	minion with &lt;b&gt;Taunt&lt;/b&gt;."""
	events = [ OWN_TURN_END.on(SidequestCounterClear(SELF)),
		   Attack(ENEMY_CHARACTERS,FRIENDLY_MINIONS).SidequestCounter(SELF,100,None),
		   OWN_TURN_BEGIN.SidequestCounterEq(SELF,1,Summon(CONTROLLER,"DRG_258t"))
		]
class DRG_258t:
	""" Indomitable Champion
	""" 
class DRG_229:
	"""Bronze Explorer		3	2	3	Minion	Common	Dragon	Battlecry
	&lt;b&gt;Lifesteal&lt;/b&gt;
	&lt;b&gt;Battlecry:&lt;/b&gt; &lt;b&gt;Discover&lt;/b&gt; a Dragon."""
	play = Discover(CONTROLLER, DRAGON)
class DRG_235:
	"""Dragonrider Talritha		3	3	3	Minion	Legendary	-	Deathrattle
	&lt;b&gt;Deathrattle:&lt;/b&gt; Give a Dragon in your hand +3/+3 and this &lt;b&gt;Deathrattle&lt;/b&gt;."""
	deathrattle = Buff(RANDOM(FRIENDLY_HAND + DRAGON - SELF), "DRG_235e")
class DRG_235e:
	tags = {GameTag.DEATHRATTLE: True}
	atk = 3
	health = 3
	deathrattle = Buff(RANDOM(FRIENDLY_HAND + DRAGON - SELF), "DRG_235e")
class DRG_225:
	"""Sky Claw		3	1	2	Minion	Rare	Mech	Battlecry
	Your other Mechs
	have +1 Attack.
	&lt;b&gt;Battlecry:&lt;/b&gt; Summon two 1/1 Microcopters."""
	play = Buff(FRIENDLY_MINIONS + MECH - SELF, "DRG_225e"), Summon(CONTROLLER, "DRG_225t") * 2
class DRG_232:
	"""Lightforged Zealot		4	4	2	Minion	Rare	-	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; If your deck has no Neutral cards, equip a __4/2_Truesilver_Champion._"""
	powered_up = -Find(FRIENDLY_DECK + NEUTRAL)
	play = powered_up & Summon(CONTROLLER, "DRG_232t")
class DRG_232t:
	""" Truesilver Champion 
	Whenever your hero attacks, restore #2_Health to it."""
	events = Attack(FRIENDLY_HERO, ENEMY_CHARACTERS).on(Heal(FRIENDLY_HERO,2))
class DRG_309:
	"""Nozdormu the Timeless		4	8	8	Minion	Legendary	Dragon	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Set each player to 10 Mana Crystals."""
	def play(self):
		controller = self.controller
		oppoent = controller.opponent
		controller.max_mana = 10
		opponent.max_mana = 10
		pass
class DRG_226:
	"""Amber Watcher		5	4	6	Minion	Common	Dragon	Battlecry
	&lt;b&gt;Battlecry:&lt;/b&gt; Restore #8_Health."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0}
	play = Heal(TARGET, 8)
class DRG_:
	"""Lightforged Crusader		7	7	7	Minion	Epic	-	Battlecry
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; If your deck has
	no Neutral cards, add 5
	random Paladin cards
	to your hand."""
	powered_up = -Find(FRIENDLY_DECK + NEUTRAL)
	play = powered_up & Give(CONTROLLER, RandomMinion(card_class=CardClass.PALADIN))*5

