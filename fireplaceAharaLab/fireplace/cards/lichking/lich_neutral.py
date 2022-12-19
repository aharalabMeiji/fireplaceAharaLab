from ..utils import *

Lich_Neutral=[]

Lich_Shatterskin_Gargoyle=True
Lich_Infected_Peasant=True
Lich_Street_Sweeper=True
Lich_Brittleskin_Zombie=True
Lich_Incorporeal_Corporal=True
Lich_Drakkari_Embalmer=True
Lich_Bone_Flinger=True
Lich_Silvermoon_Arcanist=True
Lich_Sunfury_Clergy=True
Lich_Tenacious_Sanlayn=True
Lich_Crystal_Broker=True
Lich_Astalor_Bloodsworn=True
Lich_Silvermoon_Sentinel=True
Lich_The_Sunwell=True
Lich_Bonelord_Frostwhisper=True
Lich_Invincible=True
Lich_Lorthemar_Theron=True
Lich_Infectious_Ghoul=True
Lich_Sanctum_Spellbender=True
Lich_Arms_Dealer=True
Lich_Silvermoon_Farstrider_Spellpower=False# ------------------>hunter
Lich_Flesh_Behemoth=True
Lich_Plaguespreader=True
Lich_Foul_Egg=True
Lich_Nerubian_Vizier=True
Lich_Vrykul_Necrolyte=True
Lich_Scourge_Rager=True
Lich_Umbral_Geist=True
Lich_Amber_Whelp=True
Lich_Bloodied_Knight=True
Lich_Translocation_Instructor=True
Lich_Coroner=True
Lich_Enchanter=True
Lich_Silvermoon_Armorer=True
Lich_Banshee=True
Lich_Hawkstrider_Rancher=True

Lich_Banshee=True



if Lich_Shatterskin_Gargoyle:# ### OK ###
	Lich_Neutral+=['RLK_029']
class RLK_029:# <12>[1776]
	""" Shatterskin Gargoyle
	<b>Taunt</b> <b>Deathrattle:</b> Deal 4 damage to a random enemy. """
	deathrattle = Hit(RANDOM(ENEMY_CHARACTERS), 4)
	pass

if Lich_Infected_Peasant:# ### OK ###
	Lich_Neutral+=['RLK_070']
	Lich_Neutral+=['RLK_070t']
class RLK_070:# <12>[1776]
	""" Infected Peasant
	<b>Deathrattle:</b> Summon a 2/2 Undead Peasant. """
	deathrattle = Summon(CONTROLLER, 'RLK_070t')
	pass

class RLK_070t:# <12>[1776]
	""" Undead Peasant
	 """
	#
	pass

if Lich_Street_Sweeper:# ### OK ###
	Lich_Neutral+=['RLK_104']
class RLK_104:# <12>[1776]
	""" Street Sweeper
	<b>Battlecry:</b> Deal 2 damage to all other minions. """
	play = Hit(ALL_MINIONS - SELF, 2)
	pass

if Lich_Brittleskin_Zombie:# ### OK ###
	Lich_Neutral+=['RLK_113']
class RLK_113_Action(GameAction):
	def do(self, source):
		if source.controller != source.controller.game.current_player:
			for card in source.controller.opponent.field:
				Hit(card, 3).trigger(source)
		pass
class RLK_113:# <12>[1776]
	""" Brittleskin Zombie
	<b>Deathrattle:</b> If it's your opponent's turn, deal 3 damage to them. """
	deathrattle = RLK_113_Action()
	pass

if Lich_Incorporeal_Corporal:# ### OK ###
	Lich_Neutral+=['RLK_117']
class RLK_117:# <12>[1776]
	""" Incorporeal Corporal
	After this minion attacks, destroy it. """
	events = Attack(SELF).after(Destroy(Attack.DEFENDER))
	pass

if Lich_Drakkari_Embalmer:# ### OK ###
	Lich_Neutral+=['RLK_119']
class RLK_119_Action(TargetedAction):
	def do(self, source, target):
		if target and hasattr(target, 'this_is_minion') and target.race==Race.UNDEAD:
			target.reborn=True
		pass
class RLK_119:# <12>[1776]
	""" Drakkari Embalmer
	<b>Battlecry:</b> Give a friendly Undead <b>Reborn</b>. """
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0,
				PlayReq.REQ_TARGET_WITH_RACE:Race.UNDEAD }## Race.UNDEAD = 11
	play = RLK_119_Action(TARGET)
	pass

if Lich_Bone_Flinger:# ### OK ###
	Lich_Neutral+=['RLK_123']
class RLK_123_Action(GameAction):
	def do(self, source):
		cards=[card for card in source.controller.death_last_opponent_turn+source.controller.death_last_turn if card.type==CardType.MINION and card.race==Race.UNDEAD]
		if len(cards):
			card=random.choice(source.controller.opponent.field + [source.controller.opponent.hero])
			Hit(card, 2).trigger(source)
		pass
class RLK_123:# <12>[1776]
	""" Bone Flinger
	<b>Battlecry:</b> If a friendly Undead died after your last turn, deal 2 damage. """
	play = RLK_123_Action()
	pass

if Lich_Silvermoon_Arcanist:# ### OK ###
	Lich_Neutral+=['RLK_218']
	Lich_Neutral+=['RLK_218e']
	Lich_Neutral+=['RLK_218e2']
	Lich_Neutral+=['RLK_218e3']
class RLK_218_Action(GameAction):
	def do(self, source):
		source.controller.hero.cant_be_targeted_by_spells=False
		source.controller.opponent.hero.cant_be_targeted_by_spells=False
		source.remove()
		pass
class RLK_218:# <12>[1776]
	""" Silvermoon Arcanist
	<b>Spell Damage +2</b> <b>Battlecry:</b> Your spells can't target heroes this turn. """
	#<Tag enumID="192" name="SPELLPOWER" type="Int" value="2"/>
	play = Buff(CONTROLLER, 'RLK_218e')
	pass
class RLK_218e:# <12>[1776]
	""" Insane Arcanity
	Can't be targeted by spells this turn. """
	def apply(self, target):
		target.hero.cant_be_targeted_by_spells=True
		target.opponent.hero.cant_be_targeted_by_spells=True
	events = OWN_TURN_END.on(RLK_218_Action())
	pass
class RLK_218e2:# <12>[1776]
	""" Arcane Insanity
	Can't be targeted by spells this turn. """
	#
	pass
class RLK_218e3:# <12>[1776]
	""" Insane Arcane Power
	Your spells can't target heroes this turn. """
	#
	pass

if Lich_Sunfury_Clergy:# ### OK ###
	Lich_Neutral+=['RLK_219']
class RLK_219:# <12>[1776]
	""" Sunfury Clergy
	<b>Battlecry:</b> Restore 3 Health to all friendly characters. <b>Manathirst (6):</b> Restore 6 Health instead. """
	#<Tag enumID="2498" name="MANATHIRST" type="Int" value="6"/>
	#手札から使用する時、マナクリスタルがX個になっていた場合に効果が強化される。
	play = Manathirst(6, [Heal(FRIENDLY_MINIONS, 6)], [Heal(FRIENDLY_MINIONS, 3)]) 
	pass

if Lich_Tenacious_Sanlayn:# ### OK ###
	Lich_Neutral+=['RLK_220']
class RLK_220:# <12>[1776]
	""" Tenacious San'layn (5/4/6)
	<b>Lifesteal</b> Whenever this attacks, deal 2 damage to the enemy hero. """
	#<Tag enumID="685" name="LIFESTEAL" type="Int" value="1"/>
	events = Attack(SELF).on(Hit(ENEMY_HERO,2))
	pass

if Lich_Crystal_Broker:# ### OK ###
	Lich_Neutral+=['RLK_221']
class RLK_221:# <12>[1776]
	""" Crystal Broker
	<b>Manathirst (5):</b> Summon a random 3-Cost minion. <b>Manathirst (10):</b> Summon an 8-Cost minion instead. """
	play = Manathirst(10, [Summon(CONTROLLER, RandomMinion(cost=8))], []), Manathirst(5, [Summon(CONTROLLER, RandomMinion(cost=3))], [])
	pass

if Lich_Astalor_Bloodsworn:# ### OK ###
	Lich_Neutral+=['RLK_222']
	Lich_Neutral+=['RLK_222t1']
	Lich_Neutral+=['RLK_222t2']
class RLK_222:# <12>[1776]
	""" Astalor Bloodsworn
	<b>Battlecry:</b> Add Astalor, the Protector to your hand. <b>Manathirst (@):</b> Deal 2 damage. """
	#<Tag enumID="2498" name="MANATHIRST" type="Int" value="4"/>
	#<Tag enumID="2" name="TAG_SCRIPT_DATA_NUM_1" type="Int" value="4"/>
	play = Manathirst(4, [Give(CONTROLLER, 'RLK_222t1'), Hit(RANDOM(ENEMY_CHARACTERS),2)], [Give(CONTROLLER, 'RLK_222t1')])
	pass

class RLK_222t1:# <12>[1776]
	""" Astalor, the Protector
	<b>Battlecry:</b> Add Astalor, the Flamebringer to your hand. <b>Manathirst (@):</b> Gain 5 Armor. """
	#<Tag enumID="2498" name="MANATHIRST" type="Int" value="7"/>
	play = Manathirst(7, [Give(CONTROLLER, 'RLK_222t2'), GainArmor(FRIENDLY_HERO,5)], [Give(CONTROLLER, 'RLK_222t2')])
	pass

class RLK_222t2:# <12>[1776]
	""" Astalor, the Flamebringer
	<b>Battlecry:</b> Deal 8 damage randomly split between all enemies. <b>Manathirst (10):</b> Deal 8 more. """
	play = Manathirst(10, [SplitHit(CONTROLLER, ENEMY_CHARACTERS, 16)], [SplitHit(CONTROLLER, ENEMY_CHARACTERS, 8)])
	pass

if Lich_Silvermoon_Sentinel:# ### OK ###
	Lich_Neutral+=['RLK_518']
	Lich_Neutral+=['RLK_518e']
class RLK_518:# <12>[1776]
	""" Silvermoon Sentinel
	<b>Taunt</b> <b>Manathirst (@):</b> Gain +2/+2 and <b>Divine Shield</b>. """
	#<Tag enumID="2498" name="MANATHIRST" type="Int" value="8"/>
	play = Manathirst(8, [Buff(SELF, 'RLK_518e'), SetDivineShield(SELF, True)],[])
	pass
RLK_518e=buff(2,2)# <12>[1776]
""" Silvermoon's Might	+2/+2. """

if Lich_The_Sunwell:# ### OK ###
	Lich_Neutral+=['RLK_590']
class RLK_590_Action(GameAction):
	def do(self, source):
		amount = 10-len(source.controller.hand)
		cost_mod = len(source.controller.hand)
		for repeat in range(amount):
			newcard=Give(source.controller, RandomSpell()).trigger(source)
			newcard=get00(newcard)
			newcard.cost=max(newcard.cost-cost_mod, 0)
		pass
class RLK_590:# <12>[1776]
	""" The Sunwell
	Fill your hand with random spells. Costs (1) less for each other card in your hand. """
	play = RLK_590_Action()
	pass

if Lich_Bonelord_Frostwhisper:# ### OK ### 
	Lich_Neutral+=['RLK_591']
	Lich_Neutral+=['RLK_591e']
	Lich_Neutral+=['RLK_591e2']
class RLK_591_Action(GameAction):
	def do(self, source):
		for card in source.controller.hand:
			for bf in card.buffs:
				if bf.id=='RLK_591e2':
					bf.remove()
		pass
class RLK_591:# <12>[1776]
	""" Bonelord Frostwhisper
	<b>Deathrattle:</b> For the rest of the game, your first card each turn costs (0). You die in 3 turns. """
	deathrattle = Buff(CONTROLLER, 'RLK_591e'),Buff(FRIENDLY_HAND, 'RLK_591e2')
	pass
class RLK_591e:# <12>[1776]
	""" Lich Death Counter
	Your hero dies in @ turns. """
	events = [
		OWN_TURN_END.on(SidequestCounter(SELF, 3, [Destroy(FRIENDLY_HERO)]), RLK_591_Action()),
		OWN_TURN_BEGIN.on(Buff(FRIENDLY_HAND, 'RLK_591e2')),
		Play(CONTROLLER).after(RLK_591_Action())
	]
	pass
class RLK_591e2:# <12>[1776]
	""" Lich's Deathcurse
	Costs (0). """
	cost=lambda self,i:0#SET(0)
	pass

if Lich_Invincible:# ### OK ###
	Lich_Neutral+=['RLK_592']
	Lich_Neutral+=['RLK_592e']
class RLK_592:# <12>[1776]
	""" Invincible
	<b>Reborn</b> <b>Battlecry and Deathrattle:</b> Give a random friendly Undead +5/+5 and <b>Taunt</b>. """
	play = Buff(RANDOM(FRIENDLY_MINIONS + UNDEAD - SELF), 'RLK_592e')
	deathrattle = Buff(RANDOM(FRIENDLY_MINIONS + UNDEAD - SELF), 'RLK_592e')
	pass
RLK_592e=buff(5,5,taunt=True)# <12>[1776]
""" Invincible's Reins	+5/+5. """

if Lich_Lorthemar_Theron:# ### OK ###
	Lich_Neutral+=['RLK_593']
	Lich_Neutral+=['RLK_593e']
class RLK_593_Action(GameAction):
	def do(self, source):
		for card in source.controller.deck:
			if card.type==CardType.MINION:
				atk=card.atk
				hlth=card.max_health
				Buff(card, 'RLK_593e', atk=atk, max_health=hlth).trigger(source)
		pass
class RLK_593:# <12>[1776]
	""" Lor'themar Theron
	<b>Battlecry:</b> Double the stats of all minions in your deck. """
	play = RLK_593_Action()
	pass
class RLK_593e:# <12>[1776]
	""" Superior Strategy
	Doubled Attack and Health. """
	pass

if Lich_Infectious_Ghoul:# = Greybough DMF_734 ### OK ###
	Lich_Neutral+=['RLK_653']
	Lich_Neutral+=['RLK_653e']
class RLK_653:# <12>[1776]
	""" Infectious Ghoul
	<b>Deathrattle:</b> Give a random friendly minion "<b>Deathrattle:</b> Summon an Infectious Ghoul." """
	deathrattle = Buff(RANDOM(FRIENDLY_MINIONS - SELF), 'RLK_653e')
	pass
class RLK_653e:# <12>[1776]
	""" Infected
	<b>Deathrattle:</b> Summon an Infectious Ghoul. """
	tags={GameTag.DEATHRATTLE:True}
	deathrattle = Summon(CONTROLLER, 'RLK_653')
	pass

if Lich_Sanctum_Spellbender:# ### OK ###
	Lich_Neutral+=['RLK_677']
class RLK_677_Action(TargetedAction):
	TARGET=ActionArg()
	CARD=ActionArg()
	def do(self, source, target, card):
		##assert card.type==CardType.SPELL, ""
		##assert target.type==CardType.MINION and target.controller==source.controller, ""
		card.target = source
		pass
class RLK_677:# <12>[1776]
	""" Sanctum Spellbender
	Whenever your opponent targets another minion with a spell, redirect it to this. """
	events = Play(OPPONENT, SPELL, FRIENDLY+MINION).on(RLK_677_Action(Play.TARGET, Play.CARD))
	pass

if Lich_Arms_Dealer:# ### OK ###
	Lich_Neutral+=['RLK_824']
	Lich_Neutral+=['RLK_824e']
class RLK_824:# <12>[1776]
	""" Arms Dealer
	After you summon an Undead, give it +1 Attack. """
	events = Summon(CONTROLLER, UNDEAD).after(Buff(Summon.CARD, 'RLK_824e'))
	pass
RLK_824e=buff(1,0)
""" Undead Fortitude	+1 Attack. """


if Lich_Flesh_Behemoth:# ### OK ###
	Lich_Neutral+=['RLK_830']
class RLK_830_Action(GameAction):
	def do(self, source):
		cards=[card for card in source.controller.deck if card.type==CardType.MINION and card.race==Race.UNDEAD]
		if len(cards):
			card = random.choice(cards)
			card.zone=Zone.HAND
			Summon(source.controller, card.id).trigger(source)
		pass
class RLK_830:# <12>[1776]
	""" Flesh Behemoth
	<b>Taunt</b> <b>Deathrattle:</b> Draw another Undead and summon a copy of it. """
	deathrattle = RLK_830_Action()
	pass

if Lich_Plaguespreader:# ### OK ###
	Lich_Neutral+=['RLK_831']
class RLK_831:# <12>[1776]
	""" Plaguespreader
	<b>Deathrattle:</b> Transform a random minion in your opponent's hand into a Plaguespreader. """
	deathrattle = Morph(RANDOM(ENEMY_HAND + MINION),'RLK_831')
	pass

if Lich_Foul_Egg:# ### OK ###
	Lich_Neutral+=['RLK_833']
	Lich_Neutral+=['RLK_833t']
class RLK_833:# <12>[1776]
	""" Foul Egg
	<b>Deathrattle:</b> Summon a 3/3 Undead Chicken. """
	deathrattle = Summon(CONTROLLER, 'RLK_833t')
	pass

class RLK_833t:# <12>[1776]
	""" Foul Fowl
	 """
	#
	pass

if Lich_Nerubian_Vizier:# ### OK ###
	Lich_Neutral+=['RLK_834']
	Lich_Neutral+=['RLK_834e']
class RLK_834_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		card.zone=Zone.HAND
		cards=[cd for cd in self.player.death_last_opponent_turn + self.player.death_this_turn if cd.type==CardType.MINION and cd.race==Race.UNDEAD]
		if len(cards):
			Buff(card,'RLK_834e').trigger(self.source)
		pass
class RLK_834_Action(GameAction):
	def do(self, source):
		RLK_834_Choice(CONTROLLER, RandomSpell()*3).trigger(source)
		pass
class RLK_834:# <12>[1776]
	""" Nerubian Vizier
	<b>Battlecry:</b> <b>Discover</b> a spell. If a friendly Undead died after your last turn, it costs (2) less. """
	play = RLK_834_Action()
	pass
class RLK_834e:# <12>[1776]
	""" Nerubian Vision
	Costs (2) less. """
	cost=lambda self, i:max(i-2,0)
	pass

if Lich_Vrykul_Necrolyte:# ### OK ###
	Lich_Neutral+=['RLK_867']
	Lich_Neutral+=['RLK_867e','RLK_018t']
class RLK_867:# <12>[1776]
	""" Vrykul Necrolyte
	<b>Battlecry:</b> Give a friendly minion "<b>Deathrattle:</b> Summon a 2/2 Zombie with <b>Rush</b>." """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_FRIENDLY_TARGET:0 }
	play = Buff(TARGET, 'RLK_867e')
	pass
class RLK_867e:# <12>[1776]
	""" It's Necro-Lit
	<b>Deathrattle:</b> Summon a 2/2 Zombie with <b>Rush</b>. """
	tags={GameTag.DEATHRATTLE:True}
	deathrattle = Summon(CONTROLLER, 'RLK_018t')
	pass

if Lich_Scourge_Rager:# ### OK ###
	Lich_Neutral+=['RLK_900']
class RLK_900:# <12>[1776]
	""" Scourge Rager
	<b>Reborn</b> <b>Battlecry:</b> Die. """
	play = Destroy(SELF)
	pass

if Lich_Umbral_Geist:# ### OK ###
	Lich_Neutral+=['RLK_914']
class RLK_914:# <12>[1776]
	""" Umbral Geist
	<b>Deathrattle:</b> Add a random Shadow spell to your hand. """
	deathrattle = Give(CONTROLLER, RandomSpell(spell_school=SpellSchool.SHADOW))
	pass

if Lich_Amber_Whelp:# ### OK ###
	Lich_Neutral+=['RLK_915']
class RLK_915_Action(GameAction):
	def do(self, source):
		cards=[card for card in source.controller.field if card.type==CardType.MINION and card.race==Race.DRAGON]
		if len(cards):
			card = random.choice(source.controller.opponent.characters)
			Hit(card, 3).trigger(source)
		pass
class RLK_915:# <12>[1776]
	""" Amber Whelp
	<b>Battlecry:</b> If you're holding a Dragon, deal 3 damage. """
	play = RLK_915_Action()
	pass

if Lich_Bloodied_Knight:# ### OK ###
	Lich_Neutral+=['RLK_926']
class RLK_926:# <12>[1776]
	""" Bloodied Knight
	At the end of your turn, deal 2 damage to your hero. """
	events = OWN_TURN_END.on(Hit(FRIENDLY_HERO, 2))
	pass

if Lich_Translocation_Instructor:# ### OK ###
	Lich_Neutral+=['RLK_950']
class RLK_950_Action(TargetedAction):
	def do(self, source, target):
		if len(source.controller.opponent.deck):
			card = random.choice(source.controller.opponent.deck)
			target.zone=Zone.SETASIDE
			target.zone=Zone.DECK
			card.zone=Zone.PLAY
			random.shuffle(source.controller.opponent.deck)
		pass
class RLK_950:# <12>[1776]
	""" Translocation Instructor
	<b>Battlecry:</b> Choose an enemy minion. Swap it with a random one in their deck. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }	
	play = RLK_950_Action(TARGET)
	pass

if Lich_Coroner:# ### OK ###
	Lich_Neutral+=['RLK_951']
class RLK_951:# <12>[1776]
	""" Coroner
	<b>Battlecry:</b> <b>Freeze</b> an enemy minion. <b>Manathirst (6):</b> <b>Silence</b> it first. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, PlayReq.REQ_ENEMY_TARGET:0 }	
	play = Manathirst(6, [Silence(TARGET), Freeze(TARGET)], [Freeze(TARGET)])	
	pass

if Lich_Enchanter:# ### OK ###
	Lich_Neutral+=['RLK_952']
class RLK_952:# <12>[1776]
	""" Enchanter
	Enemy minions take double damage during your turn. """
	play = SetAttr(ENEMY_MINIONS, 'double_damage', 1)
	events = [
		OWN_TURN_END.on(SetAttr(ENEMY_MINIONS, 'double_damage', 0)),
		OWN_TURN_BEGIN.on(SetAttr(ENEMY_MINIONS, 'double_damage', 1)),
		Death(SELF).on(SetAttr(ENEMY_MINIONS, 'double_damage', 0))
		]
	pass

if Lich_Silvermoon_Armorer:# ### OK ###
	Lich_Neutral+=['RLK_955']
	Lich_Neutral+=['RLK_955e']
class RLK_955:# <12>[1776]
	""" Silvermoon Armorer
	<b>Rush</b> <b>Manathirst (@):</b> Gain +2/+2. """
	#<Tag enumID="2498" name="MANATHIRST" type="Int" value="7"/>
	play = Manathirst(7, [Buff(SELF, 'RLK_955e')], [])
	pass
RLK_955e=buff(2,2)
""" Supplied	+2/+2. """

if Lich_Banshee:# ### OK ###
	Lich_Neutral+=['RLK_957']
	Lich_Neutral+=['RLK_957e']
class RLK_957:# <12>[1776]
	""" Banshee
	<b>Deathrattle:</b> Give a random friendly Undead +2/+1. """
	deathrattle = Buff(RANDOM(FRIENDLY_MINIONS + UNDEAD), 'RLK_957e')
	pass
RLK_957e=buff(2,1)
""" Banshee's Wail	+2/+1. """

if Lich_Hawkstrider_Rancher:# ### OK ###
	Lich_Neutral+=['RLK_970']
	Lich_Neutral+=['RLK_970e']
	Lich_Neutral+=['RLK_970t']
class RLK_970:# <12>[1776]
	""" Hawkstrider Rancher
	After you play a minion, give it +1/+1 and "<b>Deathrattle:</b> Summon a 1/1 Hawkstrider." """
	events = Play(CONTROLLER, MINION).after(Buff(Play.CARD, 'RLK_970e'))
	pass
class RLK_970e:# <12>[1776]
	""" Hawkriding
	+1/+1. <b>Deathrattle:</b> Summon a 1/1 Hawkstrider. """
	tags = {GameTag.ATK:1, GameTag.HEALTH:1, GameTag.DEATHRATTLE:True}
	deathrattle = Summon(CONTROLLER, 'RLK_970t')
	pass
class RLK_970t:# <12>[1776]
	""" Hawkstrider
	 """
	pass


