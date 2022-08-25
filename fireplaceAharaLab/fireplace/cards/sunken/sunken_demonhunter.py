from ..utils import *

Sunken_DemonHunter=[]

Sunken_Topple_the_Idol=True  ###
Sunken_Fossil_Fanatic=True  ###
Sunken_Herald_of_Chaos=True  ###
Sunken_Multi_Strike=True  ###
Sunken_Azsharan_Defector=True  ###
Sunken_Predation=True  ###
Sunken_Wayward_Sage=True  ###
Sunken_Lady_Stheno=True  ###
Sunken_Xhilag_of_the_Abyss=True  ###
Sunken_Abyssal_Depths=True  ###
Sunken_Coilskar_Commander=True  ###
Sunken_Glaiveshark=True  ###
Sunken_Bone_Glaive=True  ###


if Sunken_Topple_the_Idol:# 
	Sunken_DemonHunter+=['TID_703']
class TID_703_DredgeChoice(Choice):
	def choose(self, card):
		super().choose(card)
		if Config.LOGINFO:
			print("(DredgeChoice.choose)%s chooses %r"%(card.controller.name, card))
		controller = card.controller
		for c in controller.deck[:3]:
			if card.id==c.id:
				controller.deck.remove(c)
				controller.deck.append(c)
				Hit(ALL_MINIONS, c.cost)
				break
		pass

class TID_703_Dredge(TargetedAction):
	"""
	TARGET=ActionArg()#CONTROLLER
	"""
	TARGET=ActionArg()
	def do(self, source, target):
		bottom3ID=[card.id for card in target.deck[:3]]
		TID_703_DredgeChoice(target, RandomID(*bottom3ID)*3).trigger(source)
	pass
class TID_703:# <14>[1658]
	""" Topple the Idol
	[Dredge]. Reveal it anddeal damage equal to_its Cost to all minions. """
	play = TID_703_Dredge(CONTROLLER)
	pass




if Sunken_Fossil_Fanatic:# 
	Sunken_DemonHunter+=['TID_704']
class TID_704:# <14>[1658]
	""" Fossil Fanatic
	After your hero attacks, draw a Fel spell. """
	events = Attack(FRIENDLY_HERO).after(Give(CONTROLLER, RANDOM(FRIENDLY_DECK + FEL)))
	pass




if Sunken_Herald_of_Chaos:# 
	Sunken_DemonHunter+=['TID_706']
	Sunken_DemonHunter+=['TID_706e']
class TID_706:# <14>[1658]
	""" Herald of Chaos
	[Lifesteal][Battlecry:] If you've cast aFel spell while holding this,gain [Rush]. """
	class Hand:
		events = Play(CONTROLLER, FEL).after(Buff(SELF, 'TID_706e'))
	pass

class TID_706e:# <14>[1658]
	""" Felfused Has [Rush]. """
	tags = {GameTag.RUSH:True,}
	pass




if Sunken_Multi_Strike:# 
	Sunken_DemonHunter+=['TSC_006']
	Sunken_DemonHunter+=['TSC_006e']
	Sunken_DemonHunter+=['TSC_006e2']
class TSC_006:# <14>[1658]
	""" Multi-Strike
	Give your hero +2 Attack this turn. They may attack an additional enemy minion. """
	play = Buff(FRIENDLY_HERO, "TSC_006e"), Buff(FRIENDLY_HERO, "TSC_006e2")
	pass

TSC_006e=buff(2,0)
#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>

class TSC_006e2:# <14>[1658]
	""" Multi-Strike enchant Attack +2. """
	#<Tag enumID="338" name="TAG_ONE_TURN_EFFECT" type="Int" value="1"/>
	tags = { GameTag.WINDFURY:1, }
	pass




if Sunken_Azsharan_Defector:# 
	Sunken_DemonHunter+=['TSC_057']
 
	Sunken_DemonHunter+=['TSC_057t']
class TSC_057:# <14>[1658]
	""" Azsharan Defector
	[Rush]. [Deathrattle:] Put a'Sunken Defector' on the_bottom of your deck. """
	#
	pass

class TSC_057t:# <14>[1658]
	""" Sunken Defector
	[Charge]. After this attacks, deal 5 damage to a random enemy minion. """
	#
	pass




if Sunken_Predation:# 
	Sunken_DemonHunter+=['TSC_058']
class TSC_058:# <14>[1658]
	""" Predation
	Deal $3 damage.Costs (0) if you played a Naga while holding this. """
	class Hand:
		events = Play(CONTROLLER, NAGA).on(Buff(FRIENDLY_HAND + ID('TSC_058'), 'TSC_058e'))
	requirements = { PlayReq.REQ_TARGET_TO_PLAY:0, }
	play = Hit(TARGET, 3)
	pass
class TSC_058e:# <14>[1658]
	""" Looting
	Costs (0). """
	cost = SET(0)#
	pass




if Sunken_Wayward_Sage:# 
	Sunken_DemonHunter+=['TSC_217']
 
	Sunken_DemonHunter+=['TSC_217e']
class TSC_217:# <14>[1658]
	""" Wayward Sage
	[Outcast:] Reduce the Costof the left and right-most_cards in your hand by (1). """
	#
	pass

class TSC_217e:# <14>[1658]
	""" Found the Wrong Way
	Costs (1) less. """
	#
	pass




if Sunken_Lady_Stheno:# 
	Sunken_DemonHunter+=['TSC_218']
class TSC_218:# <14>[1658]
	""" Lady S'theno
	[Immune] while attacking.After you cast a spell, attackthe lowest Health enemy. """
	#
	pass




if Sunken_Xhilag_of_the_Abyss:# 
	Sunken_DemonHunter+=['TSC_219','TSC_219e','TSC_219t','TSC_219t2','TSC_219t3','TSC_219t4',]
class TSC_219:# <14>[1658]
	""" Xhilag of the Abyss
	[Colossal +4]At the start of your turn,increase the damage of Xhilag's Stalks by 1. """
	play=(
		Summon(CONTROLLER,'TSC_219t'),
		Summon(CONTROLLER,'TSC_219t2'),
		Summon(CONTROLLER,'TSC_219t3'),
		Summon(CONTROLLER,'TSC_219t4')
	)
	events = OWN_TURN_BEGIN.on(
		AddScriptDataNum1(FRIENDLY_MINIONS+ID('TSC_219t'), 1),
		AddScriptDataNum1(FRIENDLY_MINIONS+ID('TSC_219t2'), 1),
		AddScriptDataNum1(FRIENDLY_MINIONS+ID('TSC_219t3'), 1),
		AddScriptDataNum1(FRIENDLY_MINIONS+ID('TSC_219t4'), 1)
		)
	pass
class TSC_219e:# <14>[1658]
	pass

class TSC_219t:# <14>[1658]
	""" Xhilag's Stalk
	At the end of your turn, deal @ damage to a random enemy. """
	events = OWN_TURN_END.on(HitScriptDataNum1(SELF, RANDOM(ENEMY_MINIONS)))
	pass

class TSC_219t2:# <14>[1658]
	""" Xhilag's Stalk
	At the end of your turn, deal @ damage to a random enemy. """
	events = OWN_TURN_END.on(HitScriptDataNum1(SELF, RANDOM(ENEMY_MINIONS)))
	pass

class TSC_219t3:# <14>[1658]
	""" Xhilag's Stalk
	At the end of your turn, deal @ damage to a random enemy. """
	events = OWN_TURN_END.on(HitScriptDataNum1(SELF, RANDOM(ENEMY_MINIONS)))
	pass

class TSC_219t4:# <14>[1658]
	""" Xhilag's Stalk
	At the end of your turn, deal @ damage to a random enemy. """
	events = OWN_TURN_END.on(HitScriptDataNum1(SELF, RANDOM(ENEMY_MINIONS)))
	pass





if Sunken_Abyssal_Depths:# 
	Sunken_DemonHunter+=['TSC_608']
class TSC_608:# <14>[1658]
	""" Abyssal Depths
	Draw your two lowest Cost minions. """
	#
	pass





if Sunken_Coilskar_Commander:# 
	Sunken_DemonHunter+=['TSC_609']
class TSC_609:# <14>[1658]
	""" Coilskar Commander
	[Taunt]. [Battlecry:] If you'vecast three spells whileholding this, summon two__copies of this.@ <i>({0} left!)</i>@ <i>(Ready!)</i> """
	#
	pass





if Sunken_Glaiveshark:# 
	Sunken_DemonHunter+=['TSC_610']
class TSC_610:# <14>[1658]
	""" Glaiveshark
	[Battlecry:] If your heroattacked this turn, deal 2damage to all enemies. """
	#
	pass





if Sunken_Bone_Glaive:# 
	Sunken_DemonHunter+=['TSC_915']
class TSC_915:# <14>[1658]
	""" Bone Glaive
	[Battlecry:] [Dredge]. """
	#
	pass

