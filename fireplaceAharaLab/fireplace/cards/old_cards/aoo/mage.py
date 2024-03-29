from ..utils import *

#AOO_Mage=['BT_002','BT_002e','BT_003','BT_004','BT_006','BT_006e','BT_014','BT_021','BT_022','BT_028','BT_028t','BT_072','BT_291',]

##
# Minions

class BT_022:
	"""Apexis Smuggler"""
	events = Play(CONTROLLER, SECRET).after(DISCOVER(RandomSpell()))


class BT_014:
	"""Starscryer"""
	deathrattle = ForceDraw(RANDOM(FRIENDLY_DECK + SPELL))


class BT_028:
	"""Astromancer Solarian"""
	deathrattle = Shuffle(CONTROLLER, "BT_028t")

class CastSpellTargetsEnemiesIfPossible(TargetedAction):
	"""
	Cast a spell target random targets enemies if possible
	"""
	CARD = CardArg()

	def do(self, source, card):
		target = None
		if card.must_choose_one:
			card = random.choice(card.choose_cards)
		if card.requires_target():
			targets = card.targets
			if len(targets) > 0:
				enemy_targets = list(filter(
					lambda item: item.controller != source.controller, targets))
				if len(enemy_targets) > 0:
					target = random.choice(enemy_targets)
				else:
					target = random.choice(targets)
			else:
				if Config.LOGINFO:
					Config.log("CastSpellTargetsEnemiesIfPossible.do","%s cast spell %s don't have a legal target", source, card)
				return
		card.target = target
		if Config.LOGINFO:
			Config.log("CastSpellTargetsEnemiesIfPossible.do","%s cast spell %s target %s", source, card, target)
		source.game.queue_actions(source, [Battlecry(card, card.target)])
		player = source.controller
		while player.choice:
			choice = random.choice(player.choice.cards)
			print("Choosing card %r" % (choice))
			player.choice.choose(choice)
		source.game.queue_actions(source, [Deaths()])

class BT_028t:
	play = CastSpellTargetsEnemiesIfPossible(RandomSpell()) * 5


class BT_004:
	dormant = 2
	awaken = Hit(ENEMY_CHARACTERS, 2)


##
# Spells

class BT_006:
	"""Evocation
	Fill your hand with random Mage spells.At the end of your turn, discard them."""
	play = Give(CONTROLLER, RandomSpell(card_class=CardClass.MAGE)).then(
		Buff(Give.CARD, "BT_006e")) * MAX_HAND_SIZE(CONTROLLER)


class BT_006e:
	events = OWN_TURN_END.on(Discard(OWNER))


class BT_021:
	"""Font of Power
	[Discover] a Mage minion. If your deck has no minions, keep all 3. """
	powered_up = -Find(FRIENDLY_DECK + MINION)##-FindDuplicates(FRIENDLY_DECK)## 
	play = powered_up & (Give(CONTROLLER, RandomMinion(card_class=CardClass.MAGE)) * 3) | (
		DISCOVER(RandomMinion(card_class=CardClass.MAGE)))


class BT_002:
	"""Incanter's Flow"""
	play = Buff(FRIENDLY_DECK + SPELL, "BT_002e")


BT_002e = buff(cost=-1)


class BT_003:
	"""Netherwind Portal"""
	secret = Play(OPPONENT, SPELL).after(Summon(CONTROLLER, RandomMinion(cost=4)))


class BT_291:
	"""Apexis Blast"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	powered_up = -FindDuplicates(FRIENDLY_DECK)
	play = Hit(TARGET, 5), powered_up & Summon(CONTROLLER, RandomMinion(cost=5))


class BT_072:
	"""Deep Freeze"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Freeze(TARGET), Summon(CONTROLLER, "CORE_CS2_033") * 2
