from ..utils import *

AOO_Warrior=['BT_120','BT_121','BT_123','BT_123t',
'BT_138','BT_140','BT_233','BT_249',]
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

class BT_120:# <10>[1414]
	""" Warmaul Challenger
	[Battlecry:] Choose an enemy minion.Battle it to the death! """
	requirements = { PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0 }#
	pass

class BT_121:# <10>[1414] #### Find a 3/2 Axe
	""" Imprisoned Gan'arg
	[Dormant] for 2 turns.When this awakens,equip a 3/2 Axe. """
	#
	pass

class BT_123:# <10>[1414] ## BT_123t
	""" Kargath Bladefist
	[Rush][Deathrattle:] Shuffle'Kargath Prime'into your deck. """
	#
	pass

class BT_123t:# <10>[1414]
	""" Kargath Prime
	[Rush]. Whenever this attacks and kills a minion, gain 10 Armor. """
	#
	pass

#class BT_124:###OK
#	"""Corsair Cache
#	Draw a weapon. Give it +1 Durability."""
#	play = ForceDraw(RANDOM(FRIENDLY_DECK + WEAPON)).then(
#		Buff(ForceDraw.TARGET, "BT_124e"))
#	pass
#BT_124e = buff(health=1)


class BT_138:# <10>[1414] # no enchantment
	""" Bloodboil Brute
	[Rush]Costs (1) less for each damaged minion. """
	#
	pass

class BT_140:# <10>[1414]
	""" Bonechewer Raider
	[Battlecry:] If there is a damaged minion, gain +1/+1 and [Rush]. """
	#
	pass

class BT_233:# <10>[1414]
	""" Sword and Board
	Deal $2 damage to a minion. Gain 2 Armor. """
	requirements = { PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0 }#
	#
	pass

class BT_249:# <10>[1414]
	""" Scrap Golem
	[Taunt]. [Deathrattle]: Gain Armor equal to this minion's Attack. """
	#
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
