from ..utils import *

Lich_Rogue=[]

Lich_Rotten_Rodent=True
Lich_Scourge_Illusionist=True
Lich_Noxious_Infiltrator=True
Lich_Shadow_of_Demise=True
Lich_Concoctor=True
Lich_Potion_Belt=True
Lich_Ghoulish_Alchemist=True
Lich_Vile_Apothecary=True
Lich_Potionmaster_Putricide=True
Lich_Ghostly_Strike=True


if Lich_Rotten_Rodent:# 
	Lich_Rogue+=['RLK_216']
	Lich_Rogue+=['RLK_216e']
class RLK_216_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		for card in controller.deck:
			if card.type==CardType.MINION and card.has_deathrattle==True:
				Buff(card, 'RLK_216e').trigger(source)
		pass
class RLK_216:# <7>[1776]
	""" Rotten Rodent (minion:2/2/1)
	<b>Battlecry:</b> Reduce the Cost of all <b>Deathrattle</b> cards in your deck by (1). """
	play = RLK_216_Action()
	pass
class RLK_216e:# <7>[1776]
	""" Rotten (0) 	Costs (1) less. """
	cost = lambda self, i:max(i-1,0)
	pass


if Lich_Scourge_Illusionist:# 
	Lich_Rogue+=['RLK_217']
	Lich_Rogue+=['RLK_217e']
	Lich_Rogue+=['RLK_217e2']
class RLK_217_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		cards=[card for card in controller.deck if getattr(card, 'has_deathrattle', False)==True]
		if len(cards):
			card = random.choice(cards)
			Buff(card, 'RLK_217e').trigger(source)
			Buff(card, 'RLK_217e2').trigger(source)
		pass
class RLK_217:# <7>[1776]
	""" Scourge Illusionist (minion:4/4/4)
	<b>Deathrattle:</b> Add a 4/4 copy of another <b>Deathrattle</b> minion in your deck to your hand. It costs (4) less. """
	deathrattle = RLK_217_Action()
	pass
RLK_217e=buff(4,4)
class RLK_217e2:# <7>[1776]
	""" Illusory (0)
	Costs (4) less. """
	cost = lambda self, i:max(i-4,0)	
	pass


if Lich_Noxious_Infiltrator:# 
	Lich_Rogue+=['RLK_529']
class RLK_529_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		cards = [card for card in controller.death_until_last_turn if card.type==CardType.MINION and card.race==Race.UNDEAD]
		targets = [target for target in controller.opponent.field]
		if len(cards) and len(targets):
			target=random.choice(targets)
			Hit(target, 1).trigger(source)
		pass
class RLK_529:# <7>[1776]
	""" Noxious Infiltrator (minion:4/2/5)
	<b>Poisonous</b> <b>Battlecry:</b> If a friendly Undead died after your last turn, deal 1 damage to a minion. """
	play = RLK_529_Action()
	pass


if Lich_Shadow_of_Demise:# 
	Lich_Rogue+=['RLK_567']
	Lich_Rogue+=['RLK_567e']
	Lich_Rogue+=['RLK_567e2']
class RLK_567_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_567:# <7>[1776]
	""" Shadow of Demise (spell:0)
	Each time you cast a spell, transform this into a copy of it. """
	class HAND:
		events = Play(CONTROLLER, SPELL).on(Morph(SELF, Play.CARD))
	pass
class RLK_567e:# <7>[1776]
	""" Death's Reflection (0)
	Always copy your last played card. """
	pass
class RLK_567e2:# <7>[1776]
	""" Shadow of Death (0)
	Transforming into recent spells. """
	pass


if Lich_Concoctor:# 
	Lich_Rogue+=['RLK_568']
class RLK_568_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		cards=['RLK_570t', 'RLK_570t1', 'RLK_570t2', 'RLK_570t3', 'RLK_570t4', 'RLK_570t5']
		card = random.choice(cards)
		Give(controller, card).trigger(source)
		pass
class RLK_568:# <7>[1776]
	""" Concoctor (minion:1/1/2)
	<b>Battlecry:</b> Add a random Concoction to your hand. """
	play = RLK_568_Action()
	pass

if Lich_Potion_Belt:# 
	Lich_Rogue+=['RLK_569']
class RLK_569_Choice(Choice):# 
	def choose(self, card):# 
		source=self.source
		source.script_data_num_1 += 1
		if source.script_data_num_1==1:
			self.next_choice=self
			super().choose(card)
			card.zone=Zone.HAND
		else:
			self.next_choice=None
			super().choose(card)
			card.zone=Zone.HAND
		pass
class RLK_569:# <7>[1776]
	""" Potion Belt (spell:2)
	<b>Discover</b> 2 Concoctions. """
	play = RLK_569_Choice(CONTROLLER, RandomID('RLK_570t', 'RLK_570t1', 'RLK_570t2', 'RLK_570t3', 'RLK_570t4', 'RLK_570t5')*3)
	pass

if Lich_Ghoulish_Alchemist:# 
	Lich_Rogue+=['RLK_570','RLK_570e','RLK_570e3','RLK_570e4']
	Lich_Rogue+=['RLK_570t', 'RLK_570tt1', 'RLK_570tt2', 'RLK_570tt3', 'RLK_570tt4', 'RLK_570tt5']
	Lich_Rogue+=['RLK_570t1', 'RLK_570t1t', 'RLK_570t1t1', 'RLK_570t1t2', 'RLK_570t1t3', 'RLK_570t1t4']
	Lich_Rogue+=['RLK_570t2', 'RLK_570t2e', 'RLK_570t2t1', 'RLK_570t2t2']
	Lich_Rogue+=['RLK_570t3', 'RLK_570t3t']
	Lich_Rogue+=['RLK_570t4', 'RLK_570t4t1', 'RLK_570t4t2', 'RLK_570t4t3']
	Lich_Rogue+=['RLK_570t5']
class RLK_570:# <7>[1776]
	""" Ghoulish Alchemist (minion:2/3/2)
	<b>Battlecry</b>: Your next Concoction costs (0). """
	play = Buff(FRIENDLY_HAND + CONCOCTION, 'RLK_570e4')
	pass
RLK_570e=buff(2,0)
class RLK_570e3:# <7>[1776]
	""" Blue Spirit (0)
	Costs (3) less. """
	cost=lambda self, i:max(0, i-3)
	pass
class RLK_570e4:# <7>[1776]
	""" Doctored (0)
	Your next Concoction costs (0). """
	cost = SET(0)
	events = [
		OWN_TURN_END.on(Destroy(SELF)),
		Play(CONTROLLER, SPELL+CONCOCTION).on(Destroy(SELF))
	]
	pass
class RLK_570t:# <7>[1776]
	""" Mixed Potion (spell:3)
	 """
	pass
class RLK_570t1:# <7>[1776]
	""" Slimy Concoction (spell:3)
	Summon a random 3-Cost minion. <i>Add another Concoction to your hand to mix together!</i> """
	play = Summon(CONTROLLER, RandomMinion(cost=3))
	pass
class RLK_570t1t:# <7>[1776]
	""" Orange Slime (minion:3/3/4)
	 """
	pass
class RLK_570t1t1_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		the_class=random.choice(CLASSES_EXCEPT_ROGUE)
		newcard=get00(RandomCollectible(card_class=the_class).evaluate(source))
		Buff(newcard, 'RLK_570e3').trigger(source)
		newcard.zone=Zone.HAND
		pass
class RLK_570t1t1:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Summon a random 3-Cost minion. Add a card to your hand from another class. It costs (3) less. """
	play = Summon(CONTROLLER, RandomMinion(cost=3)),RLK_570t1t1_Action()
	pass
class RLK_570t1t2:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Summon a random 3-Cost minion. Destroy a random enemy minion. """
	play = Summon(CONTROLLER, RandomMinion(cost=3)), Destroy(RANDOM(ENEMY_MINIONS))
	pass
class RLK_570t1t3:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Deal $3 damage. Summon a random 3-Cost minion. """
	play = Hit(ENEMY_HERO, 3), Summon(CONTROLLER, RandomMinion(cost=3)) 
	pass
class RLK_570t1t4:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Summon two random 3-Cost minions. """
	play = Summon(CONTROLLER, RandomMinion(cost=3)), Summon(CONTROLLER, RandomMinion(cost=3))
	pass
class RLK_570t2:# <7>[1776]
	""" Dreadful Concoction (spell:3)
	Destroy a random enemy minion. <i>Add another Concoction to your hand to mix together!</i> """
	play = Destroy(RANDOM(ENEMY_MINIONS))
	pass
class RLK_570t2e:# <7>[1776]
	""" Green Potion (0)
	<b>Poisonous</b> and <b>Reborn</b>. """
	#
	pass
class RLK_570t2t1:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Deal $3 damage. Destroy a random enemy minion. """
	play = Hit(ENEMY_HERO, 3), Destroy(RANDOM(ENEMY_MINIONS))
	pass
class RLK_570t2t2:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Destroy two random enemy minions. """
	play = Destroy(RANDOM(ENEMY_MINIONS)), Destroy(RANDOM(ENEMY_MINIONS))
	pass
class RLK_570t3:# <7>[1776]
	""" Bubbling Concoction (spell:3)
	Deal $3 damage. <i>Add another Concoction to your hand to mix together!</i> """
	play = Hit(ENEMY_HERO, 3)
	pass
class RLK_570t3t:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Deal $3 damage, twice. """
	play = Hit(ENEMY_HERO, 3), Hit(ENEMY_HERO, 3)
	pass
class RLK_570t4:# <7>[1776]
	""" Hazy Concoction (spell:3)
	Add a card to your hand from another class. It costs (3) less. <i>Add another Concoction to your hand to mix together!</i> """
	play = RLK_570t1t1_Action()
	pass

class RLK_570t4t1_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570t4t1:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Add a card to your hand from another class. It costs (3) less. Destroy a random enemy minion. """
	play = RLK_570t1t1_Action(), Destroy(RANDOM(ENEMY_MINIONS))
	pass
class RLK_570t4t2:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Deal $3 damage. Add a card to your hand from another class. It costs (3) less. """
	play = Hit(ENEMY_HERO, 3), RLK_570t1t1_Action()
	pass
class RLK_570t4t3:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Add two cards to your hand from another class. They cost (3) less. """
	play = RLK_570t1t1_Action(), RLK_570t1t1_Action()
	pass
class RLK_570t5:# <7>[1776]
	""" Gleaming Concoction (spell:3)
	Draw 2 cards. <i>Add another Concoction to your hand to mix together!</i> """
	play = Draw(CONTROLLER), Draw(CONTROLLER)
	pass
class RLK_570tt1:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Draw 2 cards. Summon a random 3-Cost minion. """
	play = Draw(CONTROLLER), Draw(CONTROLLER), Summon(CONTROLLER, RandomMinion(cost=3))
	pass
class RLK_570tt2:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Deal $3 damage. Draw 2 cards. """
	play = Hit(ENEMY_HERO, 3), Draw(CONTROLLER), Draw(CONTROLLER)
	pass

class RLK_570tt3_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_570tt3:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Draw 2 cards. Add a card to your hand from another class. It costs (3) less. """
	play = Draw(CONTROLLER), Draw(CONTROLLER), RLK_570t1t1_Action()
	pass
class RLK_570tt4:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Draw 2 cards. Destroy a random enemy minion. """
	play = Draw(CONTROLLER), Draw(CONTROLLER), Destroy(RANDOM(ENEMY_MINIONS))
	pass
class RLK_570tt5:# <7>[1776]
	""" Mixed Concoction (spell:3)
	Draw 4 cards. """
	play = Draw(CONTROLLER), Draw(CONTROLLER), Draw(CONTROLLER), Draw(CONTROLLER),
	pass

if Lich_Vile_Apothecary:# 
	Lich_Rogue+=['RLK_571']
class RLK_571_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_571:# <7>[1776]
	""" Vile Apothecary (minion:3/2/4)
	At the end of your turn, add a random Concoction to your hand. """
	#
	pass

if Lich_Potionmaster_Putricide:# 
	Lich_Rogue+=['RLK_572']
class RLK_572_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_572:# <7>[1776]
	""" Potionmaster Putricide (minion:2/1/4)
	After a minion dies, add a Concoction to your hand. """
	#
	pass

if Lich_Ghostly_Strike:# 
	Lich_Rogue+=['RLK_573']
class RLK_573_Action(GameAction):# 
	def do(self, source):# 
		controller=source.controller
		pass
class RLK_573:# <7>[1776]
	""" Ghostly Strike (spell:1)
	Deal $1 damage. <b>Combo:</b> Draw a card. """
	#
	pass

