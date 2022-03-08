from ..utils import *

#Alterac_Warlock=['AV_277','AV_281','AV_285','AV_286','AV_286e2','AV_308','AV_312','AV_313','AV_313e','AV_316','AV_316hp','AV_316t','AV_316t4','AV_317','AV_317e','AV_657','AV_657e','AV_657t',]
#Alterac_Warlock+= ['ONY_033','ONY_034','ONY_034t','ONY_035',]

class AV_277:# <9>[1626]
	""" Seeds of Destruction
	Shuffle four Riftsinto your deck. Theysummon a 3/3 DreadImp when drawn. """
	#
	pass

class AV_281:# <9>[1626]
	""" Felfire in the Hole!
	Draw a spell and deal $2 damage to all enemies. If it's a Fel spell, deal $1 more. """
	#
	pass

class AV_285:# <9>[1626]
	""" Full-Blown Evil
	Deal $5 damage randomly split amongall enemy minions. Repeatable this turn. """
	#
	pass

class AV_286:# <9>[1626]
	""" Felwalker
	[Taunt]. [Battlecry]: Cast the highest Cost Fel spell from your hand. """
	#
	pass

class AV_286e2:# <9>[1626]
	""" Felgorged
	+1/+1. """
	#
	pass

class AV_308:# <9>[1626]
	""" Grave Defiler
	[Battlecry:] Copy a Fel spell in your hand. """
	#
	pass

class AV_312:# <9>[1626]
	""" Sacrificial Summoner
	[Battlecry:] Destroy a friendly minion. Summon a minion from your deck that costs (1) more. """
	#
	pass

class AV_313:# <9>[1626]
	""" Hollow Abomination
	[Battlecry:] Deal 1 damage toall enemy minions.[Honorable Kill:] Gain theminion's Attack. """
	#
	pass

class AV_313e:# <9>[1626]
	""" Consumed
	Increased attack. """
	#
	pass

class AV_316:# <9>[1626]
	""" Dreadlich Tamsin
	[Battlecry:] Deal 3 damageto all minions. Shuffle 3Rifts into your deck.Draw 3 cards. """
	#
	pass

class AV_316hp:# <9>[1626]
	""" Chains of Dread
	[Hero Power]Shuffle a Rift into your deck. Draw a card. """
	#
	pass

class AV_316t:# <9>[1626]
	""" Dread Imp
	 """
	#
	pass

class AV_316t4:# <9>[1626]
	""" Fel Rift
	[Casts When Drawn]Summon a 3/3 Dread Imp. """
	#
	pass

class AV_317:# <9>[1626]
	""" Tamsin's Phylactery
	[Discover] a friendly [Deathrattle] minion that died this game. Give your minions its [Deathrattle]. """
	#
	pass

class AV_317e:# <9>[1626]
	""" Lich Perfume
	Copied [Deathrattle] from {0}. """
	#
	pass

class AV_657:# <9>[1626]
	""" Desecrated Graveyard
	At the end of your turn,destroy your lowest Attackminion to summon a4/4 Shade. Lasts 3 turns. """
	#
	pass

class AV_657e:# <9>[1626]
	""" Sacrificing
	Sacrifice this at end of turn. """
	#
	pass

class AV_657t:# <9>[1626]
	""" Desecrated Shade
	 """
	#
	pass



class ONY_033:# <9>[1626]
	""" Impfestation
	Summon a 3/3Dread Imp to attack each enemy minion. """
	#
	pass

class ONY_034:# <9>[1626]
	""" Curse of Agony
	Shuffle three Agoniesinto the opponent's deck.They deal Fatigue damagewhen drawn. """
	#
	pass

class ONY_034t:# <9>[1626]
	""" Agony
	[Casts When Drawn]Take @ Fatigue damage. """
	#
	pass

class ONY_035:# <9>[1626]
	""" Spawn of Deathwing
	[Battlecry:] Destroy a random enemy minion. Discard a random card. """
	#
	pass

class ALT_WLK_1:
	""" Felwalker (6/3/7) Demon
	Taunt. Battlecry: Cast the highest Cost Fel spell from your hand."""
	def play(self):
		controller = self.controller
		hand = controller.hand
		highestcost=[]
		if hand!=[]:
			for card in hand:
				if card.card_school==CardSchool.FEL:
					if highestcost==[]:
						highestcost=[card]
					elif highestcost[0].cost<card.cost:
						highestcost=[card]
					elif highestcost[0].cost==card.cost:
						highestcost.append(card)
			if highestcost != []:
				card = random.choice(highestcost)
				controller.game.trigger(controller,[Play(card,None,None,None)], event_args=None)
			pass
		pass
	pass

class ALT_WLK_2:
	""" Desecrated Graveyard (3)
	At the end of your turn, destroy your lowest Attack minion to summon a 4/4 Shade. Lasts 3 turns."""
	events=[
		OWN_TURN_END.on(Destroy(RANDOM(LOWEST_ATK(FRIENDLY_MINION))), Summon(CONTROLLER, 'ALT_WLK_2t')),
		OWN_TURN_BEGIN.on(SidequestCounter(CONTROLLER,3,[Destroy(SELF)]))
	]
	pass
class ALT_WLK_2t:
	"""  """
	pass

class ALT_WLK_3:#  'repeatable' is to be allowed to play the same card again within the turn
	""" Full-Blown Evil (3) Fel
	Deal 5 damage randomly split among all enemy minions. Repeatable this turn. """
	play = (
		Hit(RANDOM(ENEMY_MINIONS),1) * 5,
		Give(CONTROLLER, 'ALT_WLK_3')
		)
	events = OWN_TURN_END.on(Destroy(SELF))
	pass

class ALT_WLK_4:
	""" rave Defiler (1/2/1)
	Battlecry: Copy a Fel spell in your hand. """
	play = Give(CONTROLLER, ExactCopy(RANDOM(FRIENDLY_HAND + FEL)))
	pass

class ALT_WLK_5:
	""" Seeds of Destruction (2) Fel
	Shuffle four Rifts into your deck. They summon a 3/3 Dread Imp when drawn. """
	pass

class ALT_WLK_6:
	""" Felfire in the Hole! (5) Fel
	Draw a spell and deal 2 damage to all enemies. If it's a Fel spell, deal 1 more. """
	pass

class ALT_WLK_7:
	""" Sacrificial Summoner (3/3/3)
	Battlecry: Destroy a friendly minion. Summon a minion from your deck that costs (1) more. """
	pass

class ALT_WLK_8:
	""" Tamsin's Phylactery (4) Shadow
	Discover a friendly Deathrattle minion that died this game. Give your minions its Deathrattle. """
	pass

class ALT_WLK_9:
	""" Dreadlich Tamsin (6/*/5) Hero
	Battlecry: Deal 3 damage to all minions. Shuffle 3 Rifts into your deck. Draw 3 cards. """
	play = (
		Hit(ENEMY_MINIONS, 3),
		Shuffle(CONTROLLER, 'ALT_WLK_9t') * 3,
		Draw(CONTROLLER) * 3
		)
	pass
class ALT_WLK_9t:
	"""   """
	pass

class ALT_WLK_10:
	""" Hollow Abomination (5/2/8)
	Battlecry: Deal 1 damage to all enemy minions. Honorable Kill: Gain the minion's Attack."""
	play = Hit(ENEMY_MINIONS, 1)
	#honorable_kill = 
	pass


