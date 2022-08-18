
from ..utils import *

Barrens_DemonHunter=[]

Barrens_Sigil_of_Flame=True  ###
Barrens_Razorboar=True  ###
Barrens_Razorfen_Beastmaster=True  ###
Barrens_Vile_Call=True  ###
Barrens_Vengeful_Spirit=True  ###
Barrens_Death_Speaker_Blackthorn=True  ###
Barrens_Tuskpiercer=True  ###
Barrens_Kurtrus_Ashfallen=True  ###
Barrens_Sigil_of_Silence=True  ###
Barrens_Fury_Rank_1=True  ###
Barrens_Sigil_of_Summoning=True  ###
Barrens_Taintheart_Tormenter=True  ###
Barrens_Felrattler=True  ###

##################################################

if Barrens_Sigil_of_Flame:# 
	Barrens_DemonHunter+=['BAR_306']
class BAR_306:# <14>[1525]
	""" Sigil of Flame
	At the start of your next turn, deal $3 damageto all minions. """
	events = OWN_TURN_BEGIN.on(Hit(ENEMY_MINIONS, 3))
	pass




if Barrens_Razorboar:# 
	Barrens_DemonHunter+=['BAR_325']
class BAR_325_Summon(TargetedAction):
	TARGET=ActionArg()
	def do(self,source,target):
		cards=[card for card in target.hand if card.cost<=3 and card.has_deathrattle==True]
		if len(cards)>0:
			Summon(target, random.choice(cards)).trigger(source)
class BAR_325:# <14>[1525]
	""" Razorboar
	[Deathrattle:] Summon a [Deathrattle] minion that costs (3) or less from your hand. """
	deathrattle = BAR_325_Summon(CONTROLLER)
	pass




if Barrens_Razorfen_Beastmaster:# 
	Barrens_DemonHunter+=['BAR_326']
class BAR_326_Summon(TargetedAction):
	TARGET=ActionArg()
	def do(self,source,target):
		cards=[card for card in target.hand if card.cost<=4 and card.has_deathrattle==True]
		if len(cards)>0:
			Summon(target, random.choice(cards)).trigger(source)
class BAR_326:# <14>[1525]
	""" Razorfen Beastmaster
	[Deathrattle:] Summon a [Deathrattle] minion that costs (4) or less from your hand. """
	deathrattle = BAR_326_Summon(CONTROLLER)
	pass




if Barrens_Vile_Call:# 
	Barrens_DemonHunter+=['BAR_327']
	Barrens_DemonHunter+=['BAR_327t']
class BAR_327:# <14>[1525]
	""" Vile Call
	Summon two 2/2 Demons with [Lifesteal]. """
	play = Summon(CONTROLLER, 'BAR_327t')
	pass
class BAR_327t:# <14>[1525]
	""" Ravenous Vilefiend
	[Lifesteal] """
	#
	pass




if Barrens_Vengeful_Spirit:# 
	Barrens_DemonHunter+=['BAR_328']
class BAR_328_Give(TargetedAction):
	TARGET=ActionArg()#CONTROLLER
	def do(self,source,target):
		cards=[card for card in source.target.deck if card.has_deathrattle==True]
		if len(cards)>=2:
			cards=random.sampl(cards, 2)
		for card in cards:
			Summon(target, card).trigger(source)
class BAR_328:# <14>[1525]
	""" Vengeful Spirit
	[Outcast:] Draw 2 [Deathrattle] minions. """
	outcast = BAR_328_Give(CONTROLLER)
	pass




if Barrens_Death_Speaker_Blackthorn:# 
	Barrens_DemonHunter+=['BAR_329']
class BAR_329_Summon(TargetedAction):
	TARGET=ActionArg()
	def do(self,source,target):
		cards=[card for card in target.deck if card.cost<=5 and card.has_deathrattle==True]
		if len(cards)>3:
			cards=random.sampl(cards, 3)
		for card in cards:
			Summon(target, card).trigger(source)
class BAR_329:# <14>[1525]
	""" Death Speaker Blackthorn
	[Battlecry:] Summon 3 [Deathrattle] minions that cost (5) or less from your deck. """
	play = BAR_329_Summon(CONTROLLER)#
	pass




if Barrens_Tuskpiercer:# 
	Barrens_DemonHunter+=['BAR_330']
class BAR_330_Draw(TargetedAction):
	TARGET=ActionArg()
	def do(self,source,target):
		cards=[card for card in target.deck if card.has_deathrattle==True]
		card = random.choice(cards)
		Summon(target, card).trigger(source)
class BAR_330:# <14>[1525]
	""" Tuskpiercer
	[Deathrattle:] Draw a[Deathrattle] minion. """
	deathrattle = BAR_330_Draw(CONTROLLER)
	pass




if Barrens_Kurtrus_Ashfallen:# 
	Barrens_DemonHunter+=['BAR_333','BAR_333e']
class BAR_333_Action(TargetedAction):
	TARGET=ActionArg()
	def do(self,source,target):
		target.cant_be_damaged=True
class BAR_333:# <14>[1525]
	""" Kurtrus Ashfallen
	[Battlecry:] Attack the left andright-most enemy minions.[Outcast:] [Immune] this turn. """
	def play(self):
		controller = self.controller
		enemy_minions=controller.opponent.field
		if len(enemy_minions)>=2:
			RegularAttack(SELF, enemy_minions[-1]).trigger(self)
		if len(enemy_minions)>=1:
			RegularAttack(SELF, enemy_minions[0]).trigger(self)
	outcast = Buff(SELF, 'BAR_333e')
	pass
class BAR_333e:
	tags={GameTag.CANT_BE_DAMAGED: True}
	#Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>



if Barrens_Sigil_of_Silence:# 
	Barrens_DemonHunter+=['BAR_705']
class BAR_705:# <14>[1525]
	""" Sigil of Silence
	At the start of yournext turn, [Silence] allenemy minions. """
	events = OWN_TURN_BEGIN.on(Silence(ENEMY_MINIONS))
	pass




if Barrens_Fury_Rank_1:# 
	Barrens_DemonHunter+=['BAR_891']
	Barrens_DemonHunter+=['BAR_891e']
	Barrens_DemonHunter+=['BAR_891e2']
	Barrens_DemonHunter+=['BAR_891e3']
	Barrens_DemonHunter+=['BAR_891t']
	Barrens_DemonHunter+=['BAR_891t2']
class BAR_891:# <14>[1525]
	""" Fury (Rank 1)
	Give your hero +2 Attack this turn. <i>(Upgrades when you have 5 Mana.)</i> """
	class Hand:
		events = GradeupByMana(CONTROLLER, 5).on(Destroy(SELF),Give(CONTROLLER, 'BAR_891t'))	
	play = Buff(FRIENDLY_HERO, 'BAR_891e')
	pass
class BAR_891e:# <14>[1525]
	""" Fury +2 Attack this turn. """
	tags = {GameTag.ATK:2, }
	#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>
	pass

class BAR_891t:# <14>[1525]
	""" Fury (Rank 2)
	Give your hero +3 Attackthis turn. <i>(Upgrades whenyou have 10 Mana.)</i> """
	class Hand:
		events = GradeupByMana(CONTROLLER, 10).on(Destroy(SELF),Give(CONTROLLER, 'BAR_891t2'))	
	play = Buff(FRIENDLY_HERO, 'BAR_891e2')
	pass
class BAR_891e2:# <14>[1525]
	""" Fury 	+3 Attack this turn. """
	tags = {GameTag.ATK:3, }
	#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>
	pass

class BAR_891t2:# <14>[1525]
	""" Fury (Rank 3)
	Give your hero +4_Attack this turn. """
	play = Buff(FRIENDLY_HERO, 'BAR_891e3')
	#
	pass
class BAR_891e3:# <14>[1525]
	""" Fury 	+4 Attack this turn. """
	tags = {GameTag.ATK:4, }
	#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>
	pass



if Barrens_Sigil_of_Summoning:# 
	Barrens_DemonHunter+=['WC_003']
	Barrens_DemonHunter+=['WC_003t']
class WC_003:# <14>[1525]
	""" Sigil of Summoning
	At the start of your next turn, summon two 2/2 Demons with [Taunt]. """
	events = OWN_TURN_BEGIN.on(Buff(CONTROLLER, 'WC_003t'))
	pass

class WC_003t:# <14>[1525]
	""" Wailing Demon
	[Taunt] """
	#
	pass




if Barrens_Taintheart_Tormenter:# 
	Barrens_DemonHunter+=['WC_040']
class WC_040:# <14>[1525]
	""" Taintheart Tormenter
	[Taunt]Your opponent's spells cost (2) more. """
	update=Refresh(ENEMY_MINIONS, 'WC_040e')
	pass
class WC_040e:
	tags={GameTag.COST:2,}



if Barrens_Felrattler:# 
	Barrens_DemonHunter+=['WC_701']
class WC_701:# <14>[1525]
	""" Felrattler
	[Rush][Deathrattle:] Deal 1 damageto all enemy minions. """
	deathrattle = Hit(ENEMY_MINIONS, 1)
	pass

