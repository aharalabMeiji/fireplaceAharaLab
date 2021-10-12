from ..utils import *


class DRG_252:#OK
	"""Phase Stalker
	[x]After you use your Hero
	Power, cast a <b>Secret</b>
	from your deck."""
	events = Activate(CONTROLLER, HERO_POWER).on(Summon(CONTROLLER, RANDOM(FRIENDLY_DECK + SECRET)))
	pass

class DRG_253:#OK!
	"""Dwarven Sharpshooter
	Your Hero Power can target_minions."""
	## deal 2 damage to enemy hero HERO_05bp, HERO_05dbp
	## deal 3 damage to enemy hero HERO_05bp2
	play = ChangeHeroPower(CONTROLLER, "HERO_05dbp")
	# see also fireplace.actions.Death.do
	pass

class DRG_256:#OK
	"""Dragonbane
	After you use your Hero Power, deal 5 damage to a random enemy."""
	play = Activate(CONTROLLER, HERO_POWER).on(Hit(RANDOM_ENEMY_CHARACTER, 5))
	pass

class ULD_152:#OK
	"""Pressure Plate	Common
	<b>Secret:</b> After your opponent casts a spell, destroy a random enemy_minion."""
	secret = Play(OPPONENT, SPELL).on(Reveal(SELF), Destroy(RANDOM_ENEMY_MINION))
	pass

class EX1_536:
	"""Eaglehorn Bow"""
	events = Reveal(FRIENDLY_SECRETS).on(Buff(SELF, "EX1_536e"))
EX1_536e = buff(health=1)

class EX1_539:
	"""Kill Command"""
	requirements = {PlayReq.REQ_TARGET_TO_PLAY: 0}
	powered_up = Find(FRIENDLY_MINIONS + BEAST)
	play = powered_up & Hit(TARGET, 5) | Hit(TARGET, 3)

#class SCH_133:
#	""" Wolpertinger 
#	雄叫び: このミニオンの   コピーを1体召喚する。"""
#	play = Summon(CONTROLLER, Copy(SELF))

#class SCH_617:
#	"""  カワイイ侵入者 
#	ミニオン1体に +1/+1を付与する。 1/1の仔を1体召喚する。 仔1体を自分の 手札に追加する。"""
#	requirements = {
#		PlayReq.REQ_MINION_TARGET: 0,
#		PlayReq.REQ_TARGET_TO_PLAY: 0}
#	play = Buff(TARGET, "SCH_617e"), Summon(CONTROLLER, "SCH_617t"),Give(CONTROLLER, "SCH_617t")

#SCH_617e = buff(1, 1)

#class SCH_617t:
#	pass

#class SCH_312:
#	""" School Tour ツアーガイド
#		<b>雄叫び:</b>自分が次に使うヒーローパワーのコストは（0）
#	"""
#	play = Buff(CONTROLLER, "SCH_312e")

#class SCH_312e:
#	update = Refresh(FRIENDLY_HERO_POWER, {GameTag.COST: SET(0)})
#	events = Activate(CONTROLLER, HERO_POWER).on(Destroy(SELF))




#class SCH_231:
#	"""図太い徒弟
#	[x]<b>魔法活性:</b>攻撃力+2を獲得する。
#	"""
#	play = Play(CONTROLLER,SPELL).on(Buff(SELF, "SCH_231e"))##魔法の部分が未チェックOWN_SPELL_PLAY?
#	pass

#SCH_231e = buff(+2,0)#この書き方でよいか？

#class SCH_142:
#	""" 貪欲な読書家 
#	[x]自分のターンの終了時手札が3枚になるまでカードを引く。 """
#	events = OWN_TURN_END.on(DrawUntil(CONTROLLER,3))##チェックまだ
#	pass

#class SCH_428:
#	""" 伝承守護者ポルケルト 
#	[x]<b>雄叫び:</b>自分のデッキのカードをコストが高い順に並べ替える。 """
#	#これは無理
#	pass
