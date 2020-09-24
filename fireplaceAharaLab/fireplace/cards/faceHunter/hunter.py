from ..utils import *

class SCH_133:
	""" Wolpertinger """
	play = Summon(CONTROLLER, "SCH_133")

class SCH_617:
	"""  カワイイ侵入者 """
	requirements = {
		PlayReq.REQ_MINION_TARGET: 0,
		PlayReq.REQ_TARGET_TO_PLAY: 0}
	play = Buff(TARGET, "SCH_617e"), Summon(CONTROLLER, "SCH_617t"),Give(CONTROLLER, "SCH_617t")

SCH_617e = buff(+1, +1)

class SCH_312:
	""" ツアーガイド
		&lt;b&gt;雄叫び:&lt;/b&gt;自分が次に使うヒーローパワーのコストは（0）
	"""
	play = Buff(CONTROLLER, "SCH_312e")

class SCH_312e:
	update = Refresh(FRIENDLY_HERO_POWER, {GameTag.COST: SET(0)})
	events = Play(CONTROLLER, SPELL).on(Destroy(SELF))	##再考を要する