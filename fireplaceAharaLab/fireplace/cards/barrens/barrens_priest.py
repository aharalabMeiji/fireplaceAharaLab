
from ..utils import *

Barrens_Priest=[]

Barrens_Void_Flayer=True  ###
Barrens_Power_Word_Fortitude=True  ###
Barrens_Desperate_Prayer=True  ###
Barrens_Lightshower_Elemental=True  ###
Barrens_Devouring_Plague=True  ###
Barrens_Soothsayers_Caravan=True  ###
Barrens_Priest_of_Anshe=True  ###
Barrens_Suns_Strength=True
Barrens_Condemn_Rank_1=True  ###
Barrens_Serena_Bloodfeather=True  ###
Barrens_Xyrella=True  ###
Barrens_Devout_Dungeoneer=True  ###
Barrens_Against_All_Odds=True  ###
Barrens_Cleric_of_Anshe=True  ###

#################################################

if Barrens_Void_Flayer:# 
	Barrens_Priest+=['BAR_307']
class BAR_307:# <6>[1525]
	""" Void Flayer
	[Battlecry:] For each spell in your hand, deal 1 damage to a random enemy minion. """
	play = Hit(RANDOM(ENEMY_MINIONS),1) * Count(FRIENDLY_HAND + SPELL)
	pass




if Barrens_Power_Word_Fortitude:# 
	Barrens_Priest+=['BAR_308']
class BAR_308:# <6>[1525]
	""" Power Word: Fortitude
	Give a minion +3/+5. Costs (1) less for each spell in your hand. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, }
	def play(self):
		amount = -len([card for card in self.controller.hand if card.type==CardType.SPELL])
		Buff(self.target, 'BAR_308e', cost = amount).trigger(self)
	pass
@custom_card
class BAR_308e:
	tags={
		GameTag.CARDNAME:'Power Word: Fortitude',
		GameTag.CARDTYPE:CardType.ENCHANTMENT,
		GameTag.ATK:3,
		GameTag.HEALTH:5
		}



if Barrens_Desperate_Prayer:# 
	Barrens_Priest+=['BAR_309']
class BAR_309:# <6>[1525]
	""" Desperate Prayer
	Restore #5 Health to each hero. """
	play = Heal(FRIENDLY_HERO,5), Heal(ENEMY_HERO,5)
	pass




if Barrens_Lightshower_Elemental:# 
	Barrens_Priest+=['BAR_310']
class BAR_310:# <6>[1525]
	""" Lightshower Elemental
	[Taunt][Deathrattle:] Restore #8 Healthto all friendly characters. """
	deathrattle = Heal(FRIENDLY_CHARACTERS, 8)
	pass




if Barrens_Devouring_Plague:# 
	Barrens_Priest+=['BAR_311']
class BAR_311:# <6>[1525]
	""" Devouring Plague
	[Lifesteal]. Deal $4 damagerandomly split amongall enemy minions. """
	play = Hit(RANDOM(ENEMY_MINIONS),1) * 4
	pass




if Barrens_Soothsayers_Caravan:# 
	Barrens_Priest+=['BAR_312']
class BAR_312:# <6>[1525]
	""" Soothsayer's Caravan
	At the start of your turn, copy a spell from your opponent's deck to your hand. """
	events = OWN_TURN_BEGIN.on(Give(CONTROLLER, RANDOM(ENEMY_DECK)))
	pass




if Barrens_Priest_of_Anshe:# 
	Barrens_Priest+=['BAR_313']
	Barrens_Priest+=['BAR_313e']
class BAR_313:# <6>[1525]
	""" Priest of An'she
	[Taunt]. [Battlecry:] If you've restored Health this turn, gain +3/+3. """
	def plat(self):
		#this turn
		actions=[action for action in self.controller._targetedaction_log
		   if isinstance(action['class'],Heal) and action['turn']==self.controller.game.turn]
		if len(actions)>0:
			Buff(self, 'BAR_313e').trigger(self)
	pass
class BAR_313e:# <6>[1525]
	""" Sun's Strength 	+3/+3. """
	tags ={
		GameTag.ATK:3,
		GameTag.HEALTH:3
		}
	pass




if Barrens_Condemn_Rank_1:# 
	Barrens_Priest+=['BAR_314']
	Barrens_Priest+=['BAR_314t']
	Barrens_Priest+=['BAR_314t2']
class BAR_314:# <6>[1525]
	""" Condemn (Rank 1)
	Deal $1 damage toall enemy minions.<i>(Upgrades when youhave 5 Mana.)</i> """
	class Hand:
		events = GradeupByMana(CONTROLLER, 5).on(Destroy(SELF),Give(CONTROLLER, 'BAR_314t'))	
	play = Hit(ENEMY_MINIONS, 1)
	pass
class BAR_314t:# <6>[1525]
	""" Condemn (Rank 2)
	Deal $2 damage toall enemy minions.<i>(Upgrades when youhave 10 Mana.)</i> """
	class Hand:
		events = GradeupByMana(CONTROLLER, 10).on(Destroy(SELF),Give(CONTROLLER, 'BAR_314t2'))	
	play = Hit(ENEMY_MINIONS, 2)
	pass
class BAR_314t2:# <6>[1525]
	""" Condemn (Rank 3)
	Deal $3 damage to all enemy minions. """
	play = Hit(ENEMY_MINIONS, 3)
	pass




if Barrens_Serena_Bloodfeather:# 
	Barrens_Priest+=['BAR_315']
class BAR_315:# <6>[1525]
	""" Serena Bloodfeather
	[Battlecry:] Choose an enemy minion. Steal Attack and Health from it until this has more. """
	requirements = {PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_ENEMY_TARGET:0, PlayReq.REQ_MINION_TARGET:0,  }
	def play(self):
		controller = self.controller
		target = self.target
		Buff(self, 'BAR_315e', atk=target.atk, max_health=target.max_health).trigger(self)
	pass
@custom_card
class BAR_315e:
	tags={
		GameTag.CARDNAME:'Serena Bloodfeather',
		GameTag.CARDTYPE:CardType.ENCHANTMENT,
	}
	events = Buff(OWNER).on(Destroy(SELF))
	pass



if Barrens_Xyrella:# 
	Barrens_Priest+=['BAR_735']
class BAR_735:# <6>[1525]
	""" Xyrella
	[Battlecry:] If you've restored Health this turn, deal that much damage to all enemy minions. """
	def plat(self):
		#this turn
		actions=[action for action in self.controller._targetedaction_log if isinstance(action['class'],Heal) and action['turn']==self.controller.game.turn]
		if len(actions)>0:
			for action in actions:
				Hit(ENEMY_MINIONS, action['target_arg'][0]).trigger(self)
	pass




if Barrens_Devout_Dungeoneer:# 
	Barrens_Priest+=['WC_013']
class WC_013:# <6>[1525]
	""" Devout Dungeoneer
	[Battlecry:] Draw a spell.If it's a Holy spell,reduce its Cost by (2). """
	def play(self):
		cards = [card for card in self.controller.deck if card.type==CardType.SPELL]
		if len(cards)>0:
			card = random.choice(cards)
			Give(self.controller, card).trigger(self)
			if card.SPELL_SCHOOL(SpellSchool.HOLY):
				Buff(card, 'WC_013e').trigger(self)
	pass
@custom_card
class WC_013e:
	tags={
		GameTag.CARDNAME:"I",
		GameTag.CARDTYPE:CardType.ENCHANTMENT,
		GameTag.COST:-1,}




if Barrens_Against_All_Odds:# 
	Barrens_Priest+=['WC_014']
class WC_014:# <6>[1525]
	""" Against All Odds
	Destroy ALL odd-Attack minions. """
	def play(self):
		cards = [card for card in self.controller.field if card.type==CardType.MINION and card.atk%2==1]
		cards += [card for card in self.controller.opponent.field if card.type==CardType.MINION and card.atk%2==1]
		amount=len(cards)
		for i in range(amount):
			Destroy(cards[-1]).trigger(self)
	pass




if Barrens_Cleric_of_Anshe:# 
	Barrens_Priest+=['WC_803']
class WC_803_Choice(Choice):
	def choose(self, card):
		self.next_choice=None
		super().choose(card)
		controller = card.controller
		for c in controller.deck:
			if card.id==c.id:
				controller.deck.remove(c)
				c.zone=Zone.HAND
				break
		pass

class WC_803:# <6>[1525]
	""" Cleric of An'she
	[Battlecry:] If you've restored Health this turn, [Discover] a spell from your deck. """
	def play(self):
		#this turn
		actions=[action for action in self.controller._targetedaction_log if isinstance(action['class'],Heal) and action['turn']==self.controller.game.turn]
		if len(actions)>0:
			cards=[card.id for card in self.controller.deck if card.type==CardType.SPELL]
			if len(cards)>3:
				cards = random.sample(cards, 3)
			WC_803_Choice(self.controller, RandomID(*cards)*3).trigger(self)
	pass


######################################################