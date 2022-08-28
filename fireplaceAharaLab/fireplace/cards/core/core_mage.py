from ..utils import *


Core_Mage=[]

Shooting_Star=True##23.6
Arcane_Intellect=True##23.6
Blizzard=True##23.6
Fireball=True##23.6
Flamestrike=True##23.6
Kalecgos=True##23.6
Cone_of_Cold=True##23.6
Pyroblast=True##23.6
Counterspell=True##23.6
Ice_Barrier=True##23.6
Snap_Freeze=True##23.6
Babbling_Book=True##23.6
Ethereal_Conjurer=True##23.6
Explosive_Runes=True##23.6
Pyromaniac=True##23.6
Arcanologist=True##23.6
Aegwynn_the_Guardian=True##23.6 
#########################
#CORE_AT_003:# <4>[1637] #22.6
#CORE_AT_008:# <4>[1637] ##22.6
#
#
#
#

class CORE_AT_003:# <4>[1637] #22.6
	""" Fallen Hero
	Your Hero Power deals 1_extra damage. """
	# HEROPOWER_DAMAGE=1
	pass

class CORE_AT_008:# <4>[1637] ##22.6
	""" Coldarra Drake
	You can use your Hero Power any number of times. """
	update = Refresh(FRIENDLY_HERO_POWER, {GameTag.HEROPOWER_ADDITIONAL_ACTIVATIONS: SET(-1)})
	pass

if Shooting_Star:# ##23.6
	Core_Mage+=['CORE_BOT_453']
class CORE_BOT_453:# <4>[1637]
	""" Shooting Star
	Deal $1 damage to a minion and the minions next to it. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET,1),Hit(TARGET_ADJACENT,1)
	pass

if Arcane_Intellect:# ##23.6
	Core_Mage+=['CORE_CS2_023']
class CORE_CS2_023:# <4>[1637]
	""" Arcane Intellect
	Draw 2 cards. """
	play = Draw(CONTROLLER) * 2
	pass

if Blizzard:# ##23.6
	Core_Mage+=['CORE_CS2_028']
class CORE_CS2_028:# <4>[1637] ###################
	""" Blizzard
	Deal $2 damage to all enemy minions and [Freeze] them. """
	play = Hit(ENEMY_MINIONS, 2), Freeze(ENEMY_MINIONS)	
	pass

if Fireball:# ##23.6
	Core_Mage+=['CORE_CS2_029']
class CORE_CS2_029:# <4>[1637]
	""" Fireball
	Deal $6 damage. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0, PlayReq.REQ_HERO_OR_MINION_TARGET: 0}
	play = Hit(TARGET, 6)
	pass

if Flamestrike:# ##23.6
	Core_Mage+=['CORE_CS2_032']
class CORE_CS2_032:# <4>[1637]
	""" Flamestrike
	Deal $5 damage to all enemy minions. """
	play = Hit(ENEMY_MINIONS, 5)
	pass

class CORE_CS2_033:# <4>[1637] 22.6
	""" Water Elemental
	[Freeze] any character damaged by this minion. """
	events = Damage(CHARACTER, None, SELF).on(Freeze(Damage.TARGET))
	pass

if Kalecgos:# ##23.6
	Core_Mage+=['CORE_DAL_609','DAL_609e']
class CORE_DAL_609:# <4>[1637]###################
	""" Kalecgos
	Your first spell each turn costs (0).[Battlecry:] [Discover]a spell. """
	events = OWN_TURN_BEGIN.on(Buff(FRIENDLY_HAND + SPELL, "DAL_609e"))
	play = Discover(CONTROLLER, RandomSpell())
class DAL_609e:
	cost = SET(0)
	events =  OWN_SPELL_PLAY.after(Destroy(SELF))

if Cone_of_Cold:# ##23.6
	Core_Mage+=['CORE_EX1_275']
class CORE_EX1_275:# <4>[1637]
	""" Cone of Cold
	[Freeze] a minion and the minions next to it, and deal $1 damage to them. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET | TARGET_ADJACENT, 1), Freeze(TARGET | TARGET_ADJACENT)
	pass

if Pyroblast:# ##23.6
	Core_Mage+=['CORE_EX1_279']
class CORE_EX1_279:# <4>[1637]
	""" Pyroblast
	Deal $10 damage. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 10)
	pass

if Counterspell:# ##23.6
	Core_Mage+=['CORE_EX1_287']
class CORE_EX1_287:# <4>[1637]
	""" Counterspell
	[Secret:] When your opponent casts a spell, [Counter] it. """
	secret = Play(OPPONENT, SPELL).on(Reveal(SELF), Counter(Play.CARD))
	pass

if Ice_Barrier:# ##23.6
	Core_Mage+=['CORE_EX1_289']
class CORE_EX1_289:# <4>[1637]
	""" Ice Barrier
	[Secret:] When your hero is attacked, gain 8 Armor. """
	secret = Attack(CHARACTER, FRIENDLY_HERO).on( Reveal(SELF), GainArmor(FRIENDLY_HERO, 8) )
	pass

class CORE_EX1_294:# <4>[1637] 22.6
	""" Mirror Entity
	[Secret:] After your opponent plays a minion, summon a copy of it. """
	secret = [
		Play(OPPONENT, MINION).after(Reveal(SELF), Summon(CONTROLLER, ExactCopy(Play.CARD))	),
		#Play(OPPONENT, ID("EX1_323h")).after(Reveal(SELF), Summon(CONTROLLER, "EX1_323"))  # :-)
		]
	pass

if Snap_Freeze:# ##23.6
	Core_Mage+=['CORE_GIL_801']
#class FreezeOrDeath(TargetedAction):
#	def do (self, source, target):
#		if target.frozen:
#			Destroy(target).trigger(source)
#		else:
#			Freeze(target).trigger(source)
#		pass
class CORE_GIL_801:# <4>[1637]
	""" Snap Freeze
	[Freeze] a minion.If it's already [Frozen], destroy it. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	#play = FreezeOrDeath(TARGET);
	play = Frozen(TARGET) & Destroy(TARGET) | Freeze(TARGET)
	pass

if Babbling_Book:# ##23.6
	Core_Mage+=['CORE_KAR_009']
class CORE_KAR_009:# <4>[1637]
	""" Babbling Book
	[Battlecry:] Add a random Mage spell to your hand. """
	play = Give(CONTROLLER, RandomSpell(card_class=FRIENDLY_CLASS))## card_class=CardClass.MAGE
	pass

if Ethereal_Conjurer:# ##23.6
	Core_Mage+=['CORE_LOE_003']
class CORE_LOE_003:# <4>[1637]
	""" Ethereal Conjurer
	[Battlecry: Discover] a spell. """
	play = DISCOVER(RandomSpell())
	pass

if Explosive_Runes:# ##23.6
	Core_Mage+=['CORE_LOOT_101']
class CORE_LOOT_101_Action(TargetedAction):
	CARDS=ActionArg()
	def do(self, source, cards):
		if cards==[]:
			return
		if isinstance(cards,list):
			card=cards[0]
		else:
			card=cards
		if card.health<6:
			Hit(source.controller.opponent.hero, 6-card.health).trigger(source)
			Hit(card, card.health).trigger(source)
		else:
			Hit(card, 6).trigger(source)
class CORE_LOOT_101:# <4>[1637]
	""" Explosive Runes
	[Secret:] After your opponent plays a minion, deal $6 damage to it and any excess to their hero. """
	secret = Play(OPPONENT, MINION).on(CORE_LOOT_101_Action(Play.CARD))
	pass

if Pyromaniac:# ##23.6
	Core_Mage+=['CORE_TRL_315']
class CORE_TRL_315_Action(TargetedAction):
	CARD=ActionArg()
	TARGET=ActionArg()
	def do(self, source, card, target):
		if card.id=='HERO_08bp':
			atk=1
		elif card.id=='HERO_08bp2':
			atk=2
		else:
			atk=0
		if target.health<=atk:
			Draw(source.controller).trigger(source)
class CORE_TRL_315:# <4>[1637]
	""" Pyromaniac
	Whenever your Hero Power_kills a minion, draw a card. """
	events = Activate(CONTROLLER, FRIENDLY_HERO_POWER, MINION).on(CORE_TRL_315_Action(Activate.CARD, Activate.TARGET))
	pass

if Arcanologist:# ##23.6
	Core_Mage+=['CORE_UNG_020']
class CORE_UNG_020:# <4>[1637]
	""" Arcanologist
	[Battlecry:] Draw a [Secret]. """
	play = Give(CONTROLLER,RANDOM(FRIENDLY_DECK + SECRET))
	pass

if Aegwynn_the_Guardian:# ##23.6
	Core_Mage+=['CS3_001']
	Core_Mage+=['CS3_001e']
	Core_Mage+=['CS3_001e2']
class CS3_001_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):#target = controller(player)
		Buff(target, "CS3_001e2").trigger(source)# inherit the ability from a card to a player
		#print("Guardian's legacy flag on (%r)"%(target))
		pass
class CS3_001_Action2(TargetedAction):
	TARGET=ActionArg()
	def do(self, source, target):#target = new card
		player = target.controller#
		if target.type == CardType.MINION:
			for buff in player.buffs:
				if buff.id=='CS3_001e2':
					player.buffs.remove(buff)
					break
			target.spellpower = 2
			Buff(target, 'CS3_001e').trigger(source)
			#print("Guardian's legacy is inderited by %r"%(card))		
		pass
class CS3_001:# <4>[1637]
	""" Aegwynn, the Guardian
	[Spell Damage +2][Deathrattle:] The next minion_you draw inherits these powers. """
	#play = Buff(SELF, 'CS3_001e')
	deathrattle = CS3_001_Action(CONTROLLER)
class CS3_001e:# <4>[1637]
	tags={GameTag.DEATHRATTLE:True}
	deathrattle = CS3_001_Action(CONTROLLER)
	pass
class CS3_001e2:# <4>[1637]
	events = Draw(CONTROLLER).on(CS3_001_Action2(Draw.CARD))
	pass


##########################


