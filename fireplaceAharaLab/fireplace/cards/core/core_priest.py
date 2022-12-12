from ..utils import *

from fireplace.card import Card


#########################################

Core_Priest=[]
Flash_Heal=True
Drakonid_Operative=True
Holy_Nova=True
Holy_Smite=True
Northshire_Cleric=True
Murozond_the_Infinite=True
Psychic_Conjurer=True
Power_Infusion=True
Kul_Tiran_Chaplain=True
Shadow_Word_Ruin=True
Shadow_Word_Death=True
Lightbomb=True
Radiant_Elemental=True
Lyra_the_Sunshard=True
Shadowed_Spirit=True
Holy_Affinity=True
Focused_Will=True
Focused_Will=True
Thrive_in_the_Shadows=True

##########################

if Flash_Heal:# 
	Core_Priest+=['CORE_AT_055']
class CORE_AT_055:# <6>[1637] ## 23.6 ## OK
	""" Flash Heal
	Restore #5 Health. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Heal(TARGET, 5)
	pass

if Drakonid_Operative:# 
	Core_Priest+=['CORE_CFM_605']
class CORE_CFM_605:# <6>[1637]## 23.6
	""" Drakonid Operative
	[Battlecry:] If you're holdinga Dragon, [Discover] a copy of a card in your opponent's deck. """
	def play(self):
		holding_dragon=False
		for card in self.controller.hand:##  hand
			if card != self and card.type==CardType.MINION and card.race==Race.DRAGON:
				holding_dragon=True
				break
		decklist = [i.id for i in self.controller.opponent.deck]
		if decklist and holding_dragon:
			DISCOVER(RandomID(*decklist)).trigger(self)
			#print(self.controller.choice.cards)

if Holy_Nova:# 
	Core_Priest+=['CORE_CS1_112']
class CORE_CS1_112:# <6>[1637]## 23.6 ## OK
	""" Holy Nova
	Deal $2 damage to all enemy minions. Restore #2 Health to all friendly characters. """
	play = Hit(ENEMY_MINIONS, 2), Heal(FRIENDLY_CHARACTERS, 2)
	pass

if Holy_Smite:# 
	Core_Priest+=['CORE_CS1_130']
class CORE_CS1_130:# <6>[1637]## 23.6 ## OK
	""" Holy Smite
	Deal $3 damageto a minion. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 3)
	pass

if Northshire_Cleric:# 
	Core_Priest+=['CORE_CS2_235']
class CORE_CS2_235:# <6>[1637]## 23.6 ## visually OK
	""" Northshire Cleric
	Whenever a minion is healed, draw a card. """
	events = Heal(ALL_MINIONS).on(Draw(CONTROLLER))
	pass

if Murozond_the_Infinite:# 
	Core_Priest+=['CORE_DRG_090']
class CORE_DRG_090:# <6>[1637]## 23.6 ################ not yet ##########
	""" Murozond the Infinite
	[Battlecry:] Play all cards your opponent played last_turn. """
	#[雄叫び:]相手が前のターンに手札から使用した全てのカードを使用する。
	def play(self):
		controller=self.controller
		ret = []
		for _log in controller.opponent._play_log:
			if _log.turn == controller.game.turn - 1:
				ret.append(_log.card)
		for c in ret:
			card = controller.card(c.id)
			card.zone=Zone.HAND
			if card.type==CardType.MINION:
				Summon(controller, card).trigger(self)
			elif card.type==CardType.SPELL:
				CastSpell(card, None, None).trigger(self)
	pass

if Psychic_Conjurer:# 
	Core_Priest+=['CORE_EX1_193']
class CORE_EX1_193:# <6>[1637]## 23.6 ## OK
	""" Psychic Conjurer
	[Battlecry:] Copy a card in your opponent's deck and add it to your hand. """
	play= Give(CONTROLLER, Copy(RANDOM(ENEMY_DECK)))
	pass

if Power_Infusion:# 
	Core_Priest+=['CORE_EX1_194','EX1_194e']
class CORE_EX1_194:# <6>[1637]## 23.6 ## OK
	""" Power Infusion
	Give a minion +2/+6. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "EX1_194e")
	pass
EX1_194e = buff(2,6)

if Kul_Tiran_Chaplain:# 
	Core_Priest+=['CORE_EX1_195','EX1_195e']
class CORE_EX1_195:# <6>[1637]## 23.6 ## OK
	""" Kul Tiran Chaplain
	[Battlecry:] Give a friendly minion +2 Health. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Buff(TARGET, "EX1_195e")
	pass
EX1_195e = buff(health=2)

if Shadow_Word_Ruin:# 
	Core_Priest+=['CORE_EX1_197']
class CORE_EX1_197:# <6>[1637]## 23.6 ## OK
	""" Shadow Word: Ruin
	Destroy all minions with 5 or more Attack. """
	def play(self):
		for  card in self.controller.field:
			if hasattr(card,'atk') and card.atk>=5:
				Destroy(card).trigger(self)
		for  card in self.controller.opponent.field:
			if card.type==CardType.MINION and card.atk>=5:
				Destroy(card).trigger(self)
	pass




class CORE_EX1_198:# <6>[1637]## ## 22.6 ## OK
	""" Natalie Seline
	[Battlecry:] Destroy a minion and gain its Health. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_ENEMY_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = (
		Buff(SELF, 'EX1_198e', max_health=CURRENT_HEALTH(TARGET)),
		Destroy(TARGET)
		)
	pass

class CORE_EX1_335:# <6>[1637] ## 22.6 ## OK
	""" Lightspawn
	This minion's Attack is always equal to its Health. """
	update = Refresh(SELF, {GameTag.ATK: lambda self, i: self.health}, priority=100)
	pass

if Shadow_Word_Death:# 
	Core_Priest+=['CORE_EX1_622']
class CORE_EX1_622:# <6>[1637]## 23.6 ## OK
	""" Shadow Word: Death
	Destroy a minion with 5_or more Attack. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_MIN_ATTACK: 5,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Destroy(TARGET)
	pass

class CORE_EX1_623:# <6>[1637] ## 22.6 ## OK
	""" Temple Enforcer
	[Battlecry:] Give a friendly minion +3 Health. """
	requirements = {
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Buff(TARGET, "EX1_623e")
	pass
EX1_623e = buff(health=3)

class CORE_EX1_625:# <6>[1637] ## 22.6 ## OK
	""" Shadowform
	Your Hero Power becomes 'Deal 2 damage.' """
	play = Switch(FRIENDLY_HERO_POWER, {
		"EX1_625t": Summon(CONTROLLER, "EX1_625t2"),
		"EX1_625t2": (),
		None: Summon(CONTROLLER, "EX1_625t"),
	})
class EX1_625t:
	"""Mind Spike"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	activate = Hit(TARGET, 2)
	update = Refresh(CONTROLLER, {GameTag.SHADOWFORM: True})
class EX1_625t2:
	"""Mind Shatter"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	activate = Hit(TARGET, 3)
	update = Refresh(CONTROLLER, {GameTag.SHADOWFORM: True})
	pass

if Lightbomb:# 
	Core_Priest+=['CORE_GVG_008']
class CORE_GVG_008:# <6>[1637]## 23.6 # visually OK
	""" Lightbomb
	Deal damage to each minion equal to its Attack. """
	def play(self):
		for target in self.game.board:
			yield Hit(target, target.atk)
	pass

if Radiant_Elemental:# 
	Core_Priest+=['CORE_UNG_034','UNG_034e']
class CORE_UNG_034:# <6>[1637]## 23.6 ## visually OK
	""" Radiant Elemental
	Your spells cost (1) less. """
	play = Buff(FRIENDLY_HAND + SPELL, "UNG_034e")
	pass
class UNG_034e:
	tags={GameTag.COST:-1}

if Lyra_the_Sunshard:# 
	Core_Priest+=['CORE_UNG_963']
class CORE_UNG_963:# <6>[1637]## 23.6 ## visually OK
	""" Lyra the Sunshard
	Whenever you cast a spell, add a random Priest spell to your hand. """
	events = OWN_SPELL_PLAY.on(Give(CONTROLLER, RandomSpell(card_class=CardClass.PRIEST)))
	pass

if Shadowed_Spirit:# 
	Core_Priest+=['CS3_013']
class CS3_013:# <6>[1637]## 23.6 ## OK
	""" Shadowed Spirit
	[Deathrattle:] Deal 3damage to theenemy hero. """
	deathrattle = Hit(ENEMY_HERO, 3)
	pass

class CS3_014:# <6>[1637] ## 22.6 ## OK
	""" Crimson Clergy
	After a friendly character is healed, gain +1 Attack. """
	events=Heal(FRIENDLY_CHARACTERS).on(Buff(SELF,'CS3_014e'))
	pass
CS3_014e=buff(1,0)

if Focused_Will:# 
	Core_Priest+=['CS3_027']
	Core_Priest+=['CS3_027e']
class CS3_027:# <6>[1637]## 23.6 ## OK
	""" Focused Will
	[Silence] a minion, then give it +3 Health. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0 }
	play = Silence(TARGET), Buff(TARGET, 'CS3_027e')
	pass
CS3_027e=buff(0,3)


if Thrive_in_the_Shadows:# 
	Core_Priest+=['CS3_028']
class CS3_028:# <6>[1637]## 23.6
	""" Thrive in the Shadows
	[Discover] a spell from your deck. """
	Play=GenericChoice(CONTROLLER, RANDOM(FRIENDLY_DECK)*3)
	pass

#######################################
