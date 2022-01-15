from ..utils import *


class SW_023:###OK <10>[1578]
	"""Provoke
	Tradeable: Choose a friendly minion. Enemy minions attack it."""
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0, 
		PlayReq.REQ_MINIMUM_ENEMY_MINIONS: 1,
		PlayReq.REQ_TARGET_TO_PLAY: 0, 
		PlayReq.REQ_FRIENDLY_TARGET: 0}
	def play(self):
		target = self.target
		for minion in self.controller.opponent.field:
			Attack(minion,target).trigger(self.controller)
	pass


class SCH_237_Choice(GenericChoice):## SCH_237
	def choose(self, card):
		super().choose(card)
		controller = self.player
		for handcard in controller.hand:
			if hasattr(handcard,'rush') and handcard.rush:
				Buff(handcard,'SCH_237e').trigger(controller)
		pass

class SCH_237:###OK
	"""Athletic Studies
	Discover a Rush minion. Your next one costs (1) less."""
	play = SCH_237_Choice(CONTROLLER, RandomMinion(rush=True)*3)
	pass


class SCH_237e:
	"""Athletic Studies
		Your next [Rush] minion costs (1) less."""
	cost = lambda self, i: max(i-1,0)
	events = Play(CONTROLLER, RUSH).on(Destroy(SELF))
	pass

class CORE_EX1_410: ###OK <- cards.core.warrior
	"""Shield Slam
	Deal 1 damage to a minion for each Armor you have."""
	requirements = {PlayReq.REQ_MINION_TARGET: 0,
					PlayReq.REQ_TARGET_TO_PLAY: 0}
	def play(self):
		controller = self.controller
		armor = controller.hero.armor
		Hit(self.target, armor).trigger(controller)
	pass


class BT_124:###OK
	"""Corsair Cache
	Draw a weapon. Give it +1 Durability."""
	play = ForceDraw(RANDOM(FRIENDLY_DECK + WEAPON)).then(
		Buff(ForceDraw.TARGET, "BT_124e"))
	pass
BT_124e = buff(health=1)


class DMF_522:###OK
	"""Minefield
	Deal 5 damage randomly split among all minions."""
	play = Hit(RANDOM_MINION, 1) * 5
	pass


class BT_117:###OK
	"""Bladestorm
	Deal 1 damage to all minions. Repeat until one dies."""
	def play(self):
		controller = self.controller
		game = controller.game
		before = game.board
		if len(game.board)>0:
			min=20
			for card in game.board:
				if card.health<min:
					min=card.health
			for card in game.board:
				Hit(card, min).trigger(controller)
		pass
	pass

class SW_094:###OK <10>[1578]
	"""Heavy Plate
	Tradeable: Gain 8 Armor."""
	play = GainArmor(FRIENDLY_HERO, 8)
	pass

class BT_781:###OK
	"""Bulwark of Azzinoth
	Whenever your hero would take damage, this loses 1 Durability instead.
	"""
	# see AT_124
	#update = Refresh(FRIENDLY_HERO, {GameTag.HEAVILY_ARMORED: True})
	events = Predamage(FRIENDLY_HERO).on(
		 Predamage(FRIENDLY_HERO, 0), Hit(SELF, 1))
	# BuffじゃなくてHit??
	pass


class BAR_845:###OK
	"""Rancor
	Deal 2 damage to all minions. Gain 2 Armor for each destroyed."""
	# 生の苦悩、ケルスザード校長らへんが参考になりそうだがわからん
	# これでよいなら・・・動いているような感じはある。
	#play = Hit(ALL_MINIONS, 2).then( Dead(ALL_MINIONS + Hit.TARGET) & GainArmor(FRIENDLY_HERO, 2))
	def play(self):
		controller = self.controller
		hero = controller.hero
		minionList = controller.game.board
		count = 0
		for card in minionList:
			if card.health<2:
				count+=1
		for card in minionList:
			Hit(card, 2).trigger(controller)
		GainArmor(hero, 2*count).trigger(controller)
	pass


class BAR_844:### excellent!
	"""Outrider's Axe
	After your hero attacks and kills a minion, draw a card."""
	events = Attack(FRIENDLY_HERO, ALL_MINIONS).after(
		Dead(ALL_MINIONS + Attack.DEFENDER) & Draw(CONTROLLER))
	pass


class YOP_005:###OK <12>[1466]
	"""Barricade
	Summon a 2/4 Guard with Taunt. If it's your only minion, summon another."""

	def play(self):
		controller = self.controller
		Summon(controller, "YOP_005t").trigger(controller)
		if len(controller.field) == 1:
			Summon(controller, "YOP_005t").trigger(controller)
	pass

class YOP_005t:#<12>[1466]
	"""Race Guard
	Taunt"""
	pass


class CORE_EX1_407:###OK
	"""Brawl
	Destroy all minions except one. (chosen randomly)"""
	requirements = {PlayReq.REQ_MINIMUM_TOTAL_MINIONS: 2}
	play = (
		Find(ALL_MINIONS + ALWAYS_WINS_BRAWLS) &
		Destroy(ALL_MINIONS - RANDOM(ALL_MINIONS + ALWAYS_WINS_BRAWLS)) |
		Destroy(ALL_MINIONS - RANDOM_MINION)#たぶんこれだけでよい、と思う。
	)
	pass


class SW_021:###OK <10>[1578]
	"""Cowardly Grunt
	Deathrattle: Summon a minion from your deck."""
	# CardDefsにdeathrattleタグがついていない
	play = SetTag(SELF, (GameTag.DEATHRATTLE, ))
	deathrattle = Summon(CONTROLLER, RANDOM(FRIENDLY_DECK+MINION))
	pass


#class SCH_533: #-> cards.scholo.paladin
#	"""Commencement
#	Summon a minion from your deck. Give it Taunt and Divine Shield."""
#	play = Summon(CONTROLLER, RANDOM(FRIENDLY_DECK+MINION)
#				  ).then(SetTag(Summon.CARD, (GameTag.DIVINE_SHIELD, GameTag.TAUNT)))
#	pass

class SW_024_Action(TargetedAction):
	TARGET = ActionArg()# 
	def do(self, source, target):
		controller = source.controller
		enemy = controller.opponent
		if len(enemy.field)==0:
			return
		deffender = random.choice(enemy.field)##
		Attack(source, deffender).trigger(controller)
		if deffender.health <= 0:
			Buff(source, 'SW_024e').trigger(controller)
		pass

class SW_024:###OK <10>[1578]
	"""Lothar
	At the end of your turn, attack a random enemy minion. If it dies, gain +3/+3."""
	events = OWN_TURN_END.on(SW_024_Action(SELF))
	#Attackは使い方が難しい。BAR_844のように、事象発生の条件として使われるほうがふつうなので。
	#events = OWN_TURN_END.on(Attack(SELF, RANDOM_ENEMY_MINION).then(
	#	Dead(Attack.DEFENDER) & Buff(SELF, "SW_024e")))
	pass
SW_024e = buff(atk=3, health=3)


class SCH_337_Troublemaker(TargetedAction):
	TARGET = ActionArg()
	def do(self, source, target):
		new_minion1 = Summon(target, "SCH_337t").trigger(source.controller)
		if new_minion1[0] != []:
			new_minion1 = new_minion1[0][0]
			new_minion2 = Summon(target, "SCH_337t").trigger(source.controller)
			if new_minion2[0] != []:
				new_minion2 = new_minion2[0][0]
				enemy = source.controller.opponent
				if len(enemy.field)>0:
					Attack(new_minion1, random.choice(enemy.field)).trigger(source.controller)##
					Attack(new_minion2, random.choice(enemy.field)).trigger(source.controller)##
		pass
class SCH_337:###OK
	"""Troublemaker
	At the end of your turn, summon two 3/3 Ruffians that attack random enemies."""
	events = OWN_TURN_END.on(SCH_337_Troublemaker(CONTROLLER))
	pass
class SCH_337t:
	pass

class SW_068:###OK
	"""Mo'arg Forgefiend
	Taunt Deathrattle: Gain 8 Armor."""
	deathrattle = GainArmor(FRIENDLY_HERO, 8)
	pass

class SCH_621_Action(TargetedAction):
	TARGET = ActionArg()
	CARD = ActionArg()
	def do(self, source, target):
		new_atk = source.atk - 1
		new_health = source.max_health - 1
		new_minion = Summon(target, source.id).trigger(source.controller)
		if new_minion[0] != []:
			new_minion = new_minion[0][0]
			new_minion.atk = new_atk
			new_minion.max_health = new_health
		pass

class SCH_621:###OK
	"""Rattlegore
	Deathrattle: Resummon this with -1/-1."""
	deathrattle = SCH_621_Action(CONTROLLER)
	#https://wiki.denfaminicogamer.jp/hearthstone/ラトルゴア_Rattlegore 
	# のメモに要注意
	#enchantmentがない！
	pass

