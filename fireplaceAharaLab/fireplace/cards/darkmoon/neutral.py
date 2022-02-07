# neutral in DMF
# by Miyaryo, Sep. 2021
from ..utils import *

# 未実装
#DMF_053e,DMF_054e,DMF_055e,DMF_056e
#DMF_071e,DMF_079,DMF_113e,DMF_116e,DMF_120e2,DMF_187e
#DMF_224e,DMF_229e,DMF_229e2,DMF_230e,DMF_240e,
#DMF_247e,DMF_249e,DMF_534e,DMF_534e2,
#YOP_007e, 


class YOP_003:##OK
	""" Luckysoul Hoarder
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; Shuffle 2 Soul
Fragments into your deck.
&lt;b&gt;Corrupt:&lt;/b&gt; Draw a card."""
	play = Shuffle(CONTROLLER,'SCH_307t') * 2
	pass
class YOP_003t:#OK
	"""Luckysoul Hoarder
	[x]&lt;b&gt;Corrupted&lt;/b&gt; &lt;b&gt;Battlecry:&lt;/b&gt; Shuffle 2 Soul Fragments into your deck and draw a card."""
	play = Shuffle(CONTROLLER,'SCH_307t') * 2, Draw(CONTROLLER)
	pass
class YOP_006:#OK
	""" Hysteria
	[x]Choose an enemy minion.
It attacks random
minions until it dies."""
	requirements = { PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_ENEMY_TARGET:0, PlayReq.REQ_MINION_TARGET:0,}
	def play(self):
		game = self.game
		for repeat in range(1000):
			field = game.board
			if len(field)<=1:
				return
			target = self.target
			defender = random.choice(field)##
			if defender != target:
				Hit(defender, target.atk).trigger(self.controller)
				Hit(target, defender.atk).trigger(self.controller)
				if target.health<=0:
					return
	pass

#YOP_007e=buff(cost=-2)
#""" Dark Inquisition
#"""

class YOP_009:#OK
	""" Rally!
	Resurrect a friendly
1-Cost, 2-Cost, and
3-Cost minion. """
	def play(self):
		controller = self.controller
		minionList = controller.death_log
		cost1=[]
		cost2=[]
		cost3=[]
		for card in minionList:
			if card.cost==1:
				cost1.append(card)
			elif card.cost==2:
				cost2.append(card)
			elif card.cost==3:
				cost3.append(card)
		if cost1 != []:
			card = random.choice(cost1)##
			yield Summon(CONTROLLER,card.id)
		if cost2 != []:
			card = random.choice(cost2)##
			yield Summon(CONTROLLER,card.id)
		if cost3 != []:
			card = random.choice(cost3)##
			yield Summon(CONTROLLER,card.id)
	pass



class YOP_015:#OK
	""" Nitroboost Poison
	Give a minion +2 Attack. &lt;b&gt;Corrupt:&lt;/b&gt; And your weapon. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, }
	play = Buff(TARGET, 'YOP_015e')
	pass
YOP_015e=buff(atk=2)

class YOP_015t:#OK
	"""
	"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0, }
	play = Buff(TARGET, 'YOP_015e'), Buff(FRIENDLY_WEAPON, 'YOP_015e')
	pass

class YOP_018:################################
	"""Keywarden Ivory
	[x]&lt;b&gt;Battlecry:&lt;/b&gt; &lt;b&gt;Discover&lt;/b&gt; a
Dual Class spell from
any class. &lt;b&gt;&lt;b&gt;Spellburst&lt;/b&gt;:&lt;/b&gt;
Get another copy. """
	play = Discover(CONTROLLER, RandomSpell())#multiple_classes=True
	#.then(
	#	OWN_SPELL_PLAY.on(Give(CONTROLLER, Copy(Discover.CARDS))
	#	)
	pass
class YOP_018e:
	"""
	"""
	pass
class YOP_021:
	"""Imprisoned Phoenix
	&lt;b&gt;Dormant&lt;/b&gt; for 2 turns. &lt;b&gt;Spell Damage +2&lt;/b&gt;"""
	dormant = 2
	pass
class YOP_024:#OK
	"""Guidance
	Look at two spells. Add one to your hand or &lt;b&gt;Overload:&lt;/b&gt; (1) to get both."""
	def play(self):
		card1 = (RandomSpell().evaluate(self.controller))[0]
		card2 = (RandomSpell().evaluate(self.controller))[0]
		self.entourage = ['YOP_024t', card1.id, card2.id]
		self.controller.carry_cards=[card1.id, card2.id]
		Overload(self.controller, -1).trigger(self.controller)
		yield Discover(CONTROLLER, RandomEntourage())
		pass
	pass
class YOP_024t:
	"""Spirit Path
	Add both spells to your hand. &lt;b&gt;Overload&lt;/b&gt; (1)"""
	#no use #tags = {GameTag.CASTSWHENDRAWN: True}
	def play(self):## casts_when_chosen
		cards = self.controller.carry_cards
		for card in cards:
			Give(self.controller, card).trigger(self.controller)
		Overload(self.controller, 1).trigger(self.controller)
	pass
class YOP_029:#OK
	"""Resizing Pouch
	[x]&lt;b&gt;Discover&lt;/b&gt; a card with Cost equal to your remaining Mana Crystals."""
	def play(self):
		remain_mana = self.controller.mana 
		yield Discover(CONTROLLER, RandomCollectible(cost=remain_mana))
	pass
class YOP_030:#OK
	"""Felfire Deadeye
	Your Hero Power costs (1) less."""
	play = Buff(FRIENDLY_HERO_POWER, 'YOP_030e')
	pass
YOP_030e=buff(cost=-1)
"""Deadeye
Costs (1) less."""


class YOP_032:###OK
	"""Armor Vendor"""
	## <b>Battlecry:</b> Give 4 Armor to_each hero.
	play = (GainArmor(FRIENDLY_HERO,4),GainArmor(ENEMY_HERO,4))
	pass

class ShuffleLowestCostCard(TargetedAction):###OK
	def do(self, source, target):
		_lowestCostCards=[]
		for _card in target.hand:
			if len(_lowestCostCards)==0:
				_lowestCostCards = [_card]
			elif _lowestCostCards[0].cost > _card.cost:
				_lowestCostCards = [_card]
			elif _lowestCostCards[0].cost == _card.cost:
				_lowestCostCards.append(_card)
		if len(_lowestCostCards)>0:
			_card = random.choice(_lowestCostCards)##
			_cost = _card.cost
			log.info("Lowest cost card is %r (cost %d)"%(_card, _cost))
			Shuffle(target,_card).trigger(source)
		else:
			log.info("no hand"%())

class DMF_125:###OK
	"""Safety Inspector"""
	##[x]&lt;b&gt;Battlecry:&lt;/b&gt; Shuffle the_lowest-Cost card from your hand into your deck. Draw a card.
	play = ShuffleLowestCostCard(CONTROLLER),Draw(CONTROLLER)
	pass
#ULD_706のようにかけるかも？

class DMF_189:###OK
	"""Costumed Entertainer"""
	##[x]&lt;b&gt;Battlecry:&lt;/b&gt; Give a random minion in your hand +2/+2.
	play = Buff(RANDOM(FRIENDLY_HAND + MINION), "DMF_189e")
	pass
DMF_189e = buff(atk=2, health=2)

class YOP_031:###OK
	"""Crabrider"""
	##[x]&lt;b&gt;Rush&lt;/b&gt; &lt;b&gt;Battlecry:&lt;/b&gt; Gain &lt;b&gt;Windfury&lt;/b&gt; this turn only.
	play = Buff(SELF, "YOP_031e")
	pass
class YOP_031e:
	windfury = SET(1)

class DMF_124:###OK
	"""Horrendous Growth"""
	##&lt;b&gt;Corrupt:&lt;/b&gt; Gain +1/+1. Can be &lt;b&gt;Corrupted&lt;/b&gt; endlessly.
	pass

class DMF_124t:###OK
	"""Horrendous Growth"""
	##&lt;b&gt;Corrupt:&lt;/b&gt; Gain +1/+1. Can be &lt;b&gt;Corrupted&lt;/b&gt; endlessly.
	pass

class DMF_520:###OK
	"""Parade Leader"""
	##After you summon a &lt;b&gt;Rush&lt;/b&gt; minion, give it +2 Attack.
	events = Summon(CONTROLLER,rush=True).on(Buff(Summon.CARD,"DMF_520e"))
	pass
DMF_520e = buff(atk=2)

class DMF_067:###OK
	"""Prize Vendor"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; Each player draws a card.
	play = Draw(CONTROLLER),Draw(OPPONENT)
	pass

class DMF_044:###OK
	"""Rock Rager"""
	##&lt;b&gt;Taunt&lt;/b&gt;
	pass

class DMF_191:###OK
	"""Showstopper"""
	##&lt;b&gt;Deathrattle:&lt;/b&gt; &lt;b&gt;Silence&lt;/b&gt; all_minions.
	deathrattle = Silence(ALL_MINIONS)
	pass

class DMF_091:###OK
	"""Wriggling Horror"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; Give adjacent minions +1/+1.
	play = Buff(SELF_ADJACENT, "DMF_091e2")
	pass
DMF_091e2 = buff(atk=1,health=1)

class DMF_065:###OK
	"""Banana Vendor"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; Add 2 Bananas to each player's hand.
	play = Give(CONTROLLER, "DMF_065t") * 2, Give(OPPONENT, "DMF_065t") * 2
	pass
DMF_065e=buff(1,1)#no use
class DMF_065t:
	""" Banana
	Give a minion +1/+1. """
	requirements = {PlayReq.REQ_MINION_TARGET: 0, PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "DMF_065e")
	pass

class DMF_073:###OK
	"""Darkmoon Dirigible"""
	##&lt;b&gt;Divine Shield&lt;/b&gt; &lt;b&gt;Corrupt:&lt;/b&gt; Gain &lt;b&gt;Rush&lt;/b&gt;.
	pass

class DMF_073t:###OK
	"""Darkmoon Dirigible"""
	##&lt;b&gt;Corrupted&lt;/b&gt; &lt;b&gt;Rush&lt;/b&gt;, &lt;b&gt;Divine Shield&lt;/b&gt;
	pass

class DMF_082: ###OK ## not implementation for 'This gains +4 attack'
	"""Darkmoon Statue"""
	##Your other minions have +1 Attack. &lt;b&gt;Corrupt:&lt;/b&gt; This gains +4 Attack.
	update = Refresh(FRIENDLY_MINIONS - SELF, buff="DMF_082e")
	pass
DMF_082e = buff(atk=1)

class DMF_082t:
	"""Darkmoon Statue"""
	##lt;b&gt;Corrupted&lt;/b&gt; Your other minions have +1 Attack.
	update = Refresh(FRIENDLY_MINIONS - SELF, buff="DMF_082e")
	pass

class YOP_012_Deathrattle(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		game = target.game
		entities = game.entities
		destroyList=[]
		ownerList=[]
		## The enchantment YOP_012e is created artificially, so we need to proceed other 'refesh_aura' and 'destory'
		for entity in entities:
			if hasattr(entity,'id') and entity.id == 'YOP_012e':
				destroyList.append(entity)
				ownerList.append(entity.owner)
		for entity in destroyList:
			entity.remove()
		for entity in ownerList:
			entity.deathrattle_valid = True
		pass

class YOP_012:###OK
	"""Deathwarden"""
	##&lt;b&gt;Deathrattles&lt;/b&gt; can't trigger.
	update = Refresh(ALL_MINIONS - SELF, buff='YOP_012e')
	tags = {GameTag.DEATHRATTLE: True}
	deathrattle = YOP_012_Deathrattle(CONTROLLER)


class YOP_012e:
	pass

class DMF_062:###OK
	"""Gyreworm"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; If you played an Elemental last turn, deal 3_damage.
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	def play(self):
		current_turn = self.controller.game.turn
		for candidate in self.controller.game._myLog_:
			if candidate.turn == current_turn-2: #it is my last turn
				if hasattr(candidate.card, 'race'):
					if candidate.card.race == Race.ELEMENTAL:
						Hit(self.target,3).trigger(self.controller)
		pass
	pass

class DMF_081:###OK
	"""K'thir Ritualist"""
	##[x]&lt;b&gt;Taunt&lt;/b&gt; &lt;b&gt;Battlecry:&lt;/b&gt; Add a random 4-Cost minion to your opponent's hand.
	play = Give(OPPONENT, RandomMinion(cost=4))
	pass

class DMF_532:###OK
	"""Circus Amalgam"""
	##&lt;b&gt;Taunt&lt;/b&gt; &lt;i&gt;This has all minion types.&lt;/i&gt;
	pass

class DMF_174:###OK
	"""Circus Medic"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; Restore #4 Health. &lt;b&gt;Corrupt:&lt;/b&gt; Deal 4 damage instead.
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Heal(TARGET,4)
	pass

class DMF_174t:###OK
	"""Circus Medic"""
	##&lt;b&gt;Corrupted&lt;/b&gt; &lt;b&gt;Battlecry:&lt;/b&gt; Deal 4 damage.
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Hit(TARGET,4)
	pass

class DMF_190:###OK
	"""Fantastic Firebird"""
	##&lt;b&gt;Windfury&lt;/b&gt;
	pass

class DMF_066:###OK
	"""Knife Vendor"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; Deal 4 damage to each hero.
	play = Hit(FRIENDLY_HERO, 4),Hit(ENEMY_HERO, 4)
	pass

class DMF_202:###OK
	"""Derailed Coaster"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; Summon a 1/1 Rider with &lt;b&gt;Rush&lt;/b&gt; for each minion in your hand.
	play = Summon(CONTROLLER, "DMF_523t") * Count(FRIENDLY_HAND + MINION)
	pass

class DMF_080:
	"""Fleethoof Pearltusk"""
	##&lt;b&gt;Rush&lt;/b&gt; &lt;b&gt;Corrupt:&lt;/b&gt; Gain +4/+4.
	pass

class DMF_080t:
	"""Fleethoof Pearltusk"""
	##&lt;b&gt;Corrupted&lt;/b&gt; &lt;b&gt;Rush&lt;/b&gt;
	pass

class YOP_035:
	"""Moonfang"""
	##Can only take 1 damage at_a time.
	tags = {GameTag.HEAVILY_ARMORED: True}
	pass

class DMF_068:###OK
	"""Optimistic Ogre"""
	##50% chance to attack the correct enemy.
	events = FORGETFUL
	pass

class DMF_069:###OK
	"""Claw Machine"""
	##&lt;b&gt;Rush&lt;/b&gt;. &lt;b&gt;Deathrattle:&lt;/b&gt; Draw a minion and give it +3/+3.
	deathrattle = Give(CONTROLLER, RANDOM(FRIENDLY_DECK + MINION)).then(
		Buff(Give.CARD, "BT_213e"))
	pass
DMF_069e = buff(atk=3,health=3)

class DMF_074: #don't consider about chooseboth #OK
	"""Silas Darkmoon"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; Choose a direction to rotate all minions.
	choose = ("DMF_074a", "DMF_074b")
	pass

class DMF_074a:
	"""This Way"""
	def play(self):
		controller = self.controller
		enemy = controller.opponent
		if len(enemy.field) == 0:
			target = controller.field[0]
			zone = target.zone
			target.zone = Zone.SETASIDE
			target.controller = enemy
			target.turns_in_play = 0  # To ensure summoning sickness
			target._summon_index = None
			target.zone = zone
		else:
			target1 = controller.field[0]
			zone = target1.zone # might be PLAY
			target1.zone = Zone.SETASIDE
			target1.controller = enemy
			target1.turns_in_play = 0  # To ensure summoning sickness
			target1._summon_index = None
			target1.zone = zone

			target2 = enemy.field[0]
			zone = target2.zone # might be PLAY
			target2.zone = Zone.SETASIDE
			target2.controller = controller
			target2.turns_in_play = 0  # To ensure summoning sickness
			target2._summon_index = None
			target2.zone = zone
			pass
	pass

class DMF_074b:
	"""That Way"""
	def play(self):
		controller = self.controller
		enemy = controller.opponent
		if len(enemy.field) == 0:
			target = controller.field[-1]
			zone = target.zone
			target.zone = Zone.SETASIDE
			target.controller = enemy
			target.turns_in_play = 0  # To ensure summoning sickness
			target._summon_index = 0
			target.zone = zone
		else:
			target1 = controller.field[-1]
			zone = target1.zone
			target1.zone = Zone.SETASIDE
			target1.controller = enemy
			target1.turns_in_play = 0  # To ensure summoning sickness
			target1._summon_index = 0
			target1.zone = zone
			
			#for i in range(len(enemy.characters)-2):
			#	target = enemy.characters[1]
			#	target.zone = Zone.SETASIDE
			#	target.zone = Zone.PLAY

			target2 = enemy.field[-1]
			zone = target2.zone
			target2.zone = Zone.SETASIDE
			target2.controller = controller
			target2.turns_in_play = 0  # To ensure summoning sickness
			target2._summon_index = 0
			target2.zone = zone

			#for i in range(len(controller.characters)-2):
			#	target = controller.characters[1]
			#	target.zone = Zone.SETASIDE
			#	target.zone = Zone.PLAY
	pass

class DMF_078:###OK
	"""Strongman"""
	##&lt;b&gt;Taunt&lt;/b&gt; &lt;b&gt;Corrupt:&lt;/b&gt; This costs (0).
	pass
DMF_078e=buff(cost=0)
class DMF_078t:###OK
	"""Strongman"""
	##&lt;b&gt;Corrupted&lt;/b&gt; &lt;b&gt;Taunt&lt;/b&gt;
	pass

class DMF_163:###OK
	"""Carnival Clown"""
	##[x]&lt;b&gt;Taunt&lt;/b&gt; &lt;b&gt;Battlecry:&lt;/b&gt; Summon 2 copies of this. &lt;b&gt;Corrupt:&lt;/b&gt; Fill your board with copies.
	play = Summon(CONTROLLER, ExactCopy(SELF)) * 2
	pass

class DMF_163t:###OK
	"""Carnival Clown"""
	##[x]&lt;b&gt;Corrupted&lt;/b&gt; &lt;b&gt;Taunt&lt;/b&gt; &lt;b&gt;Battlecry:&lt;/b&gt; Fill your board with copies of this.
	play = Summon(CONTROLLER, ExactCopy(SELF)) * 6
	pass

class DMF_002:###OK
	"""N'Zoth, God of the Deep"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; Resurrect a friendly minion of each minion type.
	def summonRace(self, myRace, exclude):
		friendly_graveyard = self.controller.graveyard
		choice = []
		for card in friendly_graveyard:
			if not card in exclude and hasattr(card,'race'):
				if card.race == myRace or card.race == Race.ALL:
					choice.append(card)
		if len(choice)>0:
			card = random.choice(choice)##
			Summon(self.controller, card.id).trigger(self.controller)
			exclude.append(card)

	def play(self):
		exclude = []
		DMF_002.summonRace(self, Race.BEAST, exclude)
		DMF_002.summonRace(self, Race.DEMON, exclude)
		DMF_002.summonRace(self, Race.DRAGON, exclude)
		DMF_002.summonRace(self, Race.MECHANICAL, exclude)
		DMF_002.summonRace(self, Race.MURLOC, exclude)
		DMF_002.summonRace(self, Race.PIRATE, exclude)
		DMF_002.summonRace(self, Race.TOTEM, exclude)
		DMF_002.summonRace(self, Race.ELEMENTAL, exclude)
		DMF_002.summonRace(self, Race.QUILBOAR, exclude)


class YOP_034:###OK
	"""Runaway Blackwing"""
	##[x]At the end of your turn, deal 9 damage to a random enemy minion.
	events = OWN_TURN_END.on(Hit(RANDOM_ENEMY_MINION,9))
	pass

class DMF_254t_Action(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		card = target
		controller = card.controller
		if card.id=='DMF_254t3':
			controller.piece_of_cthun[0] = 1
		if card.id=='DMF_254t4':
			controller.piece_of_cthun[1] = 1
		if card.id=='DMF_254t5':
			controller.piece_of_cthun[2] = 1
		if card.id=='DMF_254t7':
			controller.piece_of_cthun[3] = 1
		c = sum(controller.piece_of_cthun)
		log.info("C'thun counts his pieces (%d/4)"%(c))
		if c==4:
			Shuffle(controller,'DMF_254').trigger(controller)
		pass

class DMF_254:###OK
	"""C'Thun, the Shattered"""
	##[x]&lt;b&gt;Start of Game:&lt;/b&gt; Break into pieces. &lt;b&gt;Battlecry:&lt;/b&gt; Deal 30 damage randomly split among all enemies.
	play = Hit(RANDOM_ENEMY_CHARACTER,1) * 30
	pass

class DMF_254t3:###OK
	""" Eye of C'Thun
	[x]&lt;b&gt;Piece_of_C'Thun_(@/4)&lt;/b&gt;Deal $7 damage randomly split among all enemies. """
	play = DMF_254t_Action(SELF),Hit(RANDOM_ENEMY_CHARACTER,1) * 7
	pass
class DMF_254t4:###OK
	""" Heart of C'Thun
	&lt;b&gt;Piece of C'Thun (@/4)&lt;/b&gt; Deal $3 damage to all minions. """
	play = DMF_254t_Action(SELF),Hit(ENEMY_MINIONS,3)
	pass
class DMF_254t5:###OK
	""" Body of C'Thun
	&lt;b&gt;Piece of C'Thun (@/4)&lt;/b&gt; Summon a 6/6 C'Thun's Body with &lt;b&gt;Taunt&lt;/b&gt;. """
	play = DMF_254t_Action(SELF),Summon(CONTROLLER,'DMF_254t5t')
	pass
class DMF_254t5t:
	""" C'Thun's Body
	&lt;b&gt;Taunt&lt;/b&gt; """
	pass
class DMF_254t7:###OK
	""" Maw of C'Thun
	&lt;b&gt;Piece of C'Thun (@/4)&lt;/b&gt; Destroy a minion. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0}
	play = DMF_254t_Action(SELF),Destroy(TARGET)
	pass

class DMF_070:###OK
	"""Darkmoon Rabbit"""
	##&lt;b&gt;Rush&lt;/b&gt;, &lt;b&gt;Poisonous&lt;/b&gt; Also damages the minions next to whomever this attacks.
	events = Attack(SELF, ENEMY_MINIONS).on(RegularAttack(SELF, ADJACENT(Attack.DEFENDER)))
	pass

class DMF_188: #this turn only??# yes! ##OK
	"""Y'Shaarj, the Defiler"""
	##[x]&lt;b&gt;Battlecry:&lt;/b&gt; Add a copy of each &lt;b&gt;Corrupted&lt;/b&gt; card you've played this game to your hand. They cost (0) this turn.
	def play(self):
		for card in self.controller.play_log:
			if hasattr(card,'corruptedcard') and card.corruptedcard:
				if (card.id)[-1]=='t':  #assert corrupted
					new_card = Give(self.controller, card.id[:-1]).trigger(self.controller)
					if new_card[0] != []:
						new_card = new_card[0][0]
						Buff(new_card, "DMF_188e2").trigger(self)
	pass
class DMF_188e:
	pass
class DMF_188e2:### ONE_TURN_EFFECT 
	cost = SET(0)
	events = EndTurn(CONTROLLER).on(Destroy(SELF))
class DMF_188t:
	pass

class Find10SpellsAndSpin(TargetedAction):
	CONTROLLER = ActionArg()
	def do(self, source, controller):
		count = 0
		for card in controller.play_log:
			if card.type==CardType.SPELL:
				count += 1
		if count >= 10:
			Give(controller,random.choice(['DMF_004t1','DMF_004t2','DMF_004t3','DMF_004t4','DMF_004t5','DMF_004t6'])).trigger(controller)##
		pass
class CountSpells(TargetedAction):
	CONTROLLER = ActionArg()
	def do(self, source, controller):
		count = 0
		for card in controller.play_log:
			if card.type==CardType.SPELL:
				count += 1
		source.script_data_num_1 = count
		source.script_data_text_0 = str(10-count)
		return count
		pass

class DMF_004:###OK
	"""Yogg-Saron, Master of Fate"""
	##[x]&lt;b&gt;Battlecry:&lt;/b&gt; If you've cast 10 spells this game, spin the Wheel of Yogg-Saron.
	#@ &lt;i&gt;({0} left!)&lt;/i&gt;@ &lt;i&gt;(Ready!)&lt;/i&gt;
	play = Find10SpellsAndSpin(CONTROLLER)
	class Hand:
		events = OWN_SPELL_PLAY.on(CountSpells(CONTROLLER))
	pass
class CastRandomSpell(TargetedAction):
	CONTROLLER = ActionArg()
	def do(self, source,controller):
		count = 0
		for card in controller.play_log:
			if card.type==CardType.SPELL:
				count+=1
		for repeat in range(count-1):
			spell = RandomSpell().evaluate(controller)
			spell = spell[0]
			spell.zone = Zone.HAND
			spell.cost = 0
			if spell.requires_target():
				target = random.choice(controller.field + controller.opponent.field + [controller.hero] + [controller.opponent.hero])##
				spell.play(target=target)
			else:
				spell.play()
		pass
class DMF_004t1:###OK
	"""Mysterybox
	Cast a random spell for every spell you've cast this game &lt;i&gt;(targets chosen randomly)&lt;/i&gt;. """
	play = CastRandomSpell(CONTROLLER)
	pass
DMF_004t1e=buff(0,0)
class DMF_004t2:###OK
	"""Hand of Fate
	Fill your hand with random spells. They cost (0) this turn. """
	play = (Give(CONTROLLER,RANDOM(SPELL)).then(Buff(Give.CARD,'DMF_188e2')),#借りてきた
		 Give(CONTROLLER,RANDOM(SPELL)).then(Buff(Give.CARD,'DMF_188e2')),
		 Give(CONTROLLER,RANDOM(SPELL)).then(Buff(Give.CARD,'DMF_188e2')),
		 Give(CONTROLLER,RANDOM(SPELL)).then(Buff(Give.CARD,'DMF_188e2')),
		 Give(CONTROLLER,RANDOM(SPELL)).then(Buff(Give.CARD,'DMF_188e2')),
		 Give(CONTROLLER,RANDOM(SPELL)).then(Buff(Give.CARD,'DMF_188e2')),
		 Give(CONTROLLER,RANDOM(SPELL)).then(Buff(Give.CARD,'DMF_188e2')),
		 Give(CONTROLLER,RANDOM(SPELL)).then(Buff(Give.CARD,'DMF_188e2')))
	pass
class DMF_004t3:###OK
	"""Curse of Flesh
	Fill the board with random minions, then give yours &lt;b&gt;Rush&lt;/b&gt; """
	play = (Summon(CONTROLLER,RANDOM(MINION)).then(SetTag(Give.CARD, (GameTag.RUSH,))),
		 Summon(CONTROLLER,RANDOM(MINION)).then(SetTag(Give.CARD, (GameTag.RUSH,))),
		 Summon(CONTROLLER,RANDOM(MINION)).then(SetTag(Give.CARD, (GameTag.RUSH,))),
		 Summon(CONTROLLER,RANDOM(MINION)).then(SetTag(Give.CARD, (GameTag.RUSH,))),
		 Summon(CONTROLLER,RANDOM(MINION)).then(SetTag(Give.CARD, (GameTag.RUSH,))),
		 Summon(CONTROLLER,RANDOM(MINION)).then(SetTag(Give.CARD, (GameTag.RUSH,))),
		 Summon(OPPONENT,RANDOM(MINION)),
		 Summon(OPPONENT,RANDOM(MINION)),
		 Summon(OPPONENT,RANDOM(MINION)),
		 Summon(OPPONENT,RANDOM(MINION)),
		 Summon(OPPONENT,RANDOM(MINION)),
		 Summon(OPPONENT,RANDOM(MINION))
		 )
	pass
class DMF_004t4:###OK
	"""Mindflayer Goggles
	Take control of three random enemy minions """
	play = (Destroy(RANDOM(ENEMY_MINIONS)).then(Summon(CONTROLLER,ExactCopy(Destroy.TARGET))),
		 Destroy(RANDOM(ENEMY_MINIONS)).then(Summon(CONTROLLER,ExactCopy(Destroy.TARGET))),
		 Destroy(RANDOM(ENEMY_MINIONS)).then(Summon(CONTROLLER,ExactCopy(Destroy.TARGET)))
		 )
	pass
class DestroyAll_GainStats(TargetedAction):
	CONTROLLER = ActionArg()
	def do(self, source, controller):
		minions = controller.field+controller.opponent.field
		new_atk=0
		new_health=0
		master = None
		for card in minions:
			if card.id != 'DMF_004':
				new_atk += card.atk
				new_health += card.max_health
				card.destroy()
			else:
				master = card
		if master != None:
			master.atk += new_atk
			master.max_health += new_health
		pass
	pass

class DMF_004t5:###OK
	"""Devouring Hunger
	Destroy all other minions. Gain their Attack and Health. """
	play = DestroyAll_GainStats(CONTROLLER)
	pass
DMF_004t5e=buff(0,0)

class RandomPyroblast(TargetedAction):
	CONTROLLER = ActionArg()
	def do(self, source, controller):
		while True:
			x = random.choice([controller.hero,controller.opponent.hero])##
			if x.health<10:
				Hit(x,10).trigger(source)
				# do something here?
				return
			else:
				Hit(x,10).trigger(source)
		pass
	pass
class DMF_004t6:### OK
	"""Rod of Roasting
	Cast 'Pyroblast' randomly until a hero dies."""
	play = RandomPyroblast(CONTROLLER)
	pass
