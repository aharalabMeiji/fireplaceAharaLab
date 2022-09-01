
from ..utils import *

Alterac_DemonHunter=[]


Alterac_Battleworn_Vanguard=True  ###
Alterac_Kurtrus_Demon_Render=True  ###
Alterac_Dreadprison_Glaive=True  ###
Alterac_Flag_Runner=True  ###
Alterac_Warden_of_Chains=True  ###
Alterac_Sigil_of_Reckoning=True  ###
Alterac_Urzul_Giant=True  ###
Alterac_Caria_Felsoul=True  ###
Alterac_Flanking_Maneuver=True  ###
Alterac_Field_of_Strife=True  ###
Alterac_Keen_Reflex=True  ###
Alterac_Wings_of_Hate_Rank_1=True  ###
Alterac_Razorglaive_Sentinel=True  ###


if Alterac_Battleworn_Vanguard:# 
	Alterac_DemonHunter+=['AV_118','BT_922t']
class AV_118:# <14>[1626]
	""" Battleworn Vanguard
	After your hero attacks,summon two 1/1 Felwings. """
	events = Attack(FRIENDLY_HERO).after(Summon(CONTROLLER, 'BT_922t')*2)
	pass
class BT_922t:
	""" Felwing """
	pass




if Alterac_Kurtrus_Demon_Render:# 
	Alterac_DemonHunter+=['AV_204']
	Alterac_DemonHunter+=['AV_204e']
	Alterac_DemonHunter+=['AV_204p']
	Alterac_DemonHunter+=['AV_204t2']
class AV_204:# <14>[1626]  Hero (6/*/30) ##OK
	""" Kurtrus, Demon-Render
	[Battlecry:] Summon two@/4 Demons with [Rush].<i>(Improved by your hero attacks this game.)</i> """
	play = Summon(CONTROLLER, 'AV_204t2')*2
	pass
class AV_204e:# <14>[1626] ##OK
	""" Ashfallen's Power
	+2 Attack this turn. """
	tags={GameTag.ATK:2, }
	#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>
	pass
class AV_204p:# <14>[1626] ###### need check
	""" Ashfallen's Fury
	[Hero Power]+2 Attack this turn.After a friendly minion attacks, refresh this. """
	activate = Buff(FRIENDLY_HERO, 'AV_204e')
	events = Attack(FRIENDLY_MINIONS).after(RefreshHeroPower(FRIENDLY_HERO_POWER))
	pass
class AV_204t2:# <14>[1626] ##OK
	""" Felbat Shrieker
	[Rush] """
	#
	pass




if Alterac_Dreadprison_Glaive:# 
	Alterac_DemonHunter+=['AV_209']
class AV_209:# <14>[1626]
	""" Dreadprison Glaive
	[Honorable Kill:] Deal damage equal to your hero's Attack to the enemy hero. """
	honorable_kill = Hit(ENEMY_HERO, ATK(FRIENDLY_HERO))
	pass




if Alterac_Flag_Runner:# 
	Alterac_DemonHunter+=['AV_261']
	Alterac_DemonHunter+=['AV_261e']
class AV_261:# <14>[1626]
	""" Flag Runner
	Whenever a friendly minion dies, gain +1 Attack. """
	events = Death(FRIENDLY_MINIONS).on(Buff(SELF,'AV_261e'))
	pass
AV_261e=buff(1,0)# <14>[1626]
""" Team Player	+1 Attack """




if Alterac_Warden_of_Chains:# 
	Alterac_DemonHunter+=['AV_262']
	Alterac_DemonHunter+=['AV_262e2']
class AV_262:# <14>[1626] #
	""" Warden of Chains
	[Taunt][Battlecry:] If you're holdinga Demon that costs (5) or more, gain +1/+2. """
	def play(self):
		cards=[card for card in self.controller.hand if card.type==CardType.MINION and card.race==Race.DEMON and card.cost>=5]
		if len(cards)>0:
			Buff(SELF, 'AV_262e2').trigger(self)
	pass
AV_262e2=buff(1,2)# <14>[1626]
""" Terrifying	+1/+2. """




if Alterac_Sigil_of_Reckoning:# 
	Alterac_DemonHunter+=['AV_264']
class AV_264:# <14>[1626]
	""" Sigil of Reckoning
	At the start of your next turn, summon a random Demon from your hand. """
	events = OWN_TURN_BEGIN.on(Find(FRIENDLY_HAND+DEMON) & Summon(CONTROLLER, RANDOM(FRIENDLY_HAND+DEMON)))
	pass




if Alterac_Urzul_Giant:# 
	Alterac_DemonHunter+=['AV_265']
class AV_265:# <14>[1626]
	""" Ur'zul Giant
	Costs (1) less for each friendly minion that died this game. """
	cost_mod = -Count(FRIENDLY+ KILLED)	
	pass




if Alterac_Caria_Felsoul:# 
	Alterac_DemonHunter+=['AV_267']
	Alterac_DemonHunter+=['AV_267e2']
class AV_267:# <14>[1626]
	""" Caria Felsoul
	[Battlecry:] Transform into a 7/7 copy of a Demon in your deck. """
	play = Buff(FRIENDLY_DECK + DEMON, 'AV_267e2')
	pass
class AV_267e2:# <14>[1626]
	""" Demonic
	Attack and Health set to 7. """
	atk=SET(7)
	max_health=SET(7)
	pass




if Alterac_Flanking_Maneuver:# 
	Alterac_DemonHunter+=['AV_269']
	Alterac_DemonHunter+=['AV_269e']
	Alterac_DemonHunter+=['AV_269t']
class AV_269:# <14>[1626]
	""" Flanking Maneuver
	Summon a 4/2 Demon with [Rush]. If it dies this turn, summon another. """
	play = Summon(CONTROLLER, 'AV_269t').then(Buff(Summon.CARD, 'AV_269e'))
	pass
class AV_269e:# <14>[1626]
	""" Woe Is Me
	If this dies summon another. """
	#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>### if in this turn
	events = Death(OWNER).on(Summon(CONTROLLER, 'AV_269t'))  
	pass
class AV_269t:# <14>[1626]
	""" Snowy Satyr
	[Rush] """
	pass




if Alterac_Field_of_Strife:# 
	Alterac_DemonHunter+=['AV_661']
	Alterac_DemonHunter+=['AV_661e2']
class AV_661:# <14>[1626]
	""" Field of Strife
	Your minions have+1 Attack.Lasts 3 turns. """
	tags={GameTag.SIDEQUEST:True, }
	update = Refresh(FRIENDLY_MINIONS, buff='AV_661e2')
	events = OWN_TURN_BEGIN.on(SidequestCounter(SELF, 3, [Destroy(SELF)]))	
	pass
class AV_661e2:# <14>[1626]
	""" Empowered 	+1 Attack from {0}. """
	tags = {GameTag.ATK:1,}
	pass




if Alterac_Keen_Reflex:# 
	Alterac_DemonHunter+=['ONY_014']
	Alterac_DemonHunter+=['ONY_014e']
class ONY_014:# <14>[1626]
	""" Keen Reflex
	Deal $1 damage to all minions. [Honorable Kill:]Gain +1 Attack this turn. """
	play = Hit(ALL_MINIONS, 1)
	honorable_kill = Buff(FRIENDLY_HERO, 'ONY_014e')
	pass
class ONY_014e:# <14>[1626]
	""" Keen Reflex 	+1 Attack this turn. """
	#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>
	atk = lambda self,i: i+1
	pass




if Alterac_Wings_of_Hate_Rank_1:# 
	Alterac_DemonHunter+=['ONY_016']
	Alterac_DemonHunter+=['ONY_016t']
	Alterac_DemonHunter+=['ONY_016t2']
class ONY_016:# <14>[1626]
	""" Wings of Hate (Rank 1)
	Summon two 1/1Felwings. <i>(Upgrades when you have 5 Mana.)</i> """
	class Hand:
		events = GradeupByMana(CONTROLLER, 5).on(Destroy(SELF),Give(CONTROLLER, 'ONY_016t'))	
	play = Summon(CONTROLLER, 'BT_922t')*2
	pass
class ONY_016t:# <14>[1626]
	""" Wings of Hate (Rank 2)
	Summon three 1/1Felwings. <i>(Upgradeswhen you have 10 Mana.)</i> """
	class Hand:
		events = GradeupByMana(CONTROLLER, 10).on(Destroy(SELF),Give(CONTROLLER, 'ONY_016t2'))	
	play = Summon(CONTROLLER, 'BT_922t')*3
	pass
class ONY_016t2:# <14>[1626]
	""" Wings of Hate (Rank 3)
	Summon four1/1 Felwings. """
	play = Summon(CONTROLLER, 'BT_922t')*4
	pass




if Alterac_Razorglaive_Sentinel:# 
	Alterac_DemonHunter+=['ONY_036']
class ONY_036:# <14>[1626]
	""" Razorglaive Sentinel
	After you play the left or right-most card in your hand, draw a card. """
	events = Play(CONTROLLER, OUTERMOST_HAND).on(Draw(CONTROLLER))
	pass


