# neutral in DMF
from ..utils import *

class YOP_032:
	"""Armor Vendor"""
	## <b>Battlecry:</b> Give 4 Armor to_each hero.
	play = (GainArmor(FRIENDLY_HERO,4),GainArmor(ENEMY_HERO,4))
	pass

class ShuffleLowestCostCard(TargetedAction):
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

class DMF_125:
	"""Safety Inspector"""
	##[x]&lt;b&gt;Battlecry:&lt;/b&gt; Shuffle the_lowest-Cost card from your hand into your deck. Draw a card.
	play = ShuffleLowestCostCard(CONTROLLER),Draw(CONTROLLER)
	pass
#ULD_706のようにかけるかも？

class DMF_189:
	"""Costumed Entertainer"""
	##[x]&lt;b&gt;Battlecry:&lt;/b&gt; Give a random minion in your hand +2/+2.
	play = Buff(RANDOM(FRIENDLY_HAND + MINION), "DMF_189e")
	pass
DMF_189e = buff(atk=2, health=2)

class YOP_031:
	"""Crabrider"""
	##[x]&lt;b&gt;Rush&lt;/b&gt; &lt;b&gt;Battlecry:&lt;/b&gt; Gain &lt;b&gt;Windfury&lt;/b&gt; this turn only.
	play = Buff(SELF, "YOP_031e")
	pass

class YOP_031e:
	windfury = SET(1)

class DMF_124:
	"""Horrendous Growth"""
	##&lt;b&gt;Corrupt:&lt;/b&gt; Gain +1/+1. Can be &lt;b&gt;Corrupted&lt;/b&gt; endlessly.
	pass

class DMF_520:
	"""Parade Leader"""
	##After you summon a &lt;b&gt;Rush&lt;/b&gt; minion, give it +2 Attack.
	events = Summon(CONTROLLER,rush=True).on(Buff(Summon.CARD,"dmf_520e"))
	pass
DMF_520e = buff(atk=2)

class DMF_067:
	"""Prize Vendor"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; Each player draws a card.
	play = Draw(CONTROLLER),Draw(OPPONENT)
	pass

class DMF_044:
	"""Rock Rager"""
	##&lt;b&gt;Taunt&lt;/b&gt;
	pass

class DMF_191:
	"""Showstopper"""
	##&lt;b&gt;Deathrattle:&lt;/b&gt; &lt;b&gt;Silence&lt;/b&gt; all_minions.
	deathrattle = Silence(ALL_MINIONS)
	pass

class DMF_091:
	"""Wriggling Horror"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; Give adjacent minions +1/+1.
	play = Buff(SELF_ADJACENT, "DMF_091e2")
	pass
DMF_091e2 = buff(atk=1,health=1)

class DMF_065:
	"""Banana Vendor"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; Add 2 Bananas to each player's hand.
	play = Give(CONTROLLER, "EX1_014t") * 2, Give(OPPONENT, "EX1_014t") * 2
	pass

class DMF_073:
	"""Darkmoon Dirigible"""
	##&lt;b&gt;Divine Shield&lt;/b&gt; &lt;b&gt;Corrupt:&lt;/b&gt; Gain &lt;b&gt;Rush&lt;/b&gt;.
	pass

class DMF_073t:
	"""Darkmoon Dirigible"""
	##&lt;b&gt;Corrupted&lt;/b&gt; &lt;b&gt;Rush&lt;/b&gt;, &lt;b&gt;Divine Shield&lt;/b&gt;
	pass

class DMF_082:
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

☆
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
	"""K'thir Ritualist"""
	##[x]&lt;b&gt;Taunt&lt;/b&gt; &lt;b&gt;Battlecry:&lt;/b&gt; Add a random 4-Cost minion to your opponent's hand.
	play = Give(OPPONENT, RandomMinion(cost=4))
	pass

class DMF_532:
	"""Circus Amalgam"""
	##&lt;b&gt;Taunt&lt;/b&gt; &lt;i&gt;This has all minion types.&lt;/i&gt;
	pass

class DMF_174:
	"""Circus Medic"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; Restore #4 Health. &lt;b&gt;Corrupt:&lt;/b&gt; Deal 4 damage instead.
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Heal(TARGET,4)
	pass

class DMF_174t:
	"""Circus Medic"""
	##&lt;b&gt;Corrupted&lt;/b&gt; &lt;b&gt;Battlecry:&lt;/b&gt; Deal 4 damage.
	requirements = {PlayReq.REQ_TARGET_IF_AVAILABLE: 0}
	play = Hit(TARGET,4)

	pass

class DMF_190:
	"""Fantastic Firebird"""
	##&lt;b&gt;Windfury&lt;/b&gt;
	pass

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

class YOP_035:
	"""Moonfang"""
	##Can only take 1 damage at_a time.
	tags = {GameTag.HEAVILY_ARMORED: True}
	pass

class DMF_068:
	"""Optimistic Ogre"""
	##50% chance to attack the correct enemy.
	events = FORGETFUL
	pass

class DMF_069:
	"""Claw Machine"""
	##&lt;b&gt;Rush&lt;/b&gt;. &lt;b&gt;Deathrattle:&lt;/b&gt; Draw a minion and give it +3/+3.
	play = ForceDraw(RANDOM(FRIENDLY_DECK + MINION)).then(
		Buff(ForceDraw.TARGET, "BT_213e"))
	pass
DMF_069e = buff(atk=3,health=3)
☆
class DMF_074:
	"""Silas Darkmoon"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; Choose a direction to rotate all minions.
	pass

class DMF_078:
	"""Strongman"""
	##&lt;b&gt;Taunt&lt;/b&gt; &lt;b&gt;Corrupt:&lt;/b&gt; This costs (0).
	pass

class DMF_078t:
	"""Strongman"""
	##&lt;b&gt;Corrupted&lt;/b&gt; &lt;b&gt;Taunt&lt;/b&gt;
	pass

class DMF_163:
	"""Carnival Clown"""
	##[x]&lt;b&gt;Taunt&lt;/b&gt; &lt;b&gt;Battlecry:&lt;/b&gt; Summon 2 copies of this. &lt;b&gt;Corrupt:&lt;/b&gt; Fill your board with copies.
	pass

class DMF_002:
	"""N'Zoth, God of the Deep"""
	##&lt;b&gt;Battlecry:&lt;/b&gt; Resurrect a friendly minion of each minion type.
	pass

class YOP_034:
	"""Runaway Blackwing"""
	##[x]At the end of your turn, deal 9 damage to a random enemy minion.
	pass

class DMF_254:
	"""C'Thun, the Shattered"""
	##[x]&lt;b&gt;Start of Game:&lt;/b&gt; Break into pieces. &lt;b&gt;Battlecry:&lt;/b&gt; Deal 30 damage randomly split among all enemies.
	pass

class DMF_:
	"""Darkmoon Rabbit"""
	##&lt;b&gt;Rush&lt;/b&gt;, &lt;b&gt;Poisonous&lt;/b&gt; Also damages the minions next to whomever this attacks.
	pass

class DMF_188:
	"""Y'Shaarj, the Defiler"""
	##[x]&lt;b&gt;Battlecry:&lt;/b&gt; Add a copy of each &lt;b&gt;Corrupted&lt;/b&gt; card you've played this game to your hand. They cost (0) this turn.
	pass

class DMF_004:
	"""Yogg-Saron, Master of Fate"""
	##[x]&lt;b&gt;Battlecry:&lt;/b&gt; If you've cast 10 spells this game, spin the Wheel of Yogg-Saron.@ &lt;i&gt;({0} left!)&lt;/i&gt;@ &lt;i&gt;(Ready!)&lt;/i&gt;
	pass

	