# neutral in DMF
# by Miyaryo, Sep. 2021
from ..utils import *

class YOP_032:###OK
	"""Armor Vendor"""
	## <b>Battlecry:</b> Give 4 Armor to_each hero.
	play = (GainArmor(FRIENDLY_HERO,4),GainArmor(ENEMY_HERO,4))
	pass

<<<<<<< HEAD
class ShuffleLowestCostCard(TargetedAction):
=======
class ShuffleLowestCostCard(TargetedAction):###OK
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
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
			_card = random.choice(_lowestCostCards)
			_cost = _card.cost
			log.info("Lowest cost card is %r (cost %d)"%(_card, _cost))
			Shuffle(target,_card).trigger(source)
		else:
			log.info("no hand"%())

<<<<<<< HEAD
class DMF_125:
=======
class DMF_125:###OK
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	"""Safety Inspector"""
	##[x]&lt;b&gt;Battlecry:&lt;/b&gt; Shuffle the_lowest-Cost card from your hand into your deck. Draw a card.
	play = ShuffleLowestCostCard(CONTROLLER),Draw(CONTROLLER)
	pass
#ULD_706のようにかけるかも？

<<<<<<< HEAD
class DMF_189:
=======
class DMF_189:###OK
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	"""Costumed Entertainer"""
	##[x]&lt;b&gt;Battlecry:&lt;/b&gt; Give a random minion in your hand +2/+2.
	play = Buff(RANDOM(FRIENDLY_HAND + MINION), "DMF_189e")
	pass
DMF_189e = buff(atk=2, health=2)

<<<<<<< HEAD
class YOP_031:
=======
class YOP_031:###OK
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	"""Crabrider"""
	##[x]&lt;b&gt;Rush&lt;/b&gt; &lt;b&gt;Battlecry:&lt;/b&gt; Gain &lt;b&gt;Windfury&lt;/b&gt; this turn only.
	play = Buff(SELF, "YOP_031e")
	pass
class YOP_031e:
	windfury = SET(1)

<<<<<<< HEAD
class YOP_031e:
	windfury = SET(1)

class DMF_124:
=======
class DMF_124:###OK
	"""Horrendous Growth"""
	##&lt;b&gt;Corrupt:&lt;/b&gt; Gain +1/+1. Can be &lt;b&gt;Corrupted&lt;/b&gt; endlessly.
	pass

class DMF_124t:###OK
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	"""Horrendous Growth"""
	##&lt;b&gt;Corrupt:&lt;/b&gt; Gain +1/+1. Can be &lt;b&gt;Corrupted&lt;/b&gt; endlessly.
	pass

<<<<<<< HEAD
class DMF_520:
	"""Parade Leader"""
	##After you summon a &lt;b&gt;Rush&lt;/b&gt; minion, give it +2 Attack.
	events = Summon(CONTROLLER,rush=True).on(Buff(Summon.CARD,"dmf_520e"))
	pass
DMF_520e = buff(atk=2)

class DMF_067:
=======
class DMF_520:###OK
	"""Parade Leader"""
	##After you summon a &lt;b&gt;Rush&lt;/b&gt; minion, give it +2 Attack.
	events = Summon(CONTROLLER,rush=True).on(Buff(Summon.CARD,"DMF_520e"))
	pass
DMF_520e = buff(atk=2)

class DMF_067:###OK
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	"""Prize Vendor"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; Each player draws a card.
	play = Draw(CONTROLLER),Draw(OPPONENT)
	pass

<<<<<<< HEAD
class DMF_044:
=======
class DMF_044:###OK
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	"""Rock Rager"""
	##&lt;b&gt;Taunt&lt;/b&gt;
	pass

<<<<<<< HEAD
class DMF_191:
=======
class DMF_191:###OK
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	"""Showstopper"""
	##&lt;b&gt;Deathrattle:&lt;/b&gt; &lt;b&gt;Silence&lt;/b&gt; all_minions.
	deathrattle = Silence(ALL_MINIONS)
	pass

<<<<<<< HEAD
class DMF_091:
=======
class DMF_091:###OK
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	"""Wriggling Horror"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; Give adjacent minions +1/+1.
	play = Buff(SELF_ADJACENT, "DMF_091e2")
	pass
DMF_091e2 = buff(atk=1,health=1)

<<<<<<< HEAD
class DMF_065:
=======
class DMF_065:###OK
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	"""Banana Vendor"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; Add 2 Bananas to each player's hand.
	play = Give(CONTROLLER, "EX1_014t") * 2, Give(OPPONENT, "EX1_014t") * 2
	pass

<<<<<<< HEAD
class DMF_073:
=======
class DMF_073:###OK
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	"""Darkmoon Dirigible"""
	##&lt;b&gt;Divine Shield&lt;/b&gt; &lt;b&gt;Corrupt:&lt;/b&gt; Gain &lt;b&gt;Rush&lt;/b&gt;.
	pass

<<<<<<< HEAD
class DMF_073t:
=======
class DMF_073t:###OK
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	"""Darkmoon Dirigible"""
	##&lt;b&gt;Corrupted&lt;/b&gt; &lt;b&gt;Rush&lt;/b&gt;, &lt;b&gt;Divine Shield&lt;/b&gt;
	pass

<<<<<<< HEAD
class DMF_082:
=======
class DMF_082: ###OK ## not implementation for 'This gains +4 attack'
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
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
<<<<<<< HEAD

#☆
class YOP_012:
	"""Deathwarden"""
	##&lt;b&gt;Deathrattles&lt;/b&gt; can't trigger.
	pass

class DMF_062:
	"""Gyreworm"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; If you played an Elemental last turn, deal 3_damage.
	def play(self):
		current_turn = self.controller.game.turn
		for candidate in self.controller.game.__myLog__:
			if candidate.turn == current_turn-2: #it is my last turn
				if hasattr(candidate.card, 'race'):
					if candidate.card.race == Race.ELEMENTAL:
						requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
						Hit(TARGET,3)
		pass
	pass

class DMF_079:
	"""Inconspicuous Rider"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; Cast a &lt;b&gt;Secret&lt;/b&gt; from your deck.
	play = Summon(CONTROLLER, RANDOM(FRIENDLY_DECK + SECRET))
	pass

class DMF_081:
=======

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
		for candidate in self.controller.game.__myLog__:
			if candidate.turn == current_turn-2: #it is my last turn
				if hasattr(candidate.card, 'race'):
					if candidate.card.race == Race.ELEMENTAL:
						Hit(self.target,3).trigger(self.controller)
		pass
	pass

class DMF_081:###OK
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	"""K'thir Ritualist"""
	##[x]&lt;b&gt;Taunt&lt;/b&gt; &lt;b&gt;Battlecry:&lt;/b&gt; Add a random 4-Cost minion to your opponent's hand.
	play = Give(OPPONENT, RandomMinion(cost=4))
	pass

<<<<<<< HEAD
class DMF_532:
=======
class DMF_532:###OK
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	"""Circus Amalgam"""
	##&lt;b&gt;Taunt&lt;/b&gt; &lt;i&gt;This has all minion types.&lt;/i&gt;
	pass

<<<<<<< HEAD
class DMF_174:
=======

class DMF_174:###OK
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	"""Circus Medic"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; Restore #4 Health. &lt;b&gt;Corrupt:&lt;/b&gt; Deal 4 damage instead.
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Heal(TARGET,4)
	pass

<<<<<<< HEAD
class DMF_174t:
=======
class DMF_174t:###OK
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	"""Circus Medic"""
	##&lt;b&gt;Corrupted&lt;/b&gt; &lt;b&gt;Battlecry:&lt;/b&gt; Deal 4 damage.
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Hit(TARGET,4)
<<<<<<< HEAD

	pass

class DMF_190:
=======
	pass

class DMF_190:###OK
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	"""Fantastic Firebird"""
	##&lt;b&gt;Windfury&lt;/b&gt;
	pass

<<<<<<< HEAD
class DMF_066:
	"""Knife Vendor"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; Deal 4 damage to each hero.
	play = Hit(FRIENDLY_HERO + ENEMY_HERO, 4)
	pass

class DMF_202:
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

=======
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

>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
class YOP_035:
	"""Moonfang"""
	##Can only take 1 damage at_a time.
	tags = {GameTag.HEAVILY_ARMORED: True}
	pass

<<<<<<< HEAD
class DMF_068:
=======
class DMF_068:###OK
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	"""Optimistic Ogre"""
	##50% chance to attack the correct enemy.
	events = FORGETFUL
	pass

<<<<<<< HEAD
class DMF_069:
	"""Claw Machine"""
	##&lt;b&gt;Rush&lt;/b&gt;. &lt;b&gt;Deathrattle:&lt;/b&gt; Draw a minion and give it +3/+3.
	play = ForceDraw(RANDOM(FRIENDLY_DECK + MINION)).then(
		Buff(ForceDraw.TARGET, "BT_213e"))
=======
class DMF_069:###OK
	"""Claw Machine"""
	##&lt;b&gt;Rush&lt;/b&gt;. &lt;b&gt;Deathrattle:&lt;/b&gt; Draw a minion and give it +3/+3.
	deathrattle = Give(CONTROLLER, RANDOM(FRIENDLY_DECK + MINION)).then(
		Buff(Give.CARD, "BT_213e"))
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
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
		if len(enemy.characters) <= 1:
			target = controller.characters[1]
			zone = target.zone
			target.zone = Zone.SETASIDE
			target.controller = enemy
			target.turns_in_play = 0  # To ensure summoning sickness
			target.zone = zone
		else:
			target1 = controller.characters[1]
			zone = target1.zone
			target1.zone = Zone.SETASIDE
			target1.controller = enemy
			target1.turns_in_play = 0  # To ensure summoning sickness
			target1.zone = zone

			target2 = enemy.characters[1]
			zone = target2.zone
			target2.zone = Zone.SETASIDE
			target2.controller = controller
			target2.turns_in_play = 0  # To ensure summoning sickness
			target2.zone = zone
	pass

class DMF_074b:
	"""That Way"""
	def play(self):
		controller = self.controller
		enemy = controller.opponent
		if len(enemy.characters) <= 1:
			target = controller.characters[-1]
			zone = target.zone
			target.zone = Zone.SETASIDE
			target.controller = enemy
			target.turns_in_play = 0  # To ensure summoning sickness
			target.zone = zone
		else:
			target1 = controller.characters[-1]
			zone = target1.zone
			target1.zone = Zone.SETASIDE
			target1.controller = enemy
			target1.turns_in_play = 0  # To ensure summoning sickness
			target1.zone = zone
			
			for i in range(len(enemy.characters)-2):
				target = enemy.characters[1]
				target.zone = Zone.SETASIDE
				target.zone = Zone.PLAY

			target2 = enemy.characters[-1]
			zone = target2.zone
			target2.zone = Zone.SETASIDE
			target2.controller = controller
			target2.turns_in_play = 0  # To ensure summoning sickness
			target2.zone = zone

			for i in range(len(controller.characters)-2):
				target = controller.characters[1]
				target.zone = Zone.SETASIDE
				target.zone = Zone.PLAY
	pass

<<<<<<< HEAD
class DMF_078:
=======
class DMF_078:###OK
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	"""Strongman"""
	##&lt;b&gt;Taunt&lt;/b&gt; &lt;b&gt;Corrupt:&lt;/b&gt; This costs (0).
	pass

<<<<<<< HEAD
class DMF_078t:
=======
class DMF_078t:###OK
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	"""Strongman"""
	##&lt;b&gt;Corrupted&lt;/b&gt; &lt;b&gt;Taunt&lt;/b&gt;
	pass

<<<<<<< HEAD
class DMF_163:
	"""Carnival Clown"""
	play = Summon(CONTROLLER, Copy(SELF)) * 2
	##[x]&lt;b&gt;Taunt&lt;/b&gt; &lt;b&gt;Battlecry:&lt;/b&gt; Summon 2 copies of this. &lt;b&gt;Corrupt:&lt;/b&gt; Fill your board with copies.

	pass

class DMF_163t:
=======
class DMF_163:###OK
	"""Carnival Clown"""
	##[x]&lt;b&gt;Taunt&lt;/b&gt; &lt;b&gt;Battlecry:&lt;/b&gt; Summon 2 copies of this. &lt;b&gt;Corrupt:&lt;/b&gt; Fill your board with copies.
	play = Summon(CONTROLLER, Copy(SELF)) * 2
	pass

class DMF_163t:###OK
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	"""Carnival Clown"""
	##[x]&lt;b&gt;Corrupted&lt;/b&gt; &lt;b&gt;Taunt&lt;/b&gt; &lt;b&gt;Battlecry:&lt;/b&gt; Fill your board with copies of this.
	play = Summon(CONTROLLER, Copy(SELF)) * 6
	pass

<<<<<<< HEAD
class DMF_002:
	"""N'Zoth, God of the Deep"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; Resurrect a friendly minion of each minion type.
	def play(self):
		Summon(CONTROLLER, Copy(RANDOM(FRIENDLY + KILLED + MINION + (BEAST | ALL))))
		Summon(CONTROLLER, Copy(RANDOM(FRIENDLY + KILLED + MINION + (DEMON | ALL))))
		Summon(CONTROLLER, Copy(RANDOM(FRIENDLY + KILLED + MINION + (DRAGON | ALL))))
		Summon(CONTROLLER, Copy(RANDOM(FRIENDLY + KILLED + MINION + (MECH | ALL))))
		Summon(CONTROLLER, Copy(RANDOM(FRIENDLY + KILLED + MINION + (MURLOC | ALL))))
		Summon(CONTROLLER, Copy(RANDOM(FRIENDLY + KILLED + MINION + (PIRATE | ALL))))
		Summon(CONTROLLER, Copy(RANDOM(FRIENDLY + KILLED + MINION + (TOTEM | ALL))))
		Summon(CONTROLLER, Copy(RANDOM(FRIENDLY + KILLED + MINION + (ELEMENTAL | ALL))))
		Summon(CONTROLLER, Copy(RANDOM(FRIENDLY + KILLED + MINION + (QUILBOAR | ALL))))
		pass
	pass

class YOP_034:
	"""Runaway Blackwing"""
	##[x]At the end of your turn, deal 9 damage to a random enemy minion.
	events = OWN_TURN_END.on(Hit(RANDOM_ENEMY_MINION,9))
	pass

class DMF_254:
	"""C'Thun, the Shattered"""
	##[x]&lt;b&gt;Start of Game:&lt;/b&gt; Break into pieces. &lt;b&gt;Battlecry:&lt;/b&gt; Deal 30 damage randomly split among all enemies.
=======
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
			card = random.choice(choice)
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
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	pass

class DMF_070:###OK
	"""Darkmoon Rabbit"""
	##&lt;b&gt;Rush&lt;/b&gt;, &lt;b&gt;Poisonous&lt;/b&gt; Also damages the minions next to whomever this attacks.
	events = Attack(SELF, ENEMY_MINIONS).on(RegularAttack(SELF, ADJACENT(Attack.DEFENDER)))
<<<<<<< HEAD

	pass

class DMF_188: #this turn only??
	"""Y'Shaarj, the Defiler"""
	##[x]&lt;b&gt;Battlecry:&lt;/b&gt; Add a copy of each &lt;b&gt;Corrupted&lt;/b&gt; card you've played this game to your hand. They cost (0) this turn.
	def play(self):
		for candidate in self.controller.game.__myLog__:
			if hasattr(candidate.card,'corrupted'):
				Give(CONTROLLER, Copy(candidate.card)).then(Buff(Give.CARD, "DMF_188e2"))
	pass
class MF_188e2:
	cost = SET(0)

class DMF_004:
	"""Yogg-Saron, Master of Fate"""
	##[x]&lt;b&gt;Battlecry:&lt;/b&gt; If you've cast 10 spells this game, spin the Wheel of Yogg-Saron.@ &lt;i&gt;({0} left!)&lt;/i&gt;@ &lt;i&gt;(Ready!)&lt;/i&gt;
=======
	pass

class DMF_188: #this turn only??# yes! ##OK
	"""Y'Shaarj, the Defiler"""
	##[x]&lt;b&gt;Battlecry:&lt;/b&gt; Add a copy of each &lt;b&gt;Corrupted&lt;/b&gt; card you've played this game to your hand. They cost (0) this turn.
	def play(self):
		for card in self.controller.play_log:
			if hasattr(card,'corruptedcard') and card.corruptedcard:
				#a=(card.id)[-1]
				#b=card.id[:-1]
				if (card.id)[-1]=='t':  #assert corrupted
					new_card = Give(self.controller, card.id[:-1]).trigger(self.controller)
					new_card = new_card[0][0]
					Buff(new_card, "DMF_188e2").trigger(self)
	pass
class DMF_188e2:###  
	cost = SET(0)
	events = EndTurn(CONTROLLER).on(Destroy(SELF))

class Find10SpellsAndSpin(TargetedAction):
	CONTROLLER = ActionArg()
	def do(self, source, controller):
		count = 0
		for card in controller.play_log:
			if card.type==CardType.SPELL:
				count += 1
		if count >= 10:
			Give(controller,random.choice(['DMF_004t1','DMF_004t2','DMF_004t3','DMF_004t4','DMF_004t5','DMF_004t6'])).trigger(controller)
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
				target = random.choice(controller.field + controller.opponent.field + [controller.hero] + [controller.opponent.hero])
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
		 Summon(OPPONENT,RANDOM(MINION)).then(SetTag(Give.CARD, (GameTag.RUSH,))),
		 Summon(OPPONENT,RANDOM(MINION)).then(SetTag(Give.CARD, (GameTag.RUSH,))),
		 Summon(OPPONENT,RANDOM(MINION)).then(SetTag(Give.CARD, (GameTag.RUSH,))),
		 Summon(OPPONENT,RANDOM(MINION)).then(SetTag(Give.CARD, (GameTag.RUSH,))),
		 Summon(OPPONENT,RANDOM(MINION)).then(SetTag(Give.CARD, (GameTag.RUSH,))),
		 Summon(OPPONENT,RANDOM(MINION)).then(SetTag(Give.CARD, (GameTag.RUSH,))))
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
DMF_005t5e=buff(0,0)

class RandomPyroblast(TargetedAction):
	CONTROLLER = ActionArg()
	def do(self, source, controller):
		while True:
			x = random.choice([controller.hero,controller.opponent.hero])
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
>>>>>>> 048bb85c68c0bb4b687cd9e82f60bb17b1344375
	pass
