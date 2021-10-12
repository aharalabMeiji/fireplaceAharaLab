from ..utils import *

####### paladin in dragon  10 cards #######

class DRG_008:#OK
	"""Righteous Cause		1	-	-	Spell	Rare	-	Sidequest
	<b>Sidequest:</b> Summon 5 minions.
	<b>Reward:</b> Give your minions +1/+1."""
	#		<Tag enumID="1192" name="SIDEQUEST" type="Int" value="1"/>
	events = Play(CONTROLLER, MINION).on(SidequestCounter(SELF, 5, [Buff(FRIENDLY_MINIONS, "DRG_008e"), Destroy(SELF)]))
DRG_008e = buff(1,1)
class DRG_233:#OK
	"""Sand Breath		1	-	-	Spell	Common	-	Divine Shield
	[x]Give a minion +1/+2.
	Give it <b>Divine Shield</b> if
	you're holding a Dragon."""
	requirements = { PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0 }
	play = Buff(TARGET, "DRG_233e"), HOLDING_DRAGON & SetTag(TARGET, (GameTag.DIVINE_SHIELD, ))
DRG_233e =buff(1,2)
class DRG_258:#OK
	"""Sanctuary		2	-	-	Spell	Epic	-	Sidequest
	[x]<b>Sidequest:</b> Take no
	damage for a turn.
	<b>Reward:</b> Summon a 3/6
	minion with <b>Taunt</b>."""
	events = [ OWN_TURN_END.on(SidequestCounterClear(SELF)),
		   Attack(ENEMY,FRIENDLY).on(SidequestCounter(SELF,-1,None)),
		   OWN_TURN_BEGIN.on(SidequestCounterEq(SELF,0, [Summon(CONTROLLER,"DRG_258t"), Destroy(SELF)]))
		]
class DRG_258t:
	""" Indomitable Champion
	""" 
class DRG_229:#OK
	"""Bronze Explorer		3	2	3	Minion	Common	Dragon	Battlecry
	<b>Lifesteal</b>
	<b>Battlecry:</b> <b>Discover</b> a Dragon."""
	play = Discover(CONTROLLER, RandomDragon())
class DRG_235:#OK
	"""Dragonrider Talritha		3	3	3	Minion	Legendary	-	Deathrattle
	<b>Deathrattle:</b> Give a Dragon in your hand +3/+3 and this <b>Deathrattle</b>."""
	deathrattle = Buff(RANDOM(FRIENDLY_HAND + DRAGON - SELF), "DRG_235e")
class DRG_235e:
	tags = {GameTag.DEATHRATTLE: True}
	atk = lambda self,i: i+3
	max_health = lambda self,i:i+3
	deathrattle = Buff(RANDOM(FRIENDLY_HAND + DRAGON - SELF), "DRG_235e")
class DRG_225:#OK
	"""Sky Claw		3	1	2	Minion	Rare	Mech	Battlecry
	Your other Mechs
	have +1 Attack.
	<b>Battlecry:</b> Summon two 1/1 Microcopters."""
	class Hand:
		update = Buff(FRIENDLY + MECH - SELF, "DRG_225e")
	play = Summon(CONTROLLER, "DRG_225t") * 2
DRG_225e = buff(1,0)
class DRG_232:########################  hard to check, maybe OK
	"""Lightforged Zealot		4	4	2	Minion	Rare	-	Battlecry
	<b>Battlecry:</b> If your deck has no Neutral cards, equip a __4/2_Truesilver_Champion._"""
	powered_up = -Find(FRIENDLY_DECK + EnumSelector(CardClass.NEUTRAL))
	play = powered_up & Summon(CONTROLLER, "DRG_232t")
class DRG_232t:
	""" Truesilver Champion 
	Whenever your hero attacks, restore #2_Health to it."""
	events = Attack(FRIENDLY_HERO, ENEMY_CHARACTERS).on(Heal(FRIENDLY_HERO,2))
class DRG_309:#OK
	"""Nozdormu the Timeless		4	8	8	Minion	Legendary	Dragon	Battlecry
	<b>Battlecry:</b> Set each player to 10 Mana Crystals."""
	def play(self):
		controller = self.controller
		opponent = controller.opponent
		controller.max_mana = 10
		opponent.max_mana = 10
		pass
class DRG_226:#OK
	"""Amber Watcher		5	4	6	Minion	Common	Dragon	Battlecry
	<b>Battlecry:</b> Restore #8_Health."""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0}
	play = Heal(TARGET, 8)
class DRG_231:########################  hard to check, maybe OK
	"""Lightforged Crusader		7	7	7	Minion	Epic	-	Battlecry
	[x]<b>Battlecry:</b> If your deck has
	no Neutral cards, add 5
	random Paladin cards
	to your hand."""
	powered_up = -Find(FRIENDLY_DECK + EnumSelector(CardClass.NEUTRAL))
	play = powered_up & Give(CONTROLLER, RandomMinion(card_class=CardClass.PALADIN))*5

