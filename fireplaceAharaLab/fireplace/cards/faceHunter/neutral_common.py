from ..utils import *

class SCH_312:
	""" School Tour ツアーガイド
		&lt;b&gt;雄叫び:&lt;/b&gt;自分が次に使うヒーローパワーのコストは（0）
	"""
	play = Buff(FRIENDLY_HERO_POWER, "SCH_312e")

class SCH_312e:
	update = Refresh(FRIENDLY_HERO_POWER, {GameTag.COST: -2})
	events = OWN_TURN_END.on(Destroy(SELF))

class SCH_231:
	"""図太い徒弟
	[x]&lt;b&gt;魔法活性:&lt;/b&gt;攻撃力+2を獲得する。
	"""
	play = Play(CONTROLLER,SPELL).on(Buff(SELF, "SCH_617e"))##魔法の部分が未チェック
	pass

SCH_231e = buff(atk=+2)#この書き方でよいか？

class SCH_142:
	""" 貪欲な読書家 
	[x]自分のターンの終了時手札が3枚になるまでカードを引く。 """
	OWN_TURN_END.on(DrawUntil(CONTROLLER,3))##チェックまだ
	pass

class SCH_428:
	""" 伝承守護者ポルケルト 
	[x]&lt;b&gt;雄叫び:&lt;/b&gt;自分のデッキのカードをコストが高い順に並べ替える。 """
	#これは無理
	pass
