from ..utils import *

AOO_Warrior=['BT_120','BT_121','BT_123','BT_123t',
'BT_138','BT_140','BT_140e','BT_233','BT_249',]
#bigWarrior:'BT_117','BT_124','BT_124e','BT_781',

#'BTA_BOSS_04h','BTA_BOSS_04s','BTA_BOSS_06h',
#'BTA_BOSS_08h','BTA_BOSS_08p','BTA_BOSS_11p','BTA_BOSS_12t',
#'BTA_BOSS_14h2','BTA_BOSS_14p2','BTA_BOSS_23p',
#'Prologue_Azzinoth','Story_09_BonechewerRaider',]

#class BT_117:# <10>[1414]
#	""" Bladestorm
#	Deal $1 damage to all minions. Repeat until one dies. """
#    def play(self):
#        controller = self.controller
#        game = controller.game
#        before = game.board
#        for i in range(100):# 1000? lol
#            if len(game.board)>0:
#                for card in game.board:
#                    Hit(card, 1).trigger(controller)
#                for card in game.board:
#                    if card.health == 0:
#                        return
#            else:
#                return
#        pass
#    pass

class BT_120:#OK  <10>[1414]
	""" Warmaul Challenger
	[Battlecry:] Choose an enemy minion.Battle it to the death! """
	requirements = { 
		PlayReq.REQ_TARGET_TO_PLAY:0, 
		PlayReq.REQ_MINION_TARGET:0,
		PlayReq.REQ_ENEMY_TARGET:0
		}#
	def play(self):
		controller=self.controller
		target = self.target
		for repeat in range(100):
			Hit(target, self.atk).trigger(controller)
			Hit(self, target.atk).trigger(controller.opponent)
			if self.health==0 or target.health==0:
				return
		pass
	pass

class BT_121:#OK <10>[1414] #### Find a 3/2 Axe
	""" Imprisoned Gan'arg
	[Dormant] for 2 turns.When this awakens,equip a 3/2 Axe. """
	dormant = 2
	awaken = Summon(CONTROLLER, 'CORE_CS2_106')
	pass

class BT_123:# <10>[1414] ## BT_123t
	""" Kargath Bladefist
	[Rush][Deathrattle:] Shuffle'Kargath Prime'into your deck. """
	deathrattle = Shuffle(CONTROLLER, 'BT_123t')
	pass

class BT_123t:#OK <10>[1414]#
	""" Kargath Prime
	[Rush]. Whenever this attacks and kills a minion, gain 10 Armor. """
	events = Attack(SELF, ENEMY_MINIONS).after(Dead(ALL_MINIONS + Attack.DEFENDER) &GainArmor(FRIENDLY_HERO, 10))
	#
	#BT_123t_Action(Attack.DEFENDER)
	pass

#class BT_124:###OK
#	"""Corsair Cache
#	Draw a weapon. Give it +1 Durability."""
#	play = ForceDraw(RANDOM(FRIENDLY_DECK + WEAPON)).then(
#		Buff(ForceDraw.TARGET, "BT_124e"))
#	pass
#BT_124e = buff(health=1)


class BT_138:#OK <10>[1414] # no enchantment
	""" Bloodboil Brute
	[Rush]Costs (1) less for each damaged minion. """
	cost_mod = -Count(FRIENDLY_MINIONS + DAMAGED)
	pass

class BT_140:#OK <10>[1414]
	""" Bonechewer Raider
	[Battlecry:] If there is a damaged minion, gain +1/+1 and [Rush]. """
	play = Find(FRIENDLY_MINIONS + DAMAGED) & BuffOnce(SELF, 'BT_140e')
	pass
BT_140e=buff(atk=1, health=1, rush=True)#<12>[1414]

class BT_233:#OK <10>[1414]
	""" Sword and Board
	Deal $2 damage to a minion. Gain 2 Armor. """
	requirements = { PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0 }#
	play = Hit(TARGET, 2), GainArmor(FRIENDLY_HERO, 2)
	#
	pass

class BT_249:#OK <10>[1414]
	""" Scrap Golem
	[Taunt]. [Deathrattle]: Gain Armor equal to this minion's Attack. """
	deathrattle = GainArmor(FRIENDLY_HERO, ATK(SELF))
	pass

#class BT_781:###OK
#	"""Bulwark of Azzinoth
#	Whenever your hero would take damage, this loses 1 Durability instead.
#	"""
#	# see AT_124
#	#update = Refresh(FRIENDLY_HERO, {GameTag.HEAVILY_ARMORED: True})
#	events = Predamage(FRIENDLY_HERO).on(
#		 Predamage(FRIENDLY_HERO, 0), Hit(SELF, 1))
#	# BuffじゃなくてHit??
#	pass
