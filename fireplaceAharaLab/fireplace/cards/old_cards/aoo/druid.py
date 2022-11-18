from ..utils import *

#AOO_DRUID=['BT_127','BT_127e','BT_128','BT_129','BT_129e','BT_130','BT_131','BT_132',
#'BT_132e','BT_133','BT_134','BT_135','BT_135t',
#'BT_136','BT_136t','BT_136ta','BT_136tb','BT_136tt','BT_136tt2','BT_136tt3']
#outrage=['BTA_05','BTA_05e','BTA_BOSS_03t','BTA_BOSS_10e','BTA_BOSS_10h2','BTA_BOSS_10h4','BTA_BOSS_10t','Prologue_Cenarius','Prologue_CenariusHP','Prologue_MoongladePortal','TB_HERO_MALFURION',]

class BT_127:#OK <2>[1414]
	""" Imprisoned Satyr
	[Dormant] for 2 turns.When this awakens, reduce
	the Cost of a random minionin your hand by (5). """
	dormant = 2
	awaken = Buff(RANDOM(FRIENDLY_HAND + MINION), "BT_127e")
BT_127e = buff(cost=-5)
""" Imprisoned Satyr
Costs (5) less. """

class BT_128:#OK <2>[1414]
	""" Fungal Fortunes
	Draw 3 cards. Discard any minions drawn. """
	play = Draw(CONTROLLER).then(Discard(Draw.CARD + MINION)) * 3
	pass

class BT_129:#OK <2>[1414]
	""" Germination
	Summon a copy of a friendly minion.Give the copy [Taunt]. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_FRIENDLY_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Summon(CONTROLLER, ExactCopy(TARGET)).then(Buff(Summon.CARD, "BT_129e"))
	pass
BT_129e = buff(taunt=True)##<12>[1414}

class BT_130:# <2>[1414]# clownDruid
	"""Overgrowth, Gain two empty Mana Crystals."""
	play = GainEmptyMana(CONTROLLER, 2)
	pass

class BT_131:#OK <2>[1414]
	""" Ysiel Windsinger
	Your spells cost (1). """
	play = Buff(FRIENDLY_HAND + SPELL, 'BT_131e')
	pass
class BT_131e:
	cost=SET(1)
	pass

class BT_132_Action(TargetedAction):
	def do(self,source,target):
		#controller = target
		if target.mana>=7:
			source.cost=0
		else:
			source.cost=2
		pass
class BT_132:#OK <2>[1414]
	""" Ironbark
	Give a minion +1/+3 and [Taunt].Costs (0) if you have at least 7 Mana Crystals. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "BT_132e")
	pass
	class Hand:
		update = BT_132_Action(CONTROLLER)
BT_132e = buff(atk=1, health=3, taunt=True)
""" Ironbark
+1/+3 and [Taunt]. """

class BT_133:#OK <2>[1414]
	""" Marsh Hydra
	[Rush]After this attacks, add arandom 8-Cost minionto your hand. """
	events = Attack(SELF).after(Give(CONTROLLER, RandomMinion(cost=8)))
	pass

class BT_134_Action(TargetedAction):
	def do(self,source,target):
		#controller = target
		if target.mana>=7:
			source.cost=0
		else:
			source.cost=3
		pass
class BT_134:#OK <2>[1414]
	""" Bogbeam
	Deal $3 damage to_a minion.Costs (0) if you have at least 7 Mana Crystals. """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Hit(TARGET, 3)
	class Hand:
		update = BT_134_Action(CONTROLLER)#(MANA(CONTROLLER) >= 7) & Refresh(SELF, {GameTag.COST: SET(0)})
	pass

class BT_135:#OK <2>[1414]
	""" Glowfly Swarm
	Summon a 2/2 Glowfly for each spell in your_hand. """
	play = Summon(CONTROLLER, "BT_135t") * Count(FRIENDLY_HAND + SPELL)
	pass

class BT_135t:# <2>[1414]
	""" Glowfly
	 """
	#
	pass

class BT_136:#OK <2>[1414]
	""" Archspore Msshi'fn
	[Taunt][Deathrattle:] Shuffle'Msshi'fn Prime'into your deck. """
	deathrattle = Shuffle(CONTROLLER, "BT_136t")

class BT_136t:#OK <2>[1414]
	""" Msshi'fn Prime
	[Taunt][Choose One -] Summon a 9/9 Fungal Giant with [Taunt]; or [Rush]. """
	choose = ("BT_136ta", "BT_136tb")
	play = ChooseBoth(SELF) & (
		Summon(CONTROLLER, "BT_136tt3"))
	pass

class BT_136ta:# <2>[1414]
	""" Msshi'fn Pro'tec
	Summon a 9/9 Guardian with [Taunt]. """
	play = Summon(CONTROLLER, "BT_136tt")
	pass

class BT_136tb:# <2>[1414]
	""" Msshi'fn At'tac
	Summon a 9/9 Bruiser with [Rush]. """
	play = Summon(CONTROLLER, "BT_136tt2")
	pass

class BT_136tt:# <2>[1414]
	""" Fungal Guardian
	[Taunt] """
	#
	pass

class BT_136tt2:# <2>[1414]
	""" Fungal Bruiser
	[Rush] """
	#
	pass

class BT_136tt3:# <2>[1414]
	""" Fungal Gargantuan
	[Rush][Taunt] """
	#
	pass

