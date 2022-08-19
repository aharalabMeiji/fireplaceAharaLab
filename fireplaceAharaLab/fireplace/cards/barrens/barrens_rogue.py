
from ..utils import *

Barrens_Rogue=[]

Barrens_Oil_Rig_Ambusher=True  ###
Barrens_Field_Contact=True  ###
Barrens_Silverleaf_Poison=True  ###
Barrens_Wicked_Stab_Rank_1=True  ###
Barrens_Efficient_Octo_bot=True  ###
Barrens_Paralytic_Poison=True  ###
Barrens_Swinetusk_Shank=True  ###
Barrens_Yoink=True  ###
Barrens_Apothecary_Helbrim=True  ###
Barrens_Scabbs_Cutterbutter=True  ###
Barrens_Water_Moccasin=True  ###
Barrens_Shroud_of_Concealment=True  ###
Barrens_Savory_Deviate_Delight=True  ###

###################################################

if Barrens_Oil_Rig_Ambusher:# 
	Barrens_Rogue+=['BAR_316']
class BAR_316:# <7>[1525]
	""" Oil Rig Ambusher
	[Battlecry:] Deal 2 damage.If this entered your hand_this turn, deal 4 instead. """
	requirements ={PlayReq.REQ_MINION_TARGET:0,PlayReq.REQ_TARGET_TO_PLAY:0,PlayReq.REQ_ENEMY_TARGET:0,}
	def play(self):
		actions = [action for action in self.controller._targetedaction_log \
			if isinstance(action['class'], Give) and action['target'].id=='BAR_316']
		actions += [action for action in self.controller._targetedaction_log \
			if isinstance(action['class'], Draw) and action['target_arg'][0].id=='BAR_316']
		if len(actions)>0:
			Hit(TARGET,4)
		else:
			Hit(TARGET,2)

	pass




if Barrens_Field_Contact:# 
	Barrens_Rogue+=['BAR_317']
class BAR_317:# <7>[1525]
	""" Field Contact
	After you play a [Battlecry]or [Combo] card, draw a card. """
	events = [
		Play(CONTROLLER, FRIENDLY + BATTLECRY).Draw(CONTROLLER),
		Play(CONTROLLER, FRIENDLY + COMBO).Draw(CONTROLLER)
	]
	pass




if Barrens_Silverleaf_Poison:# 
	Barrens_Rogue+=['BAR_318']
class BAR_318:# <7>[1525]
	""" Silverleaf Poison
	Give your weapon "After your hero attacks, draw a card." """
	play = Buff(FRIENDLY_WEAPON, 'BAR_318e')
	pass
class BAR_318e:
	events = Attack(FRIENDLY_HERO).after(Draw(CONTROLLER))
	pass



if Barrens_Wicked_Stab_Rank_1:# 
	Barrens_Rogue+=['BAR_319']
	Barrens_Rogue+=['BAR_319t']
	Barrens_Rogue+=['BAR_319t2']
class BAR_319:# <7>[1525]
	""" Wicked Stab (Rank 1)
	Deal $2 damage. <i>(Upgrades when you have 5 Mana.)</i> """
	class Hand:
		events = GradeupByMana(CONTROLLER, 5).on(Destroy(SELF),Give(CONTROLLER, 'BAR_319t'))	
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0,}
	play=Hit(TARGET, 2)
	pass
class BAR_319t:# <7>[1525]
	""" Wicked Stab (Rank 2)
	Deal $4 damage. <i>(Upgrades when you have 10 Mana.)</i> """
	class Hand:
		events = GradeupByMana(CONTROLLER, 10).on(Destroy(SELF),Give(CONTROLLER, 'BAR_319t2'))	
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0,}
	play=Hit(TARGET, 4)
	pass
class BAR_319t2:# <7>[1525]
	""" Wicked Stab (Rank 3)
	Deal $6 damage. """
	requirements={PlayReq.REQ_TARGET_TO_PLAY:0, PlayReq.REQ_MINION_TARGET:0,}
	play=Hit(TARGET, 6)
	pass




if Barrens_Efficient_Octo_bot:# 
	Barrens_Rogue+=['BAR_320']
class BAR_320:# <7>[1525]
	""" Efficient Octo-bot
	[Frenzy:] Reduce the cost of cards in your hand by (1). """
	events = Damage(SELF).on(Frenzy(SELF, Buff(FRIENDLY_HAND, 'BAR_320e')))	#
	pass
class BAR_320e:
	tags={GameTag.COST:-1}



if Barrens_Paralytic_Poison:# 
	Barrens_Rogue+=['BAR_321']
	Barrens_Rogue+=['BAR_321e']
class BAR_321:# <7>[1525]
	""" Paralytic Poison
	Give your weapon +1 Attack and "Your hero is[Immune] while attacking." """
	play = Buff(FRIENDLY_WEAPON, 'BAR_321e')
	pass
class BAR_321e:# <7>[1525]
	""" Paralytic Poison
	+1 Attack and [Immune] while attacking. """
	tags={
		GameTag.ATK:1,
		GameTag.IMMUNE_WHILE_ATTACKING:1
	}
	pass




if Barrens_Swinetusk_Shank:# 
	Barrens_Rogue+=['BAR_322']
class BAR_322:# <7>[1525]
	""" Swinetusk Shank
	After you play a Poison,_gain +1 Durability. """
	events = Play(CONTROLLER, POISONOUS).after(Buff(FRIENDLY_WEAPON, 'BAR_322e'))
	pass
class BAR_322e:
	tags={
		GameTag.DURABILITY:1,
	}


if Barrens_Yoink:# 
	Barrens_Rogue+=['BAR_323']
	Barrens_Rogue+=['BAR_323e']
class BAR_323:# <7>[1525]
	""" Yoink!
	[Discover] a Hero Power and set its Cost to (0). Swap back after 2 uses. """
	#
	pass
class BAR_323e:# <7>[1525]
	""" Yoink!
	 """
	#
	pass




if Barrens_Apothecary_Helbrim:# 
	Barrens_Rogue+=['BAR_324']
class BAR_324:# <7>[1525]
	""" Apothecary Helbrim
	[Battlecry and Deathrattle:] Add a random Poison to your hand. """
	#
	pass




if Barrens_Scabbs_Cutterbutter:# 
	Barrens_Rogue+=['BAR_552']
	Barrens_Rogue+=['BAR_552o']
class BAR_552:# <7>[1525]
	""" Scabbs Cutterbutter
	[Combo:] The next twocards you play this turncost (3) less. """
	#
	pass
class BAR_552o:# <7>[1525]
	""" Cookin!
	The next two cards you play this turn costs (3) less. """
	#
	pass




if Barrens_Water_Moccasin:# 
	Barrens_Rogue+=['WC_015']
class WC_015:# <7>[1525]
	""" Water Moccasin
	[Stealth]Has [Poisonous] while you_have no other minions. """
	#
	pass




if Barrens_Shroud_of_Concealment:# 
	Barrens_Rogue+=['WC_016']
	Barrens_Rogue+=['WC_016e']
	Barrens_Rogue+=['WC_016e2']
class WC_016:# <7>[1525]
	""" Shroud of Concealment
	Draw 2 minions. Any played this turn gain [Stealth] for 1 turn. """
	#
	pass
class WC_016e:# <7>[1525]
	""" Cloaking
	Play this turn to gain [Stealth] for 1 turn. """
	#
	pass
class WC_016e2:# <7>[1525]
	""" Cloaked
	[Stealth] for 1 turn. """
	#
	pass




if Barrens_Savory_Deviate_Delight:# 
	Barrens_Rogue+=['WC_017']
class WC_017:# <7>[1525]
	""" Savory Deviate Delight
	Transform a minion in both players' hands into a Pirate or [Stealth] minion. """
	#
	pass



