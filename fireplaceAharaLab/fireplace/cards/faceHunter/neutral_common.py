from ..utils import *

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
