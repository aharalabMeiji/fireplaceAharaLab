from ..utils import *

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


